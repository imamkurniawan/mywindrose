#!/usr/bin/env python

import numpy as np
import matplotlib.cm as cm
from matplotlib.pyplot import figure, show, rc
import matplotlib.pyplot as plt


# force square figure and square axes looks better for polar, IMO
fig = figure(figsize=(8,8)) # panjang x lebar frame
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True) # posisi (koordinat grafik)

ax.set_xticklabels(['East','NE','North','NW','West','SW','South','SE'])
ax.set_title("WInd speed distribution\nMarch 2018", va='bottom')
ax.set_yticklabels(['2%','4%','6%','8%','10%'])

N = 8 # Jumlah direction
theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
# radii = 10*np.random.rand(N)
li1 = [0,0,0,0,0,0,0,0] # ws > 25 Knots
a = np.array( li1 )
radii = a
width = np.pi/4*np.random.rand(N)
bars = ax.bar(theta, radii, width=0.8, bottom=0.0)
for r,bar in zip(radii, bars):
    #bar.set_facecolor( cm.jet(r/10.))
    bar.set_facecolor('#FF0000')
    bar.set_alpha(1)
    bar.set_edgecolor('#000000')
    bar.set_linewidth(0.5)

li2 = [0,0,0,0,0,0,0,0]    # ws (20-25 Knots)
a = np.array( li2 )
radii = a
width = np.pi/4*np.random.rand(N)
bars = ax.bar(theta, radii, width=0.8, bottom=0.0)
for r,bar in zip(radii, bars):
    #bar.set_facecolor( cm.jet(r/10.))
    bar.set_facecolor('#FF7331')
    bar.set_alpha(1)
    bar.set_edgecolor('#000000')
    bar.set_linewidth(0.5)

li3 = [0,0,0,0,0,0,0,0]    # ws (15-20 Knots)
a = np.array( li3 )
radii = a
width = np.pi/4*np.random.rand(N)
bars = ax.bar(theta, radii, width=0.8, bottom=0.0)
for r,bar in zip(radii, bars):
    #bar.set_facecolor( cm.jet(r/10.))
    bar.set_facecolor('#FFFE25')
    bar.set_alpha(1)
    bar.set_edgecolor('#000000')
    bar.set_linewidth(0.5)

li4 = [0,0,0,0,0,0,0,0]    # ws (10-15 Knots)
a = np.array(li4)
radii = a
width = np.pi/4*np.random.rand(N)
bars = ax.bar(theta, radii, width=0.8, bottom=0.0)
for r,bar in zip(radii, bars):
    #bar.set_facecolor( cm.jet(r/10.))
    bar.set_facecolor('#098122')
    bar.set_alpha(1)
    bar.set_edgecolor('#000000')
    bar.set_linewidth(0.5)

li5 = [0,0,0,0.3,0,0,3.2,7.1]    # ws (5-10 Knots)
a = np.array (li5)
radii = a
width = np.pi/4*np.random.rand(N)
bars = ax.bar(theta, radii, width=0.8, bottom=0.0)
for r,bar in zip(radii, bars):
    #bar.set_facecolor( cm.jet(r/10.))
    bar.set_facecolor('#000BE7')
    bar.set_alpha(1)
    bar.set_edgecolor('#000000')
    bar.set_linewidth(0.5)

li6 = [0,0,0,0.1,0,0,2.2,5.1]    # ws (0.97-5 Knots)
a = np.array (li6)
radii = a
width = np.pi/4*np.random.rand(N)
bars = ax.bar(theta, radii, width=0.8, bottom=0.0)
for r,bar in zip(radii, bars):
    #bar.set_facecolor( cm.jet(r/10.))
    bar.set_facecolor('#00FFFF')
    bar.set_alpha(1)
    bar.set_edgecolor('#000000')
    bar.set_linewidth(0.5)

'''
print (type(a))
print (radii)
print (a)
print (theta)
print (bars)
'''
ax.legend(['> 25 Knots','20 - 25 Knots','15 - 20 Knots','10 - 15 Knots','5 - 10 Knots', '0.9 - 5 Knots'], loc='upper right')
plt.savefig('figures/windrose_8d.png',dpi=300)
show()
