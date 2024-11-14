from django.contrib import admin

from apps.features.models import Feature, FeatureValue


class FeatureValueInline(admin.TabularInline):
    model = FeatureValue

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    inlines = [FeatureValueInline]
