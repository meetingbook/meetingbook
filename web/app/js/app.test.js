import { sum } from './app.js';

describe('App Suite', () => {
  it('should add 2 + 2', () => {
    expect(sum(2, 2)).toBe(4);
  });
});
