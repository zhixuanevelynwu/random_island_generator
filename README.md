# Procedural Game Map Generation using Multi-leveled Cellular Automata

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This is an algorithm for Procedural Game Map Generation that outputs natural-looking game environments. The algorithm is designed to generate flexible and customizable maps. You can adjust different parameters to make the resulting map look dramatically different.

## Getting Started <a name = "getting_started"></a>

### Prerequisites

Have Python3 environment and Pygame Library installed to run the map visualization locally.

### Installing

Clone the repo to your local folder

```
git clone https://github.com/zhixuanevelynwu/random_island_generator.git
```

## Usage <a name = "usage"></a>

On your terminal, navigate to the project folder and run

```
python3 show_map.py
```

You will get a randomly generated visualization window.
At this point, you can use "S" key to generate a completed map with all islands, desert, and mountain elements:
![initial window](images/result.png?raw=true "Title")

</br>
OR
</br>

You may use "I" key to first generate islands:
![initial window](images/island.png?raw=true "Title")

"M" key to generate mountains:
![initial window](images/forest.png?raw=true "Title")

Then, "D" key to generate deserts and beaches:
![initial window](images/desert.png?raw=true "Title")
<br/>
Whenever you want a brand new map, type "N". 
<br/>
Use "F" key to save a map to the folder.
<br/>
To tweak the parameters and generate different looking maps, go to automaton.py file and modify the init function. Below are some examples of maps generated using different parameters:
![initial window](images/compare_1.png?raw=true "Title")
![initial window](images/compare_2.png?raw=true "Title")
![initial window](images/compare_3.png?raw=true "Title")
