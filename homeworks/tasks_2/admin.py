from django.contrib import admin
from .models import User, Product, Order


class UserAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['email']
    list_filter = ['registration_date']
    search_fields = ['name']
    search_help_text = 'Поиск по полю имя user'

    readonly_fields = ['phone']
    fieldsets = [
        (
            'Автор',
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['address', 'phone', 'email'],
            },
        ),

    ]


class ProductAdmin(admin.ModelAdmin):

    # @admin.action(description="Стереть содержания статьи")
    # def reset_content(modeladmin, request, queryset):
    #     queryset.update(content='')

    list_display = ['title', 'price', 'quantity']
    ordering = ['title']
    list_filter = ['title', 'description']
    search_fields = ['title']
    search_help_text = 'Поиск по полю заголовок'
    # actions = [reset_content]

    fieldsets = [
        (
            'Продукт',
            {
                'classes': ['wide'],
                'fields': ['title', 'price'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробности',
                'fields': ['description'],
            },
        ),
        (
            'Дополнительная информация',
            {
                'description': 'Прочая информация',
                'fields': ['quantity'],
            }
        ),
    ]


admin.site.register(Order)
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
