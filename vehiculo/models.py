from django.db import models
from django.conf import settings

# Create your models here.

class VehiculoModel(models.Model):

    opMarca  = (
        ('Chevrolet', 'Chevrolet'),
        ('Fiat','Fiat'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )

    opCategoria = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )

    marca = models.CharField(max_length=20, choices=opMarca)
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=opCategoria)
    precio = models.IntegerField()
    clasificacion = models.CharField(max_length=20, blank=True)
    imagen = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "vehículo"
        verbose_name_plural = "vehículos"
        ordering = ["-fecha_creacion"]
        permissions = (
            ("visualizar_catalogo", "Visualizar Catálogo"),
        )

    def save(self, *args, **kwargs):
        if self.precio <= 10000:
            self.clasificacion = 'Bajo'
        elif self.precio <= 30000:
            self.clasificacion = 'Medio'
        else:
            self.clasificacion = 'Alto'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.marca
    

class ColorModel(models.Model):

    colorChoice  = (
        ('Azul', 'Azul'),
        ('Morado','Morado'),
        ('Verde', 'Verde'),
        ('AzulD', 'AzulD'),
        ('MoradoD','MoradoD'),
        ('VerdeD', 'VerdeD'),
    )

    color = models.CharField(max_length=20, choices=colorChoice, default='Azul')
    color1 = models.CharField(max_length=30, default='#F3F3F5')
    color2 = models.CharField(max_length=30, default='#1D5B79')
    color3 = models.CharField(max_length=30, default='#3093C5')
    color4 = models.CharField(max_length=30, default='#f5f5f5')
    color5 = models.CharField(max_length=30, default='#202020')
    color6 = models.CharField(max_length=30, default='#20202020')
  
    class Meta:
        verbose_name = "color"
        verbose_name_plural = "colores"
        ordering = ["-color"]

    def save(self, *args, **kwargs):
        if self.color == 'Azul':
            self.color1 = '#F3F3F5'
            self.color2 = '#1D5B79'
            self.color3 = '#3093C5'
            self.color4 = '#f5f5f5'
            self.color5 = '#202020'
            self.color6 = '#20202010'
        elif self.color == 'Morado':
            self.color1 = '#F5F3F5'
            self.color2 = '#534077'
            self.color3 = '#7A60A9'
            self.color4 = '#f5f5f5'
            self.color5 = '#202020'
            self.color6 = '#20202010'
        elif self.color == 'Verde':
            self.color1 = '#F3F5F3'
            self.color2 = '#569C30'
            self.color3 = '#7DCA53'
            self.color4 = '#f5f5f5'
            self.color5 = '#202020'
            self.color6 = '#20202010'
        elif self.color == 'AzulD':
            self.color1 = '#111112'
            self.color2 = '#287BA4'
            self.color3 = '#3A9DCF'
            self.color4 = '#202020'
            self.color5 = '#f5f5f5'
            self.color6 = '#f5f5f510'
        elif self.color == 'MoradoD':
            self.color1 = '#121112'
            self.color2 = '#6F569F'
            self.color3 = '#856DB0'
            self.color4 = '#202020'
            self.color5 = '#f5f5f5'
            self.color6 = '#f5f5f510'
        else:
            self.color1 = '#111211'
            self.color2 = '#5EAC35'
            self.color3 = '#7DCA53'
            self.color4 = '#202020'
            self.color5 = '#f5f5f5'
            self.color6 = '#f5f5f510'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.color