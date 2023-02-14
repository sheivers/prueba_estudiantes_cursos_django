'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';
const RESOURCES = {
  "version.json": "5c5d406511b0d3f0e6139ee4659b6111",
"index.html": "100b0f30efa7ae81c7c234c3abc94dab",
"/": "100b0f30efa7ae81c7c234c3abc94dab",
"main.dart.js": "3019e14e84b2d8fa23f8db68cca19412",
"flutter.js": "1cfe996e845b3a8a33f57607e8b09ee4",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"icons/Icon-192.png": "ac9a721a12bbc803b44f645561ecb1e1",
"icons/Icon-maskable-192.png": "c457ef57daa1d16f64b27b786ec2ea3c",
"icons/Icon-maskable-512.png": "301a7604d45b3e739efc881eb04896ea",
"icons/Icon-512.png": "96e752610906ba2a93c65f8abe1645f1",
"manifest.json": "16d1d08b61d13156ace1bad0735b9f2c",
"assets/AssetManifest.json": "c05ae481c02be7a955aa04da2e5c0fa2",
"assets/NOTICES": "c8a7d8f2f05ae9b9eb042e7310442362",
"assets/FontManifest.json": "4ae1af717c2a91cac830572228078dc3",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "6d342eb68f170c97609e9da345464e5e",
"assets/fonts/MaterialIcons-Regular.otf": "e7069dfd19b331be16bed984668fe080",
"assets/assets/images/memo-10.png": "62f8409584af4a35d40aea0eb94ca43e",
"assets/assets/images/memo-11.png": "fecf1fcc78db2bc1dd426c782b43bd82",
"assets/assets/images/memo-13.png": "7d8ebca433c1b4033ebe8272eec40095",
"assets/assets/images/memo-12.png": "d7d9a5a6434e0a66ee6c19f8f53e11f7",
"assets/assets/images/memo-16.png": "57ee9ac4059d0fd0bb247a694f980ef1",
"assets/assets/images/memo-17.png": "447237208324bee2793b1bd421054a22",
"assets/assets/images/memo-29.png": "07976d3380ba89c689f814c3d2ed7865",
"assets/assets/images/memo-15.png": "cf8cd970bfb30451eef4a05f925fc3bd",
"assets/assets/images/memo-14.png": "8efacd34bf228099d9497fd49a7a09b7",
"assets/assets/images/memo-28.png": "678f341a18bf244daa9e20969874d0b9",
"assets/assets/images/memo-9.png": "1d9c0e53a8ba4488c851c441aceb347c",
"assets/assets/images/memo-8.png": "b3bc24b507f33d3341dfd42632f1b5ac",
"assets/assets/images/logoBase.png": "02f13bfee72f4a23b72550bce120082c",
"assets/assets/images/memo-1.png": "026c850abe8d9bf047665d26dbd0fe97",
"assets/assets/images/memo-3.png": "faa3679da474c9ab7e3610ffc077509b",
"assets/assets/images/memo-2.png": "54f3a09b124a22d6409e623fa0083b6c",
"assets/assets/images/memo-6.png": "46828b0a880e05d326dab0c06787d87f",
"assets/assets/images/memo-7.png": "8e4448551c7000a9b1689217c258661b",
"assets/assets/images/memo-5.png": "103fd5c72ce099a2e2d85a5565777471",
"assets/assets/images/memo-4.png": "2fb8fdc6819519957bba97e633ebb077",
"assets/assets/images/memo-31.png": "002af4bd78e742fadfce5021976cf8e7",
"assets/assets/images/memo-25.png": "5b1653540abc6e5c8a3ad2a7b3ffa51f",
"assets/assets/images/memo-19.png": "6f87227f59debf49339538d5f48747ad",
"assets/assets/images/memo-18.png": "13feea9b9962b94e4445c22fdeae5975",
"assets/assets/images/memo-24.png": "d116d74df68694587e8d87f40165f937",
"assets/assets/images/memo-30.png": "3ca64e8f1980e70a9b43af9f50465224",
"assets/assets/images/memo-26.png": "82f8835cfd6b3862ae04da38ac971dfe",
"assets/assets/images/memo-32.png": "fe92d7655f124c03e0800f007a29c4a4",
"assets/assets/images/memo-27.png": "c68defe945f559c5c01a69bf543fd00f",
"assets/assets/images/memo-23.png": "4eb0e9b8dca4c38e9ae30ddc47e8bb15",
"assets/assets/images/memo-22.png": "db170764285ed9fe02ca9617d6139cec",
"assets/assets/images/memo-20.png": "27020804b5b3b1e810267b77b5af5b60",
"assets/assets/images/memo-21.png": "fd38874ecdd8bda19d314b2dd07bd3d3",
"assets/assets/fonts/DMSans-Regular.ttf": "7c217bc9433889f55c38ca9d058514d3",
"assets/assets/fonts/DMSans-Medium.ttf": "24bfda9719b2ba60b94a0f9412757d10",
"assets/assets/fonts/DMSans-Bold.ttf": "b9cec5212f09838534e6215d1f23ed55",
"assets/assets/fonts/DMSerifDisplay-Regular.ttf": "25b39681f8cf94ad3cbfc6d25d9c0c4e",
"canvaskit/canvaskit.js": "97937cb4c2c2073c968525a3e08c86a3",
"canvaskit/profiling/canvaskit.js": "c21852696bc1cc82e8894d851c01921a",
"canvaskit/profiling/canvaskit.wasm": "371bc4e204443b0d5e774d64a046eb99",
"canvaskit/canvaskit.wasm": "3de12d898ec208a5f31362cc00f09b9e"
};

// The application shell files that are downloaded before a service worker can
// start.
const CORE = [
  "main.dart.js",
"index.html",
"assets/AssetManifest.json",
"assets/FontManifest.json"];
// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});

// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});

// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});

self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});

// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}

// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
