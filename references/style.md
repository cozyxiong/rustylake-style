# Cube Escape / Rusty Lake look

This file is the only style source. Copy the constraints into every image-edit prompt. Do not replace them with a synonym of "Rusty Lake style".

The 锈湖头像 look is a **full illustration**: bold black outlines and flat cel fills. It is not a photograph with a filter, and not a photoreal face pasted onto a cartoon body.

## Shared look

Bold even-weight **black outlines** around every shape (face, hair, clothes, props). Flat low-fi illustration with limited shading — two or three cel-fill values max. Graphic, slightly crude analog-game stills. Not painterly oil, not 3D, not photoreal.

Muted desaturated palette: dusty greys, ochre, mustard, pale earth, rust brown, cream, dirty white, sickly olive / grey-green. Wallpaper and walls carry the olive-grey. Skin is pale ivory / light peach — readable as skin, with a hint of pink. It is not grey-green, not olive, not corpse-green; do not tint the face with the wallpaper. No neon, no saturated pop, no glossy photoreal.

Uncanny doll-like stillness. Deadpan. Figures and objects sit as if drawn and placed; they do not smile, blur, or pose cinematically.

Isolated subject. One person or one object owns the frame. No crowd, no busy tableau, no cinematic landscape.

## Face (avatars)

Image-edit look plates are **face crops only** (brows, eyes, nose, mouth). Never pass the full bust files `avatar-look.jpg` / `avatar-look-b.jpg` into the image tool — those busts share a blunt hair mass and a round ribbed crew collar, and the model will reuse them as a template.

Pass both:

- `references/avatar-look-face.jpg`
- `references/avatar-look-b-face.jpg`

Copy **only** how brows, eyes, and lips are inked. Ignore hair in those crops. They contain no garment — do not invent a sweater from them.

Simplified geometric face:

- eyebrows: thin simple arches, a few short strokes
- eyes: large almond, half-lidded, a row of simple upper lashes, pale grey-green iris
- nose: a short angular line
- lips: small closed peach-pink mouth, two simple shapes

Hair and clothes are **new drawings from the upload**, not edits of a look-plate silhouette:

- Rebuild the hair mass from the upload's outline: part, bangs type, wave, length, volume. Do not paste the look-plate blunt straight hair block and recolor it.
- Rebuild the garment from the upload's construction: neckline, collar, sleeves, fabric. Do not keep a round ribbed crew-neck outline and swap the fill. If the upload is a fuzzy funnel, lace blouse, V-neck, or open collar, the black outline of the neck must match that, not the look-plate sweater.

Face *shape*, moles, lip piercings, earrings come from the upload.

Front-facing bust, head-and-shoulders, stiff. Background: repeating damask or floral wallpaper in muted olive / grey-green. No look-plate rotary phone unless the upload has one. No cinematic leftover (sunset, beach, cherry blossom, wisteria, sky).

## Identity inventory (fill this before the one image-edit call)

Write these lines from the **upload**, then paste them into the prompt. Do not skip.

- face shape:
- hair silhouette: color; length vs shoulders; part; bangs (blunt / curtain / side-swept / none); wave (straight / wavy / curly); volume; accessories
- clothes construction: garment; color; fabric (lace / knit / fuzzy / silk / denim); **neckline** (crew / V / funnel / lace collar / off-shoulder / fuzzy high neck / other); collar yes/no; sleeves
- marks: moles (where), lip piercings, earrings, glasses, tattoos — or `none`

## Look-plate leak list (never copy unless on the upload)

Do not pass full bust look plates into the image tool.

Shared fake template (NOT the look): blunt straight hair block, round ribbed crew-neck collar.

From the old busts: black hair, cream ribbed knit, mole by the eye, lip piercing, rotary phone, brown hair, purple flower, white lace blouse — only if the upload actually has that exact thing.

## One-shot avatar prompt

Make **one** image-edit / image-to-image call. Order: upload, then `avatar-look-face.jpg`, then `avatar-look-b-face.jpg`. Do not generate extra variants to pick from.

Fill the `{…}` slots from the identity inventory:

> Restyle the person in the first image into a Cube Escape / Rusty Lake 头像. Image 1 is the only source for hair and clothing geometry. Images 2 and 3 are tight face crops — copy only how brows, eyes, and lips are drawn (thin arched brows, large half-lidded almond eyes with simple upper lashes, short line nose, small peach-pink closed mouth). Ignore hair in those crops. They have no clothes; do not reuse a round ribbed crew-neck sweater. Rebuild a NEW hair mass from image 1: {hair}. Rebuild a NEW garment from image 1: {clothes}, neckline {neckline} — new collar outline, not a recolored look-plate sweater. Identity also: face shape {face}; face marks {marks}. Bold even black outlines, flat cel fills, ivory/peach skin, muted olive damask wallpaper, isolated front-facing bust, uncanny doll-like stillness. No mole, lip piercing, flower, glasses, or rotary phone unless listed in marks / hair / clothes from image 1. No cinematic leftover (wisteria, cherry blossoms, beach, sky, hand pose). Square-friendly framing, one subject.

After the image returns, check: (1) hair silhouette matches the upload, not the face-crop bangs; (2) neckline/collar matches the upload, with no leftover look-plate crew-neck ring. If either failed, that is look-plate identity leak — one retry from the original upload.

## Item prompt

Use with image-edit / image-to-image when an object photo is the source. This is an inventory piece, not a portrait. Paste, then name the object from the upload:

> Restyle this object into a Cube Escape / Rusty Lake 物品 — one isolated symbolic puzzle-inventory item, drawn the same way as the portraits: bold black outlines, flat cel fills, limited shading. Keep the object recognizable. Center it on a plain pale ground (cream, dirty white, or dusty grey), as if sitting in an analog adventure-game inventory slot. Muted desaturated palette of greys, ochre, pale earth, and sickly green. Uncanny doll-like stillness: a quiet, placed object, not a cinematic product shot or a busy still life. No extra props, no room scene, no figure.
