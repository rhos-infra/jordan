# jordan

Jordan is an Infrared plugin testing the Ceph cluster, its state, its configuration and its topology.
The tests are separated by sections:
  - overall cluster state
  - monitors state
  - OSDs state (up/in)
  - pool configuration
  - client permissions

usage:
infrared jordan --monitor-nodes controller\
                --ceph-pools volumes,vms,images,... \
                --osds-number 5 \
                --pool-pg_num 32 \
                --pool-pgp_num 32 \
                --pool-size 3 \
                --pool-min_size 1 \
                --openstack-client-name openstack \
                # for Ceph 3.x
                --ansible-args "skip-tags=monitors"