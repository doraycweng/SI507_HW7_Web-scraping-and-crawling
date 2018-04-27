# 507/206 Homework 7 Part 2
import json

count = 0
#### Your Part 2 solution goes here ####
f = open('directory_dict.json', 'r')
f_contents = f.read()
f_diction = json.loads(f_contents)
f.close()

for person in f_diction:
	if f_diction[person]["title"] == "PhD student":
		count += 1 

#### Your answer output (change the value in the variable, count)####
print('The number of PhD students: ', count)
