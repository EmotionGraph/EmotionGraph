import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot():
	x=np.genfromtxt('pred.txt.csv',delimiter=',')
	print(x)
	x = np.delete(x, (0), axis=0)
	t = np.arange(1., len(x)+1, 1.0)
	#plt.plot(t, t, 'c^', t, t**2, 'c^', t, t**3, 'c^')


	emotions = ["joy","trust","fear","surprise","sadness","disgust","anger","anticipation"]
	b_patch = mpatches.Patch(color='b', label=emotions[0])
	g_patch = mpatches.Patch(color='g', label=emotions[1])
	r_patch = mpatches.Patch(color='r', label=emotions[2])
	c_patch = mpatches.Patch(color='c', label=emotions[3])
	m_patch = mpatches.Patch(color='m', label=emotions[4])
	y_patch = mpatches.Patch(color='y', label=emotions[5])
	k_patch = mpatches.Patch(color='k', label=emotions[6])
	r__patch = mpatches.Patch(color='r', label=emotions[7],linestyle='--')
	plt.legend(handles=[b_patch,g_patch,r_patch,c_patch,m_patch,y_patch,k_patch,r__patch])
	#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

	plt.plot(t,x[:,1],'b',t,x[:,2],'g',t,x[:,3],'r',t,x[:,4],'c',t,x[:,5],'m',t,x[:,6],'y',t,x[:,7],'k',t,x[:,8],'r--')
	#l1=plt.plot(x[:,8],label=emotions[7], linestyle='--')
	plt.show()