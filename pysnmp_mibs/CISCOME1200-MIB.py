#
# PySNMP MIB module CISCOME1200-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCOME1200-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:32:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoME1200MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815))
ciscoME1200MIB.setRevisions(('2014-01-28 00:00',))
if mibBuilder.loadTexts: ciscoME1200MIB.setLastUpdated('201401280000Z')
if mibBuilder.loadTexts: ciscoME1200MIB.setOrganization('Cisco Systems, Inc')
me1200SwitchMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1))
if mibBuilder.loadTexts: me1200SwitchMgmt.setStatus('current')
mibBuilder.exportSymbols("CISCOME1200-MIB", ciscoME1200MIB=ciscoME1200MIB, PYSNMP_MODULE_ID=ciscoME1200MIB, me1200SwitchMgmt=me1200SwitchMgmt)
