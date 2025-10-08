#
# PySNMP MIB module QTECH-CAPWAP-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-CAPWAP-DNS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:24 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechIfIndex, = mibBuilder.importSymbols("QTECH-INTERFACE-MIB", "qtechIfIndex")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-CAPWAP-DNS-MIB", qtechCapwapDnsMIBCompliances=qtechCapwapDnsMIBCompliances, qtechCapwapDnsGlobalConfig=qtechCapwapDnsGlobalConfig, qtechLDnsFirstServer=qtechLDnsFirstServer, PYSNMP_MODULE_ID=qtechCapwapDnsMIB, qtechCapwapDnsMIBGroup=qtechCapwapDnsMIBGroup, qtechCapwapDnsMIBGroups=qtechCapwapDnsMIBGroups, qtechCapwapDnsMIBCompliance=qtechCapwapDnsMIBCompliance, qtechCapwapDnsMIBObjects=qtechCapwapDnsMIBObjects, qtechLDnsSecondServer=qtechLDnsSecondServer, qtechCapwapDnsMIB=qtechCapwapDnsMIB, qtechCapwapDnsMIBConformance=qtechCapwapDnsMIBConformance)
