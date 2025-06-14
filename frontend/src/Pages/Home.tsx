import { Header } from "../component/Header"

export function Home(){
    return (
        <div>
         <div className='fixed top-0 left-0 w-full z-50 bg-mycolor-300'><Header/></div>
         <main className='bg-mycolor-100 w-14/15 mx-auto mt-30 h-screen rounded-md'></main>
         <main className='bg-mycolor-500 w-14/15 mx-auto mt-20 h-screen rounded-md'></main>
    
          </div>
       )
}