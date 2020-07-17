"""
author: rexdu
create: 2020/6/27 22:14
"""


class Permutations(object):

    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        return ''.join(sorted(str1)) == str2


if __name__ == '__main__':
    str1 = 'acbdef'
    p = Permutations()
    print(p.is_permutation(str1, 'abcdef'))
