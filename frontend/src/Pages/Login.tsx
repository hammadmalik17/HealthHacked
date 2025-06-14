import { useState } from 'react';

export function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSignIn = (e:any) => {
        e.preventDefault();
        // Add your login logic here
        console.log('Login attempt:', { email, password });
    };

    const handleSignUp = () => {
        // Add navigation logic here
        console.log('Navigate to sign up');
    };

    return (
        <div className="min-h-screen flex">
            {/* Left side - Login Form */}
            <div className="flex-1 flex items-center justify-center bg-gray-50 px-8">
                <div className="w-full max-w-md space-y-8">
                    {/* Header */}
                    <div className="text-center">
                        <h2 className="text-3xl font-bold text-gray-900 mb-2">
                            Welcome Back 👋
                        </h2>
                        <p className="text-gray-600 text-sm leading-relaxed">
                            Today is a new day. It's your day. You shape it.<br />
                            Sign in to start managing your health journey.
                        </p>
                    </div>

                    {/* Login Form */}
                    <div className="space-y-6">
                        <div>
                            <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
                                Email
                            </label>
                            <input
                                id="email"
                                type="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                placeholder="Example@email.com"
                                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all duration-200"
                                required
                            />
                        </div>

                        <div>
                            <label htmlFor="password" className="block text-sm font-medium text-gray-700 mb-2">
                                Password
                            </label>
                            <input
                                id="password"
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                placeholder="At least 8 characters"
                                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all duration-200"
                                required
                            />
                            <div className="text-right mt-2">
                                <button className="text-sm text-blue-600 hover:text-blue-800 transition-colors bg-transparent border-none cursor-pointer">
                                    Forgot Password?
                                </button>
                            </div>
                        </div>

                        <button
                            onClick={handleSignIn}
                            className="w-full bg-slate-800 text-white py-3 px-4 rounded-lg font-medium hover:bg-slate-700 transition-colors duration-200 focus:ring-2 focus:ring-slate-500 focus:ring-offset-2 cursor-pointer border-none"
                        >
                            Sign In
                        </button>
                    </div>

                    {/* Divider */}
                    <div className="relative">
                        <div className="absolute inset-0 flex items-center">
                            <div className="w-full border-t border-gray-300"></div>
                        </div>
                        <div className="relative flex justify-center text-sm">
                            <span className="px-2 bg-gray-50 text-gray-500">Or</span>
                        </div>
                    </div>

                    {/* Social Login Buttons */}
                    <div className="space-y-3">
                        <button className="w-full flex items-center justify-center gap-3 py-3 px-4 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors duration-200 cursor-pointer">
                            <svg className="w-5 h-5" viewBox="0 0 24 24">
                                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                            </svg>
                            Sign in with Google
                        </button>
                        
                        <button className="w-full flex items-center justify-center gap-3 py-3 px-4 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors duration-200 cursor-pointer">
                            <svg className="w-5 h-5" fill="#1877F2" viewBox="0 0 24 24">
                                <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                            </svg>
                            Sign in with Facebook
                        </button>
                    </div>

                    {/* Sign Up Link */}
                    <div className="text-center">
                        <span className="text-gray-600 text-sm">Don't you have an account? </span>
                        <button 
                            onClick={handleSignUp}
                            className="text-blue-600 hover:text-blue-800 font-medium text-sm transition-colors bg-transparent border-none cursor-pointer"
                        >
                            Sign up
                        </button>
                    </div>

                    {/* Footer */}
                    <div className="text-center text-xs text-gray-400 mt-8">
                        © 2025 ALL RIGHTS RESERVED
                    </div>
                </div>
            </div>

            {/* Right side - Artistic Background */}
            <div className="flex-1 relative overflow-hidden bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
                {/* Decorative floral pattern */}
                <div className="absolute inset-0 opacity-30">
                    <div className="absolute top-10 left-10 text-6xl text-red-400 transform rotate-12">🌹</div>
                    <div className="absolute top-32 right-20 text-5xl text-orange-400 transform -rotate-45">🌺</div>
                    <div className="absolute top-64 left-32 text-7xl text-pink-400 transform rotate-45">🌸</div>
                    <div className="absolute bottom-40 right-16 text-8xl text-yellow-400 transform -rotate-12">🌻</div>
                    <div className="absolute bottom-20 left-20 text-6xl text-purple-400 transform rotate-30">🌷</div>
                    <div className="absolute top-1/2 left-1/4 text-4xl text-blue-400 transform -rotate-30">🌼</div>
                    <div className="absolute top-1/3 right-1/3 text-5xl text-green-400 transform rotate-60">🍃</div>
                    <div className="absolute bottom-1/3 left-1/2 text-3xl text-indigo-400 transform -rotate-15">🌿</div>
                </div>

                {/* Overlay pattern */}
                <div className="absolute inset-0 bg-black/40"></div>
                
                {/* Main content */}
                <div className="absolute inset-0 flex items-center justify-center">
                    <div className="text-center text-white p-8 z-10">
                        <h3 className="text-5xl font-bold mb-6 bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
                            Health Hacked
                        </h3>
                        <p className="text-xl opacity-90 max-w-md leading-relaxed">
                            Your journey to better health starts here. Track, monitor, and improve your wellness with AI-powered insights.
                        </p>
                        <div className="mt-8 flex justify-center space-x-4">
                            <div className="w-2 h-2 bg-white/60 rounded-full animate-pulse"></div>
                            <div className="w-2 h-2 bg-white/40 rounded-full animate-pulse delay-100"></div>
                            <div className="w-2 h-2 bg-white/60 rounded-full animate-pulse delay-200"></div>
                        </div>
                    </div>
                </div>

                {/* Decorative elements */}
                <div className="absolute top-0 right-0 w-64 h-64 bg-gradient-to-bl from-purple-500/20 to-transparent rounded-full blur-3xl"></div>
                <div className="absolute bottom-0 left-0 w-80 h-80 bg-gradient-to-tr from-blue-500/20 to-transparent rounded-full blur-3xl"></div>
            </div>
        </div>
    );
}