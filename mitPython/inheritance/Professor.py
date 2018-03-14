class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        newUtterance = 'In course ' + self.department + ' we say '
        return MITPerson.speak(self, newUtterance + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)


faculty = Professor('Doctor Arrogant', 'six')
print(m1.speak('hi there'))
print(s1.speak('hi there'))
print(faculty.speak('hi there'))
print(faculty.lecture('hi there'))
