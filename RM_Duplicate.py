from PIL import Image
import imagehash
import os

path = os.path.join('PokePic')
os.chdir(path)


def image_hash(file_path):
    return imagehash.phash(Image.open(file_path))


def rm(duplicated, file_list):
    for idx in duplicated:
      
        os.remove(file_list[idx])


def process_img(source_path):
    with Image.open(source_path) as img:
        print(f"Now processing {img}")
        if img.mode != 'RGB':
            img = img.convert("RGB")
        img.save(source_path, "PNG", optimize=True, quality=100)


def main():
    duplicated = []
    hash_key = {}
    for idx, filename in enumerate(file_list := os.listdir('.')):
        process_img(os.path.join(filename))
    for idx, filename in enumerate(file_list := os.listdir('.')):
        if os.path.isfile(filename):
            img_path = os.path.join(filename)
            file_hash = image_hash(img_path)
            if file_hash not in hash_key:
                hash_key[file_hash] = idx
            else:
                duplicated.append(idx)
    rm(duplicated, file_list)


if __name__ == '__main__':
    main()
