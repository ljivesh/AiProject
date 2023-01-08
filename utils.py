from decouple import config

opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]

credentials = {
    'USERNAME': 'Jivesh',
    'email': config('EMAIL', default='xyz@gmail.com'),
    'password': config('PASSWORD', default='12345678')
}

intro = """
Hello I am MENMA, Meta Emulated Neuro Machine Automata. I was developed by three briliant college students named
Jivesh Lakhani, Vayam Kumar Gautam and Palak Garg.
"""