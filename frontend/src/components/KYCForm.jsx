/* @jsxImportSource react */
import React from 'react'
import { useState } from 'react'
import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000/api/v1'

export default function KYCForm(){
  const [form, setForm] = useState({ full_name: '', document_id: '', country: 'UY' })
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)

  const onChange = (e) => setForm({ ...form, [e.target.name]: e.target.value })

  const onSubmit = async (e) => {
    e.preventDefault()
    setLoading(true); setError(null); setResult(null)
    try {
      const { data } = await axios.post(`${API_BASE}/kyc/verify`, form)
      setResult(data)
    } catch (err) {
      setError(err?.response?.data?.detail || 'Error')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="bg-white shadow-sm rounded-xl p-6 mt-6">
      <h2 className="text-xl font-semibold mb-4">Identity Verification</h2>

      <form onSubmit={onSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-1">Full Name</label>
          <input
            name="full_name"
            value={form.full_name}
            onChange={onChange}
            className="w-full border rounded-lg px-3 py-2"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">Document</label>
          <input
            name="document_id"
            value={form.document_id}
            onChange={onChange}
            className="w-full border rounded-lg px-3 py-2"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-1">Country</label>
          <input
            name="country"
            value={form.country}
            onChange={onChange}
            className="w-full border rounded-lg px-3 py-2"
          />
        </div>

        <button
          disabled={loading}
          className="bg-black text-white rounded-lg px-4 py-2 disabled:opacity-50"
        >
          {loading ? 'Verifying...' : 'Submit'}
        </button>
      </form>

      {result && (
        <div className="mt-4 p-3 rounded-lg bg-green-50 border border-green-200">
          <div className="font-medium">Approved ✅</div>
          <pre className="text-sm text-green-800">{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}

      {error && (
        <div className="mt-4 p-3 rounded-lg bg-red-50 border border-red-200">
          <div className="font-medium">Rejected ❌</div>
          <p className="text-sm text-red-800">{error}</p>
        </div>
      )}
    </div>
  )
}
