class Review(object):
    def __init__(self):
        self.name = 'Review_1_test_name'

    @staticmethod
    def review_1(self):
        print('I like review_1')

    @staticmethod
    def print_review_1(self, dict_data):
        if dict_data:
            for key, value in dict_data.items():
                print('key: %(key)s value: %(value)s' % {'key': key, 'value': value})

    @staticmethod
    def print_review_2(self):
        print('1 or 2 : %s' % (1 or 2))
        print('2 or 3 : %s' % (2 or 3))
        print('1 and 2 : %s' % (1 and 2))
        print('2 and 3 : %s' % (2 and 3))


if __name__ == '__main__':
    review_test_1 = Review()
    review_test_1.review_1()
    test_dict = {'name': 'test_name', 'id': '330421188', 'sex': 'mail', 'age': 29}
    # review_test_1.print_review_1(test_dict)
    review_test_1.print_review_2()
