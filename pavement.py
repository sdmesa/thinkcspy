import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
from os import environ, getcwd
import os.path
import sys
from socket import gethostname
import pkg_resources
from runestone import get_master_url

sys.path.append(getcwd())
sys.path.append('../modules')

updateProgressTables = True
try:
    from runestone.server.chapternames import populateChapterInfob
except ImportError:
    updateProgressTables = False


######## CHANGE THIS ##########
project_name = "thinkcspy"
###############################

dynamic_pages = False

master_url = 'https://sdmesa.github.io/thinkcspy/'
master_app = 'sdmesa'
serving_dir = "./docs"
dest = "./published"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir=serving_dir,
        sourcedir="./_sources/",
        outdir=serving_dir,
        confdir=".",
        project_name = project_name,
        template_args = {
            'appname':master_app,
            'course_id':project_name,
            'course_name':project_name,
            'course_title': 'How\\ to\\ Think\\ like\\ a\\ Computer\\ Scientist',
            'course_url':master_url,
            'dynamic_pages': dynamic_pages,
            'login_required':'false',
            'loglevel':10,
            'use_services': 'false',
            'python3': 'true',
            'dburl': '',
            'basecourse': 'thinkcspy',
            'downloads_enabled': 'false',
            'default_ac_lang': 'python',
            'enable_chatcodes': 'false',
            'minimal_outside_links': 'true',
            'allow_pairs': 'false'
        }

    )
)

if project_name == "<project_name>":
  print("Please edit pavement.py and give your project a name")
  exit()

version = pkg_resources.require("runestone")[0].version
options.build.template_args['runestone_version'] = version

if 'DBHOST' in environ and  'DBPASS' in environ and 'DBUSER' in environ and 'DBNAME' in environ:
    options.build.template_args['dburl'] = 'postgresql://{DBUSER}:{DBPASS}@{DBHOST}/{DBNAME}'.format(**environ)

from runestone import build
# build is called implicitly by the paver driver.
