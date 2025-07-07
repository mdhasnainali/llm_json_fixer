<div align="center">

# 🧠 LLM JSON Fixer

<h3>Robust Utility to Fix Messy AI-Generated JSON</h3>

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/llm_json_fixer?style=for-the-badge\&color=orange)](https://pypi.org/project/llm_json_fixer/)
</div>

---

<div align="center">

### 🧰 Fix JSON Chaos with One Line

A fast and lightweight fixer for malformed JSON often returned by ChatGPT, Claude, and other LLMs.

</div>

---

## 🚀 Features

* 🔧 **Fixes Quotes, Commas, Brackets, Booleans** and more
* 🎯 **Extracts JSON** from noisy text blobs
* 🧼 **Handles Markdown code blocks**
* ⚡ **Blazing Fast** & Zero Dependencies
* 📦 **Clean API** – One function, multiple options

---

## 📦 Installation

```bash
pip install llm_json_fixer
```

---

## 🧪 Usage

### ✅ Basic

```python
from llm_json_fixer import fix_json

result = fix_json("{'name': 'John', 'age': 30}")
print(result)
# {'name': 'John', 'age': 30}
```

### 🔍 Detailed Output

```python
fix_json('{"name": "John", "age": 30,}', return_dict=True)
# {
#     'success': True,
#     'data': {'name': 'John', 'age': 30},
#     'error': None,
#     'fixes_applied': [...]
# }
```

### 🔐 Validate JSON

```python
from llm_json_fixer import is_valid_json

is_valid_json('{"name": "John"}')   # True
is_valid_json("{'name': 'John'}")     # False
```

---

## 🛠️ Fixes Applied

| 🔥 Issue              | ✅ Fixed To           |
| --------------------- | -------------------- |
| 'Single quotes'       | "Double quotes"      |
| Trailing commas       | Removed              |
| Missing commas        | Inserted             |
| Python booleans/nulls | JSON equivalents     |
| Unquoted keys         | Properly quoted      |
| Markdown code blocks  | Removed cleanly      |
| Unbalanced brackets   | Balanced             |
| Multiple commas       | Cleaned up           |
| Unclosed strings      | Closed automatically |
| Extra text            | JSON extracted       |

---

## 🧾 Examples

````python
fix_json("{'name': 'John'}")                        # → {'name': 'John'}
fix_json('{"name": "John", "age": 30,}')          # → {'name': 'John', 'age': 30}
fix_json('{name: "John", age: 30}')                # → {'name': 'John', 'age': 30}
fix_json('{"active": True, "data": None}')         # → {'active': True, 'data': None}
fix_json('```json\n{"name": "John"}\n```')       # → {'name': 'John'}
fix_json('Result: {"name": "John"}')               # → {'name': 'John'}
````

---

## 🔄 Return Types

### ▶️ Simple Mode

```python
result = fix_json(json_str)
# → dict | list | None
```

### ▶️ Detailed Mode

```python
result = fix_json(json_str, return_dict=True)
# → {
#   'success': bool,
#   'data': dict | list,
#   'error': str | None,
#   'fixes_applied': List[str]
# }
```

---

## 🎯 Use Cases

* 🤖 **LLM Outputs** – Fix malformed responses from ChatGPT, Claude, Mistral
* 🔗 **APIs** – Sanitize broken payloads
* 📊 **Log Files** – Normalize JSON entries
* 🕷️ **Scraped Data** – Fix malformed embedded JSON
* ⚙️ **Config Repair** – Recover broken config files

---

## 📄 License

MIT License. See [LICENSE](./LICENSE) file for more info.

---

## 🤝 Contributing

Pull Requests and feature suggestions are welcome!

* 📂 Fork the repo
* 🔨 Create a branch
* ✅ Add your changes + tests
* 📩 Submit a PR

---

## 🆘 Support

Found a bug or need help? [Create an Issue](https://github.com/mdhasnainali/llm_json_fixer/issues)

---

<div align="center">

Made with ❤️ by Md. Hasnain Ali.

</div>
