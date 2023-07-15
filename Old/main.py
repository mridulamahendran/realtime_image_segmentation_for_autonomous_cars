import torch


def func(image_path):
    # Model
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

    # Images
    img = image_path

    # Inference
    results = model(img)

    # Results
    #x = results.print()
    print(type(results))
    #results.show() 
    results.save()
    print(results)
    return str(results)