from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'plec'
    players_per_group = 9
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    story_1 = models.LongStringField(
        label = "Please write a sentence that continues the story ")
    story_2 = models.LongStringField(
        label = "Please write a sentence that continues the story ")
    story_3 = models.LongStringField(
        label = "Please write a sentence that continues the story ")
    story_4 = models.LongStringField(
        label = "Please write a sentence that continues the story ")
    story_5 = models.LongStringField(
        label = "Please write a sentence that continues the story ")
    story_6 = models.LongStringField(
        label = "Please write a sentence that continues the story ")
    story_7 = models.LongStringField(
        label = "Please write a sentence that continues the story ")
    story_8 = models.LongStringField(
        label = "Please write a sentence that continues the story ")
    story_9 = models.LongStringField(
        label = "Please write a sentence that continues the story ")

