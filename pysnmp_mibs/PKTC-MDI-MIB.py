#
# PySNMP MIB module PKTC-MDI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/PKTC-MDI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pktcApplicationMibs, = mibBuilder.importSymbols("CLAB-DEF-MIB", "pktcApplicationMibs")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("PKTC-MDI-MIB", pktcMdiNslTable=pktcMdiNslTable, pktcMdiGroup=pktcMdiGroup, pktcMdiNslPortListOut=pktcMdiNslPortListOut, pktcMdiMdiEntry=pktcMdiMdiEntry, pktcMdiNslIndex=pktcMdiNslIndex, pktcMdiNslEntry=pktcMdiNslEntry, pktcMdiNslName=pktcMdiNslName, PktcMdiType=PktcMdiType, pktcMdiMdiType=pktcMdiMdiType, pktcMdiNslRowStatus=pktcMdiNslRowStatus, pktcMdiCompliance=pktcMdiCompliance, pktcMdiMdiActivityStatus=pktcMdiMdiActivityStatus, pktcMdiMibGroups=pktcMdiMibGroups, pktcMdiMibCompliances=pktcMdiMibCompliances, pktcMdiMibConformance=pktcMdiMibConformance, pktcMdiNslPortListIn=pktcMdiNslPortListIn, pktcMdiNotifications=pktcMdiNotifications, PYSNMP_MODULE_ID=pktcMdiMib, pktcMdiMib=pktcMdiMib, pktcMdiObjects=pktcMdiObjects, pktcMdiMdiName=pktcMdiMdiName, pktcMdiMdiTable=pktcMdiMdiTable)
