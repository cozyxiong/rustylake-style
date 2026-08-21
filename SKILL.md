---
name: rustylake-style
description: >
  Generate Rusty Lake / 锈湖 Cube Escape style 头像/avatars and 物品/items from a
  user-uploaded image (上传照片/图片). Restyle a portrait likeness or an inventory
  object with the host's image-edit tool. Use when the user asks for 锈湖风格,
  Cube Escape style, rusty lake avatar, rusty lake item, or runs /rustylake-style.
---

# Rusty Lake / 锈湖 restyle

Restyle a **user-uploaded** photo into Cube Escape / Rusty Lake illustration. Do not invent a face or object.

## Load the look

Read [`references/style.md`](references/style.md) before writing any prompt. That file is the only style source. Put its look into every image-edit prompt; do not substitute a vague "Rusty Lake style" line.

## Require an upload

If the user did not attach an image, ask them to upload a portrait (头像) or object photo (物品). Stop. Do not call text-to-image to invent a likeness.

When a photo is present, restyle it with the host **image-edit / image-to-image** tool. Do not generate a new face from a text prompt.

## Pick the path

| User gave... | Path |
|---|---|
| Face, selfie, portrait, 头像, avatar | Avatar |
| Object, prop, 物品, item, inventory | Item |
| Unclear | Ask which they want |

## Avatar

Follow this path when the upload is a portrait, selfie, face, 头像, or avatar.

1. If no portrait image is attached, ask for an upload. Stop. Do not invent a face.
2. Restyle **that** likeness with the host **image-edit / image-to-image** tool. Pass the user photo as the source. Do not use text-to-image for a likeness.
3. Keep identity: age presentation, face structure, hair, skin tone, distinguishing marks. Change medium, not person.
4. Use the **avatar prompt** in [`references/style.md`](references/style.md) (it already includes the shared look). Isolated bust or head-and-shoulders; photographic-collage / cut-out portrait — photo-like facial fragment on an illustrated body/room; uncanny doll-like stillness and a simplified geometric face.
5. If the result drifted (wrong person, neon/photoreal, busy cinematic scene), edit again from the **original upload**, not from the failed output.

## Item

Follow this path when the upload is an object, prop, 物品, item, or inventory piece.

1. If no object image is attached, ask for an upload. Stop. Do not invent the object.
2. Restyle **that** object with the host **image-edit / image-to-image** tool. Pass the user photo as the source.
3. Keep the object recognizable (shape, function, distinctive details). Change medium, not what it is.
4. Use the **item prompt** in [`references/style.md`](references/style.md). Present it as one isolated symbolic puzzle-inventory piece on a plain/pale ground — not a portrait, not a busy cinematic still life.
5. If the result became a scene of many objects, a product photo, or photoreal/neon, edit again from the **original upload**.
