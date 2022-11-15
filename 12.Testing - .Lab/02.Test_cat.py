class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


from unittest import TestCase,main

class Cat_test(TestCase):

  def test_init(self):
    cat = Cat("pisi")
    self.assertEqual('pisi', cat.name)

  def test_cat_fed(self):
    cat = Cat("pisi")
    self.assertEqual(False,cat.fed)

  def test_cat_sleepy(self):
    cat = Cat('pisi')
    self.assertEqual(False, cat.sleepy)

  def test_cat_size(self):
    cat = Cat('pisi')
    self.assertEqual(0,cat.size)

  def test_check_size_after_eating(self):
    cat = Cat('pisi')
    self.assertEqual(0,cat.size)
    cat.eat()
    self.assertEqual(1,cat.size)

  def test_cat_is_fed_after_eat(self):
    cat = Cat('pisi')
    self.assertEqual(False,cat.fed)
    cat.eat()
    self.assertEqual(True,cat.fed)

  def test_cannot_eat_if_already_fed(self):
    cat = Cat('pisi')
    cat.eat()
    with self.assertRaises(Exception) as execp:
      cat.eat()
    self.assertEqual('Already fed.', str(execp.exception))

  def test_cannot_sleep_if_not_fed(self):
    cat = Cat('pisi')
    self.assertEqual(False,cat.fed)
    with self.assertRaises(Exception) as ex:
      cat.sleep()

  def test_cat_not_sleepy_after_sleep(self):
    cat = Cat('pisi')
    self.assertEqual(False,cat.sleepy)
    cat.eat()
    cat.sleep()
    self.assertEqual(False,cat.sleepy)

if __name__ == "__main__":
  main()





