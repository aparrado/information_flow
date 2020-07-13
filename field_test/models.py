from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'field_test'
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

    # Player 1 - stories
    p1_s1 = models.LongStringField()
    p1_s2 = models.LongStringField()
    p1_s3 = models.LongStringField()

    # Player 1 - Paragraph
    p1_para = models.LongStringField()
    p1_dt1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8],
        widget=widgets.RadioSelect,
        label="Please select the correct answer: ")

    # Player 1 - Cumulative Story
    p1_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")


##### ---------------------- ####
	# Player 2
    p2_a = models.LongStringField()
    p2_b = models.LongStringField()
    p2_c = models.LongStringField()
    p2_d = models.LongStringField()
    p2_e = models.LongStringField()
    p2_f = models.LongStringField()
    p2_g = models.LongStringField()
    p2_h = models.LongStringField()
    p2_i = models.LongStringField()   

    # Player 2 - stories
    p2_s1 = models.LongStringField()
    p2_s2 = models.LongStringField()
    p2_s3 = models.LongStringField()

    # Player 2 - Paragraph
    p2_para = models.LongStringField()
    p2_dt1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8],
        widget=widgets.RadioSelect,
        label="Please select the correct answer: ")

    # Player 2 - Cumulative Story
    p2_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")
    

##### ---------------------- ####

   	# Player 3
    p3_a = models.LongStringField()
    p3_b = models.LongStringField()
    p3_c = models.LongStringField()
    p3_d = models.LongStringField()
    p3_e = models.LongStringField()
    p3_f = models.LongStringField()
    p3_g = models.LongStringField()
    p3_h = models.LongStringField()
    p3_i = models.LongStringField()   

    # Player 3 - stories
    p3_s1 = models.LongStringField()
    p3_s2 = models.LongStringField()
    p3_s3 = models.LongStringField()

    # Player 3 - Paragraph
    p3_para = models.LongStringField()
    p3_dt1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8],
        widget=widgets.RadioSelect,
        label="Please select the correct answer: ")

    # Player 3- Cumulative Story
    p3_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")

##### ---------------------- ####

    # Player 4
    p4_a = models.LongStringField()
    p4_b = models.LongStringField()
    p4_c = models.LongStringField()
    p4_d = models.LongStringField()
    p4_e = models.LongStringField()
    p4_f = models.LongStringField()
    p4_g = models.LongStringField()
    p4_h = models.LongStringField()
    p4_i = models.LongStringField()   
    
    # Player 4 - stories
    p4_s1 = models.LongStringField()
    p4_s2 = models.LongStringField()
    p4_s3 = models.LongStringField()

    # Player 4 - Paragraph
    p4_para = models.LongStringField()
    
    # Player 4- Cumulative Story
    p4_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")


##### ---------------------- ####

    # Player 5
    p5_a = models.LongStringField()
    p5_b = models.LongStringField()
    p5_c = models.LongStringField()
    p5_d = models.LongStringField()
    p5_e = models.LongStringField()
    p5_f = models.LongStringField()
    p5_g = models.LongStringField()
    p5_h = models.LongStringField()
    p5_i = models.LongStringField()   


    # Player 5 - stories
    p5_s1 = models.LongStringField()
    p5_s2 = models.LongStringField()
    p5_s3 = models.LongStringField()

    # Player 5 - Paragraph
    p5_para = models.LongStringField()

    # Player 5- Cumulative Story
    p5_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")

##### ---------------------- ####

    # Player 6
    p6_a = models.LongStringField()
    p6_b = models.LongStringField()
    p6_c = models.LongStringField()
    p6_d = models.LongStringField()
    p6_e = models.LongStringField()
    p6_f = models.LongStringField()
    p6_g = models.LongStringField()
    p6_h = models.LongStringField()
    p6_i = models.LongStringField()   

    # Player 6 - stories
    p6_s1 = models.LongStringField()
    p6_s2 = models.LongStringField()
    p6_s3 = models.LongStringField()

    # Player 6 - Paragraph
    p6_para = models.LongStringField()

    # Player 6- Cumulative Story
    p6_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")


##### ---------------------- ####

    # Player 7
    p7_a = models.LongStringField()
    p7_b = models.LongStringField()
    p7_c = models.LongStringField()
    p7_d = models.LongStringField()
    p7_e = models.LongStringField()
    p7_f = models.LongStringField()
    p7_g = models.LongStringField()
    p7_h = models.LongStringField()
    p7_i = models.LongStringField()   

    # Player 7 - stories
    p7_s1 = models.LongStringField()
    p7_s2 = models.LongStringField()
    p7_s3 = models.LongStringField()

    # Player 7 - Paragraph
    p7_para = models.LongStringField()


    # Player 7- Cumulative Story
    p7_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")

##### ---------------------- ####

    # Player 8
    p8_a = models.LongStringField()
    p8_b = models.LongStringField()
    p8_c = models.LongStringField()
    p8_d = models.LongStringField()
    p8_e = models.LongStringField()
    p8_f = models.LongStringField()
    p8_g = models.LongStringField()
    p8_h = models.LongStringField()
    p8_i = models.LongStringField()   

    # Player 8 - stories
    p8_s1 = models.LongStringField()
    p8_s2 = models.LongStringField()
    p8_s3 = models.LongStringField()

    # Player 8 - Paragraph
    p8_para = models.LongStringField()

    # Player 8- Cumulative Story
    p8_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")

##### ---------------------- ####

    # Player 9
    p9_a = models.LongStringField()
    p9_b = models.LongStringField()
    p9_c = models.LongStringField()
    p9_d = models.LongStringField()
    p9_e = models.LongStringField()
    p9_f = models.LongStringField()
    p9_g = models.LongStringField()
    p9_h = models.LongStringField()
    p9_i = models.LongStringField()   

    # Player 9 - stories
    p9_s1 = models.LongStringField()
    p9_s2 = models.LongStringField()
    p9_s3 = models.LongStringField()

    # Player 9 - Paragraph
    p9_para = models.LongStringField()


    # Player 9- Cumulative Story
    p9_story = models.LongStringField(
        label = "Please write a sentence that continues the story: ")
