# SublimeTalwindCompletions
**TailwindCompletions** is a sublime-text-3 plugin that provides [tailwindcss](https://tailwindcss.com) code completions for HTML, CSS, Vue files.

# Installation

* ### Manual Installation
    * Using Git
        * Open terminal and change the path to Sublime `Packages` directory.(`Preferences > Browse Packages`).
        * Run `git clone https://github.com/lattespirit/sublime-tailwind-completions.git`.
        * Done.

    * Using zip File
        * Click the `Preferences > Browse Packages…` menu.
        * Download the [Package](https://github.com/lattespirit/sublime-tailwind-completions/archive/master.zip) file. Unzip and place the whole folder to the path methoned in Step One.
        * Rename the folder to `TailwindCompletions`.
        * Done.

# Configuration
**TailwindCompletions** supports specific [scopes](https://www.sublimetext.com/docs/3/scope_naming.html) for HTML, CSS and Vue files as default. If auto-completion popup does not show up, try to detect your current scope(`Tools > Developer > Show Scope Name`), and add it to your `Preferences.sublime-settings` file.

```json
{
    "tailwind_completion_scopes": []
}
```

# TODO
* Provide a entry point to generate custom completions from a custom CSS file.
