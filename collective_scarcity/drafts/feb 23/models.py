from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'collective_scarcity'
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
    q11_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q12_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q13_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q14_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q15_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q16_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q17_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q18_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q19_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q20_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )    
    q21_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q22_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q23_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q24_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q25_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q26_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q27_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q28_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q29_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    q30_stars  = models.StringField(
        choices=['Right', 'Left'],
        label='Choose one option',
        widget=widgets.RadioSelect
        )
    t3_stage2_dv1 = models.LongStringField()
    t3_stage2_dv2 = models.LongStringField()
    t3_stage3_dv1 = models.LongStringField()
    t3_stage3_dv2 = models.LongStringField()



    # Scarcity
    resources = models.IntegerField(
        label='My resources are scarce',
        min=1, max=5)
    enough = models.IntegerField(
        label='I do not have enough resources',
        min=1, max=5)
    protect = models.IntegerField(
        label='I need to protect the resources I have',
        min=1, max=5)
    more = models.IntegerField(
        label='I need to aquire more resources',
        min=1, max=5)

    #Cognitive
    bat = models.IntegerField(
        min=0, max=110)
    machines = models.IntegerField(
        min=0, max=300)
    lake = models.IntegerField(
        min=0, max=48)



    # Affect
    interested = models.IntegerField(
        label='interested',
        min=1, max=5)
    distressed = models.IntegerField(
        label='distressed',
        min=1, max=5)
    excited = models.IntegerField(
        label='excited',
        min=1, max=5)
    upset = models.IntegerField(
        label='upset',
        min=1, max=5)
    strong = models.IntegerField(
        label='strong',
        min=1, max=5)
    guilty = models.IntegerField(
        label='guilty',
        min=1, max=5)
    scared = models.IntegerField(
        label='scared',
        min=1, max=5)
    hostile = models.IntegerField(
        label='hostile',
        min=1, max=5)
    enthusiastic = models.IntegerField(
        label='enthusiastic',
        min=1, max=5)
    proud = models.IntegerField(
        label='proud',
        min=1, max=5)
    irritable = models.IntegerField(
        label='irritable',
        min=1, max=5)
    alert = models.IntegerField(
        label='alert',
        min=1, max=5)
    ashamed = models.IntegerField(
        label='ashamed',
        min=1, max=5)
    inspired = models.IntegerField(
        label='inspired',
        min=1, max=5)
    nervous = models.IntegerField(
        label='nervous',
        min=1, max=5)
    determined = models.IntegerField(
        label='determined',
        min=1, max=5)
    attentive = models.IntegerField(
        label='attentive',
        min=1, max=5)
    jittery = models.IntegerField(
        label='jittery',
        min=1, max=5)
    active = models.IntegerField(
        label='active',
        min=1, max=5)
    afraid = models.IntegerField(
        label='afraid',
        min=1, max=5)