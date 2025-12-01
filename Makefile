prepare:
	python prepare_dataset.py

clean_data:
	mkdir -p data_clean
	for f in data/*.txt; do \
	base=$$(basename $$f); \
	python remove_stopwords.py data/$$base data_clean/$$base; \
	done

index:
	mkdir -p index
	awk -f build_index.awk data_clean/*.txt

run:
	python search_engine.py

clean:
	rm -rf data_clean index
