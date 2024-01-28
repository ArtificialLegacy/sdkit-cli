from sdkit.models import download_model, load_model, resolve_downloaded_model_path

def download(context, model, modelType):
    print(f"\nDownloading model {model}\n")
    
    download_model(model_type=modelType, model_id=model)
    model_path = resolve_downloaded_model_path(model_type=modelType, model_id=model)

    print(f"\nLoading model {model}n")

    context.model_paths[modelType] = model_path
    load_model(context, modelType)