from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Alex

class Alex(Adv):
    comment = 'not consider bk boost of her s2'
    a1 = ('s',0.35,'hp100')
    a3 = ('sp',0.05)

    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+The_Plaguebringer()
    conf['slots.poison.a'] = conf['slots.a']
    conf['acl'] = """
        `dragon.act('c3 s end'), self.slots.tmp.d.trickery <= 1
        `s3, not self.s3_buff
        `s4
        `s1
        `s2
        `fs, x=5
        """
    coab = ['Blade','Wand','Heinwald']
    conf['afflict_res.poison'] = 0
    share = ['Curran']

    def s1_proc(self, e):
        self.afflics.poison(e.name,100,0.396)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)