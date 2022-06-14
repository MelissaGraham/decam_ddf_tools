# decam_ddf_tools / extragalactic_fields / science_with_objects

Tools for analyzing the non-public databases at NERSC, for the DECam DDF extragalactic fields' data, COSMOS and ELAIS.

Recall:

 * "object" refers to a single detection in a difference image
 * "candidate" refers to associated detections at a given sky location


## Modules:

decam_utils.py : Useful functions for exploring our data. Currently contains:
 * plotlc(), a function that makes a lightcurve for a chosen candidate
 * rm_dupes(), a function that removes duplicate rows from arrays
 * pull_exptimes(), a function that updates fnm_exptime.txt
 * lmt_mgs(), a function that creates nightly-averaged arrays of limiting magnitudes for COSMOS and ELAIS
 
 
## Notebooks (In Progress)

### AGNpercentages.ipynb
This notebook matches our ~4000 "likely-real" detections to known AGN in COSMOS and ELAIS fields

### fastrisers_forpaper.ipynb
This notebook contains the filter used to identify fast-evolving variables and the code to make all plots used in the fast evolvers section of the paper. Any claim made in that section of the paper should be reproducible by this notebook.

### SNIasearch.ipynb

### SNsearch.ipynb

### fastrisers.ipynb

**Inputs/Outputs**<br>
 * uses decam_utils.py
