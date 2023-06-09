import bg from "./media/bgs/photo3184445660.jpg"
import "./App.css"
import { useEffect, useState } from "react"
import axios from "axios"
import Post from "./pages/post"
import { Link } from "react-router-dom"
import { useLocation } from "react-router-dom"
export default function LandingPage() {
    const [trends, setTrends] = useState([])
    function getTrends() {
        axios.get('/api/posts/trending/').then(response => setTrends(response.data))
    }
    const nav = document.getElementById("nav_section")
    const { pathname } = useLocation()

    if (nav && pathname === "/"){
        nav.style.display = "none"
    }
    useEffect(getTrends, [])
    const trendingElements = trends.map(post => <Post notshowtext={true} text={post.text} width={"400px"} height={"180px"} likes={post.likes} profile={post.profile} publicationDate={post.publicationDate} pb={post.publicationShortDate} pk={post.pk} title={post.title} authorpk={post.author} />)
    return (
        <div>
            <div className="bg">
                <img src={bg} alt="" />
                <div id="landing_nav" className="navbar">
                    <h2 to="/">Xlog</h2>
                    <Link className="link" to="/signup" ><p>Signup</p></Link>
                    <Link className="link" to="/login" ><p>Login</p></Link>
                </div>
                <h1>a place for your ideas</h1>
            </div>
            <div className="midpart">
                <h2 id="midpart_title">trending posts on blog</h2>
                <div className="trendbox">
                    {trendingElements}
                </div>
            </div>

            <div className="footer">
                <p>all rights belong to <a href="https://sadra-etaei.github.io/">Sadra Etaei</a> © 2023</p> 
            </div>
        </div>
    )
}