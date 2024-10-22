# Generated by Django 5.1.2 on 2024-10-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_alter_language_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=models.CharField(choices=[('abap', 'abap'), ('amdgpu', 'amdgpu'), ('apl', 'apl'), ('abnf', 'abnf'), ('actionscript3', 'actionscript3'), ('actionscript', 'actionscript'), ('ada', 'ada'), ('adl', 'adl'), ('agda', 'agda'), ('aheui', 'aheui'), ('alloy', 'alloy'), ('ambienttalk', 'ambienttalk'), ('ampl', 'ampl'), ('html+angular2', 'html+angular2'), ('angular2', 'angular2'), ('antlrwithactionscripttarget', 'antlrwithactionscripttarget'), ('antlrwithc#target', 'antlrwithc#target'), ('antlrwithcpptarget', 'antlrwithcpptarget'), ('antlrwithjavatarget', 'antlrwithjavatarget'), ('antlr', 'antlr'), ('antlrwithobjectivectarget', 'antlrwithobjectivectarget'), ('antlrwithperltarget', 'antlrwithperltarget'), ('antlrwithpythontarget', 'antlrwithpythontarget'), ('antlrwithrubytarget', 'antlrwithrubytarget'), ('apacheconf', 'apacheconf'), ('applescript', 'applescript'), ('arduino', 'arduino'), ('arrow', 'arrow'), ('arturo', 'arturo'), ('asciiarmored', 'asciiarmored'), ('asn.1', 'asn.1'), ('aspectj', 'aspectj'), ('asymptote', 'asymptote'), ('augeas', 'augeas'), ('autoit', 'autoit'), ('autohotkey', 'autohotkey'), ('awk', 'awk'), ('bbcbasic', 'bbcbasic'), ('bbcode', 'bbcode'), ('bc', 'bc'), ('bqn', 'bqn'), ('bst', 'bst'), ('bare', 'bare'), ('basemakefile', 'basemakefile'), ('bash', 'bash'), ('bashsession', 'bashsession'), ('batchfile', 'batchfile'), ('bdd', 'bdd'), ('befunge', 'befunge'), ('berry', 'berry'), ('bibtex', 'bibtex'), ('blitzbasic', 'blitzbasic'), ('blitzmax', 'blitzmax'), ('blueprint', 'blueprint'), ('bnf', 'bnf'), ('boa', 'boa'), ('boo', 'boo'), ('boogie', 'boogie'), ('brainfuck', 'brainfuck'), ('bugs', 'bugs'), ('camkes', 'camkes'), ('c', 'c'), ('cmake', 'cmake'), ('c-objdump', 'c-objdump'), ('cpsa', 'cpsa'), ('css+ul4', 'css+ul4'), ('aspx-cs', 'aspx-cs'), ('c#', 'c#'), ('ca65assembler', 'ca65assembler'), ('cadl', 'cadl'), ('capdl', 'capdl'), ("cap'nproto", "cap'nproto"), ('carbon', 'carbon'), ('cbmbasicv2', 'cbmbasicv2'), ('cddl', 'cddl'), ('ceylon', 'ceylon'), ('cfengine3', 'cfengine3'), ('chaiscript', 'chaiscript'), ('chapel', 'chapel'), ('charmci', 'charmci'), ('html+cheetah', 'html+cheetah'), ('javascript+cheetah', 'javascript+cheetah'), ('cheetah', 'cheetah'), ('xml+cheetah', 'xml+cheetah'), ('cirru', 'cirru'), ('clay', 'clay'), ('clean', 'clean'), ('clojure', 'clojure'), ('clojurescript', 'clojurescript'), ('cobolfree', 'cobolfree'), ('cobol', 'cobol'), ('coffeescript', 'coffeescript'), ('coldfusioncfc', 'coldfusioncfc'), ('coldfusionhtml', 'coldfusionhtml'), ('cfstatement', 'cfstatement'), ('comal-80', 'comal-80'), ('commonlisp', 'commonlisp'), ('componentpascal', 'componentpascal'), ('coq', 'coq'), ('cplint', 'cplint'), ('c++', 'c++'), ('cpp-objdump', 'cpp-objdump'), ('crmsh', 'crmsh'), ('croc', 'croc'), ('cryptol', 'cryptol'), ('crystal', 'crystal'), ('csounddocument', 'csounddocument'), ('csoundorchestra', 'csoundorchestra'), ('csoundscore', 'csoundscore'), ('css+django/jinja', 'css+django/jinja'), ('css+ruby', 'css+ruby'), ('css+genshitext', 'css+genshitext'), ('css', 'css'), ('css+php', 'css+php'), ('css+smarty', 'css+smarty'), ('cuda', 'cuda'), ('cypher', 'cypher'), ('cython', 'cython'), ('d', 'd'), ('d-objdump', 'd-objdump'), ('darcspatch', 'darcspatch'), ('dart', 'dart'), ('dasm16', 'dasm16'), ('dax', 'dax'), ('debiancontrolfile', 'debiancontrolfile'), ('delphi', 'delphi'), ('desktopfile', 'desktopfile'), ('devicetree', 'devicetree'), ('dg', 'dg'), ('diff', 'diff'), ('django/jinja', 'django/jinja'), ('zone', 'zone'), ('docker', 'docker'), ('dtd', 'dtd'), ('duel', 'duel'), ('dylansession', 'dylansession'), ('dylan', 'dylan'), ('dylanlid', 'dylanlid'), ('ecl', 'ecl'), ('ec', 'ec'), ('earlgrey', 'earlgrey'), ('easytrieve', 'easytrieve'), ('ebnf', 'ebnf'), ('eiffel', 'eiffel'), ('elixiriexsession', 'elixiriexsession'), ('elixir', 'elixir'), ('elm', 'elm'), ('elpi', 'elpi'), ('emacslisp', 'emacslisp'), ('e-mail', 'e-mail'), ('erb', 'erb'), ('erlang', 'erlang'), ('erlangerlsession', 'erlangerlsession'), ('html+evoque', 'html+evoque'), ('evoque', 'evoque'), ('xml+evoque', 'xml+evoque'), ('execline', 'execline'), ('ezhil', 'ezhil'), ('f#', 'f#'), ('fstar', 'fstar'), ('factor', 'factor'), ('fancy', 'fancy'), ('fantom', 'fantom'), ('felix', 'felix'), ('fennel', 'fennel'), ('fift', 'fift'), ('fish', 'fish'), ('flatline', 'flatline'), ('floscript', 'floscript'), ('forth', 'forth'), ('fortranfixed', 'fortranfixed'), ('fortran', 'fortran'), ('foxpro', 'foxpro'), ('freefem', 'freefem'), ('func', 'func'), ('futhark', 'futhark'), ('gapsession', 'gapsession'), ('gap', 'gap'), ('gdscript', 'gdscript'), ('glsl', 'glsl'), ('gsql', 'gsql'), ('gas', 'gas'), ('g-code', 'g-code'), ('genshi', 'genshi'), ('genshitext', 'genshitext'), ('gettextcatalog', 'gettextcatalog'), ('gherkin', 'gherkin'), ('gnuplot', 'gnuplot'), ('go', 'go'), ('golo', 'golo'), ('gooddata-cl', 'gooddata-cl'), ('gosu', 'gosu'), ('gosutemplate', 'gosutemplate'), ('graphql', 'graphql'), ('graphviz', 'graphviz'), ('groff', 'groff'), ('groovy', 'groovy'), ('hlsl', 'hlsl'), ('html+ul4', 'html+ul4'), ('haml', 'haml'), ('html+handlebars', 'html+handlebars'), ('handlebars', 'handlebars'), ('haskell', 'haskell'), ('haxe', 'haxe'), ('hexdump', 'hexdump'), ('hsail', 'hsail'), ('hspec', 'hspec'), ('html+django/jinja', 'html+django/jinja'), ('html+genshi', 'html+genshi'), ('html', 'html'), ('html+php', 'html+php'), ('html+smarty', 'html+smarty'), ('http', 'http'), ('hxml', 'hxml'), ('hy', 'hy'), ('hybris', 'hybris'), ('idl', 'idl'), ('icon', 'icon'), ('idris', 'idris'), ('igor', 'igor'), ('inform6', 'inform6'), ('inform6template', 'inform6template'), ('inform7', 'inform7'), ('ini', 'ini'), ('io', 'io'), ('ioke', 'ioke'), ('irclogs', 'irclogs'), ('isabelle', 'isabelle'), ('j', 'j'), ('jmespath', 'jmespath'), ('jslt', 'jslt'), ('jags', 'jags'), ('janet', 'janet'), ('jasmin', 'jasmin'), ('java', 'java'), ('javascript+django/jinja', 'javascript+django/jinja'), ('javascript+ruby', 'javascript+ruby'), ('javascript+genshitext', 'javascript+genshitext'), ('javascript', 'javascript'), ('javascript+php', 'javascript+php'), ('javascript+smarty', 'javascript+smarty'), ('javascript+ul4', 'javascript+ul4'), ('jcl', 'jcl'), ('jsgf', 'jsgf'), ('jsonbareobject', 'jsonbareobject'), ('json-ld', 'json-ld'), ('json', 'json'), ('jsonnet', 'jsonnet'), ('javaserverpage', 'javaserverpage'), ('jsx', 'jsx'), ('juliaconsole', 'juliaconsole'), ('julia', 'julia'), ('juttle', 'juttle'), ('k', 'k'), ('kal', 'kal'), ('kconfig', 'kconfig'), ('kernellog', 'kernellog'), ('koka', 'koka'), ('kotlin', 'kotlin'), ('kuin', 'kuin'), ('kusto', 'kusto'), ('lsl', 'lsl'), ('css+lasso', 'css+lasso'), ('html+lasso', 'html+lasso'), ('javascript+lasso', 'javascript+lasso'), ('lasso', 'lasso'), ('xml+lasso', 'xml+lasso'), ('ldapconfigurationfile', 'ldapconfigurationfile'), ('ldif', 'ldif'), ('lean', 'lean'), ('lean4', 'lean4'), ('lesscss', 'lesscss'), ('lighttpdconfigurationfile', 'lighttpdconfigurationfile'), ('lilypond', 'lilypond'), ('limbo', 'limbo'), ('liquid', 'liquid'), ('literateagda', 'literateagda'), ('literatecryptol', 'literatecryptol'), ('literatehaskell', 'literatehaskell'), ('literateidris', 'literateidris'), ('livescript', 'livescript'), ('llvm', 'llvm'), ('llvm-mirbody', 'llvm-mirbody'), ('llvm-mir', 'llvm-mir'), ('logos', 'logos'), ('logtalk', 'logtalk'), ('lua', 'lua'), ('luau', 'luau'), ('mcfunction', 'mcfunction'), ('mcschema', 'mcschema'), ('mime', 'mime'), ('mips', 'mips'), ('moocode', 'moocode'), ('msdossession', 'msdossession'), ('macaulay2', 'macaulay2'), ('makefile', 'makefile'), ('css+mako', 'css+mako'), ('html+mako', 'html+mako'), ('javascript+mako', 'javascript+mako'), ('mako', 'mako'), ('xml+mako', 'xml+mako'), ('maql', 'maql'), ('markdown', 'markdown'), ('mask', 'mask'), ('mason', 'mason'), ('mathematica', 'mathematica'), ('matlab', 'matlab'), ('matlabsession', 'matlabsession'), ('maxima', 'maxima'), ('meson', 'meson'), ('minid', 'minid'), ('miniscript', 'miniscript'), ('modelica', 'modelica'), ('modula-2', 'modula-2'), ('moinmoin/tracwikimarkup', 'moinmoin/tracwikimarkup'), ('mojo', 'mojo'), ('monkey', 'monkey'), ('monte', 'monte'), ('moonscript', 'moonscript'), ('mosel', 'mosel'), ('css+mozpreproc', 'css+mozpreproc'), ('mozhashpreproc', 'mozhashpreproc'), ('javascript+mozpreproc', 'javascript+mozpreproc'), ('mozpercentpreproc', 'mozpercentpreproc'), ('xul+mozpreproc', 'xul+mozpreproc'), ('mql', 'mql'), ('mscgen', 'mscgen'), ('mupad', 'mupad'), ('mxml', 'mxml'), ('mysql', 'mysql'), ('css+myghty', 'css+myghty'), ('html+myghty', 'html+myghty'), ('javascript+myghty', 'javascript+myghty'), ('myghty', 'myghty'), ('xml+myghty', 'xml+myghty'), ('ncl', 'ncl'), ('nsis', 'nsis'), ('nasm', 'nasm'), ('objdump-nasm', 'objdump-nasm'), ('nemerle', 'nemerle'), ('nesc', 'nesc'), ('nestedtext', 'nestedtext'), ('newlisp', 'newlisp'), ('newspeak', 'newspeak'), ('nginxconfigurationfile', 'nginxconfigurationfile'), ('nimrod', 'nimrod'), ('nit', 'nit'), ('nix', 'nix'), ('node.jsreplconsolesession', 'node.jsreplconsolesession'), ('notmuch', 'notmuch'), ('nusmv', 'nusmv'), ('numpy', 'numpy'), ('objdump', 'objdump'), ('objective-c', 'objective-c'), ('objective-c++', 'objective-c++'), ('objective-j', 'objective-j'), ('ocaml', 'ocaml'), ('octave', 'octave'), ('odin', 'odin'), ('omginterfacedefinitionlanguage', 'omginterfacedefinitionlanguage'), ('ooc', 'ooc'), ('opa', 'opa'), ('openedgeabl', 'openedgeabl'), ('openscad', 'openscad'), ('orgmode', 'orgmode'), ('textoutput', 'textoutput'), ('pacmanconf', 'pacmanconf'), ('pan', 'pan'), ('parasail', 'parasail'), ('pawn', 'pawn'), ('peg', 'peg'), ('perl6', 'perl6'), ('perl', 'perl'), ('phix', 'phix'), ('php', 'php'), ('pig', 'pig'), ('pike', 'pike'), ('pkgconfig', 'pkgconfig'), ('pl/pgsql', 'pl/pgsql'), ('pointless', 'pointless'), ('pony', 'pony'), ('portugol', 'portugol'), ('postscript', 'postscript'), ('postgresqlconsole(psql)', 'postgresqlconsole(psql)'), ('postgresqlexplaindialect', 'postgresqlexplaindialect'), ('postgresqlsqldialect', 'postgresqlsqldialect'), ('povray', 'povray'), ('powershell', 'powershell'), ('powershellsession', 'powershellsession'), ('praat', 'praat'), ('procfile', 'procfile'), ('prolog', 'prolog'), ('promql', 'promql'), ('promela', 'promela'), ('properties', 'properties'), ('protocolbuffer', 'protocolbuffer'), ('prql', 'prql'), ('psyshconsolesessionforphp', 'psyshconsolesessionforphp'), ('ptx', 'ptx'), ('pug', 'pug'), ('puppet', 'puppet'), ('pypylog', 'pypylog'), ('python2.x', 'python2.x'), ('python2.xtraceback', 'python2.xtraceback'), ('pythonconsolesession', 'pythonconsolesession'), ('python', 'python'), ('pythontraceback', 'pythontraceback'), ('python+ul4', 'python+ul4'), ('qbasic', 'qbasic'), ('q', 'q'), ('qvto', 'qvto'), ('qlik', 'qlik'), ('qml', 'qml'), ('rconsole', 'rconsole'), ('relax-ngcompact', 'relax-ngcompact'), ('rpmspec', 'rpmspec'), ('racket', 'racket'), ('ragelinchost', 'ragelinchost'), ('ragelincpphost', 'ragelincpphost'), ('ragelindhost', 'ragelindhost'), ('embeddedragel', 'embeddedragel'), ('ragelinjavahost', 'ragelinjavahost'), ('ragel', 'ragel'), ('ragelinobjectivechost', 'ragelinobjectivechost'), ('ragelinrubyhost', 'ragelinrubyhost'), ('rawtokendata', 'rawtokendata'), ('rd', 'rd'), ('reasonml', 'reasonml'), ('rebol', 'rebol'), ('red', 'red'), ('redcode', 'redcode'), ('reg', 'reg'), ('resourcebundle', 'resourcebundle'), ('rexx', 'rexx'), ('rhtml', 'rhtml'), ('ride', 'ride'), ('rita', 'rita'), ('roboconfgraph', 'roboconfgraph'), ('roboconfinstances', 'roboconfinstances'), ('robotframework', 'robotframework'), ('rql', 'rql'), ('rsl', 'rsl'), ('restructuredtext', 'restructuredtext'), ('trafficscript', 'trafficscript'), ('rubyirbsession', 'rubyirbsession'), ('ruby', 'ruby'), ('rust', 'rust'), ('sas', 'sas'), ('s', 's'), ('standardml', 'standardml'), ('snbt', 'snbt'), ('sarl', 'sarl'), ('sass', 'sass'), ('savi', 'savi'), ('scala', 'scala'), ('scaml', 'scaml'), ('scdoc', 'scdoc'), ('scheme', 'scheme'), ('scilab', 'scilab'), ('scss', 'scss'), ('sed', 'sed'), ('shexc', 'shexc'), ('shen', 'shen'), ('sieve', 'sieve'), ('silver', 'silver'), ('singularity', 'singularity'), ('slash', 'slash'), ('slim', 'slim'), ('slurm', 'slurm'), ('smali', 'smali'), ('smalltalk', 'smalltalk'), ('smartgameformat', 'smartgameformat'), ('smarty', 'smarty'), ('smithy', 'smithy'), ('snobol', 'snobol'), ('snowball', 'snowball'), ('solidity', 'solidity'), ('soong', 'soong'), ('sophia', 'sophia'), ('sourcepawn', 'sourcepawn'), ('debiansourcelist', 'debiansourcelist'), ('sparql', 'sparql'), ('spice', 'spice'), ('sql+jinja', 'sql+jinja'), ('sql', 'sql'), ('sqlite3con', 'sqlite3con'), ('squidconf', 'squidconf'), ('srcinfo', 'srcinfo'), ('scalateserverpage', 'scalateserverpage'), ('stan', 'stan'), ('stata', 'stata'), ('supercollider', 'supercollider'), ('swift', 'swift'), ('swig', 'swig'), ('systemverilog', 'systemverilog'), ('systemd', 'systemd'), ('tap', 'tap'), ('typographicnumbertheory', 'typographicnumbertheory'), ('toml', 'toml'), ('tact', 'tact'), ('tads3', 'tads3'), ('tal', 'tal'), ('tasm', 'tasm'), ('tcl', 'tcl'), ('tcsh', 'tcsh'), ('tcshsession', 'tcshsession'), ('tea', 'tea'), ('teal', 'teal'), ('teratermmacro', 'teratermmacro'), ('termcap', 'termcap'), ('terminfo', 'terminfo'), ('terraform', 'terraform'), ('tex', 'tex'), ('textonly', 'textonly'), ('thingsdb', 'thingsdb'), ('thrift', 'thrift'), ('tiddler', 'tiddler'), ('tl-b', 'tl-b'), ('tlspresentationlanguage', 'tlspresentationlanguage'), ('todotxt', 'todotxt'), ('transact-sql', 'transact-sql'), ('treetop', 'treetop'), ('turtle', 'turtle'), ('html+twig', 'html+twig'), ('twig', 'twig'), ('typescript', 'typescript'), ('typoscriptcssdata', 'typoscriptcssdata'), ('typoscripthtmldata', 'typoscripthtmldata'), ('typoscript', 'typoscript'), ('typst', 'typst'), ('ul4', 'ul4'), ('ucode', 'ucode'), ('unicon', 'unicon'), ('unix/linuxconfigfiles', 'unix/linuxconfigfiles'), ('urbiscript', 'urbiscript'), ('urlencoded', 'urlencoded'), ('usd', 'usd'), ('vbscript', 'vbscript'), ('vcl', 'vcl'), ('vclsnippets', 'vclsnippets'), ('vctreestatus', 'vctreestatus'), ('vgl', 'vgl'), ('vala', 'vala'), ('aspx-vb', 'aspx-vb'), ('vb.net', 'vb.net'), ('html+velocity', 'html+velocity'), ('velocity', 'velocity'), ('xml+velocity', 'xml+velocity'), ('verifpal', 'verifpal'), ('verilog', 'verilog'), ('vhdl', 'vhdl'), ('viml', 'viml'), ('visualprologgrammar', 'visualprologgrammar'), ('visualprolog', 'visualprolog'), ('vyper', 'vyper'), ('wdiff', 'wdiff'), ('webassembly', 'webassembly'), ('webidl', 'webidl'), ('webgpushadinglanguage', 'webgpushadinglanguage'), ('whiley', 'whiley'), ('wikitext', 'wikitext'), ('worldofwarcrafttoc', 'worldofwarcrafttoc'), ('wren', 'wren'), ('x10', 'x10'), ('xml+ul4', 'xml+ul4'), ('xquery', 'xquery'), ('xml+django/jinja', 'xml+django/jinja'), ('xml+ruby', 'xml+ruby'), ('xml', 'xml'), ('xml+php', 'xml+php'), ('xml+smarty', 'xml+smarty'), ('xorg', 'xorg'), ('x++', 'x++'), ('xslt', 'xslt'), ('xtend', 'xtend'), ('xtlang', 'xtlang'), ('yaml+jinja', 'yaml+jinja'), ('yaml', 'yaml'), ('yang', 'yang'), ('yara', 'yara'), ('zeek', 'zeek'), ('zephir', 'zephir'), ('zig', 'zig'), ('ansysparametricdesignlanguage', 'ansysparametricdesignlanguage')], max_length=50),
        ),
    ]