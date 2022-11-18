from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student('John',{'Math':['note1','note2']})
    def test_init_only_with_name(self):
        name = "John"
        student = Student(name)

        self.assertEqual(name,student.name)
        self.assertEqual({},student.courses)

    def test_init_with_all_data(self):
        name = 'John'
        course = {'Math':['math1','math2']}
        student = Student(name,course)

        self.assertEqual(name,student.name)
        self.assertEqual(course,student.courses)


    def test_enroll_with_already_enrolled_course_adds_notes_to_course(self):
        result = self.student.enroll("Math",['New_note'])

        self.assertEqual("Course already added. Notes have been updated.",result)
        self.assertEqual(['note1','note2','New_note'], self.student.courses['Math'])

    def test_enroll_with_new_course_adds_course_with_notes(self):
        course = 'FrontEnd'
        notes = ['FE1','FE2']

        result = self.student.enroll(course,notes,'Y')
        self.assertEqual("Course and course notes have been added.",result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes,self.student.courses[course])

    def test_enroll_new_course_with_empty_string(self):
        course = 'FrontEnd'
        notes = ['FE1', 'FE2']

        result = self.student.enroll(course, notes, '')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_new_course_without_note(self):
        course = 'FrontEnd'
        result = self.student.enroll(course,['FE1', 'FE2'],'N')

        self.assertEqual("Course has been added.",result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual([],self.student.courses[course])


    def test_add_notes_adds_notes_to_existing_course(self):
        result = self.student.add_notes("Math", 'extra note')
        self.assertEqual("Notes have been updated",result)
        self.assertEqual(['note1','note2','extra note'], self.student.courses['Math'])

    def test_add_notes_adds_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("English",'extra note')
        self.assertEqual("Cannot add notes. Course not found.",str(ex.exception))


    def test_leave_course_removes_the_course_from_the_student(self):
        result = self.student.leave_course('Math')
        self.assertEqual("Course has been removed", result)
        self.assertTrue('Math' not in self.student.courses)
        #self.assertTrue(len(self.student.courses) > 0)

    def test_leave_course_doesnt_exist_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("History")
        self.assertEqual("Cannot remove course. Course not found.",str(ex.exception))




if __name__ == "__main__":
    main()
