
import React from 'react'
import YouTube from 'react-youtube';

function YoutubePlayer({ item }){
    const playerOpts = {
        height: '270',
        width: '100%',
        playerVars: {
            autoplay: 0,
          },
    }
    
    return <YouTube 
            videoId={item.url_suffix.split('/watch?v=')[1]}
            opts={playerOpts}
            className="youtube__video"
            containerClassName="youtube__container"
            /> 
}

export default YoutubePlayer;