from django.contrib import admin

from .models import Blue


class BlueAdmin(admin.ModelAdmin):
    # Here we can provide the database that we want to use
    using = 'blue_db'

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def save_model(self, request, obj, form, change):
        # and providing database name while performing the actions on database
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)


admin.site.register(Blue, BlueAdmin)
