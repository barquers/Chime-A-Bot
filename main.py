import discord
import config
from discord.ext import tasks
import asyncio
import datetime
from discord import FFmpegPCMAudio

# Initialize Discord client
client = discord.Client()

# Sets path to audio files
hourly_chime_path = "Tune.mp3"
time_music_path = {
    0: "12AM.mp3",
    1: "1AM.mp3",
    2: "2AM.mp3",
    3: "3AM.mp3",
    4: "4AM.mp3",
    5: "5AM.mp3",
    6: "6AM.mp3",
    7: "7AM.mp3",
    8: "8AM.mp3",
    9: "9AM.mp3",
    10: "10AM.mp3",
    11: "11AM.mp3",
    12: "12PM.mp3",
    13: "1PM.mp3",
    14: "2PM.mp3",
    15: "3PM.mp3",
    16: "4PM.mp3",
    17: "5PM.mp3",
    18: "6PM.mp3",
    19: "7PM.mp3",
    20: "8PM.mp3",
    21: "9PM.mp3",
    22: "10PM.mp3",
    23: "11PM.mp3"
}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    hourly_music.start()

@tasks.loop(hours=1)
async def hourly_music():
    now = datetime.datetime.now()
    hour = now.hour % 12 or 12  # Convert 24-hour format to 12-hour format
    channel = client.get_channel(YOUR_CHANNEL_ID)  # Replace YOUR_CHANNEL_ID with the ID of the voice channel you want Chime to play in
    voice_client = await channel.connect()

    # Play hourly chime
    voice_client.play(discord.FFmpegPCMAudio(hourly_chime_path))
    while voice_client.is_playing():
        await asyncio.sleep(1)
    
    # Play corresponding time music
    music_file = time_music_path.get(hour)
    if music_file:
        voice_client.play(FFmpegPCMAudio(music_file))
        while voice_client.is_playing():
            await asyncio.sleep(1)

    await voice_client.disconnect()

client.run(config.BOT_TOKEN)
