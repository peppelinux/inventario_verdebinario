from django.db import models
from museo.models import Produttore
from django.contrib.auth.models import User

from os import chdir, mkdir


class Donatore(models.Model):
    id_tabella = models.AutoField(primary_key=True)
    nominativo = models.TextField(max_length=512, blank=True)
    tel = models.CharField(max_length=135, blank=True)
    email = models.CharField(max_length=512, blank=True)
    note = models.TextField(max_length=512, blank=True)

    class Meta:
        db_table = 'donatore'
        verbose_name_plural = "Donatore"
        ordering = ['nominativo']

    def __unicode__(self):
        return '%s' % (self.nominativo)


class TipologiaHardware(models.Model):
    id_tabella = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=135, blank=True)
    descrizione = models.TextField(max_length=512, blank=True)

    class Meta:
        db_table = 'tipologia_hardware'
        verbose_name_plural = "Tipologia Hardware"
        ordering = ['nome']

    def __unicode__(self):
        return '%s' % self.nome


class Inventario(models.Model):
    CONDIZIONI = (
    ('funzionante', 'funzionante'),
    ('non funzionante', 'non funzionante'),
    ('da testare', 'da testare')
    )
    STATO = (
    ('in sede', 'in sede'),
    ('distrutto', 'distrutto'),
    ('donato', 'donato'),
    ('fuori sede', 'fuori sede'),
    ('in prestito', 'in prestito'),
    ('rubato', 'rubato'),

    )
    id_tabella = models.AutoField(primary_key=True)
    modello = models.CharField(max_length=135, blank=True)
    seriale = models.CharField(unique=True, max_length=254, blank=True)
    #seriale_slug = models.SlugField(max_length=254, blank=True)
    data_inserimento = models.DateField(null=True, blank=False, auto_now_add=True)
    donatore = models.ForeignKey(Donatore, null=True, blank=True, on_delete=models.SET_NULL)
    numero_donazione = models.CharField(max_length=135, blank=True)
    produttore = models.ForeignKey(Produttore, null=True, blank=True, on_delete=models.SET_NULL)
    tipologia = models.ForeignKey(TipologiaHardware, null=True, blank=True, on_delete=models.SET_NULL)
    data_acquisizione = models.DateField(null=True, blank=True)
    etichetta_verde = models.CharField(max_length=135, blank=True, null=True, unique=True)
    ubicazione = models.CharField(max_length=135, blank=True)
    condizioni = models.CharField(choices=CONDIZIONI, blank=True, default='funzionante', max_length=135,)
    stato = models.CharField(choices=STATO, blank=True, default='in sede', max_length=135,)
    inserito_da = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    note = models.TextField(max_length=512, blank=True)

    class Meta:
        db_table = 'inventario'
        verbose_name_plural = "Gestione Inventario"

    def __unicode__(self):
        return '%s - SN: %s' % (self.modello, self.seriale)

    def do_barcode(self):
        pass
    '''
        try:
            donatore = self.donatore.nominativo
        except:
            donatore = 'non registrato'
        msg = """
        Modello: %s
        Produttore: %s
        Tipo: %s
        SN: %s
        Stato: %s
        Donatore: %s
        """ % (str(self.modello), str(self.produttore), str(self.tipologia), str(self.seriale),
str(self.stato), str(self.donatore))

        try:
            chdir(BARCODE_PATH)
        except:
            mkdir(BARCODE_PATH); chdir(BARCODE_PATH)

        b = barcode('qrcode', msg[:174], options=dict(version=9, eclevel='M'), margin=10,
data_mode='8bits')
        b.save(str(self.id_tabella)+BARCODE_EXTENSION)
    '''

    def get_barcode_url(self):
        pass
    '''
        img_url_path = BARCODE_URL+ SEP + str(self.pk)+ BARCODE_EXTENSION
        return u'<a target="_blank" href="%s"><img width=53 src="%s"></a>' % (img_url_path, img_url_path)
    get_barcode_url.allow_tags = True
    get_barcode_url.short_description = 'QRCode'

    def save(self, *args, **kwargs):
        super(Inventario, self).save(*args, **kwargs)
        try:
            self.do_barcode()
        except:
            pass
        if not self.etichetta_verde:
            try:
                self.etichetta_verde = 'vb %d' % self.pk
            except:
                pass
        if not self.seriale or self.seriale == '':
            self.seriale = None
        if not self.stato:
            self.stato = self.STATO[0][0]
        super(Inventario, self).save(*args, **kwargs)
    '''

    def get_google_search(self):
        return '<a target="_blank" href="http://www.google.it/search?q=%s+%s"> <img width=53 src="/media/images/search.png" /> </a>' % ('+'.join(self.produttore.__str__().split(' ')), '+'.join(self.modello.split(' ') ) )
    get_google_search.allow_tags = True
    get_google_search.short_description = 'google'

