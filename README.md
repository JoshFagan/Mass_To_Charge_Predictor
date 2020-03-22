# Mass_To_Charge_Predictor
A program that will take chemical "building blocks" and return all possible structures made from those blocks (with reasonably finite numbers of each block dictated by the user) along with the mass of each structure. 

The goal is to be able to make something in the lab, measure the mass of the product that was made, and then identify the structure by looking up the mass from the results of the program. The result should be permutative to give exhaustive results of all possible sequences, combinatorial to include permutations of different lengths, and recursive to simplify and expediate the calculations.

The first part of the program will be to have prompts where the user will input what building blocks they are using and what is the maximum number of each building block to be permeated(this will most likely be a different number for each type of building block). To make things very simple for chemists, it would be best to have each building block composed as molecular formulas. For example, a building block could be a portion of a molecule called "methyl", CH3 (one carbon atom and three hydrogen atoms). The progam will have defined masses for each individual atom (chemical element) and the chemical formula (CH3) will be stored as a building block with the calculated mass. Mass units are arbitrary and will be ignored, so C = 12, H = 1, therefore, CH3 = 15 arbirary mass units. The user will be asked to input a chemical formula for a building block and the program will store that value with a calculated mass.

An addendum to the unit is that the instrument used to characterize a sample measures mass/charge (m/z), where the charge is arbitrary as well. Rather than have the program calculate permutations for each possible charge, it would be better to have the user input the suspected charge, and they could always run the program several times to test different charges. Additionally, to add some finess, it would be best to have the user input an observed mass and have the program return any computed structures that have that same mass.

Most helpful package in Python might be itertools

>>> from itertools import combinations_with_replacement
>>> comb = combinations_with_replacement([1,2,3],3)
>>> for i in the list(comb):
...	print(i)
...
(1, 1, 1)
(1, 1, 2)
(1, 1, 3)
(1, 2, 2)
(1, 2, 3)
(1, 3, 3)
(2, 2, 2)
(2, 2, 3)
(2, 3, 3)
(3, 3, 3)

This function is nice because it removes any duplicates and the number of units can be controlled by controlling the length. 1, 2, 3 could be replaced by masses of the building blocks.

The length of the combinations could be incremented to calculate different size structures (e.g. 1; 1,1; 1,1,1; 1,1,1,1; 1,1,1,1,1, etc.).

SUMMARY

Putting it all together:
Store mass values of each atom
H = 1, He = 4, C = 12, N = 14, O = 16, Au = 196.97, etc.
User prompted to input a chemical formula of a building block and the max number of that block.
User prompted to input additional building blocks until the user says no more.
User prompted to input charge and observed mass of product.
The program will then calculate the mass of each building block from the chemical formula using the stored masses of each atom.
The mass of each unique building block will be used in the
combination_with_replacement([a, b, c, ..., n], x) where a,b,c, etc. are the masses of different building blocks and x is the length, which starts at the number of building blocks and increments up to the total of the specified number of blocks.

A test example:
User has an observed signal at 67.5 m/z  with an observed charge of 2.

User inputs the following blocks into the program; 5-CH2, 2-PO, NO2 (these are educated guesses).
The program interprets this as find every structure that contains any combination of carbon and hydrogen atoms (in a 1:2 ratio), posphorous and
 oxygen atoms (in 1:1 ratio) and nitrogen and oxygen atoms (in 1:2 ratio) up to the largest structure with 5 CH2 blocks, 2 PO blocks, and NO2 blocks. It then adds up the total mass of each structure and divides each of those masses by the charge. The list is now in m/z units. It then returns all chemical formulas that match the m/z value input by the user. One solution to the given m/z value is (CH2)3PONO2 or C3H6O3PN.
