args = [
    {"name": "algo", "help": "RL Algorithm", "default": "ppo", "type": "str", "required": False},
    {"name": "env", "type": "str", "default": "CartPole-v1", "help": "environment ID"},
    {"name": "tensorboard-log", "help": "Tensorboard log dir", "default": "", "type": "str"},
    {"name": "trained-agent", "help": "Path to a pretrained agent to continue training", "default": "", "type": "str"},
    {
        "name": "truncate-last-trajectory",
        "help": "When using HER with online sampling the last trajectory "
        "in the replay buffer will be truncated after reloading the replay buffer.",
        "default": True,
        "type": bool,
    },
    {"name": "n-timesteps", "help": "Overwrite the number of timesteps", "default": -1, "type": "int"},
    {"name": "num-threads", "help": "Number of threads for PyTorch (-1 to use default)", "default": -1, "type": "int"},
    {"name": "log-interval", "help": "Override log interval ( default: -1, no change)", "default": -1, "type": "int"},
    {
        "name": "eval-freq",
        "help": "Evaluate the agent every n steps (if negative, no evaluation). "
        "During hyperparameter optimization n-evaluations is used instead",
        "default": 25000,
        "type": "int",
    },
    {
        "name": "optimization-log-path",
        "help": "Path to save the evaluation log and optimal policy for each hyperparameter tried during optimization. "
        "Disabled if no argument is passed.",
        "type": "str",
    },
    {"name": "eval-episodes", "help": "Number of episodes to use for evaluation", "default": 5, "type": "int"},
    {"name": "n-eval-envs", "help": "Number of environments for evaluation", "default": 1, "type": "int"},
    {"name": "save-freq", "help": "Save the model every n steps (if negative, no checkpoint)", "default": -1, "type": "int"},
    {
        "name": "save-replay-buffer",
        "help": "Save the replay buffer too (when applicable)",
        "action": "store_true",
        "default": False,
    },
    {"name": "log-folder", "help": "Log folder", "type": "str", "default": "logs"},
    {"name": "seed", "help": "Random generator seed", "type": "int", "default": -1},
    {"name": "vec-env", "help": "VecEnv type", "type": "str", "default": "dummy", "choices": ["dummy", "subproc"]},
    {"name": "device", "help": "PyTorch device to be use (ex: cpu, cuda...)", "default": "auto", "type": "str"},
    {
        "name": "n-trials",
        "help": "Number of trials for optimizing hyperparameters. "
        "This applies to each optimization runner, not the entire optimization process.",
        "type": "int",
        "default": 500,
    },
    {
        "name": "max-total-trials",
        "help": "Number of (potentially pruned) trials for optimizing hyperparameters. "
        "This applies to the entire optimization process and takes precedence over --n-trials if set.",
        "type": "int",
        "default": None,
    },
    {"name": "optimize-hyperparameters", "action": "store_true", "default": False, "help": "Run hyperparameters search"},
    {"name": "no-optim-plots", "action": "store_true", "default": False, "help": "Disable hyperparameter optimization plots"},
    {"name": "n-jobs", "help": "Number of parallel jobs when optimizing hyperparameters", "type": "int", "default": 1},
    {
        "name": "sampler",
        "help": "Sampler to use when optimizing hyperparameters",
        "type": "str",
        "default": "tpe",
        "choices": ["random", "tpe", "skopt"],
    },
    {
        "name": "pruner",
        "help": "Pruner to use when optimizing hyperparameters",
        "type": "str",
        "default": "median",
        "choices": ["halving", "median", "none"],
    },
    {"name": "n-startup-trials", "help": "Number of trials before using optuna sampler", "type": "int", "default": 10},
    {
        "name": "n-evaluations",
        "help": "Training policies are evaluated every n-timesteps // n-evaluations steps when doing hyperparameter optimization."
        "Default is 1 evaluation per 100k timesteps.",
        "type": "int",
        "default": None,
    },
    {
        "name": "storage",
        "help": "Database storage path if distributed optimization should be used",
        "type": "str",
        "default": None,
    },
    {"name": "study-name", "help": "Study name for distributed optimization", "type": "str", "default": None},
    {"name": "verbose", "help": "Verbose mode (0: no output, 1: INFO)", "default": 1, "type": "int"},
    {
        "name": "gym-packages",
        "type": "str",
        "nargs": "+",
        "default": [],
        "help": "Additional external Gym environment package modules to import",
    },
    {
        "name": "env-kwargs",
        "type": "str",
        "nargs": "+",
        "action": "StoreDict",
        "help": "Optional keyword argument to pass to the env constructor",
    },
    {
        "name": "eval-env-kwargs",
        "type": "str",
        "nargs": "+",
        "action": "StoreDict",
        "help": "Optional keyword argument to pass to the env constructor for evaluation",
    },
    {
        "name": "hyperparams",
        "type": "str",
        "nargs": "+",
        "action": "StoreDict",
        "help": "Overwrite hyperparameter (e.g. learning_rate:0.01 train_freq:10)",
    },
    {
        "name": "conf-file",
        "type": "str",
        "default": None,
        "help": "Custom yaml file or python package from which the hyperparameters will be loaded."
        "We expect that python packages contain a dictionary called 'hyperparams' which contains a key for each environment.",
    },
    {"name": "uuid", "action": "store_true", "default": False, "help": "Ensure that the run has a unique ID"},
    {
        "name": "track",
        "action": "store_true",
        "default": False,
        "help": "if toggled, this experiment will be tracked with Weights and Biases",
    },
    {"name": "wandb-project-name", "type": "str", "default": "sb3", "help": "the wandb's project name"},
    {"name": "wandb-entity", "type": "str", "default": None, "help": "the entity (team) of wandb's project"},
    {
        "name": "progress",
        "action": "store_true",
        "default": False,
        "help": "if toggled, display a progress bar using tqdm and rich",
    },
    {
        "name": "wandb-tags",
        "type": "str",
        "default": [],
        "nargs": "+",
        "help": "Tags for wandb run, e.g.: -tags optimized pr-123",
    },
]

for arg in args:
    print(f"    {arg['name']}: {arg.get('type', '!!!!!!')} = '{arg.get('default', '!!!!!!')}' # {arg['help']}")
