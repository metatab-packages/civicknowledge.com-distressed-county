# Distressed Tracts Per County

The [FFEIC publishes a very large dataset of Census
variables](https://www.ffiec.gov/censusapp.htm) and flags indicating ways in
which housing and populations in tracts are distressed. This dataset aggregates
those tract flags into counts of distressed tracts per county.


## Processing

The source dataset is ``ffeic_distressed``, which extracts a subset of the columns from the FFEIC Census Flat File, which is itself an extract from the American Community Survey, with a few extra columns for things like ratios of income of a tract to the containing MSA. This data set aggreates the ``ffeic_distressed`` to counties, and produces for each of the source dataset flags: 

* A count of tracts in the county with the flag set.
* The sum of the populatinos of trats with the flag set
* The percentage of the county's tracts with the flag set
* The percentage of the countys' population with the flag set. 
