$(document).ready(function() {
    $('#id_post_title').on('input', function() {
      let name = $(this).val();
      name = name.toLowerCase().replace(/đ/g, 'd');
      let slug = slugify(name).replace(/[^\w-]/g, '');
      $('#id_post_slug').val(slug);
    });
});