#
# PySNMP MIB module FS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsGatewayProducts, = mibBuilder.importSymbols("FS-GATEWAY-SMI", "fsGatewayProducts")
fsRouterProducts, = mibBuilder.importSymbols("FS-ROUTER-SMI", "fsRouterProducts")
fsSmartClassProducts, = mibBuilder.importSymbols("FS-SMARTCLASS-SMI", "fsSmartClassProducts")
fsModules, fsSwitchProducts = mibBuilder.importSymbols("FS-SMI", "fsModules", "fsSwitchProducts")
fsSoftwareProducts, = mibBuilder.importSymbols("FS-SOFTWARE-SMI", "fsSoftwareProducts")
fsWirelessProducts, = mibBuilder.importSymbols("FS-WIRELESS-SMI", "fsWirelessProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 4, 1))
fsProductsMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: fsProductsMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: fsProductsMIB.setOrganization('FS.COM Inc..')
S5860_20SQ = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 1, 1)).setLabel("S5860-20SQ")
S5860_24XB_U = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 1, 2)).setLabel("S5860-24XB-U")
mibBuilder.exportSymbols("FS-PRODUCTS-MIB", fsProductsMIB=fsProductsMIB, S5860_24XB_U=S5860_24XB_U, PYSNMP_MODULE_ID=fsProductsMIB, S5860_20SQ=S5860_20SQ)
