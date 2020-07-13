from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class informedconsent(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        return True


## Player 1

class p1_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story1(Page):
    form_model = 'player'
    form_fields = ['story_1']
    timeout_seconds = 300
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story2(Page):
    form_model = 'player'
    form_fields = ['story_2']
    timeout_seconds = 300
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story3(Page):
    form_model = 'player'
    form_fields = ['story_3']
    timeout_seconds = 300
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story4(Page):
    form_model = 'player'
    form_fields = ['story_4']
    timeout_seconds = 300
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story5(Page):
    form_model = 'player'
    form_fields = ['story_5']
    timeout_seconds = 300
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story6(Page):
    form_model = 'player'
    form_fields = ['story_6']
    timeout_seconds = 300
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story7(Page):
    form_model = 'player'
    form_fields = ['story_7']
    timeout_seconds = 300
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story8(Page):
    form_model = 'player'
    form_fields = ['story_8']
    timeout_seconds = 300
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story9(Page):
    form_model = 'player'
    form_fields = ['story_9']
    timeout_seconds = 300
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

class p2_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_story1(Page):
    form_model = 'player'
    form_fields = ['story_1']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story_p1': otherplayer.story_1}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_story2(Page):
    form_model = 'player'
    form_fields = ['story_2']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story_p1': otherplayer.story_2}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_story3(Page):
    form_model = 'player'
    form_fields = ['story_3']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story_p1': otherplayer.story_3}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_story4(Page):
    form_model = 'player'
    form_fields = ['story_4']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story_p1': otherplayer.story_4}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_story5(Page):
    form_model = 'player'
    form_fields = ['story_5']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story_p1': otherplayer.story_5}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_story6(Page):
    form_model = 'player'
    form_fields = ['story_6']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story_p1': otherplayer.story_6}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_story7(Page):
    form_model = 'player'
    form_fields = ['story_7']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story_p1': otherplayer.story_7}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_story8(Page):
    form_model = 'player'
    form_fields = ['story_8']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story_p1': otherplayer.story_8}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_story9(Page):
    form_model = 'player'
    form_fields = ['story_9']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story_p1': otherplayer.story_9}
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

class p3_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_story1(Page):
    form_model = 'player'
    form_fields = ['story_1']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story_p1': otherplayer1.story_1, 
        'story_p2': otherplayer2.story_1}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_story2(Page):
    form_model = 'player'
    form_fields = ['story_2']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story_p1': otherplayer1.story_2, 
        'story_p2': otherplayer2.story_2}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_story3(Page):
    form_model = 'player'
    form_fields = ['story_3']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story_p1': otherplayer1.story_3, 
        'story_p2': otherplayer2.story_3}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False


class p3_story4(Page):
    form_model = 'player'
    form_fields = ['story_4']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story_p1': otherplayer1.story_4, 
        'story_p2': otherplayer2.story_4}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_story5(Page):
    form_model = 'player'
    form_fields = ['story_5']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story_p1': otherplayer1.story_5, 
        'story_p2': otherplayer2.story_5}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_story6(Page):
    form_model = 'player'
    form_fields = ['story_6']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story_p1': otherplayer1.story_6, 
        'story_p2': otherplayer2.story_6}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_story7(Page):
    form_model = 'player'
    form_fields = ['story_7']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story_p1': otherplayer1.story_7, 
        'story_p2': otherplayer2.story_7}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_story8(Page):
    form_model = 'player'
    form_fields = ['story_8']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story_p1': otherplayer1.story_8, 
        'story_p2': otherplayer2.story_8}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_story9(Page):
    form_model = 'player'
    form_fields = ['story_9']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story_p1': otherplayer1.story_9, 
        'story_p2': otherplayer2.story_9}
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



class p4_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_story1(Page):
    form_model = 'player'
    form_fields = ['story_1']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story_p1': otherplayer1.story_1, 
        'story_p2': otherplayer2.story_1,
        'story_p3': otherplayer3.story_1}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_story2(Page):
    form_model = 'player'
    form_fields = ['story_2']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story_p1': otherplayer1.story_2, 
        'story_p2': otherplayer2.story_2,
        'story_p3': otherplayer3.story_2}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_story3(Page):
    form_model = 'player'
    form_fields = ['story_3']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story_p1': otherplayer1.story_3, 
        'story_p2': otherplayer2.story_3,
        'story_p3': otherplayer3.story_3}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_story4(Page):
    form_model = 'player'
    form_fields = ['story_4']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story_p1': otherplayer1.story_4, 
        'story_p2': otherplayer2.story_4,
        'story_p3': otherplayer3.story_4}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_story5(Page):
    form_model = 'player'
    form_fields = ['story_5']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story_p1': otherplayer1.story_5, 
        'story_p2': otherplayer2.story_5,
        'story_p3': otherplayer3.story_5}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_story6(Page):
    form_model = 'player'
    form_fields = ['story_6']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story_p1': otherplayer1.story_6, 
        'story_p2': otherplayer2.story_6,
        'story_p3': otherplayer3.story_6}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_story7(Page):
    form_model = 'player'
    form_fields = ['story_7']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story_p1': otherplayer1.story_7, 
        'story_p2': otherplayer2.story_7,
        'story_p3': otherplayer3.story_7}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_story8(Page):
    form_model = 'player'
    form_fields = ['story_8']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story_p1': otherplayer1.story_8, 
        'story_p2': otherplayer2.story_8,
        'story_p3': otherplayer3.story_8}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False


class p4_story9(Page):
    form_model = 'player'
    form_fields = ['story_9']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story_p1': otherplayer1.story_9, 
        'story_p2': otherplayer2.story_9,
        'story_p3': otherplayer3.story_9}
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


class p5_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_story1(Page):
    form_model = 'player'
    form_fields = ['story_1']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        return {'story_p1': otherplayer1.story_1, 
        'story_p2': otherplayer2.story_1,
        'story_p3': otherplayer3.story_1,
        'story_p4': otherplayer4.story_1}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_story2(Page):
    form_model = 'player'
    form_fields = ['story_2']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        return {'story_p1': otherplayer1.story_2, 
        'story_p2': otherplayer2.story_2,
        'story_p3': otherplayer3.story_2,
        'story_p4': otherplayer4.story_2}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False


class p5_story3(Page):
    form_model = 'player'
    form_fields = ['story_3']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        return {'story_p1': otherplayer1.story_3, 
        'story_p2': otherplayer2.story_3,
        'story_p3': otherplayer3.story_3,
        'story_p4': otherplayer4.story_3}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_story4(Page):
    form_model = 'player'
    form_fields = ['story_4']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        return {'story_p1': otherplayer1.story_4, 
        'story_p2': otherplayer2.story_4,
        'story_p3': otherplayer3.story_4,
        'story_p4': otherplayer4.story_4}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_story5(Page):
    form_model = 'player'
    form_fields = ['story_5']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        return {'story_p1': otherplayer1.story_5, 
        'story_p2': otherplayer2.story_5,
        'story_p3': otherplayer3.story_5,
        'story_p4': otherplayer4.story_5}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_story6(Page):
    form_model = 'player'
    form_fields = ['story_6']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        return {'story_p1': otherplayer1.story_6, 
        'story_p2': otherplayer2.story_6,
        'story_p3': otherplayer3.story_6,
        'story_p4': otherplayer4.story_6}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_story7(Page):
    form_model = 'player'
    form_fields = ['story_7']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        return {'story_p1': otherplayer1.story_7, 
        'story_p2': otherplayer2.story_7,
        'story_p3': otherplayer3.story_7,
        'story_p4': otherplayer4.story_7}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_story8(Page):
    form_model = 'player'
    form_fields = ['story_8']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        return {'story_p1': otherplayer1.story_8, 
        'story_p2': otherplayer2.story_8,
        'story_p3': otherplayer3.story_8,
        'story_p4': otherplayer4.story_8}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_story9(Page):
    form_model = 'player'
    form_fields = ['story_9']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        return {'story_p1': otherplayer1.story_9, 
        'story_p2': otherplayer2.story_9,
        'story_p3': otherplayer3.story_9,
        'story_p4': otherplayer4.story_9}
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


class p6_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_story1(Page):
    form_model = 'player'
    form_fields = ['story_1']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        return {'story_p1': otherplayer1.story_1, 
        'story_p2': otherplayer2.story_1,
        'story_p3': otherplayer3.story_1,
        'story_p4': otherplayer4.story_1,
        'story_p5': otherplayer5.story_1}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False



class p6_story2(Page):
    form_model = 'player'
    form_fields = ['story_2']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        return {'story_p1': otherplayer1.story_2, 
        'story_p2': otherplayer2.story_2,
        'story_p3': otherplayer3.story_2,
        'story_p4': otherplayer4.story_2,
        'story_p5': otherplayer5.story_2}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_story3(Page):
    form_model = 'player'
    form_fields = ['story_3']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        return {'story_p1': otherplayer1.story_3, 
        'story_p2': otherplayer2.story_3,
        'story_p3': otherplayer3.story_3,
        'story_p4': otherplayer4.story_3,
        'story_p5': otherplayer5.story_3}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_story4(Page):
    form_model = 'player'
    form_fields = ['story_4']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        return {'story_p1': otherplayer1.story_4, 
        'story_p2': otherplayer2.story_4,
        'story_p3': otherplayer3.story_4,
        'story_p4': otherplayer4.story_4,
        'story_p5': otherplayer5.story_4}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_story5(Page):
    form_model = 'player'
    form_fields = ['story_5']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        return {'story_p1': otherplayer1.story_5, 
        'story_p2': otherplayer2.story_5,
        'story_p3': otherplayer3.story_5,
        'story_p4': otherplayer4.story_5,
        'story_p5': otherplayer5.story_5}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_story6(Page):
    form_model = 'player'
    form_fields = ['story_6']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        return {'story_p1': otherplayer1.story_6, 
        'story_p2': otherplayer2.story_6,
        'story_p3': otherplayer3.story_6,
        'story_p4': otherplayer4.story_6,
        'story_p5': otherplayer5.story_6}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_story7(Page):
    form_model = 'player'
    form_fields = ['story_7']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        return {'story_p1': otherplayer1.story_7, 
        'story_p2': otherplayer2.story_7,
        'story_p3': otherplayer3.story_7,
        'story_p4': otherplayer4.story_7,
        'story_p5': otherplayer5.story_7}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_story8(Page):
    form_model = 'player'
    form_fields = ['story_8']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        return {'story_p1': otherplayer1.story_8, 
        'story_p2': otherplayer2.story_8,
        'story_p3': otherplayer3.story_8,
        'story_p4': otherplayer4.story_8,
        'story_p5': otherplayer5.story_8}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_story9(Page):
    form_model = 'player'
    form_fields = ['story_9']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        return {'story_p1': otherplayer1.story_9, 
        'story_p2': otherplayer2.story_9,
        'story_p3': otherplayer3.story_9,
        'story_p4': otherplayer4.story_9,
        'story_p5': otherplayer5.story_9}
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

class p7_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_story1(Page):
    form_model = 'player'
    form_fields = ['story_1']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        return {'story_p1': otherplayer1.story_1, 
        'story_p2': otherplayer2.story_1,
        'story_p3': otherplayer3.story_1,
        'story_p4': otherplayer4.story_1,
        'story_p5': otherplayer5.story_1,
        'story_p6': otherplayer6.story_1}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_story2(Page):
    form_model = 'player'
    form_fields = ['story_2']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        return {'story_p1': otherplayer1.story_2, 
        'story_p2': otherplayer2.story_2,
        'story_p3': otherplayer3.story_2,
        'story_p4': otherplayer4.story_2,
        'story_p5': otherplayer5.story_2,
        'story_p6': otherplayer6.story_2}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_story3(Page):
    form_model = 'player'
    form_fields = ['story_3']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        return {'story_p1': otherplayer1.story_3, 
        'story_p2': otherplayer2.story_3,
        'story_p3': otherplayer3.story_3,
        'story_p4': otherplayer4.story_3,
        'story_p5': otherplayer5.story_3,
        'story_p6': otherplayer6.story_3}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_story4(Page):
    form_model = 'player'
    form_fields = ['story_4']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        return {'story_p1': otherplayer1.story_4, 
        'story_p2': otherplayer2.story_4,
        'story_p3': otherplayer3.story_4,
        'story_p4': otherplayer4.story_4,
        'story_p5': otherplayer5.story_4,
        'story_p6': otherplayer6.story_4}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_story5(Page):
    form_model = 'player'
    form_fields = ['story_5']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        return {'story_p1': otherplayer1.story_5, 
        'story_p2': otherplayer2.story_5,
        'story_p3': otherplayer3.story_5,
        'story_p4': otherplayer4.story_5,
        'story_p5': otherplayer5.story_5,
        'story_p6': otherplayer6.story_5}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_story6(Page):
    form_model = 'player'
    form_fields = ['story_6']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        return {'story_p1': otherplayer1.story_6, 
        'story_p2': otherplayer2.story_6,
        'story_p3': otherplayer3.story_6,
        'story_p4': otherplayer4.story_6,
        'story_p5': otherplayer5.story_6,
        'story_p6': otherplayer6.story_6}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_story7(Page):
    form_model = 'player'
    form_fields = ['story_7']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        return {'story_p1': otherplayer1.story_7, 
        'story_p2': otherplayer2.story_7,
        'story_p3': otherplayer3.story_7,
        'story_p4': otherplayer4.story_7,
        'story_p5': otherplayer5.story_7,
        'story_p6': otherplayer6.story_7}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_story8(Page):
    form_model = 'player'
    form_fields = ['story_8']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        return {'story_p1': otherplayer1.story_8, 
        'story_p2': otherplayer2.story_8,
        'story_p3': otherplayer3.story_8,
        'story_p4': otherplayer4.story_8,
        'story_p5': otherplayer5.story_8,
        'story_p6': otherplayer6.story_8}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_story9(Page):
    form_model = 'player'
    form_fields = ['story_9']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        return {'story_p1': otherplayer1.story_9, 
        'story_p2': otherplayer2.story_9,
        'story_p3': otherplayer3.story_9,
        'story_p4': otherplayer4.story_9,
        'story_p5': otherplayer5.story_9,
        'story_p6': otherplayer6.story_9}
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
      

class p8_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_story1(Page):
    form_model = 'player'
    form_fields = ['story_1']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        return {'story_p1': otherplayer1.story_1, 
        'story_p2': otherplayer2.story_1,
        'story_p3': otherplayer3.story_1,
        'story_p4': otherplayer4.story_1,
        'story_p5': otherplayer5.story_1,
        'story_p6': otherplayer6.story_1,
        'story_p7': otherplayer7.story_1}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_story2(Page):
    form_model = 'player'
    form_fields = ['story_2']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        return {'story_p1': otherplayer1.story_2, 
        'story_p2': otherplayer2.story_2,
        'story_p3': otherplayer3.story_2,
        'story_p4': otherplayer4.story_2,
        'story_p5': otherplayer5.story_2,
        'story_p6': otherplayer6.story_2,
        'story_p7': otherplayer7.story_2}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_story3(Page):
    form_model = 'player'
    form_fields = ['story_3']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        return {'story_p1': otherplayer1.story_3, 
        'story_p2': otherplayer2.story_3,
        'story_p3': otherplayer3.story_3,
        'story_p4': otherplayer4.story_3,
        'story_p5': otherplayer5.story_3,
        'story_p6': otherplayer6.story_3,
        'story_p7': otherplayer7.story_3}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_story4(Page):
    form_model = 'player'
    form_fields = ['story_4']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        return {'story_p1': otherplayer1.story_4, 
        'story_p2': otherplayer2.story_4,
        'story_p3': otherplayer3.story_4,
        'story_p4': otherplayer4.story_4,
        'story_p5': otherplayer5.story_4,
        'story_p6': otherplayer6.story_4,
        'story_p7': otherplayer7.story_4}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_story5(Page):
    form_model = 'player'
    form_fields = ['story_5']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        return {'story_p1': otherplayer1.story_5, 
        'story_p2': otherplayer2.story_5,
        'story_p3': otherplayer3.story_5,
        'story_p4': otherplayer4.story_5,
        'story_p5': otherplayer5.story_5,
        'story_p6': otherplayer6.story_5,
        'story_p7': otherplayer7.story_5}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_story6(Page):
    form_model = 'player'
    form_fields = ['story_6']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        return {'story_p1': otherplayer1.story_6, 
        'story_p2': otherplayer2.story_6,
        'story_p3': otherplayer3.story_6,
        'story_p4': otherplayer4.story_6,
        'story_p5': otherplayer5.story_6,
        'story_p6': otherplayer6.story_6,
        'story_p7': otherplayer7.story_6}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_story7(Page):
    form_model = 'player'
    form_fields = ['story_7']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        return {'story_p1': otherplayer1.story_7, 
        'story_p2': otherplayer2.story_7,
        'story_p3': otherplayer3.story_7,
        'story_p4': otherplayer4.story_7,
        'story_p5': otherplayer5.story_7,
        'story_p6': otherplayer6.story_7,
        'story_p7': otherplayer7.story_7}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_story8(Page):
    form_model = 'player'
    form_fields = ['story_8']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        return {'story_p1': otherplayer1.story_8, 
        'story_p2': otherplayer2.story_8,
        'story_p3': otherplayer3.story_8,
        'story_p4': otherplayer4.story_8,
        'story_p5': otherplayer5.story_8,
        'story_p6': otherplayer6.story_8,
        'story_p7': otherplayer7.story_8}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_story9(Page):
    form_model = 'player'
    form_fields = ['story_9']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        return {'story_p1': otherplayer1.story_9, 
        'story_p2': otherplayer2.story_9,
        'story_p3': otherplayer3.story_9,
        'story_p4': otherplayer4.story_9,
        'story_p5': otherplayer5.story_9,
        'story_p6': otherplayer6.story_9,
        'story_p7': otherplayer7.story_9}
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

class p9_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_story1(Page):
    form_model = 'player'
    form_fields = ['story_1']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        otherplayer8 = self.group.get_player_by_id(8)
        return {'story_p1': otherplayer1.story_1, 
        'story_p2': otherplayer2.story_1,
        'story_p3': otherplayer3.story_1,
        'story_p4': otherplayer4.story_1,
        'story_p5': otherplayer5.story_1,
        'story_p6': otherplayer6.story_1,
        'story_p7': otherplayer7.story_1,
        'story_p8': otherplayer8.story_1}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_story2(Page):
    form_model = 'player'
    form_fields = ['story_2']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        otherplayer8 = self.group.get_player_by_id(8)
        return {'story_p1': otherplayer1.story_2, 
        'story_p2': otherplayer2.story_2,
        'story_p3': otherplayer3.story_2,
        'story_p4': otherplayer4.story_2,
        'story_p5': otherplayer5.story_2,
        'story_p6': otherplayer6.story_2,
        'story_p7': otherplayer7.story_2,
        'story_p8': otherplayer8.story_2}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_story3(Page):
    form_model = 'player'
    form_fields = ['story_3']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        otherplayer8 = self.group.get_player_by_id(8)
        return {'story_p1': otherplayer1.story_3, 
        'story_p2': otherplayer2.story_3,
        'story_p3': otherplayer3.story_3,
        'story_p4': otherplayer4.story_3,
        'story_p5': otherplayer5.story_3,
        'story_p6': otherplayer6.story_3,
        'story_p7': otherplayer7.story_3,
        'story_p8': otherplayer8.story_3}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_story4(Page):
    form_model = 'player'
    form_fields = ['story_4']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        otherplayer8 = self.group.get_player_by_id(8)
        return {'story_p1': otherplayer1.story_4, 
        'story_p2': otherplayer2.story_4,
        'story_p3': otherplayer3.story_4,
        'story_p4': otherplayer4.story_4,
        'story_p5': otherplayer5.story_4,
        'story_p6': otherplayer6.story_4,
        'story_p7': otherplayer7.story_4,
        'story_p8': otherplayer8.story_4}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_story5(Page):
    form_model = 'player'
    form_fields = ['story_5']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        otherplayer8 = self.group.get_player_by_id(8)
        return {'story_p1': otherplayer1.story_5, 
        'story_p2': otherplayer2.story_5,
        'story_p3': otherplayer3.story_5,
        'story_p4': otherplayer4.story_5,
        'story_p5': otherplayer5.story_5,
        'story_p6': otherplayer6.story_5,
        'story_p7': otherplayer7.story_5,
        'story_p8': otherplayer8.story_5}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_story6(Page):
    form_model = 'player'
    form_fields = ['story_6']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        otherplayer8 = self.group.get_player_by_id(8)
        return {'story_p1': otherplayer1.story_6, 
        'story_p2': otherplayer2.story_6,
        'story_p3': otherplayer3.story_6,
        'story_p4': otherplayer4.story_6,
        'story_p5': otherplayer5.story_6,
        'story_p6': otherplayer6.story_6,
        'story_p7': otherplayer7.story_6,
        'story_p8': otherplayer8.story_6}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_story7(Page):
    form_model = 'player'
    form_fields = ['story_7']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        otherplayer8 = self.group.get_player_by_id(8)
        return {'story_p1': otherplayer1.story_7, 
        'story_p2': otherplayer2.story_7,
        'story_p3': otherplayer3.story_7,
        'story_p4': otherplayer4.story_7,
        'story_p5': otherplayer5.story_7,
        'story_p6': otherplayer6.story_7,
        'story_p7': otherplayer7.story_7,
        'story_p8': otherplayer8.story_7}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_story8(Page):
    form_model = 'player'
    form_fields = ['story_8']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        otherplayer8 = self.group.get_player_by_id(8)
        return {'story_p1': otherplayer1.story_8, 
        'story_p2': otherplayer2.story_8,
        'story_p3': otherplayer3.story_8,
        'story_p4': otherplayer4.story_8,
        'story_p5': otherplayer5.story_8,
        'story_p6': otherplayer6.story_8,
        'story_p7': otherplayer7.story_8,
        'story_p8': otherplayer8.story_8}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_story9(Page):
    form_model = 'player'
    form_fields = ['story_9']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4)
        otherplayer5 = self.group.get_player_by_id(5)
        otherplayer6 = self.group.get_player_by_id(6)
        otherplayer7 = self.group.get_player_by_id(7)
        otherplayer8 = self.group.get_player_by_id(8)
        return {'story_p1': otherplayer1.story_9, 
        'story_p2': otherplayer2.story_9,
        'story_p3': otherplayer3.story_9,
        'story_p4': otherplayer4.story_9,
        'story_p5': otherplayer5.story_9,
        'story_p6': otherplayer6.story_9,
        'story_p7': otherplayer7.story_9,
        'story_p8': otherplayer8.story_9}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False


page_sequence = [


# Player 1 
    #sentences
    p1_story_inst,
    p1_story1,
    p1_story2,
    p1_story3,
    p1_story4,
    p1_story5,
    p1_story6,
    p1_story7,
    p1_story8,
    p1_story9,

# Player 2
    p2_wait,
    p2_story_inst,
    p2_story1,
    p2_story2,
    p2_story3,
    p2_story4,
    p2_story5,
    p2_story6,
    p2_story7,
    p2_story8,
    p2_story9,

# Player 3
    p3_wait,
    p3_story_inst,
    p3_story1,
    p3_story2,
    p3_story3,
    p3_story4,
    p3_story5,
    p3_story6,
    p3_story7,
    p3_story8,
    p3_story9,

    # Player 4
    p4_wait,
    p4_story_inst,
    p4_story1,
    p4_story2,
    p4_story3,
    p4_story4,
    p4_story5,
    p4_story6,
    p4_story7,
    p4_story8,
    p4_story9,

    # Player 5
    p5_wait,
    p5_story_inst,
    p5_story1,
    p5_story2,
    p5_story3,
    p5_story4,
    p5_story5,
    p5_story6,
    p5_story7,
    p5_story8,
    p5_story9,

    # Player 6
    p6_wait,
    p6_story_inst,
    p6_story1,
    p6_story2,
    p6_story3,
    p6_story4,
    p6_story5,
    p6_story6,
    p6_story7,
    p6_story8,
    p6_story9,

    # Player 7
    p7_wait,
    p7_story_inst,
    p7_story1,
    p7_story2,
    p7_story3,
    p7_story4,
    p7_story5,
    p7_story6,
    p7_story7,
    p7_story8,
    p7_story9,

    # Player 8
    p8_wait,
    p8_story_inst,
    p8_story1,
    p8_story2,
    p8_story3,
    p8_story4,
    p8_story5,
    p8_story6,
    p8_story7,
    p8_story8,
    p8_story9,

    # Player 9
    p9_wait,
    p9_story_inst,
    p9_story1,
    p9_story2,
    p9_story3,
    p9_story4,
    p9_story5,
    p9_story6,
    p9_story7,
    p9_story8,
    p9_story9,

]
