#
# PySNMP MIB module QTECH-ANTI-ARPCHEAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-ANTI-ARPCHEAT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:15 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
IfIndex, = mibBuilder.importSymbols("QTECH-TC", "IfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-ANTI-ARPCHEAT-MIB", trustedArpOperationType=trustedArpOperationType, qtechTrustedArpEntry=qtechTrustedArpEntry, trustedArpIfIndex=trustedArpIfIndex, qtechAntiArpcheatMIBGroups=qtechAntiArpcheatMIBGroups, qtechAntiArpcheatMIB=qtechAntiArpcheatMIB, qtechAntiArpcheatMIBCompliance=qtechAntiArpcheatMIBCompliance, PYSNMP_MODULE_ID=qtechAntiArpcheatMIB, trustedArpIp=trustedArpIp, qtechAntiArpcheatMIBCompliances=qtechAntiArpcheatMIBCompliances, qtechAntiArpcheatMIBGroup=qtechAntiArpcheatMIBGroup, qtechAntiArpcheatMIBObjects=qtechAntiArpcheatMIBObjects, qtechTrustedArpTable=qtechTrustedArpTable, trustedArpVlan=trustedArpVlan, trustedArpMediaPhysAddress=trustedArpMediaPhysAddress, qtechTrustedArpDelete=qtechTrustedArpDelete, qtechAntiArpcheatMIBConformance=qtechAntiArpcheatMIBConformance)
