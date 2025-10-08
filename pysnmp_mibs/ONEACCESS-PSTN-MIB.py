#
# PySNMP MIB module ONEACCESS-PSTN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-PSTN-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:19 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifName, ifType, ifAlias, ifOperStatus, ifDescr, ifIndex, ifAdminStatus = mibBuilder.importSymbols("IF-MIB", "ifName", "ifType", "ifAlias", "ifOperStatus", "ifDescr", "ifIndex", "ifAdminStatus")
oacEventText, = mibBuilder.importSymbols("ONEACCESS-EVENTS-MIB", "oacEventText")
oacExpIMPstnNotifications, oacExpIMPstn, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMPstnNotifications", "oacExpIMPstn", "oacMIBModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacPstnMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 672))
oacPstnMIBModule.setRevisions(('2011-10-27 00:00',))
if mibBuilder.loadTexts: oacPstnMIBModule.setLastUpdated('201110270000Z')
if mibBuilder.loadTexts: oacPstnMIBModule.setOrganization(' OneAccess ')
dialDown = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialDown.setStatus('current')
dialUp = NotificationType((1, 3, 6, 1, 4, 1, 13191, 10, 3, 6, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifName"), ("IF-MIB", "ifAlias"))
if mibBuilder.loadTexts: dialUp.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-PSTN-MIB", PYSNMP_MODULE_ID=oacPstnMIBModule, oacPstnMIBModule=oacPstnMIBModule, dialUp=dialUp, dialDown=dialDown)
