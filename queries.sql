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


-- document dates for FSAR data

SELECT
    document_id,
    csas2_document.title_en,
    csas2_document.title_fr,
    shared_models_region.name AS region,
    CONCAT(acronym_en, ' ', csas2_document.pub_number) AS pub_number,

    DATE_FORMAT(csas2_documenttracking.submission_date, '%Y-%m-%d') AS date_submitted_by_author,
    DATE_FORMAT(csas2_documenttracking.date_chair_sent, '%Y-%m-%d') AS date_sent_to_chair,
    DATE_FORMAT(csas2_documenttracking.date_chair_appr, '%Y-%m-%d') AS date_appr_by_chair,
    DATE_FORMAT(csas2_documenttracking.date_coordinator_sent, '%Y-%m-%d') AS date_sent_to_coordinator,
    DATE_FORMAT(csas2_documenttracking.date_coordinator_appr, '%Y-%m-%d') AS date_appr_by_coordinator,
    DATE_FORMAT(csas2_documenttracking.date_division_manager_sent, '%Y-%m-%d') AS date_sent_to_division_manager,
    DATE_FORMAT(csas2_documenttracking.date_division_manager_appr, '%Y-%m-%d') AS date_appr_by_division_manager,
    DATE_FORMAT(csas2_documenttracking.date_section_head_sent, '%Y-%m-%d') AS date_sent_to_section_head,
    DATE_FORMAT(csas2_documenttracking.date_section_head_appr, '%Y-%m-%d') AS date_appr_by_section_head,
    DATE_FORMAT(csas2_documenttracking.date_director_sent, '%Y-%m-%d') AS date_sent_to_director,
    DATE_FORMAT(csas2_documenttracking.date_director_appr, '%Y-%m-%d') AS date_appr_by_director,

    DATE_FORMAT(csas2_documenttracking.date_translation_sent, '%Y-%m-%d') AS date_translation_sent,
    DATE_FORMAT(csas2_documenttracking.anticipated_return_date, '%Y-%m-%d') AS anticipated_translation_return_date,
    DATE_FORMAT(csas2_documenttracking.date_returned, '%Y-%m-%d') AS date_returned_from_translation,
    DATE_FORMAT(csas2_documenttracking.translation_review_date, '%Y-%m-%d') AS translation_review_date,

    DATE_FORMAT(csas2_documenttracking.due_date, '%Y-%m-%d') AS publication_due_date,
    DATE_FORMAT(csas2_documenttracking.date_doc_submitted, '%Y-%m-%d') AS date_doc_submitted_for_publication,
    DATE_FORMAT(csas2_documenttracking.date_proof_author_sent, '%Y-%m-%d') AS date_proof_sent_to_author,
    DATE_FORMAT(csas2_documenttracking.date_proof_author_approved, '%Y-%m-%d') AS date_approved_by_proof_author,

    DATE_FORMAT(csas2_documenttracking.anticipated_posting_date, '%Y-%m-%d') AS anticipated_posting_date,
    DATE_FORMAT(csas2_documenttracking.actual_posting_date, '%Y-%m-%d') AS actual_posting_date,
    DATE_FORMAT(csas2_documenttracking.updated_posting_date, '%Y-%m-%d') AS updated_posting_date

FROM csas2_documenttracking
    JOIN csas2_document ON csas2_documenttracking.document_id = csas2_document.id
    JOIN csas2_documenttype ON csas2_document.document_type_id = csas2_documenttype.id
    JOIN csas2_process ON csas2_document.process_id = csas2_process.id
    JOIN csas2_csasoffice ON csas2_process.lead_office_id = csas2_csasoffice.id
    JOIN shared_models_region ON csas2_csasoffice.region_id = shared_models_region.id;


-- also with meetings

SELECT meeting_id FROM csas2_document
    LEFT JOIN csas2_document_meetings ON csas2_document_meetings.document_id = csas2_document.id
    JOIN csas2_meeting ON csas2_document_meetings.meeting_id = csas2_meeting.id;

SELECT
    csas2_documenttracking.document_id AS document_id,
    csas2_document.title_en,
    csas2_document.title_fr,
    shared_models_region.name AS region,
    CONCAT(acronym_en, ' ', csas2_document.pub_number) AS pub_number,

    csas2_meeting.id AS meeting_id,
    csas2_meeting.name AS meeting_name,
    csas2_meeting.nom AS meeting_nom,
    DATE_FORMAT(csas2_meeting.start_date, '%Y-%m-%d') AS meeting_start_date,
    DATE_FORMAT(csas2_meeting.end_date, '%Y-%m-%d') AS meeting_end_date,

    DATE_FORMAT(csas2_documenttracking.submission_date, '%Y-%m-%d') AS date_submitted_by_author,
    DATE_FORMAT(csas2_documenttracking.date_chair_sent, '%Y-%m-%d') AS date_sent_to_chair,
    DATE_FORMAT(csas2_documenttracking.date_chair_appr, '%Y-%m-%d') AS date_appr_by_chair,
    DATE_FORMAT(csas2_documenttracking.date_coordinator_sent, '%Y-%m-%d') AS date_sent_to_coordinator,
    DATE_FORMAT(csas2_documenttracking.date_coordinator_appr, '%Y-%m-%d') AS date_appr_by_coordinator,
    DATE_FORMAT(csas2_documenttracking.date_division_manager_sent, '%Y-%m-%d') AS date_sent_to_division_manager,
    DATE_FORMAT(csas2_documenttracking.date_division_manager_appr, '%Y-%m-%d') AS date_appr_by_division_manager,
    DATE_FORMAT(csas2_documenttracking.date_section_head_sent, '%Y-%m-%d') AS date_sent_to_section_head,
    DATE_FORMAT(csas2_documenttracking.date_section_head_appr, '%Y-%m-%d') AS date_appr_by_section_head,
    DATE_FORMAT(csas2_documenttracking.date_director_sent, '%Y-%m-%d') AS date_sent_to_director,
    DATE_FORMAT(csas2_documenttracking.date_director_appr, '%Y-%m-%d') AS date_appr_by_director,

    DATE_FORMAT(csas2_documenttracking.date_translation_sent, '%Y-%m-%d') AS date_translation_sent,
    DATE_FORMAT(csas2_documenttracking.anticipated_return_date, '%Y-%m-%d') AS anticipated_translation_return_date,
    DATE_FORMAT(csas2_documenttracking.date_returned, '%Y-%m-%d') AS date_returned_from_translation,
    DATE_FORMAT(csas2_documenttracking.translation_review_date, '%Y-%m-%d') AS translation_review_date,

    DATE_FORMAT(csas2_documenttracking.due_date, '%Y-%m-%d') AS publication_due_date,
    DATE_FORMAT(csas2_documenttracking.date_doc_submitted, '%Y-%m-%d') AS date_doc_submitted_for_publication,
    DATE_FORMAT(csas2_documenttracking.date_proof_author_sent, '%Y-%m-%d') AS date_proof_sent_to_author,
    DATE_FORMAT(csas2_documenttracking.date_proof_author_approved, '%Y-%m-%d') AS date_approved_by_proof_author,

    DATE_FORMAT(csas2_documenttracking.anticipated_posting_date, '%Y-%m-%d') AS anticipated_posting_date,
    DATE_FORMAT(csas2_documenttracking.actual_posting_date, '%Y-%m-%d') AS actual_posting_date,
    DATE_FORMAT(csas2_documenttracking.updated_posting_date, '%Y-%m-%d') AS updated_posting_date

FROM csas2_documenttracking
    JOIN csas2_document ON csas2_documenttracking.document_id = csas2_document.id
    JOIN csas2_documenttype ON csas2_document.document_type_id = csas2_documenttype.id
    JOIN csas2_process ON csas2_document.process_id = csas2_process.id
    JOIN csas2_csasoffice ON csas2_process.lead_office_id = csas2_csasoffice.id
    JOIN shared_models_region ON csas2_csasoffice.region_id = shared_models_region.id
    LEFT JOIN csas2_document_meetings ON csas2_document_meetings.document_id = csas2_document.id
    JOIN csas2_meeting ON csas2_document_meetings.meeting_id = csas2_meeting.id;
