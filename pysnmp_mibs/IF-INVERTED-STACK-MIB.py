#
# PySNMP MIB module IF-INVERTED-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///usr/share/snmp/mibs/IF-INVERTED-STACK-MIB.txt
# Produced by pysmi-1.1.12 at Thu Sep 11 10:26:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifStackHigherLayer, ifStackLowerLayer, ifStackGroup2 = mibBuilder.importSymbols("IF-MIB", "ifStackHigherLayer", "ifStackLowerLayer", "ifStackGroup2")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("IF-INVERTED-STACK-MIB", ifInvStackGroup=ifInvStackGroup, ifInvCompliances=ifInvCompliances, ifInvStackEntry=ifInvStackEntry, ifInvGroups=ifInvGroups, PYSNMP_MODULE_ID=ifInvertedStackMIB, ifInvCompliance=ifInvCompliance, ifInvConformance=ifInvConformance, ifInvertedStackMIB=ifInvertedStackMIB, ifInvStackStatus=ifInvStackStatus, ifInvMIBObjects=ifInvMIBObjects, ifInvStackTable=ifInvStackTable)
