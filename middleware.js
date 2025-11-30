import { next } from '@vercel/edge';

export const config = {
  matcher: '/apresentacoes/:path*',
};

export default async function middleware(req) {
  const url = new URL(req.url);
  const path = url.pathname;
  
  // 1. Load Presentations DB
  // In Vercel Edge, we can import JSON directly or fetch it.
  // Assuming presentations.json is deployed to the root.
  // For simplicity and performance in this MVP, we will fetch it locally or import it if possible.
  // Note: Dynamic import of JSON in Edge might have caveats, so fetching is safer for dynamic content.
  
  let presentations = [];
  try {
    // Construct absolute URL to fetch the JSON from the same deployment
    const dbUrl = new URL('/presentations.json', req.url);
    const res = await fetch(dbUrl);
    if (res.ok) {
      presentations = await res.json();
    }
  } catch (e) {
    console.error("Failed to load presentations db", e);
  }

  // 2. Identify current presentation slug
  // Path format: /apresentacoes/{slug}/...
  const parts = path.split('/');
  // parts[0] is empty, parts[1] is 'apresentacoes', parts[2] is slug
  const currentSlug = parts[2];

  if (!currentSlug) return next();

  // 3. Check if protected
  const presentation = presentations.find(p => p.slug === currentSlug);

  if (presentation && presentation.protected) {
    // 4. Basic Auth Logic
    const basicAuth = req.headers.get('authorization');

    if (basicAuth) {
      const authValue = basicAuth.split(' ')[1];
      const [user, pwd] = atob(authValue).split(':');

      // Check against Environment Variable
      if (pwd === process.env.SITE_PASSWORD) {
        return next();
      }
    }

    // Request Auth
    return new Response('Access Denied: Senha da Diretoria Necessária', {
      status: 401,
      headers: {
        'WWW-Authenticate': 'Basic realm="ELabs Secure Area"',
      },
    });
  }

  return next();
}
