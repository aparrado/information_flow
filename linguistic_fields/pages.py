from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Contribute(Page):
    form_model = 'player'
    form_fields = ['r1']


class ResultsWaitPage(WaitPage):
    pass



class Results(Page):
    def vars_for_template(self):
        otherplayers = self.player.get_others_in_group()
        otherplayer1 = otherplayers[0]
        otherscore = otherplayer1.participant.vars
        return {'otherscore': otherplayer1.r1}


page_sequence = [
    Contribute,
    ResultsWaitPage,
    Results
]
