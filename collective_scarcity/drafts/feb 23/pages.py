from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# Introduction
class intro_all(Page):
    form_model = 'player'


##############################################################
# Demographics
class demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income']


##############################################################
# Treatment 1
class t1_stage1(Page):
    form_model = 'player'
    form_fields = ['t1_stage1']
    def is_displayed(self):
        value =  self.player.treatment in ('A','B','C','D')
        return value

class t1_stage2(Page):
    form_model = 'player'
    form_fields = ['t1_stage2']
    def is_displayed(self):
        value =  self.player.treatment in ('A','B','C','D')
        return value

class t1_stage3_description(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('A','B','C','D')
        return value

class t1_stage3_dv1(Page):
    form_model = 'player'
    form_fields = ['t1_stage3_dv1']
    timeout_seconds = 180
    def is_displayed(self):
        value =  self.player.treatment in ('A','C')
        return value

class t1_stage3_dv2(Page):
    form_model = 'player'
    form_fields = ['t1_stage3_dv2']
    timeout_seconds = 900
    def is_displayed(self):
        value =  self.player.treatment in ('B','D')
        return value

class t1_stage4(Page):
    form_model = 'player'
    form_fields = ['t1_stage4']
    def is_displayed(self):
        value =  self.player.treatment in ('A','B','C','D')
        return value

class t1_stage5(Page):
    form_model = 'player'
    form_fields = ['t1_stage5']
    def is_displayed(self):
        value =  self.player.treatment in ('A','B','C','D')
        return value

class t1_stage6_description(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('A','B','C','D')
        return value

class t1_stage6_dv2(Page):
    form_model = 'player'
    form_fields = ['t1_stage6_dv2']
    timeout_seconds = 900
    def is_displayed(self):
        value =  self.player.treatment in ('A','C')
        return value

class t1_stage6_dv1(Page):
    form_model = 'player'
    form_fields = ['t1_stage6_dv1']
    timeout_seconds = 180
    def is_displayed(self):
        value =  self.player.treatment in ('B','D')
        return value


##############################################################
# Treatment 2
class t2_stage1(Page):
    form_model = 'player'
    form_fields = ['t2_stage1']
    def is_displayed(self):
        value = self.player.treatment in ('E','F','G','H')
        return value

class t2_stage1_detail(Page):
    form_model = 'player'
    form_fields = ['t2_stage1_detail']
    def is_displayed(self):
        value = self.player.treatment in ('E','F','G','H')
        return value

class t2_stage2_description(Page):
    form_model = 'player'
    def is_displayed(self):
        value = self.player.treatment in ('E','F','G','H')
        return value

class t2_stage2_dv1(Page):
    form_model = 'player'
    form_fields = ['t2_stage2_dv1']
    timeout_seconds = 180
    def is_displayed(self):
        value = self.player.treatment in ('E','G')
        return value

class t2_stage2_dv2(Page):
    form_model = 'player'
    form_fields = ['t2_stage2_dv2']
    timeout_seconds = 900
    def is_displayed(self):
        value = self.player.treatment in ('F','H')
        return value

class t2_stage3_description(Page):
    form_model = 'player'
    def is_displayed(self):
        value = self.player.treatment in ('E','F','G','H')
        return value

class t2_stage3_dv2(Page):
    form_model = 'player'
    form_fields = ['t2_stage3_dv2']
    timeout_seconds = 900
    def is_displayed(self):
        value = self.player.treatment in ('E','G')
        return value

class t2_stage3_dv1(Page):
    form_model = 'player'
    form_fields = ['t2_stage3_dv1']
    timeout_seconds = 180
    def is_displayed(self):
        value = self.player.treatment in ('F','H')
        return value


##############################################################
# Treatment 3
class t3_instructions(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q1(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q1_choice(Page):
    form_model = 'player'
    form_fields = ['q1_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q1_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q2(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q2_choice(Page):
    form_model = 'player'
    form_fields = ['q2_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q2_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q3(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q3_choice(Page):
    form_model = 'player'
    form_fields = ['q3_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q3_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q4(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q4_choice(Page):
    form_model = 'player'
    form_fields = ['q4_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q4_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q5(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q5_choice(Page):
    form_model = 'player'
    form_fields = ['q5_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q5_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q6(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q6_choice(Page):
    form_model = 'player'
    form_fields = ['q6_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q6_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q7(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q7_choice(Page):
    form_model = 'player'
    form_fields = ['q7_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q7_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q8(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q8_choice(Page):
    form_model = 'player'
    form_fields = ['q8_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q8_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q9(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q9_choice(Page):
    form_model = 'player'
    form_fields = ['q9_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q9_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q10(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q10_choice(Page):
    form_model = 'player'
    form_fields = ['q10_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q10_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q11(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q11_choice(Page):
    form_model = 'player'
    form_fields = ['q11_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q11_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q12(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q12_choice(Page):
    form_model = 'player'
    form_fields = ['q12_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q12_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q13(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q13_choice(Page):
    form_model = 'player'
    form_fields = ['q13_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q13_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q14(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q14_choice(Page):
    form_model = 'player'
    form_fields = ['q14_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q14_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q15(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q15_choice(Page):
    form_model = 'player'
    form_fields = ['q15_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q15_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q16(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q16_choice(Page):
    form_model = 'player'
    form_fields = ['q16_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q16_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q17(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q17_choice(Page):
    form_model = 'player'
    form_fields = ['q17_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q17_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q18(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q18_choice(Page):
    form_model = 'player'
    form_fields = ['q18_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q18_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q19(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q19_choice(Page):
    form_model = 'player'
    form_fields = ['q19_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q19_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q20(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q20_choice(Page):
    form_model = 'player'
    form_fields = ['q20_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q20_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q21(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q21_choice(Page):
    form_model = 'player'
    form_fields = ['q21_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q21_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q22(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q22_choice(Page):
    form_model = 'player'
    form_fields = ['q22_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q22_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q23(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q23_choice(Page):
    form_model = 'player'
    form_fields = ['q23_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q23_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q24(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q24_choice(Page):
    form_model = 'player'
    form_fields = ['q24_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q24_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q25(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q25_choice(Page):
    form_model = 'player'
    form_fields = ['q25_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q25_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q26(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q26_choice(Page):
    form_model = 'player'
    form_fields = ['q26_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q26_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q27(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q27_choice(Page):
    form_model = 'player'
    form_fields = ['q27_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q27_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q28(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q28_choice(Page):
    form_model = 'player'
    form_fields = ['q28_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q28_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q29(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q29_choice(Page):
    form_model = 'player'
    form_fields = ['q29_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q29_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q30(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 5
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q30_choice(Page):
    form_model = 'player'
    form_fields = ['q30_stars']
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_q30_answer(Page):
    form_model = 'player'
    def is_displayed(self):
        value =  self.player.treatment in ('I','J','K','L')
        return value

class t3_stage2_description(Page):
    form_model = 'player'
    def is_displayed(self):
        value = self.player.treatment in ('I','J','K','L')
        return value

class t3_stage2_dv1(Page):
    form_model = 'player'
    form_fields = ['t3_stage2_dv1']
    timeout_seconds = 180
    def is_displayed(self):
        value = self.player.treatment in ('I','K')
        return value

class t3_stage2_dv2(Page):
    form_model = 'player'
    form_fields = ['t3_stage2_dv2']
    timeout_seconds = 900
    def is_displayed(self):
        value = self.player.treatment in ('J','L')
        return value

class t3_stage3_description(Page):
    form_model = 'player'
    def is_displayed(self):
        value = self.player.treatment in ('I','J','K','L')
        return value

class t3_stage3_dv2(Page):
    form_model = 'player'
    form_fields = ['t3_stage3_dv2']
    timeout_seconds = 900
    def is_displayed(self):
        value = self.player.treatment in ('I','K')
        return value

class t3_stage3_dv1(Page):
    form_model = 'player'
    form_fields = ['t3_stage3_dv1']
    timeout_seconds = 180
    def is_displayed(self):
        value = self.player.treatment in ('J','L')
        return value




##############################################################
# Post-survey
class scarcity(Page):
    form_model = 'player'
    form_fields = ['resources','enough','protect','more']

class cognitive(Page):
    form_model = 'player'
    form_fields = ['bat','machines','lake']

class affect(Page):
    form_model = 'player'
    form_fields = ['interested', 'distressed','excited','upset',
    'strong','guilty','scared','hostile','enthusiastic',
    'irritable','alert','ashamed','inspired','nervous',
    'determined','attentive','jittery','active','afraid']


##############################################################
# End
class ending(Page):
    form_model = 'player'


##############################################################
class ResultsWaitPage(WaitPage):
    pass



class Results(Page):
    pass

page_sequence = [
# All Treatments
    intro_all,
    demographics,

# Treatment 1
    t1_stage1,
    t1_stage2,
    t1_stage3_description,
    t1_stage3_dv1,
    t1_stage3_dv2,
    t1_stage4,
    t1_stage5,
    t1_stage6_description,
    t1_stage6_dv1,
    t1_stage6_dv2,

# Treatment 2
    t2_stage1,
    t2_stage1_detail,
    t2_stage2_description,
    t2_stage2_dv1,
    t2_stage2_dv2,
    t2_stage3_description,
    t2_stage3_dv2,
    t2_stage3_dv1,

# Treatment 3
    t3_instructions,
    t3_q1,
    t3_q1_choice,
    t3_q1_answer,
    t3_q2,
    t3_q2_choice,
    t3_q2_answer,
    t3_q3,
    t3_q3_choice,
    t3_q3_answer, 
    t3_q4,
    t3_q4_choice,
    t3_q4_answer, 
    t3_q5,
    t3_q5_choice,
    t3_q5_answer, 
    t3_q6,
    t3_q6_choice,
    t3_q6_answer, 
    t3_q7,
    t3_q7_choice,
    t3_q7_answer, 
    t3_q8,
    t3_q8_choice,
    t3_q8_answer, 
    t3_q9,
    t3_q9_choice,
    t3_q9_answer, 
    t3_q10,
    t3_q10_choice,
    t3_q10_answer,
    t3_q11,
    t3_q11_choice,
    t3_q11_answer, 
    t3_q12,
    t3_q12_choice,
    t3_q12_answer,
    t3_q13,
    t3_q13_choice,
    t3_q13_answer, 
    t3_q14,
    t3_q14_choice,
    t3_q14_answer, 
    t3_q15,
    t3_q15_choice,
    t3_q15_answer, 
    t3_q16,
    t3_q16_choice,
    t3_q16_answer, 
    t3_q17,
    t3_q17_choice,
    t3_q17_answer, 
    t3_q18,
    t3_q18_choice,
    t3_q18_answer, 
    t3_q19,
    t3_q19_choice,
    t3_q19_answer, 
    t3_q20,
    t3_q20_choice,
    t3_q20_answer, 
    t3_q21,
    t3_q21_choice,
    t3_q21_answer, 
    t3_q22,
    t3_q22_choice,
    t3_q22_answer, 
    t3_q23,
    t3_q23_choice,
    t3_q23_answer, 
    t3_q24,
    t3_q24_choice,
    t3_q24_answer, 
    t3_q25,
    t3_q25_choice,
    t3_q25_answer, 
    t3_q26,
    t3_q26_choice,
    t3_q26_answer, 
    t3_q27,
    t3_q27_choice,
    t3_q27_answer, 
    t3_q28,
    t3_q28_choice,
    t3_q28_answer, 
    t3_q29,
    t3_q29_choice,
    t3_q29_answer, 
    t3_q30,
    t3_q30_choice,
    t3_q30_answer, 
    t3_stage2_description,
    t3_stage2_dv1,
    t3_stage2_dv2,
    t3_stage3_description,
    t3_stage3_dv2,
    t3_stage3_dv1,

# Post Survey
    scarcity,
    affect,
    cognitive,

# Common to all
    ending
]
