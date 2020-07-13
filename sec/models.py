from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'sec'
    players_per_group = 9
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # Player 1 - stories
    p1_s1 = models.LongStringField()
    p1_s2 = models.LongStringField()
    p1_s3 = models.LongStringField()
    p1_s4 = models.LongStringField()
    p1_s5 = models.LongStringField()
    p1_s6 = models.LongStringField()
    p1_s7 = models.LongStringField()
    p1_s8 = models.LongStringField()
    p1_s9 = models.LongStringField()

