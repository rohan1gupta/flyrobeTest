from django.contrib import admin
from models import Product, ProductCategory, ProductOccasion


class ProductAdmin(admin.ModelAdmin):
    """
    Description:
        admin for defining mapping between master channel
        and flow
    """
    # list_filter = ['active', "master_channel", "po_required"]
    # list_display = [
    #     "flow", "master_channel", "active",
    #     "po_required", "po_generated_by",
    #     "skip_accept_reject", "po_series_by"]
    search_fields = ["name"]
    model = Product
    # list_select_related = ('flow', 'master_channel', )
    # verbose_name_plural = (
    #     "Master Channel Flow RelationShip")


admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductCategory, ProductCategoryAdmin)
# admin.site.register(ProductOccasion, ProductOccasionAdmin)
