def generate_srt(subtitles):
    srt_content = ""
    for i, (start_time, end_time, text) in enumerate(subtitles, start=1):
        # Format start and end times as HH:MM:SS,mmm
        start_time_str = milliseconds_to_srt_time(start_time)
        end_time_str = milliseconds_to_srt_time(end_time)
        # Write subtitle index
        srt_content += f"{i}\n"
        # Write start and end times
        srt_content += f"{start_time_str} --> {end_time_str}\n"
        # Write subtitle text
        srt_content += f"{text}\n\n"
    return srt_content

def milliseconds_to_srt_time(milliseconds):
    seconds = milliseconds // 1000
    milliseconds = milliseconds % 1000
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

# Example usage
subtitles = [
    (0, 5000, "Hello"),
    (6000, 10000, "How are you?"),
    (11000, 15000, "Goodbye")
]

srt_content = generate_srt(subtitles)
print(srt_content)
