_n='osAclMandatoryGroup'
_m='osAclGenConfExtendedProfile'
_l='osAclMibSupport'
_k='osAclMatchingCounterOperStatus'
_j='osAclMatchingCounterAdminStatus'
_i='osAclMatchingCounterBytes'
_h='osAclMatchingCounterPackets'
_g='osAclBindingAdminStatus'
_f='osAclBindingAclName'
_e='osAclRuleClassAdminStatus'
_d='osAclRuleClassParamValue'
_c='osAclRuleClassParamType'
_b='osAclRuleActionAdminStatus'
_a='osAclRuleActionParamValue'
_Z='osAclRuleActionParamType'
_Y='osAclRuleAdminStatus'
_X='osAclAdminStatus'
_W='osAclActive'
_V='osAclRemark'
_U='osAclDefaultPolicy'
_T='osAclType'
_S='osAclMatchingCounterIndex'
_R='osAclBindingTag'
_Q='osAclBindingPort'
_P='osAclRuleClassCondition'
_O='osAclRuleClassType'
_N='osAclRuleActionType'
_M='active'
_L='invalid'
_K='notSupported'
_J='DisplayString'
_I='OctetString'
_H='osAclRuleIndex'
_G='read-only'
_F='osAclName'
_E='not-accessible'
_D='Integer32'
_C='read-write'
_B='OS-ACL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oaOptiSwitch,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
osAcl=ModuleIdentity((1,3,6,1,4,1,6926,2,3))
if mibBuilder.loadTexts:osAcl.setRevisions(('2014-05-27 00:00','2008-01-08 00:00'))
class SupportValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),('supported',2)))
class AdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('valid',2),(_L,3)))
class ParamType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*(('integer',2),('octetString',3),('displayString',4),('noParam',5)))
class ConditionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('eq',2),('neq',3),('lt',4),('gt',5),('le',6),('ge',7),('mask',8),('none',9)))
class VlanIdOrNone(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095),ValueRangeConstraint(5000,5000))
class PortIndexOrNone(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4999),ValueRangeConstraint(5000,5000))
_OsAclTable_Object=MibTable
osAclTable=_OsAclTable_Object((1,3,6,1,4,1,6926,2,3,1))
if mibBuilder.loadTexts:osAclTable.setStatus(_A)
_OsAclEntry_Object=MibTableRow
osAclEntry=_OsAclEntry_Object((1,3,6,1,4,1,6926,2,3,1,1))
osAclEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:osAclEntry.setStatus(_A)
class _OsAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_OsAclName_Type.__name__=_J
_OsAclName_Object=MibTableColumn
osAclName=_OsAclName_Object((1,3,6,1,4,1,6926,2,3,1,1,1),_OsAclName_Type())
osAclName.setMaxAccess(_E)
if mibBuilder.loadTexts:osAclName.setStatus(_A)
class _OsAclType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('extended',2),('flow',3),('protocols',4)))
_OsAclType_Type.__name__=_D
_OsAclType_Object=MibTableColumn
osAclType=_OsAclType_Object((1,3,6,1,4,1,6926,2,3,1,1,2),_OsAclType_Type())
osAclType.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclType.setStatus(_A)
class _OsAclDefaultPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('deny',2),('permit',3),(_K,4)))
_OsAclDefaultPolicy_Type.__name__=_D
_OsAclDefaultPolicy_Object=MibTableColumn
osAclDefaultPolicy=_OsAclDefaultPolicy_Object((1,3,6,1,4,1,6926,2,3,1,1,3),_OsAclDefaultPolicy_Type())
osAclDefaultPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclDefaultPolicy.setStatus(_A)
_OsAclRemark_Type=DisplayString
_OsAclRemark_Object=MibTableColumn
osAclRemark=_OsAclRemark_Object((1,3,6,1,4,1,6926,2,3,1,1,4),_OsAclRemark_Type())
osAclRemark.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclRemark.setStatus(_A)
class _OsAclActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),('notActive',2)))
_OsAclActive_Type.__name__=_D
_OsAclActive_Object=MibTableColumn
osAclActive=_OsAclActive_Object((1,3,6,1,4,1,6926,2,3,1,1,5),_OsAclActive_Type())
osAclActive.setMaxAccess(_G)
if mibBuilder.loadTexts:osAclActive.setStatus(_A)
_OsAclAdminStatus_Type=AdminStatus
_OsAclAdminStatus_Object=MibTableColumn
osAclAdminStatus=_OsAclAdminStatus_Object((1,3,6,1,4,1,6926,2,3,1,1,6),_OsAclAdminStatus_Type())
osAclAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclAdminStatus.setStatus(_A)
_OsAclRuleTable_Object=MibTable
osAclRuleTable=_OsAclRuleTable_Object((1,3,6,1,4,1,6926,2,3,2))
if mibBuilder.loadTexts:osAclRuleTable.setStatus(_A)
_OsAclRuleEntry_Object=MibTableRow
osAclRuleEntry=_OsAclRuleEntry_Object((1,3,6,1,4,1,6926,2,3,2,1))
osAclRuleEntry.setIndexNames((0,_B,_F),(0,_B,_H))
if mibBuilder.loadTexts:osAclRuleEntry.setStatus(_A)
class _OsAclRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsAclRuleIndex_Type.__name__=_D
_OsAclRuleIndex_Object=MibTableColumn
osAclRuleIndex=_OsAclRuleIndex_Object((1,3,6,1,4,1,6926,2,3,2,1,1),_OsAclRuleIndex_Type())
osAclRuleIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:osAclRuleIndex.setStatus(_A)
class _OsAclRuleAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('enable',2),('disable',3),(_L,4)))
_OsAclRuleAdminStatus_Type.__name__=_D
_OsAclRuleAdminStatus_Object=MibTableColumn
osAclRuleAdminStatus=_OsAclRuleAdminStatus_Object((1,3,6,1,4,1,6926,2,3,2,1,2),_OsAclRuleAdminStatus_Type())
osAclRuleAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclRuleAdminStatus.setStatus(_A)
_OsAclRuleActionTable_Object=MibTable
osAclRuleActionTable=_OsAclRuleActionTable_Object((1,3,6,1,4,1,6926,2,3,3))
if mibBuilder.loadTexts:osAclRuleActionTable.setStatus(_A)
_OsAclRuleActionEntry_Object=MibTableRow
osAclRuleActionEntry=_OsAclRuleActionEntry_Object((1,3,6,1,4,1,6926,2,3,3,1))
osAclRuleActionEntry.setIndexNames((0,_B,_F),(0,_B,_H),(0,_B,_N))
if mibBuilder.loadTexts:osAclRuleActionEntry.setStatus(_A)
class _OsAclRuleActionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('osAclRuleActionDeny',2),('osAclRuleActionPermit',3),('osAclRuleActionLayer2Loopback',4),('osAclRuleActionTrapToCpu',5),('osAclRuleActionMirrorToCpu',6),('osAclRuleActionMirrorToAnalyser',7),('osAclRuleActionRedirectPort',8),('osAclRuleActionRedirectTag',9),('osAclRuleActionWithActionList',10),('osAclRuleActionMarkServiceLevel',11),('osAclRuleActionMarkDscp',12),('osAclRuleActionMarkVpt',13),('osAclRuleActionMarkByDiffserv',14),('osAclRuleActionMarkSlByDscp',15),('osAclRuleActionSwapVlan',16),('osAclRuleActionNestedVlan',17),('osAclRuleActionSwapToClientTag',18),('osAclRuleActionSwapToServerTag',19),('osAclRuleActionRedirectToCpu',20)))
_OsAclRuleActionType_Type.__name__=_D
_OsAclRuleActionType_Object=MibTableColumn
osAclRuleActionType=_OsAclRuleActionType_Object((1,3,6,1,4,1,6926,2,3,3,1,1),_OsAclRuleActionType_Type())
osAclRuleActionType.setMaxAccess(_E)
if mibBuilder.loadTexts:osAclRuleActionType.setStatus(_A)
_OsAclRuleActionParamType_Type=ParamType
_OsAclRuleActionParamType_Object=MibTableColumn
osAclRuleActionParamType=_OsAclRuleActionParamType_Object((1,3,6,1,4,1,6926,2,3,3,1,2),_OsAclRuleActionParamType_Type())
osAclRuleActionParamType.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclRuleActionParamType.setStatus(_A)
class _OsAclRuleActionParamValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OsAclRuleActionParamValue_Type.__name__=_I
_OsAclRuleActionParamValue_Object=MibTableColumn
osAclRuleActionParamValue=_OsAclRuleActionParamValue_Object((1,3,6,1,4,1,6926,2,3,3,1,3),_OsAclRuleActionParamValue_Type())
osAclRuleActionParamValue.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclRuleActionParamValue.setStatus(_A)
_OsAclRuleActionAdminStatus_Type=AdminStatus
_OsAclRuleActionAdminStatus_Object=MibTableColumn
osAclRuleActionAdminStatus=_OsAclRuleActionAdminStatus_Object((1,3,6,1,4,1,6926,2,3,3,1,4),_OsAclRuleActionAdminStatus_Type())
osAclRuleActionAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclRuleActionAdminStatus.setStatus(_A)
_OsAclRuleClassTable_Object=MibTable
osAclRuleClassTable=_OsAclRuleClassTable_Object((1,3,6,1,4,1,6926,2,3,4))
if mibBuilder.loadTexts:osAclRuleClassTable.setStatus(_A)
_OsAclRuleClassEntry_Object=MibTableRow
osAclRuleClassEntry=_OsAclRuleClassEntry_Object((1,3,6,1,4,1,6926,2,3,4,1))
osAclRuleClassEntry.setIndexNames((0,_B,_F),(0,_B,_H),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:osAclRuleClassEntry.setStatus(_A)
class _OsAclRuleClassType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('osAclRuleClassSrcIp',2),('osAclRuleClassDestIp',3),('osAclRuleClassSrcPort',4),('osAclRuleClassDestPort',5),('osAclRuleClassProtocol',6),('osAclRuleClassMacLookupResults',7),('osAclRuleClassMacDaType',8),('osAclRuleClassVpt',9),('osAclRuleClassClientVpt',10),('osAclRuleClassDscp',11),('osAclRuleClassMplsExp',12),('osAclRuleClassMplsExpTagged',13),('osAclRuleClassTag',14),('osAclRuleClassClientTag',15),('osAclRuleClassEthertype',16),('osAclRuleClassClientEthertype',17),('osAclRuleClassSrcMac',18),('osAclRuleClassDestMac',19),('osAclRuleClassSrcPhyPort',20),('osAclRuleClassArp',21),('osAclRuleClassTaggedArp',22)))
_OsAclRuleClassType_Type.__name__=_D
_OsAclRuleClassType_Object=MibTableColumn
osAclRuleClassType=_OsAclRuleClassType_Object((1,3,6,1,4,1,6926,2,3,4,1,1),_OsAclRuleClassType_Type())
osAclRuleClassType.setMaxAccess(_E)
if mibBuilder.loadTexts:osAclRuleClassType.setStatus(_A)
_OsAclRuleClassCondition_Type=ConditionType
_OsAclRuleClassCondition_Object=MibTableColumn
osAclRuleClassCondition=_OsAclRuleClassCondition_Object((1,3,6,1,4,1,6926,2,3,4,1,2),_OsAclRuleClassCondition_Type())
osAclRuleClassCondition.setMaxAccess(_E)
if mibBuilder.loadTexts:osAclRuleClassCondition.setStatus(_A)
_OsAclRuleClassParamType_Type=ParamType
_OsAclRuleClassParamType_Object=MibTableColumn
osAclRuleClassParamType=_OsAclRuleClassParamType_Object((1,3,6,1,4,1,6926,2,3,4,1,3),_OsAclRuleClassParamType_Type())
osAclRuleClassParamType.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclRuleClassParamType.setStatus(_A)
class _OsAclRuleClassParamValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OsAclRuleClassParamValue_Type.__name__=_I
_OsAclRuleClassParamValue_Object=MibTableColumn
osAclRuleClassParamValue=_OsAclRuleClassParamValue_Object((1,3,6,1,4,1,6926,2,3,4,1,4),_OsAclRuleClassParamValue_Type())
osAclRuleClassParamValue.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclRuleClassParamValue.setStatus(_A)
_OsAclRuleClassAdminStatus_Type=AdminStatus
_OsAclRuleClassAdminStatus_Object=MibTableColumn
osAclRuleClassAdminStatus=_OsAclRuleClassAdminStatus_Object((1,3,6,1,4,1,6926,2,3,4,1,5),_OsAclRuleClassAdminStatus_Type())
osAclRuleClassAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclRuleClassAdminStatus.setStatus(_A)
_OsAclBindingTable_Object=MibTable
osAclBindingTable=_OsAclBindingTable_Object((1,3,6,1,4,1,6926,2,3,5))
if mibBuilder.loadTexts:osAclBindingTable.setStatus(_A)
_OsAclBindingEntry_Object=MibTableRow
osAclBindingEntry=_OsAclBindingEntry_Object((1,3,6,1,4,1,6926,2,3,5,1))
osAclBindingEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:osAclBindingEntry.setStatus(_A)
_OsAclBindingPort_Type=PortIndexOrNone
_OsAclBindingPort_Object=MibTableColumn
osAclBindingPort=_OsAclBindingPort_Object((1,3,6,1,4,1,6926,2,3,5,1,1),_OsAclBindingPort_Type())
osAclBindingPort.setMaxAccess(_E)
if mibBuilder.loadTexts:osAclBindingPort.setStatus(_A)
_OsAclBindingTag_Type=VlanIdOrNone
_OsAclBindingTag_Object=MibTableColumn
osAclBindingTag=_OsAclBindingTag_Object((1,3,6,1,4,1,6926,2,3,5,1,2),_OsAclBindingTag_Type())
osAclBindingTag.setMaxAccess(_E)
if mibBuilder.loadTexts:osAclBindingTag.setStatus(_A)
class _OsAclBindingAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,19))
_OsAclBindingAclName_Type.__name__=_J
_OsAclBindingAclName_Object=MibTableColumn
osAclBindingAclName=_OsAclBindingAclName_Object((1,3,6,1,4,1,6926,2,3,5,1,3),_OsAclBindingAclName_Type())
osAclBindingAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclBindingAclName.setStatus(_A)
_OsAclBindingAdminStatus_Type=AdminStatus
_OsAclBindingAdminStatus_Object=MibTableColumn
osAclBindingAdminStatus=_OsAclBindingAdminStatus_Object((1,3,6,1,4,1,6926,2,3,5,1,4),_OsAclBindingAdminStatus_Type())
osAclBindingAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclBindingAdminStatus.setStatus(_A)
_OsAclMatchingCounterTable_Object=MibTable
osAclMatchingCounterTable=_OsAclMatchingCounterTable_Object((1,3,6,1,4,1,6926,2,3,6))
if mibBuilder.loadTexts:osAclMatchingCounterTable.setStatus(_A)
_OsAclMatchingCounterEntry_Object=MibTableRow
osAclMatchingCounterEntry=_OsAclMatchingCounterEntry_Object((1,3,6,1,4,1,6926,2,3,6,1))
osAclMatchingCounterEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:osAclMatchingCounterEntry.setStatus(_A)
class _OsAclMatchingCounterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2048))
_OsAclMatchingCounterIndex_Type.__name__=_D
_OsAclMatchingCounterIndex_Object=MibTableColumn
osAclMatchingCounterIndex=_OsAclMatchingCounterIndex_Object((1,3,6,1,4,1,6926,2,3,6,1,1),_OsAclMatchingCounterIndex_Type())
osAclMatchingCounterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:osAclMatchingCounterIndex.setStatus(_A)
_OsAclMatchingCounterPackets_Type=Counter64
_OsAclMatchingCounterPackets_Object=MibTableColumn
osAclMatchingCounterPackets=_OsAclMatchingCounterPackets_Object((1,3,6,1,4,1,6926,2,3,6,1,2),_OsAclMatchingCounterPackets_Type())
osAclMatchingCounterPackets.setMaxAccess(_G)
if mibBuilder.loadTexts:osAclMatchingCounterPackets.setStatus(_A)
_OsAclMatchingCounterBytes_Type=Counter64
_OsAclMatchingCounterBytes_Object=MibTableColumn
osAclMatchingCounterBytes=_OsAclMatchingCounterBytes_Object((1,3,6,1,4,1,6926,2,3,6,1,3),_OsAclMatchingCounterBytes_Type())
osAclMatchingCounterBytes.setMaxAccess(_G)
if mibBuilder.loadTexts:osAclMatchingCounterBytes.setStatus(_A)
class _OsAclMatchingCounterAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nothing',1),('clear',2)))
_OsAclMatchingCounterAdminStatus_Type.__name__=_D
_OsAclMatchingCounterAdminStatus_Object=MibTableColumn
osAclMatchingCounterAdminStatus=_OsAclMatchingCounterAdminStatus_Object((1,3,6,1,4,1,6926,2,3,6,1,98),_OsAclMatchingCounterAdminStatus_Type())
osAclMatchingCounterAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclMatchingCounterAdminStatus.setStatus(_A)
class _OsAclMatchingCounterOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),(_M,2)))
_OsAclMatchingCounterOperStatus_Type.__name__=_D
_OsAclMatchingCounterOperStatus_Object=MibTableColumn
osAclMatchingCounterOperStatus=_OsAclMatchingCounterOperStatus_Object((1,3,6,1,4,1,6926,2,3,6,1,99),_OsAclMatchingCounterOperStatus_Type())
osAclMatchingCounterOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:osAclMatchingCounterOperStatus.setStatus(_A)
_OsAclGenConfGrp_ObjectIdentity=ObjectIdentity
osAclGenConfGrp=_OsAclGenConfGrp_ObjectIdentity((1,3,6,1,4,1,6926,2,3,50))
class _OsAclGenConfExtendedProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),('normal',1),('doubleTag',2),('mplsExp',3)))
_OsAclGenConfExtendedProfile_Type.__name__=_D
_OsAclGenConfExtendedProfile_Object=MibScalar
osAclGenConfExtendedProfile=_OsAclGenConfExtendedProfile_Object((1,3,6,1,4,1,6926,2,3,50,5),_OsAclGenConfExtendedProfile_Type())
osAclGenConfExtendedProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:osAclGenConfExtendedProfile.setStatus(_A)
_OsAclSupportGrp_ObjectIdentity=ObjectIdentity
osAclSupportGrp=_OsAclSupportGrp_ObjectIdentity((1,3,6,1,4,1,6926,2,3,100))
_OsAclMibSupport_Type=SupportValue
_OsAclMibSupport_Object=MibScalar
osAclMibSupport=_OsAclMibSupport_Object((1,3,6,1,4,1,6926,2,3,100,1),_OsAclMibSupport_Type())
osAclMibSupport.setMaxAccess(_G)
if mibBuilder.loadTexts:osAclMibSupport.setStatus(_A)
_OsAclConformance_ObjectIdentity=ObjectIdentity
osAclConformance=_OsAclConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,3,101))
_OsAclMIBCompliances_ObjectIdentity=ObjectIdentity
osAclMIBCompliances=_OsAclMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,3,101,1))
_OsAclMIBGroups_ObjectIdentity=ObjectIdentity
osAclMIBGroups=_OsAclMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,3,101,2))
osAclMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,3,101,2,1))
osAclMandatoryGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:osAclMandatoryGroup.setStatus(_A)
osAclMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,3,101,1,1))
osAclMIBCompliance.setObjects((_B,_n))
if mibBuilder.loadTexts:osAclMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SupportValue':SupportValue,'AdminStatus':AdminStatus,'ParamType':ParamType,'ConditionType':ConditionType,'VlanIdOrNone':VlanIdOrNone,'PortIndexOrNone':PortIndexOrNone,'osAcl':osAcl,'osAclTable':osAclTable,'osAclEntry':osAclEntry,_F:osAclName,_T:osAclType,_U:osAclDefaultPolicy,_V:osAclRemark,_W:osAclActive,_X:osAclAdminStatus,'osAclRuleTable':osAclRuleTable,'osAclRuleEntry':osAclRuleEntry,_H:osAclRuleIndex,_Y:osAclRuleAdminStatus,'osAclRuleActionTable':osAclRuleActionTable,'osAclRuleActionEntry':osAclRuleActionEntry,_N:osAclRuleActionType,_Z:osAclRuleActionParamType,_a:osAclRuleActionParamValue,_b:osAclRuleActionAdminStatus,'osAclRuleClassTable':osAclRuleClassTable,'osAclRuleClassEntry':osAclRuleClassEntry,_O:osAclRuleClassType,_P:osAclRuleClassCondition,_c:osAclRuleClassParamType,_d:osAclRuleClassParamValue,_e:osAclRuleClassAdminStatus,'osAclBindingTable':osAclBindingTable,'osAclBindingEntry':osAclBindingEntry,_Q:osAclBindingPort,_R:osAclBindingTag,_f:osAclBindingAclName,_g:osAclBindingAdminStatus,'osAclMatchingCounterTable':osAclMatchingCounterTable,'osAclMatchingCounterEntry':osAclMatchingCounterEntry,_S:osAclMatchingCounterIndex,_h:osAclMatchingCounterPackets,_i:osAclMatchingCounterBytes,_j:osAclMatchingCounterAdminStatus,_k:osAclMatchingCounterOperStatus,'osAclGenConfGrp':osAclGenConfGrp,_m:osAclGenConfExtendedProfile,'osAclSupportGrp':osAclSupportGrp,_l:osAclMibSupport,'osAclConformance':osAclConformance,'osAclMIBCompliances':osAclMIBCompliances,'osAclMIBCompliance':osAclMIBCompliance,'osAclMIBGroups':osAclMIBGroups,_n:osAclMandatoryGroup})