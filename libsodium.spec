Name:           libsodium
Version:        1.0.11
Release:        1
Summary:        The Sodium crypto library
License:        ISC
URL:            http://libsodium.org/
Source0:        %{name}-%{version}.tar.gz

%description
Sodium is a new, easy-to-use software library for encryption, decryption, 
signatures, password hashing and more. It is a portable, cross-compilable, 
installable, packageable fork of NaCl, with a compatible API, and an extended 
API to improve usability even further. Its goal is to provide all of the core 
operations needed to build higher-level cryptographic tools. The design 
choices emphasize security, and "magic constants" have clear rationales.

The same cannot be said of NIST curves, where the specific origins of certain 
constants are not described by the standards. And despite the emphasis on 
higher security, primitives are faster across-the-board than most 
implementations of the NIST standards.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name} libraries.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -name '*.la' -delete -print

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE
%{_libdir}/libsodium.so.*

%files devel
%doc AUTHORS ChangeLog README.markdown THANKS
%doc test/default/*.{c,exp,h}
%doc test/quirks/quirks.h
%{_includedir}/sodium.h
%{_includedir}/sodium/
%{_libdir}/libsodium.so
%{_libdir}/pkgconfig/libsodium.pc

%changelog
* Tue Dec 06 2016 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com> 1.0.11-1
- libsodium.spec: update to 1.0.11 (tomasz.rostanski@thalesgroup.com)
- Remove dev flag (github@pureftpd.org)
- _MSC_VER > 1600 -> _MSC_VER >= 1700 for consistency (github@pureftpd.org)
- Reintroduce 27a2756479032deb970c7e57cd0ff7567994eda4 (github@pureftpd.org)
- Revert "VS2010 debug symbols" (github@pureftpd.org)
- Revert "VS2012 debug symbols" (github@pureftpd.org)
- Revert "VS2013 debug symbols" (github@pureftpd.org)
- Fix VS2010 (and VC9) x64 build (github@ehrhardt.nl)
- VS2013 debug symbols (github@ehrhardt.nl)
- VS2012 debug symbols (github@ehrhardt.nl)
- VS2010 debug symbols (github@ehrhardt.nl)
- cpuid is not available on i686-nacl (github@pureftpd.org)
- crit_{enter,leave} can fail (github@pureftpd.org)
- Warn if the library is being compiled in a custom way (github@pureftpd.org)
- Version bump (not released yet) (github@pureftpd.org)
- Add license title (waldyrious@gmail.com)
- Update ChangeLog (github@pureftpd.org)
- Update comment (github@pureftpd.org)
- Expose sodium_crit_enter() and sodium_crit_leave() internally
  (github@pureftpd.org)
- Slightly change how the length of argon2 strings is checked
  (github@pureftpd.org)
- Nits (github@pureftpd.org)
- document why RtlGenRandom is used (azet@azet.org)
- Correct whitespace in path detection, and turn it into a fatal error
  (github@pureftpd.org)
- Remove extra space (github@pureftpd.org)
- CRLF (github@pureftpd.org)
- Android: compile for platform 24, check compat with 16 or 21 (64 bit)
  (github@pureftpd.org)
- Forgot to ignore libsodium-uninstalled.pc (github@pureftpd.org)
- Ignore test/js.done (github@pureftpd.org)
- Sort .gitignore (github@pureftpd.org)
- Remove curvecp from .gitignore (github@pureftpd.org)
- Ignore more specific directories than libsodium-* (github@pureftpd.org)
- Don't include <immintrin.h> if it is not needed (github@pureftpd.org)
- Fix & simplify MADV_DO{NO}DUMP alternatives (github@pureftpd.org)
- Support madvise() on FreeBSD (blacklion+git@gmail.com)
- Indent (github@pureftpd.org)
- don't crash on Win32 (sneves@dei.uc.pt)
- CRLF (github@pureftpd.org)
- fix avx2 feature detection, fixes #395 (tw@waldmann-edv.de)
- sandy2x: don't mix VEX and non-VEX instructions (github@pureftpd.org)
- sandy2x: clean the upper halves of the AVX registers (github@pureftpd.org)
- Fixing a small documentation typo (langboost@gmail.com)
- Align loops (github@pureftpd.org)
- sandy2x: align branch targets (github@pureftpd.org)
- On ancient Linux kernels, block on /dev/random before using /dev/urandom
  (github@pureftpd.org)
- Clone msvc .filters (from vs2013 version) for uniformity. (eric@voskuil.org)
- Use lowest common denominator .vcxproj ToolsVersion. (eric@voskuil.org)
- Rewrite aesni_key256_expand() for clarity (github@pureftpd.org)
- Rename REDUCE4 to MULREDUCE4 for clarity (github@pureftpd.org)
- Grammar (github@pureftpd.org)
- Try using cpuid on NativeClient (github@pureftpd.org)
- Try MMX/SSE/SSE2/SSE3/SSSE4/SSE4.1 instructions on NativeClient
  (github@pureftpd.org)
- Add nativeclient-x86.sh (github@pureftpd.org)
- Disable SIMD instructions on NativeClient (github@pureftpd.org)
- Remove extra CRLF (github@pureftpd.org)
- Do not use pthreads on NativeClient (github@pureftpd.org)
- x86-64 -> x86_64 (github@pureftpd.org)
- Disable ssp and aesni on nativeclient, nativeclient.sh->nativeclient-pnacl.sh
  (github@pureftpd.org)
- Add dist-build/nativeclient-x86-64.sh (github@pureftpd.org)
- Put `then` and `if` on the same line. (github@pureftpd.org)
- Build scripts don't clean after themselves (github@pureftpd.org)
- CRLF (github@pureftpd.org)
- NativeClient complains about __memset_chk being undefined on OSX. Work around
  this. There might be a better fix, but at least the test suite compiles with
  the newlib. (github@pureftpd.org)
- NativeClient: use get_random_bytes directly instead of the wrapper
  (github@pureftpd.org)
- abort() if nacl_secure_random() ever returns 0 but the wrong size
  (github@pureftpd.org)
- Use pepper_49 (github@pureftpd.org)
- Disable asm on native client (github@pureftpd.org)
- Tabify (github@pureftpd.org)
- Indent (github@pureftpd.org)
- Proper lock test on Windows (jedisct1@users.noreply.github.com)
- Simplify the fallback _sodium_crit_enter() code (github@pureftpd.org)
- Add locks around sodium_init() (github@pureftpd.org)
- Update include guard (github@pureftpd.org)
- Use the same convention for include guards everywhere (github@pureftpd.org)
- scrypt/sse - Note that B's layout is permuted compared to nosse
  (github@pureftpd.org)
- Hand-roll zeroing instead of relying on memset() (github@pureftpd.org)
- Remove README (github@pureftpd.org)
- Larger logo, less prominent saltcellar (github@pureftpd.org)
- Import ax_pthread.m4 (github@pureftpd.org)
- Quotes (github@pureftpd.org)
- Repair NativeClient support (github@pureftpd.org)
- Compile with pthreads (github@pureftpd.org)
- if -> ifdef (github@pureftpd.org)
- Do not use emscripten's headless mode (github@pureftpd.org)
- Remove crypto_pwhash_*() from the non-sumo Javascript distribution
  (github@pureftpd.org)
- pwhash_*() require heap allocations, but everything else doesn't
  (github@pureftpd.org)
- Revamp the emscripten build script (github@pureftpd.org)
- Reduce TOTAL_MEMORY (github@pureftpd.org)
- JS target: use -Os instead of -O3 (github@pureftpd.org)
- Do not use getrandom(2) on SLES11 service pack 4 (github@pureftpd.org)
- Do not use -Ofast (github@pureftpd.org)
- Run `make clean` after `./configure` instead of `distclean` before
  (github@pureftpd.org)
- Check for MinGW presence (github@pureftpd.org)
- Not an ELF system, not an Apple system, weak symbols may not work
  (github@pureftpd.org)
- Revert -lfto addition on msys2 (github@pureftpd.org)
- msys2 supports -Ofast and -flto these days (github@pureftpd.org)
- Do not forget crypto_pwhash.c on Visual Studio (github@pureftpd.org)
- Replace two more memcpy() with a local loop (github@pureftpd.org)
- sha{512,256}: use a local loop instead of if + memcpy() (github@pureftpd.org)
- https (github@pureftpd.org)
- Make assertions more readable (github@pureftpd.org)
- Avoid bit shifting with signed values (github@pureftpd.org)
- memcpy(): pointers must be valid even if the size is 0 (github@pureftpd.org)
- Use slightly more modern target CPUs for the msys2 builds
  (github@pureftpd.org)
- Decryption functions can now accept a `NULL` pointer for the output
  (github@pureftpd.org)
- Set randombytes_implementation to NULL by default, to cope with Visual Studio
  2008 (github@pureftpd.org)
- Back to dev mode (github@pureftpd.org)
- Require Visual Studio 2010+ for AESNI (github@pureftpd.org)
- Argon2: initialize ctx{.pwd,.pwdlen} in the verify function
  (github@pureftpd.org)
- Use absolute .done files (github@pureftpd.org)
- Use a specific "done" file for every javascript target (github@pureftpd.org)
- Use different folders for libsodium-js and for the sumo version
  (github@pureftpd.org)
- Return -1 if crypto_generichash_final() is called twice (github@pureftpd.org)
- Remove the "examples" directory. (github@pureftpd.org)
- Update the changelog (github@pureftpd.org)
- Update appveyor version (github@pureftpd.org)
- Move curve25519_ref10.h to include/sodium/private/ (github@pureftpd.org)
- Remove headers that are not required in MSVC solutions (github@pureftpd.org)
- include/sodium/private.h -> include/sodium/private/common.h
  (github@pureftpd.org)
- Remove some unneeded dependencies from MSVC project filters
  (github@pureftpd.org)
- Relocate sodium/common.h (github@pureftpd.org)
- Version bump [only the package] (github@pureftpd.org)
- Test that ciphertexts shorter than the MAC size aren't even read
  (github@pureftpd.org)
- Make the test of truncated chacha20poly1305 ciphers less deterministic
  (github@pureftpd.org)
- Adjust another relative path for sodium/common.h (github@pureftpd.org)
- Fix up relative includes of sodium/common.h (david@sandstorm.io)
- Increase TOTAL_MEMORY for the Javascript target (github@pureftpd.org)
- Explain why blake2b_param_set_digest_length() is not needed
  (github@pureftpd.org)
- Workaround for old gcc versions missing _mm256_broadcastsi128_si256()
  (github@pureftpd.org)
- Update Appveyor version (github@pureftpd.org)
- Nits (github@pureftpd.org)
- NO_BROWSER is not required any more, even for tests (github@pureftpd.org)
- Initialize constant (github@pureftpd.org)
- Consistency (github@pureftpd.org)
- Reuse STORE64_LE whenever possible (github@pureftpd.org)
- Include missing structures definitions (github@pureftpd.org)
- Consistency (github@pureftpd.org)
- Stronger types for >= 16 bits shifts (github@pureftpd.org)
- ((unsigned long long) 1) -> 1ULL (github@pureftpd.org)
- (1 << x) -> (1UL << x) for compilers where sizeof(int) == 2
  (github@pureftpd.org)
- l -> L (github@pureftpd.org)
- Update the list of symbols exported to Javascript (github@pureftpd.org)
- Add symbols to include/ignore (github@pureftpd.org)
- Reformat (github@pureftpd.org)
- Add crypto_pwhash_argon2i_ALG_ARGON2I13 (github@pureftpd.org)
- Require an algorithm identifier in crypto_pwhash() (github@pureftpd.org)
- Remove mlen_p from the AEAD detached interface (github@pureftpd.org)
- Revisit the default set of compiler warnings (github@pureftpd.org)
- Mark test functions as static and __attribute__ ((noreturn))
  (github@pureftpd.org)
- Mark the _out_of_bounds() function as noreturn (github@pureftpd.org)
- Include blake2b_long prototype (github@pureftpd.org)
- Thanks! (github@pureftpd.org)
- 1.0.9 is almost ready to be tagged (github@pureftpd.org)
- Restore the previous sodium_malloc(0) behavior (github@pureftpd.org)
- Explicit cast; length is already checked by the caller (github@pureftpd.org)
- More Argon2 tests (github@pureftpd.org)
- More tests / lcov exclusions (github@pureftpd.org)
- Make Argon2 encode/decode return codes consistent with other functions
  (github@pureftpd.org)
- Remove unused code (github@pureftpd.org)
- The version in Argon2i strings is separated from other parameters
  (github@pureftpd.org)
- Avoid implicit sodium_malloc(0) in tests (github@pureftpd.org)
- Remove useless check (github@pureftpd.org)
- Nits (github@pureftpd.org)
- Make sodium_malloc(0) well-defined. It always returns NULL.
  (github@pureftpd.org)
- Check memory base instead of the aligned pointer No behavior change, but it
  is less confusing to static analyzers (github@pureftpd.org)
- More tests (github@pureftpd.org)
- Additional tests for BLAKE2b (github@pureftpd.org)
- Remove unused declaration (github@pureftpd.org)
- Have the SSE2 test trigger a conversion with old gcc versions
  (github@pureftpd.org)
- Old gcc versions need -flax-vector-conversions to compile some intrinsics
  (github@pureftpd.org)
- Use existing functions for unaligned access in hash_sha*
  (github@pureftpd.org)
- Nits (github@pureftpd.org)
- Remove hidden symbols from emscripten-symbols.def (github@pureftpd.org)
- -save-temps is messing with the detection of supported directives Remove it
  from --enable-opt, and don't use any directives to restrict symbol visibility
  if detection appears to be unreliable (github@pureftpd.org)
- Force LITTLE_ENDIAN detection on x86 and x86_64 This is a sad workaround for
  CompCert 2.6 (github@pureftpd.org)
- Endianness (github@pureftpd.org)
- C++ compat (github@pureftpd.org)
- Tests must use sodium_malloc() as much as possible (github@pureftpd.org)
- sizeof() -> constants (github@pureftpd.org)
- Nits (github@pureftpd.org)
- Add tests for the detached chacha20poly1305 API (github@pureftpd.org)
- Update ChangeLog (github@pureftpd.org)
- Of course, GNU ld doesn't know about .private_extern (github@pureftpd.org)
- Only use .private_extern if this is supported (github@pureftpd.org)
- Reduce symbols visibility in curve25519_sandy2x (github@pureftpd.org)
- Set JS_EXPORTS_FLAGS after EXPORTED_FUNCTIONS (github@pureftpd.org)
- Add the script to generate the emscripten symbols (github@pureftpd.org)
- Update emscripten symbols, add a "sumo" mode (github@pureftpd.org)
- Add crypto_pwhash_primitive() (github@pureftpd.org)
- Add missing SODIUM_EXPORT statements (github@pureftpd.org)
- Add detached versions of ChaCha20-Poly1305 (github@pureftpd.org)
- Replace some constants (github@pureftpd.org)
- clen -> clen_p (github@pureftpd.org)
- test/pwhash_argon2i -> test/pwhash (github@pureftpd.org)
- Add support for optional parameters to future-proof crypto_pwhash()
  (github@pureftpd.org)
- Rename CPUID bits constants for clarity (github@pureftpd.org)
- AVX2 bit is in %%ebx, not %%ecx (github@pureftpd.org)
- Double crypto_pwhash_argon2i_MEMLIMIT_INTERACTIVE (github@pureftpd.org)
- Simplify quirks for C++Builder (github@pureftpd.org)
- Some platforms don't define ENOSYS - use ENXIO instead on these.
  (github@pureftpd.org)
- Introduce C++Builder compatibility (jcollier@CC1182.cook.local)
- Verify at compile time that blake2b_param is packed as expected
  (github@pureftpd.org)
- Remove unnecessary extern "C" and unused prototypes (github@pureftpd.org)
- Remove BLAKE2s-related declarations (github@pureftpd.org)
- Consistent comment style (github@pureftpd.org)
- Link text = "installation" only (github@pureftpd.org)
- Mention which section + split line (github@pureftpd.org)
- Make it easier to find the integrity checking instructions
  (scott@paragonie.com)
- Avoid BLAKE2 AVX2 implementation on Win32 (github@pureftpd.org)
- Update Makefiles and MSVC solutions (github@pureftpd.org)
- Indent (github@pureftpd.org)
- Add blake2b-compress-avx2.c to the top-level Visual Studio solution
  (github@pureftpd.org)
- BLAKE2b AVX2 implementation By the marvellous Samuel Neves -
  https://github.com/sneves/blake2-avx2 (github@pureftpd.org)
- CRLF (github@pureftpd.org)
- Update description (github@pureftpd.org)
- Luminous beings are we, not this crude matter (github@pureftpd.org)
- The Yoda style avoiding we can. In a similar test above, that style we didn't
  use. (github@pureftpd.org)
- Argon2: avoid initial zeroing by calling fill_block() on the first pass
  (github@pureftpd.org)
- Add AVX2 detection (github@pureftpd.org)
- Cacheline alignment (github@pureftpd.org)
- Spacing (github@pureftpd.org)
- Add crypto_core/curve25519 (github@pureftpd.org)
- Add tests for the detached aes256gcm API (github@pureftpd.org)
- Add a detached API for aes256gcm (github@pureftpd.org)
- Update blake2b licensing (github@pureftpd.org)
- We only support data independent addressing for Argon2 Let the compiler
  automatically remove unused code (github@pureftpd.org)
- p -> R for clarity (github@pureftpd.org)
- Remove superflous constant type qualifiers (github@pureftpd.org)
- ed25519_verify: check for small-order R (github@pureftpd.org)
- Check what the implications of versioned Argon2 strings will be
  (github@pureftpd.org)
- The version number in Argon2 strings will require 5 extra bytes Round
  `crypto_pwhash_argon2i_STRBYTES` up to 128 (github@pureftpd.org)
- Consistent indentation (github@pureftpd.org)
- Ed25519: verify 0<=s<2^252+27742317777372353535851937790883648493
  (github@pureftpd.org)
- Update test for short output (github@pureftpd.org)
- pwhash_argon2i_str(): zero the output buffer even on error path
  (github@pureftpd.org)
- Require a least 128 bits for an Argon2i digest (github@pureftpd.org)
- Tab (github@pureftpd.org)
- Enable Valgrind for the unit tests only if --enable-valgrind is passed Also
  mention that the Valgrind checks currently require GNU make, unlike all other
  targets. (github@pureftpd.org)
- Have --enable-opt use -O3, not -Ofast (github@pureftpd.org)
- Revisit Argon2i predefined parameters (github@pureftpd.org)
- Argon2: use negative error codes (github@pureftpd.org)
- Typo (github@pureftpd.org)
- Remove the test dir from the VS solutions, except the top one
  (github@pureftpd.org)
- Remove the test part from the vs2010 projects (github@pureftpd.org)
- Remove disabled files (github@pureftpd.org)
- Explicit downcast (github@pureftpd.org)
- VS2015 update (github@pureftpd.org)
- VS2013 update (github@pureftpd.org)
- Update the VS2012 project (github@pureftpd.org)
- VS2010 update (github@pureftpd.org)
- Unused param (github@pureftpd.org)
- Remove obsolete and redundant globals (github@pureftpd.org)
- int vs size_t (github@pureftpd.org)
- Remove unneeded prototypes (github@pureftpd.org)
- Remove unused variables (github@pureftpd.org)
- Blame me for hchacha20 (github@pureftpd.org)
- Add support for running the test suite with Valgrind (github@pureftpd.org)
- scrypt: zeroize the temporary output buffer (github@pureftpd.org)
- inttypes.h -> stdint.h (github@pureftpd.org)
- Compile optimized Argon2i impl on 32-bit MSVC (github@pureftpd.org)
- MSVC analyzer FP (github@pureftpd.org)
- Update root MSVC project (github@pureftpd.org)
- NO_BROWSER is not required any more with recent Emscripten versions
  (github@pureftpd.org)
- Update the list of symbols exported to Javascript (github@pureftpd.org)
- Bump ARGON2_MIN_TIME to 3, adjust tests accordingly (github@pureftpd.org)
- Let core_salsa20* accept a default constant (github@pureftpd.org)
- Use stdint types a bit more (github@pureftpd.org)
- Let `crypto_core_hsalsa20()` accept `NULL` for the default constants
  (github@pureftpd.org)
- Trim/untab/indent (github@pureftpd.org)
- scrypt/sysendian.h is gone (github@pureftpd.org)
- common_aes128ctr.c is gone (github@pureftpd.org)
- Use a single way to do unaligned memory access/endianness conversion
  (github@pureftpd.org)
- Hide store32()/load32() in the header (github@pureftpd.org)
- Faster HChaCha20 (github@pureftpd.org)
- Faster with clang (github@pureftpd.org)
- Add HChaCha20 (github@pureftpd.org)
- Argon2: issue different error codes for VERIFY_MISMATCH and DECODING_FAIL
  Only used internally, not exposed in the Sodium API (github@pureftpd.org)
- Use calloc() instead of malloc()+memset() (github@pureftpd.org)
- Update Argon2 tests (github@pureftpd.org)
- Argon2: fill_block() now XORs blocks instead of overwriting them
  (github@pureftpd.org)
- Remove ...edwards25519sha512batch_*() wrappers for the constants
  (github@pureftpd.org)
- Define ZEROBYTES as BOXZEROBYTES + MACBYTES ZEROBYTES and BOXZEROBYTES are
  rarely used compared to MACBYTES, so it makes more sense to define MACBYTES
  and define the compat macros based on it that the other way round.
  (github@pureftpd.org)
- Added all argon2 files to other msvc project files and project filter files
  (gnieboer@corpcomm.net)
- Wipe secret keys before public keys and nonces (github@pureftpd.org)
- Comments cleanup (github@pureftpd.org)
- added argon2-fill-block-ssse3.c to VS project (gnieboer@corpcomm.net)
- Indent (github@pureftpd.org)
- aes256gcm_encrypt_afternm() - abort() if mlen > 2^39-256 bits
  (github@pureftpd.org)
- On non-ELF platforms, mark pointers as volatile, not just what they point to.
  See http://sk.tl/Wj3pmI vs http://sk.tl/VNsyd9 (github@pureftpd.org)
- Argon2: explicitly initialize ctx.secret to NULL (github@pureftpd.org)
- Sync argon2 implementation with upstream (github@pureftpd.org)
- argon2_core() -> argon2_ctx() (github@pureftpd.org)
- Caps (github@pureftpd.org)
- Add comments to argon2-encoding.c Upstream `decode_string()` can return
  `ARGON2_INCORRECT_TYPE`. This change is not merged. Either have a function
  return an ARGON2 constant, have it return 0/1, or have it return 0/-1, but
  mixing different systems is confusing. (encode|decode)_string() should
  probably all return an ARGON2 code. (github@pureftpd.org)
- Add extra sodium_memzero() in Argon2 (github@pureftpd.org)
- Relax max sizes in argon2 decoding (github@pureftpd.org)
- Add aes256gcm stubs for platforms where it is not available
  (github@pureftpd.org)
- Initialize ctx->pwdlen in argon2 string decoder (github@pureftpd.org)
- zero the context, in case we forget to initialize some members
  (github@pureftpd.org)
- Argon2: use existing constants more consistently By @technion via the
  reference implementation (github@pureftpd.org)
- Add crypt_generichash_blake2b_statebytes function (paul@paulbarker.me.uk)
- Add new macros for chacha20poly1305_ietf constants, for clarity
  (github@pureftpd.org)
- The occasional absence of braces is disturbing. (github@pureftpd.org)
- Reuse validate_inputs() to validate parameters in argon2-encoding.c
  (github@pureftpd.org)
- Export crypto_pwhash*() to Javascript (github@pureftpd.org)
- Version bump (not released yet) (github@pureftpd.org)
- Untab (github@pureftpd.org)
- Argon2: Let fill_{memory_blocks,segment} return an error code
  (github@pureftpd.org)
- Add AppVeyor configuration (github@pureftpd.org)
- Add Appveyor status (github@pureftpd.org)
- Visual Studio's preprocessor doesn't support #warning (github@pureftpd.org)
- argon2i strings are variable length; check that they are zero-padded
  (github@pureftpd.org)
- Add extra CRYPTO_ALIGN() required for Minix (github@pureftpd.org)
- Bring back tests vectors for argon2 strings (github@pureftpd.org)
- 2016 (github@pureftpd.org)
- Make argon2i blocks allocation functions static (github@pureftpd.org)
- Update the top-level MSVC project (github@pureftpd.org)
- Do not forget Daniel Dinu and Thomas Pornin in the list of contributors to
  the Argon2 code (github@pureftpd.org)
- Check for crypto_pwhash_*limit_moderate() presence (github@pureftpd.org)
- argon2: memory usage is m_cost KiB, not 2^m_cost KiB (github@pureftpd.org)
- We don't need no external memory allocators (github@pureftpd.org)
- Check for _mm_set_epi64x() usability in the SSE2 test (github@pureftpd.org)
- Add sodium/crypto_pwhash.h to the distribution (github@pureftpd.org)
- We don't need the ability to use a custom allocator (github@pureftpd.org)
- argon2: don't dereference a pointer before testing it for NULL
  (github@pureftpd.org)
- Test the high-level crypto_pwhash() functions (github@pureftpd.org)
- Add high-level crypto_pwhash() API (github@pureftpd.org)
- Consistent #include guards (github@pureftpd.org)
- Shorten a few test argon2i test vectors for V8 This is enough to reproduce an
  bug with Chrome (github@pureftpd.org)
- Credit Argon2 authors (github@pureftpd.org)
- argon2i test: remove tv3 for now; it's too much for web browsers Proper test
  vectors will be reintroduced later (github@pureftpd.org)
- Pasto (github@pureftpd.org)
- argon2: ensure that memory is cacheline aligned; use mmap(2) if possible
  (github@pureftpd.org)
- Require less indentation (github@pureftpd.org)
- argon2: make blocks allocation indirect, keep the base address
  (github@pureftpd.org)
- Put the browser-js.done marker at the right place (github@pureftpd.org)
- Don't require too much memory for the pwhash_argon2i() test so that the
  Javascript version can run in web browsers (github@pureftpd.org)
- Comment doesn't seem to be relevant any more (github@pureftpd.org)
- Indent (github@pureftpd.org)
- Remove unneeded extern "C" (github@pureftpd.org)
- Add missing header (github@pureftpd.org)
- Add tests for pwhash_argon2i (github@pureftpd.org)
- Rename the pwhash test as as pwhash_scrypt (github@pureftpd.org)
- Add crypto_pwhash_argon2i_(memlimit|opslimit)_moderate() Import missing
  crypto_pwhash_argon2i.h by the way (github@pureftpd.org)
- Have --enable-opt imply -Ofast (github@pureftpd.org)
- Require at least SSSE3 for optimized implementations (github@pureftpd.org)
- crypto_pwhash_argon2i_*() (github@pureftpd.org)
- Argon2 bits - Not exposed in the API yet (github@pureftpd.org)
- Back go to dev mode (github@pureftpd.org)
- Try --high-entropy-va on MinGW (github@pureftpd.org)
- Reorder (github@pureftpd.org)
- 1.0.8 (github@pureftpd.org)
- Get ready for the xmas release (github@pureftpd.org)
- pkg-config is not required (github@pureftpd.org)
- lcov exclusion (github@pureftpd.org)
- lcov exclusion (github@pureftpd.org)
- lcov exclusion (github@pureftpd.org)
- Check crypto_box_detached() with a small order pk (github@pureftpd.org)
- Test crypto_box_beforenm() with a small order pk (github@pureftpd.org)
- lcov exclusion (github@pureftpd.org)
- Check that crypto_box[_beforenm] fails with a small order pk
  (github@pureftpd.org)
- Constify (github@pureftpd.org)
- Update the Visual Studio solutions (github@pureftpd.org)
- Mention that the gitbook online documentation requires Javascript Add a link
  to the offline documentation (github@pureftpd.org)
- Update .gitignore (github@pureftpd.org)
- Version bump (github@pureftpd.org)
- Annotations (github@pureftpd.org)
- 2x (github@pureftpd.org)
- Test crypto_onetimeauth_update() with a null size (github@pureftpd.org)
- Document constants (github@pureftpd.org)
- wipe secret key as soon as it is no longer needed.
  (neuhaus@users.noreply.github.com)
- Update the top-level Visual Studio solution (github@pureftpd.org)
- Remove dead code (github@pureftpd.org)
- Add warning (github@pureftpd.org)
- Fix empty __attribute__ definition for !__GNUC__ (github@pureftpd.org)
- Update ChangeLog (github@pureftpd.org)
- Use memset() for fe_(0|1)() This produces faster code with gcc. constify
  precomputations by the way. (github@pureftpd.org)
- --enable-opt now enables -save-temps; remove -flto (github@pureftpd.org)
- Use stdint types instead of crypto_* (github@pureftpd.org)
- Finish replacing shifts on integers with multiplications
  (github@pureftpd.org)
- Remove redundant blank lines (github@pureftpd.org)
- Spacing (github@pureftpd.org)
- Explicitly call abort() if gettimeofday() doesn't succeed.
  (github@pureftpd.org)
- Aliasing (github@pureftpd.org)
- Use the right type for sizeof's result (bsilver16384@gmail.com)
- Don't rely on assert evaluating its argument (bsilver16384@gmail.com)
- Don't call strlen on uninitialized memory if fgets fails
  (bsilver16384@gmail.com)
- Faster scalarmult_base() when using the ref10 implementation.
  (github@pureftpd.org)
- Reorder to improve inlining (github@pureftpd.org)
- Reorder functions to help with inlining (github@pureftpd.org)
- Let the x25519 ref10 implementation use the core/curve25519/ref code cswap
  can be a convenient operation to have in core later, but it is not required
  yet. (github@pureftpd.org)
- Move most of sign/ed25519/ref10 to core/curve25519/ref10
  (github@pureftpd.org)
- Simplify AVX availabity detection, add support for Visual Studio
  (github@pureftpd.org)
- Use HAVE_AVX_ASM instead of HAVE_AMD64_ASM (github@pureftpd.org)
- Check the extended control register to see if AVX is actually usable
  (github@pureftpd.org)
- Reduce diff between curve25519/ref10 and ed25519/ref10, add missing includes
  (github@pureftpd.org)
- ref10: inline, constify (github@pureftpd.org)
- Travis: Limit the double compilation to a single OS (github@pureftpd.org)
- The output of "make distclean" is not worth logging in Travis
  (github@pureftpd.org)
- Travis: Run the pre-C99 compilation test only once, with gcc Compile without
  optimizations (and symbols) as an opportunity to also check that it properly
  compiles under these conditions (re: force_inline issues)
  (github@pureftpd.org)
- Travis: check that we get the same code with&without named struct
  initializers (github@pureftpd.org)
- Don't refine SODIUM_C99 if it has already been defined (github@pureftpd.org)
- Reorder struct members to keep values of the same type together
  (github@pureftpd.org)
- salsa20random stream struct members must match initializers for compatibility
  with old non-C99 compilers. Spotted and reported by @sneves
  (github@pureftpd.org)
- printf("%%llu") is not expected work on mingw32/Windows XP.
  (github@pureftpd.org)
- __attribute__((...)) -> __attribute__ ((...)) (github@pureftpd.org)
- Run make distclean, not just make clean in the msys2 build scripts for
  consistency with other build scripts (github@pureftpd.org)
- Run "make clean" first in the build scripts (github@pureftpd.org)
- Fix offset in obsolete crypto_sign_edwards25519sha512batch_open
  (github@pureftpd.org)
- Revert "Use minimal builds on msys2" (github@pureftpd.org)
- Remove dead globals, bump the number of rounds in the box{7,8} tests
  (github@pureftpd.org)
- Reduce the number of rounds in the box7 test, use guarded memory
  (github@pureftpd.org)
- Shorten the verify1 test (github@pureftpd.org)
- 1.0.7 is ready (github@pureftpd.org)
- Force alignment for _mm_loadl_epi64() in DEBUG mode Required to work around
  gcc sanitizer (github@pureftpd.org)
- Shorten auth7 (github@pureftpd.org)
- Remove browser-js.done or js.done, but not both (github@pureftpd.org)
- Let emscripten.sh support a --browser-tests switch (github@pureftpd.org)
- C++ compat (github@pureftpd.org)
- Ignore test/default/browser, import HTML template (github@pureftpd.org)
- Reduce box8 even more (github@pureftpd.org)
- Use guarded memory for the box8 test (github@pureftpd.org)
- Reduce a few expensive tests (github@pureftpd.org)
- Reduce some test cases, generate html test files (github@pureftpd.org)
- Reduce even more, for Chrome (github@pureftpd.org)
- On a web browser, reduce the number of vectors for the sign test
  (github@pureftpd.org)
- Revert "Output signatures prefix in the signature test" (github@pureftpd.org)
- Nits (github@pureftpd.org)
- Output signatures prefix in the signature test (github@pureftpd.org)
- Support a BROWSER_TESTS env variable to build tests for browsers
  (github@pureftpd.org)
- Update the examples for libsodium 1.0.7 (github@pureftpd.org)
- Update ChangeLog (github@pureftpd.org)
- More checks for sodium_add() (overlaps) and sodium_increment()
  (github@pureftpd.org)
- Don't define unused variables (github@pureftpd.org)
- autoconf: check that named registers work (github@pureftpd.org)
- Assembly optimized _increment() and _add() for common nonce types
  (github@pureftpd.org)
- Add a --enable-opt compile-time switch (github@pureftpd.org)
- Use -O2 & -flto for iOS targets (github@pureftpd.org)
- On OSX, compile with -flto for better performance (github@pureftpd.org)
- Reformat (github@pureftpd.org)
- +floodyberry for poly1305/sse2 (github@pureftpd.org)
- THANKS << Scott Arciszewski (github@pureftpd.org)
- Add a test with a null message in box_easy() (github@pureftpd.org)
- Add tests with null message in secretbox_easy.c (github@pureftpd.org)
- Use sodium_malloc() for the secretbox_easy2 test (github@pureftpd.org)
- Use guarded memory for the box_easy2() test + non-deterministic buffer sizes
  (github@pureftpd.org)
- Let blake2b abort on invalid parameters instead of returning -1
  (github@pureftpd.org)
- Remove generichash tests with invalid parameters They must be reintroduced at
  some point, probably by overriding the `abort` symbol. (github@pureftpd.org)
- Nit (github@pureftpd.org)
- Constify & add a note on _mm_loadl_epi64() (github@pureftpd.org)
- Use memcpy() instead of a cast (github@pureftpd.org)
- Don't assume that substracting unrelated pointers is acceptable. Having to
  increment two pointers instead of one is the price to pay for portability,
  but it's not that big of a deal here. (github@pureftpd.org)
- Avoid unnecessary casts for the nonce/counter (github@pureftpd.org)
- format (github@pureftpd.org)
- Use uint128_t consistently (github@pureftpd.org)
- Replace some casts with memcpy() (github@pureftpd.org)
- Revert (github@pureftpd.org)
- Directly use the internal state type when possible (github@pureftpd.org)
- Use memset() instead of a cast (github@pureftpd.org)
- Fix aliasing violations, even though we always disable strict aliasing
  (github@pureftpd.org)
- Avoid pointer casting when using Emscripten (github@pureftpd.org)
- Keep it simple to avoid issues with the different heaps in Emscripten
  (github@pureftpd.org)
- Move Ted Krovetz to the implementors list (github@pureftpd.org)
- Rephrase (github@pureftpd.org)
- Move size checks to the main chacha20 encryption function
  (github@pureftpd.org)
- Remove unused code (github@pureftpd.org)
- Constify pointers & acknowledge that unaligned accesses are okay
  (github@pureftpd.org)
- C++ compat (github@pureftpd.org)
- 1.0.7 (not released yet) (github@pureftpd.org)
- Update ChangeLog (github@pureftpd.org)
- Update ChangeLog (github@pureftpd.org)
- Don't use C99 when it's not required (github@pureftpd.org)
- Use more portable types (github@pureftpd.org)
- Remove blank line (github@pureftpd.org)
- !__GNUC__ : not yet (github@pureftpd.org)
- Use chacha20_vec if available (github@pureftpd.org)
- + Ted Krovetz (github@pureftpd.org)
- Link chacha20_vec (github@pureftpd.org)
- x -> ctx (github@pureftpd.org)
- + missing stdint.h inclusion (github@pureftpd.org)
- No need to zero the counter (github@pureftpd.org)
- Less deterministic crypto_verify_*() tests (github@pureftpd.org)
- Slightly faster verify_{16,32,64} (github@pureftpd.org)
- Make crypto_stream_chacha20 modular like the rest In preparation for
  optimized implementations (github@pureftpd.org)
- Support the IBM compiler (github@pureftpd.org)
- Mark everything as static in tests (github@pureftpd.org)
- Update the Visual Studio 2015 solution (github@pureftpd.org)
- Revert "Temporarily remove Coverity Scan button, as Coverity Scan is down"
  (github@pureftpd.org)
- Remove api.h from the Visual Studio solutions (github@pureftpd.org)
- api.h -> stream_chacha20_ref.h (github@pureftpd.org)
- Add missing headers (github@pureftpd.org)
- Don't force inline (github@pureftpd.org)
- api.h removal (github@pureftpd.org)
- More api.h removal (github@pureftpd.org)
- api.h removal (github@pureftpd.org)
- More api.h removal (github@pureftpd.org)
- More api.h removal (github@pureftpd.org)
- Remove api.h reference (github@pureftpd.org)
- crypto_hash/sha{256,512}/cp/api.h removal (github@pureftpd.org)
- Stop hiding function names with macros in salsa20 (github@pureftpd.org)
- Limit safe_read() to SSIZE_MAX bytes (github@pureftpd.org)
- Use __uint128_t only if HAVE_TI_MODE is defined (github@pureftpd.org)
- Temporarily remove Coverity Scan button, as Coverity Scan is down
  (github@pureftpd.org)
- Remove CVS $Id (github@pureftpd.org)
- Update the Visual Studio 2013 solution (github@pureftpd.org)
- More informative messages about missing package (github@pureftpd.org)
- Mark randombytes_implementation functions static (github@pureftpd.org)
- Update the Visual Studio 2012 solution (github@pureftpd.org)
- README: Use the svg Travis image (kevin.ji@outlook.com)
- Update the Visual Studio 2010 solution (github@pureftpd.org)
- Revert "Use SSSE3 instructions even on Visual Studio with a 32-bit target"
  (github@pureftpd.org)
- Remove extra comma (github@pureftpd.org)
- Do not export randombytes_set_implementation() in Javascript
  (github@pureftpd.org)
- Check that scalarmult() returns -1 with a point of small order
  (github@pureftpd.org)
- Update ChangeLog (github@pureftpd.org)
- Check that the output of X25519 is not the all-zero value Return -1 if this
  happens, and mark crypto_scalarmult() as warn_unused_result Mark dependent
  functions with warn_unused_result as well (github@pureftpd.org)
- Consistency (github@pureftpd.org)
- Keep it simple (github@pureftpd.org)
- Add tests for sodium_add(), more tests for sodium_increment() and is_zero()
  (github@pureftpd.org)
- Indent (github@pureftpd.org)
- Repair sodium_is_zero() (github@pureftpd.org)
- Faster sodium_is_zero() and sodium_increment() helpers Also add sodium_add(),
  since people tend to reimplement this in order to add constants to nonces.
  (github@pureftpd.org)
- Replace CPU_ALIGNED_ACCESS_REQUIRED with CPU_UNALIGNED_ACCESS
  (github@pureftpd.org)
- Use SSSE3 instructions even on Visual Studio with a 32-bit target
  (github@pureftpd.org)
- Return CPU features in Visual Studio builds (github@pureftpd.org)
- Enable 128-bit arithmetic if __int128 is available (github@pureftpd.org)
- Update ChangeLog (github@pureftpd.org)
- Update the top level VS solution (github@pureftpd.org)
- Add a compile-time size check (github@pureftpd.org)
- Update ChangeLog (github@pureftpd.org)
- More explicit casts. Unaligned accesses are fine on these architectures.
  (github@pureftpd.org)
- Clear the state after poly1305_finish() (github@pureftpd.org)
- Do not require assembly code to increment with carry (github@pureftpd.org)
- Bump major (github@pureftpd.org)
- Indent (github@pureftpd.org)
- Handle partial blocks in poly1305_sse2 (github@pureftpd.org)
- Link poly1305_sse2 Breakage is expected as partial blocks are not handled yet
  (github@pureftpd.org)
- Make the poly1305_sse2 code more consistent with the other implementation
  (github@pureftpd.org)
- Import vanilla poly1305_sse2 (github@pureftpd.org)
- Different ways to avoid inlining (github@pureftpd.org)
- Remove crypto_onetimeauth_poly1305_donna_implementation_name() prototype
  (github@pureftpd.org)
- auth_poly1305_donna.c -> poly1305_donna.c for consistency
  (github@pureftpd.org)
- Check inline assembly code using __asm__ __volatile__ (github@pureftpd.org)
- Use poly1305_state_internal_t for the state of poly1305 internal functions
  (github@pureftpd.org)
- Indent (github@pureftpd.org)
- ctx -> state for consistency with the high-level functions
  (github@pureftpd.org)
- Get rid of poly1305_state to reduce the number of indirections
  (github@pureftpd.org)
- Add compilation-time poly1305 structure size checks (github@pureftpd.org)
- Add a is_zero() helper (github@pureftpd.org)
- Use minimal builds on msys2 (github@pureftpd.org)
- Always include <stdint.h> and <limits.h> for SIZE_MAX (github@pureftpd.org)
- Implement the old edwards25519sha512batch construction on top of ref10 Only
  for backward compatibility; not compiled in minimal mode.
  (github@pureftpd.org)
- Move the legacy edwards25519sha512batch code to the attic
  (github@pureftpd.org)
- Remove useless sodium_memzero() (github@pureftpd.org)
- Travis: sudo is not needed (github@pureftpd.org)
- In blake2b_final() the leftover shouldn't exceed two blocks
  (github@pureftpd.org)
- Update the top Visual Studio solution (github@pureftpd.org)
- Travis: run the compile-everything task after having run ./configure
  (github@pureftpd.org)
- Travis: check that the project compiles by including everything and
  completely ignoring the normal autotools way. (github@pureftpd.org)
- Check HAVE_AMD64_ASM to assemble x86_64 code (or not), not __x86_64__
  (github@pureftpd.org)
- HMAC-SHA1 -> Blake2b in randombytes_salsa20 No functional changes but it's
  slightly faster and more readable. (github@pureftpd.org)
- Rename s to hsigma, use hex, clarify that this constant is not a PRNG "seed"
  (github@pureftpd.org)
- Remove unused base_curve25519_donna_c64.c file from the repository
  (github@pureftpd.org)
- noinst_HEADERS might be more correct than EXTRA_DIST (github@pureftpd.org)
- Update ChangeLog (github@pureftpd.org)
- Unfortunately, some assemblers still don't know about AVX opcodes
  (github@pureftpd.org)
- EMSCRIPTEN -> __EMSCRIPTEN__ (github@pureftpd.org)
- C++ compat (github@pureftpd.org)
- Drop extra backslash (github@pureftpd.org)
- Protect Sandy2x files against double compilation (Cocoapods...)
  (github@pureftpd.org)
- Restore the initial file structure in sandy2x (github@pureftpd.org)
- Revert in order to keep the original files (github@pureftpd.org)
- Allow compilation on Linux again (github@pureftpd.org)
- Move the sandy2x implementation into a single file (github@pureftpd.org)
- Typo (github@pureftpd.org)
- Linux is not supported yet (github@pureftpd.org)
- Let sodium_init() pick the fastest curve25519 implementation
  (github@pureftpd.org)
- Enable the sandy2x implementation on CPUs with AVX support
  (github@pureftpd.org)
- Credit Tung Chou (github@pureftpd.org)
- Use the same ifndef convention as most other header files
  (github@pureftpd.org)
- scalarmult: move the constants down (github@pureftpd.org)
- sandy2x: mask the top bit (github@pureftpd.org)
- Link the sandy2x implementation Do not use it yet, because it doesn't ignore
  the top bit (github@pureftpd.org)
- Modularize scalarmult (github@pureftpd.org)
- Add stackmarkings. Required at least for Hardened Gentoo.
  (github@pureftpd.org)
- Properly tag function symbols (github@pureftpd.org)
- Don't mix .globl and .global - Pick one, stick to it (github@pureftpd.org)
- Sandy2x: make all the references relative (github@pureftpd.org)
- Import the raw Sandy2x curve25519 implementation (github@pureftpd.org)
- Add missing include (github@pureftpd.org)
- Add sodium_runtime_has_avx() (github@pureftpd.org)

* Thu Apr 21 2016 Michal Gawlik <michal.gawlik@thalesgroup.com> 1.0.6-2
- tito: switch to ReleaseTagger (michal.gawlik@thalesgroup.com)
- libsodium.spec: fix bogus date in changelog
  (tomasz.rostanski@thalesgroup.com.pl)
- libsodium.spec: remove dist name from rpm version
  (tomasz.rostanski@thalesgroup.com.pl)

* Mon Nov 02 2015 Tomasz Rostanski <tomasz.rostanski@thalesgroup.com> - 1.0.6-1
- Update to 1.0.6

* Mon Jul 13 2015 Christopher Meng <rpm@cicku.me> - 1.0.3-1
- Update to 1.0.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Christopher Meng <rpm@cicku.me> - 1.0.2-1
- Update to 1.0.2

* Sat Nov 22 2014 Christopher Meng <rpm@cicku.me> - 1.0.1-1
- Update to 1.0.1

* Sat Oct 18 2014 Christopher Meng <rpm@cicku.me> - 1.0.0-1
- Update to 1.0.0

* Sun Aug 24 2014 Christopher Meng <rpm@cicku.me> - 0.7.0-1
- Update to 0.7.0

* Thu Jul 17 2014 Christopher Meng <rpm@cicku.me> - 0.6.1-1
- Update to 0.6.1

* Thu Jul 03 2014 Christopher Meng <rpm@cicku.me> - 0.6.0-1
- Update to 0.6.0

* Fri May 16 2014 Christopher Meng <rpm@cicku.me> - 0.5.0-1
- Update to 0.5.0

* Mon Dec 09 2013 Christopher Meng <rpm@cicku.me> - 0.4.5-3
- Disable silent build rules.
- Preserve the timestamp.

* Wed Nov 20 2013 Christopher Meng <rpm@cicku.me> - 0.4.5-2
- Add doc for devel package.
- Add support for EPEL6.

* Wed Nov 20 2013 Christopher Meng <rpm@cicku.me> - 0.4.5-1
- Update to 0.4.5

* Wed Jul 10 2013 Christopher Meng <rpm@cicku.me> - 0.4.2-2
- Drop useless files.
- Improve the description.

* Wed Jul 10 2013 Christopher Meng <rpm@cicku.me> - 0.4.2-1
- Initial Package.
