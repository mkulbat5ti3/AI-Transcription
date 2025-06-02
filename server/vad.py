from pyannote.audio import Model
from pyannote.audio.pipelines import VoiceActivityDetection
from server.config import HF_AUTH_TOKEN

def setup_vad_pipeline():
    model = Model.from_pretrained("pyannote/segmentation", use_auth_token=HF_AUTH_TOKEN)
    pipeline = VoiceActivityDetection(segmentation=model)
    pipeline.instantiate({
        "onset": 0.5,
        "offset": 0.5,
        "min_duration_on": 0.3,
        "min_duration_off": 0.3
    })
    return pipeline
