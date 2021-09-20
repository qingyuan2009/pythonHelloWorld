import os

SOURCE_ROOT = "C:/Users/i035299/Documents/GitHub/manage-billing-ui/reviewAutomatedBillingUI/webapp/SharedBlocks"

candidate_exts = [
    ".js",
    ".xml",
]

def is_candidate_file(filepath):
    for ext in candidate_exts:
        if filepath.endswith(ext):
            return True
    return False

def process_file(src_filepath):
    lines = ""
    fd_r = open(src_filepath)
    while True:
        line = fd_r.readline()
        if not line:
            break
        line = line.replace("\t", "    ")
        line = line.rstrip() + "\n"
        lines += line
    fd_r.close()
    lines = lines.rstrip() + "\n\n"
    fd_w = open(src_filepath, "w")
    fd_w.write(lines)
    fd_w.close()

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filepath in files:
            if not is_candidate_file(filepath):
                continue
            full_path = os.path.join(root, filepath)
            print("-> %s" % (full_path))
            process_file(full_path)

def main():
    process_folder(SOURCE_ROOT)

main()
