import argparse

from src.esrgan import *
from src.gfpgan import *
from src.sdt import *
from src.sdi import *

parser = argparse.ArgumentParser(prog="SDKIT-CLI", description="SDKIT-CLI is a command line interface for SDKIT", epilog="SDKIT-CLI")

OPERATIONS = [
    "none",
    "esrgan",
    "gfpgan",
    "sdt", # Runs SD models with text2image.
    "sdi" # Runs SD models with image2image.
]

MODELS = {}

MODELS["esrgan"] = [
    "x4plus",
    "x4plus_anime_6",
]

MODELS["gfpgan"] = [
    "1.2",
    "1.3",
    "1.4",
]

MODELS["sd"] = [
    "sd-xl-base-1.0",
    "sd-xl-refiner-1.0",
    "2.1-512-ema-pruned",
    "2.1-512-ema-pruned-safetensors",
    "2.1-512-nonema-pruned",
    "2.1-512-nonema-pruned-safetensors",
    "2.1-768-ema-pruned",
    "2.1-768-ema-pruned-safetensors",
    "2.1-768-nonema-pruned",
    "2.1-768-nonema-pruned-safetensors",
    "2.0-512-base-ema",
    "2.0-512-base-ema-safetensors",
    "2.0-768-v-ema",
    "2.0-768-v-ema-safetensors",
    "2.0-512-depth-ema",
    "2.0-512-depth-ema-safetensors",
    "2.0-512-inpainting-ema",
    "2.0-512-inpainting-ema-safetensors",
    "2.0-x4-upscaler-ema",
    "2.0-x4-upscaler-ema-safetensors",
    "1.5-pruned-emaonly-fp16",
    "1.5-pruned-emaonly",
    "1.5-pruned",
    "1.5-inpainting",
    "1.4",
    "1.4-full-ema",
]

parser.add_argument("operation", help="Operation to perform", choices=OPERATIONS, nargs="?", default="none")
parser.add_argument("model", help="Model to use for the specific operation.", nargs="?", default="")
parser.add_argument("arg1", help="Argument 1", nargs="?", default="")
parser.add_argument("arg2", help="Argument 2", nargs="?", default="")
parser.add_argument("arg3", help="Argument 3", nargs="?", default="")
parser.add_argument("arg4", help="Argument 4", nargs="?", default="")
parser.add_argument("arg5", help="Argument 5", nargs="?", default="")
parser.add_argument("arg6", help="Argument 6", nargs="?", default="")
parser.add_argument("arg7", help="Argument 7", nargs="?", default="")
parser.add_argument("arg8", help="Argument 8", nargs="?", default="")
parser.add_argument("arg9", help="Argument 9", nargs="?", default="")
parser.add_argument("arg10", help="Argument 10", nargs="?", default="")

parser.add_argument("-i", "--input")
parser.add_argument("-o", "--output")
parser.add_argument("-ml", "--model-list", action="store_true")
parser.add_argument("-vr", "--vram-usage")
parser.add_argument("-c", "--cpu", action="store_true")
parser.add_argument("-nsfw", "--nsfw", action="store_true")

args = parser.parse_args()

if not args.input and args.operation != "sdt":
    raise Exception("Input not specified.")

if not args.output:
    raise Exception("Output not specified.")

if args.model_list:
    print("Available models:")
    for modelType in MODELS:
        print(f" * {modelType}")
        for model in MODELS[modelType]:
            print(f"    - {model}")
    exit()

match args.operation:
    case "esrgan":
        esrgan_operation(args, MODELS["esrgan"])
    case "gfpgan":
        gfpgan_operation(args, MODELS["gfpgan"])
    case "sdt":
        sdt_operation(args, MODELS["sd"])
    case "sdi":
        sdi_operation(args, MODELS["sd"])
    case _:
        raise Exception(f"Operation {args.operation} not found in operations list.")