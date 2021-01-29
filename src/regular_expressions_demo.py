import re

def get_brand_from_filename(file_name):
    try:
        # NOTE: if we put a single backslash in front of a dot in a search string we'll get
        # the following warning:
        # Anomalous backslash in string: '\.'. String constant might be missing an r prefix.
        # Backslash (\) is used as an escape for regular escape sequences (\n, \r etc...)
        # and also for regex search strings. Python interpreter first replaces regular
        # escapes e.g. \n with new line unicode character and then it comes to re module.
        # In our case \. is not a regular escape sequence so Python interperter left is as
        # it is (a raw string) but then linter complained. To silent the linter we can either
        # use \\ or indicate explicilty that we want this to be a raw string.
        # pattern = '\.(.+?)-' # this version gives a linter warning
        # pattern = '\\.(.+?)-' # this is ok but can get too verbose if have many backslashes
        pattern = r'\.(.+?)-' # this is the best solution here

        # Scan through string looking for the first location where this regular expression produces
        # a match, and return a corresponding match object. Return None if no position in the string
        # matches the pattern
        match = re.search(pattern, file_name) # <re.Match object; span=(18, 26), match='.brandA-'>

        match = None
        # match.groups() returns a tuple containing all the subgroups of the match, from 1 up to
        # however many groups are in the pattern.
        print(f'match.groups() = {match.groups()}')

        brand = match.group(1)
    except AttributeError:
        brand = ''
    return brand

def get_brand_from_filename_tests():
    file_name = 'C:/path/to/product.brandA-1.2.3.ext'
    print(f'file_name = {file_name}; brand = {get_brand_from_filename(file_name)}')

# Returns version number as M, M.m, M.m.r or M.m.r.b
def get_version_from_filename(file_name):
    version = ""
    pattern = r'\d+\.(?:\d+\.)*\d+'
    # pattern = r'(?:(\d+\.(?:\d+\.)*\d+))'

    # Return all non-overlapping matches of pattern in string, as a list of strings.
    # The string is scanned left-to-right, and matches are returned in the order found.
    # If one or more groups are present in the pattern, return a list of groups; this will be
    # a list of tuples if the pattern has more than one group. Empty matches are included in the result.
    match = re.findall(pattern, file_name)
    print(match)
    if match == []:
        print("WARNING: No version found")
        return ""

    version = match[0]
    return version

def get_version_from_filename_tests():
    file_name = 'C:/path/to/product.brandA-1.ext'
    print(f'file_name = {file_name}; version = {get_version_from_filename(file_name)}')

    file_name = 'C:/path/to/product.brandA-1.2.ext'
    print(f'file_name = {file_name}; version = {get_version_from_filename(file_name)}')

    file_name = 'C:/path/to/product.brandA-12.3.ext'
    print(f'file_name = {file_name}; version = {get_version_from_filename(file_name)}')

    file_name = 'C:/path/to/product.brandA-1.2.3.ext'
    print(f'file_name = {file_name}; version = {get_version_from_filename(file_name)}')

    file_name = 'C:/path/to/product.brandA-1.23.456.7890.ext'
    print(f'file_name = {file_name}; version = {get_version_from_filename(file_name)}')

    file_name = 'C:/path/to/product.brandA-1234.567.89.0.ext'
    print(f'file_name = {file_name}; version = {get_version_from_filename(file_name)}')


def regular_expressions_demo():
    # get_brand_from_filename_tests()
    get_version_from_filename_tests()