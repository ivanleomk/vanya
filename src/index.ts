import { Bot } from "grammy";

const token = process.env.TELEGRAM_BOT_TOKEN;

if (!token) {
  console.error("TELEGRAM_BOT_TOKEN is required");
  process.exit(1);
}

const bot = new Bot(token);

bot.command("start", (ctx) => ctx.reply("Hello! I'm Vanya 🤖"));

bot.on("message:text", (ctx) => {
  ctx.reply(`You said: ${ctx.message.text}`);
});

bot.start();
console.log("Vanya is running...");
