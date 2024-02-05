from django.contrib import admin
from .models import Coin, Author, Post


# @admin.action(description="Стереть содержания статьи")
# def reset_content(modeladmin, request, queryset):
#     queryset.update(content='')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'birthday']
    ordering = ['name', 'birthday']
    list_filter = ['name', 'birthday']
    search_fields = ['name']
    search_help_text = 'Поиск по полю имя автора'

    readonly_fields = ['birthday']
    fieldsets = [
        (
            'Автор',
            {
                'classes': ['wide'],
                'fields': ['name', 'last_name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['birthday', 'bio'],
            },
        ),
        (
            'Дополнительная информация',
            {
                'description': 'Контактная информация',
                'fields': ['email'],
            }
        ),
    ]


class PostAdmin(admin.ModelAdmin):

    @admin.action(description="Стереть содержания статьи")
    def reset_content(modeladmin, request, queryset):
        queryset.update(content='')

    list_display = ['title', 'content', 'author', 'publish_date']
    ordering = ['title', 'author']
    list_filter = ['title', 'publish_date']
    search_fields = ['title']
    search_help_text = 'Поиск по полю заголовок'
    actions = [reset_content]

    readonly_fields = ['is_published', 'publish_date']
    fieldsets = [
        (
            'Пост',
            {
                'classes': ['wide'],
                'fields': ['title', 'content'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Автора',
                'fields': ['author'],
            },
        ),
        (
            'Дополнительная информация',
            {
                'description': 'Прочая информация',
                'fields': ['publish_date', 'is_published', 'views'],
            }
        ),
    ]


admin.site.register(Coin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
