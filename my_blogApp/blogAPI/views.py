from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializers,EachBlogSerializer
from .models import Blog, Category, SubCategory
from django.db.models import Q
from django.http import Http404 
import random2
from collections import namedtuple
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib import auth


class BlogList(APIView):
    def get(self, request):
        blogs = Blog.objects.order_by('-created_at').filter(Q(status__icontains='Publish'))
        serializer = BlogSerializers(blogs, many=True)
        return Response(serializer.data)


class BlogDetail(APIView):
    re_blogs = []    
    def is_premium(self, request, blog):
        print(request.user.is_authenticated)
        if (blog.premium and request.user.is_authenticated) or (blog.premium == False and request.user.is_authenticated == False) or (blog.premium == False and request.user.is_authenticated):
            return True
        else:
            return False

    def get_object(self, slug):
        try:
            blog = Blog.objects.get(slug=slug)
            return blog
        except Blog.DoesNotExist:
            raise Http404
    
    def get(self, request, slug):        
        
        blog = self.get_object(slug=slug)
        if self.is_premium(request, blog):
            pass
        else:
            return Response({'detail': 'User must have to logged in'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            related_blogs = []        
            blog = self.get_object(slug=slug)
            categories = blog.category.all()
            subcategories = blog.subcategory.all() 
            
            x = self.Related_Blogs(slug, categories, subcategories)
        
            if len(x) > 3:                
                for i in x[:3]:
                    related_blogs.append(i)
            else:
                for i in x:
                    related_blogs.append(i)

            each_blog = namedtuple('each_blog', ('blog', 'related_blogs'))
            each_blog = each_blog(
                blog=blog,
                related_blogs=related_blogs,
            )
            serializer = EachBlogSerializer(each_blog)
            return Response(serializer.data)
        except:
            return Response(serializer.errors)

    def Related_Blogs(self, slug, categories, subcategories):
        self.re_blogs = []
        if self.subcategories_(slug, subcategories):
            return self.re_blogs

        elif self.categories_(slug, categories):
            return self.re_blogs
        else:
            return self.re_blogs

    def subcategories_(self, slug, subcategories):
        temp = []
        for subcategory in subcategories:
            x = Blog.objects.filter(Q(subcategory=subcategory) & Q(status__icontains='Publish') & ~Q(slug=slug))
            for i in x:
                if i not in temp:
                    temp.append(i)


        while len(self.re_blogs) != len(temp):
            p = random2.choice(temp)
            if p not in self.re_blogs:
                self.re_blogs.append(p)

        temp = []
        if len(self.re_blogs) >= 3:  
            return True
        else:
            return False

    def categories_(self, slug, categories):
        sub_categories = []
        for category in categories:
            x = SubCategory.objects.filter(Q(category=category))
            for i in x:
                if i not in sub_categories: 
                    sub_categories.append(i)
        if self.subcategories_(slug, sub_categories):
            return True
        else: 
            return False


