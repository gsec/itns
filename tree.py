import ipfsapi


api = ipfsapi.connect(host='localhost', port=5001)


def walker(rhash):
    dirlist = api.file_ls(rhash)
    links = dirlist['Objects'][rhash]['Links']
    if not links:
        return None

    for obj in links:
        if obj['Type'] == 'Directory':
            obj['content'] = walker(obj['Hash'])
    return links


def tree_map():
    root_obj = api.files_stat('/')
    root_obj['Name'] = '/'
    root_obj['content'] = walker(root_obj['Hash'])
    root_obj['Type'] = 'Root'

    return root_obj


if __name__ == '__main__':
    import pprint
    pprint.PrettyPrinter().pprint(tree_map())
