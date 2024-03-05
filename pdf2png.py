from pdf2image import convert_from_path
from pathlib import Path
import shutil
from datetime import datetime

# 获取当前日期和时间
current_datetime = datetime.now()

# 提取年、月、日、小时、分钟和秒

y= str(current_datetime.year).zfill(4)
m= str(current_datetime.month).zfill(2)
d= str(current_datetime.day).zfill(2)
h= str(current_datetime.hour).zfill(2)
mi= str(current_datetime.minute).zfill(2)

current_date_time = y+m+d+h+mi




# 打印当前日期和时间的各个部分
current_directory = Path.cwd()   

convert_folder = f"{str(current_directory)}\Convert_pdf"
convert_folder_path = Path(convert_folder)

destination_folder = f'{str(current_directory)}\completed'
destination_folder_path = Path(destination_folder)

output_png_folder = f"{str(current_directory)}\output_png"
output_png_folder_path = Path(output_png_folder)


def pdf_to_png(pdf_file, output_folder_str):
    try:
        # Convert PDF to list of PIL images
        images = convert_from_path(pdf_file,dpi=900 )
        file_name =pdf_file.name
        
        
        # Save each image as PNG
        
        for i, image in enumerate(images):
            
            image_path = f"{output_folder_str}\{pdf_file.stem}_{i + 1}.png"
            image.save(image_path, "png")
            # 定义源文件和目标文件夹路径
            source_file = f'{convert_folder}\{pdf_file.name}'
            destination_folder = f'{current_directory}\completed'

            if not Path(f'{destination_folder}\{pdf_file.name}').exists():
                # 将文件从源文件夹移动到目标文件夹
                shutil.move(source_file, destination_folder)
               

            else:
                pass
           
        print(f"{file_name} Convertted successfully!")        
        
    except Exception as e:
        print(f"Error: {e}")
    


    
    

def create_folder_if_not_exists(convert_folder_path):
    
    # 使用 Path 对象创建文件夹路径
    for pdf_file in convert_folder_path.glob("*.pdf"):
        
        output_folder_path = Path(f"{str(current_directory)}\output_png\{pdf_file.stem}_({current_date_time})")
        
        # 检查文件夹是否存在
        if not output_folder_path.exists():
            # 如果文件夹不存在，則創建資料夾
            output_folder_path.mkdir()
            # print(f"Folder '{output_folder_path}' created successfully！")
            pdf_to_png(pdf_file, output_folder_path)
        else:
            # 如果文件夹已存在，则提示并不执行任何操作
            # print(f"Folder '{output_folder_path}' exit already！No action required.")
            pdf_to_png(pdf_file, output_folder_path)
        
        

# 调用函数来创建文件夹（如果不存在的话）

if not destination_folder_path.exists():
            
    destination_folder_path.mkdir()
    
        



if not output_png_folder_path.exists():

    output_png_folder_path.mkdir()



print("Start converting PDF files to PNG...")

create_folder_if_not_exists(convert_folder_path)

print('   ')
print("All PDF files have been converted to PNG successfully!")
input('Press Enter to exit')




