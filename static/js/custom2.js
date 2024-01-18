function sendProductComment(articleId) {
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    console.log(parentId);
    $.get('/propduct/add_product_comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId
    }).then(res => {
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        })
    });
}
function fillParentId(parentId) {

    $('#parent_id').val(parentId)
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"})

}

function sendArticleComment(articleId) {
    var comment = $('#commentTextA').val();
    var parentId = $('#parent_idA').val();
    console.log(parentId);
    $.get('/artical/add_articale_comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId

    }).then(res => {
      Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        })
    });
}
function fillParentIdA(parentId) {

    $('#parent_idA').val(parentId)
    document.getElementById('comment_formA').scrollIntoView({behavior: "smooth"})

}

