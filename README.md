# PHP parsing
In this repository you can find my implementation of the test task for the JetBrains Research Project **Mining Grahps from Source Code**.

## How to run
Remember to clone including submodules:
```
git clone --recurse-submodules https://github.com/max-martynov/Mining-Graphs-Test-Task
```

Make sure to have latest Python version and install all requirements:
```
pip3 install -r requirements.txt
```
Specify path to the folder with php files changing `repos_root` value in `main.py`. I dind't pushed repositories used by me because it will take a lot of time.

Run
```
$ python3 main.py 
```
and see statistics in the `output.txt` file.

## My results
Can be found in `output.txt` file.

## Used tools

For cloning multiple github repositories I used a tool called [github-clone-all](https://github.com/rhysd/github-clone-all). 
As a main parser of php files I decided to take a use of [this small library](https://github.com/JameelNabbo/PHP-Parsers). It's really awkward and slow but I managed to take maximal profit out of it.
