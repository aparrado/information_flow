from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class informedconsent(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        return True


## Player 1
#simple sentences
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
        
class p1_g_read(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_g_write(Page):
    form_model = 'player'
    form_fields = ['p1_g']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_h_read(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_h_write(Page):
    form_model = 'player'
    form_fields = ['p1_h']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_i_read(Page):
    form_model = 'player'
    form_fields = []
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False

class p1_i_write(Page):
    form_model = 'player'
    form_fields = ['p1_i']
    def is_displayed(self):
        if self.player.id_in_group == 1:
            return True
        else:
            return False


# sentences stories
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

class p2_c_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'previoussentence': otherplayer.p1_c}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_c_write(Page):
    form_model = 'player'
    form_fields = ['p2_c']
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_d_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'previoussentence': otherplayer.p1_d}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_d_write(Page):
    form_model = 'player'
    form_fields = ['p2_d']
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_e_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'previoussentence': otherplayer.p1_e}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_e_write(Page):
    form_model = 'player'
    form_fields = ['p2_e']
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_f_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'previoussentence': otherplayer.p1_f}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False


class p2_f_write(Page):
    form_model = 'player'
    form_fields = ['p2_f']
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False
        
class p2_g_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'previoussentence': otherplayer.p1_g}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False


class p2_g_write(Page):
    form_model = 'player'
    form_fields = ['p2_g']
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_h_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'previoussentence': otherplayer.p1_h}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False


class p2_h_write(Page):
    form_model = 'player'
    form_fields = ['p2_h']
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False

class p2_i_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'previoussentence': otherplayer.p1_i}
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False


class p2_i_write(Page):
    form_model = 'player'
    form_fields = ['p2_i']
    def is_displayed(self):
        if self.player.id_in_group == 2:
            return True
        else:
            return False


class p2_s1(Page):
    form_model = 'player'
    form_fields = ['p2_s1']
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
    form_fields = ['p2_s2']
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
    form_fields = ['p2_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(1)
        return {'story3': otherplayer.p1_s3}
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

#sentences
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

class p3_c_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_c}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_c_write(Page):
    form_model = 'player'
    form_fields = ['p3_c']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_d_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_d}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_d_write(Page):
    form_model = 'player'
    form_fields = ['p3_d']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_d_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_d}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_d_write(Page):
    form_model = 'player'
    form_fields = ['p3_d']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_e_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_e}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_e_write(Page):
    form_model = 'player'
    form_fields = ['p3_e']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_f_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_f}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_f_write(Page):
    form_model = 'player'
    form_fields = ['p3_f']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_g_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_g}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_g_write(Page):
    form_model = 'player'
    form_fields = ['p3_g']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_h_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_h}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_h_write(Page):
    form_model = 'player'
    form_fields = ['p3_h']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_i_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'previoussentence': otherplayer.p2_i}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_i_write(Page):
    form_model = 'player'
    form_fields = ['p3_i']
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_s1(Page):
    form_model = 'player'
    form_fields = ['p3_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story1': otherplayer.p2_s1}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_s2(Page):
    form_model = 'player'
    form_fields = ['p3_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story2': otherplayer.p2_s2}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False


class p3_s3(Page):
    form_model = 'player'
    form_fields = ['p3_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(2)
        return {'story3': otherplayer.p2_s3}
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
    form_fields = ['p2_dt1']
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


## Player 4
class p4_wait(WaitPage):
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

#sentences
class p4_sent_explain(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_a_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'previoussentence': otherplayer.p3_a}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class wait_4(Page):
    form_model = 'player'
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_a_write(Page):
    form_model = 'player'
    form_fields = ['p4_a']
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_b_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'previoussentence': otherplayer.p3_b}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_b_write(Page):
    form_model = 'player'
    form_fields = ['p4_b']
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_c_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'previoussentence': otherplayer.p3_c}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_c_write(Page):
    form_model = 'player'
    form_fields = ['p4_c']
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_d_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'previoussentence': otherplayer.p3_d}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_d_write(Page):
    form_model = 'player'
    form_fields = ['p4_d']
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False


class p4_e_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'previoussentence': otherplayer.p3_e}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_e_write(Page):
    form_model = 'player'
    form_fields = ['p4_e']
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_f_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'previoussentence': otherplayer.p3_f}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_f_write(Page):
    form_model = 'player'
    form_fields = ['p4_f']
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_g_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'previoussentence': otherplayer.p3_g}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_g_write(Page):
    form_model = 'player'
    form_fields = ['p4_g']
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_h_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'previoussentence': otherplayer.p3_h}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_h_write(Page):
    form_model = 'player'
    form_fields = ['p4_h']
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_i_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'previoussentence': otherplayer.p3_i}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_i_write(Page):
    form_model = 'player'
    form_fields = ['p4_i']
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

# Sentences
class p4_s1(Page):
    form_model = 'player'
    form_fields = ['p4_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story1': otherplayer.p3_s1}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_s2(Page):
    form_model = 'player'
    form_fields = ['p4_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story2': otherplayer.p3_s2}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_s3(Page):
    form_model = 'player'
    form_fields = ['p4_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'story3': otherplayer.p3_s3}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False


class p4_para_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_dt1(Page):
    form_model = 'player'
    form_fields = ['p2_dt1']
    timeout_seconds = 15
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_para(Page):
    form_model = 'player'
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(3)
        return {'paragraph': otherplayer.p3_para}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_para_write(Page):
    form_model = 'player'
    form_fields = ['p4_para']
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

class p4_story(Page):
    form_model = 'player'
    form_fields = ['p4_story']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        return {'story1': otherplayer1.p1_story, 
        'story2': otherplayer2.p2_story,
        'story3': otherplayer3.p3_story}
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

#sentences
class p5_sent_explain(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_a_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'previoussentence': otherplayer.p4_a}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class wait_5(Page):
    form_model = 'player'
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_a_write(Page):
    form_model = 'player'
    form_fields = ['p5_a']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_b_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'previoussentence': otherplayer.p4_b}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_b_write(Page):
    form_model = 'player'
    form_fields = ['p5_b']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_c_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'previoussentence': otherplayer.p4_c}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_c_write(Page):
    form_model = 'player'
    form_fields = ['p5_c']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_d_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'previoussentence': otherplayer.p4_d}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_d_write(Page):
    form_model = 'player'
    form_fields = ['p5_d']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_e_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'previoussentence': otherplayer.p4_e}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_e_write(Page):
    form_model = 'player'
    form_fields = ['p5_e']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_f_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'previoussentence': otherplayer.p4_f}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_f_write(Page):
    form_model = 'player'
    form_fields = ['p5_f']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_g_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'previoussentence': otherplayer.p4_g}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_g_write(Page):
    form_model = 'player'
    form_fields = ['p5_g']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_h_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'previoussentence': otherplayer.p4_h}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_h_write(Page):
    form_model = 'player'
    form_fields = ['p5_h']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_i_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'previoussentence': otherplayer.p4_i}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_i_write(Page):
    form_model = 'player'
    form_fields = ['p5_i']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

# Sentences
class p5_s1(Page):
    form_model = 'player'
    form_fields = ['p5_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story1': otherplayer.p4_s1}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_s2(Page):
    form_model = 'player'
    form_fields = ['p5_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story2': otherplayer.p4_s2}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_s3(Page):
    form_model = 'player'
    form_fields = ['p5_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'story3': otherplayer.p4_s3}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_para(Page):
    form_model = 'player'
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(4)
        return {'paragraph': otherplayer.p4_para}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False


class p5_para_write(Page):
    form_model = 'player'
    form_fields = ['p5_para']
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_para_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_dt1(Page):
    form_model = 'player'
    form_fields = ['p2_dt1']
    timeout_seconds = 15
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

class p5_story(Page):
    form_model = 'player'
    form_fields = ['p5_story']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4) 
        return {'story1': otherplayer1.p1_story, 
        'story2': otherplayer2.p2_story,
        'story3': otherplayer3.p3_story,
        'story4': otherplayer4.p4_story}
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

#sentences
class p6_sent_explain(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_a_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'previoussentence': otherplayer.p5_a}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class wait_6(Page):
    form_model = 'player'
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_a_write(Page):
    form_model = 'player'
    form_fields = ['p6_a']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False


class p6_b_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'previoussentence': otherplayer.p5_b}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_b_write(Page):
    form_model = 'player'
    form_fields = ['p6_b']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_c_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'previoussentence': otherplayer.p5_c}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_c_write(Page):
    form_model = 'player'
    form_fields = ['p6_c']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_d_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'previoussentence': otherplayer.p5_d}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_d_write(Page):
    form_model = 'player'
    form_fields = ['p6_d']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_e_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'previoussentence': otherplayer.p5_e}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_e_write(Page):
    form_model = 'player'
    form_fields = ['p6_e']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_f_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'previoussentence': otherplayer.p5_f}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_f_write(Page):
    form_model = 'player'
    form_fields = ['p6_f']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_g_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'previoussentence': otherplayer.p5_g}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_g_write(Page):
    form_model = 'player'
    form_fields = ['p6_g']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_h_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'previoussentence': otherplayer.p5_h}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_h_write(Page):
    form_model = 'player'
    form_fields = ['p6_h']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_i_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'previoussentence': otherplayer.p5_i}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_i_write(Page):
    form_model = 'player'
    form_fields = ['p6_i']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

# Sentences
class p6_s1(Page):
    form_model = 'player'
    form_fields = ['p6_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story1': otherplayer.p5_s1}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_s2(Page):
    form_model = 'player'
    form_fields = ['p6_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story2': otherplayer.p5_s2}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_s3(Page):
    form_model = 'player'
    form_fields = ['p6_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'story3': otherplayer.p5_s3}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_para(Page):
    form_model = 'player'
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(5)
        return {'paragraph': otherplayer.p5_para}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False


class p6_para_write(Page):
    form_model = 'player'
    form_fields = ['p6_para']
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_para_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_dt1(Page):
    form_model = 'player'
    form_fields = ['p2_dt1']
    timeout_seconds = 15
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

class p6_story(Page):
    form_model = 'player'
    form_fields = ['p6_story']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4) 
        otherplayer5 = self.group.get_player_by_id(5) 
        return {'story1': otherplayer1.p1_story, 
        'story2': otherplayer2.p2_story,
        'story3': otherplayer3.p3_story,
        'story4': otherplayer4.p4_story,
        'story5': otherplayer5.p5_story}
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

#sentences
class p7_sent_explain(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_a_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'previoussentence': otherplayer.p6_a}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class wait_7(Page):
    form_model = 'player'
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_a_write(Page):
    form_model = 'player'
    form_fields = ['p7_a']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_b_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'previoussentence': otherplayer.p6_b}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_b_write(Page):
    form_model = 'player'
    form_fields = ['p7_b']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_c_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'previoussentence': otherplayer.p6_c}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_c_write(Page):
    form_model = 'player'
    form_fields = ['p7_c']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_d_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'previoussentence': otherplayer.p6_d}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_d_write(Page):
    form_model = 'player'
    form_fields = ['p7_d']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_e_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'previoussentence': otherplayer.p6_e}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_e_write(Page):
    form_model = 'player'
    form_fields = ['p7_e']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_f_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'previoussentence': otherplayer.p6_f}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_f_write(Page):
    form_model = 'player'
    form_fields = ['p7_f']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_g_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'previoussentence': otherplayer.p6_g}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_g_write(Page):
    form_model = 'player'
    form_fields = ['p7_g']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_h_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'previoussentence': otherplayer.p6_h}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_h_write(Page):
    form_model = 'player'
    form_fields = ['p7_h']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_i_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'previoussentence': otherplayer.p6_i}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_i_write(Page):
    form_model = 'player'
    form_fields = ['p7_i']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

# Sentences
class p7_s1(Page):
    form_model = 'player'
    form_fields = ['p7_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story1': otherplayer.p6_s1}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_s2(Page):
    form_model = 'player'
    form_fields = ['p7_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story2': otherplayer.p6_s2}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_s3(Page):
    form_model = 'player'
    form_fields = ['p7_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'story3': otherplayer.p6_s3}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_para(Page):
    form_model = 'player'
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(6)
        return {'paragraph': otherplayer.p6_para}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False


class p7_para_write(Page):
    form_model = 'player'
    form_fields = ['p7_para']
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_para_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_dt1(Page):
    form_model = 'player'
    form_fields = ['p2_dt1']
    timeout_seconds = 15
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

class p7_story(Page):
    form_model = 'player'
    form_fields = ['p7_story']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4) 
        otherplayer5 = self.group.get_player_by_id(5) 
        otherplayer6 = self.group.get_player_by_id(6) 
        return {'story1': otherplayer1.p1_story, 
        'story2': otherplayer2.p2_story,
        'story3': otherplayer3.p3_story,
        'story4': otherplayer4.p4_story,
        'story5': otherplayer5.p5_story,
        'story6': otherplayer6.p6_story}
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

#sentences
class p8_sent_explain(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_a_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'previoussentence': otherplayer.p7_a}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class wait_8(Page):
    form_model = 'player'
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_a_write(Page):
    form_model = 'player'
    form_fields = ['p8_a']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_b_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'previoussentence': otherplayer.p7_b}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_b_write(Page):
    form_model = 'player'
    form_fields = ['p8_b']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_c_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'previoussentence': otherplayer.p7_c}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_c_write(Page):
    form_model = 'player'
    form_fields = ['p8_c']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_d_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'previoussentence': otherplayer.p7_d}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_d_write(Page):
    form_model = 'player'
    form_fields = ['p8_d']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_e_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'previoussentence': otherplayer.p7_e}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_e_write(Page):
    form_model = 'player'
    form_fields = ['p8_e']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_f_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'previoussentence': otherplayer.p7_f}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_f_write(Page):
    form_model = 'player'
    form_fields = ['p8_f']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False


class p8_g_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'previoussentence': otherplayer.p7_g}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_g_write(Page):
    form_model = 'player'
    form_fields = ['p8_g']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_h_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'previoussentence': otherplayer.p7_h}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_h_write(Page):
    form_model = 'player'
    form_fields = ['p8_h']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_i_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'previoussentence': otherplayer.p7_i}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_i_write(Page):
    form_model = 'player'
    form_fields = ['p8_i']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

# Sentences
class p8_s1(Page):
    form_model = 'player'
    form_fields = ['p8_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story1': otherplayer.p7_s1}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_s2(Page):
    form_model = 'player'
    form_fields = ['p8_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story2': otherplayer.p7_s2}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_s3(Page):
    form_model = 'player'
    form_fields = ['p8_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'story3': otherplayer.p7_s3}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_para(Page):
    form_model = 'player'
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(7)
        return {'paragraph': otherplayer.p7_para}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False


class p8_para_write(Page):
    form_model = 'player'
    form_fields = ['p8_para']
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_para_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_dt1(Page):
    form_model = 'player'
    form_fields = ['p2_dt1']
    timeout_seconds = 15
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

class p8_story(Page):
    form_model = 'player'
    form_fields = ['p8_story']
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer1 = self.group.get_player_by_id(1)
        otherplayer2 = self.group.get_player_by_id(2)
        otherplayer3 = self.group.get_player_by_id(3)
        otherplayer4 = self.group.get_player_by_id(4) 
        otherplayer5 = self.group.get_player_by_id(5) 
        otherplayer6 = self.group.get_player_by_id(6) 
        otherplayer7 = self.group.get_player_by_id(7) 
        return {'story1': otherplayer1.p1_story, 
        'story2': otherplayer2.p2_story,
        'story3': otherplayer3.p3_story,
        'story4': otherplayer4.p4_story,
        'story5': otherplayer5.p5_story,
        'story6': otherplayer6.p6_story,
        'story7': otherplayer7.p7_story}        
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

#sentences
class p9_sent_explain(Page):
    form_model = 'player'
    form_fields = []
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_a_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'previoussentence': otherplayer.p8_a}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class wait_9(Page):
    form_model = 'player'
    timeout_seconds = 6
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_a_write(Page):
    form_model = 'player'
    form_fields = ['p9_a']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_b_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'previoussentence': otherplayer.p8_b}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_b_write(Page):
    form_model = 'player'
    form_fields = ['p9_b']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_c_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'previoussentence': otherplayer.p8_c}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_c_write(Page):
    form_model = 'player'
    form_fields = ['p9_c']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_d_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'previoussentence': otherplayer.p8_d}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_d_write(Page):
    form_model = 'player'
    form_fields = ['p9_d']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_e_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'previoussentence': otherplayer.p8_e}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_e_write(Page):
    form_model = 'player'
    form_fields = ['p9_e']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_f_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'previoussentence': otherplayer.p8_f}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_f_write(Page):
    form_model = 'player'
    form_fields = ['p9_f']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_g_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'previoussentence': otherplayer.p8_g}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_g_write(Page):
    form_model = 'player'
    form_fields = ['p9_g']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_h_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'previoussentence': otherplayer.p8_h}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_h_write(Page):
    form_model = 'player'
    form_fields = ['p9_h']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_i_read(Page):
    form_model = 'player'
    timeout_seconds = 6
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'previoussentence': otherplayer.p8_i}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_i_write(Page):
    form_model = 'player'
    form_fields = ['p9_i']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

# Sentences
class p9_s1(Page):
    form_model = 'player'
    form_fields = ['p9_s1']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story1': otherplayer.p8_s1}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_s2(Page):
    form_model = 'player'
    form_fields = ['p9_s2']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story2': otherplayer.p8_s2}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_s3(Page):
    form_model = 'player'
    form_fields = ['p9_s3']
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'story3': otherplayer.p8_s3}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False


class p9_para(Page):
    form_model = 'player'
    timeout_seconds = 300
    def vars_for_template(self):
        otherplayer = self.group.get_player_by_id(8)
        return {'paragraph': otherplayer.p8_para}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False


class p9_para_write(Page):
    form_model = 'player'
    form_fields = ['p9_para']
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False


class p9_para_inst(Page):
    form_model = 'player'
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_dt1(Page):
    form_model = 'player'
    form_fields = ['p2_dt1']
    timeout_seconds = 15
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

class p9_story(Page):
    form_model = 'player'
    form_fields = ['p9_story']
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
        return {'story1': otherplayer1.p1_story, 
        'story2': otherplayer2.p2_story,
        'story3': otherplayer3.p3_story,
        'story4': otherplayer4.p4_story,
        'story5': otherplayer5.p5_story,
        'story6': otherplayer6.p6_story,
        'story7': otherplayer7.p7_story,
        'story8': otherplayer8.p8_story}        
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

page_sequence = [
    informedconsent,

# Player 1 
    p1_sent_explain,
    p1_a_read,
    wait_1,
    p1_a_write,
    p1_b_read,
    wait_1,
    p1_b_write,
    p1_c_read,
    wait_1,
    p1_c_write,
    p1_d_read,
    wait_1,
    p1_d_write,
    p1_e_read,
    wait_1,
    p1_e_write, 
    p1_f_read,
    wait_1,
    p1_f_write,
    p1_g_read,
    wait_1,
    p1_g_write,
    p1_h_read,
    wait_1,
    p1_h_write,
    p1_i_read,
    wait_1,
    p1_i_write,

    #sentences
    p1_s1,
    p1_s2,
    p1_s3,
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
    p2_c_read,
    wait_2,
    p2_c_write,
    p2_d_read,
    wait_2,
    p2_d_write,
    p2_e_read,
    wait_2,
    p2_e_write, 
    p2_f_read,
    wait_2,
    p2_f_write,
    p2_g_read,
    wait_2,
    p2_g_write,
    p2_h_read,
    wait_2,
    p2_h_write,
    p2_i_read,
    wait_2,
    p2_i_write,


    #sentences
    p2_s1,
    p2_s2,
    p2_s3,
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
    p3_c_read,
    wait_3,
    p3_c_write,
    p3_d_read,
    wait_3,
    p3_d_write,
    p3_e_read,
    wait_3,
    p3_e_write,
    p3_f_read,
    wait_3,
    p3_f_write,
    p3_g_read,
    wait_3,
    p3_g_write,
    p3_h_read,
    wait_3,
    p3_h_write,
    p3_i_read,
    wait_3,
    p3_i_write,



    #sentences
    p3_s1,
    p3_s2,
    p3_s3,
    p3_para_inst,
    p3_para,
    p3_dt1,
    p3_para_write,
    p3_story_inst,
    p3_story,


    # Player 4
    p4_wait,
    p4_sent_explain,
    p4_a_read,
    wait_4,
    p4_a_write,
    p4_b_read,
    wait_4,
    p4_b_write,
    p4_c_read,
    wait_4,
    p4_c_write,
    p4_d_read,
    wait_4,
    p4_d_write,
    p4_e_read,
    wait_4,
    p4_e_write,
    p4_f_read,
    wait_4,
    p4_f_write,
    p4_g_read,
    wait_4,
    p4_g_write,
    p4_h_read,
    wait_4,
    p4_h_write,
    p4_i_read,
    wait_4,
    p4_i_write,

    #sentences
    p4_s1,
    p4_s2,
    p4_s3,
    p4_para_inst,
    p4_para,
    p4_dt1,
    p4_para_write,
    p4_story_inst,
    p4_story,

    # Player 5
    p5_wait,
    p5_sent_explain,
    p5_a_read,
    wait_5,
    p5_a_write,
    p5_b_read,
    wait_5,
    p5_b_write,
    p5_c_read,
    wait_5,
    p5_c_write,
    p5_d_read,
    wait_5,
    p5_d_write,
    p5_e_read,
    wait_5,
    p5_e_write,
    p5_f_read,
    wait_5,
    p5_f_write,
    p5_g_read,
    wait_5,
    p5_g_write,
    p5_h_read,
    wait_5,
    p5_h_write,
    p5_i_read,
    wait_5,
    p5_i_write,

    #sentences
    p5_s1,
    p5_s2,
    p5_s3,
    p5_para_inst,
    p5_para,
    p5_dt1,
    p5_para_write,
    p5_story_inst,
    p5_story,

    # Player 6
    p6_wait,
    p6_sent_explain,
    p6_a_read,
    wait_6,
    p6_a_write,
    p6_b_read,
    wait_6,
    p6_b_write,
    p6_c_read,
    wait_6,
    p6_c_write,
    p6_d_read,
    wait_6,
    p6_d_write,
    p6_e_read,
    wait_6,
    p6_e_write,
    p6_f_read,
    wait_6,
    p6_f_write,
    p6_g_read,
    wait_6,
    p6_g_write,
    p6_h_read,
    wait_6,
    p6_h_write,
    p6_i_read,
    wait_6,
    p6_i_write,

    #sentences
    p6_s1,
    p6_s2,
    p6_s3,
    p6_para_inst,
    p6_para,
    p6_dt1,
    p6_para_write,
    p6_story_inst,
    p6_story,

    # Player 7
    p7_wait,
    p7_sent_explain,
    p7_a_read,
    wait_7,
    p7_a_write,
    p7_b_read,
    wait_7,
    p7_b_write,
    p7_c_read,
    wait_7,
    p7_c_write,
    p7_d_read,
    wait_7,
    p7_d_write,
    p7_e_read,
    wait_7,
    p7_e_write,
    p7_f_read,
    wait_7,
    p7_f_write,
    p7_g_read,
    wait_7,
    p7_g_write,
    p7_h_read,
    wait_7,
    p7_h_write,
    p7_i_read,
    wait_7,
    p7_i_write,

    #sentences
    p7_s1,
    p7_s2,
    p7_s3,
    p7_para_inst,
    p7_para,
    p7_dt1,
    p7_para_write,
    p7_story_inst,
    p7_story,


    # Player 8
    p8_wait,
    p8_sent_explain,
    p8_a_read,
    wait_8,
    p8_a_write,
    p8_b_read,
    wait_8,
    p8_b_write,
    p8_c_read,
    wait_8,
    p8_c_write,
    p8_d_read,
    wait_8,
    p8_d_write,
    p8_e_read,
    wait_8,
    p8_e_write,
    p8_f_read,
    wait_8,
    p8_f_write,
    p8_g_read,
    wait_8,
    p8_g_write,
    p8_h_read,
    wait_8,
    p8_h_write,
    p8_i_read,
    wait_8,
    p8_i_write,

    #sentences
    p8_s1,
    p8_s2,
    p8_s3,
    p8_para_inst,
    p8_para,
    p8_dt1,
    p8_para_write,
    p8_story_inst,
    p8_story,

    # Player 9
    p9_wait,
    p9_sent_explain,
    p9_a_read,
    wait_9,
    p9_a_write,
    p9_b_read,
    wait_9,
    p9_b_write,
    p9_c_read,
    wait_9,
    p9_c_write,
    p9_d_read,
    wait_9,
    p9_d_write,
    p9_e_read,
    wait_9,
    p9_e_write,
    p9_f_read,
    wait_9,
    p9_f_write,
    p9_g_read,
    wait_9,
    p9_g_write,
    p9_h_read,
    wait_9,
    p9_h_write,
    p9_i_read,
    wait_9,
    p9_i_write,

    #sentences
    p9_s1,
    p9_s2,
    p9_s3,
    p9_para_inst,
    p9_para,
    p9_dt1,
    p9_para_write,
    p9_story_inst,
    p9_story,

]
