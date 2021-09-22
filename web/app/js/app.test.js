/**
 * @jest-environment jsdom
 */

import { sum } from './registration-script';

describe('App Suite', () => {
  it('should add 2 + 2', () => {
    expect(sum(2, 2)).toBe(4);
  });
});
