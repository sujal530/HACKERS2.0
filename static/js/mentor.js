const chatBox = document.getElementById("chatBox");
const question = document.getElementById("question");
const sendBtn = document.getElementById("sendBtn");
const newChat = document.getElementById("newChat");

function scrollBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}

function addUserMessage(message) {

    chatBox.innerHTML += `
    <div class="message user">
        <div class="avatar">👤</div>
        <div class="bubble">${message}</div>
    </div>
    `;

    scrollBottom();
}

function addAIMessage(message) {

    chatBox.innerHTML += `
    <div class="message ai">
        <div class="avatar">🤖</div>
        <div class="bubble">${marked.parse(message)}</div>
    </div>
    `;

    scrollBottom();
}

async function askAI() {

    const text = question.value.trim();

    if (text === "") return;

    addUserMessage(text);

    question.value = "";

    chatBox.innerHTML += `
    <div class="message ai" id="loading">
        <div class="avatar">🤖</div>
        <div class="bubble">
            Thinking...
        </div>
    </div>
    `;

    scrollBottom();

    try {

        const response = await fetch("/ask_ai", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: text
            })

        });

        const data = await response.json();

        document.getElementById("loading").remove();

        addAIMessage(data.answer);

    }

    catch (error) {

        document.getElementById("loading").remove();

        addAIMessage("Something went wrong.");

    }

}

sendBtn.addEventListener("click", askAI);

question.addEventListener("keydown", function(e){

    if(e.key==="Enter" && !e.shiftKey){

        e.preventDefault();

        askAI();

    }

});

newChat.addEventListener("click", async()=>{

    await fetch("/clear_chat",{

        method:"POST"

    });

    location.reload();

});