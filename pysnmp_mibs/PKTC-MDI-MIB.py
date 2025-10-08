#
# PySNMP MIB module PKTC-MDI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/PKTC-MDI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
pktcApplicationMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcApplicationMibs")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
pktcMdiMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6))
pktcMdiMib.setRevisions(('2009-09-17 00:00', '2009-02-26 00:00',))
if mibBuilder.loadTexts: pktcMdiMib.setLastUpdated('200909170000Z')
if mibBuilder.loadTexts: pktcMdiMib.setOrganization('Cable Television Laboratories, Inc.')
class PktcMdiType(TextualConvention, Integer32):
    reference = 'PacketCable DECT-HDV Specification'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pots", 1), ("dectPP", 2))

pktcMdiNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 0))
pktcMdiObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1))
pktcMdiMdiTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1), )
if mibBuilder.loadTexts: pktcMdiMdiTable.setStatus('current')
pktcMdiMdiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pktcMdiMdiEntry.setStatus('current')
pktcMdiMdiType = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1, 1, 1), PktcMdiType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcMdiMdiType.setStatus('current')
pktcMdiMdiName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcMdiMdiName.setStatus('current')
pktcMdiMdiActivityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcMdiMdiActivityStatus.setStatus('current')
pktcMdiNslTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2), )
if mibBuilder.loadTexts: pktcMdiNslTable.setStatus('current')
pktcMdiNslEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1), ).setIndexNames((0, "PKTC-MDI-MIB", "pktcMdiNslIndex"))
if mibBuilder.loadTexts: pktcMdiNslEntry.setStatus('current')
pktcMdiNslIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: pktcMdiNslIndex.setStatus('current')
pktcMdiNslName = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcMdiNslName.setStatus('current')
pktcMdiNslPortListIn = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcMdiNslPortListIn.setStatus('current')
pktcMdiNslPortListOut = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcMdiNslPortListOut.setStatus('current')
pktcMdiNslRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pktcMdiNslRowStatus.setStatus('current')
pktcMdiMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2))
pktcMdiMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2, 1))
pktcMdiMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2, 2))
pktcMdiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2, 1, 1)).setObjects(("PKTC-MDI-MIB", "pktcMdiGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcMdiCompliance = pktcMdiCompliance.setStatus('current')
pktcMdiGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 6, 2, 2, 1)).setObjects(("PKTC-MDI-MIB", "pktcMdiMdiType"), ("PKTC-MDI-MIB", "pktcMdiMdiName"), ("PKTC-MDI-MIB", "pktcMdiMdiActivityStatus"), ("PKTC-MDI-MIB", "pktcMdiNslName"), ("PKTC-MDI-MIB", "pktcMdiNslPortListIn"), ("PKTC-MDI-MIB", "pktcMdiNslPortListOut"), ("PKTC-MDI-MIB", "pktcMdiNslRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcMdiGroup = pktcMdiGroup.setStatus('current')
mibBuilder.exportSymbols("PKTC-MDI-MIB", pktcMdiNslRowStatus=pktcMdiNslRowStatus, pktcMdiNslEntry=pktcMdiNslEntry, pktcMdiMdiActivityStatus=pktcMdiMdiActivityStatus, pktcMdiNslPortListIn=pktcMdiNslPortListIn, pktcMdiMibConformance=pktcMdiMibConformance, PktcMdiType=PktcMdiType, pktcMdiMibCompliances=pktcMdiMibCompliances, pktcMdiMibGroups=pktcMdiMibGroups, pktcMdiNslTable=pktcMdiNslTable, pktcMdiNslName=pktcMdiNslName, pktcMdiNslPortListOut=pktcMdiNslPortListOut, pktcMdiCompliance=pktcMdiCompliance, pktcMdiGroup=pktcMdiGroup, pktcMdiMib=pktcMdiMib, pktcMdiNslIndex=pktcMdiNslIndex, pktcMdiMdiName=pktcMdiMdiName, PYSNMP_MODULE_ID=pktcMdiMib, pktcMdiObjects=pktcMdiObjects, pktcMdiNotifications=pktcMdiNotifications, pktcMdiMdiType=pktcMdiMdiType, pktcMdiMdiEntry=pktcMdiMdiEntry, pktcMdiMdiTable=pktcMdiMdiTable)
