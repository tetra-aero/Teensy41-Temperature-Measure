from os.path import join, isfile

Import("env")

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-arduinoteensy")
patchflag_path = join(FRAMEWORK_DIR, ".patching-done")

# patch file only if we didn't do it before
#if not isfile(join(FRAMEWORK_DIR, ".patching-done")):
original_file = join(FRAMEWORK_DIR, "cores", "teensy4", "tempmon.c")
patched_file = join("patch", "1-tempmon-add-isr.patch")

# assert isfile(original_file) and isfile(patched_file)
env.Execute("rm -f %s" % (patchflag_path))
patch_source_file = join("patch", "packages", "framework-arduinoteensy", "cores", "teensy4", "tempmon.c")
env.Execute("diff %s %s | cat > %s" % (original_file, patch_source_file, patched_file))
#env.Execute("diff %s %s > %s 2>/dev/null" % (original_file, patch_source_file, patched_file))

env.Execute("patch %s %s" % (original_file, patched_file))
env.Execute("touch " + patchflag_path)


def _touch(path):
	with open(path, "w") as fp:
		fp.write("")

env.Execute(lambda *args, **kwargs: _touch(patchflag_path))
