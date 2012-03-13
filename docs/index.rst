
Flask-Raptor
======================================

.. module:: Flask-Raptor

The **Flask-Raptor** [#f1]_ extension provides support for adding raptors to `Flask`_ instances.::

    import flask_raptor

    from myapp import app

    flask_raptor.init_app(app)
    
    if __name__ == "__main__":
        app.run()


**Flask-Raptor** will automatically inject a raptor into the ``<head>`` element of any HTML returned by a view function.

Source code and issue tracking at `GitHub`_.

Installing Flask-Raptor
-----------------------

Install with **pip** and **easy_install**::

    pip install Flask-Raptor

or download the latest version from version control::

    git clone https://github.com/dplepage/flask-raptor.git
    cd flask-raptor
    python setup.py develop

If you are using **virtualenv**, it is assumed that you are installing **Flask-Raptor**
in the same virtualenv as your Flask application(s).

Configuration
-------------

**Flask-Raptor** uses the following application-level configuration variables:

  * ``RAPTOR_CHANCE`` - the probability of a raptor appearing on any given page. This must be an number between 0.0 (no chance of raptor attack) and 1.0 (guaranteed raptor on every page). Default: ``1.0``
  * ``RAPTOR_FOOLS`` - whether to only invoke the raptor on April 1st. Default: ``False``
  * ``RAPTOR_TRIGGER`` - what causes a raptor attack? This must be either ``"timer"`` or ``"konami-code"``. If ``RAPTOR_TRIGGER`` is ``"timer"``, then a raptor will attack automatically after a fixed delay; if instead it is ``"konami-code"``, then a raptor will only be triggered upon entry of the `Konami Code`_.
  * ``RAPTOR_DELAY`` - The delay, in milliseconds, before a raptor attack. If ``RAPTOR_TRIGGER`` is ``"timer"``, then ``RAPTOR_DELAY`` determines the delay before a raptor attacks automatically.

.. _api:
.. _Flask: http://flask.pocoo.org
.. _GitHub: http://github.com/dplepage/flask-raptor
.. _Konami Code: http://en.wikipedia.org/wiki/Konami_Code
.. [#f1] Raptor image courtesy of `Ryan North <http://www.qwantz.com/>`_