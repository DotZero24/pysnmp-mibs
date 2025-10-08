#
# PySNMP MIB module QTECH-ANTI-ARPCHEAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-ANTI-ARPCHEAT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
IfIndex, = mibBuilder.importSymbols("QTECH-TC", "IfIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
qtechAntiArpcheatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41))
qtechAntiArpcheatMIB.setRevisions(('2007-01-29 00:00',))
if mibBuilder.loadTexts: qtechAntiArpcheatMIB.setLastUpdated('200701290000Z')
if mibBuilder.loadTexts: qtechAntiArpcheatMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechAntiArpcheatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1))
qtechTrustedArpDelete = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qtechTrustedArpDelete.setStatus('current')
qtechTrustedArpTable = MibTable((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2), )
if mibBuilder.loadTexts: qtechTrustedArpTable.setStatus('current')
qtechTrustedArpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1), ).setIndexNames((0, "QTECH-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"), (0, "QTECH-ANTI-ARPCHEAT-MIB", "trustedArpIp"))
if mibBuilder.loadTexts: qtechTrustedArpEntry.setStatus('current')
trustedArpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 1), IfIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpIfIndex.setStatus('current')
trustedArpIp = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpIp.setStatus('current')
trustedArpMediaPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpMediaPhysAddress.setStatus('current')
trustedArpVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 4), VlanId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpVlan.setStatus('current')
trustedArpOperationType = MibTableColumn((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 1, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trustedArpOperationType.setStatus('current')
qtechAntiArpcheatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2))
qtechAntiArpcheatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2, 1))
qtechAntiArpcheatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2, 2))
qtechAntiArpcheatMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2, 1, 1)).setObjects(("QTECH-ANTI-ARPCHEAT-MIB", "qtechAntiArpcheatMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechAntiArpcheatMIBCompliance = qtechAntiArpcheatMIBCompliance.setStatus('current')
qtechAntiArpcheatMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 41, 2, 2, 1)).setObjects(("QTECH-ANTI-ARPCHEAT-MIB", "qtechTrustedArpDelete"), ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpIfIndex"), ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpIp"), ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpMediaPhysAddress"), ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpVlan"), ("QTECH-ANTI-ARPCHEAT-MIB", "trustedArpOperationType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qtechAntiArpcheatMIBGroup = qtechAntiArpcheatMIBGroup.setStatus('current')
mibBuilder.exportSymbols("QTECH-ANTI-ARPCHEAT-MIB", qtechAntiArpcheatMIBGroups=qtechAntiArpcheatMIBGroups, trustedArpIp=trustedArpIp, trustedArpIfIndex=trustedArpIfIndex, qtechTrustedArpDelete=qtechTrustedArpDelete, trustedArpOperationType=trustedArpOperationType, qtechAntiArpcheatMIBConformance=qtechAntiArpcheatMIBConformance, qtechAntiArpcheatMIB=qtechAntiArpcheatMIB, trustedArpVlan=trustedArpVlan, qtechAntiArpcheatMIBCompliances=qtechAntiArpcheatMIBCompliances, PYSNMP_MODULE_ID=qtechAntiArpcheatMIB, qtechTrustedArpEntry=qtechTrustedArpEntry, qtechAntiArpcheatMIBCompliance=qtechAntiArpcheatMIBCompliance, qtechAntiArpcheatMIBObjects=qtechAntiArpcheatMIBObjects, trustedArpMediaPhysAddress=trustedArpMediaPhysAddress, qtechAntiArpcheatMIBGroup=qtechAntiArpcheatMIBGroup, qtechTrustedArpTable=qtechTrustedArpTable)
