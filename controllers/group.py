import utils, properties

def get_args(form_data):
	properties.load_properties()
	group_dataset = properties.get_group_datasets()[form_data["group"]]
	group_info = properties.groups[form_data["group"]]
	return {
		"group_dataset": group_dataset,
		"group_info": group_info,
		"maxrows": max([p.get("rows", 0) for p in group_dataset]),
		"flt": utils.flt,
		"title": group_info["label"] + " Datasets",
		"description": "Government of India list of datasets for " + group_info["label"]
	}