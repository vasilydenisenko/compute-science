# MIT License

# Copyright (c) 2021 Vasily Denisenko

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.




def rule(word, production, m):
	if production[0] == word[0]:
		out_word = word[m:] + production[1]
		return (out_word, True)
	out_word = word
	return (out_word, False)
				
				
				
def process(word, productions, m, halt, steps):
	rules_applied = True
	res = (word, True)
	word_l = list()
	word_l.append(word)
	while not halt(res[0]):
		for i in range(productions.__len__()):
			res = rule(res[0], productions[i], m)
			rules_applied = res[1]
			if steps and rules_applied:
				word_l.append(res[0])
	if not steps:
		word_l.append(res[0])
	return word_l