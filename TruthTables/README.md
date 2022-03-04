# Truth Tables in Python
Discipline: Formal Analyses
Helpful for: Algorithms and Deduction

The truth_table.py file prints a truth table for any set of logical sentences connected with any number of logical connectives. This is helpful in Formal Analyses when checking fr invalid set of arguments.

* **Dynamic** - Can work for any set of logical sentences and connectives (disregarding the limitation of computability).
* **Optimized** - Evaluates directly from the eval code rather than set out functions. Makes it simpler
* **Plug and play** - Replacement of symbolization key (letters) for logical (atomic) sentences
  * A meaningful expression is called a well-formed formula. If broken down to the fundamental atomic sentences and evaluated logically, one can spot logical fallacies and invalid arguments in sentences.

## Getting Started

To get it into your computer, you can clone it using Git or downloaded directly as a .zip file and extract it

```
git clone https://github.com/markgacoka/Logic
```

### Prerequisites

The source code uses [PrettyTable](https://ptable.readthedocs.io/en/latest/tutorial.html) library for displaying the tables neatly. To install, type this into terminal

```
python3 get-pip.py
pip3 install prettytable
```

If you have downloaded prettytable but you get an import error, download it to a virtual environment and run it from there

```
source venv/bin/activate
pip install https://pypi.python.org/packages/source/P/PrettyTable/prettytable-0.7.2.tar.bz2
```

## Running the tests
To run the program, simply run the python file and follow the prompts

```
python3 ~/truth_table.py
```

Supported connectives include:
* Conjunction (and, &)
* Disjunction (or, V, xnor)
* Implication (implies, →)
* Biconditional (bicon, ↔)
* Negation (not, ¬)
* Brackets '()'

## Examples
If you want to get the truth table for 'a and b' you would input

```
a and b
a & b
a && b
```

### 1. a and b
 ![a and b](https://github.com/markgacoka/Logic/blob/master/a_and_b.png)

### 2. a and b or c
 ![a and b or c](https://github.com/markgacoka/Logic/blob/master/a%20and%20b%20or%20c.png)

### 3. not a biconditional b or c
 ![not a biconditional b or c](https://github.com/markgacoka/Logic/blob/master/not%20a%20bicon%20bc.png)

## Practical Use Cases
#### Case 1
* A - Mark is going to the market (True)
* B - Mark is a writer (False)

A (True) and B (False) would result to False as the second argument makes it invalid.

#### Case 2
* A - I am writing a novel (True)
* B - You like cooking (False)

A implies B (same as not a or b) on the truth table would result to False thus making it an invalid argument. The truth value of an implication is dependent only on the conclusion (when we say 'therefore this') and not the premises. Thus, if A is false and B is true, A → B will still be true.

## Built With

* [Python](https://docs.python.org/3/) - The language that the source code was made with
* [PrettyTable](https://ptable.readthedocs.io/en/latest/tutorial.html) - The Library used to print the data


## Authors

* [**Gacoka Mbui**](https://github.com/markgacoka)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Prof. Albretcht at Minerva Schools at KGI for giving me feedback on this project.


TODO: Create a UI for it, create a seperate program that scrapes data and extract the logical statements from the paragraph. With proper assignment of its truth values using NLP (Natural Language Processing), we can gauge whether we have an invalid argument.

