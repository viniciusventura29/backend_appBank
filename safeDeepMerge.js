function safeDeepMerge(target, src) {
  const banned = ["__proto__", "constructor", "prototype"];
  for (const key in src) {
    if (!Object.prototype.hasOwnProperty.call(src, key)) continue;
    if (banned.includes(key)) continue; // bloqueia chaves perigosas
    const val = src[key];
    if (val && typeof val === "object" && !Array.isArray(val)) {
      if (!target[key] || typeof target[key] !== "object") target[key] = {};
      safeDeepMerge(target[key], val);
    } else {
      target[key] = val;
    }
  }
}

