# Evaluation metrics for Long-RGASP project

The objective of this markdown file is to return in a simple format all the metrics that were decided for evaluating one transcriptome submission. These metrics will allow us to compare different pipelines performance.

For this purpose two scripts are needed: one with functions to evaluate individual isoforms and other that will apply them for the whole set of transcripts described and it will calculate the final metrics. We will also need the IDs of SIRVs and ERRCs spike-ins. Please, download and store all of them in the same directory and set it as the path for the `functions.directory` at the beginning of the markdown file.

First of all, you will need to run [SQANTI3](https://github.com/ConesaLab/SQANTI3). Your transcript-models will be compared against the GENCODE annotation and using the last version available of the reference genome. We do highly recommend to use the ones uploaded on our [LRGASP submission github](https://github.com/LRGASP/lrgasp-submissions/blob/master/docs/reference-genomes.md) because they already include the spike-ins information (SIRVs and ERCC). If you are going to submit also expression values for your transcript-models, just use the `--expression` option to provide the .TSV file.

Additional information will be used to evaluate the detected isoforms:

- **CAGE peak data**: BED files can be input using `--cage_peak` option. CAGE peak data for human and mouse can be found [here](http://reftss.clst.riken.jp/reftss/Main_Page)

- **polyA motif list**: TXT file with the most common polyA motifs for human and mouse. Include it through `--polyA_motif_list` option. You can download the list we will be using for the evaluation from [here](https://raw.githubusercontent.com/Magdoll/images_public/master/SQANTI2_support_data/human.polyA.list.txt).

- **SJ coverage**: As an ortholog approach, Illumina reads will be used to call splice-junctions (SJ) and this information can also be put into SQANTI3. Using the same reference genome described above, STAR index will be built without using the reference annotation file, so _a priori_ information won't bias the mapping. To obtain the SJ files (*SJ.out.tab), pair end reads from each replicate will be mapped using the following command line:

`
STAR --runThreadN 8 --genomeDir STAR_genome_index --readFilesIn read1.fastq read2.fastq --outFileNamePrefix Sample_name
 --alignSJoverhangMin 8  --alignSJDBoverhangMin 1 --outFilterType BySJout --outSAMunmapped Within --outFilterMultimapNmax 20
 --outFilterMismatchNoverLmax 0.04 --outFilterMismatchNmax 999 --alignIntronMin 20 --alignIntronMax 1000000 --alignMatesGapMax 1000000
 --sjdbScore 1 --genomeLoad NoSharedMemory --outSAMtype BAM Unsorted
 `

Once you have run SQANTI3, its output files contain all the information needed for calculating any of the metrics, so we have to define the path where they are and the name of the pipeline as the `data.directory`. 

## Dry run examples

For the dry run, these files were uploaded to the Google Drive folder created for Long-RGASP, if you want to check how performed one pipeline you can simply download them and run the evaluation. Several Rdata files will be created inside the output folder (define `output.directory`) with the results of the evaluation.

# Knit your HTML report

Just set up the parameters `function.directory`, `data.directory`, `output.directory`, `Name`and `Platform` and press **Knit**. If you have already run this markdown and all the .RData files were created, change the `rerun` parameter to FALSE and it will skip re-doing all the calculations.
