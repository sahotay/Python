#!/www/python_current/bin/python3

'''
This script is to track SiteBuild Jar Versions. Following jar versions will be collected:
  - /www/<env>>/updateComponent/lib/updateComponent.jar
  -
  - /www/<env>>/emailSync/lib/emailsync.jar
  - /www/<env>/vendorFeeds/lib/ParseReviewsXml.jar
  - /www/<env>/vendorFeeds/lib/ProductPageUrlProcessor/ProductPageUrlProcessor.jar
  - /www/<env>/promoSync/lib/promosync.jar
  - /www/<env>/customer/lib/PsaChangeNotifier.jar
  - /www/<env>/mvRefresh/lib/mvrefresh.jar
  - /www/le-qas-a/catLoadEndeca/lib/styleCategorizer.jar    -- version found at 'src_revision'
'''

import os
import argparse
import logging
import time
import json
import zipfile

def config():
    '''get variables
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-l',
                        '--log-level',
                        dest='log_level',
                        help='set the log level',
                        default='WARNING',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    parser.add_argument('-c',
                        '--config',
                        dest='config_file',
                        help='location of the config file to use',
                        default="/www/python/lib/python3.5/site-packages/site-packages/variables.json")
    parser.add_argument('--environment_name',
                        dest='environment_name',
                        help='sitebuild environment name such as le-tst-a, le-int-a, ...',
                        type=str)
    args = parser.parse_args()
    logging.basicConfig(
        level=args.log_level,
        format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    #print(args)
    with open(args.config_file) as file_handle:
        config = json.load(file_handle)
    return config, args


def show_jar_versions(enviornment, jar_name, write_status=False):
    '''fetch the jar version
    '''
    obj = __config__[enviornment][jar_name]
    jar_file = zipfile.ZipFile(obj['source'], 'r')
    jar_version = jar_file.read('META-INF/MANIFEST.MF')
    jar_version = {j[0]:j[1] for j in [i.split(': ') for i in jar_version.decode('utf-8').split('\r\n') if i]}
    out_obj = {}
    out_obj['Title'] = 'Unknown Title'
    out_obj['version'] = 'Unknown version'
    out_obj['Title'] = jar_version['Implementation-Title']
    out_obj['version'] = jar_version['Implementation-Version']
    out_obj['timestamp'] = int(time.time())
    out_obj['timestring'] = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(int(time.time())))
    if write_status:
        with open(os.path.join(__config__['status_folder'], obj['output_file']), 'w') as outfile:
            json.dump(out_obj, outfile)
    return out_obj

def get_updateComponent_version(env):
    data = show_jar_versions(env, 'updateComponent', True)
    return data
def get_emailsync_version(env):
    data = show_jar_versions(env, 'emailSync', True)
    return data
def get_ParseReviewsXml_version():
    data = show_jar_versions(env, 'ParseReviewsXml', True)
    return data
def get_ProductPageUrlProcessor_version():
    data = show_jar_versions(env, 'ProductPageUrlProcessor', True)
    return data
def get_promosync_version():
    data = show_jar_versions(env, 'promosync', True)
    return data
def get_PsaChangeNotifier_version():
    data = show_jar_versions(env, 'PsaChangeNotifier', True)
    return data
def get_mvrefresh_version():
    data = show_jar_versions(env, 'mvrefresh', True)
    return data

def main():
    if __args__.environment_name:
        get_emailsync_version(__args__.environment_name)
    exit(0)

if __name__ == '__main__':
    __config__, __args__ = config()
    main()

