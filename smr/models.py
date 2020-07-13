from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'smr'
    players_per_group = 9
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
	# Player 1 - sentences
    p1_a = models.LongStringField()
    p1_b = models.LongStringField()
    p1_c = models.LongStringField()
    p1_d = models.LongStringField()
    p1_e = models.LongStringField()
    p1_f = models.LongStringField()
    p1_g = models.LongStringField()
    p1_h = models.LongStringField()
    p1_i = models.LongStringField()   

