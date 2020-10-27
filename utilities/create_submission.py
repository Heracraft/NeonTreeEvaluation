import glob
import os
import cv2
import pandas as pd
from deepforest import deepforest

def submission_no_chm(tiles_to_predict):
    #Predict
    results = []
    model = deepforest.deepforest()
    model.use_release()    
    for path in tiles_to_predict:   
        try:
            result = model.predict_image(path,return_plot=False)    
            result["plot_name"] = os.path.splitext(os.path.basename(path))[0]
            results.append(result)
        except Exception as e:
            print(e)
            continue    
        
    #Create plot name groups
    boxes = pd.concat(results)
    
    return boxes

tiles_to_predict = glob.glob("/home/b.weinstein/NeonTreeEvaluation/evaluation/RGB/*.tif") 
df = submission_no_chm(tiles_to_predict)
df.to_csv("all_images_submission.csv")
