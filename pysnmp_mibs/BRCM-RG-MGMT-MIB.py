#
# PySNMP MIB module BRCM-RG-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-RG-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataMgmtMIBObjects, = mibBuilder.importSymbols("BRCM-CABLEDATA-MGMT-MIB", "cableDataMgmtMIBObjects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
residentialGatewayMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7))
residentialGatewayMgmt.setRevisions(('2007-02-05 00:00', '2004-06-16 00:00', '2003-03-31 00:00',))
if mibBuilder.loadTexts: residentialGatewayMgmt.setLastUpdated('200702050000Z')
if mibBuilder.loadTexts: residentialGatewayMgmt.setOrganization('Broadcom Corporation')
rgMgmtBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 1))
rgOperMode = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("residentialGateway", 2), ("cableHome10", 3), ("cableHome11", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgOperMode.setStatus('current')
rgRipEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgRipEnabled.setStatus('current')
rgVpnEnabled = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 7, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rgVpnEnabled.setStatus('current')
mibBuilder.exportSymbols("BRCM-RG-MGMT-MIB", residentialGatewayMgmt=residentialGatewayMgmt, rgOperMode=rgOperMode, rgMgmtBase=rgMgmtBase, PYSNMP_MODULE_ID=residentialGatewayMgmt, rgRipEnabled=rgRipEnabled, rgVpnEnabled=rgVpnEnabled)
