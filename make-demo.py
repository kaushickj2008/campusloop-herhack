from pathlib import Path
import subprocess,json
root=Path(__file__).resolve().parent
frames=root/'demo-frames'
texts=[
'Campus Loop connects five everyday campus needs in one student workspace. This walkthrough uses actual captured states from the working application, with synthetic demonstration data.',
'A broken electronics cart blocks a ramp. Repair Route preserves the original report and suggests three connections: accessibility, maintenance, and component reuse. A person reviews the suggestions before creating the ticket.',
'The confirmed issue appears in Access Path. An open barrier triggers an illustrative detour through the student centre. The map is fictional, and the interface clearly says the reports are unverified.',
'After resolving the barriers in the issue board, the same route updates to the shorter direct path. This demonstrates the connection between maintenance status and accessibility planning.',
'Lab Loop matches available components to curated student projects. The environment monitor has all three required component types. Other recipes clearly show which parts are missing.',
'Reserving the kit deducts an Arduino, a temperature sensor, and a USB cable. The reservation is recorded, and the interface no longer offers a kit when its required sensor is unavailable.',
'Notice to Action extracts dates and action sentences from a workshop notice. Multiple dates are preserved for review rather than being silently treated as one deadline.',
'After confirmation, the checklist keeps the original source wording. Students can mark tasks complete and move directly to project kits or campus access.',
'Proof Pocket is separate from the campus feed. This synthetic incident note has its email and phone number redacted. Notes stay in tab memory, and exporting is explicit. Other identifying details still require human review.',
'Campus Loop is an open source Student Innovation prototype. Six automated logic tests pass. It uses transparent local rules, not a trained AI model. Campus records stay in browser storage. The working app and source repository are available for judges to explore.'
]
clips=[]; subtitles=[];offset=0
for i,text in enumerate(texts,1):
 stem=f'{i:02}'
 (frames/(stem+'.txt')).write_text(text)
 subprocess.run(['say','-r','165','-o',str(frames/(stem+'.aiff')),'-f',str(frames/(stem+'.txt'))],check=True)
 dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',str(frames/(stem+'.aiff'))]))+0.5
 out=frames/(stem+'.mp4')
 subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-i',str(frames/(stem+'.png')),'-i',str(frames/(stem+'.aiff')),'-vf','scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1','-r','25','-t',str(dur),'-c:v','libx264','-preset','fast','-tune','stillimage','-pix_fmt','yuv420p','-c:a','aac','-ar','44100','-af','apad',str(out)],check=True)
 clips.append("file '"+str(out)+"'")
 def ts(t):
  ms=int(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
 subtitles.append(f'{i}\n{ts(offset)} --> {ts(offset+dur)}\n{text}\n');offset+=dur
 print(f'Scene {i}/10 rendered',flush=True)
(frames/'clips.txt').write_text('\n'.join(clips));(root/'campusloop-demo.srt').write_text('\n'.join(subtitles))
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',str(frames/'clips.txt'),'-i',str(root/'campusloop-demo.srt'),'-map','0:v','-map','0:a','-map','1:s','-c','copy','-c:s','mov_text','-disposition:s:0','default','-movflags','+faststart',str(root/'campusloop-demo.mp4')],check=True)
print(json.dumps({'duration_seconds':round(offset,2),'video':str(root/'campusloop-demo.mp4')}))
