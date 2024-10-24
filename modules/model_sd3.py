import os
import diffusers
import transformers


default_repo_id = 'stabilityai/stable-diffusion-3-medium'


def load_sd3(checkpoint_info, cache_dir=None, config=None):
    from modules import shared, devices, modelloader, sd_models
    repo_id = sd_models.path_to_repo(checkpoint_info.name)
    dtype = devices.dtype
    kwargs = {}
    if checkpoint_info.path is not None and checkpoint_info.path.endswith('.safetensors') and os.path.exists(checkpoint_info.path):
        loader = diffusers.StableDiffusion3Pipeline.from_single_file
        fn_size = os.path.getsize(checkpoint_info.path)
        if fn_size < 5e9:
            kwargs = {
                'text_encoder': transformers.CLIPTextModelWithProjection.from_pretrained(
                    default_repo_id,
                    subfolder='text_encoder',
                    cache_dir=cache_dir,
                    torch_dtype=dtype,
                ),
                'text_encoder_2': transformers.CLIPTextModelWithProjection.from_pretrained(
                    default_repo_id,
                    subfolder='text_encoder_2',
                    cache_dir=cache_dir,
                    torch_dtype=dtype,
                ),
                'tokenizer': transformers.CLIPTokenizer.from_pretrained(
                    default_repo_id,
                    subfolder='tokenizer',
                    cache_dir=cache_dir,
                ),
                'tokenizer_2': transformers.CLIPTokenizer.from_pretrained(
                    default_repo_id,
                    subfolder='tokenizer_2',
                    cache_dir=cache_dir,
                ),
                'text_encoder_3': None,
            }
        elif fn_size < 1e10: # if model is below 10gb it does not have te3
            kwargs = {
                'text_encoder_3': None,
            }
        else:
            kwargs = {}
    else:
        modelloader.hf_login()
        loader = diffusers.StableDiffusion3Pipeline.from_pretrained
        kwargs['variant'] = 'fp16'

    if len(shared.opts.bnb_quantization) > 0:
        from modules.model_quant import load_bnb
        load_bnb('Load model: type=SD3')
        bnb_config = diffusers.BitsAndBytesConfig(
            load_in_8bit=shared.opts.bnb_quantization_type in ['fp8'],
            load_in_4bit=shared.opts.bnb_quantization_type in ['nf4', 'fp4'],
            bnb_4bit_quant_storage=shared.opts.bnb_quantization_storage,
            bnb_4bit_quant_type=shared.opts.bnb_quantization_type,
            bnb_4bit_compute_dtype=devices.dtype
        )
        if 'Model' in shared.opts.bnb_quantization:
            transformer = diffusers.SD3Transformer2DModel.from_pretrained(repo_id, subfolder="transformer", cache_dir=cache_dir, quantization_config=bnb_config, torch_dtype=devices.dtype)
            shared.log.debug(f'Quantization: module=transformer type=bnb dtype={shared.opts.bnb_quantization_type} storage={shared.opts.bnb_quantization_storage}')
            kwargs['transformer'] = transformer
        if 'Text Encoder' in shared.opts.bnb_quantization:
            te3 = transformers.T5EncoderModel.from_pretrained(repo_id, subfolder="text_encoder_3", variant='fp16', cache_dir=cache_dir, quantization_config=bnb_config, torch_dtype=devices.dtype)
            shared.log.debug(f'Quantization: module=t5 type=bnb dtype={shared.opts.bnb_quantization_type} storage={shared.opts.bnb_quantization_storage}')
            kwargs['text_encoder_3'] = te3

    pipe = loader(
        repo_id,
        torch_dtype=dtype,
        cache_dir=cache_dir,
        config=config,
        **kwargs,
    )
    devices.torch_gc()
    return pipe
