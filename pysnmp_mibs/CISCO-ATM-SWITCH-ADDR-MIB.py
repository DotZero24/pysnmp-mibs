#
# PySNMP MIB module CISCO-ATM-SWITCH-ADDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ATM-SWITCH-ADDR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:30:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoAtmSwAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 51))
ciscoAtmSwAddrMIB.setRevisions(('1996-01-10 00:00',))
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setLastUpdated('9601100000Z')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setOrganization('Cisco Systems, Inc.')
ciscoAtmSwAddrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 1))
class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
ciscoAtmSwAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1), )
if mibBuilder.loadTexts: ciscoAtmSwAddrTable.setStatus('current')
ciscoAtmSwAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1), ).setIndexNames((0, "CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrIndex"))
if mibBuilder.loadTexts: ciscoAtmSwAddrEntry.setStatus('current')
ciscoAtmSwAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ciscoAtmSwAddrIndex.setStatus('current')
ciscoAtmSwAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 2), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoAtmSwAddrAddress.setStatus('current')
ciscoAtmSwAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoAtmSwAddrRowStatus.setStatus('current')
ciscoAtmSwAddrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3))
ciscoAtmSwAddrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1))
ciscoAtmSwAddrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2))
ciscoAtmSwAddrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmSwAddrMIBCompliance = ciscoAtmSwAddrMIBCompliance.setStatus('current')
ciscoAtmSwAddrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2, 1)).setObjects(("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrAddress"), ("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmSwAddrMIBGroup = ciscoAtmSwAddrMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-SWITCH-ADDR-MIB", ciscoAtmSwAddrRowStatus=ciscoAtmSwAddrRowStatus, ciscoAtmSwAddrMIB=ciscoAtmSwAddrMIB, ciscoAtmSwAddrMIBGroups=ciscoAtmSwAddrMIBGroups, ciscoAtmSwAddrMIBConformance=ciscoAtmSwAddrMIBConformance, ciscoAtmSwAddrEntry=ciscoAtmSwAddrEntry, ciscoAtmSwAddrMIBGroup=ciscoAtmSwAddrMIBGroup, ciscoAtmSwAddrMIBObjects=ciscoAtmSwAddrMIBObjects, AtmAddr=AtmAddr, ciscoAtmSwAddrAddress=ciscoAtmSwAddrAddress, ciscoAtmSwAddrMIBCompliance=ciscoAtmSwAddrMIBCompliance, ciscoAtmSwAddrTable=ciscoAtmSwAddrTable, ciscoAtmSwAddrMIBCompliances=ciscoAtmSwAddrMIBCompliances, PYSNMP_MODULE_ID=ciscoAtmSwAddrMIB, ciscoAtmSwAddrIndex=ciscoAtmSwAddrIndex)
