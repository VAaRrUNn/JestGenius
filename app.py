import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
tokenizer = AutoTokenizer.from_pretrained("fubuki119/JokesGPT")
model = AutoModelForCausalLM.from_pretrained("fubuki119/JokesGPT")


def generate(max_length):
    starting_text = "JOKE:"
    end_token = "<|endoftext|>"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    model.eval()
    with torch.no_grad():
        cur_ids = torch.tensor(tokenizer.encode("JOKE:")
                               ).unsqueeze(0).to(device)
        for i in range(max_length):
            outputs = model(cur_ids)
            logits, _ = outputs[:]
            softmax_logits = torch.softmax(logits[0, -1], dim=0)

            next_token_id = torch.multinomial(softmax_logits, 1).item()
            cur_ids = torch.cat([cur_ids, torch.ones(
                (1, 1)).long().to(device) * next_token_id], dim=1)
            if next_token_id == tokenizer.encode(end_token)[0]:
                joke = cur_ids.detach().cpu().tolist()
                joke = joke[0]
                return tokenizer.decode(joke[3:-1])
        joke = cur_ids.detach().cpu().tolist()
        joke = joke[0]
        return tokenizer.decode(joke[3:])

iface = gr.Interface(
    fn=generate,
    inputs=gr.Number(value=200, label="Maxlen"),
    outputs="text",
)
iface.launch(share=True, debug=True)
