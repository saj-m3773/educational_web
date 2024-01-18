function addProductToOrder(productId) {

    $.get('/order/add-to-order?product_id=' + productId).then(res => {
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed &&  res.status === 'not_auth') {
                window.location.href = 'User/';
            }if (result.isConfirmed &&  res.status === 'success'){
                window.location.href = '/Dashboard/user-basket';
            }
        })
    });
}


function removeOrderDetail(detailId) {
    $.get('/Dashboard/remove-order-detail?detail_id=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}