#
# PySNMP MIB module BRCM-RG-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/broadcom/BRCM-RG-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:18:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cableDataMgmtMIBObjects, = mibBuilder.importSymbols("BRCM-CABLEDATA-MGMT-MIB", "cableDataMgmtMIBObjects")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BRCM-RG-MGMT-MIB", PYSNMP_MODULE_ID=residentialGatewayMgmt, rgRipEnabled=rgRipEnabled, rgMgmtBase=rgMgmtBase, rgOperMode=rgOperMode, rgVpnEnabled=rgVpnEnabled, residentialGatewayMgmt=residentialGatewayMgmt)
