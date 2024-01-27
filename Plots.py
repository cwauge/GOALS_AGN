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

        plt.rcParams['font.size'] = 22
        plt.rcParams['axes.linewidth'] = 3
        plt.rcParams['xtick.major.size'] = 5
        plt.rcParams['xtick.major.width'] = 4
        plt.rcParams['ytick.major.size'] = 5
        plt.rcParams['ytick.major.width'] = 4
        plt.rcParams['hatch.linewidth'] = 2.0


    def IR_colors(self,savestring,x,y,L=[np.nan],gal_x=[np.nan],gal_y=[np.nan],donley=True,Lacy=False,colorbar=False,colorbar_label='',samp1=[np.nan],samp2=[np.nan],select_sources=False,clim=[0,10],xlim=[0,1],ylim=[0,1]):
        x1d = np.linspace(0.08, 1.5)
        x2d = np.linspace(0.35, 2.0)

        x1L = np.linspace(-0.3, 1.5)

        print(len(x),len(y),len(self.ID))

        arp220 = (self.ID == 'UGC 09913')
        mrk231 = (self.ID == 'UGC 08058')


        fig = plt.figure(figsize=(15,13))
        gs = fig.add_gridspec(nrows=1,ncols=2,width_ratios=[3,0.15],top=0.95,bottom=0.1,left=0.15,right=0.85)
        # ax = plt.subplot(111, aspect='equal', adjustable='box')
        ax = fig.add_subplot(gs[0])
        if colorbar:
            pts1 = ax.scatter(x[samp1],y[samp1],c=L[samp1],edgecolor='k',s=150)
            pts2 = ax.scatter(x[samp2],y[samp2],c=L[samp2],marker='*',edgecolor='k',s=150)
            axcb = fig.colorbar(pts1)  # make colorbar
            axcb.mappable.set_clim(clim[0], clim[1])  # initialize colorbar limits
            axcb.remove()
            axcb2 = fig.colorbar(pts2)  # make colorbar
            axcb2.mappable.set_clim(clim[0], clim[1])  # initialize colorbar limits
            # axcb2.set_label(label=colorbar_label)
            axcb2.remove()
        else:
            ax.plot(x,y,'.',ms=15,color='r')
        if donley:
            ax.plot(x1d, 1.21*x1d + 0.27,color='k',lw=3,label='Donley et al. 2012')
            ax.plot(x2d, 1.21*x2d - 0.27,color='k',lw=3)
            ax.vlines(0.08,ymin=0.15,ymax=0.37,color='k',lw=3)
            ax.hlines(0.15,xmin=0.08,xmax=0.35,color='k',lw=3)
        if Lacy:
            ax.plot(x1L, 0.8*x1L + 0.5,color='gray',ls='--',lw=3,label='Lacy et al. 2013')
            ax.vlines(-0.3,ymin=-0.3,ymax=0.2575,color='gray',ls='--',lw=3)
            ax.hlines(-0.3,xmin=-0.3,xmax=2,color='gray',ls='--',lw=3)
        if select_sources:
            select1 = plt.scatter(x[arp220],y[arp220],c=L[arp220],edgecolor='k',marker='X',label='Arp 229',s=350)
            axcb3 = fig.colorbar(select1)  # make colorbar
            axcb3.mappable.set_clim(clim[0],clim[1])  # initialize colorbar limits
            axcb3.remove()
            select2 = plt.scatter(x[mrk231],y[mrk231],c=L[mrk231],edgecolor='k',marker='P',label='Mrk 231',s=400)
            axcb4 = fig.colorbar(select2)  # make colorbar
            axcb4.mappable.set_clim(clim[0],clim[1])  # initialize colorbar limits
            axcb4.remove()
        ax.set_xlim(xlim[0],xlim[1])
        ax.set_ylim(ylim[0],ylim[1])
        ax.set_xlabel(r'log $\frac{f_{5.8}}{f_{3.4}}$',fontsize=26)
        ax.set_ylabel(r'log $\frac{f_{8.0}}{f_{4.5}}$',fontsize=26)
        ax.grid()
        ax.legend(fontsize=13)

        axcb = fig.add_subplot(gs[1])
        cb = fig.colorbar(pts1, cax=axcb, orientation='vertical')
        cb.set_label(colorbar_label)
        cb.mappable.set_clim(clim[0],clim[1])

        plt.savefig(f'/Users/connor_auge/Research/Disertation/GOALS/GOALS_figs/{savestring}.pdf')
        plt.show()
    