import sendgrid
import os
import python_http_client
from sendgrid.helpers.mail import *
from decouple import config
from django import forms
from django.core.mail import send_mail
from django.db import models
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.core.validators import (
        RegexValidator, 
        MinValueValidator, 
        MaxValueValidator
    )

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
        FieldPanel,
        FieldRowPanel,
        InlinePanel,
        MultiFieldPanel,
        PageChooserPanel,
        StreamFieldPanel,
    )

from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page, Orderable
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from .blocks import BaseStreamBlock
from .forms import ContactForm

from projects.models import ProjectPage
from blog.models import BlogPage



@register_snippet
class People(ClusterableModel):
	first_name = models.CharField("First name", max_length=254)
	last_name = models.CharField("Last name", max_length=254)
	job_title = models.CharField("Job title", max_length=254)
	about = models.TextField(max_length=300)

	image = models.ForeignKey(
			'wagtailimages.Image',
			null=True,
			blank=True,
			on_delete=models.SET_NULL,
			related_name='+',
		)

	panels = [
		FieldPanel('first_name', classname="first-name"),
		FieldPanel('last_name', classname="last-name"),
		FieldPanel('job_title'),
		FieldPanel('about', classname="full"),
		ImageChooserPanel('image'),
	]

	search_fields = Page.search_fields + [
		index.SearchField('first_name'),
		index.SearchField('last_name'),
	]

	@property
	def thumb_image(self):
		# Returns an empty string if there is no profile pic or the rendition
		# file can't be found.
		try:
			return self.image.get_rendition('fill-50x50').img_tag()
		except:
			return ''

	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

	class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'People'


class StandardPage(Page):
	introduction = models.TextField(
			help_text='Text to describe the page',
			blank=True,
		)
	image = models.ForeignKey(
			'wagtailimages.Image',
			null=True,
			blank=True,
			on_delete=models.SET_NULL,
			related_name='+',
			help_text='Landscape mode only; horizontal width between 1000px and 3000px'
		)
	body = StreamField(
		BaseStreamBlock(), verbose_name="Page body", blank=True
	)

	content_panels = Page.content_panels + [
		FieldPanel('introduction', classname="full"),
		StreamFieldPanel('body'),
		ImageChooserPanel('image'),
	]



class HomePage(Page):
    logo_image = models.ForeignKey(
    		'wagtailimages.Image',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		help_text='Homepage logo',
    	)
    image = models.ForeignKey(
    		'wagtailimages.Image',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		help_text='Homepage image',
    	)
    hero_text = models.CharField(
    		max_length=255,
    		help_text='Write an introduction for the business',
    	)
    hero_title = models.CharField(
    		verbose_name='Hero CTA',
    		max_length=255,
    		help_text='Text to display on Call to Action',
    	)
    body = StreamField(
    	BaseStreamBlock(), verbose_name="Home content block", blank=True
    )
    skill_1 = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='A techincal skill i.e. Python',
    	)
    skill_2 = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='A techincal skill i.e. Python',
    	)
    skill_3 = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='A techincal skill i.e. Python',
    	)
    skill_4 = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='A techincal skill i.e. Python',
    	)
    skill_5 = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='A techincal skill i.e. Python',
    	)
    skill_6 = models.CharField(
            null=True,
            blank=True,
            max_length=255,
            help_text='A techincal skill i.e. Python',
        )
    skill_7 = models.CharField(
            null=True,
            blank=True,
            max_length=255,
            help_text='A techincal skill i.e. Python',
        )
    skill_8 = models.CharField(
            null=True,
            blank=True,
            max_length=255,
            help_text='A techincal skill i.e. Python',
        )
    skill_9 = models.CharField(
            null=True,
            blank=True,
            max_length=255,
            help_text='A techincal skill i.e. Python',
        )
    skill_1_percentage = models.IntegerField(
            null=True,
            blank=True,
            help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.',
            validators=[MinValueValidator(0), MaxValueValidator(100)]
        )
    skill_2_percentage = models.IntegerField(
            null=True,
            blank=True,
            help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.',
        )
    skill_3_percentage = models.IntegerField(
            null=True,
            blank=True,
            help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.',
        )
    skill_4_percentage = models.IntegerField(
            null=True,
            blank=True,
            help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.',
        )
    skill_5_percentage = models.IntegerField(
            null=True,
            blank=True,
            help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.',
        )
    skill_6_percentage = models.IntegerField(
            null=True,
            blank=True,
            help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.',
        )
    skill_7_percentage = models.IntegerField(
            null=True,
            blank=True,
            help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.',
        )
    skill_8_percentage = models.IntegerField(
            null=True,
            blank=True,
            help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.',
        )
    skill_9_percentage = models.IntegerField(
            null=True,
            blank=True,
            help_text='A percentage of mastery i.e. 90 percent. Just write the number not the percentage sign.',
        )
    promo_image = models.ForeignKey(
    		'wagtailimages.Image',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		help_text='Promo image',
    	)
    promo_title = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='Title to display above the promo copy',
    	)
    promo_text = RichTextField(
    		null=True,
    		blank=True,
    		help_text='Write some promotional copy',
    	)
    featured_section_1_title = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='Title to display above the promo copy',
    	)
    featured_section_1 = models.ForeignKey(
    		'wagtailcore.Page',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		help_text='First featured section for the homepage. Will display up to '
    		'three child names.',
    		verbose_name='Featured section 1',
    	)
    featured_section_2_title = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='Title to display above the promo copy',
    	)
    featured_section_2 = models.ForeignKey(
    		'wagtailcore.Page',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		help_text='First featured section for the homepage. Will display up to '
    		'three child names.',
    		verbose_name='Featured section 1',
    	)
    resume = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    content_panels = Page.content_panels + [
    	DocumentChooserPanel('resume'),
    	MultiFieldPanel([
    		FieldPanel('skill_1'),
            FieldPanel('skill_1_percentage'),
    		FieldPanel('skill_2'),
            FieldPanel('skill_2_percentage'),
    		FieldPanel('skill_3'),
            FieldPanel('skill_3_percentage'),
    		FieldPanel('skill_4'),
            FieldPanel('skill_4_percentage'),
    		FieldPanel('skill_5'),
            FieldPanel('skill_5_percentage'),
            FieldPanel('skill_6'),
            FieldPanel('skill_6_percentage'),
            FieldPanel('skill_7'),
            FieldPanel('skill_7_percentage'),
            FieldPanel('skill_8'),
            FieldPanel('skill_8_percentage'),
            FieldPanel('skill_9'),
            FieldPanel('skill_9_percentage'),
    		], heading="Skills section"),
    	MultiFieldPanel([
    		ImageChooserPanel('image'),
    		ImageChooserPanel('logo_image'),
    		FieldPanel('hero_text', classname="full"),
            FieldPanel('hero_title', classname="full"),
    		], heading="Hero section"),
    	MultiFieldPanel([
    		ImageChooserPanel('promo_image'),
    		FieldPanel('promo_title'),
    		FieldPanel('promo_text'),
    		], heading="Promo section"),
    	StreamFieldPanel('body'),
		MultiFieldPanel([
			MultiFieldPanel([
				FieldPanel('featured_section_1_title'),
				PageChooserPanel('featured_section_1'),
			]),
			MultiFieldPanel([
				FieldPanel('featured_section_2_title'),
				PageChooserPanel('featured_section_2'),
			]),
		], heading="Featured homepage section", classname="collapsible")
    ]

    def serve(self, request):
        context = super(HomePage, self).get_context(request)
        pp_list = [1, 2, 3]
        bp_list = [1, 2, 3]
        pp_objs = ProjectPage.objects.all()
        bp_objs = BlogPage.objects.all()
        for pp in pp_objs:
            for value in pp_list:
                if value == pp.feature and pp not in pp_list:
                    pp_list.insert(value-1, pp)
                    pp_list.remove(value)
        for bp in bp_objs:
            for value in bp_list:
                if value == bp.feature and bp not in bp_list:
                    bp_list.insert(value-1, bp)
                    bp_list.remove(value)
        context['pp_features_list'] = pp_list
        context['bp_features_list'] = bp_list
        form = ContactForm()
        return render(request, 'home/home_page.html', {
                'page': self,
                'form': form,
                'pp_features_list': pp_list,
                'bp_features_list': bp_list,
            })

    def submit_contact(request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form_full_name = form.cleaned_data['full_name']
            form_email = form.cleaned_data['email']
            form_message = form.cleaned_data['message']
            subject = 'Portfolio - ' + form.cleaned_data['subject'] 
            from_email = Email('telleria.portfolio@gmail.com')
            to_email = Email('andrewktelleria@gmail.com')
            context = {
                'form_full_name': form_full_name,
                'form_email': form_email,
                'form_message': form_message,
            }
            contact_message =Content("text/plain", get_template('home/contact_message.txt').render(context))
            try:
                sg = sendgrid.SendGridAPIClient(apikey=config('SENDGRID_API_KEY'))
                mail = Mail(from_email, subject, to_email, contact_message)
                print(mail)
                response = sg.client.mail.send.post(request_body=mail.get())
            except:
                return HttpResponse({'success' : False })
        return JsonResponse({'success' : True})

    def __str__(self):
    	return self.title


def GalleryPage(Page):
	"""
	This is a page to list locations from the selected Collection. We use a Q
	object to list any collection created even if they contain no items.
	"""
	introduction = models.TextField(
			help_text='Text to describe the page.',
			blank=True)
	image = models.ForeignKey(
			'wagtailimages.Image',
			null=True,
			blank=True,
			on_delete=models.SET_NULL,
			related_name='+',
			help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
		)
	body = StreamField(
		BaseStreamBlock(), verbose_name="Page body", blank=True
	)
	collection = models.ForeignKey(
			Collection,
			limit_choices_to=~model.Q(name__in=['Root']),
			null=True,
			blank=True,
			on_delete=models.SET_NULL,
			help_text='Select the image collection for this gallery.'
		)

	content_panels = Page.content_panels + [
		FieldPanel('introduction', classname="full"),
		StreamFieldPanel('body'),
		ImageChooserPanel('image'),
		FieldPanel('collection'),
	]

	# Defining what content type can sit under the parent. Since it's a blank
	# array no subpage can be added
	subpage_types = []


class HomePageImageGallery(Orderable):
	page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
	image = models.ForeignKey(
			'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
		)
	caption = models.CharField(blank=True, max_length=250)
	logo = models.BooleanField(default=False)

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
		FieldPanel('logo', widget=forms.RadioSelect),
	]


class FormField(AbstractFormField):
    """
    Wagtailforms is a module to introduce simple forms on a Wagtail site. It
    isn't intended as a replacement to Django's form support but as a quick way
    to generate a general purpose data-collection form or contact form
    without having to write code. We use it on the site for a contact form. You
    can read more about Wagtail forms at:
    http://docs.wagtail.io/en/latest/reference/contrib/forms/index.html
    """
    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)


class FormPage(AbstractEmailForm):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField(BaseStreamBlock())
    thank_you_text = RichTextField(blank=True)

    # Note how we include the FormField object via an InlinePanel using the
    # related_name value
    content_panels = AbstractEmailForm.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]
