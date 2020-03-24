# Mass To Charge Predictor

## Summary 
The goal is to be able to make something in the lab, measure the mass of the product that was made, and then identify the structure of the product. The user will suply educatd guesses for determining which molecules are in the structure in what quantities. The program will return specific combinations of molecules that result in the specified mass of the product. 

## Inputs
- List of chemical formulas for molecules (chosen as educated best guesses for components of product)
- List of corresponding maximum quantity for each molecule 
- Charge of experiment
- Observed mass of experiment

Lists of molecules and their corresponding quantities can be passed to the program via command line arguments, csv files, or input line responces. 

Run "python mass_to_charge_predictor -h" to find instructions on how to pass lists as csv and command line arguments. If both methods are selected, an error will be thrown. If the lists are to be passed as a csv, the file should be structured as the first column being the molecule, and the second column being the maximum quantity. 

The absence of any input at the command line will result in the program prompting the user for input responces to collect the required inputs. 

## Returns
- List of structures (composed of molecules specified by user) that have a total mass equal to the specified mass of experiment.

### At a High Level
- User will input a chemical formula of a building block and the max number of that block.
- User will input charge and observed mass of product.
- Program will calculate the mass of each building block from the chemical formula using the stored masses of each atom.
The mass of each unique building block will be used to find which combination of molecules result in the desired mass.

## Example
User has an observed signal at 67.5 m/z  with an observed charge of 2.

User inputs the following blocks into the program; 5-CH2, 2-PO, NO2 (these are educated guesses).
The program interprets this as find every structure that contains any combination of carbon and hydrogen atoms (in a 1:2 ratio), posphorous and
 oxygen atoms (in 1:1 ratio) and nitrogen and oxygen atoms (in 1:2 ratio) up to the largest structure with 5 CH2 blocks, 2 PO blocks, and NO2 blocks. It then adds up the total mass of each structure and divides each of those masses by the charge. The list is now in m/z units. It then returns all chemical formulas that match the m/z value input by the user. One solution to the given m/z value is (CH2)3PONO2 or C3H6O3PN.
A program that will take chemical "building blocks" and return all possible structures made from those blocks (with reasonably finite numbers of each block dictated by the user) along with the mass of each structure. 

## Developement Notes
Store mass values of each atom
H = 1, He = 4, C = 12, N = 14, O = 16, Au = 196.97, etc.

The result should be permutative to give exhaustive results of all possible sequences, combinatorial to include permutations of different lengths, and recursive to simplify and expediate the calculations.

The first part of the program will be to have prompts where the user will input what building blocks they are using and what is the maximum number of each building block to be permeated(this will most likely be a different number for each type of building block). 

To make things very simple for chemists, it would be best to have each building block composed as molecular formulas. For example, a building block could be a portion of a molecule called "methyl", CH3 (one carbon atom and three hydrogen atoms). 

The progam will have defined masses for each individual atom (chemical element)

the chemical formula (CH3) will be stored as a building block with the calculated mass.

Mass units are arbitrary and will be ignored, so C = 12, H = 1, therefore, CH3 = 15 arbirary mass units. 

### Potential Functions to Utilize
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
