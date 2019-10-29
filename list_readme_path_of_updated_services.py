# This script lists all the readme file paths in updated services
# Usage:
#   python3 list_readme_path_of_updated_services.py path branch1 branch2
# Required:
#   path:    path of the azure-rest-api-specs
#   branch1: branch name for comparion, can be any branch in 'git branch -a'
#   branch2: branch name for comparion, can be any branch in 'git branch -a'
# Outpus:
#   path of readme files which needed to be re-generated, one path in a line


import os
import subprocess
import logging
import argparse


def get_branches_from_command_line():
	parser = argparse.ArgumentParser()
	parser.add_argument('path', help = 'path of the azure-rest-api-specs')
	parser.add_argument('branch1', help = "branch with latest codes")
	parser.add_argument('branch2', help = "current working branch")
	args = parser.parse_args()
	return (args.path, args.branch1, args.branch2)


def validate_branch(path, branch):
	os.chdir(path)
	status, output = subprocess.getstatusoutput('git branch -a')
	if status:
		logging.error("failed when execute command: " + status)
		return False
	branches = [elem.strip() for elem in output.split('\n')]
	branches = [elem.strip('* ') for elem in branches]
	if branch not in branches:
		logging.error("branch %s not found in %s" % (branch, path))
		return False
	return True


def list_readme_path_of_updated_services(path, branch1, branch2):
	readme_path_list = []
	os.chdir(path)
	status, output = subprocess.getstatusoutput('git diff --name-only %s %s' %(branch1, branch2))
	if status:
		logging.error("failed when execute command: " + status)
		return False
	file_names =  [elem.strip() for elem in output.split('\n')]
	for file_name in file_names:
		name_list = file_name.split('/')[:3]
		readme_path = '/'.join(name_list) + '/readme.md'
		if name_list and name_list[0] == 'specification' and os.path.isfile(readme_path) and readme_path not in readme_path_list:
			readme_path_list.append(readme_path)
	return readme_path_list


def main():
	path, branch1, branch2 = get_branches_from_command_line()
	if validate_branch(path, branch1) and validate_branch(path, branch2):
		readme_path_list = list_readme_path_of_updated_services(path, branch1, branch2)
	print ('\n'.join(readme_path_list))


if __name__ == '__main__':
	main()
