from django.urls import path

from PBDApp.views import *


urlpatterns = [

    # Hero Video
    path(
        "hero-video/",
        HeroVideoListView.as_view(),
        name="hero-video-list"
    ),

    # Pages
    path(
        "pages/",
        PageListView.as_view(),
        name="page-list"
    ),

    path(
        "pages/<slug:slug>/",
        PageDetailView.as_view(),
        name="page-detail"
    ),

    # Our Visibility
    path(
        "our-visibility/",
        OurVisibilityListView.as_view(),
        name="our-visibility-list"
    ),

    # We Offer
    path(
        "we-offer/",
        WeOfferListView.as_view(),
        name="we-offer-list"
    ),
    path(
        "we-offer-category/",
        WeOfferView.as_view(),
        name="we-offer-category"
    ),

    # Categories
    path(
        "project-categories/",
        ProjectCategoryListView.as_view(),
        name="project-category-list"
    ),

    # Projects
    path(
        "projects/",
        CompletedProjectListView.as_view(),
        name="project-list"
    ),

    path(
        "projects/<slug:slug>/",
        CompletedProjectDetailView.as_view(),
        name="project-detail"
    ),

    path(
        "projects/category/<slug:slug>/",
        ProjectsByCategoryView.as_view(),
        name="projects-by-category"
    ),

    path(
        "upcoming-projects/",
        UpcomingProjectListView.as_view(),
        name="upcoming-project-list"
    ),


    path(
        "contact/",
        ContactCreateView.as_view(),
        name="contact-create"
    ),

    path(
        "banner-images/",
        BannerImagesListView.as_view(),
        name="banner-images-list"
    ),
]