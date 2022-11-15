class Worker:

  def __init__(self, name, salary, energy):
    self.name = name
    self.salary = salary
    self.energy = energy
    self.money = 0

  def work(self):
    if self.energy <= 0:
        raise Exception('Not enough energy.')

    self.money += self.salary
    self.energy -= 1

  def rest(self):
    self.energy += 1

  def get_info(self):
    return (f'{self.name} has saved {self.money} money.')


from unittest import TestCase,main

class WorkerTest(TestCase):
    def test_initilizing(self):
        worker = Worker("Peter", 100, 10)

        self.assertEqual("Peter", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0,worker.money)

    def test_worker_energy_after_rest(self):
      worker = Worker("Peter", 100, 10)
      self.assertEqual(10, worker.energy)
      worker.rest()
      self.assertEqual(11,worker.energy)
      worker.rest()
      self.assertEqual(12, worker.energy)

    def test_error_raised_when_work(self):
      worker = Worker("Peter", 100, 0)

      with self.assertRaises(Exception) as exp:
        worker.work()
      self.assertEqual("Not enough energy.", str(exp.exception))

    def test_error_raised_with_negative_when_work(self):
      worker = Worker("Peter", 100, -1)

      with self.assertRaises(Exception) as exp:
        worker.work()
      self.assertEqual("Not enough energy.", str(exp.exception))

    def test_money_increase_when_work(self):
      worker = Worker("Peter", 100, 10)

      self.assertEqual(0,worker.money)

      worker.work()

      self.assertEqual(100,worker.money)

      worker.work()

      self.assertEqual(200,worker.money)

    def test_energy_decreased_after_work(self):
        worker = Worker("Peter", 100, 10)
        self.assertEqual(10,worker.energy)
        worker.work()
        self.assertEqual(9,worker.energy)
        worker.work()
        self.assertEqual(8,worker.energy)

    def test_get_info(self):
        worker = Worker("Peter", 100, 10)
        self.assertEqual("Peter has saved 0 money.", worker.get_info())


if __name__ == '__main__':
    main()



