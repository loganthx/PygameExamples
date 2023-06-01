import pygame as pg, numpy as np; pg.init()

# Defines Map and its Boundaries as Rects
Map, Rects = [ [1, 1, 1, 1] , [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1] ], []
for n_row, row in enumerate(Map):
	for n_col, col in enumerate(row):
		if col == 1: Rects.append(pg.Rect(n_col*150, n_row*150, 150, 150))

scr = (600,600); screen = pg.display.set_mode(scr)
theta, r, Pos = np.pi/6, 900, (300, 300)

def RayCaster(): # Casts rays from Pos toward angle theta, from -30º to 30º
	for n, i in enumerate(np.arange(-np.pi/6, np.pi/6 + 1e-4, np.pi/180)):
		C = [] # Clips list to Check if the clipped lines are correct
		Ray = (Pos[0] + r*np.cos(theta + i), Pos[1] + r*np.sin(theta+i))
		for Rect in Rects:
			clipped_line = Rect.clipline(Pos[0], Pos[1], Ray[0], Ray[1])
			if clipped_line:
				start, end = clipped_line; x1, y1 = start
				Distance = np.sqrt((Pos[0]-x1)**2 + (Pos[1] - y1)**2) + 1e-4; D = Distance
				C.append(D)

		if len(C)>0: D = min(C) #  Check if clipped lines are ok
		else: D = 1e6 # Else: then object is from really far away

		# Draws a rectangle for each angle parameters, defining height and color:
		dW = 11; dH = np.clip( 800 * (1/(0.02*D)), 0, scr[1])
		cVar = np.clip(355*(1/(0.01*D)), 0, 255)
		Color = [.8*cVar, .1*cVar, .1*cVar]
		RectDx = pg.Rect(n*scr[0], scr[1] - dH, dW, dH)
		RectDx.center = (n*dW, scr[1]/2); pg.draw.rect(screen, Color, RectDx)
        
while 1: # Basic Game Loop
	for e in pg.event.get(): 
		if e.type == pg.QUIT: pg.quit()
      
	RayCaster(); pg.display.update()
