<body>
    <p style="margin:0 auto; font-size: 30pt; width: 90px">
        {{"YES" if frozen else "NO"}}
    </p>
    <div style="margin:0 auto; width: 375px">
        <form method="post" action={{"/unfreeze" if frozen else "/freeze"}}>
            <input type="image" src="/static/button" alt="Submit Form" />
        </form>
    </div>
<body>
