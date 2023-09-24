import unittest
from project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.student = Student('Student', {'course_name': ['notes']})

    def test_initialisation(self):
        self.assertEqual('Student', self.student.name)
        self.assertEqual({'course_name': ['notes']}, self.student.courses)

    def test_if_course_already_exists_and_add_additional_notes(self):
        result = self.student.enroll('course_name', ['second_note'])
        self.assertEqual('second_note', self.student.courses['course_name'][1])
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test_if_add_notes_in_new_course(self):
        result = self.student.enroll('new_course', ['notes'])

        self.assertEqual('notes', self.student.courses['new_course'][0])
        self.assertEqual(result, 'Course and course notes have been added.')

    def test_if_add_notes_with_third_parameter_Y(self):
        result = self.student.enroll('new_course', ['notes'], 'Y')

        self.assertEqual('notes', self.student.courses['new_course'][0])
        self.assertEqual(result, 'Course and course notes have been added.')

    def test_when_course_added_but_without_notes(self):
        result = self.student.enroll('new_course', ['notes'], 'N')
        self.assertEqual(0, len(self.student.courses['new_course']))
        self.assertEqual(result, 'Course has been added.')

    def test_add_notes_in_existing_course(self):
        result = self.student.add_notes('course_name', 'other notes')
        self.assertEqual('other notes', self.student.courses['course_name'][1])
        self.assertEqual(result, 'Notes have been updated')

    def test_add_notes_in_non_existing_course(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes('other_course', 'other notes')
        self.assertEqual(str(context.exception), 'Cannot add notes. Course not found.')

    def test_remove_existing_course(self):
        result = self.student.leave_course('course_name')
        self.assertEqual({}, self.student.courses)
        self.assertEqual(result, 'Course has been removed')

    def test_remove_non_existing_course(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course('other_course')
        self.assertEqual(str(context.exception), 'Cannot remove course. Course not found.')


if __name__ == '__main__':
    unittest.main()