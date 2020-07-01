import os

def prepare_config_file(model_name , output_file_path = "" ,batch_size = 16 , subdivision= 0 , nb_class = 1 , max_iter = 0 , nb_image = 0 , mosaic = 1 ,verbose = False) :
    config_sample = os.path.join(os.environ["YOLO_DARKNET"],"cfg","yolov4_sample.cfg")
    
    ### definir les valeur du parmetre : 
    if output_file_path == "" :
        output_file_path = os.path.join(os.environ["YOLO_DARKNET"],"cfg",model_name + ".cfg")
    if max_iter == 0 :
        max_iter = max(nb_image,2000 * nb_class)
    90max_iter = int(0.9*max_iter)
    80max_iter = int(0.8*max_iter)
    if subdivision == 0 :
        subdivision = max(1,int(batch_size//4))
        
    mosaic = bool(mosaic)
    ### regle defini par la reseau , ne le change pas
    nb_filter = (5 + nb_class) *3
    
    txt_origin = open(config_sample,"r")
    text_origin = txt_origin.read()
    txt_origin.close()
    new_text = text_origin.replace("$BATCH_SIZE$",str(batch_size))
    new_text = new_text.replace("$SUBDIVISIONS$",str(subdivision))
    new_text = new_text.replace("$ACTIVE_MOSAIC$",str(mosaic))
    new_text = new_text.replace("$MAX_ITERS$",str(max_iter))
    new_text = new_text.replace("$0.8_ITERS$",str(80max_iter))
    new_text = new_text.replace("$0.9_ITERS$",str(90max_iter))
    new_text = new_text.replace("$NB_CLASS$",str(nb_class))
    new_text = new_text.replace("$NB_filter$",str(nb_filter))
    
    
    new_cfg = open(output_file_path,"w")
    new_cfg.write(new_text)
    new_cfg.close()
    
    
    
    
    
    
