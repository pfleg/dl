import adv_test
import adv

def module():
    return Karina

class Karina(adv.Adv):
    a3 = ('prep','50%')


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=4
        `s3, seq=4
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0)

