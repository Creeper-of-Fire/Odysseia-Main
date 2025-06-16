# --- 全局常量与配置 ---

# 用于在清理历史消息时识别本机器人发出的交互面板
SIGNATURE_HELPER = "授权协议助手"

# 用于在已发布的最终协议中留下一个机器可读的“指纹”
SIGNATURE_LICENSE = "协议由授权助手生成"

# CC协议核心元素的通俗化、可复用解释
# 这是所有解释的“唯一真实来源”。
CC_ELEMENT_EXPLANATIONS = {
    "BY": "**✒️ 保留署名 (Attribution)**\n> **他人**在转载、二创等任何场景下使用**你的作品**时，都必须明确标注**你（原作者）**的名字或ID。",
    "NC": "**💰 非商业性使用 (Non-Commercial)**\n> **他人**不能将**你的作品**用于以商业盈利为主要目的的场合。例如，不能直接售卖，或用在付费才能观看的文章/视频中。",
    "SA": "**🔄 相同方式共享 (ShareAlike)**\n> 如果**他人**对**你的作品**进行了修改或二次创作，那么**他们的新作品**也必须使用与**你的作品**完全相同的CC协议进行分享。这常被称作“传染性”条款。",
    "ND": "**🚫 禁止二次创作 (NoDerivatives)**\n> **他人**不能对**你的作品**进行任何形式的修改，包括但不限于调色、裁剪、混剪、翻译等。只能原封不动地分享它。"
}

# Creative Commons 协议的标准化数据。
# 增加了 `elements` 字段，用于逐条解释。
CC_LICENSES = {
    # --- 最常用的非商业协议 ---

    "CC BY-NC-SA 4.0": {
        "label": "共享 保留署名-非商业化-相同方式共享 4.0",
        "description": "在同人创作圈很流行。能确保你的作品和所有二创作品永远保持开放共享。"
                       "比[BY-NC]协议多了一层“强制开放”保护，能防止二创作品被他人“锁死”后不再开放。",
        "elements": ["BY", "NC", "SA"],
        "reproduce": "允许转载，但必须保留署名、禁止商用，且转载时必须也采用本协议({license_type})进行分享。",
        "derive": "允许二创，但必须保留署名、禁止商用，且二创作品必须也采用本协议({license_type})进行分享。",
        "commercial": "禁止",
        "url": "https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh-hans"
    },
    "CC BY-NC 4.0": {
        "label": "共享 保留署名-非商业化 4.0",
        "description": "同样在同人圈很常见，给予了二创作者更大的自由。"
                       "与[BY-NC-SA]不同，它不强制二创作品也必须开放，二创作者可以为二创作品设置更严格的规定。",
        "elements": ["BY", "NC"],
        "reproduce": "允许转载，但必须保留署名且禁止用于商业目的。",
        "derive": "允许二创，但必须保留署名且禁止用于商业目的。(二创作品可使用不同协议)",
        "commercial": "禁止",
        "url": "https://creativecommons.org/licenses/by-nc/4.0/deed.zh-hans"
    },
    "CC BY-NC-ND 4.0": {
        "label": "共享 保留署名-非商业化-禁止修改 4.0",
        "description": "保护作品完整性的最严格非商业协议。完全禁止他人对你的作品进行任何修改。除非原作者另外许可，否则他人不能进行二次创作",
        "elements": ["BY", "NC", "ND"],
        "reproduce": "允许转载原文，但必须保留署名、禁止商用，且禁止任何修改。",
        "derive": "禁止一切形式的二次创作 (如需二创请单独联系作者)。",
        "commercial": "禁止",
        "url": "https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh-hans"
    },

    # --- 允许商业用途的协议 ---
    "CC BY 4.0": {
        "label": "共享 保留署名 4.0",
        "description": "最宽松的协议之一。只要保留你的署名，别人几乎可以做任何事，包括商业用途。",
        "elements": ["BY"],
        "reproduce": "允许转载，但必须保留作者署名。",
        "derive": "允许二创，但必须保留作者署名。",
        "commercial": "允许，但必须保留作者署名。",
        "url": "https://creativecommons.org/licenses/by/4.0/deed.zh-hans"
    },
    "CC BY-SA 4.0": {
        "label": "共享 保留署名-相同方式共享 4.0",
        "description": "允许商用版的“相同方式共享”。强调开放共享，所有二创作品（即使是商业性的）也必须以同样的开放姿态分享出去。",
        "elements": ["BY", "SA"],
        "reproduce": "允许转载，但必须保留署名并以相同方式共享({license_type})。",
        "derive": "允许二创，但必须保留署名并以相同方式共享({license_type})。",
        "commercial": "允许，但必须保留署名并以相同方式共享({license_type})。",
        "url": "https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans"
    },
    "CC BY-ND 4.0": {
        "label": "共享 保留署名-禁止修改 4.0",
        "description": "允许商用版的“禁止修改”。在保护作品完整性的同时，允许他人进行商业性的原文转载。",
        "elements": ["BY", "ND"],
        "reproduce": "允许转载原文，但必须保留署名且禁止任何修改。",
        "derive": "禁止一切形式的二次创作。",
        "commercial": "允许转载原文用于商业目的，但必须保留署名且禁止任何修改。",
        "url": "https://creativecommons.org/licenses/by-nd/4.0/deed.zh-hans"
    },
}

# 协议编辑中心的通用说明文本，方便在多处复用。
HUB_VIEW_CONTENT = (
    "请选择最适合你的授权方式。在选择前，请务必阅读以下说明：\n"
    "------------------------------------\n"
    "**选项一：【📝 自定义规则】**\n"
    "> 如果你有任何**具体要求**，例如：\n"
    "> - “**只允许**在站内转载”\n"
    "> - “**禁止**用于头像或做成表情包”\n"
    "> - “**禁止**被收录进任何合集包”\n"
    "> 那么，**建议使用【自定义】**。这是能精确表达你意愿的方式。\n\n"

    "**选项二：【📜 使用CC协议模板】**\n"
    "** Creative Commons (CC) **是一套国际通用的、成熟的授权体系，能清晰地界定你作品的分享边界。\n"
    "选择此项，你将从一系列标准模板开始，并可以借此衍生出你的自定义协议。\n"
    "> # ⚠️ 严重警告：\n"
    "> ## 若使用**标准CC协议**，意味着你接受你的作品被无限制地传播到**任何地方**！\n"
    "> ### 这**可能**会导致你的作品**合法**出现在你视野之外的网站、视频、甚至被打包成**免费素材合集**。\n"
    "> - 只要对方遵守了署名、非商用、传染等基本规则，这就是完全合规的。\n"
    "> - 如果你不能接受上述后果，请不要使用**标准CC协议**。\n"
    "> - 但本选项依旧可以让你在**标准CC协议**的基础上进行修改并且保存为你的自定义协议。\n\n"

    "**选项三：【💻 使用软件协议模板】**\n"
    "> 如果你发布的是**代码或软件项目**。\n"
)

# ============================================
#            开源软件教育平台
# ============================================

SOFTWARE_LICENSES = {
    "WTFPL": {
        "description": "“你™想干啥就干啥公共许可证”。终极的自由，已被FSF认证为兼容GPL，但未被OSI批准。",
        "url": "http://www.wtfpl.net/",
        "full_text": (
            ">>> DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE\n"
            "Version 2, December 2004\n\n"
            "Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>\n\n"
            "Everyone is permitted to copy and distribute verbatim or modified "
            "copies of this license document, and changing it is allowed as long "
            "as the name is changed.\n\n"
            "DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE\n"
            "TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION\n\n"
            "0\\. You just DO WHAT THE FUCK YOU WANT TO."
        )
    },
    "MIT": {
        "description": "最流行的宽松型许可证之一。代码可以被任意使用、修改、合并、出版、分发、再授权和/或贩卖，只需保留版权和许可声明。",
        "url": "https://opensource.org/licenses/MIT",
        "full_text": "条款很简单但还是超出了Discord的上限，所以请参考 [官方协议原文](https://opensource.org/licenses/MIT)"
    },
    "Apache-2.0": {
        "description": "一个在宽松和专利保护间取得良好平衡的许可证。除了MIT有的权限，它还明确授予了专利许可。",
        "url": "https://www.apache.org/licenses/LICENSE-2.0",
        "full_text": "条款复杂，请参考 [官方协议原文](https://www.apache.org/licenses/LICENSE-2.0)"
    },
    "GPL-3.0": {
        "description": "强大的“Copyleft”许可证。要求任何修改和分发的版本都必须以相同的GPL-3.0协议开源，保证了软件的永久自由。",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
        "full_text": "条款极其复杂，请参考 [官方协议原文](https://www.gnu.org/licenses/gpl-3.0.html)"
    },
    "AGPL-3.0": {
        "description": "GPL的超集，专为网络服务设计。即使软件仅通过网络提供服务而未分发，也必须提供修改后的源代码。反商业闭源的终极利器。",
        "url": "https://www.gnu.org/licenses/agpl-3.0.html",
        "full_text": "条款极其复杂，请参考 [官方协议原文](https://www.gnu.org/licenses/agpl-3.0.html)"
    }
}

# ============================================
#            命令与本地化配置
# ============================================
# 将所有斜杠命令的名称和描述集中在此处，便于未来进行本地化或统一修改。
COMMAND_CONFIG = {
    "group": {
        "name": "license",
        "description": "Manage your content license agreement"
    },
    "panel": {
        "name": "panel",
        "description": "Resend the license helper prompt in the current post"
    },
    "edit": {
        "name": "edit",
        "description": "Create or edit your default license agreement"
    },
    "settings": {
        "name": "settings",
        "description": "Configure the behavior of the license helper bot"
    },
    "show": {
        "name": "show",
        "description": "View your current default license agreement"
    }
}

COMMAND_CONFIG_ZH = {
    "group": {
        "name": "内容授权",
        "description": "管理你的内容授权协议"
    },
    "panel": {
        "name": "打开面板",
        "description": "在当前帖子中重新打开授权助手交互面板"
    },
    "edit": {
        "name": "编辑授权",
        "description": "创建或修改你的默认授权协议"
    },
    "settings": {
        "name": "设置助手",
        "description": "配置授权助手机器人的行为"
    },
    "show": {
        "name": "我的协议",
        "description": "查看你当前的默认授权协议"
    }
}

# 在代码中激活一套配置。当前选择中文版。
ACTIVE_COMMAND_CONFIG = COMMAND_CONFIG_ZH

MESSAGE_IGNORE = (f"{SIGNATURE_HELPER}: \n"
                  f"好的，我以后不会再主动打扰你了。\n"
                  f"你可以随时使用 `/{ACTIVE_COMMAND_CONFIG['group']['name']} {ACTIVE_COMMAND_CONFIG['settings']['name']}` 命令，在配置中重新启用我。\n"
                  f"也可以随时使用 `/{ACTIVE_COMMAND_CONFIG['group']['name']} {ACTIVE_COMMAND_CONFIG['panel']['name']}` 命令，直接调出我的主面板。\n")

MESSAGE_IGNORE_ONCE = (f"{SIGNATURE_HELPER}: \n"
                       f"好的，那我就先溜了。\n"
                       f"你可以随时使用 `/{ACTIVE_COMMAND_CONFIG['group']['name']}` 命令来设置你的授权协议。")
