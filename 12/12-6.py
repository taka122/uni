sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
                  }
               }
            }
         }


def getmarksitem(subject):
    marks = sampleDict["class"]["student"]["marks"]
    mark = marks[subject]
    return mark


a = "history"
print(getmarksitem(a))  # 80
