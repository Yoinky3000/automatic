# Stable Diffusion - Automatic

*Heavily opinionated custom fork of* <https://github.com/AUTOMATIC1111/stable-diffusion-webui>  

![screenshot](ui-screenshot.jpg)

<br>

## Notes

Fork is as close as up-to-date with origin as time allows  
All code changes are merged upstream whenever possible  

Fork adds extra functionality:

- New skin and UI layout  
- Ships with set of **CLI** tools that rely on *SD API* for execution:  
  e.g. `generate`, `train`, `bench`, etc.  
  [Full list](<cli/>)

### Integrated Extensions

- [System Info](https://github.com/vladmandic/sd-extension-system-info)
- [ControlNet](https://github.com/Mikubill/sd-webui-controlnet)
- [Image Browser](https://github.com/AlUlkesh/stable-diffusion-webui-images-browser)
- [LORA](https://github.com/kohya-ss/sd-scripts) (both training and inference)
- [LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS) (both training and inference)
- [Model Converter](https://github.com/Akegarasu/sd-webui-model-converter)
- [CLiP Interrogator](https://github.com/pharmapsychotic/clip-interrogator-ext)
- [Dynamic Thresholding](https://github.com/mcmonkeyprojects/sd-dynamic-thresholding)
- [Steps Animation](https://github.com/vladmandic/sd-extension-steps-animation)
- [Seed Travel](https://github.com/yownas/seed_travel)

*Note*: Extensions are automatically updated to latest version on `install`

### Start Script

Simplified start script: `automatic.sh`  
*Existing `webui.sh`/`webui.bat` scripts still exist for backward compatibility*  

> ./automatic.sh  

Start in default mode with optimizations enabled  

    SD server: optimized
    Version: 56f779a9 Sat Feb 25 14:04:19 2023 -0500
    Repository: https://github.com/vladmandic/automatic
    Last Merge: Sun Feb 19 10:11:25 2023 -0500 Merge pull request #37 from AUTOMATIC1111/master
    System
    - Platform: Ubuntu 22.04.1 LTS 5.15.90.1-microsoft-standard-WSL2 x86_64
    - nVIDIA: NVIDIA GeForce RTX 3060, 528.49
    - Python: 3.10.6 Torch: 2.0.0.dev20230224+cu118 CUDA: 11.8 cuDNN: 8700 GPU: NVIDIA GeForce RTX 3060 Arch: (8, 6)
    Launching Web UI

> ./automatic.sh clean  

Start with all optimizations disabled  
Use this for troubleshooting  

> ./automatic.sh install

Installs and updates to latest supported version:

- Dependencies
- Fixed sub-repositories
- Extensions
- Sub-modules

Does not update main repository

> ./automatic.sh update

Updates the main repository to the latest version  
Recommended to run `install` after `update` to update dependencies as they may have changed  

> ./automatic.sh help

Print all available options

> ./automatic.sh public  

Start with listen on public IP with authentication enabled  

<br>  

## Install

1. Install `Python`, `Git`  
2. Install `PyTorch` and `Xformers`  
   See [Wiki](wiki/Torch%20Optimizations.md) for details
   If you don't want to use `xformers`, edit `automatic.sh` as they are enabled by default
3. Clone and initialize repository  

> git clone https://github.com/vladmandic/automatic  
> cd automatic  
> ./automatic.sh install  

      SD server: install
      Version: 56f779a9 Sat Feb 25 14:04:19 2023 -0500
      Repository: https://github.com/vladmandic/automatic
      Last Merge: Sun Feb 19 10:11:25 2023 -0500 Merge pull request #37 from AUTOMATIC1111/master
      Installing general requirements
      Installing versioned requirements
      Installing requirements for Web UI
      Updating submodules
      Updating extensions
      Updating wiki
      Detached repos
      Local changes

<br>

## Differences

Fork does differ in few things:

- Drops compatibility with `python` **3.7** and requires **3.9**  
  Recommended is **Python 3.10**  
  Note that **Python 3.11** or **3.12** are NOT supported  
- New global exception handler
- Drops localizations  
- Updated **Python** libraries to latest known compatible versions  
  e.g. `accelerate`, `transformers`, `numpy`, etc.  
- Includes opinionated **System** and **Options** configuration  
  e.g. `samplers`, `upscalers`, etc.  
- Does not rely on `Accelerate` as it only affects distributed systems  
- Optimized startup order  
  Gradio web server will be initialized much earlier which model load is done in the background  
- Includes **SD2** configuration files  
- Uses simplified folder structure  
  e.g. `/train`, `/outputs/*`  
- Modified training templates  
- Built-in `LoRA`, `LyCORIS`, `Custom Diffusion`, `Dreambooth` training  

User Interface:

- Includes reskinned **UI**  
  Black and orange dark theme with fixed width options panels and larger previews  

Optimizations:

- Runs with `SDP` memory attention enabled by default if supported by system  
- Fallback to `XFormers` if SDP is not supported  
- If either `SDP` or `XFormers` are not supported, falls back to usual cmd line arguments  

Only Python library which is not auto-updated is `PyTorch` itself as that is very system specific  

Fork is compatible with regular **PyTorch 1.13**, **PyTorch 2.0** as well as pre-releases of **PyTorch** **2.1**  
See [Wiki](https://github.com/vladmandic/automatic/wiki/Torch-Optimizations) for **Torch** optimization notes

<br>

## Scripts

This repository comes with a large collection of scripts that can be used to process inputs, train, generate, and benchmark models  

As well as number of auxiliary scripts that do not rely on **WebUI**, but can be used for end-to-end solutions such as extract frames from videos, etc.  

For full details see [Docs](cli/README.md)

<br>

## Docs

- Scripts are in [Scripts](cli/README.md)  
- Everything else is in [Wiki](https://github.com/vladmandic/automatic/wiki)  
- Except my current [TODO](TODO.md)  
