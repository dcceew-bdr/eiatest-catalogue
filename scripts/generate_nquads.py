import gzip
import logging
from pathlib import Path

from rdflib import Dataset
from rdflib.exceptions import ParserError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def compress_dir_to_nq_gz(directory: Path, artifact_dir: Path):
    """
    Recursively processes RDF files from a directory, combines them into a single dataset,
    and writes the output as a gzipped N-Quads file.
    """
    if not directory.is_dir():
        logger.warning(f"Directory not found: {directory}")
        return

    output_file = artifact_dir / f"{directory.name}.nq.gz"
    logger.info(f"Processing directory: {directory} -> {output_file}")
    
    ds = Dataset(default_union=True)

    rdf_files = list(directory.rglob("*.ttl")) + list(directory.rglob("*.trig"))
    
    if not rdf_files:
        logger.warning(f"No .ttl or .trig files found in {directory}")
        return

    for file_path in rdf_files:
        logger.info(f"Parsing file: {file_path}")
        try:
            # Guess format based on file extension
            fmt = file_path.suffix.replace('.', '')
            if fmt == 'ttl':
                fmt = 'turtle'
            
            ds.parse(location=str(file_path), format=fmt)
        except ParserError as e:
            logger.error(f"Could not parse {file_path}: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred with file {file_path}: {e}")

    logger.info(f"Serializing dataset for {directory.name} to N-Quads format.")
    serialized_data = ds.serialize(format="nquads")

    logger.info(f"Compressing data and writing to {output_file}")
    with gzip.open(output_file, "wb") as f:
        f.write(serialized_data.encode("utf-8"))

    logger.info(f"Processing complete for {directory.name}. Output at {output_file}")


if __name__ == "__main__":
    root = Path(__file__).parent.parent
    
    dirs_to_process = [
        root / "resources",
        root / "config",
    ]
    
    artifacts_path = root / "for_upload"
    artifacts_path.mkdir(exist_ok=True)

    for d in dirs_to_process:
        compress_dir_to_nq_gz(d, artifacts_path)
