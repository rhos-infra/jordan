# jordan

Jordan is an Infrared plugin testing the Ceph cluster, its state, its configuration and its topology.
The tests are separated by sections:
  - overall cluster state
  - monitors state
  - OSDs state (up/in)
  - pool configuration
  - client permissions

usage:
infrared jordan --check-cluster true \
                --check-monitors true \
                --check-osds true \
                --check-clients true \
                --ceph-pools <pool>,<pool>,... \
                --pool-pg_num 32 \
                --pool-pgp_num 32 \
                --pool-size 3 \
                --openstack-client-name <client>
