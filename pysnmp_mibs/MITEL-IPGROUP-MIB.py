#
# PySNMP MIB module MITEL-IPGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mitel/MITEL-IPGROUP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:04:57 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelRouterIpGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelRouterIpGroup.setRevisions(('2003-03-24 09:08', '1999-03-01 00:00',))
if mibBuilder.loadTexts: mitelRouterIpGroup.setLastUpdated('200303240908Z')
if mibBuilder.loadTexts: mitelRouterIpGroup.setOrganization('MITEL Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelIpGrpFilterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 1))
mitelIpGrpNatGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 2))
mitelIpGrpDnsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3))
mitelIpGrpIpVirtualGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 4))
mitelIpGrpLogicalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 5))
mitelIpGrpBackupWANGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 6))
mibBuilder.exportSymbols("MITEL-IPGROUP-MIB", mitelIpGrpIpVirtualGroup=mitelIpGrpIpVirtualGroup, mitelIpGrpDnsGroup=mitelIpGrpDnsGroup, mitelIpNetRouter=mitelIpNetRouter, mitelProprietary=mitelProprietary, mitel=mitel, mitelIpGrpLogicalGroup=mitelIpGrpLogicalGroup, mitelRouterIpGroup=mitelRouterIpGroup, PYSNMP_MODULE_ID=mitelRouterIpGroup, mitelPropIpNetworking=mitelPropIpNetworking, mitelIpGrpFilterGroup=mitelIpGrpFilterGroup, mitelIpGrpBackupWANGroup=mitelIpGrpBackupWANGroup, mitelIpGrpNatGroup=mitelIpGrpNatGroup)
