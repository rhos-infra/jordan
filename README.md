# jordan

Jordan is an Infrared plugin testing the Ceph cluster, its state, its configuration and its topology.
The tests are separated by sections, defined by `main.yml`:
  - overall cluster state (`cluster.yml`)
  - monitors state (`monitors.yml`)
  - OSDs state (`osds.yml`)
  - pool configuration (`pools.yml`)
  - client permissions (`clients.yml`)
  - file content checks (`file_contents.yml`)

# for Ceph 2.x
infrared jordan --monitor-nodes controller /\
                --ceph-pools volumes,vms,images,... /\
                --osds-number 5 /\
                --pool-pg_num 32 /\
                --pool-pgp_num 32 /\
                --pool-size 3 /\
                --pool-min_size 1 /\
                --openstack-client-name openstack 

# for Ceph 3.x
infrared jordan --monitor-nodes controller /\
                --ceph-pools volumes,vms,images,... /\
                --osds-number 5 /\
                --pool-pg_num 32 /\
                --pool-pgp_num 32 /\
                --pool-size 3 /\
                --pool-min_size 1 /\
                --openstack-client-name openstack /\
                --ansible-args "skip-tags=monitors"

# for Ceph 4.x
TODO
