from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CscscontentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cscs.content
        xmlconfig.file(
            'configure.zcml',
            cscs.content,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cscs.content:default')

CSCS_CONTENT_FIXTURE = CscscontentLayer()
CSCS_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CSCS_CONTENT_FIXTURE,),
    name="CscscontentLayer:Integration"
)
