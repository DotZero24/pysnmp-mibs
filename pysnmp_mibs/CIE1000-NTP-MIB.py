#
# PySNMP MIB module CIE1000-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CIE1000-NTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:27:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
CIE1000InetAddress, = mibBuilder.importSymbols("CIE1000-TC", "CIE1000InetAddress")
cie1000SwitchMgmt, = mibBuilder.importSymbols("CISCO-IE1000-MIB", "cie1000SwitchMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
cie1000NtpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57))
cie1000NtpMib.setRevisions(('2014-10-10 00:00', '2014-07-01 00:00',))
if mibBuilder.loadTexts: cie1000NtpMib.setLastUpdated('201410100000Z')
if mibBuilder.loadTexts: cie1000NtpMib.setOrganization('Cisco Systems, Inc.')
cie1000NtpMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1))
cie1000NtpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2))
cie1000NtpConfigGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 1))
cie1000NtpConfigGlobalsMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000NtpConfigGlobalsMode.setStatus('current')
cie1000NtpConfigServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 2), )
if mibBuilder.loadTexts: cie1000NtpConfigServerTable.setStatus('current')
cie1000NtpConfigServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 2, 1), ).setIndexNames((0, "CIE1000-NTP-MIB", "cie1000NtpConfigServerIndex"))
if mibBuilder.loadTexts: cie1000NtpConfigServerEntry.setStatus('current')
cie1000NtpConfigServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cie1000NtpConfigServerIndex.setStatus('current')
cie1000NtpConfigServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 2, 1, 2), CIE1000InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cie1000NtpConfigServerAddress.setStatus('current')
cie1000NtpMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2))
cie1000NtpMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 1))
cie1000NtpMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 2))
cie1000NtpConfigGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 2, 1)).setObjects(("CIE1000-NTP-MIB", "cie1000NtpConfigGlobalsMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000NtpConfigGlobalsInfoGroup = cie1000NtpConfigGlobalsInfoGroup.setStatus('current')
cie1000NtpConfigServerTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 2, 2)).setObjects(("CIE1000-NTP-MIB", "cie1000NtpConfigServerIndex"), ("CIE1000-NTP-MIB", "cie1000NtpConfigServerAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000NtpConfigServerTableInfoGroup = cie1000NtpConfigServerTableInfoGroup.setStatus('current')
cie1000NtpMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 1, 1)).setObjects(("CIE1000-NTP-MIB", "cie1000NtpConfigGlobalsInfoGroup"), ("CIE1000-NTP-MIB", "cie1000NtpConfigServerTableInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cie1000NtpMibCompliance = cie1000NtpMibCompliance.setStatus('current')
mibBuilder.exportSymbols("CIE1000-NTP-MIB", cie1000NtpMib=cie1000NtpMib, PYSNMP_MODULE_ID=cie1000NtpMib, cie1000NtpMibCompliance=cie1000NtpMibCompliance, cie1000NtpConfigServerTable=cie1000NtpConfigServerTable, cie1000NtpConfigGlobalsMode=cie1000NtpConfigGlobalsMode, cie1000NtpConfigServerEntry=cie1000NtpConfigServerEntry, cie1000NtpMibCompliances=cie1000NtpMibCompliances, cie1000NtpConfigServerTableInfoGroup=cie1000NtpConfigServerTableInfoGroup, cie1000NtpMibObjects=cie1000NtpMibObjects, cie1000NtpConfigServerAddress=cie1000NtpConfigServerAddress, cie1000NtpMibGroups=cie1000NtpMibGroups, cie1000NtpConfigGlobalsInfoGroup=cie1000NtpConfigGlobalsInfoGroup, cie1000NtpConfigServerIndex=cie1000NtpConfigServerIndex, cie1000NtpConfig=cie1000NtpConfig, cie1000NtpMibConformance=cie1000NtpMibConformance, cie1000NtpConfigGlobals=cie1000NtpConfigGlobals)
