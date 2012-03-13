from raptorizemw import make_middleware

def init_app(app):
    random_chance = app.config.get("RAPTOR_CHANCE", 1.0)
    only_on_april_1st = app.config.get("RAPTOR_FOOLS", False)
    enterOn = app.config.get("RAPTOR_TRIGGER", 'timer')
    delayTime = app.config.get("RAPTOR_DELAY", 2000)
    app.wsgi_app = make_middleware(app.wsgi_app, random_chance=random_chance,
        only_on_april_1st=only_on_april_1st, enterOn=enterOn,
        delayTime=delayTime, serve_resources=True)
    return app
