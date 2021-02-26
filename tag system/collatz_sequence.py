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



# Example of simple 2-tag system which computes modified version of Collatz 
# sequence. Tag system production rules are taken from 
# https://en.wikipedia.org/wiki/Tag_system 


import tag_system
import sys
import re



productions = (	('a', 'bc'),
				('b', 'a'),
				('c', 'aaa'))



def halt(string):
	if string.__len__() < 2:
		return True
	return False		
	
	
	
def main():
	initial_num = int(sys.argv[1])	
	initial_str = 'a' * initial_num
	out_l = tag_system.process(initial_str, productions, 2, halt, True)
	print('Tag system operation steps results:')
	print(out_l)
	collatz_seq = list()
	for i in range(out_l.__len__()):
		res = re.fullmatch('a+', out_l[i])
		if res:
			collatz_seq.append(res[0].__len__())
	print()
	print(f'Modified version of the Collatz sequence for {initial_num} is') 
	print(collatz_seq)
	
	
	
main()