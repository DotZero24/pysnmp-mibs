#
# PySNMP MIB module TPLINK-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-LLDP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 35))
tplinkLldpMIB.setRevisions(('2012-12-13 17:30',))
if mibBuilder.loadTexts: tplinkLldpMIB.setLastUpdated('201212131730Z')
if mibBuilder.loadTexts: tplinkLldpMIB.setOrganization('TPLINK')
tplinkLldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1))
tplinkLldpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 2))
mibBuilder.exportSymbols("TPLINK-LLDP-MIB", tplinkLldpMIBNotifications=tplinkLldpMIBNotifications, tplinkLldpMIB=tplinkLldpMIB, PYSNMP_MODULE_ID=tplinkLldpMIB, tplinkLldpMIBObjects=tplinkLldpMIBObjects)
