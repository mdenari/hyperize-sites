export const config = {
  matcher: '/apresentacoes/:path*',
};

export default async function middleware(req) {
  const url = new URL(req.url);
  const path = url.pathname;
  
  let presentations = [];
  try {
    const dbUrl = new URL('/presentations.json', req.url);
    const res = await fetch(dbUrl);
    if (res.ok) {
      presentations = await res.json();
    }
  } catch (e) {
    console.error("Failed to load presentations db", e);
  }

  const parts = path.split('/');
  const currentSlug = parts[2];

  if (!currentSlug) return;

  const presentation = presentations.find(p => p.slug === currentSlug);

  if (presentation && presentation.protected) {
    const basicAuth = req.headers.get('authorization');

    if (basicAuth) {
      const authValue = basicAuth.split(' ')[1];
      const [user, pwd] = atob(authValue).split(':');

      if (pwd === process.env.SITE_PASSWORD) {
        return; // Continue to page
      }
    }

    return new Response('Access Denied: Senha da Diretoria Necessária', {
      status: 401,
      headers: {
        'WWW-Authenticate': 'Basic realm="ELabs Secure Area"',
      },
    });
  }
}