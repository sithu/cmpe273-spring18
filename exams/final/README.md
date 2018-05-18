# Coding Question I - 10 pts
Implement __contains__ method of the Bloom Filter using the baseline code: bloomfilter.py

- Expected output

```sh
python3 bloomfilter.py
'abound' is probably present!
'abounds' is probably present!
'abundance' is probably present!
'abundant' is probably present!
'accessable' is probably present!
'bloom' is probably present!
'blossom' is probably present!
'bolster' is probably present!
'bonny' is probably present!
'bonus' is probably present!
'bluff' is definitely not present!
'cheater' is definitely not present!
'hate' is definitely not present!
'war' is definitely not present!
'humanity' is definitely not present!
'racism' is definitely not present!
'hurt' is definitely not present!
'nuke' is definitely not present!
'gloomy' is definitely not present!
'facebook' is definitely not present!
'geeksforgeeks' is definitely not present!
'twitter' is a false positive!
```

# Coding Question II - 20 pts
## Gossip SWIM Protocol

This is the most challenging task and the grading is based on your best effort. The baseline code is handling the first part (ping) of the SWIM Failure Detector.

You will be implementing the second part (ping-req) from the diagram and dissemination part.

To run three Gossip instances:

```sh
python3 gossip.py 5000 5001,5002
```

```sh
python3 gossip.py 5001 5000,5002
```

```sh
python3 gossip.py 5002 5001,5000
```

