from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from PBDApp.models import *

from PBDApp.serializers import *


class HeroVideoListView(generics.ListAPIView):
    serializer_class = HeroVideoSerializer
    permission_classes = [AllowAny]

    queryset = (
        HeroVideo.objects.filter(
            is_active=True
        )
    )
# =========================================
# PAGE LIST
# =========================================

class PageListView(generics.ListAPIView):

    serializer_class = PageSerializer
    permission_classes = [AllowAny]

    queryset = (
        Page.objects.filter(
            is_active=True
        )
        .prefetch_related(
            "sections__details"
        )
    )


# =========================================
# PAGE DETAIL
# =========================================

class PageDetailView(generics.RetrieveAPIView):

    serializer_class = PageSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    queryset = (
        Page.objects.filter(
            is_active=True
        )
        .prefetch_related(
            "sections__details"
        )
    )




class OurVisibilityListView(generics.ListAPIView):
    serializer_class = OurVisibilitySerializer
    permission_classes = [AllowAny]

    queryset = (
        OurVisibility.objects.filter(
            is_active=True
        )
        .order_by("-created_at")
    )

# =========================================
# WE OFFER LIST
# =========================================

class WeOfferView(generics.ListAPIView):
    serializer_class = WeOfferCategorySerializer
    permission_classes = [AllowAny]

    queryset = (
        WeOfferCategory.objects.filter(
            is_active=True
        )
        .order_by("-created_at")
    )

class WeOfferListView(generics.ListAPIView):

    serializer_class = WeOfferDetailSerializer
    permission_classes = [AllowAny]

    queryset = (
        WeOfferDetail.objects.filter(
            is_active=True
        )
        .order_by("-created_at")
    )


# =========================================
# PROJECT CATEGORY LIST
# =========================================

class ProjectCategoryListView(generics.ListAPIView):

    serializer_class = ProjectCategorySerializer
    permission_classes = [AllowAny]

    queryset = (
        ProjectCategory.objects.filter(
            is_active=True
        )
        .order_by("-created_at")
    )


# =========================================
# COMPLETED PROJECT LIST
# =========================================

class CompletedProjectListView(generics.ListAPIView):

    serializer_class = CompletedProjectSerializer
    permission_classes = [AllowAny]

    queryset = (
        CompletedProject.objects.filter(
            is_active=True
        )
        .select_related("category")
        .prefetch_related("images")
        .order_by("-created_at")
    )


# =========================================
# COMPLETED PROJECT DETAIL
# =========================================

class CompletedProjectDetailView(generics.RetrieveAPIView):

    serializer_class = CompletedProjectSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    queryset = (
        CompletedProject.objects.filter(
            is_active=True
        )
        .select_related("category")
        .prefetch_related("images")
    )


# =========================================
# PROJECTS BY CATEGORY
# =========================================

class ProjectsByCategoryView(generics.ListAPIView):

    serializer_class = CompletedProjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):

        category_slug = self.kwargs.get("slug")

        return (
            CompletedProject.objects.filter(
                is_active=True,
                category__slug=category_slug,
                category__is_active=True,
            )
            .select_related("category")
            .prefetch_related("images")
        )




class UpcomingProjectListView(generics.ListAPIView):

    serializer_class = UpcomingProjectsSerializer
    permission_classes = [AllowAny]
    queryset = UpcomingProjects.objects.filter(
            is_active=True
        )
        




class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
    queryset = Contact.objects.all()



class BannerImagesListView(generics.ListAPIView):
    serializer_class = BannerImagesSerializer
    permission_classes = [AllowAny]
    queryset = BannerImages.objects.filter(
            is_active=True
        )
        