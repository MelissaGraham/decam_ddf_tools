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
 
 
## Notebooks (In Progress)

### SNIasearch.ipynb

### SNsearch.ipynb

### fastrisers.ipynb

**Inputs/Outputs**<br>
 * uses decam_utils.py
