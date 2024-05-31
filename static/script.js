document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('downloadForm');
    const messageDiv = document.querySelector('.message');
    const spinner = document.querySelector('.spinner');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();

        messageDiv.textContent = '';
        spinner.style.display = 'inline-block';

        const formData = new FormData(form);
        const url = formData.get('url');

        try {
            const response = await fetch('/', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const responseData = await response.json();
            
            spinner.style.display = 'none';

            if (responseData.error_message) {
                messageDiv.textContent = responseData.error_message;
            } else {
                messageDiv.textContent = responseData.message;
                if (responseData.title && responseData.views) {
                    messageDiv.innerHTML += `<p>Title: ${responseData.title}</p><p>Views: ${responseData.views}</p>`;
                }
            }
        } catch (error) {
            spinner.style.display = 'none';
            messageDiv.textContent = 'An error occurred: ' + error.message;
        }
    });
});
