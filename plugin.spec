---
plugin_type: test
subparsers:
    jordan:
        description:
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:

          - title: Ceph cluster
            options:
                ceph-version:
                    type: Value
                    help: Ceph's major version
                    default: '3'
                    
          - title: Ceph monitor nodes
            options:

                monitor-nodes:
                    type: Value
                    help: The node type on which Ceph's monitors are running
                    default: controller
          - title: Cpeh registry provider
            options:
                 ceph-reg-provider:
                    type: Value
                    help: docker for ceph v3 cnd podman for v4
                    default: 'docker'

          - title: Ceph OSD nodes
            options:

                osds-number:
                    type: Value
                    help: the number of OSDs in the cluster
                    default: 3

          - title: Ceph pools
            options:

                ceph-pools:
                    type: Value
                    help: the names of the deployed pools
                    default: volumes,images,vms,backups

                pool-pg_num:
                    type: Value
                    help: specify the pg_num in the pools
                    default: 128

                pool-pgp_num:
                    type: Value
                    help: specify the pg_num in the pools
                    default: 128

                pool-size:
                    type: Value
                    help: specify the size (replicas) set for the pools
                    default: 3

                pool-min_size:
                    type: Value
                    help: specify the minimum size (replicas) set for the pools
                    default: 2

          - title: Ceph clients
            options:

                openstack-client-name:
                    type: Value
                    help: the name of the client set for the Openstack services
                    default: openstack