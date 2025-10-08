#
# PySNMP MIB module FS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/fscom/FS-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:01:09 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fsGatewayProducts, = mibBuilder.importSymbols("FS-GATEWAY-SMI", "fsGatewayProducts")
fsRouterProducts, = mibBuilder.importSymbols("FS-ROUTER-SMI", "fsRouterProducts")
fsSmartClassProducts, = mibBuilder.importSymbols("FS-SMARTCLASS-SMI", "fsSmartClassProducts")
fsModules, fsSwitchProducts = mibBuilder.importSymbols("FS-SMI", "fsModules", "fsSwitchProducts")
fsSoftwareProducts, = mibBuilder.importSymbols("FS-SOFTWARE-SMI", "fsSoftwareProducts")
fsWirelessProducts, = mibBuilder.importSymbols("FS-WIRELESS-SMI", "fsWirelessProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fsProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 4, 1))
fsProductsMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: fsProductsMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: fsProductsMIB.setOrganization('FS.COM Inc..')
S5860_20SQ = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 1, 1)).setLabel("S5860-20SQ")
S5860_24XB_U = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 1, 2)).setLabel("S5860-24XB-U")
mibBuilder.exportSymbols("FS-PRODUCTS-MIB", PYSNMP_MODULE_ID=fsProductsMIB, S5860_24XB_U=S5860_24XB_U, fsProductsMIB=fsProductsMIB, S5860_20SQ=S5860_20SQ)
