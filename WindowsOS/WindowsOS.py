import os
import shutil

folder_to_track = 'C:\\Users\\wikyprash\\Desktop\\'

os.chdir(folder_to_track)
UserProfile = os.environ.get('USERPROFILE')

extensions_folders = {
    # No name
    'noname': f"{UserProfile}\\Desktop\\Other\\Uncategorized",
    # Audio
    '.aif': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.cda': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.mid': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.midi': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.mp3': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.mpa': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.ogg': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.wav': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.wma': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.wpl': f"{UserProfile}\\Desktop\\Media\\Audio",
    '.m3u': f"{UserProfile}\\Desktop\\Media\\Audio",
    # Docs
    '.txt': f"{UserProfile}\\Desktop\\Docs\\TextFiles",
    '.doc': f"{UserProfile}\\Desktop\\Docs\\Microsoft\\Word",
    '.docx': f"{UserProfile}\\Desktop\\Docs\\Microsoft\\Word",
    '.odt ': f"{UserProfile}\\Desktop\\Docs\\TextFiles",
    '.pdf': f"{UserProfile}\\Desktop\\Docs\\PDF",
    '.rtf': f"{UserProfile}\\Desktop\\Docs\\TextFiles",
    '.tex': f"{UserProfile}\\Desktop\\Docs\\TextFiles",
    '.wks ': f"{UserProfile}\\Desktop\\Docs\\TextFiles",
    '.wps': f"{UserProfile}\\Desktop\\Docs\\TextFiles",
    '.wpd': f"{UserProfile}\\Desktop\\Docs\\TextFiles",
    # Video
    '.3g2': f"{UserProfile}\\Desktop\\Media\\Video",
    '.3gp': f"{UserProfile}\\Desktop\\Media\\Video",
    '.avi': f"{UserProfile}\\Desktop\\Media\\Video",
    '.flv': f"{UserProfile}\\Desktop\\Media\\Video",
    '.h264': f"{UserProfile}\\Desktop\\Media\\Video",
    '.m4v': f"{UserProfile}\\Desktop\\Media\\Video",
    '.mkv': f"{UserProfile}\\Desktop\\Media\\Video",
    '.mov': f"{UserProfile}\\Desktop\\Media\\Video",
    '.mp4': f"{UserProfile}\\Desktop\\Media\\Video",
    '.mpg': f"{UserProfile}\\Desktop\\Media\\Video",
    '.mpeg': f"{UserProfile}\\Desktop\\Media\\Video",
    '.rm': f"{UserProfile}\\Desktop\\Media\\Video",
    '.swf': f"{UserProfile}\\Desktop\\Media\\Video",
    '.vob': f"{UserProfile}\\Desktop\\Media\\Video",
    '.wmv': f"{UserProfile}\\Desktop\\Media\\Video",
    # Images
    '.ai': f"{UserProfile}\\Desktop\\Media\\Images",
    '.bmp': f"{UserProfile}\\Desktop\\Media\\Images",
    '.gif': f"{UserProfile}\\Desktop\\Media\\Images",
    '.ico': f"{UserProfile}\\Desktop\\Media\\Images",
    '.jpg': f"{UserProfile}\\Desktop\\Media\\Images",
    '.jpeg': f"{UserProfile}\\Desktop\\Media\\Images",
    '.png': f"{UserProfile}\\Desktop\\Media\\Images",
    '.ps': f"{UserProfile}\\Desktop\\Media\\Images",
    '.psd': f"{UserProfile}\\Desktop\\Media\\Images",
    '.svg': f"{UserProfile}\\Desktop\\Media\\Images",
    '.tif': f"{UserProfile}\\Desktop\\Media\\Images",
    '.tiff': f"{UserProfile}\\Desktop\\Media\\Images",
    '.CR2': f"{UserProfile}\\Desktop\\Media\\Images",
    # Internet
    '.asp': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.aspx': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.cer': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.cfm': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.cgi': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.pl': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.css': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.htm': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.js': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.jsp': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.part': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.php': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.rss': f"{UserProfile}\\Desktop\\Other\\Internet",
    '.xhtml': f"{UserProfile}\\Desktop\\Other\\Internet",
    # Compressed
    '.7z': f"{UserProfile}\\Desktop\\Other\\Compressed",
    '.arj': f"{UserProfile}\\Desktop\\Other\\Compressed",
    '.deb': f"{UserProfile}\\Desktop\\Other\\Compressed",
    '.pkg': f"{UserProfile}\\Desktop\\Other\\Compressed",
    '.rar': f"{UserProfile}\\Desktop\\Other\\Compressed",
    '.rpm': f"{UserProfile}\\Desktop\\Other\\Compressed",
    '.tar.gz': f"{UserProfile}\\Desktop\\Other\\Compressed",
    '.z': f"{UserProfile}\\Desktop\\Other\\Compressed",
    '.zip': f"{UserProfile}\\Desktop\\Other\\Compressed",
    # Disc
    '.bin': f"{UserProfile}\\Desktop\\Other\\Disc",
    '.dmg': f"{UserProfile}\\Desktop\\Other\\Disc",
    '.iso': f"{UserProfile}\\Desktop\\Other\\Disc",
    '.toast': f"{UserProfile}\\Desktop\\Other\\Disc",
    '.vcd': f"{UserProfile}\\Desktop\\Other\\Disc",
    # Data
    '.csv': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.dat': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.db': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.dbf': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.log': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.mdb': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.sav': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.sql': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.tar': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.xml': f"{UserProfile}\\Desktop\\Programming\\Database",
    '.json': f"{UserProfile}\\Desktop\\Programming\\Database",
    # Executables
    '.apk': f"{UserProfile}\\Desktop\\Other\\Executables",
    '.bat': f"{UserProfile}\\Desktop\\Other\\Executables",
    '.com': f"{UserProfile}\\Desktop\\Other\\Executables",
    '.exe': f"{UserProfile}\\Desktop\\Other\\Executables",
    '.gadget': f"{UserProfile}\\Desktop\\Other\\Executables",
    '.jar': f"{UserProfile}\\Desktop\\Other\\Executables",
    '.wsf': f"{UserProfile}\\Desktop\\Other\\Executables",
    # Fonts
    '.fnt': f"{UserProfile}\\Desktop\\Other\\Fonts",
    '.fon': f"{UserProfile}\\Desktop\\Other\\Fonts",
    '.otf': f"{UserProfile}\\Desktop\\Other\\Fonts",
    '.ttf': f"{UserProfile}\\Desktop\\Other\\Fonts",
    # Presentations
    '.key': f"{UserProfile}\\Desktop\\Docs\\Presentations",
    '.odp': f"{UserProfile}\\Desktop\\Docs\\Presentations",
    '.pps': f"{UserProfile}\\Desktop\\Docs\\Presentations",
    '.ppt': f"{UserProfile}\\Desktop\\Docs\\Presentations",
    '.pptx': f"{UserProfile}\\Desktop\\Docs\\Presentations",
    # Programming
    '.c': f"{UserProfile}\\Desktop\\Programming\\C&C++",
    '.class': f"{UserProfile}\\Desktop\\Programming\\Java",
    '.dart': f"{UserProfile}\\Desktop\\Programming\\Dart",
    '.py': f"{UserProfile}\\Desktop\\Programming\\Python",
    '.sh': f"{UserProfile}\\Desktop\\Programming\\Shell",
    '.swift': f"{UserProfile}\\Desktop\\Programming\\Swift",
    '.html': f"{UserProfile}\\Desktop\\Programming\\C&C++",
    '.h': f"{UserProfile}\\Desktop\\Programming\\C&C++",
    # Spreadsheets
    '.ods': f"{UserProfile}\\Desktop\\Docs\\Microsoft\\Excel",
    '.xlr': f"{UserProfile}\\Desktop\\Docs\\Microsoft\\Excel",
    '.xls': f"{UserProfile}\\Desktop\\Docs\\Microsoft\\Excel",
    '.xlsx': f"{UserProfile}\\Desktop\\Docs\\Microsoft\\Excel",
    # System
    '.bak': f"{UserProfile}\\Desktop\\Other\\System",
    '.cab': f"{UserProfile}\\Desktop\\Other\\System",
    '.cfg': f"{UserProfile}\\Desktop\\Other\\System",
    '.cpl': f"{UserProfile}\\Desktop\\Other\\System",
    '.cur': f"{UserProfile}\\Desktop\\Other\\System",
    '.dll': f"{UserProfile}\\Desktop\\Other\\System",
    '.dmp': f"{UserProfile}\\Desktop\\Other\\System",
    '.drv': f"{UserProfile}\\Desktop\\Other\\System",
    '.icns': f"{UserProfile}\\Desktop\\Other\\System",
    '.ini': f"{UserProfile}\\Desktop\\Other\\System",
    '.lnk': f"{UserProfile}\\Desktop\\Other\\System",
    '.msi': f"{UserProfile}\\Desktop\\Other\\System",
    '.sys': f"{UserProfile}\\Desktop\\Other\\System",
    '.tmp': f"{UserProfile}\\Desktop\\Other\\System",

    '': f"{UserProfile}\\Desktop\\Folders"
}


def Cleaner():
    for filename in os.listdir(folder_to_track):
        i = 1
        if filename not in ['desktop.ini', 'automations']:
            try:
                new_name = filename
                extension = 'noname'
                try:
                    extension = str(os.path.splitext(
                        folder_to_track + '/' + filename)[1])
                except Exception:
                    extension = 'noname'

                folder_destination_path = extensions_folders[extension]
                if not os.path.exists(folder_destination_path):
                    os.makedirs(folder_destination_path)

                file_exists = os.path.isfile(
                    folder_destination_path + "/" + new_name)
                while file_exists:
                    i += 1
                    new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(
                        i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(
                        folder_destination_path + "/" + new_name)
                src = folder_to_track + "/" + filename

                new_name = folder_destination_path + "/" + new_name
                os.rename(src, new_name)
            except Exception as e:
                print(e)


Cleaner()
