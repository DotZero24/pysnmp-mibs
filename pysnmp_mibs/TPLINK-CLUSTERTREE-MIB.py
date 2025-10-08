#
# PySNMP MIB module TPLINK-CLUSTERTREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-CLUSTERTREE-MIB
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
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkClusterTreeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 33))
tplinkClusterTreeMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setOrganization('TPLINK')
tplinkClusterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1))
tplinkClusterNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 2))
mibBuilder.exportSymbols("TPLINK-CLUSTERTREE-MIB", tplinkClusterTreeMIB=tplinkClusterTreeMIB, tplinkClusterNotifications=tplinkClusterNotifications, tplinkClusterMIBObjects=tplinkClusterMIBObjects, PYSNMP_MODULE_ID=tplinkClusterTreeMIB)
