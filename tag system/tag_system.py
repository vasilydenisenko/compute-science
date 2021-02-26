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




def rule(string, production, m):
	out_str = string
	if production[0] == out_str[0]:
		out_str = string[m:]
		out_str += production[1]
	return out_str
				
				
				
def process(string, productions, m, halt, steps):
	out_str = string
	out_str_l = list()
	out_str_l.append(out_str)
	while not halt(out_str):
		for i in range(productions.__len__()):
			if productions[i][0] == out_str[0]:
				out_str = rule(out_str, productions[i], m)
				if steps:
					out_str_l.append(out_str)
	if not steps:
		out_str_l.append(out_str)
	return out_str_l