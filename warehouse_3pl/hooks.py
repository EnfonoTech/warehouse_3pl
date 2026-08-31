app_name = "warehouse_3pl"
app_title = "Warehouse 3PL"
app_publisher = "Sayanth"
app_description = "3PL Warehouse Management System"
app_email = "sayanth@example.com"
app_license = "mit"
source_link = "https://github.com/sayanthns/warehouse_3pl"
app_logo_url = "/assets/warehouse_3pl/images/logo.png"
docs_url = "https://docs-site-brown-six.vercel.app"

# Apps
# ------------------

required_apps = ["erpnext"]

# In-ERP operating guide.
# The controller/template pair is warehouse_3pl/www/warehouse_guide.{py,html} -- the
# filename must stay underscored. A hyphen is not a valid Python module name, so Frappe
# cannot import the controller, skips it silently, and serves the page to Guest with a 200,
# bypassing its permission check entirely. The hyphenated public URL comes from here instead.
website_route_rules = [
	{"from_route": "/warehouse-guide", "to_route": "warehouse_guide"},
]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "warehouse_3pl",
# 		"logo": "/assets/warehouse_3pl/logo.png",
# 		"title": "Warehouse 3PL",
# 		"route": "/warehouse_3pl",
# 		"has_permission": "warehouse_3pl.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/warehouse_3pl/css/warehouse_3pl.css"
# app_include_js = "/assets/warehouse_3pl/js/warehouse_3pl.js"

# include js, css files in header of web template
# web_include_css = "/assets/warehouse_3pl/css/warehouse_3pl.css"
# web_include_js = "/assets/warehouse_3pl/js/warehouse_3pl.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "warehouse_3pl/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "warehouse_3pl/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "warehouse_3pl.utils.jinja_methods",
# 	"filters": "warehouse_3pl.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "warehouse_3pl.install.before_install"
# after_install = "warehouse_3pl.install.after_install"

after_install = "warehouse_3pl.warehouse_3pl.custom_fields.setup.setup_custom_fields"

# Uninstallation
# ------------

# before_uninstall = "warehouse_3pl.uninstall.before_uninstall"
# after_uninstall = "warehouse_3pl.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "warehouse_3pl.utils.before_app_install"
# after_app_install = "warehouse_3pl.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "warehouse_3pl.utils.before_app_uninstall"
# after_app_uninstall = "warehouse_3pl.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "warehouse_3pl.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"warehouse_3pl.tasks.all"
# 	],
# 	"daily": [
# 		"warehouse_3pl.tasks.daily"
# 	],
# 	"hourly": [
# 		"warehouse_3pl.tasks.hourly"
# 	],
# 	"weekly": [
# 		"warehouse_3pl.tasks.weekly"
# 	],
# 	"monthly": [
# 		"warehouse_3pl.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "warehouse_3pl.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "warehouse_3pl.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "warehouse_3pl.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["warehouse_3pl.utils.before_request"]
# after_request = ["warehouse_3pl.utils.after_request"]

# Job Events
# ----------
# before_job = ["warehouse_3pl.utils.before_job"]
# after_job = ["warehouse_3pl.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"warehouse_3pl.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

