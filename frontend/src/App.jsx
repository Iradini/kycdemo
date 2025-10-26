import KYCForm from './components/KYCForm'

export default function App(){
    return (
        <div className="min-h-screen bg-slate-50">
            <header className="border-b bg-white">
                <div className="max-w-3xl mx-auto py-4 ">
                    <h1 className="text-2xl font-semibold">KYC Demo</h1>
                    <p className="text-slate-600">React + Tailwind + FastAPI + Postgres</p>
                </div>
            </header>
            <main className="max-w-3xl mx-auto p-4">
                <KYCForm />
            </main>
        </div>
    )
}