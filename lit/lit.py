# Lint as: python3
r"""Quick-start demo for a sentiment analysis model.
This demo fine-tunes a small Transformer (BERT-tiny) on the Stanford Sentiment
Treebank (SST-2), and starts a LIT server.
To run locally:
  python -m lit_nlp.examples.quickstart_sst_demo --port=5432
Training should take less than 5 minutes on a single GPU. Once you see the
ASCII-art LIT logo, navigate to localhost:5432 to access the demo UI.
"""
import os

from absl import app
from absl import flags
from absl import logging

from lit_nlp import dev_server
from lit_nlp import server_flags
from lit_nlp.components import word_replacer
from lit_nlp.examples.datasets import glue

from glue_models import *

# NOTE: additional flags defined in server_flags.py

FLAGS = flags.FLAGS

flags.DEFINE_list(
    "models", [
               "textattack/bert-base-uncased-SST-2",
               "textattack/albert-base-v2-SST-2",
               "textattack/bert-base-uncased-RTE",
               "textattack/albert-base-v2-RTE",
    ],
    "Models to load."
)

def main(_):
  # Load model

  models = {}
  for model_name_or_path in FLAGS.models:
    # Ignore path prefix, if using /path/to/<model_name> to load from a
    # specific directory rather than the default shortcut.
    model_name = os.path.basename(model_name_or_path)

    if 'SST-2' in model_name:
      models[model_name] = SST2Model(model_name_or_path)
    elif 'RTE' in model_name:
      models[model_name] = RTEModel(model_name_or_path)

  datasets = {}

  datasets["sst_dev"] = glue.SST2Data("validation")
  datasets["rte_dev"] = glue.RTEData("validation")

  # Start the LIT server. See server_flags.py for server options.
  generators = {"word_replacer": word_replacer.WordReplacer()}

  lit_server = dev_server.Server(models, datasets, generators=generators, **server_flags.get_flags())
  lit_server.serve()


if __name__ == "__main__":
  app.run(main)