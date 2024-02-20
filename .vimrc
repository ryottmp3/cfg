
" written by Ryott Glayzer


" SETTINGS ================================================================ {{{

" Disable compatibility with vi which can cause unexpected issues
set nocompatible

" Enable filetype detection (vim will try to detect filetype of current file
filetype on

" Enable filetype plugins and load plugin for the detected filetype
filetype plugin on

" Load an indent file for the detected filetype
filetype indent on

" Enable Syntax highlighting
let python_highlight_all=1
syntax on

" Allow backspacing over everything in insert mode
set backspace=indent,eol,start

" Add number to each line on the left-hand size
set number

" Set shift width to 4 spaces
set shiftwidth=4

" Set tab width to 4 columns
set tabstop=4

" Do not save backup files
set nobackup

" Scroll off
set scrolloff=10

" Don't Wrap
set nowrap

" While searching through a file incrementally highlight matching chars as type
set incsearch

" Ignore caps
set ignorecase

" override when searching for caps
set smartcase

" Show partial command you type in the last line of the screen.
set showcmd

" Show the mode you are on the last line.
set showmode

" Set 80 line width
" set colorcolumn=80

" Spell Checking
setlocal spell 
set spelllang=en_us
inoremap <C-l> <c-g>u<Esc>[s1z=`]a<c-g>u

" Show matching words during a search.
set showmatch

" Use highlighting when doing a search.
set hlsearch

" Set the commands to save in history default number is 20.
set history=1000

" Enable autocompletion for commands with TAB
set wildmenu
set wildmode=list:longest
set wildignore=*.jpg,*.docx,*.png,*.git,*.pdf,*.exe,*.flv,*.img,*.xlsx


let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" }}}
" PLUGINS ================================================================= {{{
call plug#begin()
" Polyglot, language support for vim
Plug 'sheerun/vim-polyglot'

" kitty conf syntax
" Plug 'fladson/vimkitty'

" Autopairing 
Plug 'jiangmiao/auto-pairs'

" LaTeX plugin for ViM
Plug 'lervag/vimtex'

" NERDTree, a file explorer
Plug 'preservim/nerdtree'

" tagbar, similar to a minimap
Plug 'preservim/tagbar'

" Powerline
Plug 'Lokaltog/powerline'

" CTRL P
Plug 'kien/ctrlp.vim'

" Check syntax
Plug 'vim-syntastic/syntastic'

" Check PEP 8
Plug 'nvie/vim-flake8'

" Python autocompletion
Plug 'Valloric/YouCompleteMe'

" Minimap
Plug 'wfxr/minimap.vim'

" LaTeX
Plug 'lervag/vimtex'

" Snippets
Plug 'sirver/ultisnips'
Plug 'honza/vim-snippets'
call plug#end()


 " }}}
"z MAPPINGS ================================================================ {{{
" Open/Close tagbar
nmap <F8> :TagbarToggle<CR>

" NERDTree mappings
nnoremap <leader>n :NERDTreeFocus<CR>
" nnoremap <C-o> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
" nnoremap <C-f> :NERDTreeFind<CR>

" Minimap Remap
nmap <F9> :MinimapToggle<CR>

" }}}
" VIMSCRIPT =============================================================== {{{

" Vimscript goes here

" Enable Code Folding using the 'Marker Method'
augroup filetype_vim
	autocmd!
	autocmd FileType vim setlocal foldmethod=marker
    autocmd FileType python setlocal foldmethod=indent
    autocmd FileType tex setlocal foldmethod=indent
    autocmd FileType cpp setlocal foldmethod=indent
    set foldnestmax=2
    hi Folded ctermbg=237
augroup END

" syntax for asm
au BufRead,BufNewFile *.asm set filetype=nasm

" Open NERDTree with Vim
" Start NERDTree and put the cursor back in the other window.
" autocmd VimEnter * NERDTree | wincmd p
" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif
" If another buffer tries to replace NERDTree, put it in the other window, and bring back NERDTree.
autocmd BufEnter * if bufname('#') =~ 'NERD_tree_\d\+' && bufname('%') !~ 'NERD_tree_\d\+' && winnr('$') > 1 |
    \ let buf=bufnr() | buffer# | execute "normal! \<C-W>w" | execute 'buffer'.buf | endif
let NERDTreeIgnore=['\.pyc$','\~$']

" YouCompleteMe config
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>

" minimap
let g:minimap_width = 10
let g:minimap_auto_start = 1
let g:minimap_auto_start_win_enter = 1
" If minimap is the only window left close it
" autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:minimap') && b:minimap.isTabTree() | quit | endif

" ViMTeX
let g:tex_flavor='latex'
let g:vimtex_view_method='zathura'
let g:vimtex_quickfix_mode=0
set conceallevel=2
let g:tex_conceal='abdmg'
" Default compiling format
let g:Tex_DefaultTargetFormat='pdf'

" Never Forget, To set the default viewer:: Very Important
let g:Tex_ViewRule_pdf = 'zathura'

function! Synctex()
        " remove 'silent' for debugging
        execute "silent !zathura --synctex-forward " . line('.') . ":" . col('.') . ":" . bufname('%') . " " . g:syncpdf
endfunction
map <C-enter> :call Synctex()<cr>

" Snippets
let g:UltiSnipsExpandTrigger = '<F2>'
let g:UltiSnipsJumpForwardTrigger = '<F2>'
let g:UltiSnipsJumpBackwardTrigger = '<S-F2>'
let g:UltiSnipsSnippetDirectories=[$HOME.'/.vim/snippets']

" }}} 

" STATUS LINE ============================================================= {{{

" Status bar code goes here


" }}}

