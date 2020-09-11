import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

#(jupyter notebook) jupyter의 커널명이 sys.argv의 첫 파라미터로 unittest.main에 전달되기 때문에 에러 발생. 아래와 같이 수정.
#if __name__ == '__main__':
#    unittest.main(argv=['first-arg-is-ignored'], exit=False)
