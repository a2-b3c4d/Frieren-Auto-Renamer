import asyncio
import logging
import os
import re
import shutil
import subprocess

from pyrogram import Client, filters
from pyrogram.types import Message

import codeflixbots  # Assuming this is your custom module

logger = logging.getLogger(__name__)

# Function to extract season and episode from filename
def extract_season_episode(file_name):
    try:
        season = None
        episode = None
        # Regex patterns for season and episode extraction
        season_patterns = [
            r"S(\d{1,2})E\d{1,2}",       # S01E02
            r"Season[ ._]?(\d{1,2})",    # Season 01 or Season_01
            r"(\d{1,2})x\d{1,2}"         # 1x02
        ]
        episode_patterns = [
            r"S\d{1,2}E(\d{1,2})",       # S01E02
            r"Episode[ ._]?(\d{1,2})",   # Episode 02
            r"\d{1,2}x(\d{1,2})"         # 1x02
        ]

        for pat in season_patterns:
            match = re.search(pat, file_name, re.IGNORECASE)
            if match:
                season = match.group(1)
                break

        for pat in episode_patterns:
            match = re.search(pat, file_name, re.IGNORECASE)
            if match:
                episode = match.group(1)
                break

        return season, episode
    except Exception as e:
        logger.error(f"Error extracting season/episode: {e}")
        return None, None

# Function to extract quality
def extract_quality(file_name):
    try:
        quality_patterns = [
            r"(720p|1080p|480p|2160p|4K|8K)"
        ]
        for pat in quality_patterns:
            match = re.search(pat, file_name, re.IGNORECASE)
            if match:
                return match.group(1)
        return "Unknown"
    except Exception as e:
        logger.error(f"Error extracting quality: {e}")
        return "Unknown"

async def process_thumbnail(user_id, thumb_path):
    # Dummy implementation - replace with your real processing if needed
    if not thumb_path or not os.path.exists(thumb_path):
        logger.warning(f"No valid thumbnail found for user {user_id}")
        return None
    # You may add resizing/conversion logic here
    return thumb_path

async def add_metadata(file_path, metadata):
    """
    Adds metadata to a video file using ffmpeg.
    `metadata` is expected to be a dict with keys like 'title', 'artist', etc.
    """
    try:
        cmd = [
            "ffmpeg", "-y", "-i", file_path,
            "-metadata", f"title={metadata.get('title', '')}",
            "-metadata", f"artist={metadata.get('artist', '')}",
            "-codec", "copy",
            file_path + ".tmp"
        ]
        logger.info(f"Running ffmpeg for metadata: {' '.join(cmd)}")
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            logger.error(f"ffmpeg failed: {stderr.decode()}")
            return False
        # Replace original file with updated one
        os.replace(file_path + ".tmp", file_path)
        return True
    except Exception as e:
        logger.error(f"Exception in add_metadata: {e}")
        return False

@Client.on_message(filters.command("autorename") & filters.private)
async def autorename(client: Client, message: Message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        await message.reply_text(
            "**Usage:**\n/autorename [format]\n\n"
            "Use placeholders:\n"
            "`{season}`, `{episode}`, `{quality}`\n\n"
            "Example:\n"
            "`Season {season} Episode {episode} [QUALITY {quality}]`"
        )
        return

    format_template = " ".join(message.command[1:])
    if len(format_template) > 250:
        await message.reply_text("Rename format is too long (max 250 characters).")
        return

    await codeflixbots.set_format_template(user_id, format_template)
    await message.reply_text(f"Auto rename format set to:\n`{format_template}`")

@Client.on_message(filters.private & filters.incoming)
async def auto_rename_files(client: Client, message: Message):
    user_id = message.from_user.id

    try:
        media = None
        media_type = None
        file_name = None

        # Check what media type is present
        if message.video:
            media = message.video
            media_type = "video"
            file_name = media.file_name or "video.mp4"
        elif message.document:
            media = message.document
            media_type = "document"
            file_name = media.file_name or "file.dat"
        else:
            logger.info("No video or document found in message")
            return  # Not a media message we want to process

        logger.info(f"User {user_id} uploaded file: {file_name} ({media_type})")

        # Extract season, episode, quality info from the filename
        season, episode = extract_season_episode(file_name)
        quality = extract_quality(file_name)
        logger.info(f"Extracted season={season}, episode={episode}, quality={quality}")

        # Get the user’s rename format
        format_template = await codeflixbots.get_format_template(user_id)
        if not format_template:
            logger.info(f"No rename format set for user {user_id}")
            return  # No rename template set, do nothing

        # Replace placeholders in format_template
        replacements = {
            '{season}': season or 'XX',
            '{episode}': episode or 'XX',
            '{quality}': quality or 'Unknown',
            'Season': season or 'XX',
            'Episode': episode or 'XX',
            'QUALITY': quality or 'Unknown',
        }

        for placeholder, value in replacements.items():
            format_template = format_template.replace(placeholder, value)

        # Ensure the final filename has the original extension
        ext = os.path.splitext(file_name)[1] or ".mp4"
        new_file_name = f"{format_template.strip()}{ext}"

        logger.info(f"Renaming file to: {new_file_name}")

        # Download the media
        download_path = await client.download_media(message=message, file_name=new_file_name)

        # Process thumbnail if available
        thumb_path = None
        if media.thumb:
            thumb_path = await client.download_media(media.thumb)
            thumb_path = await process_thumbnail(user_id, thumb_path)

        # Add metadata if video
        if media_type == "video":
            metadata = {
                "title": new_file_name,
                "artist": "YourBotName"  # Customize if needed
            }
            success = await add_metadata(download_path, metadata)
            if not success:
                logger.warning(f"Metadata addition failed for {download_path}")

        # Upload the renamed file back to user
        await message.reply_document(
            document=download_path,
            thumb=thumb_path,
            caption=f"Here is your renamed file:\n`{new_file_name}`",
            quote=True
        )

        # Cleanup downloaded files
        try:
            os.remove(download_path)
            if thumb_path:
                os.remove(thumb_path)
        except Exception as e:
            logger.error(f"Error cleaning up files: {e}")

    except Exception as e:
        logger.error(f"Error in auto_rename_files handler: {e}")
        await message.reply_text("Sorry, something went wrong while processing your file.")
