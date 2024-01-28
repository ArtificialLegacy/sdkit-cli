from PIL import Image

from sdkit.filter import apply_filters
from sdkit.models import unload_model

from src.init_context import init_context

def esrgan_operation(args, models):
    modelType = "realesrgan"
    context = init_context(args, models, modelType)
    image = Image.open(args.input)

    scale = 4
    if args.arg1:
        scale = float(args.arg1)

    print(f"\nUpscaling image {args.input}\n")

    upscaled = apply_filters(context, modelType, image, scale=scale)

    if args.nsfw:
        fixed = apply_filters(context, "nsfw_checker", fixed[0])

    upscaled[0].save(args.output)

    unload_model(context, modelType)