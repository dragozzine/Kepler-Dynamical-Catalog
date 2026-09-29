# Kepler Dynamical Catalog

---

Welcome to the Kepler Dynamical Catalog, a Bayesian-flavored catalog of all objects of interest discovered by the Kepler Space Telescope. This catalog includes posteriors for all orbital elements, planetary parameters (including mass), and stellar characteristics for every Kepler system. 

---

## Overview

The Kepler Dynamical Catalog (KDC) represents a homogeneous-as-possible, systematic analysis of the entire Kepler output. This homogeneity is achieved through the modeling of transit timing variations in the Kepler data:

In multiplanet systems, gravitational interactions between planets sometimes generate noticeable signals in their lightcurves. These so-called transit timing variations (TTVs) may be characterized using a photodynamical model, i.e., a model that merges lightcurve and N-body simulation. From these TTVs, planetary masses may sometimes be measured. 

One such photodynamical tool, [PhoDyMM](https://github.com/dragozzine/PhoDyMM), analyzed **every multiplanet Kepler system**. The analysis returned converged posteriors for 661/720 multiplanet systems, including over 100 planets with $4\sigma$ mass measurements. We downsampled the massive posteriors returned from this process into a 1000-sample subset. Then, adding to this base, and using best-fit stellar parameters, we generated posteriors for the remainder of the multiplanet systems, as well as all the Kepler single-planet systems. We also precalculated many values of general interest, as well as appending results from important preexisting Kepler analyses onto the table. The result is a massive table that represents perhaps the maximal information extractable from just the Kepler lightcurves. It enables a wide variety of exoplanet studies in architectures, demographics, dynamics, interiors, and more.

## Getting Started

Because of the size of the KDC, this repository stores it as a series of compressed ```.parquet``` files located in ```/data```. To turn these files into a more palatable format, i.e., ```.csv``` or ```.h5```, run ```python src/quickstart.py``` in your terminal.

A tutorial notebook (```tutorial filename```) also exists---for those new to the Kepler Dynamics Catalog, this notebook is a great place to start.


## Further Details

For an individual description of each data column in the KDC, see ```doc/Provenance.md```. A summary table of the KDC is located at ```doc/Provenance_table.xml```

For a detailed description of how PhoDyMM generated the posteriors for multiplanet systems see Jones, Ragozzine, & Fabrykcy in preparation. 

For a detailed description of the post-processing done to multiplanet systems, as well as how the single-planet posteriors were generated, see Blodgett & Ragozzine in preparation.


## Citation

Any use of this data should also cite both Jones, Ragozzine, & Fabrykcy in preparation and Blodgett & Ragozzine in preparation. In addition, many columns of the KDC were taken from other studies which should also be cited; see ```doc/Provenance.md``` and ```doc/Sources.md``` for more details.



## License

Data in this repository are under a CC-BY-4.0 license.