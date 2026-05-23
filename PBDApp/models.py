from django.db import models
from django.utils.text import slugify

# Create your models here.


class HeroVideo(models.Model):
    video = models.FileField(upload_to='hero_video/')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.video.name


from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Section(models.Model):

    SECTION_TYPES = [
        ("commitment", "Commitment"),
        ("goal", "Goal"),
        ("prime-services", "Prime Services"),
        ("about-us", "About Us"),
        ("journey", "Journey"),
        ("growth-section", "Growth Section"),
        ("highlights", "Highlights"),
    ]

    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name="sections"
    )


    type = models.CharField(
        max_length=50,
        choices=SECTION_TYPES
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page.title


class SectionDetail(models.Model):

    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="details"
    )

    heading = models.CharField(max_length=255,blank=True,null=True)

    sub_heading = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="section/",
        blank=True,
        null=True
    )

    description = models.TextField(blank=True,null=True)


    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class WeOfferCategory(models.Model):
    title= models.CharField(max_length=255)
    image= models.ImageField(upload_to='we_offer_category/',blank=True,null=True)
    description= models.TextField(blank=True,null=True)
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class WeOfferDetail(models.Model):
    category=models.ForeignKey(WeOfferCategory,on_delete=models.CASCADE,related_name="we_offers")
    description= models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='we_offer/',blank=True,null=True)
    points=models.TextField(blank=True,null=True)
    assurance=models.TextField(blank=True,null=True)
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category.title




class ProjectCategory(models.Model):
    name = models.CharField(max_length=255)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Project Categories"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CompletedProject(models.Model):


    category = models.ForeignKey(
        ProjectCategory,
        on_delete=models.CASCADE,
        related_name="completed_projects"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.category.name


class CompletedProjectImages(models.Model):

    project = models.ForeignKey(
        CompletedProject,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="projects/gallery/"
    )

    is_primary=models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.project.category.name} Image"
    


class UpcomingProjects(models.Model):
    name = models.CharField(max_length=255)

    slug = models.SlugField(
        unique=True,
        blank=True
    )
    title = models.CharField(max_length=255,blank=True,null=True)

    image = models.ImageField(
        upload_to="upcoming_projects/",
        blank=True,
        null=True
    )
    location = models.CharField(max_length=255,blank=True,null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class UpcomingProjectOverview(models.Model):
    project = models.ForeignKey(
        UpcomingProjects,
        on_delete=models.CASCADE,
        related_name="overview"
    )
    title=models.CharField(max_length=255)
    description=models.TextField()
    points=models.TextField()
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name

class UpcomingProjectImage(models.Model):
    project = models.ForeignKey(
        UpcomingProjects,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image=models.ImageField(upload_to='upcoming_projects_images/')
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name


class UpcomingProjectStructure(models.Model):
    project = models.ForeignKey(
        UpcomingProjects,
        on_delete=models.CASCADE,
        related_name="structure"
    )
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='upcoming_projects_structure/')
    description=models.TextField()
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name


class UpcomingProjectSpecifications(models.Model):
    project = models.ForeignKey(
        UpcomingProjects,
        on_delete=models.CASCADE,
        related_name="specifications"
    )
    amenities = models.TextField()
    specifications=models.TextField()
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name



class UpcomingProjectSpecificationImages(models.Model):
    project = models.ForeignKey(
        UpcomingProjects,
        on_delete=models.CASCADE,
        related_name="specification_images"
    )
    image=models.ImageField(upload_to='upcoming_projects_specification_images/')
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name


class OurVisibility(models.Model):
    image=models.ImageField(upload_to='our_visibility/')
    title=models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


SECTION_TYPES=(
    ("home","Home"),
    ("journey","Journey"),
    ("offer","Offer"),
    ("projects","Projects"),
    ("upcoming","Upcoming"),
    ("services","Services"),
)

class BannerImages(models.Model):
    section=models.CharField(max_length=50,choices=SECTION_TYPES)
    image=models.ImageField(upload_to='banner_images/')
    is_active= models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.section