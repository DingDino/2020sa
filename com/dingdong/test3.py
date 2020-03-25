import time

if __name__ == '__main__':
    share = {"UnityStorageResource": {"description": "", "existed": 'true',
                                      "filesystem": {"UnityFileSystem": {"hash": 8759255976125, "id": "fs_215"}},
                                      "hash": 8759256063425, "health": {"UnityHealth": {"hash": 8759255975997}},
                                      "id": "res_215", "is_replication_destination": 'false',
                                      "metadata_size": 3489660928,
                                      "metadata_size_allocated": 3758096384,
                                      "name": "f8723d27-f66d-43f2-8ab2-3b0789e4c1e1",
                                      "per_tier_size_used": [0, 0, 6442450944],
                                      "pools": {"UnityPoolList": [{"UnityPool":
                                                                       {"hash": 8759255965289, "id": "pool_1"}}]},
                                      "relocation_policy": "TieringPolicyEnum.AUTOTIER_HIGH",
                                      "replication_type": "ReplicationTypeEnum.NONE", "size_allocated": 283131904,
                                      "size_total": 4831838208, "size_used": 1620303872, "snap_count": 0,
                                      "snaps_size_allocated": 0, "snaps_size_total": 0,
                                      "thin_status": "ThinStatusEnum.TRUE",
                                      "type": "StorageResourceTypeEnum.FILE_SYSTEM"}}
    if share:
        result = share.get()
    print(result)
