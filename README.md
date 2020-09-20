# Real Time Monophonic Pattern Detection


This repository contains the source code for the work done by the study ***Towards Real-Time Detection of Symbolic Musical Patterns: Probabilistic vs. Deterministic Methods***.
The research was conducted by:
 - Nishal Silva, Independent researcher, Colombo, Sri Lanka.
 - Carlo Fischione, KTH Royal Institute of Technology, Stockholm, Sweden.
 - Luca Turchet, University of Trento, Trento, Italy.

*__Abstract__ — The computational detection of musical patterns is widely studied in the field of Music Information Retrieval and has numerous applications. However, pattern detection in real-time has not yet received adequate attention. The real-time  is important in several application domains, especially in the field of the Internet of Musical Things. This study considers a single musical instrument and investigates the detection in real-time of patterns of a monophonic music stream. We present a representation mechanism to denote musical notes as a single column matrix, whose content corresponds to three key attributes of each musical note - pitch, amplitude and duration. The note attributes are obtained from a symbolic MIDI representation. Based on such representation, we compare the most prominent candidate methods based on neural networks and one deterministic method. Numerical results show the accuracy of each method, and allow us to characterize the trade-offs among those methods.*


The research was presented at the 27th FRUCT Conference, Trento, Italy, 7-9 September 2020.
The published paper is available [HERE](https://fruct.org/publications/fruct27/files/Sil.pdf).



## FOLDER STRUCTURE

 - **data** - Store the csv converted MIDI track and patterns
 - **det** - Scripts for the Deterministic System
 - **midi** - Store the MIDI files
 - **snn** - Scripts for the Single Neural Network System
 - **mnn** - Scripts for the Multiple Neural Network System


 ## OPERATIONAL PROCEDURE

  *Patterns are stored as MIDI files. In a real world scenario, the track will re real time, but for simulations, the track is also saved as a MIDI file*
  *The script has specified where a user input is required*

  1. *`create_test_data.ipynb`* is used to convert the MIDI track and the patters to CSV. **User input is required here.**
   - Number of patterns should be specified
   - The track file name should be specified
   - The pattern file names should be specified 
   - The metadata value is set to ttrue for the track only. This option writes the tempo, bpm, ticks per beat, pitch tolerance, amplitude tolerance, duration tolerance, and number of patterns to a file

  2. **Determinant System** 
   *`det/det.ipynb`* simulates a real time operation by extracting sub-sequences from the track, and checking them through the defined system, on the fly. Results are saved to an array for later viewing.

  3. **Single Neural Network based system**
   - *`snn/create_test_data.ipynb`* is used to create the test data and save them to a file. The number of positive and negative patterns should be specified by the user. A single dataset will be created with variations of all the patterns. The shorter patterns are padded at the end to equalize length.
   - *`snn/train_snn.ipynb`* contains the scripts to specify the paramaters of, compile and train the neural network. The parameters of the neural network could be changed here. The trained neural network is then saved to file in *`data/`*
   - *`snn/load_snn`* loads the saved neural network. Then it simulates a real time operation by extracting sub-sequences from the track, and checking them through the neural network, on the fly. Results are saved to an array for later viewing.

   4. **Multiple Neural Network based system**
   - *`mnn/create_test_data.ipynb`* is used to create the test data and save them to a file. The number of positive and negative patterns should be specified by the user. A training dataset will be created for *each pattern*.
   - *`mnn/train_mnn.ipynb`* contains the scripts to specify the paramaters of, compile and train the neural network. Each training dataset is loaded and and each neural network is trained and saved to file in *`data/`*. The parameters of the neural network could be changed here.
   - *`mnn/load_snn`* loads all saved neural networks. Then it simulates a real time operation by extracting sub-sequences from the track, and checking them through each neural network, on the fly. Results are saved to multiple arrays for later viewing.

