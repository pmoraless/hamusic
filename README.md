<p align="center">
  <img src="https://github.com/pmoraless/hamusic/blob/a02bf1e4be7768aa0341241522899664d122eac3/images/hamusic.png"/>
</p>
<h1 align="center">Hamiltonian Music</h1>

### A project designed to analyze different types of music associated with Hamiltonian paths, and to find common trends among them.

## About the Project
Hamusic (short for Hamiltonian Music) is a collection of algorithms: data scraping, backtracking and depth-first search, as well as assorted utilities (data processing tools, data visualization tools, etc). We use two methods to process data: pre-processing and post-processing. In our pre-processing method we 1) analyze musical attributes of paired songs to get filtered edges 2) create a sparse graph with the filtered edges 3) find remaining Hamiltonian paths 4) filter and find the path with the maximum weight possible. This implementation can be found under ```preprocessing.ipynb```. On the other hand, in our post-processing method we 1) create a fully connected graph 2) find all Hamiltonian paths 3) process paths and filter paths. Our first method (pre-processing) has a worst-case time complexity of ```O(nlogn)``` and our second method (post-processing) has a worst-case time complexity of ```O(N!)```.

Hamusic was created by, and is the intellectual property of, Annie Chu, Rajiv Perera, Anusha Karandikar and Priscila Morales. Its ultimate purpose is to analyze a set of songs to find Hamiltonian patterns and update an algorithm to visualize songs that connect well perceptually  through data analytics and computing.

<p align="center">
  <img src="https://github.com/pmoraless/hamusic/blob/9fb1500921a3f06e091d08e4e0f7b8932a18d43b/images/hamusic2.gif"/>
</p>
<p>
    <em>A depiction of a knight moving on a chess board where each space is touched once.</em>
</p>

Our main goal is to find the optimal order of a song playlist such that the songs flow well together.

## Acknowledgments
Special thanks is awarded to Professor Sarah Spence Adams and the Fall 2022 CA's, who helped in finding resources for the project.

## Installation
This project was developed for both conda-based python environments and UNIX-based environments. As such, we guarantee that all dependencies are UNIX tested, and that the core source code is compatible with the rendering interfacing on that OS.

## Setup
While this project is intended for use on a local setup, it may still be run on a smaller computer, such as a Raspberry Pi, with limited functionality.

For best results, we suggest having
- 2GB of RAM storage
- stable internet connection
- a means of displaying visuals

### Local Setup
1. First, clone the repository to your computer:
    ```
    git clone https://github.com/pmoraless/hamusic.git
    ```

2. It's recommended that you run this project from a Python virtual environment with an anaconda interpreter, which can be set up like this:
    ```
    source /home/your-user/anaconda3/bin/activate
    conda activate base
    ```

3. If you don't already have pip installed, run this command from your new virtual environment:
    ```
    sudo apt install python-pip
    ```

4. Finally, use pip to install the required packages from the default source, PyPi, for packages and dependencies:
    ```
    pip install -r requirements.txt
    ```

## Running the Code

### On your local machine
1. From a new terminal, navigate to the `bin` folder of your Hamusic repo. (Note that you may need to run a different version of the executable depending on your environment)
    ```
    cd [your-path-to-Hamusic]/bin
    ```
    
2. In order for Hamusic to work, it needs Spotify API keys. Please create a new file in the root titled "config.py":
    ```
    touch src/config.py
    ```
    Then, enter this file in a text editor of your choice and assign your Spotify client ID and client secret (these can be obtained from Spotify [here](https://developer.spotify.com/dashboard/login)) as well as your Spotify user ID to variables as strings using the following template:
    ```
    CLIENT_ID = "ENTER YOUR CLIENT_ID HERE"
    CLIENT_SECRET = "ENTER YOUR CLIENT_SECRET HERE"
    USERNAME = "ENTER YOUR USERNAME HERE"
    ```

The `src` folder in the the repository contains a file `config.py` which has working Spotify user ID variables.

3. Once a Python kernel has been initiated, run the data miner, from the root directory:
    ```
    %run src/discz_scrape.py
    %run src/scrape1.py
    ```

4. From here you can utilize data visualization fuctions that will be defined in ```analysis_discz.ipynb```. If an NameError occurs, please re-run the data miner.

## External Dependencies
The following are required to run this program. Note that requirements may already be satisfied and additional platform-specific dependencies may be required depending on your target environment.

### General Use
- [cycler](https://pypi.org/project/cycler/)
- [packaging](https://pypi.org/project/packaging/)
- [pandas](https://pypi.org/project/pandas/)
- [pip](https://pypi.org/project/pip/)
- [pyparsing](https://pypi.org/project/pyparsing/)
- [python-dateutil](https://pypi.org/project/python-util/)
- [pytz](https://pypi.org/project/pytz/)
- [scipy](https://pypi.org/project/scipy/)

### Data Visualization
- [matplotlib](https://pypi.org/project/matplotlib/)
- [matplotlib-inline](https://pypi.org/project/matplotlib-inline/)
- [networkx](https://pypi.org/project/networkx/)

### Data Source
- [spotipy](https://pypi.org/project/spotipy/)