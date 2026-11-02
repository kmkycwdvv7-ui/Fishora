'use strict';
// Only local app files are pre-cached. External weather/marine, map tiles and APIs are NEVER batch downloaded.
const CACHE='fishora-v2-1-20261102-2';
const APP=['./','./index.html','./styles.css','./data.js','./app.js','./icon.svg','./icon-192.png','./icon-512.png','./manifest.webmanifest'];
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(c=>c.addAll(APP)).then(()=>self.skipWaiting())));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('fishora-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{
  const req=event.request;
  if(req.method!=='GET')return;
  const u=new URL(req.url);
  if(u.origin!==self.location.origin)return; // Respect CDN/API/OSM server caching policies.
  event.respondWith(caches.match(req).then(cached=>{
    const network=fetch(req).then(response=>{if(response.ok){let copy=response.clone();caches.open(CACHE).then(c=>c.put(req,copy)).catch(()=>{});}return response;}).catch(()=>cached||Response.error());
    return cached||network;
  }));
});
