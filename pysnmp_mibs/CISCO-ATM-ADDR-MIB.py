#
# PySNMP MIB module CISCO-ATM-ADDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-ATM-ADDR-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:23:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
ciscoAtmAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 12))
ciscoAtmAddrMIB.setRevisions(('1996-05-06 00:00',))
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setLastUpdated('9605060000Z')
if mibBuilder.loadTexts: ciscoAtmAddrMIB.setOrganization('Cisco Systems, Inc.')
class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
ciscoAtmAddrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 1))
ciscoAtmIfAdminAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1), )
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrTable.setStatus('current')
ciscoAtmIfAdminAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrAddress"))
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrEntry.setStatus('current')
ciscoAtmIfAdminAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 1), AtmAddr())
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrAddress.setStatus('current')
ciscoAtmIfAdminAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciscoAtmIfAdminAddrRowStatus.setStatus('current')
ciscoAtmIfAdminAddrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3))
ciscoAtmIfAdminAddrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1))
ciscoAtmIfAdminAddrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2))
ciscoAtmIfAdminAddrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1, 1)).setObjects(("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfAdminAddrMIBCompliance = ciscoAtmIfAdminAddrMIBCompliance.setStatus('current')
ciscoAtmIfAdminAddrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2, 1)).setObjects(("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmIfAdminAddrMIBGroup = ciscoAtmIfAdminAddrMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-ADDR-MIB", ciscoAtmIfAdminAddrMIBCompliance=ciscoAtmIfAdminAddrMIBCompliance, ciscoAtmIfAdminAddrEntry=ciscoAtmIfAdminAddrEntry, ciscoAtmIfAdminAddrTable=ciscoAtmIfAdminAddrTable, ciscoAtmIfAdminAddrMIBConformance=ciscoAtmIfAdminAddrMIBConformance, PYSNMP_MODULE_ID=ciscoAtmAddrMIB, ciscoAtmIfAdminAddrMIBCompliances=ciscoAtmIfAdminAddrMIBCompliances, AtmAddr=AtmAddr, ciscoAtmIfAdminAddrMIBGroup=ciscoAtmIfAdminAddrMIBGroup, ciscoAtmIfAdminAddrAddress=ciscoAtmIfAdminAddrAddress, ciscoAtmIfAdminAddrMIBGroups=ciscoAtmIfAdminAddrMIBGroups, ciscoAtmAddrMIBObjects=ciscoAtmAddrMIBObjects, ciscoAtmAddrMIB=ciscoAtmAddrMIB, ciscoAtmIfAdminAddrRowStatus=ciscoAtmIfAdminAddrRowStatus)
