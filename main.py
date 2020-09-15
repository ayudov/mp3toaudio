import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from tkinter import *
# from tkinter.ttk import *
from tkinter import messagebox, filedialog
import os
import webbrowser


# import audio_to_text


def get_file_path():
    tempdir = filedialog.askopenfilename(initialdir=os.getcwd(),
                                         filetypes=(("wav files", "*.wav"), ("mp3 files", "*.mp3")))
    print(tempdir)
    textInput.delete(0, END)
    textInput.insert(0, tempdir)
    # login = loginInput.get()
    # password = passField.get()
    # info_str = f'Data: {str(login)}, {str(password)}'
    # # messagebox.showinfo(title='Message box name', message=info_str)
    # messagebox.showerror(title='', message='Error always')
    return tempdir


# def get_text(path):
#     text = get_large_audio_transcription(path)
#     # text1.insert(END, text)
#     return "break"


# a function that splits the audio file into chunks
# and applies speech recognition

def get_large_audio_transcription(path: str):
    # def close_window(root):
    #     root.destroy()
    # wait_window = Toplevel(root)
    # wait_window.geometry('400x200')
    # wait_window.resizable(width=False, height=False)
    # wait_window.title = 'Info'

    # wiatLabel = Label(wait_window, text="Please, wait...", command = wait_window.destroy()).pack()
    # closeButton = Button(wait_window, text="Close").pack()

    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    print("start converting")
    print("Path to file:"+path)
    title4['text'] = 'Початок конвертації'
    print('Початок конвертації')
    root.update_idletasks()
    r = sr.Recognizer()
    # open the audio file using pydub
    if path.endswith('.wav'):
        print('it is .wav file')
        sound = AudioSegment.from_wav(path)
        title4['text'] = 'Знайдений wav файл'
        print('Знайдений wav файл')
        root.update_idletasks()
    elif path.endswith('.mp3'):
        print('it is .mp3 file')
        temp = AudioSegment.from_mp3(path)
        temp.export('temp.wav', format="wav")
        sound = AudioSegment.from_wav('temp.wav')
        os.remove('temp.wav')
        title4['text'] = 'Знайдений mp3 файл'
        print('Знайдений mp3 файл')
        root.update_idletasks()
    else:
        print('none of file')

    # split audio sound where silence is 700 milliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=500,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS - 14,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=500,
                              )
    num_of_chunks = str(len(chunks))
    title4['text'] = 'Створено '+num_of_chunks+' підфайлів'
    print('Створено '+num_of_chunks+' підфайлів')
    #title4['text'] = f'СтворeHo {num_of_chunks} підфайлів'
    root.update_idletasks()
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, "chunk"+str(i)+".wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            r.adjust_for_ambient_noise(source)
            audio_listened = r.record(source)
            # try converting it to text
            try:
                # text = r.recognize_google(audio_listened)
                text = r.recognize_google(audio_listened, language="uk-UA")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = text.capitalize()+'.'
                print(chunk_filename, ":", text)
                whole_text += text
        title4['text'] = 'Створено '+num_of_chunks+' підфайлів\nОброблено '+str(i)+'/'+num_of_chunks
        print('Оброблено '+str(i)+'/'+num_of_chunks)
        root.update_idletasks()
        os.remove(os.path.join(folder_name, "chunk"+str(i)+".wav"))

    title4['text'] = 'Завершено'
    print('Завершено')
    root.update_idletasks()
    text1.insert(END, whole_text)
    # return the text for all chunks detected
    return whole_text


root = Tk()

root['bg'] = '#fafafa'
root.title('Отримати текст')
# root.wm_attributes('-alpha', 0.7)
root.geometry('1500x1500')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=1500, width=1500)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relwidth=1, relheight=1)

title1 = Label(frame, text='Програма для конвертації аудіофайлу (mp3 або wav) у текст\nДля отримання таких форматів '
                           'скористайтесь сайтом нижче',
               bg='white', font=30)
title1.pack()


def callback(url):
    webbrowser.open_new(url)


link3 = Label(frame, text="Convert to .wav", fg="blue",  bg='white', cursor="hand2")
link3.pack()
link3.bind("<Button-1>", lambda e: callback("https://audio.online-convert.com/ru/convert-to-wav"))

title1 = Label(frame, text='Для роботи програми необхідне стабільне підключення до мережі Інтернет', bg='white', font=30)
title1.pack()

title6 = Label(frame, text='Натисніть для пошуку файлу:', bg='white', font=30)
title6.pack()

btn = Button(frame, text='Пошук...', bg='white', command=get_file_path)
btn.pack()

title2 = Label(frame, text='Шлях до файлу', bg='white', font=30)
title2.pack()

textInput = Entry(frame, bg='white')
textInput.pack()

btn_convert = Button(frame, text='Конвертувати', bg='white',
                     command=lambda: get_large_audio_transcription(textInput.get()))
btn_convert.pack()

title2 = Label(frame, text='Натисніть "Конвертувати" та чекайте.\n Для копіювання виділіть текст та натисніть '
                           'комбінацію клавіш Ctrl + C', bg='white', font=30)
title2.pack()

text1 = Text(frame)
text1.pack()

title5 = Label(frame, text='Процес: ', bg='white', font=30)
title5.pack()
title4 = Label(frame, text='', bg='white', font=30)
title4.pack()

# passField = Entry(frame, bg='white', show='*')
# passField.pack()

root.mainloop()
# root.withdraw() #use to hide tkinter window
#
# currdir = os.getcwd()
#
# tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
# if len(tempdir) > 0:
#     print ("You chose %s" % tempdir)
#     print("started process")
#
#     print(audio_to_text.get_large_audio_transcription(tempdir))
