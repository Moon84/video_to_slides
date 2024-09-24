import imagehash      ##计算图像的哈希值
from PIL import Image
import os

def find_similar_images(base_dir, hash_size=8):
    """
    这个函数用于查找指定目录下的重复图片文件。它使用了图像哈希算法来比较图片的相似性。

    参数:
    base_dir (str): 要搜索的目录路径。
    hash_size (int): 哈希值的大小，默认为8。较小的值会更快，但可能会导致误报；较大的值会更慢，但更准确。

    返回:
    tuple: 一个包含两个元素的元组。第一个元素是一个字典，其中键是图片的哈希值，值是文件名。
           第二个元素是一个列表，包含所有重复的文件名。

    """

    # 对目录下的文件进行排序
    snapshots_files = sorted(os.listdir(base_dir))

    # 初始化用于存储哈希值和文件名的字典，以及用于存储重复文件名的列表
    hash_dict = {}  
    duplicates = []  
    num_duplicates = 0  

    print('---'*5,"Finding similar files",'---'*5)

    # 遍历所有文件
    for file in snapshots_files:
        # 检查文件是否为图片文件
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # 打开图片文件
            read_file = Image.open(os.path.join(base_dir, file))
            
            # 计算图片的哈希值
            comp_hash = str(imagehash.phash(read_file, hash_size=hash_size)) 
            # 调用phash 感知哈希算法，更注重图像的视觉相似度，而不仅仅是像素级别的差异，dhash 差值哈希， Hhash 均值哈希，

            # 如果哈希值不存在于字典中，则将其添加到字典中
            if comp_hash not in hash_dict:   
                hash_dict[comp_hash] = file
            # 如果哈希值已经存在，则说明找到了重复的图片
            else:
                print('Duplicate file: ', file)
                duplicates.append(file)
                num_duplicates+=1
        
    print('\nTotal duplicate files:', num_duplicates)
    print("-----"*10)
    # 返回哈希值字典和重复文件名列表
    return hash_dict, duplicates


def remove_duplicates(base_dir):   # 删除重复图片

    _, duplicates = find_similar_images(base_dir, hash_size=12)

    if not len(duplicates):
        print('No duplicates found!')

    else:
        print("Removing duplicates...")

        for dup_file in duplicates:
            file_path = os.path.join(base_dir, dup_file)

            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                print('Filepath: ', file_path, 'does not exists.')
        

        print('All duplicates removed!, total pic is %s' % len(os.listdir(base_dir)))
    
    print('***'*10,'\n')

if __name__ == "__main__":
    remove_duplicates('sample_1')