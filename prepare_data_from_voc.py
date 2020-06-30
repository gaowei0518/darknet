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
    
