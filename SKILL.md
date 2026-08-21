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
