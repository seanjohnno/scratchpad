
from dataclasses import dataclass
import os
from pathlib import Path

import photos


@dataclass
class UploadedStats:
    uploaded: int
    not_uploaded: int


def scan():
    uploaded = os.path.join(Path(os.path.abspath(__file__)).parent, 'uploaded.txt')
    with open(uploaded, 'r') as f:
        uploaded = {l.strip():'' for l in f.readlines() if l.strip() != ''}

    stats = UploadedStats(0, 0)
    assets = photos.get_assets()
    for photo in assets:
        if photo.local_id in uploaded:
            stats.uploaded += 1
        else:
            stats.not_uploaded += 1

    return stats

def remove():
    uploaded = os.path.join(Path(os.path.abspath(__file__)).parent, 'uploaded.txt')
    with open(uploaded, 'r') as f:
        uploaded = {l.strip():'' for l in f.readlines() if l.strip() != ''}
    for photo in photos.get_assets():
        if photo.local_id in uploaded:
            photo.delete()


if __name__ == '__main__':
    output = scan()
    print(f'Uploaded: {output.uploaded}, NotUploaded: {output.not_uploaded}')
