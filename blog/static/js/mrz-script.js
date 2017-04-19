$(function () {
  var contentBodyHeight = $(document.body).height();
  var windowHeight = $(window).height();

  //当页面滑到底部自动发送请求
  $(window).on('scroll', function () {
    var windowScroll = $(window).scrollTop();
    var difference = Number(contentBodyHeight) - Number(windowHeight) - Number(windowScroll);
    if (difference === 0) {
      console.log(111);
      $.ajax({
        url: 'article_list',
        data: {page: '6'},
        success: function (data) {
          var value = JSON.parse(data);
          console.log('value', value);
        }
      })
    }
  })
});