from email.policy import default
from django.db import models
from django.utils.timezone import now

from wagtail.models import Page, Orderable

from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.fields import RichTextField
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from colorfield.fields import ColorField


class HomePage(Page):
    """_summary_

    Args:
        Page (_type_): _description_
    """

    max_count = 1

    first_name = models.CharField(max_length=64, null=True)
    second_name = models.CharField(max_length=64, null=True)
    professional_title = models.CharField(max_length=140, blank=True, null=True)
    personal_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Please, upload a square photo (for example 256px x 256px).",
    )
    about = RichTextField(blank=False, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("first_name"),
                FieldPanel("second_name"),
                FieldPanel("professional_title"),
                ImageChooserPanel("personal_photo"),
            ],
            heading="Main_info",
        ),
        FieldPanel("about"),
        InlinePanel("skills", label="skills", min_num=0, max_num=36),
        InlinePanel("projects", label="projects", min_num=0),
        InlinePanel("experience", label="experience", min_num=0),
        InlinePanel("education", label="education", min_num=0),
        InlinePanel("publication", label="publication", min_num=0),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class Skill(Orderable):
    page = ParentalKey("home.HomePage", related_name="skills")
    name = models.CharField(max_length=256)
    icon = models.CharField(max_length=256)

    class Meta(Orderable.Meta):
        unique_together = ("name", "icon")

    def __str__(self):
        return self.name


class Project(Orderable, ClusterableModel):
    page = ParentalKey("home.HomePage", related_name="projects")
    title = models.CharField(max_length=64)
    description = RichTextField(blank=True, null=True)
    logo = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    demo_url = models.URLField(blank=True, null=True)
    source_url = models.URLField()
    finished_date = models.DateField("Finished date", blank=True, null=True)

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        ImageChooserPanel("logo"),
        FieldPanel("demo_url"),
        FieldPanel("source_url"),
        FieldPanel("finished_date"),
        InlinePanel(
            "used_technologies", label="Used technologies", min_num=0, max_num=12
        ),
    ]


class ProjectTechnologyPairs(Orderable):
    project = ParentalKey(
        "home.Project", on_delete=models.CASCADE, related_name="used_technologies"
    )
    used_technology = models.ForeignKey("home.UsedTechnology", on_delete=models.CASCADE)

    panels = [SnippetChooserPanel("used_technology")]

    class Meta(Orderable.Meta):
        unique_together = ("project", "used_technology")


@register_snippet
class UsedTechnology(models.Model):
    name = models.CharField(max_length=256)
    color = ColorField(default="#FFFFFF")

    def __str__(self) -> str:
        return self.name


class Experience(Orderable):
    page = ParentalKey("home.HomePage", related_name="experience")
    job_title = models.CharField(max_length=256, default="Job Title", blank=True)
    company = models.CharField(max_length=256, default=None, blank=True)
    company_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=256, default=None, blank=True)
    start = models.DateField(default=now)
    end = models.DateField(blank=True, null=True)
    achievement_1 = models.CharField(max_length=2000, default=None, blank=True)
    achievement_2 = models.CharField(max_length=2000, default=None, blank=True)
    achievement_3 = models.CharField(max_length=2000, default=None, blank=True)
    achievement_4 = models.CharField(max_length=2000, default=None, blank=True)

    class Meta(Orderable.Meta):
        unique_together = ("job_title", "company")

    def __str__(self):
        return self.job_title


class Education(Orderable):
    page = ParentalKey("home.HomePage", related_name="education")
    program_name = models.CharField(max_length=128)
    faculty = models.CharField(max_length=128, blank=True, null=True)
    degree = models.CharField(max_length=128)
    educational_institution = models.CharField(max_length=128)
    educational_institution_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=256, default=None, blank=True)
    start = models.DateField(default=now)
    end = models.DateField(blank=True, null=True)
    gpa = models.FloatField()
    max_gpa = models.FloatField(default=5.0, blank=True)

    class Meta(Orderable.Meta):
        unique_together = ("educational_institution", "program_name")

    def __str__(self):
        return self.program_name


class Publication(Orderable):
    page = ParentalKey("home.HomePage", related_name="publication")
    name = RichTextField(blank=True, null=True)
    authors = RichTextField(blank=True, null=True)
    journal = RichTextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    doi = models.CharField(max_length=256)
    impact_factor = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta(Orderable.Meta):
        unique_together = ("name", "journal")

    def __str__(self):
        return self.name
