#
# PySNMP MIB module RADLAN-AUTOUPDATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/radlan/RADLAN-AUTOUPDATE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RADLAN-AUTOUPDATE-MIB", rlAutoUpdateFilesConf=rlAutoUpdateFilesConf, rlAutoUpdateEnable=rlAutoUpdateEnable, rlAutoUpdateCopyEnable=rlAutoUpdateCopyEnable, rlAutoUpdate=rlAutoUpdate, rlAutoUpdateFilesBoot=rlAutoUpdateFilesBoot, rlAutoUpdateFilesImage=rlAutoUpdateFilesImage, PYSNMP_MODULE_ID=rlAutoUpdate, rlAutoUpdatePreserveIP=rlAutoUpdatePreserveIP)
