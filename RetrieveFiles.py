import os
import shutil
import sys

def scan_folder (root_path, recursive, printop, destination, filehandeler, dirhandeler):
    print ("Directory: " + root_path)
    for r, d, f in os.walk (root_path):
        for file in f:
            printop (file)
            filehandeler (root_path, file, destination)
        if (recursive):
            for directory in d:
                child_source = os.path.join(root_path, directory)
                should_process = should_process_directory (child_source)
                if (should_process):
                    child_destination = os.path.join(destination, directory)
                    dirhandeler (child_destination)
                    scan_folder (child_source, recursive, printop, child_destination , filehandeler, dirhandeler)


def should_process_directory (directory):
    # Check to see if the source path actually exists.
    # Have had some issues with pyton and recursion findings paths that doesn't exist
    directory_exists = os.path.exists (directory)
    # Make sure this isn't a directory that should not be coppied.
    # Such as .git
    path = os.path.normpath(directory)
    componants = path.split(os.sep)
    top_level = componants.pop()

    directory_not_hidden = not top_level.startswith (".")
    return directory_exists and directory_not_hidden

def print_file_details (entry):
    if (os.path.isfile):
        print ("==> " + entry)

def fileHandler_move (source_path, file, destination_path):
    source_file = os.path.join(source_path, file)
    destination_file =  os.path.join(destination_path, file)
    # Check to see if the source path actually exists.
    # Have had some issues with pyton and recursion findings paths that doesn't exist
    if (os.path.exists(source_file)):
        # Check if the destination exists.
        # If it does we want to append a number so we don't clobber the old file,
        if (os.path.exists(destination_file)):
            testVal = 1
            testPath = destination_file + "." + str(testVal)
            while (os.path.exists(destination_file + "." + str(testVal))):
                testVal += 1
            # we have a unique path name now to copy
            destination_file = testPath
        # Copy the file to the new location
        shutil.copyfile (source_file, destination_file)
        #Clean up the source
        os.remove (source_file)


def directoryHandler_create (root_directory):
    if (not os.path.exists (root_directory)):
        os.mkdir (root_directory)

print ("Retrieve Files Python Script")
print ("Source Location: " + sys.argv[1])
print ("Destination Location: " + sys.argv[2])
scan_folder (sys.argv[1], True, print_file_details, sys.argv[2], fileHandler_move, directoryHandler_create)