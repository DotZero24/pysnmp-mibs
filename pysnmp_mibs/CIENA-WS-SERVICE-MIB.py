#
# PySNMP MIB module CIENA-WS-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-WS-SERVICE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:01 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaWsConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsConfig")
EnabledDisabledEnum, ServiceDomainIdx, DescriptionString, PortId, ServiceIdx = mibBuilder.importSymbols("CIENA-WS-TYPEDEFS-MIB", "EnabledDisabledEnum", "ServiceDomainIdx", "DescriptionString", "PortId", "ServiceIdx")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaWsServiceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1))
cienaWsServiceMIB.setRevisions(('2017-07-18 00:00', '2017-03-02 00:00', '2016-12-12 00:00', '2016-06-17 00:00', '2015-02-25 00:00',))
if mibBuilder.loadTexts: cienaWsServiceMIB.setLastUpdated('201707180000Z')
if mibBuilder.loadTexts: cienaWsServiceMIB.setOrganization('Ciena Corporation')
class ServiceId(TextualConvention, Unsigned32):
    status = 'current'

class ServiceMaxPort(TextualConvention, Unsigned32):
    status = 'current'

class ServiceNameStr(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

cwsServiceServicesTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 3), )
if mibBuilder.loadTexts: cwsServiceServicesTable.setStatus('current')
cwsServiceServicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 3, 1), ).setIndexNames((0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"))
if mibBuilder.loadTexts: cwsServiceServicesEntry.setStatus('current')
cwsServiceServicesServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsServiceServicesServiceIndex.setStatus('current')
cwsServiceIdTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4), )
if mibBuilder.loadTexts: cwsServiceIdTable.setStatus('current')
cwsServiceIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1), ).setIndexNames((0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"), (0, "CIENA-WS-SERVICE-MIB", "cwsServiceIdTableSnmpKey"))
if mibBuilder.loadTexts: cwsServiceIdEntry.setStatus('current')
cwsServiceIdTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsServiceIdTableSnmpKey.setStatus('current')
cwsServiceIdServiceId = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1, 2), ServiceId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsServiceIdServiceId.setStatus('current')
cwsServiceIdName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1, 3), ServiceNameStr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsServiceIdName.setStatus('current')
cwsServiceIdDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 4, 1, 4), DescriptionString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsServiceIdDescription.setStatus('current')
cwsServiceStateTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 5), )
if mibBuilder.loadTexts: cwsServiceStateTable.setStatus('current')
cwsServiceStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 5, 1), ).setIndexNames((0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"), (0, "CIENA-WS-SERVICE-MIB", "cwsServiceStateTableSnmpKey"))
if mibBuilder.loadTexts: cwsServiceStateEntry.setStatus('current')
cwsServiceStateTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsServiceStateTableSnmpKey.setStatus('current')
cwsServiceStateAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 5, 1, 2), EnabledDisabledEnum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsServiceStateAdminState.setStatus('current')
cwsServicePropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6), )
if mibBuilder.loadTexts: cwsServicePropertiesTable.setStatus('current')
cwsServicePropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1), ).setIndexNames((0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"), (0, "CIENA-WS-SERVICE-MIB", "cwsServicePropertiesTableSnmpKey"))
if mibBuilder.loadTexts: cwsServicePropertiesEntry.setStatus('current')
cwsServicePropertiesTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsServicePropertiesTableSnmpKey.setStatus('current')
cwsServicePropertiesType = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("epl", 0), ("evpl", 1), ("etree", 2), ("elan", 3), ("eepl", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsServicePropertiesType.setStatus('current')
cwsServicePropertiesMaxNumberOfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 3), ServiceMaxPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsServicePropertiesMaxNumberOfPort.setStatus('current')
cwsServicePropertiesProtectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("protected", 0), ("unprotected", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsServicePropertiesProtectionState.setStatus('current')
cwsServicePropertiesLinkStateForwarding = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 5), EnabledDisabledEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsServicePropertiesLinkStateForwarding.setStatus('current')
cwsServicePropertiesMacLearning = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 6), EnabledDisabledEnum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsServicePropertiesMacLearning.setStatus('current')
cwsServicePropertiesParentSvcDomainIdxReference = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 6, 1, 7), ServiceDomainIdx()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwsServicePropertiesParentSvcDomainIdxReference.setStatus('current')
cwsServicePortMembersReferenceTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 7), )
if mibBuilder.loadTexts: cwsServicePortMembersReferenceTable.setStatus('current')
cwsServicePortMembersReferenceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 7, 1), ).setIndexNames((0, "CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"), (0, "CIENA-WS-SERVICE-MIB", "cwsServicePropertiesTableSnmpKey"), (0, "CIENA-WS-SERVICE-MIB", "cwsServicePortMembersReferenceTableSnmpKey"))
if mibBuilder.loadTexts: cwsServicePortMembersReferenceEntry.setStatus('current')
cwsServicePortMembersReferenceTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: cwsServicePortMembersReferenceTableSnmpKey.setStatus('current')
cwsServicePortMembersReference = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 7, 1, 2), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwsServicePortMembersReference.setStatus('current')
cienaWsServiceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 1))
cienaWsServiceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2))
cienaWsServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2, 1))
cienaWsServiceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2, 1, 1)).setObjects(("CIENA-WS-SERVICE-MIB", "cwsServiceServicesServiceIndex"), ("CIENA-WS-SERVICE-MIB", "cwsServiceIdServiceId"), ("CIENA-WS-SERVICE-MIB", "cwsServiceIdName"), ("CIENA-WS-SERVICE-MIB", "cwsServiceIdDescription"), ("CIENA-WS-SERVICE-MIB", "cwsServiceStateAdminState"), ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesType"), ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesMaxNumberOfPort"), ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesProtectionState"), ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesLinkStateForwarding"), ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesMacLearning"), ("CIENA-WS-SERVICE-MIB", "cwsServicePropertiesParentSvcDomainIdxReference"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsServiceGroup = cienaWsServiceGroup.setStatus('current')
cienaWsServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2, 2))
cienaWsServiceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1271, 3, 4, 1, 2, 2, 1)).setObjects(("CIENA-WS-SERVICE-MIB", "cienaWsServiceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsServiceCompliance = cienaWsServiceCompliance.setStatus('current')
mibBuilder.exportSymbols("CIENA-WS-SERVICE-MIB", ServiceId=ServiceId, cwsServiceStateAdminState=cwsServiceStateAdminState, cienaWsServiceGroup=cienaWsServiceGroup, cwsServicePropertiesTableSnmpKey=cwsServicePropertiesTableSnmpKey, cwsServicePortMembersReferenceTableSnmpKey=cwsServicePortMembersReferenceTableSnmpKey, cwsServiceIdServiceId=cwsServiceIdServiceId, cwsServiceServicesTable=cwsServiceServicesTable, cienaWsServiceCompliance=cienaWsServiceCompliance, cwsServiceStateEntry=cwsServiceStateEntry, cwsServicePropertiesProtectionState=cwsServicePropertiesProtectionState, cwsServicePropertiesType=cwsServicePropertiesType, cwsServiceStateTableSnmpKey=cwsServiceStateTableSnmpKey, ServiceNameStr=ServiceNameStr, cwsServiceIdTableSnmpKey=cwsServiceIdTableSnmpKey, cienaWsServiceCompliances=cienaWsServiceCompliances, cwsServicePropertiesParentSvcDomainIdxReference=cwsServicePropertiesParentSvcDomainIdxReference, cwsServiceIdEntry=cwsServiceIdEntry, cwsServiceStateTable=cwsServiceStateTable, cwsServiceIdDescription=cwsServiceIdDescription, PYSNMP_MODULE_ID=cienaWsServiceMIB, ServiceMaxPort=ServiceMaxPort, cwsServicePortMembersReference=cwsServicePortMembersReference, cwsServiceServicesEntry=cwsServiceServicesEntry, cienaWsServiceMIB=cienaWsServiceMIB, cwsServiceIdTable=cwsServiceIdTable, cwsServicePropertiesTable=cwsServicePropertiesTable, cwsServicePropertiesMaxNumberOfPort=cwsServicePropertiesMaxNumberOfPort, cwsServicePropertiesLinkStateForwarding=cwsServicePropertiesLinkStateForwarding, cwsServicePortMembersReferenceTable=cwsServicePortMembersReferenceTable, cienaWsServiceGroups=cienaWsServiceGroups, cwsServicePortMembersReferenceEntry=cwsServicePortMembersReferenceEntry, cwsServicePropertiesEntry=cwsServicePropertiesEntry, cienaWsServiceConformance=cienaWsServiceConformance, cwsServiceServicesServiceIndex=cwsServiceServicesServiceIndex, cienaWsServiceObjects=cienaWsServiceObjects, cwsServiceIdName=cwsServiceIdName, cwsServicePropertiesMacLearning=cwsServicePropertiesMacLearning)
