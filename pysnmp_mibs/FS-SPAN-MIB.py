#
# PySNMP MIB module FS-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-SPAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:27 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
IfIndex, ConfigStatus = mibBuilder.importSymbols("FS-TC", "IfIndex", "ConfigStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsSPANMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23))
fsSPANMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: fsSPANMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: fsSPANMIB.setOrganization('FS.COM Inc..')
fsSPANMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1))
fsSPANSessionNum = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsSPANSessionNum.setStatus('current')
fsSPANTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2), )
if mibBuilder.loadTexts: fsSPANTable.setStatus('current')
fsSPANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1), ).setIndexNames((0, "FS-SPAN-MIB", "fsSPANSession"), (0, "FS-SPAN-MIB", "fsSPANIfIndex"))
if mibBuilder.loadTexts: fsSPANEntry.setStatus('current')
fsSPANSession = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsSPANSession.setStatus('current')
fsSPANIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1, 2), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsSPANIfIndex.setStatus('current')
fsSPANIfRole = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("span-desc", 1), ("span-src-rx", 2), ("span-src-tx", 3), ("span-src-all", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsSPANIfRole.setStatus('current')
fsSPANEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 1, 2, 1, 4), ConfigStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fsSPANEntryStatus.setStatus('current')
fsSPANMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3))
fsSPANMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3, 1))
fsSPANMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3, 2))
fsSPANMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3, 1, 1)).setObjects(("FS-SPAN-MIB", "fsSPANMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsSPANMIBCompliance = fsSPANMIBCompliance.setStatus('current')
fsSPANMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 23, 3, 2, 1)).setObjects(("FS-SPAN-MIB", "fsSPANSession"), ("FS-SPAN-MIB", "fsSPANIfIndex"), ("FS-SPAN-MIB", "fsSPANIfRole"), ("FS-SPAN-MIB", "fsSPANEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fsSPANMIBGroup = fsSPANMIBGroup.setStatus('current')
mibBuilder.exportSymbols("FS-SPAN-MIB", fsSPANMIBCompliance=fsSPANMIBCompliance, fsSPANIfIndex=fsSPANIfIndex, fsSPANSession=fsSPANSession, fsSPANIfRole=fsSPANIfRole, fsSPANMIBCompliances=fsSPANMIBCompliances, fsSPANMIBConformance=fsSPANMIBConformance, fsSPANEntryStatus=fsSPANEntryStatus, fsSPANMIB=fsSPANMIB, fsSPANMIBGroup=fsSPANMIBGroup, fsSPANTable=fsSPANTable, fsSPANEntry=fsSPANEntry, fsSPANMIBGroups=fsSPANMIBGroups, PYSNMP_MODULE_ID=fsSPANMIB, fsSPANSessionNum=fsSPANSessionNum, fsSPANMIBObjects=fsSPANMIBObjects)
