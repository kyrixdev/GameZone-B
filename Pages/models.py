from django.db import models
from django.forms import ValidationError
from Products.models import Genre, Manufacturer, Product
# Create your models here.

class Hero(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="hero_image", blank=True, null=True)

class TopDeals(models.Model):
    banner = models.ImageField(upload_to='banners/')
    deal_1 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='top_deal_1')
    deal_2 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='top_deal_2')
    deal_3 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='top_deal_3')
    deal_4 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='top_deal_4')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['deal_1', 'deal_2', 'deal_3', 'deal_4'],
                name='unique_top_deals'
            )
        ]

    def clean(self):
        deals = [self.deal_1, self.deal_2, self.deal_3, self.deal_4]
        if len(set(deals)) < len(deals):
            raise ValidationError("Each deal must be unique")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Deal(models.Model):
    image = models.ImageField(upload_to='deal_pictures/')  # Assuming you store deal pictures as images
    description = models.TextField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_deals_set')  # Assuming you have a Product model defined



class CTA1(models.Model):
    image = models.ImageField(upload_to="banners/", blank=True, null=True)
    class Meta:
        verbose_name = "CTA1"

class PreOwnedDeals(models.Model):
    banner = models.ImageField(upload_to='banners/')
    deal_1 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='pre_owned_deal_1')
    deal_2 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='pre_owned_deal_2')


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['deal_1', 'deal_2'],
                name='unique_pre_owned_deals'
            )
        ]

    def clean(self):
        deals = [self.deal_1, self.deal_2]
        if len(set(deals)) < len(deals):
            raise ValidationError("Each deal must be unique")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)



class CTA2(models.Model):
    image = models.ImageField(upload_to="banners/", blank=True, null=True)
    class Meta:
        verbose_name = "CTA2"

class TopHardware(models.Model):
    products = models.ManyToManyField(Product, related_name='top_hardware')

class Brands(models.Model):
    image = models.ImageField(upload_to="brands/", blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.manufacturer.name} - {self.pk}"
    


class CTA3(models.Model):
    image = models.ImageField(upload_to="banners/", blank=True, null=True)
    class Meta:
        verbose_name = "CTA3"


class PlaystationDeals(models.Model):
    banner = models.ImageField(upload_to='banners/')
    deal_1 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='playstation_deal_1')
    deal_2 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='playstation_deal_2')


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['deal_1', 'deal_2'],
                name='unique_playstation_deals'
            )
        ]

    def clean(self):
        deals = [self.deal_1, self.deal_2]
        if len(set(deals)) < len(deals):
            raise ValidationError("Each deal must be unique")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class XboxDeals(models.Model):
    banner = models.ImageField(upload_to='banners/')
    deal_1 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='xbox_deal_1')
    deal_2 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='xbox_deal_2')


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['deal_1', 'deal_2'],
                name='unique_xbox_deals'
            )
        ]

    def clean(self):
        deals = [self.deal_1, self.deal_2]
        if len(set(deals)) < len(deals):
            raise ValidationError("Each deal must be unique")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class TopGames(models.Model):
    products = models.ManyToManyField(Product, related_name='top_games')

class FeaturedGames(models.Model):
    deal_1 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='featured_games_deal_1')
    deal_2 = models.ForeignKey('Deal', on_delete=models.SET_NULL, null=True, related_name='featured_games_deal_2')


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['deal_1', 'deal_2'],
                name='unique_featured_games_deals'
            )
        ]

    def clean(self):
        deals = [self.deal_1, self.deal_2]
        if len(set(deals)) < len(deals):
            raise ValidationError("Each deal must be unique")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class FeaturedGamesCTA(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="featured_games_cta__image", blank=True, null=True)


class FeaturedGenres(models.Model):
    genre_1 = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='featured_genres_genre_1')
    genre_2 = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='featured_genres_genre_2')


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['genre_1', 'genre_2'],
                name='unique_featured_genres'
            )
    ]

    def clean(self):
        genres = [self.genre_1, self.genre_2]
        if len(set(genres)) < len(genres):
            raise ValidationError("Each genre must be unique")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class TopAccessories(models.Model):
    products = models.ManyToManyField(Product, related_name='top_accessories')


class CTA4(models.Model):
    image = models.ImageField(upload_to="banners/", blank=True, null=True)
    class Meta:
        verbose_name = "CTA4"