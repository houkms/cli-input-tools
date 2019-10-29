# This script lists all the readme file paths in azure-rest-api-specs/specifications
# Usgae:
#   python3 list_readme_path_of_all_services.py path [service = service] [manager = manager]
# Required:
#	path: path of azure specifications
# Optional:
#   service: ['ALL', $service_name], 'ALL' by default
#   manager: ['ALL', 'resource-manager', 'data-plane'], 'resource-manager' by default
# Output:
#   path of all readme files, one path in a line


import os
import logging
import argparse


def service_filter(services, filter):
	if filter != 'ALL':
		if os.path.isdir(parent_dir + '/' + filter):
			services = [filter]
		else:
			logging.error("can not found service %s" % filter)
	return services


def manager_filter(managers, filter):
	if filter != 'ALL' and filter in managers:
		managers = [filter]
	elif filter != 'ALL':
		managers = []
	return managers


def get_inputs_from_command_line():
	parser = argparse.ArgumentParser()
	parser.add_argument('specs_dir', help = "path of azure service specifications")
	parser.add_argument('--service', default = 'ALL', help = "filter by service name")
	parser.add_argument('--manager', default = 'resource-manager', help = "filter by resource-manager or data-plane",
						choices = ['ALL', 'resource-manager', 'data-plane'])
	args = parser.parse_args()
	filter_conds = {
		'service': args.service,
		'manager': args.manager,
	}
	return (args.specs_dir, filter_conds)


def validate_specs_path(specs_dir):
	if os.path.isdir(specs_dir):
		return True
	else:
		logging.error("readme file not found in path %s" % specs_dir)
	return False


def list_readme_path_of_all_services(specs_dir, filter_conds):
	readme_path_list = []
	# service 
	services = os.listdir(specs_dir)
	services = service_filter(services, filter_conds['service'])
	for service in services:
		service_dir = specs_dir + '/' + service
		# manager
		managers = [file for file in os.listdir(service_dir) if os.path.isdir(service_dir + '/' + file)]
		managers = manager_filter(managers, filter_conds['manager'])
		for manager in managers:
			manager_dir = service_dir + '/' + manager
			# readme
			if os.path.isfile(manager_dir + '/readme.md'):
				readme_path_list.append(manager_dir + '/readme.md')
	return readme_path_list


def main():
	specs_dir, filter_conds = get_inputs_from_command_line()
	readme_path_list = []
	if validate_specs_path(specs_dir):
		readme_path_list = list_readme_path_of_all_services(specs_dir, filter_conds)
	print('\n'.join(readme_path_list))
	return readme_path_list


if __name__ == '__main__':
	main()
