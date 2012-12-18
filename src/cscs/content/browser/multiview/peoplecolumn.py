from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from collective.portlet.collectionmultiview import BaseRenderer

class PeopleColumnRenderer(BaseRenderer):
    """ display people in a single row table """

    title = 'People Columns'
    template = ViewPageTemplateFile('peoplecolumn.pt')

