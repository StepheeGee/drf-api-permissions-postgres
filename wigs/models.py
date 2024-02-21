from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

class Wig(models.Model):
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    
    # Original fields
    original_curl_pattern = models.CharField(max_length=16, choices=[('curly', 'Curly'), ('straight', 'Straight')])
    original_density = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(300)],
        help_text="Density of the wig in percentage",
        null=True,
        blank=True
    ) 
    original_hair_origin = models.CharField(max_length=16, choices=[('brazilian', 'Brazilian'), ('peruvian', 'Peruvian')])
    
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Customization fields
    custom_color = models.CharField(max_length=32, null=True, blank=True)
    custom_length = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    custom_curl_pattern = models.CharField(max_length=16, choices=[('curly', 'Curly'), ('straight', 'Straight')], null=True, blank=True)
    custom_density = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(300)],  # Adjusted max value to 300
        help_text="Density of the wig in percentage (0-300%)",
        null=True,
        blank=True
    ) 
    custom_hair_origin = models.CharField(max_length=16, choices=[('brazilian', 'Brazilian'), ('peruvian', 'Peruvian')], null=True, blank=True)
    
    # New field to indicate whether the wig is custom or in-stock
    is_custom = models.BooleanField(default=False)

    def apply_customization(self, customization_data):
        if not self.is_custom:
            # Can't customize an in-stock original wig
            return

        # Update model fields based on customization data
        self.custom_color = customization_data.get('color', self.color)
        self.custom_length = customization_data.get('length', self.length)
        self.custom_curl_pattern = customization_data.get('curl_pattern', self.original_curl_pattern)
        self.custom_density = customization_data.get('density', self.original_density)
        self.custom_hair_origin = customization_data.get('hair_origin', self.original_hair_origin)
        # Update more fields as needed

    def __str__(self):
        return self.name
