from django import forms
from django.db import models
from django.core.validators import RegexValidator

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

from projects.models import ProjectPage
from blog.models import BlogPage, BlogPageGalleryImage



@register_snippet
class People(ClusterableModel):
	"""
	A Django model to store people objects. It uses the '@register_snippet'
	decorator to allow it to be accesible via the Snippets UI

	'People' uses the 'ClusterableModel', which allows the relationship with
	another model to be stored locally to the 'parent' model (e.g. a PageModel)
	until the parent is explicitly saved. This allows the editor to use the
	'Preview' button, to preview the content, without saving the relationships
	to the database.
	https://github.com/wagtail/django-modelcluster
	"""
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
	"""
	A generic content page. On this demo site we use it for an about page but
	it could be used for any page content that only needs a title,
	image, introduction, and body field
	"""

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
    """
	The Home Page. This looks slightly more complicated then it is. You can see
	if you visit your site and edit the homepage that it is split between a:
		- Hero area
		- Body area
		- A promotional area
		- Moveable feature site sections
    """

    # Hero section of HomePage
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
    hero_cta = models.CharField(
    		verbose_name='Hero CTA',
    		max_length=255,
    		help_text='Text to display on Call to Action',
    	)
    hero_cta_link = models.ForeignKey(
    		'wagtailcore.Page',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		verbose_name='Hero CTA link',
    		help_text='Choose a page to link to for the Call to Action',
    	)
    phone_regex = RegexValidator(regex=r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)', message="Phone must be entered in the format (555) 567-8555")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email = models.EmailField(max_length=100)

    # Body section of the HomePage
    body = StreamField(
    	BaseStreamBlock(), verbose_name="Home content block", blank=True
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

    # Featured sections on the HomePage
    # You will see on templates/home/home_page.html that these are treated
    # in different ways, and displayed in different areas of the page.
    # Each list their children items that we access via the children function
    # that we define on the individual Page models e.g. BlogIndexPage
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
    featured_section_3_title = models.CharField(
    		null=True,
    		blank=True,
    		max_length=255,
    		help_text='Title to display above the promo copy',
    	)
    featured_section_3 = models.ForeignKey(
    		'wagtailcore.Page',
    		null=True,
    		blank=True,
    		on_delete=models.SET_NULL,
    		related_name='+',
    		help_text='First featured section for the homepage. Will display up to '
    		'three child names.',
    		verbose_name='Featured section 1',
    	)
    # Resume
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
    		ImageChooserPanel('image'),
    		ImageChooserPanel('logo_image'),
    		FieldPanel('hero_text', classname="full"),
    		FieldPanel('phone_number'),
    		FieldPanel('email'),
    		MultiFieldPanel([
    			FieldPanel('hero_cta'),
    			PageChooserPanel('hero_cta_link'),
    			]),
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
			MultiFieldPanel([
				FieldPanel('featured_section_3_title'),
				PageChooserPanel('featured_section_3'),
			]),
		], heading="Featured homepage section", classname="collapsible")
    ]


    def phone_number_fixer(self):
    	HomePage.objects.get("phone_number")

    def get_context(self, request):
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
    	return context

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


class FormField(AbstractFormField):
	"""
	Wagtailforms is a module to introduce simple forms on a wagtail site. It isn't
	intended as a replacement to Django's form support but as a quick way to generate
	without having to write code. We use it on the site for a contact form.
	"""
	page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)


class FormPage(AbstractEmailForm):
	image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+',
		)
	body = StreamField(BaseStreamBlock(), null=True)
	thank_you_text = RichTextField(blank=True)

	# Note how we include the FormField object vie an InlinePanel using
	# related_name value
	content_panels = AbstractEmailForm.content_panels + [
	ImageChooserPanel('image'),
	StreamFieldPanel('body'),
	InlinePanel('form_fields', label="Form fields"),
	FieldPanel('thank_you_text', classname="full"),
	MultiFieldPanel([
		FieldRowPanel([
			FieldPanel('from_address', classname="form-page"),
			FieldPanel('to_address', classname="form-page"),
			]),
		FieldPanel('subject'),
		], "Email"),
	]


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
