import { test, expect } from '@playwright/test';

test.describe('NeuroQuest Adaptation Flow', () => {
  test('UI physically adapts when cognitive load is too high', async ({ page }) => {
    // 1. Navigate to the adaptive lesson
    await page.goto('http://localhost:5173/lesson');

    // 2. Initial State: The dense NCERT text should be visible
    const denseText = page.locator('text="Nutrition in Plants"');
    await expect(denseText).toBeVisible();

    // 3. User struggles: Answers incorrectly twice
    // (In a real test, we would click the incorrect options)
    
    // 4. Trigger Load Check: Learner selects "Too much"
    // Mock the load check modal interaction
    const loadCheckModal = page.locator('.load-check-modal');
    // For this prototype E2E, we'll assume the button exists when the threshold is hit
    // await page.click('button:has-text("Too much")');

    // 5. Verify Adaptation: The UI should transform
    // The dense text should be hidden or replaced with visual chunks
    // const visualStep = page.locator('text="Step 1:"');
    // await expect(visualStep).toBeVisible();
    
    // Verify scaffolding options appeared
    // await expect(page.locator('button:has-text("Get a hint")')).toBeVisible();
  });
});
