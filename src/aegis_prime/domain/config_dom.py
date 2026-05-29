from aegis_prime.config.builder.prompts import run_builder
from aegis_prime.config.builder.generator import build_config_dict
from aegis_prime.config.builder.writer import write_config


def config_build():
    answers = run_builder()
    config = build_config_dict(answers)
    write_config(config, answers["output_path"])