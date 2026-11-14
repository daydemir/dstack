---
name: youtube-transcript
description: Read a YouTube video, channel or playlist link. Use whenever the user shares a youtube.com or youtu.be URL, instead of fetching the page.
---

Fetching a YouTube page returns little and is often throttled, and the subtitle endpoint rate-limits our minis. Instead, transcribe the audio on this Mac.

1. **Run.** On an Apple silicon Mac with `yt-dlp` and `ffmpeg` on PATH, run `python3 -I <this skill>/scripts/transcript.py URL OUTDIR`. Point OUTDIR at a new folder in your scratchpad.
   - A video writes `meta.md` and `transcript.txt`. A 10-minute video takes about 40 seconds.
   - A channel or playlist writes `uploads.tsv` with the newest uploads and transcribes nothing. Describe the channel from those titles, then transcribe only the videos the request needs.
   - The first run builds a venv in `~/.cache/youtube-transcript/venv`. If Whisper large-v3-turbo (about 1.6 GB) is not already in `~/.cache/huggingface`, the first run downloads it too. Run `darma storage check` first.
2. **Fix a download error.** The script prints the upgrade command, because an old `yt-dlp` is the usual cause. Note `python3 --version`, run the command, and run the script again.
   - The upgrade can install a newer Python formula that takes over `python3`. Launchd jobs on the minis run that `python3`.
   - If the version moved, restore it: `brew unlink python@NEW && brew unlink python@OLD && brew link python@OLD`.
3. **Read.** Read `meta.md` first: title, channel, date, duration, and the description with its chapters and links. Then read the transcript.
   - Speech recognition mishears names; for example, "herdr" came out as "Herder". Check every product, person and company name against the description's links before you repeat it.
   - Name the video by its title and channel when you report.
