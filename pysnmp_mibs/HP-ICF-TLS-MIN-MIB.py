#
# PySNMP MIB module HP-ICF-TLS-MIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HP-ICF-TLS-MIN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:02:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
hpicfTlsMinMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112))
hpicfTlsMinMIB.setRevisions(('2020-02-24 09:00', '2017-05-11 09:00', '2017-04-05 09:00', '2016-06-22 09:00', '2014-10-01 09:00',))
if mibBuilder.loadTexts: hpicfTlsMinMIB.setLastUpdated('202002240900Z')
if mibBuilder.loadTexts: hpicfTlsMinMIB.setOrganization('HP Networking')
hpicfTlsMinObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0))
hpicfTlsMinConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1))
hpicfTlsMinConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1))
hpicfTlsMinTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1), )
if mibBuilder.loadTexts: hpicfTlsMinTable.setStatus('current')
hpicfTlsMinEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1), ).setIndexNames((0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"))
if mibBuilder.loadTexts: hpicfTlsMinEntry.setStatus('current')
hpicfTlsMinApp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("webSsl", 1), ("openflow", 2), ("syslog", 3), ("tr69", 4), ("cloud", 5), ("radsec", 6))))
if mibBuilder.loadTexts: hpicfTlsMinApp.setStatus('current')
hpicfTlsMinVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tls1dot0", 1), ("tls1dot1", 2), ("tls1dot2", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinVersion.setStatus('current')
hpicfTlsMinCloseSSLSess = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinCloseSSLSess.setStatus('current')
hpicfTlsMinRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinRowStatus.setStatus('current')
hpicfTlsStrictRfc5424 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfTlsStrictRfc5424.setStatus('current')
hpicfTlsMinCipherTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2), )
if mibBuilder.loadTexts: hpicfTlsMinCipherTable.setStatus('current')
hpicfTlsMinCipherEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1), ).setIndexNames((0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinApp"), (0, "HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipher"))
if mibBuilder.loadTexts: hpicfTlsMinCipherEntry.setStatus('current')
hpicfTlsMinCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))).clone(namedValues=NamedValues(("aes256Sha256", 1), ("aes256Sha", 2), ("aes128Sha256", 3), ("aes128Sha", 4), ("des3CbcSha", 5), ("aes256GcmSha384", 6), ("aes128GcmSha256", 7), ("ecdhEcdsaAes256GcmSha384", 8), ("ecdhRsaAaes256GcmSha384", 9), ("ecdhEcdsaAes128GcmSha256", 10), ("ecdhRsaAes128GcmSha256", 11), ("ecdhEcdsaAes256Sha384", 12), ("ecdhRsaAes256Sha384", 13), ("ecdhEcdsaAes256Sha", 14), ("ecdhRsaAes256Sha", 15), ("ecdhEcdsaAes128Sha256", 16), ("ecdhRsaAes128Sha256", 17), ("ecdhEcdsaAes128Sha", 18), ("ecdhRsaAes128Sha", 19), ("ecdhEcdsaDesCbc3Sha", 20), ("ecdhRsaDesCbc3Sha", 21), ("ecdheEcdsaAes128GcmSha256", 22), ("ecdheRsaAes128GcmSha256", 23), ("ecdheEcdsaAes128Sha256", 24), ("ecdheRsaAes128Sha256", 25), ("ecdheEcdsaAes128Sha", 26), ("ecdheRsaAes128Sha", 27), ("ecdheEcdsaAes256GcmSha384", 28), ("ecdheRsaAes256GcmSha384", 29), ("ecdheEcdsaAes256Sha384", 30), ("ecdheRsaAes256Sha384", 31), ("ecdheEcdsaAes256Sha", 32), ("ecdheRsaAes256Sha", 33), ("ecdheEcdsaDesCbc3Sha", 34), ("ecdheRsaDesCbc3Sha", 35), ("all", 36))))
if mibBuilder.loadTexts: hpicfTlsMinCipher.setStatus('current')
hpicfTlsMinCipherRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinCipherRowStatus.setStatus('current')
hpicfTlsMinCipherConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 0, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enforce", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfTlsMinCipherConfig.setStatus('current')
hpicfTlsMinCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1))
hpicfTlsMinGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2))
hpicfTlsMinCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 1)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance1 = hpicfTlsMinCompliance1.setStatus('deprecated')
hpicfTlsMinConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 1)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup = hpicfTlsMinConfigGroup.setStatus('deprecated')
hpicfTlsMinCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 2)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance2 = hpicfTlsMinCompliance2.setStatus('deprecated')
hpicfTlsMinConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 2)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup1 = hpicfTlsMinConfigGroup1.setStatus('deprecated')
hpicfTlsMinCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 3)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance3 = hpicfTlsMinCompliance3.setStatus('deprecated')
hpicfTlsMinConfigGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 3)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup2 = hpicfTlsMinConfigGroup2.setStatus('deprecated')
hpicfTlsMinCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 1, 4)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinConfigGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinCompliance4 = hpicfTlsMinCompliance4.setStatus('current')
hpicfTlsMinConfigGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112, 1, 2, 4)).setObjects(("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinVersion"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCloseSSLSess"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherRowStatus"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsMinCipherConfig"), ("HP-ICF-TLS-MIN-MIB", "hpicfTlsStrictRfc5424"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfTlsMinConfigGroup3 = hpicfTlsMinConfigGroup3.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-TLS-MIN-MIB", hpicfTlsMinEntry=hpicfTlsMinEntry, hpicfTlsMinCipherTable=hpicfTlsMinCipherTable, hpicfTlsMinConfigGroup3=hpicfTlsMinConfigGroup3, hpicfTlsStrictRfc5424=hpicfTlsStrictRfc5424, hpicfTlsMinCompliance1=hpicfTlsMinCompliance1, hpicfTlsMinCipher=hpicfTlsMinCipher, PYSNMP_MODULE_ID=hpicfTlsMinMIB, hpicfTlsMinCipherConfig=hpicfTlsMinCipherConfig, hpicfTlsMinObjects=hpicfTlsMinObjects, hpicfTlsMinMIB=hpicfTlsMinMIB, hpicfTlsMinCompliance4=hpicfTlsMinCompliance4, hpicfTlsMinCompliance2=hpicfTlsMinCompliance2, hpicfTlsMinApp=hpicfTlsMinApp, hpicfTlsMinCipherRowStatus=hpicfTlsMinCipherRowStatus, hpicfTlsMinConfigObjects=hpicfTlsMinConfigObjects, hpicfTlsMinConformance=hpicfTlsMinConformance, hpicfTlsMinCompliances=hpicfTlsMinCompliances, hpicfTlsMinConfigGroup2=hpicfTlsMinConfigGroup2, hpicfTlsMinTable=hpicfTlsMinTable, hpicfTlsMinConfigGroup=hpicfTlsMinConfigGroup, hpicfTlsMinCipherEntry=hpicfTlsMinCipherEntry, hpicfTlsMinCloseSSLSess=hpicfTlsMinCloseSSLSess, hpicfTlsMinCompliance3=hpicfTlsMinCompliance3, hpicfTlsMinVersion=hpicfTlsMinVersion, hpicfTlsMinGroups=hpicfTlsMinGroups, hpicfTlsMinRowStatus=hpicfTlsMinRowStatus, hpicfTlsMinConfigGroup1=hpicfTlsMinConfigGroup1)
