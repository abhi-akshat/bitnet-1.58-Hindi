model_name = "ai4bharat/Airavata"

class Config:
    config_100m = {
        "MODEL_CONFIG" : model_name,
        "HEADS" : 8,
        "DIMENSIONS" : 512,
        "LAYERS" : 6,
        "INTERMEDIATE_SIZE" : 1024,
        "CONTEXT_LENGTH" : 256,
        "NEW_MODEL" : "Bitnet-Airavata-100M"
    }
    config_160m = {
        "MODEL_CONFIG" : model_name,
        "HEADS" : 12,
        "DIMENSIONS" : 768,
        "LAYERS" : 12,
        "INTERMEDIATE_SIZE" : 1024,
        "CONTEXT_LENGTH" : 256,
        "NEW_MODEL" : "Bitnet-Airavata-100M"
    }
    config_400m = {
        "MODEL_CONFIG" : model_name,
        "HEADS" : 16,
        "DIMENSIONS" : 1024,
        "LAYERS" : 24,
        "INTERMEDIATE_SIZE" : 1024,
        "CONTEXT_LENGTH" : 256,
        "NEW_MODEL" : "Bitnet-Airavata-100M"
    }
    config_1b = {
        "MODEL_CONFIG" : model_name,
        "HEADS" : 8,
        "DIMENSIONS" : 2048,
        "LAYERS" : 16,
        "INTERMEDIATE_SIZE" : 1024,
        "CONTEXT_LENGTH" : 256,
        "NEW_MODEL" : "Bitnet-Airavata-100M"
    }
    config_3b = {
        "MODEL_CONFIG" : model_name,
        "HEADS" : 32,
        "DIMENSIONS" : 2560,
        "LAYERS" : 32,
        "INTERMEDIATE_SIZE" : 1024,
        "CONTEXT_LENGTH" : 256,
        "NEW_MODEL" : "Bitnet-Airavata-100M"
    }
    config_7b = {
        "MODEL_CONFIG" : model_name,
        "HEADS" : 32,
        "DIMENSIONS" : 4096,
        "LAYERS" : 32,
        "INTERMEDIATE_SIZE" : 1024,
        "CONTEXT_LENGTH" : 256,
        "NEW_MODEL" : "Bitnet-Airavata-100M"
    }
    
    def getConfig(self, param):
        if param == "100m":
            return self.config_100m
        elif param == "160m":
            return self.config_160m
        elif param == "400m":
            return self.config_400m
        elif param == "1b":
            return self.config_1b
        elif param == "3b":
            return self.config_3b
        elif param == "7b":
            return self.config_7b
        else:
            return self.config_100m
    
config  = Config()