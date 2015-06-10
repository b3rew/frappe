# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Kirkos": {
			"color": "#FA0",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("KIRKOS")
		},
		"TestModule": {
			"color": "#c0392b",
			"icon": "icon-shopping-cart",
			"type": "module",
			"label": _("TEST MODULE")
		},
		"Tapp": {
			"color": "#FA0",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Tapp")
		},
		"Price List": {
			"color": "#FA0",
			"icon": "octicon octicon-chevron-up",
			"type": "module",
			"label": _("Price List")
		},
	}
