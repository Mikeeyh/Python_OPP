from gtts import gTTS
import os


def text_to_audio(text, language='en', voice_variant='com', output_file='output.mp3'):
    try:
        # Create a gTTS object with the specified language and voice variant
        tts = gTTS(text=text, lang=language, tld=voice_variant, slow=False)

        # Save the audio file
        tts.save(output_file)

        # Play the audio file (optional)
        # os.system("start " + output_file)  # Uncomment this line to play the audio automatically

        print(f"Audio generated successfully: {output_file}")

    except Exception as e:
        print(f"Error generating audio: {e}")


if __name__ == "__main__":
    # Input text you want to convert to audio
    input_text = "Здравеите, как сте"

    # Specify the language (optional, default is English 'en')
    language_code = 'bg'

    # Specify the voice variant (optional, default is 'com' for American English)
    voice_variant_code = 'com'  # Use 'co.uk' for British English, 'com.au' for Australian English, etc.

    # Specify the output file name (optional, default is 'output.mp3')
    output_file_name = 'output.mp3'

    # Convert text to audio
    text_to_audio(input_text, language=language_code, voice_variant=voice_variant_code, output_file=output_file_name)