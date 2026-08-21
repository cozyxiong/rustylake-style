# Cube Escape / Rusty Lake look

This file is the only style source. Copy the constraints into every image-edit prompt. Do not replace them with a synonym of "Rusty Lake style".

The 锈湖头像 look is a **full illustration**: bold black outlines and flat cel fills. It is not a photograph with a filter, and not a photoreal face pasted onto a cartoon body.

## Shared look

Bold even-weight **black outlines** around every shape (face, hair, clothes, props). Flat low-fi illustration with limited shading — two or three cel-fill values max. Graphic, slightly crude analog-game stills. Not painterly oil, not 3D, not photoreal.

Muted desaturated palette: dusty greys, ochre, mustard, pale earth, rust brown, cream, dirty white, sickly olive / grey-green. Wallpaper and walls carry the olive-grey. Skin is pale ivory / light peach — readable as skin, with a hint of pink. It is not grey-green, not olive, not corpse-green; do not tint the face with the wallpaper. No neon, no saturated pop, no glossy photoreal.

Uncanny doll-like stillness. Deadpan. Figures and objects sit as if drawn and placed; they do not smile, blur, or pose cinematically.

Isolated subject. One person or one object owns the frame. No crowd, no busy tableau, no cinematic landscape.

## Face (avatars)

Canonical look plate: `references/avatar-look.jpg`. Always pass it as an extra image-edit reference for **how to draw** brows, eyes, and lips. It is not the identity.

Simplified geometric face, drawn like that plate:

Match that plate's drawing language:

- eyebrows: thin simple arches, a few short strokes
- eyes: large almond, half-lidded, a row of simple upper lashes, pale grey-green iris
- nose: a short angular line
- lips: small closed peach-pink mouth, two simple shapes
- hair *rendering*: solid outlined mass with parallel internal strand lines — but cut, length, bangs, and color come from the upload
- face *shape*, moles, lip piercings, earrings, and other marks come from the upload

Face marks (moles, beauty marks, lip piercings, earrings, scars, glasses, tattoos) come **only from the upload**. Before prompting, list them and their positions from the photo. Keep those. If the upload has none, draw none. Do not copy the look plate's mole, lip piercing, glasses, or jewelry.

Front-facing bust, head-and-shoulders, stiff posture. Background is a repeating **damask or floral wallpaper** in muted olive / grey-green. At most one quiet analog prop (rotary phone, side table). Not a sunset, beach, mountain, or fashion-illustration postcard.

## Prompt atoms (use these words)

When writing the image-edit prompt, include this block (adapt only the subject clause):

> Restyle into a Cube Escape / Rusty Lake still: full flat illustration with bold black outlines and limited shading; muted desaturated palette of greys, ochre, pale earth, and sickly green on wallpaper and props; pale ivory / light-peach skin (not grey-green); uncanny doll-like stillness; isolated subject. Analog puzzle-game frame. Not photoreal, not a photo-face collage.

Keep the upload's identity (the actual hair, clothes, face marks, or the actual object). Change medium and atmosphere, not who or what it is.

Always pass `references/avatar-look.jpg` as a look reference for avatars. If the user also attached more style examples, those are look only too. The upload is identity (face shape, hair, moles, lip piercings, earrings). Do not copy a look-plate person's face or marks.

## Avatar prompt

Use with image-edit / image-to-image when a portrait photo is the source. Paste, then fill only the identity clause from the upload:

> Restyle the person in the first image into a Cube Escape / Rusty Lake 头像. Match the second image (look plate) only for how to draw brows, eyes, and lips: thin arched brows, large half-lidded almond eyes with simple upper lashes, short line nose, small peach-pink closed mouth, bold black outlines, flat cel fills, ivory/peach skin, damask wallpaper. Keep identity from the first photo: face shape, hair cut/length/bangs/color, clothes, and face marks (moles, lip piercings, earrings — same count and place; if the photo has none, draw none). Do not copy the look plate's mole, lip piercing, glasses, or jewelry. Isolated bust, facing the viewer, stiff, uncanny doll-like stillness. Square-friendly framing, one subject, no cinematic landscape.

## Item prompt

Use with image-edit / image-to-image when an object photo is the source. This is an inventory piece, not a portrait. Paste, then name the object from the upload:

> Restyle this object into a Cube Escape / Rusty Lake 物品 — one isolated symbolic puzzle-inventory item, drawn the same way as the portraits: bold black outlines, flat cel fills, limited shading. Keep the object recognizable. Center it on a plain pale ground (cream, dirty white, or dusty grey), as if sitting in an analog adventure-game inventory slot. Muted desaturated palette of greys, ochre, pale earth, and sickly green. Uncanny doll-like stillness: a quiet, placed object, not a cinematic product shot or a busy still life. No extra props, no room scene, no figure.
