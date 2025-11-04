from django.contrib import admin
from .models import (
    ProductCategory,
    Product,
    ProductCategoryMember,
    GoodIdentification,
    ProductPrice,
)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "category_id",
        "category_name",
        "parent_category",
        "created_at",
        "updated_at",
    )
    search_fields = ("category_name",)
    list_filter = ("parent_category",)
    ordering = ("category_name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_id",
        "product_name",
        "product_type",
        "uom",
        "is_active",
        "created_by",
        "created_at",
        "updated_at",
    )
    search_fields = ("product_name", "internal_name", "product_type")
    list_filter = ("product_type", "uom", "is_active")
    ordering = ("product_name",)
    autocomplete_fields = ("created_by",)


@admin.register(ProductCategoryMember)
class ProductCategoryMemberAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "category",
        "from_date",
        "thru_date",
        "created_at",
        "updated_at",
    )
    search_fields = ("product__product_name", "category__category_name")
    list_filter = ("category",)
    ordering = ("product", "category")


@admin.register(GoodIdentification)
class GoodIdentificationAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "good_identification_type",
        "id_value",
        "from_date",
        "thru_date",
        "created_at",
        "updated_at",
    )
    search_fields = ("id_value", "product__product_name")
    list_filter = ("good_identification_type",)
    ordering = ("product", "good_identification_type")


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "price_type",
        "amount",
        "currency",
        "from_date",
        "thru_date",
        "created_at",
        "updated_at",
    )
    list_filter = ("price_type", "currency")
    search_fields = ("product__product_name",)
    ordering = ("product", "price_type")
