const buttons = document.querySelectorAll(".submit-btn");

buttons.forEach(button => {

    button.addEventListener("click", async function () {

        const challengeId = this.dataset.id;

        const card = this.closest(".challenge-card");

        const answer = card.querySelector(".answer").value.trim();

        const feedback = card.querySelector(".feedback");

        if (answer === "") {

            alert("Please write your solution first.");

            return;

        }

        feedback.classList.add("show");

        feedback.innerHTML = "🤖 Evaluating your solution...";

        try {

            const response = await fetch("/evaluate_challenge", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    challenge_id: challengeId,

                    answer: answer

                })

            });

            const data = await response.json();

            feedback.innerHTML = `

<h3>⭐ Score : ${data.score}/10</h3>

<p>${data.feedback}</p>

<p><strong>XP Earned : ${data.xp}</strong></p>

`;

        }

        catch {

            feedback.innerHTML =

            "Something went wrong.";

        }

    });

});