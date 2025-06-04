set nowrapscan
set tw=100

" The following is to compile the latex file and open the pdf file.
" let g:Run=  'AsyncRun! lualatex --shell-escape -synctex=1 SSI_Invitation_Probability_Le.tex'
" let g:Pdf=  'AsyncRun! zathura SSI_Invitation_Probability_Le.pdf &'
let g:Book=  'AsyncRun! zathura  /home/lechen/Dropbox/Research-References/52aaadf64c6f7c4189e9a52247b60151-diaconis-persi-and/output.pdf &'


" noremap <leader><leader> :update<bar>:exec g:Run<cr>
" noremap <leader><space> :exec g:Pdf<cr>
noremap <leader>r :exec g:Book<cr>
noremap <leader>l :FzfPreviewBufferLines<cr>

" The following is to open latex file without extension.
" Created one if it does not exist.
noremap gf :e <cfile>.tex<cr>


