#
# PySNMP MIB module CISCO-QOS-POLICY-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-QOS-POLICY-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:11:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
QosInterfaceQueueType, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "QosInterfaceQueueType")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoQosPolicyConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 159))
ciscoQosPolicyConfigMIB.setRevisions(('2000-11-02 10:30', '2000-02-26 19:30',))
if mibBuilder.loadTexts: ciscoQosPolicyConfigMIB.setLastUpdated('200011021030Z')
if mibBuilder.loadTexts: ciscoQosPolicyConfigMIB.setOrganization('Cisco Systems Inc.')
class QosPolicySource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("local", 2), ("cops", 3))

ciscoQosPolicyConfigMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 1))
qosPolicyGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1))
qosPolicyInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2))
qosEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosEnabled.setStatus('current')
qosPrAdminPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 2), QosPolicySource().clone('local')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosPrAdminPolicySource.setStatus('current')
qosPrOperPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 3), QosPolicySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosPrOperPolicySource.setStatus('current')
qosRsvpAdminPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 4), QosPolicySource().clone('local')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosRsvpAdminPolicySource.setStatus('current')
qosRsvpOperPolicySource = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 5), QosPolicySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosRsvpOperPolicySource.setStatus('current')
qosCopsPolicyStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("keep", 1), ("discard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosCopsPolicyStatus.setStatus('current')
qosPrIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1), )
if mibBuilder.loadTexts: qosPrIfTable.setStatus('current')
qosPrIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qosPrIfEntry.setStatus('current')
qosPrIfAdminPolicySource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1, 1), QosPolicySource().clone('cops')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qosPrIfAdminPolicySource.setStatus('current')
qosPrIfOperPolicySource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 1, 1, 2), QosPolicySource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosPrIfOperPolicySource.setStatus('current')
qosIfCapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2), )
if mibBuilder.loadTexts: qosIfCapabilityTable.setStatus('current')
qosIfCapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-QOS-POLICY-CONFIG-MIB", "qosIfDirection"), (0, "CISCO-QOS-POLICY-CONFIG-MIB", "qosIfQType"))
if mibBuilder.loadTexts: qosIfCapabilityEntry.setStatus('current')
qosIfDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2), ("both", 3))))
if mibBuilder.loadTexts: qosIfDirection.setStatus('current')
qosIfQType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 2), QosInterfaceQueueType())
if mibBuilder.loadTexts: qosIfQType.setStatus('current')
qosIfCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 159, 1, 2, 2, 1, 3), Bits().clone(namedValues=NamedValues(("unspecified", 0), ("inputL2Classification", 1), ("inputIpClassification", 2), ("outputL2Classification", 3), ("outputIpClassification", 4), ("inputPortClassification", 19), ("outputPortClassification", 20), ("inputUflowPolicing", 5), ("inputAggregatePolicing", 6), ("outputUflowPolicing", 7), ("outputAggregatePolicing", 8), ("policeByMarkingDown", 9), ("policeByDropping", 10), ("inputUflowShaping", 21), ("inputAggregateShaping", 22), ("outputUflowShaping", 23), ("outputAggregateShaping", 24), ("fifo", 11), ("wrr", 12), ("wfq", 13), ("cq", 14), ("pq", 15), ("cbwfq", 16), ("pqWrr", 25), ("pqCbwfq", 26), ("tailDrop", 17), ("wred", 18)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qosIfCapabilities.setStatus('current')
ciscoQosPolicyMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 2))
ciscoQosPolicyConfigMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 3))
ciscoQosPolicyConfigMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 1))
ciscoQosPolicyConfigMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2))
ciscoQosPolicyConfigMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 1, 1)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosGlobalGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrGlobalGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpGlobalGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrInterfaceGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosInterfaceCapabilityGroup"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosCopsPolicyStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoQosPolicyConfigMIBCompliance = ciscoQosPolicyConfigMIBCompliance.setStatus('current')
qosGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 1)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosGlobalGroup = qosGlobalGroup.setStatus('current')
qosPrGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 2)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrAdminPolicySource"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrOperPolicySource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosPrGlobalGroup = qosPrGlobalGroup.setStatus('current')
qosRsvpGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 3)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpAdminPolicySource"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosRsvpOperPolicySource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosRsvpGlobalGroup = qosRsvpGlobalGroup.setStatus('current')
qosPrInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 4)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrIfAdminPolicySource"), ("CISCO-QOS-POLICY-CONFIG-MIB", "qosPrIfOperPolicySource"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosPrInterfaceGroup = qosPrInterfaceGroup.setStatus('current')
qosInterfaceCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 5)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosIfCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosInterfaceCapabilityGroup = qosInterfaceCapabilityGroup.setStatus('current')
qosCopsPolicyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 159, 3, 2, 6)).setObjects(("CISCO-QOS-POLICY-CONFIG-MIB", "qosCopsPolicyStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qosCopsPolicyStatusGroup = qosCopsPolicyStatusGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-QOS-POLICY-CONFIG-MIB", qosPrGlobalGroup=qosPrGlobalGroup, qosCopsPolicyStatusGroup=qosCopsPolicyStatusGroup, qosRsvpGlobalGroup=qosRsvpGlobalGroup, qosIfCapabilities=qosIfCapabilities, qosPrAdminPolicySource=qosPrAdminPolicySource, qosIfDirection=qosIfDirection, qosPolicyInterfaceObjects=qosPolicyInterfaceObjects, qosEnabled=qosEnabled, qosCopsPolicyStatus=qosCopsPolicyStatus, ciscoQosPolicyConfigMIBConformance=ciscoQosPolicyConfigMIBConformance, qosRsvpAdminPolicySource=qosRsvpAdminPolicySource, ciscoQosPolicyConfigMIBGroups=ciscoQosPolicyConfigMIBGroups, qosRsvpOperPolicySource=qosRsvpOperPolicySource, qosPrIfAdminPolicySource=qosPrIfAdminPolicySource, ciscoQosPolicyConfigMIBCompliances=ciscoQosPolicyConfigMIBCompliances, qosInterfaceCapabilityGroup=qosInterfaceCapabilityGroup, qosIfCapabilityTable=qosIfCapabilityTable, ciscoQosPolicyConfigMIBObjects=ciscoQosPolicyConfigMIBObjects, qosPrOperPolicySource=qosPrOperPolicySource, QosPolicySource=QosPolicySource, qosPolicyGlobalObjects=qosPolicyGlobalObjects, qosPrIfEntry=qosPrIfEntry, PYSNMP_MODULE_ID=ciscoQosPolicyConfigMIB, ciscoQosPolicyMIBNotifications=ciscoQosPolicyMIBNotifications, ciscoQosPolicyConfigMIB=ciscoQosPolicyConfigMIB, qosIfQType=qosIfQType, qosGlobalGroup=qosGlobalGroup, qosPrIfOperPolicySource=qosPrIfOperPolicySource, ciscoQosPolicyConfigMIBCompliance=ciscoQosPolicyConfigMIBCompliance, qosPrInterfaceGroup=qosPrInterfaceGroup, qosPrIfTable=qosPrIfTable, qosIfCapabilityEntry=qosIfCapabilityEntry)
