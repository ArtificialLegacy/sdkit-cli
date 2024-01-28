import sdkit

from src.download import download

def init_context(args, models, modelType):
    if args.model not in models:
        raise Exception(f"Model {args.model} not found in models list.")
    
    context = sdkit.Context()

    if args.cpu:
        context.device = "cpu"

    if args.vram_usage == "low" or args.vram_usage == "high":
        context.vram_usage = args.vram_usage

    download(context, args.model, modelType)

    return context