import re, io, sys
src = open('/mnt/user-data/uploads/TOEFL-Drill-Web/TOEFL-Drill-satu-berkas.html', encoding='utf-8').read()
orig = src

def rep(old, new, count=1):
    global src
    n = src.count(old)
    assert n == count, f"expected {count} occurrence(s), found {n}: {old[:80]!r}"
    src = src.replace(old, new)

# ---- 1. strip document skeleton (Artifact supplies it) ----
for tag in ['<!DOCTYPE html>\n', '<html lang="id">\n', '<head>\n', '</head>\n',
            '<body>\n', '</body>\n', '</html>\n',
            '<meta charset="utf-8">\n',
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n']:
    rep(tag, '')

# ---- 2. dialog + toast styles, appended to the main stylesheet ----
EXTRA_CSS = """
/* ---------- dialog & toast (pengganti alert/confirm di halaman terbit) ---------- */
.ovl{position:fixed;inset:0;z-index:200;background:color-mix(in oklab, var(--ink) 42%, transparent);
  backdrop-filter:blur(3px);display:grid;place-items:center;padding:24px;animation:fadein .14s ease}
@keyframes fadein{from{opacity:0}to{opacity:1}}
.mdl{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);
  box-shadow:var(--shadow-lg);padding:26px 28px;max-width:520px;width:100%;animation:pop .16s ease}
@keyframes pop{from{transform:translateY(8px) scale(.98);opacity:0}to{transform:none;opacity:1}}
.mdl p{margin:0;font-size:16.5px;line-height:1.6}
.mdl h3{font-family:var(--font-display);font-weight:400;font-size:21px;margin:0 0 10px}
.mdl textarea{margin-top:12px;min-height:150px;font:13px/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%);z-index:210;
  background:var(--ink);color:var(--bg);border-radius:999px;padding:12px 22px;
  font:600 14.5px/1.3 var(--font-body);box-shadow:var(--shadow-lg);max-width:min(90vw,520px);
  text-align:center;animation:pop .16s ease}
</style>"""
rep('  padding:15px 18px;font-size:14px;line-height:1.6;margin:20px 0;max-width:70ch\n}\n</style>',
    '  padding:15px 18px;font-size:14px;line-height:1.6;margin:20px 0;max-width:70ch\n}\n' + EXTRA_CSS)

# ---- 3. helper script, injected just before the app script ----
HELPERS = """<script>
/* ============================================================
   DIALOG — halaman terbit berjalan di dalam bingkai yang memblokir
   alert()/confirm() bawaan, jadi dipakai dialog sendiri.
   ============================================================ */
function ask(msg, onYes, yesLabel){
  var ov = document.createElement('div'); ov.className = 'ovl';
  var box = document.createElement('div'); box.className = 'mdl';
  var p = document.createElement('p'); p.textContent = msg;
  var row = document.createElement('div');
  row.className = 'row'; row.style.cssText = 'justify-content:flex-end;margin-top:20px';
  var no = document.createElement('button'); no.className = 'btn ghost'; no.textContent = 'Batal';
  var yes = document.createElement('button'); yes.className = 'btn'; yes.textContent = yesLabel || 'Ya';
  row.appendChild(no); row.appendChild(yes);
  box.appendChild(p); box.appendChild(row); ov.appendChild(box);
  function close(){ if(ov.parentNode) ov.parentNode.removeChild(ov); document.removeEventListener('keydown', esc, true); }
  function esc(e){ if(e.key === 'Escape'){ e.stopPropagation(); close(); } }
  no.onclick = close;
  yes.onclick = function(){ close(); onYes(); };
  ov.onclick = function(e){ if(e.target === ov) close(); };
  document.addEventListener('keydown', esc, true);
  document.body.appendChild(ov); yes.focus();
}
function toast(msg){
  var t = document.createElement('div'); t.className = 'toast'; t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(function(){ if(t.parentNode) t.parentNode.removeChild(t); }, 2600);
}
</script>

"""
MARKER = '<script>\n/* ============================================================\n   TEMA'
rep(MARKER, HELPERS + MARKER)

# ---- 4. confirm() -> ask() ----
rep("function dropSess(){ if(confirm('Buang sesi yang belum selesai itu?')){ clearSess(); SESS=null; render(); } }",
    "function dropSess(){ ask('Buang sesi yang belum selesai itu?', function(){ clearSess(); SESS=null; render(); }, 'Buang'); }")

rep("  if(confirm('Keluar dulu? Sesi ini disimpan dan bisa dilanjutkan dari beranda.')) go('home');",
    "  ask('Keluar dulu? Sesi ini disimpan dan bisa dilanjutkan dari beranda.', function(){ go('home'); }, 'Keluar');")

rep("""function finishSession(){
  saveOpenDraft();
  var left = SESS.list.length - countAnswered();
  if(left>0 && !confirm('Masih ada '+left+' soal yang belum dijawab. Selesaikan sesi sekarang?')) return;
  SESS.list.forEach(function(q,i){""",
    """function finishSession(){
  saveOpenDraft();
  var left = SESS.list.length - countAnswered();
  if(left>0){ ask('Masih ada '+left+' soal yang belum dijawab. Selesaikan sesi sekarang?', doFinish, 'Selesaikan'); return; }
  doFinish();
}
function doFinish(){
  SESS.list.forEach(function(q,i){""")

# ---- 5. alert() -> toast() ----
rep("if(!qs.length){ alert('Belum ada soal di bank yang cocok dengan topik ini.'); return; }",
    "if(!qs.length){ toast('Belum ada soal di bank yang cocok dengan topik ini.'); return; }")
rep("if(!pool.length){ alert('Tidak ada soal yang cocok dengan filter itu.'); return; }",
    "if(!pool.length){ toast('Tidak ada soal yang cocok dengan filter itu.'); return; }")

# ---- 6. progres: unduhan & pemilih berkas diblokir di halaman terbit -> salin/tempel teks ----
rep("""   +'<h2>Kelola</h2><div class="row">'
     +'<button class="btn ghost" onclick="exportProg()">Ekspor progres (.json)</button>'
     +'<button class="btn ghost" onclick="document.getElementById(\\'imp\\').click()">Impor progres</button>'
     +'<input type="file" id="imp" hidden accept=".json" onchange="importProg(this)">'
     +'<button class="btn ghost" onclick="if(confirm(\\'Hapus semua progres?\\')){store.set(\\'td_hist\\',{});store.set(\\'td_flags\\',[]);render()}">Reset progres</button>'
   +'</div>'
   +'<div class="notice">Kalau file ini dibuka langsung dari disk, sebagian browser memblokir penyimpanan otomatis. Pakai <b>Ekspor progres</b> sebelum menutup tab kalau kamu mau menyimpannya.</div>';""",
    """   +'<h2>Kelola</h2><div class="row">'
     +'<button class="btn ghost" onclick="exportProg()">Salin progres</button>'
     +'<button class="btn ghost" onclick="importProg()">Tempel progres</button>'
     +'<button class="btn ghost" onclick="ask(\\'Hapus semua progres?\\',function(){store.set(\\'td_hist\\',{});store.set(\\'td_flags\\',[]);render();toast(\\'Progres dihapus.\\')},\\'Hapus\\')">Reset progres</button>'
   +'</div>'
   +'<div class="notice">Progres tersimpan otomatis di browser ini. <b>Salin progres</b> memberi satu blok teks yang bisa kamu simpan sendiri, lalu <b>Tempel progres</b> memulihkannya di browser lain.</div>';""")

rep("""function exportProg(){
  var blob=new Blob([JSON.stringify({hist:S.hist,flags:S.flags},null,1)],{type:'application/json'});
  var a=document.createElement('a'); a.href=URL.createObjectURL(blob);
  a.download='progres-drill-'+new Date().toISOString().slice(0,10)+'.json'; a.click();
}
function importProg(inp){
  var f=inp.files[0]; if(!f) return; var r=new FileReader();
  r.onload=function(){ try{ var d=JSON.parse(r.result);
    if(d.hist) S.hist=d.hist; if(d.flags) S.flags=d.flags; render(); alert('Progres dimuat.');
  }catch(e){ alert('File tidak terbaca.'); } };
  r.readAsText(f);
}""",
    """function progModal(title, note, value, actionLabel, onAction){
  var ov=document.createElement('div'); ov.className='ovl';
  var box=document.createElement('div'); box.className='mdl';
  var h=document.createElement('h3'); h.textContent=title;
  var p=document.createElement('p'); p.className='small muted'; p.textContent=note;
  var ta=document.createElement('textarea'); ta.value=value; ta.spellcheck=false;
  var row=document.createElement('div'); row.className='row';
  row.style.cssText='justify-content:flex-end;margin-top:16px';
  var close=document.createElement('button'); close.className='btn ghost'; close.textContent='Tutup';
  var act=document.createElement('button'); act.className='btn'; act.textContent=actionLabel;
  row.appendChild(close); row.appendChild(act);
  box.appendChild(h); box.appendChild(p); box.appendChild(ta); box.appendChild(row);
  ov.appendChild(box);
  function shut(){ if(ov.parentNode) ov.parentNode.removeChild(ov); }
  close.onclick=shut;
  ov.onclick=function(e){ if(e.target===ov) shut(); };
  act.onclick=function(){ onAction(ta, shut); };
  document.body.appendChild(ov);
  ta.focus(); if(value) ta.select();
}
function exportProg(){
  var txt=JSON.stringify({hist:S.hist,flags:S.flags});
  progModal('Salin progres','Simpan teks ini di catatanmu. Tempelkan lagi lewat "Tempel progres" untuk memulihkannya.',
    txt,'Salin',function(ta,shut){
      ta.select();
      var done=false;
      try{ done=document.execCommand('copy'); }catch(e){}
      if(navigator.clipboard && !done){ navigator.clipboard.writeText(ta.value).then(function(){ shut(); toast('Progres disalin.'); },function(){ toast('Salin manual dengan Ctrl+C.'); }); return; }
      shut(); toast(done?'Progres disalin.':'Salin manual dengan Ctrl+C.');
    });
}
function importProg(){
  progModal('Tempel progres','Tempelkan teks progres yang pernah kamu salin, lalu tekan Muat.',
    '','Muat',function(ta,shut){
      try{
        var d=JSON.parse(ta.value);
        if(d.hist) S.hist=d.hist; if(d.flags) S.flags=d.flags;
        shut(); render(); toast('Progres dimuat.');
      }catch(e){ toast('Teks itu tidak terbaca.'); }
    });
}""")

assert '<!DOCTYPE' not in src and '</body>' not in src
bad=[l for l in src.split('\n') if ('confirm(' in l or 'alert(' in l) and 'bawaan' not in l]
assert not bad, bad
open('/home/claude/build/toefl-drill.html','w',encoding='utf-8').write(src)
print('ok', len(orig), '->', len(src))
