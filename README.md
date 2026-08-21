# rustylake-style

**语言 / Language:** 中文 | [English](README_EN.md)

将用户**上传**的肖像或物品，重绘成 Cube Escape / Rusty Lake（锈湖）插画风格的 Agent Skill：头像 / avatars 与 物品 / items。

把这个仓库地址交给你的 Agent，即可下载并安装此 skill：

```
https://github.com/cozyxiong/rustylake-style.git
```

或使用 skills CLI 安装：

```
npx skills add cozyxiong/rustylake-style
```

`SKILL.md` 位于仓库根目录，Agent Skills 扫描器与 `npx skills` 都能发现它。

## 使用

1. 安装 skill（上面的仓库地址，或 `npx skills add`）。
2. 上传一张人物照片（头像 / avatar）或物品照片（物品 / item）。
3. 请 Agent 做成 Rusty Lake / 锈湖风格。

Agent 必须用 image-edit / image-to-image 基于你上传的照片重绘；没有照片时不应凭空捏造面孔。

## 许可

MIT。见 [LICENSE](LICENSE)。本 skill 生成的是**原创**的「锈湖风格」图像，不复制官方立绘或精灵图。
