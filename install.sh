#!/usr/bin/env bash
# UTM Link Generator — 安装脚本
# 将 skill 以 symlink 方式安装到 ~/.codex/skills 和 ~/.agents/skills

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
SKILL_NAME="utm-link-generator"
SKILL_SOURCE="$REPO_DIR/skills/$SKILL_NAME"

echo "🔗 Installing UTM Link Generator skill..."

# 检测可用的 skill 目录
SKILL_DIRS=()

if [ -n "${CODEX_HOME:-}" ]; then
    SKILL_DIRS+=("$CODEX_HOME/skills")
fi

if [ -d "$HOME/.codex/skills" ]; then
    SKILL_DIRS+=("$HOME/.codex/skills")
fi

if [ -d "$HOME/.agents/skills" ]; then
    SKILL_DIRS+=("$HOME/.agents/skills")
fi

# Proma workspace
PROMA_SKILLS="$HOME/.proma/agent-workspaces/c/skills"
if [ -d "$PROMA_SKILLS" ]; then
    SKILL_DIRS+=("$PROMA_SKILLS")
fi

if [ ${#SKILL_DIRS[@]} -eq 0 ]; then
    echo "⚠️  未检测到 skill 目录，创建 ~/.agents/skills"
    mkdir -p "$HOME/.agents/skills"
    SKILL_DIRS+=("$HOME/.agents/skills")
fi

INSTALLED=0
for DIR in "${SKILL_DIRS[@]}"; do
    TARGET="$DIR/$SKILL_NAME"
    if [ -L "$TARGET" ] && [ "$(readlink "$TARGET")" = "$SKILL_SOURCE" ]; then
        echo "  ✅ $TARGET — 已安装"
        INSTALLED=1
    elif [ -e "$TARGET" ]; then
        echo "  ⚠️  $TARGET — 已存在但不是 symlink，跳过"
    else
        mkdir -p "$DIR"
        ln -sfn "$SKILL_SOURCE" "$TARGET"
        echo "  ✅ $TARGET — symlink 安装完成"
        INSTALLED=1
    fi
done

if [ "$INSTALLED" -eq 1 ]; then
    echo ""
    echo "🎉 UTM Link Generator 安装完成！"
    echo ""
    echo "使用方法："
    echo "  在 AI 会话中输入以下关键词触发："
    echo "    - \"生成utm链接\""
    echo "    - \"帮我生成UTM链接\""
    echo ""
    echo "或者直接使用命令行："
    echo "  python3 skills/utm-link-generator/scripts/utm_generator.py --interactive"
    echo ""
    echo "查看所有选项："
    echo "  python3 skills/utm-link-generator/scripts/utm_generator.py --help"
else
    echo "❌ 安装失败，请检查目录权限"
    exit 1
fi
