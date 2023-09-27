Below are a few notes that should be valid for Cold Steel (3 and 4) and Reverie's animation system.
##### Summary
* [Model and animations](#model-and-animations) 
* [Scripting](#scripting) 
* [TBL editing](#tbl-editing)    


# Model and animations  
The first thing to understand about Cold Steel's facial animation system is that there are no "real" animation for speaking, like you would have one for walking, running, etc. It is more of a succession of static frames that are not meant to be played in order, but instead two or more can be selected from that list and the game will only interpolate between the selected ones following a cycle of frames.  
Basically all the characters in the game should share the same type of order for the frames: frame 0 is a "normal mood, eyes open" face, frame 1 is "the same mood but eyes closed". Then frame 2 is a more "determined" kind of mood with eyes open, then frame 3 the "same but eyes closed".
You can already tell that eyes will be closed on _even _frame numbers and open for _odd _numbers. It is not actually always the case, because out of the ~30 different frames there are, only 10 are used for blinking, while around 20 are used for the mouth movement when speaking.

The keyframes used for each frame are specificied in the .dae.phyre files for the mouth, the eyebrows and the eyeball, inside C_CHRXXX_FC1.pkg. This pkg is linked to the character using the t_name table.  
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/edeae715-8c5a-45e0-a476-bcf52e20ee8e">
</p>
<p align="center"><i>a t_name entry with the FC1 pkg specified</i></p>
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/1ac49d69-e92c-43e4-9a3f-e8fff67ba322">

</p>
<p align="center"><i>content of a _FC1 pkg</i></p>

In each of the .dae.phyre, you will find the keyframes for each group of bones related to the mouth, the eyebrows, etc.  

<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/45fc7a11-43d1-4cb1-a1a3-71591e652843">

</p>
<p align="center"><i>content of the eyebrow_l.dae.phyre</i></p>

Currently to my knowledge there is no easy process to visualize what each frame looks like, which is necessary if you want to make your own set of frames, but you can have a look at that [document](https://docs.google.com/spreadsheets/d/1n-qY9clxxM5-6F3n3OWx6Ig9vQktf48y_ILzKAxKSAA/edit#gid=0) which contains visuals of most of the frames that are used in blinking and speaking animations.

In the document, the whole section highlighted in yellow concerns the frames of the mouth that are used while speaking, and the highlighted section for the eyebrows is used for blinking. It is important to note that both sets of frames are completely uncorrelated. The keyframe of frame 0 for the mouth starts at t = 0s, while the first frame of the eyebrows starts at t = 1.3 s (which is the 40th frame if you're counting at 30 fps, which is the frequency used by the game for this).
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/9bbc9b3b-c9ad-4d02-bbd4-fd6e5a2a2e2a">
</p>
<p align="center"><i>"official" rean's frames for the mouth (the frame cursor is aligned with the frames since the scene was at 30 fps before importing the glb. You can see that it has a duration of 33 frames</i></p>

All of the above means that you need to create your own frames of angry, sad, happy faces for the mouth and eyebrows, animating the bones that are part of the mouth and eyebrows groups, separately. The most important thing to do however is making sure that your faces are at the correct frame. For this you can use the document above, where the frame number is specified for each face.

For example if you want to first make sure that blinking works, you need at least the "regular mood blinking". The document tells you that the blinking section starts at frame 50 and goes until frame 60. You need to at least make frame 50 and frame 51 (eyes open in regular mood, eyes closed in regular mood). More explanation on why you specifically need frame 50 and frame 51 will come later. 
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/68f9b8da-67bc-4ec1-b122-f08cc37c1041">
</p>
Like on the above screenshot, it is also important to set an initial frame at frame 0 for blender to not "simplify" it too much and erase the first second that is not used. Timing is very important and your two frames need to be placed at the 50 and 51 frames.
You also should make sure your scene is set at 30 fps: 
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/79b1736f-62b7-4f54-bf6b-1840b2242dab">
</p>
And finally note that eyebrows come in two files: one for the left and one for the right, both with the same timings but with different keyframe values for rotation/translation/scaling, and different bones.

Once your model is ready (all the faces are set at the correct frames), export it from Blender to fbx in order to open it in Maya. For this the export settings are really important. You need to make sure:
- that Armature is the only thing exported
- No leaf bones should be added 
- Key all bones is disabled
- No force Start/End keys
- Simplify is set to 1.00
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/5fa7c729-38de-479a-84e2-070edc3d8e92">
</p>
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/eefe4a89-fc58-4692-ba55-d87dc19854da">
</p>
<p align="center"><i>Export settings for Blender</i></p>
After reimportation in Maya, you can directly export it to dae with the following settings:
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/efa8d739-965a-43a0-a532-eb817c45a9da">
</p>   
<p align="center"><i>Export settings for Maya using the collada plugin</i></p>
Note: for the whole process in Blender and Maya, it is very important that the armature is preserved as in the base model. Do not make any change like removing parent bones, just keep it as was in the original model file.
Also, you have to make sure that your facial animations will not overlap with your global animations. This means that your regular animations (event, run, etc) where you're not supposed to be using the facial animation system (because the blinking is baked into those animations, for example) can have facial bones keyframes, BUT the animations that will use the facial animation system (typically, the WAIT animation, which will often be used to talk), SHOULD NOT have keyframes for the bones of the mouth and eyebrows. Failing to make sure of that will heavily alter the facial animations.

Finally, you'll have to repack it into a pkg (C_CHRXXX_FC1.pkg).
# Scripting

So the reason why you need to edit frames 50 and 51 for the regular blinking animation is actually related to scripts. Remember when in scena scripts you can often see the strings "0[autoE0]", "0[autoM0]", etc?
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/6ed7d92d-d71b-4da7-aeea-00bc33834a5e">
</p>   
<p align="center"><i>Example of a script using facial commands</i></p>

The 0 designates the frame 0, while E and M are for Eyes and Mouth respectively.
The game actually replaces "autoM0" with a facial string pattern that will describes the cycle. This string is defined in face.dat and comes in a few different combinations.
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/3c084778-78e1-41e6-a18a-43fb6239a100">
</p>   
<p align="center"><i>Face.dat</i></p>

So let's take an example, "0[autoE0]" which is the regular mood blinking. The game will replace [autoE0] with the string defined in face.dat for FC_autoE0, which is "0#r10#0x"
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/45068444-f076-4090-9a8c-f77cf3d63140">
</p>   
That gives: 0[autoE0] -> 00#r10#0x  
  
This pattern can be read like a list of frames that will be played in order, with special tags defined by # and a lowercase lettter that can alter the speed and other properties of the animation. Unfortunately I don't know what all the tags do.  
  
What I know is:  

* #Xr generates a random number and creates a timing based on that number, timing set at t = 4.0 + RNG (where t is in s).
* #Xs sets the speed of the animation to X% of the original speed
* #b is used to sync both eyebrows (it enables symmetry)
* If a number or a uppercase letter is not between a # and a lowercase letter, it can be interpreted as a frame number.
* If there is a + after a frame number, for example "0+", it will play the face at frame 0.5 (interpolated from frame 0 and 1)
* an uppercase letter can be A,B,C,D,E,F,G,H,I,J. A reads as frame 10, B, 11, ..., J 19.

so 00#r10#0x reads as playing the frame 0 two times, then wait a random delay of 4.0s + RNG, then play frame 1, then play frame 0, then there is a #0x special tag (maybe it's some fade out, or a sign to loop the cycle, I don't know). Which basically means eyes open, then for a random delay (to add more of a natural feeling) stays like this, then at frame 1, close the eyes, and directly proceeds to frame 0 (open the eyes again). It's basically a blinking.
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/4d5a98cb-5895-4ff4-9c53-ed510bdb4120">
</p>   
<p align="center"><i>Execution of the facial pattern in game</i></p>

Another example is for the mouth, 0[autoM0]:
0#70sJ00+010#0x means:
1. starts with frame 0
2. plays at 70% speed
3. plays frames J(frame 19), 0, 0.5, 0, 1
4. loops

This is the speaking animation. It alternates between different shapes of the mouth at a relatively slow rate while text is appearing on the screen.

Now that you know how patterns work, it's up to you to create your own cycles in face.dat.

# TBL editing
When adding a dubbed line to the game, it is important to make sure that the mouth animation aligns with the different pauses that can occur during it.  
For example, in:  
  
>"I guess this is the part where I say 
'Nice to meet you!". I'm Dana."
  
There is one significant pause, between the two sentences.   
  
>I guess this is the part where I say 
'Nice to meet you!".**[PAUSE]** I'm Dana.
  
When saying it, the character should move their mouth up until the PAUSE, then stops for a certain amount of time, then opens it back for the last part of the line, all in sync with the audio file that is playing. To define the duration and timing of the pauses, you will need to edit a tbl file called "vc_timing_[us/jp].tbl".

First start by adding a "VoiceTiming" entry copying an existing entry from an unrelated line. Then starts filling the different fields of the structure.
The structure is very short, 12 bytes long.
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/a9831831-ba8b-43f2-a6fe-57a51fdd8b31">
</p>   
<p align="center"><i>A VoiceTiming entry</i></p>

Ignoring the generic fields, the content of the entry is basically an array of "weirdly" encoded durations. On the screenshot above you can see there are 3 durations: FF, DF, and 3F. 
Note that there is another type of entry in this TBL file, called "VoiceTimingInfo". There is only one entry of that type and it only contains two things: 
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/d43e37ac-0230-4ce2-922c-3e74b4783b38">
</p>  
<p align="center"><i>A VoiceTimingInfo entry</i></p>
An integer equal to 0xC8 = 200, and another integer equal to 9. The 9 specifies the total length of the array of the VoiceTiming entries (including the padding), while the 200 is related to how the game converts real time to the encoded form it is using to store the durations.
  
Each byte in the array of durations describes a period of 1.6 seconds, calculated by 1000 (hardcoded in the exe) divided by 200 (the 200 from the VoiceTimingInfo). The bytes tell how long the character has their mouth open and how long they have it closed, in chronological order, during their respective period of 1.6 seconds. However, how they do it is a bit tricky and involves binary representations.
  
FF binary representation is 11111111. Each bit here represents a period of 1.6s/8 = 0.2 seconds. If it's 1, the mouth is open, if 0 it's closed during 0.2s. Thus a period of FF will make the character open their mouth for 1.6s. A period of DF which is 11011111 in binary will have 5 periods of 0.2s with the mouse open, then one period of 0.2s with the mouse closed, then again the mouth reopens for two periods of 0.2s.
  
<p align="center">
  <img src="https://github.com/Trails-Research-Group/Doc/assets/69110695/376160a8-50a1-45da-b954-74420f40fe25">
</p>  
<p align="center"><i>How the content of the VoiceTiming entry relates to the audio track</i></p>
  
This also means that you can only tune it as accurate as 0.2s periods are. If a silence occurs in the middle of a 0.2s long period, it should still be fine but if not you can still extend the silent part by editing the audio file it self.



