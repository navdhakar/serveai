import subprocess, sys
class Autoalpacalora:
    def __init__(self, input, base_model, lora_weights):
        self.input = input
        self.load_8bit = False,
        self.base_model = base_model,
        self.lora_weights = lora_weights,
        self.prompt_template= "",  
        self.server_name = "0.0.0.0",  

       # require_install = ['accelerate', 'appdirs', 'loralib', 'bitsandbytes', 'black', 'black[jupyter]', 'datasets', 'fire', 'git+https://github.com/huggingface/peft.git', 'transformers>=4.28.0', 'sentencepiece', 'gradio', 'scipy', 'tqdm']
       # for package in require_install:
       #     subprocess.run([sys.executable, "-m", "pip", "install", package])
       # from serveai.models.alpacalora import Loadmodel, Evalmodel

    def loadmodel(self):
        self.model = Loadmodel(load_8bit = self.load_8bit, base_model = self.base_model, lora_weights = self.lora_weights)
        out
    def inference(
        self,
        instruction,
        model,
        input=None,
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        max_new_tokens=128,
        stream_output=False,
    ):
        if model:
            self.output = Evalmodel(
                                instruction=instruction,
                                model=model,
                                input=None,
                                temperature=0.1,
                                top_p=0.75,
                                top_k=40,
                                num_beams=4,
                                max_new_tokens=128,
                                stream_output=False,
                            )    
            return output
        else:
            return "Please load the model first(modelinstance.loadmodel())."
    def train(self):
        return f"training model" 
