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



# Example of Tag system emulation by Cyclic Tag System. 
# Production rules are taken from 
# https://en.wikipedia.org/wiki/Tag_system 


import cts



productions = (	'010010',
				'100010001',
				'001',
				'',
				'',
				'')



codes_ts_cts = {	'a': '100',
					'b': '010',
					'H': '001'}



codes_cts_ts = {'100': 'a',
				'010': 'b',
				'001': 'H'}



def encode(word, codes):
	out_word = ''
	for i in range(word.__len__()):
		out_word += codes[word[i]]
	return out_word
	
	
	
def decode(word, codes):
	out_word = ''
	i = 3
	while i <= word.__len__():
		p_word = word[i-3:i]
		if p_word in codes:
			out_word += codes[p_word]
		i += 3
	return out_word
	

	
def main():
	initial_tag_system_word = 'ba'
	initial_cyclic_tag_system_word = encode(initial_tag_system_word, codes_ts_cts)
	print(initial_cyclic_tag_system_word)
	out_l = cts.process(initial_cyclic_tag_system_word, productions, 16)
	print('Cyclic Tag System operation steps results:')
	print(out_l)	
	print()
	print('Emulated Tag system operation steps results:')
	for i in range(out_l.__len__()):
		if i % 6 == 0:
			print(decode(out_l[i], codes_cts_ts))

	

main()	