from django.contrib import admin

	


from customers.models import Company, Customer, Interaction
# admin.site.register(Company)

class InteractionAdminInline(admin.StackedInline):
	model = Interaction

class CustomerAdmin(admin.ModelAdmin):
	list_display = ['id','name','last_name','company']
	list_filter = ['company']
	list_editable = ['name','last_name','company']
	search_fields = ['name','last_name','company__name']
	inlines = [InteractionAdminInline]

class CompanyAdmin(admin.ModelAdmin):
	list_display = ['name']

class InteractionAdmin(admin.ModelAdmin):
	list_display = ['when','customer','kind','what']
	list_filter = ['customer','customer__company']

admin.site.register(Company, CompanyAdmin)		
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Interaction, InteractionAdmin)