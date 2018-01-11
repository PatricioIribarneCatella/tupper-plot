#!/usr/bin/env python

import sys
import matplotlib.pyplot as plot

def plot_tupper():

	N = 4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300
	H = 17
	W = 106

	def tupper(x, y):
		return 0.5 < ((y//H) // (2**(H*x + y%H))) % 2

	print "x range: 0 < x < %d, (type 0 for default witdth)" % W,
	r = int(raw_input())
	if r:
		W = r
		print 'Got width: %d' % W
	
	print "y range: N < y < N+%d, where N = (type 0 for default)" % H,
	t = int(raw_input())
	if t: N=t
	
	print

	plot.rc('patch', antialiased=False)
	
	print 'Plotting...'
	
	for x in xrange(W):
		for yy in xrange(H):
			y = N + yy
			if tupper(x,y):
				plot.bar(left=x, bottom=yy, height=1, width=1, linewidth=0, color='black')
	
	print 'Done plotting, please wait...'

	plot.axis('scaled')
	buf = 2
	plot.xlim((-buf,W+buf))
	plot.ylim((-buf,H+buf))
	plot.rc('font', size=10)
	plot.xticks(range(0, W, 100))
	yticks = range(0, H+1, 4)
	plot.yticks(yticks, ['N']+['N + %d'%i for i in yticks][1:])

	plot.savefig('out.png')
	plot.savefig('out.svg')

if __name__ == '__main__':
	plot_tupper()