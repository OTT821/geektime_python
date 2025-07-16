attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']
          ]
result = []
for value in values:
    d = {}
    for i, attribute in enumerate(attributes):
        d[attribute] = value[i]
    result.append(d)
print(result)


result = [{attribute: value[i] for i, attribute in enumerate(attributes)} for value in values]
print(result)