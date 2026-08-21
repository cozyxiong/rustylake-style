# Cube Escape / Rusty Lake look

This file is the only style source. Copy the constraints into every image-edit prompt. Do not replace them with a synonym of "Rusty Lake style".

The 锈湖头像 look is a **full illustration**: bold black outlines and flat cel fills. It is not a photograph with a filter, and not a photoreal face pasted onto a cartoon body.

## Shared look

Bold even-weight **black outlines** around every shape (face, hair, clothes, props). Flat low-fi illustration with limited shading — two or three cel-fill values max. Graphic, slightly crude analog-game stills. Not painterly oil, not 3D, not photoreal.

Muted desaturated palette: dusty greys, ochre, mustard, pale earth, rust brown, cream, dirty white, sickly olive / grey-green. Wallpaper and walls carry the olive-grey. Skin is pale ivory / light peach — readable as skin, with a hint of pink. It is not grey-green, not olive, not corpse-green; do not tint the face with the wallpaper. No neon, no saturated pop, no glossy photoreal.

Uncanny doll-like stillness. Deadpan. Figures and objects sit as if drawn and placed; they do not smile, blur, or pose cinematically.

Isolated subject. One person or one object owns the frame. No crowd, no busy tableau, no cinematic landscape.

## Face (avatars)

Look plates (drawing language only — two different people, same hand):

- `references/avatar-look.jpg`
- `references/avatar-look-b.jpg`

Always pass **both** as extra image-edit references so the model sees that hair, clothes, and marks change while brows/eyes/lips stay the same. They are not the identity.

Simplified geometric face, drawn like those plates:

- eyebrows: thin simple arches, a few short strokes
- eyes: large almond, half-lidded, a row of simple upper lashes, pale grey-green iris
- nose: a short angular line
- lips: small closed peach-pink mouth, two simple shapes
- hair *rendering*: solid outlined mass with parallel internal strand lines — cut, length, bangs, and color come from the upload
- clothes *rendering*: graphic outlined garment with fabric named from the upload (lace stays lace, knit stays knit)
- face *shape*, moles, lip piercings, earrings, and other marks come from the upload

Front-facing bust, head-and-shoulders, stiff posture. Background is a repeating **damask or floral wallpaper** in muted olive / grey-green. Do not copy a look plate's rotary phone or side table unless the upload has a similar prop. Not a sunset, beach, mountain, cherry blossom, or fashion-illustration postcard.

## Identity inventory (fill this before the one image-edit call)

Write these lines from the **upload**, then paste them into the prompt. Do not skip.

- face shape:
- hair: color, length, bangs, up/down, accessories (flower, clip, …)
- clothes: garment + color + fabric (say lace / knit / silk / denim explicitly)
- marks: moles (where), lip piercings, earrings, glasses, tattoos — or `none`

## Look-plate leak list (never copy these unless they are on the upload)

From `avatar-look.jpg`: black hair, cream ribbed knit sweater, mole by the eye, lip piercing, rotary phone.

From `avatar-look-b.jpg`: brown hair, purple flower, white lace blouse.

If the upload does not have it, it must not appear.

## One-shot avatar prompt

Make **one** image-edit / image-to-image call. Order: upload, then `avatar-look.jpg`, then `avatar-look-b.jpg`. Do not generate extra variants to pick from.

Fill the `{…}` slots from the identity inventory:

> Restyle the person in the first image into a Cube Escape / Rusty Lake 头像. Images 2 and 3 are look plates of two different people with the same drawing language — copy only that language: bold even black outlines, flat cel fills, thin arched brows, large half-lidded almond eyes with simple upper lashes, short line nose, small peach-pink closed mouth, ivory/peach skin, muted olive damask wallpaper, isolated front-facing bust, uncanny doll-like stillness. Identity from image 1 only: face shape {face}; hair {hair}; clothes {clothes}; face marks {marks}. Do not copy hair, clothes, knit sweater, lace blouse, flower, mole, lip piercing, glasses, jewelry, or rotary phone from the look plates unless that exact thing is on image 1. No cinematic leftover from the photo (no cherry blossoms, beach, sky, hand-on-face pose). Square-friendly framing, one subject.

## Item prompt

Use with image-edit / image-to-image when an object photo is the source. This is an inventory piece, not a portrait. Paste, then name the object from the upload:

> Restyle this object into a Cube Escape / Rusty Lake 物品 — one isolated symbolic puzzle-inventory item, drawn the same way as the portraits: bold black outlines, flat cel fills, limited shading. Keep the object recognizable. Center it on a plain pale ground (cream, dirty white, or dusty grey), as if sitting in an analog adventure-game inventory slot. Muted desaturated palette of greys, ochre, pale earth, and sickly green. Uncanny doll-like stillness: a quiet, placed object, not a cinematic product shot or a busy still life. No extra props, no room scene, no figure.
