from django.contrib import admin
from django.contrib.sites.models import Site

from .models import *

class InventarioAdmin(admin.ModelAdmin):
    list_filter = ['tipologia','data_acquisizione', 'data_inserimento', 'produttore', 'condizioni', 'stato']
    list_display = ['modello', 'seriale', 'produttore', 'tipologia','data_acquisizione',
        'data_inserimento', 'etichetta_verde','get_barcode_url', 'get_google_search']
    search_fields = ['modello', 'seriale', 'etichetta_verde']
    list_per_page = 100
    #prepopulated_fields = {'seriale_slug': ('seriale',)}
    exclude = ('inserito_da',)

    def save_model(self, request, obj, form, change):
        obj.inserito_da = request.user
        # se manca salvare un serial standard nullo
        obj.seriale = obj.seriale.strip().upper()
        #obj.modello =  obj.modello.strip().upper()
        obj.save()

class DonatoreAdmin(admin.ModelAdmin):
    #list_filter = ['tipologia','data_acquisizione', 'data_inserimento', 'produttore']
    #list_display = ['modello', 'seriale', 'produttore', 'tipologia','data_acquisizione', 'data_inserimento']
    search_fields = ['nominativo', 'email', 'tel']
    list_per_page = 33
    ordering = ('nominativo',)

class TipologiaHardwareAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'descrizione']
    list_display = search_fields
    list_per_page = 33
    def save_model(self, request, obj, form, change):
        obj.nome =  obj.nome.strip().upper()
        obj.save()
    ordering = ('nome',)

admin.site.register(Donatore, DonatoreAdmin)
admin.site.register(TipologiaHardware, TipologiaHardwareAdmin)
admin.site.register(Inventario, InventarioAdmin)

