from huggingface_hub import snapshot_download

dataset_repo = "robbyant/robotwin-clean-and-aug-lerobot"
local_dir = "/mnt/nas/datasets5/robotwin_lerobot"

snapshot_download(
    repo_id=dataset_repo,
    repo_type="dataset",
    local_dir=local_dir,
    local_dir_use_symlinks=False,
    resume_download=True
)