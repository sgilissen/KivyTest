def fo_transition():
    '''Transition where the new screen 'falls' from the screen centre,
    becoming smaller and more transparent until it disappears, and
    revealing the new screen behind it. Mimics the popular/standard
    Android transition.

    .. versionadded:: 1.8.0

    '''

    # duration = NumericProperty(0.15)
    '''Duration in seconds of the transition, replacing the default of
    :class:`TransitionBase`.

    :class:`duration` is a :class:`~kivy.properties.NumericProperty` and
    defaults to .15 (= 150ms).
    '''

    shader = '''$HEADER$
    uniform float t;
    uniform sampler2D tex_in;
    uniform sampler2D tex_out;

    void main(void) {
        /* quantities for position and opacity calculation */
        float tr = 0.5*sin(t);  /* 'real' time */
        vec2 diff = (tex_coord0.st - 0.5) * (1.0/(1.0-tr));
        vec2 dist = diff + 0.5;
        float max_dist = 1.0 - tr;

        /* in and out colors */
        vec4 cin = vec4(texture2D(tex_in, tex_coord0.st));
        vec4 cout = vec4(texture2D(tex_out, dist));

        /* opacities for in and out textures */
        float oin = clamp(1.0-cos(t), 0.0, 1.0);
        float oout = clamp(cos(t), 0.0, 1.0);

        bvec2 outside_bounds = bvec2(abs(tex_coord0.s - 0.5) > 0.5*max_dist,
                                     abs(tex_coord0.t - 0.5) > 0.5*max_dist);

        vec4 frag_col;
        if (any(outside_bounds) ){
            frag_col = vec4(cin.x, cin.y, cin.z, 1.0);
            }
        else {
            frag_col = vec4(oout*cout.x + oin*cin.x, oout*cout.y + oin*cin.y,
                            oout*cout.z + oin*cin.z, 1.0);
            }

        gl_FragColor = frag_col;
    }
    '''

    return shader
