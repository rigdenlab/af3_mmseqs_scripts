def main_argpase_util(parser):
    parser.add_argument("input_json", help="Input sequence file")
    parser.add_argument("output_dir", help="Output directory")

    return parser


def mmseqs2_argparse_util(parser):
    parser.add_argument(
        "--mmseqs2",
        action="store_true",
        help="Use MMseqs2 for MSA",
    )
    parser.add_argument(
        "--templates", action="store_true", help="Include templates in the output json"
    )
    parser.add_argument(
        "--num_templates",
        type=int,
        default=20,
        help="Number of templates to include in the output json",
    )
    return parser


def custom_template_argpase_util(parser):
    parser.add_argument("--target_id", help="Target id relating to the custom template")
    parser.add_argument(
        "--custom_template", help="Custom template to include in the output json"
    )
    parser.add_argument(
        "--custom_template_chain",
        help="Custom template chain to include in the output json",
    )

    return parser


def boltz_argparse_util(parser):
    parser.add_argument(
        "-b",
        "--boltz1",
        action="store_true",
        help="Run Boltz1",
    )
    parser.add_argument(
        "--save_input",
        action="store_true",
        help="Save the input json file",
        default=False,
    )
    # add more arguments here
    return parser


def alphafold_argparse_util(parser):

    parser.add_argument("--output_json", help="Output json file")
    # make the vartible saved as database_dir
    parser.add_argument(
        "--database",
        help="The Database directory for the generation of the MSA.",
        dest="database_dir",
        default=None,
    )

    parser.add_argument(
        "--model_params",
        help="The directory containing the model parameters",
        default=None,
    )

    parser.add_argument(
        "-a",
        "--alphafold3",
        action="store_true",
        help="Run Alphafold",
    )

    parser.add_argument(
        "--override",
        help="Override the existing output directory, if it exists",
        action="store_true",
    )
    # add more arguments here

    return parser
