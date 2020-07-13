from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'study_bocconi'
    players_per_group = 12
    num_rounds = 1



class Subsession(BaseSubsession):

	def creating_session(self):
		import itertools
		treatment = itertools.cycle(['A', 'B','C','D','E','F','G','H','I','J','K','L'])
		for p in self.get_players():
			p.treatment = next(treatment)


class Group(BaseGroup):
	pass



class Player(BasePlayer):
    # All players
    treatment = models.StringField()

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
    
    # Treatment 1 variables
    t1_stage1 = models.LongStringField()
    t1_stage2 = models.LongStringField()
    t1_stage3_dv1 = models.LongStringField()
    t1_stage3_dv2 = models.LongStringField()
    t1_stage4 = models.LongStringField()
    t1_stage5 = models.LongStringField()
    t1_stage6_dv1 = models.LongStringField()
    t1_stage6_dv2 = models.LongStringField()


    # Treatment 2 variables
    t2_stage1 = models.LongStringField()
    t2_stage1_detail = models.LongStringField()
    t2_stage2_dv1 = models.LongStringField()
    t2_stage2_dv2 = models.LongStringField()
    t2_stage3_dv1 = models.LongStringField()
    t2_stage3_dv2 = models.LongStringField()


    # Treatment 3 variables
    q1_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q2_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q3_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q4_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q5_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q6_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q7_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q8_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q9_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q10_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    t3_stage2_dv1 = models.LongStringField()
    t3_stage2_dv2 = models.LongStringField()
    t3_stage3_dv1 = models.LongStringField()
    t3_stage3_dv2 = models.LongStringField()


    
    #Cognitive
    bat = models.IntegerField(
        min=0, max=110)
    machines = models.IntegerField(
        min=0, max=300)
    lake = models.IntegerField(
        min=0, max=48)



