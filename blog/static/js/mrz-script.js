$(function () {
  let windowHeight = $(window).height();

  //当页面滑到底部自动发送请求
  $(window).on('scroll', function () {
    let contentBodyHeight = $(document.body).height();
    let windowScroll = $(window).scrollTop();

    let difference = Number(contentBodyHeight) - Number(windowHeight) - Number(windowScroll);
    let articleCount = $('#main').children('article').length;

    if (difference === 0) {
      $.ajax({
        url: 'article_list',
        data: {page: articleCount},
        success: function (data) {
          data.map(item => {
            $('#main').append(`<article class="post post-1">
              <header class="entry-header">
                <h1 class="entry-title">
                  <a href="/single/${item.id}">${item.title}</a>
                </h1>
                <div class="entry-meta">
                  <span class="post-category"><a href="#">Web Design</a></span>

                  <span class="post-date"><a href="#"><time class="entry-date" datetime="2012-11-09T23:15:57+00:00">February 2, 2013</time></a></span>

                  <span class="post-author"><a href="#">Albert Einstein</a></span>

                  <span class="comments-link"><a href="#">4 Comments</a></span>
                </div>
              </header>

              <div class="entry-content clearfix">
                <p>${item.content}</p>
                <div class="read-more cl-effect-14">
                  <a href="#" class="more-link">Continue reading <span class="meta-nav">→</span></a>
                </div>
              </div>
            </article>`)
          })
        }
      })
    }
  })
});