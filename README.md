# epilepsy_classification
## Files for creating/pre processing the data
 open_and_display_data.py opens the edf files and then format the data in a numpy array for each patient. The y contains two dimension, one with the label, the other with the time of the concerned 1sec datapoint turned into the FFT with the 16 channel.
 
 from_raw_to_4hours_array get rid of the 4hours before and after seizures from the precedent vectors
 
 from_raw_to_temporel opens the edf files and then format the data
 
## File for the learning phase
 Jupyters notebook for each case investigated + the violin plot with analyse_stat.ypnb and violin_plot.py
