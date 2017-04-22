# To-do list para o bot do @grupos_ti
#### Recursos para a versão 0.1
* Sincronização do banco de dados do @grupos_ti com o tg-list.online
* Categorias
* Busca inline
* Função com as palavras-chave


OBS: maiores informações sobre essas funções estão no arquivo [especificacao.md](https://github.com/marcel-carvalho/bot-grupos_ti/blob/master/especificacao.md).
#### To-do list
1. **Exportar todos os grupos/canais do @grupos_ti**  
Uma maneira (provavelmente a mais viável) de fazer isso seria usando o [telegram-cli](https://github.com/vysheng/tg). Poderíamos criar um script nele, que percoresse todas as postagens do canal e salvasse o conteúdo delas (hashtags, link do grupo, descrição) em um banco de dados.
2. **Colocar esses grupos/canais no tg-list.online**  
Usaríamos a API do site (poderíamos automatizar isso, também).
3. **Terminar a função de categorias**  
Ela já está parcialmente feita pelo Pablo, só falta decidir o que será mostrado nela e ver se precisa mudar a parte visual.
4. **Consturir a busca inline**
5. **Construir a função com as palavras-chave**
6. **Realizar uma sincronização automática entre posts no @grupos_ti e no tg-list.online**  
Construir uma função no Bot para automaticamente enviar todo novo grupo postado no @grupos_ti para o tg-list.online
