from django.db import models

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from home.blocks import BaseStreamBlock


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    class Meta:
        verbose_name = "blog indexpage"
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    subpage_types = ['Blogpage']

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        # Get the full unpaginated listing of resource pages as a queryset
        all_resources = BlogPage.objects.descendant_of(
            self).live().order_by(
            '-first_published_at')
        paginator = Paginator(all_resources, 5)
        page = request.GET.get('page')
        try:
            resources = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            resources = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            resources = paginator.page(paginator.num_pages)
        context['resources'] = resources
        return context


class BlogPageTag(TaggedItemBase):

    class Meta:
        verbose_name = "blogpage tag"

    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):
    author = models.ForeignKey(
        'home.People',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
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
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="""Landscape mode only;
            horizontal width between 1000px and 3000px."""
    )
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    class Meta:
        verbose_name = "blogpage"

    def main_image(self):
        return self.image

    search_fields = Page.search_fields + [
        index.SearchField('author'),
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = [
        FieldPanel('title', classname="full"),
        SnippetChooserPanel('author'),
        FieldPanel('feature'),
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]


class BlogTagIndexPage(Page):

    class Meta:
        verbose_name = "blogtag indexpage"

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context
