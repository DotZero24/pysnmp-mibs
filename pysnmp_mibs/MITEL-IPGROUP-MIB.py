#
# PySNMP MIB module MITEL-IPGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mitel/MITEL-IPGROUP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:38:38 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MITEL-IPGROUP-MIB", mitelProprietary=mitelProprietary, mitelIpGrpBackupWANGroup=mitelIpGrpBackupWANGroup, mitelPropIpNetworking=mitelPropIpNetworking, mitelIpGrpFilterGroup=mitelIpGrpFilterGroup, mitelIpGrpIpVirtualGroup=mitelIpGrpIpVirtualGroup, mitel=mitel, mitelIpGrpDnsGroup=mitelIpGrpDnsGroup, mitelRouterIpGroup=mitelRouterIpGroup, mitelIpNetRouter=mitelIpNetRouter, mitelIpGrpNatGroup=mitelIpGrpNatGroup, mitelIpGrpLogicalGroup=mitelIpGrpLogicalGroup, PYSNMP_MODULE_ID=mitelRouterIpGroup)
