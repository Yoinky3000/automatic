def postprocessing_scripts():
    import modules.scripts
    return modules.scripts.scripts_postproc.scripts


def sd_vae_items():
    import modules.sd_vae
    return ["Automatic", "None"] + list(modules.sd_vae.vae_dict)


def refresh_vae_list():
    import modules.sd_vae
    modules.sd_vae.refresh_vae_list()


def list_crossattention(diffusers=False):
    if diffusers:
        return [
            "Disabled",
            "xFormers",
            "Scaled-Dot-Product",
            "Torch BMM",
            "Split attention",
            "Dynamic Attention BMM",
            "Dynamic Attention SDP"
        ]
    else:
        return [
            "Disabled",
            "xFormers",
            "Scaled-Dot-Product",
            "Doggettx's",
            "InvokeAI's",
            "Sub-quadratic",
            "Split attention"
        ]

def get_pipelines():
    import diffusers
    from installer import log

    pipelines = { # note: not all pipelines can be used manually as they require prior pipeline next to decoder pipeline
        'Autodetect': None,
        'Stable Diffusion': getattr(diffusers, 'StableDiffusionPipeline', None),
        'Stable Diffusion Inpaint': getattr(diffusers, 'StableDiffusionInpaintPipeline', None),
        'Stable Diffusion Img2Img': getattr(diffusers, 'StableDiffusionImg2ImgPipeline', None),
        'Stable Diffusion Instruct': getattr(diffusers, 'StableDiffusionInstructPix2PixPipeline', None),
        'Stable Diffusion Upscale': getattr(diffusers, 'StableDiffusionUpscalePipeline', None),
        'Stable Diffusion XL': getattr(diffusers, 'StableDiffusionXLPipeline', None),
        'Stable Diffusion XL Img2Img': getattr(diffusers, 'StableDiffusionXLImg2ImgPipeline', None),
        'Stable Diffusion XL Inpaint': getattr(diffusers, 'StableDiffusionXLInpaintPipeline', None),
        'Stable Diffusion XL Instruct': getattr(diffusers, 'StableDiffusionXLInstructPix2PixPipeline', None),
        'Latent Consistency Model': getattr(diffusers, 'LatentConsistencyModelPipeline', None),
        'PixArt Alpha': getattr(diffusers, 'PixArtAlphaPipeline', None),
        'UniDiffuser': getattr(diffusers, 'UniDiffuserPipeline', None),
        'Wuerstchen': getattr(diffusers, 'WuerstchenCombinedPipeline', None),
        'Kandinsky 2.1': getattr(diffusers, 'KandinskyPipeline', None),
        'Kandinsky 2.2': getattr(diffusers, 'KandinskyV22Pipeline', None),
        'Kandinsky 3': getattr(diffusers, 'Kandinsky3Pipeline', None),
        'DeepFloyd IF': getattr(diffusers, 'IFPipeline', None),
        'ONNX Stable Diffusion': getattr(diffusers, 'OnnxStableDiffusionPipeline', None),
        'ONNX Stable Diffusion Img2Img': getattr(diffusers, 'OnnxStableDiffusionImg2ImgPipeline', None),
        'ONNX Stable Diffusion Inpaint': getattr(diffusers, 'OnnxStableDiffusionInpaintPipeline', None),
        'ONNX Stable Diffusion Upscale': getattr(diffusers, 'OnnxStableDiffusionUpscalePipeline', None),
        'ONNX Stable Diffusion XL': getattr(diffusers, 'OnnxStableDiffusionXLPipeline', None),
        'ONNX Stable Diffusion XL Img2Img': getattr(diffusers, 'OnnxStableDiffusionXLImg2ImgPipeline', None),
        'Custom Diffusers Pipeline': getattr(diffusers, 'DiffusionPipeline', None),
        'InstaFlow': getattr(diffusers, 'StableDiffusionPipeline', None), # dynamically redefined and loaded in sd_models.load_diffuser
        'SegMoE': getattr(diffusers, 'StableDiffusionPipeline', None), # dynamically redefined and loaded in sd_models.load_diffuser
        # Segmind SSD-1B, Segmind Tiny
    }

    for k, v in pipelines.items():
        if k != 'Autodetect' and v is None:
            log.error(f'Not available: pipeline={k} diffusers={diffusers.__version__} path={diffusers.__file__}')
    return pipelines
