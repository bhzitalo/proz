const chatBox = document.getElementById("chatBox");

function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();

  if (message === "") return;

  // Mostra a mensagem do usuário
  const userMsg = document.createElement("div");
  userMsg.className = "user-message";
  userMsg.textContent = message;
  chatBox.appendChild(userMsg);

  input.value = "";

  // Resposta automática simulada da IA
  setTimeout(() => {
    const botMsg = document.createElement("div");
    botMsg.className = "bot-message";

    if (message.toLowerCase().includes("febre")) {
      botMsg.textContent = "Entendi. Além da febre, você está sentindo dor no corpo ou cansaço?";
    } else if (message.toLowerCase().includes("dor de cabeça")) {
      botMsg.textContent = "Obrigado pela informação. Você sente essa dor com frequência?";
    } else {
      botMsg.textContent = "Certo. Poderia me dizer há quanto tempo está com esses sintomas?";
    }

    chatBox.appendChild(botMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }, 1000);
}
