from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import time


class cognitive(Page):
    form_model = 'player'
    form_fields = ['bat','machines','lake']

##############################################################
# Demographics
class demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income']


##############################################################
# End
class ending(Page):
    form_model = 'player'



page_sequence = [
    # Non-ravens
    cognitive,
    demographics,

# Common to all
    ending
]
