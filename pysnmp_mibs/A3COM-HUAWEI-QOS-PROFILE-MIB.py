_AW='h3cQoSProfPortMappingTrapsGroup'
_AV='h3cQoSProfPortMappingGroup'
_AU='h3cQoSActionGroup'
_AT='h3cQoSProfGroup'
_AS='h3cQoSProfPortMappingError'
_AR='h3cQoSProfDynPortMappingUserProfName'
_AQ='h3cQoSProfDynPortMappingUserVLANID'
_AP='h3cQoSProfDynPortMappingUserIPAddr'
_AO='h3cQoSProfDynPortMappingUserName'
_AN='h3cQoSProfPortMappingMode'
_AM='h3cQoSProfPortMappingRowStatus'
_AL='h3cQoSTrafFilterRowStatus'
_AK='h3cQoSTrafFilterLinkAclRule'
_AJ='h3cQoSTrafFilterLinkAclNum'
_AI='h3cQoSTrafFilterIpAclRule'
_AH='h3cQoSTrafFilterIpAclNum'
_AG='h3cQoSTrafFilterUserAclRule'
_AF='h3cQoSTrafFilterUserAclNum'
_AE='h3cQoSTrafFilterDirection'
_AD='h3cQoSTrafPrioRowStatus'
_AC='h3cQoSTrafPrioPolicedServiceDropPriority'
_AB='h3cQoSTrafPrioPolicedServiceLoaclPre'
_AA='h3cQoSTrafPrioPolicedServiceCos'
_A9='h3cQoSTrafPrioPolicedServiceExp'
_A8='h3cQoSTrafPrioPolicedServiceDscp'
_A7='h3cQoSTrafPrioPolicedServiceType'
_A6='h3cQoSTrafPrioLocalPre'
_A5='h3cQoSTrafPrioCosFromIpPre'
_A4='h3cQoSTrafPrioCos'
_A3='h3cQoSTrafPrioIpPreFromCos'
_A2='h3cQoSTrafPrioIpPre'
_A1='h3cQoSTrafPrioDscp'
_A0='h3cQoSTrafPrioLinkAclRule'
_z='h3cQoSTrafPrioLinkAclNum'
_y='h3cQoSTrafPrioIpAclRule'
_x='h3cQoSTrafPrioIpAclNum'
_w='h3cQoSTrafPrioUserAclRule'
_v='h3cQoSTrafPrioUserAclNum'
_u='h3cQoSTrafPrioDirection'
_t='h3cQoSTrafLmtConformDscp'
_s='h3cQoSTrafLmtConformCos'
_r='h3cQoSTrafLmtRowStatus'
_q='h3cQoSTrafLmtExceedCos'
_p='h3cQoSTrafLmtExceedDscp'
_o='h3cQoSTrafLmtExceedActionType'
_n='h3cQoSTrafLmtConformActionType'
_m='h3cQoSTrafLmtConformLocalPre'
_l='h3cQoSTrafLmtPIR'
_k='h3cQoSTrafLmtEBS'
_j='h3cQoSTrafLmtCBS'
_i='h3cQoSTrafLmtCIR'
_h='h3cQoSTrafLmtPeakRate'
_g='h3cQoSTrafLmtTargetRateKbps'
_f='h3cQoSTrafLmtTargetRateMbps'
_e='h3cQoSTrafLmtLinkAclRule'
_d='h3cQoSTrafLmtLinkAclNum'
_c='h3cQoSTrafLmtIpAclRule'
_b='h3cQoSTrafLmtIpAclNum'
_a='h3cQoSTrafLmtUserAclRule'
_Z='h3cQoSTrafLmtUserAclNum'
_Y='h3cQoSTrafLmtDirection'
_X='h3cQoSProfRowStatus'
_W='h3cQoSProfActionNumber'
_V='h3cQoSProfName'
_U='h3cQoSProfDynPortMappingUserSrcMAC'
_T='h3cQoSProfDynPortMappingIfIndex'
_S='h3cQoSProfPortMappingModeIfIndex'
_R='h3cQoSProfPortMappingProfIndex'
_Q='h3cQoSProfPortMappingIfIndex'
_P='h3cQoSTrafFilterActionIndex'
_O='h3cQoSTrafFilterProfIndex'
_N='h3cQoSTrafPrioActionIndex'
_M='h3cQoSTrafPrioProfIndex'
_L='h3cQoSTrafLmtActionIndex'
_K='h3cQoSTrafLmtProfIndex'
_J='h3cQoSProfIndex'
_I='TruthValue'
_H='invalid'
_G='OctetString'
_F='read-only'
_E='not-accessible'
_D='read-create'
_C='Integer32'
_B='A3COM-HUAWEI-QOS-PROFILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
h3cQosProfile=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,17))
class H3cQoSDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('input',1),('ouput',2)))
_H3cQoSProfObjects_ObjectIdentity=ObjectIdentity
h3cQoSProfObjects=_H3cQoSProfObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,17,1))
_H3cQoSProf_ObjectIdentity=ObjectIdentity
h3cQoSProf=_H3cQoSProf_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,17,1,1))
_H3cQoSProfTable_Object=MibTable
h3cQoSProfTable=_H3cQoSProfTable_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,1,1))
if mibBuilder.loadTexts:h3cQoSProfTable.setStatus(_A)
_H3cQoSProfEntry_Object=MibTableRow
h3cQoSProfEntry=_H3cQoSProfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,1,1,1))
h3cQoSProfEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:h3cQoSProfEntry.setStatus(_A)
class _H3cQoSProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQoSProfIndex_Type.__name__=_C
_H3cQoSProfIndex_Object=MibTableColumn
h3cQoSProfIndex=_H3cQoSProfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,1,1,1,1),_H3cQoSProfIndex_Type())
h3cQoSProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSProfIndex.setStatus(_A)
class _H3cQoSProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cQoSProfName_Type.__name__=_G
_H3cQoSProfName_Object=MibTableColumn
h3cQoSProfName=_H3cQoSProfName_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,1,1,1,2),_H3cQoSProfName_Type())
h3cQoSProfName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSProfName.setStatus(_A)
class _H3cQoSProfActionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSProfActionNumber_Type.__name__=_C
_H3cQoSProfActionNumber_Object=MibTableColumn
h3cQoSProfActionNumber=_H3cQoSProfActionNumber_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,1,1,1,3),_H3cQoSProfActionNumber_Type())
h3cQoSProfActionNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSProfActionNumber.setStatus(_A)
_H3cQoSProfRowStatus_Type=RowStatus
_H3cQoSProfRowStatus_Object=MibTableColumn
h3cQoSProfRowStatus=_H3cQoSProfRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,1,1,1,4),_H3cQoSProfRowStatus_Type())
h3cQoSProfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSProfRowStatus.setStatus(_A)
_H3cQoSAction_ObjectIdentity=ObjectIdentity
h3cQoSAction=_H3cQoSAction_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,17,1,2))
_H3cQoSTrafficLimitTable_Object=MibTable
h3cQoSTrafficLimitTable=_H3cQoSTrafficLimitTable_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1))
if mibBuilder.loadTexts:h3cQoSTrafficLimitTable.setStatus(_A)
_H3cQoSTrafficLimitEntry_Object=MibTableRow
h3cQoSTrafficLimitEntry=_H3cQoSTrafficLimitEntry_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1))
h3cQoSTrafficLimitEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:h3cQoSTrafficLimitEntry.setStatus(_A)
class _H3cQoSTrafLmtProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQoSTrafLmtProfIndex_Type.__name__=_C
_H3cQoSTrafLmtProfIndex_Object=MibTableColumn
h3cQoSTrafLmtProfIndex=_H3cQoSTrafLmtProfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,1),_H3cQoSTrafLmtProfIndex_Type())
h3cQoSTrafLmtProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSTrafLmtProfIndex.setStatus(_A)
class _H3cQoSTrafLmtActionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQoSTrafLmtActionIndex_Type.__name__=_C
_H3cQoSTrafLmtActionIndex_Object=MibTableColumn
h3cQoSTrafLmtActionIndex=_H3cQoSTrafLmtActionIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,2),_H3cQoSTrafLmtActionIndex_Type())
h3cQoSTrafLmtActionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSTrafLmtActionIndex.setStatus(_A)
_H3cQoSTrafLmtDirection_Type=H3cQoSDirection
_H3cQoSTrafLmtDirection_Object=MibTableColumn
h3cQoSTrafLmtDirection=_H3cQoSTrafLmtDirection_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,3),_H3cQoSTrafLmtDirection_Type())
h3cQoSTrafLmtDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtDirection.setStatus(_A)
class _H3cQoSTrafLmtUserAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999))
_H3cQoSTrafLmtUserAclNum_Type.__name__=_C
_H3cQoSTrafLmtUserAclNum_Object=MibTableColumn
h3cQoSTrafLmtUserAclNum=_H3cQoSTrafLmtUserAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,4),_H3cQoSTrafLmtUserAclNum_Type())
h3cQoSTrafLmtUserAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtUserAclNum.setStatus(_A)
class _H3cQoSTrafLmtUserAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSTrafLmtUserAclRule_Type.__name__=_C
_H3cQoSTrafLmtUserAclRule_Object=MibTableColumn
h3cQoSTrafLmtUserAclRule=_H3cQoSTrafLmtUserAclRule_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,5),_H3cQoSTrafLmtUserAclRule_Type())
h3cQoSTrafLmtUserAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtUserAclRule.setStatus(_A)
class _H3cQoSTrafLmtIpAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_H3cQoSTrafLmtIpAclNum_Type.__name__=_C
_H3cQoSTrafLmtIpAclNum_Object=MibTableColumn
h3cQoSTrafLmtIpAclNum=_H3cQoSTrafLmtIpAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,6),_H3cQoSTrafLmtIpAclNum_Type())
h3cQoSTrafLmtIpAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtIpAclNum.setStatus(_A)
class _H3cQoSTrafLmtIpAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSTrafLmtIpAclRule_Type.__name__=_C
_H3cQoSTrafLmtIpAclRule_Object=MibTableColumn
h3cQoSTrafLmtIpAclRule=_H3cQoSTrafLmtIpAclRule_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,7),_H3cQoSTrafLmtIpAclRule_Type())
h3cQoSTrafLmtIpAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtIpAclRule.setStatus(_A)
class _H3cQoSTrafLmtLinkAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999))
_H3cQoSTrafLmtLinkAclNum_Type.__name__=_C
_H3cQoSTrafLmtLinkAclNum_Object=MibTableColumn
h3cQoSTrafLmtLinkAclNum=_H3cQoSTrafLmtLinkAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,8),_H3cQoSTrafLmtLinkAclNum_Type())
h3cQoSTrafLmtLinkAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtLinkAclNum.setStatus(_A)
class _H3cQoSTrafLmtLinkAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSTrafLmtLinkAclRule_Type.__name__=_C
_H3cQoSTrafLmtLinkAclRule_Object=MibTableColumn
h3cQoSTrafLmtLinkAclRule=_H3cQoSTrafLmtLinkAclRule_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,9),_H3cQoSTrafLmtLinkAclRule_Type())
h3cQoSTrafLmtLinkAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtLinkAclRule.setStatus(_A)
class _H3cQoSTrafLmtTargetRateMbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_H3cQoSTrafLmtTargetRateMbps_Type.__name__=_C
_H3cQoSTrafLmtTargetRateMbps_Object=MibTableColumn
h3cQoSTrafLmtTargetRateMbps=_H3cQoSTrafLmtTargetRateMbps_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,10),_H3cQoSTrafLmtTargetRateMbps_Type())
h3cQoSTrafLmtTargetRateMbps.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtTargetRateMbps.setStatus(_A)
class _H3cQoSTrafLmtTargetRateKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_H3cQoSTrafLmtTargetRateKbps_Type.__name__=_C
_H3cQoSTrafLmtTargetRateKbps_Object=MibTableColumn
h3cQoSTrafLmtTargetRateKbps=_H3cQoSTrafLmtTargetRateKbps_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,11),_H3cQoSTrafLmtTargetRateKbps_Type())
h3cQoSTrafLmtTargetRateKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtTargetRateKbps.setStatus(_A)
class _H3cQoSTrafLmtPeakRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,8388608))
_H3cQoSTrafLmtPeakRate_Type.__name__=_C
_H3cQoSTrafLmtPeakRate_Object=MibTableColumn
h3cQoSTrafLmtPeakRate=_H3cQoSTrafLmtPeakRate_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,12),_H3cQoSTrafLmtPeakRate_Type())
h3cQoSTrafLmtPeakRate.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtPeakRate.setStatus(_A)
class _H3cQoSTrafLmtCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34120000))
_H3cQoSTrafLmtCIR_Type.__name__=_C
_H3cQoSTrafLmtCIR_Object=MibTableColumn
h3cQoSTrafLmtCIR=_H3cQoSTrafLmtCIR_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,13),_H3cQoSTrafLmtCIR_Type())
h3cQoSTrafLmtCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtCIR.setStatus(_A)
class _H3cQoSTrafLmtCBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_H3cQoSTrafLmtCBS_Type.__name__=_C
_H3cQoSTrafLmtCBS_Object=MibTableColumn
h3cQoSTrafLmtCBS=_H3cQoSTrafLmtCBS_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,14),_H3cQoSTrafLmtCBS_Type())
h3cQoSTrafLmtCBS.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtCBS.setStatus(_A)
class _H3cQoSTrafLmtEBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435455))
_H3cQoSTrafLmtEBS_Type.__name__=_C
_H3cQoSTrafLmtEBS_Object=MibTableColumn
h3cQoSTrafLmtEBS=_H3cQoSTrafLmtEBS_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,15),_H3cQoSTrafLmtEBS_Type())
h3cQoSTrafLmtEBS.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtEBS.setStatus(_A)
class _H3cQoSTrafLmtPIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34120000))
_H3cQoSTrafLmtPIR_Type.__name__=_C
_H3cQoSTrafLmtPIR_Object=MibTableColumn
h3cQoSTrafLmtPIR=_H3cQoSTrafLmtPIR_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,16),_H3cQoSTrafLmtPIR_Type())
h3cQoSTrafLmtPIR.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtPIR.setStatus(_A)
class _H3cQoSTrafLmtConformLocalPre_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cQoSTrafLmtConformLocalPre_Type.__name__=_C
_H3cQoSTrafLmtConformLocalPre_Object=MibTableColumn
h3cQoSTrafLmtConformLocalPre=_H3cQoSTrafLmtConformLocalPre_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,17),_H3cQoSTrafLmtConformLocalPre_Type())
h3cQoSTrafLmtConformLocalPre.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtConformLocalPre.setStatus(_A)
class _H3cQoSTrafLmtConformActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_H,0),('remark-cos',1),('remark-drop-priority',2),('remark-cos-drop-priority',3),('remark-policed-service',4),('remark-dscp',5)))
_H3cQoSTrafLmtConformActionType_Type.__name__=_C
_H3cQoSTrafLmtConformActionType_Object=MibTableColumn
h3cQoSTrafLmtConformActionType=_H3cQoSTrafLmtConformActionType_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,18),_H3cQoSTrafLmtConformActionType_Type())
h3cQoSTrafLmtConformActionType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtConformActionType.setStatus(_A)
class _H3cQoSTrafLmtExceedActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('forward',1),('drop',2),('remarkdscp',3),('exceed-cos',4)))
_H3cQoSTrafLmtExceedActionType_Type.__name__=_C
_H3cQoSTrafLmtExceedActionType_Object=MibTableColumn
h3cQoSTrafLmtExceedActionType=_H3cQoSTrafLmtExceedActionType_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,19),_H3cQoSTrafLmtExceedActionType_Type())
h3cQoSTrafLmtExceedActionType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtExceedActionType.setStatus(_A)
class _H3cQoSTrafLmtExceedDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cQoSTrafLmtExceedDscp_Type.__name__=_C
_H3cQoSTrafLmtExceedDscp_Object=MibTableColumn
h3cQoSTrafLmtExceedDscp=_H3cQoSTrafLmtExceedDscp_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,20),_H3cQoSTrafLmtExceedDscp_Type())
h3cQoSTrafLmtExceedDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtExceedDscp.setStatus(_A)
class _H3cQoSTrafLmtExceedCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSTrafLmtExceedCos_Type.__name__=_C
_H3cQoSTrafLmtExceedCos_Object=MibTableColumn
h3cQoSTrafLmtExceedCos=_H3cQoSTrafLmtExceedCos_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,21),_H3cQoSTrafLmtExceedCos_Type())
h3cQoSTrafLmtExceedCos.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtExceedCos.setStatus(_A)
_H3cQoSTrafLmtRowStatus_Type=RowStatus
_H3cQoSTrafLmtRowStatus_Object=MibTableColumn
h3cQoSTrafLmtRowStatus=_H3cQoSTrafLmtRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,22),_H3cQoSTrafLmtRowStatus_Type())
h3cQoSTrafLmtRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtRowStatus.setStatus(_A)
class _H3cQoSTrafLmtConformCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSTrafLmtConformCos_Type.__name__=_C
_H3cQoSTrafLmtConformCos_Object=MibTableColumn
h3cQoSTrafLmtConformCos=_H3cQoSTrafLmtConformCos_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,23),_H3cQoSTrafLmtConformCos_Type())
h3cQoSTrafLmtConformCos.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtConformCos.setStatus(_A)
class _H3cQoSTrafLmtConformDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cQoSTrafLmtConformDscp_Type.__name__=_C
_H3cQoSTrafLmtConformDscp_Object=MibTableColumn
h3cQoSTrafLmtConformDscp=_H3cQoSTrafLmtConformDscp_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,1,1,24),_H3cQoSTrafLmtConformDscp_Type())
h3cQoSTrafLmtConformDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafLmtConformDscp.setStatus(_A)
_H3cQoSTrafficPriorityTable_Object=MibTable
h3cQoSTrafficPriorityTable=_H3cQoSTrafficPriorityTable_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2))
if mibBuilder.loadTexts:h3cQoSTrafficPriorityTable.setStatus(_A)
_H3cQoSTrafficPriorityEntry_Object=MibTableRow
h3cQoSTrafficPriorityEntry=_H3cQoSTrafficPriorityEntry_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1))
h3cQoSTrafficPriorityEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:h3cQoSTrafficPriorityEntry.setStatus(_A)
class _H3cQoSTrafPrioProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQoSTrafPrioProfIndex_Type.__name__=_C
_H3cQoSTrafPrioProfIndex_Object=MibTableColumn
h3cQoSTrafPrioProfIndex=_H3cQoSTrafPrioProfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,1),_H3cQoSTrafPrioProfIndex_Type())
h3cQoSTrafPrioProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSTrafPrioProfIndex.setStatus(_A)
class _H3cQoSTrafPrioActionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQoSTrafPrioActionIndex_Type.__name__=_C
_H3cQoSTrafPrioActionIndex_Object=MibTableColumn
h3cQoSTrafPrioActionIndex=_H3cQoSTrafPrioActionIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,2),_H3cQoSTrafPrioActionIndex_Type())
h3cQoSTrafPrioActionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSTrafPrioActionIndex.setStatus(_A)
_H3cQoSTrafPrioDirection_Type=H3cQoSDirection
_H3cQoSTrafPrioDirection_Object=MibTableColumn
h3cQoSTrafPrioDirection=_H3cQoSTrafPrioDirection_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,3),_H3cQoSTrafPrioDirection_Type())
h3cQoSTrafPrioDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioDirection.setStatus(_A)
class _H3cQoSTrafPrioUserAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999))
_H3cQoSTrafPrioUserAclNum_Type.__name__=_C
_H3cQoSTrafPrioUserAclNum_Object=MibTableColumn
h3cQoSTrafPrioUserAclNum=_H3cQoSTrafPrioUserAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,4),_H3cQoSTrafPrioUserAclNum_Type())
h3cQoSTrafPrioUserAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioUserAclNum.setStatus(_A)
class _H3cQoSTrafPrioUserAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSTrafPrioUserAclRule_Type.__name__=_C
_H3cQoSTrafPrioUserAclRule_Object=MibTableColumn
h3cQoSTrafPrioUserAclRule=_H3cQoSTrafPrioUserAclRule_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,5),_H3cQoSTrafPrioUserAclRule_Type())
h3cQoSTrafPrioUserAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioUserAclRule.setStatus(_A)
class _H3cQoSTrafPrioIpAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_H3cQoSTrafPrioIpAclNum_Type.__name__=_C
_H3cQoSTrafPrioIpAclNum_Object=MibTableColumn
h3cQoSTrafPrioIpAclNum=_H3cQoSTrafPrioIpAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,6),_H3cQoSTrafPrioIpAclNum_Type())
h3cQoSTrafPrioIpAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioIpAclNum.setStatus(_A)
class _H3cQoSTrafPrioIpAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSTrafPrioIpAclRule_Type.__name__=_C
_H3cQoSTrafPrioIpAclRule_Object=MibTableColumn
h3cQoSTrafPrioIpAclRule=_H3cQoSTrafPrioIpAclRule_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,7),_H3cQoSTrafPrioIpAclRule_Type())
h3cQoSTrafPrioIpAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioIpAclRule.setStatus(_A)
class _H3cQoSTrafPrioLinkAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999))
_H3cQoSTrafPrioLinkAclNum_Type.__name__=_C
_H3cQoSTrafPrioLinkAclNum_Object=MibTableColumn
h3cQoSTrafPrioLinkAclNum=_H3cQoSTrafPrioLinkAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,8),_H3cQoSTrafPrioLinkAclNum_Type())
h3cQoSTrafPrioLinkAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioLinkAclNum.setStatus(_A)
class _H3cQoSTrafPrioLinkAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSTrafPrioLinkAclRule_Type.__name__=_C
_H3cQoSTrafPrioLinkAclRule_Object=MibTableColumn
h3cQoSTrafPrioLinkAclRule=_H3cQoSTrafPrioLinkAclRule_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,9),_H3cQoSTrafPrioLinkAclRule_Type())
h3cQoSTrafPrioLinkAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioLinkAclRule.setStatus(_A)
class _H3cQoSTrafPrioDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cQoSTrafPrioDscp_Type.__name__=_C
_H3cQoSTrafPrioDscp_Object=MibTableColumn
h3cQoSTrafPrioDscp=_H3cQoSTrafPrioDscp_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,10),_H3cQoSTrafPrioDscp_Type())
h3cQoSTrafPrioDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioDscp.setStatus(_A)
class _H3cQoSTrafPrioIpPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSTrafPrioIpPre_Type.__name__=_C
_H3cQoSTrafPrioIpPre_Object=MibTableColumn
h3cQoSTrafPrioIpPre=_H3cQoSTrafPrioIpPre_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,11),_H3cQoSTrafPrioIpPre_Type())
h3cQoSTrafPrioIpPre.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioIpPre.setStatus(_A)
class _H3cQoSTrafPrioIpPreFromCos_Type(TruthValue):defaultValue=2
_H3cQoSTrafPrioIpPreFromCos_Type.__name__=_I
_H3cQoSTrafPrioIpPreFromCos_Object=MibTableColumn
h3cQoSTrafPrioIpPreFromCos=_H3cQoSTrafPrioIpPreFromCos_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,12),_H3cQoSTrafPrioIpPreFromCos_Type())
h3cQoSTrafPrioIpPreFromCos.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioIpPreFromCos.setStatus(_A)
class _H3cQoSTrafPrioCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSTrafPrioCos_Type.__name__=_C
_H3cQoSTrafPrioCos_Object=MibTableColumn
h3cQoSTrafPrioCos=_H3cQoSTrafPrioCos_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,13),_H3cQoSTrafPrioCos_Type())
h3cQoSTrafPrioCos.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioCos.setStatus(_A)
class _H3cQoSTrafPrioCosFromIpPre_Type(TruthValue):defaultValue=2
_H3cQoSTrafPrioCosFromIpPre_Type.__name__=_I
_H3cQoSTrafPrioCosFromIpPre_Object=MibTableColumn
h3cQoSTrafPrioCosFromIpPre=_H3cQoSTrafPrioCosFromIpPre_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,14),_H3cQoSTrafPrioCosFromIpPre_Type())
h3cQoSTrafPrioCosFromIpPre.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioCosFromIpPre.setStatus(_A)
class _H3cQoSTrafPrioLocalPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSTrafPrioLocalPre_Type.__name__=_C
_H3cQoSTrafPrioLocalPre_Object=MibTableColumn
h3cQoSTrafPrioLocalPre=_H3cQoSTrafPrioLocalPre_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,15),_H3cQoSTrafPrioLocalPre_Type())
h3cQoSTrafPrioLocalPre.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioLocalPre.setStatus(_A)
class _H3cQoSTrafPrioPolicedServiceType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4)));namedValues=NamedValues(*((_H,0),('trust-dscp',2),('new-dscp',3),('untrusted',4)))
_H3cQoSTrafPrioPolicedServiceType_Type.__name__=_C
_H3cQoSTrafPrioPolicedServiceType_Object=MibTableColumn
h3cQoSTrafPrioPolicedServiceType=_H3cQoSTrafPrioPolicedServiceType_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,16),_H3cQoSTrafPrioPolicedServiceType_Type())
h3cQoSTrafPrioPolicedServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioPolicedServiceType.setStatus(_A)
class _H3cQoSTrafPrioPolicedServiceDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cQoSTrafPrioPolicedServiceDscp_Type.__name__=_C
_H3cQoSTrafPrioPolicedServiceDscp_Object=MibTableColumn
h3cQoSTrafPrioPolicedServiceDscp=_H3cQoSTrafPrioPolicedServiceDscp_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,17),_H3cQoSTrafPrioPolicedServiceDscp_Type())
h3cQoSTrafPrioPolicedServiceDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioPolicedServiceDscp.setStatus(_A)
class _H3cQoSTrafPrioPolicedServiceExp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSTrafPrioPolicedServiceExp_Type.__name__=_C
_H3cQoSTrafPrioPolicedServiceExp_Object=MibTableColumn
h3cQoSTrafPrioPolicedServiceExp=_H3cQoSTrafPrioPolicedServiceExp_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,18),_H3cQoSTrafPrioPolicedServiceExp_Type())
h3cQoSTrafPrioPolicedServiceExp.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioPolicedServiceExp.setStatus(_A)
class _H3cQoSTrafPrioPolicedServiceCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSTrafPrioPolicedServiceCos_Type.__name__=_C
_H3cQoSTrafPrioPolicedServiceCos_Object=MibTableColumn
h3cQoSTrafPrioPolicedServiceCos=_H3cQoSTrafPrioPolicedServiceCos_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,19),_H3cQoSTrafPrioPolicedServiceCos_Type())
h3cQoSTrafPrioPolicedServiceCos.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioPolicedServiceCos.setStatus(_A)
class _H3cQoSTrafPrioPolicedServiceLoaclPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSTrafPrioPolicedServiceLoaclPre_Type.__name__=_C
_H3cQoSTrafPrioPolicedServiceLoaclPre_Object=MibTableColumn
h3cQoSTrafPrioPolicedServiceLoaclPre=_H3cQoSTrafPrioPolicedServiceLoaclPre_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,20),_H3cQoSTrafPrioPolicedServiceLoaclPre_Type())
h3cQoSTrafPrioPolicedServiceLoaclPre.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioPolicedServiceLoaclPre.setStatus(_A)
class _H3cQoSTrafPrioPolicedServiceDropPriority_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2),ValueRangeConstraint(255,255))
_H3cQoSTrafPrioPolicedServiceDropPriority_Type.__name__=_C
_H3cQoSTrafPrioPolicedServiceDropPriority_Object=MibTableColumn
h3cQoSTrafPrioPolicedServiceDropPriority=_H3cQoSTrafPrioPolicedServiceDropPriority_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,21),_H3cQoSTrafPrioPolicedServiceDropPriority_Type())
h3cQoSTrafPrioPolicedServiceDropPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioPolicedServiceDropPriority.setStatus(_A)
_H3cQoSTrafPrioRowStatus_Type=RowStatus
_H3cQoSTrafPrioRowStatus_Object=MibTableColumn
h3cQoSTrafPrioRowStatus=_H3cQoSTrafPrioRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,2,1,22),_H3cQoSTrafPrioRowStatus_Type())
h3cQoSTrafPrioRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafPrioRowStatus.setStatus(_A)
_H3cQoSTrafficFilterTable_Object=MibTable
h3cQoSTrafficFilterTable=_H3cQoSTrafficFilterTable_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3))
if mibBuilder.loadTexts:h3cQoSTrafficFilterTable.setStatus(_A)
_H3cQoSTrafficFilterEntry_Object=MibTableRow
h3cQoSTrafficFilterEntry=_H3cQoSTrafficFilterEntry_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1))
h3cQoSTrafficFilterEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:h3cQoSTrafficFilterEntry.setStatus(_A)
class _H3cQoSTrafFilterProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQoSTrafFilterProfIndex_Type.__name__=_C
_H3cQoSTrafFilterProfIndex_Object=MibTableColumn
h3cQoSTrafFilterProfIndex=_H3cQoSTrafFilterProfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,1),_H3cQoSTrafFilterProfIndex_Type())
h3cQoSTrafFilterProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSTrafFilterProfIndex.setStatus(_A)
class _H3cQoSTrafFilterActionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQoSTrafFilterActionIndex_Type.__name__=_C
_H3cQoSTrafFilterActionIndex_Object=MibTableColumn
h3cQoSTrafFilterActionIndex=_H3cQoSTrafFilterActionIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,2),_H3cQoSTrafFilterActionIndex_Type())
h3cQoSTrafFilterActionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSTrafFilterActionIndex.setStatus(_A)
_H3cQoSTrafFilterDirection_Type=H3cQoSDirection
_H3cQoSTrafFilterDirection_Object=MibTableColumn
h3cQoSTrafFilterDirection=_H3cQoSTrafFilterDirection_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,3),_H3cQoSTrafFilterDirection_Type())
h3cQoSTrafFilterDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafFilterDirection.setStatus(_A)
class _H3cQoSTrafFilterUserAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999))
_H3cQoSTrafFilterUserAclNum_Type.__name__=_C
_H3cQoSTrafFilterUserAclNum_Object=MibTableColumn
h3cQoSTrafFilterUserAclNum=_H3cQoSTrafFilterUserAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,4),_H3cQoSTrafFilterUserAclNum_Type())
h3cQoSTrafFilterUserAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafFilterUserAclNum.setStatus(_A)
class _H3cQoSTrafFilterUserAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSTrafFilterUserAclRule_Type.__name__=_C
_H3cQoSTrafFilterUserAclRule_Object=MibTableColumn
h3cQoSTrafFilterUserAclRule=_H3cQoSTrafFilterUserAclRule_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,5),_H3cQoSTrafFilterUserAclRule_Type())
h3cQoSTrafFilterUserAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafFilterUserAclRule.setStatus(_A)
class _H3cQoSTrafFilterIpAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_H3cQoSTrafFilterIpAclNum_Type.__name__=_C
_H3cQoSTrafFilterIpAclNum_Object=MibTableColumn
h3cQoSTrafFilterIpAclNum=_H3cQoSTrafFilterIpAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,6),_H3cQoSTrafFilterIpAclNum_Type())
h3cQoSTrafFilterIpAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafFilterIpAclNum.setStatus(_A)
class _H3cQoSTrafFilterIpAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSTrafFilterIpAclRule_Type.__name__=_C
_H3cQoSTrafFilterIpAclRule_Object=MibTableColumn
h3cQoSTrafFilterIpAclRule=_H3cQoSTrafFilterIpAclRule_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,7),_H3cQoSTrafFilterIpAclRule_Type())
h3cQoSTrafFilterIpAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafFilterIpAclRule.setStatus(_A)
class _H3cQoSTrafFilterLinkAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999))
_H3cQoSTrafFilterLinkAclNum_Type.__name__=_C
_H3cQoSTrafFilterLinkAclNum_Object=MibTableColumn
h3cQoSTrafFilterLinkAclNum=_H3cQoSTrafFilterLinkAclNum_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,8),_H3cQoSTrafFilterLinkAclNum_Type())
h3cQoSTrafFilterLinkAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafFilterLinkAclNum.setStatus(_A)
class _H3cQoSTrafFilterLinkAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSTrafFilterLinkAclRule_Type.__name__=_C
_H3cQoSTrafFilterLinkAclRule_Object=MibTableColumn
h3cQoSTrafFilterLinkAclRule=_H3cQoSTrafFilterLinkAclRule_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,9),_H3cQoSTrafFilterLinkAclRule_Type())
h3cQoSTrafFilterLinkAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafFilterLinkAclRule.setStatus(_A)
_H3cQoSTrafFilterRowStatus_Type=RowStatus
_H3cQoSTrafFilterRowStatus_Object=MibTableColumn
h3cQoSTrafFilterRowStatus=_H3cQoSTrafFilterRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,2,3,1,10),_H3cQoSTrafFilterRowStatus_Type())
h3cQoSTrafFilterRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSTrafFilterRowStatus.setStatus(_A)
_H3cQoSProfPortMapping_ObjectIdentity=ObjectIdentity
h3cQoSProfPortMapping=_H3cQoSProfPortMapping_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,17,1,3))
_H3cQoSProfPortMappingTable_Object=MibTable
h3cQoSProfPortMappingTable=_H3cQoSProfPortMappingTable_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,1))
if mibBuilder.loadTexts:h3cQoSProfPortMappingTable.setStatus(_A)
_H3cQoSProfPortMappingEntry_Object=MibTableRow
h3cQoSProfPortMappingEntry=_H3cQoSProfPortMappingEntry_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,1,1))
h3cQoSProfPortMappingEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:h3cQoSProfPortMappingEntry.setStatus(_A)
class _H3cQoSProfPortMappingIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cQoSProfPortMappingIfIndex_Type.__name__=_C
_H3cQoSProfPortMappingIfIndex_Object=MibTableColumn
h3cQoSProfPortMappingIfIndex=_H3cQoSProfPortMappingIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,1,1,1),_H3cQoSProfPortMappingIfIndex_Type())
h3cQoSProfPortMappingIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSProfPortMappingIfIndex.setStatus(_A)
class _H3cQoSProfPortMappingProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQoSProfPortMappingProfIndex_Type.__name__=_C
_H3cQoSProfPortMappingProfIndex_Object=MibTableColumn
h3cQoSProfPortMappingProfIndex=_H3cQoSProfPortMappingProfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,1,1,2),_H3cQoSProfPortMappingProfIndex_Type())
h3cQoSProfPortMappingProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSProfPortMappingProfIndex.setStatus(_A)
_H3cQoSProfPortMappingRowStatus_Type=RowStatus
_H3cQoSProfPortMappingRowStatus_Object=MibTableColumn
h3cQoSProfPortMappingRowStatus=_H3cQoSProfPortMappingRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,1,1,3),_H3cQoSProfPortMappingRowStatus_Type())
h3cQoSProfPortMappingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cQoSProfPortMappingRowStatus.setStatus(_A)
_H3cQoSProfPortMappingModeTable_Object=MibTable
h3cQoSProfPortMappingModeTable=_H3cQoSProfPortMappingModeTable_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,2))
if mibBuilder.loadTexts:h3cQoSProfPortMappingModeTable.setStatus(_A)
_H3cQoSProfPortMappingModeEntry_Object=MibTableRow
h3cQoSProfPortMappingModeEntry=_H3cQoSProfPortMappingModeEntry_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,2,1))
h3cQoSProfPortMappingModeEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:h3cQoSProfPortMappingModeEntry.setStatus(_A)
class _H3cQoSProfPortMappingModeIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cQoSProfPortMappingModeIfIndex_Type.__name__=_C
_H3cQoSProfPortMappingModeIfIndex_Object=MibTableColumn
h3cQoSProfPortMappingModeIfIndex=_H3cQoSProfPortMappingModeIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,2,1,1),_H3cQoSProfPortMappingModeIfIndex_Type())
h3cQoSProfPortMappingModeIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSProfPortMappingModeIfIndex.setStatus(_A)
class _H3cQoSProfPortMappingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('user-based',1),('port-based',2)))
_H3cQoSProfPortMappingMode_Type.__name__=_C
_H3cQoSProfPortMappingMode_Object=MibTableColumn
h3cQoSProfPortMappingMode=_H3cQoSProfPortMappingMode_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,2,1,2),_H3cQoSProfPortMappingMode_Type())
h3cQoSProfPortMappingMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cQoSProfPortMappingMode.setStatus(_A)
_H3cQoSProfDynPortMappingTable_Object=MibTable
h3cQoSProfDynPortMappingTable=_H3cQoSProfDynPortMappingTable_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,3))
if mibBuilder.loadTexts:h3cQoSProfDynPortMappingTable.setStatus(_A)
_H3cQoSProfDynPortMappingEntry_Object=MibTableRow
h3cQoSProfDynPortMappingEntry=_H3cQoSProfDynPortMappingEntry_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,3,1))
h3cQoSProfDynPortMappingEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:h3cQoSProfDynPortMappingEntry.setStatus(_A)
class _H3cQoSProfDynPortMappingIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cQoSProfDynPortMappingIfIndex_Type.__name__=_C
_H3cQoSProfDynPortMappingIfIndex_Object=MibTableColumn
h3cQoSProfDynPortMappingIfIndex=_H3cQoSProfDynPortMappingIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,3,1,1),_H3cQoSProfDynPortMappingIfIndex_Type())
h3cQoSProfDynPortMappingIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSProfDynPortMappingIfIndex.setStatus(_A)
_H3cQoSProfDynPortMappingUserSrcMAC_Type=MacAddress
_H3cQoSProfDynPortMappingUserSrcMAC_Object=MibTableColumn
h3cQoSProfDynPortMappingUserSrcMAC=_H3cQoSProfDynPortMappingUserSrcMAC_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,3,1,2),_H3cQoSProfDynPortMappingUserSrcMAC_Type())
h3cQoSProfDynPortMappingUserSrcMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cQoSProfDynPortMappingUserSrcMAC.setStatus(_A)
class _H3cQoSProfDynPortMappingUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cQoSProfDynPortMappingUserName_Type.__name__=_G
_H3cQoSProfDynPortMappingUserName_Object=MibTableColumn
h3cQoSProfDynPortMappingUserName=_H3cQoSProfDynPortMappingUserName_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,3,1,3),_H3cQoSProfDynPortMappingUserName_Type())
h3cQoSProfDynPortMappingUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSProfDynPortMappingUserName.setStatus(_A)
_H3cQoSProfDynPortMappingUserIPAddr_Type=IpAddress
_H3cQoSProfDynPortMappingUserIPAddr_Object=MibTableColumn
h3cQoSProfDynPortMappingUserIPAddr=_H3cQoSProfDynPortMappingUserIPAddr_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,3,1,4),_H3cQoSProfDynPortMappingUserIPAddr_Type())
h3cQoSProfDynPortMappingUserIPAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSProfDynPortMappingUserIPAddr.setStatus(_A)
class _H3cQoSProfDynPortMappingUserVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQoSProfDynPortMappingUserVLANID_Type.__name__=_C
_H3cQoSProfDynPortMappingUserVLANID_Object=MibTableColumn
h3cQoSProfDynPortMappingUserVLANID=_H3cQoSProfDynPortMappingUserVLANID_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,3,1,5),_H3cQoSProfDynPortMappingUserVLANID_Type())
h3cQoSProfDynPortMappingUserVLANID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSProfDynPortMappingUserVLANID.setStatus(_A)
class _H3cQoSProfDynPortMappingUserProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cQoSProfDynPortMappingUserProfName_Type.__name__=_G
_H3cQoSProfDynPortMappingUserProfName_Object=MibTableColumn
h3cQoSProfDynPortMappingUserProfName=_H3cQoSProfDynPortMappingUserProfName_Object((1,3,6,1,4,1,43,45,1,10,2,17,1,3,3,1,6),_H3cQoSProfDynPortMappingUserProfName_Type())
h3cQoSProfDynPortMappingUserProfName.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSProfDynPortMappingUserProfName.setStatus(_A)
_H3cQoSProfPortMappingTraps_ObjectIdentity=ObjectIdentity
h3cQoSProfPortMappingTraps=_H3cQoSProfPortMappingTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,17,2))
_H3cQoSProfMibConformance_ObjectIdentity=ObjectIdentity
h3cQoSProfMibConformance=_H3cQoSProfMibConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,17,3))
_H3cQoSProfMibCompliances_ObjectIdentity=ObjectIdentity
h3cQoSProfMibCompliances=_H3cQoSProfMibCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,17,3,1))
_H3cQoSProfMibGroups_ObjectIdentity=ObjectIdentity
h3cQoSProfMibGroups=_H3cQoSProfMibGroups_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,17,3,2))
h3cQoSProfGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,17,3,2,1))
h3cQoSProfGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:h3cQoSProfGroup.setStatus(_A)
h3cQoSActionGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,17,3,2,2))
h3cQoSActionGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:h3cQoSActionGroup.setStatus(_A)
h3cQoSProfPortMappingGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,17,3,2,3))
h3cQoSProfPortMappingGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:h3cQoSProfPortMappingGroup.setStatus(_A)
h3cQoSProfPortMappingError=NotificationType((1,3,6,1,4,1,43,45,1,10,2,17,2,1))
if mibBuilder.loadTexts:h3cQoSProfPortMappingError.setStatus(_A)
h3cQoSProfPortMappingTrapsGroup=NotificationGroup((1,3,6,1,4,1,43,45,1,10,2,17,3,2,4))
h3cQoSProfPortMappingTrapsGroup.setObjects((_B,_AS))
if mibBuilder.loadTexts:h3cQoSProfPortMappingTrapsGroup.setStatus(_A)
h3cQoSProfMibCompliance=ModuleCompliance((1,3,6,1,4,1,43,45,1,10,2,17,3,1,1))
h3cQoSProfMibCompliance.setObjects(*((_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:h3cQoSProfMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'H3cQoSDirection':H3cQoSDirection,'h3cQosProfile':h3cQosProfile,'h3cQoSProfObjects':h3cQoSProfObjects,'h3cQoSProf':h3cQoSProf,'h3cQoSProfTable':h3cQoSProfTable,'h3cQoSProfEntry':h3cQoSProfEntry,_J:h3cQoSProfIndex,_V:h3cQoSProfName,_W:h3cQoSProfActionNumber,_X:h3cQoSProfRowStatus,'h3cQoSAction':h3cQoSAction,'h3cQoSTrafficLimitTable':h3cQoSTrafficLimitTable,'h3cQoSTrafficLimitEntry':h3cQoSTrafficLimitEntry,_K:h3cQoSTrafLmtProfIndex,_L:h3cQoSTrafLmtActionIndex,_Y:h3cQoSTrafLmtDirection,_Z:h3cQoSTrafLmtUserAclNum,_a:h3cQoSTrafLmtUserAclRule,_b:h3cQoSTrafLmtIpAclNum,_c:h3cQoSTrafLmtIpAclRule,_d:h3cQoSTrafLmtLinkAclNum,_e:h3cQoSTrafLmtLinkAclRule,_f:h3cQoSTrafLmtTargetRateMbps,_g:h3cQoSTrafLmtTargetRateKbps,_h:h3cQoSTrafLmtPeakRate,_i:h3cQoSTrafLmtCIR,_j:h3cQoSTrafLmtCBS,_k:h3cQoSTrafLmtEBS,_l:h3cQoSTrafLmtPIR,_m:h3cQoSTrafLmtConformLocalPre,_n:h3cQoSTrafLmtConformActionType,_o:h3cQoSTrafLmtExceedActionType,_p:h3cQoSTrafLmtExceedDscp,_q:h3cQoSTrafLmtExceedCos,_r:h3cQoSTrafLmtRowStatus,_s:h3cQoSTrafLmtConformCos,_t:h3cQoSTrafLmtConformDscp,'h3cQoSTrafficPriorityTable':h3cQoSTrafficPriorityTable,'h3cQoSTrafficPriorityEntry':h3cQoSTrafficPriorityEntry,_M:h3cQoSTrafPrioProfIndex,_N:h3cQoSTrafPrioActionIndex,_u:h3cQoSTrafPrioDirection,_v:h3cQoSTrafPrioUserAclNum,_w:h3cQoSTrafPrioUserAclRule,_x:h3cQoSTrafPrioIpAclNum,_y:h3cQoSTrafPrioIpAclRule,_z:h3cQoSTrafPrioLinkAclNum,_A0:h3cQoSTrafPrioLinkAclRule,_A1:h3cQoSTrafPrioDscp,_A2:h3cQoSTrafPrioIpPre,_A3:h3cQoSTrafPrioIpPreFromCos,_A4:h3cQoSTrafPrioCos,_A5:h3cQoSTrafPrioCosFromIpPre,_A6:h3cQoSTrafPrioLocalPre,_A7:h3cQoSTrafPrioPolicedServiceType,_A8:h3cQoSTrafPrioPolicedServiceDscp,_A9:h3cQoSTrafPrioPolicedServiceExp,_AA:h3cQoSTrafPrioPolicedServiceCos,_AB:h3cQoSTrafPrioPolicedServiceLoaclPre,_AC:h3cQoSTrafPrioPolicedServiceDropPriority,_AD:h3cQoSTrafPrioRowStatus,'h3cQoSTrafficFilterTable':h3cQoSTrafficFilterTable,'h3cQoSTrafficFilterEntry':h3cQoSTrafficFilterEntry,_O:h3cQoSTrafFilterProfIndex,_P:h3cQoSTrafFilterActionIndex,_AE:h3cQoSTrafFilterDirection,_AF:h3cQoSTrafFilterUserAclNum,_AG:h3cQoSTrafFilterUserAclRule,_AH:h3cQoSTrafFilterIpAclNum,_AI:h3cQoSTrafFilterIpAclRule,_AJ:h3cQoSTrafFilterLinkAclNum,_AK:h3cQoSTrafFilterLinkAclRule,_AL:h3cQoSTrafFilterRowStatus,'h3cQoSProfPortMapping':h3cQoSProfPortMapping,'h3cQoSProfPortMappingTable':h3cQoSProfPortMappingTable,'h3cQoSProfPortMappingEntry':h3cQoSProfPortMappingEntry,_Q:h3cQoSProfPortMappingIfIndex,_R:h3cQoSProfPortMappingProfIndex,_AM:h3cQoSProfPortMappingRowStatus,'h3cQoSProfPortMappingModeTable':h3cQoSProfPortMappingModeTable,'h3cQoSProfPortMappingModeEntry':h3cQoSProfPortMappingModeEntry,_S:h3cQoSProfPortMappingModeIfIndex,_AN:h3cQoSProfPortMappingMode,'h3cQoSProfDynPortMappingTable':h3cQoSProfDynPortMappingTable,'h3cQoSProfDynPortMappingEntry':h3cQoSProfDynPortMappingEntry,_T:h3cQoSProfDynPortMappingIfIndex,_U:h3cQoSProfDynPortMappingUserSrcMAC,_AO:h3cQoSProfDynPortMappingUserName,_AP:h3cQoSProfDynPortMappingUserIPAddr,_AQ:h3cQoSProfDynPortMappingUserVLANID,_AR:h3cQoSProfDynPortMappingUserProfName,'h3cQoSProfPortMappingTraps':h3cQoSProfPortMappingTraps,_AS:h3cQoSProfPortMappingError,'h3cQoSProfMibConformance':h3cQoSProfMibConformance,'h3cQoSProfMibCompliances':h3cQoSProfMibCompliances,'h3cQoSProfMibCompliance':h3cQoSProfMibCompliance,'h3cQoSProfMibGroups':h3cQoSProfMibGroups,_AT:h3cQoSProfGroup,_AU:h3cQoSActionGroup,_AV:h3cQoSProfPortMappingGroup,_AW:h3cQoSProfPortMappingTrapsGroup})