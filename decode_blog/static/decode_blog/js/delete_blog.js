// document.addEventListener('DOMContentLoaded', function() {
//     const deleteButtons = document.querySelectorAll('.delete-blog-button');
  
//     deleteButtons.forEach(button => {
//       button.addEventListener('click', function() {
//         const blogId = this.getAttribute('data-blog-id');
//         if (confirm('Вы уверены, что хотите удалить этот блог?')) {
//           fetch(`/decode_blog/delete/${blogId}/`, {
//             method: 'DELETE',
//             headers: {
//               'X-CSRFToken': getCookie('csrftoken')
//             }
//           })
//           .then(response => response.json())
//           .then(data => {
//             if (data.success) {
//               location.reload();
//             } else {
//               alert('Ошибка при удалении блога.');
//             }
//           });
//         }
//       });
//     });
  
//     // Функция для получения значения CSRF-токена из куков
//     function getCookie(name) {
//       let cookieValue = null;
//       if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//           const cookie = cookies[i].trim();
//           if (cookie.substring(0, name.length + 1) === (name + '=')) {
//             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//             break;
//           }
//         }
//       }
//       return cookieValue;
//     }
//   });
  