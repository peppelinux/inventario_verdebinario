from django.contrib import admin

from .models import *


class ProduttoreAdmin(admin.ModelAdmin):
    #prepopulated_fields = {'slug': ('nome',)}
    list_display = ('nome_abbreviato', 'nome', 'url', 'admin_thumbnail')
    list_per_page = 100
    ordering = ('nome_abbreviato',)

    def save_model(self, request, obj, form, change):
        obj.inserito_da = request.user
        obj.seriale = obj.nome.strip()
        obj.seriale = obj.nome_abbreviato.strip()
        obj.save()


class SchedaTecnicaAdmin(admin.ModelAdmin):
    list_display = ('modello', 'produttore', 'paese_di_origine', 'anno', 'prezzo')
    list_per_page = 100

    def save_model(self, request, obj, form, change):
        obj.inserito_da = request.user
        obj.seriale = obj.seriale.strip()
        obj.save()


class FotoHardwareMuseoAdmin(admin.ModelAdmin):
    list_display = ('id_tabella', 'seriale', 'scheda_tecnica', 'admin_thumbnail')
    search_fields = ['seriale', 'scheda_tecnica']

admin.site.register(Produttore, ProduttoreAdmin)
admin.site.register(SchedaTecnica)
admin.site.register(FotoHardwareMuseo, FotoHardwareMuseoAdmin)

