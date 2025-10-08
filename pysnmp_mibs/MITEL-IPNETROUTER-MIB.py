#
# PySNMP MIB module MITEL-IPNETROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mitel/MITEL-IPNETROUTER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:39 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelIpNetRouter = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpNetRouter.setRevisions(('2003-03-24 09:27', '1999-03-01 00:00',))
if mibBuilder.loadTexts: mitelIpNetRouter.setLastUpdated('200303240927Z')
if mibBuilder.loadTexts: mitelIpNetRouter.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelRouterPppGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 2))
mitelRouterDhcpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3))
mitelRouterLogicalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 4))
mitelRouterIpRouterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 5))
mitelRouterRipExtensionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6))
mitelRouterSnmpTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 7))
mibBuilder.exportSymbols("MITEL-IPNETROUTER-MIB", mitelProprietary=mitelProprietary, mitelRouterLogicalGroup=mitelRouterLogicalGroup, mitelPropIpNetworking=mitelPropIpNetworking, mitelRouterDhcpGroup=mitelRouterDhcpGroup, mitelRouterRipExtensionGroup=mitelRouterRipExtensionGroup, mitelRouterSnmpTrapGroup=mitelRouterSnmpTrapGroup, mitel=mitel, mitelRouterIpGroup=mitelRouterIpGroup, mitelIpNetRouter=mitelIpNetRouter, mitelRouterIpRouterGroup=mitelRouterIpRouterGroup, mitelRouterPppGroup=mitelRouterPppGroup, PYSNMP_MODULE_ID=mitelIpNetRouter)
