# decam_ddf_tools / extragalactic_fields / science_with_candidates

Tools for analyzing publicly-available "probably-real" (see below) candidates datasets from the DECam DDF extragalactic fields, COSMOS and ELAIS.

Start with the notebook 01_demo_candidates.ipynb to learn about the candidate datasets available and how to use them. 

See also the DECAT Extragalactic Subtraction Viewer (by Rob Knop): https://decat-webap.lbl.gov/decatview.py/

Anyone is welcome to use these data. Enjoy!

Recall:

 * "object" refers to a single detection in a difference image
 * "candidate" refers to associated detections at a given sky location
 * "probably-real" candidates means >= 10 detections, mean R/B >= 0.4
   * cuts shown to be reasonable in `source_detection_summary_figures.ipynb`
   * cuts also discussed in Section 3 of Graham et al. (in prep)

 
## Notebooks (Complete)

### 01_demo_candidates.ipynb

Is saved in an executed state as a quicklook demo.

**Description**<br>
 * Demonstrates how to use the available candidates data files.
 * Make lightcurve plots that combine individual exposures, nightly-epoch photometry, and non-detection limits.

**Inputs/Outputs**<br>
 * inputs include:
   * `source_detection_summary_files/`
     * exposures.dat (exposure data, e.g., date, seeing, limiting magnitudes)
     * candidates.dat ("probably-real" candidate data, e.g., ra, dec, number of objects, mean R/B score)
     * candidates_object.dat (all detections for all "probably-real" candidates, e.g., mag, R/B score)
   * `candidate_nightly_epoch_files/`
     * candidate_lightcurves.dat (nightly-combined photometry for "probably-real" candidates)
     * candidate_lightcurve_parameters.dat (e.g., time span, minimum magnitude, amplitude, number of epochs)
 * no outputs, just in-line plots

### MLG_snia_menagerie.ipynb

**Description**<br>
 * Uses known relations between light curve duration and amplitude to identify potential SNIa.
 * Plots a 5x5 grid of lightcurves for potential SNeIa.

**Inputs/Outputs**<br>
 * inputs are:
   * the candidate data files in `candidate_nightly_epoch_files/`
   * `MLG_snia_menagerie_files/MLG_polygons_tspan_lcamp.dat`
 * output is `MLG_snia_menagerie_files/MLG_snia_menagerie.png`

## Notebooks (In Progress)

### MLG_lowCobj_highMRB_investigation.ipynb

**Description**<br>
 * Investigate the nature of the low-Cobj, high mean R/B score candidates
 
**Inputs/Outputs**<br>
 * inputs are `../source_detection_summary_files/MLG_lowCobj_highMRB/`
