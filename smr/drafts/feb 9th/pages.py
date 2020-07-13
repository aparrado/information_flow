from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

## Player 1
class p1_sent_explain(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_a_read(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class wait_1(Page):
    form_model = 'player'
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_a_write(Page):
    form_model = 'player'
    form_fields = ['p1_a']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_b_read(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_b_write(Page):
    form_model = 'player'
    form_fields = ['p1_b']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_c_read(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_c_write(Page):
    form_model = 'player'
    form_fields = ['p1_c']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_d_read(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_d_write(Page):
    form_model = 'player'
    form_fields = ['p1_d']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_e_read(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_e_write(Page):
    form_model = 'player'
    form_fields = ['p1_e']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_f_read(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_f_write(Page):
    form_model = 'player'
    form_fields = ['p1_f']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_s(Page):
    form_model = 'player'
    form_fields = ['p1_s1','p1_s2','p1_s3']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_para_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_para(Page):
    form_model = 'player'
    timeout_seconds = 300
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_dt1(Page):
    form_model = 'player'
    form_fields = ['p1_dt1']
    timeout_seconds = 15
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_para_write(Page):
    form_model = 'player'
    form_fields = ['p1_para']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_story(Page):
    form_model = 'player'
    form_fields = ['p1_story']
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

class p2_sent_explain(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_a_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'previoussentence': otherplayer.p1_a}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class wait_2(Page):
    form_model = 'player'
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_a_write(Page):
    form_model = 'player'
    form_fields = ['p2_a']
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_b_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'previoussentence': otherplayer.p1_b}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_b_write(Page):
    form_model = 'player'
    form_fields = ['p2_b']
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_s(Page):
    form_model = 'player'
    form_fields = ['p2_s1','p2_s2','p2_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story1': otherplayer.p1_s1, 
        'story2':otherplayer.p1_s2, 'story3':otherplayer.p1_s3}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_para_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_para(Page):
    form_model = 'player'
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'paragraph': otherplayer.p1_para}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_dt1(Page):
    form_model = 'player'
    form_fields = ['p2_dt1']
    timeout_seconds = 15
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_para_write(Page):
    form_model = 'player'
    form_fields = ['p2_para']
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

class p2_story(Page):
    form_model = 'player'
    form_fields = ['p2_story']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story1': otherplayer.p1_story}
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

class p3_sent_explain(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_a_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_a}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class wait_3(Page):
    form_model = 'player'
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_a_write(Page):
    form_model = 'player'
    form_fields = ['p3_a']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_b_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_b}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_b_write(Page):
    form_model = 'player'
    form_fields = ['p3_b']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False


class p3_s(Page):
    form_model = 'player'
    form_fields = ['p3_s1','p3_s2','p3_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story1': otherplayer.p2_s1, 
        'story2':otherplayer.p2_s2, 'story3':otherplayer.p2_s3}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_para_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_para(Page):
    form_model = 'player'
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'paragraph': otherplayer.p2_para}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_dt1(Page):
    form_model = 'player'
    form_fields = ['p3_dt1']
    timeout_seconds = 15
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_para_write(Page):
    form_model = 'player'
    form_fields = ['p3_para']
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

class p3_story(Page):
    form_model = 'player'
    form_fields = ['p3_story']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        return {'story1': otherplayer1.p1_story, 
        'story2': otherplayer2.p2_story}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False



page_sequence = [
# Player 1 
    p1_sent_explain,
    p1_a_read,
    wait_1,
    p1_a_write,
    p1_b_read,
    wait_1,
    p1_b_write,
    p1_s,
    p1_para_inst,
    p1_para,
    p1_dt1,
    p1_para_write,
    p1_story_inst,
    p1_story,

# Player 2
    p2_wait,
    p2_sent_explain,
    p2_a_read,
    wait_2,
    p2_a_write,
    p2_b_read,
    wait_2,
    p2_b_write,
    p2_s,
    p2_para_inst,
    p2_para,
    p2_dt1,
    p2_para_write,
    p2_story_inst,
    p2_story,


# Player 3
    p3_wait,
    p3_sent_explain,
    p3_a_read,
    wait_3,
    p3_a_write,
    p3_b_read,
    wait_3,
    p3_b_write,
    p3_s,
    p3_para_inst,
    p3_para,
    p3_dt1,
    p3_para_write,
    p3_story_inst,
    p3_story

]
