#
# PySNMP MIB module CISCO-LEC-DATA-VCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-LEC-DATA-VCC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:24:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
atmVclVci, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
lecIndex, AtmLaneAddress = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "lecIndex", "AtmLaneAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLecDataVccMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 69))
ciscoLecDataVccMIB.setRevisions(('1997-01-06 00:00',))
if mibBuilder.loadTexts: ciscoLecDataVccMIB.setLastUpdated('9701060000Z')
if mibBuilder.loadTexts: ciscoLecDataVccMIB.setOrganization('Cisco Systems, Inc.')
ciscoLecDataVccMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 1))
cLecDataDirectVcc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1))
cLecDataDirectVccTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1), )
if mibBuilder.loadTexts: cLecDataDirectVccTable.setStatus('current')
cLecDataDirectVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1), ).setIndexNames((0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"), (0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: cLecDataDirectVccEntry.setStatus('current')
cLecDataDirectLocalAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1, 1), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLecDataDirectLocalAtmAddress.setStatus('current')
cLecDataDirectRemoteAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1, 2), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLecDataDirectRemoteAtmAddress.setStatus('current')
ciscoLecDataVccMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 2))
ciscoLecDataVccMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 2, 0))
ciscoLecDataVccMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 3))
ciscoLecDataVccMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 1))
ciscoLecDataVccMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 2))
ciscoLecDataVccMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 1, 1)).setObjects(("CISCO-LEC-DATA-VCC-MIB", "ciscoLecDataVccBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecDataVccMIBCompliance = ciscoLecDataVccMIBCompliance.setStatus('current')
ciscoLecDataVccBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 2, 1)).setObjects(("CISCO-LEC-DATA-VCC-MIB", "cLecDataDirectLocalAtmAddress"), ("CISCO-LEC-DATA-VCC-MIB", "cLecDataDirectRemoteAtmAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecDataVccBaseMIBGroup = ciscoLecDataVccBaseMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-LEC-DATA-VCC-MIB", ciscoLecDataVccBaseMIBGroup=ciscoLecDataVccBaseMIBGroup, ciscoLecDataVccMIBConformance=ciscoLecDataVccMIBConformance, ciscoLecDataVccMIBObjects=ciscoLecDataVccMIBObjects, ciscoLecDataVccMIBCompliances=ciscoLecDataVccMIBCompliances, cLecDataDirectRemoteAtmAddress=cLecDataDirectRemoteAtmAddress, ciscoLecDataVccMIBNotifications=ciscoLecDataVccMIBNotifications, cLecDataDirectLocalAtmAddress=cLecDataDirectLocalAtmAddress, ciscoLecDataVccMIBCompliance=ciscoLecDataVccMIBCompliance, cLecDataDirectVcc=cLecDataDirectVcc, ciscoLecDataVccMIBGroups=ciscoLecDataVccMIBGroups, ciscoLecDataVccMIB=ciscoLecDataVccMIB, PYSNMP_MODULE_ID=ciscoLecDataVccMIB, ciscoLecDataVccMIBNotificationPrefix=ciscoLecDataVccMIBNotificationPrefix, cLecDataDirectVccTable=cLecDataDirectVccTable, cLecDataDirectVccEntry=cLecDataDirectVccEntry)
