.. _itns:

ITNS
====


Prologue
---------
The interplanetary file system (`IPFS <https://ipfs.io/>`_) is a structure to organize 
data based on self-authenticating names (namely the cryptographic hashes of a data block). 
Hashes can be grouped to form a parent, which is the hash of hashes. This form of data is 
known as merkle tree, or in its generalized form, as merkle directed acyclic graph (DAG).

An outstanding advantage of such a system is, that given a root hash, all sub-hashes and
inner objects can be authenticated. This means, given the correct hash one can retrieve
data and confirm its integrity, independent from the actual provider of the data. This
makes it very well suited for organization of information in the time of decentralization.

The purpose of this project is to create a link between IPFS hashes and a human readable
name space. We aim to take the power of cryptographic hashes and link it to meaningful
names bringing practicality into everyday usage.

Individual nodes name spaces
----------------------------
To lift the restriction (which definitely is a feature) of immutability, each node in the
IPFS network, addressed by the hash of its public key, can publish their own hash. Meaning
every node can set a link from their name to a given file, directory or any kind of 
digital information representable by a merkle dag. Taking this further, every node can
publish a directory structure containing all data it wants to publish. This leads to a
network of nodes, each containing its own name space. These published hashes can be
accessed individually per peer, while the containing data will be retrieved over the
entire network.


Intergalactic Trust Name Space
==============================

Lists and list of lists
-----------------------
The foundation of IPFS is the hash-based naming, securing integrity and immutability. The
downside is that those are not as meaningful for humans, who can not distinguish, yet 
alone remember, these hashes for a large number of files.

A simple solution that pops into mind would be keeping a database of files and the
corresponding hashes. When looking for a file, one would query the database to then
retrieve the file from the network. Every node (here as individual network participant)
can have his own curated list of data blobs he wants to store and access.

.. image:: _static/ipns_example.svg

One populated name space
------------------------
This is an attempt to make the secure ipfs hashes more accessible to human minds.
In order to achieve this translation we build a global mutable space based on names and an 
UNIX/POSIX file system structure. A local database attaches a name to some ipfs hash, we 
can repeat this as many times as needed. The collection of name <> hash linking is then 
called the local name space. The name space then can be published through the ipns 
protocol and gets signed by the publisher. Every client then can `claim` to put it in a 
specific location of the itns. Every one can put a name (which is linked to a hash) in the 
global name space as long as it complies with formating rules etc. 

Let a local trusted namespace be 'L/ipfs/go'-<hash> (L for local, I for intergalactic).
We could publish this record and have it broadcast to 'I/repos/go'-<hash>-<pubkey>

The important things is that anyone can populate the name space at will (every entry once)
But the equal hashes are then brought together. All same hashes on the global name space 
will then be signed by public key owners, for which elevated trust levels are possible 
such as in PKI-like structures.

So a distributor of an app can have the ultimate authority for a specific path down the 
itns in a specific, local configuration. Also with multiple distributors(who have acquired 
some trust from the local user) claiming a name be populated with a certain ipfs hash and 
therefore the same data, the certainty of this data blob being the right one is increased.
