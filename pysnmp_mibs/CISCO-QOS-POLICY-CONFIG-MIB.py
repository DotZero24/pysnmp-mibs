_a='qosCopsPolicyStatusGroup'
_Z='qosInterfaceCapabilityGroup'
_Y='qosPrInterfaceGroup'
_X='qosRsvpGlobalGroup'
_W='qosPrGlobalGroup'
_V='qosGlobalGroup'
_U='qosCopsPolicyStatus'
_T='qosIfCapabilities'
_S='qosPrIfOperPolicySource'
_R='qosPrIfAdminPolicySource'
_Q='qosRsvpOperPolicySource'
_P='qosRsvpAdminPolicySource'
_O='qosPrOperPolicySource'
_N='qosPrAdminPolicySource'
_M='qosEnabled'
_L='not-accessible'
_K='qosIfQType'
_J='qosIfDirection'
_I='TruthValue'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='QosPolicySource'
_C='read-write'
_B='CISCO-QOS-POLICY-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
QosInterfaceQueueType,=mibBuilder.importSymbols('CISCO-QOS-PIB-MIB','QosInterfaceQueueType')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
ciscoQosPolicyConfigMIB=ModuleIdentity((1,3,6,1,4,1,9,9,159))
if mibBuilder.loadTexts:ciscoQosPolicyConfigMIB.setRevisions(('2000-11-02 10:30','2000-02-26 19:30'))
class QosPolicySource(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('local',2),('cops',3)))
_CiscoQosPolicyConfigMIBObjects_ObjectIdentity=ObjectIdentity
ciscoQosPolicyConfigMIBObjects=_CiscoQosPolicyConfigMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,159,1))
_QosPolicyGlobalObjects_ObjectIdentity=ObjectIdentity
qosPolicyGlobalObjects=_QosPolicyGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,159,1,1))
class _QosEnabled_Type(TruthValue):defaultValue=2
_QosEnabled_Type.__name__=_I
_QosEnabled_Object=MibScalar
qosEnabled=_QosEnabled_Object((1,3,6,1,4,1,9,9,159,1,1,1),_QosEnabled_Type())
qosEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:qosEnabled.setStatus(_A)
class _QosPrAdminPolicySource_Type(QosPolicySource):defaultValue=2
_QosPrAdminPolicySource_Type.__name__=_D
_QosPrAdminPolicySource_Object=MibScalar
qosPrAdminPolicySource=_QosPrAdminPolicySource_Object((1,3,6,1,4,1,9,9,159,1,1,2),_QosPrAdminPolicySource_Type())
qosPrAdminPolicySource.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPrAdminPolicySource.setStatus(_A)
_QosPrOperPolicySource_Type=QosPolicySource
_QosPrOperPolicySource_Object=MibScalar
qosPrOperPolicySource=_QosPrOperPolicySource_Object((1,3,6,1,4,1,9,9,159,1,1,3),_QosPrOperPolicySource_Type())
qosPrOperPolicySource.setMaxAccess(_E)
if mibBuilder.loadTexts:qosPrOperPolicySource.setStatus(_A)
class _QosRsvpAdminPolicySource_Type(QosPolicySource):defaultValue=2
_QosRsvpAdminPolicySource_Type.__name__=_D
_QosRsvpAdminPolicySource_Object=MibScalar
qosRsvpAdminPolicySource=_QosRsvpAdminPolicySource_Object((1,3,6,1,4,1,9,9,159,1,1,4),_QosRsvpAdminPolicySource_Type())
qosRsvpAdminPolicySource.setMaxAccess(_C)
if mibBuilder.loadTexts:qosRsvpAdminPolicySource.setStatus(_A)
_QosRsvpOperPolicySource_Type=QosPolicySource
_QosRsvpOperPolicySource_Object=MibScalar
qosRsvpOperPolicySource=_QosRsvpOperPolicySource_Object((1,3,6,1,4,1,9,9,159,1,1,5),_QosRsvpOperPolicySource_Type())
qosRsvpOperPolicySource.setMaxAccess(_E)
if mibBuilder.loadTexts:qosRsvpOperPolicySource.setStatus(_A)
class _QosCopsPolicyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('keep',1),('discard',2)))
_QosCopsPolicyStatus_Type.__name__=_H
_QosCopsPolicyStatus_Object=MibScalar
qosCopsPolicyStatus=_QosCopsPolicyStatus_Object((1,3,6,1,4,1,9,9,159,1,1,6),_QosCopsPolicyStatus_Type())
qosCopsPolicyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qosCopsPolicyStatus.setStatus(_A)
_QosPolicyInterfaceObjects_ObjectIdentity=ObjectIdentity
qosPolicyInterfaceObjects=_QosPolicyInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,9,9,159,1,2))
_QosPrIfTable_Object=MibTable
qosPrIfTable=_QosPrIfTable_Object((1,3,6,1,4,1,9,9,159,1,2,1))
if mibBuilder.loadTexts:qosPrIfTable.setStatus(_A)
_QosPrIfEntry_Object=MibTableRow
qosPrIfEntry=_QosPrIfEntry_Object((1,3,6,1,4,1,9,9,159,1,2,1,1))
qosPrIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:qosPrIfEntry.setStatus(_A)
class _QosPrIfAdminPolicySource_Type(QosPolicySource):defaultValue=3
_QosPrIfAdminPolicySource_Type.__name__=_D
_QosPrIfAdminPolicySource_Object=MibTableColumn
qosPrIfAdminPolicySource=_QosPrIfAdminPolicySource_Object((1,3,6,1,4,1,9,9,159,1,2,1,1,1),_QosPrIfAdminPolicySource_Type())
qosPrIfAdminPolicySource.setMaxAccess(_C)
if mibBuilder.loadTexts:qosPrIfAdminPolicySource.setStatus(_A)
_QosPrIfOperPolicySource_Type=QosPolicySource
_QosPrIfOperPolicySource_Object=MibTableColumn
qosPrIfOperPolicySource=_QosPrIfOperPolicySource_Object((1,3,6,1,4,1,9,9,159,1,2,1,1,2),_QosPrIfOperPolicySource_Type())
qosPrIfOperPolicySource.setMaxAccess(_E)
if mibBuilder.loadTexts:qosPrIfOperPolicySource.setStatus(_A)
_QosIfCapabilityTable_Object=MibTable
qosIfCapabilityTable=_QosIfCapabilityTable_Object((1,3,6,1,4,1,9,9,159,1,2,2))
if mibBuilder.loadTexts:qosIfCapabilityTable.setStatus(_A)
_QosIfCapabilityEntry_Object=MibTableRow
qosIfCapabilityEntry=_QosIfCapabilityEntry_Object((1,3,6,1,4,1,9,9,159,1,2,2,1))
qosIfCapabilityEntry.setIndexNames((0,_F,_G),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:qosIfCapabilityEntry.setStatus(_A)
class _QosIfDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ingress',1),('egress',2),('both',3)))
_QosIfDirection_Type.__name__=_H
_QosIfDirection_Object=MibTableColumn
qosIfDirection=_QosIfDirection_Object((1,3,6,1,4,1,9,9,159,1,2,2,1,1),_QosIfDirection_Type())
qosIfDirection.setMaxAccess(_L)
if mibBuilder.loadTexts:qosIfDirection.setStatus(_A)
_QosIfQType_Type=QosInterfaceQueueType
_QosIfQType_Object=MibTableColumn
qosIfQType=_QosIfQType_Object((1,3,6,1,4,1,9,9,159,1,2,2,1,2),_QosIfQType_Type())
qosIfQType.setMaxAccess(_L)
if mibBuilder.loadTexts:qosIfQType.setStatus(_A)
class _QosIfCapabilities_Type(Bits):namedValues=NamedValues(*(('unspecified',0),('inputL2Classification',1),('inputIpClassification',2),('outputL2Classification',3),('outputIpClassification',4),('inputUflowPolicing',5),('inputAggregatePolicing',6),('outputUflowPolicing',7),('outputAggregatePolicing',8),('policeByMarkingDown',9),('policeByDropping',10),('fifo',11),('wrr',12),('wfq',13),('cq',14),('pq',15),('cbwfq',16),('tailDrop',17),('wred',18),('inputPortClassification',19),('outputPortClassification',20),('inputUflowShaping',21),('inputAggregateShaping',22),('outputUflowShaping',23),('outputAggregateShaping',24),('pqWrr',25),('pqCbwfq',26)))
_QosIfCapabilities_Type.__name__='Bits'
_QosIfCapabilities_Object=MibTableColumn
qosIfCapabilities=_QosIfCapabilities_Object((1,3,6,1,4,1,9,9,159,1,2,2,1,3),_QosIfCapabilities_Type())
qosIfCapabilities.setMaxAccess(_E)
if mibBuilder.loadTexts:qosIfCapabilities.setStatus(_A)
_CiscoQosPolicyMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoQosPolicyMIBNotifications=_CiscoQosPolicyMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,159,2))
_CiscoQosPolicyConfigMIBConformance_ObjectIdentity=ObjectIdentity
ciscoQosPolicyConfigMIBConformance=_CiscoQosPolicyConfigMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,159,3))
_CiscoQosPolicyConfigMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoQosPolicyConfigMIBCompliances=_CiscoQosPolicyConfigMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,159,3,1))
_CiscoQosPolicyConfigMIBGroups_ObjectIdentity=ObjectIdentity
ciscoQosPolicyConfigMIBGroups=_CiscoQosPolicyConfigMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,159,3,2))
qosGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,159,3,2,1))
qosGlobalGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:qosGlobalGroup.setStatus(_A)
qosPrGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,159,3,2,2))
qosPrGlobalGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:qosPrGlobalGroup.setStatus(_A)
qosRsvpGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,159,3,2,3))
qosRsvpGlobalGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:qosRsvpGlobalGroup.setStatus(_A)
qosPrInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,9,159,3,2,4))
qosPrInterfaceGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:qosPrInterfaceGroup.setStatus(_A)
qosInterfaceCapabilityGroup=ObjectGroup((1,3,6,1,4,1,9,9,159,3,2,5))
qosInterfaceCapabilityGroup.setObjects((_B,_T))
if mibBuilder.loadTexts:qosInterfaceCapabilityGroup.setStatus(_A)
qosCopsPolicyStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,159,3,2,6))
qosCopsPolicyStatusGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:qosCopsPolicyStatusGroup.setStatus(_A)
ciscoQosPolicyConfigMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,159,3,1,1))
ciscoQosPolicyConfigMIBCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoQosPolicyConfigMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_D:QosPolicySource,'ciscoQosPolicyConfigMIB':ciscoQosPolicyConfigMIB,'ciscoQosPolicyConfigMIBObjects':ciscoQosPolicyConfigMIBObjects,'qosPolicyGlobalObjects':qosPolicyGlobalObjects,_M:qosEnabled,_N:qosPrAdminPolicySource,_O:qosPrOperPolicySource,_P:qosRsvpAdminPolicySource,_Q:qosRsvpOperPolicySource,_U:qosCopsPolicyStatus,'qosPolicyInterfaceObjects':qosPolicyInterfaceObjects,'qosPrIfTable':qosPrIfTable,'qosPrIfEntry':qosPrIfEntry,_R:qosPrIfAdminPolicySource,_S:qosPrIfOperPolicySource,'qosIfCapabilityTable':qosIfCapabilityTable,'qosIfCapabilityEntry':qosIfCapabilityEntry,_J:qosIfDirection,_K:qosIfQType,_T:qosIfCapabilities,'ciscoQosPolicyMIBNotifications':ciscoQosPolicyMIBNotifications,'ciscoQosPolicyConfigMIBConformance':ciscoQosPolicyConfigMIBConformance,'ciscoQosPolicyConfigMIBCompliances':ciscoQosPolicyConfigMIBCompliances,'ciscoQosPolicyConfigMIBCompliance':ciscoQosPolicyConfigMIBCompliance,'ciscoQosPolicyConfigMIBGroups':ciscoQosPolicyConfigMIBGroups,_V:qosGlobalGroup,_W:qosPrGlobalGroup,_X:qosRsvpGlobalGroup,_Y:qosPrInterfaceGroup,_Z:qosInterfaceCapabilityGroup,_a:qosCopsPolicyStatusGroup})