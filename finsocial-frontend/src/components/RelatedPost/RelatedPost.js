import React, { useEffect } from 'react';
import YoutubePlayer from '../YoutubePlayer/YoutubePlayer';

function RelatedPost( { details } ){

    useEffect(()=>{
        window.twttr.widgets.load() 
    }, []);
    return (
        <div>
            <div dangerouslySetInnerHTML={{__html: details.tweet.html}}></div>
            <h2>Related Videos: </h2>
            <div className="related__container">
                {details.youtubes.map( item => (<YoutubePlayer item={item} />))}
            </div>
        </div>
        
    )
}

export default RelatedPost;