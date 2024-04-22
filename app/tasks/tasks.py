from app.tasks.celery import celery
from PIL import Image
from pathlib import Path


@celery.task
def process_pic(
        path: str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    for width, height in [
        (1000, 500),
        (200, 100)
    ]:
        resized_img = im.resize(size=(width, height))
        resized_img.save(f"app/static/images/resized_{width}_{height}_{im_path.name}")
