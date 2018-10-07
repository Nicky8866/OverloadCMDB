#coding:utf-8
#@Author    :   Nicky

from django import forms

class CMDBUserForm(forms.Form):
    username = forms.CharField(max_length=32, label='用户账号', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'required': "",
            'minlength': 2,
            'maxlength': 32,
        }))
    password = forms.CharField(max_length=32, label='用户密码', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'required': "",
            'minlength': 6,
            'maxlength': 32,
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

def clean_phone(self):
    #获取前端提交的值
    phonedata = self.cleaned_data["phone"]
    if len(phonedata) < 11:
        raise forms.ValidationError("手机号不可以小于11位")
    else:
        return phonedata

def clean_photo(self):
    photodata = self.cleaned_data["photo"]
    if photodata.zise > 20480:
        raise forms.ValidationError("图片大小不能大于20KB")
    else:
        return photodata