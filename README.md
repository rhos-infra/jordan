# jordan

Jordan is an Infrared plugin testing the Ceph cluster, its state, its configuration and its topology.
The tests are separated by sections:
  - overall cluster state
  - monitors state
  - OSDs state (up/in)
  - pool configuration
  - client permissions

usage:
infrared jordan \
                --monitor-nodes [node] \
                --osds-number 3 \
                --ceph-pools [pool],[pool]... \
                --pool-pg_num 128 \
                --pool-pgp_num 128 \
                --pool-size 3 \
                --pool-min_size 2 \
                --openstack-client-name [opensatck]
