class SnapshotArray:

    def __init__(self, length: int):
        self.snapSet = {}
        self.current = [0] * length
        self.currentsnap = -1

    def set(self, index: int, val: int) -> None:
        self.current[index] = val

    def snap(self) -> int:
        self.currentsnap += 1
        self.snapSet[self.currentsnap] = list(self.current)
        return self.currentsnap

    def get(self, index: int, snap_id: int) -> int:
        return self.snapSet[snap_id][index]
