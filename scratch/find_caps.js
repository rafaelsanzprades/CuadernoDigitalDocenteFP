const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        file = path.join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) { 
            results = results.concat(walk(file));
        } else { 
            if (file.endsWith('.tsx') || file.endsWith('.ts')) {
                results.push(file);
            }
        }
    });
    return results;
}

const files = walk('frontend/src/components');
const titleCaseRegex = /(?:label=|placeholder=|title>|>[A-Za-z0-9\s/().,-]+<\/)[^>]*([A-ZÁÉÍÓÚ][a-zñáéíóú]+\s+[A-ZÁÉÍÓÚ][a-zñáéíóú]+)/g;

files.forEach(f => {
    const content = fs.readFileSync(f, 'utf8');
    const matches = [...content.matchAll(/(label="[^"]+"|label=\{[^}]+\}|<h[1-6][^>]*>[^<]+<\/h[1-6]>|<label[^>]*>[^<]+<\/label>|title:\s*"[^"]+")/g)];
    matches.forEach(m => {
        const text = m[0];
        // check if has at least two Capitalized words that are not acronyms
        const words = text.split(/\s+/);
        let capCount = 0;
        for (let w of words) {
            if (/^[A-ZÁÉÍÓÚ][a-zñáéíóú]+/.test(w) && w.length > 2) {
                capCount++;
            }
        }
        if (capCount >= 2) {
            console.log(`${f}: ${text}`);
        }
    });
});
