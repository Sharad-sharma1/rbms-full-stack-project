import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function InsertMortgage() {
  const initialFormData = {
    credit_score: "",
    loan_amount: "",
    property_value: "",
    annual_income: "",
    debt_amount: "",
    loan_type: "fixed",
    property_type: "single_family",
  };

  const [formData, setFormData] = useState(initialFormData);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (JSON.stringify(formData) === JSON.stringify(initialFormData)) {
      window.alert("No changes detected. Please modify the form before submitting.");
      return;
    }
  
    try {
      const response = await fetch("http://127.0.0.1:8003/insert-mortgage-record", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
  
      if (!response.ok) {
        throw new Error(`Server Error: ${response.status}`);
      }
  
      const result = await response.json();
      window.alert(result.message); // Show success message
      navigate("/"); // Redirect to home page
  
    } catch (error) {
      console.error("Error:", error);
      
      if (error.message.includes("Failed to fetch")) {
        window.alert("Server is unreachable. Please try again later.");
      } else {
        window.alert("An unexpected error occurred. Please try again.");
      }
    }
  };
  

  return (
    <div className="container my-4">
      <div className="row">
        <div className="col-md-8 mx-auto rounded border p-4">
          <h2 className="text-center mb-5">Create Mortgage</h2>
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label">Credit Score(300-850)</label>
              <input type="number" className="form-control" name="credit_score" value={formData.credit_score} onChange={handleChange} required />
            </div>
            <div className="mb-3">
              <label className="form-label">Loan Amount (₹)</label>
              <input type="number" className="form-control" name="loan_amount" value={formData.loan_amount} onChange={handleChange} required />
            </div>
            <div className="mb-3">
              <label className="form-label">Property Value (₹)</label>
              <input type="number" className="form-control" name="property_value" value={formData.property_value} onChange={handleChange} required />
            </div>
            <div className="mb-3">
              <label className="form-label">Annual Income (₹)</label>
              <input type="number" className="form-control" name="annual_income" value={formData.annual_income} onChange={handleChange} required />
            </div>
            <div className="mb-3">
              <label className="form-label">Debt Amount (₹)</label>
              <input type="number" className="form-control" name="debt_amount" value={formData.debt_amount} onChange={handleChange} required />
            </div>
            <div className="mb-3">
              <label className="form-label">Loan Type</label>
              <select className="form-select" name="loan_type" value={formData.loan_type} onChange={handleChange}>
                <option value="fixed">Fixed</option>
                <option value="adjustable">Adjustable</option>
              </select>
            </div>
            <div className="mb-3">
              <label className="form-label">Property Type</label>
              <select className="form-select" name="property_type" value={formData.property_type} onChange={handleChange}>
                <option value="single_family">Single Family</option>
                <option value="condo">Condo</option>
              </select>
            </div>
            <button type="submit" className="btn btn-primary w-100">Submit</button>
          </form>
        </div>
      </div>
    </div>
  );
}
