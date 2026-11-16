# Lecture 12 — Files, file dialogs, and drag-and-drop

Ten standalone PyQt5 programs, following the `startWindow`, `init_ui()`, signal/slot,
and Korean-comment style of the previous lecture folders. Run them in order;
each file works independently.

## Run

Use the Python environment you used for previous weeks (with PyQt5 installed).
From `workspace`:

```sh
python lec12/1.read_file.py
python lec12/8.drag_drop_file.py
```

On this Mac, the existing environment can be used directly:

```sh
.venv_mac/bin/python lec12/1.read_file.py
```

For a new environment, install the dependency with `python -m pip install PyQt5`.
Sample paths are based on `__file__`, so running from another directory also works.

## Programs

| # | File | Main concept | Try it |
|---|---|---|---|
| 1 | `1.read_file.py` | `open(..., 'r')`, `with`, `read()`, UTF-8 | Read the bundled English/Korean text. |
| 2 | `2.write_append_file.py` | `'w'` replaces; `'a'` appends; `write()` | Write once, change the text, then append twice. |
| 3 | `3.file_select.py` | `getOpenFileName()`, filters, returned tuple | Select a file, then try Cancel. |
| 4 | `4.multiple_file_select.py` | `getOpenFileNames()`, list of paths | Select both sample files with Ctrl/Cmd or Shift. |
| 5 | `5.open_text_file.py` | Select a path, then read its contents | Open a sample file; try a non-text file. |
| 6 | `6.save_text_file.py` | `getSaveFileName()`, `toPlainText()`, UTF-8 write | Save as `note.txt`, then open it with example 5. |
| 7 | `7.select_folder.py` | `getExistingDirectory()`, `Path.iterdir()` | Select `lec12/samples` and inspect the listing. |
| 8 | `8.drag_drop_file.py` | `setAcceptDrops()`, drag/drop events, local URLs | Drag one or several files from Explorer/Finder. |
| 9 | `9.drag_drop_text.py` | `setDragEnabled()`, `hasText()`, `text()` | Select words in the input, then drag the selection onto the box. |
| 10 | `10.drag_drop_image.py` | File drop + `QPixmap`, aspect-ratio scaling | Drop `workspace/assets/image.png`, then resize the window. |

## Teaching points

- A file dialog returns a path. It does not read or write the file for you.
- One-file and save dialogs return `(path, selected_filter)`; the multiple-file
  dialog returns `(paths, selected_filter)`. Folder selection returns a single string.
- Cancel returns an empty path or list. Check it before opening a file.
- Example 2 creates `lec12/output/notes.txt` on the first write or append. Write
  asks before replacing existing contents; append preserves them. Generated output
  is ignored by Git. The bundled samples are separate from this output.
- Example 5 previews UTF-8 / UTF-8-with-BOM files up to 1 MB. A file filter only
  changes the dialog listing; it does not validate the contents. Read errors appear
  in a message box and keep the previous preview.
- Example 6 is a focused Save As exercise: save before closing. The standard save
  dialog confirms replacement of an existing file. Include the desired extension
  in the filename, such as `note.txt`.
- Drag-and-drop sequence: `setAcceptDrops(True)` → `dragEnterEvent()` accepts
  supported data → `dropEvent()` reads `event.mimeData()`.
- File drops provide URLs. Use `isLocalFile()` and `toLocalFile()` to handle local
  paths, including spaces and Korean names. Example 8 ignores folders and web URLs.
- URLs can also advertise text. Example 9 excludes URLs to demonstrate plain-text
  drops separately. Start by selecting text, release the mouse, then press and hold
  on the selection to drag it.
- Examples 8–10 respond with `Qt.CopyAction` and only display paths, text, or an
  image preview. They do not move files or write copies to disk.
- Example 10 accepts one local PNG/JPG/JPEG/BMP/GIF file at a time. It checks that
  the image can actually be decoded and keeps the original pixmap for resizing.

## Small student activities

1. Before running example 2, predict the saved contents after Write → Append → Append.
2. Change example 3's filter to show Python files only. Does selecting a file read it?
3. Combine examples 5 and 8: read and preview the first dropped UTF-8 text file.
4. Add a Clear button to the drop examples using the signal/slot pattern from earlier weeks.

Qt references: [file dialogs](https://doc.qt.io/qt-6.8/qfiledialog.html),
[file-drop URL handling](https://wiki.qt.io/Drag_and_Drop_of_files).
The dialog reference describes Qt's shared behavior; the examples use PyQt5's
Python return values and the PyQt5 version already used in this workspace.
