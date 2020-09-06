import React, { useEffect } from 'react';
import YoutubePlayer from '../YoutubePlayer/YoutubePlayer';

function SocialMediaPost( { details } ){

    useEffect(()=>{
        window.instgrm.Embeds.process()
        window.twttr.widgets.load() 
    }, []);
    return (
        <div>
            {details.provider_name === 'Youtube' ? 
            <YoutubePlayer item={details} /> : 
            <div dangerouslySetInnerHTML={{__html: details.html}}></div>}
        </div>
        
    )
}

export default SocialMediaPost;