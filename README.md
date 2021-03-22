
## Four Russians algorithm

This project includes Python implementation of Four Russains algorithm for boolean matrices multiplication and some tests in separated files in a folder "UnitTests" for this algorithm.

## Algorithm description
We have 2 matrices for their multiplication: matrix A (left matrix) and matrix B (right matrix). Then we calculate blocks size and their number. After that we split matrix A on column blocks and matrix B on row blocks. Then we should create and fill the table to store all combinations of rows of matrix Bn and fill the resulting matrix regarding rows An and corresponding entries in table.

The time comlexity is O(n^3/lg n).There are improvements for O(n^3/ lg^2 n) complexity.

The pseudocode of the algorithm is given below:
![pseudocode](https://louridas.github.io/rwa/assignments/four-russians/four_russians_algorithm.png)

Algotithm details with full description and examples can be found [here][df1].

## Usage
Download project and open in python supporting IDE e.g. PyCharm. Project consists of .main file with algorithm implementation and test files in a folder "UnitTests". Tests were provided by 'unittest', matrices implementations were used with numpy. 
To run the algorithm run .main file and fill the matrixA.txt and matrixB.txt files with imput data.
The format of input is:

```sh
1,0
0,1
```

To run in terminal, you should go to the project directory and run with:


```sh
python3 main.py
```

   [df1]: <https://louridas.github.io/rwa/assignments/four-russians/>
