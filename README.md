
# Furia API

API que integra o modelo de IA `compound-beta-mini` da Groq, permitindo inferência rápida e gratuita com suporte a ferramentas como busca na web e execução de código Python. Além desse chatbot, você pode acessar a outra parte desse projeto [aqui](https://github.com/moreira-m98/portal-furia), um portal para acompanhar todas as informações sobre o time de CS da Fúria.

---

## 🔧 Requisitos

- Python 3.8 ou superior
- Conta gratuita na [GroqCloud](https://console.groq.com)
- API Key da Groq configurada no arquivo `.env`

---

## 🚀 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/moreira-m98/furia-api.git
   cd furia-api


2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua API Key da Groq:

   ```
   GROQ_API_KEY=sua-api-key-aqui
   ```

   > 🔐 **Importante:** Nunca compartilhe sua API Key publicamente.

---

## 🧠 Sobre o modelo `compound-beta-mini`

O `compound-beta-mini` é um sistema de IA composto que utiliza modelos como Llama 4 Scout e Llama 3.3 70B para realizar tarefas de raciocínio, busca na web e execução de código. Ele é otimizado para baixa latência e é ideal para aplicações que requerem respostas rápidas.

**Características principais:**

- **Baixa latência:** Aproximadamente 275 tokens por segundo.
- **Suporte a ferramentas:** Busca na web via Tavily e execução de código Python via E2B.
- **Limitações gratuitas:** 200 requisições por dia e 70.000 tokens por minuto.

Para mais detalhes, consulte a [documentação oficial da Groq](https://console.groq.com/docs/agentic-tooling/compound-beta-mini).

---

## 📝 Como obter sua API Key da Groq

1. Acesse o [GroqCloud](https://console.groq.com) e crie uma conta gratuita.
2. No painel de controle, vá até a seção de API Keys.
3. Gere uma nova API Key e copie o valor.
4. Adicione a chave ao arquivo `.env` conforme instruído acima.

---

## ⚙️ Executando a aplicação

Após configurar o ambiente, execute o script principal:

```bash
python main.py
```

Certifique-se de que o arquivo `.env` está corretamente configurado com sua API Key.

---


## 📬 Contato

Para dúvidas ou sugestões, entre em contato com [@moreira-m98](https://github.com/moreira-m98).

---

