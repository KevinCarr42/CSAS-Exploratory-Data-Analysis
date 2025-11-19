# Meeting Summary - Technical Details & Documentation

## Phase 1: Evaluation & Planning

### File Inventory
Located in: `C:\Users\CARRK\Documents\Repositories\dm_apps_root\csas_eda\sept_24_coordinators_meeting\`

**File Count**: 12 files
- **Word Documents (.docx)**: 6 files
  - Centralization of web and publication.docx
  - Coordinators F2F Agenda.docx
  - F2F Action Items.docx
  - F2F Meeting Notes (draft).docx
  - F2F Meeting Report (near final).docx
  - F2F Meeting Report (near final)_TG_FR_LS_Final.docx
  - Options and best practices for timely publication v2.docx
- **PowerPoint Presentations (.pptx)**: 5 files
  - CSAS Publications.pptx
  - CSAS Transformation update.pptx
  - CSAS Transformation update-FR.pptx (French version)
  - Process vs Product.pptx
  - Survival exercise.pptx

**Known Content Characteristics**:
- Bilingual content (English and French)
- Draft/incomplete documents with editorial comments
- Mix of formal reports and working documents
- Some redundancy expected (multiple versions of reports)

### Parsing Strategy

#### Word Documents (.docx)
- **Tool**: Python `python-docx` library
- **Approach**: Extract paragraphs with hierarchy (headings, body text, lists)
- **Challenges**:
  - Comments may be embedded; need separate extraction
  - Mixed languages; may need to detect language per paragraph
  - Track document version/date from filename

#### PowerPoint Presentations (.pptx)
- **Tool**: Python `python-pptx` library
- **Approach**: Extract slide text, notes, and speaker notes
- **Challenges**:
  - Text may be in shapes, text boxes, or grouped elements
  - Slide order may not reflect logical flow
  - Tables and diagrams need special handling

#### Output Format
- Primary storage: Pandas DataFrames
- Index columns: `source_file`, `source_type`, `section`, `language`
- Data columns: `text`, `element_type` (heading, body, list, table, etc.), `confidence`

### Tools & Dependencies Required

```
python-docx     # Extract from .docx
python-pptx     # Extract from .pptx
pandas          # Data organization and manipulation
langdetect      # Language detection (French vs English)
openpyxl        # Potential export to Excel for review
```

### Known Issues & Constraints

1. **Bilingual Content**: Will need language detection to separate or identify translations
2. **Draft Status**: Some text may be incomplete; will need to mark uncertainty
3. **Comments**: May need to extract and differentiate from body text
4. **Redundancy**: Multiple report versions (near final, final) - will need deduplication
5. **French Version**: `CSAS Transformation update-FR.pptx` - likely duplicate of English version

### Parsing Permissions

- ✅ Read file contents using python libraries
- ✅ Create temporary files for processing
- ✅ Use language detection to identify French/English
- ✅ Extract and organize all text content
- ✅ Create DataFrames for analysis
- ✅ Export to intermediate formats (CSV, pickle) for processing

### Decision Log

**Decision 1**: Use python-docx and python-pptx for extraction
- **Rationale**: Native Python libraries, minimal external dependencies, good for bilingual content
- **Date**: Initial planning phase

**Decision 2**: Primary output format = Pandas DataFrames
- **Rationale**: Allows flexible filtering, grouping, and analysis; can export to multiple formats
- **Date**: Initial planning phase

---

## Phase 2: Data Parsing

### Status: PENDING

### Extraction Workflow
1. Install dependencies
2. Extract from Word documents
3. Extract from PowerPoint presentations
4. Combine into master DataFrame
5. Validate extraction completeness

### Phase 3: Data Cleaning & Normalization

### Status: PENDING

### Cleaning Tasks
- [ ] Identify and mark incomplete/draft text
- [ ] Separate French and English content (or mark language)
- [ ] Extract and organize comments separately
- [ ] Normalize whitespace and line breaks
- [ ] Identify and flag duplicates across documents
- [ ] Create canonical versions of repeated items

### Phase 4: Iterative Refinement

### Status: PENDING

---

## Key Metrics & Success Criteria

- **Extraction Completeness**: >95% of readable text extracted
- **Data Quality**: <5% manual corrections needed after cleaning
- **Deduplication Accuracy**: All duplicates identified with confidence >80%
- **Language Detection**: Correct language identified for >99% of content

---

## Output Deliverables

1. **Raw Extraction**: DataFrame with all extracted text
2. **Cleaned Data**: Normalized, deduplicated, language-tagged
3. **Summary Reports**:
   - Key Points (by topic)
   - Points of Contention (with supporting evidence)
   - Action Items (with owner, timeline)
   - Follow-up Recommendations
4. **Data Quality Report**: Issues encountered and how they were resolved
5. **Visual Summary**: If applicable

---

## File Locations

- **Strategy Document**: `MEETING_SUMMARY_STRATEGY.md`
- **Technical Details**: `MEETING_SUMMARY_DETAILS.md` (this file)
- **Processing Notebook**: (to be created during Phase 2)
- **Source Documents**: `sept_24_coordinators_meeting/`
- **Output Directory**: (to be created - `meeting_summary_output/`)

