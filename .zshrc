# Path to your oh-my-zsh installation.
export ZSH=~/.oh-my-zsh
export TERM="kitty"
export EDITOR=vim
export QT_QPA_PLATFORM=wayland

# THEME TO LOAD
ZSH_THEME="agnosterzak"

# Uncomment the following line to use case-sensitive completion.
CASE_SENSITIVE="false"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# This changes the timestamp fon history
HIST_STAMPS="yyyy-mm-dd"

### PLUGINS ###
# colored-man-pages: self-explanatory
# command-not-found: helpful tool to parse pacman if command isn't found
# common-aliases: a lot of useful aliases
# dirhistory: adds functionality for dirnav (ALT+direction)
# git: adds git functionality and aliases
# lol: adds fun lolcat aliases {bringz = git pull; cya = reboot; gtfo = mv; etc...}
plugins=(colored-man-pages command-not-found dirhistory git lol)

### PATHS ###
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/local/sbin:/usr/sbin:/sbin:/home/ryott/.config/scripts:/usr/lib/surfraw:/usr/bin/links"


# Export paths used for work
export RN=~/work/radon
export EMAN=~/work/pythonrnemanationanalysis

# sourcefile
source $ZSH/oh-my-zsh.sh
# Compilation flags
export ARCHFLAGS="-arch x86_64"

# Aliases
alias zshrc="vim ~/.zshrc"
alias ohmyzsh="vim ~/.oh-my-zsh"
alias vimrc="vim ~/.vimrc"
alias l='ls -lh'
alias L='ls -lah'
alias clean='clear; biblesay'
alias analysis='cd ~/work/pythonrnemanationanalysis; clear; pipenv shell; biblesay'
alias playground='cd ~/projects/playground; pipenv shell; clear; biblesay'
alias radon='cd ~/work/radon; pipenv shell; clear; biblesay'
alias sshbison='ssh ryottmp3@bison.sdsmt.edu'
alias pdf='mupdf'
alias ...='nocorrect ...'
alias pdftex='pdflatex'
alias qfig='vim ~/.config/qtile/config.py'
alias scap='cd /home/ryott/videos/screencast; recordmydesktop --fps 4 --v_quality 63 -o "$(date +%F_%H%M%S)" '
alias monitor='xrandr --output DP-1 --mode 1920x1080 --noprimary'
alias vimrc='vim ~/.vimrc'
alias math='cd ~/school/MATH125'
alias chem='cd ~/school/CHEM112'
alias lab='cd ~/school/CHEM112L'
alias cfg='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'

### Startup Sequence ###

# This documents all installed packages
pacman -Qq > ~/public/pacman/paclist
pacman -Qe > ~/public/pacman/paclist-explicit
pacman -Qii > ~/public/pacman/paclist-deps
pacman -Qiie > ~/public/pacman/paclist-explicit-deps

# clear terminal
clear

# This sends a dove with a bible verse to stdout
biblesay
