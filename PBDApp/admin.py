from PBDApp.models import WeOfferDetail
from django.contrib import admin
from PBDApp.models import *

@admin.register(HeroVideo)
class HeroVideoAdmin(admin.ModelAdmin):
    list_display = (
        "video",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "video",
    )

    list_editable = ("is_active",)


# =========================
# INLINES
# =========================

class SectionDetailInline(admin.TabularInline):
    model = SectionDetail
    extra = 1
    fields = (
        "heading",
        "sub_heading",
        "description",
        "image",
        "is_active",
    )


class CompletedProjectImagesInline(admin.TabularInline):
    model = CompletedProjectImages
    extra = 1
    fields = (
        "image",
        "is_primary",
    )


# =========================
# PAGE ADMIN
# =========================

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }


    list_editable = ("is_active",)


# =========================
# SECTION ADMIN
# =========================

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "page",
        "type",
        "is_active",
        "created_at",
    )

    list_filter = (
        "type",
        "page",
        "is_active",
    )

    search_fields = (
        "page__title",
        "type",
    )

    

    list_editable = ("is_active",)

    inlines = [SectionDetailInline]


# =========================
# SECTION DETAIL ADMIN
# =========================

@admin.register(SectionDetail)
class SectionDetailAdmin(admin.ModelAdmin):
    list_display = (
        "heading",
        "section",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "section",
    )

    search_fields = (
        "heading",
        "sub_heading",
        "description",
    )

    

    list_editable = ("is_active",)



@admin.register(OurVisibility)
class OurVisibilityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
    )

    

    list_editable = ("is_active",)


# =========================
# WE OFFER ADMIN
# =========================


@admin.register(WeOfferCategory)
class WeOfferCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    

    list_editable = ("is_active",)


@admin.register(WeOfferDetail)
class WeOfferAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "description",
    )

    

    list_editable = ("is_active",)


# =========================
# PROJECT CATEGORY ADMIN
# =========================

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    

    list_editable = ("is_active",)


# =========================
# COMPLETED PROJECT ADMIN
# =========================

@admin.register(CompletedProject)
class CompletedProjectAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "category__name",
    )

    

    list_editable = ("is_active",)

    inlines = [CompletedProjectImagesInline]


# =========================
# COMPLETED PROJECT IMAGES
# =========================

@admin.register(CompletedProjectImages)
class CompletedProjectImagesAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "is_primary",
        "created_at",
    )

    list_filter = (
        "is_primary",
    )

    search_fields = (
        "project__category__name",
    )

    

    list_editable = ("is_primary",)



class UpcomingProjectOverviewInline(admin.StackedInline):
    model = UpcomingProjectOverview
    extra = 1

    fields = (
        "title",
        "description",
        "points",
        "is_active",
    )


class UpcomingProjectImageInline(admin.TabularInline):
    model = UpcomingProjectImage
    extra = 1

    fields = (
        "image",
        "is_active",
    )


class UpcomingProjectStructureInline(admin.StackedInline):
    model = UpcomingProjectStructure
    extra = 1

    fields = (
        "title",
        "image",
        "description",
        "is_active",
    )


class UpcomingProjectSpecificationsInline(admin.StackedInline):
    model = UpcomingProjectSpecifications
    extra = 1

    fields = (
        "amenities",
        "specifications",
        "is_active",
    )


class UpcomingProjectSpecificationImagesInline(admin.TabularInline):
    model = UpcomingProjectSpecificationImages
    extra = 1

    fields = (
        "image",
        "is_active",
    )


# =====================================================
# MAIN PROJECT ADMIN
# =====================================================

@admin.register(UpcomingProjects)
class UpcomingProjectsAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "location",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "title",
        "location",
    )

    readonly_fields = (
        "created_at",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    list_editable = (
        "is_active",
    )

    ordering = ("-created_at",)

    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "title",
                    "location",
                    "image",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "is_active",
                    "created_at",
                )
            },
        ),
    )

    inlines = [
        UpcomingProjectOverviewInline,
        UpcomingProjectImageInline,
        UpcomingProjectStructureInline,
        UpcomingProjectSpecificationsInline,
        UpcomingProjectSpecificationImagesInline,
    ]


# =====================================================
# OVERVIEW ADMIN
# =====================================================

@admin.register(UpcomingProjectOverview)
class UpcomingProjectOverviewAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "title",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "project__name",
        "title",
    )

    list_editable = (
        "is_active",
    )


# =====================================================
# PROJECT IMAGE ADMIN
# =====================================================

@admin.register(UpcomingProjectImage)
class UpcomingProjectImageAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "project__name",
    )

    list_editable = (
        "is_active",
    )


# =====================================================
# STRUCTURE ADMIN
# =====================================================

@admin.register(UpcomingProjectStructure)
class UpcomingProjectStructureAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "title",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "project__name",
        "title",
    )

    list_editable = (
        "is_active",
    )


# =====================================================
# SPECIFICATION ADMIN
# =====================================================

@admin.register(UpcomingProjectSpecifications)
class UpcomingProjectSpecificationsAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "project__name",
    )

    list_editable = (
        "is_active",
    )


# =====================================================
# SPECIFICATION IMAGE ADMIN
# =====================================================

@admin.register(UpcomingProjectSpecificationImages)
class UpcomingProjectSpecificationImagesAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "project__name",
    )

    list_editable = (
        "is_active",
    )



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=(
        "name",
        "email",
        "phone",
        "created_at",
    )

    list_filter=(
        "created_at",
    )

    search_fields=(
        "name",
        "email",
        "phone",
    )



@admin.register(BannerImages)
class BannerImagesAdmin(admin.ModelAdmin):
    list_display=(
        "section",
        "image",
        "is_active",
        "created_at",
    )

    list_filter=(
        "section",
        "is_active",
    )

    search_fields=(
        "section",
    )

    list_editable=(
        "is_active",
    )
