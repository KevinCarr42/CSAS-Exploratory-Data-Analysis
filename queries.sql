SELECT * FROM csas2_csasrequest;

SELECT * FROM csas2_process
    JOIN csas2_csasoffice ON csas2_process.lead_office_id = csas2_csasoffice.id
    JOIN shared_models_region ON csas2_csasoffice.region_id = shared_models_region.id;

SELECT * FROM csas2_csasoffice;
SELECT * FROM shared_models_region;

SELECT * FROM csas2_csasrequestreview;

SELECT * FROM csas2_termsofreference;

SELECT * FROM csas2_meeting;

SELECT * FROM csas2_invitee;

SELECT * FROM csas2_document
    JOIN csas2_documenttype ON csas2_document.document_type_id = csas2_documenttype.id;

SELECT * FROM csas2_document
    JOIN csas2_documenttype ON csas2_document.document_type_id = csas2_documenttype.id
    JOIN csas2_documenttracking ON csas2_documenttracking.document_id = csas2_document.id;

SELECT * FROM csas2_documenttracking LIMIT 1;

SELECT * FROM csas2_changelog;
SELECT DISTINCT(model_name) FROM csas2_changelog;
