# TL; DR

For proteins that do not have 3D structures, we tried to predict the end-to-end distance of the protein sequences by computing Sequence Charge Decoration (SCD). SCD is computed by using the formula in this article and I have developed the code needed for this project.




# Summer-Research

### Abstract ###
Polymers are made up of monomers covalently linked to a chain, similar to beads/pearls on a chain/necklace. Proteins are heteropolymers where monomers — called amino acids — are not identical, unlike homopolymers that have identical monomers. In spite of a long history of studies on linear homopolymers and heteropolymers there has been limited research on the conformation of branched heteropolymers. This research studies the conformational properties of branched heteropolymers. Specifically we explore the selective placement of amino acids on the heteropolymers even when the total number of constituent amino acids are the same. We will present results by using mathematical theory and computer simulations. The ability to tune the conformation of these branched proteins is important in biology with specific application in designing novel biocompatible materials relevant in bio-therapeutics.


### Background ###
* Networks of branched polymers can be useful in biology and biomedicine. For example, in the formation of tissue matrix.
* Different types of network (Fig. 1) determine the physical and/or chemical properties of the material, such as how strong or weak the specific material is.
<p align="center">
  <img src="https://github.com/Chameleon-7/Summer-Research/blob/master/simple_branched_polymer.png" width="400" height="200">
</p>
<p align="center">
  Fig. 1 Simple illustration of heteropolymer network
</p> 

* In biological systems, networks can be made of proteins
* Proteins are polymers made of building blocks (amino acids)
<p align="center">
  <img src="https://github.com/Chameleon-7/Summer-Research/blob/master/linear-vs-branched.png" width="400" height="200">
</p>
<p align="center">
  Fig. 2 Linear polymer (left) and branched polymer (right)
</p>  

<p align="center">
  &nbsp;&nbsp;&nbsp;&nbsp;Circles show different building blocks (amino acids)
</p>

<p align="center">
     Different color indiciates different chemical properties
</p>

### Objectives ###
* We wanted to investigate the role of protein sequence on its size.
* Specifically, how does the end to end distance (R) depend on a given protein sequence?
<p align="center">
  <img src="https://github.com/Chameleon-7/Summer-Research/blob/master/Tail-Effect.png" width="400" height="400">
</p>

* The two sequences have different tail branch. Which sequence will have bigger size, or comparable?

### Methods ###
#### A. Mathematical theory for end-to-end distance ####
<p align="center">
  <img src="https://github.com/Chameleon-7/Summer-Research/blob/master/Mathematical Formula.png" width="400" height="240">
</p>

<p align="center">
  <img src="https://github.com/Chameleon-7/Summer-Research/blob/master/Terms-of-Q.png" width="400" height="240">
</p>

#### B. All-atom computer simulations ####
* We performed all-atom Monte Carlo simulations with the synthetic sequences described above in room temperature. 
* After finishing the simulations, R values were found.

### Results ###
#### A. Mathematical theory for end-to-end distance ####
* Qb values were calculated through theoretical formula and are shown in Table 1.
* The Q b values are comparable for both sequences, thus the R values are expected to be comparable too.

#### B. Simulation results agree with the theoretical prediction ####
The values of the R from the simulation are also shown in the following Table.
<p align="center">
  <img src="https://github.com/Chameleon-7/Summer-Research/blob/master/results.png" width="400" height="180">
</p>

* The results from the simulation are consistent with the theoretical results as the the values lie within the uncertainty range.

### Conclusion
In summary, we present that the charge sequence dictates the size of the branched polymers. Further investigation needs to be done to determine the role of non-charged amino acids and other sequences.
