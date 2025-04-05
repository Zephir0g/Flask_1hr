document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("noteForm");
    const notesList = document.getElementById("notesList");

    function renderNotes(notes) {
        notesList.innerHTML = "";
        if (notes.length === 0) {
            notesList.innerHTML = "<p>No notes yet.</p>";
            return;
        }

        notes.forEach(note => {
            const div = document.createElement("div");
            div.innerHTML = `
                <h3>${note.title}</h3>
                <p>${note.content}</p>
                <small>Created: ${new Date(note.created_at).toLocaleString()}</small><br />
                <button data-id="${note.id}">Delete</button>
                <hr />
            `;
            notesList.appendChild(div);
        });

        document.querySelectorAll("button[data-id]").forEach(btn => {
            btn.addEventListener("click", function () {
                const id = this.getAttribute("data-id");
                fetch(`/notes/${id}`, { method: "DELETE" })
                    .then(() => loadNotes());
            });
        });
    }

    function loadNotes() {
        fetch("/notes")
            .then(res => res.json())
            .then(data => renderNotes(data.notes))
            .catch(err => {
                notesList.innerHTML = "<p style='color: red;'>Failed to load notes.</p>";
                console.error(err);
            });
    }

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const title = document.getElementById("title").value.trim();
        const content = document.getElementById("content").value.trim();

        if (!title || !content) return;

        fetch("/notes", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ title, content })
        })
            .then(() => {
                form.reset();
                loadNotes();
            });
    });

    loadNotes();
});
