# cli-input-tools

This repository provides some scripts helping to generate input files for autorest.cli

## list_readme_path_of_all_services.py
This script lists all the readme file paths in azure-rest-api-specs/specifications

#### Usgae:
``` bash
  python3 list_readme_path_of_all_services.py path [service = service] [manager = manager]
```

#### Required:
  - `path`: path of azure specifications

#### Optional:
  - `service`: ['ALL', $service_name], 'ALL' by default
  - `manager`: ['ALL', 'resource-manager', 'data-plane'], 'resource-manager' by default

#### Output:
  - path of all readme files, one path in a line


## list_readme_path_of_updated_services.py
This script lists all the readme file paths in updated services

#### Usage:
``` bash
  python3 list_readme_path_of_updated_services.py path branch1 branch2
```
#### Required:
  - `path`:    path of the azure-rest-api-specs
  - `branch1`: branch name for comparion, can be any branch in 'git branch -a'
  - `branch2`: branch name for comparion, can be any branch in 'git branch -a'

#### Outpus:
  - path of readme files which needed to be re-generated, one path in a line
  
  
## get_tags_from_readme.py
This script finds all the tags in a readme file

#### Usage:
``` bash
  python3 get_tags_from_readme.py path
```

#### Required:
  - `path`: path of a readme file

#### Output:
  all the tags found in the readme file, one tag in a line


## add_snippets_for_readme.py
This script adds cli snippets for the readme file

#### Usage:
``` bash
  python3 add_snippets_for_readme.py path
```
#### Required:
  - `path`: path of the readme file
