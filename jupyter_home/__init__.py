from .app import JupyterHome


def _jupyter_server_extension_paths():
    return [
        {
            'module': 'jupyter_home.app',
            'app': JupyterHome
        }
    ]