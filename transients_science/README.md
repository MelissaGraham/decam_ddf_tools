# transients_science

Data and code for the initial characterization of candidate time-domain events
from the DECam Deep Drilling Fields (DDF).

Cite Graham et al. (2024; in prep.) if you use the contents of this directory or its sub-directories.

Cite <a href="https://ui.adsabs.harvard.edu/abs/2023MNRAS.519.3881G/abstract">Graham et al. 2023</a>
for the DECam DDF in general, or use of other files in other directories of this repository.

Terminology:
 * "object": a detection in a single difference image
 * "candidate": the association of `objects` by sky coordinate
 * "nightly-epoch": the combination of photometry from multiple difference-images obtained the same night
 * "good candidate": >10 objects and a mean real-bogus score > 0.4
 * "PQLD candidate": poor-quality long-duration candidates


## Publicly available data sets

All of the files in this repository are available for public use.

The files of interest for most people will be:

`all_nightly_epochs_files/candidate_lightcurves.dat`
 * created by `create_nightly_epoch_lightcurves.ipynb`
 * nightly-epoch light curves for DECam DDF candidates

`all_nightly_epochs_files/candidate_lightcurve_parameters.dat`
 * created by `create_nightly_epoch_lightcurves.ipynb`
 * parameters measured from the nightly-epoch light curve

`cross_matched_LSDR10/candidate_xmatch_LSdr10.dat`
 * nearest neighbors in the DESI Legacy Survey DR10 Tractor catalog
 * https://datalab.noirlab.edu/ls/ls.php 
 * matching described in Graham et al. (2024; in prep.)

`cross_matched_LSDR10/candidate_links.dat`
 * links to more information for candidates
 * static-sky deeply coadded color image cutout hosted by the Legacy Survey
 * Rob Knop's DECAT viewer page (detection triplets, light curves)


## Jupyter Notebooks

The Jupyter Notebooks which create the data files of interest are:

`create_nightly_epoch_lightcurves.ipynb`
 * identify "good" candidates
 * combine individual difference-image detections into nightly-epoch light curves
 * calculate light curve summary parameters

`explore_nightly_epoch_lightcurves.ipynb`
 * creates plots to explore the nightly-epoch light curves 
 * histograms and scatter plots of the light curve summary parameters


## Analysis for Graham et al. (in prep)

Various sub-directories focus on identifying and characterizing different types of transients.