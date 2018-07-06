from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
	FieldPanel,
	FieldRowPanel,
	InlinePanel,
	MultiFieldPanel,
	PageChooserPanel,
	StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField

from .blocks import BaseStreamBlock


class HomePage(Page):
    body = StreamField(
    	BaseStreamBlock(), verbose_name="Page body", blank=True
    )

    content_panels = Page.content_panels + [
    	StreamFieldPanel('body'),
    ]
