
async function runAnalysis(){
document.getElementById("status").innerText="Running analysis..."

const res = await fetch("/run-analysis",{method:"POST"})
const data = await res.json()

document.getElementById("status").innerText="Analysis complete"

document.getElementById("chatgpt").innerText=data.ai.chatgpt.summary
document.getElementById("grok").innerText=data.ai.grok.summary
document.getElementById("gemini").innerText=data.ai.gemini.summary

drawConsensus(data.consensus)

}

function drawConsensus(scores){

const ctx=document.getElementById("consensusChart").getContext("2d")

new Chart(ctx,{
type:"bar",
data:{
labels:["ChatGPT","Grok","Gemini"],
datasets:[{
label:"Risk Score",
data:[scores.chatgpt,scores.grok,scores.gemini],
backgroundColor:["#4ade80","#60a5fa","#fbbf24"]
}]
}
})

}
