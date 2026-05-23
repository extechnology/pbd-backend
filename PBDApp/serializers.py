from rest_framework import serializers
from PBDApp.models import *


class HeroVideoSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = HeroVideo
        fields = [
            "id",
            "video",
            "is_active",
        ]

    def get_video(self, obj):
        request = self.context.get("request")

        if obj.video:
            return request.build_absolute_uri(obj.video.url)

        return None


# ======================================
# SECTION DETAIL
# ======================================

class SectionDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = SectionDetail
        fields = [
            "id",
            "heading",
            "sub_heading",
            "description",
            "image",
            "is_active",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(obj.image.url)

        return None


# ======================================
# SECTION
# ======================================

class SectionSerializer(serializers.ModelSerializer):

    details = SectionDetailSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Section
        fields = [
            "id",
            "type",
            "is_active",
            "details",
        ]


# ======================================
# PAGE
# ======================================

class PageSerializer(serializers.ModelSerializer):

    sections = SectionSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Page
        fields = [
            "id",
            "title",
            "slug",
            "is_active",
            "sections",
        ]


# ======================================
# WE OFFER
# ======================================

class WeOfferCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeOfferCategory
        fields = [
            "id",
            "title",
            "image",
            "description",
            "is_active",
        ]


class WeOfferDetailSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    category = WeOfferCategorySerializer(
        read_only=True
    )

    class Meta:
        model = WeOfferDetail
        fields = [
            "id",
            "description",
            "image",
            "category",
            "points",
            "assurance",
            "is_active",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(obj.image.url)

        return None



class OurVisibilitySerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = OurVisibility
        fields = [
            "id",
            "image",
            "title",
            "is_active",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(obj.image.url)

        return None


# ======================================
# PROJECT IMAGES
# ======================================

class CompletedProjectImagesSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = CompletedProjectImages
        fields = [
            "id",
            "image",
            "is_primary",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(obj.image.url)

        return None


# ======================================
# PROJECT CATEGORY
# ======================================

class ProjectCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectCategory
        fields = [
            "id",
            "name",
            "slug",
        ]


# ======================================
# COMPLETED PROJECT
# ======================================

class CompletedProjectSerializer(serializers.ModelSerializer):

    category = ProjectCategorySerializer(
        read_only=True
    )

    images = CompletedProjectImagesSerializer(
        many=True,
        read_only=True
    )

    primary_image = serializers.SerializerMethodField()

    class Meta:
        model = CompletedProject
        fields = [
            "id",
            "category",
            "primary_image",
            "images",
            "is_active",
            "created_at",
        ]

    def get_primary_image(self, obj):

        request = self.context.get("request")

        primary = obj.images.filter(
            is_primary=True
        ).first()

        if primary and primary.image:
            return request.build_absolute_uri(
                primary.image.url
            )

        first_image = obj.images.first()

        if first_image and first_image.image:
            return request.build_absolute_uri(
                first_image.image.url
            )

        return None



class UpcomingProjectOverviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpcomingProjectOverview
        fields = [
            "id",
            "title",
            "description",
            "points",
            "is_active",
        ]

class UpcomingProjectImageSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = UpcomingProjectImage
        fields = [
            "id",
            "image",
            "is_active",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(obj.image.url)

        return None


class UpcomingProjectStructureSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = UpcomingProjectStructure
        fields = [
            "id",
            "title",
            "image",
            "description",
            "is_active",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(obj.image.url)

        return None


class UpcomingProjectSpecificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpcomingProjectSpecifications
        fields = [
            "id",
            "amenities",
            "specifications",
            "is_active",
        ]


class UpcomingProjectSpecificationImagesSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = UpcomingProjectSpecificationImages
        fields = [
            "id",
            "image",
            "is_active",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(obj.image.url)

        return None



class UpcomingProjectsSerializer(serializers.ModelSerializer):

    overview = UpcomingProjectOverviewSerializer(
        many=True,
        read_only=True
    )

    images = UpcomingProjectImageSerializer(
        many=True,
        read_only=True
    )

    structure = UpcomingProjectStructureSerializer(
        many=True,
        read_only=True
    )


    specifications = UpcomingProjectSpecificationsSerializer(
        many=True,
        read_only=True
    )

    specification_images = UpcomingProjectSpecificationImagesSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = UpcomingProjects
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "message",
            "created_at",
        ]



class BannerImagesSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = BannerImages
        fields = [
            "id",
            "image",
            "section",
            "is_active",
            "created_at",
        ]

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            return request.build_absolute_uri(obj.image.url)

        return None