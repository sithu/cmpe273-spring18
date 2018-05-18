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

![](https://www.brianstorti.com/assets/images/swim/failure-detection.png)


[SWIM Paper](https://pdfs.semanticscholar.org/8712/3307869ac84fc16122043a4a313604bd948f.pdf)


### Abstract

The SWIM failure detector algorithm uses two parameters: protocol period T (in time units) and integer k, the size of failure detection subgroups. The protocol does not require clocks to be synchronized across members, and properties of the protocol hold if T is the average protocol period at group members.

Figure 1 illustrates the working of the protocol at an arbitrary member Mi. During each protocol period of length T time units (on M's local clock), a random member is
selected from Mi's membership list (say Mj), and a ping message sent to it. Mi then waits for a replying ack from

- If this is not received within a prespecified time-out (determined by the message round-trip time, which is chosen smaller than the protocol period), indirectly probes Mj. Mi selects k members at random and sends each a ping-req(Mj) message. Each of these members in turn (those that are non-faulty), on receiving this message, pings Mj and forwards the ack from Mj (if received) back to Mi.

- At the end of this protocol period, Mi checks if it has received any acks, directly from or indirectly through one of the k members; if not, it declares as failed in
its local membership list, and hands this update off to the Dissemination Component.

```

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

