from django.contrib import admin


from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    fieldsets =(
        ('Dados', {'fields': ('nome', 'email', 'matricula', 'senha')}),

    )


list_filter = ('nome', 'matricula')
list_display = ('nome', 'matricula')
search_fields = ('id', 'nome')







admin.site.register(Usuario,UsuarioAdmin)
