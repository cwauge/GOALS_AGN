import numpy as np 
import matplotlib.pyplot as plt 


def main(ID,z,Lx,LIR):
    plot = Plotter(ID,z,Lx,LIR)
    

class Plotter():

    def __init__(self,ID,z,Lx,LIR):
        self.ID = ID
        self.z = z
        self.Lx = Lx
        self.Lir = LIR

    def IR_colors(self,savestring,x,y,L=[np.nan],gal_x=[np.nan],gal_y=[np.nan],donley=True,Lacy=False,colorbar=False,colorbar_label='',samp1=[np.nan],samp2=[np.nan],select_sources=False):
        x1d = np.linspace(0.08, 1.5)
        x2d = np.linspace(0.35, 2.0)

        x1L = np.linspace(-0.3, 1.5)

        arp220 = (self.ID == 'UGC 09913')
        mrk231 = (self.ID == 'UGC 08058')
        print('here')
        print(L)

        fig = plt.figure(figsize=(15,13))
        ax = plt.subplot(111, aspect='equal', adjustable='box')
        if colorbar:
            pts = plt.scatter(x[samp1],y[samp1],c=L[samp1],edgecolor='k',s=175)
            agn_pts = plt.scatter(x[samp2],y[samp2],c=L[samp2],marker='*',edgecolor='k',s=175)
            # plt.colorbar(label=colorbar_label)
            axcb = fig.colorbar(agn_pts)  # make colorbar
            axcb.mappable.set_clim(10.75, 12.25)  # initialize colorbar limits
            # axcb.mappable.set_clim(43, 46)  # initialize colorbar limits
            # axcb.remove()
            # axcb2 = fig.colorbar(pts)  # make colorbar
            # axcb2.mappable.set_clim(10.75, 12.25)  # initialize colorbar limits
            # axcb2.mappable.set_clim(43, 46)
            # axcb2.set_label(label=colorbar_label)
        else:
            plt.plot(x,y,'.',ms=15,color='r')
        if donley:
            plt.plot(x1d, 1.21*x1d + 0.27,color='k',lw=3,label='Donley et al. 2012')
            plt.plot(x2d, 1.21*x2d - 0.27,color='k',lw=3)
            plt.vlines(0.08,ymin=0.15,ymax=0.37,color='k',lw=3)
            plt.hlines(0.15,xmin=0.08,xmax=0.35,color='k',lw=3)
        if Lacy:
            plt.plot(x1L, 0.8*x1L + 0.5,color='gray',ls='--',lw=3,label='Lacy et al. 2013')
            plt.vlines(-0.3,ymin=-0.3,ymax=0.2575,color='gray',ls='--',lw=3)
            plt.hlines(-0.3,xmin=-0.3,xmax=2,color='gray',ls='--',lw=3)
        if select_sources:
            select1 = plt.scatter(x[arp220],y[arp220],c=L[arp220],edgecolor='k',marker='X',label='Arp 229',s=350)
            axcb3 = fig.colorbar(select1)  # make colorbar
            axcb3.mappable.set_clim(10.75, 12.25)  # initialize colorbar limits
            axcb3.remove()
            select2 = plt.scatter(x[mrk231],y[mrk231],c=L[mrk231],edgecolor='k',marker='P',label='Mrk 231',s=400)
            axcb4 = fig.colorbar(select2)  # make colorbar
            axcb4.mappable.set_clim(10.75, 12.25)  # initialize colorbar limits
            axcb4.remove()
        plt.xlim(-0.5,1.5)
        plt.ylim(-0.5,1.5)
        plt.xlabel(r'log $\frac{f_{5.8}}{f_{3.4}}$',fontsize=26)
        plt.ylabel(r'log $\frac{f_{8.0}}{f_{4.5}}$',fontsize=26)
        plt.grid()
        plt.legend(fontsize=13)
        # plt.savefig(f'/Users/connor_auge/Desktop/Final_plots/{savestring}.pdf')
        plt.show()
    