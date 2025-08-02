_Ac='hpnicfWIPSDctUnassocStaRtpSensorName'
_Ab='hpnicfWIPSMalPktStatSensorName'
_Aa='hpnicfWIPSCtmDeviceMAC'
_AZ='hpnicfWIPSCtmDeviceVSD'
_AY='hpnicfWIPSDevStatChannel'
_AX='hpnicfWIPSDevStatDevMacAddress'
_AW='hpnicfWIPSDevStatSensorMacAddr'
_AV='hpnicfWIPSChlStatChannel'
_AU='hpnicfWIPSChlStatSensorMacAddr'
_AT='hpnicfWIPSTrustListMacAddress'
_AS='hpnicfWIPSIgnoreListMacAddress'
_AR='hpnicfWIPSCtmListMacAddress'
_AQ='hpnicfWIPSChannelNum'
_AP='staticAndDynamic'
_AO='hpnicfWIPSBlockListMacAddress'
_AN='hpnicfWIPSDctNetworkBSSID'
_AM='hpnicfWIPSDctStaRtpSensorName'
_AL='unassociation'
_AK='deauthentication'
_AJ='disassociation'
_AI='eapLogoff'
_AH='eapSuccess'
_AG='association'
_AF='authentication'
_AE='hpnicfWIPSDctAPRptSensorName'
_AD='hpnicfWIPSDctAPAttachStaMac'
_AC='HpnicfWIPSDevCategoryWay'
_AB='hpnicfWIPSStaticTrustVendorListVendor'
_AA='hpnicfWIPSStaticTrustOUIListOUI'
_A9='hpnicfWIPSMalPktDctPolicyName'
_A8='hpnicfWIPSCtmPolicyDevMAC'
_A7='hpnicfWIPSSigSubRulePatternID'
_A6='hpnicfWIPSSigRule2PolicySigRuleIDCfg'
_A5='hpnicfWIPSDctModeRadio'
_A4='hpnicfWIPSDctModeAPName'
_A3='hpnicfWIPSIgnoreListMAC'
_A2='hpnicfWIPSStaticTrustListMAC'
_A1='hpnicfWIPSStaticBlockListMAC'
_A0='hpnicfWIPSStaticCtmListMAC'
_z='hpnicfWIPSAtkDctPolicyName'
_y='HpnicfWIPSAPSecurityType'
_x='notequal'
_w='notinclude'
_v='hpnicfWIPSAPClaRuleName'
_u='detectOnly'
_t='middle'
_s='detectFirst'
_r='accessFirst'
_q='hpnicfWIPSSensorRadioRadioId'
_p='hpnicfWIPSRule2VsdAPClaRuleNameCfg'
_o='pskANDdot1xANDother'
_n='dot1xANDother'
_m='pskANDother'
_l='pskANDdot1x'
_k='uncategorized'
_j='external'
_i='misconfigured'
_h='hpnicfWIPSDctUnassocStaMac'
_g='hpnicfWIPSDctUnassocStaVSD'
_f='dynamic'
_e='static'
_d='hpnicfWIPSDctNetworkCfg'
_c='hpnicfWIPSDctNetworkSSID'
_b='hpnicfWIPSDctNetworkVSD'
_a='hpnicfWIPSDctStaMac'
_Z='hpnicfWIPSDctStaVSD'
_Y='hpnicfWIPSCtmPolicyName'
_X='hpnicfWIPSSigRuleName'
_W='hpnicfWIPSSigPolicyNameCfg'
_V='hpnicfWIPSSensorNameCfg'
_U='other'
_T='rogue'
_S='authorized'
_R='hpnicfWIPSDctAPBSSID'
_Q='hpnicfWIPSDctAPVSD'
_P='equal'
_O='include'
_N='hpnicfWIPSVsdNameCfg'
_M='none'
_L='second'
_K='TruthValue'
_J='Unsigned32'
_I='read-write'
_H='OctetString'
_G='not-accessible'
_F='Integer32'
_E='HPN-ICF-WIPS-MIB'
_D='Counter64'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32',_D,'Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
hpnicfWIPS=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118))
if mibBuilder.loadTexts:hpnicfWIPS.setRevisions(('2011-12-29 14:50',))
class HpnicfWIPSRadioType(TextualConvention,Unsigned32):status=_A;displayHint='d'
class HpnicfWIPSDevStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
class HpnicfWIPSDevCategoryWay(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('autoByNMS',2),('autoByDev',3)))
class HpnicfWIPSDeviceCategoryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_M,0),('authorizedAP',1),('authorizedClient',2),('misconfiguredAP',3),('rogueAP',4),('unauthorizedClient',5),('externalAP',6),('adhoc',7),('bridge',8),('misassociatedClient',9),('potentialAuthorizedAP',10),('potentialRogueAP',11),('potentialExternalAP',12),('uncategorizedAP',13),('uncategorizedClient',14)))
class HpnicfWIPSAPCategoryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('adhoc',1),(_S,2),(_T,3),(_i,4),(_j,5),('potentialAuthorized',6),('potentialRogue',7),('potentialExternal',8),(_k,9)))
class HpnicfWIPSClientCategoryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),('unauthorized',2),('misassociated',3),(_k,4),('unassociated',5)))
class HpnicfWIPSChannel(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,224))
class HpnicfWIPSEncryptMethod(TextualConvention,Unsigned32):status=_A;displayHint='d'
class HpnicfWIPSAuthMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),('psk',2),('dot1x',3),(_U,4),(_l,5),(_m,6),(_n,7),(_o,8)))
class HpnicfWIPSAPClassifyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_S,2),(_j,3),(_i,4),(_T,5)))
class HpnicfWIPSAPSecurityType(TextualConvention,Unsigned32):status=_A;displayHint='d'
_HpnicfWIPSConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfWIPSConfigGroup=_HpnicfWIPSConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118,1))
_HpnicfWIPSGlobalConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfWIPSGlobalConfigGroup=_HpnicfWIPSGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1))
_HpnicfWIPSEnable_Type=TruthValue
_HpnicfWIPSEnable_Object=MibScalar
hpnicfWIPSEnable=_HpnicfWIPSEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,1),_HpnicfWIPSEnable_Type())
hpnicfWIPSEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSEnable.setStatus(_A)
_HpnicfWIPSSensorLicenseNum_Type=Unsigned32
_HpnicfWIPSSensorLicenseNum_Object=MibScalar
hpnicfWIPSSensorLicenseNum=_HpnicfWIPSSensorLicenseNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,2),_HpnicfWIPSSensorLicenseNum_Type())
hpnicfWIPSSensorLicenseNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSSensorLicenseNum.setStatus(_A)
class _HpnicfWIPSBlocklistAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('block',1),('unblock',2)))
_HpnicfWIPSBlocklistAction_Type.__name__=_F
_HpnicfWIPSBlocklistAction_Object=MibScalar
hpnicfWIPSBlocklistAction=_HpnicfWIPSBlocklistAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,3),_HpnicfWIPSBlocklistAction_Type())
hpnicfWIPSBlocklistAction.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSBlocklistAction.setStatus(_A)
class _HpnicfWIPSAPInactiveTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_HpnicfWIPSAPInactiveTime_Type.__name__=_F
_HpnicfWIPSAPInactiveTime_Object=MibScalar
hpnicfWIPSAPInactiveTime=_HpnicfWIPSAPInactiveTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,4),_HpnicfWIPSAPInactiveTime_Type())
hpnicfWIPSAPInactiveTime.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSAPInactiveTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSAPInactiveTime.setUnits(_L)
class _HpnicfWIPSSTAInactiveTime_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,1200))
_HpnicfWIPSSTAInactiveTime_Type.__name__=_F
_HpnicfWIPSSTAInactiveTime_Object=MibScalar
hpnicfWIPSSTAInactiveTime=_HpnicfWIPSSTAInactiveTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,5),_HpnicfWIPSSTAInactiveTime_Type())
hpnicfWIPSSTAInactiveTime.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSSTAInactiveTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSSTAInactiveTime.setUnits(_L)
class _HpnicfWIPSDevAgingTime_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2592000))
_HpnicfWIPSDevAgingTime_Type.__name__=_F
_HpnicfWIPSDevAgingTime_Object=MibScalar
hpnicfWIPSDevAgingTime=_HpnicfWIPSDevAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,6),_HpnicfWIPSDevAgingTime_Type())
hpnicfWIPSDevAgingTime.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDevAgingTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSDevAgingTime.setUnits(_L)
class _HpnicfWIPSStatisticPeriod_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_HpnicfWIPSStatisticPeriod_Type.__name__=_F
_HpnicfWIPSStatisticPeriod_Object=MibScalar
hpnicfWIPSStatisticPeriod=_HpnicfWIPSStatisticPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,7),_HpnicfWIPSStatisticPeriod_Type())
hpnicfWIPSStatisticPeriod.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSStatisticPeriod.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSStatisticPeriod.setUnits(_L)
class _HpnicfWIPSReclassificationPeriod_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_HpnicfWIPSReclassificationPeriod_Type.__name__=_F
_HpnicfWIPSReclassificationPeriod_Object=MibScalar
hpnicfWIPSReclassificationPeriod=_HpnicfWIPSReclassificationPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,8),_HpnicfWIPSReclassificationPeriod_Type())
hpnicfWIPSReclassificationPeriod.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSReclassificationPeriod.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSReclassificationPeriod.setUnits(_L)
_HpnicfWIPSResetAllTrustList_Type=TruthValue
_HpnicfWIPSResetAllTrustList_Object=MibScalar
hpnicfWIPSResetAllTrustList=_HpnicfWIPSResetAllTrustList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,9),_HpnicfWIPSResetAllTrustList_Type())
hpnicfWIPSResetAllTrustList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSResetAllTrustList.setStatus(_A)
_HpnicfWIPSResetAllBlockList_Type=TruthValue
_HpnicfWIPSResetAllBlockList_Object=MibScalar
hpnicfWIPSResetAllBlockList=_HpnicfWIPSResetAllBlockList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,10),_HpnicfWIPSResetAllBlockList_Type())
hpnicfWIPSResetAllBlockList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSResetAllBlockList.setStatus(_A)
_HpnicfWIPSResetAllIgnoreList_Type=TruthValue
_HpnicfWIPSResetAllIgnoreList_Object=MibScalar
hpnicfWIPSResetAllIgnoreList=_HpnicfWIPSResetAllIgnoreList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,11),_HpnicfWIPSResetAllIgnoreList_Type())
hpnicfWIPSResetAllIgnoreList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSResetAllIgnoreList.setStatus(_A)
_HpnicfWIPSResetAllCtmList_Type=TruthValue
_HpnicfWIPSResetAllCtmList_Object=MibScalar
hpnicfWIPSResetAllCtmList=_HpnicfWIPSResetAllCtmList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,12),_HpnicfWIPSResetAllCtmList_Type())
hpnicfWIPSResetAllCtmList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSResetAllCtmList.setStatus(_A)
class _HpnicfWIPSPermitChlBitMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_HpnicfWIPSPermitChlBitMap_Type.__name__=_H
_HpnicfWIPSPermitChlBitMap_Object=MibScalar
hpnicfWIPSPermitChlBitMap=_HpnicfWIPSPermitChlBitMap_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,13),_HpnicfWIPSPermitChlBitMap_Type())
hpnicfWIPSPermitChlBitMap.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSPermitChlBitMap.setStatus(_A)
class _HpnicfWIPSDynamicTrustListAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_HpnicfWIPSDynamicTrustListAgingTime_Type.__name__=_F
_HpnicfWIPSDynamicTrustListAgingTime_Object=MibScalar
hpnicfWIPSDynamicTrustListAgingTime=_HpnicfWIPSDynamicTrustListAgingTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,14),_HpnicfWIPSDynamicTrustListAgingTime_Type())
hpnicfWIPSDynamicTrustListAgingTime.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDynamicTrustListAgingTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSDynamicTrustListAgingTime.setUnits(_L)
class _HpnicfWIPSDevUpdateTime_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_HpnicfWIPSDevUpdateTime_Type.__name__=_F
_HpnicfWIPSDevUpdateTime_Object=MibScalar
hpnicfWIPSDevUpdateTime=_HpnicfWIPSDevUpdateTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,15),_HpnicfWIPSDevUpdateTime_Type())
hpnicfWIPSDevUpdateTime.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDevUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSDevUpdateTime.setUnits(_L)
class _HpnicfWIPSADOSEnable_Type(TruthValue):defaultValue=2
_HpnicfWIPSADOSEnable_Type.__name__=_K
_HpnicfWIPSADOSEnable_Object=MibScalar
hpnicfWIPSADOSEnable=_HpnicfWIPSADOSEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,16),_HpnicfWIPSADOSEnable_Type())
hpnicfWIPSADOSEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSADOSEnable.setStatus(_A)
class _HpnicfWIPSAccessFlowScanEnable_Type(TruthValue):defaultValue=2
_HpnicfWIPSAccessFlowScanEnable_Type.__name__=_K
_HpnicfWIPSAccessFlowScanEnable_Object=MibScalar
hpnicfWIPSAccessFlowScanEnable=_HpnicfWIPSAccessFlowScanEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,1,17),_HpnicfWIPSAccessFlowScanEnable_Type())
hpnicfWIPSAccessFlowScanEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSAccessFlowScanEnable.setStatus(_A)
_HpnicfWIPSVsdConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfWIPSVsdConfigGroup=_HpnicfWIPSVsdConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2))
_HpnicfWIPSVsdTable_Object=MibTable
hpnicfWIPSVsdTable=_HpnicfWIPSVsdTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,1))
if mibBuilder.loadTexts:hpnicfWIPSVsdTable.setStatus(_A)
_HpnicfWIPSVsdEntry_Object=MibTableRow
hpnicfWIPSVsdEntry=_HpnicfWIPSVsdEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,1,1))
hpnicfWIPSVsdEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:hpnicfWIPSVsdEntry.setStatus(_A)
class _HpnicfWIPSVsdNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSVsdNameCfg_Type.__name__=_H
_HpnicfWIPSVsdNameCfg_Object=MibTableColumn
hpnicfWIPSVsdNameCfg=_HpnicfWIPSVsdNameCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,1,1,1),_HpnicfWIPSVsdNameCfg_Type())
hpnicfWIPSVsdNameCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSVsdNameCfg.setStatus(_A)
_HpnicfWIPSVsdRowStatus_Type=RowStatus
_HpnicfWIPSVsdRowStatus_Object=MibTableColumn
hpnicfWIPSVsdRowStatus=_HpnicfWIPSVsdRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,1,1,2),_HpnicfWIPSVsdRowStatus_Type())
hpnicfWIPSVsdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSVsdRowStatus.setStatus(_A)
class _HpnicfWIPSVsdAtkDctPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWIPSVsdAtkDctPolicyNameCfg_Type.__name__=_H
_HpnicfWIPSVsdAtkDctPolicyNameCfg_Object=MibTableColumn
hpnicfWIPSVsdAtkDctPolicyNameCfg=_HpnicfWIPSVsdAtkDctPolicyNameCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,1,1,3),_HpnicfWIPSVsdAtkDctPolicyNameCfg_Type())
hpnicfWIPSVsdAtkDctPolicyNameCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSVsdAtkDctPolicyNameCfg.setStatus(_A)
class _HpnicfWIPSVsdCtmPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWIPSVsdCtmPolicyNameCfg_Type.__name__=_H
_HpnicfWIPSVsdCtmPolicyNameCfg_Object=MibTableColumn
hpnicfWIPSVsdCtmPolicyNameCfg=_HpnicfWIPSVsdCtmPolicyNameCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,1,1,4),_HpnicfWIPSVsdCtmPolicyNameCfg_Type())
hpnicfWIPSVsdCtmPolicyNameCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSVsdCtmPolicyNameCfg.setStatus(_A)
class _HpnicfWIPSVsdSigPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWIPSVsdSigPolicyNameCfg_Type.__name__=_H
_HpnicfWIPSVsdSigPolicyNameCfg_Object=MibTableColumn
hpnicfWIPSVsdSigPolicyNameCfg=_HpnicfWIPSVsdSigPolicyNameCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,1,1,5),_HpnicfWIPSVsdSigPolicyNameCfg_Type())
hpnicfWIPSVsdSigPolicyNameCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSVsdSigPolicyNameCfg.setStatus(_A)
class _HpnicfWIPSVsdMalPktPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWIPSVsdMalPktPolicyNameCfg_Type.__name__=_H
_HpnicfWIPSVsdMalPktPolicyNameCfg_Object=MibTableColumn
hpnicfWIPSVsdMalPktPolicyNameCfg=_HpnicfWIPSVsdMalPktPolicyNameCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,1,1,6),_HpnicfWIPSVsdMalPktPolicyNameCfg_Type())
hpnicfWIPSVsdMalPktPolicyNameCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSVsdMalPktPolicyNameCfg.setStatus(_A)
_HpnicfWIPSRule2VsdTable_Object=MibTable
hpnicfWIPSRule2VsdTable=_HpnicfWIPSRule2VsdTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,2))
if mibBuilder.loadTexts:hpnicfWIPSRule2VsdTable.setStatus(_A)
_HpnicfWIPSRule2VsdEntry_Object=MibTableRow
hpnicfWIPSRule2VsdEntry=_HpnicfWIPSRule2VsdEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,2,1))
hpnicfWIPSRule2VsdEntry.setIndexNames((0,_E,_N),(0,_E,_p))
if mibBuilder.loadTexts:hpnicfWIPSRule2VsdEntry.setStatus(_A)
class _HpnicfWIPSRule2VsdAPClaRuleNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSRule2VsdAPClaRuleNameCfg_Type.__name__=_H
_HpnicfWIPSRule2VsdAPClaRuleNameCfg_Object=MibTableColumn
hpnicfWIPSRule2VsdAPClaRuleNameCfg=_HpnicfWIPSRule2VsdAPClaRuleNameCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,2,1,1),_HpnicfWIPSRule2VsdAPClaRuleNameCfg_Type())
hpnicfWIPSRule2VsdAPClaRuleNameCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSRule2VsdAPClaRuleNameCfg.setStatus(_A)
_HpnicfWIPSRule2VsdRowStatus_Type=RowStatus
_HpnicfWIPSRule2VsdRowStatus_Object=MibTableColumn
hpnicfWIPSRule2VsdRowStatus=_HpnicfWIPSRule2VsdRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,2,1,2),_HpnicfWIPSRule2VsdRowStatus_Type())
hpnicfWIPSRule2VsdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSRule2VsdRowStatus.setStatus(_A)
class _HpnicfWIPSRule2VsdPrecedence_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfWIPSRule2VsdPrecedence_Type.__name__=_F
_HpnicfWIPSRule2VsdPrecedence_Object=MibTableColumn
hpnicfWIPSRule2VsdPrecedence=_HpnicfWIPSRule2VsdPrecedence_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,2,1,3),_HpnicfWIPSRule2VsdPrecedence_Type())
hpnicfWIPSRule2VsdPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSRule2VsdPrecedence.setStatus(_A)
_HpnicfWIPSSensor2VsdTable_Object=MibTable
hpnicfWIPSSensor2VsdTable=_HpnicfWIPSSensor2VsdTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,3))
if mibBuilder.loadTexts:hpnicfWIPSSensor2VsdTable.setStatus(_A)
_HpnicfWIPSSensor2VsdEntry_Object=MibTableRow
hpnicfWIPSSensor2VsdEntry=_HpnicfWIPSSensor2VsdEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,3,1))
hpnicfWIPSSensor2VsdEntry.setIndexNames((0,_E,_N),(0,_E,_V))
if mibBuilder.loadTexts:hpnicfWIPSSensor2VsdEntry.setStatus(_A)
class _HpnicfWIPSSensorNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfWIPSSensorNameCfg_Type.__name__=_H
_HpnicfWIPSSensorNameCfg_Object=MibTableColumn
hpnicfWIPSSensorNameCfg=_HpnicfWIPSSensorNameCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,3,1,1),_HpnicfWIPSSensorNameCfg_Type())
hpnicfWIPSSensorNameCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSSensorNameCfg.setStatus(_A)
_HpnicfWIPSSensor2VsdRowStatus_Type=RowStatus
_HpnicfWIPSSensor2VsdRowStatus_Object=MibTableColumn
hpnicfWIPSSensor2VsdRowStatus=_HpnicfWIPSSensor2VsdRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,3,1,2),_HpnicfWIPSSensor2VsdRowStatus_Type())
hpnicfWIPSSensor2VsdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSensor2VsdRowStatus.setStatus(_A)
class _HpnicfWIPSSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('idle',2)))
_HpnicfWIPSSensorState_Type.__name__=_F
_HpnicfWIPSSensorState_Object=MibTableColumn
hpnicfWIPSSensorState=_HpnicfWIPSSensorState_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,3,1,3),_HpnicfWIPSSensorState_Type())
hpnicfWIPSSensorState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSensorState.setStatus(_A)
_HpnicfWIPSSensorRadioTable_Object=MibTable
hpnicfWIPSSensorRadioTable=_HpnicfWIPSSensorRadioTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,4))
if mibBuilder.loadTexts:hpnicfWIPSSensorRadioTable.setStatus(_A)
_HpnicfWIPSSensorRadioEntry_Object=MibTableRow
hpnicfWIPSSensorRadioEntry=_HpnicfWIPSSensorRadioEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,4,1))
hpnicfWIPSSensorRadioEntry.setIndexNames((0,_E,_N),(0,_E,_V),(0,_E,_q))
if mibBuilder.loadTexts:hpnicfWIPSSensorRadioEntry.setStatus(_A)
class _HpnicfWIPSSensorRadioRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HpnicfWIPSSensorRadioRadioId_Type.__name__=_F
_HpnicfWIPSSensorRadioRadioId_Object=MibTableColumn
hpnicfWIPSSensorRadioRadioId=_HpnicfWIPSSensorRadioRadioId_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,4,1,1),_HpnicfWIPSSensorRadioRadioId_Type())
hpnicfWIPSSensorRadioRadioId.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSSensorRadioRadioId.setStatus(_A)
class _HpnicfWIPSSensorRadioScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3),(_u,4)))
_HpnicfWIPSSensorRadioScanMode_Type.__name__=_F
_HpnicfWIPSSensorRadioScanMode_Object=MibTableColumn
hpnicfWIPSSensorRadioScanMode=_HpnicfWIPSSensorRadioScanMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,2,4,1,2),_HpnicfWIPSSensorRadioScanMode_Type())
hpnicfWIPSSensorRadioScanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSSensorRadioScanMode.setStatus(_A)
_HpnicfWIPSAPClaRuleTable_Object=MibTable
hpnicfWIPSAPClaRuleTable=_HpnicfWIPSAPClaRuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3))
if mibBuilder.loadTexts:hpnicfWIPSAPClaRuleTable.setStatus(_A)
_HpnicfWIPSAPClaRuleEntry_Object=MibTableRow
hpnicfWIPSAPClaRuleEntry=_HpnicfWIPSAPClaRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1))
hpnicfWIPSAPClaRuleEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:hpnicfWIPSAPClaRuleEntry.setStatus(_A)
class _HpnicfWIPSAPClaRuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSAPClaRuleName_Type.__name__=_H
_HpnicfWIPSAPClaRuleName_Object=MibTableColumn
hpnicfWIPSAPClaRuleName=_HpnicfWIPSAPClaRuleName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,1),_HpnicfWIPSAPClaRuleName_Type())
hpnicfWIPSAPClaRuleName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSAPClaRuleName.setStatus(_A)
_HpnicfWIPSAPClaRowStatus_Type=RowStatus
_HpnicfWIPSAPClaRowStatus_Object=MibTableColumn
hpnicfWIPSAPClaRowStatus=_HpnicfWIPSAPClaRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,2),_HpnicfWIPSAPClaRowStatus_Type())
hpnicfWIPSAPClaRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAPClaRowStatus.setStatus(_A)
class _HpnicfWIPSAPClaSeverityLevel_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSAPClaSeverityLevel_Type.__name__=_J
_HpnicfWIPSAPClaSeverityLevel_Object=MibTableColumn
hpnicfWIPSAPClaSeverityLevel=_HpnicfWIPSAPClaSeverityLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,3),_HpnicfWIPSAPClaSeverityLevel_Type())
hpnicfWIPSAPClaSeverityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAPClaSeverityLevel.setStatus(_A)
class _HpnicfWIPSAPClaRuleMatchAll_Type(TruthValue):defaultValue=2
_HpnicfWIPSAPClaRuleMatchAll_Type.__name__=_K
_HpnicfWIPSAPClaRuleMatchAll_Object=MibTableColumn
hpnicfWIPSAPClaRuleMatchAll=_HpnicfWIPSAPClaRuleMatchAll_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,4),_HpnicfWIPSAPClaRuleMatchAll_Type())
hpnicfWIPSAPClaRuleMatchAll.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAPClaRuleMatchAll.setStatus(_A)
_HpnicfWIPSAPClaType_Type=HpnicfWIPSAPClassifyType
_HpnicfWIPSAPClaType_Object=MibTableColumn
hpnicfWIPSAPClaType=_HpnicfWIPSAPClaType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,5),_HpnicfWIPSAPClaType_Type())
hpnicfWIPSAPClaType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAPClaType.setStatus(_A)
class _HpnicfWIPSAPClaSubRuleSSIDOperator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_w,2),(_P,3),(_x,4)))
_HpnicfWIPSAPClaSubRuleSSIDOperator_Type.__name__=_F
_HpnicfWIPSAPClaSubRuleSSIDOperator_Object=MibTableColumn
hpnicfWIPSAPClaSubRuleSSIDOperator=_HpnicfWIPSAPClaSubRuleSSIDOperator_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,6),_HpnicfWIPSAPClaSubRuleSSIDOperator_Type())
hpnicfWIPSAPClaSubRuleSSIDOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAPClaSubRuleSSIDOperator.setStatus(_A)
class _HpnicfWIPSAPClaSubRuleSSIDCase_Type(TruthValue):defaultValue=2
_HpnicfWIPSAPClaSubRuleSSIDCase_Type.__name__=_K
_HpnicfWIPSAPClaSubRuleSSIDCase_Object=MibTableColumn
hpnicfWIPSAPClaSubRuleSSIDCase=_HpnicfWIPSAPClaSubRuleSSIDCase_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,7),_HpnicfWIPSAPClaSubRuleSSIDCase_Type())
hpnicfWIPSAPClaSubRuleSSIDCase.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAPClaSubRuleSSIDCase.setStatus(_A)
class _HpnicfWIPSAPClaSubRuleSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWIPSAPClaSubRuleSSID_Type.__name__=_H
_HpnicfWIPSAPClaSubRuleSSID_Object=MibTableColumn
hpnicfWIPSAPClaSubRuleSSID=_HpnicfWIPSAPClaSubRuleSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,8),_HpnicfWIPSAPClaSubRuleSSID_Type())
hpnicfWIPSAPClaSubRuleSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAPClaSubRuleSSID.setStatus(_A)
class _HpnicfWIPSSecurityType_Type(HpnicfWIPSAPSecurityType):defaultValue=4294967295
_HpnicfWIPSSecurityType_Type.__name__=_y
_HpnicfWIPSSecurityType_Object=MibTableColumn
hpnicfWIPSSecurityType=_HpnicfWIPSSecurityType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,9),_HpnicfWIPSSecurityType_Type())
hpnicfWIPSSecurityType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSecurityType.setStatus(_A)
class _HpnicfWIPSSecurityTypeMatch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_O,2)))
_HpnicfWIPSSecurityTypeMatch_Type.__name__=_F
_HpnicfWIPSSecurityTypeMatch_Object=MibTableColumn
hpnicfWIPSSecurityTypeMatch=_HpnicfWIPSSecurityTypeMatch_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,10),_HpnicfWIPSSecurityTypeMatch_Type())
hpnicfWIPSSecurityTypeMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSecurityTypeMatch.setStatus(_A)
class _HpnicfWIPSAPAuthType_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_M,1),('psk',2),('dot1x',3),(_U,4),('undo',5),(_l,6),(_m,7),(_n,8),(_o,9),('noneANDpsk',10),('noneANDdot1x',11),('noneANDother',12),('noneANDpskANDdot1x',13),('noneANDpskANDother',14),('noneANDdot1xANDother',15),('noneANDpskANDdot1xANDother',16)))
_HpnicfWIPSAPAuthType_Type.__name__=_F
_HpnicfWIPSAPAuthType_Object=MibTableColumn
hpnicfWIPSAPAuthType=_HpnicfWIPSAPAuthType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,11),_HpnicfWIPSAPAuthType_Type())
hpnicfWIPSAPAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAPAuthType.setStatus(_A)
class _HpnicfWIPSMaxRSSIValue_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSMaxRSSIValue_Type.__name__=_J
_HpnicfWIPSMaxRSSIValue_Object=MibTableColumn
hpnicfWIPSMaxRSSIValue=_HpnicfWIPSMaxRSSIValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,12),_HpnicfWIPSMaxRSSIValue_Type())
hpnicfWIPSMaxRSSIValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMaxRSSIValue.setStatus(_A)
class _HpnicfWIPSMinRSSIValue_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSMinRSSIValue_Type.__name__=_J
_HpnicfWIPSMinRSSIValue_Object=MibTableColumn
hpnicfWIPSMinRSSIValue=_HpnicfWIPSMinRSSIValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,13),_HpnicfWIPSMinRSSIValue_Type())
hpnicfWIPSMinRSSIValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMinRSSIValue.setStatus(_A)
class _HpnicfWIPSMaxDuration_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSMaxDuration_Type.__name__=_J
_HpnicfWIPSMaxDuration_Object=MibTableColumn
hpnicfWIPSMaxDuration=_HpnicfWIPSMaxDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,14),_HpnicfWIPSMaxDuration_Type())
hpnicfWIPSMaxDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMaxDuration.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSMaxDuration.setUnits(_L)
class _HpnicfWIPSMinDuration_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSMinDuration_Type.__name__=_J
_HpnicfWIPSMinDuration_Object=MibTableColumn
hpnicfWIPSMinDuration=_HpnicfWIPSMinDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,15),_HpnicfWIPSMinDuration_Type())
hpnicfWIPSMinDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMinDuration.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSMinDuration.setUnits(_L)
class _HpnicfWIPSMaxAPNum_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSMaxAPNum_Type.__name__=_J
_HpnicfWIPSMaxAPNum_Object=MibTableColumn
hpnicfWIPSMaxAPNum=_HpnicfWIPSMaxAPNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,16),_HpnicfWIPSMaxAPNum_Type())
hpnicfWIPSMaxAPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMaxAPNum.setStatus(_A)
class _HpnicfWIPSMinAPNum_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSMinAPNum_Type.__name__=_J
_HpnicfWIPSMinAPNum_Object=MibTableColumn
hpnicfWIPSMinAPNum=_HpnicfWIPSMinAPNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,17),_HpnicfWIPSMinAPNum_Type())
hpnicfWIPSMinAPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMinAPNum.setStatus(_A)
class _HpnicfWIPSMaxClientNum_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSMaxClientNum_Type.__name__=_J
_HpnicfWIPSMaxClientNum_Object=MibTableColumn
hpnicfWIPSMaxClientNum=_HpnicfWIPSMaxClientNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,18),_HpnicfWIPSMaxClientNum_Type())
hpnicfWIPSMaxClientNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMaxClientNum.setStatus(_A)
class _HpnicfWIPSMinClientNum_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSMinClientNum_Type.__name__=_J
_HpnicfWIPSMinClientNum_Object=MibTableColumn
hpnicfWIPSMinClientNum=_HpnicfWIPSMinClientNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,19),_HpnicfWIPSMinClientNum_Type())
hpnicfWIPSMinClientNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMinClientNum.setStatus(_A)
class _HpnicfWIPSOUIInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_HpnicfWIPSOUIInfo_Type.__name__=_H
_HpnicfWIPSOUIInfo_Object=MibTableColumn
hpnicfWIPSOUIInfo=_HpnicfWIPSOUIInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,20),_HpnicfWIPSOUIInfo_Type())
hpnicfWIPSOUIInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSOUIInfo.setStatus(_A)
class _HpnicfWIPSVendorInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfWIPSVendorInfo_Type.__name__=_H
_HpnicfWIPSVendorInfo_Object=MibTableColumn
hpnicfWIPSVendorInfo=_HpnicfWIPSVendorInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,21),_HpnicfWIPSVendorInfo_Type())
hpnicfWIPSVendorInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSVendorInfo.setStatus(_A)
class _HpnicfWIPSAPAuthTypeMatch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_O,2)))
_HpnicfWIPSAPAuthTypeMatch_Type.__name__=_F
_HpnicfWIPSAPAuthTypeMatch_Object=MibTableColumn
hpnicfWIPSAPAuthTypeMatch=_HpnicfWIPSAPAuthTypeMatch_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,3,1,22),_HpnicfWIPSAPAuthTypeMatch_Type())
hpnicfWIPSAPAuthTypeMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAPAuthTypeMatch.setStatus(_A)
_HpnicfWIPSAtkDctPolicyCfgGroup_ObjectIdentity=ObjectIdentity
hpnicfWIPSAtkDctPolicyCfgGroup=_HpnicfWIPSAtkDctPolicyCfgGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4))
class _HpnicfWIPSAtkDctPolicyCfgSupportSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_HpnicfWIPSAtkDctPolicyCfgSupportSet_Type.__name__=_H
_HpnicfWIPSAtkDctPolicyCfgSupportSet_Object=MibScalar
hpnicfWIPSAtkDctPolicyCfgSupportSet=_HpnicfWIPSAtkDctPolicyCfgSupportSet_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,1),_HpnicfWIPSAtkDctPolicyCfgSupportSet_Type())
hpnicfWIPSAtkDctPolicyCfgSupportSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyCfgSupportSet.setStatus(_A)
_HpnicfWIPSAtkDctPolicyCfgTable_Object=MibTable
hpnicfWIPSAtkDctPolicyCfgTable=_HpnicfWIPSAtkDctPolicyCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2))
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyCfgTable.setStatus(_A)
_HpnicfWIPSAtkDctPolicyCfgEntry_Object=MibTableRow
hpnicfWIPSAtkDctPolicyCfgEntry=_HpnicfWIPSAtkDctPolicyCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1))
hpnicfWIPSAtkDctPolicyCfgEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyCfgEntry.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSAtkDctPolicyName_Type.__name__=_H
_HpnicfWIPSAtkDctPolicyName_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyName=_HpnicfWIPSAtkDctPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,1),_HpnicfWIPSAtkDctPolicyName_Type())
hpnicfWIPSAtkDctPolicyName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyName.setStatus(_A)
_HpnicfWIPSAtkDctPolicyCfgRowStatus_Type=RowStatus
_HpnicfWIPSAtkDctPolicyCfgRowStatus_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyCfgRowStatus=_HpnicfWIPSAtkDctPolicyCfgRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,2),_HpnicfWIPSAtkDctPolicyCfgRowStatus_Type())
hpnicfWIPSAtkDctPolicyCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyCfgRowStatus.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyBitString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_HpnicfWIPSAtkDctPolicyBitString_Type.__name__=_H
_HpnicfWIPSAtkDctPolicyBitString_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyBitString=_HpnicfWIPSAtkDctPolicyBitString_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,3),_HpnicfWIPSAtkDctPolicyBitString_Type())
hpnicfWIPSAtkDctPolicyBitString.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyBitString.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyAPFloodQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyAPFloodQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyAPFloodQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyAPFloodQT=_HpnicfWIPSAtkDctPolicyAPFloodQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,4),_HpnicfWIPSAtkDctPolicyAPFloodQT_Type())
hpnicfWIPSAtkDctPolicyAPFloodQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyAPFloodQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyAPSpoofQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyAPSpoofQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyAPSpoofQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyAPSpoofQT=_HpnicfWIPSAtkDctPolicyAPSpoofQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,5),_HpnicfWIPSAtkDctPolicyAPSpoofQT_Type())
hpnicfWIPSAtkDctPolicyAPSpoofQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyAPSpoofQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyCliSpoofQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyCliSpoofQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyCliSpoofQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyCliSpoofQT=_HpnicfWIPSAtkDctPolicyCliSpoofQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,6),_HpnicfWIPSAtkDctPolicyCliSpoofQT_Type())
hpnicfWIPSAtkDctPolicyCliSpoofQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyCliSpoofQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyDosAssoQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyDosAssoQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyDosAssoQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyDosAssoQT=_HpnicfWIPSAtkDctPolicyDosAssoQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,7),_HpnicfWIPSAtkDctPolicyDosAssoQT_Type())
hpnicfWIPSAtkDctPolicyDosAssoQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyDosAssoQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyDosAuthQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyDosAuthQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyDosAuthQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyDosAuthQT=_HpnicfWIPSAtkDctPolicyDosAuthQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,8),_HpnicfWIPSAtkDctPolicyDosAuthQT_Type())
hpnicfWIPSAtkDctPolicyDosAuthQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyDosAuthQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyDosEAPOLStartQT=_HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,9),_HpnicfWIPSAtkDctPolicyDosEAPOLStartQT_Type())
hpnicfWIPSAtkDctPolicyDosEAPOLStartQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyDosEAPOLStartQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyDosReAssoQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyDosReAssoQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyDosReAssoQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyDosReAssoQT=_HpnicfWIPSAtkDctPolicyDosReAssoQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,10),_HpnicfWIPSAtkDctPolicyDosReAssoQT_Type())
hpnicfWIPSAtkDctPolicyDosReAssoQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyDosReAssoQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyWeakIVQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyWeakIVQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyWeakIVQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyWeakIVQT=_HpnicfWIPSAtkDctPolicyWeakIVQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,11),_HpnicfWIPSAtkDctPolicyWeakIVQT_Type())
hpnicfWIPSAtkDctPolicyWeakIVQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyWeakIVQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyInvalidOUIAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_T,1)))
_HpnicfWIPSAtkDctPolicyInvalidOUIAction_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyInvalidOUIAction_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyInvalidOUIAction=_HpnicfWIPSAtkDctPolicyInvalidOUIAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,12),_HpnicfWIPSAtkDctPolicyInvalidOUIAction_Type())
hpnicfWIPSAtkDctPolicyInvalidOUIAction.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyInvalidOUIAction.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyUnencryptedAuthApQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyUnencryptedAuthApQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyUnencryptedAuthApQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyUnencryptedAuthApQT=_HpnicfWIPSAtkDctPolicyUnencryptedAuthApQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,13),_HpnicfWIPSAtkDctPolicyUnencryptedAuthApQT_Type())
hpnicfWIPSAtkDctPolicyUnencryptedAuthApQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyUnencryptedAuthApQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT=_HpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,14),_HpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT_Type())
hpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyPSAttackQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyPSAttackQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyPSAttackQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyPSAttackQT=_HpnicfWIPSAtkDctPolicyPSAttackQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,15),_HpnicfWIPSAtkDctPolicyPSAttackQT_Type())
hpnicfWIPSAtkDctPolicyPSAttackQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyPSAttackQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyPSAttackMinOffPacket_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,150))
_HpnicfWIPSAtkDctPolicyPSAttackMinOffPacket_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyPSAttackMinOffPacket_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyPSAttackMinOffPacket=_HpnicfWIPSAtkDctPolicyPSAttackMinOffPacket_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,16),_HpnicfWIPSAtkDctPolicyPSAttackMinOffPacket_Type())
hpnicfWIPSAtkDctPolicyPSAttackMinOffPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyPSAttackMinOffPacket.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyPSAttackOnOffPercent_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfWIPSAtkDctPolicyPSAttackOnOffPercent_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyPSAttackOnOffPercent_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyPSAttackOnOffPercent=_HpnicfWIPSAtkDctPolicyPSAttackOnOffPercent_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,17),_HpnicfWIPSAtkDctPolicyPSAttackOnOffPercent_Type())
hpnicfWIPSAtkDctPolicyPSAttackOnOffPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyPSAttackOnOffPercent.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyApImpersonationQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSAtkDctPolicyApImpersonationQT_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyApImpersonationQT_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyApImpersonationQT=_HpnicfWIPSAtkDctPolicyApImpersonationQT_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,18),_HpnicfWIPSAtkDctPolicyApImpersonationQT_Type())
hpnicfWIPSAtkDctPolicyApImpersonationQT.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyApImpersonationQT.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold=_HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,19),_HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Type())
hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold.setStatus(_A)
class _HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,360000))
_HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Type.__name__=_F
_HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Object=MibTableColumn
hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime=_HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,20),_HpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Type())
hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime.setStatus(_A)
class _HpnicfWIPSAtkDctPolicySoftApConvertTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_HpnicfWIPSAtkDctPolicySoftApConvertTime_Type.__name__=_F
_HpnicfWIPSAtkDctPolicySoftApConvertTime_Object=MibTableColumn
hpnicfWIPSAtkDctPolicySoftApConvertTime=_HpnicfWIPSAtkDctPolicySoftApConvertTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,4,2,1,21),_HpnicfWIPSAtkDctPolicySoftApConvertTime_Type())
hpnicfWIPSAtkDctPolicySoftApConvertTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSAtkDctPolicySoftApConvertTime.setStatus(_A)
_HpnicfWIPSStaticCtmListCfgTable_Object=MibTable
hpnicfWIPSStaticCtmListCfgTable=_HpnicfWIPSStaticCtmListCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,5))
if mibBuilder.loadTexts:hpnicfWIPSStaticCtmListCfgTable.setStatus(_A)
_HpnicfWIPSStaticCtmListCfgEntry_Object=MibTableRow
hpnicfWIPSStaticCtmListCfgEntry=_HpnicfWIPSStaticCtmListCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,5,1))
hpnicfWIPSStaticCtmListCfgEntry.setIndexNames((0,_E,_A0))
if mibBuilder.loadTexts:hpnicfWIPSStaticCtmListCfgEntry.setStatus(_A)
_HpnicfWIPSStaticCtmListMAC_Type=MacAddress
_HpnicfWIPSStaticCtmListMAC_Object=MibTableColumn
hpnicfWIPSStaticCtmListMAC=_HpnicfWIPSStaticCtmListMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,5,1,1),_HpnicfWIPSStaticCtmListMAC_Type())
hpnicfWIPSStaticCtmListMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSStaticCtmListMAC.setStatus(_A)
_HpnicfWIPSStaticCtmListRowStatus_Type=RowStatus
_HpnicfWIPSStaticCtmListRowStatus_Object=MibTableColumn
hpnicfWIPSStaticCtmListRowStatus=_HpnicfWIPSStaticCtmListRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,5,1,2),_HpnicfWIPSStaticCtmListRowStatus_Type())
hpnicfWIPSStaticCtmListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSStaticCtmListRowStatus.setStatus(_A)
_HpnicfWIPSStaticBlockListCfgTable_Object=MibTable
hpnicfWIPSStaticBlockListCfgTable=_HpnicfWIPSStaticBlockListCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,6))
if mibBuilder.loadTexts:hpnicfWIPSStaticBlockListCfgTable.setStatus(_A)
_HpnicfWIPSStaticBlockListCfgEntry_Object=MibTableRow
hpnicfWIPSStaticBlockListCfgEntry=_HpnicfWIPSStaticBlockListCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,6,1))
hpnicfWIPSStaticBlockListCfgEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:hpnicfWIPSStaticBlockListCfgEntry.setStatus(_A)
_HpnicfWIPSStaticBlockListMAC_Type=MacAddress
_HpnicfWIPSStaticBlockListMAC_Object=MibTableColumn
hpnicfWIPSStaticBlockListMAC=_HpnicfWIPSStaticBlockListMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,6,1,1),_HpnicfWIPSStaticBlockListMAC_Type())
hpnicfWIPSStaticBlockListMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSStaticBlockListMAC.setStatus(_A)
_HpnicfWIPSStaticBlockListRowStatus_Type=RowStatus
_HpnicfWIPSStaticBlockListRowStatus_Object=MibTableColumn
hpnicfWIPSStaticBlockListRowStatus=_HpnicfWIPSStaticBlockListRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,6,1,2),_HpnicfWIPSStaticBlockListRowStatus_Type())
hpnicfWIPSStaticBlockListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSStaticBlockListRowStatus.setStatus(_A)
_HpnicfWIPSStaticTrustListCfgTable_Object=MibTable
hpnicfWIPSStaticTrustListCfgTable=_HpnicfWIPSStaticTrustListCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,7))
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustListCfgTable.setStatus(_A)
_HpnicfWIPSStaticTrustListCfgEntry_Object=MibTableRow
hpnicfWIPSStaticTrustListCfgEntry=_HpnicfWIPSStaticTrustListCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,7,1))
hpnicfWIPSStaticTrustListCfgEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustListCfgEntry.setStatus(_A)
_HpnicfWIPSStaticTrustListMAC_Type=MacAddress
_HpnicfWIPSStaticTrustListMAC_Object=MibTableColumn
hpnicfWIPSStaticTrustListMAC=_HpnicfWIPSStaticTrustListMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,7,1,1),_HpnicfWIPSStaticTrustListMAC_Type())
hpnicfWIPSStaticTrustListMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustListMAC.setStatus(_A)
_HpnicfWIPSStaticTrustListRowStatus_Type=RowStatus
_HpnicfWIPSStaticTrustListRowStatus_Object=MibTableColumn
hpnicfWIPSStaticTrustListRowStatus=_HpnicfWIPSStaticTrustListRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,7,1,2),_HpnicfWIPSStaticTrustListRowStatus_Type())
hpnicfWIPSStaticTrustListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustListRowStatus.setStatus(_A)
_HpnicfWIPSIgnoreListCfgTable_Object=MibTable
hpnicfWIPSIgnoreListCfgTable=_HpnicfWIPSIgnoreListCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,8))
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListCfgTable.setStatus(_A)
_HpnicfWIPSIgnoreListCfgEntry_Object=MibTableRow
hpnicfWIPSIgnoreListCfgEntry=_HpnicfWIPSIgnoreListCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,8,1))
hpnicfWIPSIgnoreListCfgEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListCfgEntry.setStatus(_A)
_HpnicfWIPSIgnoreListMAC_Type=MacAddress
_HpnicfWIPSIgnoreListMAC_Object=MibTableColumn
hpnicfWIPSIgnoreListMAC=_HpnicfWIPSIgnoreListMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,8,1,1),_HpnicfWIPSIgnoreListMAC_Type())
hpnicfWIPSIgnoreListMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListMAC.setStatus(_A)
_HpnicfWIPSIgnoreListRowStatus_Type=RowStatus
_HpnicfWIPSIgnoreListRowStatus_Object=MibTableColumn
hpnicfWIPSIgnoreListRowStatus=_HpnicfWIPSIgnoreListRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,8,1,2),_HpnicfWIPSIgnoreListRowStatus_Type())
hpnicfWIPSIgnoreListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListRowStatus.setStatus(_A)
_HpnicfWIPSDctModeTable_Object=MibTable
hpnicfWIPSDctModeTable=_HpnicfWIPSDctModeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,9))
if mibBuilder.loadTexts:hpnicfWIPSDctModeTable.setStatus(_A)
_HpnicfWIPSDctModeEntry_Object=MibTableRow
hpnicfWIPSDctModeEntry=_HpnicfWIPSDctModeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,9,1))
hpnicfWIPSDctModeEntry.setIndexNames((0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:hpnicfWIPSDctModeEntry.setStatus(_A)
class _HpnicfWIPSDctModeAPName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfWIPSDctModeAPName_Type.__name__=_H
_HpnicfWIPSDctModeAPName_Object=MibTableColumn
hpnicfWIPSDctModeAPName=_HpnicfWIPSDctModeAPName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,9,1,1),_HpnicfWIPSDctModeAPName_Type())
hpnicfWIPSDctModeAPName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctModeAPName.setStatus(_A)
class _HpnicfWIPSDctModeRadio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HpnicfWIPSDctModeRadio_Type.__name__=_F
_HpnicfWIPSDctModeRadio_Object=MibTableColumn
hpnicfWIPSDctModeRadio=_HpnicfWIPSDctModeRadio_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,9,1,2),_HpnicfWIPSDctModeRadio_Type())
hpnicfWIPSDctModeRadio.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctModeRadio.setStatus(_A)
class _HpnicfWIPSDctModeScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3),(_u,4)))
_HpnicfWIPSDctModeScanMode_Type.__name__=_F
_HpnicfWIPSDctModeScanMode_Object=MibTableColumn
hpnicfWIPSDctModeScanMode=_HpnicfWIPSDctModeScanMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,9,1,3),_HpnicfWIPSDctModeScanMode_Type())
hpnicfWIPSDctModeScanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSDctModeScanMode.setStatus(_A)
_HpnicfWIPSDctModeRowStatus_Type=RowStatus
_HpnicfWIPSDctModeRowStatus_Object=MibTableColumn
hpnicfWIPSDctModeRowStatus=_HpnicfWIPSDctModeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,9,1,4),_HpnicfWIPSDctModeRowStatus_Type())
hpnicfWIPSDctModeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSDctModeRowStatus.setStatus(_A)
_HpnicfWIPSSigConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfWIPSSigConfigGroup=_HpnicfWIPSSigConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10))
_HpnicfWIPSSigPolicyTable_Object=MibTable
hpnicfWIPSSigPolicyTable=_HpnicfWIPSSigPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,1))
if mibBuilder.loadTexts:hpnicfWIPSSigPolicyTable.setStatus(_A)
_HpnicfWIPSSigPolicyEntry_Object=MibTableRow
hpnicfWIPSSigPolicyEntry=_HpnicfWIPSSigPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,1,1))
hpnicfWIPSSigPolicyEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:hpnicfWIPSSigPolicyEntry.setStatus(_A)
class _HpnicfWIPSSigPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSSigPolicyNameCfg_Type.__name__=_H
_HpnicfWIPSSigPolicyNameCfg_Object=MibTableColumn
hpnicfWIPSSigPolicyNameCfg=_HpnicfWIPSSigPolicyNameCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,1,1,1),_HpnicfWIPSSigPolicyNameCfg_Type())
hpnicfWIPSSigPolicyNameCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSSigPolicyNameCfg.setStatus(_A)
_HpnicfWIPSSigPolicyRowStatus_Type=RowStatus
_HpnicfWIPSSigPolicyRowStatus_Object=MibTableColumn
hpnicfWIPSSigPolicyRowStatus=_HpnicfWIPSSigPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,1,1,2),_HpnicfWIPSSigPolicyRowStatus_Type())
hpnicfWIPSSigPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigPolicyRowStatus.setStatus(_A)
_HpnicfWIPSSigRule2PolicyTable_Object=MibTable
hpnicfWIPSSigRule2PolicyTable=_HpnicfWIPSSigRule2PolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,2))
if mibBuilder.loadTexts:hpnicfWIPSSigRule2PolicyTable.setStatus(_A)
_HpnicfWIPSSigRule2PolicyEntry_Object=MibTableRow
hpnicfWIPSSigRule2PolicyEntry=_HpnicfWIPSSigRule2PolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,2,1))
hpnicfWIPSSigRule2PolicyEntry.setIndexNames((0,_E,_W),(0,_E,_A6))
if mibBuilder.loadTexts:hpnicfWIPSSigRule2PolicyEntry.setStatus(_A)
class _HpnicfWIPSSigRule2PolicySigRuleIDCfg_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfWIPSSigRule2PolicySigRuleIDCfg_Type.__name__=_J
_HpnicfWIPSSigRule2PolicySigRuleIDCfg_Object=MibTableColumn
hpnicfWIPSSigRule2PolicySigRuleIDCfg=_HpnicfWIPSSigRule2PolicySigRuleIDCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,2,1,1),_HpnicfWIPSSigRule2PolicySigRuleIDCfg_Type())
hpnicfWIPSSigRule2PolicySigRuleIDCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSSigRule2PolicySigRuleIDCfg.setStatus(_A)
_HpnicfWIPSSigRule2PolicyRowStatus_Type=RowStatus
_HpnicfWIPSSigRule2PolicyRowStatus_Object=MibTableColumn
hpnicfWIPSSigRule2PolicyRowStatus=_HpnicfWIPSSigRule2PolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,2,1,2),_HpnicfWIPSSigRule2PolicyRowStatus_Type())
hpnicfWIPSSigRule2PolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRule2PolicyRowStatus.setStatus(_A)
class _HpnicfWIPSSigRule2PolicyPrecedence_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfWIPSSigRule2PolicyPrecedence_Type.__name__=_J
_HpnicfWIPSSigRule2PolicyPrecedence_Object=MibTableColumn
hpnicfWIPSSigRule2PolicyPrecedence=_HpnicfWIPSSigRule2PolicyPrecedence_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,2,1,3),_HpnicfWIPSSigRule2PolicyPrecedence_Type())
hpnicfWIPSSigRule2PolicyPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRule2PolicyPrecedence.setStatus(_A)
_HpnicfWIPSSigRuleTable_Object=MibTable
hpnicfWIPSSigRuleTable=_HpnicfWIPSSigRuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3))
if mibBuilder.loadTexts:hpnicfWIPSSigRuleTable.setStatus(_A)
_HpnicfWIPSSigRuleEntry_Object=MibTableRow
hpnicfWIPSSigRuleEntry=_HpnicfWIPSSigRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1))
hpnicfWIPSSigRuleEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:hpnicfWIPSSigRuleEntry.setStatus(_A)
class _HpnicfWIPSSigRuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSSigRuleName_Type.__name__=_H
_HpnicfWIPSSigRuleName_Object=MibTableColumn
hpnicfWIPSSigRuleName=_HpnicfWIPSSigRuleName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,1),_HpnicfWIPSSigRuleName_Type())
hpnicfWIPSSigRuleName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleName.setStatus(_A)
class _HpnicfWIPSSigRuleID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfWIPSSigRuleID_Type.__name__=_F
_HpnicfWIPSSigRuleID_Object=MibTableColumn
hpnicfWIPSSigRuleID=_HpnicfWIPSSigRuleID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,2),_HpnicfWIPSSigRuleID_Type())
hpnicfWIPSSigRuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleID.setStatus(_A)
_HpnicfWIPSSigRuleRowStatus_Type=RowStatus
_HpnicfWIPSSigRuleRowStatus_Object=MibTableColumn
hpnicfWIPSSigRuleRowStatus=_HpnicfWIPSSigRuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,3),_HpnicfWIPSSigRuleRowStatus_Type())
hpnicfWIPSSigRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleRowStatus.setStatus(_A)
_HpnicfWIPSSigSubRuleMatchAll_Type=TruthValue
_HpnicfWIPSSigSubRuleMatchAll_Object=MibTableColumn
hpnicfWIPSSigSubRuleMatchAll=_HpnicfWIPSSigSubRuleMatchAll_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,4),_HpnicfWIPSSigSubRuleMatchAll_Type())
hpnicfWIPSSigSubRuleMatchAll.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleMatchAll.setStatus(_A)
_HpnicfWIPSSigRuleDctPeriod_Type=Unsigned32
_HpnicfWIPSSigRuleDctPeriod_Object=MibTableColumn
hpnicfWIPSSigRuleDctPeriod=_HpnicfWIPSSigRuleDctPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,5),_HpnicfWIPSSigRuleDctPeriod_Type())
hpnicfWIPSSigRuleDctPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleDctPeriod.setStatus(_A)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleDctPeriod.setUnits(_L)
class _HpnicfWIPSSigRuleTrackMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('perSig',1),('perMAC',2),('both',3)))
_HpnicfWIPSSigRuleTrackMethod_Type.__name__=_F
_HpnicfWIPSSigRuleTrackMethod_Object=MibTableColumn
hpnicfWIPSSigRuleTrackMethod=_HpnicfWIPSSigRuleTrackMethod_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,6),_HpnicfWIPSSigRuleTrackMethod_Type())
hpnicfWIPSSigRuleTrackMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleTrackMethod.setStatus(_A)
_HpnicfWIPSSigRuleDctThresholdPerMAC_Type=Unsigned32
_HpnicfWIPSSigRuleDctThresholdPerMAC_Object=MibTableColumn
hpnicfWIPSSigRuleDctThresholdPerMAC=_HpnicfWIPSSigRuleDctThresholdPerMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,7),_HpnicfWIPSSigRuleDctThresholdPerMAC_Type())
hpnicfWIPSSigRuleDctThresholdPerMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleDctThresholdPerMAC.setStatus(_A)
_HpnicfWIPSSigRuleDctThresholdPerSig_Type=Unsigned32
_HpnicfWIPSSigRuleDctThresholdPerSig_Object=MibTableColumn
hpnicfWIPSSigRuleDctThresholdPerSig=_HpnicfWIPSSigRuleDctThresholdPerSig_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,8),_HpnicfWIPSSigRuleDctThresholdPerSig_Type())
hpnicfWIPSSigRuleDctThresholdPerSig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleDctThresholdPerSig.setStatus(_A)
_HpnicfWIPSSigRuleActionEvtLevel_Type=Unsigned32
_HpnicfWIPSSigRuleActionEvtLevel_Object=MibTableColumn
hpnicfWIPSSigRuleActionEvtLevel=_HpnicfWIPSSigRuleActionEvtLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,9),_HpnicfWIPSSigRuleActionEvtLevel_Type())
hpnicfWIPSSigRuleActionEvtLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleActionEvtLevel.setStatus(_A)
_HpnicfWIPSSigRuleQuietTime_Type=Unsigned32
_HpnicfWIPSSigRuleQuietTime_Object=MibTableColumn
hpnicfWIPSSigRuleQuietTime=_HpnicfWIPSSigRuleQuietTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,10),_HpnicfWIPSSigRuleQuietTime_Type())
hpnicfWIPSSigRuleQuietTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigRuleQuietTime.setStatus(_A)
class _HpnicfWIPSSigSubRuleFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('manage',0),('control',1),('data',2),('undo',3)))
_HpnicfWIPSSigSubRuleFrameType_Type.__name__=_F
_HpnicfWIPSSigSubRuleFrameType_Object=MibTableColumn
hpnicfWIPSSigSubRuleFrameType=_HpnicfWIPSSigSubRuleFrameType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,11),_HpnicfWIPSSigSubRuleFrameType_Type())
hpnicfWIPSSigSubRuleFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleFrameType.setStatus(_A)
class _HpnicfWIPSSigSubRuleFrameSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,0),('assocReq',1),('assocRes',2),('probeReq',3),('beacon',4),('disasso',5),('auth',6),('deauth',7)))
_HpnicfWIPSSigSubRuleFrameSubType_Type.__name__=_F
_HpnicfWIPSSigSubRuleFrameSubType_Object=MibTableColumn
hpnicfWIPSSigSubRuleFrameSubType=_HpnicfWIPSSigSubRuleFrameSubType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,12),_HpnicfWIPSSigSubRuleFrameSubType_Type())
hpnicfWIPSSigSubRuleFrameSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleFrameSubType.setStatus(_A)
class _HpnicfWIPSSigSubRuleMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_HpnicfWIPSSigSubRuleMac_Type.__name__=_H
_HpnicfWIPSSigSubRuleMac_Object=MibTableColumn
hpnicfWIPSSigSubRuleMac=_HpnicfWIPSSigSubRuleMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,13),_HpnicfWIPSSigSubRuleMac_Type())
hpnicfWIPSSigSubRuleMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleMac.setStatus(_A)
class _HpnicfWIPSSigSubRuleMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('source',0),('dest',1),('bssid',2)))
_HpnicfWIPSSigSubRuleMacType_Type.__name__=_F
_HpnicfWIPSSigSubRuleMacType_Object=MibTableColumn
hpnicfWIPSSigSubRuleMacType=_HpnicfWIPSSigSubRuleMacType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,14),_HpnicfWIPSSigSubRuleMacType_Type())
hpnicfWIPSSigSubRuleMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleMacType.setStatus(_A)
_HpnicfWIPSSigSubRuleSeqNumMin_Type=Unsigned32
_HpnicfWIPSSigSubRuleSeqNumMin_Object=MibTableColumn
hpnicfWIPSSigSubRuleSeqNumMin=_HpnicfWIPSSigSubRuleSeqNumMin_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,15),_HpnicfWIPSSigSubRuleSeqNumMin_Type())
hpnicfWIPSSigSubRuleSeqNumMin.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleSeqNumMin.setStatus(_A)
_HpnicfWIPSSigSubRuleSeqNumMax_Type=Unsigned32
_HpnicfWIPSSigSubRuleSeqNumMax_Object=MibTableColumn
hpnicfWIPSSigSubRuleSeqNumMax=_HpnicfWIPSSigSubRuleSeqNumMax_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,16),_HpnicfWIPSSigSubRuleSeqNumMax_Type())
hpnicfWIPSSigSubRuleSeqNumMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleSeqNumMax.setStatus(_A)
_HpnicfWIPSSigSubRuleSSIDLenMin_Type=Unsigned32
_HpnicfWIPSSigSubRuleSSIDLenMin_Object=MibTableColumn
hpnicfWIPSSigSubRuleSSIDLenMin=_HpnicfWIPSSigSubRuleSSIDLenMin_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,17),_HpnicfWIPSSigSubRuleSSIDLenMin_Type())
hpnicfWIPSSigSubRuleSSIDLenMin.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleSSIDLenMin.setStatus(_A)
_HpnicfWIPSSigSubRuleSSIDLenMax_Type=Unsigned32
_HpnicfWIPSSigSubRuleSSIDLenMax_Object=MibTableColumn
hpnicfWIPSSigSubRuleSSIDLenMax=_HpnicfWIPSSigSubRuleSSIDLenMax_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,18),_HpnicfWIPSSigSubRuleSSIDLenMax_Type())
hpnicfWIPSSigSubRuleSSIDLenMax.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleSSIDLenMax.setStatus(_A)
class _HpnicfWIPSSigSubRuleSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWIPSSigSubRuleSSID_Type.__name__=_H
_HpnicfWIPSSigSubRuleSSID_Object=MibTableColumn
hpnicfWIPSSigSubRuleSSID=_HpnicfWIPSSigSubRuleSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,19),_HpnicfWIPSSigSubRuleSSID_Type())
hpnicfWIPSSigSubRuleSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleSSID.setStatus(_A)
class _HpnicfWIPSSigSubRuleSSIDOpe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_w,2),(_P,3),(_x,4)))
_HpnicfWIPSSigSubRuleSSIDOpe_Type.__name__=_F
_HpnicfWIPSSigSubRuleSSIDOpe_Object=MibTableColumn
hpnicfWIPSSigSubRuleSSIDOpe=_HpnicfWIPSSigSubRuleSSIDOpe_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,20),_HpnicfWIPSSigSubRuleSSIDOpe_Type())
hpnicfWIPSSigSubRuleSSIDOpe.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleSSIDOpe.setStatus(_A)
class _HpnicfWIPSSigSubRuleSSIDCase_Type(TruthValue):defaultValue=2
_HpnicfWIPSSigSubRuleSSIDCase_Type.__name__=_K
_HpnicfWIPSSigSubRuleSSIDCase_Object=MibTableColumn
hpnicfWIPSSigSubRuleSSIDCase=_HpnicfWIPSSigSubRuleSSIDCase_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,3,1,21),_HpnicfWIPSSigSubRuleSSIDCase_Type())
hpnicfWIPSSigSubRuleSSIDCase.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleSSIDCase.setStatus(_A)
_HpnicfWIPSSigSubRulePatternTable_Object=MibTable
hpnicfWIPSSigSubRulePatternTable=_HpnicfWIPSSigSubRulePatternTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4))
if mibBuilder.loadTexts:hpnicfWIPSSigSubRulePatternTable.setStatus(_A)
_HpnicfWIPSSigSubRulePatternEntry_Object=MibTableRow
hpnicfWIPSSigSubRulePatternEntry=_HpnicfWIPSSigSubRulePatternEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4,1))
hpnicfWIPSSigSubRulePatternEntry.setIndexNames((0,_E,_X),(0,_E,_A7))
if mibBuilder.loadTexts:hpnicfWIPSSigSubRulePatternEntry.setStatus(_A)
class _HpnicfWIPSSigSubRulePatternID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,27))
_HpnicfWIPSSigSubRulePatternID_Type.__name__=_J
_HpnicfWIPSSigSubRulePatternID_Object=MibTableColumn
hpnicfWIPSSigSubRulePatternID=_HpnicfWIPSSigSubRulePatternID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4,1,1),_HpnicfWIPSSigSubRulePatternID_Type())
hpnicfWIPSSigSubRulePatternID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRulePatternID.setStatus(_A)
_HpnicfWIPSSigSubRuleRowStatus_Type=RowStatus
_HpnicfWIPSSigSubRuleRowStatus_Object=MibTableColumn
hpnicfWIPSSigSubRuleRowStatus=_HpnicfWIPSSigSubRuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4,1,2),_HpnicfWIPSSigSubRuleRowStatus_Type())
hpnicfWIPSSigSubRuleRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRuleRowStatus.setStatus(_A)
class _HpnicfWIPSSigSubRulePatternName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWIPSSigSubRulePatternName_Type.__name__=_H
_HpnicfWIPSSigSubRulePatternName_Object=MibTableColumn
hpnicfWIPSSigSubRulePatternName=_HpnicfWIPSSigSubRulePatternName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4,1,3),_HpnicfWIPSSigSubRulePatternName_Type())
hpnicfWIPSSigSubRulePatternName.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRulePatternName.setStatus(_A)
class _HpnicfWIPSSigSubRulePatternOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2346))
_HpnicfWIPSSigSubRulePatternOffset_Type.__name__=_F
_HpnicfWIPSSigSubRulePatternOffset_Object=MibTableColumn
hpnicfWIPSSigSubRulePatternOffset=_HpnicfWIPSSigSubRulePatternOffset_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4,1,4),_HpnicfWIPSSigSubRulePatternOffset_Type())
hpnicfWIPSSigSubRulePatternOffset.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRulePatternOffset.setStatus(_A)
class _HpnicfWIPSSigSubRulePatternMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfWIPSSigSubRulePatternMask_Type.__name__=_F
_HpnicfWIPSSigSubRulePatternMask_Object=MibTableColumn
hpnicfWIPSSigSubRulePatternMask=_HpnicfWIPSSigSubRulePatternMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4,1,5),_HpnicfWIPSSigSubRulePatternMask_Type())
hpnicfWIPSSigSubRulePatternMask.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRulePatternMask.setStatus(_A)
class _HpnicfWIPSSigSubRulePatternValueMin_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSSigSubRulePatternValueMin_Type.__name__=_J
_HpnicfWIPSSigSubRulePatternValueMin_Object=MibTableColumn
hpnicfWIPSSigSubRulePatternValueMin=_HpnicfWIPSSigSubRulePatternValueMin_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4,1,6),_HpnicfWIPSSigSubRulePatternValueMin_Type())
hpnicfWIPSSigSubRulePatternValueMin.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRulePatternValueMin.setStatus(_A)
class _HpnicfWIPSSigSubRulePatternValueMax_Type(Unsigned32):defaultValue=4294967295
_HpnicfWIPSSigSubRulePatternValueMax_Type.__name__=_J
_HpnicfWIPSSigSubRulePatternValueMax_Object=MibTableColumn
hpnicfWIPSSigSubRulePatternValueMax=_HpnicfWIPSSigSubRulePatternValueMax_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4,1,7),_HpnicfWIPSSigSubRulePatternValueMax_Type())
hpnicfWIPSSigSubRulePatternValueMax.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRulePatternValueMax.setStatus(_A)
class _HpnicfWIPSSigSubRulePatternFromPayload_Type(TruthValue):defaultValue=2
_HpnicfWIPSSigSubRulePatternFromPayload_Type.__name__=_K
_HpnicfWIPSSigSubRulePatternFromPayload_Object=MibTableColumn
hpnicfWIPSSigSubRulePatternFromPayload=_HpnicfWIPSSigSubRulePatternFromPayload_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,10,4,1,8),_HpnicfWIPSSigSubRulePatternFromPayload_Type())
hpnicfWIPSSigSubRulePatternFromPayload.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSSigSubRulePatternFromPayload.setStatus(_A)
_HpnicfWIPSCtmConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfWIPSCtmConfigGroup=_HpnicfWIPSCtmConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11))
class _HpnicfWIPSCtmPolicyCfgSupportSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_HpnicfWIPSCtmPolicyCfgSupportSet_Type.__name__=_H
_HpnicfWIPSCtmPolicyCfgSupportSet_Object=MibScalar
hpnicfWIPSCtmPolicyCfgSupportSet=_HpnicfWIPSCtmPolicyCfgSupportSet_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,1),_HpnicfWIPSCtmPolicyCfgSupportSet_Type())
hpnicfWIPSCtmPolicyCfgSupportSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyCfgSupportSet.setStatus(_A)
_HpnicfWIPSCtmPolicyTable_Object=MibTable
hpnicfWIPSCtmPolicyTable=_HpnicfWIPSCtmPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2))
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyTable.setStatus(_A)
_HpnicfWIPSCtmPolicyEntry_Object=MibTableRow
hpnicfWIPSCtmPolicyEntry=_HpnicfWIPSCtmPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1))
hpnicfWIPSCtmPolicyEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyEntry.setStatus(_A)
class _HpnicfWIPSCtmPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSCtmPolicyName_Type.__name__=_H
_HpnicfWIPSCtmPolicyName_Object=MibTableColumn
hpnicfWIPSCtmPolicyName=_HpnicfWIPSCtmPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,1),_HpnicfWIPSCtmPolicyName_Type())
hpnicfWIPSCtmPolicyName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyName.setStatus(_A)
_HpnicfWIPSCtmPolicyCfgRowStatus_Type=RowStatus
_HpnicfWIPSCtmPolicyCfgRowStatus_Object=MibTableColumn
hpnicfWIPSCtmPolicyCfgRowStatus=_HpnicfWIPSCtmPolicyCfgRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,2),_HpnicfWIPSCtmPolicyCfgRowStatus_Type())
hpnicfWIPSCtmPolicyCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyCfgRowStatus.setStatus(_A)
class _HpnicfWIPSCtmPolicyBitString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_HpnicfWIPSCtmPolicyBitString_Type.__name__=_H
_HpnicfWIPSCtmPolicyBitString_Object=MibTableColumn
hpnicfWIPSCtmPolicyBitString=_HpnicfWIPSCtmPolicyBitString_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,3),_HpnicfWIPSCtmPolicyBitString_Type())
hpnicfWIPSCtmPolicyBitString.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyBitString.setStatus(_A)
class _HpnicfWIPSCtmPolicyFixedChl_Type(TruthValue):defaultValue=2
_HpnicfWIPSCtmPolicyFixedChl_Type.__name__=_K
_HpnicfWIPSCtmPolicyFixedChl_Object=MibTableColumn
hpnicfWIPSCtmPolicyFixedChl=_HpnicfWIPSCtmPolicyFixedChl_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,4),_HpnicfWIPSCtmPolicyFixedChl_Type())
hpnicfWIPSCtmPolicyFixedChl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyFixedChl.setStatus(_A)
class _HpnicfWIPSCtmPolicyRogueAPPre_Type(Unsigned32):defaultValue=9
_HpnicfWIPSCtmPolicyRogueAPPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyRogueAPPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyRogueAPPre=_HpnicfWIPSCtmPolicyRogueAPPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,5),_HpnicfWIPSCtmPolicyRogueAPPre_Type())
hpnicfWIPSCtmPolicyRogueAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyRogueAPPre.setStatus(_A)
class _HpnicfWIPSCtmPolicyPtRogueAPPre_Type(Unsigned32):defaultValue=7
_HpnicfWIPSCtmPolicyPtRogueAPPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyPtRogueAPPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyPtRogueAPPre=_HpnicfWIPSCtmPolicyPtRogueAPPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,6),_HpnicfWIPSCtmPolicyPtRogueAPPre_Type())
hpnicfWIPSCtmPolicyPtRogueAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyPtRogueAPPre.setStatus(_A)
class _HpnicfWIPSCtmPolicyMisconfAPPre_Type(Unsigned32):defaultValue=3
_HpnicfWIPSCtmPolicyMisconfAPPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyMisconfAPPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyMisconfAPPre=_HpnicfWIPSCtmPolicyMisconfAPPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,7),_HpnicfWIPSCtmPolicyMisconfAPPre_Type())
hpnicfWIPSCtmPolicyMisconfAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyMisconfAPPre.setStatus(_A)
class _HpnicfWIPSCtmPolicyExternalAPPre_Type(Unsigned32):defaultValue=1
_HpnicfWIPSCtmPolicyExternalAPPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyExternalAPPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyExternalAPPre=_HpnicfWIPSCtmPolicyExternalAPPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,8),_HpnicfWIPSCtmPolicyExternalAPPre_Type())
hpnicfWIPSCtmPolicyExternalAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyExternalAPPre.setStatus(_A)
class _HpnicfWIPSCtmPolicyPtExternalAPPre_Type(Unsigned32):defaultValue=2
_HpnicfWIPSCtmPolicyPtExternalAPPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyPtExternalAPPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyPtExternalAPPre=_HpnicfWIPSCtmPolicyPtExternalAPPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,9),_HpnicfWIPSCtmPolicyPtExternalAPPre_Type())
hpnicfWIPSCtmPolicyPtExternalAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyPtExternalAPPre.setStatus(_A)
class _HpnicfWIPSCtmPolicyUncateAPPre_Type(Unsigned32):defaultValue=5
_HpnicfWIPSCtmPolicyUncateAPPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyUncateAPPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyUncateAPPre=_HpnicfWIPSCtmPolicyUncateAPPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,10),_HpnicfWIPSCtmPolicyUncateAPPre_Type())
hpnicfWIPSCtmPolicyUncateAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyUncateAPPre.setStatus(_A)
class _HpnicfWIPSCtmPolicyPtAuthAPPre_Type(Unsigned32):defaultValue=0
_HpnicfWIPSCtmPolicyPtAuthAPPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyPtAuthAPPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyPtAuthAPPre=_HpnicfWIPSCtmPolicyPtAuthAPPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,11),_HpnicfWIPSCtmPolicyPtAuthAPPre_Type())
hpnicfWIPSCtmPolicyPtAuthAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyPtAuthAPPre.setStatus(_A)
class _HpnicfWIPSCtmPolicyMisassoStaPre_Type(Unsigned32):defaultValue=6
_HpnicfWIPSCtmPolicyMisassoStaPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyMisassoStaPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyMisassoStaPre=_HpnicfWIPSCtmPolicyMisassoStaPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,12),_HpnicfWIPSCtmPolicyMisassoStaPre_Type())
hpnicfWIPSCtmPolicyMisassoStaPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyMisassoStaPre.setStatus(_A)
class _HpnicfWIPSCtmPolicyUncateStaPre_Type(Unsigned32):defaultValue=4
_HpnicfWIPSCtmPolicyUncateStaPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyUncateStaPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyUncateStaPre=_HpnicfWIPSCtmPolicyUncateStaPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,13),_HpnicfWIPSCtmPolicyUncateStaPre_Type())
hpnicfWIPSCtmPolicyUncateStaPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyUncateStaPre.setStatus(_A)
class _HpnicfWIPSCtmPolicyUnauthStaPre_Type(Unsigned32):defaultValue=8
_HpnicfWIPSCtmPolicyUnauthStaPre_Type.__name__=_J
_HpnicfWIPSCtmPolicyUnauthStaPre_Object=MibTableColumn
hpnicfWIPSCtmPolicyUnauthStaPre=_HpnicfWIPSCtmPolicyUnauthStaPre_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,2,1,14),_HpnicfWIPSCtmPolicyUnauthStaPre_Type())
hpnicfWIPSCtmPolicyUnauthStaPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyUnauthStaPre.setStatus(_A)
_HpnicfWIPSCtmPolicyDevListTable_Object=MibTable
hpnicfWIPSCtmPolicyDevListTable=_HpnicfWIPSCtmPolicyDevListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,3))
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyDevListTable.setStatus(_A)
_HpnicfWIPSCtmPolicyDevListEntry_Object=MibTableRow
hpnicfWIPSCtmPolicyDevListEntry=_HpnicfWIPSCtmPolicyDevListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,3,1))
hpnicfWIPSCtmPolicyDevListEntry.setIndexNames((0,_E,_Y),(0,_E,_A8))
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyDevListEntry.setStatus(_A)
_HpnicfWIPSCtmPolicyDevMAC_Type=MacAddress
_HpnicfWIPSCtmPolicyDevMAC_Object=MibTableColumn
hpnicfWIPSCtmPolicyDevMAC=_HpnicfWIPSCtmPolicyDevMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,3,1,1),_HpnicfWIPSCtmPolicyDevMAC_Type())
hpnicfWIPSCtmPolicyDevMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyDevMAC.setStatus(_A)
_HpnicfWIPSCtmPolicyDevRowStatus_Type=RowStatus
_HpnicfWIPSCtmPolicyDevRowStatus_Object=MibTableColumn
hpnicfWIPSCtmPolicyDevRowStatus=_HpnicfWIPSCtmPolicyDevRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,11,3,1,2),_HpnicfWIPSCtmPolicyDevRowStatus_Type())
hpnicfWIPSCtmPolicyDevRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSCtmPolicyDevRowStatus.setStatus(_A)
_HpnicfWIPSMalPktDctConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfWIPSMalPktDctConfigGroup=_HpnicfWIPSMalPktDctConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12))
class _HpnicfWIPSMalPktDctCfgLogSupportSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_HpnicfWIPSMalPktDctCfgLogSupportSet_Type.__name__=_H
_HpnicfWIPSMalPktDctCfgLogSupportSet_Object=MibScalar
hpnicfWIPSMalPktDctCfgLogSupportSet=_HpnicfWIPSMalPktDctCfgLogSupportSet_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,1),_HpnicfWIPSMalPktDctCfgLogSupportSet_Type())
hpnicfWIPSMalPktDctCfgLogSupportSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctCfgLogSupportSet.setStatus(_A)
class _HpnicfWIPSMalPktDctCfgTrapSupportSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_HpnicfWIPSMalPktDctCfgTrapSupportSet_Type.__name__=_H
_HpnicfWIPSMalPktDctCfgTrapSupportSet_Object=MibScalar
hpnicfWIPSMalPktDctCfgTrapSupportSet=_HpnicfWIPSMalPktDctCfgTrapSupportSet_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,2),_HpnicfWIPSMalPktDctCfgTrapSupportSet_Type())
hpnicfWIPSMalPktDctCfgTrapSupportSet.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctCfgTrapSupportSet.setStatus(_A)
_HpnicfWIPSMalPktDctPolicyTable_Object=MibTable
hpnicfWIPSMalPktDctPolicyTable=_HpnicfWIPSMalPktDctPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,3))
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctPolicyTable.setStatus(_A)
_HpnicfWIPSMalPktDctPolicyEntry_Object=MibTableRow
hpnicfWIPSMalPktDctPolicyEntry=_HpnicfWIPSMalPktDctPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,3,1))
hpnicfWIPSMalPktDctPolicyEntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctPolicyEntry.setStatus(_A)
class _HpnicfWIPSMalPktDctPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSMalPktDctPolicyName_Type.__name__=_H
_HpnicfWIPSMalPktDctPolicyName_Object=MibTableColumn
hpnicfWIPSMalPktDctPolicyName=_HpnicfWIPSMalPktDctPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,3,1,1),_HpnicfWIPSMalPktDctPolicyName_Type())
hpnicfWIPSMalPktDctPolicyName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctPolicyName.setStatus(_A)
_HpnicfWIPSMalPktDctPolicyCfgRowStatus_Type=RowStatus
_HpnicfWIPSMalPktDctPolicyCfgRowStatus_Object=MibTableColumn
hpnicfWIPSMalPktDctPolicyCfgRowStatus=_HpnicfWIPSMalPktDctPolicyCfgRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,3,1,2),_HpnicfWIPSMalPktDctPolicyCfgRowStatus_Type())
hpnicfWIPSMalPktDctPolicyCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctPolicyCfgRowStatus.setStatus(_A)
class _HpnicfWIPSMalPktDctPolicyLogBitString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_HpnicfWIPSMalPktDctPolicyLogBitString_Type.__name__=_H
_HpnicfWIPSMalPktDctPolicyLogBitString_Object=MibTableColumn
hpnicfWIPSMalPktDctPolicyLogBitString=_HpnicfWIPSMalPktDctPolicyLogBitString_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,3,1,3),_HpnicfWIPSMalPktDctPolicyLogBitString_Type())
hpnicfWIPSMalPktDctPolicyLogBitString.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctPolicyLogBitString.setStatus(_A)
class _HpnicfWIPSMalPktDctPolicyTrapBitString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_HpnicfWIPSMalPktDctPolicyTrapBitString_Type.__name__=_H
_HpnicfWIPSMalPktDctPolicyTrapBitString_Object=MibTableColumn
hpnicfWIPSMalPktDctPolicyTrapBitString=_HpnicfWIPSMalPktDctPolicyTrapBitString_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,3,1,4),_HpnicfWIPSMalPktDctPolicyTrapBitString_Type())
hpnicfWIPSMalPktDctPolicyTrapBitString.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctPolicyTrapBitString.setStatus(_A)
class _HpnicfWIPSMalPktDctPolicyDurationThreshold_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_HpnicfWIPSMalPktDctPolicyDurationThreshold_Type.__name__=_F
_HpnicfWIPSMalPktDctPolicyDurationThreshold_Object=MibTableColumn
hpnicfWIPSMalPktDctPolicyDurationThreshold=_HpnicfWIPSMalPktDctPolicyDurationThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,3,1,5),_HpnicfWIPSMalPktDctPolicyDurationThreshold_Type())
hpnicfWIPSMalPktDctPolicyDurationThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctPolicyDurationThreshold.setStatus(_A)
class _HpnicfWIPSMalPktDctPolicyQuietTime_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_HpnicfWIPSMalPktDctPolicyQuietTime_Type.__name__=_F
_HpnicfWIPSMalPktDctPolicyQuietTime_Object=MibTableColumn
hpnicfWIPSMalPktDctPolicyQuietTime=_HpnicfWIPSMalPktDctPolicyQuietTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,12,3,1,6),_HpnicfWIPSMalPktDctPolicyQuietTime_Type())
hpnicfWIPSMalPktDctPolicyQuietTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSMalPktDctPolicyQuietTime.setStatus(_A)
_HpnicfWIPSStaticTrustOUIListCfgTable_Object=MibTable
hpnicfWIPSStaticTrustOUIListCfgTable=_HpnicfWIPSStaticTrustOUIListCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,13))
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustOUIListCfgTable.setStatus(_A)
_HpnicfWIPSStaticTrustOUIListCfgEntry_Object=MibTableRow
hpnicfWIPSStaticTrustOUIListCfgEntry=_HpnicfWIPSStaticTrustOUIListCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,13,1))
hpnicfWIPSStaticTrustOUIListCfgEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustOUIListCfgEntry.setStatus(_A)
class _HpnicfWIPSStaticTrustOUIListOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpnicfWIPSStaticTrustOUIListOUI_Type.__name__=_H
_HpnicfWIPSStaticTrustOUIListOUI_Object=MibTableColumn
hpnicfWIPSStaticTrustOUIListOUI=_HpnicfWIPSStaticTrustOUIListOUI_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,13,1,1),_HpnicfWIPSStaticTrustOUIListOUI_Type())
hpnicfWIPSStaticTrustOUIListOUI.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustOUIListOUI.setStatus(_A)
_HpnicfWIPSStaticTrustOUIListRowStatus_Type=RowStatus
_HpnicfWIPSStaticTrustOUIListRowStatus_Object=MibTableColumn
hpnicfWIPSStaticTrustOUIListRowStatus=_HpnicfWIPSStaticTrustOUIListRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,13,1,2),_HpnicfWIPSStaticTrustOUIListRowStatus_Type())
hpnicfWIPSStaticTrustOUIListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustOUIListRowStatus.setStatus(_A)
_HpnicfWIPSStaticTrustVendorListCfgTable_Object=MibTable
hpnicfWIPSStaticTrustVendorListCfgTable=_HpnicfWIPSStaticTrustVendorListCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,14))
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustVendorListCfgTable.setStatus(_A)
_HpnicfWIPSStaticTrustVendorListCfgEntry_Object=MibTableRow
hpnicfWIPSStaticTrustVendorListCfgEntry=_HpnicfWIPSStaticTrustVendorListCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,14,1))
hpnicfWIPSStaticTrustVendorListCfgEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustVendorListCfgEntry.setStatus(_A)
class _HpnicfWIPSStaticTrustVendorListVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfWIPSStaticTrustVendorListVendor_Type.__name__=_H
_HpnicfWIPSStaticTrustVendorListVendor_Object=MibTableColumn
hpnicfWIPSStaticTrustVendorListVendor=_HpnicfWIPSStaticTrustVendorListVendor_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,14,1,1),_HpnicfWIPSStaticTrustVendorListVendor_Type())
hpnicfWIPSStaticTrustVendorListVendor.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustVendorListVendor.setStatus(_A)
_HpnicfWIPSStaticTrustVendorListRowStatus_Type=RowStatus
_HpnicfWIPSStaticTrustVendorListRowStatus_Object=MibTableColumn
hpnicfWIPSStaticTrustVendorListRowStatus=_HpnicfWIPSStaticTrustVendorListRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,1,14,1,2),_HpnicfWIPSStaticTrustVendorListRowStatus_Type())
hpnicfWIPSStaticTrustVendorListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWIPSStaticTrustVendorListRowStatus.setStatus(_A)
_HpnicfWIPSDetectGroup_ObjectIdentity=ObjectIdentity
hpnicfWIPSDetectGroup=_HpnicfWIPSDetectGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118,2))
_HpnicfWIPSDctAPTable_Object=MibTable
hpnicfWIPSDctAPTable=_HpnicfWIPSDctAPTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1))
if mibBuilder.loadTexts:hpnicfWIPSDctAPTable.setStatus(_A)
_HpnicfWIPSDctAPEntry_Object=MibTableRow
hpnicfWIPSDctAPEntry=_HpnicfWIPSDctAPEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1))
hpnicfWIPSDctAPEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:hpnicfWIPSDctAPEntry.setStatus(_A)
class _HpnicfWIPSDctAPVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSDctAPVSD_Type.__name__=_H
_HpnicfWIPSDctAPVSD_Object=MibTableColumn
hpnicfWIPSDctAPVSD=_HpnicfWIPSDctAPVSD_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,1),_HpnicfWIPSDctAPVSD_Type())
hpnicfWIPSDctAPVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctAPVSD.setStatus(_A)
_HpnicfWIPSDctAPBSSID_Type=MacAddress
_HpnicfWIPSDctAPBSSID_Object=MibTableColumn
hpnicfWIPSDctAPBSSID=_HpnicfWIPSDctAPBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,2),_HpnicfWIPSDctAPBSSID_Type())
hpnicfWIPSDctAPBSSID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctAPBSSID.setStatus(_A)
_HpnicfWIPSDctAPRunningTime_Type=TimeTicks
_HpnicfWIPSDctAPRunningTime_Object=MibTableColumn
hpnicfWIPSDctAPRunningTime=_HpnicfWIPSDctAPRunningTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,3),_HpnicfWIPSDctAPRunningTime_Type())
hpnicfWIPSDctAPRunningTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPRunningTime.setStatus(_A)
_HpnicfWIPSDctAPRunTmLastUpdateTm_Type=TimeTicks
_HpnicfWIPSDctAPRunTmLastUpdateTm_Object=MibTableColumn
hpnicfWIPSDctAPRunTmLastUpdateTm=_HpnicfWIPSDctAPRunTmLastUpdateTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,4),_HpnicfWIPSDctAPRunTmLastUpdateTm_Type())
hpnicfWIPSDctAPRunTmLastUpdateTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPRunTmLastUpdateTm.setStatus(_A)
_HpnicfWIPSDctAPIsCountered_Type=TruthValue
_HpnicfWIPSDctAPIsCountered_Object=MibTableColumn
hpnicfWIPSDctAPIsCountered=_HpnicfWIPSDctAPIsCountered_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,5),_HpnicfWIPSDctAPIsCountered_Type())
hpnicfWIPSDctAPIsCountered.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPIsCountered.setStatus(_A)
_HpnicfWIPSDctAPWorkChannel_Type=HpnicfWIPSChannel
_HpnicfWIPSDctAPWorkChannel_Object=MibTableColumn
hpnicfWIPSDctAPWorkChannel=_HpnicfWIPSDctAPWorkChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,6),_HpnicfWIPSDctAPWorkChannel_Type())
hpnicfWIPSDctAPWorkChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPWorkChannel.setStatus(_A)
_HpnicfWIPSDctAPRadioType_Type=HpnicfWIPSRadioType
_HpnicfWIPSDctAPRadioType_Object=MibTableColumn
hpnicfWIPSDctAPRadioType=_HpnicfWIPSDctAPRadioType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,7),_HpnicfWIPSDctAPRadioType_Type())
hpnicfWIPSDctAPRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPRadioType.setStatus(_A)
_HpnicfWIPSDctAPAuthMethod_Type=HpnicfWIPSAuthMethod
_HpnicfWIPSDctAPAuthMethod_Object=MibTableColumn
hpnicfWIPSDctAPAuthMethod=_HpnicfWIPSDctAPAuthMethod_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,8),_HpnicfWIPSDctAPAuthMethod_Type())
hpnicfWIPSDctAPAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPAuthMethod.setStatus(_A)
_HpnicfWIPSDctAPEncryptMethod_Type=HpnicfWIPSEncryptMethod
_HpnicfWIPSDctAPEncryptMethod_Object=MibTableColumn
hpnicfWIPSDctAPEncryptMethod=_HpnicfWIPSDctAPEncryptMethod_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,9),_HpnicfWIPSDctAPEncryptMethod_Type())
hpnicfWIPSDctAPEncryptMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPEncryptMethod.setStatus(_A)
_HpnicfWIPSDctAPSecurity_Type=HpnicfWIPSAPSecurityType
_HpnicfWIPSDctAPSecurity_Object=MibTableColumn
hpnicfWIPSDctAPSecurity=_HpnicfWIPSDctAPSecurity_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,10),_HpnicfWIPSDctAPSecurity_Type())
hpnicfWIPSDctAPSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPSecurity.setStatus(_A)
class _HpnicfWIPSDctAPSeverityLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfWIPSDctAPSeverityLevel_Type.__name__=_J
_HpnicfWIPSDctAPSeverityLevel_Object=MibTableColumn
hpnicfWIPSDctAPSeverityLevel=_HpnicfWIPSDctAPSeverityLevel_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,11),_HpnicfWIPSDctAPSeverityLevel_Type())
hpnicfWIPSDctAPSeverityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPSeverityLevel.setStatus(_A)
_HpnicfWIPSDctAPLastDctTm_Type=TimeTicks
_HpnicfWIPSDctAPLastDctTm_Object=MibTableColumn
hpnicfWIPSDctAPLastDctTm=_HpnicfWIPSDctAPLastDctTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,12),_HpnicfWIPSDctAPLastDctTm_Type())
hpnicfWIPSDctAPLastDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPLastDctTm.setStatus(_A)
_HpnicfWIPSDctAPFirstDctTm_Type=TimeTicks
_HpnicfWIPSDctAPFirstDctTm_Object=MibTableColumn
hpnicfWIPSDctAPFirstDctTm=_HpnicfWIPSDctAPFirstDctTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,13),_HpnicfWIPSDctAPFirstDctTm_Type())
hpnicfWIPSDctAPFirstDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPFirstDctTm.setStatus(_A)
class _HpnicfWIPSDctAPAdd2BlackList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctAPAdd2BlackList_Type.__name__=_K
_HpnicfWIPSDctAPAdd2BlackList_Object=MibTableColumn
hpnicfWIPSDctAPAdd2BlackList=_HpnicfWIPSDctAPAdd2BlackList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,14),_HpnicfWIPSDctAPAdd2BlackList_Type())
hpnicfWIPSDctAPAdd2BlackList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctAPAdd2BlackList.setStatus(_A)
class _HpnicfWIPSDctAPAdd2WhiteList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctAPAdd2WhiteList_Type.__name__=_K
_HpnicfWIPSDctAPAdd2WhiteList_Object=MibTableColumn
hpnicfWIPSDctAPAdd2WhiteList=_HpnicfWIPSDctAPAdd2WhiteList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,15),_HpnicfWIPSDctAPAdd2WhiteList_Type())
hpnicfWIPSDctAPAdd2WhiteList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctAPAdd2WhiteList.setStatus(_A)
class _HpnicfWIPSDctAPAdd2IgnoreList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctAPAdd2IgnoreList_Type.__name__=_K
_HpnicfWIPSDctAPAdd2IgnoreList_Object=MibTableColumn
hpnicfWIPSDctAPAdd2IgnoreList=_HpnicfWIPSDctAPAdd2IgnoreList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,16),_HpnicfWIPSDctAPAdd2IgnoreList_Type())
hpnicfWIPSDctAPAdd2IgnoreList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctAPAdd2IgnoreList.setStatus(_A)
class _HpnicfWIPSDctAPAdd2CtmList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctAPAdd2CtmList_Type.__name__=_K
_HpnicfWIPSDctAPAdd2CtmList_Object=MibTableColumn
hpnicfWIPSDctAPAdd2CtmList=_HpnicfWIPSDctAPAdd2CtmList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,17),_HpnicfWIPSDctAPAdd2CtmList_Type())
hpnicfWIPSDctAPAdd2CtmList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctAPAdd2CtmList.setStatus(_A)
_HpnicfWIPSDctAPCategory_Type=HpnicfWIPSAPCategoryType
_HpnicfWIPSDctAPCategory_Object=MibTableColumn
hpnicfWIPSDctAPCategory=_HpnicfWIPSDctAPCategory_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,18),_HpnicfWIPSDctAPCategory_Type())
hpnicfWIPSDctAPCategory.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctAPCategory.setStatus(_A)
class _HpnicfWIPSDctAPCategoryWay_Type(HpnicfWIPSDevCategoryWay):defaultValue=3
_HpnicfWIPSDctAPCategoryWay_Type.__name__=_AC
_HpnicfWIPSDctAPCategoryWay_Object=MibTableColumn
hpnicfWIPSDctAPCategoryWay=_HpnicfWIPSDctAPCategoryWay_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,19),_HpnicfWIPSDctAPCategoryWay_Type())
hpnicfWIPSDctAPCategoryWay.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctAPCategoryWay.setStatus(_A)
_HpnicfWIPSDctAPStatus_Type=HpnicfWIPSDevStatus
_HpnicfWIPSDctAPStatus_Object=MibTableColumn
hpnicfWIPSDctAPStatus=_HpnicfWIPSDctAPStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,20),_HpnicfWIPSDctAPStatus_Type())
hpnicfWIPSDctAPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPStatus.setStatus(_A)
class _HpnicfWIPSDctAPSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfWIPSDctAPSSID_Type.__name__=_H
_HpnicfWIPSDctAPSSID_Object=MibTableColumn
hpnicfWIPSDctAPSSID=_HpnicfWIPSDctAPSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,21),_HpnicfWIPSDctAPSSID_Type())
hpnicfWIPSDctAPSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPSSID.setStatus(_A)
_HpnicfWIPSDctAPAttachStaNum_Type=Integer32
_HpnicfWIPSDctAPAttachStaNum_Object=MibTableColumn
hpnicfWIPSDctAPAttachStaNum=_HpnicfWIPSDctAPAttachStaNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,22),_HpnicfWIPSDctAPAttachStaNum_Type())
hpnicfWIPSDctAPAttachStaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPAttachStaNum.setStatus(_A)
_HpnicfWIPSDctAPRptSensorNum_Type=Integer32
_HpnicfWIPSDctAPRptSensorNum_Object=MibTableColumn
hpnicfWIPSDctAPRptSensorNum=_HpnicfWIPSDctAPRptSensorNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,23),_HpnicfWIPSDctAPRptSensorNum_Type())
hpnicfWIPSDctAPRptSensorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPRptSensorNum.setStatus(_A)
class _HpnicfWIPSDctAPVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfWIPSDctAPVendor_Type.__name__=_H
_HpnicfWIPSDctAPVendor_Object=MibTableColumn
hpnicfWIPSDctAPVendor=_HpnicfWIPSDctAPVendor_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,1,1,24),_HpnicfWIPSDctAPVendor_Type())
hpnicfWIPSDctAPVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPVendor.setStatus(_A)
_HpnicfWIPSDctAPAttachStaTable_Object=MibTable
hpnicfWIPSDctAPAttachStaTable=_HpnicfWIPSDctAPAttachStaTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,2))
if mibBuilder.loadTexts:hpnicfWIPSDctAPAttachStaTable.setStatus(_A)
_HpnicfWIPSDctAPAttachStaEntry_Object=MibTableRow
hpnicfWIPSDctAPAttachStaEntry=_HpnicfWIPSDctAPAttachStaEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,2,1))
hpnicfWIPSDctAPAttachStaEntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_AD))
if mibBuilder.loadTexts:hpnicfWIPSDctAPAttachStaEntry.setStatus(_A)
_HpnicfWIPSDctAPAttachStaMac_Type=MacAddress
_HpnicfWIPSDctAPAttachStaMac_Object=MibTableColumn
hpnicfWIPSDctAPAttachStaMac=_HpnicfWIPSDctAPAttachStaMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,2,1,1),_HpnicfWIPSDctAPAttachStaMac_Type())
hpnicfWIPSDctAPAttachStaMac.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctAPAttachStaMac.setStatus(_A)
_HpnicfWIPSDctAPAttachStaRowStatus_Type=RowStatus
_HpnicfWIPSDctAPAttachStaRowStatus_Object=MibTableColumn
hpnicfWIPSDctAPAttachStaRowStatus=_HpnicfWIPSDctAPAttachStaRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,2,1,2),_HpnicfWIPSDctAPAttachStaRowStatus_Type())
hpnicfWIPSDctAPAttachStaRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPAttachStaRowStatus.setStatus(_A)
_HpnicfWIPSDctAPRptSensorTable_Object=MibTable
hpnicfWIPSDctAPRptSensorTable=_HpnicfWIPSDctAPRptSensorTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,3))
if mibBuilder.loadTexts:hpnicfWIPSDctAPRptSensorTable.setStatus(_A)
_HpnicfWIPSDctAPRptSensorEntry_Object=MibTableRow
hpnicfWIPSDctAPRptSensorEntry=_HpnicfWIPSDctAPRptSensorEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,3,1))
hpnicfWIPSDctAPRptSensorEntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_AE))
if mibBuilder.loadTexts:hpnicfWIPSDctAPRptSensorEntry.setStatus(_A)
class _HpnicfWIPSDctAPRptSensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfWIPSDctAPRptSensorName_Type.__name__=_H
_HpnicfWIPSDctAPRptSensorName_Object=MibTableColumn
hpnicfWIPSDctAPRptSensorName=_HpnicfWIPSDctAPRptSensorName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,3,1,1),_HpnicfWIPSDctAPRptSensorName_Type())
hpnicfWIPSDctAPRptSensorName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctAPRptSensorName.setStatus(_A)
class _HpnicfWIPSDctAPRptSensorRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HpnicfWIPSDctAPRptSensorRadioId_Type.__name__=_F
_HpnicfWIPSDctAPRptSensorRadioId_Object=MibTableColumn
hpnicfWIPSDctAPRptSensorRadioId=_HpnicfWIPSDctAPRptSensorRadioId_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,3,1,2),_HpnicfWIPSDctAPRptSensorRadioId_Type())
hpnicfWIPSDctAPRptSensorRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPRptSensorRadioId.setStatus(_A)
class _HpnicfWIPSDctAPRptRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_HpnicfWIPSDctAPRptRSSI_Type.__name__=_F
_HpnicfWIPSDctAPRptRSSI_Object=MibTableColumn
hpnicfWIPSDctAPRptRSSI=_HpnicfWIPSDctAPRptRSSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,3,1,3),_HpnicfWIPSDctAPRptRSSI_Type())
hpnicfWIPSDctAPRptRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPRptRSSI.setStatus(_A)
_HpnicfWIPSDctAPLastRptTm_Type=TimeTicks
_HpnicfWIPSDctAPLastRptTm_Object=MibTableColumn
hpnicfWIPSDctAPLastRptTm=_HpnicfWIPSDctAPLastRptTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,3,1,4),_HpnicfWIPSDctAPLastRptTm_Type())
hpnicfWIPSDctAPLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctAPLastRptTm.setStatus(_A)
_HpnicfWIPSDctStaTable_Object=MibTable
hpnicfWIPSDctStaTable=_HpnicfWIPSDctStaTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4))
if mibBuilder.loadTexts:hpnicfWIPSDctStaTable.setStatus(_A)
_HpnicfWIPSDctStaEntry_Object=MibTableRow
hpnicfWIPSDctStaEntry=_HpnicfWIPSDctStaEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1))
hpnicfWIPSDctStaEntry.setIndexNames((0,_E,_Z),(0,_E,_a))
if mibBuilder.loadTexts:hpnicfWIPSDctStaEntry.setStatus(_A)
class _HpnicfWIPSDctStaVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSDctStaVSD_Type.__name__=_H
_HpnicfWIPSDctStaVSD_Object=MibTableColumn
hpnicfWIPSDctStaVSD=_HpnicfWIPSDctStaVSD_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,1),_HpnicfWIPSDctStaVSD_Type())
hpnicfWIPSDctStaVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctStaVSD.setStatus(_A)
_HpnicfWIPSDctStaMac_Type=MacAddress
_HpnicfWIPSDctStaMac_Object=MibTableColumn
hpnicfWIPSDctStaMac=_HpnicfWIPSDctStaMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,2),_HpnicfWIPSDctStaMac_Type())
hpnicfWIPSDctStaMac.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctStaMac.setStatus(_A)
_HpnicfWIPSDctStaAssocBSSID_Type=MacAddress
_HpnicfWIPSDctStaAssocBSSID_Object=MibTableColumn
hpnicfWIPSDctStaAssocBSSID=_HpnicfWIPSDctStaAssocBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,3),_HpnicfWIPSDctStaAssocBSSID_Type())
hpnicfWIPSDctStaAssocBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaAssocBSSID.setStatus(_A)
_HpnicfWIPSDctStaStatus_Type=HpnicfWIPSDevStatus
_HpnicfWIPSDctStaStatus_Object=MibTableColumn
hpnicfWIPSDctStaStatus=_HpnicfWIPSDctStaStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,4),_HpnicfWIPSDctStaStatus_Type())
hpnicfWIPSDctStaStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaStatus.setStatus(_A)
_HpnicfWIPSDctStaCategory_Type=HpnicfWIPSClientCategoryType
_HpnicfWIPSDctStaCategory_Object=MibTableColumn
hpnicfWIPSDctStaCategory=_HpnicfWIPSDctStaCategory_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,5),_HpnicfWIPSDctStaCategory_Type())
hpnicfWIPSDctStaCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaCategory.setStatus(_A)
_HpnicfWIPSDctStaRadioType_Type=HpnicfWIPSRadioType
_HpnicfWIPSDctStaRadioType_Object=MibTableColumn
hpnicfWIPSDctStaRadioType=_HpnicfWIPSDctStaRadioType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,6),_HpnicfWIPSDctStaRadioType_Type())
hpnicfWIPSDctStaRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaRadioType.setStatus(_A)
_HpnicfWIPSDctStaWorkChannel_Type=HpnicfWIPSChannel
_HpnicfWIPSDctStaWorkChannel_Object=MibTableColumn
hpnicfWIPSDctStaWorkChannel=_HpnicfWIPSDctStaWorkChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,7),_HpnicfWIPSDctStaWorkChannel_Type())
hpnicfWIPSDctStaWorkChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaWorkChannel.setStatus(_A)
_HpnicfWIPSDctStaIsCountered_Type=TruthValue
_HpnicfWIPSDctStaIsCountered_Object=MibTableColumn
hpnicfWIPSDctStaIsCountered=_HpnicfWIPSDctStaIsCountered_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,8),_HpnicfWIPSDctStaIsCountered_Type())
hpnicfWIPSDctStaIsCountered.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaIsCountered.setStatus(_A)
class _HpnicfWIPSDctStaAdd2BlackList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctStaAdd2BlackList_Type.__name__=_K
_HpnicfWIPSDctStaAdd2BlackList_Object=MibTableColumn
hpnicfWIPSDctStaAdd2BlackList=_HpnicfWIPSDctStaAdd2BlackList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,9),_HpnicfWIPSDctStaAdd2BlackList_Type())
hpnicfWIPSDctStaAdd2BlackList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctStaAdd2BlackList.setStatus(_A)
class _HpnicfWIPSDctStaAdd2WhiteList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctStaAdd2WhiteList_Type.__name__=_K
_HpnicfWIPSDctStaAdd2WhiteList_Object=MibTableColumn
hpnicfWIPSDctStaAdd2WhiteList=_HpnicfWIPSDctStaAdd2WhiteList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,10),_HpnicfWIPSDctStaAdd2WhiteList_Type())
hpnicfWIPSDctStaAdd2WhiteList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctStaAdd2WhiteList.setStatus(_A)
class _HpnicfWIPSDctStaAdd2IgnoreList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctStaAdd2IgnoreList_Type.__name__=_K
_HpnicfWIPSDctStaAdd2IgnoreList_Object=MibTableColumn
hpnicfWIPSDctStaAdd2IgnoreList=_HpnicfWIPSDctStaAdd2IgnoreList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,11),_HpnicfWIPSDctStaAdd2IgnoreList_Type())
hpnicfWIPSDctStaAdd2IgnoreList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctStaAdd2IgnoreList.setStatus(_A)
class _HpnicfWIPSDctStaAdd2CtmList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctStaAdd2CtmList_Type.__name__=_K
_HpnicfWIPSDctStaAdd2CtmList_Object=MibTableColumn
hpnicfWIPSDctStaAdd2CtmList=_HpnicfWIPSDctStaAdd2CtmList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,12),_HpnicfWIPSDctStaAdd2CtmList_Type())
hpnicfWIPSDctStaAdd2CtmList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctStaAdd2CtmList.setStatus(_A)
_HpnicfWIPSDctStaFirstDctTm_Type=TimeTicks
_HpnicfWIPSDctStaFirstDctTm_Object=MibTableColumn
hpnicfWIPSDctStaFirstDctTm=_HpnicfWIPSDctStaFirstDctTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,13),_HpnicfWIPSDctStaFirstDctTm_Type())
hpnicfWIPSDctStaFirstDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaFirstDctTm.setStatus(_A)
_HpnicfWIPSDctStaLastDctTm_Type=TimeTicks
_HpnicfWIPSDctStaLastDctTm_Object=MibTableColumn
hpnicfWIPSDctStaLastDctTm=_HpnicfWIPSDctStaLastDctTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,14),_HpnicfWIPSDctStaLastDctTm_Type())
hpnicfWIPSDctStaLastDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaLastDctTm.setStatus(_A)
_HpnicfWIPSDctStaRptSensorNum_Type=Integer32
_HpnicfWIPSDctStaRptSensorNum_Object=MibTableColumn
hpnicfWIPSDctStaRptSensorNum=_HpnicfWIPSDctStaRptSensorNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,15),_HpnicfWIPSDctStaRptSensorNum_Type())
hpnicfWIPSDctStaRptSensorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaRptSensorNum.setStatus(_A)
class _HpnicfWIPSDctStaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_AF,1),(_AG,2),(_AH,3),(_AI,4),(_AJ,5),(_AK,6),(_AL,7)))
_HpnicfWIPSDctStaState_Type.__name__=_F
_HpnicfWIPSDctStaState_Object=MibTableColumn
hpnicfWIPSDctStaState=_HpnicfWIPSDctStaState_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,16),_HpnicfWIPSDctStaState_Type())
hpnicfWIPSDctStaState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaState.setStatus(_A)
class _HpnicfWIPSDctStaVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfWIPSDctStaVendor_Type.__name__=_H
_HpnicfWIPSDctStaVendor_Object=MibTableColumn
hpnicfWIPSDctStaVendor=_HpnicfWIPSDctStaVendor_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,4,1,17),_HpnicfWIPSDctStaVendor_Type())
hpnicfWIPSDctStaVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaVendor.setStatus(_A)
_HpnicfWIPSDctStaRptSensorTable_Object=MibTable
hpnicfWIPSDctStaRptSensorTable=_HpnicfWIPSDctStaRptSensorTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,5))
if mibBuilder.loadTexts:hpnicfWIPSDctStaRptSensorTable.setStatus(_A)
_HpnicfWIPSDctStaRptSensorEntry_Object=MibTableRow
hpnicfWIPSDctStaRptSensorEntry=_HpnicfWIPSDctStaRptSensorEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,5,1))
hpnicfWIPSDctStaRptSensorEntry.setIndexNames((0,_E,_Z),(0,_E,_a),(0,_E,_AM))
if mibBuilder.loadTexts:hpnicfWIPSDctStaRptSensorEntry.setStatus(_A)
class _HpnicfWIPSDctStaRtpSensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfWIPSDctStaRtpSensorName_Type.__name__=_H
_HpnicfWIPSDctStaRtpSensorName_Object=MibTableColumn
hpnicfWIPSDctStaRtpSensorName=_HpnicfWIPSDctStaRtpSensorName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,5,1,1),_HpnicfWIPSDctStaRtpSensorName_Type())
hpnicfWIPSDctStaRtpSensorName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctStaRtpSensorName.setStatus(_A)
class _HpnicfWIPSDctStaRptSensorRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HpnicfWIPSDctStaRptSensorRadioId_Type.__name__=_F
_HpnicfWIPSDctStaRptSensorRadioId_Object=MibTableColumn
hpnicfWIPSDctStaRptSensorRadioId=_HpnicfWIPSDctStaRptSensorRadioId_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,5,1,2),_HpnicfWIPSDctStaRptSensorRadioId_Type())
hpnicfWIPSDctStaRptSensorRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaRptSensorRadioId.setStatus(_A)
_HpnicfWIPSDctStaRptRSSI_Type=Integer32
_HpnicfWIPSDctStaRptRSSI_Object=MibTableColumn
hpnicfWIPSDctStaRptRSSI=_HpnicfWIPSDctStaRptRSSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,5,1,3),_HpnicfWIPSDctStaRptRSSI_Type())
hpnicfWIPSDctStaRptRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaRptRSSI.setStatus(_A)
_HpnicfWIPSDctStaLastRptTm_Type=TimeTicks
_HpnicfWIPSDctStaLastRptTm_Object=MibTableColumn
hpnicfWIPSDctStaLastRptTm=_HpnicfWIPSDctStaLastRptTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,5,1,4),_HpnicfWIPSDctStaLastRptTm_Type())
hpnicfWIPSDctStaLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctStaLastRptTm.setStatus(_A)
_HpnicfWIPSDctSSIDTable_Object=MibTable
hpnicfWIPSDctSSIDTable=_HpnicfWIPSDctSSIDTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6))
if mibBuilder.loadTexts:hpnicfWIPSDctSSIDTable.setStatus(_A)
_HpnicfWIPSDctSSIDEntry_Object=MibTableRow
hpnicfWIPSDctSSIDEntry=_HpnicfWIPSDctSSIDEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6,1))
hpnicfWIPSDctSSIDEntry.setIndexNames((0,_E,_b),(0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:hpnicfWIPSDctSSIDEntry.setStatus(_A)
class _HpnicfWIPSDctNetworkVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSDctNetworkVSD_Type.__name__=_H
_HpnicfWIPSDctNetworkVSD_Object=MibTableColumn
hpnicfWIPSDctNetworkVSD=_HpnicfWIPSDctNetworkVSD_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6,1,1),_HpnicfWIPSDctNetworkVSD_Type())
hpnicfWIPSDctNetworkVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkVSD.setStatus(_A)
class _HpnicfWIPSDctNetworkSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSDctNetworkSSID_Type.__name__=_H
_HpnicfWIPSDctNetworkSSID_Object=MibTableColumn
hpnicfWIPSDctNetworkSSID=_HpnicfWIPSDctNetworkSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6,1,2),_HpnicfWIPSDctNetworkSSID_Type())
hpnicfWIPSDctNetworkSSID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkSSID.setStatus(_A)
_HpnicfWIPSDctNetworkCfg_Type=Unsigned32
_HpnicfWIPSDctNetworkCfg_Object=MibTableColumn
hpnicfWIPSDctNetworkCfg=_HpnicfWIPSDctNetworkCfg_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6,1,3),_HpnicfWIPSDctNetworkCfg_Type())
hpnicfWIPSDctNetworkCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkCfg.setStatus(_A)
_HpnicfWIPSDctNetworkFirstRptTm_Type=TimeTicks
_HpnicfWIPSDctNetworkFirstRptTm_Object=MibTableColumn
hpnicfWIPSDctNetworkFirstRptTm=_HpnicfWIPSDctNetworkFirstRptTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6,1,4),_HpnicfWIPSDctNetworkFirstRptTm_Type())
hpnicfWIPSDctNetworkFirstRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkFirstRptTm.setStatus(_A)
_HpnicfWIPSDctNetworkLastRptTm_Type=TimeTicks
_HpnicfWIPSDctNetworkLastRptTm_Object=MibTableColumn
hpnicfWIPSDctNetworkLastRptTm=_HpnicfWIPSDctNetworkLastRptTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6,1,5),_HpnicfWIPSDctNetworkLastRptTm_Type())
hpnicfWIPSDctNetworkLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkLastRptTm.setStatus(_A)
_HpnicfWIPSDctNetworkStatus_Type=HpnicfWIPSDevStatus
_HpnicfWIPSDctNetworkStatus_Object=MibTableColumn
hpnicfWIPSDctNetworkStatus=_HpnicfWIPSDctNetworkStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6,1,6),_HpnicfWIPSDctNetworkStatus_Type())
hpnicfWIPSDctNetworkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkStatus.setStatus(_A)
class _HpnicfWIPSDctNetworkSSIDHide_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctNetworkSSIDHide_Type.__name__=_K
_HpnicfWIPSDctNetworkSSIDHide_Object=MibTableColumn
hpnicfWIPSDctNetworkSSIDHide=_HpnicfWIPSDctNetworkSSIDHide_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6,1,7),_HpnicfWIPSDctNetworkSSIDHide_Type())
hpnicfWIPSDctNetworkSSIDHide.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkSSIDHide.setStatus(_A)
_HpnicfWIPSDctNetworkBSSNum_Type=Integer32
_HpnicfWIPSDctNetworkBSSNum_Object=MibTableColumn
hpnicfWIPSDctNetworkBSSNum=_HpnicfWIPSDctNetworkBSSNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,6,1,8),_HpnicfWIPSDctNetworkBSSNum_Type())
hpnicfWIPSDctNetworkBSSNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkBSSNum.setStatus(_A)
_HpnicfWIPSDctSSIDBSSTable_Object=MibTable
hpnicfWIPSDctSSIDBSSTable=_HpnicfWIPSDctSSIDBSSTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,7))
if mibBuilder.loadTexts:hpnicfWIPSDctSSIDBSSTable.setStatus(_A)
_HpnicfWIPSDctSSIDBSSEntry_Object=MibTableRow
hpnicfWIPSDctSSIDBSSEntry=_HpnicfWIPSDctSSIDBSSEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,7,1))
hpnicfWIPSDctSSIDBSSEntry.setIndexNames((0,_E,_b),(0,_E,_c),(0,_E,_d),(0,_E,_AN))
if mibBuilder.loadTexts:hpnicfWIPSDctSSIDBSSEntry.setStatus(_A)
_HpnicfWIPSDctNetworkBSSID_Type=MacAddress
_HpnicfWIPSDctNetworkBSSID_Object=MibTableColumn
hpnicfWIPSDctNetworkBSSID=_HpnicfWIPSDctNetworkBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,7,1,1),_HpnicfWIPSDctNetworkBSSID_Type())
hpnicfWIPSDctNetworkBSSID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkBSSID.setStatus(_A)
_HpnicfWIPSDctNetworkBSSWorkChl_Type=HpnicfWIPSChannel
_HpnicfWIPSDctNetworkBSSWorkChl_Object=MibTableColumn
hpnicfWIPSDctNetworkBSSWorkChl=_HpnicfWIPSDctNetworkBSSWorkChl_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,7,1,2),_HpnicfWIPSDctNetworkBSSWorkChl_Type())
hpnicfWIPSDctNetworkBSSWorkChl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkBSSWorkChl.setStatus(_A)
_HpnicfWIPSDctNetworkBSSStaNum_Type=Integer32
_HpnicfWIPSDctNetworkBSSStaNum_Object=MibTableColumn
hpnicfWIPSDctNetworkBSSStaNum=_HpnicfWIPSDctNetworkBSSStaNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,7,1,3),_HpnicfWIPSDctNetworkBSSStaNum_Type())
hpnicfWIPSDctNetworkBSSStaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctNetworkBSSStaNum.setStatus(_A)
_HpnicfWIPSBlockListTable_Object=MibTable
hpnicfWIPSBlockListTable=_HpnicfWIPSBlockListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,8))
if mibBuilder.loadTexts:hpnicfWIPSBlockListTable.setStatus(_A)
_HpnicfWIPSBlockListEntry_Object=MibTableRow
hpnicfWIPSBlockListEntry=_HpnicfWIPSBlockListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,8,1))
hpnicfWIPSBlockListEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:hpnicfWIPSBlockListEntry.setStatus(_A)
_HpnicfWIPSBlockListMacAddress_Type=MacAddress
_HpnicfWIPSBlockListMacAddress_Object=MibTableColumn
hpnicfWIPSBlockListMacAddress=_HpnicfWIPSBlockListMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,8,1,1),_HpnicfWIPSBlockListMacAddress_Type())
hpnicfWIPSBlockListMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSBlockListMacAddress.setStatus(_A)
class _HpnicfWIPSBlockListStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_AP,3)))
_HpnicfWIPSBlockListStatus_Type.__name__=_F
_HpnicfWIPSBlockListStatus_Object=MibTableColumn
hpnicfWIPSBlockListStatus=_HpnicfWIPSBlockListStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,8,1,2),_HpnicfWIPSBlockListStatus_Type())
hpnicfWIPSBlockListStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSBlockListStatus.setStatus(_A)
_HpnicfWIPSChannelTable_Object=MibTable
hpnicfWIPSChannelTable=_HpnicfWIPSChannelTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,9))
if mibBuilder.loadTexts:hpnicfWIPSChannelTable.setStatus(_A)
_HpnicfWIPSChannelEntry_Object=MibTableRow
hpnicfWIPSChannelEntry=_HpnicfWIPSChannelEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,9,1))
hpnicfWIPSChannelEntry.setIndexNames((0,_E,_AQ))
if mibBuilder.loadTexts:hpnicfWIPSChannelEntry.setStatus(_A)
_HpnicfWIPSChannelNum_Type=HpnicfWIPSChannel
_HpnicfWIPSChannelNum_Object=MibTableColumn
hpnicfWIPSChannelNum=_HpnicfWIPSChannelNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,9,1,1),_HpnicfWIPSChannelNum_Type())
hpnicfWIPSChannelNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSChannelNum.setStatus(_A)
_HpnicfWIPSChannelRadioType_Type=HpnicfWIPSRadioType
_HpnicfWIPSChannelRadioType_Object=MibTableColumn
hpnicfWIPSChannelRadioType=_HpnicfWIPSChannelRadioType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,9,1,2),_HpnicfWIPSChannelRadioType_Type())
hpnicfWIPSChannelRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChannelRadioType.setStatus(_A)
_HpnicfWIPSChannelIsPermitted_Type=TruthValue
_HpnicfWIPSChannelIsPermitted_Object=MibTableColumn
hpnicfWIPSChannelIsPermitted=_HpnicfWIPSChannelIsPermitted_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,9,1,3),_HpnicfWIPSChannelIsPermitted_Type())
hpnicfWIPSChannelIsPermitted.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChannelIsPermitted.setStatus(_A)
_HpnicfWIPSChannelLastRptTm_Type=TimeTicks
_HpnicfWIPSChannelLastRptTm_Object=MibTableColumn
hpnicfWIPSChannelLastRptTm=_HpnicfWIPSChannelLastRptTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,9,1,4),_HpnicfWIPSChannelLastRptTm_Type())
hpnicfWIPSChannelLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChannelLastRptTm.setStatus(_A)
_HpnicfWIPSCountermeasureListTable_Object=MibTable
hpnicfWIPSCountermeasureListTable=_HpnicfWIPSCountermeasureListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,10))
if mibBuilder.loadTexts:hpnicfWIPSCountermeasureListTable.setStatus(_A)
_HpnicfWIPSCountermeasureListEntry_Object=MibTableRow
hpnicfWIPSCountermeasureListEntry=_HpnicfWIPSCountermeasureListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,10,1))
hpnicfWIPSCountermeasureListEntry.setIndexNames((0,_E,_AR))
if mibBuilder.loadTexts:hpnicfWIPSCountermeasureListEntry.setStatus(_A)
_HpnicfWIPSCtmListMacAddress_Type=MacAddress
_HpnicfWIPSCtmListMacAddress_Object=MibTableColumn
hpnicfWIPSCtmListMacAddress=_HpnicfWIPSCtmListMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,10,1,1),_HpnicfWIPSCtmListMacAddress_Type())
hpnicfWIPSCtmListMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSCtmListMacAddress.setStatus(_A)
_HpnicfWIPSCtmListLastestWorkChl_Type=HpnicfWIPSChannel
_HpnicfWIPSCtmListLastestWorkChl_Object=MibTableColumn
hpnicfWIPSCtmListLastestWorkChl=_HpnicfWIPSCtmListLastestWorkChl_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,10,1,2),_HpnicfWIPSCtmListLastestWorkChl_Type())
hpnicfWIPSCtmListLastestWorkChl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmListLastestWorkChl.setStatus(_A)
_HpnicfWIPSCtmListFirstTm_Type=TimeTicks
_HpnicfWIPSCtmListFirstTm_Object=MibTableColumn
hpnicfWIPSCtmListFirstTm=_HpnicfWIPSCtmListFirstTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,10,1,3),_HpnicfWIPSCtmListFirstTm_Type())
hpnicfWIPSCtmListFirstTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmListFirstTm.setStatus(_A)
_HpnicfWIPSCtmListLastTm_Type=TimeTicks
_HpnicfWIPSCtmListLastTm_Object=MibTableColumn
hpnicfWIPSCtmListLastTm=_HpnicfWIPSCtmListLastTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,10,1,4),_HpnicfWIPSCtmListLastTm_Type())
hpnicfWIPSCtmListLastTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmListLastTm.setStatus(_A)
_HpnicfWIPSCtmListQurCnt_Type=Integer32
_HpnicfWIPSCtmListQurCnt_Object=MibTableColumn
hpnicfWIPSCtmListQurCnt=_HpnicfWIPSCtmListQurCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,10,1,5),_HpnicfWIPSCtmListQurCnt_Type())
hpnicfWIPSCtmListQurCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmListQurCnt.setStatus(_A)
_HpnicfWIPSCtmListSensorNum_Type=Integer32
_HpnicfWIPSCtmListSensorNum_Object=MibTableColumn
hpnicfWIPSCtmListSensorNum=_HpnicfWIPSCtmListSensorNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,10,1,6),_HpnicfWIPSCtmListSensorNum_Type())
hpnicfWIPSCtmListSensorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmListSensorNum.setStatus(_A)
_HpnicfWIPSIgnoreListTable_Object=MibTable
hpnicfWIPSIgnoreListTable=_HpnicfWIPSIgnoreListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,11))
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListTable.setStatus(_A)
_HpnicfWIPSIgnoreListEntry_Object=MibTableRow
hpnicfWIPSIgnoreListEntry=_HpnicfWIPSIgnoreListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,11,1))
hpnicfWIPSIgnoreListEntry.setIndexNames((0,_E,_AS))
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListEntry.setStatus(_A)
_HpnicfWIPSIgnoreListMacAddress_Type=MacAddress
_HpnicfWIPSIgnoreListMacAddress_Object=MibTableColumn
hpnicfWIPSIgnoreListMacAddress=_HpnicfWIPSIgnoreListMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,11,1,1),_HpnicfWIPSIgnoreListMacAddress_Type())
hpnicfWIPSIgnoreListMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListMacAddress.setStatus(_A)
_HpnicfWIPSIgnoreListFirstIgnoreTm_Type=TimeTicks
_HpnicfWIPSIgnoreListFirstIgnoreTm_Object=MibTableColumn
hpnicfWIPSIgnoreListFirstIgnoreTm=_HpnicfWIPSIgnoreListFirstIgnoreTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,11,1,2),_HpnicfWIPSIgnoreListFirstIgnoreTm_Type())
hpnicfWIPSIgnoreListFirstIgnoreTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListFirstIgnoreTm.setStatus(_A)
_HpnicfWIPSIgnoreListLastIgnoreTm_Type=TimeTicks
_HpnicfWIPSIgnoreListLastIgnoreTm_Object=MibTableColumn
hpnicfWIPSIgnoreListLastIgnoreTm=_HpnicfWIPSIgnoreListLastIgnoreTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,11,1,3),_HpnicfWIPSIgnoreListLastIgnoreTm_Type())
hpnicfWIPSIgnoreListLastIgnoreTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListLastIgnoreTm.setStatus(_A)
_HpnicfWIPSIgnoreListIgnoreCnt_Type=Integer32
_HpnicfWIPSIgnoreListIgnoreCnt_Object=MibTableColumn
hpnicfWIPSIgnoreListIgnoreCnt=_HpnicfWIPSIgnoreListIgnoreCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,11,1,4),_HpnicfWIPSIgnoreListIgnoreCnt_Type())
hpnicfWIPSIgnoreListIgnoreCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSIgnoreListIgnoreCnt.setStatus(_A)
_HpnicfWIPSTrustListTable_Object=MibTable
hpnicfWIPSTrustListTable=_HpnicfWIPSTrustListTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,12))
if mibBuilder.loadTexts:hpnicfWIPSTrustListTable.setStatus(_A)
_HpnicfWIPSTrustListEntry_Object=MibTableRow
hpnicfWIPSTrustListEntry=_HpnicfWIPSTrustListEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,12,1))
hpnicfWIPSTrustListEntry.setIndexNames((0,_E,_AT))
if mibBuilder.loadTexts:hpnicfWIPSTrustListEntry.setStatus(_A)
_HpnicfWIPSTrustListMacAddress_Type=MacAddress
_HpnicfWIPSTrustListMacAddress_Object=MibTableColumn
hpnicfWIPSTrustListMacAddress=_HpnicfWIPSTrustListMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,12,1,1),_HpnicfWIPSTrustListMacAddress_Type())
hpnicfWIPSTrustListMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSTrustListMacAddress.setStatus(_A)
class _HpnicfWIPSTrustListStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_AP,3)))
_HpnicfWIPSTrustListStatus_Type.__name__=_F
_HpnicfWIPSTrustListStatus_Object=MibTableColumn
hpnicfWIPSTrustListStatus=_HpnicfWIPSTrustListStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,12,1,2),_HpnicfWIPSTrustListStatus_Type())
hpnicfWIPSTrustListStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSTrustListStatus.setStatus(_A)
_HpnicfWIPSChlStatTable_Object=MibTable
hpnicfWIPSChlStatTable=_HpnicfWIPSChlStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13))
if mibBuilder.loadTexts:hpnicfWIPSChlStatTable.setStatus(_A)
_HpnicfWIPSChlStatEntry_Object=MibTableRow
hpnicfWIPSChlStatEntry=_HpnicfWIPSChlStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1))
hpnicfWIPSChlStatEntry.setIndexNames((0,_E,_AU),(0,_E,_AV))
if mibBuilder.loadTexts:hpnicfWIPSChlStatEntry.setStatus(_A)
_HpnicfWIPSChlStatSensorMacAddr_Type=MacAddress
_HpnicfWIPSChlStatSensorMacAddr_Object=MibTableColumn
hpnicfWIPSChlStatSensorMacAddr=_HpnicfWIPSChlStatSensorMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,1),_HpnicfWIPSChlStatSensorMacAddr_Type())
hpnicfWIPSChlStatSensorMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSChlStatSensorMacAddr.setStatus(_A)
_HpnicfWIPSChlStatChannel_Type=HpnicfWIPSChannel
_HpnicfWIPSChlStatChannel_Object=MibTableColumn
hpnicfWIPSChlStatChannel=_HpnicfWIPSChlStatChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,2),_HpnicfWIPSChlStatChannel_Type())
hpnicfWIPSChlStatChannel.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSChlStatChannel.setStatus(_A)
class _HpnicfWIPSChlStatTotalPkt_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatTotalPkt_Type.__name__=_D
_HpnicfWIPSChlStatTotalPkt_Object=MibTableColumn
hpnicfWIPSChlStatTotalPkt=_HpnicfWIPSChlStatTotalPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,3),_HpnicfWIPSChlStatTotalPkt_Type())
hpnicfWIPSChlStatTotalPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatTotalPkt.setStatus(_A)
class _HpnicfWIPSChlStatTotalByte_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatTotalByte_Type.__name__=_D
_HpnicfWIPSChlStatTotalByte_Object=MibTableColumn
hpnicfWIPSChlStatTotalByte=_HpnicfWIPSChlStatTotalByte_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,4),_HpnicfWIPSChlStatTotalByte_Type())
hpnicfWIPSChlStatTotalByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatTotalByte.setStatus(_A)
class _HpnicfWIPSChlStatBmcastPkt_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatBmcastPkt_Type.__name__=_D
_HpnicfWIPSChlStatBmcastPkt_Object=MibTableColumn
hpnicfWIPSChlStatBmcastPkt=_HpnicfWIPSChlStatBmcastPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,5),_HpnicfWIPSChlStatBmcastPkt_Type())
hpnicfWIPSChlStatBmcastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatBmcastPkt.setStatus(_A)
class _HpnicfWIPSChlStatBmcastByte_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatBmcastByte_Type.__name__=_D
_HpnicfWIPSChlStatBmcastByte_Object=MibTableColumn
hpnicfWIPSChlStatBmcastByte=_HpnicfWIPSChlStatBmcastByte_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,6),_HpnicfWIPSChlStatBmcastByte_Type())
hpnicfWIPSChlStatBmcastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatBmcastByte.setStatus(_A)
class _HpnicfWIPSChlStatUnicastPkt_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatUnicastPkt_Type.__name__=_D
_HpnicfWIPSChlStatUnicastPkt_Object=MibTableColumn
hpnicfWIPSChlStatUnicastPkt=_HpnicfWIPSChlStatUnicastPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,7),_HpnicfWIPSChlStatUnicastPkt_Type())
hpnicfWIPSChlStatUnicastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatUnicastPkt.setStatus(_A)
class _HpnicfWIPSChlStatUnicastByte_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatUnicastByte_Type.__name__=_D
_HpnicfWIPSChlStatUnicastByte_Object=MibTableColumn
hpnicfWIPSChlStatUnicastByte=_HpnicfWIPSChlStatUnicastByte_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,8),_HpnicfWIPSChlStatUnicastByte_Type())
hpnicfWIPSChlStatUnicastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatUnicastByte.setStatus(_A)
class _HpnicfWIPSChlStatManagement_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatManagement_Type.__name__=_D
_HpnicfWIPSChlStatManagement_Object=MibTableColumn
hpnicfWIPSChlStatManagement=_HpnicfWIPSChlStatManagement_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,9),_HpnicfWIPSChlStatManagement_Type())
hpnicfWIPSChlStatManagement.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatManagement.setStatus(_A)
class _HpnicfWIPSChlStatControl_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatControl_Type.__name__=_D
_HpnicfWIPSChlStatControl_Object=MibTableColumn
hpnicfWIPSChlStatControl=_HpnicfWIPSChlStatControl_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,10),_HpnicfWIPSChlStatControl_Type())
hpnicfWIPSChlStatControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatControl.setStatus(_A)
class _HpnicfWIPSChlStatData_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatData_Type.__name__=_D
_HpnicfWIPSChlStatData_Object=MibTableColumn
hpnicfWIPSChlStatData=_HpnicfWIPSChlStatData_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,11),_HpnicfWIPSChlStatData_Type())
hpnicfWIPSChlStatData.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatData.setStatus(_A)
class _HpnicfWIPSChlStatBeacon_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatBeacon_Type.__name__=_D
_HpnicfWIPSChlStatBeacon_Object=MibTableColumn
hpnicfWIPSChlStatBeacon=_HpnicfWIPSChlStatBeacon_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,12),_HpnicfWIPSChlStatBeacon_Type())
hpnicfWIPSChlStatBeacon.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatBeacon.setStatus(_A)
class _HpnicfWIPSChlStatRTS_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatRTS_Type.__name__=_D
_HpnicfWIPSChlStatRTS_Object=MibTableColumn
hpnicfWIPSChlStatRTS=_HpnicfWIPSChlStatRTS_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,13),_HpnicfWIPSChlStatRTS_Type())
hpnicfWIPSChlStatRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatRTS.setStatus(_A)
class _HpnicfWIPSChlStatCTS_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatCTS_Type.__name__=_D
_HpnicfWIPSChlStatCTS_Object=MibTableColumn
hpnicfWIPSChlStatCTS=_HpnicfWIPSChlStatCTS_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,14),_HpnicfWIPSChlStatCTS_Type())
hpnicfWIPSChlStatCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatCTS.setStatus(_A)
class _HpnicfWIPSChlStatProbeRequest_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatProbeRequest_Type.__name__=_D
_HpnicfWIPSChlStatProbeRequest_Object=MibTableColumn
hpnicfWIPSChlStatProbeRequest=_HpnicfWIPSChlStatProbeRequest_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,15),_HpnicfWIPSChlStatProbeRequest_Type())
hpnicfWIPSChlStatProbeRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatProbeRequest.setStatus(_A)
class _HpnicfWIPSChlStatProbeResponse_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatProbeResponse_Type.__name__=_D
_HpnicfWIPSChlStatProbeResponse_Object=MibTableColumn
hpnicfWIPSChlStatProbeResponse=_HpnicfWIPSChlStatProbeResponse_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,16),_HpnicfWIPSChlStatProbeResponse_Type())
hpnicfWIPSChlStatProbeResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatProbeResponse.setStatus(_A)
class _HpnicfWIPSChlStatFragment_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatFragment_Type.__name__=_D
_HpnicfWIPSChlStatFragment_Object=MibTableColumn
hpnicfWIPSChlStatFragment=_HpnicfWIPSChlStatFragment_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,17),_HpnicfWIPSChlStatFragment_Type())
hpnicfWIPSChlStatFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatFragment.setStatus(_A)
class _HpnicfWIPSChlStatRetry_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatRetry_Type.__name__=_D
_HpnicfWIPSChlStatRetry_Object=MibTableColumn
hpnicfWIPSChlStatRetry=_HpnicfWIPSChlStatRetry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,18),_HpnicfWIPSChlStatRetry_Type())
hpnicfWIPSChlStatRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatRetry.setStatus(_A)
class _HpnicfWIPSChlStatEapSuccess_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatEapSuccess_Type.__name__=_D
_HpnicfWIPSChlStatEapSuccess_Object=MibTableColumn
hpnicfWIPSChlStatEapSuccess=_HpnicfWIPSChlStatEapSuccess_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,19),_HpnicfWIPSChlStatEapSuccess_Type())
hpnicfWIPSChlStatEapSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatEapSuccess.setStatus(_A)
class _HpnicfWIPSChlStatEapFailure_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatEapFailure_Type.__name__=_D
_HpnicfWIPSChlStatEapFailure_Object=MibTableColumn
hpnicfWIPSChlStatEapFailure=_HpnicfWIPSChlStatEapFailure_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,20),_HpnicfWIPSChlStatEapFailure_Type())
hpnicfWIPSChlStatEapFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatEapFailure.setStatus(_A)
class _HpnicfWIPSChlStatEapolStart_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatEapolStart_Type.__name__=_D
_HpnicfWIPSChlStatEapolStart_Object=MibTableColumn
hpnicfWIPSChlStatEapolStart=_HpnicfWIPSChlStatEapolStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,21),_HpnicfWIPSChlStatEapolStart_Type())
hpnicfWIPSChlStatEapolStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatEapolStart.setStatus(_A)
class _HpnicfWIPSChlStatEapolLogoff_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatEapolLogoff_Type.__name__=_D
_HpnicfWIPSChlStatEapolLogoff_Object=MibTableColumn
hpnicfWIPSChlStatEapolLogoff=_HpnicfWIPSChlStatEapolLogoff_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,22),_HpnicfWIPSChlStatEapolLogoff_Type())
hpnicfWIPSChlStatEapolLogoff.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatEapolLogoff.setStatus(_A)
class _HpnicfWIPSChlStatAssocRequest_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatAssocRequest_Type.__name__=_D
_HpnicfWIPSChlStatAssocRequest_Object=MibTableColumn
hpnicfWIPSChlStatAssocRequest=_HpnicfWIPSChlStatAssocRequest_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,23),_HpnicfWIPSChlStatAssocRequest_Type())
hpnicfWIPSChlStatAssocRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatAssocRequest.setStatus(_A)
class _HpnicfWIPSChlStatAssocResponse_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatAssocResponse_Type.__name__=_D
_HpnicfWIPSChlStatAssocResponse_Object=MibTableColumn
hpnicfWIPSChlStatAssocResponse=_HpnicfWIPSChlStatAssocResponse_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,24),_HpnicfWIPSChlStatAssocResponse_Type())
hpnicfWIPSChlStatAssocResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatAssocResponse.setStatus(_A)
class _HpnicfWIPSChlStatUnicastDisassoc_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatUnicastDisassoc_Type.__name__=_D
_HpnicfWIPSChlStatUnicastDisassoc_Object=MibTableColumn
hpnicfWIPSChlStatUnicastDisassoc=_HpnicfWIPSChlStatUnicastDisassoc_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,25),_HpnicfWIPSChlStatUnicastDisassoc_Type())
hpnicfWIPSChlStatUnicastDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatUnicastDisassoc.setStatus(_A)
class _HpnicfWIPSChlStatBroadcastDisassoc_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatBroadcastDisassoc_Type.__name__=_D
_HpnicfWIPSChlStatBroadcastDisassoc_Object=MibTableColumn
hpnicfWIPSChlStatBroadcastDisassoc=_HpnicfWIPSChlStatBroadcastDisassoc_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,26),_HpnicfWIPSChlStatBroadcastDisassoc_Type())
hpnicfWIPSChlStatBroadcastDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatBroadcastDisassoc.setStatus(_A)
class _HpnicfWIPSChlStatAuthentication_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatAuthentication_Type.__name__=_D
_HpnicfWIPSChlStatAuthentication_Object=MibTableColumn
hpnicfWIPSChlStatAuthentication=_HpnicfWIPSChlStatAuthentication_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,27),_HpnicfWIPSChlStatAuthentication_Type())
hpnicfWIPSChlStatAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatAuthentication.setStatus(_A)
class _HpnicfWIPSChlStatUnicastDeauthen_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatUnicastDeauthen_Type.__name__=_D
_HpnicfWIPSChlStatUnicastDeauthen_Object=MibTableColumn
hpnicfWIPSChlStatUnicastDeauthen=_HpnicfWIPSChlStatUnicastDeauthen_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,28),_HpnicfWIPSChlStatUnicastDeauthen_Type())
hpnicfWIPSChlStatUnicastDeauthen.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatUnicastDeauthen.setStatus(_A)
class _HpnicfWIPSChlStatBroadcastDeauthen_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatBroadcastDeauthen_Type.__name__=_D
_HpnicfWIPSChlStatBroadcastDeauthen_Object=MibTableColumn
hpnicfWIPSChlStatBroadcastDeauthen=_HpnicfWIPSChlStatBroadcastDeauthen_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,29),_HpnicfWIPSChlStatBroadcastDeauthen_Type())
hpnicfWIPSChlStatBroadcastDeauthen.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatBroadcastDeauthen.setStatus(_A)
class _HpnicfWIPSChlStatMalformed_Type(Counter64):defaultValue=0
_HpnicfWIPSChlStatMalformed_Type.__name__=_D
_HpnicfWIPSChlStatMalformed_Object=MibTableColumn
hpnicfWIPSChlStatMalformed=_HpnicfWIPSChlStatMalformed_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,13,1,30),_HpnicfWIPSChlStatMalformed_Type())
hpnicfWIPSChlStatMalformed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSChlStatMalformed.setStatus(_A)
_HpnicfWIPSDevStatTable_Object=MibTable
hpnicfWIPSDevStatTable=_HpnicfWIPSDevStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14))
if mibBuilder.loadTexts:hpnicfWIPSDevStatTable.setStatus(_A)
_HpnicfWIPSDevStatEntry_Object=MibTableRow
hpnicfWIPSDevStatEntry=_HpnicfWIPSDevStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1))
hpnicfWIPSDevStatEntry.setIndexNames((0,_E,_AW),(0,_E,_AX),(0,_E,_AY))
if mibBuilder.loadTexts:hpnicfWIPSDevStatEntry.setStatus(_A)
_HpnicfWIPSDevStatSensorMacAddr_Type=MacAddress
_HpnicfWIPSDevStatSensorMacAddr_Object=MibTableColumn
hpnicfWIPSDevStatSensorMacAddr=_HpnicfWIPSDevStatSensorMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,1),_HpnicfWIPSDevStatSensorMacAddr_Type())
hpnicfWIPSDevStatSensorMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDevStatSensorMacAddr.setStatus(_A)
_HpnicfWIPSDevStatDevMacAddress_Type=MacAddress
_HpnicfWIPSDevStatDevMacAddress_Object=MibTableColumn
hpnicfWIPSDevStatDevMacAddress=_HpnicfWIPSDevStatDevMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,2),_HpnicfWIPSDevStatDevMacAddress_Type())
hpnicfWIPSDevStatDevMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDevStatDevMacAddress.setStatus(_A)
_HpnicfWIPSDevStatChannel_Type=HpnicfWIPSChannel
_HpnicfWIPSDevStatChannel_Object=MibTableColumn
hpnicfWIPSDevStatChannel=_HpnicfWIPSDevStatChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,3),_HpnicfWIPSDevStatChannel_Type())
hpnicfWIPSDevStatChannel.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDevStatChannel.setStatus(_A)
class _HpnicfWIPSDevStatTxTotalPkt_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxTotalPkt_Type.__name__=_D
_HpnicfWIPSDevStatTxTotalPkt_Object=MibTableColumn
hpnicfWIPSDevStatTxTotalPkt=_HpnicfWIPSDevStatTxTotalPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,4),_HpnicfWIPSDevStatTxTotalPkt_Type())
hpnicfWIPSDevStatTxTotalPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxTotalPkt.setStatus(_A)
class _HpnicfWIPSDevStatTxTotalByte_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxTotalByte_Type.__name__=_D
_HpnicfWIPSDevStatTxTotalByte_Object=MibTableColumn
hpnicfWIPSDevStatTxTotalByte=_HpnicfWIPSDevStatTxTotalByte_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,5),_HpnicfWIPSDevStatTxTotalByte_Type())
hpnicfWIPSDevStatTxTotalByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxTotalByte.setStatus(_A)
class _HpnicfWIPSDevStatTxBMcastPkt_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxBMcastPkt_Type.__name__=_D
_HpnicfWIPSDevStatTxBMcastPkt_Object=MibTableColumn
hpnicfWIPSDevStatTxBMcastPkt=_HpnicfWIPSDevStatTxBMcastPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,6),_HpnicfWIPSDevStatTxBMcastPkt_Type())
hpnicfWIPSDevStatTxBMcastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxBMcastPkt.setStatus(_A)
class _HpnicfWIPSDevStatTxBMcastByte_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxBMcastByte_Type.__name__=_D
_HpnicfWIPSDevStatTxBMcastByte_Object=MibTableColumn
hpnicfWIPSDevStatTxBMcastByte=_HpnicfWIPSDevStatTxBMcastByte_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,7),_HpnicfWIPSDevStatTxBMcastByte_Type())
hpnicfWIPSDevStatTxBMcastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxBMcastByte.setStatus(_A)
class _HpnicfWIPSDevStatTxUnicastPkt_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxUnicastPkt_Type.__name__=_D
_HpnicfWIPSDevStatTxUnicastPkt_Object=MibTableColumn
hpnicfWIPSDevStatTxUnicastPkt=_HpnicfWIPSDevStatTxUnicastPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,8),_HpnicfWIPSDevStatTxUnicastPkt_Type())
hpnicfWIPSDevStatTxUnicastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxUnicastPkt.setStatus(_A)
class _HpnicfWIPSDevStatTxUnicastByte_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxUnicastByte_Type.__name__=_D
_HpnicfWIPSDevStatTxUnicastByte_Object=MibTableColumn
hpnicfWIPSDevStatTxUnicastByte=_HpnicfWIPSDevStatTxUnicastByte_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,9),_HpnicfWIPSDevStatTxUnicastByte_Type())
hpnicfWIPSDevStatTxUnicastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxUnicastByte.setStatus(_A)
class _HpnicfWIPSDevStatTxMgmt_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxMgmt_Type.__name__=_D
_HpnicfWIPSDevStatTxMgmt_Object=MibTableColumn
hpnicfWIPSDevStatTxMgmt=_HpnicfWIPSDevStatTxMgmt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,10),_HpnicfWIPSDevStatTxMgmt_Type())
hpnicfWIPSDevStatTxMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxMgmt.setStatus(_A)
class _HpnicfWIPSDevStatTxCtrl_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxCtrl_Type.__name__=_D
_HpnicfWIPSDevStatTxCtrl_Object=MibTableColumn
hpnicfWIPSDevStatTxCtrl=_HpnicfWIPSDevStatTxCtrl_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,11),_HpnicfWIPSDevStatTxCtrl_Type())
hpnicfWIPSDevStatTxCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxCtrl.setStatus(_A)
class _HpnicfWIPSDevStatTxData_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxData_Type.__name__=_D
_HpnicfWIPSDevStatTxData_Object=MibTableColumn
hpnicfWIPSDevStatTxData=_HpnicfWIPSDevStatTxData_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,12),_HpnicfWIPSDevStatTxData_Type())
hpnicfWIPSDevStatTxData.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxData.setStatus(_A)
class _HpnicfWIPSDevStatTxBeacon_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxBeacon_Type.__name__=_D
_HpnicfWIPSDevStatTxBeacon_Object=MibTableColumn
hpnicfWIPSDevStatTxBeacon=_HpnicfWIPSDevStatTxBeacon_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,13),_HpnicfWIPSDevStatTxBeacon_Type())
hpnicfWIPSDevStatTxBeacon.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxBeacon.setStatus(_A)
class _HpnicfWIPSDevStatTxRTS_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxRTS_Type.__name__=_D
_HpnicfWIPSDevStatTxRTS_Object=MibTableColumn
hpnicfWIPSDevStatTxRTS=_HpnicfWIPSDevStatTxRTS_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,14),_HpnicfWIPSDevStatTxRTS_Type())
hpnicfWIPSDevStatTxRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxRTS.setStatus(_A)
class _HpnicfWIPSDevStatTxProbeRequest_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxProbeRequest_Type.__name__=_D
_HpnicfWIPSDevStatTxProbeRequest_Object=MibTableColumn
hpnicfWIPSDevStatTxProbeRequest=_HpnicfWIPSDevStatTxProbeRequest_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,15),_HpnicfWIPSDevStatTxProbeRequest_Type())
hpnicfWIPSDevStatTxProbeRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxProbeRequest.setStatus(_A)
class _HpnicfWIPSDevStatTxProbeResponse_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxProbeResponse_Type.__name__=_D
_HpnicfWIPSDevStatTxProbeResponse_Object=MibTableColumn
hpnicfWIPSDevStatTxProbeResponse=_HpnicfWIPSDevStatTxProbeResponse_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,16),_HpnicfWIPSDevStatTxProbeResponse_Type())
hpnicfWIPSDevStatTxProbeResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxProbeResponse.setStatus(_A)
class _HpnicfWIPSDevStatTxFragment_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxFragment_Type.__name__=_D
_HpnicfWIPSDevStatTxFragment_Object=MibTableColumn
hpnicfWIPSDevStatTxFragment=_HpnicfWIPSDevStatTxFragment_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,17),_HpnicfWIPSDevStatTxFragment_Type())
hpnicfWIPSDevStatTxFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxFragment.setStatus(_A)
class _HpnicfWIPSDevStatTxRetry_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxRetry_Type.__name__=_D
_HpnicfWIPSDevStatTxRetry_Object=MibTableColumn
hpnicfWIPSDevStatTxRetry=_HpnicfWIPSDevStatTxRetry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,18),_HpnicfWIPSDevStatTxRetry_Type())
hpnicfWIPSDevStatTxRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxRetry.setStatus(_A)
class _HpnicfWIPSDevStatTxAssocRequest_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxAssocRequest_Type.__name__=_D
_HpnicfWIPSDevStatTxAssocRequest_Object=MibTableColumn
hpnicfWIPSDevStatTxAssocRequest=_HpnicfWIPSDevStatTxAssocRequest_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,19),_HpnicfWIPSDevStatTxAssocRequest_Type())
hpnicfWIPSDevStatTxAssocRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxAssocRequest.setStatus(_A)
class _HpnicfWIPSDevStatTxAssocResponse_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxAssocResponse_Type.__name__=_D
_HpnicfWIPSDevStatTxAssocResponse_Object=MibTableColumn
hpnicfWIPSDevStatTxAssocResponse=_HpnicfWIPSDevStatTxAssocResponse_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,20),_HpnicfWIPSDevStatTxAssocResponse_Type())
hpnicfWIPSDevStatTxAssocResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxAssocResponse.setStatus(_A)
class _HpnicfWIPSDevStatTxUnicastDisassoc_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxUnicastDisassoc_Type.__name__=_D
_HpnicfWIPSDevStatTxUnicastDisassoc_Object=MibTableColumn
hpnicfWIPSDevStatTxUnicastDisassoc=_HpnicfWIPSDevStatTxUnicastDisassoc_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,21),_HpnicfWIPSDevStatTxUnicastDisassoc_Type())
hpnicfWIPSDevStatTxUnicastDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxUnicastDisassoc.setStatus(_A)
class _HpnicfWIPSDevStatTxBcastDisassoc_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxBcastDisassoc_Type.__name__=_D
_HpnicfWIPSDevStatTxBcastDisassoc_Object=MibTableColumn
hpnicfWIPSDevStatTxBcastDisassoc=_HpnicfWIPSDevStatTxBcastDisassoc_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,22),_HpnicfWIPSDevStatTxBcastDisassoc_Type())
hpnicfWIPSDevStatTxBcastDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxBcastDisassoc.setStatus(_A)
class _HpnicfWIPSDevStatTxAuth_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxAuth_Type.__name__=_D
_HpnicfWIPSDevStatTxAuth_Object=MibTableColumn
hpnicfWIPSDevStatTxAuth=_HpnicfWIPSDevStatTxAuth_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,23),_HpnicfWIPSDevStatTxAuth_Type())
hpnicfWIPSDevStatTxAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxAuth.setStatus(_A)
class _HpnicfWIPSDevStatTxUnicastDeauth_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxUnicastDeauth_Type.__name__=_D
_HpnicfWIPSDevStatTxUnicastDeauth_Object=MibTableColumn
hpnicfWIPSDevStatTxUnicastDeauth=_HpnicfWIPSDevStatTxUnicastDeauth_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,24),_HpnicfWIPSDevStatTxUnicastDeauth_Type())
hpnicfWIPSDevStatTxUnicastDeauth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxUnicastDeauth.setStatus(_A)
class _HpnicfWIPSDevStatTxBcastDeauth_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxBcastDeauth_Type.__name__=_D
_HpnicfWIPSDevStatTxBcastDeauth_Object=MibTableColumn
hpnicfWIPSDevStatTxBcastDeauth=_HpnicfWIPSDevStatTxBcastDeauth_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,25),_HpnicfWIPSDevStatTxBcastDeauth_Type())
hpnicfWIPSDevStatTxBcastDeauth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxBcastDeauth.setStatus(_A)
class _HpnicfWIPSDevStatTxEAPSuccess_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxEAPSuccess_Type.__name__=_D
_HpnicfWIPSDevStatTxEAPSuccess_Object=MibTableColumn
hpnicfWIPSDevStatTxEAPSuccess=_HpnicfWIPSDevStatTxEAPSuccess_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,26),_HpnicfWIPSDevStatTxEAPSuccess_Type())
hpnicfWIPSDevStatTxEAPSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxEAPSuccess.setStatus(_A)
class _HpnicfWIPSDevStatTxEAPFailure_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxEAPFailure_Type.__name__=_D
_HpnicfWIPSDevStatTxEAPFailure_Object=MibTableColumn
hpnicfWIPSDevStatTxEAPFailure=_HpnicfWIPSDevStatTxEAPFailure_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,27),_HpnicfWIPSDevStatTxEAPFailure_Type())
hpnicfWIPSDevStatTxEAPFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxEAPFailure.setStatus(_A)
class _HpnicfWIPSDevStatTxEAPOLStart_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxEAPOLStart_Type.__name__=_D
_HpnicfWIPSDevStatTxEAPOLStart_Object=MibTableColumn
hpnicfWIPSDevStatTxEAPOLStart=_HpnicfWIPSDevStatTxEAPOLStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,28),_HpnicfWIPSDevStatTxEAPOLStart_Type())
hpnicfWIPSDevStatTxEAPOLStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxEAPOLStart.setStatus(_A)
class _HpnicfWIPSDevStatTxEAPOLLogOff_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxEAPOLLogOff_Type.__name__=_D
_HpnicfWIPSDevStatTxEAPOLLogOff_Object=MibTableColumn
hpnicfWIPSDevStatTxEAPOLLogOff=_HpnicfWIPSDevStatTxEAPOLLogOff_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,29),_HpnicfWIPSDevStatTxEAPOLLogOff_Type())
hpnicfWIPSDevStatTxEAPOLLogOff.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxEAPOLLogOff.setStatus(_A)
class _HpnicfWIPSDevStatTxMalformed_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatTxMalformed_Type.__name__=_D
_HpnicfWIPSDevStatTxMalformed_Object=MibTableColumn
hpnicfWIPSDevStatTxMalformed=_HpnicfWIPSDevStatTxMalformed_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,30),_HpnicfWIPSDevStatTxMalformed_Type())
hpnicfWIPSDevStatTxMalformed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatTxMalformed.setStatus(_A)
class _HpnicfWIPSDevStatRxTotalPkt_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxTotalPkt_Type.__name__=_D
_HpnicfWIPSDevStatRxTotalPkt_Object=MibTableColumn
hpnicfWIPSDevStatRxTotalPkt=_HpnicfWIPSDevStatRxTotalPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,31),_HpnicfWIPSDevStatRxTotalPkt_Type())
hpnicfWIPSDevStatRxTotalPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxTotalPkt.setStatus(_A)
class _HpnicfWIPSDevStatRxTotalByte_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxTotalByte_Type.__name__=_D
_HpnicfWIPSDevStatRxTotalByte_Object=MibTableColumn
hpnicfWIPSDevStatRxTotalByte=_HpnicfWIPSDevStatRxTotalByte_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,32),_HpnicfWIPSDevStatRxTotalByte_Type())
hpnicfWIPSDevStatRxTotalByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxTotalByte.setStatus(_A)
class _HpnicfWIPSDevStatRxUnicastPkt_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxUnicastPkt_Type.__name__=_D
_HpnicfWIPSDevStatRxUnicastPkt_Object=MibTableColumn
hpnicfWIPSDevStatRxUnicastPkt=_HpnicfWIPSDevStatRxUnicastPkt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,33),_HpnicfWIPSDevStatRxUnicastPkt_Type())
hpnicfWIPSDevStatRxUnicastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxUnicastPkt.setStatus(_A)
class _HpnicfWIPSDevStatRxUnicastByte_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxUnicastByte_Type.__name__=_D
_HpnicfWIPSDevStatRxUnicastByte_Object=MibTableColumn
hpnicfWIPSDevStatRxUnicastByte=_HpnicfWIPSDevStatRxUnicastByte_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,34),_HpnicfWIPSDevStatRxUnicastByte_Type())
hpnicfWIPSDevStatRxUnicastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxUnicastByte.setStatus(_A)
class _HpnicfWIPSDevStatRxMgmt_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxMgmt_Type.__name__=_D
_HpnicfWIPSDevStatRxMgmt_Object=MibTableColumn
hpnicfWIPSDevStatRxMgmt=_HpnicfWIPSDevStatRxMgmt_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,35),_HpnicfWIPSDevStatRxMgmt_Type())
hpnicfWIPSDevStatRxMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxMgmt.setStatus(_A)
class _HpnicfWIPSDevStatRxCtrl_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxCtrl_Type.__name__=_D
_HpnicfWIPSDevStatRxCtrl_Object=MibTableColumn
hpnicfWIPSDevStatRxCtrl=_HpnicfWIPSDevStatRxCtrl_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,36),_HpnicfWIPSDevStatRxCtrl_Type())
hpnicfWIPSDevStatRxCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxCtrl.setStatus(_A)
class _HpnicfWIPSDevStatRxData_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxData_Type.__name__=_D
_HpnicfWIPSDevStatRxData_Object=MibTableColumn
hpnicfWIPSDevStatRxData=_HpnicfWIPSDevStatRxData_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,37),_HpnicfWIPSDevStatRxData_Type())
hpnicfWIPSDevStatRxData.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxData.setStatus(_A)
class _HpnicfWIPSDevStatRxRTS_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxRTS_Type.__name__=_D
_HpnicfWIPSDevStatRxRTS_Object=MibTableColumn
hpnicfWIPSDevStatRxRTS=_HpnicfWIPSDevStatRxRTS_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,38),_HpnicfWIPSDevStatRxRTS_Type())
hpnicfWIPSDevStatRxRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxRTS.setStatus(_A)
class _HpnicfWIPSDevStatRxCTS_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxCTS_Type.__name__=_D
_HpnicfWIPSDevStatRxCTS_Object=MibTableColumn
hpnicfWIPSDevStatRxCTS=_HpnicfWIPSDevStatRxCTS_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,39),_HpnicfWIPSDevStatRxCTS_Type())
hpnicfWIPSDevStatRxCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxCTS.setStatus(_A)
class _HpnicfWIPSDevStatRxProbeRequest_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxProbeRequest_Type.__name__=_D
_HpnicfWIPSDevStatRxProbeRequest_Object=MibTableColumn
hpnicfWIPSDevStatRxProbeRequest=_HpnicfWIPSDevStatRxProbeRequest_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,40),_HpnicfWIPSDevStatRxProbeRequest_Type())
hpnicfWIPSDevStatRxProbeRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxProbeRequest.setStatus(_A)
class _HpnicfWIPSDevStatRxProbeResponse_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxProbeResponse_Type.__name__=_D
_HpnicfWIPSDevStatRxProbeResponse_Object=MibTableColumn
hpnicfWIPSDevStatRxProbeResponse=_HpnicfWIPSDevStatRxProbeResponse_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,41),_HpnicfWIPSDevStatRxProbeResponse_Type())
hpnicfWIPSDevStatRxProbeResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxProbeResponse.setStatus(_A)
class _HpnicfWIPSDevStatRxFragment_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxFragment_Type.__name__=_D
_HpnicfWIPSDevStatRxFragment_Object=MibTableColumn
hpnicfWIPSDevStatRxFragment=_HpnicfWIPSDevStatRxFragment_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,42),_HpnicfWIPSDevStatRxFragment_Type())
hpnicfWIPSDevStatRxFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxFragment.setStatus(_A)
class _HpnicfWIPSDevStatRxRetry_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxRetry_Type.__name__=_D
_HpnicfWIPSDevStatRxRetry_Object=MibTableColumn
hpnicfWIPSDevStatRxRetry=_HpnicfWIPSDevStatRxRetry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,43),_HpnicfWIPSDevStatRxRetry_Type())
hpnicfWIPSDevStatRxRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxRetry.setStatus(_A)
class _HpnicfWIPSDevStatRxAssoRequest_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxAssoRequest_Type.__name__=_D
_HpnicfWIPSDevStatRxAssoRequest_Object=MibTableColumn
hpnicfWIPSDevStatRxAssoRequest=_HpnicfWIPSDevStatRxAssoRequest_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,44),_HpnicfWIPSDevStatRxAssoRequest_Type())
hpnicfWIPSDevStatRxAssoRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxAssoRequest.setStatus(_A)
class _HpnicfWIPSDevStatRxAssoResponse_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxAssoResponse_Type.__name__=_D
_HpnicfWIPSDevStatRxAssoResponse_Object=MibTableColumn
hpnicfWIPSDevStatRxAssoResponse=_HpnicfWIPSDevStatRxAssoResponse_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,45),_HpnicfWIPSDevStatRxAssoResponse_Type())
hpnicfWIPSDevStatRxAssoResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxAssoResponse.setStatus(_A)
class _HpnicfWIPSDevStatRxDisassoc_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxDisassoc_Type.__name__=_D
_HpnicfWIPSDevStatRxDisassoc_Object=MibTableColumn
hpnicfWIPSDevStatRxDisassoc=_HpnicfWIPSDevStatRxDisassoc_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,46),_HpnicfWIPSDevStatRxDisassoc_Type())
hpnicfWIPSDevStatRxDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxDisassoc.setStatus(_A)
class _HpnicfWIPSDevStatRxAuth_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxAuth_Type.__name__=_D
_HpnicfWIPSDevStatRxAuth_Object=MibTableColumn
hpnicfWIPSDevStatRxAuth=_HpnicfWIPSDevStatRxAuth_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,47),_HpnicfWIPSDevStatRxAuth_Type())
hpnicfWIPSDevStatRxAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxAuth.setStatus(_A)
class _HpnicfWIPSDevStatRxDeauth_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxDeauth_Type.__name__=_D
_HpnicfWIPSDevStatRxDeauth_Object=MibTableColumn
hpnicfWIPSDevStatRxDeauth=_HpnicfWIPSDevStatRxDeauth_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,48),_HpnicfWIPSDevStatRxDeauth_Type())
hpnicfWIPSDevStatRxDeauth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxDeauth.setStatus(_A)
class _HpnicfWIPSDevStatRxEAPSuccess_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxEAPSuccess_Type.__name__=_D
_HpnicfWIPSDevStatRxEAPSuccess_Object=MibTableColumn
hpnicfWIPSDevStatRxEAPSuccess=_HpnicfWIPSDevStatRxEAPSuccess_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,49),_HpnicfWIPSDevStatRxEAPSuccess_Type())
hpnicfWIPSDevStatRxEAPSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxEAPSuccess.setStatus(_A)
class _HpnicfWIPSDevStatRxEAPFailure_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxEAPFailure_Type.__name__=_D
_HpnicfWIPSDevStatRxEAPFailure_Object=MibTableColumn
hpnicfWIPSDevStatRxEAPFailure=_HpnicfWIPSDevStatRxEAPFailure_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,50),_HpnicfWIPSDevStatRxEAPFailure_Type())
hpnicfWIPSDevStatRxEAPFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxEAPFailure.setStatus(_A)
class _HpnicfWIPSDevStatRxEAPOLStart_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxEAPOLStart_Type.__name__=_D
_HpnicfWIPSDevStatRxEAPOLStart_Object=MibTableColumn
hpnicfWIPSDevStatRxEAPOLStart=_HpnicfWIPSDevStatRxEAPOLStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,51),_HpnicfWIPSDevStatRxEAPOLStart_Type())
hpnicfWIPSDevStatRxEAPOLStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxEAPOLStart.setStatus(_A)
class _HpnicfWIPSDevStatRxEAPOLLogoff_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxEAPOLLogoff_Type.__name__=_D
_HpnicfWIPSDevStatRxEAPOLLogoff_Object=MibTableColumn
hpnicfWIPSDevStatRxEAPOLLogoff=_HpnicfWIPSDevStatRxEAPOLLogoff_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,52),_HpnicfWIPSDevStatRxEAPOLLogoff_Type())
hpnicfWIPSDevStatRxEAPOLLogoff.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxEAPOLLogoff.setStatus(_A)
class _HpnicfWIPSDevStatRxMalformed_Type(Counter64):defaultValue=0
_HpnicfWIPSDevStatRxMalformed_Type.__name__=_D
_HpnicfWIPSDevStatRxMalformed_Object=MibTableColumn
hpnicfWIPSDevStatRxMalformed=_HpnicfWIPSDevStatRxMalformed_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,14,1,53),_HpnicfWIPSDevStatRxMalformed_Type())
hpnicfWIPSDevStatRxMalformed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDevStatRxMalformed.setStatus(_A)
_HpnicfWIPSCtmDeviceTable_Object=MibTable
hpnicfWIPSCtmDeviceTable=_HpnicfWIPSCtmDeviceTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15))
if mibBuilder.loadTexts:hpnicfWIPSCtmDeviceTable.setStatus(_A)
_HpnicfWIPSCtmDeviceEntry_Object=MibTableRow
hpnicfWIPSCtmDeviceEntry=_HpnicfWIPSCtmDeviceEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15,1))
hpnicfWIPSCtmDeviceEntry.setIndexNames((0,_E,_AZ),(0,_E,_Aa))
if mibBuilder.loadTexts:hpnicfWIPSCtmDeviceEntry.setStatus(_A)
class _HpnicfWIPSCtmDeviceVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSCtmDeviceVSD_Type.__name__=_H
_HpnicfWIPSCtmDeviceVSD_Object=MibTableColumn
hpnicfWIPSCtmDeviceVSD=_HpnicfWIPSCtmDeviceVSD_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15,1,1),_HpnicfWIPSCtmDeviceVSD_Type())
hpnicfWIPSCtmDeviceVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSCtmDeviceVSD.setStatus(_A)
_HpnicfWIPSCtmDeviceMAC_Type=MacAddress
_HpnicfWIPSCtmDeviceMAC_Object=MibTableColumn
hpnicfWIPSCtmDeviceMAC=_HpnicfWIPSCtmDeviceMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15,1,2),_HpnicfWIPSCtmDeviceMAC_Type())
hpnicfWIPSCtmDeviceMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSCtmDeviceMAC.setStatus(_A)
class _HpnicfWIPSCtmDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),('staticAnddynamic',3)))
_HpnicfWIPSCtmDeviceType_Type.__name__=_F
_HpnicfWIPSCtmDeviceType_Object=MibTableColumn
hpnicfWIPSCtmDeviceType=_HpnicfWIPSCtmDeviceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15,1,3),_HpnicfWIPSCtmDeviceType_Type())
hpnicfWIPSCtmDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmDeviceType.setStatus(_A)
class _HpnicfWIPSCtmDeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),('idle',1),('pending',2),('action',3)))
_HpnicfWIPSCtmDeviceState_Type.__name__=_F
_HpnicfWIPSCtmDeviceState_Object=MibTableColumn
hpnicfWIPSCtmDeviceState=_HpnicfWIPSCtmDeviceState_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15,1,4),_HpnicfWIPSCtmDeviceState_Type())
hpnicfWIPSCtmDeviceState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmDeviceState.setStatus(_A)
_HpnicfWIPSCtmDeviceStartTime_Type=TimeTicks
_HpnicfWIPSCtmDeviceStartTime_Object=MibTableColumn
hpnicfWIPSCtmDeviceStartTime=_HpnicfWIPSCtmDeviceStartTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15,1,5),_HpnicfWIPSCtmDeviceStartTime_Type())
hpnicfWIPSCtmDeviceStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmDeviceStartTime.setStatus(_A)
_HpnicfWIPSCtmDeviceCategory_Type=HpnicfWIPSDeviceCategoryType
_HpnicfWIPSCtmDeviceCategory_Object=MibTableColumn
hpnicfWIPSCtmDeviceCategory=_HpnicfWIPSCtmDeviceCategory_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15,1,6),_HpnicfWIPSCtmDeviceCategory_Type())
hpnicfWIPSCtmDeviceCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmDeviceCategory.setStatus(_A)
_HpnicfWIPSCtmDeviceChl_Type=Unsigned32
_HpnicfWIPSCtmDeviceChl_Object=MibTableColumn
hpnicfWIPSCtmDeviceChl=_HpnicfWIPSCtmDeviceChl_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15,1,7),_HpnicfWIPSCtmDeviceChl_Type())
hpnicfWIPSCtmDeviceChl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmDeviceChl.setStatus(_A)
class _HpnicfWIPSCtmDevicePrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HpnicfWIPSCtmDevicePrecedence_Type.__name__=_F
_HpnicfWIPSCtmDevicePrecedence_Object=MibTableColumn
hpnicfWIPSCtmDevicePrecedence=_HpnicfWIPSCtmDevicePrecedence_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,15,1,8),_HpnicfWIPSCtmDevicePrecedence_Type())
hpnicfWIPSCtmDevicePrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSCtmDevicePrecedence.setStatus(_A)
_HpnicfWIPSMalPktStatTable_Object=MibTable
hpnicfWIPSMalPktStatTable=_HpnicfWIPSMalPktStatTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16))
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatTable.setStatus(_A)
_HpnicfWIPSMalPktStatEntry_Object=MibTableRow
hpnicfWIPSMalPktStatEntry=_HpnicfWIPSMalPktStatEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1))
hpnicfWIPSMalPktStatEntry.setIndexNames((0,_E,_Ab))
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatEntry.setStatus(_A)
class _HpnicfWIPSMalPktStatSensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfWIPSMalPktStatSensorName_Type.__name__=_H
_HpnicfWIPSMalPktStatSensorName_Object=MibTableColumn
hpnicfWIPSMalPktStatSensorName=_HpnicfWIPSMalPktStatSensorName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,1),_HpnicfWIPSMalPktStatSensorName_Type())
hpnicfWIPSMalPktStatSensorName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatSensorName.setStatus(_A)
class _HpnicfWIPSMalPktStatInvalidIELength_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatInvalidIELength_Type.__name__=_D
_HpnicfWIPSMalPktStatInvalidIELength_Object=MibTableColumn
hpnicfWIPSMalPktStatInvalidIELength=_HpnicfWIPSMalPktStatInvalidIELength_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,2),_HpnicfWIPSMalPktStatInvalidIELength_Type())
hpnicfWIPSMalPktStatInvalidIELength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatInvalidIELength.setStatus(_A)
class _HpnicfWIPSMalPktStatDuplicatedIE_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatDuplicatedIE_Type.__name__=_D
_HpnicfWIPSMalPktStatDuplicatedIE_Object=MibTableColumn
hpnicfWIPSMalPktStatDuplicatedIE=_HpnicfWIPSMalPktStatDuplicatedIE_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,3),_HpnicfWIPSMalPktStatDuplicatedIE_Type())
hpnicfWIPSMalPktStatDuplicatedIE.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatDuplicatedIE.setStatus(_A)
class _HpnicfWIPSMalPktStatRedundantIE_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatRedundantIE_Type.__name__=_D
_HpnicfWIPSMalPktStatRedundantIE_Object=MibTableColumn
hpnicfWIPSMalPktStatRedundantIE=_HpnicfWIPSMalPktStatRedundantIE_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,4),_HpnicfWIPSMalPktStatRedundantIE_Type())
hpnicfWIPSMalPktStatRedundantIE.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatRedundantIE.setStatus(_A)
class _HpnicfWIPSMalPktStatInvalidPktLength_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatInvalidPktLength_Type.__name__=_D
_HpnicfWIPSMalPktStatInvalidPktLength_Object=MibTableColumn
hpnicfWIPSMalPktStatInvalidPktLength=_HpnicfWIPSMalPktStatInvalidPktLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,5),_HpnicfWIPSMalPktStatInvalidPktLength_Type())
hpnicfWIPSMalPktStatInvalidPktLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatInvalidPktLength.setStatus(_A)
class _HpnicfWIPSMalPktStatIllegalIBSSESS_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatIllegalIBSSESS_Type.__name__=_D
_HpnicfWIPSMalPktStatIllegalIBSSESS_Object=MibTableColumn
hpnicfWIPSMalPktStatIllegalIBSSESS=_HpnicfWIPSMalPktStatIllegalIBSSESS_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,6),_HpnicfWIPSMalPktStatIllegalIBSSESS_Type())
hpnicfWIPSMalPktStatIllegalIBSSESS.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatIllegalIBSSESS.setStatus(_A)
class _HpnicfWIPSMalPktStatInvalidSourceAddr_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatInvalidSourceAddr_Type.__name__=_D
_HpnicfWIPSMalPktStatInvalidSourceAddr_Object=MibTableColumn
hpnicfWIPSMalPktStatInvalidSourceAddr=_HpnicfWIPSMalPktStatInvalidSourceAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,7),_HpnicfWIPSMalPktStatInvalidSourceAddr_Type())
hpnicfWIPSMalPktStatInvalidSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatInvalidSourceAddr.setStatus(_A)
class _HpnicfWIPSMalPktStatOverflowEAPOLKey_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatOverflowEAPOLKey_Type.__name__=_D
_HpnicfWIPSMalPktStatOverflowEAPOLKey_Object=MibTableColumn
hpnicfWIPSMalPktStatOverflowEAPOLKey=_HpnicfWIPSMalPktStatOverflowEAPOLKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,8),_HpnicfWIPSMalPktStatOverflowEAPOLKey_Type())
hpnicfWIPSMalPktStatOverflowEAPOLKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatOverflowEAPOLKey.setStatus(_A)
class _HpnicfWIPSMalPktStatMalAuth_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatMalAuth_Type.__name__=_D
_HpnicfWIPSMalPktStatMalAuth_Object=MibTableColumn
hpnicfWIPSMalPktStatMalAuth=_HpnicfWIPSMalPktStatMalAuth_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,9),_HpnicfWIPSMalPktStatMalAuth_Type())
hpnicfWIPSMalPktStatMalAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatMalAuth.setStatus(_A)
class _HpnicfWIPSMalPktStatMalAssoReq_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatMalAssoReq_Type.__name__=_D
_HpnicfWIPSMalPktStatMalAssoReq_Object=MibTableColumn
hpnicfWIPSMalPktStatMalAssoReq=_HpnicfWIPSMalPktStatMalAssoReq_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,10),_HpnicfWIPSMalPktStatMalAssoReq_Type())
hpnicfWIPSMalPktStatMalAssoReq.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatMalAssoReq.setStatus(_A)
class _HpnicfWIPSMalPktStatMalHTIE_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatMalHTIE_Type.__name__=_D
_HpnicfWIPSMalPktStatMalHTIE_Object=MibTableColumn
hpnicfWIPSMalPktStatMalHTIE=_HpnicfWIPSMalPktStatMalHTIE_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,11),_HpnicfWIPSMalPktStatMalHTIE_Type())
hpnicfWIPSMalPktStatMalHTIE.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatMalHTIE.setStatus(_A)
class _HpnicfWIPSMalPktStatLargeDuration_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatLargeDuration_Type.__name__=_D
_HpnicfWIPSMalPktStatLargeDuration_Object=MibTableColumn
hpnicfWIPSMalPktStatLargeDuration=_HpnicfWIPSMalPktStatLargeDuration_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,12),_HpnicfWIPSMalPktStatLargeDuration_Type())
hpnicfWIPSMalPktStatLargeDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatLargeDuration.setStatus(_A)
class _HpnicfWIPSMalPktStatNULLProbeRes_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatNULLProbeRes_Type.__name__=_D
_HpnicfWIPSMalPktStatNULLProbeRes_Object=MibTableColumn
hpnicfWIPSMalPktStatNULLProbeRes=_HpnicfWIPSMalPktStatNULLProbeRes_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,13),_HpnicfWIPSMalPktStatNULLProbeRes_Type())
hpnicfWIPSMalPktStatNULLProbeRes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatNULLProbeRes.setStatus(_A)
class _HpnicfWIPSMalPktStatInvalidDeAuthCode_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatInvalidDeAuthCode_Type.__name__=_D
_HpnicfWIPSMalPktStatInvalidDeAuthCode_Object=MibTableColumn
hpnicfWIPSMalPktStatInvalidDeAuthCode=_HpnicfWIPSMalPktStatInvalidDeAuthCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,14),_HpnicfWIPSMalPktStatInvalidDeAuthCode_Type())
hpnicfWIPSMalPktStatInvalidDeAuthCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatInvalidDeAuthCode.setStatus(_A)
class _HpnicfWIPSMalPktStatInvalidDisAssoCode_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatInvalidDisAssoCode_Type.__name__=_D
_HpnicfWIPSMalPktStatInvalidDisAssoCode_Object=MibTableColumn
hpnicfWIPSMalPktStatInvalidDisAssoCode=_HpnicfWIPSMalPktStatInvalidDisAssoCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,15),_HpnicfWIPSMalPktStatInvalidDisAssoCode_Type())
hpnicfWIPSMalPktStatInvalidDisAssoCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatInvalidDisAssoCode.setStatus(_A)
class _HpnicfWIPSMalPktStatOverflowSSID_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatOverflowSSID_Type.__name__=_D
_HpnicfWIPSMalPktStatOverflowSSID_Object=MibTableColumn
hpnicfWIPSMalPktStatOverflowSSID=_HpnicfWIPSMalPktStatOverflowSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,16),_HpnicfWIPSMalPktStatOverflowSSID_Type())
hpnicfWIPSMalPktStatOverflowSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatOverflowSSID.setStatus(_A)
class _HpnicfWIPSMalPktStatFatajack_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatFatajack_Type.__name__=_D
_HpnicfWIPSMalPktStatFatajack_Object=MibTableColumn
hpnicfWIPSMalPktStatFatajack=_HpnicfWIPSMalPktStatFatajack_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,17),_HpnicfWIPSMalPktStatFatajack_Type())
hpnicfWIPSMalPktStatFatajack.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatFatajack.setStatus(_A)
class _HpnicfWIPSMalPktStatInvalidChannel_Type(Counter64):defaultValue=0
_HpnicfWIPSMalPktStatInvalidChannel_Type.__name__=_D
_HpnicfWIPSMalPktStatInvalidChannel_Object=MibTableColumn
hpnicfWIPSMalPktStatInvalidChannel=_HpnicfWIPSMalPktStatInvalidChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,16,1,18),_HpnicfWIPSMalPktStatInvalidChannel_Type())
hpnicfWIPSMalPktStatInvalidChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSMalPktStatInvalidChannel.setStatus(_A)
_HpnicfWIPSDctUnassocStaTable_Object=MibTable
hpnicfWIPSDctUnassocStaTable=_HpnicfWIPSDctUnassocStaTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17))
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaTable.setStatus(_A)
_HpnicfWIPSDctUnassocStaEntry_Object=MibTableRow
hpnicfWIPSDctUnassocStaEntry=_HpnicfWIPSDctUnassocStaEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1))
hpnicfWIPSDctUnassocStaEntry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaEntry.setStatus(_A)
class _HpnicfWIPSDctUnassocStaVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfWIPSDctUnassocStaVSD_Type.__name__=_H
_HpnicfWIPSDctUnassocStaVSD_Object=MibTableColumn
hpnicfWIPSDctUnassocStaVSD=_HpnicfWIPSDctUnassocStaVSD_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,1),_HpnicfWIPSDctUnassocStaVSD_Type())
hpnicfWIPSDctUnassocStaVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaVSD.setStatus(_A)
_HpnicfWIPSDctUnassocStaMac_Type=MacAddress
_HpnicfWIPSDctUnassocStaMac_Object=MibTableColumn
hpnicfWIPSDctUnassocStaMac=_HpnicfWIPSDctUnassocStaMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,2),_HpnicfWIPSDctUnassocStaMac_Type())
hpnicfWIPSDctUnassocStaMac.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaMac.setStatus(_A)
_HpnicfWIPSDctUnassocStaCategory_Type=HpnicfWIPSClientCategoryType
_HpnicfWIPSDctUnassocStaCategory_Object=MibTableColumn
hpnicfWIPSDctUnassocStaCategory=_HpnicfWIPSDctUnassocStaCategory_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,3),_HpnicfWIPSDctUnassocStaCategory_Type())
hpnicfWIPSDctUnassocStaCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaCategory.setStatus(_A)
_HpnicfWIPSDctUnassocStaRadioType_Type=Unsigned32
_HpnicfWIPSDctUnassocStaRadioType_Object=MibTableColumn
hpnicfWIPSDctUnassocStaRadioType=_HpnicfWIPSDctUnassocStaRadioType_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,4),_HpnicfWIPSDctUnassocStaRadioType_Type())
hpnicfWIPSDctUnassocStaRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaRadioType.setStatus(_A)
_HpnicfWIPSDctUnassocStaIsCountered_Type=TruthValue
_HpnicfWIPSDctUnassocStaIsCountered_Object=MibTableColumn
hpnicfWIPSDctUnassocStaIsCountered=_HpnicfWIPSDctUnassocStaIsCountered_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,5),_HpnicfWIPSDctUnassocStaIsCountered_Type())
hpnicfWIPSDctUnassocStaIsCountered.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaIsCountered.setStatus(_A)
class _HpnicfWIPSDctUnassocStaAdd2BlackList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctUnassocStaAdd2BlackList_Type.__name__=_K
_HpnicfWIPSDctUnassocStaAdd2BlackList_Object=MibTableColumn
hpnicfWIPSDctUnassocStaAdd2BlackList=_HpnicfWIPSDctUnassocStaAdd2BlackList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,6),_HpnicfWIPSDctUnassocStaAdd2BlackList_Type())
hpnicfWIPSDctUnassocStaAdd2BlackList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaAdd2BlackList.setStatus(_A)
class _HpnicfWIPSDctUnassocStaAdd2WhiteList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctUnassocStaAdd2WhiteList_Type.__name__=_K
_HpnicfWIPSDctUnassocStaAdd2WhiteList_Object=MibTableColumn
hpnicfWIPSDctUnassocStaAdd2WhiteList=_HpnicfWIPSDctUnassocStaAdd2WhiteList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,7),_HpnicfWIPSDctUnassocStaAdd2WhiteList_Type())
hpnicfWIPSDctUnassocStaAdd2WhiteList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaAdd2WhiteList.setStatus(_A)
class _HpnicfWIPSDctUnassocStaAdd2IgnoreList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctUnassocStaAdd2IgnoreList_Type.__name__=_K
_HpnicfWIPSDctUnassocStaAdd2IgnoreList_Object=MibTableColumn
hpnicfWIPSDctUnassocStaAdd2IgnoreList=_HpnicfWIPSDctUnassocStaAdd2IgnoreList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,8),_HpnicfWIPSDctUnassocStaAdd2IgnoreList_Type())
hpnicfWIPSDctUnassocStaAdd2IgnoreList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaAdd2IgnoreList.setStatus(_A)
class _HpnicfWIPSDctUnassocStaAdd2CtmList_Type(TruthValue):defaultValue=2
_HpnicfWIPSDctUnassocStaAdd2CtmList_Type.__name__=_K
_HpnicfWIPSDctUnassocStaAdd2CtmList_Object=MibTableColumn
hpnicfWIPSDctUnassocStaAdd2CtmList=_HpnicfWIPSDctUnassocStaAdd2CtmList_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,9),_HpnicfWIPSDctUnassocStaAdd2CtmList_Type())
hpnicfWIPSDctUnassocStaAdd2CtmList.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaAdd2CtmList.setStatus(_A)
_HpnicfWIPSDctUnassocStaFirstDctTm_Type=TimeTicks
_HpnicfWIPSDctUnassocStaFirstDctTm_Object=MibTableColumn
hpnicfWIPSDctUnassocStaFirstDctTm=_HpnicfWIPSDctUnassocStaFirstDctTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,10),_HpnicfWIPSDctUnassocStaFirstDctTm_Type())
hpnicfWIPSDctUnassocStaFirstDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaFirstDctTm.setStatus(_A)
_HpnicfWIPSDctUnassocStaLastDctTm_Type=TimeTicks
_HpnicfWIPSDctUnassocStaLastDctTm_Object=MibTableColumn
hpnicfWIPSDctUnassocStaLastDctTm=_HpnicfWIPSDctUnassocStaLastDctTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,11),_HpnicfWIPSDctUnassocStaLastDctTm_Type())
hpnicfWIPSDctUnassocStaLastDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaLastDctTm.setStatus(_A)
_HpnicfWIPSDctUnassocStaRptSensorNum_Type=Integer32
_HpnicfWIPSDctUnassocStaRptSensorNum_Object=MibTableColumn
hpnicfWIPSDctUnassocStaRptSensorNum=_HpnicfWIPSDctUnassocStaRptSensorNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,12),_HpnicfWIPSDctUnassocStaRptSensorNum_Type())
hpnicfWIPSDctUnassocStaRptSensorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaRptSensorNum.setStatus(_A)
class _HpnicfWIPSDctUnassocStaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_AF,1),(_AG,2),(_AH,3),(_AI,4),(_AJ,5),(_AK,6),(_AL,7)))
_HpnicfWIPSDctUnassocStaState_Type.__name__=_F
_HpnicfWIPSDctUnassocStaState_Object=MibTableColumn
hpnicfWIPSDctUnassocStaState=_HpnicfWIPSDctUnassocStaState_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,13),_HpnicfWIPSDctUnassocStaState_Type())
hpnicfWIPSDctUnassocStaState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaState.setStatus(_A)
class _HpnicfWIPSDctUnassocStaVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfWIPSDctUnassocStaVendor_Type.__name__=_H
_HpnicfWIPSDctUnassocStaVendor_Object=MibTableColumn
hpnicfWIPSDctUnassocStaVendor=_HpnicfWIPSDctUnassocStaVendor_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,17,1,14),_HpnicfWIPSDctUnassocStaVendor_Type())
hpnicfWIPSDctUnassocStaVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaVendor.setStatus(_A)
_HpnicfWIPSDctUnassocStaRptSensorTable_Object=MibTable
hpnicfWIPSDctUnassocStaRptSensorTable=_HpnicfWIPSDctUnassocStaRptSensorTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,18))
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaRptSensorTable.setStatus(_A)
_HpnicfWIPSDctUnassocStaRptSensorEntry_Object=MibTableRow
hpnicfWIPSDctUnassocStaRptSensorEntry=_HpnicfWIPSDctUnassocStaRptSensorEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,18,1))
hpnicfWIPSDctUnassocStaRptSensorEntry.setIndexNames((0,_E,_g),(0,_E,_h),(0,_E,_Ac))
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaRptSensorEntry.setStatus(_A)
class _HpnicfWIPSDctUnassocStaRtpSensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfWIPSDctUnassocStaRtpSensorName_Type.__name__=_H
_HpnicfWIPSDctUnassocStaRtpSensorName_Object=MibTableColumn
hpnicfWIPSDctUnassocStaRtpSensorName=_HpnicfWIPSDctUnassocStaRtpSensorName_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,18,1,1),_HpnicfWIPSDctUnassocStaRtpSensorName_Type())
hpnicfWIPSDctUnassocStaRtpSensorName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaRtpSensorName.setStatus(_A)
class _HpnicfWIPSDctUnassocStaRptSensorRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HpnicfWIPSDctUnassocStaRptSensorRadioId_Type.__name__=_F
_HpnicfWIPSDctUnassocStaRptSensorRadioId_Object=MibTableColumn
hpnicfWIPSDctUnassocStaRptSensorRadioId=_HpnicfWIPSDctUnassocStaRptSensorRadioId_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,18,1,2),_HpnicfWIPSDctUnassocStaRptSensorRadioId_Type())
hpnicfWIPSDctUnassocStaRptSensorRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaRptSensorRadioId.setStatus(_A)
_HpnicfWIPSDctUnassocStaRptRSSI_Type=Integer32
_HpnicfWIPSDctUnassocStaRptRSSI_Object=MibTableColumn
hpnicfWIPSDctUnassocStaRptRSSI=_HpnicfWIPSDctUnassocStaRptRSSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,18,1,3),_HpnicfWIPSDctUnassocStaRptRSSI_Type())
hpnicfWIPSDctUnassocStaRptRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaRptRSSI.setStatus(_A)
_HpnicfWIPSDctUnassocStaLastRptTm_Type=TimeTicks
_HpnicfWIPSDctUnassocStaLastRptTm_Object=MibTableColumn
hpnicfWIPSDctUnassocStaLastRptTm=_HpnicfWIPSDctUnassocStaLastRptTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,118,2,18,1,4),_HpnicfWIPSDctUnassocStaLastRptTm_Type())
hpnicfWIPSDctUnassocStaLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfWIPSDctUnassocStaLastRptTm.setStatus(_A)
_HpnicfWIPSNotifyGroup_ObjectIdentity=ObjectIdentity
hpnicfWIPSNotifyGroup=_HpnicfWIPSNotifyGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,118,3))
mibBuilder.exportSymbols(_E,**{'HpnicfWIPSRadioType':HpnicfWIPSRadioType,'HpnicfWIPSDevStatus':HpnicfWIPSDevStatus,_AC:HpnicfWIPSDevCategoryWay,'HpnicfWIPSDeviceCategoryType':HpnicfWIPSDeviceCategoryType,'HpnicfWIPSAPCategoryType':HpnicfWIPSAPCategoryType,'HpnicfWIPSClientCategoryType':HpnicfWIPSClientCategoryType,'HpnicfWIPSChannel':HpnicfWIPSChannel,'HpnicfWIPSEncryptMethod':HpnicfWIPSEncryptMethod,'HpnicfWIPSAuthMethod':HpnicfWIPSAuthMethod,'HpnicfWIPSAPClassifyType':HpnicfWIPSAPClassifyType,_y:HpnicfWIPSAPSecurityType,'hpnicfWIPS':hpnicfWIPS,'hpnicfWIPSConfigGroup':hpnicfWIPSConfigGroup,'hpnicfWIPSGlobalConfigGroup':hpnicfWIPSGlobalConfigGroup,'hpnicfWIPSEnable':hpnicfWIPSEnable,'hpnicfWIPSSensorLicenseNum':hpnicfWIPSSensorLicenseNum,'hpnicfWIPSBlocklistAction':hpnicfWIPSBlocklistAction,'hpnicfWIPSAPInactiveTime':hpnicfWIPSAPInactiveTime,'hpnicfWIPSSTAInactiveTime':hpnicfWIPSSTAInactiveTime,'hpnicfWIPSDevAgingTime':hpnicfWIPSDevAgingTime,'hpnicfWIPSStatisticPeriod':hpnicfWIPSStatisticPeriod,'hpnicfWIPSReclassificationPeriod':hpnicfWIPSReclassificationPeriod,'hpnicfWIPSResetAllTrustList':hpnicfWIPSResetAllTrustList,'hpnicfWIPSResetAllBlockList':hpnicfWIPSResetAllBlockList,'hpnicfWIPSResetAllIgnoreList':hpnicfWIPSResetAllIgnoreList,'hpnicfWIPSResetAllCtmList':hpnicfWIPSResetAllCtmList,'hpnicfWIPSPermitChlBitMap':hpnicfWIPSPermitChlBitMap,'hpnicfWIPSDynamicTrustListAgingTime':hpnicfWIPSDynamicTrustListAgingTime,'hpnicfWIPSDevUpdateTime':hpnicfWIPSDevUpdateTime,'hpnicfWIPSADOSEnable':hpnicfWIPSADOSEnable,'hpnicfWIPSAccessFlowScanEnable':hpnicfWIPSAccessFlowScanEnable,'hpnicfWIPSVsdConfigGroup':hpnicfWIPSVsdConfigGroup,'hpnicfWIPSVsdTable':hpnicfWIPSVsdTable,'hpnicfWIPSVsdEntry':hpnicfWIPSVsdEntry,_N:hpnicfWIPSVsdNameCfg,'hpnicfWIPSVsdRowStatus':hpnicfWIPSVsdRowStatus,'hpnicfWIPSVsdAtkDctPolicyNameCfg':hpnicfWIPSVsdAtkDctPolicyNameCfg,'hpnicfWIPSVsdCtmPolicyNameCfg':hpnicfWIPSVsdCtmPolicyNameCfg,'hpnicfWIPSVsdSigPolicyNameCfg':hpnicfWIPSVsdSigPolicyNameCfg,'hpnicfWIPSVsdMalPktPolicyNameCfg':hpnicfWIPSVsdMalPktPolicyNameCfg,'hpnicfWIPSRule2VsdTable':hpnicfWIPSRule2VsdTable,'hpnicfWIPSRule2VsdEntry':hpnicfWIPSRule2VsdEntry,_p:hpnicfWIPSRule2VsdAPClaRuleNameCfg,'hpnicfWIPSRule2VsdRowStatus':hpnicfWIPSRule2VsdRowStatus,'hpnicfWIPSRule2VsdPrecedence':hpnicfWIPSRule2VsdPrecedence,'hpnicfWIPSSensor2VsdTable':hpnicfWIPSSensor2VsdTable,'hpnicfWIPSSensor2VsdEntry':hpnicfWIPSSensor2VsdEntry,_V:hpnicfWIPSSensorNameCfg,'hpnicfWIPSSensor2VsdRowStatus':hpnicfWIPSSensor2VsdRowStatus,'hpnicfWIPSSensorState':hpnicfWIPSSensorState,'hpnicfWIPSSensorRadioTable':hpnicfWIPSSensorRadioTable,'hpnicfWIPSSensorRadioEntry':hpnicfWIPSSensorRadioEntry,_q:hpnicfWIPSSensorRadioRadioId,'hpnicfWIPSSensorRadioScanMode':hpnicfWIPSSensorRadioScanMode,'hpnicfWIPSAPClaRuleTable':hpnicfWIPSAPClaRuleTable,'hpnicfWIPSAPClaRuleEntry':hpnicfWIPSAPClaRuleEntry,_v:hpnicfWIPSAPClaRuleName,'hpnicfWIPSAPClaRowStatus':hpnicfWIPSAPClaRowStatus,'hpnicfWIPSAPClaSeverityLevel':hpnicfWIPSAPClaSeverityLevel,'hpnicfWIPSAPClaRuleMatchAll':hpnicfWIPSAPClaRuleMatchAll,'hpnicfWIPSAPClaType':hpnicfWIPSAPClaType,'hpnicfWIPSAPClaSubRuleSSIDOperator':hpnicfWIPSAPClaSubRuleSSIDOperator,'hpnicfWIPSAPClaSubRuleSSIDCase':hpnicfWIPSAPClaSubRuleSSIDCase,'hpnicfWIPSAPClaSubRuleSSID':hpnicfWIPSAPClaSubRuleSSID,'hpnicfWIPSSecurityType':hpnicfWIPSSecurityType,'hpnicfWIPSSecurityTypeMatch':hpnicfWIPSSecurityTypeMatch,'hpnicfWIPSAPAuthType':hpnicfWIPSAPAuthType,'hpnicfWIPSMaxRSSIValue':hpnicfWIPSMaxRSSIValue,'hpnicfWIPSMinRSSIValue':hpnicfWIPSMinRSSIValue,'hpnicfWIPSMaxDuration':hpnicfWIPSMaxDuration,'hpnicfWIPSMinDuration':hpnicfWIPSMinDuration,'hpnicfWIPSMaxAPNum':hpnicfWIPSMaxAPNum,'hpnicfWIPSMinAPNum':hpnicfWIPSMinAPNum,'hpnicfWIPSMaxClientNum':hpnicfWIPSMaxClientNum,'hpnicfWIPSMinClientNum':hpnicfWIPSMinClientNum,'hpnicfWIPSOUIInfo':hpnicfWIPSOUIInfo,'hpnicfWIPSVendorInfo':hpnicfWIPSVendorInfo,'hpnicfWIPSAPAuthTypeMatch':hpnicfWIPSAPAuthTypeMatch,'hpnicfWIPSAtkDctPolicyCfgGroup':hpnicfWIPSAtkDctPolicyCfgGroup,'hpnicfWIPSAtkDctPolicyCfgSupportSet':hpnicfWIPSAtkDctPolicyCfgSupportSet,'hpnicfWIPSAtkDctPolicyCfgTable':hpnicfWIPSAtkDctPolicyCfgTable,'hpnicfWIPSAtkDctPolicyCfgEntry':hpnicfWIPSAtkDctPolicyCfgEntry,_z:hpnicfWIPSAtkDctPolicyName,'hpnicfWIPSAtkDctPolicyCfgRowStatus':hpnicfWIPSAtkDctPolicyCfgRowStatus,'hpnicfWIPSAtkDctPolicyBitString':hpnicfWIPSAtkDctPolicyBitString,'hpnicfWIPSAtkDctPolicyAPFloodQT':hpnicfWIPSAtkDctPolicyAPFloodQT,'hpnicfWIPSAtkDctPolicyAPSpoofQT':hpnicfWIPSAtkDctPolicyAPSpoofQT,'hpnicfWIPSAtkDctPolicyCliSpoofQT':hpnicfWIPSAtkDctPolicyCliSpoofQT,'hpnicfWIPSAtkDctPolicyDosAssoQT':hpnicfWIPSAtkDctPolicyDosAssoQT,'hpnicfWIPSAtkDctPolicyDosAuthQT':hpnicfWIPSAtkDctPolicyDosAuthQT,'hpnicfWIPSAtkDctPolicyDosEAPOLStartQT':hpnicfWIPSAtkDctPolicyDosEAPOLStartQT,'hpnicfWIPSAtkDctPolicyDosReAssoQT':hpnicfWIPSAtkDctPolicyDosReAssoQT,'hpnicfWIPSAtkDctPolicyWeakIVQT':hpnicfWIPSAtkDctPolicyWeakIVQT,'hpnicfWIPSAtkDctPolicyInvalidOUIAction':hpnicfWIPSAtkDctPolicyInvalidOUIAction,'hpnicfWIPSAtkDctPolicyUnencryptedAuthApQT':hpnicfWIPSAtkDctPolicyUnencryptedAuthApQT,'hpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT':hpnicfWIPSAtkDctPolicyUnencryptedAuthClientQT,'hpnicfWIPSAtkDctPolicyPSAttackQT':hpnicfWIPSAtkDctPolicyPSAttackQT,'hpnicfWIPSAtkDctPolicyPSAttackMinOffPacket':hpnicfWIPSAtkDctPolicyPSAttackMinOffPacket,'hpnicfWIPSAtkDctPolicyPSAttackOnOffPercent':hpnicfWIPSAtkDctPolicyPSAttackOnOffPercent,'hpnicfWIPSAtkDctPolicyApImpersonationQT':hpnicfWIPSAtkDctPolicyApImpersonationQT,'hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold':hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncThreshold,'hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime':hpnicfWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime,'hpnicfWIPSAtkDctPolicySoftApConvertTime':hpnicfWIPSAtkDctPolicySoftApConvertTime,'hpnicfWIPSStaticCtmListCfgTable':hpnicfWIPSStaticCtmListCfgTable,'hpnicfWIPSStaticCtmListCfgEntry':hpnicfWIPSStaticCtmListCfgEntry,_A0:hpnicfWIPSStaticCtmListMAC,'hpnicfWIPSStaticCtmListRowStatus':hpnicfWIPSStaticCtmListRowStatus,'hpnicfWIPSStaticBlockListCfgTable':hpnicfWIPSStaticBlockListCfgTable,'hpnicfWIPSStaticBlockListCfgEntry':hpnicfWIPSStaticBlockListCfgEntry,_A1:hpnicfWIPSStaticBlockListMAC,'hpnicfWIPSStaticBlockListRowStatus':hpnicfWIPSStaticBlockListRowStatus,'hpnicfWIPSStaticTrustListCfgTable':hpnicfWIPSStaticTrustListCfgTable,'hpnicfWIPSStaticTrustListCfgEntry':hpnicfWIPSStaticTrustListCfgEntry,_A2:hpnicfWIPSStaticTrustListMAC,'hpnicfWIPSStaticTrustListRowStatus':hpnicfWIPSStaticTrustListRowStatus,'hpnicfWIPSIgnoreListCfgTable':hpnicfWIPSIgnoreListCfgTable,'hpnicfWIPSIgnoreListCfgEntry':hpnicfWIPSIgnoreListCfgEntry,_A3:hpnicfWIPSIgnoreListMAC,'hpnicfWIPSIgnoreListRowStatus':hpnicfWIPSIgnoreListRowStatus,'hpnicfWIPSDctModeTable':hpnicfWIPSDctModeTable,'hpnicfWIPSDctModeEntry':hpnicfWIPSDctModeEntry,_A4:hpnicfWIPSDctModeAPName,_A5:hpnicfWIPSDctModeRadio,'hpnicfWIPSDctModeScanMode':hpnicfWIPSDctModeScanMode,'hpnicfWIPSDctModeRowStatus':hpnicfWIPSDctModeRowStatus,'hpnicfWIPSSigConfigGroup':hpnicfWIPSSigConfigGroup,'hpnicfWIPSSigPolicyTable':hpnicfWIPSSigPolicyTable,'hpnicfWIPSSigPolicyEntry':hpnicfWIPSSigPolicyEntry,_W:hpnicfWIPSSigPolicyNameCfg,'hpnicfWIPSSigPolicyRowStatus':hpnicfWIPSSigPolicyRowStatus,'hpnicfWIPSSigRule2PolicyTable':hpnicfWIPSSigRule2PolicyTable,'hpnicfWIPSSigRule2PolicyEntry':hpnicfWIPSSigRule2PolicyEntry,_A6:hpnicfWIPSSigRule2PolicySigRuleIDCfg,'hpnicfWIPSSigRule2PolicyRowStatus':hpnicfWIPSSigRule2PolicyRowStatus,'hpnicfWIPSSigRule2PolicyPrecedence':hpnicfWIPSSigRule2PolicyPrecedence,'hpnicfWIPSSigRuleTable':hpnicfWIPSSigRuleTable,'hpnicfWIPSSigRuleEntry':hpnicfWIPSSigRuleEntry,_X:hpnicfWIPSSigRuleName,'hpnicfWIPSSigRuleID':hpnicfWIPSSigRuleID,'hpnicfWIPSSigRuleRowStatus':hpnicfWIPSSigRuleRowStatus,'hpnicfWIPSSigSubRuleMatchAll':hpnicfWIPSSigSubRuleMatchAll,'hpnicfWIPSSigRuleDctPeriod':hpnicfWIPSSigRuleDctPeriod,'hpnicfWIPSSigRuleTrackMethod':hpnicfWIPSSigRuleTrackMethod,'hpnicfWIPSSigRuleDctThresholdPerMAC':hpnicfWIPSSigRuleDctThresholdPerMAC,'hpnicfWIPSSigRuleDctThresholdPerSig':hpnicfWIPSSigRuleDctThresholdPerSig,'hpnicfWIPSSigRuleActionEvtLevel':hpnicfWIPSSigRuleActionEvtLevel,'hpnicfWIPSSigRuleQuietTime':hpnicfWIPSSigRuleQuietTime,'hpnicfWIPSSigSubRuleFrameType':hpnicfWIPSSigSubRuleFrameType,'hpnicfWIPSSigSubRuleFrameSubType':hpnicfWIPSSigSubRuleFrameSubType,'hpnicfWIPSSigSubRuleMac':hpnicfWIPSSigSubRuleMac,'hpnicfWIPSSigSubRuleMacType':hpnicfWIPSSigSubRuleMacType,'hpnicfWIPSSigSubRuleSeqNumMin':hpnicfWIPSSigSubRuleSeqNumMin,'hpnicfWIPSSigSubRuleSeqNumMax':hpnicfWIPSSigSubRuleSeqNumMax,'hpnicfWIPSSigSubRuleSSIDLenMin':hpnicfWIPSSigSubRuleSSIDLenMin,'hpnicfWIPSSigSubRuleSSIDLenMax':hpnicfWIPSSigSubRuleSSIDLenMax,'hpnicfWIPSSigSubRuleSSID':hpnicfWIPSSigSubRuleSSID,'hpnicfWIPSSigSubRuleSSIDOpe':hpnicfWIPSSigSubRuleSSIDOpe,'hpnicfWIPSSigSubRuleSSIDCase':hpnicfWIPSSigSubRuleSSIDCase,'hpnicfWIPSSigSubRulePatternTable':hpnicfWIPSSigSubRulePatternTable,'hpnicfWIPSSigSubRulePatternEntry':hpnicfWIPSSigSubRulePatternEntry,_A7:hpnicfWIPSSigSubRulePatternID,'hpnicfWIPSSigSubRuleRowStatus':hpnicfWIPSSigSubRuleRowStatus,'hpnicfWIPSSigSubRulePatternName':hpnicfWIPSSigSubRulePatternName,'hpnicfWIPSSigSubRulePatternOffset':hpnicfWIPSSigSubRulePatternOffset,'hpnicfWIPSSigSubRulePatternMask':hpnicfWIPSSigSubRulePatternMask,'hpnicfWIPSSigSubRulePatternValueMin':hpnicfWIPSSigSubRulePatternValueMin,'hpnicfWIPSSigSubRulePatternValueMax':hpnicfWIPSSigSubRulePatternValueMax,'hpnicfWIPSSigSubRulePatternFromPayload':hpnicfWIPSSigSubRulePatternFromPayload,'hpnicfWIPSCtmConfigGroup':hpnicfWIPSCtmConfigGroup,'hpnicfWIPSCtmPolicyCfgSupportSet':hpnicfWIPSCtmPolicyCfgSupportSet,'hpnicfWIPSCtmPolicyTable':hpnicfWIPSCtmPolicyTable,'hpnicfWIPSCtmPolicyEntry':hpnicfWIPSCtmPolicyEntry,_Y:hpnicfWIPSCtmPolicyName,'hpnicfWIPSCtmPolicyCfgRowStatus':hpnicfWIPSCtmPolicyCfgRowStatus,'hpnicfWIPSCtmPolicyBitString':hpnicfWIPSCtmPolicyBitString,'hpnicfWIPSCtmPolicyFixedChl':hpnicfWIPSCtmPolicyFixedChl,'hpnicfWIPSCtmPolicyRogueAPPre':hpnicfWIPSCtmPolicyRogueAPPre,'hpnicfWIPSCtmPolicyPtRogueAPPre':hpnicfWIPSCtmPolicyPtRogueAPPre,'hpnicfWIPSCtmPolicyMisconfAPPre':hpnicfWIPSCtmPolicyMisconfAPPre,'hpnicfWIPSCtmPolicyExternalAPPre':hpnicfWIPSCtmPolicyExternalAPPre,'hpnicfWIPSCtmPolicyPtExternalAPPre':hpnicfWIPSCtmPolicyPtExternalAPPre,'hpnicfWIPSCtmPolicyUncateAPPre':hpnicfWIPSCtmPolicyUncateAPPre,'hpnicfWIPSCtmPolicyPtAuthAPPre':hpnicfWIPSCtmPolicyPtAuthAPPre,'hpnicfWIPSCtmPolicyMisassoStaPre':hpnicfWIPSCtmPolicyMisassoStaPre,'hpnicfWIPSCtmPolicyUncateStaPre':hpnicfWIPSCtmPolicyUncateStaPre,'hpnicfWIPSCtmPolicyUnauthStaPre':hpnicfWIPSCtmPolicyUnauthStaPre,'hpnicfWIPSCtmPolicyDevListTable':hpnicfWIPSCtmPolicyDevListTable,'hpnicfWIPSCtmPolicyDevListEntry':hpnicfWIPSCtmPolicyDevListEntry,_A8:hpnicfWIPSCtmPolicyDevMAC,'hpnicfWIPSCtmPolicyDevRowStatus':hpnicfWIPSCtmPolicyDevRowStatus,'hpnicfWIPSMalPktDctConfigGroup':hpnicfWIPSMalPktDctConfigGroup,'hpnicfWIPSMalPktDctCfgLogSupportSet':hpnicfWIPSMalPktDctCfgLogSupportSet,'hpnicfWIPSMalPktDctCfgTrapSupportSet':hpnicfWIPSMalPktDctCfgTrapSupportSet,'hpnicfWIPSMalPktDctPolicyTable':hpnicfWIPSMalPktDctPolicyTable,'hpnicfWIPSMalPktDctPolicyEntry':hpnicfWIPSMalPktDctPolicyEntry,_A9:hpnicfWIPSMalPktDctPolicyName,'hpnicfWIPSMalPktDctPolicyCfgRowStatus':hpnicfWIPSMalPktDctPolicyCfgRowStatus,'hpnicfWIPSMalPktDctPolicyLogBitString':hpnicfWIPSMalPktDctPolicyLogBitString,'hpnicfWIPSMalPktDctPolicyTrapBitString':hpnicfWIPSMalPktDctPolicyTrapBitString,'hpnicfWIPSMalPktDctPolicyDurationThreshold':hpnicfWIPSMalPktDctPolicyDurationThreshold,'hpnicfWIPSMalPktDctPolicyQuietTime':hpnicfWIPSMalPktDctPolicyQuietTime,'hpnicfWIPSStaticTrustOUIListCfgTable':hpnicfWIPSStaticTrustOUIListCfgTable,'hpnicfWIPSStaticTrustOUIListCfgEntry':hpnicfWIPSStaticTrustOUIListCfgEntry,_AA:hpnicfWIPSStaticTrustOUIListOUI,'hpnicfWIPSStaticTrustOUIListRowStatus':hpnicfWIPSStaticTrustOUIListRowStatus,'hpnicfWIPSStaticTrustVendorListCfgTable':hpnicfWIPSStaticTrustVendorListCfgTable,'hpnicfWIPSStaticTrustVendorListCfgEntry':hpnicfWIPSStaticTrustVendorListCfgEntry,_AB:hpnicfWIPSStaticTrustVendorListVendor,'hpnicfWIPSStaticTrustVendorListRowStatus':hpnicfWIPSStaticTrustVendorListRowStatus,'hpnicfWIPSDetectGroup':hpnicfWIPSDetectGroup,'hpnicfWIPSDctAPTable':hpnicfWIPSDctAPTable,'hpnicfWIPSDctAPEntry':hpnicfWIPSDctAPEntry,_Q:hpnicfWIPSDctAPVSD,_R:hpnicfWIPSDctAPBSSID,'hpnicfWIPSDctAPRunningTime':hpnicfWIPSDctAPRunningTime,'hpnicfWIPSDctAPRunTmLastUpdateTm':hpnicfWIPSDctAPRunTmLastUpdateTm,'hpnicfWIPSDctAPIsCountered':hpnicfWIPSDctAPIsCountered,'hpnicfWIPSDctAPWorkChannel':hpnicfWIPSDctAPWorkChannel,'hpnicfWIPSDctAPRadioType':hpnicfWIPSDctAPRadioType,'hpnicfWIPSDctAPAuthMethod':hpnicfWIPSDctAPAuthMethod,'hpnicfWIPSDctAPEncryptMethod':hpnicfWIPSDctAPEncryptMethod,'hpnicfWIPSDctAPSecurity':hpnicfWIPSDctAPSecurity,'hpnicfWIPSDctAPSeverityLevel':hpnicfWIPSDctAPSeverityLevel,'hpnicfWIPSDctAPLastDctTm':hpnicfWIPSDctAPLastDctTm,'hpnicfWIPSDctAPFirstDctTm':hpnicfWIPSDctAPFirstDctTm,'hpnicfWIPSDctAPAdd2BlackList':hpnicfWIPSDctAPAdd2BlackList,'hpnicfWIPSDctAPAdd2WhiteList':hpnicfWIPSDctAPAdd2WhiteList,'hpnicfWIPSDctAPAdd2IgnoreList':hpnicfWIPSDctAPAdd2IgnoreList,'hpnicfWIPSDctAPAdd2CtmList':hpnicfWIPSDctAPAdd2CtmList,'hpnicfWIPSDctAPCategory':hpnicfWIPSDctAPCategory,'hpnicfWIPSDctAPCategoryWay':hpnicfWIPSDctAPCategoryWay,'hpnicfWIPSDctAPStatus':hpnicfWIPSDctAPStatus,'hpnicfWIPSDctAPSSID':hpnicfWIPSDctAPSSID,'hpnicfWIPSDctAPAttachStaNum':hpnicfWIPSDctAPAttachStaNum,'hpnicfWIPSDctAPRptSensorNum':hpnicfWIPSDctAPRptSensorNum,'hpnicfWIPSDctAPVendor':hpnicfWIPSDctAPVendor,'hpnicfWIPSDctAPAttachStaTable':hpnicfWIPSDctAPAttachStaTable,'hpnicfWIPSDctAPAttachStaEntry':hpnicfWIPSDctAPAttachStaEntry,_AD:hpnicfWIPSDctAPAttachStaMac,'hpnicfWIPSDctAPAttachStaRowStatus':hpnicfWIPSDctAPAttachStaRowStatus,'hpnicfWIPSDctAPRptSensorTable':hpnicfWIPSDctAPRptSensorTable,'hpnicfWIPSDctAPRptSensorEntry':hpnicfWIPSDctAPRptSensorEntry,_AE:hpnicfWIPSDctAPRptSensorName,'hpnicfWIPSDctAPRptSensorRadioId':hpnicfWIPSDctAPRptSensorRadioId,'hpnicfWIPSDctAPRptRSSI':hpnicfWIPSDctAPRptRSSI,'hpnicfWIPSDctAPLastRptTm':hpnicfWIPSDctAPLastRptTm,'hpnicfWIPSDctStaTable':hpnicfWIPSDctStaTable,'hpnicfWIPSDctStaEntry':hpnicfWIPSDctStaEntry,_Z:hpnicfWIPSDctStaVSD,_a:hpnicfWIPSDctStaMac,'hpnicfWIPSDctStaAssocBSSID':hpnicfWIPSDctStaAssocBSSID,'hpnicfWIPSDctStaStatus':hpnicfWIPSDctStaStatus,'hpnicfWIPSDctStaCategory':hpnicfWIPSDctStaCategory,'hpnicfWIPSDctStaRadioType':hpnicfWIPSDctStaRadioType,'hpnicfWIPSDctStaWorkChannel':hpnicfWIPSDctStaWorkChannel,'hpnicfWIPSDctStaIsCountered':hpnicfWIPSDctStaIsCountered,'hpnicfWIPSDctStaAdd2BlackList':hpnicfWIPSDctStaAdd2BlackList,'hpnicfWIPSDctStaAdd2WhiteList':hpnicfWIPSDctStaAdd2WhiteList,'hpnicfWIPSDctStaAdd2IgnoreList':hpnicfWIPSDctStaAdd2IgnoreList,'hpnicfWIPSDctStaAdd2CtmList':hpnicfWIPSDctStaAdd2CtmList,'hpnicfWIPSDctStaFirstDctTm':hpnicfWIPSDctStaFirstDctTm,'hpnicfWIPSDctStaLastDctTm':hpnicfWIPSDctStaLastDctTm,'hpnicfWIPSDctStaRptSensorNum':hpnicfWIPSDctStaRptSensorNum,'hpnicfWIPSDctStaState':hpnicfWIPSDctStaState,'hpnicfWIPSDctStaVendor':hpnicfWIPSDctStaVendor,'hpnicfWIPSDctStaRptSensorTable':hpnicfWIPSDctStaRptSensorTable,'hpnicfWIPSDctStaRptSensorEntry':hpnicfWIPSDctStaRptSensorEntry,_AM:hpnicfWIPSDctStaRtpSensorName,'hpnicfWIPSDctStaRptSensorRadioId':hpnicfWIPSDctStaRptSensorRadioId,'hpnicfWIPSDctStaRptRSSI':hpnicfWIPSDctStaRptRSSI,'hpnicfWIPSDctStaLastRptTm':hpnicfWIPSDctStaLastRptTm,'hpnicfWIPSDctSSIDTable':hpnicfWIPSDctSSIDTable,'hpnicfWIPSDctSSIDEntry':hpnicfWIPSDctSSIDEntry,_b:hpnicfWIPSDctNetworkVSD,_c:hpnicfWIPSDctNetworkSSID,_d:hpnicfWIPSDctNetworkCfg,'hpnicfWIPSDctNetworkFirstRptTm':hpnicfWIPSDctNetworkFirstRptTm,'hpnicfWIPSDctNetworkLastRptTm':hpnicfWIPSDctNetworkLastRptTm,'hpnicfWIPSDctNetworkStatus':hpnicfWIPSDctNetworkStatus,'hpnicfWIPSDctNetworkSSIDHide':hpnicfWIPSDctNetworkSSIDHide,'hpnicfWIPSDctNetworkBSSNum':hpnicfWIPSDctNetworkBSSNum,'hpnicfWIPSDctSSIDBSSTable':hpnicfWIPSDctSSIDBSSTable,'hpnicfWIPSDctSSIDBSSEntry':hpnicfWIPSDctSSIDBSSEntry,_AN:hpnicfWIPSDctNetworkBSSID,'hpnicfWIPSDctNetworkBSSWorkChl':hpnicfWIPSDctNetworkBSSWorkChl,'hpnicfWIPSDctNetworkBSSStaNum':hpnicfWIPSDctNetworkBSSStaNum,'hpnicfWIPSBlockListTable':hpnicfWIPSBlockListTable,'hpnicfWIPSBlockListEntry':hpnicfWIPSBlockListEntry,_AO:hpnicfWIPSBlockListMacAddress,'hpnicfWIPSBlockListStatus':hpnicfWIPSBlockListStatus,'hpnicfWIPSChannelTable':hpnicfWIPSChannelTable,'hpnicfWIPSChannelEntry':hpnicfWIPSChannelEntry,_AQ:hpnicfWIPSChannelNum,'hpnicfWIPSChannelRadioType':hpnicfWIPSChannelRadioType,'hpnicfWIPSChannelIsPermitted':hpnicfWIPSChannelIsPermitted,'hpnicfWIPSChannelLastRptTm':hpnicfWIPSChannelLastRptTm,'hpnicfWIPSCountermeasureListTable':hpnicfWIPSCountermeasureListTable,'hpnicfWIPSCountermeasureListEntry':hpnicfWIPSCountermeasureListEntry,_AR:hpnicfWIPSCtmListMacAddress,'hpnicfWIPSCtmListLastestWorkChl':hpnicfWIPSCtmListLastestWorkChl,'hpnicfWIPSCtmListFirstTm':hpnicfWIPSCtmListFirstTm,'hpnicfWIPSCtmListLastTm':hpnicfWIPSCtmListLastTm,'hpnicfWIPSCtmListQurCnt':hpnicfWIPSCtmListQurCnt,'hpnicfWIPSCtmListSensorNum':hpnicfWIPSCtmListSensorNum,'hpnicfWIPSIgnoreListTable':hpnicfWIPSIgnoreListTable,'hpnicfWIPSIgnoreListEntry':hpnicfWIPSIgnoreListEntry,_AS:hpnicfWIPSIgnoreListMacAddress,'hpnicfWIPSIgnoreListFirstIgnoreTm':hpnicfWIPSIgnoreListFirstIgnoreTm,'hpnicfWIPSIgnoreListLastIgnoreTm':hpnicfWIPSIgnoreListLastIgnoreTm,'hpnicfWIPSIgnoreListIgnoreCnt':hpnicfWIPSIgnoreListIgnoreCnt,'hpnicfWIPSTrustListTable':hpnicfWIPSTrustListTable,'hpnicfWIPSTrustListEntry':hpnicfWIPSTrustListEntry,_AT:hpnicfWIPSTrustListMacAddress,'hpnicfWIPSTrustListStatus':hpnicfWIPSTrustListStatus,'hpnicfWIPSChlStatTable':hpnicfWIPSChlStatTable,'hpnicfWIPSChlStatEntry':hpnicfWIPSChlStatEntry,_AU:hpnicfWIPSChlStatSensorMacAddr,_AV:hpnicfWIPSChlStatChannel,'hpnicfWIPSChlStatTotalPkt':hpnicfWIPSChlStatTotalPkt,'hpnicfWIPSChlStatTotalByte':hpnicfWIPSChlStatTotalByte,'hpnicfWIPSChlStatBmcastPkt':hpnicfWIPSChlStatBmcastPkt,'hpnicfWIPSChlStatBmcastByte':hpnicfWIPSChlStatBmcastByte,'hpnicfWIPSChlStatUnicastPkt':hpnicfWIPSChlStatUnicastPkt,'hpnicfWIPSChlStatUnicastByte':hpnicfWIPSChlStatUnicastByte,'hpnicfWIPSChlStatManagement':hpnicfWIPSChlStatManagement,'hpnicfWIPSChlStatControl':hpnicfWIPSChlStatControl,'hpnicfWIPSChlStatData':hpnicfWIPSChlStatData,'hpnicfWIPSChlStatBeacon':hpnicfWIPSChlStatBeacon,'hpnicfWIPSChlStatRTS':hpnicfWIPSChlStatRTS,'hpnicfWIPSChlStatCTS':hpnicfWIPSChlStatCTS,'hpnicfWIPSChlStatProbeRequest':hpnicfWIPSChlStatProbeRequest,'hpnicfWIPSChlStatProbeResponse':hpnicfWIPSChlStatProbeResponse,'hpnicfWIPSChlStatFragment':hpnicfWIPSChlStatFragment,'hpnicfWIPSChlStatRetry':hpnicfWIPSChlStatRetry,'hpnicfWIPSChlStatEapSuccess':hpnicfWIPSChlStatEapSuccess,'hpnicfWIPSChlStatEapFailure':hpnicfWIPSChlStatEapFailure,'hpnicfWIPSChlStatEapolStart':hpnicfWIPSChlStatEapolStart,'hpnicfWIPSChlStatEapolLogoff':hpnicfWIPSChlStatEapolLogoff,'hpnicfWIPSChlStatAssocRequest':hpnicfWIPSChlStatAssocRequest,'hpnicfWIPSChlStatAssocResponse':hpnicfWIPSChlStatAssocResponse,'hpnicfWIPSChlStatUnicastDisassoc':hpnicfWIPSChlStatUnicastDisassoc,'hpnicfWIPSChlStatBroadcastDisassoc':hpnicfWIPSChlStatBroadcastDisassoc,'hpnicfWIPSChlStatAuthentication':hpnicfWIPSChlStatAuthentication,'hpnicfWIPSChlStatUnicastDeauthen':hpnicfWIPSChlStatUnicastDeauthen,'hpnicfWIPSChlStatBroadcastDeauthen':hpnicfWIPSChlStatBroadcastDeauthen,'hpnicfWIPSChlStatMalformed':hpnicfWIPSChlStatMalformed,'hpnicfWIPSDevStatTable':hpnicfWIPSDevStatTable,'hpnicfWIPSDevStatEntry':hpnicfWIPSDevStatEntry,_AW:hpnicfWIPSDevStatSensorMacAddr,_AX:hpnicfWIPSDevStatDevMacAddress,_AY:hpnicfWIPSDevStatChannel,'hpnicfWIPSDevStatTxTotalPkt':hpnicfWIPSDevStatTxTotalPkt,'hpnicfWIPSDevStatTxTotalByte':hpnicfWIPSDevStatTxTotalByte,'hpnicfWIPSDevStatTxBMcastPkt':hpnicfWIPSDevStatTxBMcastPkt,'hpnicfWIPSDevStatTxBMcastByte':hpnicfWIPSDevStatTxBMcastByte,'hpnicfWIPSDevStatTxUnicastPkt':hpnicfWIPSDevStatTxUnicastPkt,'hpnicfWIPSDevStatTxUnicastByte':hpnicfWIPSDevStatTxUnicastByte,'hpnicfWIPSDevStatTxMgmt':hpnicfWIPSDevStatTxMgmt,'hpnicfWIPSDevStatTxCtrl':hpnicfWIPSDevStatTxCtrl,'hpnicfWIPSDevStatTxData':hpnicfWIPSDevStatTxData,'hpnicfWIPSDevStatTxBeacon':hpnicfWIPSDevStatTxBeacon,'hpnicfWIPSDevStatTxRTS':hpnicfWIPSDevStatTxRTS,'hpnicfWIPSDevStatTxProbeRequest':hpnicfWIPSDevStatTxProbeRequest,'hpnicfWIPSDevStatTxProbeResponse':hpnicfWIPSDevStatTxProbeResponse,'hpnicfWIPSDevStatTxFragment':hpnicfWIPSDevStatTxFragment,'hpnicfWIPSDevStatTxRetry':hpnicfWIPSDevStatTxRetry,'hpnicfWIPSDevStatTxAssocRequest':hpnicfWIPSDevStatTxAssocRequest,'hpnicfWIPSDevStatTxAssocResponse':hpnicfWIPSDevStatTxAssocResponse,'hpnicfWIPSDevStatTxUnicastDisassoc':hpnicfWIPSDevStatTxUnicastDisassoc,'hpnicfWIPSDevStatTxBcastDisassoc':hpnicfWIPSDevStatTxBcastDisassoc,'hpnicfWIPSDevStatTxAuth':hpnicfWIPSDevStatTxAuth,'hpnicfWIPSDevStatTxUnicastDeauth':hpnicfWIPSDevStatTxUnicastDeauth,'hpnicfWIPSDevStatTxBcastDeauth':hpnicfWIPSDevStatTxBcastDeauth,'hpnicfWIPSDevStatTxEAPSuccess':hpnicfWIPSDevStatTxEAPSuccess,'hpnicfWIPSDevStatTxEAPFailure':hpnicfWIPSDevStatTxEAPFailure,'hpnicfWIPSDevStatTxEAPOLStart':hpnicfWIPSDevStatTxEAPOLStart,'hpnicfWIPSDevStatTxEAPOLLogOff':hpnicfWIPSDevStatTxEAPOLLogOff,'hpnicfWIPSDevStatTxMalformed':hpnicfWIPSDevStatTxMalformed,'hpnicfWIPSDevStatRxTotalPkt':hpnicfWIPSDevStatRxTotalPkt,'hpnicfWIPSDevStatRxTotalByte':hpnicfWIPSDevStatRxTotalByte,'hpnicfWIPSDevStatRxUnicastPkt':hpnicfWIPSDevStatRxUnicastPkt,'hpnicfWIPSDevStatRxUnicastByte':hpnicfWIPSDevStatRxUnicastByte,'hpnicfWIPSDevStatRxMgmt':hpnicfWIPSDevStatRxMgmt,'hpnicfWIPSDevStatRxCtrl':hpnicfWIPSDevStatRxCtrl,'hpnicfWIPSDevStatRxData':hpnicfWIPSDevStatRxData,'hpnicfWIPSDevStatRxRTS':hpnicfWIPSDevStatRxRTS,'hpnicfWIPSDevStatRxCTS':hpnicfWIPSDevStatRxCTS,'hpnicfWIPSDevStatRxProbeRequest':hpnicfWIPSDevStatRxProbeRequest,'hpnicfWIPSDevStatRxProbeResponse':hpnicfWIPSDevStatRxProbeResponse,'hpnicfWIPSDevStatRxFragment':hpnicfWIPSDevStatRxFragment,'hpnicfWIPSDevStatRxRetry':hpnicfWIPSDevStatRxRetry,'hpnicfWIPSDevStatRxAssoRequest':hpnicfWIPSDevStatRxAssoRequest,'hpnicfWIPSDevStatRxAssoResponse':hpnicfWIPSDevStatRxAssoResponse,'hpnicfWIPSDevStatRxDisassoc':hpnicfWIPSDevStatRxDisassoc,'hpnicfWIPSDevStatRxAuth':hpnicfWIPSDevStatRxAuth,'hpnicfWIPSDevStatRxDeauth':hpnicfWIPSDevStatRxDeauth,'hpnicfWIPSDevStatRxEAPSuccess':hpnicfWIPSDevStatRxEAPSuccess,'hpnicfWIPSDevStatRxEAPFailure':hpnicfWIPSDevStatRxEAPFailure,'hpnicfWIPSDevStatRxEAPOLStart':hpnicfWIPSDevStatRxEAPOLStart,'hpnicfWIPSDevStatRxEAPOLLogoff':hpnicfWIPSDevStatRxEAPOLLogoff,'hpnicfWIPSDevStatRxMalformed':hpnicfWIPSDevStatRxMalformed,'hpnicfWIPSCtmDeviceTable':hpnicfWIPSCtmDeviceTable,'hpnicfWIPSCtmDeviceEntry':hpnicfWIPSCtmDeviceEntry,_AZ:hpnicfWIPSCtmDeviceVSD,_Aa:hpnicfWIPSCtmDeviceMAC,'hpnicfWIPSCtmDeviceType':hpnicfWIPSCtmDeviceType,'hpnicfWIPSCtmDeviceState':hpnicfWIPSCtmDeviceState,'hpnicfWIPSCtmDeviceStartTime':hpnicfWIPSCtmDeviceStartTime,'hpnicfWIPSCtmDeviceCategory':hpnicfWIPSCtmDeviceCategory,'hpnicfWIPSCtmDeviceChl':hpnicfWIPSCtmDeviceChl,'hpnicfWIPSCtmDevicePrecedence':hpnicfWIPSCtmDevicePrecedence,'hpnicfWIPSMalPktStatTable':hpnicfWIPSMalPktStatTable,'hpnicfWIPSMalPktStatEntry':hpnicfWIPSMalPktStatEntry,_Ab:hpnicfWIPSMalPktStatSensorName,'hpnicfWIPSMalPktStatInvalidIELength':hpnicfWIPSMalPktStatInvalidIELength,'hpnicfWIPSMalPktStatDuplicatedIE':hpnicfWIPSMalPktStatDuplicatedIE,'hpnicfWIPSMalPktStatRedundantIE':hpnicfWIPSMalPktStatRedundantIE,'hpnicfWIPSMalPktStatInvalidPktLength':hpnicfWIPSMalPktStatInvalidPktLength,'hpnicfWIPSMalPktStatIllegalIBSSESS':hpnicfWIPSMalPktStatIllegalIBSSESS,'hpnicfWIPSMalPktStatInvalidSourceAddr':hpnicfWIPSMalPktStatInvalidSourceAddr,'hpnicfWIPSMalPktStatOverflowEAPOLKey':hpnicfWIPSMalPktStatOverflowEAPOLKey,'hpnicfWIPSMalPktStatMalAuth':hpnicfWIPSMalPktStatMalAuth,'hpnicfWIPSMalPktStatMalAssoReq':hpnicfWIPSMalPktStatMalAssoReq,'hpnicfWIPSMalPktStatMalHTIE':hpnicfWIPSMalPktStatMalHTIE,'hpnicfWIPSMalPktStatLargeDuration':hpnicfWIPSMalPktStatLargeDuration,'hpnicfWIPSMalPktStatNULLProbeRes':hpnicfWIPSMalPktStatNULLProbeRes,'hpnicfWIPSMalPktStatInvalidDeAuthCode':hpnicfWIPSMalPktStatInvalidDeAuthCode,'hpnicfWIPSMalPktStatInvalidDisAssoCode':hpnicfWIPSMalPktStatInvalidDisAssoCode,'hpnicfWIPSMalPktStatOverflowSSID':hpnicfWIPSMalPktStatOverflowSSID,'hpnicfWIPSMalPktStatFatajack':hpnicfWIPSMalPktStatFatajack,'hpnicfWIPSMalPktStatInvalidChannel':hpnicfWIPSMalPktStatInvalidChannel,'hpnicfWIPSDctUnassocStaTable':hpnicfWIPSDctUnassocStaTable,'hpnicfWIPSDctUnassocStaEntry':hpnicfWIPSDctUnassocStaEntry,_g:hpnicfWIPSDctUnassocStaVSD,_h:hpnicfWIPSDctUnassocStaMac,'hpnicfWIPSDctUnassocStaCategory':hpnicfWIPSDctUnassocStaCategory,'hpnicfWIPSDctUnassocStaRadioType':hpnicfWIPSDctUnassocStaRadioType,'hpnicfWIPSDctUnassocStaIsCountered':hpnicfWIPSDctUnassocStaIsCountered,'hpnicfWIPSDctUnassocStaAdd2BlackList':hpnicfWIPSDctUnassocStaAdd2BlackList,'hpnicfWIPSDctUnassocStaAdd2WhiteList':hpnicfWIPSDctUnassocStaAdd2WhiteList,'hpnicfWIPSDctUnassocStaAdd2IgnoreList':hpnicfWIPSDctUnassocStaAdd2IgnoreList,'hpnicfWIPSDctUnassocStaAdd2CtmList':hpnicfWIPSDctUnassocStaAdd2CtmList,'hpnicfWIPSDctUnassocStaFirstDctTm':hpnicfWIPSDctUnassocStaFirstDctTm,'hpnicfWIPSDctUnassocStaLastDctTm':hpnicfWIPSDctUnassocStaLastDctTm,'hpnicfWIPSDctUnassocStaRptSensorNum':hpnicfWIPSDctUnassocStaRptSensorNum,'hpnicfWIPSDctUnassocStaState':hpnicfWIPSDctUnassocStaState,'hpnicfWIPSDctUnassocStaVendor':hpnicfWIPSDctUnassocStaVendor,'hpnicfWIPSDctUnassocStaRptSensorTable':hpnicfWIPSDctUnassocStaRptSensorTable,'hpnicfWIPSDctUnassocStaRptSensorEntry':hpnicfWIPSDctUnassocStaRptSensorEntry,_Ac:hpnicfWIPSDctUnassocStaRtpSensorName,'hpnicfWIPSDctUnassocStaRptSensorRadioId':hpnicfWIPSDctUnassocStaRptSensorRadioId,'hpnicfWIPSDctUnassocStaRptRSSI':hpnicfWIPSDctUnassocStaRptRSSI,'hpnicfWIPSDctUnassocStaLastRptTm':hpnicfWIPSDctUnassocStaLastRptTm,'hpnicfWIPSNotifyGroup':hpnicfWIPSNotifyGroup})