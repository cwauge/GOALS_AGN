import numpy as np
import matplotlib.pyplot as plt 
from astropy.io import fits
from astropy.io import ascii
from match import match

from Plots import Plotter


# Read in the Photometry data data
with fits.open('/Users/connor_auge/Research/Disertation/catalogs/GOALS_total.fits') as hdul:
    Ned_phot_data = hdul[1].data 

Ned_phot_ID = Ned_phot_data['ID']


# Read in the X-ray data
cgoals = ascii.read('/Users/connor_auge/Research/Disertation/catalogs/CGOALS_Xray.txt',guess=False,delimiter=',',encoding='utf-8')
ricci = ascii.read('/Users/connor_auge/Research/Disertation/catalogs/ULIRG_Xray2.csv',guess=False,delimiter=',')

cgoals_ID = cgoals['ID']
cgoals_z = cgoals['z']
cgoals_Lx = cgoals['Lhx']*1E40
cgoals_Lir = cgoals['LIR']
cgoals_Fhx = cgoals['Fhx']*1E-14
cgoals_Fsx = cgoals['Fsx']*1E-14

ricci_ID = np.asarray(ricci['ID'])
ricci_z = np.asarray(ricci['z'])
ricci_Lx_hard = np.asarray(ricci['Lx2_10'])
ricci_Lx_full = np.asarray(ricci['Lx2_10']) + np.log10(1.64)
ricci_Lx_hard_obs = np.asarray(ricci['Lx2_10_obs'])
ricci_Fhx = np.asarray(ricci['Fx2_10'])
ricci_Fsx = np.asarray(ricci['Fx05_2'])
ricci_Nh = np.asarray(ricci['Nh'])
ricci_LIR = np.asarray(ricci['LIR'])


ix, iy = match(ricci_ID, Ned_phot_ID)
ricci_ID_match_Ned = ricci_ID[ix]
ricci_z_match_Ned = ricci_z[ix]
ricci_Lx_hard_match_Ned = ricci_Lx_hard[ix]
ricci_Lx_full_match_Ned = ricci_Lx_full[ix]
ricci_Lx_hard_obs_match_Ned = ricci_Lx_hard_obs[ix]
ricci_Fhx_match_Ned = ricci_Fhx[ix]
ricci_Fsx_match_Ned = ricci_Fsx[ix]
ricci_Nh_match_Ned = ricci_Nh[ix]
ricci_LIR_match_Ned = ricci_LIR[ix]

Ned_phot_ID_match = Ned_phot_ID[iy]

ricci_Fx_hard_match_mjy_Ned = ricci_Fhx_match_Ned*4.136E8/(10-2)
ricci_Fx_soft_match_mjy_Ned = ricci_Fsx_match_Ned*4.136E8/(2-0.5)

goals_Fx_int_array = np.array([ricci_Fx_hard_match_mjy_Ned])
goals_Fx_int_err_array = np.array([ricci_Fx_hard_match_mjy_Ned*0.3])

IRAC_ch1 = np.asarray(Ned_phot_data['IRAC1'][iy],dtype=float)*1E6
IRAC_ch2 = np.asarray(Ned_phot_data['IRAC2'][iy],dtype=float)*1E6
IRAC_ch3 = np.asarray(Ned_phot_data['IRAC3'][iy],dtype=float)*1E6
IRAC_ch4 = np.asarray(Ned_phot_data['IRAC4'][iy],dtype=float)*1E6


plot = Plotter(Ned_phot_ID,ricci_z_match_Ned,ricci_Lx_full_match_Ned,ricci_LIR_match_Ned)


print(IRAC_ch1)
print(IRAC_ch2)
print(IRAC_ch3)
print(IRAC_ch4)
print(ricci_LIR_match_Ned)


plot.IR_colors('IR_colors',np.log10(IRAC_ch3/IRAC_ch1),np.log10(IRAC_ch4/IRAC_ch2),L=ricci_LIR_match_Ned,colorbar=True,samp1=np.where(ricci_Lx_full_match_Ned > 42.9),samp2=np.where(ricci_Lx_full_match_Ned > 999))