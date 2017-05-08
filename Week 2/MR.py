from mrjob.job import MRJob

class PrimeDivisor(MRJob):

    def mapper(self, _, line):
        def is_prime(val):
            if val > 2:
                return all(val % i for i in xrange(2, val))
            else:
                return False
        ints = line.split(',')
        for value in ints:
            value = int(value)
            primeDivisor = [(i, value) for i in range(2, value) if value % i == 0 and is_prime(i)]
            for prime, i in primeDivisor:
                yield prime, i

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    PrimeDivisor.run()