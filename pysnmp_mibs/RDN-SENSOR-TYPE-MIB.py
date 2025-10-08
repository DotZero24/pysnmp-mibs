#
# PySNMP MIB module RDN-SENSOR-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/riverdelta/RDN-SENSOR-TYPE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnSensorTypes = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 6))
rdnSensorTypes.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2001-08-07 00:00',))
if mibBuilder.loadTexts: rdnSensorTypes.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnSensorTypes.setOrganization('Motorola')
rdnSensorsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 0))
rdnSensorsSRM750 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 1))
rdnSensorsSRMDIMM = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 2))
rdnSensorsSRMDC2DC = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 3))
rdnSensorsSRMXFAB = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 4))
rdnSensorsFan = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 5))
mibBuilder.exportSymbols("RDN-SENSOR-TYPE-MIB", rdnSensorsSRMDC2DC=rdnSensorsSRMDC2DC, rdnSensorsFan=rdnSensorsFan, rdnSensorsSRMXFAB=rdnSensorsSRMXFAB, rdnSensorsUnknown=rdnSensorsUnknown, PYSNMP_MODULE_ID=rdnSensorTypes, rdnSensorsSRM750=rdnSensorsSRM750, rdnSensorsSRMDIMM=rdnSensorsSRMDIMM, rdnSensorTypes=rdnSensorTypes)
