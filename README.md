<h1>Projeto de Gerenciamento de Usuários</h1>

<h2>Descrição do Projeto</h2>
<p>Este projeto é uma aplicação para gerenciamento de usuários, oferecendo funcionalidades essenciais como cadastro, login e alteração de senha. Para sua interface gráfica, ele utiliza o framework <code>customtkinter</code>, proporcionando uma experiência de usuário intuitiva e amigável. O gerenciamento do banco de dados <code>Postgesql</code> é realizado por meio do poderoso <code>SQLAlchemy</code>, garantindo eficiência e robustez.</p>
<p>Este projeto foi desenvolvido como parte de um desafio Python Full, onde os participantes foram desafiados a criar um sistema de login completo. Optei por ir além e implementar uma interface gráfica utilizando o Tkinter, adicionando novas funcionalidades ao sistema. Além das operações tradicionais de login e cadastro, introduzi recursos avançados como a atualização de senha e a opção de recuperar a senha enviando um código de verificação por email, fornecendo uma camada adicional de segurança e conveniência para os usuários.</p>

<h2>Funcionalidades Principais</h2>
<ul>
<li>Cadastro de novos usuários.</li>
<li>Autenticação de usuários.</li>
<li>Atualização de senha.</li>
<li>Recuperar senha com envio de código de verificação por email.</li>
</ul>

<h2>Configuração e Instalação</h2>

<h3>Requisitos</h3>
<ul>
<li>Python 3.8 ou superior</li>
<li>Pacotes listados em <code>requirements.txt</code></li>
</ul>

<h3>Passos de Instalação</h3>
<ol>
<li>Clone o repositório:
<h4>HTTPS</h4>
<pre><code>git clone &lt;https://github.com/ANDERSONGUASSU/Projeto-Login.git&gt;</code></pre>
<h4>SSH</h4>
<pre><code>git clone &lt;git@github.com:ANDERSONGUASSU/Projeto-Login.git&gt;</code></pre>
</li>
<li>Crie um ambiente virtual:
<pre><code>python -m venv venv
source venv/bin/activate # ou .\venv\Scripts\activate no Windows</code></pre>
</li>
<li>Instale as dependências:
<pre><code>pip install -r requirements.txt</code></pre>
</li>
<li>Crie um arquivo <code>.env</code> na raiz do projeto com as seguintes variáveis:
<pre><code>DB_MENAGER=&lt;seu_gerenciador_de_banco_de_dados&gt;
DB_USER=&lt;seu_usuario_de_banco_de_dados&gt;
PASSWORD=&lt;sua_senha_de_banco_de_dados&gt;
HOST=&lt;seu_host_de_banco_de_dados&gt;
DB=&lt;nome_do_seu_banco_de_dados&gt;
EMAIL=&lt;seu_email_para_envio_de_codigo_de_verificacao&gt;
EMAIL_PASSWORD=&lt;token_de_senha_gerado&gt;</code></pre>
</li>
<li>Gere um token de senha para seu email:
<ol>
<li>Vá para <a href="https://security.google.com/settings/security/apppasswords">Google App Passwords</a>.</li>
<li>Selecione a opção “Outro” para definir um nome para seu projeto.</li>
<li>Gere o token e use-o na variável <code>EMAIL_PASSWORD</code>.</li>
</ol>
</li>
<li>Inicialize o banco de dados:
<pre><code>python -c 'from models import Base, engine; Base.metadata.create_all(engine)'</code></pre>
</li>
</ol>

<h2>Uso</h2>

<ol>
<li>Para iniciar a aplicação, execute:
<pre><code>python app.py</code></pre>
</li>
<li>Utilize a interface gráfica para:
<ul>
<li>Registrar novos usuários.</li>
<li>Fazer login.</li>
<li>Alterar senha.</li>
<li>Recuperar senha esquecida.</li>
</ul>
</li>
</ol>

<h2>Estrutura do Projeto</h2>

<ul>
<li><strong>view/</strong>
<ul>
<li><code>registerView.py</code>: Tela de cadastro de novos usuários.</li>
<li><code>changePassword.py</code>: Tela de alteração de senha.</li>
<li><code>mainView.py</code>: Tela principal após login.</li>
<li><code>forgotPassworView.py</code>: Tela para recuperar senha esquecida.</li>
</ul>
</li>
<li><strong>controller/</strong>
<ul>
<li><code>controllerUser.py</code>: Controlador para operações com usuários.</li>
</ul>
</li>
<li><strong>models/</strong>
<ul>
<li><code>models.py</code>: Definições do banco de dados e do modelo de usuário.</li>
</ul>
</li>
<li><strong>config/</strong>
<ul>
<li>Configurações e URL do banco de dados.</li>
</ul>
</li>
</ul>

<h2>Contribuição</h2>

<ol>
<li>Faça um fork do projeto e ajude-me a melhorá-lo.</li>
<li>Crie uma branch para sua feature (<code>git checkout -b feature/AmazingFeature</code>).</li>
<li>Commit suas mudanças (<code>git commit -m 'Add some AmazingFeature'</code>).</li>
<li>Push para a branch (<code>git push origin feature/AmazingFeature</code>).</li>
<li>Abra um Pull Request.</li>
</ol>

<h2>Contato</h2>

<p>Para suporte ou contribuições, entre em contato através do email: <code>andersonguassu@hotmail.com</code></p>

