#
# PySNMP MIB module RADIUS-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/RADIUS-ACCOUNTING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
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
mibBuilder.exportSymbols("RADIUS-ACCOUNTING-MIB", swRadiusAccountMGMTMIB=swRadiusAccountMGMTMIB, accountingSystemState=accountingSystemState, radiusAccountCtrl=radiusAccountCtrl, PYSNMP_MODULE_ID=swRadiusAccountMGMTMIB, accountingNetworkState=accountingNetworkState, accountingShellState=accountingShellState)
