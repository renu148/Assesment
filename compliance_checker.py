import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_compliance(text):
    matches = tool.check(text)
    return [{"message": m.message, "context": m.context, "offset": m.offset} for m in matches]

def fix_text(text):
    return tool.correct(text)
