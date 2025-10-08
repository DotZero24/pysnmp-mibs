#
# PySNMP MIB module DES7200-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES7200-SPAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
myMgmt, = mibBuilder.importSymbols("DES7200-SMI", "myMgmt")
MemberMap, IfIndex, ConfigStatus = mibBuilder.importSymbols("DES7200-TC", "MemberMap", "IfIndex", "ConfigStatus")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
mySPANMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23))
mySPANMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: mySPANMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: mySPANMIB.setOrganization('$Company$')
mySPANMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1))
mySPANSessionNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mySPANSessionNum.setStatus('current')
mySPANTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2), )
if mibBuilder.loadTexts: mySPANTable.setStatus('current')
mySPANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1), ).setIndexNames((0, "DES7200-SPAN-MIB", "mySPANSession"), (0, "DES7200-SPAN-MIB", "mySPANIfIndex"))
if mibBuilder.loadTexts: mySPANEntry.setStatus('current')
mySPANSession = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mySPANSession.setStatus('current')
mySPANIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1, 2), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mySPANIfIndex.setStatus('current')
mySPANIfRole = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("span-desc", 1), ("span-src-rx", 2), ("span-src-tx", 3), ("span-src-all", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mySPANIfRole.setStatus('current')
mySPANEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 1, 2, 1, 4), ConfigStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mySPANEntryStatus.setStatus('current')
mySPANMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3))
mySPANMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3, 1))
mySPANMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3, 2))
mySPANMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3, 1, 1)).setObjects(("DES7200-SPAN-MIB", "mySPANMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mySPANMIBCompliance = mySPANMIBCompliance.setStatus('current')
mySPANMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 23, 3, 2, 1)).setObjects(("DES7200-SPAN-MIB", "mySPANSession"), ("DES7200-SPAN-MIB", "mySPANIfIndex"), ("DES7200-SPAN-MIB", "mySPANIfRole"), ("DES7200-SPAN-MIB", "mySPANEntryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mySPANMIBGroup = mySPANMIBGroup.setStatus('current')
mibBuilder.exportSymbols("DES7200-SPAN-MIB", mySPANEntryStatus=mySPANEntryStatus, mySPANTable=mySPANTable, mySPANSession=mySPANSession, mySPANMIBCompliances=mySPANMIBCompliances, mySPANIfIndex=mySPANIfIndex, mySPANEntry=mySPANEntry, mySPANIfRole=mySPANIfRole, PYSNMP_MODULE_ID=mySPANMIB, mySPANMIB=mySPANMIB, mySPANMIBGroup=mySPANMIBGroup, mySPANMIBObjects=mySPANMIBObjects, mySPANMIBGroups=mySPANMIBGroups, mySPANSessionNum=mySPANSessionNum, mySPANMIBConformance=mySPANMIBConformance, mySPANMIBCompliance=mySPANMIBCompliance)
