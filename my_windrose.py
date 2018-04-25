#!/usr/bin/env python
# my_windrose
# This is library to plot windrose from list data
# Author : Imam Kurniawan 

import numpy as np
import matplotlib.cm as cm
from matplotlib.pyplot import figure, show, rc
import matplotlib.pyplot as plt

# fungsi menggambar plot windrose
# count_wind_dir = jumlah wind direction = 4, 8, atau 16
# l1 - l6 = variabel dengan tipe data list yang berisi persentase distribusi angin berdasarkan kecepatan
# 		l1 : ws > 25 Knots
# 		l2 : ws (20-25 Knots)
# 		l3 : ws (15-20 Knots)
# 		l4 : ws (10-15 Knots)
# 		l5 : ws (5-10 Knots)
# 		l6 : ws (0.97-5 Knots)
# legend_loc = lokasi legend akan ditampilkan
#		Location String	Location Code
# 		‘best’			0
#		‘upper right’	1
#		‘upper left’	2
#		‘lower left’	3
#		‘lower right’	4
#		‘right’			5
#		‘center left’	6
#		‘center right’	7
#		‘lower center’	8
#		‘upper center’	9
#		‘center’		10
#
def plotWindrose(count_wind_dir,l1,l2,l3,l4,l5,l6,legend_loc):
	# force square figure and square axes looks better for polar, IMO
	# figsize = panjang x lebar frame
	fig = figure(figsize=(8,8)) 
	# posisi (koordinat grafik)
	ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True) 

	ax.set_xticklabels(['East','NE','North','NW','West','SW','South','SE'])
	ax.set_title("Wind speed distribution\n", va='bottom')
	# ax.set_yticklabels(['20%','40%','60%','80%','100%'])
	# Jumlah wind direction = 4,8, dan 16
	N = count_wind_dir 
	theta = np.arange(0.0, 2*np.pi, 2*np.pi/N)
	# radii = 10*np.random.rand(N)

	# Ukuran lebar bar grafik
	# jika N = 16 -> bar_width = 0.4
	# jika N = 8 -> bar_width = 0.8
	bar_width = 0.8

	def six_times(l1,l2,l3,l4,l5,l6):
		return l1+l2+l3+l4+l5+l6
	li1 = list(map(six_times,l1,l2,l3,l4,l5,l6))
	a = np.array( li1 )
	radii = a
	width = np.pi/4*np.random.rand(N)
	bars = ax.bar(theta, radii, width=bar_width, bottom=0.0)
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
	bars = ax.bar(theta, radii, width=bar_width, bottom=0.0)
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
	bars = ax.bar(theta, radii, width=bar_width, bottom=0.0)
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
	bars = ax.bar(theta, radii, width=bar_width, bottom=0.0)
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
	bars = ax.bar(theta, radii, width=bar_width, bottom=0.0)
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
	bars = ax.bar(theta, radii, width=bar_width, bottom=0.0)
	for r,bar in zip(radii, bars):
	    #bar.set_facecolor( cm.jet(r/10.))
	    bar.set_facecolor('#00FFFF')
	    bar.set_alpha(1)
	    bar.set_edgecolor('#000000')
	    bar.set_linewidth(0.5)

	ax.legend(['> 25 Knots','20 - 25 Knots','15 - 20 Knots','10 - 15 Knots','5 - 10 Knots', '0.9 - 5 Knots'], loc=legend_loc, title='Wind Speed')
	plt.savefig('figures/windrose_8d.png',dpi=300)
	show()


# Sample to use
# li = Percentage of windspeed distribution
# N = 16
# li = [E,67.5,NE,22.5,N,'','NW','','W','','SW','','S','','SE','']
# N = 8
# li = [E,NE,N,NW,W,SW,S,SE]
count_wind_dir = 8
li1 = [10,20,30,40,50,60,70,80] 	
li2 = [0,0,0,0,0,0,0,0]    	
li3 = [0,0,0,0,0,0,0,0]    	
li4 = [0,0,0,0,0,0,0,0]    	
li5 = [0,0,0,0,0,0,0,0]   		
li6 = [0,0,0,0,0,0,0,0]
legend_loc = 1

plotWindrose(count_wind_dir,li1,li2,li3,li4,li5,li6,legend_loc)
