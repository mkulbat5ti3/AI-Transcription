import os
import shutil
import datetime

AUDIO_DIR = "audio_files"
ARCHIVE_DIR = "archive"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(ARCHIVE_DIR, exist_ok=True)

def get_timestamped_filename(client_id, ext="wav"):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{client_id}_{now}.{ext}", now[:10]

def copy_to_archive(file_path, client_id):
    _, date = get_timestamped_filename(client_id)
    archive_day_dir = os.path.join(ARCHIVE_DIR, date)
    os.makedirs(archive_day_dir, exist_ok=True)
    destination = os.path.join(archive_day_dir, os.path.basename(file_path))
    shutil.copy(file_path, destination)
    return destination

def save_text_to_archive(client_id, date, text, suffix):
    folder = os.path.join(ARCHIVE_DIR, date)
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{client_id}_{suffix}.txt")
    with open(path, "w") as f:
        f.write(text)
    return path
