# This script adds cli snippets for the readme file
# Usage:
#   python3 add_snippets_for_readme.py path
# Required:
#   path: path of the readme file


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


def snippets_exsit(file_path, content):
	with open(file_path) as file:
		for line in file.readlines():
			if line.strip() == content:
				return True
	return False


def get_service_name(file_path):
	service_names = []
	with open(file_path, 'r') as file:
		service_line = file.readline()
		service_names = service_line[2:].strip().split(' ')
	return ('').join([elem for elem in service_names])


def add_snippets_for_readme(file_path):
	with open(file_path, 'a') as file:
		if not snippets_exsit(file_path, '# Code Generation'):
			file.write('\n')
			file.write('# Code Generation\n\n')
		file.write('## cli\n\n')
		file.write('These settings apply only when `--cli` is specified on the command line.\n\n')
		file.write('``` yaml $(cli)\n')
		file.write('cli:\n')
		file.write('  cli-name: ' + get_service_name(file_path) + '\n')
		file.write('  azure-arm: true\n')
		file.write('  license-header: MICROSOFT_MIT_NO_VERSION\n')
		file.write('  payload-flattening-threshold: 2\n')
		file.write('  namespace: azure.mgmt.' + get_service_name(file_path) + '\n')
		file.write('  package-name: azure-mgmt-' + get_service_name(file_path) + '\n')
		file.write('  clear-output-folder: false\n')
		file.write('```\n')

		file.write('\n')
		file.write('## terraform\n\n')
		file.write('These settings apply only when `--terraform` is specified on the command line.\n\n')
		file.write('``` yaml $(terraform)\n')
		file.write('terraform:\n')
		file.write('  cli_name: ' + get_service_name(file_path) + '\n')
		file.write('  azure_arm: true\n')
		file.write('  license_header: MICROSOFT_MIT_NO_VERSION\n')
		file.write('  payload_flattening_threshold: 2\n')
		file.write('  namespace: azure.mgmt.' + get_service_name(file_path) + '\n')
		file.write('  package_name: azure-mgmt-' + get_service_name(file_path) + '\n')
		file.write('  clear_output_folder: false\n')
		file.write('```\n')
	return True


def main():
	file_path = get_file_path_from_command_line()
	if not validate_file_path(file_path):
		return False
	if snippets_exsit(file_path, '## cli'):
		logging.warning("cli snippets already exsit in readme %s" % file_path)
	else:
		add_snippets_for_readme(file_path)
	return True


if __name__ == '__main__':
	main()
