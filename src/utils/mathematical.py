from functools import reduce


class Mathematical():

    @classmethod
    def clean_data(self, numbers):
        try:
            numbers = [int(i.replace('[','').replace(']','')) for i in numbers.split(',')]
            return numbers
        except (ValueError, Exception) as e:
            raise ValueError('one value of list is not valued')

    @classmethod
    def  mcd(self, n1, n2):
        a = max(n1, n2)
        b = min(n1, n2)
        while b != 0:
            mcd = b
            b = a % b
            a = mcd
        return mcd

    @classmethod
    def mcm(self, n1, n2):
        a = max(n1, n2)
        b = min(n1, n2)
        mcm = (a/ self.mcd(a,b)) * b
        return mcm

    @classmethod
    def mcm_for(self, numbers):
        return reduce(lambda x, y: self.mcm(x, y), numbers)


    @classmethod
    def more_one(self, number):
        numbers = int(number)+1
        return numbers
