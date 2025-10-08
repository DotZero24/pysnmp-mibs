#
# PySNMP MIB module ME1200-UPNP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ME1200-UPNP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:27:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ME1200Unsigned8, = mibBuilder.importSymbols("ME1200-TC", "ME1200Unsigned8")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
me1200UpnpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52))
me1200UpnpMib.setRevisions(('2014-04-14 00:00',))
if mibBuilder.loadTexts: me1200UpnpMib.setLastUpdated('201404140000Z')
if mibBuilder.loadTexts: me1200UpnpMib.setOrganization('Cisco Systems, Inc')
me1200UpnpMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1))
me1200UpnpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2))
me1200UpnpConfigGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2, 1))
me1200UpnpConfigGlobalsMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200UpnpConfigGlobalsMode.setStatus('current')
me1200UpnpConfigGlobalsTtl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2, 1, 2), ME1200Unsigned8().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200UpnpConfigGlobalsTtl.setStatus('current')
me1200UpnpConfigGlobalsAdvertisingDuration = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 86400))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200UpnpConfigGlobalsAdvertisingDuration.setStatus('current')
me1200UpnpMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2))
me1200UpnpMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2, 1))
me1200UpnpMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2, 2))
me1200UpnpConfigGlobalsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2, 2, 1)).setObjects(("ME1200-UPNP-MIB", "me1200UpnpConfigGlobalsMode"), ("ME1200-UPNP-MIB", "me1200UpnpConfigGlobalsTtl"), ("ME1200-UPNP-MIB", "me1200UpnpConfigGlobalsAdvertisingDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200UpnpConfigGlobalsInfoGroup = me1200UpnpConfigGlobalsInfoGroup.setStatus('current')
me1200UpnpMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 52, 2, 1, 1)).setObjects(("ME1200-UPNP-MIB", "me1200UpnpConfigGlobalsInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200UpnpMibCompliance = me1200UpnpMibCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-UPNP-MIB", me1200UpnpMibConformance=me1200UpnpMibConformance, me1200UpnpMibCompliances=me1200UpnpMibCompliances, me1200UpnpConfigGlobalsInfoGroup=me1200UpnpConfigGlobalsInfoGroup, me1200UpnpConfigGlobalsMode=me1200UpnpConfigGlobalsMode, me1200UpnpConfigGlobalsTtl=me1200UpnpConfigGlobalsTtl, me1200UpnpConfig=me1200UpnpConfig, me1200UpnpMibObjects=me1200UpnpMibObjects, me1200UpnpMib=me1200UpnpMib, me1200UpnpMibCompliance=me1200UpnpMibCompliance, PYSNMP_MODULE_ID=me1200UpnpMib, me1200UpnpMibGroups=me1200UpnpMibGroups, me1200UpnpConfigGlobals=me1200UpnpConfigGlobals, me1200UpnpConfigGlobalsAdvertisingDuration=me1200UpnpConfigGlobalsAdvertisingDuration)
