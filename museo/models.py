from django.db import models
from photologue.models import ImageModel
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Produttore(ImageModel):
    id_tabella = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=135, blank=True)
    nome_abbreviato = models.CharField(max_length=135, blank=True)
    #slug = models.SlugField(unique=True, help_text=('"slug": un identificatore automatico e univoco'))
    descrizione = models.TextField(max_length=1024, blank=True)
    data_nascita = models.DateField(null=True, blank=True)
    data_chiusura = models.DateField(null=True, blank=True)
    #immagine_logo = models.ImageField(upload_to="LoghiProduttori", blank=True)
    url = models.CharField(max_length=256, blank=True)

    def save(self, *args, **kwargs):
        if self.nome_abbreviato == None or self.nome_abbreviato.split() == []:
            self.nome_abbreviato = self.nome.upper()
        super(self.__class__, self).save(*args, **kwargs) # Call the "real" save() method.

    class Meta:
        ordering = ['nome']
        db_table = 'produttore'
        verbose_name_plural = "Produttore"

    def get_absolute_url(self):
        return '%s' % (self.url)

    def __unicode__(self):
        return '%s' % (self.nome_abbreviato)


class SchedaTecnica(models.Model):
    id_tabella = models.AutoField(primary_key=True)
    modello = models.CharField(max_length=135, blank=True)
    produttore = models.ForeignKey(Produttore, null=True, blank=True, on_delete=models.SET_NULL)
    paese_di_origine = models.CharField(max_length=135, blank=True)
    anno = models.CharField(max_length=135, blank=True)
    tastiera = models.CharField(max_length=135, blank=True)
    cpu = models.CharField(max_length=135, blank=True)
    velocita = models.CharField(max_length=135, blank=True)
    memoria_volatile = models.CharField(max_length=135, blank=True)
    memoria_di_massa = models.CharField(max_length=135, blank=True)
    modalita_grafica = models.CharField(max_length=135, blank=True)
    audio = models.CharField(max_length=135, blank=True)
    dispositivi_media = models.CharField(max_length=135, blank=True)
    alimentazione = models.CharField(max_length=135, blank=True)
    prezzo = models.CharField(max_length=135, blank=True)
    descrizione = models.TextField(max_length=1024, blank=True)
    data_inserimento = models.DateField(null=True, blank=False, auto_now_add=True)

    class Meta:
        db_table = 'scheda_tecnica'
        verbose_name_plural = "Scheda Tecnica"


class FotoHardwareMuseo(ImageModel):
    id_tabella = models.AutoField(primary_key=True)
    #immagine = models.ImageField(upload_to="FotoHardwareMuseo/%d.%m.%Y", blank=True)
    etichetta_verde = models.CharField(max_length=135, blank=True)
    data_inserimento = models.DateField(null=True, blank=False, auto_now_add=True)
    seriale = models.CharField(max_length=384, blank=True)
    didascalia = models.TextField(max_length=328, blank=True)
    scheda_tecnica = models.ForeignKey(SchedaTecnica, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'foto_hardware_museo'
        verbose_name_plural = "Foto Hardware Museo"

    def __unicode__(self):
        return '%s %s' % (self.seriale, self.scheda_tecnica)

    def get_absolute_url(self):
        #return '/media/foto/FotoHardwareMuseo/' + self.data_inserimento.strftime('%d.%m.%Y') + '/' + self.image.name
        return '/media/%s' % self.image.name

    def admin_thumbnail(self):
        func = getattr(self, 'get_admin_thumbnail_url', None)
        if func is None:
            return _('An "admin_thumbnail" photo size has not been defined.')
        else:
            if hasattr(self, 'get_absolute_url'):
                return '<a class="foto_admin_thumbs" target="_blank" href="%s"><img src="%s"></a>' % \
                    (self.get_absolute_url(), func())
            else:
                return '<a class="foto_admin_thumbs" target="_blank"  href="%s"><img src="%s"></a>' % \
                    (self.image.url, func())
    admin_thumbnail.short_description = _('Thumbnail')
    admin_thumbnail.allow_tags = True
