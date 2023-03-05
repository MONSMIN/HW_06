
import os
import shutil
import sys

def normalize(name):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh',
        'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'iu', 'я': 'ia'
    }
    translit_alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    name = name.lower()
    name = ''.join([translit_dict.get(i, i) for i in name])
    name = ''.join([i if i in translit_alphabet else '_' for i in name])
    return name


def sort_folder(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name, file_extension = os.path.splitext(file)
            new_file_name = normalize(file_name)
            new_file_name = f"{new_file_name}{file_extension}"
            new_file_path = os.path.join(root, new_file_name)
            
            # Ігнорування певних папок
            if os.path.basename(root) in ['archives', 'video', 'audio', 'documents', 'images']:
                continue
            
            # Обробка архівів
            if file_extension in ['.zip', '.gz', '.tar']:
                new_dir_name = os.path.join(root, file_name)
                new_dir_path = os.path.join(root, new_dir_name)
                if not os.path.exists(new_dir_path):
                    os.makedirs(new_dir_path)
                shutil.unpack_archive(file_path, new_dir_path)
                os.remove(file_path)
                continue
            
            # Обробка зображень
            if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.svg']:
                target_folder = os.path.join(root, 'images')
            
            # Обробка відео
            elif file_extension.lower() in ['.avi', '.mp4', '.mov', '.mkv']:
                target_folder = os.path.join(root, 'video')
            
            # Обробка документів
            elif file_extension.lower() in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                target_folder = os.path.join(root, 'documents')
            
            # Обробка музики
            elif file_extension.lower() in ['.mp3', '.ogg', '.wav', '.amr']:
                target_folder = os.path.join(root, 'audio')
            
            # Невідомі файли
            else:
                target_folder = os.path.join(root, 'unknown')
            
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
                
            shutil.move(file_path, os.path.join(target_folder, new_file_name))
            
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)


if __name__ == '__main__':
    # Перевірка чи передано шлях до папки
    if len(sys.argv) == 2:
        path = sys.argv[1]
        # Перевірка чи існує папка з вказаним шляхом
        if os.path.isdir(path):
            sort_folder(path)
        else:
            print(f"Папки '{path}' не існує")
    else:
        print("Вкажіть шлях до папки, яку треба відсортувати")

















































# import os
# import shutil

# def normalize(name):
#     translit_dict = {
#         'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh',
#         'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
#         'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
#         'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'iu', 'я': 'ia'
#     }
#     translit_alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
#     name = name.lower()
#     name = ''.join([translit_dict.get(i, i) for i in name])
#     name = ''.join([i if i in translit_alphabet else '_' for i in name])
#     return name




# def main(path_to_folder):

#     extensions = {"images": ["jpeg", "png", "jpg", "svg"],
#         "video": ["avi", "mp4", "mov", "mkv"],
#         "documents": ["doc",  "docx", "txt", "docx", "pdf", "xlsx", "pptx"],
#         "audio": ["mp3", "ogg", "raw", "wav", "wma"],
#         "archives": ["zip", "gz", "tar"],
#         "other": ["*"]}
                 
#     with open(file='sorted.log', mode= 'w', encoding='utf-8') as file:

#         def create_folders_from_list(path_to_folder, folder_names):

#             for folder in folder:

#                 if not os.exists(f'{path_to_folder}\\{folder} \n'):
#                     log = f'[+] {folder} {path_to_folder}'
#                     file.write(log)
#                     os.mkdir(f'{path_to_folder}\\{folder}')

# def get_subfolder_paths(path_to_folder) -> list:
#     subfolder_paths = [folder.path for folder in os.scandir(path_to_folder) if folder.is_dir()]
#     return 









# if __name__ == '__name__':
#     path_to_folder = 'folder' # Шлях до папки для сортування
#     main(path_to_folder)