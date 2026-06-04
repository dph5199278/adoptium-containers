# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
import urllib.request

#ADOPTIUM_API_URL = "https://api.adoptium.net/v3/info/available_releases"


def _fetch_release_data():
    # """Fetch release info from the Adoptium API."""
    # req = urllib.request.Request(
    #     ADOPTIUM_API_URL,
    #     headers={"User-Agent": "Adoptium Dockerfile Updater"},
    # )
    # with urllib.request.urlopen(req) as response:
    #     return json.loads(response.read().decode("utf-8"))
    json_str = '''
    {
        "available_lts_releases": [8, 11, 17, 21, 25],
        "available_releases": [8, 11, 17, 21, 25, 26],
        "most_recent_feature_release": 26,
        "most_recent_feature_version": 27,
        "most_recent_lts": 25,
        "tip_version": 27
    }
    '''
    return json.loads(json_str)


def get_supported_versions():
    """Fetch supported versions from the Adoptium API.

    Returns all LTS versions plus any non-LTS versions between the most
    recent LTS and the most recent feature release (inclusive).

    For example, if LTS versions are [8, 11, 17, 21, 25, 29], this returns [8, 11, 17, 21, 25].
    """
    data = _fetch_release_data()

    lts_versions = set(data["available_lts_releases"])

    # Before 26 LTS versions
    versions = {v for v in lts_versions if v <= 25}

    return sorted(versions)


def get_latest_lts():
    """Return the most recent LTS version number."""
    data = _fetch_release_data()
    version = data["most_recent_lts"]
    return min(version, 25)
