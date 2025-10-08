#
# PySNMP MIB module ONEACCESS-PSTN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-PSTN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:02 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifAlias, ifType, ifDescr, ifName, ifIndex, ifAdminStatus, ifOperStatus = mibBuilder.importSymbols("IF-MIB", "ifAlias", "ifType", "ifDescr", "ifName", "ifIndex", "ifAdminStatus", "ifOperStatus")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacExpIMPstn, oacMIBModules, oacExpIMPstnNotifications = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMPstn", "oacMIBModules", "oacExpIMPstnNotifications")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacPstnMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 672))
oacPstnMIBModule.setRevisions(('2011-10-27 00:00',))
if mibBuilder.loadTexts: oacPstnMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacPstnMIBModule.setOrganization(' OneAccess ')
dialDown = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialDown.setStatus('current')
dialUp = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialUp.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-PSTN-MIB", PYSNMP_MODULE_ID=oacPstnMIBModule, oacPstnMIBModule=oacPstnMIBModule, dialUp=dialUp, dialDown=dialDown)
