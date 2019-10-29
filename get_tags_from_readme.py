# This script finds all the tags in a readme file
# Usage:
#   python3 get_tags_from_readme.py path
# Required:
#   path: path of a readme file
# Output:
#   all the tags found in the readme file, one tag in a line


import os
import logging
import argparse

def get_file_path_from_command_line():
	parser = argparse.ArgumentParser()
	parser.add_argument('file_path', help = "readme file path of service")
	args = parser.parse_args()
	return args.file_path


def validate_file_path(file_path):
	if os.path.isfile(file_path):
		return True
	else:
		logging.error("readme file not found in path %s" % file_path)
	return False


def get_tags_from_readme(file_path):
	tags_list = []
	with open(file_path, 'r') as file:
		for line in file.readlines():
			line.strip()
			if len(line) > 8 and line[:8] == '### Tag:':
				tags_list.append(line[8:].strip())
	return tags_list


def main():
	file_path = get_file_path_from_command_line()
	tags_list = []
	if validate_file_path(file_path):
		tags_list = get_tags_from_readme(file_path)
	print ('\n'.join(tags_list))
	return tags_list


if __name__ == '__main__':
	main()
