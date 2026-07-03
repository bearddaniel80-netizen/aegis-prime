from datetime import datetime


class SnapshotManager:

    def create_metadata(
        self,
        source_root: str
    ):

        return {
            "snapshot_id":
                datetime.utcnow().strftime(
                    "%Y%m%d_%H%M%S"
                ),

            "created_at":
                datetime.utcnow().isoformat(),

            "source_root":
                source_root,

            "traceplan_version":
                "0.4"
        }