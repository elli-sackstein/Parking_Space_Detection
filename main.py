import cv2
import supervision as sv
from tqdm import tqdm
import gradio as gr
import torch
from inference.models.yolo_world.yolo_world import YOLOWorld

SOURCE_IMAGE_PATH = "C:/Users/Elli/PycharmProjects/Parking Space Detection/photos"
model = YOLOWorld(model_id="yolo_world/l")
classes = ["car","tree","bag","person", "backpack"]
model.set_classes(classes)
image = cv2.imread(SOURCE_IMAGE_PATH)
results = model.infer(image)
detections = sv.Detections.from_inference(results)
BOUNDING_BOX_ANNOTATOR = sv.BoundingBoxAnnotator(thickness=2)
LABEL_ANNOTATOR = sv.LabelAnnotator(text_thickness=2, text_scale=1,text_color=sv.Color.BLACK)
annotated_image = image.copy()
annotated_image = BOUNDING_BOX_ANNOTATOR.annotate(annotated_image, detections)
annotated_image = LABEL_ANNOTATOR.annotate(annotated_image, detections)
sv.plot_image(annotated_image, (10, 10))