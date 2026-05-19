import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import './App.css';

function Home() {
  return (
    <div className="container py-4">
      <h1 className="display-5">OctoFit Tracker</h1>
      <p className="lead">
        Track workouts, manage teams, view leaderboards, and get personalized
        workout suggestions.
      </p>
      <div className="row gy-3">
        <div className="col-md-6">
          <div className="card shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Authentication & Profiles</h5>
              <p className="card-text">
                Sign in, manage your profile, and keep your workout history in
                sync.
              </p>
            </div>
          </div>
        </div>
        <div className="col-md-6">
          <div className="card shadow-sm">
            <div className="card-body">
              <h5 className="card-title">Activity Tracking</h5>
              <p className="card-text">
                Log running, cycling, strength training, yoga, and more.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function Authentication() {
  return (
    <div className="container py-4">
      <h2>Authentication</h2>
      <p>
        This page will support user registration, login, and profile management
        via the backend API.
      </p>
    </div>
  );
}

function Activities() {
  return (
    <div className="container py-4">
      <h2>Activity Logging</h2>
      <p>
        Log workouts and activity sessions, including duration, distance, and
        calories.
      </p>
    </div>
  );
}

function Teams() {
  return (
    <div className="container py-4">
      <h2>Teams</h2>
      <p>
        Create and manage teams for group challenges and community fitness
        goals.
      </p>
    </div>
  );
}

function Leaderboard() {
  return (
    <div className="container py-4">
      <h2>Leaderboard</h2>
      <p>
        Compare user progress and standings with a competitive leaderboard.
      </p>
    </div>
  );
}

function Workouts() {
  return (
    <div className="container py-4">
      <h2>Personalized Workouts</h2>
      <p>
        View curated and suggested workout plans tailored to your goals.
      </p>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">
              OctoFit Tracker
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon" />
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/auth">
                    Auth
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">
                    Activities
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">
                    Teams
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">
                    Leaderboard
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">
                    Workouts
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/auth" element={<Authentication />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
