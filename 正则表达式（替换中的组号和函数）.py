import re
emphasis_pattern = re.compile(r'''
\*                          #起始突出标志————一个星号
(                           #与要突出的内容匹配的编组的起始位置
[^\*]+                      #与除星号外的其他字符都匹配
)                           #编组到此结束
\*                          #结束突出标志—————一个星号
\*''', re.VERBOSE)
print(emphasis_pattern)
print(re.sub(emphasis_pattern, r'<em>\1<em>', 'hello, *world*!'))

