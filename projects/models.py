from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    InlinePanel, 
    MultiFieldPanel, 
    StreamFieldPanel,
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class ProjectIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        projectpages = self.get_children().live().order_by('-first_published_at')
        context['projectpages'] = projectpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class ProjectPage(Page):
    FEATURE_1 = 1
    FEATURE_2 = 2
    FEATURE_3 = 3
    NO_FEATURE = 0
    FEATURE_CHOICES = (
        (FEATURE_1, 'Feature 1'),
        (FEATURE_2, 'Feature 2'),
        (FEATURE_3, 'Feature 3'),
        (NO_FEATURE, 'No feature')
    )
    feature = models.IntegerField(
        choices=FEATURE_CHOICES,
        default=0,
    )
    project_url = models.CharField(max_length=250)
    github = models.CharField(max_length=250)
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ])
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    class Meta:
        verbose_name = "projectpage"

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels =  [
        FieldPanel('title', classname="full"),
        FieldPanel('intro', classname="full"),
        FieldPanel('date'),
        FieldPanel('feature'),
        FieldPanel('project_url'),
        FieldPanel('github'),
        ImageChooserPanel('image'),
        InlinePanel('gallery_images', label="Gallery images"),
        StreamFieldPanel('body'),
    ]

class ProjectPageGalleryImage(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
            'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
        )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]