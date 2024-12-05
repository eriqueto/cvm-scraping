Fundos de Investimento - Extração e Análise de Dados

Este repositório contém um script em Python para download, extração e análise de dados sobre Fundos de Investimento (FI) disponibilizados pela CVM. O objetivo é obter informações financeiras mais recentes relacionadas a uma lista específica de CNPJs fornecida. Este projeto foi inspirado pela curiosidade e interesse em analisar os fundos de investimento de meu avô.
📋 Funcionalidades

    Download e extração de dados: Realiza o download automático do arquivo mais recente disponível no formato .zip e extrai os dados.
    Filtragem por CNPJs: Processa o arquivo extraído para buscar dados relacionados a uma lista específica de CNPJs.
    Análise dos dados: Filtra e organiza as informações financeiras mais recentes, como patrimônio líquido, captação no dia, resgate no dia, entre outros.
    Exportação para Excel: Salva os resultados finais em um arquivo Excel (resultado_fundos.xlsx) para análise posterior.

📂 Estrutura do Projeto

.
├── data/                       # Diretório onde os arquivos extraídos e gerados serão armazenados
├── script.py                   # Código principal do projeto
├── README.md                   # Descrição do projeto
└── requirements.txt            # Dependências do projeto

🛠️ Como Executar

    Clone este repositório:

git clone https://github.com/seu-usuario/fundos-investimento.git
cd fundos-investimento

Instale as dependências: Certifique-se de que você tem o Python instalado. Em seguida, instale as bibliotecas necessárias:

pip install -r requirements.txt

Execute o script:

    python script.py

    O script fará o download dos dados mais recentes disponíveis, filtrará as informações e salvará os resultados no arquivo data/resultado_fundos.xlsx.

🗂️ Exemplo de Resultados

O arquivo Excel gerado conterá as seguintes colunas:

    Data da Informação: Data da última atualização das informações financeiras.
    Total da Carteira: Valor total da carteira.
    Quota: Valor da cota.
    Patrimônio Líquido: Valor do patrimônio líquido.
    Captação no Dia: Valor captado no dia.
    Resgate no Dia: Valor resgatado no dia.
    N total de Cotistas: Número total de cotistas.

📝 Observações

    A lista de CNPJs utilizada é pessoal. Por favor, substitua a lista no código (cnpj_list) com os CNPJs de interesse para realizar sua análise.
    Este script depende dos dados disponibilizados pela CVM. Caso não existam dados para o mês atual, ele tentará buscar o arquivo do mês anterior.

📈 Futuras Melhorias

    Adicionar suporte para múltiplas listas de CNPJs com diferentes arquivos de saída.
    Implementar testes unitários para verificar a integridade do processamento dos dados.
    Criar uma interface gráfica para facilitar a execução do script.

🛡️ Licença

Este projeto é de uso pessoal e educativo. Sinta-se à vontade para explorar e adaptar, mas cite este repositório como fonte.

📧 Contato: Caso tenha dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou me contatar diretamente. 😊
