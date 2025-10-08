#
# PySNMP MIB module CISCOME1200-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCOME1200-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:28 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoME1200MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815))
ciscoME1200MIB.setRevisions(('2014-01-28 00:00',))
if mibBuilder.loadTexts: ciscoME1200MIB.setLastUpdated('201401280000Z')
if mibBuilder.loadTexts: ciscoME1200MIB.setOrganization('Cisco Systems, Inc')
me1200SwitchMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 815, 1))
if mibBuilder.loadTexts: me1200SwitchMgmt.setStatus('current')
mibBuilder.exportSymbols("CISCOME1200-MIB", PYSNMP_MODULE_ID=ciscoME1200MIB, ciscoME1200MIB=ciscoME1200MIB, me1200SwitchMgmt=me1200SwitchMgmt)
