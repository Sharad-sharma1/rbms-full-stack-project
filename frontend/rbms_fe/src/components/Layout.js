import { Link } from "react-router-dom";

export function Navbar() {
    return (
        <nav
            className="navbar navbar-expand-lg bg-white border-bottom box-shadow"
            style={{
                backgroundColor: "#8EC5FC",
                backgroundImage: "linear-gradient(62deg, #8EC5FC 0%, #E0C3FC 100%)",
            }}
        >
            <div className="container">
                {/* Brand Logo */}
                <Link className="navbar-brand" to="/">
                    <img
                        src="/page_main_logo.png"
                        alt="Brand Logo"
                        width="90"
                        className="me-2"
                        style={{ borderRadius: "50px" }}
                    />
                </Link>

                {/* Toggle Button for Small Screens */}
                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>

                {/* Navigation Links */}
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link className="nav-link text-dark" to="/">Home</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link text-dark" to="/admin">Admin</Link>
                        </li>
                    </ul>

                    {/* Admin/User Dropdown */}
                    <ul className="navbar-nav">
                        <li className="nav-item dropdown">
                            <a
                                className="nav-link dropdown-toggle"
                                href="#"
                                role="button"
                                data-bs-toggle="dropdown"
                                aria-expanded="false"
                            >
                                Admin/User
                            </a>
                            <ul className="dropdown-menu">
                                <li>
                                    <Link className="dropdown-item" to="/profile">Profile</Link>
                                </li>
                                <li><hr className="dropdown-divider" /></li>
                                <li>
                                    <Link className="dropdown-item" to="/logout">Logout</Link>
                                </li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
}

export function Footer() {
    return (
        <footer className="text-center p-4 border-top">
            <img src="/cr_logo.png" alt="Footer Logo" width="50" className="me-2" />
        </footer>
    );
}
