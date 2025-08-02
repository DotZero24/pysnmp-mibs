_c='capSidSessionInfoGroup'
_b='capSidSessionPolicyGroup'
_a='capSessionStatisticsGroup'
_Z='capSidSecurityGroupTag'
_Y='capSidUrlRedirectAclState'
_X='capSidUrlRedirectAclName'
_W='capSidRedirectUrlStringState'
_V='capSidRedirectUrlString'
_U='capSidDownloadableAclState'
_T='capSidDownloadableAclName'
_S='capSidEgressQosPolicyState'
_R='capSidEgressQosPolicy'
_Q='capSidIngressQosPolicyState'
_P='capSidIngressQosPolicy'
_O='capSidSessionFeatureType'
_N='capSidSessionMacAddress'
_M='capSidSessionIfIndex'
_L='capSidSessionAddress'
_K='capSidSessionAddressType'
_J='capActiveSessions'
_I='capTotalSessions'
_H='capSidSessionPolicyIndex'
_G='authProxy'
_F='not-accessible'
_E='capSidSessionIndex'
_D='Integer32'
_C='read-only'
_B='CISCO-ADMISSION-POLICY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ciscoAdmissionPolicyMIB=ModuleIdentity((1,3,6,1,4,1,9,9,653))
if mibBuilder.loadTexts:ciscoAdmissionPolicyMIB.setRevisions(('2008-06-11 00:00',))
class CapSessionId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
class CapQosPolicy(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class CapAclName(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class CapURLString(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class CapPolicyState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notApplicable',1),('success',2),('failure',3),('inProgress',4),('ipWait',5)))
_CiscoAdmissionPolicyMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoAdmissionPolicyMIBNotifs=_CiscoAdmissionPolicyMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,653,0))
_CiscoAdmissionPolicyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAdmissionPolicyMIBObjects=_CiscoAdmissionPolicyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,653,1))
_CapSessions_ObjectIdentity=ObjectIdentity
capSessions=_CapSessions_ObjectIdentity((1,3,6,1,4,1,9,9,653,1,1))
_CapTotalSessions_Type=Counter32
_CapTotalSessions_Object=MibScalar
capTotalSessions=_CapTotalSessions_Object((1,3,6,1,4,1,9,9,653,1,1,1),_CapTotalSessions_Type())
capTotalSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:capTotalSessions.setStatus(_A)
_CapActiveSessions_Type=Gauge32
_CapActiveSessions_Object=MibScalar
capActiveSessions=_CapActiveSessions_Object((1,3,6,1,4,1,9,9,653,1,1,2),_CapActiveSessions_Type())
capActiveSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:capActiveSessions.setStatus(_A)
_CapSidSessionInfoTable_Object=MibTable
capSidSessionInfoTable=_CapSidSessionInfoTable_Object((1,3,6,1,4,1,9,9,653,1,1,3))
if mibBuilder.loadTexts:capSidSessionInfoTable.setStatus(_A)
_CapSidSessionInfoEntry_Object=MibTableRow
capSidSessionInfoEntry=_CapSidSessionInfoEntry_Object((1,3,6,1,4,1,9,9,653,1,1,3,1))
capSidSessionInfoEntry.setIndexNames((1,_B,_E))
if mibBuilder.loadTexts:capSidSessionInfoEntry.setStatus(_A)
_CapSidSessionIndex_Type=CapSessionId
_CapSidSessionIndex_Object=MibTableColumn
capSidSessionIndex=_CapSidSessionIndex_Object((1,3,6,1,4,1,9,9,653,1,1,3,1,1),_CapSidSessionIndex_Type())
capSidSessionIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:capSidSessionIndex.setStatus(_A)
_CapSidSessionIfIndex_Type=InterfaceIndex
_CapSidSessionIfIndex_Object=MibTableColumn
capSidSessionIfIndex=_CapSidSessionIfIndex_Object((1,3,6,1,4,1,9,9,653,1,1,3,1,2),_CapSidSessionIfIndex_Type())
capSidSessionIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidSessionIfIndex.setStatus(_A)
_CapSidSessionMacAddress_Type=MacAddress
_CapSidSessionMacAddress_Object=MibTableColumn
capSidSessionMacAddress=_CapSidSessionMacAddress_Object((1,3,6,1,4,1,9,9,653,1,1,3,1,3),_CapSidSessionMacAddress_Type())
capSidSessionMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidSessionMacAddress.setStatus(_A)
_CapSidSessionAddressType_Type=InetAddressType
_CapSidSessionAddressType_Object=MibTableColumn
capSidSessionAddressType=_CapSidSessionAddressType_Object((1,3,6,1,4,1,9,9,653,1,1,3,1,4),_CapSidSessionAddressType_Type())
capSidSessionAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidSessionAddressType.setStatus(_A)
_CapSidSessionAddress_Type=InetAddress
_CapSidSessionAddress_Object=MibTableColumn
capSidSessionAddress=_CapSidSessionAddress_Object((1,3,6,1,4,1,9,9,653,1,1,3,1,5),_CapSidSessionAddress_Type())
capSidSessionAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidSessionAddress.setStatus(_A)
class _CapSidSessionFeatureType_Type(Bits):namedValues=NamedValues(*(('dot1x',0),('mab',1),('eou',2),(_G,3)))
_CapSidSessionFeatureType_Type.__name__='Bits'
_CapSidSessionFeatureType_Object=MibTableColumn
capSidSessionFeatureType=_CapSidSessionFeatureType_Object((1,3,6,1,4,1,9,9,653,1,1,3,1,6),_CapSidSessionFeatureType_Type())
capSidSessionFeatureType.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidSessionFeatureType.setStatus(_A)
_CapSidSessionPolicyTable_Object=MibTable
capSidSessionPolicyTable=_CapSidSessionPolicyTable_Object((1,3,6,1,4,1,9,9,653,1,1,4))
if mibBuilder.loadTexts:capSidSessionPolicyTable.setStatus(_A)
_CapSidSessionPolicyEntry_Object=MibTableRow
capSidSessionPolicyEntry=_CapSidSessionPolicyEntry_Object((1,3,6,1,4,1,9,9,653,1,1,4,1))
capSidSessionPolicyEntry.setIndexNames((0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:capSidSessionPolicyEntry.setStatus(_A)
class _CapSidSessionPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dot1x',1),('mab',2),('eou',3),(_G,4)))
_CapSidSessionPolicyIndex_Type.__name__=_D
_CapSidSessionPolicyIndex_Object=MibTableColumn
capSidSessionPolicyIndex=_CapSidSessionPolicyIndex_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,1),_CapSidSessionPolicyIndex_Type())
capSidSessionPolicyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:capSidSessionPolicyIndex.setStatus(_A)
_CapSidIngressQosPolicy_Type=CapQosPolicy
_CapSidIngressQosPolicy_Object=MibTableColumn
capSidIngressQosPolicy=_CapSidIngressQosPolicy_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,2),_CapSidIngressQosPolicy_Type())
capSidIngressQosPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidIngressQosPolicy.setStatus(_A)
_CapSidIngressQosPolicyState_Type=CapPolicyState
_CapSidIngressQosPolicyState_Object=MibTableColumn
capSidIngressQosPolicyState=_CapSidIngressQosPolicyState_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,3),_CapSidIngressQosPolicyState_Type())
capSidIngressQosPolicyState.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidIngressQosPolicyState.setStatus(_A)
_CapSidEgressQosPolicy_Type=CapQosPolicy
_CapSidEgressQosPolicy_Object=MibTableColumn
capSidEgressQosPolicy=_CapSidEgressQosPolicy_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,4),_CapSidEgressQosPolicy_Type())
capSidEgressQosPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidEgressQosPolicy.setStatus(_A)
_CapSidEgressQosPolicyState_Type=CapPolicyState
_CapSidEgressQosPolicyState_Object=MibTableColumn
capSidEgressQosPolicyState=_CapSidEgressQosPolicyState_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,5),_CapSidEgressQosPolicyState_Type())
capSidEgressQosPolicyState.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidEgressQosPolicyState.setStatus(_A)
_CapSidDownloadableAclName_Type=CapAclName
_CapSidDownloadableAclName_Object=MibTableColumn
capSidDownloadableAclName=_CapSidDownloadableAclName_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,6),_CapSidDownloadableAclName_Type())
capSidDownloadableAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidDownloadableAclName.setStatus(_A)
_CapSidDownloadableAclState_Type=CapPolicyState
_CapSidDownloadableAclState_Object=MibTableColumn
capSidDownloadableAclState=_CapSidDownloadableAclState_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,7),_CapSidDownloadableAclState_Type())
capSidDownloadableAclState.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidDownloadableAclState.setStatus(_A)
_CapSidUrlRedirectAclName_Type=CapAclName
_CapSidUrlRedirectAclName_Object=MibTableColumn
capSidUrlRedirectAclName=_CapSidUrlRedirectAclName_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,8),_CapSidUrlRedirectAclName_Type())
capSidUrlRedirectAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidUrlRedirectAclName.setStatus(_A)
_CapSidUrlRedirectAclState_Type=CapPolicyState
_CapSidUrlRedirectAclState_Object=MibTableColumn
capSidUrlRedirectAclState=_CapSidUrlRedirectAclState_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,9),_CapSidUrlRedirectAclState_Type())
capSidUrlRedirectAclState.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidUrlRedirectAclState.setStatus(_A)
_CapSidRedirectUrlString_Type=CapURLString
_CapSidRedirectUrlString_Object=MibTableColumn
capSidRedirectUrlString=_CapSidRedirectUrlString_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,10),_CapSidRedirectUrlString_Type())
capSidRedirectUrlString.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidRedirectUrlString.setStatus(_A)
_CapSidRedirectUrlStringState_Type=CapPolicyState
_CapSidRedirectUrlStringState_Object=MibTableColumn
capSidRedirectUrlStringState=_CapSidRedirectUrlStringState_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,11),_CapSidRedirectUrlStringState_Type())
capSidRedirectUrlStringState.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidRedirectUrlStringState.setStatus(_A)
class _CapSidSecurityGroupTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
_CapSidSecurityGroupTag_Type.__name__=_D
_CapSidSecurityGroupTag_Object=MibTableColumn
capSidSecurityGroupTag=_CapSidSecurityGroupTag_Object((1,3,6,1,4,1,9,9,653,1,1,4,1,12),_CapSidSecurityGroupTag_Type())
capSidSecurityGroupTag.setMaxAccess(_C)
if mibBuilder.loadTexts:capSidSecurityGroupTag.setStatus(_A)
_CiscoAdmissionPolicyMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAdmissionPolicyMIBConformance=_CiscoAdmissionPolicyMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,653,2))
_CiscoAdmissionPolicyMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAdmissionPolicyMIBCompliances=_CiscoAdmissionPolicyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,653,2,1))
_CiscoAdmissionPolicyMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAdmissionPolicyMIBGroups=_CiscoAdmissionPolicyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,653,2,2))
capSessionStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,653,2,2,1))
capSessionStatisticsGroup.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:capSessionStatisticsGroup.setStatus(_A)
capSidSessionInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,653,2,2,2))
capSidSessionInfoGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:capSidSessionInfoGroup.setStatus(_A)
capSidSessionPolicyGroup=ObjectGroup((1,3,6,1,4,1,9,9,653,2,2,3))
capSidSessionPolicyGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:capSidSessionPolicyGroup.setStatus(_A)
ciscoAdmissionPolicyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,653,2,1,1))
ciscoAdmissionPolicyMIBCompliance.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:ciscoAdmissionPolicyMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CapSessionId':CapSessionId,'CapQosPolicy':CapQosPolicy,'CapAclName':CapAclName,'CapURLString':CapURLString,'CapPolicyState':CapPolicyState,'ciscoAdmissionPolicyMIB':ciscoAdmissionPolicyMIB,'ciscoAdmissionPolicyMIBNotifs':ciscoAdmissionPolicyMIBNotifs,'ciscoAdmissionPolicyMIBObjects':ciscoAdmissionPolicyMIBObjects,'capSessions':capSessions,_I:capTotalSessions,_J:capActiveSessions,'capSidSessionInfoTable':capSidSessionInfoTable,'capSidSessionInfoEntry':capSidSessionInfoEntry,_E:capSidSessionIndex,_M:capSidSessionIfIndex,_N:capSidSessionMacAddress,_K:capSidSessionAddressType,_L:capSidSessionAddress,_O:capSidSessionFeatureType,'capSidSessionPolicyTable':capSidSessionPolicyTable,'capSidSessionPolicyEntry':capSidSessionPolicyEntry,_H:capSidSessionPolicyIndex,_P:capSidIngressQosPolicy,_Q:capSidIngressQosPolicyState,_R:capSidEgressQosPolicy,_S:capSidEgressQosPolicyState,_T:capSidDownloadableAclName,_U:capSidDownloadableAclState,_X:capSidUrlRedirectAclName,_Y:capSidUrlRedirectAclState,_V:capSidRedirectUrlString,_W:capSidRedirectUrlStringState,_Z:capSidSecurityGroupTag,'ciscoAdmissionPolicyMIBConformance':ciscoAdmissionPolicyMIBConformance,'ciscoAdmissionPolicyMIBCompliances':ciscoAdmissionPolicyMIBCompliances,'ciscoAdmissionPolicyMIBCompliance':ciscoAdmissionPolicyMIBCompliance,'ciscoAdmissionPolicyMIBGroups':ciscoAdmissionPolicyMIBGroups,_a:capSessionStatisticsGroup,_c:capSidSessionInfoGroup,_b:capSidSessionPolicyGroup})