from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import (
    ExtensionHandlerMixin,
    ExtensionHandlerJinjaMixin
)
from jupyter_server.utils import url_path_join


class MainHandler(
    ExtensionHandlerJinjaMixin,
    ExtensionHandlerMixin,
    JupyterHandler
):

    @property
    def frontends(self):
        return self.settings['jupyter_home_frontends']

    @staticmethod
    def build_static_url(frontend):
        return url_path_join(frontend.static_url_prefix, "home.svg")

    # patch namespace to inject frontends into html page.
    @property
    def template_namespace(self):
        tn = super(MainHandler, self).template_namespace
        frontend_data = {}
        for extname, f in self.frontends.items():
            frontend_data[extname] = {
                "extension_url": f.extension_url,
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg"
            }
        tn['frontend_data'] = frontend_data
        return tn

    def get(self):
        html = self.render_template("main.html")
        self.write(html)

    post = put = get
