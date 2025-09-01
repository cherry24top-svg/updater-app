
import os
import zipfile
import hashlib

def sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def verify_patch():
    if not os.path.exists("patch.zip") or not os.path.exists("patch.sig") or not os.path.exists("manifest.json"):
        return False, "❌ Отсутствуют необходимые файлы для проверки."

    # Пример: проверка хэша (для демонстрации)
    hash_zip = sha256("patch.zip")
    with open("patch.sig", "r") as f:
        expected = f.read().strip()

    if hash_zip != expected:
        return False, "❌ Хэш не совпадает. SEC_HASH_MISMATCH"

    return True, "✅ Проверка пройдена"

def self_update(check_only=False):
    ok, msg = verify_patch()
    if not ok:
        return msg

    if check_only:
        return "✅ Обновление доступно и проверено"

    with zipfile.ZipFile("patch.zip", "r") as zip_ref:
        zip_ref.extractall(".")

    with open("version.txt", "w") as f:
        f.write("1.6.0")

    return "✅ Обновление установлено"
