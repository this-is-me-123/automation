const puppeteer = require('puppeteer');

async function run() {
  const browser = await puppeteer.launch({
    headless: true, // change to false for debugging
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  const page = await browser.newPage();
  await page.goto('https://onlyfans.com/', { waitUntil: 'networkidle2' });

  // Example: fill form (adjust selectors if needed)
  await page.type('input[name="email"]', 'your-email@example.com');
  await page.type('input[name="password"]', 'yourpassword');
  await page.click('button[type="submit"]');

  await page.waitForTimeout(5000); // wait for page to settle
  const url = page.url();
  const content = await page.content();

  console.log({ url, snippet: content.slice(0, 500) });
  await browser.close();
}

run().catch(console.error);
