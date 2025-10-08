#
# PySNMP MIB module TPLINK-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-CLUSTER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:52 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkClusterMIBObjects, = mibBuilder.importSymbols("TPLINK-CLUSTERTREE-MIB", "tplinkClusterMIBObjects")
tplinkClusterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1))
tplinkClusterMIB.setRevisions(('2009-08-27 00:00',))
if mibBuilder.loadTexts: tplinkClusterMIB.setLastUpdated('200908270000Z')
if mibBuilder.loadTexts: tplinkClusterMIB.setOrganization('TPLINK')
ndpManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 1))
ntdpManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 2))
clusterManage = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3))
mibBuilder.exportSymbols("TPLINK-CLUSTER-MIB", ntdpManage=ntdpManage, tplinkClusterMIB=tplinkClusterMIB, PYSNMP_MODULE_ID=tplinkClusterMIB, ndpManage=ndpManage, clusterManage=clusterManage)
