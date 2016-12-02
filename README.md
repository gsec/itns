ITNS - intergalactic trust name space
========================================

This is an attempt to make the secure ipfs hashes more accessible to human minds.
In order to achieve this translation we build a global mutable space based on names and an 
UNIX/POSIX file system structure.
A local database attaches a name to some ipfs hash, we can repeat this as many times as 
needed. The collection of name <> hash linking is then called the local name space. The 
name space then can be published through the ipns protocol and gets signed by the 
publisher.
Every client then can `claim` to put it in a specific location of the itns. Every one can 
put a name (which is linked to a hash) in the global name space as long as it complies 
with formating rules etc. 

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
