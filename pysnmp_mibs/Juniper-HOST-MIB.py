#
# PySNMP MIB module Juniper-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/junose/Juniper-HOST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
juniHostMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33))
juniHostMIB.setRevisions(('2004-11-26 00:00', '2002-09-16 21:44', '2001-05-07 17:02', '2000-01-26 00:00',))
if mibBuilder.loadTexts: juniHostMIB.setLastUpdated('200209162144Z')
if mibBuilder.loadTexts: juniHostMIB.setOrganization('Juniper Networks, Inc.')
juniHostObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1))
juniHost = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1))
juniHostTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1), )
if mibBuilder.loadTexts: juniHostTable.setStatus('current')
juniHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1), ).setIndexNames((1, "Juniper-HOST-MIB", "juniHostName"))
if mibBuilder.loadTexts: juniHostEntry.setStatus('current')
juniHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniHostName.setStatus('current')
juniHostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHostIpAddress.setStatus('current')
juniHostProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("juniHostFtp", 1), ("juniHostTftp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHostProtocol.setStatus('current')
juniHostUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHostUserName.setStatus('current')
juniHostUserPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHostUserPassword.setStatus('current')
juniHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 1, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniHostRowStatus.setStatus('current')
juniHostMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4))
juniHostMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4, 1))
juniHostMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4, 2))
juniHostCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4, 1, 1)).setObjects(("Juniper-HOST-MIB", "juniHostGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHostCompliance = juniHostCompliance.setStatus('current')
juniHostGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 33, 4, 2, 1)).setObjects(("Juniper-HOST-MIB", "juniHostName"), ("Juniper-HOST-MIB", "juniHostIpAddress"), ("Juniper-HOST-MIB", "juniHostProtocol"), ("Juniper-HOST-MIB", "juniHostUserName"), ("Juniper-HOST-MIB", "juniHostUserPassword"), ("Juniper-HOST-MIB", "juniHostRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniHostGroup = juniHostGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-HOST-MIB", juniHostIpAddress=juniHostIpAddress, juniHostCompliance=juniHostCompliance, juniHostRowStatus=juniHostRowStatus, juniHostUserPassword=juniHostUserPassword, juniHostObjects=juniHostObjects, juniHostMIBGroups=juniHostMIBGroups, juniHostMIBCompliances=juniHostMIBCompliances, juniHostTable=juniHostTable, juniHostGroup=juniHostGroup, juniHostName=juniHostName, juniHostUserName=juniHostUserName, juniHost=juniHost, juniHostMIB=juniHostMIB, juniHostMIBConformance=juniHostMIBConformance, juniHostEntry=juniHostEntry, PYSNMP_MODULE_ID=juniHostMIB, juniHostProtocol=juniHostProtocol)
