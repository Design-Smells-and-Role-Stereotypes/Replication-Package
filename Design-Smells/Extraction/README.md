## Design Smells Preprocessing

[![DOI](https://zenodo.org/badge/345998973.svg)](https://zenodo.org/badge/latestdoi/345998973)

This repositry provide code for preprocessing `.ini` files which are the output of the [ptidej](https://github.com/ptidejteam/v5.2) design smell detection tool

We provide step-by-step guide to help you extract and associate java class files with design smells detected in them. 

### Installation 
- Clone this repository locally using `git clone` command.
- Afterwards, `cd` to `Extraction`.

- Create a python virtual environment. On `macOS` or `Linux` you can use the following commands: `python3 -m venv env`, aftewards, activate the newly created virtual environment using `source env/bin/activate`.

- Now you can install the required packages using `pip install -r requirements.txt`
That's it, now we can move on to extract and preprocess design smells.

### Preprocessing
- Go to `app.py` and change the `design_smell_path` to point to where your `.ini` files are located.

- Run the command `python src/app.py --help` to see the required arguments. See output below:

```
usage: app.py [-h] --regex REGEX --output OUTPUT

design smell extraction args

optional arguments:
  -h, --help       show this help message and exit
  --regex REGEX    the regular expression for extracting design smells
  --output OUTPUT  the output filename with .csv extension. Example ds_project_name.csv
```

- `--regex` is determined empirically, looking at the structure of the `.ini`
- `--ouput` is simply the output filename and must end with `.csv`

- Now, run `src/app.py --regex=[enter regular expression] --output=[enter output filename]`

The result of the extraction and preprocessing task will be stored in `src/result/` subdirectory.

