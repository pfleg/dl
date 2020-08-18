from core.advbase import *

def module():
    return Amane

class Amane(Adv):
    a3 = ('bk',0.35)
    a1 = [('prep',1.00), ('scharge_all', 0.05)]
    
    conf = {}
    conf['acl'] = """
        `dragon
        `s2
        `s1
        `s3
        `s4
        """
    coab = ['Blade','Sharena','Peony']
    conf['afflict_res.paralysis'] = 0
    share = ['Summer_Patia', 'Ranzal']
    
     def init(self):
        self.s1_stance = 1

    def s1_proc(self, e):
        self.afflics.paralysis(e.name,120, 0.97)

    def s2_proc(self, e):


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
