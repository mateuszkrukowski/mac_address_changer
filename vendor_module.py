import random
import logging
import sys


def open_file_and_prepare_list():
    vendors_file = 'vendors.txt'

    try:
        imported_vendors = open(vendors_file, "r")
        pass
    except OSError:
        print(f"Couldn't open or read file {vendors_file}")
        sys.exit(1)
    not_formated_vendors_list = imported_vendors.read()

    formated_vendors_list = not_formated_vendors_list.split('\n')

    imported_vendors.close()

    return formated_vendors_list


def shuffle_list_and_prapare_prefix_vendor():
    formated_vendors_list = open_file_and_prepare_list()

    random.shuffle(formated_vendors_list)

    prefix_and_vendor = formated_vendors_list[(random.randint(0, (len(formated_vendors_list) - 1)))]

    return prefix_and_vendor


def formated_prefix_and_vendor():
    prefix_vendor = shuffle_list_and_prapare_prefix_vendor()

    prefix_vendor = str(prefix_vendor).split()

    prefix = prefix_vendor[0]
    vendor = prefix_vendor[1]

    prefix = ':'.join(prefix[i : i + 2] for i in range(0, len(prefix), 2)) + ':'

    return prefix, vendor
    print(prefix)
    print(vendor)
