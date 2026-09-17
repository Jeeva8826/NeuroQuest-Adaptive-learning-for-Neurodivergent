import { test, expect } from '@playwright/test';
import { injectAxe, checkA11y } from 'axe-playwright';

test.describe('NeuroQuest Accessibility Audit', () => {
  test('Home page meets WCAG 2.2 AA standards', async ({ page }) => {
    // Navigate to the main application hub
    await page.goto('http://localhost:5173/home-new');
    
    // Inject the axe-core library into the page
    await injectAxe(page);
    
    // Run the accessibility audit targeting WCAG 2.1 / 2.2 AA guidelines
    await checkA11y(page, null, {
      axeOptions: {
        runOnly: {
          type: 'tag',
          values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']
        }
      },
      detailedReport: true,
      detailedReportOptions: { html: true }
    });
  });

  test('Adaptive Lesson UI meets WCAG 2.2 AA standards', async ({ page }) => {
    await page.goto('http://localhost:5173/lesson');
    await injectAxe(page);
    
    await checkA11y(page, null, {
      axeOptions: {
        runOnly: {
          type: 'tag',
          values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa']
        }
      }
    });
  });
});
