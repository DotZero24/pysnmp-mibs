#
# PySNMP MIB module TPLINK-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-LLDP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:54 2025
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
tplinkLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 35))
tplinkLldpMIB.setRevisions(('2012-12-13 17:30',))
if mibBuilder.loadTexts: tplinkLldpMIB.setLastUpdated('201212131730Z')
if mibBuilder.loadTexts: tplinkLldpMIB.setOrganization('TPLINK')
tplinkLldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1))
tplinkLldpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 2))
mibBuilder.exportSymbols("TPLINK-LLDP-MIB", PYSNMP_MODULE_ID=tplinkLldpMIB, tplinkLldpMIBNotifications=tplinkLldpMIBNotifications, tplinkLldpMIBObjects=tplinkLldpMIBObjects, tplinkLldpMIB=tplinkLldpMIB)
