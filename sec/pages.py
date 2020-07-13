from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class informedconsent(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        return True


## Player 1

# sentences stories
class p1_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s1(Page):
    form_model = 'player'
    form_fields = ['p1_s1']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s2(Page):
    form_model = 'player'
    form_fields = ['p1_s2']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s3(Page):
    form_model = 'player'
    form_fields = ['p1_s3']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s4(Page):
    form_model = 'player'
    form_fields = ['p1_s4']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s5(Page):
    form_model = 'player'
    form_fields = ['p1_s5']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s6(Page):
    form_model = 'player'
    form_fields = ['p1_s6']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s7(Page):
    form_model = 'player'
    form_fields = ['p1_s7']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s8(Page):
    form_model = 'player'
    form_fields = ['p1_s8']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s9(Page):
    form_model = 'player'
    form_fields = ['p1_s9']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

## Player 2
class p2_wait(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_s1(Page):
    form_model = 'player'
    form_fields = ['p1_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story1': otherplayer.p1_s1}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_s2(Page):
    form_model = 'player'
    form_fields = ['p1_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story2': otherplayer.p1_s2}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_s3(Page):
    form_model = 'player'
    form_fields = ['p1_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story3': otherplayer.p1_s3}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_s4(Page):
    form_model = 'player'
    form_fields = ['p1_s4']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story': otherplayer.p1_s4}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_s5(Page):
    form_model = 'player'
    form_fields = ['p1_s5']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story': otherplayer.p1_s5}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_s6(Page):
    form_model = 'player'
    form_fields = ['p1_s6']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story': otherplayer.p1_s6}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_s7(Page):
    form_model = 'player'
    form_fields = ['p1_s7']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story': otherplayer.p1_s7}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_s8(Page):
    form_model = 'player'
    form_fields = ['p1_s8']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story': otherplayer.p1_s8}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False   

class p2_s9(Page):
    form_model = 'player'
    form_fields = ['p1_s9']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story': otherplayer.p1_s9}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False            

## Player 3
class p3_wait(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_s1(Page):
    form_model = 'player'
    form_fields = ['p1_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story1': otherplayer.p1_s1}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_s2(Page):
    form_model = 'player'
    form_fields = ['p1_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story2': otherplayer.p1_s2}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False


class p3_s3(Page):
    form_model = 'player'
    form_fields = ['p1_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story3': otherplayer.p1_s3}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False


class p3_s4(Page):
    form_model = 'player'
    form_fields = ['p1_s4']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story': otherplayer.p1_s4}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_s5(Page):
    form_model = 'player'
    form_fields = ['p1_s5']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story': otherplayer.p1_s5}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_s6(Page):
    form_model = 'player'
    form_fields = ['p1_s6']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story': otherplayer.p1_s6}
    def is_displayed(self):
        if self.player.id_in_group ==3:
            return True
        else:
            return False

class p3_s7(Page):
    form_model = 'player'
    form_fields = ['p1_s7']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story': otherplayer.p1_s7}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_s8(Page):
    form_model = 'player'
    form_fields = ['p1_s8']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story': otherplayer.p1_s8}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False   

class p3_s9(Page):
    form_model = 'player'
    form_fields = ['p1_s9']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story': otherplayer.p1_s9}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False        

## Player 4
class p4_wait(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False
class p4_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

# Sentences
class p4_s1(Page):
    form_model = 'player'
    form_fields = ['p1_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story1': otherplayer.p1_s1}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_s2(Page):
    form_model = 'player'
    form_fields = ['p1_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story2': otherplayer.p1_s2}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_s3(Page):
    form_model = 'player'
    form_fields = ['p1_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story3': otherplayer.p1_s3}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False




class p4_s4(Page):
    form_model = 'player'
    form_fields = ['p1_s4']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story': otherplayer.p1_s4}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_s5(Page):
    form_model = 'player'
    form_fields = ['p1_s5']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story': otherplayer.p1_s5}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_s6(Page):
    form_model = 'player'
    form_fields = ['p1_s6']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story': otherplayer.p1_s6}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_s7(Page):
    form_model = 'player'
    form_fields = ['p1_s7']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story': otherplayer.p1_s7}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_s8(Page):
    form_model = 'player'
    form_fields = ['p1_s8']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story': otherplayer.p1_s8}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False   

class p4_s9(Page):
    form_model = 'player'
    form_fields = ['p1_s9']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story': otherplayer.p1_s9}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False        



## Player 5
class p5_wait(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

# Sentences
class p5_s1(Page):
    form_model = 'player'
    form_fields = ['p1_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story1': otherplayer.p1_s1}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_s2(Page):
    form_model = 'player'
    form_fields = ['p1_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story2': otherplayer.p1_s2}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_s3(Page):
    form_model = 'player'
    form_fields = ['p1_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story3': otherplayer.p1_s3}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_s4(Page):
    form_model = 'player'
    form_fields = ['p1_s4']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story': otherplayer.p1_s4}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_s5(Page):
    form_model = 'player'
    form_fields = ['p1_s5']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story': otherplayer.p1_s5}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_s6(Page):
    form_model = 'player'
    form_fields = ['p1_s6']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story': otherplayer.p1_s6}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_s7(Page):
    form_model = 'player'
    form_fields = ['p1_s7']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story': otherplayer.p1_s7}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_s8(Page):
    form_model = 'player'
    form_fields = ['p1_s8']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story': otherplayer.p1_s8}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False   

class p5_s9(Page):
    form_model = 'player'
    form_fields = ['p1_s9']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story': otherplayer.p1_s9}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False        




## Player 6
class p6_wait(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

# Sentences
class p6_s1(Page):
    form_model = 'player'
    form_fields = ['p1_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story1': otherplayer.p1_s1}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_s2(Page):
    form_model = 'player'
    form_fields = ['p1_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story2': otherplayer.p1_s2}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_s3(Page):
    form_model = 'player'
    form_fields = ['p1_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story3': otherplayer.p1_s3}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False


class p6_s4(Page):
    form_model = 'player'
    form_fields = ['p1_s4']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story': otherplayer.p1_s4}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_s5(Page):
    form_model = 'player'
    form_fields = ['p1_s5']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story': otherplayer.p1_s5}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_s6(Page):
    form_model = 'player'
    form_fields = ['p1_s6']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story': otherplayer.p1_s6}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_s7(Page):
    form_model = 'player'
    form_fields = ['p1_s7']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story': otherplayer.p1_s7}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_s8(Page):
    form_model = 'player'
    form_fields = ['p1_s8']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story': otherplayer.p1_s8}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False   

class p6_s9(Page):
    form_model = 'player'
    form_fields = ['p1_s9']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story': otherplayer.p1_s9}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False        





## Player 7
class p7_wait(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

# Sentences
class p7_s1(Page):
    form_model = 'player'
    form_fields = ['p1_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story1': otherplayer.p1_s1}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_s2(Page):
    form_model = 'player'
    form_fields = ['p1_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story2': otherplayer.p1_s2}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_s3(Page):
    form_model = 'player'
    form_fields = ['p1_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story3': otherplayer.p1_s3}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False


class p7_s4(Page):
    form_model = 'player'
    form_fields = ['p1_s4']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story': otherplayer.p1_s4}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_s5(Page):
    form_model = 'player'
    form_fields = ['p1_s5']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story': otherplayer.p1_s5}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_s6(Page):
    form_model = 'player'
    form_fields = ['p1_s6']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story': otherplayer.p1_s6}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_s7(Page):
    form_model = 'player'
    form_fields = ['p1_s7']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story': otherplayer.p1_s7}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_s8(Page):
    form_model = 'player'
    form_fields = ['p1_s8']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story': otherplayer.p1_s8}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False   

class p7_s9(Page):
    form_model = 'player'
    form_fields = ['p1_s9']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story': otherplayer.p1_s9}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False  


## Player 8
class p8_wait(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False
# Sentences
class p8_s1(Page):
    form_model = 'player'
    form_fields = ['p1_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story1': otherplayer.p1_s1}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_s2(Page):
    form_model = 'player'
    form_fields = ['p1_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story2': otherplayer.p1_s2}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_s3(Page):
    form_model = 'player'
    form_fields = ['p1_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story3': otherplayer.p1_s3}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False


class p8_s4(Page):
    form_model = 'player'
    form_fields = ['p1_s4']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story': otherplayer.p1_s4}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_s5(Page):
    form_model = 'player'
    form_fields = ['p1_s5']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story': otherplayer.p1_s5}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_s6(Page):
    form_model = 'player'
    form_fields = ['p1_s6']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story': otherplayer.p1_s6}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_s7(Page):
    form_model = 'player'
    form_fields = ['p1_s7']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story': otherplayer.p1_s7}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_s8(Page):
    form_model = 'player'
    form_fields = ['p1_s8']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story': otherplayer.p1_s8}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False   

class p8_s9(Page):
    form_model = 'player'
    form_fields = ['p1_s9']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story': otherplayer.p1_s9}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False  

class p8_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

## Player 9
class p9_wait(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

# Sentences
class p9_s1(Page):
    form_model = 'player'
    form_fields = ['p1_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story1': otherplayer.p1_s1}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_s2(Page):
    form_model = 'player'
    form_fields = ['p1_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story2': otherplayer.p1_s2}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_s3(Page):
    form_model = 'player'
    form_fields = ['p1_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story3': otherplayer.p1_s3}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_s4(Page):
    form_model = 'player'
    form_fields = ['p1_s4']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story': otherplayer.p1_s4}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_s5(Page):
    form_model = 'player'
    form_fields = ['p1_s5']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story': otherplayer.p1_s5}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_s6(Page):
    form_model = 'player'
    form_fields = ['p1_s6']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story': otherplayer.p1_s6}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_s7(Page):
    form_model = 'player'
    form_fields = ['p1_s7']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story': otherplayer.p1_s7}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_s8(Page):
    form_model = 'player'
    form_fields = ['p1_s8']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story': otherplayer.p1_s8}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False   

class p9_s9(Page):
    form_model = 'player'
    form_fields = ['p1_s9']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story': otherplayer.p1_s9}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False  

class p9_sentences_instructions(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

page_sequence = [

# Player 1 
 
    #sentences
    p1_sentences_instructions,
    p1_s1,
    p1_s2,
    p1_s3,
    p1_s4,
    p1_s5,
    p1_s6,
    p1_s7,
    p1_s8,
    p1_s9,


# Player 2
    p2_wait,


    #sentences
    p2_sentences_instructions,
    p2_s1,
    p2_s2,
    p2_s3,
    p2_s4,
    p2_s5,
    p2_s6,
    p2_s7,
    p2_s8,
    p2_s9,



# Player 3
    p3_wait,
    #sentences
    p3_sentences_instructions,
    p3_s1,
    p3_s2,
    p3_s3,
    p3_s4,
    p3_s5,
    p3_s6,
    p3_s7,
    p3_s8,
    p3_s9,

    # Player 4
    p4_wait,

    #sentences
    p4_sentences_instructions,
    p4_s1,
    p4_s2,
    p4_s3,
    p4_s4,
    p4_s5,
    p4_s6,
    p4_s7,
    p4_s8,
    p4_s9,

    # Player 5
    p5_wait,

    #sentences
    p5_sentences_instructions,
    p5_s1,
    p5_s2,
    p5_s3,
    p5_s4,
    p5_s5,
    p5_s6,
    p5_s7,
    p5_s8,
    p5_s9,

    # Player 6
    p6_wait,

    #sentences
    p6_sentences_instructions,
    p6_s1,
    p6_s2,
    p6_s3,
    p6_s4,
    p6_s5,
    p6_s6,
    p6_s7,
    p6_s8,
    p6_s9,

    # Player 7
    p7_wait,

    #sentences
    p7_s1,
    p7_s2,
    p7_s3,
    p7_s4,
    p7_s5,
    p7_s6,
    p7_s7,
    p7_s8,
    p7_s9,

    # Player 8
    p8_wait,
    p8_sentences_instructions,
  

    #sentences
    p8_s1,
    p8_s2,
    p8_s3,
    p8_s4,
    p8_s5,
    p8_s6,
    p8_s7,
    p8_s8,
    p8_s9,

    # Player 9
    p9_wait,
    p9_sentences_instructions,

    #sentences
    p9_s1,
    p9_s2,
    p9_s3,
    p9_s4,
    p9_s5,
    p9_s6,
    p9_s7,
    p9_s8,
    p9_s9,

]
