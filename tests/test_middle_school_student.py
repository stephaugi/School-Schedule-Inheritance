from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Emma"
    grade = "8th grader"
    classes = ["Science"]

    # Act
    emma = MiddleSchoolStudent(name, grade, classes)

    assert emma.name == name
    assert emma.grade == grade
    assert emma.classes == classes
    assert len(emma.classes) == 1
    assert not emma.gets_transportation

def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Emma"
    grade = "8th grader"
    classes = ["Science"]

    # Act
    emma = MiddleSchoolStudent(name, grade, classes, True)

    summary = emma.summary()

    assert summary == "Emma is a 8th grader enrolled in 1 classes: Science\nEmma gets transportation."

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Emma"
    grade = "8th grader"
    classes = ["Science"]

    # Act
    emma = MiddleSchoolStudent(name, grade, classes)

    summary = emma.summary()

    assert summary == "Emma is a 8th grader enrolled in 1 classes: Science\nEmma doesn't get transportation."

