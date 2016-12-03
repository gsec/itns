import subprocess


def get_hash(fname):
    outp = subprocess.run(['ipfs', 'add', fname], stdout=subprocess.PIPE)
    hsh = outp.stdout.decode().split()[1]
    return(hsh)
