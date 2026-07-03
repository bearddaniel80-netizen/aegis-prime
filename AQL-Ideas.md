# Dev artifaacts
FROM wheel('package.whl')
FROM npm('package.tgz')
FROM dll('foo.dll')
FROM elf('binary')
FROM apk('app.apk')
FROM docker('image.tar')

ArtifactSource
 ├── JarSource
 ├── WheelSource
 ├── NpmPackageSource
 ├── ElfSource
 ├── ApkSource
 └── DockerLayerSource
## fields
| Table         | Meaning           |
| ------------- | ----------------- |
| classes       | Java classes      |
| methods       | Methods/functions |
| fields        | Fields            |
| annotations   | Java annotations  |
| dependencies  | Maven/Gradle deps |
| bytecode_refs | Call graph        |
| strings       | Extracted strings |
| manifests     | META-INF          |
| resources     | Embedded files    |
| signatures    | Signing info      |

artifacts
symbols
dependencies
resources
imports
exports
strings
licenses
signatures

# image artifacts
FROM tar('backup.tar')
FROM zip('app.zip')
FROM dmg('mac.dmg')
FROM vmdk('vm.vmdk')
FROM qcow2('disk.qcow2')
FROM apk('android.apk')
FROM ipa('ios.ipa')

## fields
| Projection  | Meaning                 |
| ----------- | ----------------------- |
| files       | extracted file metadata |
| strings     | extracted strings       |
| executables | binaries                |
| packages    | installed packages      |
| signatures  | signatures/certs        |
| licenses    | license data            |
| hashes      | hashes                  |
| entropy     | entropy metrics         |
| yara        | yara matches            |
| imports     | binary imports          |
| exports     | exported symbols        |
