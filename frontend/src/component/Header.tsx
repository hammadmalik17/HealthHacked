import { useNavigate } from 'react-router-dom';

export function Header() {

    const navigate = useNavigate();

    const handleSignUp = () => {
        navigate('/signup');
    };

    const handleLogin = () => {
        navigate('/login');
    };

    return (
        <div className="flex w-screen h-25 items-center justify-around font-light text-lg font-mono">
            <div className='font-bold text-3xl'>Health Hacked</div>
            <div className="hidden gap-x-10 bg-stone-300 p-3 w-170 items-center justify-center rounded-full lg:flex"> 
            <div className="group cursor-pointer flex flex-col items-center">
                <div>Home</div>
                <div className="bg-black h-1 w-0 group-hover:w-full transition-all duration-300 rounded-full"></div>
            </div>
            <div className="group cursor-pointer flex flex-col items-center">
                <div>Facts</div>
                <div className="bg-black h-1 w-0 group-hover:w-full transition-all duration-300 rounded-full"></div>
            </div>
            <div className="group cursor-pointer flex flex-col items-center">
                <div>Symptoms-bot</div>
                <div className="bg-black h-1 w-0 group-hover:w-full transition-all duration-300 rounded-full"></div>
            </div>
            <div className="group cursor-pointer flex flex-col items-center">
                <div>News</div>
                <div className="bg-black h-1 w-0 group-hover:w-full transition-all duration-300 rounded-full"></div>
            </div>
            <div className="group cursor-pointer flex flex-col items-center">
                <div>About</div>
                <div className="bg-black h-1 w-0 group-hover:w-full transition-all duration-300 rounded-full"></div>
            </div>
            <div className="group cursor-pointer flex flex-col items-center">
                <div>Contact Us</div>
                <div className="bg-black h-1 w-0 group-hover:w-full transition-all duration-300 rounded-full"></div>
            </div>
            
            </div>
            <div className="flex gap-x-5">
                <button 
                    className=" p-2 cursor-pointer bg-gray-300 rounded-md w-28"
                    onClick={handleSignUp}
                >Sign Up</button>
                <button 
                    className=" p-2 cursor-pointer bg-mycolor-100 rounded-md w-28"
                    onClick={handleLogin}
                >Login</button>
            </div>
        </div>
    )
}
