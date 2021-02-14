set -e
# python run.py --definitions chip.yaml
# python run.py --local --algorithm ball --run-disabled --dataset random-xs-20-euclidean --definitions chip.yaml
# python run.py --local --algorithm trilat --run-disabled --dataset random-xs-20-euclidean --definitions chip.yaml
python run.py --local --algorithm trilatapprox --run-disabled --dataset random-xs-20-euclidean --definitions chip.yaml
# python plot.py --dataset random-xs-20-euclidean
