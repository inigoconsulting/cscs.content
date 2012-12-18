from collective.portlet.collectionmultiview import BaseRenderer
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.interface import Interface
from zope import schema
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget

class FeaturedRenderer(BaseRenderer):

    title = 'Featured Renderer'
    template = ViewPageTemplateFile('featured.pt')

class ImageListingRenderer(BaseRenderer):

    title = 'Image Listing Renderer'
    template = ViewPageTemplateFile('image_listing.pt')


class ILeadSummaryRendererSchema(Interface):
    more_text = schema.TextLine(
        title=u'Title for "More" link',
        default=u"More",
        required=False
    )
    more_url = schema.TextLine(
        title=u'URL for "More" link',
        default=None,
        required=False
    )

class LeadSummaryRenderer(BaseRenderer):

    title = 'Lead Summary Renderer'
    schema = ILeadSummaryRendererSchema
    template = ViewPageTemplateFile('lead_summary.pt')

class EventsRenderer(BaseRenderer):

    title = 'Events Renderer'
    template = ViewPageTemplateFile('events.pt')

class RichTextRenderer(BaseRenderer):

    title = 'RichTextRenderer'
    template = ViewPageTemplateFile('richtext.pt')


class IStaticRichTextSchema(Interface):

    text = schema.Text(
        title=u'Text'
    )

    more_text = schema.TextLine(
        title=u'Title for "More" link',
        default=u"More",
        required=False
    )
    more_url = schema.TextLine(
        title=u'URL for "More" link',
        default=None,
        required=False
    )


class StaticRichTextRenderer(BaseRenderer):
    custom_widgets = {
        'text': WYSIWYGWidget
    }
    schema = IStaticRichTextSchema
    title = 'StaticRichTextRenderer'
    template = ViewPageTemplateFile('static_richtext.pt')
