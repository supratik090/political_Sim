import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

const isNativeApp = typeof window !== 'undefined' && (window.Capacitor?.isNativePlatform?.() || (window.location.protocol === 'https:' && window.location.hostname === 'localhost'));

// Register Service Worker for PWA support only in Web Production
if ('serviceWorker' in navigator) {
  if (isNativeApp) {
    // Clear any service workers and caches inside Native Android webview
    navigator.serviceWorker.getRegistrations().then((registrations) => {
      for (const registration of registrations) {
        registration.unregister();
      }
    });
    if (typeof caches !== 'undefined') {
      caches.keys().then((names) => {
        names.forEach((name) => caches.delete(name));
      });
    }
  } else if (import.meta.env.PROD) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js')
        .then((registration) => {
          console.log('PWA ServiceWorker registered successfully: ', registration.scope);
        })
        .catch((error) => {
          console.log('PWA ServiceWorker registration failed: ', error);
        });
    });
  } else {
    // Unregister active service worker in DEV mode to prevent caching stale dev chunks
    navigator.serviceWorker.getRegistrations().then((registrations) => {
      for (const registration of registrations) {
        registration.unregister();
      }
    });
  }
}

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
