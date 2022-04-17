# decam_ddf_tools / extragalactic_fields / science_with_candidates

Tools for analyzing "probably-real" candidates in the DECam DDF extragalactic fields' data, COSMOS and ELAIS.

Recall:

 * "object" refers to a single detection in a difference image
 * "candidate" refers to associated detections at a given sky location
 * "probably-real" candidates means >10 detections, mean R/B>0.4
   * cuts shown to be reasonable in `source_detection_summary_figures.ipynb/`
   * cuts also discussed in Section 3 of Graham et al. (in prep)

 
## Notebooks (In Progress).

### 01_demo_candidates.ipynb

**Description**<br>
 * Demonstrates how to use the available candidates data.

**Inputs/Outputs**<br>
 * inputs are the candidate data files in `source_detection_summary_files/` (no password)
 * polygons_tspan_lcamp.dat

### MLG_snia_menagerie.ipynb

