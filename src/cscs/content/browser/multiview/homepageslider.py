from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from collective.portlet.collectionmultiview import BaseRenderer

class HomepageSliderRenderer(BaseRenderer):

    title = 'Homepage Slider'
    template = ViewPageTemplateFile('homepageslider.pt')

