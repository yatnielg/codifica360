from django.contrib import admin
from .models import Country, State, Municipality
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'first_level', 'second_level')
    search_fields = ('nome',)
    list_filter = ('first_level', 'second_level')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('nome', 'country')
    search_fields = ('nome',)
    list_filter = ('country',)

@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('nome', 'state')
    search_fields = ('nome',)
    list_filter = ('state',)
# The admin interface for the Country, State, and Municipality models