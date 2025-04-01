import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

export default function Home() {
    const [mortgages, setMortgages] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [totalPages, setTotalPages] = useState(1);

    const getMortgages = async (page = 1) => {
        try {
            const response = await fetch(`http://127.0.0.1:8003/get-mortgage-record?page=${page}`);
            if (!response.ok) throw new Error("Failed to fetch mortgages");
    
            const result = await response.json();
            console.log("Fetched Data:", result);
    
            if (result.status === "success" && Array.isArray(result.data)) {
                setMortgages(result.data);
                setTotalPages(result.total_pages || 1);
                setCurrentPage(page);
            } else {
                setMortgages([]);
                setTotalPages(1);
            }
        } catch (error) {
            alert("Unable to fetch the mortgage records.");
            console.error("Fetch error:", error);
        }
    };

    const deleteMortgage = async (id) => {
        if (!window.confirm("Are you sure you want to delete this record?")) return;

        try {
            const response = await fetch(`http://127.0.0.1:8003/delete-mortgage-record/${id}`, {
                method: "DELETE",
            });

            const result = await response.json();
            if (result.status === "success") {
                alert(result.message || "Mortgage deleted successfully");
                getMortgages(currentPage);
            } else {
                alert("Failed to delete the mortgage record.");
            }
        } catch (error) {
            console.error("Error deleting mortgage:", error);
            alert("An error occurred while deleting the mortgage record.");
        }
    };

    useEffect(() => { getMortgages(); }, []);

    return (
        <div className="container my-4">
            <h2 className="text-center mb-4">Mortgages</h2>

            <div className="row mb-3">
                <div className="col d-flex gap-2 flex-wrap">
                    <Link className="btn btn-primary" to="/insert-mortgage" role="button">
                        Add Mortgage
                    </Link>
                    <button className="btn btn-outline-primary" onClick={() => getMortgages(currentPage)}>
                        Refresh
                    </button>
                </div>
            </div>

            <div className="table-responsive">
                <table className="table table-striped table-bordered">
                    <thead className="table-primary">
                        <tr>
                            <th>ID</th>
                            <th>Credit Score</th>
                            <th>Loan Amount</th>
                            <th>Property Value</th>
                            <th>Annual Income</th>
                            <th>Debt Amount</th>
                            <th>Loan Type</th>
                            <th>Property Type</th>
                            <th>Credit Rating</th>
                            <th>Created At</th>
                            <th>Modified At</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {mortgages.length > 0 ? (
                            mortgages.map((mortgage) => (
                                <tr key={mortgage.id}>
                                    <td>{mortgage.id}</td>
                                    <td>{mortgage.credit_score}</td>
                                    <td>₹{mortgage.loan_amount.toLocaleString("en-IN")}</td>
                                    <td>₹{mortgage.property_value.toLocaleString("en-IN")}</td>
                                    <td>₹{mortgage.annual_income.toLocaleString("en-IN")}</td>
                                    <td>₹{mortgage.debt_amount.toLocaleString("en-IN")}</td>
                                    <td>{mortgage.loan_type}</td>
                                    <td>{mortgage.property_type}</td>
                                    <td>{mortgage.credit_rating}</td>
                                    <td>{mortgage.created_at}</td>
                                    <td>{mortgage.modified_at}</td>
                                    <td style={{ whiteSpace: "nowrap" }}>
                                        <Link className="btn btn-primary btn-sm me-1" to={`/update-mortgage/${mortgage.id}`}>
                                            Edit
                                        </Link>
                                        <button className="btn btn-danger btn-sm" onClick={() => deleteMortgage(mortgage.id)}>
                                            Delete
                                        </button>
                                    </td>
                                </tr>
                            ))
                        ) : (
                            <tr>
                                <td colSpan="12" className="text-center">
                                    No mortgage records found.
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>

            <div className="d-flex justify-content-center mt-3">
                <button
                    className="btn btn-outline-secondary me-2"
                    onClick={() => getMortgages(currentPage - 1)}
                    disabled={currentPage === 1}
                >
                    Previous
                </button>
                <span className="align-self-center">Page {currentPage} of {totalPages}</span>
                <button
                    className="btn btn-outline-secondary ms-2"
                    onClick={() => getMortgages(currentPage + 1)}
                    disabled={currentPage === totalPages}
                >
                    Next
                </button>
            </div>
        </div>
    );
}
