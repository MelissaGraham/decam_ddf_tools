# decam_ddf_tools / old

## Old Stuff

### images

A stash of some of the early plots.

### old_files

archive_image_list_2021A.txt : deprecated; use archive_image_list.txt

moondata.txt : deprecated; use the moon data in archive_image_list.txt

medpixval.txt : deprecated; use the moon data in archive_image_list.txt

fnm_exptime : A table of filenames and exposure times, generated using the decam_utils.pull_exptimes() function (which pulls from Rob's database)

### old_notebooks

basics_COSMOS.ipynb : answers a few basics questions about the extragalactic field data-- how many objects and candidates were detected, how objects are distributed among candidates, and how those distributions change when an R/B cutoff is applied.

sources_per_image_COSMOS.ipynb : looks at how many "good" (R/B > 0.6) objects are found per extragalactic field image, and at how a candidate's average R/B score is correlated to the number of times it is detected.

weather_sky_moon_COSMOS.ipynb : examines correlations between sky factors (moon distance, moon illumination, seeing, and zero-point magnitude) and the number of "good" (R/B > 0.6) object detections per exposure.

RB.ipynb : This notebook looks for correlations between the legitimacy of candidates and the RB scores of their candidates