import React, { useEffect, useState } from 'react';
import SocialMediaPost from '../../components/SocialMediaPost/SocialMediaPost';

function Home () {
    const [entryData, setEntryData] = useState([])

    const getEntries = () => {
        fetch("http://a73f55b02b9e646769137711ea54cc99-660186764.ap-southeast-1.elb.amazonaws.com/get_socials")
            .then( response => response.json())
            .then( data => setEntryData(data.data));
    }

    useEffect(() => {
        const scriptTwitter = document.createElement("script");
        scriptTwitter.src = "https://platform.twitter.com/widgets.js";
        scriptTwitter.async = true;
        scriptTwitter.onload = () =>{
            window.twttr.widgets.load() 
        }


        const scriptTiktok = document.createElement("script");
        scriptTiktok.src = "https://www.tiktok.com/embed.js";
        scriptTiktok.async = true;

        const scriptInstagram = document.createElement("script");
        scriptInstagram.src = "https://www.instagram.com/embed.js";
        scriptInstagram.async = true;
        scriptInstagram.onload = () => {
            window.instgrm.Embeds.process()
        }
    
        document.body.appendChild(scriptTwitter);
        document.body.appendChild(scriptTiktok);
        document.body.appendChild(scriptInstagram);

        getEntries();

        return () =>{
            document.body.removeChild(scriptTwitter)
            document.body.removeChild(scriptTiktok);
            document.body.removeChild(scriptInstagram);
        }
      }, [])

    return (
        <div className="home__feed">
            {entryData.map((entry, index) => (<SocialMediaPost key={index} details={entry} />))}
        </div>
    )
}

export default Home;