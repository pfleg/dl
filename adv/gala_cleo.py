from core.advbase import *
from slot import *
from slot.a import *
from slot.d import *
from module.x_alt import Fs_alt

import random
random.seed()

def module():
    return Gala_Cleo

class Gala_Cleo(Adv):
    comment = '(the true cleo is here)'
    a3 = ('prep','100%')
    conf = {}
    conf['slots.a'] = Candy_Couriers()+Primal_Crisis()  # wand c2*1.08 = 217
    conf['acl'] = """
        `dragon.act("c3 s end"), x=5 and self.slots.tmp.d.trickery <= 1
        `s3, not self.s3_buff
        `fs, s1.charged>=s1.sp and self.fs_alt.uses > 0
        if x=5 or x=4 or fsc or s
        `s4
        `s2
        end
        `s1, s or fsc

        # Buffbot Gleo with Azazel & Memory_of_a_Friend
        # `s3, not self.s3_buff
        # `fs, (s1.check() or s2.check()) and self.fs_alt.uses > 0
        # `s4, cancel
        # `s2, cancel
        # `s1, cancel
        """
    coab = ['Blade','Bow','Dagger']
    share = ['Curran']

    def fs_proc_alt(self, e):
        if self.a1_buffed:
            Teambuff('a1_str',0.25,10).no_bufftime().on()

    def prerun(self):
        self.a1_buffed = self.condition('a1 buff for 10s')
        self.phase['s1'] = 0

        conf_fs_alt = {
            'fs.dmg':0,
            'fs.sp' :0,
            'fs.charge': 30/60.0,
            'fs.startup': 20/60.0,
            'fs.recovery': 60/60.0,
        }
        self.fs_alt = Fs_alt(self, Conf(conf_fs_alt), self.fs_proc_alt)

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.phase[dst] = 0
        adv.fs_alt = Dummy()
        adv.rebind_function(Gala_Cleo, 's1_dmg')

    def s1_dmg(self, t):
        self.dmg_make(t.name,0.88)
        self.add_hits(1)
        self.dmg_make(t.name,2.65)
        self.add_hits(1)

    def s1_proc(self, e):
        self.phase[e.name] += 1
        for i in range(0, 3 + self.phase[e.name]):
            s1_timer = Timer(self.s1_dmg)
            s1_timer.name = e.name
            s1_timer.on((42.0 + 12*i )/60)
        self.fs_alt.on()
        self.phase[e.name] %= 3

    def s2_proc(self, e):
        Debuff(e.name, 0.10, 20).on()
        Debuff(e.name, 0.05, 20, 1, 'attack').on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
