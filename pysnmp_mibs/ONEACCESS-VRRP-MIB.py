#
# PySNMP MIB module ONEACCESS-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-VRRP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:05 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacExpIMVrrpNotifications, oacMIBModules, oacExpIMIpVrrp = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMVrrpNotifications", "oacMIBModules", "oacExpIMIpVrrp")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacVrrpMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 670))
oacVrrpMIBModule.setRevisions(('2011-10-27 00:00',))
if mibBuilder.loadTexts: oacVrrpMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacVrrpMIBModule.setOrganization(' OneAccess ')
vrrpTrapNewBackup = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 5, 1, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
if mibBuilder.loadTexts: vrrpTrapNewBackup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-VRRP-MIB", oacVrrpMIBModule=oacVrrpMIBModule, vrrpTrapNewBackup=vrrpTrapNewBackup, PYSNMP_MODULE_ID=oacVrrpMIBModule)
