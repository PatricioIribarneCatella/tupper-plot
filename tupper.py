#!/usr/bin/env python3

import sys
import os

import matplotlib.pyplot as plot

def tupper_belongs(x, y, H):
    return 0.5 < ((y//H) // (2**(H*x + y%H))) % 2

def get_data():

    # Tupper´s number for tupper´s plot
    N = 4858450636189713423582095962494202044581400587983244549483093085061934704708809928450644769865524364849997247024915119110411605739177407856919754326571855442057210445735883681829823754139634338225199452191651284348332905131193199953502413758765239264874613394906870130562295813219481113685339535565290850023875092856892694555974281546386510730049106723058933586052544096664351265349363643957125565695936815184334857605266940161251266951421550539554519153785457525756590740540157929001765967965480064427829131488548259914721248506352686630476300
    H = 17 # height
    W = 106 # width

    r = int(input("x range: 0 < x < {}, (type 0 for default width): ".format(W)))

    if r:
        W = r
        print('Width set to: {}'.format(W))
    
    t = int(input("y range: N < y < N+{}, where N = (type 0 for default): ".format(H)))

    if t:
        N = t

    print("\n")

    return (N, H, W)

def tupper_plot(N, H, W):

    plot.rc('patch', antialiased=False)
    
    print('Plotting started')
    
    for x in range(W):
        for yy in range(H):
            y = N + yy
            if tupper_belongs(x, y, H):
                plot.bar(x=x, bottom=yy,
                         height=1, width=1,
                         linewidth=0, color='black')
    
    print('Plotting finished. Generating images...')

    plot.axis('scaled')
    
    limit = 2
    plot.xlim((-limit, W + limit))
    plot.ylim((-limit, H + limit))
    
    plot.rc('font', size=10)
    
    plot.xticks(range(0, W, 100))
    
    yticks = range(0, H + 1, 4)
    plot.yticks(yticks, ['N']+['N + %d' %i for i in yticks][1:])

    # Creates the directory for saving the images
    if not os.path.exists("images/"):
        os.makedirs("images/")

    # Save plot into different images format
    plot.savefig('images/out.png')
    plot.savefig('images/out.svg')

def tupper():

    (N, H, W) = get_data()

    tupper_plot(N, H, W)	

if __name__ == '__main__':
    tupper()

