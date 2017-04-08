from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from . import models
from . import forms 



class home(View):
    form_class = forms.UserForm
    template_name = 'index.html'
    
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            #cleaned normalized data
            username = form.cleaned_data['username']
            Password = form.cleaned_data['Password']
            user.set_password(Password)
            form.save()

            user = authenticate(username=username,Password=Password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('main:index')
        return render(request,self.template_name,{'form':form})

def login(request):
    if request.POST:
        username = request.POST.get('username')
        Password = request.POST.get('Password')

        user = authenticate(username=username,Password=Password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('main:index')
        else:
            return redirect('/404')