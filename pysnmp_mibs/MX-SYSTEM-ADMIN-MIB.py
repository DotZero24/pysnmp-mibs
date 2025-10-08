#
# PySNMP MIB module MX-SYSTEM-ADMIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-SYSTEM-ADMIN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:21 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mediatrixAdmin, = mibBuilder.importSymbols("MX-SMI", "mediatrixAdmin")
MxEnableState, = mibBuilder.importSymbols("MX-TC", "MxEnableState")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sysAdminMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 5, 1))
sysAdminMIB.setRevisions(('2006-03-06 00:00', '2005-04-20 00:00', '2004-02-12 00:00', '1903-12-02 00:00',))
if mibBuilder.loadTexts: sysAdminMIB.setLastUpdated('200603060000Z')
if mibBuilder.loadTexts: sysAdminMIB.setOrganization('Mediatrix Telecom, Inc.')
sysAdminMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 5, 1, 1))
sysAdminConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 5, 1, 2))
sysAdminCommand = MibScalar((1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noOp", 0), ("checkRam", 1), ("checkRom", 2), ("downloadSoftware", 3), ("resetStats", 4), ("setConfigSourcesStatic", 5), ("updateConfiguration", 6))).clone('noOp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysAdminCommand.setStatus('current')
sysAdminDefaultSettingsEnable = MibScalar((1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 5), MxEnableState().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysAdminDefaultSettingsEnable.setStatus('current')
sysAdminLastCheckRam = MibScalar((1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notTested", 0), ("fail", 1), ("success", 2))).clone('notTested')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAdminLastCheckRam.setStatus('current')
sysAdminLastCheckRom = MibScalar((1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fail", 1), ("success", 2))).clone('success')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAdminLastCheckRom.setStatus('current')
sysAdminLastDownloadSoftware = MibScalar((1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fail", 1), ("success", 2))).clone('success')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAdminLastDownloadSoftware.setStatus('current')
sysAdminDownloadConfigFileStatus = MibScalar((1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 0), ("fail", 1), ("success", 2), ("inProgress", 3), ("listening", 4))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAdminDownloadConfigFileStatus.setStatus('current')
sysAdminAppMode = MibScalar((1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("recovery", 1))).clone('normal')).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysAdminAppMode.setStatus('current')
sysAdminCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 5, 1, 2, 1))
sysAdminComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 5, 1, 2, 1, 1)).setObjects(("MX-SYSTEM-ADMIN-MIB", "sysAdminGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysAdminComplVer1 = sysAdminComplVer1.setStatus('current')
sysAdminGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 5, 1, 2, 2))
sysAdminGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 5, 1, 2, 2, 1)).setObjects(("MX-SYSTEM-ADMIN-MIB", "sysAdminDownloadConfigFileStatus"), ("MX-SYSTEM-ADMIN-MIB", "sysAdminCommand"), ("MX-SYSTEM-ADMIN-MIB", "sysAdminDefaultSettingsEnable"), ("MX-SYSTEM-ADMIN-MIB", "sysAdminLastCheckRam"), ("MX-SYSTEM-ADMIN-MIB", "sysAdminLastCheckRom"), ("MX-SYSTEM-ADMIN-MIB", "sysAdminLastDownloadSoftware"), ("MX-SYSTEM-ADMIN-MIB", "sysAdminAppMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysAdminGroupVer1 = sysAdminGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-SYSTEM-ADMIN-MIB", sysAdminMIB=sysAdminMIB, sysAdminDefaultSettingsEnable=sysAdminDefaultSettingsEnable, sysAdminConformance=sysAdminConformance, sysAdminDownloadConfigFileStatus=sysAdminDownloadConfigFileStatus, sysAdminComplVer1=sysAdminComplVer1, sysAdminLastCheckRam=sysAdminLastCheckRam, sysAdminLastDownloadSoftware=sysAdminLastDownloadSoftware, sysAdminGroups=sysAdminGroups, sysAdminLastCheckRom=sysAdminLastCheckRom, PYSNMP_MODULE_ID=sysAdminMIB, sysAdminCompliances=sysAdminCompliances, sysAdminMIBObjects=sysAdminMIBObjects, sysAdminAppMode=sysAdminAppMode, sysAdminGroupVer1=sysAdminGroupVer1, sysAdminCommand=sysAdminCommand)
