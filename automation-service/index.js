import express from 'express';
import cors from 'cors';
import { launch } from 'puppeteer-extra';
import StealthPlugin from 'puppeteer-extra-plugin-stealth';

const app = express();
app.use(cors());
app.use(express.json());

puppeteerExtra.use(StealthPlugin());

app.post('/login-scrape', async (req, res) => {
  const { username, password } = req.body;

  try {
    const browser = await launch({ headless: true, args: ['--no-sandbox'] });
    const page = await browser.newPage();

    await page.goto('https://onlyfans.com', { waitUntil: 'networkidle2' });
    await page.type('input[name="email"]', username);
    await page.type('input[name="password"]', password);
    await page.click('button[type="submit"]');

    await page.waitForTimeout(3000);
    const screenshot = await page.screenshot({ encoding: 'base64' });

    const url = page.url();
    const title = await page.title();
    await browser.close();

    res.json({
      status: 'success',
      url,
      title,
      screenshot_base64: screenshot
    });
  } catch (err) {
    res.status(500).json({ status: 'error', message: err.message });
  }
});

const PORT = process.env.PORT || 8001;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
