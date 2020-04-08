#ffmpeg -i input.flv -ss 00:00:14.435 -vframes 1 out.png # one pic

rm split/*

#ffmpeg -i load/SXSW1.mp4 -vf fps=1  split/out%03d.png    # every second
ffmpeg -i load/SXSW1.mp4 -vf fps=1/60  split/out%03d.png # every minute
#ffmpeg -i load/SXSW1.mp4 -vf fps=1/600 thumb%04d.png     # every 10 minutes