prepare:
	python preparar_dataset.py

clean_data:
	mkdir -p data_clean
	for f in data/*.txt; do \
		python eliminar_stopwords.py "$$f" "data_clean/$$(basename "$$f")"; \
	done

index:
	mkdir -p index
	awk -f build_index.awk data_clean/*.txt

run:
	python motor_busqueda.py

clean:
	rm -rf data_clean
	rm -rf index
