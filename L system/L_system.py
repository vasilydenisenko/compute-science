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




def gen(variables, constants, axiom, rules, iteration):	
	if iteration == 0:
		L_string = axiom
		
	prev_string = axiom
	for itr in range(iteration):
		L_string = ''
		for i in range(prev_string.__len__()):
			cur_string = rules(variables, constants, prev_string[i])
			L_string += cur_string
		prev_string = L_string
	return L_string			
			
			
	
# Turtle's instruction set:
#	
# F : draw segment with step length
# G : draw segment with step length
# M : miss (do not draw) segment	
# R : turn right at angle
# L : turn left at angle
# [ : push current position and orientation on stack
# ] : pop position and orientation from stack
def draw(turtle, instruction, step, angle, stack):
	for i in range(instruction.__len__()):
		if 	instruction[i] == 'F' or instruction[i] == 'G':
			turtle.forward(step)
		elif instruction[i] == 'M':
			turtle.penup()
			turtle.forward(step)
			turtle.pendown()
		elif instruction[i] == 'R':
			turtle.right(angle)
		elif instruction[i] == 'L':
			turtle.left(angle)
		elif instruction[i] == '[':
			cur_pos = turtle.pos()
			cur_ang = turtle.heading()
			stack_item = (cur_pos, cur_ang)
			stack.append(stack_item)
		elif instruction[i] == ']':
			stack_item = stack[-1]
			prev_pos = stack_item[0]
			prev_angle = stack_item[1]
			turtle.penup()
			turtle.setpos(prev_pos)
			turtle.setheading(prev_angle)
			turtle.pendown()
			del stack[-1]
					
			
			
			
			
			