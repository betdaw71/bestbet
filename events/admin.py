from django.contrib import admin
from .models import Event,Team,Sport,Match,Bet,Express,BetToExpress

# Register your models here.
class MatchEventInline(admin.TabularInline):
    model = Event
    extra = 1

class MatchAdmin(admin.ModelAdmin):
    inlines = [ MatchEventInline, ]

class ExpressBetInline(admin.TabularInline):
    model = BetToExpress
    extra = 1

class ExpessAdmin(admin.ModelAdmin):
    inlines = [ ExpressBetInline, ]
    
    

class EventAdmin(admin.ModelAdmin):
    list_display = ('match','title','name','coefficient','win')
    search_fields = ('title','name', )

    def save_model(self, request, obj, form, change):
        print('Saved')
        if change: 
            if 'win' in form.changed_data:
                for i in obj.bets.all():
                    print(i.user.balance)
                    print(i.sum,i.coefficient)
                    i.event.win = True
                    i.event.save()
                    i.user.balance += i.sum*i.coefficient
                    i.user.save()
                    print(i.user.balance)
            else:
                print('no win')
        else:
            print('no Changed')
        super().save_model(request, obj, form, change) 
        
class BetAdmin(admin.ModelAdmin):
    list_display = ('event','user','match','coefficient','sum','win')
    list_filter = ('event__match',)
    class Media:
        js = ("adminbet.js",)
    
admin.site.register(Bet,BetAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Team)
admin.site.register(Sport)
admin.site.register(Match,MatchAdmin)

admin.site.register(Express,ExpessAdmin)
admin.site.register(BetToExpress)
