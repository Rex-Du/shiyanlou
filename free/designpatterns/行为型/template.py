"""
author: rexdu
create: 2020/6/27 10:59
"""
import abc


class Fishing:
    __metaclass__ = abc.ABCMeta

    def finishing(self):
        self.prepare_bait()
        self.go_to_riverbank()
        self.find_location()
        print("start fishing...")

    @abc.abstractmethod
    def prepare_bait(self):
        pass

    @abc.abstractmethod
    def go_to_riverbank(self):
        pass

    @abc.abstractmethod
    def find_location(self):
        pass


class JoinFishing(Fishing):
    def prepare_bait(self):
        print("John buy bait from TaoBao")

    def go_to_riverbank(self):
        print("John to river by driving")

    def find_location(self):
        print("John: select location on the island")


class SimonFishing(Fishing):
    def prepare_bait(self):
        print("Simon buy bait from JD")

    def go_to_riverbank(self):
        print("Simon to river by biking")

    def find_location(self):
        print("Simon select location on the riverbank")


if __name__ == '__main__':
    f = JoinFishing()
    f.finishing()
    print('----------------------')
    f = SimonFishing()
    f.finishing()
