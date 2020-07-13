from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

SESSION_CONFIGS = [
        dict(
        name='field_test',
        num_demo_participants=9,
        app_sequence=['field_test']
    ),

        dict(
        name='testing_all',
        num_demo_participants=9,
        app_sequence=['smr','sec','plec']
    ),

        dict(
        name='sutudy_bocconi',
        num_demo_participants=12,
        app_sequence=['collective_scarcity','ravens','survey']
    ),


        dict(
        name='survey',
        num_demo_participants=1,
        app_sequence=['ravens','survey']
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt'
    ),
    dict(
        name='live_demo',
        display_name='Room for live demo (no participant labels)'
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '#=c13f8kc)_91tvgu!06p)99bhb1w*$xhv7fps9ll6fb1rz+92'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

