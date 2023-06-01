import minium
# .\cli.bat --auto "D:\学习app\CS304\CS304-project\Visiting-SUSTech-Frontend" --auto-port 9420
# 实际端口号为0
mini = minium.Minium({
    "project_path": "D:\\学习app\\CS304\\CS304-project\\Visiting-SUSTech-Frontend",
    "dev_tool_path": "D:\\学习app\\微信开发\\微信web开发者工具\\cli.bat",
})
print(mini.get_system_info())
