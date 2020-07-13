from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Huanren Zhang'

doc = """
Raven's progressive matrices test measuring cognitive ability
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField(choices=[1,2,3,4,5,6,7,8])
    ans_correct = models.BooleanField()

        #Cognitive
    bat = models.IntegerField(
        min=0, max=110)
    machines = models.IntegerField(
        min=0, max=300)
    lake = models.IntegerField(
        min=0, max=48)

    # Demographics
    age = models.IntegerField(
        label='What is your age?',
        min=13, max=125)

    gender = models.StringField(
        choices=['Male', 'Female', 'Other'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    income = models.IntegerField(
        label='What is the annual income of your family in USD?',
        min=100, max=3000000)
