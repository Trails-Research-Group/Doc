# Thanks
Special thanks to Arc for helping with the research, as well as helping with the guide.

# Introduction
The present guide will use the [Kuro Tools MDL Importer](https://github.com/nnguyen259/KuroTools). It will describe the essential steps and provide details on certain parts in order for you to inject a model into Kuro no Kiseki (CLE version) while being able to more or less understand what you are doing.

Make sure you have [Blender](https://www.blender.org/download/) - preferably the latest version because some problems were found using versions < 3.4 - installed on your computer as it is the only modeling software that was validated for this injection process. This guide also assumes you have a FBX file in your possession, preferably with custom animations. For this guide, we will use a blend file containing F!Alear's model from Fire Emblem Engage, and her corresponding animations that we provide [here](https://github.com/Trails-Research-Group/Doc/releases/download/v0.0/Guide.Kuro.Model.Injection.zip).

##### Steps
* [Setting up the model (required)](#setting-up-the-model)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Setting the right size (required)](#setting-the-right-size)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Textures](#textures)    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Animations](#animations)    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Clean Up and Debugging](#clean-up-and-debugging)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Creating the shadow](#creating-the-shadow)    
* [Export to FBX (required)](#export-to-fbx)    
* [Materials json files (required)](#materials-json-file)  
* [Import the model (required)](#import-the-model)  

# Setting up the model
The first thing you need is a model of the character open in Blender, at the very least in T-pose, with or without animations. The demo files we provide for this guide contain a .blend with the mesh, rigged and in bind pose, and some animations (wait, attack, run) already embedded in the file. 
Preparing the model is out of the scope of this guide except for a few fixes that need to be mentioned, considering they could lead to a crash/no model visible in game.
## Setting the right size
So the first thing to do is setting up the right size for the model. In order to do this, we also provide a .fbx of a character taken from Kuro 1 that you will need to import in your .blend to check that both sizes match. Note that if the character is too big, the camera could clip into it, making it look like the model is not there, where it actually would be.  
First, import the dummy fbx to the scene like this:  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216250978-3640f720-8830-4bbb-951b-00d46c4876b8.png"/></p>
If you can't see the imported mesh, it likely means your model was scaled to (1.0,1.0,1.0), while base Kuro models are scaled to (0.01, 0.01, 0.01) when imported in Blender. This will result in something like this:  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216252140-d32deeab-9a2d-4e85-a83e-79fcdfd085e6.png"/></p>
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216252194-358fcaa6-dd59-40c8-b0aa-83b9934e1029.png"/></p>  
To fix this, you will need to apply the (0.01, 0.01, 0.01) scale to Alear's top rig node (which corresponds to "uAcc_spine2_Hair051 (merge)" in our case). It is basically the node just above the "Pose" and "Mesh" in the scene.  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216252926-5229ddcb-6928-49f1-a222-48682a5886c8.png"/></p>  
When this is done, both size should match:  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216253053-f7c2f09f-5696-4f18-8a67-1a9f585a8e5e.png"/></p>  
Now you can get rid of the dummy van's model and focus on Alear entirely.  

## Textures  
Textures in Kuro are split into a few distinct parts. For the sake of organization, it is best to name textures in the same style as Kuro does, where it is given the name of the mdl, as well as a few distinct identifiers. The identifiers each have a different meaning and informs us what style of texture the file contains, such as:  

00 - Face textures  
01 - Hair textures  
02 - /woman01/man01 - Skin textures  
03 - Clothing textures  
04 - Decals, logos, or additonal clothing textures  
05 - _eyes - Eye textures  

Many textures also have another identifier, and these ones tell you what kind of texure map the file is, and are as follows:

No letter identifier - A regular diffuse map with no special properties.  
_a - A diffuse texture with an alpha/transparency layer, typically hair but are also in a few select clothing maps.  
_n - Normal map texture.  
_q & _p - Mask map texture, used to provide various types of detailing.  
_r_p - Glow/Emissive Maps  
Toon - Cartoon maps which control angling and levels of light, includes maps like toon_cloth or toon_hair.   

These are the types of textures you will see most often, and the majority of them will have to be set in the chr json which will be discussed later. Some however, like diffuse and normal, can be set directly inside of blender and will have priority in the chr json over what maps are present in the default json. 

## Animations  
### Removing irrelevant animations
The first thing to do with animations is to remove the irrelevant ones. Blender stores the animation data as "Actions", that you can edit using the "Action Editor" in the "Animations" panel.      
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216254732-e4a8fc65-ff4b-403b-9cb4-f428685a3716.png"/>
</p>  
When importing a fbx file containing an animation, you expect to find a single "action" but will actually find more than one.
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216420199-83c893b8-a2af-4783-b587-057f00b3c398.png"/></p>  
Us, we only need one: the one which, when selected, plays the animation we are expecting the model to play. Usually it starts with the name of the "Pose" node: The node containing the "Pose" in the scene hierarchy.
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216420761-4b768b1a-4e1f-4821-b72c-5d5d0ac35970.png"/></p>  
we will need to remove the others. To do this, go to "Blender file" in the outliner:
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216420975-72df2733-efb5-497a-915a-f89f8165bd79.png"/></p>  
Then develop "Actions" and remove all of them except the one which plays the animation as you want it.
If you keep those irrelevant actions it will bloat the output file by a lot when exporting, as well as confusing you about which one is the MDL you want to include to your game.

### "Setting the bind pose" when exporting
This step is not mandatory if ALL of the animations you are going to use are inside your blend or fbx file. If you plan to use the original game animation mdl such as chr0000_mot_wait.mdl, you will need to do this step.
#### Explanations
Animations are a bit tricky because even if they play correctly in Blender, the mesh could very well be distorted in game. One of the main concerns is the "bind pose", which corresponds to the "origin" pose from which all the keyframes of the animation (rotation, translation, scale) are offsets. It directly depends on the transform (the set of position, rotation, scale) of the nodes composing the model, which are not set in stone.  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216254445-da8fb816-b1f7-4e55-b745-77d6f30f54da.png"/></p>  
 

At the FBX export step, the exported transforms are taken from the initial pose in which your character is at the first frame of the first blender action (which I believe is defined by alphabetical order based on the action's names).  
This is not a problem if you add all your animations in the same fbx file, and works with a single fbx, since all the keyframes (Pos, Rot, Scl) will be computed with the same origin pose (the first frame of the first blender action).  
However if you decide to import other animations in separate fbx files (because putting all your animations in the .blend file could bloat it), to convert them in .mdl later, the bind pose (or key frames' origin) will be different for each animation file. This is because the run.fbx animation file will have a bind pose based on the first frame of the run animation, while the wait animation file will have the first frame of the wait animation as its bind pose. Both origins are different so the coordinates in the keyframes will not be compatible.  

This is especially important if you plan to give your model the original animations from Kuro 1.  
The existing ones (ex: chr0000_mot_wait.mdl) in the model folder were compiled by falcom based on a bind pose in "T-pose". In that case, you will have to make sure each separate animation fbx file contains a dummy T pose animation as well to set the first frame and thus bind pose correctly.  

#### The actual process of setting a bind pose in Blender
To set up a bind pose, first go to the Animations panel and unlink (unselect, basically) any action that could be active at the moment:
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216315808-7028bd1a-db17-4ba3-965a-6e2dae042332.png"/></p>  
Then create a new action that will become our bind pose. You can name it however you want as long as the new action is the first one in the list of animations in the Action Editor (which is sorted using alphabetical order).  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216316376-7a99114e-8fab-4dd7-b77c-beaa1a37bbb5.png"/></p>  
The new action:  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216316455-0cbefa33-c932-4e8d-beb3-cf89a4b2f5cc.png"/></p>  
Now return to the "Layout" panel. You will select the pose of the character in the scene:  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216316599-13262fb5-2eaa-424a-9a87-03c375082e62.png"/></p>  
Switch to Pose Mode:  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216316681-b6a9bb9f-eb3d-4411-86cc-1d7649d77b7e.png"/></p>  
Select > All. It will select all the bones of the armature. Then Pose > Clear Transform > All.  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216316889-8c6b1655-9720-4fd2-aaa0-4e58a3cfd78a.png"/></p>  
This should reposition the model at bind pose. The only thing left to do is pressing I + "Location, Rotation & Scale", in order to set a  key frame for all channels of the animation. Go back to "Animation" and check that a key was indeed added:  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216317253-d5bf7e93-287d-441e-9d45-33532bdd4976.png"/></p>  
You should now be able to export animations correctly.


## Clean Up and Debugging

At this point, if your model is added to the game, their is a chance it may not work off the bat. Kuro is very particular with its models and basically any junk data in the mdl can prevent the game from functioning correctly. Here are a few things you can do to your model in Blender which may help to prevent or fix any issues within the game itself. Make sure your blend is saved before this to ensure no data loss while attempting any of these.   

1) Merge by Distance - Probably the most common issue is duplicate vertices, and its also one of the easiest to fix. Simply select all your vertices in edit mode, then go to Mesh/Clean up/Merge by distance. A menu will appear in the bottom left, with a few options. Make sure you select Keep Sharp Edges, but the distance is something you may need to toy with. .0001 is the largest you can go typically without merging separate vertices that need to stay apart, but testing has showed that you may need to go up to maybe .0004 for results. Check though afterwards if you go that high that nothing like vertices in the face have been badly affected by the merge, especially the mouth area. You can also deselect the face though from the materials tab beforehand if you want to go higher.   

2) Normalize weights - Occasionally some weights may not add up to 1, which the game really does not like. You can go to Weight Mode, then select the weights tab and hit normalize all to ensure that all weights on a certain mesh are normalized. You can also deselect lock active weights if your active vertex group may be the issue. Some weight painting may also be done here, if you know what you are doing in regards to that.   

3) Delete the shadow - An error in the decimation of the shadow can cause even the main mesh to deform in game, so if the previous options don't work, delete the shadow to see if their is an error in it and not the main mesh. It can always be remade afterwards so removing a potential factor is always useful.   

4) Delete individual meshes - This one only applies if you have kept all of the meshes separate. Usually, errors in models only occur if rigs have been change and/or meshes were merged, but on very rare occasions it can be individual meshes themselves. Going through and deleting ones you see are deformed may help to isolate the issue but it is unlikely unmerged meshes will error in the first place.   

5) Check your bones/Re-parent the rig - It may be possible that if you are adding new bones or swapping rigs, the weights did not apply correctly or the bind was incorrect. Removing your mesh from the rig, and reparenting it by selecting the rig and the mesh then going to Objects/Parent/Armature Deform may help reassign it properly. Also ensure that any bones needed have been added to the rig before this as missing bones damage the hierarchy, as well as the ability for the tool to properly compute the Inverse Bind Matrix.   

If your mesh is still erroring after all this, you may want to try a different approach from the beginning to see if it may not be an error in the original file. For example, if you are attempting to port an outfit to a different character, ensure that all bones are in the new rig from the beginning, and if possible avoid actively merging or moving any meshes until necessary. Making sure your base outfit works in game before porting something like the characters head will help isolate where the issues are in the mesh before they appear.   

## Creating the shadow
One of the things you will want to do at some point is create a shadow mesh for the game to use. In all 3d trails games, a low poly mesh is flattened to the ground and used to create the effect of a shadow, using only a single material on the whole mesh that is typically named "chr_shadow". To create this mesh, the easiest thing to do is to:

1) Select your mesh/meshes.
2) Ensure you are in Object Mode, then go to Objects tab and select Duplicate Objects.
3) Merge your new meshes together to create a single model. Delete all of the materials from it and create a new one named chr_shadow.
4) Select your new mesh then go to Edit Mode. 
5) Select all vertices, then go to Clean Up/Decimate Geometry, and set it to .2.

This drastically reduces the number of vertices while retaining the general shape of the mesh for use as a shadow. This can then be hidden while continuing to work on the model, or kept revealed if your next step is exporting. 

# Export to FBX    
If your scale is set, model work is done and the shadow created, it is time to export your model to an FBX. The most important things to note at this step is just the export settings. Ensure that Add Leaf Bones is turned off, as well as triangulation and tangent space is also turned off. Tangents are calculated by the Import tool itself and pre-existing ones will prevent the tool from reading the FBX. 

# Materials json files 
The tool relies on a system of json files in order to setup the parameters for each material/shader. 
There are two json files of interest: the first one is called "default_layouts.json". It is basically a catalogue of layouts for the most used materials that will help you gain time when writing a material file.  
Those layouts were generated by drag and dropping .mdl files onto "GenerateParametersLayout.exe". It will extract the parameters and their values. Then, you can copy the content of the generated json into "default_layouts.json".  

<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216321173-5d6eabac-6343-4397-9b7b-7a47a0461c47.png"/></p>

The other json is named after the model you are going to import into Kuro. You can either generate it by hand, copying the default_layouts json file's content manually, or drag and dropping the .fbx file onto the "GenerateParametersLayout.exe" executable. 

This one is pretty much necessary, while default_layouts is not. Also as stated before, it is named the same as the FBX file you are trying to export.

The typical process regarding json files is: 
- Make sure all materials names are defined inside the default_layouts. If for example your "default_layouts" does not have "chr_shadow" defined inside, you can take a random .mdl with a shadow from the base game and drop the file on "GenerateParametersLayout.exe", then copy the chr_shadow list of parameters.  
- Once the default_layouts is complete, export your .fbx file from Blender  
- Drag and drop your fbx file on "GenerateParametersLayout.exe" to generate the definitive list of material parameters for the model  
  
Once you have your <fbx_file_name>.json located in the same folder as ED9MDLTool.exe, you can generate the .mdl file.  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216322854-12b2998b-b9dd-41a4-86c2-d5f32fb3983a.png"/></p>

# Import the model
Once your fbx file and your corresponding json file are ready, you can convert your .fbx into .mdl for the game to read it.  
This step is pretty simple, you just have to drag and drop your .fbx file onto ED9MDLTool.exe.  
Afterwards, place your model inside the game directory/c/asset/common/model, and your textures inside c/asset/dx11/image.  
<p align="center"><img src="https://user-images.githubusercontent.com/69110695/216805451-2a0018f9-a6c0-413f-aff5-77e2e0afc739.gif"/></p>






