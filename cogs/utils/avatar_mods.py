#From sir-lancebot

import discord
from io import BytesIO
from PIL import Image
from typing import Callable



class AvatarMods:
    @staticmethod
    def apply_effect(
        image_bytes: bytes, effect: Callable, filename: str, *args
    ) -> discord.File:
        """Applies the given effect to the image passed to it."""
        im = Image.open(BytesIO(image_bytes))
        im = im.convert("RGBA")
        im = im.resize((1024, 1024))
        im = effect(im, *args)

        bufferedio = BytesIO()
        im.save(bufferedio, format="PNG")
        bufferedio.seek(0)

        return discord.File(bufferedio, filename=filename)

    @staticmethod
    def eight_bit_effect(image: Image.Image) -> Image.Image:
        image = image.resize((32, 32), resample=Image.NEAREST)
        image = image.resize((1024, 1024), resample=Image.NEAREST)
        return image.quantize()

    @staticmethod
    def pixelate(image: Image.Image, distortion: int) -> Image.Image:
        if not 1 <= distortion <= 100:
            raise ValueError("distortion must be between 1 and 1024.")

        dist_level = distortion * 1024 // 100
        image = image.resize((dist_level, dist_level), resample=Image.NEAREST)
        image = image.resize((1024, 1024), resample=Image.NEAREST)
        return image.quantize()