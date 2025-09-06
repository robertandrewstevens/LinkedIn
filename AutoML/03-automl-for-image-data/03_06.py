# TODO: pip install azure-cognitiveservices-vision-customvision
import os
import time

from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch
from msrest.authentication import ApiKeyCredentials

# STORE OUR CREDENTIALS 
ENDPOINT = "XXXXX"
TRAINING_KEY = "XXXX"
PREDICTION_KEY = "XXXX"
PREDICTION_ID= "XXXX"
ITERATION_NAME = 'afrifashion-classifier-1'

credentials = ApiKeyCredentials(in_headers={"Training-key": TRAINING_KEY})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# CREATE OUR PROJECT AND IMAGE TAGS
project_name = "afrifashion"
project = trainer.create_project(project_name)

agbada_tag = trainer.create_tag(project.id, "agbada")
blouse_tag = trainer.create_tag(project.id, "blouse")
gele_tag = trainer.create_tag(project.id, "gele")
shirts_tag = trainer.create_tag(project.id, "shirts")
wrapper_blouse_tag = trainer.create_tag(project.id, "wrapper_blouse")
gown_tag = trainer.create_tag(project.id, "gown")
buba_trouser_tag = trainer.create_tag(project.id, "buba_trouser")
skirt_blouse_tag = trainer.create_tag(project.id, "skirt_blouse")

# UPLOAD AND TAG OUR IMAGES
dataset_folder = "data/afrifashion1600/train"
fashion_styles = [
    "agbada", "blouse", "buba_and_trouser", 
    "gele", "gown", "shirts", "skirt_and_blouse", 
    "wrapper_and_blouse"
]
tags = [
    agbada_tag, blouse_tag, buba_trouser_tag, 
    gele_tag, gown_tag, shirts_tag, skirt_blouse_tag,
    wrapper_blouse_tag
]

image_list = []

for i, style, tag in enumerate(zip(fashion_styles, tags)):
    style_folder = os.path.join(dataset_folder, style)
    for img in os.listdir(style_folder):
        with open(os.path.join (style_folder, img), "rb") as image_contents:
            image_list.append(
                ImageFileCreateEntry(name=img, contents=image_contents.read(), tag_ids=[tag.id])
            )

        if (i+1) % 64 == 0:
            upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))
            if not upload_result.is_batch_successful:
                print("Image batch upload failed.")
                for image in upload_result.images:
                    print("Image status: ", image.status)
                exit(-1)
            image_list = []

# TRAIN AND PUBLISH A MODEL
iteration = trainer.train_project(project.id, training_type='Regular', notification_email_address='hello@hi.com')
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    print ("Waiting 10 seconds...")
    time.sleep(10)

trainer.publish_iteration(project.id, iteration.id, ITERATION_NAME, PREDICTION_ID)
