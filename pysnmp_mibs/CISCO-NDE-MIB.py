#
# PySNMP MIB module CISCO-NDE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-NDE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:15:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("CISCO-NDE-MIB", cndeMIBGroups=cndeMIBGroups, ciscoNDEMIB=ciscoNDEMIB, cndeMIBNotifs=cndeMIBNotifs, cndeMIBNotifications=cndeMIBNotifications, cndeMIBCompliance=cndeMIBCompliance, cndeCollectorEntry=cndeCollectorEntry, cndeCollectorAddress=cndeCollectorAddress, cndeMIBConformance=cndeMIBConformance, cndeCollectorPort=cndeCollectorPort, PYSNMP_MODULE_ID=ciscoNDEMIB, ciscoNDEMIBObjects=ciscoNDEMIBObjects, cndeMIBCompliances=cndeMIBCompliances, cndeCollectorTable=cndeCollectorTable, cndeCollectorStatus=cndeCollectorStatus, cndeCollectorAddressType=cndeCollectorAddressType, cndeCollectorConfigurationGroup=cndeCollectorConfigurationGroup, cndeCollectorConfiguration=cndeCollectorConfiguration, cndeMaxCollectors=cndeMaxCollectors)
