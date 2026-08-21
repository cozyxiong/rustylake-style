# rustylake-style

**Language / 语言:** [中文](README.md) | English

An [Agent Skill](https://agentskills.io/) that restyles a **user-uploaded** portrait or object into Cube Escape / Rusty Lake (锈湖) illustration: 头像/avatars and 物品/items.

Give this repo to your Agent so it can download the skill:

```
https://github.com/cozyxiong/rustylake-style.git
```

Or install with the skills CLI:

```
npx skills add cozyxiong/rustylake-style
```

`SKILL.md` sits at the repository root so Agent Skills scanners and `npx skills` discover it.

## Use

1. Install the skill (URL above, or `npx skills add`).
2. Upload a photo of a person (头像/avatar) or an object (物品/item).
3. Ask the Agent for a Rusty Lake / 锈湖 restyle.

The Agent must restyle the upload with image-edit / image-to-image. It should not invent a face when no photo is attached.

## License

MIT. See [LICENSE](LICENSE). This skill produces original images *in the style of* Cube Escape / Rusty Lake. It does not copy official sprites or portraits.
