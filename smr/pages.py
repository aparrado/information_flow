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
    form_fields = ['p1_a']
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
    form_fields = ['p1_b']
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
    form_fields = ['p1_c']
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
    form_fields = ['p1_d']
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
    form_fields = ['p1_e']
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
    form_fields = ['p1_f']
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
    form_fields = ['p1_g']
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
    form_fields = ['p1_h']
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
    form_fields = ['p1_i']
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
        return {'previoussentence': otherplayer.p1_a}
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
    form_fields = ['p1_a']
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
        return {'previoussentence': otherplayer.p1_b}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_b_write(Page):
    form_model = 'player'
    form_fields = ['p1_b']
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
        return {'previoussentence': otherplayer.p1_c}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_c_write(Page):
    form_model = 'player'
    form_fields = ['p1_c']
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
        return {'previoussentence': otherplayer.p1_d}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_d_write(Page):
    form_model = 'player'
    form_fields = ['p1_d']
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
        return {'previoussentence': otherplayer.p1_d}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_d_write(Page):
    form_model = 'player'
    form_fields = ['p1_d']
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
        return {'previoussentence': otherplayer.p1_e}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_e_write(Page):
    form_model = 'player'
    form_fields = ['p1_e']
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
        return {'previoussentence': otherplayer.p1_f}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_f_write(Page):
    form_model = 'player'
    form_fields = ['p1_f']
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
        return {'previoussentence': otherplayer.p1_g}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_g_write(Page):
    form_model = 'player'
    form_fields = ['p1_g']
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
        return {'previoussentence': otherplayer.p1_h}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_h_write(Page):
    form_model = 'player'
    form_fields = ['p1_h']
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
        return {'previoussentence': otherplayer.p1_i}
    def is_displayed(self):
        if self.player.id_in_group == 3:
            return True
        else:
            return False

class p3_i_write(Page):
    form_model = 'player'
    form_fields = ['p1_i']
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
        return {'previoussentence': otherplayer.p1_a}
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
    form_fields = ['p1_a']
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
        return {'previoussentence': otherplayer.p1_b}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_b_write(Page):
    form_model = 'player'
    form_fields = ['p1_b']
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
        return {'previoussentence': otherplayer.p1_c}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_c_write(Page):
    form_model = 'player'
    form_fields = ['p1_c']
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
        return {'previoussentence': otherplayer.p1_d}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_d_write(Page):
    form_model = 'player'
    form_fields = ['p1_d']
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
        return {'previoussentence': otherplayer.p1_e}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_e_write(Page):
    form_model = 'player'
    form_fields = ['p1_e']
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
        return {'previoussentence': otherplayer.p1_f}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_f_write(Page):
    form_model = 'player'
    form_fields = ['p1_f']
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
        return {'previoussentence': otherplayer.p1_g}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_g_write(Page):
    form_model = 'player'
    form_fields = ['p1_g']
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
        return {'previoussentence': otherplayer.p1_h}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_h_write(Page):
    form_model = 'player'
    form_fields = ['p1_h']
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
        return {'previoussentence': otherplayer.p1_i}
    def is_displayed(self):
        if self.player.id_in_group == 4:
            return True
        else:
            return False

class p4_i_write(Page):
    form_model = 'player'
    form_fields = ['p1_i']
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
        return {'previoussentence': otherplayer.p1_a}
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
    form_fields = ['p1_a']
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
        return {'previoussentence': otherplayer.p1_b}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_b_write(Page):
    form_model = 'player'
    form_fields = ['p1_b']
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
        return {'previoussentence': otherplayer.p1_c}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_c_write(Page):
    form_model = 'player'
    form_fields = ['p1_c']
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
        return {'previoussentence': otherplayer.p1_d}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_d_write(Page):
    form_model = 'player'
    form_fields = ['p1_d']
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
        return {'previoussentence': otherplayer.p1_e}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_e_write(Page):
    form_model = 'player'
    form_fields = ['p1_e']
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
        return {'previoussentence': otherplayer.p1_f}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_f_write(Page):
    form_model = 'player'
    form_fields = ['p1_f']
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
        return {'previoussentence': otherplayer.p1_g}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_g_write(Page):
    form_model = 'player'
    form_fields = ['p1_g']
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
        return {'previoussentence': otherplayer.p1_h}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_h_write(Page):
    form_model = 'player'
    form_fields = ['p1_h']
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
        return {'previoussentence': otherplayer.p1_i}
    def is_displayed(self):
        if self.player.id_in_group == 5:
            return True
        else:
            return False

class p5_i_write(Page):
    form_model = 'player'
    form_fields = ['p1_i']
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
        return {'previoussentence': otherplayer.p1_a}
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
    form_fields = ['p1_a']
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
        return {'previoussentence': otherplayer.p1_b}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_b_write(Page):
    form_model = 'player'
    form_fields = ['p1_b']
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
        return {'previoussentence': otherplayer.p1_c}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_c_write(Page):
    form_model = 'player'
    form_fields = ['p1_c']
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
        return {'previoussentence': otherplayer.p1_d}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_d_write(Page):
    form_model = 'player'
    form_fields = ['p1_d']
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
        return {'previoussentence': otherplayer.p1_e}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_e_write(Page):
    form_model = 'player'
    form_fields = ['p1_e']
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
        return {'previoussentence': otherplayer.p1_f}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_f_write(Page):
    form_model = 'player'
    form_fields = ['p1_f']
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
        return {'previoussentence': otherplayer.p1_g}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_g_write(Page):
    form_model = 'player'
    form_fields = ['p1_g']
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
        return {'previoussentence': otherplayer.p1_h}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_h_write(Page):
    form_model = 'player'
    form_fields = ['p1_h']
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
        return {'previoussentence': otherplayer.p1_i}
    def is_displayed(self):
        if self.player.id_in_group == 6:
            return True
        else:
            return False

class p6_i_write(Page):
    form_model = 'player'
    form_fields = ['p1_i']
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
        return {'previoussentence': otherplayer.p1_a}
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
    form_fields = ['p1_a']
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
        return {'previoussentence': otherplayer.p1_b}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_b_write(Page):
    form_model = 'player'
    form_fields = ['p1_b']
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
        return {'previoussentence': otherplayer.p1_c}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_c_write(Page):
    form_model = 'player'
    form_fields = ['p1_c']
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
        return {'previoussentence': otherplayer.p1_d}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_d_write(Page):
    form_model = 'player'
    form_fields = ['p1_d']
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
        return {'previoussentence': otherplayer.p1_e}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_e_write(Page):
    form_model = 'player'
    form_fields = ['p1_e']
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
        return {'previoussentence': otherplayer.p1_f}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_f_write(Page):
    form_model = 'player'
    form_fields = ['p1_f']
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
        return {'previoussentence': otherplayer.p1_g}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_g_write(Page):
    form_model = 'player'
    form_fields = ['p1_g']
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
        return {'previoussentence': otherplayer.p1_h}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_h_write(Page):
    form_model = 'player'
    form_fields = ['p1_h']
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
        return {'previoussentence': otherplayer.p1_i}
    def is_displayed(self):
        if self.player.id_in_group == 7:
            return True
        else:
            return False

class p7_i_write(Page):
    form_model = 'player'
    form_fields = ['p1_i']
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
        return {'previoussentence': otherplayer.p1_a}
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
    form_fields = ['p1_a']
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
        return {'previoussentence': otherplayer.p1_b}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_b_write(Page):
    form_model = 'player'
    form_fields = ['p1_b']
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
        return {'previoussentence': otherplayer.p1_c}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_c_write(Page):
    form_model = 'player'
    form_fields = ['p1_c']
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
        return {'previoussentence': otherplayer.p1_d}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_d_write(Page):
    form_model = 'player'
    form_fields = ['p1_d']
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
        return {'previoussentence': otherplayer.p1_e}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_e_write(Page):
    form_model = 'player'
    form_fields = ['p1_e']
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
        return {'previoussentence': otherplayer.p1_f}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_f_write(Page):
    form_model = 'player'
    form_fields = ['p1_f']
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
        return {'previoussentence': otherplayer.p1_g}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_g_write(Page):
    form_model = 'player'
    form_fields = ['p1_g']
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
        return {'previoussentence': otherplayer.p1_h}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_h_write(Page):
    form_model = 'player'
    form_fields = ['p1_h']
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
        return {'previoussentence': otherplayer.p1_i}
    def is_displayed(self):
        if self.player.id_in_group == 8:
            return True
        else:
            return False

class p8_i_write(Page):
    form_model = 'player'
    form_fields = ['p1_i']
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
        return {'previoussentence': otherplayer.p1_a}
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
    form_fields = ['p1_a']
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
        return {'previoussentence': otherplayer.p1_b}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_b_write(Page):
    form_model = 'player'
    form_fields = ['p1_b']
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
        return {'previoussentence': otherplayer.p1_c}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_c_write(Page):
    form_model = 'player'
    form_fields = ['p1_c']
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
        return {'previoussentence': otherplayer.p1_d}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_d_write(Page):
    form_model = 'player'
    form_fields = ['p1_d']
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
        return {'previoussentence': otherplayer.p1_e}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_e_write(Page):
    form_model = 'player'
    form_fields = ['p1_e']
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
        return {'previoussentence': otherplayer.p1_f}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_f_write(Page):
    form_model = 'player'
    form_fields = ['p1_f']
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
        return {'previoussentence': otherplayer.p1_g}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_g_write(Page):
    form_model = 'player'
    form_fields = ['p1_g']
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
        return {'previoussentence': otherplayer.p1_h}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_h_write(Page):
    form_model = 'player'
    form_fields = ['p1_h']
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
        return {'previoussentence': otherplayer.p1_i}
    def is_displayed(self):
        if self.player.id_in_group == 9:
            return True
        else:
            return False

class p9_i_write(Page):
    form_model = 'player'
    form_fields = ['p1_i']
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
    p9_i_write


]
