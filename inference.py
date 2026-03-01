import onnxruntime as ort
import numpy as np
import librosa

class MechGPTInference:
    def __init__(self, model_path):
        # This is the "Axiom Lab" secret: Calling the Vitis AI Execution Provider
        # This tells the code to skip the CPU and go straight to the AMD NPU
        providers = ['VitisAIExecutionProvider', 'CPUExecutionProvider']
        
        # Configuration for AMD XDNA architecture
        provider_options = [{
            'config_file': '/etc/vaip_config.json', # Standard path for Vitis AI config
            'cacheDir': './model_cache',
            'cacheKey': 'mech_gpt_v1'
        }, {}]

        try:
            self.session = ort.InferenceSession(
                model_path, 
                providers=providers, 
                provider_options=provider_options
            )
            print("✅ SUCCESS: Mech-GPT is running on AMD Ryzen AI NPU")
        except Exception as e:
            print(f"⚠️ NPU Handshake failed, falling back to CPU: {e}")
            self.session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])

    def process_audio(self, audio_path):
        """Convert raw factory noise into a Mel-Spectrogram for the NPU"""
        y, sr = librosa.load(audio_path, sr=22050)
        # We use Mel-spectrograms as the 'Acoustic Fingerprint'
        spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
        log_spectrogram = librosa.power_to_db(spectrogram, ref=np.max)
        
        # Prepare for the NPU (Reshape to match model input)
        input_data = log_spectrogram[np.newaxis, np.newaxis, :, :]
        return input_data.astype(np.float32)

    def detect_anomaly(self, input_data):
        """Run the sub-2ms inference"""
        input_name = self.session.get_inputs()[0].name
        # The actual 'thinking' happens here on the AMD silicon
        reconstruction = self.session.run(None, {input_name: input_data})[0]
        
        # We calculate the 'Reconstruction Error' 
        # High error = The machine sound has changed (Failure impending)
        mse = np.mean(np.power(input_data - reconstruction, 2))
        return mse
