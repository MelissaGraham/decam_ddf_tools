import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def make_lc( candname, cursor, rbcut=0.3 ):
    """
    This function creates a lightcurve plot for a given candidate in our dataset. To use it, just give it a candidate ID
    and whatever you've named your cursor object, and it will generate a lightcurve plot and return the final data it used to
    make that plot in the form [gxdata, rxdata, ixdata], [gydata, rydata, iydata], [gyerrs, ryerrs, iyerrs].
    
    The optional argument(s):
    rbcut : the lower bound to use for the RB cutoff (Default: 0.3)
    """
    # Grabbing all necessary data
    query = ( 'SELECT o.candidate_id, e.mjd, o.mag, e.filter, o.magerr, e.filename, o.ra FROM objects o '
             'JOIN subtractions s ON o.subtraction_id = s.id '
             'JOIN exposures e ON e.id = s.exposure_id '
             'WHERE o.candidate_id = %s '
             'AND o.rb > %s '
             'ORDER BY o.candidate_id '
             'LIMIT 10000000' )
    cursor.execute(query, (candname, rbcut))
    rawdata = np.array(cursor.fetchall())
    
    # Removing duplicates
    dupedata = np.array( [" ".join(i) for i in rawdata] )
    unique, ind = np.unique( dupedata, return_index=True )
    udata = np.array( [ i.split(" ") for i in unique ] ).transpose()    
    
    # Read in lookup table with filenames and exposure times
    lutable = np.loadtxt( "archive_image_list.txt", dtype=object ).transpose()
    fnmtable, exptable = lutable[0], lutable[7].astype(float)

    # Assign filenames and truncate to match lookup table format
    fnms = udata[5]
    fnms = [fnms[i][:21] for i in range( len( fnms ) )] 

    # Attach an exposure time to every object we pulled in the query
    exptime = np.array( [exptable[ np.where( fnms[i] == fnmtable )[0]][0] for i in range( len( fnms ) )], dtype=float )
    
    # Eliminate objects from non-standard images
    gmsk   =  np.where( ( udata[3] == "g" ) & ( exptime > 50 ) )[0]
    rmsk   =  np.where( ( udata[3] == "r" ) & ( exptime > 20 ) )[0]
    imsk   =  np.where( ( udata[3] == "i" ) & ( exptime > 20 ) )[0]
    grmsk  =  np.append( rmsk, gmsk )
    grimsk =  np.append( grmsk, imsk )
    
    # Make arrays to store the data in the plot
    plotdates   = np.empty( 3, dtype=object )
    plotmags    = np.empty( 3, dtype=object )
    plotmagerrs = np.empty( 3, dtype=object )
    
    # Assign field based on RA
    if float(udata[6][0]) < 50:
        field = "ELIAS"
    else:
        field = "COSMOS"
    # Assign color palette for plotting based on field
    if field == "COSMOS": c = ["darkgreen", "red", "brown"]
    elif field == "ELIAS": c = ["limegreen", "darkorange", "peru"]
    
    plt.figure(figsize=(8,5))
    
    filters = ["g", "r", "i"]
    for i in [0, 1, 2]: # Looping through filters
        # Grab only the data in the filter you want
        fmsk = np.where( udata[3] == filters[i] )[0]
        fmsk = [i for i in grimsk if i in fmsk]
        fdata = [i[fmsk] for i in udata]
        # Create an array of all unique dates (rounded) this candidate was detected on in this filter 
        fdates = np.unique( np.round( fdata[1].astype(float) ) )
        
        # Pull out all of the dates (rounded but non-unique)
        fcanddates = np.round(fdata[1].astype(float))
        # Pull out all of the measured magnitudes
        fcandmags = fdata[2].astype(float)
        # Pull out all of the measured magnitude errors
        fcandmagerrs = fdata[4].astype(float)
        
        # Create arrays to store the night, mag, and magerr data for just this filter
        fnight  = np.empty( len( fdates ), dtype=object )
        fmag    = np.empty( len( fdates ), dtype=object )
        fmagerr = np.empty( len( fdates ), dtype=object )
        
        # Loop through each night to assign a magnitude and magnitude error to each
        for j in range( len( fdates ) ):
            msk = np.where( fcanddates == fdates[j] )[0]
            # Magnitude for the night just the average mag of the night
            fmag[j] = np.mean( fcandmags[msk] )
            # Magerr for the night is the square root of the sum of squares of:
            # the standard deviation of the mag values for the night, and
            # the mean of the pipeline-assigned errors for the night
            fmagerr[j] = np.sqrt( np.mean( fcandmagerrs[msk] )**2 + np.std( fcandmags[msk] )**2 ) 
        
        # Plot the lightcurve in whichever filter we're in
        plt.errorbar( fdates, fmag, yerr=fmagerr, color=c[i] )
        
        # Save this filter's data in the appropriate places for the return statement
        plotdates[i]   = fdates
        plotmags[i]    = fmag
        plotmagerrs[i] = fmagerr
    
    # Plot formatting
    plt.title(candname)
    plt.ylabel("Magnitude")
    plt.xlabel("MJD")
    plt.gca().invert_yaxis()
    plt.show()
    
    return plotdates, plotmags, plotmagerrs