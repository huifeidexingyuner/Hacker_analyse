# __author: DuZhen
# date: 2018/12/8
import json
from flashtext import KeywordProcessor
import random


def get_area(jsonname):
    '''
    file:param json_f open() return
    list:return top 10(<=10) random area/terms

    print term list:active

    json structure
    example
    {"user": "_py", "history": ["my name is duzhen", "I love re"]}
    '''
    terms_list = ['a*', 'a11y', 'abend', 'abstract class', 'abstract data type', 'abstraction', 'acceptance testing',
                  'accessibility', 'acme', 'actionscript', 'address resolution protocol (arp)',
                  'address space layout randomization', 'adger', 'afaict', 'agile', 'ajax', 'algebraic data type',
                  'algorithm', 'allocation', 'alpha', 'amd64', 'analog', 'android', 'angularjs', 'anonymous function',
                  'ansible', 'anti-pattern', 'apache lucene', 'apache pig', 'apache solr',
                  'api (application programming interface)', 'appcache', 'appkit', 'ar (augmented reality)',
                  'architecture', 'arguments', 'aria', 'arity', 'array', 'array list', 'arrow functions', 'asic',
                  'assembler', 'assembly language', 'assistive technology', 'associative array (php)',
                  'ast (abstract syntax tree)', 'asynchronous', 'atomic operation', 'authentication', 'authorization',
                  'auto id', 'awk', 'aws', 'axios', 'azure', 'ba (business analyst)', 'babel', 'back-end', 'backlog',
                  'backronym', 'backup', 'bag of words', 'bang', 'bar', 'bar code', 'barb', 'bash', 'basic', 'batch',
                  'baz', 'bc (backwards compatibility)', 'bc (business continuity)', 'best practice', 'beta',
                  'bi (business intelligence)', 'big bang', 'big data', 'big o', 'big-endian', 'bikeshedding', 'binary',
                  'binary search tree', 'binary tree', 'bit', 'bit bang', 'bit rot', 'bitbucket', 'bitcoin', 'bitmask',
                  'bitwise operators', 'black hat hacker', 'blender', 'blob (binary large object)', 'blockchain',
                  'bodge', 'bogon', 'bogosort', 'boilerplate code', 'boolean', 'bootstrap', 'borked', 'bot', 'botnet',
                  'bounce', 'bower', 'box', 'boxen', 'boyscouting', 'brackets (text editor)', 'brainfuck',
                  'branch and bound', 'brogrammer', 'browser', 'brute force', 'bsod', 'buffer', 'bug', 'build',
                  'build or buy', 'build out', 'build up', 'builder', 'bundler', 'byte', 'bytecode', 'c (language)',
                  'c#', 'c++', 'cache', 'call stack', 'callback', 'callback hell', 'calling a function',
                  'canvas (html)', 'captcha', 'cargo culting', 'carthage', 'cassandra', 'cast', 'category',
                  'category theory', 'cdn (content delivery network)', 'celery', 'change control management',
                  'changelog', 'checkout', 'chrome', 'chronicle queue', 'ci', 'circleci', 'cisc', 'clang', 'class',
                  'cli', 'client', 'client-server model', 'clobber', 'clojure', 'clone and go', 'closed source',
                  'closed-form expression', 'closure', 'cloud', 'cmd', 'cms (content management system)',
                  'cnd (content delivery network)', 'cobol', 'cochcarna', 'cocoa', 'code', 'code bloat', 'code debt',
                  'code monkey', 'code review', 'code rot', 'code smell', 'codeigniter', 'coffee', 'coffeescript',
                  'cohesion', 'cold site', 'colorzilla', 'command', 'commit (git)', 'compiled language', 'compiler',
                  'component', 'composer (php)', 'compression', 'computer appliance', 'computer language',
                  'concurrency', 'confluence', 'connascence', 'console', 'constant', 'constant time',
                  'continuous delivery', 'continuous deployment', 'continuous integration', 'contravariance',
                  'contravariant functor', 'convention over configuration', "conway's law", 'cookie', 'coq',
                  'core data', 'core memory', 'coroutine', 'coupling', 'covariance', 'cpq', 'cqrs', 'cqs',
                  'create-react-app', 'cron', 'cron job', 'cross-platform', 'crud (create, read, update, delete)',
                  'cruft', 'crystal', 'css', 'css framework', 'currying', 'cursor', 'cve', 'cyclomatic complexity',
                  'c艹', 'daemon', 'dag', 'dance of death', 'dart', 'data class', 'data dictionary', 'data race',
                  'data science', 'data store', 'data structure', 'data transfer object', 'database', 'ddd', 'ddos',
                  'deadlock', 'debugger', 'debugging', 'decimal', 'declaration', 'declarative programming',
                  'decompilation', 'decomposition', 'defense in depth', 'deferred', 'delegate', 'delegation', 'delphi',
                  'delta', 'denormalize', 'dependency', 'dependency hell', 'dependency injection',
                  'dependency management', 'deprecated', 'dereference', 'dereference a null pointer',
                  'design for maintainability', 'design pattern', 'development hell', 'devops', 'diamond of death',
                  'diaper', 'dictionary', 'digital', "dijkstra's algorithm", 'directed acyclic graph', 'directed graph',
                  'distributed data protocol (ddp)', 'div soup', 'divide and conquer', 'django', 'dnf',
                  'dns (domain name system)', 'docker', 'docusaurus', 'domain-specific language', 'dongle', 'dos',
                  'downcasting', 'dp (data processing)', 'dp9ik', 'dr (disaster recovery)', 'drink your own champagne',
                  'dry code', "dry principle (don't repeat yourself)", 'duck punching', 'duck typing', "duff's device",
                  'dummy', 'dynamic programming', 'dynamic typing', 'dynamicate', 'eafp',
                  'eating your own dog food (dogfooding)', 'ec2', 'ecc', 'eclipse', 'ecm', 'ecmascript', 'ecs',
                  'ed (text editor)', 'edge', 'edge case', 'edi', 'edison reset', 'ejs (embedded javascript)',
                  'electron', 'eli5', 'elixir', 'elk', 'elm', 'else', 'elvis operator', 'emacs', 'emmet',
                  'encapsulation', 'encryption', 'end user', 'end-of-life', 'enum', 'environment', 'ephemeral', 'error',
                  'es6', 'esb', 'esoteric language', 'etl (extract transform load)', 'everything is a file',
                  'exception', 'express.js', 'f#', 'faas', 'facade', 'factoring', 'factory', 'fairlop', 'fake', 'false',
                  'faq (frequently asked questions)', 'feature', 'fedora', 'fiddler', 'fifo', 'filan', 'fildil',
                  'finite state machine', 'firefox', 'fkp', 'flask', 'flexbox', 'float (floating point)', 'flow',
                  'flutter', 'flux', 'font', 'foo', 'foobar', 'foreign key', 'fork', 'fork bomb', 'form', 'forth',
                  'fortran', 'foss', 'fpga', 'framer.js', 'framework', 'free software', 'freemarker', 'front-end',
                  'fsck', 'fsck up', 'fsm', 'fte', 'fubar', 'full stack developer', 'function',
                  'functional programming', 'functional test', 'functor', 'future', 'fuzz testing', 'fuzzing', 'g11n',
                  'garbage collection', 'gc', 'gdpr', 'gem (ruby)', 'generational garbage collection',
                  'generic programming', 'genetic algorithm', 'gis', 'git', 'git blame', 'github', 'gitversion',
                  'glitch', 'glob', 'globalization', 'globbing', 'gnu', 'gnu/linux', 'go', 'golang', 'golden hammer',
                  'google analytics', 'google apps script', 'gopher', 'goroutine', 'gradient descent', 'gradle',
                  'graph', 'graph theory', 'greenfield', 'grep', 'grok', 'groovy', 'grunt', 'gts', 'guard clause',
                  'gulp', 'hack', 'hacking', 'hackintosh', 'hadoop', 'handle', 'handlebars.js', 'happy path scenario',
                  'haptics', 'hash', 'hash map', 'haskell', 'hateoas', 'haxe', 'heap', 'heisenbug', 'hell',
                  'hello world', 'heroku', 'hex', 'hexadecimal', 'hft', 'high-level', 'highlander', 'hkt',
                  'hoc (higher order component)', "hofstadter's law", 'hollerith code', 'hooking', 'horizontal scaling',
                  'hot site', 'hsm', 'http', 'http status code', 'http/2', 'https', 'i/o', 'i18n', 'id10t',
                  'ide (integrated development environment)', 'idempotent', 'idris', 'ietf', 'if', 'if else',
                  "if it ain't broke don't fix it", 'iframe', 'iife', 'imap', 'immutable object',
                  'imperative programming', 'impersonation', 'implementation', 'implementation detail',
                  'impure function', 'include guard', 'indentation', 'induction', 'inferno-os', 'infinite loop',
                  'inheritance', 'inheritance chain', 'inpc', 'input', 'instance', 'instruction set architecture',
                  'integer', 'integration test', 'interface', 'internationalization', 'internet', 'interpreter',
                  'interrupt', 'invariance', 'invariant', 'inversion of control', 'iot', 'ip (intellectual property)',
                  'ip (internet protocol)', 'ipc', 'it (information technology)', 'iterable', 'iterate', 'jargon file',
                  'java', 'javafx', 'javascript', 'jaws', 'jekyll', 'jenkins', 'jhipster', 'jira', 'jit', 'jquery',
                  'json (javascript object notation)', 'jsx', 'just works', 'jvm', 'jwt (json web token)', 'kanban',
                  'kata', 'kernel', 'key value pair', 'kill -9', 'kiss', 'kludge', 'kotlin', 'kubernetes', 'l10n',
                  'lambda function', 'laragon', 'laravel', 'latency', 'lazy evaluation', 'lazy loading', 'leaf node',
                  'lean software development', 'least significant bit', 'legacy code', 'less', 'let statement',
                  'lexing', 'lgtm', 'library', 'lifecycle (rendering)', 'linked list', 'linker', 'linter', 'linux',
                  'lisp', 'list (python)', 'list comprehension', 'little-endian', 'load balancing', 'local maxima',
                  'local minima', 'localization', 'log shipping', 'lolcode', 'long-term support', 'loop',
                  'loose coupling', 'low-level', 'lru cache', 'lts', 'lua', 'lzw', 'machine code', 'machine learning',
                  'machine word', 'macos', 'magic', 'magic number', 'magic rebuild fairy', 'magic smoke', 'mainframe',
                  'malloc', 'malware', 'man month', 'man-in-the-middle attack', 'map reduce', 'markdown',
                  'markup language', 'master', 'materialize', 'matlab', 'matrix', 'maven', 'maybe', 'memoization',
                  'memory', 'memory leak', 'metadata', 'metaprogramming', 'metasploit', 'meteor', 'method',
                  'microservices', 'middleware', 'minify', 'mob programming', 'mocha', 'mock', 'modal', 'monad',
                  'mongodb', 'mongoose', 'monkey patch', 'mono', 'monoid', 'monospace', 'most significant bit',
                  'multiple inheritance', 'mutability', 'mvc (massive view controller)',
                  'mvc (model, view, controller)', 'mvn', 'mvp (minimum viable product)',
                  'mvp (model, view, presenter)', 'mvvm (model-view-viewmodel)', 'mysql', 'mythical man month',
                  'namespace', 'namespace collision', 'nas', 'natural language processing (nlp)', 'ncat',
                  'negative test', 'netbeans', 'netcat', 'network', 'new testament', 'nfc', 'nibble', 'nil', 'nim',
                  'nmap', 'noc', 'node', 'node.js', 'nodejs', 'normalization', 'nosql', 'notepad++', 'npe', 'npm',
                  'nuget', 'null', 'null pointer', 'null pointer exception', 'nvda', 'oauth', 'obfuscation', 'object',
                  'object initializer', 'object-oriented programming (oop)', 'object-relational mapping (orm)',
                  'objective-c', 'ocaml', 'ocr', 'offshore', 'oltp', 'omgifu call', 'omgwdid call', 'one way hash',
                  'open source', 'opencv', 'opengl', 'openssl', 'operating system', 'opinionated', 'ops',
                  'optimization', 'orm', 'orthogonal', 'os', 'osi model', 'output', 'overhead', 'overkill', 'override',
                  'p5.js', 'package manager', 'package.json', 'packing', 'padding', 'paging', 'pair programming',
                  'paradigm', 'parameter object', 'parameters', 'partial application', 'pass by reference',
                  'pass by value', 'password', 'pathfinding', 'pawn', 'pci standards', 'pebcak', 'pebkac',
                  'penetration testing', 'performance test', 'perl', 'pfm', 'php', 'phreaking', 'picnic', 'pig latin',
                  'pii', 'pip', 'pki', 'plan 9', 'pmbok', 'pmo', 'pmp (project management professional)', 'po', 'poco',
                  'pointer', 'pojo', 'pokemon exception handling', 'polling', 'polyfill', 'polymorphism', 'pop3',
                  'port', 'postgresql', 'postman', 'pots (plain old telephone service)', 'pr', 'pre-alpha', 'predicate',
                  'prelude', 'preprocessor', 'primary key', 'printf debugging', 'procan', 'processing', 'prod',
                  'product manager (pm)', 'production environment', 'programmer', 'programming language',
                  'project management', 'project manager', 'promise', 'protobuf', 'prototype',
                  'prototypical inheritance', 'ptal', 'public', 'public-key encryption', 'pure function', 'push',
                  'push (git)', 'python', 'q#', 'qa', 'ql', 'qos (quality of service)', 'qr code', 'qt', 'query',
                  'queue', 'r (language)', 'rabbitmq', 'race condition', 'raid', 'raii', 'rails (ruby on rails)',
                  'rainbow table', 'ram', 'ransomware', 'raster graphics', 'rc', 'react.js', 'recovery', 'recursion',
                  'recursive acronym', 'redis', 'redux', 'refactoring', 'reference counting',
                  'referential transparency', 'regex', 'regression testing', 'relational database', 'release candidate',
                  'render', 'repl', 'repo (git repository)', 'reproduce', 'request-response', 'requirements creep',
                  'rest', 'rest api', 'return', 'return-oriented programming', 'reverse engineering', 'reverse shell',
                  'rfc', 'rfid', 'rfp (request for proposal)', 'ricef', 'risc', 'root node', 'round robin', 'router',
                  'rpc', 'rpg (report program generator)', 'rpn (reverse polish notation)', 'rss', 'rtfm',
                  'rubber duck', 'rubber duck debugging', 'ruby', 'rubygems', 'rust', 'rvo', 's3', 'saas', 'sakura',
                  'salt', 'salting', 'sam', 'san', 'sap', 'sass', 'sbo', 'scalability', 'scale out', 'scale up',
                  'scheduling', 'schema', 'scope', 'scotty', 'scratch', 'screen reader', 'screen scraping',
                  'script kiddie', 'scrum', 'scss', 'sdlc (software development life cycle)', 'sed',
                  'segfault (segmentation fault)', 'semantic html', 'semantic version', 'semaphore', 'semigroup',
                  'sendy', 'seo', 'serialization', 'servant', 'server', 'serverless', 'service level agreement (sla)',
                  'service level objective (slo)', 'session', 'shadowing', 'sharding', 'shared library', 'shell',
                  'shift', 'shitcode', 'simd', 'sinatra', 'single page application (spa)',
                  'single-responsibility principle', 'singleton pattern', 'site reliability engineering (sre)', 'slack',
                  'slit', 'smoke test', 'smoke testing', 'snmp', 'soa', 'soap', 'socat', 'solid', 'soundex',
                  'source maps', 'sow (statement of work)', 'spaghetti code', 'spark', 'sparse matrix', 'special form',
                  'spoofing', 'spool', 'spring boot', 'sprint', 'spy', 'sql', 'sql injection', 'ssas', 'ssd', 'ssh',
                  'ssis', 'ssl', 'sso', 'ssrs', 'stack', 'stack overflow', 'staging environment', 'stakeholder',
                  'standard library', 'star schema', 'state', 'static (java keyword)', 'static analysis',
                  'static library', 'static typing', 'stop word', 'stored procedure', 'storm', 'string',
                  'strong typing', 'stub', 'sublime text', 'sudo', 'sut (system under test)', 'swe', 'swift',
                  'swift playgrounds', 'swizzle', 'symfony', 'symmetrical-key algorithm', 'syntactic sugar', 'syntax',
                  'syscall', 'system32', 'table', 'tail call optimization', 'tarball', 'task runner',
                  'tco (total cost of ownership)', 'tcp/ip', 'tech debt', 'technical debt', 'terminal',
                  'ternary operator', 'test', 'test double', 'test driven development (tdd)', 'testing', 'text editor',
                  'third normal form', 'thrash', 'threading', 'throw catch', 'thunk', 'tight coupling',
                  'time complexity', 'time-sharing', 'tla', 'tle', 'tmux', 'toil', 'tostring',
                  'tracing garbage collection', 'trainwreck', 'transpile', 'transpiler', 'traveling salesman problem',
                  'tree', 'trigger', 'trojan power source', 'true', 'ttl (time to live)', 'tuple', 'tuple (python)',
                  'turing machine', 'turing test', 'turing-complete', 'two factor authentication', 'type erasure',
                  'type safety', 'type system', 'typeless', 'typescript', 'ub (undefined behavior)',
                  'ui (user interface)', 'ui ux', 'uikit', 'uml', 'undirected graph', 'unicode',
                  'unit record equipment', 'unit test', 'unity', 'unix', 'upcasting', 'upsert', 'upstream',
                  'uri (uniform resource identifier)', 'url (uniform resource locator)', 'use after free', 'use strict',
                  'user', 'userland', 'ux (user experience)', 'v8', 'vanilla javascript', 'vector graphics',
                  'vectorization', 'vertical scaling', 'vi', 'view', 'vim', 'viper', 'virtual machine', 'visual basic',
                  'visual studio', 'visual studio code', 'voiceover', 'void', 'voip (voice over ip)', 'volumetrics',
                  'vr (virtual reality)', 'vs code', 'vue.js', 'vulkan', 'warm site', 'waterfall',
                  'waving a dead chicken', 'wbs', 'weak reference', 'weak typing', 'web development', 'webhook',
                  'webpack', 'webpacker', 'webscale', 'websocket', 'webvr', 'webxr', 'welf', 'wet', 'wget magic',
                  'while loop', 'white hat hacker', 'white paper', 'whitespace', 'windows', 'wip', 'wordpress',
                  'work products', 'workflow', 'wpf', 'wrapper', 'wrapper class', 'wygiwyg', 'wysiwyg', 'x86', 'xcode',
                  'xml', 'xtla', 'yagni', 'yak shaving', 'yesod', 'yum', 'zsh', '.net', '.net core', '.net framework',
                  '.net standard', '/dev/null', '10x', '1337', '3nf', '400', '418', '500 internal server error',
                  '9front', '9p']
    print("1.黑客的研究领域")
    json_f = open(jsonname, encoding='utf-8')
    setting = json.load(json_f)
    setting["history"] = list(set(setting["history"]))
    text = ""
    for item in setting["history"]:
        text += item + "\n"
    keyword_processor = KeywordProcessor()
    for item in terms_list:
        keyword_processor.add_keyword(item)
    keywords_found = keyword_processor.extract_keywords(text)
    keywords_found = list(set(keywords_found))
    json_f.close()
    if len(keywords_found) < 10:
        print("**", end="")
        for  i in keywords_found:
            print(i, end=" ")
        print()
        return keywords_found
    else:
        tmp = []
        resultList = random.sample(range(0, len(keywords_found)), 10)
        for i in resultList:
            tmp.append(keywords_found[i])
        #print(tmp)
        print("**",end="")
        for i in tmp:
            print(i,end=" ")
        print()
        return tmp

#get_area("./data/user/0x00pf.json")