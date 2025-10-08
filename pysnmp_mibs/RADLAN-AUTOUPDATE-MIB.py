#
# PySNMP MIB module RADLAN-AUTOUPDATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/radlan/RADLAN-AUTOUPDATE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlAutoUpdate = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 123))
if mibBuilder.loadTexts: rlAutoUpdate.setLastUpdated('2007010600Z')
if mibBuilder.loadTexts: rlAutoUpdate.setOrganization('Radlan Computer Communications Ltd.')
rlAutoUpdateEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 123, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlAutoUpdateEnable.setStatus('current')
rlAutoUpdateFilesBoot = MibScalar((1, 3, 6, 1, 4, 1, 89, 123, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlAutoUpdateFilesBoot.setStatus('current')
rlAutoUpdateFilesImage = MibScalar((1, 3, 6, 1, 4, 1, 89, 123, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlAutoUpdateFilesImage.setStatus('current')
rlAutoUpdateFilesConf = MibScalar((1, 3, 6, 1, 4, 1, 89, 123, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlAutoUpdateFilesConf.setStatus('current')
rlAutoUpdateCopyEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 123, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlAutoUpdateCopyEnable.setStatus('current')
rlAutoUpdatePreserveIP = MibScalar((1, 3, 6, 1, 4, 1, 89, 123, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlAutoUpdatePreserveIP.setStatus('current')
mibBuilder.exportSymbols("RADLAN-AUTOUPDATE-MIB", PYSNMP_MODULE_ID=rlAutoUpdate, rlAutoUpdateFilesImage=rlAutoUpdateFilesImage, rlAutoUpdateEnable=rlAutoUpdateEnable, rlAutoUpdateFilesBoot=rlAutoUpdateFilesBoot, rlAutoUpdate=rlAutoUpdate, rlAutoUpdatePreserveIP=rlAutoUpdatePreserveIP, rlAutoUpdateFilesConf=rlAutoUpdateFilesConf, rlAutoUpdateCopyEnable=rlAutoUpdateCopyEnable)
