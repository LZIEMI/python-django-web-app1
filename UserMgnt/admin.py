from django.contrib import admin

# Register your models here.

admin.site.site_header = 'edwiki.in'
admin.AdminSite.site_title = 'Edwiki Trainings'
admin.AdminSite.index_title = 'Welcome to the Edwiki Trainings'

# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# from main.models import MyUser
# from django import forms
#
# class MyUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = MyUser
#
#
# class MyUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = MyUser
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         try:
#             MyUser.objects.get(username=username)
#         except MyUser.DoesNotExist:
#             return username
#         raise forms.ValidationError(self.error_messages['duplicate_username'])
#
#
# class MyUserAdmin(UserAdmin):
#     form = MyUserChangeForm
#     add_form = MyUserCreationForm
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('extra_field1', 'extra_field2',)}),
#     )
#
# admin.site.register(MyUser, MyUserAdmin)

