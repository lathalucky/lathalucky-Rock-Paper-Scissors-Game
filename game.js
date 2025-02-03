function playGame(userChoice) {
    const choices = ["rock", "paper", "scissors"];
    const computerChoice = choices[Math.floor(Math.random() * choices.length)];

    document.getElementById("user-choice").textContent = `You chose: ${userChoice}`;
    document.getElementById("computer-choice").textContent = `Computer chose: ${computerChoice}`;

    let result = "";
    if (userChoice === computerChoice) {
        result = "It's a tie!";
    } else if (
        (userChoice === "rock" && computerChoice === "scissors") ||
        (userChoice === "scissors" && computerChoice === "paper") ||
        (userChoice === "paper" && computerChoice === "rock")
    ) {
        result = "You win! 🎉";
    } else {
        result = "Computer wins! 😢";
    }

    document.getElementById("game-result").textContent = result;
}
