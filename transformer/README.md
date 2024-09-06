# Matemática da Arquitetura Transformer na Análise e Forecast de Séries Temporais

O modelo Transformer, introduzido no artigo "Attention is All You Need" pelos pesquisadores do Google, revolucionou a maneira como as sequências de dados são processadas, particularmente na área de Processamento de Linguagem Natural (PLN).

**Entrada de dados:** As sequências de entrada são primeiro convertidas em vetores usando uma camada de incorporação (embedding). Isso permite que o modelo trate as palavras (ou qualquer outro tipo de unidade de dados) como representações densas em um espaço vetorial de alta dimensão. Além disso, o Transformer adiciona uma codificação posicional a esses vetores para incorporar a informação sobre a posição de cada elemento na sequência.

**Mecanismo de Atenção:** O coração do Transformer é o mecanismo de atenção. Este mecanismo permite que o modelo pondere a importância de diferentes partes da sequência de entrada ao processar um determinado elemento. A atenção multi-cabeça repete esse processo várias vezes em paralelo, cada uma focando em diferentes subespaços das representações vetoriais.

**Blocos de Encoder e Decoder:** O encoder processa a sequência de entrada em um conjunto de representações vetoriais e cada bloco do encoder contém uma subcamada de atenção seguida de uma rede neural feedforward. A saída de cada subcamada passa por uma normalização de camada e, em seguida, é enviada à próxima subcamada. O decoder funciona de maneira similar, mas com uma camada de atenção adicional que permite focar nas saídas do encoder.

**Conexões Residuais e Normalização:** Para facilitar o treinamento de redes profundas, cada subcamada no encoder e no decoder tem uma conexão residual em torno dela seguida por uma normalização de camada. Isso significa que a saída de cada subcamada é somada à sua entrada antes de ser passada à próxima subcamada, ajudando a mitigar o problema do desvanecimento do gradiente em redes profundas.

**Saída Final:** No final do decoder, a saída passa por uma camada linear e, em seguida, por uma função softmax para gerar as probabilidades da próxima palavra na sequência. Essas probabilidades são usadas para selecionar a saída final, seja durante o treinamento ou na geração de texto.
