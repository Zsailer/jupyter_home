from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin, ExtensionHandlerJinjaMixin
from jupyter_server.utils import url_path_join

class MainHandler(ExtensionHandlerJinjaMixin, ExtensionHandlerMixin, JupyterHandler):

    @property
    def frontends(self):
        return self.settings['frontends']

    @staticmethod
    def build_static_url(frontend):
        return url_path_join(frontend.static_url_prefix, "home.svg")

    # patch namespace to inject frontends into html page.
    @property
    def template_namespace(self):
        tn = super(MainHandler, self).template_namespace
        frontend_data = {}
        for f in self.frontends.values():
            frontend_data[f.extension_name] = {
                "default_url": f.default_url,
                "image_url": self.build_static_url(f)
            }

        tn['frontend_data'] = self.frontends
        return tn

    def get(self):
        html = self.render_template("main.html")
        self.write(html)

    post = put = get
