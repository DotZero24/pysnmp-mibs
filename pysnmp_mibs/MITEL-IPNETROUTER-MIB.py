#
# PySNMP MIB module MITEL-IPNETROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mitel/MITEL-IPNETROUTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MITEL-IPNETROUTER-MIB", mitelRouterPppGroup=mitelRouterPppGroup, mitelRouterIpRouterGroup=mitelRouterIpRouterGroup, mitelProprietary=mitelProprietary, mitel=mitel, mitelRouterLogicalGroup=mitelRouterLogicalGroup, mitelPropIpNetworking=mitelPropIpNetworking, mitelRouterIpGroup=mitelRouterIpGroup, mitelRouterRipExtensionGroup=mitelRouterRipExtensionGroup, mitelIpNetRouter=mitelIpNetRouter, mitelRouterDhcpGroup=mitelRouterDhcpGroup, mitelRouterSnmpTrapGroup=mitelRouterSnmpTrapGroup, PYSNMP_MODULE_ID=mitelIpNetRouter)
