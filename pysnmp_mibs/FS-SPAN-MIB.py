#
# PySNMP MIB module FS-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-SPAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
IfIndex, ConfigStatus = mibBuilder.importSymbols("FS-TC", "IfIndex", "ConfigStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("FS-SPAN-MIB", fsSPANMIBCompliances=fsSPANMIBCompliances, fsSPANMIB=fsSPANMIB, fsSPANEntry=fsSPANEntry, fsSPANIfIndex=fsSPANIfIndex, fsSPANMIBCompliance=fsSPANMIBCompliance, fsSPANSession=fsSPANSession, fsSPANSessionNum=fsSPANSessionNum, fsSPANIfRole=fsSPANIfRole, fsSPANTable=fsSPANTable, fsSPANMIBObjects=fsSPANMIBObjects, fsSPANMIBGroups=fsSPANMIBGroups, fsSPANMIBConformance=fsSPANMIBConformance, PYSNMP_MODULE_ID=fsSPANMIB, fsSPANMIBGroup=fsSPANMIBGroup, fsSPANEntryStatus=fsSPANEntryStatus)
