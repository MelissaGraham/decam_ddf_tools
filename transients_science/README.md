# transients_science

The processing and analysis that is done in this folder, in order, by file name.

create_nightly_epoch_lightcurves.ipynb

 * recall that `object` is a detection in a single difference image
 * recall that `candidate` is the association of `objects`
 * the DDF obtains multiple images per field per filter per night
 * this notebook combines `objects` for the same night, filter, and candidate
 * the result is nightly-epoch lightcurves: one photometry point per night, per filter, per candidate
 * this notebook also calculates lightcurve summary parameters from the nightly-epoch lightcurves
 * two files are written to all_candidate_nightly_epochs_files

explore_nightly_epoch_lightcurves.ipynb

 * creates plots exploring the nightly epoch lightcurves
 * histograms of, and correlations between, the lightcurve summary parameters 
 * plots some demo lightcurves (brightest candidates, etc.)
 * no output files
 
create_potential_snia_list.ipynb

 * TBD