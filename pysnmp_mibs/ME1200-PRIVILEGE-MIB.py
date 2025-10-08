#
# PySNMP MIB module ME1200-PRIVILEGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/ME1200-PRIVILEGE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:31:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
me1200SwitchMgmt, = mibBuilder.importSymbols("CISCOME1200-MIB", "me1200SwitchMgmt")
ME1200DisplayString, = mibBuilder.importSymbols("ME1200-TC", "ME1200DisplayString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
me1200PrivilegeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59))
me1200PrivilegeMib.setRevisions(('2014-04-17 00:00',))
if mibBuilder.loadTexts: me1200PrivilegeMib.setLastUpdated('201404170000Z')
if mibBuilder.loadTexts: me1200PrivilegeMib.setOrganization('Cisco Systems, Inc')
me1200PrivilegeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1))
me1200PrivilegeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2))
me1200PrivilegeConfigWebTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1), )
if mibBuilder.loadTexts: me1200PrivilegeConfigWebTable.setStatus('current')
me1200PrivilegeConfigWebEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1), ).setIndexNames((0, "ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebModuleName"))
if mibBuilder.loadTexts: me1200PrivilegeConfigWebEntry.setStatus('current')
me1200PrivilegeConfigWebModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 1), ME1200DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31)))
if mibBuilder.loadTexts: me1200PrivilegeConfigWebModuleName.setStatus('current')
me1200PrivilegeConfigWebConfigRoPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200PrivilegeConfigWebConfigRoPriv.setStatus('current')
me1200PrivilegeConfigWebConfigRwPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200PrivilegeConfigWebConfigRwPriv.setStatus('current')
me1200PrivilegeConfigWebStatusRoPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200PrivilegeConfigWebStatusRoPriv.setStatus('current')
me1200PrivilegeConfigWebStatusRwPriv = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: me1200PrivilegeConfigWebStatusRwPriv.setStatus('current')
me1200PrivilegeMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2))
me1200PrivilegeMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2, 1))
me1200PrivilegeMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2, 2))
me1200PrivilegeConfigWebInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2, 2, 1)).setObjects(("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebConfigRoPriv"), ("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebConfigRwPriv"), ("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebStatusRoPriv"), ("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebStatusRwPriv"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200PrivilegeConfigWebInfoGroup = me1200PrivilegeConfigWebInfoGroup.setStatus('current')
me1200PrivilegeMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 59, 2, 1, 1)).setObjects(("ME1200-PRIVILEGE-MIB", "me1200PrivilegeConfigWebInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    me1200PrivilegeMibCompliance = me1200PrivilegeMibCompliance.setStatus('current')
mibBuilder.exportSymbols("ME1200-PRIVILEGE-MIB", me1200PrivilegeConfigWebEntry=me1200PrivilegeConfigWebEntry, me1200PrivilegeConfig=me1200PrivilegeConfig, me1200PrivilegeConfigWebStatusRoPriv=me1200PrivilegeConfigWebStatusRoPriv, me1200PrivilegeConfigWebModuleName=me1200PrivilegeConfigWebModuleName, me1200PrivilegeConfigWebStatusRwPriv=me1200PrivilegeConfigWebStatusRwPriv, me1200PrivilegeMib=me1200PrivilegeMib, PYSNMP_MODULE_ID=me1200PrivilegeMib, me1200PrivilegeConfigWebInfoGroup=me1200PrivilegeConfigWebInfoGroup, me1200PrivilegeMibCompliances=me1200PrivilegeMibCompliances, me1200PrivilegeConfigWebConfigRwPriv=me1200PrivilegeConfigWebConfigRwPriv, me1200PrivilegeMibCompliance=me1200PrivilegeMibCompliance, me1200PrivilegeConfigWebTable=me1200PrivilegeConfigWebTable, me1200PrivilegeMibGroups=me1200PrivilegeMibGroups, me1200PrivilegeMibObjects=me1200PrivilegeMibObjects, me1200PrivilegeConfigWebConfigRoPriv=me1200PrivilegeConfigWebConfigRoPriv, me1200PrivilegeMibConformance=me1200PrivilegeMibConformance)
