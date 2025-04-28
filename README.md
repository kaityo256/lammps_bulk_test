# 物性研バルクジョブテストリポジトリ

## テスト方法

リポジトリをcloneして、`python3 generate_config.py`を実行して`test.atoms`を生成する。

```sh
git clone https://github.com/kaityo256/lammps_bulk_test.git
cd lammps_bulk_test
python3 generate_config.py
```

## ジョブの投入

### 4ノードシリアルジョブ

4ノードを使い、4ノード512プロセスのジョブをシリアルに実行。

```sh
sbatch job4_serial.sh 
```

ジョブスクリプトは

```sh
#!/bin/sh

#SBATCH -p i8cpu
#SBATCH -N 4
#SBATCH -n 512

source /home/issp/materiapps/intel/lammps/lammpsvars.sh

srun lammps < test1.input
srun lammps < test2.input
```

となっており、4ノード512プロセスのLAMMPSのジョブをシリアルに実行している。

実行時間を調べる。

```sh
$ tail -n 1 test*.log
==> test1.log <==
Total wall time: 0:00:13

==> test2.log <==
Total wall time: 0:00:06
```

それぞれ10秒程度で終了している。

### 8ノードバルクジョブ

4ノードを使い、4ノード512プロセスのジョブをバルク実行。

```sh
sbatch job8.sh 
```

ジョブスクリプトは

```sh
#!/bin/sh

#SBATCH -p i8cpu
#SBATCH -N 8

source /home/issp/materiapps/intel/lammps/lammpsvars.sh

srun --exclusive --mem-per-cpu=1840 -n 512 -c 1 lammps < test1.input &
srun --exclusive --mem-per-cpu=1840 -n 512 -c 1 lammps < test2.input &

wait
cat test1.log
cat test2.log
```

となっており、4ノード512プロセスのジョブを同時実行することが想定されている。


