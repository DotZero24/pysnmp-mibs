_AW='hpnicfQoSProfPortMappingTrapsGroup'
_AV='hpnicfQoSProfPortMappingGroup'
_AU='hpnicfQoSActionGroup'
_AT='hpnicfQoSProfGroup'
_AS='hpnicfQoSProfPortMappingError'
_AR='hpnicfQoSProfDynPortMappingUserProfName'
_AQ='hpnicfQoSProfDynPortMappingUserVLANID'
_AP='hpnicfQoSProfDynPortMappingUserIPAddr'
_AO='hpnicfQoSProfDynPortMappingUserName'
_AN='hpnicfQoSProfPortMappingMode'
_AM='hpnicfQoSProfPortMappingRowStatus'
_AL='hpnicfQoSTrafFilterRowStatus'
_AK='hpnicfQoSTrafFilterLinkAclRule'
_AJ='hpnicfQoSTrafFilterLinkAclNum'
_AI='hpnicfQoSTrafFilterIpAclRule'
_AH='hpnicfQoSTrafFilterIpAclNum'
_AG='hpnicfQoSTrafFilterUserAclRule'
_AF='hpnicfQoSTrafFilterUserAclNum'
_AE='hpnicfQoSTrafFilterDirection'
_AD='hpnicfQoSTrafPrioRowStatus'
_AC='hpnicfQoSTrafPrioPolicedServiceDropPriority'
_AB='hpnicfQoSTrafPrioPolicedServiceLoaclPre'
_AA='hpnicfQoSTrafPrioPolicedServiceCos'
_A9='hpnicfQoSTrafPrioPolicedServiceExp'
_A8='hpnicfQoSTrafPrioPolicedServiceDscp'
_A7='hpnicfQoSTrafPrioPolicedServiceType'
_A6='hpnicfQoSTrafPrioLocalPre'
_A5='hpnicfQoSTrafPrioCosFromIpPre'
_A4='hpnicfQoSTrafPrioCos'
_A3='hpnicfQoSTrafPrioIpPreFromCos'
_A2='hpnicfQoSTrafPrioIpPre'
_A1='hpnicfQoSTrafPrioDscp'
_A0='hpnicfQoSTrafPrioLinkAclRule'
_z='hpnicfQoSTrafPrioLinkAclNum'
_y='hpnicfQoSTrafPrioIpAclRule'
_x='hpnicfQoSTrafPrioIpAclNum'
_w='hpnicfQoSTrafPrioUserAclRule'
_v='hpnicfQoSTrafPrioUserAclNum'
_u='hpnicfQoSTrafPrioDirection'
_t='hpnicfQoSTrafLmtConformDscp'
_s='hpnicfQoSTrafLmtConformCos'
_r='hpnicfQoSTrafLmtRowStatus'
_q='hpnicfQoSTrafLmtExceedCos'
_p='hpnicfQoSTrafLmtExceedDscp'
_o='hpnicfQoSTrafLmtExceedActionType'
_n='hpnicfQoSTrafLmtConformActionType'
_m='hpnicfQoSTrafLmtConformLocalPre'
_l='hpnicfQoSTrafLmtPIR'
_k='hpnicfQoSTrafLmtEBS'
_j='hpnicfQoSTrafLmtCBS'
_i='hpnicfQoSTrafLmtCIR'
_h='hpnicfQoSTrafLmtPeakRate'
_g='hpnicfQoSTrafLmtTargetRateKbps'
_f='hpnicfQoSTrafLmtTargetRateMbps'
_e='hpnicfQoSTrafLmtLinkAclRule'
_d='hpnicfQoSTrafLmtLinkAclNum'
_c='hpnicfQoSTrafLmtIpAclRule'
_b='hpnicfQoSTrafLmtIpAclNum'
_a='hpnicfQoSTrafLmtUserAclRule'
_Z='hpnicfQoSTrafLmtUserAclNum'
_Y='hpnicfQoSTrafLmtDirection'
_X='hpnicfQoSProfRowStatus'
_W='hpnicfQoSProfActionNumber'
_V='hpnicfQoSProfName'
_U='hpnicfQoSProfDynPortMappingUserSrcMAC'
_T='hpnicfQoSProfDynPortMappingIfIndex'
_S='hpnicfQoSProfPortMappingModeIfIndex'
_R='hpnicfQoSProfPortMappingProfIndex'
_Q='hpnicfQoSProfPortMappingIfIndex'
_P='hpnicfQoSTrafFilterActionIndex'
_O='hpnicfQoSTrafFilterProfIndex'
_N='hpnicfQoSTrafPrioActionIndex'
_M='hpnicfQoSTrafPrioProfIndex'
_L='hpnicfQoSTrafLmtActionIndex'
_K='hpnicfQoSTrafLmtProfIndex'
_J='hpnicfQoSProfIndex'
_I='TruthValue'
_H='invalid'
_G='OctetString'
_F='read-only'
_E='not-accessible'
_D='read-create'
_C='Integer32'
_B='HPN-ICF-QOS-PROFILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
hpnicfQosProfile=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,17))
class HpnicfQoSDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),('input',1),('ouput',2)))
_HpnicfQoSProfObjects_ObjectIdentity=ObjectIdentity
hpnicfQoSProfObjects=_HpnicfQoSProfObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,17,1))
_HpnicfQoSProf_ObjectIdentity=ObjectIdentity
hpnicfQoSProf=_HpnicfQoSProf_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,17,1,1))
_HpnicfQoSProfTable_Object=MibTable
hpnicfQoSProfTable=_HpnicfQoSProfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,1,1))
if mibBuilder.loadTexts:hpnicfQoSProfTable.setStatus(_A)
_HpnicfQoSProfEntry_Object=MibTableRow
hpnicfQoSProfEntry=_HpnicfQoSProfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,1,1,1))
hpnicfQoSProfEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpnicfQoSProfEntry.setStatus(_A)
class _HpnicfQoSProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQoSProfIndex_Type.__name__=_C
_HpnicfQoSProfIndex_Object=MibTableColumn
hpnicfQoSProfIndex=_HpnicfQoSProfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,1,1,1,1),_HpnicfQoSProfIndex_Type())
hpnicfQoSProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSProfIndex.setStatus(_A)
class _HpnicfQoSProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfQoSProfName_Type.__name__=_G
_HpnicfQoSProfName_Object=MibTableColumn
hpnicfQoSProfName=_HpnicfQoSProfName_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,1,1,1,2),_HpnicfQoSProfName_Type())
hpnicfQoSProfName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSProfName.setStatus(_A)
class _HpnicfQoSProfActionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSProfActionNumber_Type.__name__=_C
_HpnicfQoSProfActionNumber_Object=MibTableColumn
hpnicfQoSProfActionNumber=_HpnicfQoSProfActionNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,1,1,1,3),_HpnicfQoSProfActionNumber_Type())
hpnicfQoSProfActionNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSProfActionNumber.setStatus(_A)
_HpnicfQoSProfRowStatus_Type=RowStatus
_HpnicfQoSProfRowStatus_Object=MibTableColumn
hpnicfQoSProfRowStatus=_HpnicfQoSProfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,1,1,1,4),_HpnicfQoSProfRowStatus_Type())
hpnicfQoSProfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSProfRowStatus.setStatus(_A)
_HpnicfQoSAction_ObjectIdentity=ObjectIdentity
hpnicfQoSAction=_HpnicfQoSAction_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2))
_HpnicfQoSTrafficLimitTable_Object=MibTable
hpnicfQoSTrafficLimitTable=_HpnicfQoSTrafficLimitTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1))
if mibBuilder.loadTexts:hpnicfQoSTrafficLimitTable.setStatus(_A)
_HpnicfQoSTrafficLimitEntry_Object=MibTableRow
hpnicfQoSTrafficLimitEntry=_HpnicfQoSTrafficLimitEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1))
hpnicfQoSTrafficLimitEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpnicfQoSTrafficLimitEntry.setStatus(_A)
class _HpnicfQoSTrafLmtProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQoSTrafLmtProfIndex_Type.__name__=_C
_HpnicfQoSTrafLmtProfIndex_Object=MibTableColumn
hpnicfQoSTrafLmtProfIndex=_HpnicfQoSTrafLmtProfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,1),_HpnicfQoSTrafLmtProfIndex_Type())
hpnicfQoSTrafLmtProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtProfIndex.setStatus(_A)
class _HpnicfQoSTrafLmtActionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQoSTrafLmtActionIndex_Type.__name__=_C
_HpnicfQoSTrafLmtActionIndex_Object=MibTableColumn
hpnicfQoSTrafLmtActionIndex=_HpnicfQoSTrafLmtActionIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,2),_HpnicfQoSTrafLmtActionIndex_Type())
hpnicfQoSTrafLmtActionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtActionIndex.setStatus(_A)
_HpnicfQoSTrafLmtDirection_Type=HpnicfQoSDirection
_HpnicfQoSTrafLmtDirection_Object=MibTableColumn
hpnicfQoSTrafLmtDirection=_HpnicfQoSTrafLmtDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,3),_HpnicfQoSTrafLmtDirection_Type())
hpnicfQoSTrafLmtDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtDirection.setStatus(_A)
class _HpnicfQoSTrafLmtUserAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999))
_HpnicfQoSTrafLmtUserAclNum_Type.__name__=_C
_HpnicfQoSTrafLmtUserAclNum_Object=MibTableColumn
hpnicfQoSTrafLmtUserAclNum=_HpnicfQoSTrafLmtUserAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,4),_HpnicfQoSTrafLmtUserAclNum_Type())
hpnicfQoSTrafLmtUserAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtUserAclNum.setStatus(_A)
class _HpnicfQoSTrafLmtUserAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSTrafLmtUserAclRule_Type.__name__=_C
_HpnicfQoSTrafLmtUserAclRule_Object=MibTableColumn
hpnicfQoSTrafLmtUserAclRule=_HpnicfQoSTrafLmtUserAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,5),_HpnicfQoSTrafLmtUserAclRule_Type())
hpnicfQoSTrafLmtUserAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtUserAclRule.setStatus(_A)
class _HpnicfQoSTrafLmtIpAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_HpnicfQoSTrafLmtIpAclNum_Type.__name__=_C
_HpnicfQoSTrafLmtIpAclNum_Object=MibTableColumn
hpnicfQoSTrafLmtIpAclNum=_HpnicfQoSTrafLmtIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,6),_HpnicfQoSTrafLmtIpAclNum_Type())
hpnicfQoSTrafLmtIpAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtIpAclNum.setStatus(_A)
class _HpnicfQoSTrafLmtIpAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSTrafLmtIpAclRule_Type.__name__=_C
_HpnicfQoSTrafLmtIpAclRule_Object=MibTableColumn
hpnicfQoSTrafLmtIpAclRule=_HpnicfQoSTrafLmtIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,7),_HpnicfQoSTrafLmtIpAclRule_Type())
hpnicfQoSTrafLmtIpAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtIpAclRule.setStatus(_A)
class _HpnicfQoSTrafLmtLinkAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999))
_HpnicfQoSTrafLmtLinkAclNum_Type.__name__=_C
_HpnicfQoSTrafLmtLinkAclNum_Object=MibTableColumn
hpnicfQoSTrafLmtLinkAclNum=_HpnicfQoSTrafLmtLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,8),_HpnicfQoSTrafLmtLinkAclNum_Type())
hpnicfQoSTrafLmtLinkAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtLinkAclNum.setStatus(_A)
class _HpnicfQoSTrafLmtLinkAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSTrafLmtLinkAclRule_Type.__name__=_C
_HpnicfQoSTrafLmtLinkAclRule_Object=MibTableColumn
hpnicfQoSTrafLmtLinkAclRule=_HpnicfQoSTrafLmtLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,9),_HpnicfQoSTrafLmtLinkAclRule_Type())
hpnicfQoSTrafLmtLinkAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtLinkAclRule.setStatus(_A)
class _HpnicfQoSTrafLmtTargetRateMbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_HpnicfQoSTrafLmtTargetRateMbps_Type.__name__=_C
_HpnicfQoSTrafLmtTargetRateMbps_Object=MibTableColumn
hpnicfQoSTrafLmtTargetRateMbps=_HpnicfQoSTrafLmtTargetRateMbps_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,10),_HpnicfQoSTrafLmtTargetRateMbps_Type())
hpnicfQoSTrafLmtTargetRateMbps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtTargetRateMbps.setStatus(_A)
class _HpnicfQoSTrafLmtTargetRateKbps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_HpnicfQoSTrafLmtTargetRateKbps_Type.__name__=_C
_HpnicfQoSTrafLmtTargetRateKbps_Object=MibTableColumn
hpnicfQoSTrafLmtTargetRateKbps=_HpnicfQoSTrafLmtTargetRateKbps_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,11),_HpnicfQoSTrafLmtTargetRateKbps_Type())
hpnicfQoSTrafLmtTargetRateKbps.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtTargetRateKbps.setStatus(_A)
class _HpnicfQoSTrafLmtPeakRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,8388608))
_HpnicfQoSTrafLmtPeakRate_Type.__name__=_C
_HpnicfQoSTrafLmtPeakRate_Object=MibTableColumn
hpnicfQoSTrafLmtPeakRate=_HpnicfQoSTrafLmtPeakRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,12),_HpnicfQoSTrafLmtPeakRate_Type())
hpnicfQoSTrafLmtPeakRate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtPeakRate.setStatus(_A)
class _HpnicfQoSTrafLmtCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34120000))
_HpnicfQoSTrafLmtCIR_Type.__name__=_C
_HpnicfQoSTrafLmtCIR_Object=MibTableColumn
hpnicfQoSTrafLmtCIR=_HpnicfQoSTrafLmtCIR_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,13),_HpnicfQoSTrafLmtCIR_Type())
hpnicfQoSTrafLmtCIR.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtCIR.setStatus(_A)
class _HpnicfQoSTrafLmtCBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_HpnicfQoSTrafLmtCBS_Type.__name__=_C
_HpnicfQoSTrafLmtCBS_Object=MibTableColumn
hpnicfQoSTrafLmtCBS=_HpnicfQoSTrafLmtCBS_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,14),_HpnicfQoSTrafLmtCBS_Type())
hpnicfQoSTrafLmtCBS.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtCBS.setStatus(_A)
class _HpnicfQoSTrafLmtEBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435455))
_HpnicfQoSTrafLmtEBS_Type.__name__=_C
_HpnicfQoSTrafLmtEBS_Object=MibTableColumn
hpnicfQoSTrafLmtEBS=_HpnicfQoSTrafLmtEBS_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,15),_HpnicfQoSTrafLmtEBS_Type())
hpnicfQoSTrafLmtEBS.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtEBS.setStatus(_A)
class _HpnicfQoSTrafLmtPIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34120000))
_HpnicfQoSTrafLmtPIR_Type.__name__=_C
_HpnicfQoSTrafLmtPIR_Object=MibTableColumn
hpnicfQoSTrafLmtPIR=_HpnicfQoSTrafLmtPIR_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,16),_HpnicfQoSTrafLmtPIR_Type())
hpnicfQoSTrafLmtPIR.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtPIR.setStatus(_A)
class _HpnicfQoSTrafLmtConformLocalPre_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfQoSTrafLmtConformLocalPre_Type.__name__=_C
_HpnicfQoSTrafLmtConformLocalPre_Object=MibTableColumn
hpnicfQoSTrafLmtConformLocalPre=_HpnicfQoSTrafLmtConformLocalPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,17),_HpnicfQoSTrafLmtConformLocalPre_Type())
hpnicfQoSTrafLmtConformLocalPre.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtConformLocalPre.setStatus(_A)
class _HpnicfQoSTrafLmtConformActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_H,0),('remark-cos',1),('remark-drop-priority',2),('remark-cos-drop-priority',3),('remark-policed-service',4),('remark-dscp',5)))
_HpnicfQoSTrafLmtConformActionType_Type.__name__=_C
_HpnicfQoSTrafLmtConformActionType_Object=MibTableColumn
hpnicfQoSTrafLmtConformActionType=_HpnicfQoSTrafLmtConformActionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,18),_HpnicfQoSTrafLmtConformActionType_Type())
hpnicfQoSTrafLmtConformActionType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtConformActionType.setStatus(_A)
class _HpnicfQoSTrafLmtExceedActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('forward',1),('drop',2),('remarkdscp',3),('exceed-cos',4)))
_HpnicfQoSTrafLmtExceedActionType_Type.__name__=_C
_HpnicfQoSTrafLmtExceedActionType_Object=MibTableColumn
hpnicfQoSTrafLmtExceedActionType=_HpnicfQoSTrafLmtExceedActionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,19),_HpnicfQoSTrafLmtExceedActionType_Type())
hpnicfQoSTrafLmtExceedActionType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtExceedActionType.setStatus(_A)
class _HpnicfQoSTrafLmtExceedDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfQoSTrafLmtExceedDscp_Type.__name__=_C
_HpnicfQoSTrafLmtExceedDscp_Object=MibTableColumn
hpnicfQoSTrafLmtExceedDscp=_HpnicfQoSTrafLmtExceedDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,20),_HpnicfQoSTrafLmtExceedDscp_Type())
hpnicfQoSTrafLmtExceedDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtExceedDscp.setStatus(_A)
class _HpnicfQoSTrafLmtExceedCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSTrafLmtExceedCos_Type.__name__=_C
_HpnicfQoSTrafLmtExceedCos_Object=MibTableColumn
hpnicfQoSTrafLmtExceedCos=_HpnicfQoSTrafLmtExceedCos_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,21),_HpnicfQoSTrafLmtExceedCos_Type())
hpnicfQoSTrafLmtExceedCos.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtExceedCos.setStatus(_A)
_HpnicfQoSTrafLmtRowStatus_Type=RowStatus
_HpnicfQoSTrafLmtRowStatus_Object=MibTableColumn
hpnicfQoSTrafLmtRowStatus=_HpnicfQoSTrafLmtRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,22),_HpnicfQoSTrafLmtRowStatus_Type())
hpnicfQoSTrafLmtRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtRowStatus.setStatus(_A)
class _HpnicfQoSTrafLmtConformCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSTrafLmtConformCos_Type.__name__=_C
_HpnicfQoSTrafLmtConformCos_Object=MibTableColumn
hpnicfQoSTrafLmtConformCos=_HpnicfQoSTrafLmtConformCos_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,23),_HpnicfQoSTrafLmtConformCos_Type())
hpnicfQoSTrafLmtConformCos.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtConformCos.setStatus(_A)
class _HpnicfQoSTrafLmtConformDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfQoSTrafLmtConformDscp_Type.__name__=_C
_HpnicfQoSTrafLmtConformDscp_Object=MibTableColumn
hpnicfQoSTrafLmtConformDscp=_HpnicfQoSTrafLmtConformDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,1,1,24),_HpnicfQoSTrafLmtConformDscp_Type())
hpnicfQoSTrafLmtConformDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafLmtConformDscp.setStatus(_A)
_HpnicfQoSTrafficPriorityTable_Object=MibTable
hpnicfQoSTrafficPriorityTable=_HpnicfQoSTrafficPriorityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2))
if mibBuilder.loadTexts:hpnicfQoSTrafficPriorityTable.setStatus(_A)
_HpnicfQoSTrafficPriorityEntry_Object=MibTableRow
hpnicfQoSTrafficPriorityEntry=_HpnicfQoSTrafficPriorityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1))
hpnicfQoSTrafficPriorityEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:hpnicfQoSTrafficPriorityEntry.setStatus(_A)
class _HpnicfQoSTrafPrioProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQoSTrafPrioProfIndex_Type.__name__=_C
_HpnicfQoSTrafPrioProfIndex_Object=MibTableColumn
hpnicfQoSTrafPrioProfIndex=_HpnicfQoSTrafPrioProfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,1),_HpnicfQoSTrafPrioProfIndex_Type())
hpnicfQoSTrafPrioProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioProfIndex.setStatus(_A)
class _HpnicfQoSTrafPrioActionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQoSTrafPrioActionIndex_Type.__name__=_C
_HpnicfQoSTrafPrioActionIndex_Object=MibTableColumn
hpnicfQoSTrafPrioActionIndex=_HpnicfQoSTrafPrioActionIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,2),_HpnicfQoSTrafPrioActionIndex_Type())
hpnicfQoSTrafPrioActionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioActionIndex.setStatus(_A)
_HpnicfQoSTrafPrioDirection_Type=HpnicfQoSDirection
_HpnicfQoSTrafPrioDirection_Object=MibTableColumn
hpnicfQoSTrafPrioDirection=_HpnicfQoSTrafPrioDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,3),_HpnicfQoSTrafPrioDirection_Type())
hpnicfQoSTrafPrioDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioDirection.setStatus(_A)
class _HpnicfQoSTrafPrioUserAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999))
_HpnicfQoSTrafPrioUserAclNum_Type.__name__=_C
_HpnicfQoSTrafPrioUserAclNum_Object=MibTableColumn
hpnicfQoSTrafPrioUserAclNum=_HpnicfQoSTrafPrioUserAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,4),_HpnicfQoSTrafPrioUserAclNum_Type())
hpnicfQoSTrafPrioUserAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioUserAclNum.setStatus(_A)
class _HpnicfQoSTrafPrioUserAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSTrafPrioUserAclRule_Type.__name__=_C
_HpnicfQoSTrafPrioUserAclRule_Object=MibTableColumn
hpnicfQoSTrafPrioUserAclRule=_HpnicfQoSTrafPrioUserAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,5),_HpnicfQoSTrafPrioUserAclRule_Type())
hpnicfQoSTrafPrioUserAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioUserAclRule.setStatus(_A)
class _HpnicfQoSTrafPrioIpAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_HpnicfQoSTrafPrioIpAclNum_Type.__name__=_C
_HpnicfQoSTrafPrioIpAclNum_Object=MibTableColumn
hpnicfQoSTrafPrioIpAclNum=_HpnicfQoSTrafPrioIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,6),_HpnicfQoSTrafPrioIpAclNum_Type())
hpnicfQoSTrafPrioIpAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioIpAclNum.setStatus(_A)
class _HpnicfQoSTrafPrioIpAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSTrafPrioIpAclRule_Type.__name__=_C
_HpnicfQoSTrafPrioIpAclRule_Object=MibTableColumn
hpnicfQoSTrafPrioIpAclRule=_HpnicfQoSTrafPrioIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,7),_HpnicfQoSTrafPrioIpAclRule_Type())
hpnicfQoSTrafPrioIpAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioIpAclRule.setStatus(_A)
class _HpnicfQoSTrafPrioLinkAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999))
_HpnicfQoSTrafPrioLinkAclNum_Type.__name__=_C
_HpnicfQoSTrafPrioLinkAclNum_Object=MibTableColumn
hpnicfQoSTrafPrioLinkAclNum=_HpnicfQoSTrafPrioLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,8),_HpnicfQoSTrafPrioLinkAclNum_Type())
hpnicfQoSTrafPrioLinkAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioLinkAclNum.setStatus(_A)
class _HpnicfQoSTrafPrioLinkAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSTrafPrioLinkAclRule_Type.__name__=_C
_HpnicfQoSTrafPrioLinkAclRule_Object=MibTableColumn
hpnicfQoSTrafPrioLinkAclRule=_HpnicfQoSTrafPrioLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,9),_HpnicfQoSTrafPrioLinkAclRule_Type())
hpnicfQoSTrafPrioLinkAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioLinkAclRule.setStatus(_A)
class _HpnicfQoSTrafPrioDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfQoSTrafPrioDscp_Type.__name__=_C
_HpnicfQoSTrafPrioDscp_Object=MibTableColumn
hpnicfQoSTrafPrioDscp=_HpnicfQoSTrafPrioDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,10),_HpnicfQoSTrafPrioDscp_Type())
hpnicfQoSTrafPrioDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioDscp.setStatus(_A)
class _HpnicfQoSTrafPrioIpPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSTrafPrioIpPre_Type.__name__=_C
_HpnicfQoSTrafPrioIpPre_Object=MibTableColumn
hpnicfQoSTrafPrioIpPre=_HpnicfQoSTrafPrioIpPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,11),_HpnicfQoSTrafPrioIpPre_Type())
hpnicfQoSTrafPrioIpPre.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioIpPre.setStatus(_A)
class _HpnicfQoSTrafPrioIpPreFromCos_Type(TruthValue):defaultValue=2
_HpnicfQoSTrafPrioIpPreFromCos_Type.__name__=_I
_HpnicfQoSTrafPrioIpPreFromCos_Object=MibTableColumn
hpnicfQoSTrafPrioIpPreFromCos=_HpnicfQoSTrafPrioIpPreFromCos_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,12),_HpnicfQoSTrafPrioIpPreFromCos_Type())
hpnicfQoSTrafPrioIpPreFromCos.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioIpPreFromCos.setStatus(_A)
class _HpnicfQoSTrafPrioCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSTrafPrioCos_Type.__name__=_C
_HpnicfQoSTrafPrioCos_Object=MibTableColumn
hpnicfQoSTrafPrioCos=_HpnicfQoSTrafPrioCos_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,13),_HpnicfQoSTrafPrioCos_Type())
hpnicfQoSTrafPrioCos.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioCos.setStatus(_A)
class _HpnicfQoSTrafPrioCosFromIpPre_Type(TruthValue):defaultValue=2
_HpnicfQoSTrafPrioCosFromIpPre_Type.__name__=_I
_HpnicfQoSTrafPrioCosFromIpPre_Object=MibTableColumn
hpnicfQoSTrafPrioCosFromIpPre=_HpnicfQoSTrafPrioCosFromIpPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,14),_HpnicfQoSTrafPrioCosFromIpPre_Type())
hpnicfQoSTrafPrioCosFromIpPre.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioCosFromIpPre.setStatus(_A)
class _HpnicfQoSTrafPrioLocalPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSTrafPrioLocalPre_Type.__name__=_C
_HpnicfQoSTrafPrioLocalPre_Object=MibTableColumn
hpnicfQoSTrafPrioLocalPre=_HpnicfQoSTrafPrioLocalPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,15),_HpnicfQoSTrafPrioLocalPre_Type())
hpnicfQoSTrafPrioLocalPre.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioLocalPre.setStatus(_A)
class _HpnicfQoSTrafPrioPolicedServiceType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4)));namedValues=NamedValues(*((_H,0),('trust-dscp',2),('new-dscp',3),('untrusted',4)))
_HpnicfQoSTrafPrioPolicedServiceType_Type.__name__=_C
_HpnicfQoSTrafPrioPolicedServiceType_Object=MibTableColumn
hpnicfQoSTrafPrioPolicedServiceType=_HpnicfQoSTrafPrioPolicedServiceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,16),_HpnicfQoSTrafPrioPolicedServiceType_Type())
hpnicfQoSTrafPrioPolicedServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioPolicedServiceType.setStatus(_A)
class _HpnicfQoSTrafPrioPolicedServiceDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfQoSTrafPrioPolicedServiceDscp_Type.__name__=_C
_HpnicfQoSTrafPrioPolicedServiceDscp_Object=MibTableColumn
hpnicfQoSTrafPrioPolicedServiceDscp=_HpnicfQoSTrafPrioPolicedServiceDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,17),_HpnicfQoSTrafPrioPolicedServiceDscp_Type())
hpnicfQoSTrafPrioPolicedServiceDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioPolicedServiceDscp.setStatus(_A)
class _HpnicfQoSTrafPrioPolicedServiceExp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSTrafPrioPolicedServiceExp_Type.__name__=_C
_HpnicfQoSTrafPrioPolicedServiceExp_Object=MibTableColumn
hpnicfQoSTrafPrioPolicedServiceExp=_HpnicfQoSTrafPrioPolicedServiceExp_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,18),_HpnicfQoSTrafPrioPolicedServiceExp_Type())
hpnicfQoSTrafPrioPolicedServiceExp.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioPolicedServiceExp.setStatus(_A)
class _HpnicfQoSTrafPrioPolicedServiceCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSTrafPrioPolicedServiceCos_Type.__name__=_C
_HpnicfQoSTrafPrioPolicedServiceCos_Object=MibTableColumn
hpnicfQoSTrafPrioPolicedServiceCos=_HpnicfQoSTrafPrioPolicedServiceCos_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,19),_HpnicfQoSTrafPrioPolicedServiceCos_Type())
hpnicfQoSTrafPrioPolicedServiceCos.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioPolicedServiceCos.setStatus(_A)
class _HpnicfQoSTrafPrioPolicedServiceLoaclPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSTrafPrioPolicedServiceLoaclPre_Type.__name__=_C
_HpnicfQoSTrafPrioPolicedServiceLoaclPre_Object=MibTableColumn
hpnicfQoSTrafPrioPolicedServiceLoaclPre=_HpnicfQoSTrafPrioPolicedServiceLoaclPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,20),_HpnicfQoSTrafPrioPolicedServiceLoaclPre_Type())
hpnicfQoSTrafPrioPolicedServiceLoaclPre.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioPolicedServiceLoaclPre.setStatus(_A)
class _HpnicfQoSTrafPrioPolicedServiceDropPriority_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2),ValueRangeConstraint(255,255))
_HpnicfQoSTrafPrioPolicedServiceDropPriority_Type.__name__=_C
_HpnicfQoSTrafPrioPolicedServiceDropPriority_Object=MibTableColumn
hpnicfQoSTrafPrioPolicedServiceDropPriority=_HpnicfQoSTrafPrioPolicedServiceDropPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,21),_HpnicfQoSTrafPrioPolicedServiceDropPriority_Type())
hpnicfQoSTrafPrioPolicedServiceDropPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioPolicedServiceDropPriority.setStatus(_A)
_HpnicfQoSTrafPrioRowStatus_Type=RowStatus
_HpnicfQoSTrafPrioRowStatus_Object=MibTableColumn
hpnicfQoSTrafPrioRowStatus=_HpnicfQoSTrafPrioRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,2,1,22),_HpnicfQoSTrafPrioRowStatus_Type())
hpnicfQoSTrafPrioRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafPrioRowStatus.setStatus(_A)
_HpnicfQoSTrafficFilterTable_Object=MibTable
hpnicfQoSTrafficFilterTable=_HpnicfQoSTrafficFilterTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3))
if mibBuilder.loadTexts:hpnicfQoSTrafficFilterTable.setStatus(_A)
_HpnicfQoSTrafficFilterEntry_Object=MibTableRow
hpnicfQoSTrafficFilterEntry=_HpnicfQoSTrafficFilterEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1))
hpnicfQoSTrafficFilterEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:hpnicfQoSTrafficFilterEntry.setStatus(_A)
class _HpnicfQoSTrafFilterProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQoSTrafFilterProfIndex_Type.__name__=_C
_HpnicfQoSTrafFilterProfIndex_Object=MibTableColumn
hpnicfQoSTrafFilterProfIndex=_HpnicfQoSTrafFilterProfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,1),_HpnicfQoSTrafFilterProfIndex_Type())
hpnicfQoSTrafFilterProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterProfIndex.setStatus(_A)
class _HpnicfQoSTrafFilterActionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQoSTrafFilterActionIndex_Type.__name__=_C
_HpnicfQoSTrafFilterActionIndex_Object=MibTableColumn
hpnicfQoSTrafFilterActionIndex=_HpnicfQoSTrafFilterActionIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,2),_HpnicfQoSTrafFilterActionIndex_Type())
hpnicfQoSTrafFilterActionIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterActionIndex.setStatus(_A)
_HpnicfQoSTrafFilterDirection_Type=HpnicfQoSDirection
_HpnicfQoSTrafFilterDirection_Object=MibTableColumn
hpnicfQoSTrafFilterDirection=_HpnicfQoSTrafFilterDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,3),_HpnicfQoSTrafFilterDirection_Type())
hpnicfQoSTrafFilterDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterDirection.setStatus(_A)
class _HpnicfQoSTrafFilterUserAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999))
_HpnicfQoSTrafFilterUserAclNum_Type.__name__=_C
_HpnicfQoSTrafFilterUserAclNum_Object=MibTableColumn
hpnicfQoSTrafFilterUserAclNum=_HpnicfQoSTrafFilterUserAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,4),_HpnicfQoSTrafFilterUserAclNum_Type())
hpnicfQoSTrafFilterUserAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterUserAclNum.setStatus(_A)
class _HpnicfQoSTrafFilterUserAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSTrafFilterUserAclRule_Type.__name__=_C
_HpnicfQoSTrafFilterUserAclRule_Object=MibTableColumn
hpnicfQoSTrafFilterUserAclRule=_HpnicfQoSTrafFilterUserAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,5),_HpnicfQoSTrafFilterUserAclRule_Type())
hpnicfQoSTrafFilterUserAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterUserAclRule.setStatus(_A)
class _HpnicfQoSTrafFilterIpAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999))
_HpnicfQoSTrafFilterIpAclNum_Type.__name__=_C
_HpnicfQoSTrafFilterIpAclNum_Object=MibTableColumn
hpnicfQoSTrafFilterIpAclNum=_HpnicfQoSTrafFilterIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,6),_HpnicfQoSTrafFilterIpAclNum_Type())
hpnicfQoSTrafFilterIpAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterIpAclNum.setStatus(_A)
class _HpnicfQoSTrafFilterIpAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSTrafFilterIpAclRule_Type.__name__=_C
_HpnicfQoSTrafFilterIpAclRule_Object=MibTableColumn
hpnicfQoSTrafFilterIpAclRule=_HpnicfQoSTrafFilterIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,7),_HpnicfQoSTrafFilterIpAclRule_Type())
hpnicfQoSTrafFilterIpAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterIpAclRule.setStatus(_A)
class _HpnicfQoSTrafFilterLinkAclNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999))
_HpnicfQoSTrafFilterLinkAclNum_Type.__name__=_C
_HpnicfQoSTrafFilterLinkAclNum_Object=MibTableColumn
hpnicfQoSTrafFilterLinkAclNum=_HpnicfQoSTrafFilterLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,8),_HpnicfQoSTrafFilterLinkAclNum_Type())
hpnicfQoSTrafFilterLinkAclNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterLinkAclNum.setStatus(_A)
class _HpnicfQoSTrafFilterLinkAclRule_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSTrafFilterLinkAclRule_Type.__name__=_C
_HpnicfQoSTrafFilterLinkAclRule_Object=MibTableColumn
hpnicfQoSTrafFilterLinkAclRule=_HpnicfQoSTrafFilterLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,9),_HpnicfQoSTrafFilterLinkAclRule_Type())
hpnicfQoSTrafFilterLinkAclRule.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterLinkAclRule.setStatus(_A)
_HpnicfQoSTrafFilterRowStatus_Type=RowStatus
_HpnicfQoSTrafFilterRowStatus_Object=MibTableColumn
hpnicfQoSTrafFilterRowStatus=_HpnicfQoSTrafFilterRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,2,3,1,10),_HpnicfQoSTrafFilterRowStatus_Type())
hpnicfQoSTrafFilterRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSTrafFilterRowStatus.setStatus(_A)
_HpnicfQoSProfPortMapping_ObjectIdentity=ObjectIdentity
hpnicfQoSProfPortMapping=_HpnicfQoSProfPortMapping_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3))
_HpnicfQoSProfPortMappingTable_Object=MibTable
hpnicfQoSProfPortMappingTable=_HpnicfQoSProfPortMappingTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,1))
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingTable.setStatus(_A)
_HpnicfQoSProfPortMappingEntry_Object=MibTableRow
hpnicfQoSProfPortMappingEntry=_HpnicfQoSProfPortMappingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,1,1))
hpnicfQoSProfPortMappingEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingEntry.setStatus(_A)
class _HpnicfQoSProfPortMappingIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfQoSProfPortMappingIfIndex_Type.__name__=_C
_HpnicfQoSProfPortMappingIfIndex_Object=MibTableColumn
hpnicfQoSProfPortMappingIfIndex=_HpnicfQoSProfPortMappingIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,1,1,1),_HpnicfQoSProfPortMappingIfIndex_Type())
hpnicfQoSProfPortMappingIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingIfIndex.setStatus(_A)
class _HpnicfQoSProfPortMappingProfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQoSProfPortMappingProfIndex_Type.__name__=_C
_HpnicfQoSProfPortMappingProfIndex_Object=MibTableColumn
hpnicfQoSProfPortMappingProfIndex=_HpnicfQoSProfPortMappingProfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,1,1,2),_HpnicfQoSProfPortMappingProfIndex_Type())
hpnicfQoSProfPortMappingProfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingProfIndex.setStatus(_A)
_HpnicfQoSProfPortMappingRowStatus_Type=RowStatus
_HpnicfQoSProfPortMappingRowStatus_Object=MibTableColumn
hpnicfQoSProfPortMappingRowStatus=_HpnicfQoSProfPortMappingRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,1,1,3),_HpnicfQoSProfPortMappingRowStatus_Type())
hpnicfQoSProfPortMappingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingRowStatus.setStatus(_A)
_HpnicfQoSProfPortMappingModeTable_Object=MibTable
hpnicfQoSProfPortMappingModeTable=_HpnicfQoSProfPortMappingModeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,2))
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingModeTable.setStatus(_A)
_HpnicfQoSProfPortMappingModeEntry_Object=MibTableRow
hpnicfQoSProfPortMappingModeEntry=_HpnicfQoSProfPortMappingModeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,2,1))
hpnicfQoSProfPortMappingModeEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingModeEntry.setStatus(_A)
class _HpnicfQoSProfPortMappingModeIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfQoSProfPortMappingModeIfIndex_Type.__name__=_C
_HpnicfQoSProfPortMappingModeIfIndex_Object=MibTableColumn
hpnicfQoSProfPortMappingModeIfIndex=_HpnicfQoSProfPortMappingModeIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,2,1,1),_HpnicfQoSProfPortMappingModeIfIndex_Type())
hpnicfQoSProfPortMappingModeIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingModeIfIndex.setStatus(_A)
class _HpnicfQoSProfPortMappingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('user-based',1),('port-based',2)))
_HpnicfQoSProfPortMappingMode_Type.__name__=_C
_HpnicfQoSProfPortMappingMode_Object=MibTableColumn
hpnicfQoSProfPortMappingMode=_HpnicfQoSProfPortMappingMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,2,1,2),_HpnicfQoSProfPortMappingMode_Type())
hpnicfQoSProfPortMappingMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingMode.setStatus(_A)
_HpnicfQoSProfDynPortMappingTable_Object=MibTable
hpnicfQoSProfDynPortMappingTable=_HpnicfQoSProfDynPortMappingTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,3))
if mibBuilder.loadTexts:hpnicfQoSProfDynPortMappingTable.setStatus(_A)
_HpnicfQoSProfDynPortMappingEntry_Object=MibTableRow
hpnicfQoSProfDynPortMappingEntry=_HpnicfQoSProfDynPortMappingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,3,1))
hpnicfQoSProfDynPortMappingEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:hpnicfQoSProfDynPortMappingEntry.setStatus(_A)
class _HpnicfQoSProfDynPortMappingIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfQoSProfDynPortMappingIfIndex_Type.__name__=_C
_HpnicfQoSProfDynPortMappingIfIndex_Object=MibTableColumn
hpnicfQoSProfDynPortMappingIfIndex=_HpnicfQoSProfDynPortMappingIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,3,1,1),_HpnicfQoSProfDynPortMappingIfIndex_Type())
hpnicfQoSProfDynPortMappingIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSProfDynPortMappingIfIndex.setStatus(_A)
_HpnicfQoSProfDynPortMappingUserSrcMAC_Type=MacAddress
_HpnicfQoSProfDynPortMappingUserSrcMAC_Object=MibTableColumn
hpnicfQoSProfDynPortMappingUserSrcMAC=_HpnicfQoSProfDynPortMappingUserSrcMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,3,1,2),_HpnicfQoSProfDynPortMappingUserSrcMAC_Type())
hpnicfQoSProfDynPortMappingUserSrcMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQoSProfDynPortMappingUserSrcMAC.setStatus(_A)
class _HpnicfQoSProfDynPortMappingUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfQoSProfDynPortMappingUserName_Type.__name__=_G
_HpnicfQoSProfDynPortMappingUserName_Object=MibTableColumn
hpnicfQoSProfDynPortMappingUserName=_HpnicfQoSProfDynPortMappingUserName_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,3,1,3),_HpnicfQoSProfDynPortMappingUserName_Type())
hpnicfQoSProfDynPortMappingUserName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSProfDynPortMappingUserName.setStatus(_A)
_HpnicfQoSProfDynPortMappingUserIPAddr_Type=IpAddress
_HpnicfQoSProfDynPortMappingUserIPAddr_Object=MibTableColumn
hpnicfQoSProfDynPortMappingUserIPAddr=_HpnicfQoSProfDynPortMappingUserIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,3,1,4),_HpnicfQoSProfDynPortMappingUserIPAddr_Type())
hpnicfQoSProfDynPortMappingUserIPAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSProfDynPortMappingUserIPAddr.setStatus(_A)
class _HpnicfQoSProfDynPortMappingUserVLANID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQoSProfDynPortMappingUserVLANID_Type.__name__=_C
_HpnicfQoSProfDynPortMappingUserVLANID_Object=MibTableColumn
hpnicfQoSProfDynPortMappingUserVLANID=_HpnicfQoSProfDynPortMappingUserVLANID_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,3,1,5),_HpnicfQoSProfDynPortMappingUserVLANID_Type())
hpnicfQoSProfDynPortMappingUserVLANID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSProfDynPortMappingUserVLANID.setStatus(_A)
class _HpnicfQoSProfDynPortMappingUserProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfQoSProfDynPortMappingUserProfName_Type.__name__=_G
_HpnicfQoSProfDynPortMappingUserProfName_Object=MibTableColumn
hpnicfQoSProfDynPortMappingUserProfName=_HpnicfQoSProfDynPortMappingUserProfName_Object((1,3,6,1,4,1,11,2,14,11,15,2,17,1,3,3,1,6),_HpnicfQoSProfDynPortMappingUserProfName_Type())
hpnicfQoSProfDynPortMappingUserProfName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSProfDynPortMappingUserProfName.setStatus(_A)
_HpnicfQoSProfPortMappingTraps_ObjectIdentity=ObjectIdentity
hpnicfQoSProfPortMappingTraps=_HpnicfQoSProfPortMappingTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,17,2))
_HpnicfQoSProfMibConformance_ObjectIdentity=ObjectIdentity
hpnicfQoSProfMibConformance=_HpnicfQoSProfMibConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,17,3))
_HpnicfQoSProfMibCompliances_ObjectIdentity=ObjectIdentity
hpnicfQoSProfMibCompliances=_HpnicfQoSProfMibCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,17,3,1))
_HpnicfQoSProfMibGroups_ObjectIdentity=ObjectIdentity
hpnicfQoSProfMibGroups=_HpnicfQoSProfMibGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,17,3,2))
hpnicfQoSProfGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,17,3,2,1))
hpnicfQoSProfGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:hpnicfQoSProfGroup.setStatus(_A)
hpnicfQoSActionGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,17,3,2,2))
hpnicfQoSActionGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:hpnicfQoSActionGroup.setStatus(_A)
hpnicfQoSProfPortMappingGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,17,3,2,3))
hpnicfQoSProfPortMappingGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingGroup.setStatus(_A)
hpnicfQoSProfPortMappingError=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,17,2,1))
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingError.setStatus(_A)
hpnicfQoSProfPortMappingTrapsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,17,3,2,4))
hpnicfQoSProfPortMappingTrapsGroup.setObjects((_B,_AS))
if mibBuilder.loadTexts:hpnicfQoSProfPortMappingTrapsGroup.setStatus(_A)
hpnicfQoSProfMibCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,17,3,1,1))
hpnicfQoSProfMibCompliance.setObjects(*((_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:hpnicfQoSProfMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpnicfQoSDirection':HpnicfQoSDirection,'hpnicfQosProfile':hpnicfQosProfile,'hpnicfQoSProfObjects':hpnicfQoSProfObjects,'hpnicfQoSProf':hpnicfQoSProf,'hpnicfQoSProfTable':hpnicfQoSProfTable,'hpnicfQoSProfEntry':hpnicfQoSProfEntry,_J:hpnicfQoSProfIndex,_V:hpnicfQoSProfName,_W:hpnicfQoSProfActionNumber,_X:hpnicfQoSProfRowStatus,'hpnicfQoSAction':hpnicfQoSAction,'hpnicfQoSTrafficLimitTable':hpnicfQoSTrafficLimitTable,'hpnicfQoSTrafficLimitEntry':hpnicfQoSTrafficLimitEntry,_K:hpnicfQoSTrafLmtProfIndex,_L:hpnicfQoSTrafLmtActionIndex,_Y:hpnicfQoSTrafLmtDirection,_Z:hpnicfQoSTrafLmtUserAclNum,_a:hpnicfQoSTrafLmtUserAclRule,_b:hpnicfQoSTrafLmtIpAclNum,_c:hpnicfQoSTrafLmtIpAclRule,_d:hpnicfQoSTrafLmtLinkAclNum,_e:hpnicfQoSTrafLmtLinkAclRule,_f:hpnicfQoSTrafLmtTargetRateMbps,_g:hpnicfQoSTrafLmtTargetRateKbps,_h:hpnicfQoSTrafLmtPeakRate,_i:hpnicfQoSTrafLmtCIR,_j:hpnicfQoSTrafLmtCBS,_k:hpnicfQoSTrafLmtEBS,_l:hpnicfQoSTrafLmtPIR,_m:hpnicfQoSTrafLmtConformLocalPre,_n:hpnicfQoSTrafLmtConformActionType,_o:hpnicfQoSTrafLmtExceedActionType,_p:hpnicfQoSTrafLmtExceedDscp,_q:hpnicfQoSTrafLmtExceedCos,_r:hpnicfQoSTrafLmtRowStatus,_s:hpnicfQoSTrafLmtConformCos,_t:hpnicfQoSTrafLmtConformDscp,'hpnicfQoSTrafficPriorityTable':hpnicfQoSTrafficPriorityTable,'hpnicfQoSTrafficPriorityEntry':hpnicfQoSTrafficPriorityEntry,_M:hpnicfQoSTrafPrioProfIndex,_N:hpnicfQoSTrafPrioActionIndex,_u:hpnicfQoSTrafPrioDirection,_v:hpnicfQoSTrafPrioUserAclNum,_w:hpnicfQoSTrafPrioUserAclRule,_x:hpnicfQoSTrafPrioIpAclNum,_y:hpnicfQoSTrafPrioIpAclRule,_z:hpnicfQoSTrafPrioLinkAclNum,_A0:hpnicfQoSTrafPrioLinkAclRule,_A1:hpnicfQoSTrafPrioDscp,_A2:hpnicfQoSTrafPrioIpPre,_A3:hpnicfQoSTrafPrioIpPreFromCos,_A4:hpnicfQoSTrafPrioCos,_A5:hpnicfQoSTrafPrioCosFromIpPre,_A6:hpnicfQoSTrafPrioLocalPre,_A7:hpnicfQoSTrafPrioPolicedServiceType,_A8:hpnicfQoSTrafPrioPolicedServiceDscp,_A9:hpnicfQoSTrafPrioPolicedServiceExp,_AA:hpnicfQoSTrafPrioPolicedServiceCos,_AB:hpnicfQoSTrafPrioPolicedServiceLoaclPre,_AC:hpnicfQoSTrafPrioPolicedServiceDropPriority,_AD:hpnicfQoSTrafPrioRowStatus,'hpnicfQoSTrafficFilterTable':hpnicfQoSTrafficFilterTable,'hpnicfQoSTrafficFilterEntry':hpnicfQoSTrafficFilterEntry,_O:hpnicfQoSTrafFilterProfIndex,_P:hpnicfQoSTrafFilterActionIndex,_AE:hpnicfQoSTrafFilterDirection,_AF:hpnicfQoSTrafFilterUserAclNum,_AG:hpnicfQoSTrafFilterUserAclRule,_AH:hpnicfQoSTrafFilterIpAclNum,_AI:hpnicfQoSTrafFilterIpAclRule,_AJ:hpnicfQoSTrafFilterLinkAclNum,_AK:hpnicfQoSTrafFilterLinkAclRule,_AL:hpnicfQoSTrafFilterRowStatus,'hpnicfQoSProfPortMapping':hpnicfQoSProfPortMapping,'hpnicfQoSProfPortMappingTable':hpnicfQoSProfPortMappingTable,'hpnicfQoSProfPortMappingEntry':hpnicfQoSProfPortMappingEntry,_Q:hpnicfQoSProfPortMappingIfIndex,_R:hpnicfQoSProfPortMappingProfIndex,_AM:hpnicfQoSProfPortMappingRowStatus,'hpnicfQoSProfPortMappingModeTable':hpnicfQoSProfPortMappingModeTable,'hpnicfQoSProfPortMappingModeEntry':hpnicfQoSProfPortMappingModeEntry,_S:hpnicfQoSProfPortMappingModeIfIndex,_AN:hpnicfQoSProfPortMappingMode,'hpnicfQoSProfDynPortMappingTable':hpnicfQoSProfDynPortMappingTable,'hpnicfQoSProfDynPortMappingEntry':hpnicfQoSProfDynPortMappingEntry,_T:hpnicfQoSProfDynPortMappingIfIndex,_U:hpnicfQoSProfDynPortMappingUserSrcMAC,_AO:hpnicfQoSProfDynPortMappingUserName,_AP:hpnicfQoSProfDynPortMappingUserIPAddr,_AQ:hpnicfQoSProfDynPortMappingUserVLANID,_AR:hpnicfQoSProfDynPortMappingUserProfName,'hpnicfQoSProfPortMappingTraps':hpnicfQoSProfPortMappingTraps,_AS:hpnicfQoSProfPortMappingError,'hpnicfQoSProfMibConformance':hpnicfQoSProfMibConformance,'hpnicfQoSProfMibCompliances':hpnicfQoSProfMibCompliances,'hpnicfQoSProfMibCompliance':hpnicfQoSProfMibCompliance,'hpnicfQoSProfMibGroups':hpnicfQoSProfMibGroups,_AT:hpnicfQoSProfGroup,_AU:hpnicfQoSActionGroup,_AV:hpnicfQoSProfPortMappingGroup,_AW:hpnicfQoSProfPortMappingTrapsGroup})