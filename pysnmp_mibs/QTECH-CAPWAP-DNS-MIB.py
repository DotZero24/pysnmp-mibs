#
# PySNMP MIB module QTECH-CAPWAP-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-CAPWAP-DNS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
qtechIfIndex, = mibBuilder.importSymbols("QTECH-INTERFACE-MIB", "qtechIfIndex")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
qtechCapwapDnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88))
qtechCapwapDnsMIB.setRevisions(('2010-07-09 00:00',))
if mibBuilder.loadTexts: qtechCapwapDnsMIB.setLastUpdated('201007090000Z')
if mibBuilder.loadTexts: qtechCapwapDnsMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechCapwapDnsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 0))
qtechCapwapDnsGlobalConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 0, 1))
qtechLDnsFirstServer = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 0, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechLDnsFirstServer.setStatus('current')
qtechLDnsSecondServer = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 0, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechLDnsSecondServer.setStatus('current')
qtechCapwapDnsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2))
qtechCapwapDnsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2, 1))
qtechCapwapDnsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2, 2))
qtechCapwapDnsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2, 1, 1)).setObjects(("QTECH-CAPWAP-DNS-MIB", "qtechCapwapDnsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechCapwapDnsMIBCompliance = qtechCapwapDnsMIBCompliance.setStatus('current')
qtechCapwapDnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 88, 2, 2, 1)).setObjects(("QTECH-CAPWAP-DNS-MIB", "qtechLDnsFirstServer"), ("QTECH-CAPWAP-DNS-MIB", "qtechLDnsSecondServer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechCapwapDnsMIBGroup = qtechCapwapDnsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-CAPWAP-DNS-MIB", qtechCapwapDnsMIBGroups=qtechCapwapDnsMIBGroups, qtechCapwapDnsMIBCompliances=qtechCapwapDnsMIBCompliances, PYSNMP_MODULE_ID=qtechCapwapDnsMIB, qtechLDnsFirstServer=qtechLDnsFirstServer, qtechCapwapDnsMIBObjects=qtechCapwapDnsMIBObjects, qtechCapwapDnsMIBGroup=qtechCapwapDnsMIBGroup, qtechCapwapDnsMIBCompliance=qtechCapwapDnsMIBCompliance, qtechCapwapDnsGlobalConfig=qtechCapwapDnsGlobalConfig, qtechLDnsSecondServer=qtechLDnsSecondServer, qtechCapwapDnsMIBConformance=qtechCapwapDnsMIBConformance, qtechCapwapDnsMIB=qtechCapwapDnsMIB)
