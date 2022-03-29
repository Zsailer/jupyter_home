from jupyter_server.extension.application import ExtensionApp, ExtensionAppJinjaMixin
from jupyter_server.extension.serverextension import _get_extmanager_for_context

from .paths import DEFAULT_STATIC_FILES_PATH, DEFAULT_TEMPLATE_PATH_LIST
from .handler import MainHandler


class JupyterHome(ExtensionAppJinjaMixin, ExtensionApp):

    name = "jupyter-home"
    extension_name = "jupyter_home"
    extension_url = '/home'

    template_paths = DEFAULT_TEMPLATE_PATH_LIST
    static_paths = DEFAULT_STATIC_FILES_PATH

    def initialize_settings(self):

        frontends = {}

        configurations = (
            {"user": True, "sys_prefix": False},
            {"user": False, "sys_prefix": True},
            {"user": False, "sys_prefix": False}
        )
        for option in configurations:
            _, ext_manager = _get_extmanager_for_context(**option)
            for extname, extapps in ext_manager.extension_apps.items():
                self.log.info(extname)
                self.log.info(extapps)
                for extapp in extapps:
                    if isinstance(extapp, ExtensionApp):
                        if extname != self.extension_name:
                            frontends[extname] = extapp
        self.log.info(frontends)
        self.settings['jupyter_home_frontends'] = frontends

    def initialize_handlers(self):
        self.handlers.append(
            ('/home', MainHandler)
        )


main = JupyterHome.launch_instance