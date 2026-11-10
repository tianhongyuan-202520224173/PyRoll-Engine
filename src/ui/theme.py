"""自定义主题 —— 冷色深底 + 朱红点缀，字体与配色均可在此统一调整。"""

COLORS = {
    # 背景色（冷色深底）
    "bg_primary":   "#17181C",
    "bg_secondary": "#1F2127",
    "bg_card":      "#24262D",
    "bg_header":    "#0E0F12",
    "bg_input":     "#2C2F37",
    "bg_hover":     "#31343D",

    # 强调色 —— 朱红
    "accent_primary": "#D8392B",
    "accent_hover":   "#E85444",

    # 次要按钮
    "btn_secondary":       "#34373F",
    "btn_secondary_hover": "#434650",

    # 文字
    "text_primary":   "#ECEDF0",
    "text_secondary": "#9AA0AC",
    "text_muted":     "#6B7280",
    "text_on_dark":   "#ECEDF0",
    "text_on_accent": "#FFFFFF",

    # 边框
    "border_light":  "#34373F",
    "border_medium": "#434650",

    # 状态色
    "success": "#4CAF7D",
    "warning": "#D9A93F",
    "error":   "#E05252",
}

FONTS = {
    "heading_lg": ("Microsoft YaHei UI", 16, "bold"),
    "heading_md": ("Microsoft YaHei UI", 13, "bold"),
    "body_md":    ("Microsoft YaHei UI", 11),
    "body_sm":    ("Microsoft YaHei UI", 10),
    "mono_md":    ("Consolas", 11),
    "label":      ("Microsoft YaHei UI", 9, "bold"),
}

PAD = {
    "xs": 4,
    "sm": 8,
    "md": 12,
    "lg": 16,
    "xl": 24,
}
