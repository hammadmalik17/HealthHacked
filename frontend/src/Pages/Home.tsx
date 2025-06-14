import { Header } from "../component/Header"
import logo from "../assets/logo.png"
import { ArrowRight } from "lucide-react";
import { useNavigate } from 'react-router-dom';

export function Home(){
    const navigate = useNavigate();

    const handleSignup = () => {
        navigate('/signup');
    };
    return (
        <div className="bg-mycolor-100">
         <div className='fixed top-0 left-0 w-full z-50 bg-mycolor-300'><Header/></div>
         <main className="bg-mycolor-100 w-11/12 mx-auto mt-32 h-screen rounded-md flex flex-col items-center">
                <h1 className="text-8xl font-bold text-mycolor-200 mt-16">
                    Health Hacked
                </h1>
                <p className="mt-20 text-3xl text-mycolor-200 max-w-4xl text-center">
                    Your smart healthcare assistant powered by AI. Track symptoms, get recommendations, and take control of your health journey.
                </p>

                <button 
                    className="mt-10 flex items-center gap-2 text-mycolor-200 text-xl font-semibold transition-all duration-300 ease-in-out bg-transparent border-none shadow-none hover:scale-105 hover:gap-3 hover:underline"
                    onClick= {handleSignup}
                >
                    Get Started
                    <ArrowRight className="w-5 h-5 transition-transform duration-300 ease-in-out group-hover:translate-x-1" />
                </button>


            </main>
         {/* <main className='bg-mycolor-500 w-14/15 mx-auto mt-20 h-screen rounded-md'></main> */}
    
          </div>
       )
}