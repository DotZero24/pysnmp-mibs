#
# PySNMP MIB module QTECH-CAPWAP-MULTICAST6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-CAPWAP-MULTICAST6-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
qtechCapwapMulticast6MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85))
qtechCapwapMulticast6MIB.setRevisions(('2010-05-20 00:00',))
if mibBuilder.loadTexts: qtechCapwapMulticast6MIB.setLastUpdated('201005200000Z')
if mibBuilder.loadTexts: qtechCapwapMulticast6MIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechCapwapMulticast6MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 1))
qtechCapwapMulticast6WorkingMode = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("unicast", 2), ("multicast", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechCapwapMulticast6WorkingMode.setStatus('current')
qtechCapwapMulticast6Group = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechCapwapMulticast6Group.setStatus('current')
qtechCapwapMulticast6MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2))
qtechCapwapMulticast6MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2, 1))
qtechCapwapMulticast6MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2, 2))
qtechCapwapMulticast6MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2, 1, 1)).setObjects(("QTECH-CAPWAP-MULTICAST6-MIB", "qtechCapwapMulticast6MIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechCapwapMulticast6MIBCompliance = qtechCapwapMulticast6MIBCompliance.setStatus('current')
qtechCapwapMulticast6MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 85, 2, 2, 1)).setObjects(("QTECH-CAPWAP-MULTICAST6-MIB", "qtechCapwapMulticast6WorkingMode"), ("QTECH-CAPWAP-MULTICAST6-MIB", "qtechCapwapMulticast6Group"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechCapwapMulticast6MIBGroup = qtechCapwapMulticast6MIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-CAPWAP-MULTICAST6-MIB", qtechCapwapMulticast6WorkingMode=qtechCapwapMulticast6WorkingMode, qtechCapwapMulticast6Group=qtechCapwapMulticast6Group, PYSNMP_MODULE_ID=qtechCapwapMulticast6MIB, qtechCapwapMulticast6MIBGroups=qtechCapwapMulticast6MIBGroups, qtechCapwapMulticast6MIBCompliances=qtechCapwapMulticast6MIBCompliances, qtechCapwapMulticast6MIB=qtechCapwapMulticast6MIB, qtechCapwapMulticast6MIBConformance=qtechCapwapMulticast6MIBConformance, qtechCapwapMulticast6MIBObjects=qtechCapwapMulticast6MIBObjects, qtechCapwapMulticast6MIBGroup=qtechCapwapMulticast6MIBGroup, qtechCapwapMulticast6MIBCompliance=qtechCapwapMulticast6MIBCompliance)
