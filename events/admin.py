from django.contrib import admin
from .models import Event,Team,Sport,Match,Bet

# Register your models here.
class MatchEventInline(admin.TabularInline):
    model = Event
    extra = 1

class MatchAdmin(admin.ModelAdmin):
    inlines = [ MatchEventInline, ]


admin.site.register(Bet)
admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Sport)
admin.site.register(Match,MatchAdmin)
