from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
	FieldPanel,
	FieldRowPanel,
	InlinePanel,
	MultiFieldPanel,
	PageChooserPanel,
	StreamFieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from home.blocks import BaseStreamBlock


class BlogIndexPage(Page):
	intro = RichTextField(blank=True)

	def get_context(self, request):
		context = super().get_context(request)
		blogpages = self.get_children().live().order_by('-first_published_at')
		context['blogpages'] = blogpages
		return context

	content_panels = Page.content_panels + [
		FieldPanel('intro', classname="full"),
	]


class BlogPage(Page):
	date = models.DateField("Post date")
	intro = models.CharField(max_length=255)
	body = StreamField(
		BaseStreamBlock(), verbose_name="Blog body", blank=True
	)

	def main_image(self):
		gallery_item = self.gallery_images.first()
		if gallery_item:
			return gallery_item.image
		else:
			return None

	search_fields = Page.content_panels + [
		index.SearchField('intro'),
		index.SearchField('body'),
	]

	content_panels = Page.content_panels + [
		FieldPanel('date'),
		FieldPanel('intro'),
		StreamFieldPanel('body'),
		InlinePanel('gallery_images', label="Gallery images"),
	]


class BlogPageGalleryImage(Orderable):
	page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
	)
	caption = models.CharField(blank=True, max_length=250)

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
	]	








