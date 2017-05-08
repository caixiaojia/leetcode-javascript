# -*- coding: UTF-8 -*-
import os

filename = './README.md'
filepath = '../problems/'
if not os.path.isfile(filename):
    exit(-1)
git_url = ' [javascript](https://github.com/caixiaojia/leetcode-javascript/blob/master/problems/%s) '

f = open(filename, 'r')
content = f.readlines()
for index in range(len(content) - 1):
    if index >= 10:
        contentArr = content[index].split('|')
        # index 3: javascript url
        name = contentArr[2].split('/')[4] + '.js'
        # newFile = open(filepath + name, 'w')
        # newFile.close()
        problem_url = git_url % name
        contentArr[3] = problem_url
        # contentArr.pop(4)
        contentArr[4] = " <font color='#A52A2A'>unsolved</font> "
        line = "|".join(contentArr)
        content[index] = line
f.close()

print content
w = open(filename, 'w')
w.writelines(content)
w.flush()
w.close()
