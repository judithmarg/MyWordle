const WORDLE_BASE_URL = 'http://localhost:8012/wordle';

const defaultHeaders = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
};

export async function compareWord(idWordle) {
    const response = await fetch(`${WORDLE_BASE_URL}/compare/${idWordle}`, {
        method:'GET',
        headers:defaultHeaders,
    });
    return response.json();
}