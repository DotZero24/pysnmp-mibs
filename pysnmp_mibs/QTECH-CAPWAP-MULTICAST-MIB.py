#
# PySNMP MIB module QTECH-CAPWAP-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-CAPWAP-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechCapwapMulticastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59))
qtechCapwapMulticastMIB.setRevisions(('2009-10-22 00:00',))
if mibBuilder.loadTexts: qtechCapwapMulticastMIB.setLastUpdated('200910220000Z')
if mibBuilder.loadTexts: qtechCapwapMulticastMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechCapwapMulticastMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 1))
qtechCapwapMulticastWorkingMode = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unicast", 1), ("multicast", 2))).clone('unicast')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechCapwapMulticastWorkingMode.setStatus('current')
qtechCapwapMulticastGroup = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechCapwapMulticastGroup.setStatus('current')
qtechCapwapMulticastMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2))
qtechCapwapMulticastMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2, 1))
qtechCapwapMulticastMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2, 2))
qtechCapwapMulticastMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2, 1, 1)).setObjects(("QTECH-CAPWAP-MULTICAST-MIB", "qtechCapwapMulticastMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechCapwapMulticastMIBCompliance = qtechCapwapMulticastMIBCompliance.setStatus('current')
qtechCapwapMulticastMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 59, 2, 2, 1)).setObjects(("QTECH-CAPWAP-MULTICAST-MIB", "qtechCapwapMulticastWorkingMode"), ("QTECH-CAPWAP-MULTICAST-MIB", "qtechCapwapMulticastGroup"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechCapwapMulticastMIBGroup = qtechCapwapMulticastMIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-CAPWAP-MULTICAST-MIB", qtechCapwapMulticastGroup=qtechCapwapMulticastGroup, qtechCapwapMulticastMIBCompliances=qtechCapwapMulticastMIBCompliances, qtechCapwapMulticastMIB=qtechCapwapMulticastMIB, PYSNMP_MODULE_ID=qtechCapwapMulticastMIB, qtechCapwapMulticastMIBObjects=qtechCapwapMulticastMIBObjects, qtechCapwapMulticastMIBGroups=qtechCapwapMulticastMIBGroups, qtechCapwapMulticastMIBGroup=qtechCapwapMulticastMIBGroup, qtechCapwapMulticastMIBConformance=qtechCapwapMulticastMIBConformance, qtechCapwapMulticastMIBCompliance=qtechCapwapMulticastMIBCompliance, qtechCapwapMulticastWorkingMode=qtechCapwapMulticastWorkingMode)
