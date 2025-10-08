#
# PySNMP MIB module QTECH-CAPWAP-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-CAPWAP-MULTICAST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:59 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-CAPWAP-MULTICAST-MIB", qtechCapwapMulticastWorkingMode=qtechCapwapMulticastWorkingMode, qtechCapwapMulticastGroup=qtechCapwapMulticastGroup, qtechCapwapMulticastMIB=qtechCapwapMulticastMIB, PYSNMP_MODULE_ID=qtechCapwapMulticastMIB, qtechCapwapMulticastMIBGroup=qtechCapwapMulticastMIBGroup, qtechCapwapMulticastMIBObjects=qtechCapwapMulticastMIBObjects, qtechCapwapMulticastMIBConformance=qtechCapwapMulticastMIBConformance, qtechCapwapMulticastMIBGroups=qtechCapwapMulticastMIBGroups, qtechCapwapMulticastMIBCompliance=qtechCapwapMulticastMIBCompliance, qtechCapwapMulticastMIBCompliances=qtechCapwapMulticastMIBCompliances)
