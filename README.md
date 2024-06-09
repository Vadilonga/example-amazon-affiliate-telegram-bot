# Example Amazon Affiliate Telegram Bot

This repository contains a simple Telegram bot that utilizes the Amazon Affiliate Program API to automatically generate a product post on your Telegram channel. When an Amazon link is received, the bot fetches product information, an image, and generates a referenced link, then posts this on your Telegram channel.

## Features

- Receives Amazon product links
- Fetches product details using Amazon Affiliate Program API
- Posts the product post with information, image and affiliate link to a specified Telegram channel

## Prerequisites

- Python 3.7+
- Telegram bot token
- Amazon Affiliate Program API credentials (Access Key, Secret Key, Associate Tag)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Vadilonga/example-amazon-affiliate-telegram-bot.git
   cd example-amazon-affiliate-telegram-bot
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your variables:**

   Edit the file `constants.py` in the root of your project directory and add the following:

   ```plaintext
   TELEGRAM_TOKEN=your-telegram-bot-token
   CHANNEL_ID=your-telegram-channel-id
   AMAZON_ACCESS_KEY=your-amazon-access-key
   AMAZON_SECRET_KEY=your-your-amazon-secret-key
   PARTNER_TAG=your-amazon-associate-tag
   AMAZON_HOST=your-amazon-host
   AMAZON_REGION=your-amazon-region
   ```

5. **Run the bot:**

   ```bash
   python bot.py
   ```

## Usage

1. Create a bot on [@botfather](https://t.me/BotFather)
2. Create a channel on Telegram
3. Add the bot as an Administrator in the channel
4. Start your bot
5. Send an Amazon product link to the bot
6. The bot will fetch product details, generate an affiliate link, and post the product information on the specified Telegram channel

## Example

Send an Amazon product link like this:

```
https://www.amazon.com/dp/example-product-id
```

The bot will respond with a post in your Telegram channel that includes:

- Product title
- Product image
- Product price
- Product old price (if exist)
- Affiliate link to the product

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy coding! This code was developed exclusively for educational purposes for a university thesis, if you have any questions I will be happy to answer you!
