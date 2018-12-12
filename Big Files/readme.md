
Big Files Assignment

Python Features Required: os.walk, os.path.getsize

File(s) to Submit: bigfiles.py

Specification:
It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive.
If you’re trying to free up room on your computer, you’ll get the most bang for your buck by deleting the most massive of the unwanted files. But first you have to find them.
Write a function bigfiles() with argument a folder path basepth. The function should walk through the folder tree starting at basepth searching for files whose size excedes 100MB. Remember that to get a file’s size, you can use os.path.getsize() from
the os module. The function should return a list of the paths to these files.
