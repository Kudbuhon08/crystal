from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Banner Header"
    )
    image = models.ImageField(
        upload_to="image/",
        verbose_name="Banner photo"
    )
    logo = models.ImageField(
        upload_to="image/",
        verbose_name="Site logo"
    )
    facebook = models.URLField(
        verbose_name='facebook',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    linkedin = models.URLField(
        max_length=255,
        verbose_name='linkedin',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Site settings"
        
class Giv(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = " Giveaway for laptop (title)"
    )
    video = models.FileField(
        upload_to="image/",
        verbose_name=' Giveaway for laptop (video)',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = " Giveaway for laptop "
        
class Questions(models.Model):
    questions = models.CharField(
        max_length = 255,
        verbose_name = "questions"
    )    
    answers = models.TextField(
        verbose_name = "answers"
    )
    
    def __str__(self):
        return self.questions
    
    class Meta:
        verbose_name = "Questions and answers"\
            
class СonfigurationsImage(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name="photo (configurations)"
    )   
    
    class Meta:
        verbose_name = "Configurations (products) image" 
            
class Сonfigurations(models.Model):
    image = models.ForeignKey(
        СonfigurationsImage, on_delete=models.CASCADE,
        related_name="configurations_image"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "title (configurations)"
    )    
    descriptions = models.TextField(
        verbose_name = "descriptions (configurations)"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Configurations (products)"