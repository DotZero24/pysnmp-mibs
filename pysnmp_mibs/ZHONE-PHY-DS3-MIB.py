#
# PySNMP MIB module ZHONE-PHY-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/zhone/ZHONE-PHY-DS3-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:09:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dsx3ConfigEntry, = mibBuilder.importSymbols("DS3-MIB", "dsx3ConfigEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
zhoneModules, zhoneDs3Ext = mibBuilder.importSymbols("Zhone", "zhoneModules", "zhoneDs3Ext")
phyDs3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 17))
phyDs3.setRevisions(('2001-05-14 14:35', '2001-04-25 14:25', '2001-03-15 08:34',))
if mibBuilder.loadTexts: phyDs3.setLastUpdated('200105151435Z')
if mibBuilder.loadTexts: phyDs3.setOrganization('Zhone Technologies, Inc.')
dsx3ConfigExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 5, 10, 1)).setObjects(("ZHONE-PHY-DS3-MIB", "dsx3ConfigExtScrambleEnabled"), ("ZHONE-PHY-DS3-MIB", "dsx3ConfigExtE3Framing"), ("ZHONE-PHY-DS3-MIB", "dsx3ConfigExtAtmFraming"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dsx3ConfigExtGroup = dsx3ConfigExtGroup.setStatus('current')
dsx3ConfigExtTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 5, 10, 2), )
if mibBuilder.loadTexts: dsx3ConfigExtTable.setStatus('current')
dsx3ConfigExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 5, 10, 2, 1), )
dsx3ConfigEntry.registerAugmentions(("ZHONE-PHY-DS3-MIB", "dsx3ConfigExtEntry"))
dsx3ConfigExtEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: dsx3ConfigExtEntry.setStatus('current')
dsx3ConfigExtScrambleEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 10, 2, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3ConfigExtScrambleEnabled.setStatus('current')
dsx3ConfigExtE3Framing = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 10, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("e3FrameOther", 1), ("e3FrameG832", 2), ("e3FrameG751", 3))).clone('e3FrameG832')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3ConfigExtE3Framing.setStatus('current')
dsx3ConfigExtAtmFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 5, 10, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dsx3AtmFramingOther", 1), ("dsx3AtmFramingPLCP", 2), ("dsx3AtmFramingDirectCellMapped", 3))).clone('dsx3AtmFramingDirectCellMapped')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx3ConfigExtAtmFraming.setStatus('current')
mibBuilder.exportSymbols("ZHONE-PHY-DS3-MIB", dsx3ConfigExtAtmFraming=dsx3ConfigExtAtmFraming, dsx3ConfigExtScrambleEnabled=dsx3ConfigExtScrambleEnabled, dsx3ConfigExtEntry=dsx3ConfigExtEntry, dsx3ConfigExtTable=dsx3ConfigExtTable, PYSNMP_MODULE_ID=phyDs3, phyDs3=phyDs3, dsx3ConfigExtGroup=dsx3ConfigExtGroup, dsx3ConfigExtE3Framing=dsx3ConfigExtE3Framing)
