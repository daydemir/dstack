---
name: youtube-transcript
description: Read a YouTube video, channel or playlist link, or look at a video's frames. Use whenever the user shares a youtube.com or youtu.be URL, instead of fetching the page.
---

Fetching a YouTube page returns little and is often throttled, and the subtitle endpoint rate-limits our minis. Instead, transcribe the audio and pull frames on this Mac. `python3 -I <this skill>/scripts/youtube.py --help` lists the commands. Both need an Apple silicon Mac with `yt-dlp` and `ffmpeg` on PATH. Give each video its own new OUTDIR in your scratchpad, and reuse it across commands.

1. **Transcribe.** Run `youtube.py transcript URL OUTDIR`.
   - A video writes `meta.md` and `transcript.txt`, with one `[M:SS] text` line per segment. A 10-minute video takes about 40 seconds.
   - A channel or playlist writes `uploads.tsv` with the newest uploads and transcribes nothing. Describe the channel from those titles, then transcribe only the videos the request needs.
   - The first run builds a venv in `~/.cache/youtube-transcript/venv`. If Whisper large-v3-turbo (about 1.6 GB) is not already in `~/.cache/huggingface`, the first run downloads it too. Run `darma storage check` first.
2. **Fix a download error.** The script prints the upgrade command, because an old `yt-dlp` is the usual cause. Note `python3 --version`, run the command, and run the script again.
   - The upgrade can install a newer Python formula that takes over `python3`. Launchd jobs on the minis run that `python3`.
   - If the version moved, restore it: `brew unlink python@NEW && brew unlink python@OLD && brew link python@OLD`.
3. **Read.** Read `meta.md` first: title, channel, date, duration, and the description with its chapters and links. Then read the transcript.
   - Speech recognition mishears names; for example, "herdr" came out as "Herder". Check every product, person and company name against the description's links before you repeat it.
   - Name the video by its title and channel when you report.
4. **Look.** When the answer depends on the screen (slides, code, a UI, a chart, a demo), run `youtube.py frames URL OUTDIR` with one of these, then view the frames you need:
   - `--at 1:23 4:56`: the moments the transcript points at ("as you can see here"). This is the usual choice.
   - `--scenes`: one frame per scene change, to skim a slide deck or screencast. A 10-minute film gave 123 frames in under a minute.
   - `--every SECONDS`: an even sample, for footage without clear cuts.
   - Frames land in `OUTDIR/frames/HH-MM-SS.jpg` at up to 1280px wide. The first frames run downloads the video at up to 720p (about 80 MB for 10 minutes) into `OUTDIR/video/`; later runs reuse it.
