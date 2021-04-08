def faceTrain():
    import cv2
    import numpy as np
    from os import listdir
    from os.path import isfile, join

    data_path = "F:/projects/FaceDetection/data/"+dept+"/"+student+"/"
    onlyfiles = [f for f in listdir( data_path ) if isfile(join ( data_path, f ))]

    training_data, labels = [], []

    for i, files in enumerate(onlyfiles):
        image_path = data_path + onlyfiles[i]
        images = cv2.imread(image_path,0)
        training_data.append(np.asarray(images, dtype = np.uint8))
        labels.append(i)    
        
    labels = np.asarray(labels,dtype = np.int32)

    model = cv2.face.LBPHFaceRecognizer_create()

    model.train (np.asarray(training_data), np.asarray(labels))
    print ('model training completed')
    

    return model

faceTrain()
