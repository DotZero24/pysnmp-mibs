#
# PySNMP MIB module ME1200-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ME1200-NTP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:26:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ME1200InetAddress, = mibBuilder.importSymbols("ME1200-TC", "ME1200InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
me1200NtpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57))
me1200NtpMib.setRevisions(('2014-05-21 00:00',))
if mibBuilder.loadTexts: me1200NtpMib.setLastUpdated('201405210000Z')
if mibBuilder.loadTexts: me1200NtpMib.setOrganization('Cisco Systems, Inc')
me1200NtpMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1))
me1200NtpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2))
me1200NtpConfigGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 1))
me1200NtpConfigGlobalsMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200NtpConfigGlobalsMode.setStatus('current')
me1200NtpConfigServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 2), )
if mibBuilder.loadTexts: me1200NtpConfigServerTable.setStatus('current')
me1200NtpConfigServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 2, 1), ).setIndexNames((0, "ME1200-NTP-MIB", "me1200NtpConfigServerIndex"))
if mibBuilder.loadTexts: me1200NtpConfigServerEntry.setStatus('current')
me1200NtpConfigServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: me1200NtpConfigServerIndex.setStatus('current')
me1200NtpConfigServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 2, 1, 2), ME1200InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200NtpConfigServerAddress.setStatus('current')
me1200NtpMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2))
me1200NtpMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 1))
me1200NtpMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 2))
me1200NtpConfigGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 2, 1)).setObjects(("ME1200-NTP-MIB", "me1200NtpConfigGlobalsMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200NtpConfigGlobalsInfoGroup = me1200NtpConfigGlobalsInfoGroup.setStatus('current')
me1200NtpConfigServerTableInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 2, 2)).setObjects(("ME1200-NTP-MIB", "me1200NtpConfigServerAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200NtpConfigServerTableInfoGroup = me1200NtpConfigServerTableInfoGroup.setStatus('current')
me1200NtpMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 1, 1)).setObjects(("ME1200-NTP-MIB", "me1200NtpConfigGlobalsInfoGroup"), ("ME1200-NTP-MIB", "me1200NtpConfigServerTableInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200NtpMibCompliance = me1200NtpMibCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-NTP-MIB", me1200NtpMib=me1200NtpMib, PYSNMP_MODULE_ID=me1200NtpMib, me1200NtpConfigGlobalsInfoGroup=me1200NtpConfigGlobalsInfoGroup, me1200NtpConfigServerIndex=me1200NtpConfigServerIndex, me1200NtpConfigServerAddress=me1200NtpConfigServerAddress, me1200NtpMibCompliances=me1200NtpMibCompliances, me1200NtpMibGroups=me1200NtpMibGroups, me1200NtpConfigServerTableInfoGroup=me1200NtpConfigServerTableInfoGroup, me1200NtpMibCompliance=me1200NtpMibCompliance, me1200NtpConfigGlobals=me1200NtpConfigGlobals, me1200NtpConfigServerEntry=me1200NtpConfigServerEntry, me1200NtpConfigGlobalsMode=me1200NtpConfigGlobalsMode, me1200NtpMibConformance=me1200NtpMibConformance, me1200NtpConfig=me1200NtpConfig, me1200NtpMibObjects=me1200NtpMibObjects, me1200NtpConfigServerTable=me1200NtpConfigServerTable)
