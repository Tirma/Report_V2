import numpy as np
import pickle as pk
import matplotlib.pyplot as plt

simu=0
second = 0

x=[]
y=[]

if simu:
	with open("/home/thomas/Bureau/DBC/polychrom/no_fanout/inter_70_3365_3435_1pixel/Retrieved_data/BL12/BL12_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC/polychrom/no_fanout/inter_70_3365_3435_1pixel/Retrieved_data/BL13/BL13_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC/polychrom/no_fanout/inter_70_3365_3435_1pixel/Retrieved_data/BL14/BL14_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC/polychrom/no_fanout/inter_70_3365_3435_1pixel/Retrieved_data/BL23/BL23_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC/polychrom/no_fanout/inter_70_3365_3435_1pixel/Retrieved_data/BL24/BL24_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC/polychrom/no_fanout/inter_70_3365_3435_1pixel/Retrieved_data/BL34/BL34_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	plt.close('all')

	fig, ax = plt.subplots(2,3)#,figsize=(25,12))
	ax1 = ax[0][0]
	ax2 = ax[0][1]
	ax3 = ax[0][2]
	ax4 = ax[1][0]
	ax5 = ax[1][1]
	ax6 = ax[1][2]
	
	ytheo1 = np.linspace(2*np.pi, 0,250)
	ytheo2 = np.concatenate((ytheo1,ytheo1))
	ytheo = np.concatenate((ytheo2,ytheo2))
	ytheo = np.concatenate((ytheo,ytheo2))

	xtheo = np.linspace(-10.2,10.2,len(ytheo))
	
	title = ["$\phi_{12}$","$\phi_{13}$","$\phi_{14}$","$\phi_{23}$","$\phi_{24}$","$\phi_{34}$"]
	def std_me(x):
		return np.sqrt(np.mean(abs(x)**2))

	s = np.zeros(6)
	s2=s
	for i in range(6):
		
		residute = []
		close = []
		for j in range(len(x[i])):
			idx = np.where(abs(x[i][j]-xtheo-s2[i]) == np.min(abs(x[i][j]-xtheo-s2[i])))
			close.append(idx[0][0])
		#print(close)
		residute = np.array(ytheo)[close]-np.array(y[i])
		residute1 = residute[np.where(abs(residute)<1)]
		print(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-s[i])<5.6175)]))
		#plt.plot(residute), plt.show()
		eval('ax'+str(i+1)+'.plot(x['+str(i)+'],y['+str(i)+'],"+")')
		eval('ax'+str(i+1)+'.plot(xtheo+'+str(s2[i])+',ytheo,"--",linewidth=1)')
		eval('ax'+str(i+1)+'.set_title(r'+'"'+title[i]+'"'+')')
		eval('ax'+str(i+1)+'.set_xlim(['+str(-5.1+s[i])+','+str(5.1+s[i])+'])')
	
	#	print(x[i][close][np.where(abs(residute)<1)])
		eval('ax'+str(i+1)+'.plot((np.array(xtheo) + s2['+str(i)+'])[close][np.where(abs(residute)<1)],residute1,"--",label=r"$\sigma ={0:2f}$".format(np.std(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-s[i])<5.6175)])))')
		eval('ax'+str(i+1)+'.legend()')
		#eval('ax'+str(i+1)+'.set_title(r'+'"residute '+title[i]+'"'+')')
		eval('ax'+str(i+1)+'.set_xlim(['+str(-5.1+s[i])+','+str(5.1+s[i])+'])')

if not simu and not second and 0:
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/Retrieved_data/BL12_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/Retrieved_data/BL13_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/Retrieved_data/BL14_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/Retrieved_data/BL23_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/Retrieved_data/BL24_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/Retrieved_data/BL34_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	plt.close('all')

	fig, ax = plt.subplots(2,3)#,figsize=(25,12))
	ax1 = ax[0][0]
	ax2 = ax[0][1]
	ax3 = ax[0][2]
	ax4 = ax[1][0]
	ax5 = ax[1][1]
	ax6 = ax[1][2]
	
	ytheo1 = np.linspace(2*np.pi, 0,500)
	ytheo2 = np.concatenate((ytheo1,ytheo1))
	ytheo = np.concatenate((ytheo2,ytheo2))
	ytheo = np.concatenate((ytheo,ytheo2))

	xtheo = np.linspace(-11.235,11.235,len(ytheo))
	
	title = ["$\phi_{12}$","$\phi_{13}$","$\phi_{14}$","$\phi_{23}$","$\phi_{24}$","$\phi_{34}$"]
	s = [453.7,367.3,449,479,360.3,265]
	s2 = np.array([453.44,367.38,452.47,479.5,360.41,263.18])-3.745/2

	def std_me(x):
		return np.sqrt(np.mean(abs(x)**2))

	for i in range(6):
		
		residute = []
		close = []
		for j in range(len(x[i])):
			idx = np.where(abs(x[i][j]-xtheo-s2[i]) == np.min(abs(x[i][j]-xtheo-s2[i])))
			close.append(idx[0][0])
		#print(close)
		residute = np.array(ytheo)[close]-np.array(y[i])
		residute1 = residute[np.where(abs(residute)<1)]
		print(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-s[i])<5.6175)]))
		#plt.plot(residute), plt.show()
		eval('ax'+str(i+1)+'.plot(x['+str(i)+'],y['+str(i)+'],"+")')
		eval('ax'+str(i+1)+'.plot(xtheo+'+str(s2[i])+',ytheo,"--",linewidth=1)')
		eval('ax'+str(i+1)+'.set_title(r'+'"'+title[i]+'"'+')')
		eval('ax'+str(i+1)+'.set_xlim(['+str(-5.6175+s[i])+','+str(5.6175+s[i])+'])')
	
	#	print(x[i][close][np.where(abs(residute)<1)])
		eval('ax'+str(i+1)+'.plot((np.array(xtheo) + s2['+str(i)+'])[close][np.where(abs(residute)<1)],residute1,"--",label=r"$\sigma ={0:2f}$".format(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-s[i])<5.6175)])))')
		eval('ax'+str(i+1)+'.legend()')
		#eval('ax'+str(i+1)+'.set_title(r'+'"residute '+title[i]+'"'+')')
		eval('ax'+str(i+1)+'.set_xlim(['+str(-5.6175+s[i])+','+str(5.6175+s[i])+'])')

if not simu and second and 0:
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/12/Retrieved/12_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/13/Retrieved/13_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/14/Retrieved/14_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/23/Retrieved/23_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/24/Retrieved/24_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/34/Retrieved/34_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	plt.close('all')

	fig, ax = plt.subplots(2,3)#,figsize=(25,12))
	ax1 = ax[0][0]
	ax2 = ax[0][1]
	ax3 = ax[0][2]
	ax4 = ax[1][0]
	ax5 = ax[1][1]
	ax6 = ax[1][2]
	
	ytheo1 = np.linspace(0,2*np.pi,500)
	ytheo2 = np.concatenate((ytheo1,ytheo1))
	ytheo = np.concatenate((ytheo2,ytheo2))
	ytheo = np.concatenate((ytheo,ytheo2))

	xtheo = np.linspace(-11.235,11.235,len(ytheo))
	
	title = ["$\phi_{12}$","$\phi_{13}$","$\phi_{14}$","$\phi_{23}$","$\phi_{24}$","$\phi_{34}$"]
	s = [258.3,163.4,289,280.9,126,41.2]
	s2 = np.array([256.59,161.22,287.15,278.84,124.14,39.28])

	def std_me(x):
		return np.sqrt(np.mean(abs(x)**2))

	for i in range(6):
		
		residute = []
		close = []
		for j in range(len(x[i])):
			idx = np.where(abs(x[i][j]-xtheo-s2[i]) == np.min(abs(x[i][j]-xtheo-s2[i])))
			close.append(idx[0][0])
		#print(close)
		residute = np.array(ytheo)[close]-np.array(y[i])
		residute1 = residute[np.where(abs(residute)<1)]
		print(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-s[i])<5.6175)]))
		#plt.plot(residute), plt.show()
		eval('ax'+str(i+1)+'.plot(x['+str(i)+'],y['+str(i)+'],"+")')
		eval('ax'+str(i+1)+'.plot(xtheo+'+str(s2[i])+',ytheo,"--",linewidth=1)')
		eval('ax'+str(i+1)+'.set_title(r'+'"'+title[i]+'"'+')')
		eval('ax'+str(i+1)+'.set_xlim(['+str(-5.6175+s[i])+','+str(5.6175+s[i])+'])')
	
	#	print(x[i][close][np.where(abs(residute)<1)])
		eval('ax'+str(i+1)+'.plot((np.array(xtheo) + s2['+str(i)+'])[close][np.where(abs(residute)<1)],residute1,"--",label=r"$\sigma ={0:2f}$".format(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-s[i])<5.6175)])))')
		eval('ax'+str(i+1)+'.legend()')
		#eval('ax'+str(i+1)+'.set_title(r'+'"residute '+title[i]+'"'+')')
		eval('ax'+str(i+1)+'.set_xlim(['+str(-5.6175+s[i])+','+str(5.6175+s[i])+'])')

if 0:
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_2/Retrieved/12_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_2/Retrieved/13_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_2/Retrieved/14_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_2/Retrieved/23_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_2/Retrieved/24_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_2/Retrieved/34_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	plt.close('all')

	fig, ax = plt.subplots(2,3)#,figsize=(25,12))
	ax1 = ax[0][0]
	ax2 = ax[0][1]
	ax3 = ax[0][2]
	ax4 = ax[1][0]
	ax5 = ax[1][1]
	ax6 = ax[1][2]
	
	ytheo1 = np.linspace(2*np.pi,0,500)
	ytheo2 = np.concatenate((ytheo1,ytheo1))
	ytheo = np.concatenate((ytheo2,ytheo2))
	ytheo = np.concatenate((ytheo,ytheo2))

	xtheo = np.linspace(-11.235,11.235,len(ytheo))
	
	title = ["$\phi_{12}$","$\phi_{13}$","$\phi_{14}$","$\phi_{23}$","$\phi_{24}$","$\phi_{34}$"]
	s = [[x[0][0],x[0][-1]],[200-5.6175,200+5.6175],[x[2][0],x[2][-1]],[280-5.6175,280+5.6175],[x[4][0],x[4][-1]],[310-5.6175,310+5.6175]]
	s2 = np.array([256.39,200.12,287.05,280.74,124.04,311.52])
	def std_me(x):
		return np.sqrt(np.mean(abs(x)**2))

	for i in range(6):
		residute = []
		close = []
		for j in range(len(x[i])):
			idx = np.where(abs(x[i][j]-xtheo-s2[i]) == np.min(abs(x[i][j]-xtheo-s2[i])))
			close.append(idx[0][0])
		#print(close)
		
		if i==3:
			ytheo1 = np.linspace(0,2*np.pi,500)
			ytheo2 = np.concatenate((ytheo1,ytheo1))
			ytheo = np.concatenate((ytheo2,ytheo2))
			ytheo = np.concatenate((ytheo,ytheo2))		
		else:
			ytheo1 = np.linspace(2*np.pi,0,500)
			ytheo2 = np.concatenate((ytheo1,ytheo1))
			ytheo = np.concatenate((ytheo2,ytheo2))
			ytheo = np.concatenate((ytheo,ytheo2))				
		
		residute = np.array(ytheo)[close]-np.array(y[i])
		residute1 = residute[np.where(abs(residute)<1)]
		print(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-np.mean(s[i]))<5.6175)]))
		#plt.plot(residute), plt.show()
		eval('ax'+str(i+1)+'.plot(x['+str(i)+'],y['+str(i)+'],"+")')
		if  i%2:
			eval('ax'+str(i+1)+'.plot(xtheo+'+str(s2[i])+',ytheo,"--",linewidth=1)')
		eval('ax'+str(i+1)+'.set_title(r'+'"'+title[i]+'"'+')')
		#eval('ax'+str(i+1)+'.set_xlim(['+str(-5.6175+s[i])+','+str(5.6175+s[i])+'])')
		if  i%2:
	#	print(x[i][close][np.where(abs(residute)<1)])
			eval('ax'+str(i+1)+'.plot((np.array(xtheo) + s2['+str(i)+'])[close][np.where(abs(residute)<1)],residute1,"--",label=r"$\sigma ={0:2f}$".format(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-np.mean(s[i]))<5.6175)])))')
			eval('ax'+str(i+1)+'.legend()')
		else:
			eval('ax'+str(i+1)+'.plot(x['+str(i)+'],np.mean(y['+str(i)+'])*np.ones(len(x['+str(i)+'])),"--",label=r"$\sigma ={0:2f}$".format(std_me(y['+str(i)+']-np.mean(y['+str(i)+']))))')
			eval('ax'+str(i+1)+'.legend()')
		#eval('ax'+str(i+1)+'.set_title(r'+'"residute '+title[i]+'"'+')')
		eval('ax'+str(i+1)+'.set_xlim('+str(s[i])+')')
		eval('ax'+str(i+1)+'.set_ylim([-1,2*np.pi+1])')

if 0:
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/12_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/13_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/14_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/23_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/24_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/34_phase.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	plt.close('all')

	fig, ax = plt.subplots(2,3)#,figsize=(25,12))
	ax1 = ax[0][0]
	ax2 = ax[0][1]
	ax3 = ax[0][2]
	ax4 = ax[1][0]
	ax5 = ax[1][1]
	ax6 = ax[1][2]
	
	ytheo1 = np.linspace(2*np.pi,0,500)
	ytheo2 = np.concatenate((ytheo1,ytheo1))
	ytheo = np.concatenate((ytheo2,ytheo2))
	ytheo = np.concatenate((ytheo,ytheo2))

	xtheo = np.linspace(-11.235,11.235,len(ytheo))
	
	title = ["$\phi_{12}$","$\phi_{13}$","$\phi_{14}$","$\phi_{23}$","$\phi_{24}$","$\phi_{34}$"]
	s = [[x[0][0],x[0][-1]],[x[1][0],x[1][-1]],[70-5.6175,70+5.6175],[x[3][0],x[3][-1]],[140-5.6175,140+5.6175],[40-5.6175,40+5.6175]]
	s2 = np.array([256.39,200.12,67.8,280.74,139.04,41.1])
	def std_me(x):
		return np.sqrt(np.mean(abs(x)**2))

	for i in range(6):
		residute = []
		close = []
		for j in range(len(x[i])):
			idx = np.where(abs(x[i][j]-xtheo-s2[i]) == np.min(abs(x[i][j]-xtheo-s2[i])))
			close.append(idx[0][0])
		#print(close)
		
		if i>3:
			ytheo1 = np.linspace(0,2*np.pi,500)
			ytheo2 = np.concatenate((ytheo1,ytheo1))
			ytheo = np.concatenate((ytheo2,ytheo2))
			ytheo = np.concatenate((ytheo,ytheo2))		
		else:
			ytheo1 = np.linspace(2*np.pi,0,500)
			ytheo2 = np.concatenate((ytheo1,ytheo1))
			ytheo = np.concatenate((ytheo2,ytheo2))
			ytheo = np.concatenate((ytheo,ytheo2))				
		
		residute = np.array(ytheo)[close]-np.array(y[i])
		residute1 = residute[np.where(abs(residute)<2)]
		print(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-np.mean(s[i]))<5.6175)]))
		#plt.plot(residute), plt.show()
		eval('ax'+str(i+1)+'.plot(x['+str(i)+'],y['+str(i)+'],"+")')
		if  not(i<2 or i==3):
			eval('ax'+str(i+1)+'.plot(xtheo+'+str(s2[i])+',ytheo,"--",linewidth=1)')
		eval('ax'+str(i+1)+'.set_title(r'+'"'+title[i]+'"'+')')
		#eval('ax'+str(i+1)+'.set_xlim(['+str(-5.6175+s[i])+','+str(5.6175+s[i])+'])')
		if  not(i<2 or i==3):
	#	print(x[i][close][np.where(abs(residute)<1)])
			eval('ax'+str(i+1)+'.plot((np.array(xtheo) + s2['+str(i)+'])[close][np.where(abs(residute)<2)],residute1,"--",label=r"$\sigma ={0:2f}$".format(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-np.mean(s[i]))<5.6175)])))')
			eval('ax'+str(i+1)+'.legend()')
		else:
			eval('ax'+str(i+1)+'.plot(x['+str(i)+'],np.mean(y['+str(i)+'])*np.ones(len(x['+str(i)+'])),"--",label=r"$\sigma ={0:2f}$".format(std_me(y['+str(i)+']-np.mean(y['+str(i)+']))))')
			eval('ax'+str(i+1)+'.legend()')
		#eval('ax'+str(i+1)+'.set_title(r'+'"residute '+title[i]+'"'+')')
		eval('ax'+str(i+1)+'.set_xlim('+str(s[i])+')')
		eval('ax'+str(i+1)+'.set_ylim([-1,2*np.pi+1])')

if 1:
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/12.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/13.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/14.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/23.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())

	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/24.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	
	with open("/home/thomas/Bureau/DBC_measurement/39_7_compressor/For_Retrieve/4BL_1/Retrieved/34.pickle",'rb') as f:
		fig = pk.load(f)
	ax = fig.get_axes()
	ax = ax[0]
	ax = ax.get_children()[0]
	x.append(ax.get_xdata())
	y.append(ax.get_ydata())
	plt.close('all')

	fig, ax = plt.subplots(2,3)#,figsize=(25,12))
	ax1 = ax[0][0]
	ax2 = ax[0][1]
	ax3 = ax[0][2]
	ax4 = ax[1][0]
	ax5 = ax[1][1]
	ax6 = ax[1][2]
	
	ytheo1 = np.linspace(2*np.pi,0,500)
	ytheo2 = np.concatenate((ytheo1,ytheo1))
	ytheo = np.concatenate((ytheo2,ytheo2))
	ytheo = np.concatenate((ytheo,ytheo2))

	xtheo = np.linspace(-11.235,11.235,len(ytheo))
	
	title = ["$\phi_{12}$","$\phi_{13}$","$\phi_{14}$","$\phi_{23}$","$\phi_{24}$","$\phi_{34}$"]
	s = [[x[0][0],x[0][-1]],[x[1][0],x[1][-1]],[x[2][0],x[2][-1]],[x[3][0],x[3][-1]],[x[4][0],x[4][-1]],[x[5][0],x[5][-1]]]
	s2 = np.array([256.39,200.12,67.8,280.74,139.04,41.1])
	def std_me(x):
		return np.sqrt(np.mean(abs(x)**2))

	for i in range(6):
		residute = []
		close = []
		for j in range(len(x[i])):
			idx = np.where(abs(x[i][j]-xtheo-s2[i]) == np.min(abs(x[i][j]-xtheo-s2[i])))
			close.append(idx[0][0])
		#print(close)
		
		if i>3:
			ytheo1 = np.linspace(0,2*np.pi,500)
			ytheo2 = np.concatenate((ytheo1,ytheo1))
			ytheo = np.concatenate((ytheo2,ytheo2))
			ytheo = np.concatenate((ytheo,ytheo2))		
		else:
			ytheo1 = np.linspace(2*np.pi,0,500)
			ytheo2 = np.concatenate((ytheo1,ytheo1))
			ytheo = np.concatenate((ytheo2,ytheo2))
			ytheo = np.concatenate((ytheo,ytheo2))				
		
		residute = np.array(ytheo)[close]-np.array(y[i])
		residute1 = residute[np.where(abs(residute)<2)]
		print(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-np.mean(s[i]))<5.6175)]))
		#plt.plot(residute), plt.show()
		eval('ax'+str(i+1)+'.plot(x['+str(i)+'],y['+str(i)+'],"+")')
		#if  not(i<2 or i==3):
		#	eval('ax'+str(i+1)+'.plot(xtheo+'+str(s2[i])+',ytheo,"--",linewidth=1)')
		eval('ax'+str(i+1)+'.set_title(r'+'"'+title[i]+'"'+')')
		#eval('ax'+str(i+1)+'.set_xlim(['+str(-5.6175+s[i])+','+str(5.6175+s[i])+'])')
		#if  not(i<2 or i==3):
	#	print(x[i][close][np.where(abs(residute)<1)])
		#	eval('ax'+str(i+1)+'.plot((np.array(xtheo) + s2['+str(i)+'])[close][np.where(abs(residute)<2)],residute1,"--",label=r"$\sigma ={0:2f}$".format(std_me(residute1[np.where(abs(abs((np.array(xtheo) + s2[i])[close][np.where(abs(residute)<1)])-np.mean(s[i]))<5.6175)])))')
		#	eval('ax'+str(i+1)+'.legend()')
		#eval('ax'+str(i+1)+'.plot(x['+str(i)+'],np.mean(y['+str(i)+'])*np.ones(len(x['+str(i)+'])),"--",label=r"$\sigma ={0:2f}$".format(std_me(y['+str(i)+']-np.mean(y['+str(i)+']))))')
		#eval('ax'+str(i+1)+'.legend()')
		#eval('ax'+str(i+1)+'.set_title(r'+'"residute '+title[i]+'"'+')')
		eval('ax'+str(i+1)+'.set_xlim('+str(s[i])+')')
		eval('ax'+str(i+1)+'.set_ylim([-.2,3])')		
plt.show()
