#
# PySNMP MIB module CISCO-QINQ-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-QINQ-VLAN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoQinqVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 445))
ciscoQinqVlanMIB.setRevisions(('2004-11-29 00:00',))
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setLastUpdated('200411290000Z')
if mibBuilder.loadTexts: ciscoQinqVlanMIB.setOrganization('Cisco Systems, Inc.')
ciscoQinqVlanMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 0))
ciscoQinqVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1))
ciscoQinqVlanMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2))
cqvTermination = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1))
cqvTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2))
class CqvVlanIdOrZero(TextualConvention, Unsigned32):
    reference = 'RFC-2674, Bridge MIB Extensions, August 1999, Q-BRIDGE-MIB, E. Bell.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4094)

class CqvEncapsulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("isl", 1), ("dot1Q", 2))

cqvTerminationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1), )
if mibBuilder.loadTexts: cqvTerminationTable.setStatus('current')
cqvTerminationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTerminationCeVlanId"))
if mibBuilder.loadTexts: cqvTerminationEntry.setStatus('current')
cqvTerminationPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 1), VlanId())
if mibBuilder.loadTexts: cqvTerminationPeVlanId.setStatus('current')
cqvTerminationCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 2), VlanId())
if mibBuilder.loadTexts: cqvTerminationCeVlanId.setStatus('current')
cqvTerminationPeEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 3), CqvEncapsulationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationPeEncap.setStatus('current')
cqvTerminationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTerminationRowStatus.setStatus('current')
cqvTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1), )
if mibBuilder.loadTexts: cqvTranslationTable.setStatus('current')
cqvTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalPeVlanId"), (0, "CISCO-QINQ-VLAN-MIB", "cqvTranslationInternalCeVlanId"))
if mibBuilder.loadTexts: cqvTranslationEntry.setStatus('current')
cqvTranslationInternalPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 1), CqvVlanIdOrZero())
if mibBuilder.loadTexts: cqvTranslationInternalPeVlanId.setStatus('current')
cqvTranslationInternalCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 2), CqvVlanIdOrZero())
if mibBuilder.loadTexts: cqvTranslationInternalCeVlanId.setStatus('current')
cqvTranslationTrunkPeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 3), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkPeVlanId.setStatus('current')
cqvTranslationTrunkCeVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 4), CqvVlanIdOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationTrunkCeVlanId.setStatus('current')
cqvTranslationType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("doubleToSingle", 1), ("doubleToDouble", 2), ("doubleToDoubleOutOfRange", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationType.setStatus('current')
cqvTranslationCosPBits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("copyFromOuterTag", 1), ("copyFromInnerTag", 2))).clone('copyFromOuterTag')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationCosPBits.setStatus('current')
cqvTranslationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 445, 1, 2, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cqvTranslationRowStatus.setStatus('current')
ciscoQinqVlanMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1))
ciscoQinqVlanMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2))
ciscoQinQVlanMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 1, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTerminationGroup"), ("CISCO-QINQ-VLAN-MIB", "ciscoQinqVlanTranslationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinQVlanMIBCompliance = ciscoQinQVlanMIBCompliance.setStatus('current')
ciscoQinqVlanTerminationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 1)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTerminationPeEncap"), ("CISCO-QINQ-VLAN-MIB", "cqvTerminationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTerminationGroup = ciscoQinqVlanTerminationGroup.setStatus('current')
ciscoQinqVlanTranslationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 445, 2, 2, 2)).setObjects(("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkPeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationTrunkCeVlanId"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationType"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationCosPBits"), ("CISCO-QINQ-VLAN-MIB", "cqvTranslationRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQinqVlanTranslationGroup = ciscoQinqVlanTranslationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-QINQ-VLAN-MIB", ciscoQinqVlanMIB=ciscoQinqVlanMIB, ciscoQinqVlanMIBGroups=ciscoQinqVlanMIBGroups, cqvTerminationCeVlanId=cqvTerminationCeVlanId, ciscoQinqVlanMIBConform=ciscoQinqVlanMIBConform, cqvTranslationType=cqvTranslationType, cqvTermination=cqvTermination, cqvTranslationInternalCeVlanId=cqvTranslationInternalCeVlanId, ciscoQinqVlanMIBObjects=ciscoQinqVlanMIBObjects, cqvTranslation=cqvTranslation, PYSNMP_MODULE_ID=ciscoQinqVlanMIB, cqvTerminationPeEncap=cqvTerminationPeEncap, cqvTranslationTable=cqvTranslationTable, cqvTerminationPeVlanId=cqvTerminationPeVlanId, cqvTranslationInternalPeVlanId=cqvTranslationInternalPeVlanId, ciscoQinqVlanTranslationGroup=ciscoQinqVlanTranslationGroup, ciscoQinqVlanMIBNotifs=ciscoQinqVlanMIBNotifs, cqvTranslationEntry=cqvTranslationEntry, cqvTranslationCosPBits=cqvTranslationCosPBits, ciscoQinqVlanMIBCompliances=ciscoQinqVlanMIBCompliances, cqvTerminationEntry=cqvTerminationEntry, CqvEncapsulationType=CqvEncapsulationType, cqvTerminationTable=cqvTerminationTable, cqvTerminationRowStatus=cqvTerminationRowStatus, cqvTranslationTrunkCeVlanId=cqvTranslationTrunkCeVlanId, cqvTranslationTrunkPeVlanId=cqvTranslationTrunkPeVlanId, cqvTranslationRowStatus=cqvTranslationRowStatus, ciscoQinQVlanMIBCompliance=ciscoQinQVlanMIBCompliance, ciscoQinqVlanTerminationGroup=ciscoQinqVlanTerminationGroup, CqvVlanIdOrZero=CqvVlanIdOrZero)
