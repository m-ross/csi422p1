# d,D = rotate body
# h,H = rotate head
# f,F = rotate forelegs
# g,G = rotate forelegs below elbow
# b,B = rotate hind leg
# n,N = rotate hind leg below knee
# t,T = rotate tail

#import basic OpenGL functionality
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *
import numpy as np

window_width = 500.0
window_hight = 500.0

color = [0.0, 1.0, 1.0]

class Dog:

	def __init__(self):

		self.body = 0
		self.head = 180
		self.tail = 0
		self.leg_b_r_upper = 270
		self.leg_b_r_lower = 180
		self.leg_b_l_upper = 270
		self.leg_b_l_lower = 180
		self.leg_f_r_upper = 90
		self.leg_f_r_lower = 180
		self.leg_f_l_upper = 90
		self.leg_f_l_lower = 180

	def initGL(self):

		glClearColor (0.0, 0.0, 0.0, 0.0)
		glShadeModel (GL_FLAT)
		glOrtho(0, 500, 0, 500, 0, 500)

	def display(self):

		glClear (GL_COLOR_BUFFER_BIT)
		glPushMatrix()
		glTranslatef (-1.0, 0.0, 0.0)
		glRotatef (self.body, 0.0, 0.0, 1.0)
		glTranslatef (1.0, 0.0, 0.0)
		glPushMatrix()
		glScalef (4.0, 1.0, 1.0)
		glutWireCube (1.0)
		glPopMatrix()

		glPushMatrix()
		glTranslatef (-1.4, 0.3, 0.0)
		glRotatef (self.head, 0.0, 0.0, 1.0)
		glTranslatef (1.4, 0.0, 0.0)
		glPushMatrix()
		glScalef (1.0, 0.5, 0.5)
		glutWireCube (1.0)
		glPopMatrix()
		glPopMatrix()

		glPushMatrix()
		glTranslatef (1.3, 0.325, -0.3)
		glRotatef (self.leg_b_r_upper, 0.0, 0.0, 1.0)
		glTranslatef (1.3, 0.0, 0.0)
		glPushMatrix()
		glScalef (0.75, 0.2, 0.2)
		glutWireCube (1.0)
		glPopMatrix()

		glPushMatrix()
		glTranslatef (0.325, 0.0, 0.0)
		glRotatef (self.leg_b_r_lower, 0.0, 0.0, 1.0)
		glTranslatef (-0.325, 0.0, 0.0)
		glPushMatrix()
		glScalef (0.75, 0.2, 0.2)
		glutWireCube (1.0)
		glPopMatrix()
		glPopMatrix()
		glPopMatrix()

		glPushMatrix()
		glTranslatef (1.3, 0.325, 0.3)
		glRotatef (self.leg_b_l_upper, 0.0, 0.0, 1.0)
		glTranslatef (1.3, 0.0, 0.0)
		glPushMatrix()
		glScalef (0.75, 0.2, 0.2)
		glutWireCube (1.0)
		glPopMatrix()

		glPushMatrix()
		glTranslatef (0.325, 0.0, 0.0)
		glRotatef (self.leg_b_l_lower, 0.0, 0.0, 1.0)
		glTranslatef (-0.325, 0.0, 0.0)
		glPushMatrix()
		glScalef (0.75, 0.2, 0.2)
		glutWireCube (1.0)
		glPopMatrix()
		glPopMatrix()
		glPopMatrix()

		glPushMatrix()
		glTranslatef (-1.3, 0.325, -0.3)
		glRotatef (self.leg_f_r_upper, 0.0, 0.0, 1.0)
		glTranslatef (-1.3, 0.0, 0.0)
		glPushMatrix()
		glScalef (0.75, 0.2, 0.2)
		glutWireCube (1.0)
		glPopMatrix()

		glPushMatrix()
		glTranslatef (-0.325, 0.0, 0.0)
		glRotatef (self.leg_f_r_lower, 0.0, 0.0, 1.0)
		glTranslatef (0.325, 0.0, 0.0)
		glPushMatrix()
		glScalef (0.75, 0.2, 0.2)
		glutWireCube (1.0)
		glPopMatrix()
		glPopMatrix()
		glPopMatrix()

		glPushMatrix()
		glTranslatef (-1.3, 0.325, 0.3)
		glRotatef (self.leg_f_l_upper, 0.0, 0.0, 1.0)
		glTranslatef (-1.3, 0.0, 0.0)
		glPushMatrix()
		glScalef (0.75, 0.2, 0.2)
		glutWireCube (1.0)
		glPopMatrix()

		glPushMatrix()
		glTranslatef (-0.325, 0.0, 0.0)
		glRotatef (self.leg_f_l_lower, 0.0, 0.0, 1.0)
		glTranslatef (0.325, 0.0, 0.0)
		glPushMatrix()
		glScalef (0.75, 0.2, 0.2)
		glutWireCube (1.0)
		glPopMatrix()
		glPopMatrix()
		glPopMatrix()

		glPushMatrix()
		glTranslatef (1.4, 0.3, 0.0)
		glRotatef (self.tail, 0.0, 1.0, 0.0)
		glTranslatef (1.4, 0.0, 0.0)
		glPushMatrix()
		glScalef (1.5, 0.15, 0.15)
		glutWireCube (1.0)
		glPopMatrix()
		glPopMatrix()

		glPopMatrix()
		glutSwapBuffers()


	def reshape (self, w, h):

		glViewport (0, 0, w, h)		#Defines a pixel rectangle in the window into which the final image is mapped. The (x, y) parameter specifies the lower-left corner of the viewport, and width and height are the size of the viewport rectangle. By default, the initial viewport values are (0, 0, winWidth, winHeight), where winWidth and winHeight are the size of the window.
		glMatrixMode (GL_PROJECTION)
		glLoadIdentity ()
		gluPerspective(95.0, w/h, 1, 20.0) #GLdouble fovy, GLdouble aspect, GLdouble zNear, GLdouble zFar
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glTranslatef (0.0, 0.0, -5.0)


	def keyboard (self, *args):

		if (args[0] == 'd'):
			self.body = (self.body - 5) % 360
			self.body = (self.body - 5) % 360
		elif (args[0] == 'D'):
			self.body = (self.body + 5) % 360
			self.body = (self.body + 5) % 360

		if (args[0] == 'H' and self.head >= 150):
			self.head = (self.head - 5) % 360
			self.head = (self.head - 5) % 360
		elif (args[0] == 'h' and self.head <= 210):
			self.head = (self.head + 5) % 360
			self.head = (self.head + 5) % 360

		if (args[0] == 'b' and self.leg_b_r_upper >= 235):
			self.leg_b_r_upper = (self.leg_b_r_upper - 5) % 360
			self.leg_b_l_upper = (self.leg_b_l_upper - 5) % 360
		elif (args[0] == 'B' and self.leg_b_r_upper <= 325):
			self.leg_b_r_upper = (self.leg_b_r_upper + 5) % 360
			self.leg_b_l_upper = (self.leg_b_l_upper + 5) % 360

		if (args[0] == 'n' and self.leg_b_r_lower > 180):
			self.leg_b_r_lower = (self.leg_b_r_lower - 5) % 360
			self.leg_b_l_lower = (self.leg_b_l_lower - 5) % 360
		elif (args[0] == 'N' and self.leg_b_r_lower < 270):
			self.leg_b_r_lower = (self.leg_b_r_lower + 5) % 360
			self.leg_b_l_lower = (self.leg_b_l_lower + 5) % 360

		if (args[0] == 'f' and self.leg_f_r_upper >= 45):
			self.leg_f_r_upper = (self.leg_f_r_upper - 5) % 360
			self.leg_f_l_upper = (self.leg_f_l_upper - 5) % 360
		elif (args[0] == 'F' and self.leg_f_r_upper <= 125):
			self.leg_f_r_upper = (self.leg_f_r_upper + 5) % 360
			self.leg_f_l_upper = (self.leg_f_l_upper + 5) % 360

		if (args[0] == 'g' and self.leg_f_r_lower > 180):
			self.leg_f_r_lower = (self.leg_f_r_lower - 5) % 360
			self.leg_f_l_lower = (self.leg_f_l_lower - 5) % 360
		elif (args[0] == 'G' and self.leg_f_r_lower < 270):
			self.leg_f_r_lower = (self.leg_f_r_lower + 5) % 360
			self.leg_f_l_lower = (self.leg_f_l_lower + 5) % 360

		if (args[0] == 't' and (self.tail >= 330 or self.tail <= 50)):
			self.tail = (self.tail - 5) % 360
			self.tail = (self.tail - 5) % 360
		elif (args[0] == 'T' and (self.tail >= 310 or self.tail <= 30)):
			self.tail = (self.tail + 5) % 360
			self.tail = (self.tail + 5) % 360

		glutPostRedisplay()


	def main(self):

		glutInit(sys.argv)					#initial the system
		glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)

		glutInitWindowSize(int(window_width), int(window_hight))			#initial window size
		glutInitWindowPosition(100, 100)			#initial window position

		glutCreateWindow("ICSI 422 Transformer Dog")	 #assign a title for the window

		self.initGL()

		glutDisplayFunc(self.display)
		glutReshapeFunc(self.reshape)
		glutKeyboardFunc(self.keyboard)

		glutMainLoop()						#callback function enter the GLUT event processing loop

if __name__ == "__main__":

	dog = Dog() #call the main function
	dog.main()
