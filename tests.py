import unittest

from flask import Flask
from flask_raptor import init_app


class RaptorTestCase(unittest.TestCase):
    
    def build_app(self):
        app = Flask(__name__)
        app.debug = True
        app.secret_key = 'hunter2'
        self.app = app

        @app.route('/')
        def foo():
            return '<html><head></head><body>foo</body></html>'
        return app
    
    def test_raptorize(self):
        app = self.build_app()
        init_app(app)
        response = app.test_client().get("/")
        assert '/raptorizemw/resources/jquery.raptorize' in response.data
    
    def test_resources(self):
        app = self.build_app()
        init_app(app)
        response = app.test_client().get("/raptorizemw/resources/js_helper.js")
        assert 'function include_js(url, success)' in response.data
        assert response.status == "200 OK"
    
    def test_options(self):
        app = self.build_app()
        app.config['RAPTOR_TRIGGER'] = 'konami-code'
        # app.config['RAPTOR_CHANCE'] = .5
        # app.config['RAPTOR_FOOLS'] = "true"
        app.config['RAPTOR_DELAY'] = 5000
        init_app(app)
        response = app.test_client().get("/")
        assert 'enterOn: "konami-code"' in response.data
        assert 'delayTime: 5000' in response.data

    def test_chance(self):
        app = self.build_app()
        app.config['RAPTOR_CHANCE'] = 0
        init_app(app)
        response = app.test_client().get("/")
        assert '/raptorizemw/resources/jquery.raptorize' not in response.data
        

if __name__ == '__main__':
    unittest.main()

