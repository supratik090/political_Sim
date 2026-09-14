export function isAndroidApp() {
  if (typeof window === 'undefined') return false;
  return (
    Boolean(window.Capacitor?.isNativePlatform()) ||
    window.Capacitor?.getPlatform() === 'android' ||
    (window.location.hostname === 'localhost' && window.location.port === '') ||
    import.meta.env.MODE === 'android' ||
    navigator.userAgent.includes('wv') ||
    window.location.search.includes('platform=android')
  );
}
