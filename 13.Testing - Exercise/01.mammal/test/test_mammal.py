from unittest import TestCase, main

from project.mammal import Mammal


class Test_Mammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Peter','type','sound')

    def test_init(self):
        name = 'Peter'
        type = 'Type'
        sound = 'sound'

        mammal = Mammal(name, type, sound)

        self.assertEqual(mammal.name, name)
        self.assertEqual(mammal.type, type)
        self.assertEqual(mammal.sound, sound)
        self.assertEqual(mammal._Mammal__kingdom,'animals')

    def test_make_sound(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        actual = self.mammal.make_sound()
        self.assertEqual(actual,expected)

    def test_get_kingdom(self):
        expected = self.mammal.get_kingdom()
        actual = self.mammal._Mammal__kingdom
        self.assertEqual(actual,expected)


    def test_info(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        actual = self.mammal.info()
        self.assertEqual(actual,expected)





if __name__ == "__main__":
    main()
