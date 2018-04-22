#!/usr/bin/env python

import numpy as np
import matplotlib.cm as cm
from matplotlib.pyplot import figure, show, rc
import matplotlib.pyplot as plt


def createWindrose(count_wind_dir,l1,l2,l3,l4,l5,l6,legend_loc):
	# force square figure and square axes looks better for polar, IMO
	fig = figure(figsize=(8,8)) # panjang x lebar frame
	ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True) # posisi (koordinat grafik)

	ax.set_xticklabels(['East','NE','North','NW','West','SW','South','SE'])
	ax.set_title("Wind speed distribution\n", va='bottom')
	# ax.set_yticklabels(['20%','40%','60%','80%','100%'])

	N = count_wind_dir # Jumlah direction
	theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
	# radii = 10*np.random.rand(N)

	def six_times(l1,l2,l3,l4,l5,l6):
		return l1+l2+l3+l4+l5+l6
	li1 = list(map(six_times,l1,l2,l3,l4,l5,l6))
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

	def five_times(l2,l3,l4,l5,l6):
		return l2+l3+l4+l5+l6
	li2 = list(map(five_times,l2,l3,l4,l5,l6))
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

	def four_times(l3,l4,l5,l6):
		return l3+l4+l5+l6
	li3 = list(map(four_times,l3,l4,l5,l6))
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

	def three_times(l4,l5,l6):
		return l4+l5+l6
	li4 = list(map(three_times,l4,l5,l6))
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

	def two_times(l5,l6):
		return l5+l6
	li5 = list(map(two_times,l5,l6))
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

	li6 = l6
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


	ax.legend(['> 25 Knots','20 - 25 Knots','15 - 20 Knots','10 - 15 Knots','5 - 10 Knots', '0.9 - 5 Knots'], loc=legend_loc)
	plt.savefig('figures/windrose_8d.png',dpi=300)
	show()

count_wind_dir = 16
li1 = [10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 		# ws > 25 Knots
li2 = [50.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    		# ws (20-25 Knots)
li3 = [50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    		# ws (15-20 Knots)
li4 = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    	# ws (10-15 Knots)
li5 = [300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]   		# ws (5-10 Knots)
li6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]   # ws (0.97-5 Knots)
legend_loc = 'lower right'

createWindrose(count_wind_dir,li1,li2,li3,li4,li5,li6,legend_loc)
