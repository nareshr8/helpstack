# HelpStack  [![Downloads](https://static.pepy.tech/personalized-badge/helpstack?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/helpstack)
> The Library to help developers who fight with the stack trace of errors


## Install

`pip install helpstack`

## How to use

After you install the library, we can use the decorator to simply get relevant links about the issue in jupyter notebook (or any ipython notebooks)

We do the following:
- Go through Stackoverflow and get top answered results that are relevent to this stack trace
- Get all libraries that are available in the environment and search its github issues that are relevent to its stack trace.

```python
@help_stack
def div_by_zero(a):
    return a/0

div_by_zero(12)
```

![Sample Image](tab_view.png)

## Areas of improvement / TODO list:
- Add additional Searches with results from other relevent sites
- Ease logging of github issues from the same notebook if the user feels its an issue in the library
- Improve accuracy of matches with results by using ML algorithms (have to read through couple of papers on the same)
- Performance improvement of the results as there are lots of network calls involved
- Adding compatibility to other IDEs/Platforms/ Languages
