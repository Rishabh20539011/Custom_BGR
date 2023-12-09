import React from 'react';
import '@/styles/globals.css';

export default function App({ Component, pageProps }) {
  React.useEffect(() => {
    // Logging the NEXT_PUBLIC_BACKEND_URL environment variable
    console.log('Backend URL:', process.env.NEXT_PUBLIC_URL);
  }, []);

  return <Component {...pageProps} />;
}
