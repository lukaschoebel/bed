import os
import sys
import pylab
import librosa
import matplotlib
import numpy as np
import librosa.display
from pathlib import Path
from pydub import AudioSegment

matplotlib.use('Agg') # No pictures displayed 

class PreProcessor:
    def __init__(self, sample_path, frame_size=960, dir_path="../data/processed"):
        """
        Initializes the PreProcessor class for setting up training data.
        
        Here, audio samples are getting preprocessed and the respective spectrogram
        of the chunks of frame_size ms are getting exported to the specified dir_path.

        Parameters
        ----------

        sample_path : str
            path to the provided audio sample as .wav file

        frame_size : int > 0, optional
            framesize in ms

        dir_path : str, optional
            directory to which the processed images should be written to
        """
        
        # check if file exists
        assert os.path.isfile(sample_path), f"file '{sample_path}' cannot be found"
    
        self.fs = frame_size
        self.dir_path = dir_path
        self.sample_path = sample_path
        self.sample_name = sample_path.split("/")[-1]

        
        # If dir_path doesn't exist => create
        Path(dir_path).mkdir(parents=True, exist_ok=True)

        self.tmp_path = f'{self.dir_path}/tmp'
        Path(self.tmp_path).mkdir(parents=True, exist_ok=True)
    
        ## 1. Create snippets
        self.create_snippets()

        ## 2. Create spectrograms from snippets
        self.create_specs()

        print(f'Processed {self.sample_name} and saved to {dir_path}.')
        

    def create_snippets(self):
        """
        Cuts the audio sample into pieces of self.fs ms length and saves them into a specified folder
        """
        
        wav = AudioSegment.from_file(self.sample_path, format="wav")
        for i, chunk in enumerate(wav[::self.fs]):
            if len(chunk) != self.fs: break ## Throw away if snippet length is not self.fs
            with open(f"{self.tmp_path}/{self.sample_name.replace('.wav', '')}-tmp-{i}.wav", "wb") as f:
                chunk.export(f, format="wav")

    def create_specs(self, n_fft=2048, hop_length=50, n_mels=64):
        """
        Creates the respective spectrograms from the short sequences

        Parameters
        ----------

        n_fft : int > 0 [scalar], optional
            length of the FFT window

        hop_length : int > 0 [scalar], optional
            number of samples between successive frames.

        n_mels : int > 0 [scalar], optional
            number of Mel bands to generate

        """

        # iterate over processed/tmp
        for f in os.listdir(self.tmp_path):
            # load the tmp sound snippets
            sample, sr = librosa.load(f'{self.tmp_path}/{f}', sr=None, mono=True, offset=0.0, duration=None)   
            save_path = f"{self.dir_path}/{f.replace('.wav', '.jpg').replace('-tmp', '')}"

            # axis formatting
            pylab.axis('off') # no axis
            pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
            
            # create spectrogram
            S = librosa.feature.melspectrogram(y=sample, sr=sr, n_fft=n_fft, n_mels=n_mels)
            S_DB = librosa.power_to_db(S, ref=np.max)
            librosa.display.specshow(data=S_DB, sr=sr, hop_length=hop_length)
            
            # save spectrogram to loc
            pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
            pylab.close()

        # remove processed/tmp directory to delete tmp sound snippets
        os.system(f"rm -r {os.getcwd().replace('/scripts', self.tmp_path.replace('..', ''))}")

if __name__ == "__main__":

    if len(sys.argv) == 2:
        p = PreProcessor(sys.argv[1])
    else:
        p = PreProcessor("../data/desk.wav")
