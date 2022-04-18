# decam_ddf_tools / extragalactic_fields

Tools for analyzing the DECam DDF extragalactic fields' data, COSMOS and ELAIS.

For science investigations with the candidates nightly-epoch lightcurves, see the `science_with_candidates/` directory.

The notebooks in the `science_with_objects/` use the non-public databases and are still in development.

Note:

 * "object" refers to a single detection in a difference image
 * "candidate" refers to associated detections at a given sky location
 * "probably-real" extragalactic candidates means >10 detections, mean R/B>0.4
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
 * Identify **"probably-real" candidates (>10 detections, mean R/B>0.4)** and create data files just for these candidates.
 * Write two naive filters to test methods for identifying transients and fast-risers with alerts. Find they're too simple to work well.
   * 'Transients' as candidates with >=5 objects in two consecutive nights in any filter (118 candidates)
   * 'Fast Risers' as candidates with >=5 objects in the first night in any filter, all brightening (0 candidates)

**Inputs/Outputs**<br>
 * inputs are Rob's databases, requires password
 * output plots are in `source_detection_summary_figures/`
 * output files of **"probably-real"** candidate data are in `source_detection_summary_files/`
   * candidates.dat (summary statistics for "probably-real" candidates, like number of detections)
   * candidate_objects_(field).dat (all objects for all "probably-real" candidates)
   * exposures_(field).dat (data for all exposures, e.g., limiting magnitudes, seeing)

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
 * no outputs (plots displayed in line)