# © 2019 Nokia

# Licensed under the BSD 3 Clause license
# SPDX-License-Identifier: BSD-3-Clause

from radish_ext import get_radish_ext_dir
from radish_ext.sdk.helpers import get_cucumber_json_report_name, json_pretty_dump
from radish_ext.tools.main_radish_ext import main_radish_ext

from conduit_ui_tests.sign_up.ff_location import FeatureFilesLocation

if __name__ == "__main__":
    start_path, full_path_ff = FeatureFilesLocation().get_full_ff_path()
    print("Feature files to run:\n{}".format(json_pretty_dump(full_path_ff)))
    print("Feature files implementation location: {}".format(start_path))
    main_radish_ext(*['--write-ids',
                      '-b', get_radish_ext_dir(),
                      '-b', start_path,
                      '-t',
                      '--cucumber-json={}'.format(get_cucumber_json_report_name(__file__)),
                      '--user-data', 'cfg=conduit_ui_conf.yaml',
                      '--user-data', 'package=conduit_ui',
                      '--tags', 'auto',
                      *full_path_ff]
                    )
