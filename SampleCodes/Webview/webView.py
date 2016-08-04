def __init__(self, coding='utf-8'):
        gobject.GObject.__init__(self)
        gtk.VBox.__init__(self, False)
        
        self.coding = coding
        self.uri = 'file://' + os.path.dirname(__file__)
        self.settings = webkit.WebSettings()
        self.settings.set_property('enable-default-context-menu', False)
        '''
        self.settings.enable_java_applet = False
        self.settings.enable_plugins = False
        self.settings.enable_page_cache = True
        self.settings.enable_offline_web_application_cache = False
        self.settings.enable_html5_local_storage = False
        self.settings.enable_html5_database = False
        self.settings.enable_default_context_menu = False
        '''
        self.view = webkit.WebView()
        self.view.set_settings(self.settings)
        self.view.connect('load-started', self.__started)
        self.view.connect('load-finished', self.__finished)
        self.view.connect('console-message', self.__console_message)
        self.view.connect('navigation-policy-decision-requested', self.__process)
        
        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scroll.set_shadow_type(gtk.SHADOW_IN)
        scroll.add(self.view)
        
        self.pack_start(scroll, True, True, 0)
