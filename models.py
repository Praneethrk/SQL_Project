from collections import namedtuple

Internship = namedtuple("Intership", ["id","iname", "company", "i_year","status"])
Student = namedtuple("Student", ["usn", "name", "sem","placed"])
Register = namedtuple("Register",["iid","usn","status"])
Company = namedtuple("Company",["company","count"])
StudentCount = namedtuple("StudentCount",["usn","name","count"])
Report = namedtuple("Report",["usn","name","iname","company","i_year"])