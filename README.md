# OSL Repo Extractor

A tool which mines GitHub repositories for [Fabio Marcos'](https://github.com/fabiojavamarcos) NAU-OSL project pipeline.


## Purpose
The GitHub Repo Extractor ("extractor") provides an expedient way to gather data from GitHub repositories using the [GitHub REST API](https://docs.github.com/en/rest).




## Requirements
- Written in `Python 3.8.3`
- Packages:
    - [PyGithub](https://pygithub.readthedocs.io/en/latest/introduction.html)
        - `pip install pygithub`
    - [Cerberus](https://docs.python-cerberus.org/en/stable/)
        - `pip install cerberus`




## Usage
### arguments
```shell
$ python main.py
usage: main.py [-h] extractor_cfg_file
main.py: error: the following arguments are required: extractor_cfg_file
```

The extractor requires only a path to a configuration file. The sample configuration at
`repo-extractor/data/input/configs/sample.json` is a good place to start experimenting. The extractor will report to you
what keys are missing, if any, and whether the values for those keys are acceptable. An acceptable call from the command line
will look like:

```shell
$ python main.py <path/to/cfg/file>
```


### configuration
```shell
~/files/work/repo-extractor/data/input/configs
» cat sample.json
{
    "repo": "JabRef/jabref",
    "state": "closed"
    "auth_file": "/home/m/files/work/repo-extractor/data/input/auths/mp_auth.txt",
    "output_dir": "/home/m/files/work/GitHub-Repo-Extractor-2/data/output",
    "range": [
        270,
        280
    ],
    "commit_fields": [
        "commit_author_name",
        "commit_date",
        "commit_message"
    ],
    "issue_fields": [
        "username"
    ],
    "pr_fields": [
        "body",
        "title"
    ]
}
```

Some key points about the configuration:

- The `auth_file` value requires a path to a file containing a GitHub Personal Access Token. Please format the PAT with no
  extra newlines or trailing spaces. The PAT should be on the first line.

- The `output_dir` value will be used to create the necessary outputs for you using the provided repo. You do not need to
  provide a name to an output file nor do you need to create the output directory by hand; it will be created for you if it
  does not exist.  After an execution, the output directory structure will look like `<output_dir>/<repo>/<repo>_output.json`
  e.g. `<output_dir>/jabref/jabref_output.json`

- The `state` value is used to determine whether or not the extractor will gather data on PR's that are either
    1. open
    2. closed *and* merged

    The extractor will not look at PR's that are closed and not merged.

- The `range` value discusses the actual item numbers you want to gather data from. If you want data from PR #270 up to
  PR #280 in a given repository, give [270, 280] to the range key, as above. The range behaves [x, y]; it is inclusive of both values.

- The `fields` keys discuss what pieces of data you want to gather from the objects in the given range. The extractor will
  merge gathered data. If you collected one piece of data for a range of API items, e.g. the body of a set of PR's, but now want to collect the title of those same PR's, you can simply add the correct field, "title", to the "pr_fields" list and the extractor will collect that data and merge it with the already existing JSON dictionary at the current output.
    - You do not need to ask for:
        - issue numbers
        - PR numbers
        - a PR's merged status

      Those pieces of data are mandatory when collecting data for those API item types, meaning that they will always be collected when collecting data on their respective item. *You do not need to attempt to provide them as arguments to the configuration files "fields" lists.*


### output
During a round of API calls, the extractor will compile gathered outputs into a dictionary. Under two conditions, the
extractor will write output to the output file provided in the configuration:

1. before sleeping when rate-limited by the GitHub REST API
2. after finishing gathering all the data for a range

This means that data will be collected even when the program does not completely finish.

The output produced by the extractor is pretty-printed JSON. Because it is printed in a human-readable format, it is very
easy to see what the extractor has collected and where the program left off in the case that you must stop it. See the
example output at `data/output/jabref/jabref_output.JSON`.

The human-readable output paired with the range functionality discussed above conveniently allows the user to start and stop
at will. For example, you may be collecting data from a very large range but must stop for some reason. You can look at the
output, see what PR or issue number the extractor last collected data for, and use that as the starting value in your range
during your next execution.

### troubleshooting
1. `v2` package does not exists

You likely need to update your `PYTHONPATH` environment variable so that your Python executable knows where to look for packages and modules. To do this, you can modify and paste the `export` statment below into your shell rc file e.g. `~/.bashrc` or `~/.zshrc`:

```shell
export PYTHONPATH='$PYTHONPATH:<path>/GitHub-Repo-Extractor/extractor'
```




## Contributing

#### commit formatting
Please attempt to abide by the ["Conventional Commits"](https://www.conventionalcommits.org) specification

#### source code standards
Using default settings for each, please:
- format all contributions with [black](https://pypi.org/project/black/)
    - `pip install black`
- lint all contributions with [pylint](https://pypi.org/project/pylint/)
    - `pip install pylint`
