# decam_ddf_tools
Tools for analyzing the DECam DDF program data.

To use the publicly-available photometry for candidates in the extragalactic fields (COSMOS and ELAIS), please go straight to the `extragalactic_fields/science_with_candidates/` directory (<a href="https://github.com/MelissaGraham/decam_ddf_tools/tree/main/extragalactic_fields/science_with_candidates">link</a>).

All of the notebooks in this repo use Python 3 and were developed in the NERSC JupyterHub environment.

Most of the notebooks (except in the `extragalactic_fields/science_with_candidates/` directory) access password-protected databases and are not intended for public use.

Note:

 * "object" refers to a single detection in a difference image
 * "candidate" refers to associated detections at a given sky location
 * "probably-real" extragalactic candidates means >= 10 detections, mean R/B >= 0.4
   * cuts shown to be reasonable in `extragalactic_fields/source_detection_summary_figures.ipynb/`
   * cuts also discussed in Section 3 of Graham et al. (in prep)


## Files:

archive_image_list.txt : generated by MLG using NOIRLab's DataLab to access DECam images from archive; contains a bunch of metadata for DDF images (RA, Dec, MJD, filter, airmass, target, exposure time, sequence ID, image type classification, moon separation, moon illumination, estimate of sky background in counts)
