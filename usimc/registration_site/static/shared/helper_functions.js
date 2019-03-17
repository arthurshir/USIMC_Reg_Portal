function replace_new_line_with_br(str) {
  return str.replace(/(?:\r\n|\r|\n)/g, '<br />');
}