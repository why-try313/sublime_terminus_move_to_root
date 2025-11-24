import os
import sublime
import sublime_plugin

HOOK_TIMEOUT = 50
TERMINUS_ROOT_KEY = "TERMINUS_ROOT"

def get_last_terminus_view(window):
    for v in reversed(window.views()):
        if v.settings().get("terminus_view"):
            return v
    return None

class SaveTerminusSaveListener(sublime_plugin.EventListener):
    def on_post_window_command(self, window, command, args):
        if command == "terminus_open":
            sublime.set_timeout(lambda: self.load_last_dir(window), HOOK_TIMEOUT)


    def get_env_value(self, env_path, key):
        if not os.path.exists(env_path):
            return None
        with open(env_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    k, v = line.split("=", 1)
                    if k.strip() == key:
                        return v.strip()
        return None

    def load_last_dir(self, window):
        project_data = window.project_data()
        if not project_data or "folders" not in project_data:
            print("No project folders found.")
            return
        project_folder = project_data["folders"][0]["path"]
        env_file_path = os.path.join(project_folder, ".env")
        terminus_root = self.get_env_value(env_file_path, TERMINUS_ROOT_KEY).strip('"')
        term_view = get_last_terminus_view(window)

        if not term_view:
            return

        term_view_path = term_view.settings().get("terminus_view.args").get("cwd")
        if terminus_root and term_view_path and terminus_root in term_view_path:
            print("Moving Terminus to %s (%s)" % (TERMINUS_ROOT_KEY, terminus_root))
            window.run_command("terminus_send_string", {"string": "cd {}\nclear\n".format(terminus_root), "tag": None, "visible_only": False})
