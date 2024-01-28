
# SDKit-CLI

* A CLI wrapper for [sdkit](https://github.com/easydiffusion/sdkit).
* This is primarly for calling sdkit from other programs / languages
    but can be used standalone.

## Documentation

`./sdkit-cli.exe <operation> <model> [..args] [...flags]`

### Operations

* esrgan - Upscale images.
* gfpgan - Face restoration.
* sdt - Stable Diffusion with only text input.
* sdi - Stable Diffusion with image input.

### Models

#### ESRGAN

* x4plus
* x4plus_anime_6

#### GFPGAN

* 1.2
* 1.3
* 1.4

#### Stable Diffusion

* sd-xl-base-1.0
* sd-xl-refiner-1.0
* 2.1-512-ema-pruned
* 2.1-512-ema-pruned-safetensors
* 2.1-512-nonema-pruned
* 2.1-512-nonema-pruned-safetensors
* 2.1-768-ema-pruned
* 2.1-768-ema-pruned-safetensors
* 2.1-768-nonema-pruned
* 2.1-768-nonema-pruned-safetensors
* 2.0-512-base-ema
* 2.0-512-base-ema-safetensors
* 2.0-768-v-ema
* 2.0-768-v-ema-safetensors
* 2.0-512-depth-ema
* 2.0-512-depth-ema-safetensors
* 2.0-512-inpainting-ema
* 2.0-512-inpainting-ema-safetensors
* 2.0-x4-upscaler-ema
* 2.0-x4-upscaler-ema-safetensors
* 1.5-pruned-emaonly-fp16
* 1.5-pruned-emaonly
* 1.5-pruned
* 1.5-inpainting
* 1.4
* 1.4-full-ema

### esrgan

* ? arg1 - scale (must be >0, defaults to 4)

### gfpgan

> Takes in no args.

### sdt

> Ignores the `-i` flag.

* ! arg1 - prompt
* ! arg2 - width (power of 2)
* ! arg3 - height (power of 2)
* ? arg4 - guidance scale (defaults to 7.5)
* ? arg5 - seed (defaults to random)

### sdi

* ! arg1 - prompt
* ! arg2 - width (power of 2)
* ! arg3 - height (power of 2)
* ? arg4 - guidance scale (defaults to 7.5)
* ? arg5 - seed (defaults to random)

### Flags

* `-i` - The input image to use.
* `-o` - The name of the image to output.
* `-ml` - Prints a list of all available models, will not run any operations.
* `-vr` - Control the level of vram usage, defaults to medium usage, accepts [low, high]
* `-c` - Use the cpu instead of gpu for generation. (Very slow)
* `-nsfw` - Activates the nsfw filter after running an operation.
