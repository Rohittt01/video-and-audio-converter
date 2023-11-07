import ffmpeg

format = input("What format do you  want? ")
input_file = 'videos/sicko.mp4'
output_file = f'output_video.{format}'

ffmpeg.input(input_file).output(output_file).run()
