from pathlib import Path
import os.path
from split_settings.tools import include, optional

# So now the base directory is two folder above, now we will going to add two more 'parent'
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Namespace our onw custom environment variables
ENVVAR_SETTINGS_PREFIX = "CORESETTINGS_"

LOCAL_SETTINGS_FILE = os.getenv(
    f"${ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH")  # If developers want their local environment setting to be in different location then they can specify on this environment variable

if not LOCAL_SETTINGS_FILE:  # It means that they don't have it set and default one is '../../../local/settings.dev.py'
    LOCAL_SETTINGS_FILE = 'local/settings.dev.py'


# we will now convert to absolution path for
if not os.path.isabs(LOCAL_SETTINGS_FILE):
    LOCAL_SETTINGS_FILE = str(BASE_DIR/LOCAL_SETTINGS_FILE)

include(
    # this will aggregate all the settings
    # file1
    # file2
    'base.py',

    # we will specify the local settings as optional so that if they have these file these we will include them here
    # In this case what ever we will add above optional settings and if optional settings will be found then options settings will override the above settings
    optional(LOCAL_SETTINGS_FILE)
)
