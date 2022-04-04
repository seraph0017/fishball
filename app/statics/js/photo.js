// external js: masonry.pkgd.js, imagesloaded.pkgd.js
$(document).ready(function () {
  $.fn.fileinputBsVersion = "3.3.7"; // if not set, this will be auto-derived
  // with plugin options
  $("#photoupload").fileinput({
    language: "zh",
    showUpload: false,
    previewFileType: "any",
  });
});
