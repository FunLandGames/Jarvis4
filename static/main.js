document.getElementById("askBtn").addEventListener("click", async () => {
    const question = document.getElementById("question").value;
    if (!question) return alert("Please type a question!");

    const res = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ question })
    });

    const data = await res.json();
    document.getElementById("answer").innerText = data.answer;

    // Speak answer
    responsiveVoice.speak(data.answer, "Hindi Male");
});
