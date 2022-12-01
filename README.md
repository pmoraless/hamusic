<p align="center">
  <img src="https://github.com/pmoraless/hamusic/blob/a02bf1e4be7768aa0341241522899664d122eac3/images/hamusic.png"/>
</p>
<h1 align="center">Hamiltonian Music</h1>

### A project designed to analyze different types of music associated with Hamiltonian cycles and paths, and to find common trends among them.

## About the Project
Hamusic (short for Hamiltonian Music) is a collection of algorithms: data scraping, sorting, algorithm C, and algorithm D, as well as assorted utilities (data processing tools, data visualization tools, etc). Hamusic was created by, and is the intellectual property of, Annie Chu, Rajiv Perera, Anusha Karandikar and Priscila Morales. Its ultimate purpose is to analyze a set of songs to find Hamiltonian patterns and update an algorithm to visualize songs that connect well perceptually  through data analytics and computing.

<p align="center">
  <img src="https://github.com/pmoraless/hamusic/blob/9fb1500921a3f06e091d08e4e0f7b8932a18d43b/images/hamusic2.gif"/>
</p>
<p>
    <em>A depiction of a knight moving on a chess board where each space is touched once.</em>
</p>

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
    CLIENT_ID = "9767f9a551144dc99704a14c60c91301"
    CLIENT_SECRET = "e51d830974e64cd6a00d43b2270f4c23"
    USERNAME = "INSERT YOUR USER ID HERE"
    ```