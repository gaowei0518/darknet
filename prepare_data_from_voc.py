import os
import shutil
def prepare_data_from_voc(list_class , model_name , data_root = "" , output_folder="") :
    
    new_data_folder = output_folder+"/"+model_name
    if not(os.path.isdir(new_data_folder)) :
        os.makedirs(new_data_folder)
        
    for image in os.listdir(data_root + "/JPEGImages") :
        if os.path.isfile(image) and image.find(".jpg") >= 0 :
            shutil.copyfile(data_root + "/JPEGImages/" + image ,new_data_folder+"/" + image)
            
    for anno in os.listdir(data_root + "/Annotations") :
        if os.path.isfile(anno) and image.find(".xml") >= 0 :
            shutil.copyfile(data_root + "/Annotations/" + anno ,new_data_folder+"/" + anno)
            
    from convert_xml import convert_all_to_xml_in_folder
    
    convert_all_to_xml_in_folder(folder_path = new_data_folder)
    prepare_obj_names(output_folder , list_class , model_name)
    prepare_obj_data(output_folder , list_class , model_name)
    
    from prepare_config import prepare_config_file
    prepare_config_file(model_name , output_file_path = "" ,batch_size = 16 , subdivision= 0 , nb_class = 1 , max_iter = 0 , nb_image = 0 , mosaic = 1 ,verbose = False)
    
def prepare_obj_names(output_folder , list_class , model_name) : 
    
    txt = open(output_folder + "/" + model_name +".names" , "w")
    for cls in list_class :
        txt.write(str(cls)+"\n")
        
    txt.close()
    
def prepare_obj_data(output_folder , list_class , model_name) : 
    
    txt = open(output_folder + "/" + model_name +".data" , "w")
    nb_class = len(list_class)
    txt.write("classes= {}\n".format(nb_class))
    txt.write("train  = {}/{}/train.txt\n".format(output_folder,model_name))
    txt.write("valid  = {}/{}/train.txt\n".format(output_folder,model_name))
    txt.write("names = {}/{}.names\n".format(output_folder,model_name))

    backup = output_folder + "/" + model_name + "_backup"
    if not(os.path.isdir(backup)) :
        os.makedirs(backup) 
    txt.write("backup = {}\n".format(backup))
    txt.close()
    
if __name__ == "__main__":
    model_name = sys.argv[1]
    data_root = sys.argv[2]
    list_class = sys.argv[3]
    prepare_data_from_voc(list_class , model_name , data_root = data_root , output_folder="data")
