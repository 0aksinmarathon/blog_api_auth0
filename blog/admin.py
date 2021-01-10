from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from blog.modules.user.models import User
from blog.modules.article.models import Article
from blog.modules.comment.models import Comment
from django.contrib.auth.admin import UserAdmin


class BlogUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class BlogUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'password')


class BlogUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

    form = BlogUserChangeForm
    add_form = BlogUserCreationForm
    list_display = ('email', 'name', 'is_superuser', 'is_admin', 'is_staff')
    list_filter = ('email', 'name', 'is_superuser',)
    search_fields = ('email', 'name')

    ordering = ('email',)


admin.site.register(User, BlogUserAdmin)
admin.site.register(Article)
admin.site.register(Comment)
