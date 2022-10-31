# PHP parsing
In this repository you can find my implementation of the test task for the JetBrains Research Project **Mining Grahps from Source Code**.

# How to run
Make sure to have latest Python version and install all requirements:
```
pip3 install -r requirements.txt
```
To run on the whole set of repositories simply run
```
$ python3 main.py 
```
from the root directory.
However, it will take some time since we have to process more than 100 Mb of data. To speed up the process change `repos_root` variable to relative path to some of the repositories in folder `repos/`.

Details of the implementation and used technologies will be posted soon.