from PIL import Image

from sdkit.filter import apply_filters
from sdkit.models import unload_model

from src.init_context import init_context

def gfpgan_operation(args, models):    
    modelType = "gfpgan"
    context = init_context(args, models, modelType)
    image = Image.open(args.input)

    print(f"\nFixing faces in image {args.input}\n")

    fixed = apply_filters(context, modelType, image)
    
    if args.nsfw:
        fixed = apply_filters(context, "nsfw_checker", fixed[0])

    fixed[0].save(args.output)

    unload_model(context, modelType)