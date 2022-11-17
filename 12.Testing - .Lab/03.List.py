class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):
    def test_is_initialized_correctly_without_data(self):
        integer = IntegerList()
        self.assertEqual([],integer._IntegerList__data)

    def test_is_initialized_correctly_with_wrong_data(self):
        integer = IntegerList('asd',5.6,10.2)
        self.assertEqual([], integer._IntegerList__data)

    def test_is_initialized_correctly_with_integers_data(self):
        integer = IntegerList('asd',5)
        self.assertEqual([5],integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(5)
        self.assertEqual([5],integer._IntegerList__data)
        result = integer.get_data()
        self.assertEqual([5],result)

    def test_add_is_not_integer(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)
        with self.assertRaises(ValueError) as ex:
            integer.add('5')
        self.assertEqual('Element is not Integer', str(ex.exception))


    def test_add_happy_case(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)
        integer.add(10)
        self.assertEqual([5,10], integer._IntegerList__data)


    def test_remove_element_removes_the_element(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)
        integer.remove_index(0)
        self.assertEqual([],integer._IntegerList__data)

    def test_remove_invalid_index_raises(self):
        integer = IntegerList(5)
        with self.assertRaises(IndexError) as exe:
            integer.remove_index(2)
        self.assertEqual('Index is out of range', str(exe.exception))

        with self.assertRaises(IndexError) as exe:
            integer.remove_index(1)
        self.assertEqual('Index is out of range', str(exe.exception))


    def test_remove_returns_element_at_the_removed_index(self):
        integer = IntegerList(5)
        result = integer.remove_index(0)
        self.assertEqual(5,result)

    def test_get_invalid_index_raises(self):
        integer = IntegerList(5)
        with self.assertRaises(IndexError) as exe:
            integer.get(2)
        self.assertEqual('Index is out of range', str(exe.exception))

        with self.assertRaises(IndexError) as exe:
            integer.get(1)
        self.assertEqual('Index is out of range', str(exe.exception))

    def test_get_valid_index_return_element(self):
        integer = IntegerList(5)

        result = integer.get(0)
        self.assertEqual(5,result)

    def test_insert_invalid_index_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(IndexError) as exe:
            integer.insert(2,10)
        self.assertEqual('Index is out of range',str(exe.exception))

    def test_insert_invalid_data_type_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(ValueError) as exe:
            integer.insert(0, "10")
        self.assertEqual('Element is not Integer', str(exe.exception))

    def test_insert_add_element(self):
        integer = IntegerList(5)

        integer.insert(0,200)

        self.assertEqual([200,5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(5,-2,100,300,-44)
        result = integer.get_biggest()
        self.assertEqual(300,result)

    def test_get_index(self):
        integer = IntegerList(10)

        result = integer.get_index(10)

        self.assertEqual(0,result)



if __name__ == '__main__':
    main()