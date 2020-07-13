from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'field_test'
    players_per_group = 3
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
    p1_j = models.LongStringField()

    # Player 1 - stories
    p1_s1 = models.LongStringField()
    p1_s2 = models.LongStringField()
    p1_s3 = models.LongStringField()

    # Player 1 - Paragraph
    p1_para = models.LongStringField()
    p1_dt1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8],
        label="Please select the correct answer: ")

    # Player 1 - Cumulative Story
    p1_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")


##### ---------------------- ####
	# Player 2
    p2_a = models.LongStringField()
    p2_b = models.LongStringField()

    # Player 2 - stories
    p2_s1 = models.LongStringField()
    p2_s2 = models.LongStringField()
    p2_s3 = models.LongStringField()

    # Player 2 - Paragraph
    p2_para = models.LongStringField()
    p2_dt1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8],
        label="Please select the correct answer: ")

    # Player 2 - Cumulative Story
    p2_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")
    

##### ---------------------- ####

   	# Player 3
    p3_a = models.LongStringField()
    p3_b = models.LongStringField()

    # Player 3 - stories
    p3_s1 = models.LongStringField()
    p3_s2 = models.LongStringField()
    p3_s3 = models.LongStringField()

    # Player 3 - Paragraph
    p3_para = models.LongStringField()
    p3_dt1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8],
        label="Please select the correct answer: ")

    # Player 13- Cumulative Story
    p3_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")
    

##### ---------------------- ####

