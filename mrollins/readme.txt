Online Supplementary Material

"Radio AGN Selection and Characterization in Three Deep-Drilling Fields of the Vera C. Rubin Observatory Legacy Survey of Space and Time"
Shifu Zhu, W. N. Brandt, Fan Zou, Bin Luo, Qingling Ni, Yongquan Xue, and Wei Yan

The supplementary material includes four fits files (table3.fits, table4.fits, table6.fits, and tableB1.fits).
They contain the full tables of Table 3, Table 4, Table 6, and Table B1 of the paper.


Description of each column of the four fits files.

table3.fits - the full table for optical/IR counterparts of ATLAS/W-CDF-S and ATLAS/ELAIS-S1 radio sources.
'Name': The name of the optical/IR counterpart in the format of Jhhmmss.ssddmmss.s. Note that a unique optical/IR counterpart might be associated with multiple radio sources. 
'ATLASID': The ID of the ATLAS source. 
'TractorID': The ID of the Tractor catalog (Zou et al. 2021, Nyland et al. in preparation). 
'vis': The method of the matching result, 1 = visualization and 0 = automatic. 
'ext': The largest extent of radio galaxies. We have filled empty values with −99.


table4.fits - optical/IR counterparts of MIGHTEE/XMM-LSS and VLA/XMM-LSS radio sources.
'Name': The name of the optical/IR counterparts in the format of Jhhmmss.ssddmmss.s. Note that a unique optical/IR counterpart might be associated with multiple radio sources. 
'mtID': The ID of the MIGHTEE source. 
'vlaID': The ID of the VLA source. 
'tractorID': The ID of the Tractor catalog (Nyland et al. in preparation). 
'vis': The method of the matching result, 1 = visualization and 0 = automatic. 
'ext': The largest extent of radio galaxies.

table6.fits - radio AGNs selection and cigale modeling results.
'Field': Field name. 
'Name': Object name.  
'redshift': Redshift. 
'ztype': Redshift type. 
'zphot_lowlim' & 'zphot_upplim': Lower and upper limit of redshift if the redshift type is photometric. 
'radio_agn': Three flags that indicate if the object is selected as a radio AGN based on morphology, radio slope, and radio excess. 
'x_agn': The flag for X-ray AGNs, and −1, 1, and 0 represent X-ray unmatched, X-ray AGNs, and X-ray galaxies, respectively. 
'mir_agn': The flag for MIR AGNs. 
'S20cm' & 'S20cm_err': The flux density and error at 1.4 GHz (20 cm). 
'S24micron' & 'S24micron_err': The flux density and error at 24 𝜇m. 
'Mstar_gal', 'SFR_gal', and 'reduced_chi_gal': The stellar mass, SFR, and 𝜒2 of the cigale 𝜈 fits with a galaxy-only model. 
'Mstar_agn', 'SFR_agn', and 'reduced_chi_agn': The stellar mass, SFR, and 𝜒2 of the cigale fits with a galaxy+agn model. 
'ndet': The number of detected UV-to-FIR flux densities used in the cigale modeling.

tableB1.fits - the full results of the probability cross matching
'RCat': Radio catalog. 
'OIRCat': Optical/IR catalog. 
'rID': ID of the radio source. 
'rRA' & 'rDec': The RA and Dec of the radio source. 
'eRA' & 'eDec': The positional errors of the radio source in units of arcsec. 
'oirRA' & 'oirDec': The RA and Dec of the optical/IR candidate. 
'starMask': A flag indicating if the radio source is in the region masked by bright stars. 
'Li' & 'Ri': The likelihood ratio and corresponding reliability of the optical/IR candidate. See Eqs. 4 and 5. 
'mlrc': A flag indicating if the optical/IR is the MLRC among all candidates. 
'mlrcL': The likelihood ratio of the MLRC.
'confused': A flag indicating if the radio source is found to be confused by visual inspection.
