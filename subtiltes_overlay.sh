#!/bin/bash

# Step 1: Capture Audio and Pipe to Python Script
ffmpeg -i input_stream -f s16le -ar 44100 -ac 2 - | python subtitle_generator.py | \

# Step 2: Transcribe and Translate
while IFS= read -r line; do
    echo "$line" | python subtitle_generator.py
done | \

# Step 3: Generate SRT Subtitles (Not implemented in the provided Python code)
python generate_srt.py | \

# Step 4: Overlay Subtitles and Output Stream
ffmpeg -i input_video -vf "subtitles=subtitles.srt" -c:v libx264 -c:a copy -f flv output_stream
