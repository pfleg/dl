import adv_test
import adv

def module():
    return Vanessa

class Vanessa(adv.Adv):
    comment = "do not use weapon skill"
    conf = {
        "mod_a": ('fs', 'passive', 0.40),
        } 

    def s2_proc(this, e):
        adv.Buff('defdown',-0.05,10,'def').on()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

