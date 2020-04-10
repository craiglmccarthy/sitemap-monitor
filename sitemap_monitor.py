#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Monitors changes to Sitemap over time. Script compares URLs in a "live" Sitemap
with URLs in a saved JSON file. If no JSON file is present, script will give 
option to initialize the JSON file for future comparisons. Includes basic
filtering for new URLs.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from xml.etree import ElementTree

import requests

parser = argparse.ArgumentParser(description='Monitor changes to Sitemap.')
parser.add_argument('--sitemap', nargs='+',
                    help='Sitemap input', required=True)
parser.add_argument('-or', '--outputremoved',
                    action='store_true', help="Show removed URLs")
parser.add_argument('-on', '--outputnew',
                    action='store_true', help="Show new URLs")
parser.add_argument('-f', '--filter', nargs='*', help="Show new URLs")
args = parser.parse_args()

sitemap_urls = args.sitemap
sitemap_memory = "./sitemap_memory.json"
filter_words = args.filter


def get_latest_sitemap_urls(sitemap_urls):
    """Gets latest Sitemap URLs from live site"""
    url_tree = []
    for sitemap in sitemap_urls:
        response = requests.get(sitemap)
        tree = ElementTree.fromstring(response.content)
        for i in range(len(tree)):
            url_tree.append(tree[i][0].text)
    return url_tree


def get_previous_sitemap_urls(sitemap_memory, latest_sitemap_urls):
    """Gets previous Sitemap URLs from previously saved JSON. If no previous 
    JSON is found, prompt to save latest Sitemap"""
    if Path(sitemap_memory).is_file():
        with open(sitemap_memory, 'r') as f:
            previous_sitemap_urls = json.loads(f.read())
        return previous_sitemap_urls
    else:
        print("Previous Sitemap file does not exist.")
        ans = input('Would you like to save URLs from latest Sitemap? (Y/N): ')
        if ans.lower() == 'y':
            print('Saving Sitemap...')
            with open(sitemap_memory, 'w') as f:
                json.dump(latest_sitemap_urls, f, indent=4)
        else:
            print("Exiting...")
            sys.exit(0)
        return latest_sitemap_urls


def compare_sitemaps(latest_sitemap_urls, previous_sitemap_urls):
    """Compares Sitemap lists and returns a list of pages not present in 
    previous Sitemap, and pages present in previous Sitemap but not present 
    in latest"""
    new_urls = []
    removed_urls = []
    for i in latest_sitemap_urls:
        if i not in previous_sitemap_urls:
            new_urls.append(i)
    for i in previous_sitemap_urls:
        if i not in latest_sitemap_urls:
            removed_urls.append(i)
    changes = [new_urls, removed_urls]
    return changes


def filter_urls(new_urls, filter_words):
    """Returns filtered list of URLs based on URL filtering"""
    filtered_urls = []
    for i in new_urls:
        for j in filter_words:
            if j in i:
                filtered_urls.append(i)
    filtered_urls = list(set(filtered_urls))
    return filtered_urls


def sitemap_last_mod(sitemap_memory):
    """Get time stamp for when previous Sitemap was modified"""
    mod_since_epoc = os.path.getmtime(sitemap_memory)
    last_mod = time.strftime(
        '%Y-%m-%d %H:%M', time.localtime(mod_since_epoc))
    return last_mod


def update_sitemap(new_urls, removed_urls, latest_sitemap_urls):
    """Update Sitemap to latest"""
    if len(new_urls) > 0 or len(removed_urls) > 0:
        ans = input('Update Sitemap? (Y/N): ')
        if ans.lower() == 'y':
            print('Updating Sitemap...')
            with open(sitemap_memory, 'w') as f:
                json.dump(latest_sitemap_urls, f, indent=4)


def main():
    latest_sitemap_urls = get_latest_sitemap_urls(sitemap_urls)
    previous_sitemap_urls = get_previous_sitemap_urls(
        sitemap_memory, latest_sitemap_urls)
    new_urls, removed_urls = compare_sitemaps(
        latest_sitemap_urls, previous_sitemap_urls)

    print("Sitemap previously checked:", sitemap_last_mod(sitemap_memory))
    print("Number of URLs in Sitemap (current):", len(latest_sitemap_urls))
    print("Number of URLs in Sitemap (previous):", len(previous_sitemap_urls))

    print("Number of removed URLs:", len(removed_urls))
    if args.outputremoved == True:
        for i in removed_urls:
            print(i)

    print("Number of new URLs:", len(new_urls))
    if args.outputnew == True:
        for i in new_urls:
            print(i)

    if args.filter != None:
        new_urls_filtered = filter_urls(new_urls, filter_words)
        print('Number of new URLs (filtered):', len(new_urls_filtered))
        for i in new_urls_filtered:
            print(i)

    update_sitemap(new_urls, removed_urls, latest_sitemap_urls)


if __name__ == '__main__':
    main()
