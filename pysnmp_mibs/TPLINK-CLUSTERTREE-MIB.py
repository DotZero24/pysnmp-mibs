#
# PySNMP MIB module TPLINK-CLUSTERTREE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-CLUSTERTREE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkClusterTreeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 33))
tplinkClusterTreeMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkClusterTreeMIB.setOrganization('TPLINK')
tplinkClusterMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 1))
tplinkClusterNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 33, 2))
mibBuilder.exportSymbols("TPLINK-CLUSTERTREE-MIB", tplinkClusterMIBObjects=tplinkClusterMIBObjects, PYSNMP_MODULE_ID=tplinkClusterTreeMIB, tplinkClusterTreeMIB=tplinkClusterTreeMIB, tplinkClusterNotifications=tplinkClusterNotifications)
