# json to xml
import xmltodict

student = {
  "data" : {
    "name" : "Shubham",
    "marks" : {
      "math" : 92,
      "english" : 99
    },
    "id" : "s387hs3"
  }
}

print(xmltodict.unparse(student, pretty=True))
