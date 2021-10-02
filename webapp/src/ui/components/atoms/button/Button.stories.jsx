import { Button } from '.';

export default {
  title: 'UI/Atoms/Button',
  component: Button,
  argTypes: {
    backgroundColor: { control: 'color' },
  },
};

const Template = (args) => <Button {...args}>Click me</Button>;

export const Primary = Template.bind({});
Primary.args = {
  primary: true,
};
