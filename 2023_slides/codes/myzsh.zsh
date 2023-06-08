run_n_times() {
  for i in {1..$2}; do
    ./$1 &
  done
}

alias 1D-BM='run_n_times 1D-BM-Animation-Dots.py 5'
alias 1D-Exp-BM='run_n_times 1D-Exp-BM-Animation.py 5'
alias 2D-BM='run_n_times 2D-BM.py 5'
alias 2D-BM-Animation='run_n_times 2D-BM-Animation.py 5'
alias 2D-RW='run_n_times 2D-RandowWalk.py 5'
alias 2D-RW-Animation='run_n_times 2D-RandowWalk-Animation.py 5'
alias 2D-RWRE='run_n_times 2D-RWRE.py 5'
alias 2D-RWRE-Animation='run_n_times 2D-RWRE-Animation.py 5'
alias 2D-Self-Avoiding-RW='run_n_times 2D-Self-Avoiding-RW.py 5'
alias SHE-R='Delta_L_TwoRows.pdf'

timestemp='20230608-0021'
SHE-Interval() {
  sxiv "$timestemp"_SHE-Lambda_0.png &
  sxiv "$timestemp"_SHE-Lambda_1.png &
  sxiv "$timestemp"_SHE-Lambda_2.png &
  # sxiv "$timestemp"_SHE-Lambda_3.png &
}
SHE-Interval-Animation() {
  mpv  "$timestemp"_SHE-Lambda_0.gif &
  mpv  "$timestemp"_SHE-Lambda_1.gif &
  mpv  "$timestemp"_SHE-Lambda_2.gif &
  # mpv  "$timestemp"_SHE-Lambda_3.gif &
}
