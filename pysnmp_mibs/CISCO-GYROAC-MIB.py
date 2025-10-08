#
# PySNMP MIB module CISCO-GYROAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-GYROAC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGyroacMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 859))
ciscoGyroacMIB.setRevisions(('2019-01-09 00:00',))
if mibBuilder.loadTexts: ciscoGyroacMIB.setLastUpdated('201901090000Z')
if mibBuilder.loadTexts: ciscoGyroacMIB.setOrganization('Cisco Systems, Inc.')
ciscoGyroacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 859, 0))
ciscoGyro = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 859, 0, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoGyro.setStatus('current')
mibBuilder.exportSymbols("CISCO-GYROAC-MIB", ciscoGyro=ciscoGyro, ciscoGyroacMIBObjects=ciscoGyroacMIBObjects, ciscoGyroacMIB=ciscoGyroacMIB, PYSNMP_MODULE_ID=ciscoGyroacMIB)
