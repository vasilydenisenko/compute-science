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



import L_system
import turtle




VARIABLES_Cantor = ('F', 'M')
CONSTANTS_Cantor = ('')
AXIOM_Cantor = 'F'

# F -> FMF
# M -> MMM
def RULES_Cantor(variables, constants, predecessor):
	successor = ''
	if predecessor == variables[0]:
		successor =	variables[0] \
					+ variables[1] \
					+ variables[0]
	if predecessor == variables[1]:
		successor =	variables[1] \
					+ variables[1] \
					+ variables[1]
	elif predecessor in constants:
		successor =	predecessor
	return successor




def main():
	screen = turtle.Screen()
	t = turtle.Turtle()
	t.speed('fastest')
	t.hideturtle()
	t.color('blue')

	order = 4
	STEP = 10
	if order > 1:
		STEP = STEP / 1.41421356**(order - 1)
	angle = 90	
	L_string = L_system.gen(VARIABLES_Cantor, 
							CONSTANTS_Cantor, 
							AXIOM_Cantor, 
							RULES_Cantor, 
							order)
	stack = list()							
	L_system.draw(t, L_string, STEP, angle, stack)
	
	input()

main()