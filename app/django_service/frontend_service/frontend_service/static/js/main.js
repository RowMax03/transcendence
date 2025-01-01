// Button actions

document.getElementById('sign-in-with-intra').onclick = function() {
    query("/auth/", `query SignInWithIntra {
      redirectUri
    }`).then(data => {
        const redirectUri = data.data.redirectUri;
        const urlParams = new URLSearchParams(new URL(redirectUri).search);
        const clientId = urlParams.get('client_id');
        const state = urlParams.get('state');
        window.location.href = `https://signin.intra.42.fr/oauth/authorize?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=code&state=${state}`;
        // Perform the next query or action here
        // Example: query("/next-endpoint/", `query NextQuery { clientId: "${clientId}", state: "${state}" }`);
    }).catch(error => {
        console.error("Error fetching data:", error);
    });
}

function generateStateToken() {
    const array = new Uint8Array(32); // 32 bytes = 256 bits of randomness
    window.crypto.getRandomValues(array);
    return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
}

const stateToken = generateStateToken();


async function query(uri, query) {
    const response = await fetch(uri, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ query }),
	});
	if (!response.ok) {
		throw new Error("Network response was not ok " + response.statusText);
	}
	return await response.json();
}