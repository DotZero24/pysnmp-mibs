#
# PySNMP MIB module ONEACCESS-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-VRRP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:23 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacExpIMVrrpNotifications, oacExpIMIpVrrp, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMVrrpNotifications", "oacExpIMIpVrrp", "oacMIBModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacVrrpMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 670))
oacVrrpMIBModule.setRevisions(('2011-10-27 00:00',))
if mibBuilder.loadTexts: oacVrrpMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacVrrpMIBModule.setOrganization(' OneAccess ')
vrrpTrapNewBackup = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 5, 1, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
if mibBuilder.loadTexts: vrrpTrapNewBackup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-VRRP-MIB", PYSNMP_MODULE_ID=oacVrrpMIBModule, vrrpTrapNewBackup=vrrpTrapNewBackup, oacVrrpMIBModule=oacVrrpMIBModule)
