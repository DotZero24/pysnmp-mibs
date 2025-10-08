#
# PySNMP MIB module BRCM-SNMP-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-SNMP-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataMgmtBase, = mibBuilder.importSymbols("BRCM-CABLEDATA-MGMT-MIB", "cableDataMgmtBase")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 2))
snmpMgmt.setRevisions(('2007-02-05 00:00', '2006-10-05 00:00', '2003-04-29 00:00',))
if mibBuilder.loadTexts: snmpMgmt.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: snmpMgmt.setOrganization('Broadcom Corporation')
snmpUdpPort = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 2, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(161)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpUdpPort.setStatus('current')
snmpNotifyUdpPort = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(162)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpNotifyUdpPort.setStatus('current')
snmpDscpTag = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpDscpTag.setStatus('current')
mibBuilder.exportSymbols("BRCM-SNMP-MGMT-MIB", snmpDscpTag=snmpDscpTag, PYSNMP_MODULE_ID=snmpMgmt, snmpMgmt=snmpMgmt, snmpNotifyUdpPort=snmpNotifyUdpPort, snmpUdpPort=snmpUdpPort)
