SELECT * FROM csas2_document
    JOIN csas2_documenttype ON csas2_document.document_type_id = csas2_documenttype.id;

SELECT * FROM csas2_process
    JOIN csas2_csasoffice ON csas2_process.lead_office_id = csas2_csasoffice.id
    JOIN shared_models_region ON csas2_csasoffice.region_id = shared_models_region.id;




