function openModal(activityId) {
        var modal = document.getElementById("myModal");
        var confirmRemoveButton = document.getElementById("confirmRemoveButton");

        modal.style.display = "block";

        confirmRemoveButton.onclick = function() {
            removeActivity(activityId);
            modal.style.display = "none";
        }
    }

    window.onclick = function(event) {
        var modal = document.getElementById("myModal");
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    function toggleActivity(id) {
        var activityDescription = document.getElementById(id).querySelector('p');
        var commentContainer = document.getElementById('comment-container-' + id.substr(-1));

        if (activityDescription.style.display === 'none' || activityDescription.style.display === '') {
            activityDescription.style.display = 'block';
            commentContainer.classList.add('active');
        } else {
            activityDescription.style.display = 'none';
            commentContainer.classList.remove('active');
        }
    }

    function removeActivity(id) {
        var activityContainer = document.getElementById(id);
        activityContainer.parentNode.removeChild(activityContainer);
    }

    function toggleSidebar() {
        var sidebar = document.querySelector('.sidebar');
        sidebar.classList.toggle('sidebar-visible');
    }