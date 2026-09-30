async function callAPI(url, data) {
    const resultDiv = document.getElementById('result') || document.getElementById('output');
    if(resultDiv) resultDiv.innerHTML = "Loading... 🤖 Wait pannu da... AI yosikuthu...";

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        console.log(result);
        if(resultDiv) resultDiv.innerHTML = `<div style="white-space:pre-wrap; text-align:left; background:#f9f9ff; padding:20px; border-radius:12px; line-height:1.6;">${result.result.replace(/\*\*(.*?)\*\*/g, '<b>$1</b>').replace(/###/g, '<br><h3>')}</div>`;
    } catch (err) {
        if(resultDiv) resultDiv.innerHTML = `Error da: ${err.message}`;
        console.error(err);
    }
}
// Buttons
document.addEventListener('DOMContentLoaded', () => {
    const topicInput = document.querySelector('input[placeholder]') || document.querySelector('input');
    const levelSelect = document.querySelector('select');

    // Explain button
    const explainBtn = document.querySelectorAll('button')[5] || document.querySelector('button:last-child');
    if(explainBtn){
        explainBtn.onclick = () => {
            const topic = document.querySelector('input').value;
            const level = document.querySelector('select').value;
            callAPI('/explain', {topic: topic, level: level});
        }
    }
});