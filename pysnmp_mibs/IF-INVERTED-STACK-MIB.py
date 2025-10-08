#
# PySNMP MIB module IF-INVERTED-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/IF-INVERTED-STACK-MIB.txt
# Produced by pysmi-1.1.12 at Wed Oct  8 10:48:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifStackGroup2, ifStackLowerLayer, ifStackHigherLayer = mibBuilder.importSymbols("IF-MIB", "ifStackGroup2", "ifStackLowerLayer", "ifStackHigherLayer")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ifInvertedStackMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 77))
ifInvertedStackMIB.setRevisions(('2000-06-14 00:00',))
if mibBuilder.loadTexts: ifInvertedStackMIB.setLastUpdated('200006140000Z')
if mibBuilder.loadTexts: ifInvertedStackMIB.setOrganization('IETF Interfaces MIB Working Group')
ifInvMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1))
ifInvStackTable = MibTable((1, 3, 6, 1, 2, 1, 77, 1, 1), )
if mibBuilder.loadTexts: ifInvStackTable.setStatus('current')
ifInvStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 77, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: ifInvStackEntry.setStatus('current')
ifInvStackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 77, 1, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInvStackStatus.setStatus('current')
ifInvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2))
ifInvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 1))
ifInvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 2))
ifInvCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 77, 1, 2, 2, 1)).setObjects(("IF-INVERTED-STACK-MIB", "ifInvStackGroup"), ("IF-MIB", "ifStackGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifInvCompliance = ifInvCompliance.setStatus('current')
ifInvStackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 77, 1, 2, 1, 1)).setObjects(("IF-INVERTED-STACK-MIB", "ifInvStackStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifInvStackGroup = ifInvStackGroup.setStatus('current')
mibBuilder.exportSymbols("IF-INVERTED-STACK-MIB", ifInvCompliance=ifInvCompliance, ifInvStackGroup=ifInvStackGroup, ifInvCompliances=ifInvCompliances, ifInvertedStackMIB=ifInvertedStackMIB, ifInvStackStatus=ifInvStackStatus, ifInvStackEntry=ifInvStackEntry, PYSNMP_MODULE_ID=ifInvertedStackMIB, ifInvConformance=ifInvConformance, ifInvStackTable=ifInvStackTable, ifInvMIBObjects=ifInvMIBObjects, ifInvGroups=ifInvGroups)
