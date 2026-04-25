import os
import sys

def patch_gradio_client():
    try:
        import gradio_client.utils as utils
        file_path = utils.__file__
        print(f"Patching {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Patch get_type
        old_get_type = 'def get_type(schema: dict):'
        new_get_type = 'def get_type(schema: Any):'
        if old_get_type in content:
            content = content.replace(old_get_type, new_get_type)
            content = content.replace('    if "const" in schema:', '    if not isinstance(schema, dict):\n        return {}\n    if "const" in schema:')
            print("Patched get_type")
        
        # Patch _json_schema_to_python_type
        old_json_schema = 'if schema == {}:'
        new_json_schema = 'if schema == {} or not isinstance(schema, dict):'
        if old_json_schema in content:
            content = content.replace(old_json_schema, new_json_schema)
            print("Patched _json_schema_to_python_type")

        old_desc = 'if "json" in schema.get("description", {}):'
        new_desc = 'if isinstance(schema, dict) and "json" in schema.get("description", {}):'
        if old_desc in content:
            content = content.replace(old_desc, new_desc)
            print("Patched description check")
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Gradio Client patched successfully")
    except Exception as e:
        print(f"Failed to patch Gradio Client: {e}")

if __name__ == "__main__":
    patch_gradio_client()
