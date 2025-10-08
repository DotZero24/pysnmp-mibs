#
# PySNMP MIB module RDN-SENSOR-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/riverdelta/RDN-SENSOR-TYPE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RDN-SENSOR-TYPE-MIB", rdnSensorsSRMXFAB=rdnSensorsSRMXFAB, rdnSensorsSRMDIMM=rdnSensorsSRMDIMM, rdnSensorsUnknown=rdnSensorsUnknown, rdnSensorsSRM750=rdnSensorsSRM750, PYSNMP_MODULE_ID=rdnSensorTypes, rdnSensorsSRMDC2DC=rdnSensorsSRMDC2DC, rdnSensorsFan=rdnSensorsFan, rdnSensorTypes=rdnSensorTypes)
