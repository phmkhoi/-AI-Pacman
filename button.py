import pygame

class Button():
	def __init__(self, pos, img):
		self.x_pos = pos[0]
		self.y_pos = pos[1]

		self.img = img

	def render(self, screen):
		screen.blit(self.img, (self.x_pos, self.y_pos))

	def update(self, position):
		self.x_pos, self.y_pos = position