
project = 'MRAG'
copyright = '2025, KSV Muralidhar'
author = 'KSV Muralidhar'

html_logo = "logo.png"
extensions = []

templates_path = []
exclude_patterns = []

html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme = 'furo'
html_theme_options = {
}

root_doc = 'index'

html_context = {
        'display_github': False,
        'display_gitlab': False,
        'display_bitbucket': False,
        'display_version': False,
    }
