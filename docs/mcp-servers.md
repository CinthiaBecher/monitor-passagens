# Servidores MCP deste projeto

Este projeto pode usar servidores MCP (Model Context Protocol) para buscar voos
diretamente durante uma conversa com o Claude Code.

## google-flights (configurado em `.mcp.json`)

- **Fonte:** [google-flights-mcp](https://github.com/tistaharahap/google-flights-mcp)
- **O que faz:** busca voos, aeroportos e preços usando dados públicos do Google
  Flights, via a biblioteca `fast-flights`.
- **Requer API key?** Não — usa dados públicos, sem necessidade de cadastro
  ou credenciais.
- **Dependência:** [`uv`/`uvx`](https://docs.astral.sh/uv/) instalado
  localmente (Python 3.8+). O comando configurado (`uvx google-flights-mcp
  serve`) baixa e roda o pacote automaticamente na primeira execução.
- **Tools expostas:** `search_flights`, `find_airports`,
  `get_cheapest_flights`, `get_best_flights`, `get_server_status`.

### Como ativar

O Claude Code carrega os servidores listados em `.mcp.json` **no início da
sessão**. Depois de este arquivo existir no repositório:

1. Rode `claude` (CLI) dentro da pasta do projeto normalmente, ou abra uma
   nova sessão do Claude Code na web/app para este repositório.
2. Aprove o servidor `google-flights` quando solicitado (primeira vez).
3. As tools `search_flights`, `find_airports` etc. passam a aparecer
   disponíveis no chat.

> Uma sessão já em andamento não ganha automaticamente as tools de um MCP
> adicionado ao `.mcp.json` depois que ela começou — é necessário iniciar
> uma sessão nova para o servidor ser carregado.

### Alternativa já disponível sem instalação

Este ambiente também tem o conector **Kiwi.com** (`kiwi`) conectado,
que expõe `search-flight` e já funciona em qualquer sessão sem passos
extras — é o que usamos para pesquisas rápidas dentro do próprio chat.

### Outras opções descartadas

- [`all-flights-mcp`](https://github.com/shayben/all-flights-mcp): agrega
  ITA Matrix, Google Flights, Duffel e Skyscanner, mas exige credenciais
  pagas (Duffel, Skyscanner) que este projeto não possui.
