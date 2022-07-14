import boto3
import datetime
import time
from logger import Logger
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import as_completed
from args import parse_args

snapshots_to_delete = []

class SnapshotLifecycle():
    def __init__(self, log_level) -> None:
        self.log = Logger(log_level)
    
    def days_old(self, date):
        date_obj = date.replace(tzinfo=None)
        diff = datetime.datetime.now() - date_obj
        return diff.days
    
    def get_snapshots(self, snapshots, age):
        for snapshot in snapshots['Snapshots']:
            create_date = snapshot['StartTime']
            snapshot_id = snapshot['SnapshotId']
            day_old = self.days_old(create_date)
            if day_old > age:
                snapshots_to_delete.append(snapshot_id)
            else:
                self.log.debug(f"{snapshot_id} will not be delete since is not older than 30 days ago")
        self.log.info(f"Snapshots to delete: {len(snapshots_to_delete)}")
    
    def delete_snapshots(self, client, dry_run, snapshot):
        try:
            if dry_run:
                self.log.info(f"Dry run: deleting {snapshot}")
            else:
                self.log.info(f"Snapshot {snapshot} deleted")
                client.delete_snapshot(SnapshotId=snapshot)
        except Exception as e:
            self.log.warn(f"{e}")
        

def main():
    start = time.perf_counter()
    args = parse_args()
    log = Logger(log_level=args.log_level)
    client = boto3.client('ec2', region_name=args.aws_region)
    snapshots = client.describe_snapshots(OwnerIds=[args.aws_account_id])

    app = SnapshotLifecycle(log_level=args.log_level)
    app.get_snapshots(snapshots,args.age)
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(app.delete_snapshots, client, args.dry_run, snapshot) for snapshot in snapshots_to_delete]
        for future in as_completed(futures):
            if future.result() is not None:
                log.info(f"{future.result()}")

    finish = time.perf_counter()

    log.info(f"Finished in {round(finish - start, 2)} second(s)")

if __name__ == "__main__":
    main()