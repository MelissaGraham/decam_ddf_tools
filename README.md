# decam_ddf_tools
Tools for analyzing the DECam DDF program data.

## Python notebooks:

basics_COSMOS.ipynb : answers a few basics questions about the COSMOS field data-- how many objects and candidates were detected, how objects are distributed among candidates, and how those distributions change when an R/B cutoff is applied.

sources_per_image_COSMOS.ipynb : looks at how many "good" (R/B > 0.6) objects are found per COSMOS field image, and at how a candidate's average R/B score is correlated to the number of times it is detected.

weather_sky_moon_COSMOS.ipynb : examines correlations between sky factors (moon distance, moon illumination, seeing, and zero-point magnitude) and the number of "good" (R/B > 0.6) object detections per exposure.

SNsearch.ipynb : The purpose of this notebook is to search through the COSMOS field objects to identify candidates that are likely supernovae. This is done by selecting every candidate that has at least 10 detections over at least 15 days, with a change of at least 1.4 mag, and that doesn't increase in brightness more than once

fastrisers.ipynb : This notebook searches the COSMOS field for candidates that (on their first night of detection) rose by at least 0.2 mag over at least 4 detections


## .txt files:

moondata.txt : generated by MLG, columns are (respectively) the archive filename base, the moon separation (in degrees), and the moon illumination (as a fraction). Only contains nonzero values for observations that were obtained with a <60 deg separation from the moon and when the moon illumination fraction was >0.2

medpixval.txt : generated by MLG, columns are (respectively) the archive filename base and the median pixel value (in counts)