import random

from sdkit.generate import generate_images
from sdkit.models import unload_model

from src.init_context import init_context

def sdt_operation(args, models):
    if not args.arg1:
        raise Exception("Prompt not specified.")

    if not args.args2:
        raise Exception("Width not specified.")
    
    if not args.args3:
        raise Exception("Height not specified.")

    modelType = "stable-diffusion"
    context = init_context(args, models, modelType)

    print(f"\nGenerating image with prompt {args.arg1}\n")

    guidance = float(args.arg4) if args.arg4 else 7.5
    seed = random.randint(0, 100000) if not args.arg5 else int(args.arg5)

    images = generate_images(context, prompt=args.arg1, width=int(args.arg2), height=int(args.arg3), guidance_scale=guidance, seed=seed)

    images[0].save(args.output)

    unload_model(context, modelType)