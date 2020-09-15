# import speech_recognition as sr
# import os
# from pydub import AudioSegment
# from pydub.silence import split_on_silence
# from main import btn_convert
# from tkinter import RAISED
#
#
# # a function that splits the audio file into chunks
# # and applies speech recognition
#
# def get_large_audio_transcription(path):
#     """
#     Splitting the large audio file into chunks
#     and apply speech recognition on each of these chunks
#     """
#     btn_convert['relief'] = RAISED
#     r = sr.Recognizer()
#     # open the audio file using pydub
#     sound = AudioSegment.from_wav(path)
#     # split audio sound where silence is 700 milliseconds or more and get chunks
#     chunks = split_on_silence(sound,
#                               # experiment with this value for your target audio file
#                               min_silence_len=500,
#                               # adjust this per requirement
#                               silence_thresh=sound.dBFS - 14,
#                               # keep the silence for 1 second, adjustable as well
#                               keep_silence=500,
#                               )
#     folder_name = "audio-chunks"
#     # create a directory to store the audio chunks
#     if not os.path.isdir(folder_name):
#         os.mkdir(folder_name)
#     whole_text = ""
#     # process each chunk
#     for i, audio_chunk in enumerate(chunks, start=1):
#         # export audio chunk and save it in
#         # the `folder_name` directory.
#         chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
#         audio_chunk.export(chunk_filename, format="wav")
#         # recognize the chunk
#         with sr.AudioFile(chunk_filename) as source:
#             r.adjust_for_ambient_noise(source)
#             audio_listened = r.record(source)
#             # try converting it to text
#             try:
#                 # text = r.recognize_google(audio_listened)
#                 text = r.recognize_google(audio_listened, language="uk-UA")
#             except sr.UnknownValueError as e:
#                 print("Error:", str(e))
#             else:
#                 text = f"{text.capitalize()}. "
#                 print(chunk_filename, ":", text)
#                 whole_text += text
#         os.remove(os.path.join(folder_name, f"chunk{i}.wav"))
#     # return the text for all chunks detected
#     return whole_text
#
# # path = "7601-291468-0006.wav" path = os.path.join(os.path.join(os.path.expanduser('~')),
# # 'Desktop/Смертельна_ДТП_у_Запорізькій_області_водій_навмисно_збив_односельця.wav') print("\nFull text:",
# # get_large_audio_transcription(path))
