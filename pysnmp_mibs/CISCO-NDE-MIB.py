#
# PySNMP MIB module CISCO-NDE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-NDE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoNDEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 226))
ciscoNDEMIB.setRevisions(('2006-03-01 00:00', '2005-12-06 00:00', '2001-08-08 00:00',))
if mibBuilder.loadTexts: ciscoNDEMIB.setLastUpdated('200603010000Z')
if mibBuilder.loadTexts: ciscoNDEMIB.setOrganization('Cisco Systems, Inc.')
ciscoNDEMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 1))
cndeCollectorConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1))
cndeMaxCollectors = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cndeMaxCollectors.setStatus('current')
cndeCollectorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2), )
if mibBuilder.loadTexts: cndeCollectorTable.setStatus('current')
cndeCollectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-NDE-MIB", "cndeCollectorAddressType"), (0, "CISCO-NDE-MIB", "cndeCollectorAddress"), (0, "CISCO-NDE-MIB", "cndeCollectorPort"))
if mibBuilder.loadTexts: cndeCollectorEntry.setStatus('current')
cndeCollectorAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: cndeCollectorAddressType.setStatus('current')
cndeCollectorAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 2), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cndeCollectorAddress.setStatus('current')
cndeCollectorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cndeCollectorPort.setStatus('current')
cndeCollectorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 226, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cndeCollectorStatus.setStatus('current')
cndeMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 2))
cndeMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 0))
cndeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 3))
cndeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 1))
cndeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 2))
cndeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 1, 1)).setObjects(("CISCO-NDE-MIB", "cndeCollectorConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cndeMIBCompliance = cndeMIBCompliance.setStatus('current')
cndeCollectorConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 226, 3, 2, 1)).setObjects(("CISCO-NDE-MIB", "cndeMaxCollectors"), ("CISCO-NDE-MIB", "cndeCollectorStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cndeCollectorConfigurationGroup = cndeCollectorConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NDE-MIB", cndeCollectorAddress=cndeCollectorAddress, cndeMIBNotifs=cndeMIBNotifs, ciscoNDEMIBObjects=ciscoNDEMIBObjects, cndeCollectorAddressType=cndeCollectorAddressType, cndeCollectorPort=cndeCollectorPort, cndeMIBGroups=cndeMIBGroups, cndeCollectorTable=cndeCollectorTable, cndeCollectorEntry=cndeCollectorEntry, PYSNMP_MODULE_ID=ciscoNDEMIB, ciscoNDEMIB=ciscoNDEMIB, cndeCollectorConfigurationGroup=cndeCollectorConfigurationGroup, cndeCollectorConfiguration=cndeCollectorConfiguration, cndeMIBConformance=cndeMIBConformance, cndeMIBCompliances=cndeMIBCompliances, cndeMaxCollectors=cndeMaxCollectors, cndeCollectorStatus=cndeCollectorStatus, cndeMIBCompliance=cndeMIBCompliance, cndeMIBNotifications=cndeMIBNotifications)
