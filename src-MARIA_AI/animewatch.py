from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from jnius import autoclass
from android.runnable import run_on_ui_thread

WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

class Wv(Widget):
    def __init__(self, url, **kwargs):
        super(Wv, self).__init__(**kwargs)
        self.url = url
        Clock.schedule_once(self._setup_webview, 0)

    @run_on_ui_thread
    def _setup_webview(self, *args):
        self.webview = WebView(activity)
        self.webview.setWebViewClient(WebViewClient())
        activity.addContentView(self.webview,
                                autoclass('android.view.ViewGroup$LayoutParams')(
                                    autoclass('android.view.ViewGroup$LayoutParams').MATCH_PARENT,
                                    autoclass('android.view.ViewGroup$LayoutParams').MATCH_PARENT))
        self.webview.loadUrl(self.url)

class WebViewApp(App):
    def build(self):
        return Wv(url='https://www.kivy.org')

if __name__ == '__main__':
    WebViewApp().run()