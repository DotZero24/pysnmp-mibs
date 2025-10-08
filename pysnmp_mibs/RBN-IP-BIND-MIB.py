#
# PySNMP MIB module RBN-IP-BIND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-IP-BIND-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:25 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnCircuitHandle, = mibBuilder.importSymbols("RBN-TC", "RbnCircuitHandle")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnIpBindMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 26))
rbnIpBindMib.setRevisions(('2002-08-20 12:00',))
if mibBuilder.loadTexts: rbnIpBindMib.setLastUpdated('200208201200Z')
if mibBuilder.loadTexts: rbnIpBindMib.setOrganization('Redback Networks, Inc.')
rbnIpBindMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 0))
rbnIpBindMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1))
rbnIpBindMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2))
rbnIpBindTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1), )
if mibBuilder.loadTexts: rbnIpBindTable.setStatus('current')
rbnIpBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RBN-IP-BIND-MIB", "rbnIpBindCircuitHandle"))
if mibBuilder.loadTexts: rbnIpBindEntry.setStatus('current')
rbnIpBindCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 1), RbnCircuitHandle())
if mibBuilder.loadTexts: rbnIpBindCircuitHandle.setStatus('current')
rbnIpBindIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnIpBindIfIndex.setStatus('current')
rbnIpBindHierarchicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnIpBindHierarchicalIfIndex.setStatus('current')
rbnIpBindCircuitDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnIpBindCircuitDescr.setStatus('current')
rbnIpBindContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 26, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnIpBindContextName.setStatus('current')
rbnIpBindCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 1))
rbnIpBindGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 2))
rbnIpBindCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 1, 1)).setObjects(("RBN-IP-BIND-MIB", "rbnIpBindDisplayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIpBindCompliance = rbnIpBindCompliance.setStatus('current')
rbnIpBindDisplayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 26, 2, 2, 1)).setObjects(("RBN-IP-BIND-MIB", "rbnIpBindIfIndex"), ("RBN-IP-BIND-MIB", "rbnIpBindHierarchicalIfIndex"), ("RBN-IP-BIND-MIB", "rbnIpBindCircuitDescr"), ("RBN-IP-BIND-MIB", "rbnIpBindContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnIpBindDisplayGroup = rbnIpBindDisplayGroup.setStatus('current')
mibBuilder.exportSymbols("RBN-IP-BIND-MIB", rbnIpBindTable=rbnIpBindTable, rbnIpBindContextName=rbnIpBindContextName, rbnIpBindCompliance=rbnIpBindCompliance, PYSNMP_MODULE_ID=rbnIpBindMib, rbnIpBindHierarchicalIfIndex=rbnIpBindHierarchicalIfIndex, rbnIpBindGroups=rbnIpBindGroups, rbnIpBindDisplayGroup=rbnIpBindDisplayGroup, rbnIpBindMibObjects=rbnIpBindMibObjects, rbnIpBindCircuitDescr=rbnIpBindCircuitDescr, rbnIpBindIfIndex=rbnIpBindIfIndex, rbnIpBindCircuitHandle=rbnIpBindCircuitHandle, rbnIpBindEntry=rbnIpBindEntry, rbnIpBindMib=rbnIpBindMib, rbnIpBindMibNotifications=rbnIpBindMibNotifications, rbnIpBindCompliances=rbnIpBindCompliances, rbnIpBindMibConformance=rbnIpBindMibConformance)
