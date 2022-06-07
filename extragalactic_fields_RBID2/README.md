# decam_ddf_tools / extragalactic_fields

Tools for analyzing the DECam DDF extragalactic fields' data, COSMOS and ELAIS.

In Version 2 of this repository, we use the retrained R/B score (RB ID = 2).

To do science investigations with the publicly-available "probably-real" (see below) candidates, using either their individual-exposure photometry or combined nightly-epoch lightcurves, see the `science_with_candidates/` directory.

The notebooks in the `science_with_objects/` use the non-public databases and are still in development.

Note:

 * "object" refers to a single detection in a difference image
 * "candidate" refers to associated detections at a given sky location
 * "probably-real" extragalactic candidates means >= 10 detections, mean R/B >= 0.4
   * cuts shown to be reasonable in `extragalactic_fields/source_detection_summary_figures.ipynb/`
   * cuts also discussed in Section 3 of Graham et al. (in prep)


## Notebooks (Complete)

### image_processing_summary.ipynb

**Description**<br>
 * Create plots to analyze the DDF's image quality parameters.
   * e.g., limiting magnitude, sky background, seeing, and zeropoint
   * how parameters are correlated with moon separation/illumination

**Inputs/Outputs**<br>
 * inputs are Rob's databases, requires password
 * outputs are plots in `image_processing_summary_figures/`

### source_detection_summary.ipynb

**Description**<br>
 * Create plots to explore object detection and R/B scores vs. image quality.
 * Identify **"probably-real" candidates (>= 10 detections, mean R/B >= 0.4)** and create data files just for these candidates.
 * Identify potential flare stars as candidates with > 1 detections in g-band, a mean R/B >=0.6, and a time span of <0.5 days (i.e., detected in one night only).

**Inputs/Outputs**<br>
 * inputs are Rob's databases, requires password
 * output plots are in `source_detection_summary_figures/`
 * output files of **"probably-real"** candidate data are in `source_detection_summary_files/`
   * candidates.dat (summary statistics for "probably-real" candidates, like number of detections)
   * candidate_objects.dat (all objects for all "probably-real" candidates)
   * exposures.dat (data for all exposures, e.g., limiting magnitudes, seeing)
 * output files for further study of potential flare stars in `source_detection_summary_files/potential_flare_stars/`
   * contains a candidates.dat and candidate_objects.dat

### candidate_nightly_epochs.ipynb

**Description**<br>
 * Use the data files of **"probably-real" candidates** and combine intra-night detections (objects) into nightly-epoch photometry.
 * Calculate summary parameters for the nightly-epoch lightcurves like duration and amplitude.

**Inputs/Outputs**<br>
 * inputs are the candidate data files in `source_detection_summary_files/` (no password)
 * output files are in `candidate_nightly_epochs_files/`
   * candidate_lightcurves.dat (combined nightly-epoch photometry, and magnitude limits)
   * candidate_lightcurve_parameters.dat (duration, minimum magnitude, amplitude, and number of epochs)

### candidate_nightly_epochs_summary.ipynb

**Description**<br>
 * Use the candidate nightly-epoch lightcurves files to explore the lightcurve parameters.
 * Plot histograms of candidate lightcurve parameters (time span, amplitude, minimum magnitude, number of epochs).
 * Plot lightcurves of special candidates (brightest, best sampled, etc.)
 
**Inputs/Outputs**<br>
 * inputs are the files in `candidate_nightly_epochs_files/`
 * output plots are in `candidate_nightly_epochs_summary_figures/`
