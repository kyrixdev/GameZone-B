from django.db import models
from Users.models import CustomUser

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category_image', null=True, blank=True)
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    parent_subcategory = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        if self.parent_subcategory:
            return str(self.id) + "-" + f"{self.get_full_path()}"
        return str(self.id) + "-" + self.name

    def get_full_path(self):
        """
        Returns the full path of the subcategory including all parent subcategories.
        """
        path_list = [self.name]
        parent = self.parent_subcategory
        while parent is not None:
            path_list.append(parent.name)
            parent = parent.parent_subcategory
        path_list.reverse()  # Reverse the list
        return ' / '.join(path_list)

class Genre(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='genre_image', null=True, blank=True)
    def __str__(self):
        return self.name

class ProductColor(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="product_colors_images/", blank=True, null=True)

    def __str__(self):
        return self.name

class ProductSize(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    subcategories = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    colors = models.ManyToManyField(ProductColor)
    sizes = models.ManyToManyField(ProductSize)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    availability = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre, blank=True)
    related_products = models.ManyToManyField('self', blank=True)
    subImages = models.ManyToManyField('SubImage', blank=True)
    discount_percentage = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='product_image', null=True, blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField(default=5)
    comment = models.TextField()
    
    def __str__(self):
        return f"Review by {self.user.user.username} for {self.product.title}"

class SubImage(models.Model):
    image_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="subimage_set", null=True, blank=True)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"Image for {self.image_product}"