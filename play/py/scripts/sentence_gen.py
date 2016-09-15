# credit: Fluent Python

import re

RE_WORD = re.compile('\w+')

class Sentence:
  def __init__(self, text):
    self.text = text
  def __repr__(self):
    return "Sentence(%s)" % repr(self.text)

# one way to go: use generator function
#
  def __iter__(self):
    for m in RE_WORD.finditer(self.text):
      yield m.group()

#  another way to go: use generator expression
#
#  def __iter__(self):
#    return (m.group() for m in RE_WORD.finditer(self.text))


s = Sentence("""
this is "foo bar" sent.
that is baz...
""")

print(s)
print(list(s))

