#coding:utf-8
#@Author    :   Nicky

from django import forms

class CMDBUserForm(forms.Form):
    username = forms.CharField(max_length=32, label='用户账号', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'required': "",
            'minlength': 2,
            'maxlength': 10,
        }))
    password = forms.CharField(max_length=32, label='用户密码', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'required': "",
            'minlength': 2,
            'maxlength': 10,
        }))
    nickname = forms.CharField(max_length=32, label='用户姓名', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }))
    phone = forms.IntegerField(label='用户手机', widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'required': "",
        }))
    email = forms.EmailField(label='用户邮箱', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'required': "",
        }))
    photo = forms.ImageField(label='用户头像')
