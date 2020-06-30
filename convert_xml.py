import xml.etree.ElementTree as ET
#import pickle
import os
from os import listdir, getcwd
from os.path import join

# sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

#classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
classes = ["p2p_windows"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(xml_path):
    in_file = open(xml_path)
    out_file = open(xml_path.replace(".xml",".txt"), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    print(w,h)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        print(b)
        bb = convert((w,h), b)
        if bb[0] <=0 or bb[0] > 1 or bb[1] <=0 or bb[1] > 1 :
            print("incorrect bbox")
            continue
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

        
def convert_all_to_xml_in_folder(folder_path = "") : 

    train_txt = open(folder_path+"/train.txt","w")
    for image_xml in os.listdir(folder_path):
        if os.path.isfile(image_xml) :
            if image_xml.find(".xml") >= 0 :
                convert_annotation(image_xml)
                train_txt.write("{}/{}\n".format(folder_path,image_xml.replace(".xml",".jpg")))
    train_txt.close()
    
if __name__ == "__main__":
    wd = getcwd()
    convert_all_to_xml_in_folder(folder_path = wd)
