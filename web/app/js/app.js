export function sum(a, b) {
  return a + b;
}

Array.from(document.querySelectorAll('.mdc-button')).forEach(
  (button) => new window.mdc.ripple.MDCRipple(button)
);

Array.from(document.querySelectorAll('.mdc-text-field')).forEach(
  (textField) => new window.mdc.textField.MDCTextField(textField)
);
