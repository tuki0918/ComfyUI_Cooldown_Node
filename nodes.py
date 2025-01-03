import time

class CooldownStringNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "STRING" : ("STRING", {"forceInput": True}),
                "sleep" : ("INT", {"default": 1, "min": 0, "max": 300})
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)
    CATEGORY = "Cooldown"
    FUNCTION = "main"

    def main(self, STRING, sleep):
        time.sleep(sleep)
        return (STRING,)

class CooldownIntNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "INT" : ("INT", {"forceInput": True}),
                "sleep" : ("INT", {"default": 1, "min": 0, "max": 300})
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("INT",)
    CATEGORY = "Cooldown"
    FUNCTION = "main"

    def main(self, INT, sleep):
        time.sleep(sleep)
        return (INT,)

class CooldownImageNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "IMAGE" : ("IMAGE", {"forceInput": True}),
                "sleep" : ("INT", {"default": 1, "min": 0, "max": 300})
            },
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("IMAGE",)
    CATEGORY = "Cooldown"
    FUNCTION = "main"

    def main(self, IMAGE, sleep):
        time.sleep(sleep)
        return (IMAGE,)

NODE_CLASS_MAPPINGS = {
    "CooldownStringNode": CooldownStringNode,
    "CooldownIntNode": CooldownIntNode,
    "CooldownImageNode": CooldownImageNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CooldownStringNode": "Cooldown -STRING-",
    "CooldownIntNode": "Cooldown -INT-",
    "CooldownImageNode": "Cooldown -IMAGE-",
}
