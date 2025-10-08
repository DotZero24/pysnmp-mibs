#
# PySNMP MIB module RADIUS-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/RADIUS-ACCOUNTING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:26 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swRadiusAccountMGMTMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 55))
if mibBuilder.loadTexts: swRadiusAccountMGMTMIB.setLastUpdated('0712200000Z')
if mibBuilder.loadTexts: swRadiusAccountMGMTMIB.setOrganization('D-Link Corp.')
radiusAccountCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 55, 1))
accountingShellState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 55, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accountingShellState.setStatus('current')
accountingSystemState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 55, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accountingSystemState.setStatus('current')
accountingNetworkState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 55, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accountingNetworkState.setStatus('current')
mibBuilder.exportSymbols("RADIUS-ACCOUNTING-MIB", radiusAccountCtrl=radiusAccountCtrl, PYSNMP_MODULE_ID=swRadiusAccountMGMTMIB, accountingNetworkState=accountingNetworkState, accountingSystemState=accountingSystemState, swRadiusAccountMGMTMIB=swRadiusAccountMGMTMIB, accountingShellState=accountingShellState)
