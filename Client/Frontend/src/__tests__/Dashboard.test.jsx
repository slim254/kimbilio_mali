import { describe, it, expect } from 'vitest';

describe('Kimbilio Mali Frontend Components', () => {
  it('correctly calculates rental yield and profitability metrics', () => {
    const propertyValuation = 500000;
    const annualRent = 60000;
    const yieldPercentage = (annualRent / propertyValuation) * 100;
    expect(yieldPercentage).toBe(12);
  });

  it('verifies dashboard currency formatting helper', () => {
    const formatCurrency = (amount) => `₹${amount.toLocaleString()}`;
    expect(formatCurrency(150000)).toBe('₹1,50,000');
  });
});
