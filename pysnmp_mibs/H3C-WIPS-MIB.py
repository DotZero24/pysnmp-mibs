_Ac='h3cWIPSDctUnassocStaRtpSensorName'
_Ab='h3cWIPSMalPktStatSensorName'
_Aa='h3cWIPSCtmDeviceMAC'
_AZ='h3cWIPSCtmDeviceVSD'
_AY='h3cWIPSDevStatChannel'
_AX='h3cWIPSDevStatDevMacAddress'
_AW='h3cWIPSDevStatSensorMacAddr'
_AV='h3cWIPSChlStatChannel'
_AU='h3cWIPSChlStatSensorMacAddr'
_AT='h3cWIPSTrustListMacAddress'
_AS='h3cWIPSIgnoreListMacAddress'
_AR='h3cWIPSCtmListMacAddress'
_AQ='h3cWIPSChannelNum'
_AP='staticAndDynamic'
_AO='h3cWIPSBlockListMacAddress'
_AN='h3cWIPSDctNetworkBSSID'
_AM='h3cWIPSDctStaRtpSensorName'
_AL='unassociation'
_AK='deauthentication'
_AJ='disassociation'
_AI='eapLogoff'
_AH='eapSuccess'
_AG='association'
_AF='authentication'
_AE='h3cWIPSDctAPRptSensorName'
_AD='h3cWIPSDctAPAttachStaMac'
_AC='H3cWIPSDevCategoryWay'
_AB='h3cWIPSStaticTrustVendorListVendor'
_AA='h3cWIPSStaticTrustOUIListOUI'
_A9='h3cWIPSMalPktDctPolicyName'
_A8='h3cWIPSCtmPolicyDevMAC'
_A7='h3cWIPSSigSubRulePatternID'
_A6='h3cWIPSSigRule2PolicySigRuleIDCfg'
_A5='h3cWIPSDctModeRadio'
_A4='h3cWIPSDctModeAPName'
_A3='h3cWIPSIgnoreListMAC'
_A2='h3cWIPSStaticTrustListMAC'
_A1='h3cWIPSStaticBlockListMAC'
_A0='h3cWIPSStaticCtmListMAC'
_z='h3cWIPSAtkDctPolicyName'
_y='H3cWIPSAPSecurityType'
_x='notequal'
_w='notinclude'
_v='h3cWIPSAPClaRuleName'
_u='detectOnly'
_t='middle'
_s='detectFirst'
_r='accessFirst'
_q='h3cWIPSSensorRadioRadioId'
_p='h3cWIPSRule2VsdAPClaRuleNameCfg'
_o='pskANDdot1xANDother'
_n='dot1xANDother'
_m='pskANDother'
_l='pskANDdot1x'
_k='uncategorized'
_j='external'
_i='misconfigured'
_h='h3cWIPSDctUnassocStaMac'
_g='h3cWIPSDctUnassocStaVSD'
_f='dynamic'
_e='static'
_d='h3cWIPSDctNetworkCfg'
_c='h3cWIPSDctNetworkSSID'
_b='h3cWIPSDctNetworkVSD'
_a='h3cWIPSDctStaMac'
_Z='h3cWIPSDctStaVSD'
_Y='h3cWIPSCtmPolicyName'
_X='h3cWIPSSigRuleName'
_W='h3cWIPSSigPolicyNameCfg'
_V='h3cWIPSSensorNameCfg'
_U='other'
_T='rogue'
_S='authorized'
_R='h3cWIPSDctAPBSSID'
_Q='h3cWIPSDctAPVSD'
_P='equal'
_O='include'
_N='h3cWIPSVsdNameCfg'
_M='none'
_L='second'
_K='TruthValue'
_J='Unsigned32'
_I='read-write'
_H='OctetString'
_G='not-accessible'
_F='Integer32'
_E='H3C-WIPS-MIB'
_D='Counter64'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32',_D,'Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
h3cWIPS=ModuleIdentity((1,3,6,1,4,1,2011,10,2,118))
if mibBuilder.loadTexts:h3cWIPS.setRevisions(('2011-12-29 14:50',))
class H3cWIPSRadioType(TextualConvention,Unsigned32):status=_A;displayHint='d'
class H3cWIPSDevStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
class H3cWIPSDevCategoryWay(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('autoByNMS',2),('autoByDev',3)))
class H3cWIPSDeviceCategoryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_M,0),('authorizedAP',1),('authorizedClient',2),('misconfiguredAP',3),('rogueAP',4),('unauthorizedClient',5),('externalAP',6),('adhoc',7),('bridge',8),('misassociatedClient',9),('potentialAuthorizedAP',10),('potentialRogueAP',11),('potentialExternalAP',12),('uncategorizedAP',13),('uncategorizedClient',14)))
class H3cWIPSAPCategoryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('adhoc',1),(_S,2),(_T,3),(_i,4),(_j,5),('potentialAuthorized',6),('potentialRogue',7),('potentialExternal',8),(_k,9)))
class H3cWIPSClientCategoryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),('unauthorized',2),('misassociated',3),(_k,4),('unassociated',5)))
class H3cWIPSChannel(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,224))
class H3cWIPSEncryptMethod(TextualConvention,Unsigned32):status=_A;displayHint='d'
class H3cWIPSAuthMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),('psk',2),('dot1x',3),(_U,4),(_l,5),(_m,6),(_n,7),(_o,8)))
class H3cWIPSAPClassifyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_S,2),(_j,3),(_i,4),(_T,5)))
class H3cWIPSAPSecurityType(TextualConvention,Unsigned32):status=_A;displayHint='d'
_H3cWIPSConfigGroup_ObjectIdentity=ObjectIdentity
h3cWIPSConfigGroup=_H3cWIPSConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,118,1))
_H3cWIPSGlobalConfigGroup_ObjectIdentity=ObjectIdentity
h3cWIPSGlobalConfigGroup=_H3cWIPSGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,118,1,1))
_H3cWIPSEnable_Type=TruthValue
_H3cWIPSEnable_Object=MibScalar
h3cWIPSEnable=_H3cWIPSEnable_Object((1,3,6,1,4,1,2011,10,2,118,1,1,1),_H3cWIPSEnable_Type())
h3cWIPSEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSEnable.setStatus(_A)
_H3cWIPSSensorLicenseNum_Type=Unsigned32
_H3cWIPSSensorLicenseNum_Object=MibScalar
h3cWIPSSensorLicenseNum=_H3cWIPSSensorLicenseNum_Object((1,3,6,1,4,1,2011,10,2,118,1,1,2),_H3cWIPSSensorLicenseNum_Type())
h3cWIPSSensorLicenseNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSSensorLicenseNum.setStatus(_A)
class _H3cWIPSBlocklistAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('block',1),('unblock',2)))
_H3cWIPSBlocklistAction_Type.__name__=_F
_H3cWIPSBlocklistAction_Object=MibScalar
h3cWIPSBlocklistAction=_H3cWIPSBlocklistAction_Object((1,3,6,1,4,1,2011,10,2,118,1,1,3),_H3cWIPSBlocklistAction_Type())
h3cWIPSBlocklistAction.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSBlocklistAction.setStatus(_A)
class _H3cWIPSAPInactiveTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,600))
_H3cWIPSAPInactiveTime_Type.__name__=_F
_H3cWIPSAPInactiveTime_Object=MibScalar
h3cWIPSAPInactiveTime=_H3cWIPSAPInactiveTime_Object((1,3,6,1,4,1,2011,10,2,118,1,1,4),_H3cWIPSAPInactiveTime_Type())
h3cWIPSAPInactiveTime.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSAPInactiveTime.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSAPInactiveTime.setUnits(_L)
class _H3cWIPSSTAInactiveTime_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,1200))
_H3cWIPSSTAInactiveTime_Type.__name__=_F
_H3cWIPSSTAInactiveTime_Object=MibScalar
h3cWIPSSTAInactiveTime=_H3cWIPSSTAInactiveTime_Object((1,3,6,1,4,1,2011,10,2,118,1,1,5),_H3cWIPSSTAInactiveTime_Type())
h3cWIPSSTAInactiveTime.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSSTAInactiveTime.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSSTAInactiveTime.setUnits(_L)
class _H3cWIPSDevAgingTime_Type(Integer32):defaultValue=86400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2592000))
_H3cWIPSDevAgingTime_Type.__name__=_F
_H3cWIPSDevAgingTime_Object=MibScalar
h3cWIPSDevAgingTime=_H3cWIPSDevAgingTime_Object((1,3,6,1,4,1,2011,10,2,118,1,1,6),_H3cWIPSDevAgingTime_Type())
h3cWIPSDevAgingTime.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDevAgingTime.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSDevAgingTime.setUnits(_L)
class _H3cWIPSStatisticPeriod_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_H3cWIPSStatisticPeriod_Type.__name__=_F
_H3cWIPSStatisticPeriod_Object=MibScalar
h3cWIPSStatisticPeriod=_H3cWIPSStatisticPeriod_Object((1,3,6,1,4,1,2011,10,2,118,1,1,7),_H3cWIPSStatisticPeriod_Type())
h3cWIPSStatisticPeriod.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSStatisticPeriod.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSStatisticPeriod.setUnits(_L)
class _H3cWIPSReclassificationPeriod_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,3600))
_H3cWIPSReclassificationPeriod_Type.__name__=_F
_H3cWIPSReclassificationPeriod_Object=MibScalar
h3cWIPSReclassificationPeriod=_H3cWIPSReclassificationPeriod_Object((1,3,6,1,4,1,2011,10,2,118,1,1,8),_H3cWIPSReclassificationPeriod_Type())
h3cWIPSReclassificationPeriod.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSReclassificationPeriod.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSReclassificationPeriod.setUnits(_L)
_H3cWIPSResetAllTrustList_Type=TruthValue
_H3cWIPSResetAllTrustList_Object=MibScalar
h3cWIPSResetAllTrustList=_H3cWIPSResetAllTrustList_Object((1,3,6,1,4,1,2011,10,2,118,1,1,9),_H3cWIPSResetAllTrustList_Type())
h3cWIPSResetAllTrustList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSResetAllTrustList.setStatus(_A)
_H3cWIPSResetAllBlockList_Type=TruthValue
_H3cWIPSResetAllBlockList_Object=MibScalar
h3cWIPSResetAllBlockList=_H3cWIPSResetAllBlockList_Object((1,3,6,1,4,1,2011,10,2,118,1,1,10),_H3cWIPSResetAllBlockList_Type())
h3cWIPSResetAllBlockList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSResetAllBlockList.setStatus(_A)
_H3cWIPSResetAllIgnoreList_Type=TruthValue
_H3cWIPSResetAllIgnoreList_Object=MibScalar
h3cWIPSResetAllIgnoreList=_H3cWIPSResetAllIgnoreList_Object((1,3,6,1,4,1,2011,10,2,118,1,1,11),_H3cWIPSResetAllIgnoreList_Type())
h3cWIPSResetAllIgnoreList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSResetAllIgnoreList.setStatus(_A)
_H3cWIPSResetAllCtmList_Type=TruthValue
_H3cWIPSResetAllCtmList_Object=MibScalar
h3cWIPSResetAllCtmList=_H3cWIPSResetAllCtmList_Object((1,3,6,1,4,1,2011,10,2,118,1,1,12),_H3cWIPSResetAllCtmList_Type())
h3cWIPSResetAllCtmList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSResetAllCtmList.setStatus(_A)
class _H3cWIPSPermitChlBitMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_H3cWIPSPermitChlBitMap_Type.__name__=_H
_H3cWIPSPermitChlBitMap_Object=MibScalar
h3cWIPSPermitChlBitMap=_H3cWIPSPermitChlBitMap_Object((1,3,6,1,4,1,2011,10,2,118,1,1,13),_H3cWIPSPermitChlBitMap_Type())
h3cWIPSPermitChlBitMap.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSPermitChlBitMap.setStatus(_A)
class _H3cWIPSDynamicTrustListAgingTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_H3cWIPSDynamicTrustListAgingTime_Type.__name__=_F
_H3cWIPSDynamicTrustListAgingTime_Object=MibScalar
h3cWIPSDynamicTrustListAgingTime=_H3cWIPSDynamicTrustListAgingTime_Object((1,3,6,1,4,1,2011,10,2,118,1,1,14),_H3cWIPSDynamicTrustListAgingTime_Type())
h3cWIPSDynamicTrustListAgingTime.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDynamicTrustListAgingTime.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSDynamicTrustListAgingTime.setUnits(_L)
class _H3cWIPSDevUpdateTime_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,30))
_H3cWIPSDevUpdateTime_Type.__name__=_F
_H3cWIPSDevUpdateTime_Object=MibScalar
h3cWIPSDevUpdateTime=_H3cWIPSDevUpdateTime_Object((1,3,6,1,4,1,2011,10,2,118,1,1,15),_H3cWIPSDevUpdateTime_Type())
h3cWIPSDevUpdateTime.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDevUpdateTime.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSDevUpdateTime.setUnits(_L)
class _H3cWIPSADOSEnable_Type(TruthValue):defaultValue=2
_H3cWIPSADOSEnable_Type.__name__=_K
_H3cWIPSADOSEnable_Object=MibScalar
h3cWIPSADOSEnable=_H3cWIPSADOSEnable_Object((1,3,6,1,4,1,2011,10,2,118,1,1,16),_H3cWIPSADOSEnable_Type())
h3cWIPSADOSEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSADOSEnable.setStatus(_A)
class _H3cWIPSAccessFlowScanEnable_Type(TruthValue):defaultValue=2
_H3cWIPSAccessFlowScanEnable_Type.__name__=_K
_H3cWIPSAccessFlowScanEnable_Object=MibScalar
h3cWIPSAccessFlowScanEnable=_H3cWIPSAccessFlowScanEnable_Object((1,3,6,1,4,1,2011,10,2,118,1,1,17),_H3cWIPSAccessFlowScanEnable_Type())
h3cWIPSAccessFlowScanEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSAccessFlowScanEnable.setStatus(_A)
_H3cWIPSVsdConfigGroup_ObjectIdentity=ObjectIdentity
h3cWIPSVsdConfigGroup=_H3cWIPSVsdConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,118,1,2))
_H3cWIPSVsdTable_Object=MibTable
h3cWIPSVsdTable=_H3cWIPSVsdTable_Object((1,3,6,1,4,1,2011,10,2,118,1,2,1))
if mibBuilder.loadTexts:h3cWIPSVsdTable.setStatus(_A)
_H3cWIPSVsdEntry_Object=MibTableRow
h3cWIPSVsdEntry=_H3cWIPSVsdEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,2,1,1))
h3cWIPSVsdEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:h3cWIPSVsdEntry.setStatus(_A)
class _H3cWIPSVsdNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSVsdNameCfg_Type.__name__=_H
_H3cWIPSVsdNameCfg_Object=MibTableColumn
h3cWIPSVsdNameCfg=_H3cWIPSVsdNameCfg_Object((1,3,6,1,4,1,2011,10,2,118,1,2,1,1,1),_H3cWIPSVsdNameCfg_Type())
h3cWIPSVsdNameCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSVsdNameCfg.setStatus(_A)
_H3cWIPSVsdRowStatus_Type=RowStatus
_H3cWIPSVsdRowStatus_Object=MibTableColumn
h3cWIPSVsdRowStatus=_H3cWIPSVsdRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,2,1,1,2),_H3cWIPSVsdRowStatus_Type())
h3cWIPSVsdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSVsdRowStatus.setStatus(_A)
class _H3cWIPSVsdAtkDctPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWIPSVsdAtkDctPolicyNameCfg_Type.__name__=_H
_H3cWIPSVsdAtkDctPolicyNameCfg_Object=MibTableColumn
h3cWIPSVsdAtkDctPolicyNameCfg=_H3cWIPSVsdAtkDctPolicyNameCfg_Object((1,3,6,1,4,1,2011,10,2,118,1,2,1,1,3),_H3cWIPSVsdAtkDctPolicyNameCfg_Type())
h3cWIPSVsdAtkDctPolicyNameCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSVsdAtkDctPolicyNameCfg.setStatus(_A)
class _H3cWIPSVsdCtmPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWIPSVsdCtmPolicyNameCfg_Type.__name__=_H
_H3cWIPSVsdCtmPolicyNameCfg_Object=MibTableColumn
h3cWIPSVsdCtmPolicyNameCfg=_H3cWIPSVsdCtmPolicyNameCfg_Object((1,3,6,1,4,1,2011,10,2,118,1,2,1,1,4),_H3cWIPSVsdCtmPolicyNameCfg_Type())
h3cWIPSVsdCtmPolicyNameCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSVsdCtmPolicyNameCfg.setStatus(_A)
class _H3cWIPSVsdSigPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWIPSVsdSigPolicyNameCfg_Type.__name__=_H
_H3cWIPSVsdSigPolicyNameCfg_Object=MibTableColumn
h3cWIPSVsdSigPolicyNameCfg=_H3cWIPSVsdSigPolicyNameCfg_Object((1,3,6,1,4,1,2011,10,2,118,1,2,1,1,5),_H3cWIPSVsdSigPolicyNameCfg_Type())
h3cWIPSVsdSigPolicyNameCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSVsdSigPolicyNameCfg.setStatus(_A)
class _H3cWIPSVsdMalPktPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWIPSVsdMalPktPolicyNameCfg_Type.__name__=_H
_H3cWIPSVsdMalPktPolicyNameCfg_Object=MibTableColumn
h3cWIPSVsdMalPktPolicyNameCfg=_H3cWIPSVsdMalPktPolicyNameCfg_Object((1,3,6,1,4,1,2011,10,2,118,1,2,1,1,6),_H3cWIPSVsdMalPktPolicyNameCfg_Type())
h3cWIPSVsdMalPktPolicyNameCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSVsdMalPktPolicyNameCfg.setStatus(_A)
_H3cWIPSRule2VsdTable_Object=MibTable
h3cWIPSRule2VsdTable=_H3cWIPSRule2VsdTable_Object((1,3,6,1,4,1,2011,10,2,118,1,2,2))
if mibBuilder.loadTexts:h3cWIPSRule2VsdTable.setStatus(_A)
_H3cWIPSRule2VsdEntry_Object=MibTableRow
h3cWIPSRule2VsdEntry=_H3cWIPSRule2VsdEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,2,2,1))
h3cWIPSRule2VsdEntry.setIndexNames((0,_E,_N),(0,_E,_p))
if mibBuilder.loadTexts:h3cWIPSRule2VsdEntry.setStatus(_A)
class _H3cWIPSRule2VsdAPClaRuleNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSRule2VsdAPClaRuleNameCfg_Type.__name__=_H
_H3cWIPSRule2VsdAPClaRuleNameCfg_Object=MibTableColumn
h3cWIPSRule2VsdAPClaRuleNameCfg=_H3cWIPSRule2VsdAPClaRuleNameCfg_Object((1,3,6,1,4,1,2011,10,2,118,1,2,2,1,1),_H3cWIPSRule2VsdAPClaRuleNameCfg_Type())
h3cWIPSRule2VsdAPClaRuleNameCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSRule2VsdAPClaRuleNameCfg.setStatus(_A)
_H3cWIPSRule2VsdRowStatus_Type=RowStatus
_H3cWIPSRule2VsdRowStatus_Object=MibTableColumn
h3cWIPSRule2VsdRowStatus=_H3cWIPSRule2VsdRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,2,2,1,2),_H3cWIPSRule2VsdRowStatus_Type())
h3cWIPSRule2VsdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSRule2VsdRowStatus.setStatus(_A)
class _H3cWIPSRule2VsdPrecedence_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cWIPSRule2VsdPrecedence_Type.__name__=_F
_H3cWIPSRule2VsdPrecedence_Object=MibTableColumn
h3cWIPSRule2VsdPrecedence=_H3cWIPSRule2VsdPrecedence_Object((1,3,6,1,4,1,2011,10,2,118,1,2,2,1,3),_H3cWIPSRule2VsdPrecedence_Type())
h3cWIPSRule2VsdPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSRule2VsdPrecedence.setStatus(_A)
_H3cWIPSSensor2VsdTable_Object=MibTable
h3cWIPSSensor2VsdTable=_H3cWIPSSensor2VsdTable_Object((1,3,6,1,4,1,2011,10,2,118,1,2,3))
if mibBuilder.loadTexts:h3cWIPSSensor2VsdTable.setStatus(_A)
_H3cWIPSSensor2VsdEntry_Object=MibTableRow
h3cWIPSSensor2VsdEntry=_H3cWIPSSensor2VsdEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,2,3,1))
h3cWIPSSensor2VsdEntry.setIndexNames((0,_E,_N),(0,_E,_V))
if mibBuilder.loadTexts:h3cWIPSSensor2VsdEntry.setStatus(_A)
class _H3cWIPSSensorNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cWIPSSensorNameCfg_Type.__name__=_H
_H3cWIPSSensorNameCfg_Object=MibTableColumn
h3cWIPSSensorNameCfg=_H3cWIPSSensorNameCfg_Object((1,3,6,1,4,1,2011,10,2,118,1,2,3,1,1),_H3cWIPSSensorNameCfg_Type())
h3cWIPSSensorNameCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSSensorNameCfg.setStatus(_A)
_H3cWIPSSensor2VsdRowStatus_Type=RowStatus
_H3cWIPSSensor2VsdRowStatus_Object=MibTableColumn
h3cWIPSSensor2VsdRowStatus=_H3cWIPSSensor2VsdRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,2,3,1,2),_H3cWIPSSensor2VsdRowStatus_Type())
h3cWIPSSensor2VsdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSensor2VsdRowStatus.setStatus(_A)
class _H3cWIPSSensorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('idle',2)))
_H3cWIPSSensorState_Type.__name__=_F
_H3cWIPSSensorState_Object=MibTableColumn
h3cWIPSSensorState=_H3cWIPSSensorState_Object((1,3,6,1,4,1,2011,10,2,118,1,2,3,1,3),_H3cWIPSSensorState_Type())
h3cWIPSSensorState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSensorState.setStatus(_A)
_H3cWIPSSensorRadioTable_Object=MibTable
h3cWIPSSensorRadioTable=_H3cWIPSSensorRadioTable_Object((1,3,6,1,4,1,2011,10,2,118,1,2,4))
if mibBuilder.loadTexts:h3cWIPSSensorRadioTable.setStatus(_A)
_H3cWIPSSensorRadioEntry_Object=MibTableRow
h3cWIPSSensorRadioEntry=_H3cWIPSSensorRadioEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,2,4,1))
h3cWIPSSensorRadioEntry.setIndexNames((0,_E,_N),(0,_E,_V),(0,_E,_q))
if mibBuilder.loadTexts:h3cWIPSSensorRadioEntry.setStatus(_A)
class _H3cWIPSSensorRadioRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_H3cWIPSSensorRadioRadioId_Type.__name__=_F
_H3cWIPSSensorRadioRadioId_Object=MibTableColumn
h3cWIPSSensorRadioRadioId=_H3cWIPSSensorRadioRadioId_Object((1,3,6,1,4,1,2011,10,2,118,1,2,4,1,1),_H3cWIPSSensorRadioRadioId_Type())
h3cWIPSSensorRadioRadioId.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSSensorRadioRadioId.setStatus(_A)
class _H3cWIPSSensorRadioScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3),(_u,4)))
_H3cWIPSSensorRadioScanMode_Type.__name__=_F
_H3cWIPSSensorRadioScanMode_Object=MibTableColumn
h3cWIPSSensorRadioScanMode=_H3cWIPSSensorRadioScanMode_Object((1,3,6,1,4,1,2011,10,2,118,1,2,4,1,2),_H3cWIPSSensorRadioScanMode_Type())
h3cWIPSSensorRadioScanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSSensorRadioScanMode.setStatus(_A)
_H3cWIPSAPClaRuleTable_Object=MibTable
h3cWIPSAPClaRuleTable=_H3cWIPSAPClaRuleTable_Object((1,3,6,1,4,1,2011,10,2,118,1,3))
if mibBuilder.loadTexts:h3cWIPSAPClaRuleTable.setStatus(_A)
_H3cWIPSAPClaRuleEntry_Object=MibTableRow
h3cWIPSAPClaRuleEntry=_H3cWIPSAPClaRuleEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1))
h3cWIPSAPClaRuleEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:h3cWIPSAPClaRuleEntry.setStatus(_A)
class _H3cWIPSAPClaRuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSAPClaRuleName_Type.__name__=_H
_H3cWIPSAPClaRuleName_Object=MibTableColumn
h3cWIPSAPClaRuleName=_H3cWIPSAPClaRuleName_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,1),_H3cWIPSAPClaRuleName_Type())
h3cWIPSAPClaRuleName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSAPClaRuleName.setStatus(_A)
_H3cWIPSAPClaRowStatus_Type=RowStatus
_H3cWIPSAPClaRowStatus_Object=MibTableColumn
h3cWIPSAPClaRowStatus=_H3cWIPSAPClaRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,2),_H3cWIPSAPClaRowStatus_Type())
h3cWIPSAPClaRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAPClaRowStatus.setStatus(_A)
class _H3cWIPSAPClaSeverityLevel_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSAPClaSeverityLevel_Type.__name__=_J
_H3cWIPSAPClaSeverityLevel_Object=MibTableColumn
h3cWIPSAPClaSeverityLevel=_H3cWIPSAPClaSeverityLevel_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,3),_H3cWIPSAPClaSeverityLevel_Type())
h3cWIPSAPClaSeverityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAPClaSeverityLevel.setStatus(_A)
class _H3cWIPSAPClaRuleMatchAll_Type(TruthValue):defaultValue=2
_H3cWIPSAPClaRuleMatchAll_Type.__name__=_K
_H3cWIPSAPClaRuleMatchAll_Object=MibTableColumn
h3cWIPSAPClaRuleMatchAll=_H3cWIPSAPClaRuleMatchAll_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,4),_H3cWIPSAPClaRuleMatchAll_Type())
h3cWIPSAPClaRuleMatchAll.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAPClaRuleMatchAll.setStatus(_A)
_H3cWIPSAPClaType_Type=H3cWIPSAPClassifyType
_H3cWIPSAPClaType_Object=MibTableColumn
h3cWIPSAPClaType=_H3cWIPSAPClaType_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,5),_H3cWIPSAPClaType_Type())
h3cWIPSAPClaType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAPClaType.setStatus(_A)
class _H3cWIPSAPClaSubRuleSSIDOperator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_w,2),(_P,3),(_x,4)))
_H3cWIPSAPClaSubRuleSSIDOperator_Type.__name__=_F
_H3cWIPSAPClaSubRuleSSIDOperator_Object=MibTableColumn
h3cWIPSAPClaSubRuleSSIDOperator=_H3cWIPSAPClaSubRuleSSIDOperator_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,6),_H3cWIPSAPClaSubRuleSSIDOperator_Type())
h3cWIPSAPClaSubRuleSSIDOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAPClaSubRuleSSIDOperator.setStatus(_A)
class _H3cWIPSAPClaSubRuleSSIDCase_Type(TruthValue):defaultValue=2
_H3cWIPSAPClaSubRuleSSIDCase_Type.__name__=_K
_H3cWIPSAPClaSubRuleSSIDCase_Object=MibTableColumn
h3cWIPSAPClaSubRuleSSIDCase=_H3cWIPSAPClaSubRuleSSIDCase_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,7),_H3cWIPSAPClaSubRuleSSIDCase_Type())
h3cWIPSAPClaSubRuleSSIDCase.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAPClaSubRuleSSIDCase.setStatus(_A)
class _H3cWIPSAPClaSubRuleSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWIPSAPClaSubRuleSSID_Type.__name__=_H
_H3cWIPSAPClaSubRuleSSID_Object=MibTableColumn
h3cWIPSAPClaSubRuleSSID=_H3cWIPSAPClaSubRuleSSID_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,8),_H3cWIPSAPClaSubRuleSSID_Type())
h3cWIPSAPClaSubRuleSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAPClaSubRuleSSID.setStatus(_A)
class _H3cWIPSSecurityType_Type(H3cWIPSAPSecurityType):defaultValue=4294967295
_H3cWIPSSecurityType_Type.__name__=_y
_H3cWIPSSecurityType_Object=MibTableColumn
h3cWIPSSecurityType=_H3cWIPSSecurityType_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,9),_H3cWIPSSecurityType_Type())
h3cWIPSSecurityType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSecurityType.setStatus(_A)
class _H3cWIPSSecurityTypeMatch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_O,2)))
_H3cWIPSSecurityTypeMatch_Type.__name__=_F
_H3cWIPSSecurityTypeMatch_Object=MibTableColumn
h3cWIPSSecurityTypeMatch=_H3cWIPSSecurityTypeMatch_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,10),_H3cWIPSSecurityTypeMatch_Type())
h3cWIPSSecurityTypeMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSecurityTypeMatch.setStatus(_A)
class _H3cWIPSAPAuthType_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_M,1),('psk',2),('dot1x',3),(_U,4),('undo',5),(_l,6),(_m,7),(_n,8),(_o,9),('noneANDpsk',10),('noneANDdot1x',11),('noneANDother',12),('noneANDpskANDdot1x',13),('noneANDpskANDother',14),('noneANDdot1xANDother',15),('noneANDpskANDdot1xANDother',16)))
_H3cWIPSAPAuthType_Type.__name__=_F
_H3cWIPSAPAuthType_Object=MibTableColumn
h3cWIPSAPAuthType=_H3cWIPSAPAuthType_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,11),_H3cWIPSAPAuthType_Type())
h3cWIPSAPAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAPAuthType.setStatus(_A)
class _H3cWIPSMaxRSSIValue_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSMaxRSSIValue_Type.__name__=_J
_H3cWIPSMaxRSSIValue_Object=MibTableColumn
h3cWIPSMaxRSSIValue=_H3cWIPSMaxRSSIValue_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,12),_H3cWIPSMaxRSSIValue_Type())
h3cWIPSMaxRSSIValue.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMaxRSSIValue.setStatus(_A)
class _H3cWIPSMinRSSIValue_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSMinRSSIValue_Type.__name__=_J
_H3cWIPSMinRSSIValue_Object=MibTableColumn
h3cWIPSMinRSSIValue=_H3cWIPSMinRSSIValue_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,13),_H3cWIPSMinRSSIValue_Type())
h3cWIPSMinRSSIValue.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMinRSSIValue.setStatus(_A)
class _H3cWIPSMaxDuration_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSMaxDuration_Type.__name__=_J
_H3cWIPSMaxDuration_Object=MibTableColumn
h3cWIPSMaxDuration=_H3cWIPSMaxDuration_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,14),_H3cWIPSMaxDuration_Type())
h3cWIPSMaxDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMaxDuration.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSMaxDuration.setUnits(_L)
class _H3cWIPSMinDuration_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSMinDuration_Type.__name__=_J
_H3cWIPSMinDuration_Object=MibTableColumn
h3cWIPSMinDuration=_H3cWIPSMinDuration_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,15),_H3cWIPSMinDuration_Type())
h3cWIPSMinDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMinDuration.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSMinDuration.setUnits(_L)
class _H3cWIPSMaxAPNum_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSMaxAPNum_Type.__name__=_J
_H3cWIPSMaxAPNum_Object=MibTableColumn
h3cWIPSMaxAPNum=_H3cWIPSMaxAPNum_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,16),_H3cWIPSMaxAPNum_Type())
h3cWIPSMaxAPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMaxAPNum.setStatus(_A)
class _H3cWIPSMinAPNum_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSMinAPNum_Type.__name__=_J
_H3cWIPSMinAPNum_Object=MibTableColumn
h3cWIPSMinAPNum=_H3cWIPSMinAPNum_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,17),_H3cWIPSMinAPNum_Type())
h3cWIPSMinAPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMinAPNum.setStatus(_A)
class _H3cWIPSMaxClientNum_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSMaxClientNum_Type.__name__=_J
_H3cWIPSMaxClientNum_Object=MibTableColumn
h3cWIPSMaxClientNum=_H3cWIPSMaxClientNum_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,18),_H3cWIPSMaxClientNum_Type())
h3cWIPSMaxClientNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMaxClientNum.setStatus(_A)
class _H3cWIPSMinClientNum_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSMinClientNum_Type.__name__=_J
_H3cWIPSMinClientNum_Object=MibTableColumn
h3cWIPSMinClientNum=_H3cWIPSMinClientNum_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,19),_H3cWIPSMinClientNum_Type())
h3cWIPSMinClientNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMinClientNum.setStatus(_A)
class _H3cWIPSOUIInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_H3cWIPSOUIInfo_Type.__name__=_H
_H3cWIPSOUIInfo_Object=MibTableColumn
h3cWIPSOUIInfo=_H3cWIPSOUIInfo_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,20),_H3cWIPSOUIInfo_Type())
h3cWIPSOUIInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSOUIInfo.setStatus(_A)
class _H3cWIPSVendorInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cWIPSVendorInfo_Type.__name__=_H
_H3cWIPSVendorInfo_Object=MibTableColumn
h3cWIPSVendorInfo=_H3cWIPSVendorInfo_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,21),_H3cWIPSVendorInfo_Type())
h3cWIPSVendorInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSVendorInfo.setStatus(_A)
class _H3cWIPSAPAuthTypeMatch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_O,2)))
_H3cWIPSAPAuthTypeMatch_Type.__name__=_F
_H3cWIPSAPAuthTypeMatch_Object=MibTableColumn
h3cWIPSAPAuthTypeMatch=_H3cWIPSAPAuthTypeMatch_Object((1,3,6,1,4,1,2011,10,2,118,1,3,1,22),_H3cWIPSAPAuthTypeMatch_Type())
h3cWIPSAPAuthTypeMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAPAuthTypeMatch.setStatus(_A)
_H3cWIPSAtkDctPolicyCfgGroup_ObjectIdentity=ObjectIdentity
h3cWIPSAtkDctPolicyCfgGroup=_H3cWIPSAtkDctPolicyCfgGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,118,1,4))
class _H3cWIPSAtkDctPolicyCfgSupportSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_H3cWIPSAtkDctPolicyCfgSupportSet_Type.__name__=_H
_H3cWIPSAtkDctPolicyCfgSupportSet_Object=MibScalar
h3cWIPSAtkDctPolicyCfgSupportSet=_H3cWIPSAtkDctPolicyCfgSupportSet_Object((1,3,6,1,4,1,2011,10,2,118,1,4,1),_H3cWIPSAtkDctPolicyCfgSupportSet_Type())
h3cWIPSAtkDctPolicyCfgSupportSet.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyCfgSupportSet.setStatus(_A)
_H3cWIPSAtkDctPolicyCfgTable_Object=MibTable
h3cWIPSAtkDctPolicyCfgTable=_H3cWIPSAtkDctPolicyCfgTable_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2))
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyCfgTable.setStatus(_A)
_H3cWIPSAtkDctPolicyCfgEntry_Object=MibTableRow
h3cWIPSAtkDctPolicyCfgEntry=_H3cWIPSAtkDctPolicyCfgEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1))
h3cWIPSAtkDctPolicyCfgEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyCfgEntry.setStatus(_A)
class _H3cWIPSAtkDctPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSAtkDctPolicyName_Type.__name__=_H
_H3cWIPSAtkDctPolicyName_Object=MibTableColumn
h3cWIPSAtkDctPolicyName=_H3cWIPSAtkDctPolicyName_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,1),_H3cWIPSAtkDctPolicyName_Type())
h3cWIPSAtkDctPolicyName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyName.setStatus(_A)
_H3cWIPSAtkDctPolicyCfgRowStatus_Type=RowStatus
_H3cWIPSAtkDctPolicyCfgRowStatus_Object=MibTableColumn
h3cWIPSAtkDctPolicyCfgRowStatus=_H3cWIPSAtkDctPolicyCfgRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,2),_H3cWIPSAtkDctPolicyCfgRowStatus_Type())
h3cWIPSAtkDctPolicyCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyCfgRowStatus.setStatus(_A)
class _H3cWIPSAtkDctPolicyBitString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_H3cWIPSAtkDctPolicyBitString_Type.__name__=_H
_H3cWIPSAtkDctPolicyBitString_Object=MibTableColumn
h3cWIPSAtkDctPolicyBitString=_H3cWIPSAtkDctPolicyBitString_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,3),_H3cWIPSAtkDctPolicyBitString_Type())
h3cWIPSAtkDctPolicyBitString.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyBitString.setStatus(_A)
class _H3cWIPSAtkDctPolicyAPFloodQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyAPFloodQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyAPFloodQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyAPFloodQT=_H3cWIPSAtkDctPolicyAPFloodQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,4),_H3cWIPSAtkDctPolicyAPFloodQT_Type())
h3cWIPSAtkDctPolicyAPFloodQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyAPFloodQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyAPSpoofQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyAPSpoofQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyAPSpoofQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyAPSpoofQT=_H3cWIPSAtkDctPolicyAPSpoofQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,5),_H3cWIPSAtkDctPolicyAPSpoofQT_Type())
h3cWIPSAtkDctPolicyAPSpoofQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyAPSpoofQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyCliSpoofQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyCliSpoofQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyCliSpoofQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyCliSpoofQT=_H3cWIPSAtkDctPolicyCliSpoofQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,6),_H3cWIPSAtkDctPolicyCliSpoofQT_Type())
h3cWIPSAtkDctPolicyCliSpoofQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyCliSpoofQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyDosAssoQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyDosAssoQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyDosAssoQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyDosAssoQT=_H3cWIPSAtkDctPolicyDosAssoQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,7),_H3cWIPSAtkDctPolicyDosAssoQT_Type())
h3cWIPSAtkDctPolicyDosAssoQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyDosAssoQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyDosAuthQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyDosAuthQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyDosAuthQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyDosAuthQT=_H3cWIPSAtkDctPolicyDosAuthQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,8),_H3cWIPSAtkDctPolicyDosAuthQT_Type())
h3cWIPSAtkDctPolicyDosAuthQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyDosAuthQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyDosEAPOLStartQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyDosEAPOLStartQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyDosEAPOLStartQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyDosEAPOLStartQT=_H3cWIPSAtkDctPolicyDosEAPOLStartQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,9),_H3cWIPSAtkDctPolicyDosEAPOLStartQT_Type())
h3cWIPSAtkDctPolicyDosEAPOLStartQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyDosEAPOLStartQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyDosReAssoQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyDosReAssoQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyDosReAssoQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyDosReAssoQT=_H3cWIPSAtkDctPolicyDosReAssoQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,10),_H3cWIPSAtkDctPolicyDosReAssoQT_Type())
h3cWIPSAtkDctPolicyDosReAssoQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyDosReAssoQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyWeakIVQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyWeakIVQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyWeakIVQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyWeakIVQT=_H3cWIPSAtkDctPolicyWeakIVQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,11),_H3cWIPSAtkDctPolicyWeakIVQT_Type())
h3cWIPSAtkDctPolicyWeakIVQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyWeakIVQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyInvalidOUIAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_M,0),(_T,1)))
_H3cWIPSAtkDctPolicyInvalidOUIAction_Type.__name__=_F
_H3cWIPSAtkDctPolicyInvalidOUIAction_Object=MibTableColumn
h3cWIPSAtkDctPolicyInvalidOUIAction=_H3cWIPSAtkDctPolicyInvalidOUIAction_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,12),_H3cWIPSAtkDctPolicyInvalidOUIAction_Type())
h3cWIPSAtkDctPolicyInvalidOUIAction.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyInvalidOUIAction.setStatus(_A)
class _H3cWIPSAtkDctPolicyUnencryptedAuthApQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyUnencryptedAuthApQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyUnencryptedAuthApQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyUnencryptedAuthApQT=_H3cWIPSAtkDctPolicyUnencryptedAuthApQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,13),_H3cWIPSAtkDctPolicyUnencryptedAuthApQT_Type())
h3cWIPSAtkDctPolicyUnencryptedAuthApQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyUnencryptedAuthApQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyUnencryptedAuthClientQT=_H3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,14),_H3cWIPSAtkDctPolicyUnencryptedAuthClientQT_Type())
h3cWIPSAtkDctPolicyUnencryptedAuthClientQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyUnencryptedAuthClientQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyPSAttackQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyPSAttackQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyPSAttackQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyPSAttackQT=_H3cWIPSAtkDctPolicyPSAttackQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,15),_H3cWIPSAtkDctPolicyPSAttackQT_Type())
h3cWIPSAtkDctPolicyPSAttackQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyPSAttackQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyPSAttackMinOffPacket_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,150))
_H3cWIPSAtkDctPolicyPSAttackMinOffPacket_Type.__name__=_F
_H3cWIPSAtkDctPolicyPSAttackMinOffPacket_Object=MibTableColumn
h3cWIPSAtkDctPolicyPSAttackMinOffPacket=_H3cWIPSAtkDctPolicyPSAttackMinOffPacket_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,16),_H3cWIPSAtkDctPolicyPSAttackMinOffPacket_Type())
h3cWIPSAtkDctPolicyPSAttackMinOffPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyPSAttackMinOffPacket.setStatus(_A)
class _H3cWIPSAtkDctPolicyPSAttackOnOffPercent_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cWIPSAtkDctPolicyPSAttackOnOffPercent_Type.__name__=_F
_H3cWIPSAtkDctPolicyPSAttackOnOffPercent_Object=MibTableColumn
h3cWIPSAtkDctPolicyPSAttackOnOffPercent=_H3cWIPSAtkDctPolicyPSAttackOnOffPercent_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,17),_H3cWIPSAtkDctPolicyPSAttackOnOffPercent_Type())
h3cWIPSAtkDctPolicyPSAttackOnOffPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyPSAttackOnOffPercent.setStatus(_A)
class _H3cWIPSAtkDctPolicyApImpersonationQT_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSAtkDctPolicyApImpersonationQT_Type.__name__=_F
_H3cWIPSAtkDctPolicyApImpersonationQT_Object=MibTableColumn
h3cWIPSAtkDctPolicyApImpersonationQT=_H3cWIPSAtkDctPolicyApImpersonationQT_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,18),_H3cWIPSAtkDctPolicyApImpersonationQT_Type())
h3cWIPSAtkDctPolicyApImpersonationQT.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyApImpersonationQT.setStatus(_A)
class _H3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Type.__name__=_F
_H3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Object=MibTableColumn
h3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold=_H3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,19),_H3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold_Type())
h3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold.setStatus(_A)
class _H3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,360000))
_H3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Type.__name__=_F
_H3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Object=MibTableColumn
h3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime=_H3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,20),_H3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime_Type())
h3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime.setStatus(_A)
class _H3cWIPSAtkDctPolicySoftApConvertTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,600))
_H3cWIPSAtkDctPolicySoftApConvertTime_Type.__name__=_F
_H3cWIPSAtkDctPolicySoftApConvertTime_Object=MibTableColumn
h3cWIPSAtkDctPolicySoftApConvertTime=_H3cWIPSAtkDctPolicySoftApConvertTime_Object((1,3,6,1,4,1,2011,10,2,118,1,4,2,1,21),_H3cWIPSAtkDctPolicySoftApConvertTime_Type())
h3cWIPSAtkDctPolicySoftApConvertTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSAtkDctPolicySoftApConvertTime.setStatus(_A)
_H3cWIPSStaticCtmListCfgTable_Object=MibTable
h3cWIPSStaticCtmListCfgTable=_H3cWIPSStaticCtmListCfgTable_Object((1,3,6,1,4,1,2011,10,2,118,1,5))
if mibBuilder.loadTexts:h3cWIPSStaticCtmListCfgTable.setStatus(_A)
_H3cWIPSStaticCtmListCfgEntry_Object=MibTableRow
h3cWIPSStaticCtmListCfgEntry=_H3cWIPSStaticCtmListCfgEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,5,1))
h3cWIPSStaticCtmListCfgEntry.setIndexNames((0,_E,_A0))
if mibBuilder.loadTexts:h3cWIPSStaticCtmListCfgEntry.setStatus(_A)
_H3cWIPSStaticCtmListMAC_Type=MacAddress
_H3cWIPSStaticCtmListMAC_Object=MibTableColumn
h3cWIPSStaticCtmListMAC=_H3cWIPSStaticCtmListMAC_Object((1,3,6,1,4,1,2011,10,2,118,1,5,1,1),_H3cWIPSStaticCtmListMAC_Type())
h3cWIPSStaticCtmListMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSStaticCtmListMAC.setStatus(_A)
_H3cWIPSStaticCtmListRowStatus_Type=RowStatus
_H3cWIPSStaticCtmListRowStatus_Object=MibTableColumn
h3cWIPSStaticCtmListRowStatus=_H3cWIPSStaticCtmListRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,5,1,2),_H3cWIPSStaticCtmListRowStatus_Type())
h3cWIPSStaticCtmListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSStaticCtmListRowStatus.setStatus(_A)
_H3cWIPSStaticBlockListCfgTable_Object=MibTable
h3cWIPSStaticBlockListCfgTable=_H3cWIPSStaticBlockListCfgTable_Object((1,3,6,1,4,1,2011,10,2,118,1,6))
if mibBuilder.loadTexts:h3cWIPSStaticBlockListCfgTable.setStatus(_A)
_H3cWIPSStaticBlockListCfgEntry_Object=MibTableRow
h3cWIPSStaticBlockListCfgEntry=_H3cWIPSStaticBlockListCfgEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,6,1))
h3cWIPSStaticBlockListCfgEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:h3cWIPSStaticBlockListCfgEntry.setStatus(_A)
_H3cWIPSStaticBlockListMAC_Type=MacAddress
_H3cWIPSStaticBlockListMAC_Object=MibTableColumn
h3cWIPSStaticBlockListMAC=_H3cWIPSStaticBlockListMAC_Object((1,3,6,1,4,1,2011,10,2,118,1,6,1,1),_H3cWIPSStaticBlockListMAC_Type())
h3cWIPSStaticBlockListMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSStaticBlockListMAC.setStatus(_A)
_H3cWIPSStaticBlockListRowStatus_Type=RowStatus
_H3cWIPSStaticBlockListRowStatus_Object=MibTableColumn
h3cWIPSStaticBlockListRowStatus=_H3cWIPSStaticBlockListRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,6,1,2),_H3cWIPSStaticBlockListRowStatus_Type())
h3cWIPSStaticBlockListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSStaticBlockListRowStatus.setStatus(_A)
_H3cWIPSStaticTrustListCfgTable_Object=MibTable
h3cWIPSStaticTrustListCfgTable=_H3cWIPSStaticTrustListCfgTable_Object((1,3,6,1,4,1,2011,10,2,118,1,7))
if mibBuilder.loadTexts:h3cWIPSStaticTrustListCfgTable.setStatus(_A)
_H3cWIPSStaticTrustListCfgEntry_Object=MibTableRow
h3cWIPSStaticTrustListCfgEntry=_H3cWIPSStaticTrustListCfgEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,7,1))
h3cWIPSStaticTrustListCfgEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:h3cWIPSStaticTrustListCfgEntry.setStatus(_A)
_H3cWIPSStaticTrustListMAC_Type=MacAddress
_H3cWIPSStaticTrustListMAC_Object=MibTableColumn
h3cWIPSStaticTrustListMAC=_H3cWIPSStaticTrustListMAC_Object((1,3,6,1,4,1,2011,10,2,118,1,7,1,1),_H3cWIPSStaticTrustListMAC_Type())
h3cWIPSStaticTrustListMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSStaticTrustListMAC.setStatus(_A)
_H3cWIPSStaticTrustListRowStatus_Type=RowStatus
_H3cWIPSStaticTrustListRowStatus_Object=MibTableColumn
h3cWIPSStaticTrustListRowStatus=_H3cWIPSStaticTrustListRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,7,1,2),_H3cWIPSStaticTrustListRowStatus_Type())
h3cWIPSStaticTrustListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSStaticTrustListRowStatus.setStatus(_A)
_H3cWIPSIgnoreListCfgTable_Object=MibTable
h3cWIPSIgnoreListCfgTable=_H3cWIPSIgnoreListCfgTable_Object((1,3,6,1,4,1,2011,10,2,118,1,8))
if mibBuilder.loadTexts:h3cWIPSIgnoreListCfgTable.setStatus(_A)
_H3cWIPSIgnoreListCfgEntry_Object=MibTableRow
h3cWIPSIgnoreListCfgEntry=_H3cWIPSIgnoreListCfgEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,8,1))
h3cWIPSIgnoreListCfgEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:h3cWIPSIgnoreListCfgEntry.setStatus(_A)
_H3cWIPSIgnoreListMAC_Type=MacAddress
_H3cWIPSIgnoreListMAC_Object=MibTableColumn
h3cWIPSIgnoreListMAC=_H3cWIPSIgnoreListMAC_Object((1,3,6,1,4,1,2011,10,2,118,1,8,1,1),_H3cWIPSIgnoreListMAC_Type())
h3cWIPSIgnoreListMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSIgnoreListMAC.setStatus(_A)
_H3cWIPSIgnoreListRowStatus_Type=RowStatus
_H3cWIPSIgnoreListRowStatus_Object=MibTableColumn
h3cWIPSIgnoreListRowStatus=_H3cWIPSIgnoreListRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,8,1,2),_H3cWIPSIgnoreListRowStatus_Type())
h3cWIPSIgnoreListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSIgnoreListRowStatus.setStatus(_A)
_H3cWIPSDctModeTable_Object=MibTable
h3cWIPSDctModeTable=_H3cWIPSDctModeTable_Object((1,3,6,1,4,1,2011,10,2,118,1,9))
if mibBuilder.loadTexts:h3cWIPSDctModeTable.setStatus(_A)
_H3cWIPSDctModeEntry_Object=MibTableRow
h3cWIPSDctModeEntry=_H3cWIPSDctModeEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,9,1))
h3cWIPSDctModeEntry.setIndexNames((0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:h3cWIPSDctModeEntry.setStatus(_A)
class _H3cWIPSDctModeAPName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cWIPSDctModeAPName_Type.__name__=_H
_H3cWIPSDctModeAPName_Object=MibTableColumn
h3cWIPSDctModeAPName=_H3cWIPSDctModeAPName_Object((1,3,6,1,4,1,2011,10,2,118,1,9,1,1),_H3cWIPSDctModeAPName_Type())
h3cWIPSDctModeAPName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctModeAPName.setStatus(_A)
class _H3cWIPSDctModeRadio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_H3cWIPSDctModeRadio_Type.__name__=_F
_H3cWIPSDctModeRadio_Object=MibTableColumn
h3cWIPSDctModeRadio=_H3cWIPSDctModeRadio_Object((1,3,6,1,4,1,2011,10,2,118,1,9,1,2),_H3cWIPSDctModeRadio_Type())
h3cWIPSDctModeRadio.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctModeRadio.setStatus(_A)
class _H3cWIPSDctModeScanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_r,1),(_s,2),(_t,3),(_u,4)))
_H3cWIPSDctModeScanMode_Type.__name__=_F
_H3cWIPSDctModeScanMode_Object=MibTableColumn
h3cWIPSDctModeScanMode=_H3cWIPSDctModeScanMode_Object((1,3,6,1,4,1,2011,10,2,118,1,9,1,3),_H3cWIPSDctModeScanMode_Type())
h3cWIPSDctModeScanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSDctModeScanMode.setStatus(_A)
_H3cWIPSDctModeRowStatus_Type=RowStatus
_H3cWIPSDctModeRowStatus_Object=MibTableColumn
h3cWIPSDctModeRowStatus=_H3cWIPSDctModeRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,9,1,4),_H3cWIPSDctModeRowStatus_Type())
h3cWIPSDctModeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSDctModeRowStatus.setStatus(_A)
_H3cWIPSSigConfigGroup_ObjectIdentity=ObjectIdentity
h3cWIPSSigConfigGroup=_H3cWIPSSigConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,118,1,10))
_H3cWIPSSigPolicyTable_Object=MibTable
h3cWIPSSigPolicyTable=_H3cWIPSSigPolicyTable_Object((1,3,6,1,4,1,2011,10,2,118,1,10,1))
if mibBuilder.loadTexts:h3cWIPSSigPolicyTable.setStatus(_A)
_H3cWIPSSigPolicyEntry_Object=MibTableRow
h3cWIPSSigPolicyEntry=_H3cWIPSSigPolicyEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,10,1,1))
h3cWIPSSigPolicyEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:h3cWIPSSigPolicyEntry.setStatus(_A)
class _H3cWIPSSigPolicyNameCfg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSSigPolicyNameCfg_Type.__name__=_H
_H3cWIPSSigPolicyNameCfg_Object=MibTableColumn
h3cWIPSSigPolicyNameCfg=_H3cWIPSSigPolicyNameCfg_Object((1,3,6,1,4,1,2011,10,2,118,1,10,1,1,1),_H3cWIPSSigPolicyNameCfg_Type())
h3cWIPSSigPolicyNameCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSSigPolicyNameCfg.setStatus(_A)
_H3cWIPSSigPolicyRowStatus_Type=RowStatus
_H3cWIPSSigPolicyRowStatus_Object=MibTableColumn
h3cWIPSSigPolicyRowStatus=_H3cWIPSSigPolicyRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,10,1,1,2),_H3cWIPSSigPolicyRowStatus_Type())
h3cWIPSSigPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigPolicyRowStatus.setStatus(_A)
_H3cWIPSSigRule2PolicyTable_Object=MibTable
h3cWIPSSigRule2PolicyTable=_H3cWIPSSigRule2PolicyTable_Object((1,3,6,1,4,1,2011,10,2,118,1,10,2))
if mibBuilder.loadTexts:h3cWIPSSigRule2PolicyTable.setStatus(_A)
_H3cWIPSSigRule2PolicyEntry_Object=MibTableRow
h3cWIPSSigRule2PolicyEntry=_H3cWIPSSigRule2PolicyEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,10,2,1))
h3cWIPSSigRule2PolicyEntry.setIndexNames((0,_E,_W),(0,_E,_A6))
if mibBuilder.loadTexts:h3cWIPSSigRule2PolicyEntry.setStatus(_A)
class _H3cWIPSSigRule2PolicySigRuleIDCfg_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cWIPSSigRule2PolicySigRuleIDCfg_Type.__name__=_J
_H3cWIPSSigRule2PolicySigRuleIDCfg_Object=MibTableColumn
h3cWIPSSigRule2PolicySigRuleIDCfg=_H3cWIPSSigRule2PolicySigRuleIDCfg_Object((1,3,6,1,4,1,2011,10,2,118,1,10,2,1,1),_H3cWIPSSigRule2PolicySigRuleIDCfg_Type())
h3cWIPSSigRule2PolicySigRuleIDCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSSigRule2PolicySigRuleIDCfg.setStatus(_A)
_H3cWIPSSigRule2PolicyRowStatus_Type=RowStatus
_H3cWIPSSigRule2PolicyRowStatus_Object=MibTableColumn
h3cWIPSSigRule2PolicyRowStatus=_H3cWIPSSigRule2PolicyRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,10,2,1,2),_H3cWIPSSigRule2PolicyRowStatus_Type())
h3cWIPSSigRule2PolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRule2PolicyRowStatus.setStatus(_A)
class _H3cWIPSSigRule2PolicyPrecedence_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cWIPSSigRule2PolicyPrecedence_Type.__name__=_J
_H3cWIPSSigRule2PolicyPrecedence_Object=MibTableColumn
h3cWIPSSigRule2PolicyPrecedence=_H3cWIPSSigRule2PolicyPrecedence_Object((1,3,6,1,4,1,2011,10,2,118,1,10,2,1,3),_H3cWIPSSigRule2PolicyPrecedence_Type())
h3cWIPSSigRule2PolicyPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRule2PolicyPrecedence.setStatus(_A)
_H3cWIPSSigRuleTable_Object=MibTable
h3cWIPSSigRuleTable=_H3cWIPSSigRuleTable_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3))
if mibBuilder.loadTexts:h3cWIPSSigRuleTable.setStatus(_A)
_H3cWIPSSigRuleEntry_Object=MibTableRow
h3cWIPSSigRuleEntry=_H3cWIPSSigRuleEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1))
h3cWIPSSigRuleEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:h3cWIPSSigRuleEntry.setStatus(_A)
class _H3cWIPSSigRuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSSigRuleName_Type.__name__=_H
_H3cWIPSSigRuleName_Object=MibTableColumn
h3cWIPSSigRuleName=_H3cWIPSSigRuleName_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,1),_H3cWIPSSigRuleName_Type())
h3cWIPSSigRuleName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSSigRuleName.setStatus(_A)
class _H3cWIPSSigRuleID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cWIPSSigRuleID_Type.__name__=_F
_H3cWIPSSigRuleID_Object=MibTableColumn
h3cWIPSSigRuleID=_H3cWIPSSigRuleID_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,2),_H3cWIPSSigRuleID_Type())
h3cWIPSSigRuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRuleID.setStatus(_A)
_H3cWIPSSigRuleRowStatus_Type=RowStatus
_H3cWIPSSigRuleRowStatus_Object=MibTableColumn
h3cWIPSSigRuleRowStatus=_H3cWIPSSigRuleRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,3),_H3cWIPSSigRuleRowStatus_Type())
h3cWIPSSigRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRuleRowStatus.setStatus(_A)
_H3cWIPSSigSubRuleMatchAll_Type=TruthValue
_H3cWIPSSigSubRuleMatchAll_Object=MibTableColumn
h3cWIPSSigSubRuleMatchAll=_H3cWIPSSigSubRuleMatchAll_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,4),_H3cWIPSSigSubRuleMatchAll_Type())
h3cWIPSSigSubRuleMatchAll.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleMatchAll.setStatus(_A)
_H3cWIPSSigRuleDctPeriod_Type=Unsigned32
_H3cWIPSSigRuleDctPeriod_Object=MibTableColumn
h3cWIPSSigRuleDctPeriod=_H3cWIPSSigRuleDctPeriod_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,5),_H3cWIPSSigRuleDctPeriod_Type())
h3cWIPSSigRuleDctPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRuleDctPeriod.setStatus(_A)
if mibBuilder.loadTexts:h3cWIPSSigRuleDctPeriod.setUnits(_L)
class _H3cWIPSSigRuleTrackMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('perSig',1),('perMAC',2),('both',3)))
_H3cWIPSSigRuleTrackMethod_Type.__name__=_F
_H3cWIPSSigRuleTrackMethod_Object=MibTableColumn
h3cWIPSSigRuleTrackMethod=_H3cWIPSSigRuleTrackMethod_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,6),_H3cWIPSSigRuleTrackMethod_Type())
h3cWIPSSigRuleTrackMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRuleTrackMethod.setStatus(_A)
_H3cWIPSSigRuleDctThresholdPerMAC_Type=Unsigned32
_H3cWIPSSigRuleDctThresholdPerMAC_Object=MibTableColumn
h3cWIPSSigRuleDctThresholdPerMAC=_H3cWIPSSigRuleDctThresholdPerMAC_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,7),_H3cWIPSSigRuleDctThresholdPerMAC_Type())
h3cWIPSSigRuleDctThresholdPerMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRuleDctThresholdPerMAC.setStatus(_A)
_H3cWIPSSigRuleDctThresholdPerSig_Type=Unsigned32
_H3cWIPSSigRuleDctThresholdPerSig_Object=MibTableColumn
h3cWIPSSigRuleDctThresholdPerSig=_H3cWIPSSigRuleDctThresholdPerSig_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,8),_H3cWIPSSigRuleDctThresholdPerSig_Type())
h3cWIPSSigRuleDctThresholdPerSig.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRuleDctThresholdPerSig.setStatus(_A)
_H3cWIPSSigRuleActionEvtLevel_Type=Unsigned32
_H3cWIPSSigRuleActionEvtLevel_Object=MibTableColumn
h3cWIPSSigRuleActionEvtLevel=_H3cWIPSSigRuleActionEvtLevel_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,9),_H3cWIPSSigRuleActionEvtLevel_Type())
h3cWIPSSigRuleActionEvtLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRuleActionEvtLevel.setStatus(_A)
_H3cWIPSSigRuleQuietTime_Type=Unsigned32
_H3cWIPSSigRuleQuietTime_Object=MibTableColumn
h3cWIPSSigRuleQuietTime=_H3cWIPSSigRuleQuietTime_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,10),_H3cWIPSSigRuleQuietTime_Type())
h3cWIPSSigRuleQuietTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigRuleQuietTime.setStatus(_A)
class _H3cWIPSSigSubRuleFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('manage',0),('control',1),('data',2),('undo',3)))
_H3cWIPSSigSubRuleFrameType_Type.__name__=_F
_H3cWIPSSigSubRuleFrameType_Object=MibTableColumn
h3cWIPSSigSubRuleFrameType=_H3cWIPSSigSubRuleFrameType_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,11),_H3cWIPSSigSubRuleFrameType_Type())
h3cWIPSSigSubRuleFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleFrameType.setStatus(_A)
class _H3cWIPSSigSubRuleFrameSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,0),('assocReq',1),('assocRes',2),('probeReq',3),('beacon',4),('disasso',5),('auth',6),('deauth',7)))
_H3cWIPSSigSubRuleFrameSubType_Type.__name__=_F
_H3cWIPSSigSubRuleFrameSubType_Object=MibTableColumn
h3cWIPSSigSubRuleFrameSubType=_H3cWIPSSigSubRuleFrameSubType_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,12),_H3cWIPSSigSubRuleFrameSubType_Type())
h3cWIPSSigSubRuleFrameSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleFrameSubType.setStatus(_A)
class _H3cWIPSSigSubRuleMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_H3cWIPSSigSubRuleMac_Type.__name__=_H
_H3cWIPSSigSubRuleMac_Object=MibTableColumn
h3cWIPSSigSubRuleMac=_H3cWIPSSigSubRuleMac_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,13),_H3cWIPSSigSubRuleMac_Type())
h3cWIPSSigSubRuleMac.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleMac.setStatus(_A)
class _H3cWIPSSigSubRuleMacType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('source',0),('dest',1),('bssid',2)))
_H3cWIPSSigSubRuleMacType_Type.__name__=_F
_H3cWIPSSigSubRuleMacType_Object=MibTableColumn
h3cWIPSSigSubRuleMacType=_H3cWIPSSigSubRuleMacType_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,14),_H3cWIPSSigSubRuleMacType_Type())
h3cWIPSSigSubRuleMacType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleMacType.setStatus(_A)
_H3cWIPSSigSubRuleSeqNumMin_Type=Unsigned32
_H3cWIPSSigSubRuleSeqNumMin_Object=MibTableColumn
h3cWIPSSigSubRuleSeqNumMin=_H3cWIPSSigSubRuleSeqNumMin_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,15),_H3cWIPSSigSubRuleSeqNumMin_Type())
h3cWIPSSigSubRuleSeqNumMin.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleSeqNumMin.setStatus(_A)
_H3cWIPSSigSubRuleSeqNumMax_Type=Unsigned32
_H3cWIPSSigSubRuleSeqNumMax_Object=MibTableColumn
h3cWIPSSigSubRuleSeqNumMax=_H3cWIPSSigSubRuleSeqNumMax_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,16),_H3cWIPSSigSubRuleSeqNumMax_Type())
h3cWIPSSigSubRuleSeqNumMax.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleSeqNumMax.setStatus(_A)
_H3cWIPSSigSubRuleSSIDLenMin_Type=Unsigned32
_H3cWIPSSigSubRuleSSIDLenMin_Object=MibTableColumn
h3cWIPSSigSubRuleSSIDLenMin=_H3cWIPSSigSubRuleSSIDLenMin_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,17),_H3cWIPSSigSubRuleSSIDLenMin_Type())
h3cWIPSSigSubRuleSSIDLenMin.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleSSIDLenMin.setStatus(_A)
_H3cWIPSSigSubRuleSSIDLenMax_Type=Unsigned32
_H3cWIPSSigSubRuleSSIDLenMax_Object=MibTableColumn
h3cWIPSSigSubRuleSSIDLenMax=_H3cWIPSSigSubRuleSSIDLenMax_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,18),_H3cWIPSSigSubRuleSSIDLenMax_Type())
h3cWIPSSigSubRuleSSIDLenMax.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleSSIDLenMax.setStatus(_A)
class _H3cWIPSSigSubRuleSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWIPSSigSubRuleSSID_Type.__name__=_H
_H3cWIPSSigSubRuleSSID_Object=MibTableColumn
h3cWIPSSigSubRuleSSID=_H3cWIPSSigSubRuleSSID_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,19),_H3cWIPSSigSubRuleSSID_Type())
h3cWIPSSigSubRuleSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleSSID.setStatus(_A)
class _H3cWIPSSigSubRuleSSIDOpe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_w,2),(_P,3),(_x,4)))
_H3cWIPSSigSubRuleSSIDOpe_Type.__name__=_F
_H3cWIPSSigSubRuleSSIDOpe_Object=MibTableColumn
h3cWIPSSigSubRuleSSIDOpe=_H3cWIPSSigSubRuleSSIDOpe_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,20),_H3cWIPSSigSubRuleSSIDOpe_Type())
h3cWIPSSigSubRuleSSIDOpe.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleSSIDOpe.setStatus(_A)
class _H3cWIPSSigSubRuleSSIDCase_Type(TruthValue):defaultValue=2
_H3cWIPSSigSubRuleSSIDCase_Type.__name__=_K
_H3cWIPSSigSubRuleSSIDCase_Object=MibTableColumn
h3cWIPSSigSubRuleSSIDCase=_H3cWIPSSigSubRuleSSIDCase_Object((1,3,6,1,4,1,2011,10,2,118,1,10,3,1,21),_H3cWIPSSigSubRuleSSIDCase_Type())
h3cWIPSSigSubRuleSSIDCase.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleSSIDCase.setStatus(_A)
_H3cWIPSSigSubRulePatternTable_Object=MibTable
h3cWIPSSigSubRulePatternTable=_H3cWIPSSigSubRulePatternTable_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4))
if mibBuilder.loadTexts:h3cWIPSSigSubRulePatternTable.setStatus(_A)
_H3cWIPSSigSubRulePatternEntry_Object=MibTableRow
h3cWIPSSigSubRulePatternEntry=_H3cWIPSSigSubRulePatternEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4,1))
h3cWIPSSigSubRulePatternEntry.setIndexNames((0,_E,_X),(0,_E,_A7))
if mibBuilder.loadTexts:h3cWIPSSigSubRulePatternEntry.setStatus(_A)
class _H3cWIPSSigSubRulePatternID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,27))
_H3cWIPSSigSubRulePatternID_Type.__name__=_J
_H3cWIPSSigSubRulePatternID_Object=MibTableColumn
h3cWIPSSigSubRulePatternID=_H3cWIPSSigSubRulePatternID_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4,1,1),_H3cWIPSSigSubRulePatternID_Type())
h3cWIPSSigSubRulePatternID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSSigSubRulePatternID.setStatus(_A)
_H3cWIPSSigSubRuleRowStatus_Type=RowStatus
_H3cWIPSSigSubRuleRowStatus_Object=MibTableColumn
h3cWIPSSigSubRuleRowStatus=_H3cWIPSSigSubRuleRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4,1,2),_H3cWIPSSigSubRuleRowStatus_Type())
h3cWIPSSigSubRuleRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSSigSubRuleRowStatus.setStatus(_A)
class _H3cWIPSSigSubRulePatternName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWIPSSigSubRulePatternName_Type.__name__=_H
_H3cWIPSSigSubRulePatternName_Object=MibTableColumn
h3cWIPSSigSubRulePatternName=_H3cWIPSSigSubRulePatternName_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4,1,3),_H3cWIPSSigSubRulePatternName_Type())
h3cWIPSSigSubRulePatternName.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSSigSubRulePatternName.setStatus(_A)
class _H3cWIPSSigSubRulePatternOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2346))
_H3cWIPSSigSubRulePatternOffset_Type.__name__=_F
_H3cWIPSSigSubRulePatternOffset_Object=MibTableColumn
h3cWIPSSigSubRulePatternOffset=_H3cWIPSSigSubRulePatternOffset_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4,1,4),_H3cWIPSSigSubRulePatternOffset_Type())
h3cWIPSSigSubRulePatternOffset.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSSigSubRulePatternOffset.setStatus(_A)
class _H3cWIPSSigSubRulePatternMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cWIPSSigSubRulePatternMask_Type.__name__=_F
_H3cWIPSSigSubRulePatternMask_Object=MibTableColumn
h3cWIPSSigSubRulePatternMask=_H3cWIPSSigSubRulePatternMask_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4,1,5),_H3cWIPSSigSubRulePatternMask_Type())
h3cWIPSSigSubRulePatternMask.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSSigSubRulePatternMask.setStatus(_A)
class _H3cWIPSSigSubRulePatternValueMin_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSSigSubRulePatternValueMin_Type.__name__=_J
_H3cWIPSSigSubRulePatternValueMin_Object=MibTableColumn
h3cWIPSSigSubRulePatternValueMin=_H3cWIPSSigSubRulePatternValueMin_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4,1,6),_H3cWIPSSigSubRulePatternValueMin_Type())
h3cWIPSSigSubRulePatternValueMin.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSSigSubRulePatternValueMin.setStatus(_A)
class _H3cWIPSSigSubRulePatternValueMax_Type(Unsigned32):defaultValue=4294967295
_H3cWIPSSigSubRulePatternValueMax_Type.__name__=_J
_H3cWIPSSigSubRulePatternValueMax_Object=MibTableColumn
h3cWIPSSigSubRulePatternValueMax=_H3cWIPSSigSubRulePatternValueMax_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4,1,7),_H3cWIPSSigSubRulePatternValueMax_Type())
h3cWIPSSigSubRulePatternValueMax.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSSigSubRulePatternValueMax.setStatus(_A)
class _H3cWIPSSigSubRulePatternFromPayload_Type(TruthValue):defaultValue=2
_H3cWIPSSigSubRulePatternFromPayload_Type.__name__=_K
_H3cWIPSSigSubRulePatternFromPayload_Object=MibTableColumn
h3cWIPSSigSubRulePatternFromPayload=_H3cWIPSSigSubRulePatternFromPayload_Object((1,3,6,1,4,1,2011,10,2,118,1,10,4,1,8),_H3cWIPSSigSubRulePatternFromPayload_Type())
h3cWIPSSigSubRulePatternFromPayload.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSSigSubRulePatternFromPayload.setStatus(_A)
_H3cWIPSCtmConfigGroup_ObjectIdentity=ObjectIdentity
h3cWIPSCtmConfigGroup=_H3cWIPSCtmConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,118,1,11))
class _H3cWIPSCtmPolicyCfgSupportSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_H3cWIPSCtmPolicyCfgSupportSet_Type.__name__=_H
_H3cWIPSCtmPolicyCfgSupportSet_Object=MibScalar
h3cWIPSCtmPolicyCfgSupportSet=_H3cWIPSCtmPolicyCfgSupportSet_Object((1,3,6,1,4,1,2011,10,2,118,1,11,1),_H3cWIPSCtmPolicyCfgSupportSet_Type())
h3cWIPSCtmPolicyCfgSupportSet.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyCfgSupportSet.setStatus(_A)
_H3cWIPSCtmPolicyTable_Object=MibTable
h3cWIPSCtmPolicyTable=_H3cWIPSCtmPolicyTable_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2))
if mibBuilder.loadTexts:h3cWIPSCtmPolicyTable.setStatus(_A)
_H3cWIPSCtmPolicyEntry_Object=MibTableRow
h3cWIPSCtmPolicyEntry=_H3cWIPSCtmPolicyEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1))
h3cWIPSCtmPolicyEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:h3cWIPSCtmPolicyEntry.setStatus(_A)
class _H3cWIPSCtmPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSCtmPolicyName_Type.__name__=_H
_H3cWIPSCtmPolicyName_Object=MibTableColumn
h3cWIPSCtmPolicyName=_H3cWIPSCtmPolicyName_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,1),_H3cWIPSCtmPolicyName_Type())
h3cWIPSCtmPolicyName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyName.setStatus(_A)
_H3cWIPSCtmPolicyCfgRowStatus_Type=RowStatus
_H3cWIPSCtmPolicyCfgRowStatus_Object=MibTableColumn
h3cWIPSCtmPolicyCfgRowStatus=_H3cWIPSCtmPolicyCfgRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,2),_H3cWIPSCtmPolicyCfgRowStatus_Type())
h3cWIPSCtmPolicyCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyCfgRowStatus.setStatus(_A)
class _H3cWIPSCtmPolicyBitString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_H3cWIPSCtmPolicyBitString_Type.__name__=_H
_H3cWIPSCtmPolicyBitString_Object=MibTableColumn
h3cWIPSCtmPolicyBitString=_H3cWIPSCtmPolicyBitString_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,3),_H3cWIPSCtmPolicyBitString_Type())
h3cWIPSCtmPolicyBitString.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyBitString.setStatus(_A)
class _H3cWIPSCtmPolicyFixedChl_Type(TruthValue):defaultValue=2
_H3cWIPSCtmPolicyFixedChl_Type.__name__=_K
_H3cWIPSCtmPolicyFixedChl_Object=MibTableColumn
h3cWIPSCtmPolicyFixedChl=_H3cWIPSCtmPolicyFixedChl_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,4),_H3cWIPSCtmPolicyFixedChl_Type())
h3cWIPSCtmPolicyFixedChl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyFixedChl.setStatus(_A)
class _H3cWIPSCtmPolicyRogueAPPre_Type(Unsigned32):defaultValue=9
_H3cWIPSCtmPolicyRogueAPPre_Type.__name__=_J
_H3cWIPSCtmPolicyRogueAPPre_Object=MibTableColumn
h3cWIPSCtmPolicyRogueAPPre=_H3cWIPSCtmPolicyRogueAPPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,5),_H3cWIPSCtmPolicyRogueAPPre_Type())
h3cWIPSCtmPolicyRogueAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyRogueAPPre.setStatus(_A)
class _H3cWIPSCtmPolicyPtRogueAPPre_Type(Unsigned32):defaultValue=7
_H3cWIPSCtmPolicyPtRogueAPPre_Type.__name__=_J
_H3cWIPSCtmPolicyPtRogueAPPre_Object=MibTableColumn
h3cWIPSCtmPolicyPtRogueAPPre=_H3cWIPSCtmPolicyPtRogueAPPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,6),_H3cWIPSCtmPolicyPtRogueAPPre_Type())
h3cWIPSCtmPolicyPtRogueAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyPtRogueAPPre.setStatus(_A)
class _H3cWIPSCtmPolicyMisconfAPPre_Type(Unsigned32):defaultValue=3
_H3cWIPSCtmPolicyMisconfAPPre_Type.__name__=_J
_H3cWIPSCtmPolicyMisconfAPPre_Object=MibTableColumn
h3cWIPSCtmPolicyMisconfAPPre=_H3cWIPSCtmPolicyMisconfAPPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,7),_H3cWIPSCtmPolicyMisconfAPPre_Type())
h3cWIPSCtmPolicyMisconfAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyMisconfAPPre.setStatus(_A)
class _H3cWIPSCtmPolicyExternalAPPre_Type(Unsigned32):defaultValue=1
_H3cWIPSCtmPolicyExternalAPPre_Type.__name__=_J
_H3cWIPSCtmPolicyExternalAPPre_Object=MibTableColumn
h3cWIPSCtmPolicyExternalAPPre=_H3cWIPSCtmPolicyExternalAPPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,8),_H3cWIPSCtmPolicyExternalAPPre_Type())
h3cWIPSCtmPolicyExternalAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyExternalAPPre.setStatus(_A)
class _H3cWIPSCtmPolicyPtExternalAPPre_Type(Unsigned32):defaultValue=2
_H3cWIPSCtmPolicyPtExternalAPPre_Type.__name__=_J
_H3cWIPSCtmPolicyPtExternalAPPre_Object=MibTableColumn
h3cWIPSCtmPolicyPtExternalAPPre=_H3cWIPSCtmPolicyPtExternalAPPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,9),_H3cWIPSCtmPolicyPtExternalAPPre_Type())
h3cWIPSCtmPolicyPtExternalAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyPtExternalAPPre.setStatus(_A)
class _H3cWIPSCtmPolicyUncateAPPre_Type(Unsigned32):defaultValue=5
_H3cWIPSCtmPolicyUncateAPPre_Type.__name__=_J
_H3cWIPSCtmPolicyUncateAPPre_Object=MibTableColumn
h3cWIPSCtmPolicyUncateAPPre=_H3cWIPSCtmPolicyUncateAPPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,10),_H3cWIPSCtmPolicyUncateAPPre_Type())
h3cWIPSCtmPolicyUncateAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyUncateAPPre.setStatus(_A)
class _H3cWIPSCtmPolicyPtAuthAPPre_Type(Unsigned32):defaultValue=0
_H3cWIPSCtmPolicyPtAuthAPPre_Type.__name__=_J
_H3cWIPSCtmPolicyPtAuthAPPre_Object=MibTableColumn
h3cWIPSCtmPolicyPtAuthAPPre=_H3cWIPSCtmPolicyPtAuthAPPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,11),_H3cWIPSCtmPolicyPtAuthAPPre_Type())
h3cWIPSCtmPolicyPtAuthAPPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyPtAuthAPPre.setStatus(_A)
class _H3cWIPSCtmPolicyMisassoStaPre_Type(Unsigned32):defaultValue=6
_H3cWIPSCtmPolicyMisassoStaPre_Type.__name__=_J
_H3cWIPSCtmPolicyMisassoStaPre_Object=MibTableColumn
h3cWIPSCtmPolicyMisassoStaPre=_H3cWIPSCtmPolicyMisassoStaPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,12),_H3cWIPSCtmPolicyMisassoStaPre_Type())
h3cWIPSCtmPolicyMisassoStaPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyMisassoStaPre.setStatus(_A)
class _H3cWIPSCtmPolicyUncateStaPre_Type(Unsigned32):defaultValue=4
_H3cWIPSCtmPolicyUncateStaPre_Type.__name__=_J
_H3cWIPSCtmPolicyUncateStaPre_Object=MibTableColumn
h3cWIPSCtmPolicyUncateStaPre=_H3cWIPSCtmPolicyUncateStaPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,13),_H3cWIPSCtmPolicyUncateStaPre_Type())
h3cWIPSCtmPolicyUncateStaPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyUncateStaPre.setStatus(_A)
class _H3cWIPSCtmPolicyUnauthStaPre_Type(Unsigned32):defaultValue=8
_H3cWIPSCtmPolicyUnauthStaPre_Type.__name__=_J
_H3cWIPSCtmPolicyUnauthStaPre_Object=MibTableColumn
h3cWIPSCtmPolicyUnauthStaPre=_H3cWIPSCtmPolicyUnauthStaPre_Object((1,3,6,1,4,1,2011,10,2,118,1,11,2,1,14),_H3cWIPSCtmPolicyUnauthStaPre_Type())
h3cWIPSCtmPolicyUnauthStaPre.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyUnauthStaPre.setStatus(_A)
_H3cWIPSCtmPolicyDevListTable_Object=MibTable
h3cWIPSCtmPolicyDevListTable=_H3cWIPSCtmPolicyDevListTable_Object((1,3,6,1,4,1,2011,10,2,118,1,11,3))
if mibBuilder.loadTexts:h3cWIPSCtmPolicyDevListTable.setStatus(_A)
_H3cWIPSCtmPolicyDevListEntry_Object=MibTableRow
h3cWIPSCtmPolicyDevListEntry=_H3cWIPSCtmPolicyDevListEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,11,3,1))
h3cWIPSCtmPolicyDevListEntry.setIndexNames((0,_E,_Y),(0,_E,_A8))
if mibBuilder.loadTexts:h3cWIPSCtmPolicyDevListEntry.setStatus(_A)
_H3cWIPSCtmPolicyDevMAC_Type=MacAddress
_H3cWIPSCtmPolicyDevMAC_Object=MibTableColumn
h3cWIPSCtmPolicyDevMAC=_H3cWIPSCtmPolicyDevMAC_Object((1,3,6,1,4,1,2011,10,2,118,1,11,3,1,1),_H3cWIPSCtmPolicyDevMAC_Type())
h3cWIPSCtmPolicyDevMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyDevMAC.setStatus(_A)
_H3cWIPSCtmPolicyDevRowStatus_Type=RowStatus
_H3cWIPSCtmPolicyDevRowStatus_Object=MibTableColumn
h3cWIPSCtmPolicyDevRowStatus=_H3cWIPSCtmPolicyDevRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,11,3,1,2),_H3cWIPSCtmPolicyDevRowStatus_Type())
h3cWIPSCtmPolicyDevRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSCtmPolicyDevRowStatus.setStatus(_A)
_H3cWIPSMalPktDctConfigGroup_ObjectIdentity=ObjectIdentity
h3cWIPSMalPktDctConfigGroup=_H3cWIPSMalPktDctConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,118,1,12))
class _H3cWIPSMalPktDctCfgLogSupportSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_H3cWIPSMalPktDctCfgLogSupportSet_Type.__name__=_H
_H3cWIPSMalPktDctCfgLogSupportSet_Object=MibScalar
h3cWIPSMalPktDctCfgLogSupportSet=_H3cWIPSMalPktDctCfgLogSupportSet_Object((1,3,6,1,4,1,2011,10,2,118,1,12,1),_H3cWIPSMalPktDctCfgLogSupportSet_Type())
h3cWIPSMalPktDctCfgLogSupportSet.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktDctCfgLogSupportSet.setStatus(_A)
class _H3cWIPSMalPktDctCfgTrapSupportSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_H3cWIPSMalPktDctCfgTrapSupportSet_Type.__name__=_H
_H3cWIPSMalPktDctCfgTrapSupportSet_Object=MibScalar
h3cWIPSMalPktDctCfgTrapSupportSet=_H3cWIPSMalPktDctCfgTrapSupportSet_Object((1,3,6,1,4,1,2011,10,2,118,1,12,2),_H3cWIPSMalPktDctCfgTrapSupportSet_Type())
h3cWIPSMalPktDctCfgTrapSupportSet.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktDctCfgTrapSupportSet.setStatus(_A)
_H3cWIPSMalPktDctPolicyTable_Object=MibTable
h3cWIPSMalPktDctPolicyTable=_H3cWIPSMalPktDctPolicyTable_Object((1,3,6,1,4,1,2011,10,2,118,1,12,3))
if mibBuilder.loadTexts:h3cWIPSMalPktDctPolicyTable.setStatus(_A)
_H3cWIPSMalPktDctPolicyEntry_Object=MibTableRow
h3cWIPSMalPktDctPolicyEntry=_H3cWIPSMalPktDctPolicyEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,12,3,1))
h3cWIPSMalPktDctPolicyEntry.setIndexNames((0,_E,_A9))
if mibBuilder.loadTexts:h3cWIPSMalPktDctPolicyEntry.setStatus(_A)
class _H3cWIPSMalPktDctPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSMalPktDctPolicyName_Type.__name__=_H
_H3cWIPSMalPktDctPolicyName_Object=MibTableColumn
h3cWIPSMalPktDctPolicyName=_H3cWIPSMalPktDctPolicyName_Object((1,3,6,1,4,1,2011,10,2,118,1,12,3,1,1),_H3cWIPSMalPktDctPolicyName_Type())
h3cWIPSMalPktDctPolicyName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSMalPktDctPolicyName.setStatus(_A)
_H3cWIPSMalPktDctPolicyCfgRowStatus_Type=RowStatus
_H3cWIPSMalPktDctPolicyCfgRowStatus_Object=MibTableColumn
h3cWIPSMalPktDctPolicyCfgRowStatus=_H3cWIPSMalPktDctPolicyCfgRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,12,3,1,2),_H3cWIPSMalPktDctPolicyCfgRowStatus_Type())
h3cWIPSMalPktDctPolicyCfgRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMalPktDctPolicyCfgRowStatus.setStatus(_A)
class _H3cWIPSMalPktDctPolicyLogBitString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_H3cWIPSMalPktDctPolicyLogBitString_Type.__name__=_H
_H3cWIPSMalPktDctPolicyLogBitString_Object=MibTableColumn
h3cWIPSMalPktDctPolicyLogBitString=_H3cWIPSMalPktDctPolicyLogBitString_Object((1,3,6,1,4,1,2011,10,2,118,1,12,3,1,3),_H3cWIPSMalPktDctPolicyLogBitString_Type())
h3cWIPSMalPktDctPolicyLogBitString.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMalPktDctPolicyLogBitString.setStatus(_A)
class _H3cWIPSMalPktDctPolicyTrapBitString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_H3cWIPSMalPktDctPolicyTrapBitString_Type.__name__=_H
_H3cWIPSMalPktDctPolicyTrapBitString_Object=MibTableColumn
h3cWIPSMalPktDctPolicyTrapBitString=_H3cWIPSMalPktDctPolicyTrapBitString_Object((1,3,6,1,4,1,2011,10,2,118,1,12,3,1,4),_H3cWIPSMalPktDctPolicyTrapBitString_Type())
h3cWIPSMalPktDctPolicyTrapBitString.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMalPktDctPolicyTrapBitString.setStatus(_A)
class _H3cWIPSMalPktDctPolicyDurationThreshold_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_H3cWIPSMalPktDctPolicyDurationThreshold_Type.__name__=_F
_H3cWIPSMalPktDctPolicyDurationThreshold_Object=MibTableColumn
h3cWIPSMalPktDctPolicyDurationThreshold=_H3cWIPSMalPktDctPolicyDurationThreshold_Object((1,3,6,1,4,1,2011,10,2,118,1,12,3,1,5),_H3cWIPSMalPktDctPolicyDurationThreshold_Type())
h3cWIPSMalPktDctPolicyDurationThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMalPktDctPolicyDurationThreshold.setStatus(_A)
class _H3cWIPSMalPktDctPolicyQuietTime_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,604800))
_H3cWIPSMalPktDctPolicyQuietTime_Type.__name__=_F
_H3cWIPSMalPktDctPolicyQuietTime_Object=MibTableColumn
h3cWIPSMalPktDctPolicyQuietTime=_H3cWIPSMalPktDctPolicyQuietTime_Object((1,3,6,1,4,1,2011,10,2,118,1,12,3,1,6),_H3cWIPSMalPktDctPolicyQuietTime_Type())
h3cWIPSMalPktDctPolicyQuietTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSMalPktDctPolicyQuietTime.setStatus(_A)
_H3cWIPSStaticTrustOUIListCfgTable_Object=MibTable
h3cWIPSStaticTrustOUIListCfgTable=_H3cWIPSStaticTrustOUIListCfgTable_Object((1,3,6,1,4,1,2011,10,2,118,1,13))
if mibBuilder.loadTexts:h3cWIPSStaticTrustOUIListCfgTable.setStatus(_A)
_H3cWIPSStaticTrustOUIListCfgEntry_Object=MibTableRow
h3cWIPSStaticTrustOUIListCfgEntry=_H3cWIPSStaticTrustOUIListCfgEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,13,1))
h3cWIPSStaticTrustOUIListCfgEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:h3cWIPSStaticTrustOUIListCfgEntry.setStatus(_A)
class _H3cWIPSStaticTrustOUIListOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_H3cWIPSStaticTrustOUIListOUI_Type.__name__=_H
_H3cWIPSStaticTrustOUIListOUI_Object=MibTableColumn
h3cWIPSStaticTrustOUIListOUI=_H3cWIPSStaticTrustOUIListOUI_Object((1,3,6,1,4,1,2011,10,2,118,1,13,1,1),_H3cWIPSStaticTrustOUIListOUI_Type())
h3cWIPSStaticTrustOUIListOUI.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSStaticTrustOUIListOUI.setStatus(_A)
_H3cWIPSStaticTrustOUIListRowStatus_Type=RowStatus
_H3cWIPSStaticTrustOUIListRowStatus_Object=MibTableColumn
h3cWIPSStaticTrustOUIListRowStatus=_H3cWIPSStaticTrustOUIListRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,13,1,2),_H3cWIPSStaticTrustOUIListRowStatus_Type())
h3cWIPSStaticTrustOUIListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSStaticTrustOUIListRowStatus.setStatus(_A)
_H3cWIPSStaticTrustVendorListCfgTable_Object=MibTable
h3cWIPSStaticTrustVendorListCfgTable=_H3cWIPSStaticTrustVendorListCfgTable_Object((1,3,6,1,4,1,2011,10,2,118,1,14))
if mibBuilder.loadTexts:h3cWIPSStaticTrustVendorListCfgTable.setStatus(_A)
_H3cWIPSStaticTrustVendorListCfgEntry_Object=MibTableRow
h3cWIPSStaticTrustVendorListCfgEntry=_H3cWIPSStaticTrustVendorListCfgEntry_Object((1,3,6,1,4,1,2011,10,2,118,1,14,1))
h3cWIPSStaticTrustVendorListCfgEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:h3cWIPSStaticTrustVendorListCfgEntry.setStatus(_A)
class _H3cWIPSStaticTrustVendorListVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cWIPSStaticTrustVendorListVendor_Type.__name__=_H
_H3cWIPSStaticTrustVendorListVendor_Object=MibTableColumn
h3cWIPSStaticTrustVendorListVendor=_H3cWIPSStaticTrustVendorListVendor_Object((1,3,6,1,4,1,2011,10,2,118,1,14,1,1),_H3cWIPSStaticTrustVendorListVendor_Type())
h3cWIPSStaticTrustVendorListVendor.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSStaticTrustVendorListVendor.setStatus(_A)
_H3cWIPSStaticTrustVendorListRowStatus_Type=RowStatus
_H3cWIPSStaticTrustVendorListRowStatus_Object=MibTableColumn
h3cWIPSStaticTrustVendorListRowStatus=_H3cWIPSStaticTrustVendorListRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,1,14,1,2),_H3cWIPSStaticTrustVendorListRowStatus_Type())
h3cWIPSStaticTrustVendorListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cWIPSStaticTrustVendorListRowStatus.setStatus(_A)
_H3cWIPSDetectGroup_ObjectIdentity=ObjectIdentity
h3cWIPSDetectGroup=_H3cWIPSDetectGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,118,2))
_H3cWIPSDctAPTable_Object=MibTable
h3cWIPSDctAPTable=_H3cWIPSDctAPTable_Object((1,3,6,1,4,1,2011,10,2,118,2,1))
if mibBuilder.loadTexts:h3cWIPSDctAPTable.setStatus(_A)
_H3cWIPSDctAPEntry_Object=MibTableRow
h3cWIPSDctAPEntry=_H3cWIPSDctAPEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1))
h3cWIPSDctAPEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:h3cWIPSDctAPEntry.setStatus(_A)
class _H3cWIPSDctAPVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSDctAPVSD_Type.__name__=_H
_H3cWIPSDctAPVSD_Object=MibTableColumn
h3cWIPSDctAPVSD=_H3cWIPSDctAPVSD_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,1),_H3cWIPSDctAPVSD_Type())
h3cWIPSDctAPVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctAPVSD.setStatus(_A)
_H3cWIPSDctAPBSSID_Type=MacAddress
_H3cWIPSDctAPBSSID_Object=MibTableColumn
h3cWIPSDctAPBSSID=_H3cWIPSDctAPBSSID_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,2),_H3cWIPSDctAPBSSID_Type())
h3cWIPSDctAPBSSID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctAPBSSID.setStatus(_A)
_H3cWIPSDctAPRunningTime_Type=TimeTicks
_H3cWIPSDctAPRunningTime_Object=MibTableColumn
h3cWIPSDctAPRunningTime=_H3cWIPSDctAPRunningTime_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,3),_H3cWIPSDctAPRunningTime_Type())
h3cWIPSDctAPRunningTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPRunningTime.setStatus(_A)
_H3cWIPSDctAPRunTmLastUpdateTm_Type=TimeTicks
_H3cWIPSDctAPRunTmLastUpdateTm_Object=MibTableColumn
h3cWIPSDctAPRunTmLastUpdateTm=_H3cWIPSDctAPRunTmLastUpdateTm_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,4),_H3cWIPSDctAPRunTmLastUpdateTm_Type())
h3cWIPSDctAPRunTmLastUpdateTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPRunTmLastUpdateTm.setStatus(_A)
_H3cWIPSDctAPIsCountered_Type=TruthValue
_H3cWIPSDctAPIsCountered_Object=MibTableColumn
h3cWIPSDctAPIsCountered=_H3cWIPSDctAPIsCountered_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,5),_H3cWIPSDctAPIsCountered_Type())
h3cWIPSDctAPIsCountered.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPIsCountered.setStatus(_A)
_H3cWIPSDctAPWorkChannel_Type=H3cWIPSChannel
_H3cWIPSDctAPWorkChannel_Object=MibTableColumn
h3cWIPSDctAPWorkChannel=_H3cWIPSDctAPWorkChannel_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,6),_H3cWIPSDctAPWorkChannel_Type())
h3cWIPSDctAPWorkChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPWorkChannel.setStatus(_A)
_H3cWIPSDctAPRadioType_Type=H3cWIPSRadioType
_H3cWIPSDctAPRadioType_Object=MibTableColumn
h3cWIPSDctAPRadioType=_H3cWIPSDctAPRadioType_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,7),_H3cWIPSDctAPRadioType_Type())
h3cWIPSDctAPRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPRadioType.setStatus(_A)
_H3cWIPSDctAPAuthMethod_Type=H3cWIPSAuthMethod
_H3cWIPSDctAPAuthMethod_Object=MibTableColumn
h3cWIPSDctAPAuthMethod=_H3cWIPSDctAPAuthMethod_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,8),_H3cWIPSDctAPAuthMethod_Type())
h3cWIPSDctAPAuthMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPAuthMethod.setStatus(_A)
_H3cWIPSDctAPEncryptMethod_Type=H3cWIPSEncryptMethod
_H3cWIPSDctAPEncryptMethod_Object=MibTableColumn
h3cWIPSDctAPEncryptMethod=_H3cWIPSDctAPEncryptMethod_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,9),_H3cWIPSDctAPEncryptMethod_Type())
h3cWIPSDctAPEncryptMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPEncryptMethod.setStatus(_A)
_H3cWIPSDctAPSecurity_Type=H3cWIPSAPSecurityType
_H3cWIPSDctAPSecurity_Object=MibTableColumn
h3cWIPSDctAPSecurity=_H3cWIPSDctAPSecurity_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,10),_H3cWIPSDctAPSecurity_Type())
h3cWIPSDctAPSecurity.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPSecurity.setStatus(_A)
class _H3cWIPSDctAPSeverityLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cWIPSDctAPSeverityLevel_Type.__name__=_J
_H3cWIPSDctAPSeverityLevel_Object=MibTableColumn
h3cWIPSDctAPSeverityLevel=_H3cWIPSDctAPSeverityLevel_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,11),_H3cWIPSDctAPSeverityLevel_Type())
h3cWIPSDctAPSeverityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPSeverityLevel.setStatus(_A)
_H3cWIPSDctAPLastDctTm_Type=TimeTicks
_H3cWIPSDctAPLastDctTm_Object=MibTableColumn
h3cWIPSDctAPLastDctTm=_H3cWIPSDctAPLastDctTm_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,12),_H3cWIPSDctAPLastDctTm_Type())
h3cWIPSDctAPLastDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPLastDctTm.setStatus(_A)
_H3cWIPSDctAPFirstDctTm_Type=TimeTicks
_H3cWIPSDctAPFirstDctTm_Object=MibTableColumn
h3cWIPSDctAPFirstDctTm=_H3cWIPSDctAPFirstDctTm_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,13),_H3cWIPSDctAPFirstDctTm_Type())
h3cWIPSDctAPFirstDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPFirstDctTm.setStatus(_A)
class _H3cWIPSDctAPAdd2BlackList_Type(TruthValue):defaultValue=2
_H3cWIPSDctAPAdd2BlackList_Type.__name__=_K
_H3cWIPSDctAPAdd2BlackList_Object=MibTableColumn
h3cWIPSDctAPAdd2BlackList=_H3cWIPSDctAPAdd2BlackList_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,14),_H3cWIPSDctAPAdd2BlackList_Type())
h3cWIPSDctAPAdd2BlackList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctAPAdd2BlackList.setStatus(_A)
class _H3cWIPSDctAPAdd2WhiteList_Type(TruthValue):defaultValue=2
_H3cWIPSDctAPAdd2WhiteList_Type.__name__=_K
_H3cWIPSDctAPAdd2WhiteList_Object=MibTableColumn
h3cWIPSDctAPAdd2WhiteList=_H3cWIPSDctAPAdd2WhiteList_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,15),_H3cWIPSDctAPAdd2WhiteList_Type())
h3cWIPSDctAPAdd2WhiteList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctAPAdd2WhiteList.setStatus(_A)
class _H3cWIPSDctAPAdd2IgnoreList_Type(TruthValue):defaultValue=2
_H3cWIPSDctAPAdd2IgnoreList_Type.__name__=_K
_H3cWIPSDctAPAdd2IgnoreList_Object=MibTableColumn
h3cWIPSDctAPAdd2IgnoreList=_H3cWIPSDctAPAdd2IgnoreList_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,16),_H3cWIPSDctAPAdd2IgnoreList_Type())
h3cWIPSDctAPAdd2IgnoreList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctAPAdd2IgnoreList.setStatus(_A)
class _H3cWIPSDctAPAdd2CtmList_Type(TruthValue):defaultValue=2
_H3cWIPSDctAPAdd2CtmList_Type.__name__=_K
_H3cWIPSDctAPAdd2CtmList_Object=MibTableColumn
h3cWIPSDctAPAdd2CtmList=_H3cWIPSDctAPAdd2CtmList_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,17),_H3cWIPSDctAPAdd2CtmList_Type())
h3cWIPSDctAPAdd2CtmList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctAPAdd2CtmList.setStatus(_A)
_H3cWIPSDctAPCategory_Type=H3cWIPSAPCategoryType
_H3cWIPSDctAPCategory_Object=MibTableColumn
h3cWIPSDctAPCategory=_H3cWIPSDctAPCategory_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,18),_H3cWIPSDctAPCategory_Type())
h3cWIPSDctAPCategory.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctAPCategory.setStatus(_A)
class _H3cWIPSDctAPCategoryWay_Type(H3cWIPSDevCategoryWay):defaultValue=3
_H3cWIPSDctAPCategoryWay_Type.__name__=_AC
_H3cWIPSDctAPCategoryWay_Object=MibTableColumn
h3cWIPSDctAPCategoryWay=_H3cWIPSDctAPCategoryWay_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,19),_H3cWIPSDctAPCategoryWay_Type())
h3cWIPSDctAPCategoryWay.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctAPCategoryWay.setStatus(_A)
_H3cWIPSDctAPStatus_Type=H3cWIPSDevStatus
_H3cWIPSDctAPStatus_Object=MibTableColumn
h3cWIPSDctAPStatus=_H3cWIPSDctAPStatus_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,20),_H3cWIPSDctAPStatus_Type())
h3cWIPSDctAPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPStatus.setStatus(_A)
class _H3cWIPSDctAPSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cWIPSDctAPSSID_Type.__name__=_H
_H3cWIPSDctAPSSID_Object=MibTableColumn
h3cWIPSDctAPSSID=_H3cWIPSDctAPSSID_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,21),_H3cWIPSDctAPSSID_Type())
h3cWIPSDctAPSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPSSID.setStatus(_A)
_H3cWIPSDctAPAttachStaNum_Type=Integer32
_H3cWIPSDctAPAttachStaNum_Object=MibTableColumn
h3cWIPSDctAPAttachStaNum=_H3cWIPSDctAPAttachStaNum_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,22),_H3cWIPSDctAPAttachStaNum_Type())
h3cWIPSDctAPAttachStaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPAttachStaNum.setStatus(_A)
_H3cWIPSDctAPRptSensorNum_Type=Integer32
_H3cWIPSDctAPRptSensorNum_Object=MibTableColumn
h3cWIPSDctAPRptSensorNum=_H3cWIPSDctAPRptSensorNum_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,23),_H3cWIPSDctAPRptSensorNum_Type())
h3cWIPSDctAPRptSensorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPRptSensorNum.setStatus(_A)
class _H3cWIPSDctAPVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cWIPSDctAPVendor_Type.__name__=_H
_H3cWIPSDctAPVendor_Object=MibTableColumn
h3cWIPSDctAPVendor=_H3cWIPSDctAPVendor_Object((1,3,6,1,4,1,2011,10,2,118,2,1,1,24),_H3cWIPSDctAPVendor_Type())
h3cWIPSDctAPVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPVendor.setStatus(_A)
_H3cWIPSDctAPAttachStaTable_Object=MibTable
h3cWIPSDctAPAttachStaTable=_H3cWIPSDctAPAttachStaTable_Object((1,3,6,1,4,1,2011,10,2,118,2,2))
if mibBuilder.loadTexts:h3cWIPSDctAPAttachStaTable.setStatus(_A)
_H3cWIPSDctAPAttachStaEntry_Object=MibTableRow
h3cWIPSDctAPAttachStaEntry=_H3cWIPSDctAPAttachStaEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,2,1))
h3cWIPSDctAPAttachStaEntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_AD))
if mibBuilder.loadTexts:h3cWIPSDctAPAttachStaEntry.setStatus(_A)
_H3cWIPSDctAPAttachStaMac_Type=MacAddress
_H3cWIPSDctAPAttachStaMac_Object=MibTableColumn
h3cWIPSDctAPAttachStaMac=_H3cWIPSDctAPAttachStaMac_Object((1,3,6,1,4,1,2011,10,2,118,2,2,1,1),_H3cWIPSDctAPAttachStaMac_Type())
h3cWIPSDctAPAttachStaMac.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctAPAttachStaMac.setStatus(_A)
_H3cWIPSDctAPAttachStaRowStatus_Type=RowStatus
_H3cWIPSDctAPAttachStaRowStatus_Object=MibTableColumn
h3cWIPSDctAPAttachStaRowStatus=_H3cWIPSDctAPAttachStaRowStatus_Object((1,3,6,1,4,1,2011,10,2,118,2,2,1,2),_H3cWIPSDctAPAttachStaRowStatus_Type())
h3cWIPSDctAPAttachStaRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPAttachStaRowStatus.setStatus(_A)
_H3cWIPSDctAPRptSensorTable_Object=MibTable
h3cWIPSDctAPRptSensorTable=_H3cWIPSDctAPRptSensorTable_Object((1,3,6,1,4,1,2011,10,2,118,2,3))
if mibBuilder.loadTexts:h3cWIPSDctAPRptSensorTable.setStatus(_A)
_H3cWIPSDctAPRptSensorEntry_Object=MibTableRow
h3cWIPSDctAPRptSensorEntry=_H3cWIPSDctAPRptSensorEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,3,1))
h3cWIPSDctAPRptSensorEntry.setIndexNames((0,_E,_Q),(0,_E,_R),(0,_E,_AE))
if mibBuilder.loadTexts:h3cWIPSDctAPRptSensorEntry.setStatus(_A)
class _H3cWIPSDctAPRptSensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cWIPSDctAPRptSensorName_Type.__name__=_H
_H3cWIPSDctAPRptSensorName_Object=MibTableColumn
h3cWIPSDctAPRptSensorName=_H3cWIPSDctAPRptSensorName_Object((1,3,6,1,4,1,2011,10,2,118,2,3,1,1),_H3cWIPSDctAPRptSensorName_Type())
h3cWIPSDctAPRptSensorName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctAPRptSensorName.setStatus(_A)
class _H3cWIPSDctAPRptSensorRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_H3cWIPSDctAPRptSensorRadioId_Type.__name__=_F
_H3cWIPSDctAPRptSensorRadioId_Object=MibTableColumn
h3cWIPSDctAPRptSensorRadioId=_H3cWIPSDctAPRptSensorRadioId_Object((1,3,6,1,4,1,2011,10,2,118,2,3,1,2),_H3cWIPSDctAPRptSensorRadioId_Type())
h3cWIPSDctAPRptSensorRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPRptSensorRadioId.setStatus(_A)
class _H3cWIPSDctAPRptRSSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90))
_H3cWIPSDctAPRptRSSI_Type.__name__=_F
_H3cWIPSDctAPRptRSSI_Object=MibTableColumn
h3cWIPSDctAPRptRSSI=_H3cWIPSDctAPRptRSSI_Object((1,3,6,1,4,1,2011,10,2,118,2,3,1,3),_H3cWIPSDctAPRptRSSI_Type())
h3cWIPSDctAPRptRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPRptRSSI.setStatus(_A)
_H3cWIPSDctAPLastRptTm_Type=TimeTicks
_H3cWIPSDctAPLastRptTm_Object=MibTableColumn
h3cWIPSDctAPLastRptTm=_H3cWIPSDctAPLastRptTm_Object((1,3,6,1,4,1,2011,10,2,118,2,3,1,4),_H3cWIPSDctAPLastRptTm_Type())
h3cWIPSDctAPLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctAPLastRptTm.setStatus(_A)
_H3cWIPSDctStaTable_Object=MibTable
h3cWIPSDctStaTable=_H3cWIPSDctStaTable_Object((1,3,6,1,4,1,2011,10,2,118,2,4))
if mibBuilder.loadTexts:h3cWIPSDctStaTable.setStatus(_A)
_H3cWIPSDctStaEntry_Object=MibTableRow
h3cWIPSDctStaEntry=_H3cWIPSDctStaEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1))
h3cWIPSDctStaEntry.setIndexNames((0,_E,_Z),(0,_E,_a))
if mibBuilder.loadTexts:h3cWIPSDctStaEntry.setStatus(_A)
class _H3cWIPSDctStaVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSDctStaVSD_Type.__name__=_H
_H3cWIPSDctStaVSD_Object=MibTableColumn
h3cWIPSDctStaVSD=_H3cWIPSDctStaVSD_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,1),_H3cWIPSDctStaVSD_Type())
h3cWIPSDctStaVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctStaVSD.setStatus(_A)
_H3cWIPSDctStaMac_Type=MacAddress
_H3cWIPSDctStaMac_Object=MibTableColumn
h3cWIPSDctStaMac=_H3cWIPSDctStaMac_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,2),_H3cWIPSDctStaMac_Type())
h3cWIPSDctStaMac.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctStaMac.setStatus(_A)
_H3cWIPSDctStaAssocBSSID_Type=MacAddress
_H3cWIPSDctStaAssocBSSID_Object=MibTableColumn
h3cWIPSDctStaAssocBSSID=_H3cWIPSDctStaAssocBSSID_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,3),_H3cWIPSDctStaAssocBSSID_Type())
h3cWIPSDctStaAssocBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaAssocBSSID.setStatus(_A)
_H3cWIPSDctStaStatus_Type=H3cWIPSDevStatus
_H3cWIPSDctStaStatus_Object=MibTableColumn
h3cWIPSDctStaStatus=_H3cWIPSDctStaStatus_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,4),_H3cWIPSDctStaStatus_Type())
h3cWIPSDctStaStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaStatus.setStatus(_A)
_H3cWIPSDctStaCategory_Type=H3cWIPSClientCategoryType
_H3cWIPSDctStaCategory_Object=MibTableColumn
h3cWIPSDctStaCategory=_H3cWIPSDctStaCategory_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,5),_H3cWIPSDctStaCategory_Type())
h3cWIPSDctStaCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaCategory.setStatus(_A)
_H3cWIPSDctStaRadioType_Type=H3cWIPSRadioType
_H3cWIPSDctStaRadioType_Object=MibTableColumn
h3cWIPSDctStaRadioType=_H3cWIPSDctStaRadioType_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,6),_H3cWIPSDctStaRadioType_Type())
h3cWIPSDctStaRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaRadioType.setStatus(_A)
_H3cWIPSDctStaWorkChannel_Type=H3cWIPSChannel
_H3cWIPSDctStaWorkChannel_Object=MibTableColumn
h3cWIPSDctStaWorkChannel=_H3cWIPSDctStaWorkChannel_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,7),_H3cWIPSDctStaWorkChannel_Type())
h3cWIPSDctStaWorkChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaWorkChannel.setStatus(_A)
_H3cWIPSDctStaIsCountered_Type=TruthValue
_H3cWIPSDctStaIsCountered_Object=MibTableColumn
h3cWIPSDctStaIsCountered=_H3cWIPSDctStaIsCountered_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,8),_H3cWIPSDctStaIsCountered_Type())
h3cWIPSDctStaIsCountered.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaIsCountered.setStatus(_A)
class _H3cWIPSDctStaAdd2BlackList_Type(TruthValue):defaultValue=2
_H3cWIPSDctStaAdd2BlackList_Type.__name__=_K
_H3cWIPSDctStaAdd2BlackList_Object=MibTableColumn
h3cWIPSDctStaAdd2BlackList=_H3cWIPSDctStaAdd2BlackList_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,9),_H3cWIPSDctStaAdd2BlackList_Type())
h3cWIPSDctStaAdd2BlackList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctStaAdd2BlackList.setStatus(_A)
class _H3cWIPSDctStaAdd2WhiteList_Type(TruthValue):defaultValue=2
_H3cWIPSDctStaAdd2WhiteList_Type.__name__=_K
_H3cWIPSDctStaAdd2WhiteList_Object=MibTableColumn
h3cWIPSDctStaAdd2WhiteList=_H3cWIPSDctStaAdd2WhiteList_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,10),_H3cWIPSDctStaAdd2WhiteList_Type())
h3cWIPSDctStaAdd2WhiteList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctStaAdd2WhiteList.setStatus(_A)
class _H3cWIPSDctStaAdd2IgnoreList_Type(TruthValue):defaultValue=2
_H3cWIPSDctStaAdd2IgnoreList_Type.__name__=_K
_H3cWIPSDctStaAdd2IgnoreList_Object=MibTableColumn
h3cWIPSDctStaAdd2IgnoreList=_H3cWIPSDctStaAdd2IgnoreList_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,11),_H3cWIPSDctStaAdd2IgnoreList_Type())
h3cWIPSDctStaAdd2IgnoreList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctStaAdd2IgnoreList.setStatus(_A)
class _H3cWIPSDctStaAdd2CtmList_Type(TruthValue):defaultValue=2
_H3cWIPSDctStaAdd2CtmList_Type.__name__=_K
_H3cWIPSDctStaAdd2CtmList_Object=MibTableColumn
h3cWIPSDctStaAdd2CtmList=_H3cWIPSDctStaAdd2CtmList_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,12),_H3cWIPSDctStaAdd2CtmList_Type())
h3cWIPSDctStaAdd2CtmList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctStaAdd2CtmList.setStatus(_A)
_H3cWIPSDctStaFirstDctTm_Type=TimeTicks
_H3cWIPSDctStaFirstDctTm_Object=MibTableColumn
h3cWIPSDctStaFirstDctTm=_H3cWIPSDctStaFirstDctTm_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,13),_H3cWIPSDctStaFirstDctTm_Type())
h3cWIPSDctStaFirstDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaFirstDctTm.setStatus(_A)
_H3cWIPSDctStaLastDctTm_Type=TimeTicks
_H3cWIPSDctStaLastDctTm_Object=MibTableColumn
h3cWIPSDctStaLastDctTm=_H3cWIPSDctStaLastDctTm_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,14),_H3cWIPSDctStaLastDctTm_Type())
h3cWIPSDctStaLastDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaLastDctTm.setStatus(_A)
_H3cWIPSDctStaRptSensorNum_Type=Integer32
_H3cWIPSDctStaRptSensorNum_Object=MibTableColumn
h3cWIPSDctStaRptSensorNum=_H3cWIPSDctStaRptSensorNum_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,15),_H3cWIPSDctStaRptSensorNum_Type())
h3cWIPSDctStaRptSensorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaRptSensorNum.setStatus(_A)
class _H3cWIPSDctStaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_AF,1),(_AG,2),(_AH,3),(_AI,4),(_AJ,5),(_AK,6),(_AL,7)))
_H3cWIPSDctStaState_Type.__name__=_F
_H3cWIPSDctStaState_Object=MibTableColumn
h3cWIPSDctStaState=_H3cWIPSDctStaState_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,16),_H3cWIPSDctStaState_Type())
h3cWIPSDctStaState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaState.setStatus(_A)
class _H3cWIPSDctStaVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cWIPSDctStaVendor_Type.__name__=_H
_H3cWIPSDctStaVendor_Object=MibTableColumn
h3cWIPSDctStaVendor=_H3cWIPSDctStaVendor_Object((1,3,6,1,4,1,2011,10,2,118,2,4,1,17),_H3cWIPSDctStaVendor_Type())
h3cWIPSDctStaVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaVendor.setStatus(_A)
_H3cWIPSDctStaRptSensorTable_Object=MibTable
h3cWIPSDctStaRptSensorTable=_H3cWIPSDctStaRptSensorTable_Object((1,3,6,1,4,1,2011,10,2,118,2,5))
if mibBuilder.loadTexts:h3cWIPSDctStaRptSensorTable.setStatus(_A)
_H3cWIPSDctStaRptSensorEntry_Object=MibTableRow
h3cWIPSDctStaRptSensorEntry=_H3cWIPSDctStaRptSensorEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,5,1))
h3cWIPSDctStaRptSensorEntry.setIndexNames((0,_E,_Z),(0,_E,_a),(0,_E,_AM))
if mibBuilder.loadTexts:h3cWIPSDctStaRptSensorEntry.setStatus(_A)
class _H3cWIPSDctStaRtpSensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cWIPSDctStaRtpSensorName_Type.__name__=_H
_H3cWIPSDctStaRtpSensorName_Object=MibTableColumn
h3cWIPSDctStaRtpSensorName=_H3cWIPSDctStaRtpSensorName_Object((1,3,6,1,4,1,2011,10,2,118,2,5,1,1),_H3cWIPSDctStaRtpSensorName_Type())
h3cWIPSDctStaRtpSensorName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctStaRtpSensorName.setStatus(_A)
class _H3cWIPSDctStaRptSensorRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_H3cWIPSDctStaRptSensorRadioId_Type.__name__=_F
_H3cWIPSDctStaRptSensorRadioId_Object=MibTableColumn
h3cWIPSDctStaRptSensorRadioId=_H3cWIPSDctStaRptSensorRadioId_Object((1,3,6,1,4,1,2011,10,2,118,2,5,1,2),_H3cWIPSDctStaRptSensorRadioId_Type())
h3cWIPSDctStaRptSensorRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaRptSensorRadioId.setStatus(_A)
_H3cWIPSDctStaRptRSSI_Type=Integer32
_H3cWIPSDctStaRptRSSI_Object=MibTableColumn
h3cWIPSDctStaRptRSSI=_H3cWIPSDctStaRptRSSI_Object((1,3,6,1,4,1,2011,10,2,118,2,5,1,3),_H3cWIPSDctStaRptRSSI_Type())
h3cWIPSDctStaRptRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaRptRSSI.setStatus(_A)
_H3cWIPSDctStaLastRptTm_Type=TimeTicks
_H3cWIPSDctStaLastRptTm_Object=MibTableColumn
h3cWIPSDctStaLastRptTm=_H3cWIPSDctStaLastRptTm_Object((1,3,6,1,4,1,2011,10,2,118,2,5,1,4),_H3cWIPSDctStaLastRptTm_Type())
h3cWIPSDctStaLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctStaLastRptTm.setStatus(_A)
_H3cWIPSDctSSIDTable_Object=MibTable
h3cWIPSDctSSIDTable=_H3cWIPSDctSSIDTable_Object((1,3,6,1,4,1,2011,10,2,118,2,6))
if mibBuilder.loadTexts:h3cWIPSDctSSIDTable.setStatus(_A)
_H3cWIPSDctSSIDEntry_Object=MibTableRow
h3cWIPSDctSSIDEntry=_H3cWIPSDctSSIDEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,6,1))
h3cWIPSDctSSIDEntry.setIndexNames((0,_E,_b),(0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:h3cWIPSDctSSIDEntry.setStatus(_A)
class _H3cWIPSDctNetworkVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSDctNetworkVSD_Type.__name__=_H
_H3cWIPSDctNetworkVSD_Object=MibTableColumn
h3cWIPSDctNetworkVSD=_H3cWIPSDctNetworkVSD_Object((1,3,6,1,4,1,2011,10,2,118,2,6,1,1),_H3cWIPSDctNetworkVSD_Type())
h3cWIPSDctNetworkVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctNetworkVSD.setStatus(_A)
class _H3cWIPSDctNetworkSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSDctNetworkSSID_Type.__name__=_H
_H3cWIPSDctNetworkSSID_Object=MibTableColumn
h3cWIPSDctNetworkSSID=_H3cWIPSDctNetworkSSID_Object((1,3,6,1,4,1,2011,10,2,118,2,6,1,2),_H3cWIPSDctNetworkSSID_Type())
h3cWIPSDctNetworkSSID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctNetworkSSID.setStatus(_A)
_H3cWIPSDctNetworkCfg_Type=Unsigned32
_H3cWIPSDctNetworkCfg_Object=MibTableColumn
h3cWIPSDctNetworkCfg=_H3cWIPSDctNetworkCfg_Object((1,3,6,1,4,1,2011,10,2,118,2,6,1,3),_H3cWIPSDctNetworkCfg_Type())
h3cWIPSDctNetworkCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctNetworkCfg.setStatus(_A)
_H3cWIPSDctNetworkFirstRptTm_Type=TimeTicks
_H3cWIPSDctNetworkFirstRptTm_Object=MibTableColumn
h3cWIPSDctNetworkFirstRptTm=_H3cWIPSDctNetworkFirstRptTm_Object((1,3,6,1,4,1,2011,10,2,118,2,6,1,4),_H3cWIPSDctNetworkFirstRptTm_Type())
h3cWIPSDctNetworkFirstRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctNetworkFirstRptTm.setStatus(_A)
_H3cWIPSDctNetworkLastRptTm_Type=TimeTicks
_H3cWIPSDctNetworkLastRptTm_Object=MibTableColumn
h3cWIPSDctNetworkLastRptTm=_H3cWIPSDctNetworkLastRptTm_Object((1,3,6,1,4,1,2011,10,2,118,2,6,1,5),_H3cWIPSDctNetworkLastRptTm_Type())
h3cWIPSDctNetworkLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctNetworkLastRptTm.setStatus(_A)
_H3cWIPSDctNetworkStatus_Type=H3cWIPSDevStatus
_H3cWIPSDctNetworkStatus_Object=MibTableColumn
h3cWIPSDctNetworkStatus=_H3cWIPSDctNetworkStatus_Object((1,3,6,1,4,1,2011,10,2,118,2,6,1,6),_H3cWIPSDctNetworkStatus_Type())
h3cWIPSDctNetworkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctNetworkStatus.setStatus(_A)
class _H3cWIPSDctNetworkSSIDHide_Type(TruthValue):defaultValue=2
_H3cWIPSDctNetworkSSIDHide_Type.__name__=_K
_H3cWIPSDctNetworkSSIDHide_Object=MibTableColumn
h3cWIPSDctNetworkSSIDHide=_H3cWIPSDctNetworkSSIDHide_Object((1,3,6,1,4,1,2011,10,2,118,2,6,1,7),_H3cWIPSDctNetworkSSIDHide_Type())
h3cWIPSDctNetworkSSIDHide.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctNetworkSSIDHide.setStatus(_A)
_H3cWIPSDctNetworkBSSNum_Type=Integer32
_H3cWIPSDctNetworkBSSNum_Object=MibTableColumn
h3cWIPSDctNetworkBSSNum=_H3cWIPSDctNetworkBSSNum_Object((1,3,6,1,4,1,2011,10,2,118,2,6,1,8),_H3cWIPSDctNetworkBSSNum_Type())
h3cWIPSDctNetworkBSSNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctNetworkBSSNum.setStatus(_A)
_H3cWIPSDctSSIDBSSTable_Object=MibTable
h3cWIPSDctSSIDBSSTable=_H3cWIPSDctSSIDBSSTable_Object((1,3,6,1,4,1,2011,10,2,118,2,7))
if mibBuilder.loadTexts:h3cWIPSDctSSIDBSSTable.setStatus(_A)
_H3cWIPSDctSSIDBSSEntry_Object=MibTableRow
h3cWIPSDctSSIDBSSEntry=_H3cWIPSDctSSIDBSSEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,7,1))
h3cWIPSDctSSIDBSSEntry.setIndexNames((0,_E,_b),(0,_E,_c),(0,_E,_d),(0,_E,_AN))
if mibBuilder.loadTexts:h3cWIPSDctSSIDBSSEntry.setStatus(_A)
_H3cWIPSDctNetworkBSSID_Type=MacAddress
_H3cWIPSDctNetworkBSSID_Object=MibTableColumn
h3cWIPSDctNetworkBSSID=_H3cWIPSDctNetworkBSSID_Object((1,3,6,1,4,1,2011,10,2,118,2,7,1,1),_H3cWIPSDctNetworkBSSID_Type())
h3cWIPSDctNetworkBSSID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctNetworkBSSID.setStatus(_A)
_H3cWIPSDctNetworkBSSWorkChl_Type=H3cWIPSChannel
_H3cWIPSDctNetworkBSSWorkChl_Object=MibTableColumn
h3cWIPSDctNetworkBSSWorkChl=_H3cWIPSDctNetworkBSSWorkChl_Object((1,3,6,1,4,1,2011,10,2,118,2,7,1,2),_H3cWIPSDctNetworkBSSWorkChl_Type())
h3cWIPSDctNetworkBSSWorkChl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctNetworkBSSWorkChl.setStatus(_A)
_H3cWIPSDctNetworkBSSStaNum_Type=Integer32
_H3cWIPSDctNetworkBSSStaNum_Object=MibTableColumn
h3cWIPSDctNetworkBSSStaNum=_H3cWIPSDctNetworkBSSStaNum_Object((1,3,6,1,4,1,2011,10,2,118,2,7,1,3),_H3cWIPSDctNetworkBSSStaNum_Type())
h3cWIPSDctNetworkBSSStaNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctNetworkBSSStaNum.setStatus(_A)
_H3cWIPSBlockListTable_Object=MibTable
h3cWIPSBlockListTable=_H3cWIPSBlockListTable_Object((1,3,6,1,4,1,2011,10,2,118,2,8))
if mibBuilder.loadTexts:h3cWIPSBlockListTable.setStatus(_A)
_H3cWIPSBlockListEntry_Object=MibTableRow
h3cWIPSBlockListEntry=_H3cWIPSBlockListEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,8,1))
h3cWIPSBlockListEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:h3cWIPSBlockListEntry.setStatus(_A)
_H3cWIPSBlockListMacAddress_Type=MacAddress
_H3cWIPSBlockListMacAddress_Object=MibTableColumn
h3cWIPSBlockListMacAddress=_H3cWIPSBlockListMacAddress_Object((1,3,6,1,4,1,2011,10,2,118,2,8,1,1),_H3cWIPSBlockListMacAddress_Type())
h3cWIPSBlockListMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSBlockListMacAddress.setStatus(_A)
class _H3cWIPSBlockListStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_AP,3)))
_H3cWIPSBlockListStatus_Type.__name__=_F
_H3cWIPSBlockListStatus_Object=MibTableColumn
h3cWIPSBlockListStatus=_H3cWIPSBlockListStatus_Object((1,3,6,1,4,1,2011,10,2,118,2,8,1,2),_H3cWIPSBlockListStatus_Type())
h3cWIPSBlockListStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSBlockListStatus.setStatus(_A)
_H3cWIPSChannelTable_Object=MibTable
h3cWIPSChannelTable=_H3cWIPSChannelTable_Object((1,3,6,1,4,1,2011,10,2,118,2,9))
if mibBuilder.loadTexts:h3cWIPSChannelTable.setStatus(_A)
_H3cWIPSChannelEntry_Object=MibTableRow
h3cWIPSChannelEntry=_H3cWIPSChannelEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,9,1))
h3cWIPSChannelEntry.setIndexNames((0,_E,_AQ))
if mibBuilder.loadTexts:h3cWIPSChannelEntry.setStatus(_A)
_H3cWIPSChannelNum_Type=H3cWIPSChannel
_H3cWIPSChannelNum_Object=MibTableColumn
h3cWIPSChannelNum=_H3cWIPSChannelNum_Object((1,3,6,1,4,1,2011,10,2,118,2,9,1,1),_H3cWIPSChannelNum_Type())
h3cWIPSChannelNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSChannelNum.setStatus(_A)
_H3cWIPSChannelRadioType_Type=H3cWIPSRadioType
_H3cWIPSChannelRadioType_Object=MibTableColumn
h3cWIPSChannelRadioType=_H3cWIPSChannelRadioType_Object((1,3,6,1,4,1,2011,10,2,118,2,9,1,2),_H3cWIPSChannelRadioType_Type())
h3cWIPSChannelRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChannelRadioType.setStatus(_A)
_H3cWIPSChannelIsPermitted_Type=TruthValue
_H3cWIPSChannelIsPermitted_Object=MibTableColumn
h3cWIPSChannelIsPermitted=_H3cWIPSChannelIsPermitted_Object((1,3,6,1,4,1,2011,10,2,118,2,9,1,3),_H3cWIPSChannelIsPermitted_Type())
h3cWIPSChannelIsPermitted.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChannelIsPermitted.setStatus(_A)
_H3cWIPSChannelLastRptTm_Type=TimeTicks
_H3cWIPSChannelLastRptTm_Object=MibTableColumn
h3cWIPSChannelLastRptTm=_H3cWIPSChannelLastRptTm_Object((1,3,6,1,4,1,2011,10,2,118,2,9,1,4),_H3cWIPSChannelLastRptTm_Type())
h3cWIPSChannelLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChannelLastRptTm.setStatus(_A)
_H3cWIPSCountermeasureListTable_Object=MibTable
h3cWIPSCountermeasureListTable=_H3cWIPSCountermeasureListTable_Object((1,3,6,1,4,1,2011,10,2,118,2,10))
if mibBuilder.loadTexts:h3cWIPSCountermeasureListTable.setStatus(_A)
_H3cWIPSCountermeasureListEntry_Object=MibTableRow
h3cWIPSCountermeasureListEntry=_H3cWIPSCountermeasureListEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,10,1))
h3cWIPSCountermeasureListEntry.setIndexNames((0,_E,_AR))
if mibBuilder.loadTexts:h3cWIPSCountermeasureListEntry.setStatus(_A)
_H3cWIPSCtmListMacAddress_Type=MacAddress
_H3cWIPSCtmListMacAddress_Object=MibTableColumn
h3cWIPSCtmListMacAddress=_H3cWIPSCtmListMacAddress_Object((1,3,6,1,4,1,2011,10,2,118,2,10,1,1),_H3cWIPSCtmListMacAddress_Type())
h3cWIPSCtmListMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSCtmListMacAddress.setStatus(_A)
_H3cWIPSCtmListLastestWorkChl_Type=H3cWIPSChannel
_H3cWIPSCtmListLastestWorkChl_Object=MibTableColumn
h3cWIPSCtmListLastestWorkChl=_H3cWIPSCtmListLastestWorkChl_Object((1,3,6,1,4,1,2011,10,2,118,2,10,1,2),_H3cWIPSCtmListLastestWorkChl_Type())
h3cWIPSCtmListLastestWorkChl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmListLastestWorkChl.setStatus(_A)
_H3cWIPSCtmListFirstTm_Type=TimeTicks
_H3cWIPSCtmListFirstTm_Object=MibTableColumn
h3cWIPSCtmListFirstTm=_H3cWIPSCtmListFirstTm_Object((1,3,6,1,4,1,2011,10,2,118,2,10,1,3),_H3cWIPSCtmListFirstTm_Type())
h3cWIPSCtmListFirstTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmListFirstTm.setStatus(_A)
_H3cWIPSCtmListLastTm_Type=TimeTicks
_H3cWIPSCtmListLastTm_Object=MibTableColumn
h3cWIPSCtmListLastTm=_H3cWIPSCtmListLastTm_Object((1,3,6,1,4,1,2011,10,2,118,2,10,1,4),_H3cWIPSCtmListLastTm_Type())
h3cWIPSCtmListLastTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmListLastTm.setStatus(_A)
_H3cWIPSCtmListQurCnt_Type=Integer32
_H3cWIPSCtmListQurCnt_Object=MibTableColumn
h3cWIPSCtmListQurCnt=_H3cWIPSCtmListQurCnt_Object((1,3,6,1,4,1,2011,10,2,118,2,10,1,5),_H3cWIPSCtmListQurCnt_Type())
h3cWIPSCtmListQurCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmListQurCnt.setStatus(_A)
_H3cWIPSCtmListSensorNum_Type=Integer32
_H3cWIPSCtmListSensorNum_Object=MibTableColumn
h3cWIPSCtmListSensorNum=_H3cWIPSCtmListSensorNum_Object((1,3,6,1,4,1,2011,10,2,118,2,10,1,6),_H3cWIPSCtmListSensorNum_Type())
h3cWIPSCtmListSensorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmListSensorNum.setStatus(_A)
_H3cWIPSIgnoreListTable_Object=MibTable
h3cWIPSIgnoreListTable=_H3cWIPSIgnoreListTable_Object((1,3,6,1,4,1,2011,10,2,118,2,11))
if mibBuilder.loadTexts:h3cWIPSIgnoreListTable.setStatus(_A)
_H3cWIPSIgnoreListEntry_Object=MibTableRow
h3cWIPSIgnoreListEntry=_H3cWIPSIgnoreListEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,11,1))
h3cWIPSIgnoreListEntry.setIndexNames((0,_E,_AS))
if mibBuilder.loadTexts:h3cWIPSIgnoreListEntry.setStatus(_A)
_H3cWIPSIgnoreListMacAddress_Type=MacAddress
_H3cWIPSIgnoreListMacAddress_Object=MibTableColumn
h3cWIPSIgnoreListMacAddress=_H3cWIPSIgnoreListMacAddress_Object((1,3,6,1,4,1,2011,10,2,118,2,11,1,1),_H3cWIPSIgnoreListMacAddress_Type())
h3cWIPSIgnoreListMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSIgnoreListMacAddress.setStatus(_A)
_H3cWIPSIgnoreListFirstIgnoreTm_Type=TimeTicks
_H3cWIPSIgnoreListFirstIgnoreTm_Object=MibTableColumn
h3cWIPSIgnoreListFirstIgnoreTm=_H3cWIPSIgnoreListFirstIgnoreTm_Object((1,3,6,1,4,1,2011,10,2,118,2,11,1,2),_H3cWIPSIgnoreListFirstIgnoreTm_Type())
h3cWIPSIgnoreListFirstIgnoreTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSIgnoreListFirstIgnoreTm.setStatus(_A)
_H3cWIPSIgnoreListLastIgnoreTm_Type=TimeTicks
_H3cWIPSIgnoreListLastIgnoreTm_Object=MibTableColumn
h3cWIPSIgnoreListLastIgnoreTm=_H3cWIPSIgnoreListLastIgnoreTm_Object((1,3,6,1,4,1,2011,10,2,118,2,11,1,3),_H3cWIPSIgnoreListLastIgnoreTm_Type())
h3cWIPSIgnoreListLastIgnoreTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSIgnoreListLastIgnoreTm.setStatus(_A)
_H3cWIPSIgnoreListIgnoreCnt_Type=Integer32
_H3cWIPSIgnoreListIgnoreCnt_Object=MibTableColumn
h3cWIPSIgnoreListIgnoreCnt=_H3cWIPSIgnoreListIgnoreCnt_Object((1,3,6,1,4,1,2011,10,2,118,2,11,1,4),_H3cWIPSIgnoreListIgnoreCnt_Type())
h3cWIPSIgnoreListIgnoreCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSIgnoreListIgnoreCnt.setStatus(_A)
_H3cWIPSTrustListTable_Object=MibTable
h3cWIPSTrustListTable=_H3cWIPSTrustListTable_Object((1,3,6,1,4,1,2011,10,2,118,2,12))
if mibBuilder.loadTexts:h3cWIPSTrustListTable.setStatus(_A)
_H3cWIPSTrustListEntry_Object=MibTableRow
h3cWIPSTrustListEntry=_H3cWIPSTrustListEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,12,1))
h3cWIPSTrustListEntry.setIndexNames((0,_E,_AT))
if mibBuilder.loadTexts:h3cWIPSTrustListEntry.setStatus(_A)
_H3cWIPSTrustListMacAddress_Type=MacAddress
_H3cWIPSTrustListMacAddress_Object=MibTableColumn
h3cWIPSTrustListMacAddress=_H3cWIPSTrustListMacAddress_Object((1,3,6,1,4,1,2011,10,2,118,2,12,1,1),_H3cWIPSTrustListMacAddress_Type())
h3cWIPSTrustListMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSTrustListMacAddress.setStatus(_A)
class _H3cWIPSTrustListStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),(_AP,3)))
_H3cWIPSTrustListStatus_Type.__name__=_F
_H3cWIPSTrustListStatus_Object=MibTableColumn
h3cWIPSTrustListStatus=_H3cWIPSTrustListStatus_Object((1,3,6,1,4,1,2011,10,2,118,2,12,1,2),_H3cWIPSTrustListStatus_Type())
h3cWIPSTrustListStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSTrustListStatus.setStatus(_A)
_H3cWIPSChlStatTable_Object=MibTable
h3cWIPSChlStatTable=_H3cWIPSChlStatTable_Object((1,3,6,1,4,1,2011,10,2,118,2,13))
if mibBuilder.loadTexts:h3cWIPSChlStatTable.setStatus(_A)
_H3cWIPSChlStatEntry_Object=MibTableRow
h3cWIPSChlStatEntry=_H3cWIPSChlStatEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1))
h3cWIPSChlStatEntry.setIndexNames((0,_E,_AU),(0,_E,_AV))
if mibBuilder.loadTexts:h3cWIPSChlStatEntry.setStatus(_A)
_H3cWIPSChlStatSensorMacAddr_Type=MacAddress
_H3cWIPSChlStatSensorMacAddr_Object=MibTableColumn
h3cWIPSChlStatSensorMacAddr=_H3cWIPSChlStatSensorMacAddr_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,1),_H3cWIPSChlStatSensorMacAddr_Type())
h3cWIPSChlStatSensorMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSChlStatSensorMacAddr.setStatus(_A)
_H3cWIPSChlStatChannel_Type=H3cWIPSChannel
_H3cWIPSChlStatChannel_Object=MibTableColumn
h3cWIPSChlStatChannel=_H3cWIPSChlStatChannel_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,2),_H3cWIPSChlStatChannel_Type())
h3cWIPSChlStatChannel.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSChlStatChannel.setStatus(_A)
class _H3cWIPSChlStatTotalPkt_Type(Counter64):defaultValue=0
_H3cWIPSChlStatTotalPkt_Type.__name__=_D
_H3cWIPSChlStatTotalPkt_Object=MibTableColumn
h3cWIPSChlStatTotalPkt=_H3cWIPSChlStatTotalPkt_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,3),_H3cWIPSChlStatTotalPkt_Type())
h3cWIPSChlStatTotalPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatTotalPkt.setStatus(_A)
class _H3cWIPSChlStatTotalByte_Type(Counter64):defaultValue=0
_H3cWIPSChlStatTotalByte_Type.__name__=_D
_H3cWIPSChlStatTotalByte_Object=MibTableColumn
h3cWIPSChlStatTotalByte=_H3cWIPSChlStatTotalByte_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,4),_H3cWIPSChlStatTotalByte_Type())
h3cWIPSChlStatTotalByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatTotalByte.setStatus(_A)
class _H3cWIPSChlStatBmcastPkt_Type(Counter64):defaultValue=0
_H3cWIPSChlStatBmcastPkt_Type.__name__=_D
_H3cWIPSChlStatBmcastPkt_Object=MibTableColumn
h3cWIPSChlStatBmcastPkt=_H3cWIPSChlStatBmcastPkt_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,5),_H3cWIPSChlStatBmcastPkt_Type())
h3cWIPSChlStatBmcastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatBmcastPkt.setStatus(_A)
class _H3cWIPSChlStatBmcastByte_Type(Counter64):defaultValue=0
_H3cWIPSChlStatBmcastByte_Type.__name__=_D
_H3cWIPSChlStatBmcastByte_Object=MibTableColumn
h3cWIPSChlStatBmcastByte=_H3cWIPSChlStatBmcastByte_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,6),_H3cWIPSChlStatBmcastByte_Type())
h3cWIPSChlStatBmcastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatBmcastByte.setStatus(_A)
class _H3cWIPSChlStatUnicastPkt_Type(Counter64):defaultValue=0
_H3cWIPSChlStatUnicastPkt_Type.__name__=_D
_H3cWIPSChlStatUnicastPkt_Object=MibTableColumn
h3cWIPSChlStatUnicastPkt=_H3cWIPSChlStatUnicastPkt_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,7),_H3cWIPSChlStatUnicastPkt_Type())
h3cWIPSChlStatUnicastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatUnicastPkt.setStatus(_A)
class _H3cWIPSChlStatUnicastByte_Type(Counter64):defaultValue=0
_H3cWIPSChlStatUnicastByte_Type.__name__=_D
_H3cWIPSChlStatUnicastByte_Object=MibTableColumn
h3cWIPSChlStatUnicastByte=_H3cWIPSChlStatUnicastByte_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,8),_H3cWIPSChlStatUnicastByte_Type())
h3cWIPSChlStatUnicastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatUnicastByte.setStatus(_A)
class _H3cWIPSChlStatManagement_Type(Counter64):defaultValue=0
_H3cWIPSChlStatManagement_Type.__name__=_D
_H3cWIPSChlStatManagement_Object=MibTableColumn
h3cWIPSChlStatManagement=_H3cWIPSChlStatManagement_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,9),_H3cWIPSChlStatManagement_Type())
h3cWIPSChlStatManagement.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatManagement.setStatus(_A)
class _H3cWIPSChlStatControl_Type(Counter64):defaultValue=0
_H3cWIPSChlStatControl_Type.__name__=_D
_H3cWIPSChlStatControl_Object=MibTableColumn
h3cWIPSChlStatControl=_H3cWIPSChlStatControl_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,10),_H3cWIPSChlStatControl_Type())
h3cWIPSChlStatControl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatControl.setStatus(_A)
class _H3cWIPSChlStatData_Type(Counter64):defaultValue=0
_H3cWIPSChlStatData_Type.__name__=_D
_H3cWIPSChlStatData_Object=MibTableColumn
h3cWIPSChlStatData=_H3cWIPSChlStatData_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,11),_H3cWIPSChlStatData_Type())
h3cWIPSChlStatData.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatData.setStatus(_A)
class _H3cWIPSChlStatBeacon_Type(Counter64):defaultValue=0
_H3cWIPSChlStatBeacon_Type.__name__=_D
_H3cWIPSChlStatBeacon_Object=MibTableColumn
h3cWIPSChlStatBeacon=_H3cWIPSChlStatBeacon_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,12),_H3cWIPSChlStatBeacon_Type())
h3cWIPSChlStatBeacon.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatBeacon.setStatus(_A)
class _H3cWIPSChlStatRTS_Type(Counter64):defaultValue=0
_H3cWIPSChlStatRTS_Type.__name__=_D
_H3cWIPSChlStatRTS_Object=MibTableColumn
h3cWIPSChlStatRTS=_H3cWIPSChlStatRTS_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,13),_H3cWIPSChlStatRTS_Type())
h3cWIPSChlStatRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatRTS.setStatus(_A)
class _H3cWIPSChlStatCTS_Type(Counter64):defaultValue=0
_H3cWIPSChlStatCTS_Type.__name__=_D
_H3cWIPSChlStatCTS_Object=MibTableColumn
h3cWIPSChlStatCTS=_H3cWIPSChlStatCTS_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,14),_H3cWIPSChlStatCTS_Type())
h3cWIPSChlStatCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatCTS.setStatus(_A)
class _H3cWIPSChlStatProbeRequest_Type(Counter64):defaultValue=0
_H3cWIPSChlStatProbeRequest_Type.__name__=_D
_H3cWIPSChlStatProbeRequest_Object=MibTableColumn
h3cWIPSChlStatProbeRequest=_H3cWIPSChlStatProbeRequest_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,15),_H3cWIPSChlStatProbeRequest_Type())
h3cWIPSChlStatProbeRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatProbeRequest.setStatus(_A)
class _H3cWIPSChlStatProbeResponse_Type(Counter64):defaultValue=0
_H3cWIPSChlStatProbeResponse_Type.__name__=_D
_H3cWIPSChlStatProbeResponse_Object=MibTableColumn
h3cWIPSChlStatProbeResponse=_H3cWIPSChlStatProbeResponse_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,16),_H3cWIPSChlStatProbeResponse_Type())
h3cWIPSChlStatProbeResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatProbeResponse.setStatus(_A)
class _H3cWIPSChlStatFragment_Type(Counter64):defaultValue=0
_H3cWIPSChlStatFragment_Type.__name__=_D
_H3cWIPSChlStatFragment_Object=MibTableColumn
h3cWIPSChlStatFragment=_H3cWIPSChlStatFragment_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,17),_H3cWIPSChlStatFragment_Type())
h3cWIPSChlStatFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatFragment.setStatus(_A)
class _H3cWIPSChlStatRetry_Type(Counter64):defaultValue=0
_H3cWIPSChlStatRetry_Type.__name__=_D
_H3cWIPSChlStatRetry_Object=MibTableColumn
h3cWIPSChlStatRetry=_H3cWIPSChlStatRetry_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,18),_H3cWIPSChlStatRetry_Type())
h3cWIPSChlStatRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatRetry.setStatus(_A)
class _H3cWIPSChlStatEapSuccess_Type(Counter64):defaultValue=0
_H3cWIPSChlStatEapSuccess_Type.__name__=_D
_H3cWIPSChlStatEapSuccess_Object=MibTableColumn
h3cWIPSChlStatEapSuccess=_H3cWIPSChlStatEapSuccess_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,19),_H3cWIPSChlStatEapSuccess_Type())
h3cWIPSChlStatEapSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatEapSuccess.setStatus(_A)
class _H3cWIPSChlStatEapFailure_Type(Counter64):defaultValue=0
_H3cWIPSChlStatEapFailure_Type.__name__=_D
_H3cWIPSChlStatEapFailure_Object=MibTableColumn
h3cWIPSChlStatEapFailure=_H3cWIPSChlStatEapFailure_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,20),_H3cWIPSChlStatEapFailure_Type())
h3cWIPSChlStatEapFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatEapFailure.setStatus(_A)
class _H3cWIPSChlStatEapolStart_Type(Counter64):defaultValue=0
_H3cWIPSChlStatEapolStart_Type.__name__=_D
_H3cWIPSChlStatEapolStart_Object=MibTableColumn
h3cWIPSChlStatEapolStart=_H3cWIPSChlStatEapolStart_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,21),_H3cWIPSChlStatEapolStart_Type())
h3cWIPSChlStatEapolStart.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatEapolStart.setStatus(_A)
class _H3cWIPSChlStatEapolLogoff_Type(Counter64):defaultValue=0
_H3cWIPSChlStatEapolLogoff_Type.__name__=_D
_H3cWIPSChlStatEapolLogoff_Object=MibTableColumn
h3cWIPSChlStatEapolLogoff=_H3cWIPSChlStatEapolLogoff_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,22),_H3cWIPSChlStatEapolLogoff_Type())
h3cWIPSChlStatEapolLogoff.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatEapolLogoff.setStatus(_A)
class _H3cWIPSChlStatAssocRequest_Type(Counter64):defaultValue=0
_H3cWIPSChlStatAssocRequest_Type.__name__=_D
_H3cWIPSChlStatAssocRequest_Object=MibTableColumn
h3cWIPSChlStatAssocRequest=_H3cWIPSChlStatAssocRequest_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,23),_H3cWIPSChlStatAssocRequest_Type())
h3cWIPSChlStatAssocRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatAssocRequest.setStatus(_A)
class _H3cWIPSChlStatAssocResponse_Type(Counter64):defaultValue=0
_H3cWIPSChlStatAssocResponse_Type.__name__=_D
_H3cWIPSChlStatAssocResponse_Object=MibTableColumn
h3cWIPSChlStatAssocResponse=_H3cWIPSChlStatAssocResponse_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,24),_H3cWIPSChlStatAssocResponse_Type())
h3cWIPSChlStatAssocResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatAssocResponse.setStatus(_A)
class _H3cWIPSChlStatUnicastDisassoc_Type(Counter64):defaultValue=0
_H3cWIPSChlStatUnicastDisassoc_Type.__name__=_D
_H3cWIPSChlStatUnicastDisassoc_Object=MibTableColumn
h3cWIPSChlStatUnicastDisassoc=_H3cWIPSChlStatUnicastDisassoc_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,25),_H3cWIPSChlStatUnicastDisassoc_Type())
h3cWIPSChlStatUnicastDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatUnicastDisassoc.setStatus(_A)
class _H3cWIPSChlStatBroadcastDisassoc_Type(Counter64):defaultValue=0
_H3cWIPSChlStatBroadcastDisassoc_Type.__name__=_D
_H3cWIPSChlStatBroadcastDisassoc_Object=MibTableColumn
h3cWIPSChlStatBroadcastDisassoc=_H3cWIPSChlStatBroadcastDisassoc_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,26),_H3cWIPSChlStatBroadcastDisassoc_Type())
h3cWIPSChlStatBroadcastDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatBroadcastDisassoc.setStatus(_A)
class _H3cWIPSChlStatAuthentication_Type(Counter64):defaultValue=0
_H3cWIPSChlStatAuthentication_Type.__name__=_D
_H3cWIPSChlStatAuthentication_Object=MibTableColumn
h3cWIPSChlStatAuthentication=_H3cWIPSChlStatAuthentication_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,27),_H3cWIPSChlStatAuthentication_Type())
h3cWIPSChlStatAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatAuthentication.setStatus(_A)
class _H3cWIPSChlStatUnicastDeauthen_Type(Counter64):defaultValue=0
_H3cWIPSChlStatUnicastDeauthen_Type.__name__=_D
_H3cWIPSChlStatUnicastDeauthen_Object=MibTableColumn
h3cWIPSChlStatUnicastDeauthen=_H3cWIPSChlStatUnicastDeauthen_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,28),_H3cWIPSChlStatUnicastDeauthen_Type())
h3cWIPSChlStatUnicastDeauthen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatUnicastDeauthen.setStatus(_A)
class _H3cWIPSChlStatBroadcastDeauthen_Type(Counter64):defaultValue=0
_H3cWIPSChlStatBroadcastDeauthen_Type.__name__=_D
_H3cWIPSChlStatBroadcastDeauthen_Object=MibTableColumn
h3cWIPSChlStatBroadcastDeauthen=_H3cWIPSChlStatBroadcastDeauthen_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,29),_H3cWIPSChlStatBroadcastDeauthen_Type())
h3cWIPSChlStatBroadcastDeauthen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatBroadcastDeauthen.setStatus(_A)
class _H3cWIPSChlStatMalformed_Type(Counter64):defaultValue=0
_H3cWIPSChlStatMalformed_Type.__name__=_D
_H3cWIPSChlStatMalformed_Object=MibTableColumn
h3cWIPSChlStatMalformed=_H3cWIPSChlStatMalformed_Object((1,3,6,1,4,1,2011,10,2,118,2,13,1,30),_H3cWIPSChlStatMalformed_Type())
h3cWIPSChlStatMalformed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSChlStatMalformed.setStatus(_A)
_H3cWIPSDevStatTable_Object=MibTable
h3cWIPSDevStatTable=_H3cWIPSDevStatTable_Object((1,3,6,1,4,1,2011,10,2,118,2,14))
if mibBuilder.loadTexts:h3cWIPSDevStatTable.setStatus(_A)
_H3cWIPSDevStatEntry_Object=MibTableRow
h3cWIPSDevStatEntry=_H3cWIPSDevStatEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1))
h3cWIPSDevStatEntry.setIndexNames((0,_E,_AW),(0,_E,_AX),(0,_E,_AY))
if mibBuilder.loadTexts:h3cWIPSDevStatEntry.setStatus(_A)
_H3cWIPSDevStatSensorMacAddr_Type=MacAddress
_H3cWIPSDevStatSensorMacAddr_Object=MibTableColumn
h3cWIPSDevStatSensorMacAddr=_H3cWIPSDevStatSensorMacAddr_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,1),_H3cWIPSDevStatSensorMacAddr_Type())
h3cWIPSDevStatSensorMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDevStatSensorMacAddr.setStatus(_A)
_H3cWIPSDevStatDevMacAddress_Type=MacAddress
_H3cWIPSDevStatDevMacAddress_Object=MibTableColumn
h3cWIPSDevStatDevMacAddress=_H3cWIPSDevStatDevMacAddress_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,2),_H3cWIPSDevStatDevMacAddress_Type())
h3cWIPSDevStatDevMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDevStatDevMacAddress.setStatus(_A)
_H3cWIPSDevStatChannel_Type=H3cWIPSChannel
_H3cWIPSDevStatChannel_Object=MibTableColumn
h3cWIPSDevStatChannel=_H3cWIPSDevStatChannel_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,3),_H3cWIPSDevStatChannel_Type())
h3cWIPSDevStatChannel.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDevStatChannel.setStatus(_A)
class _H3cWIPSDevStatTxTotalPkt_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxTotalPkt_Type.__name__=_D
_H3cWIPSDevStatTxTotalPkt_Object=MibTableColumn
h3cWIPSDevStatTxTotalPkt=_H3cWIPSDevStatTxTotalPkt_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,4),_H3cWIPSDevStatTxTotalPkt_Type())
h3cWIPSDevStatTxTotalPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxTotalPkt.setStatus(_A)
class _H3cWIPSDevStatTxTotalByte_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxTotalByte_Type.__name__=_D
_H3cWIPSDevStatTxTotalByte_Object=MibTableColumn
h3cWIPSDevStatTxTotalByte=_H3cWIPSDevStatTxTotalByte_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,5),_H3cWIPSDevStatTxTotalByte_Type())
h3cWIPSDevStatTxTotalByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxTotalByte.setStatus(_A)
class _H3cWIPSDevStatTxBMcastPkt_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxBMcastPkt_Type.__name__=_D
_H3cWIPSDevStatTxBMcastPkt_Object=MibTableColumn
h3cWIPSDevStatTxBMcastPkt=_H3cWIPSDevStatTxBMcastPkt_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,6),_H3cWIPSDevStatTxBMcastPkt_Type())
h3cWIPSDevStatTxBMcastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxBMcastPkt.setStatus(_A)
class _H3cWIPSDevStatTxBMcastByte_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxBMcastByte_Type.__name__=_D
_H3cWIPSDevStatTxBMcastByte_Object=MibTableColumn
h3cWIPSDevStatTxBMcastByte=_H3cWIPSDevStatTxBMcastByte_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,7),_H3cWIPSDevStatTxBMcastByte_Type())
h3cWIPSDevStatTxBMcastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxBMcastByte.setStatus(_A)
class _H3cWIPSDevStatTxUnicastPkt_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxUnicastPkt_Type.__name__=_D
_H3cWIPSDevStatTxUnicastPkt_Object=MibTableColumn
h3cWIPSDevStatTxUnicastPkt=_H3cWIPSDevStatTxUnicastPkt_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,8),_H3cWIPSDevStatTxUnicastPkt_Type())
h3cWIPSDevStatTxUnicastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxUnicastPkt.setStatus(_A)
class _H3cWIPSDevStatTxUnicastByte_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxUnicastByte_Type.__name__=_D
_H3cWIPSDevStatTxUnicastByte_Object=MibTableColumn
h3cWIPSDevStatTxUnicastByte=_H3cWIPSDevStatTxUnicastByte_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,9),_H3cWIPSDevStatTxUnicastByte_Type())
h3cWIPSDevStatTxUnicastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxUnicastByte.setStatus(_A)
class _H3cWIPSDevStatTxMgmt_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxMgmt_Type.__name__=_D
_H3cWIPSDevStatTxMgmt_Object=MibTableColumn
h3cWIPSDevStatTxMgmt=_H3cWIPSDevStatTxMgmt_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,10),_H3cWIPSDevStatTxMgmt_Type())
h3cWIPSDevStatTxMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxMgmt.setStatus(_A)
class _H3cWIPSDevStatTxCtrl_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxCtrl_Type.__name__=_D
_H3cWIPSDevStatTxCtrl_Object=MibTableColumn
h3cWIPSDevStatTxCtrl=_H3cWIPSDevStatTxCtrl_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,11),_H3cWIPSDevStatTxCtrl_Type())
h3cWIPSDevStatTxCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxCtrl.setStatus(_A)
class _H3cWIPSDevStatTxData_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxData_Type.__name__=_D
_H3cWIPSDevStatTxData_Object=MibTableColumn
h3cWIPSDevStatTxData=_H3cWIPSDevStatTxData_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,12),_H3cWIPSDevStatTxData_Type())
h3cWIPSDevStatTxData.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxData.setStatus(_A)
class _H3cWIPSDevStatTxBeacon_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxBeacon_Type.__name__=_D
_H3cWIPSDevStatTxBeacon_Object=MibTableColumn
h3cWIPSDevStatTxBeacon=_H3cWIPSDevStatTxBeacon_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,13),_H3cWIPSDevStatTxBeacon_Type())
h3cWIPSDevStatTxBeacon.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxBeacon.setStatus(_A)
class _H3cWIPSDevStatTxRTS_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxRTS_Type.__name__=_D
_H3cWIPSDevStatTxRTS_Object=MibTableColumn
h3cWIPSDevStatTxRTS=_H3cWIPSDevStatTxRTS_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,14),_H3cWIPSDevStatTxRTS_Type())
h3cWIPSDevStatTxRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxRTS.setStatus(_A)
class _H3cWIPSDevStatTxProbeRequest_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxProbeRequest_Type.__name__=_D
_H3cWIPSDevStatTxProbeRequest_Object=MibTableColumn
h3cWIPSDevStatTxProbeRequest=_H3cWIPSDevStatTxProbeRequest_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,15),_H3cWIPSDevStatTxProbeRequest_Type())
h3cWIPSDevStatTxProbeRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxProbeRequest.setStatus(_A)
class _H3cWIPSDevStatTxProbeResponse_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxProbeResponse_Type.__name__=_D
_H3cWIPSDevStatTxProbeResponse_Object=MibTableColumn
h3cWIPSDevStatTxProbeResponse=_H3cWIPSDevStatTxProbeResponse_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,16),_H3cWIPSDevStatTxProbeResponse_Type())
h3cWIPSDevStatTxProbeResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxProbeResponse.setStatus(_A)
class _H3cWIPSDevStatTxFragment_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxFragment_Type.__name__=_D
_H3cWIPSDevStatTxFragment_Object=MibTableColumn
h3cWIPSDevStatTxFragment=_H3cWIPSDevStatTxFragment_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,17),_H3cWIPSDevStatTxFragment_Type())
h3cWIPSDevStatTxFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxFragment.setStatus(_A)
class _H3cWIPSDevStatTxRetry_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxRetry_Type.__name__=_D
_H3cWIPSDevStatTxRetry_Object=MibTableColumn
h3cWIPSDevStatTxRetry=_H3cWIPSDevStatTxRetry_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,18),_H3cWIPSDevStatTxRetry_Type())
h3cWIPSDevStatTxRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxRetry.setStatus(_A)
class _H3cWIPSDevStatTxAssocRequest_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxAssocRequest_Type.__name__=_D
_H3cWIPSDevStatTxAssocRequest_Object=MibTableColumn
h3cWIPSDevStatTxAssocRequest=_H3cWIPSDevStatTxAssocRequest_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,19),_H3cWIPSDevStatTxAssocRequest_Type())
h3cWIPSDevStatTxAssocRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxAssocRequest.setStatus(_A)
class _H3cWIPSDevStatTxAssocResponse_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxAssocResponse_Type.__name__=_D
_H3cWIPSDevStatTxAssocResponse_Object=MibTableColumn
h3cWIPSDevStatTxAssocResponse=_H3cWIPSDevStatTxAssocResponse_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,20),_H3cWIPSDevStatTxAssocResponse_Type())
h3cWIPSDevStatTxAssocResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxAssocResponse.setStatus(_A)
class _H3cWIPSDevStatTxUnicastDisassoc_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxUnicastDisassoc_Type.__name__=_D
_H3cWIPSDevStatTxUnicastDisassoc_Object=MibTableColumn
h3cWIPSDevStatTxUnicastDisassoc=_H3cWIPSDevStatTxUnicastDisassoc_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,21),_H3cWIPSDevStatTxUnicastDisassoc_Type())
h3cWIPSDevStatTxUnicastDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxUnicastDisassoc.setStatus(_A)
class _H3cWIPSDevStatTxBcastDisassoc_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxBcastDisassoc_Type.__name__=_D
_H3cWIPSDevStatTxBcastDisassoc_Object=MibTableColumn
h3cWIPSDevStatTxBcastDisassoc=_H3cWIPSDevStatTxBcastDisassoc_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,22),_H3cWIPSDevStatTxBcastDisassoc_Type())
h3cWIPSDevStatTxBcastDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxBcastDisassoc.setStatus(_A)
class _H3cWIPSDevStatTxAuth_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxAuth_Type.__name__=_D
_H3cWIPSDevStatTxAuth_Object=MibTableColumn
h3cWIPSDevStatTxAuth=_H3cWIPSDevStatTxAuth_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,23),_H3cWIPSDevStatTxAuth_Type())
h3cWIPSDevStatTxAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxAuth.setStatus(_A)
class _H3cWIPSDevStatTxUnicastDeauth_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxUnicastDeauth_Type.__name__=_D
_H3cWIPSDevStatTxUnicastDeauth_Object=MibTableColumn
h3cWIPSDevStatTxUnicastDeauth=_H3cWIPSDevStatTxUnicastDeauth_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,24),_H3cWIPSDevStatTxUnicastDeauth_Type())
h3cWIPSDevStatTxUnicastDeauth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxUnicastDeauth.setStatus(_A)
class _H3cWIPSDevStatTxBcastDeauth_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxBcastDeauth_Type.__name__=_D
_H3cWIPSDevStatTxBcastDeauth_Object=MibTableColumn
h3cWIPSDevStatTxBcastDeauth=_H3cWIPSDevStatTxBcastDeauth_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,25),_H3cWIPSDevStatTxBcastDeauth_Type())
h3cWIPSDevStatTxBcastDeauth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxBcastDeauth.setStatus(_A)
class _H3cWIPSDevStatTxEAPSuccess_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxEAPSuccess_Type.__name__=_D
_H3cWIPSDevStatTxEAPSuccess_Object=MibTableColumn
h3cWIPSDevStatTxEAPSuccess=_H3cWIPSDevStatTxEAPSuccess_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,26),_H3cWIPSDevStatTxEAPSuccess_Type())
h3cWIPSDevStatTxEAPSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxEAPSuccess.setStatus(_A)
class _H3cWIPSDevStatTxEAPFailure_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxEAPFailure_Type.__name__=_D
_H3cWIPSDevStatTxEAPFailure_Object=MibTableColumn
h3cWIPSDevStatTxEAPFailure=_H3cWIPSDevStatTxEAPFailure_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,27),_H3cWIPSDevStatTxEAPFailure_Type())
h3cWIPSDevStatTxEAPFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxEAPFailure.setStatus(_A)
class _H3cWIPSDevStatTxEAPOLStart_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxEAPOLStart_Type.__name__=_D
_H3cWIPSDevStatTxEAPOLStart_Object=MibTableColumn
h3cWIPSDevStatTxEAPOLStart=_H3cWIPSDevStatTxEAPOLStart_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,28),_H3cWIPSDevStatTxEAPOLStart_Type())
h3cWIPSDevStatTxEAPOLStart.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxEAPOLStart.setStatus(_A)
class _H3cWIPSDevStatTxEAPOLLogOff_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxEAPOLLogOff_Type.__name__=_D
_H3cWIPSDevStatTxEAPOLLogOff_Object=MibTableColumn
h3cWIPSDevStatTxEAPOLLogOff=_H3cWIPSDevStatTxEAPOLLogOff_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,29),_H3cWIPSDevStatTxEAPOLLogOff_Type())
h3cWIPSDevStatTxEAPOLLogOff.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxEAPOLLogOff.setStatus(_A)
class _H3cWIPSDevStatTxMalformed_Type(Counter64):defaultValue=0
_H3cWIPSDevStatTxMalformed_Type.__name__=_D
_H3cWIPSDevStatTxMalformed_Object=MibTableColumn
h3cWIPSDevStatTxMalformed=_H3cWIPSDevStatTxMalformed_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,30),_H3cWIPSDevStatTxMalformed_Type())
h3cWIPSDevStatTxMalformed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatTxMalformed.setStatus(_A)
class _H3cWIPSDevStatRxTotalPkt_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxTotalPkt_Type.__name__=_D
_H3cWIPSDevStatRxTotalPkt_Object=MibTableColumn
h3cWIPSDevStatRxTotalPkt=_H3cWIPSDevStatRxTotalPkt_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,31),_H3cWIPSDevStatRxTotalPkt_Type())
h3cWIPSDevStatRxTotalPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxTotalPkt.setStatus(_A)
class _H3cWIPSDevStatRxTotalByte_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxTotalByte_Type.__name__=_D
_H3cWIPSDevStatRxTotalByte_Object=MibTableColumn
h3cWIPSDevStatRxTotalByte=_H3cWIPSDevStatRxTotalByte_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,32),_H3cWIPSDevStatRxTotalByte_Type())
h3cWIPSDevStatRxTotalByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxTotalByte.setStatus(_A)
class _H3cWIPSDevStatRxUnicastPkt_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxUnicastPkt_Type.__name__=_D
_H3cWIPSDevStatRxUnicastPkt_Object=MibTableColumn
h3cWIPSDevStatRxUnicastPkt=_H3cWIPSDevStatRxUnicastPkt_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,33),_H3cWIPSDevStatRxUnicastPkt_Type())
h3cWIPSDevStatRxUnicastPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxUnicastPkt.setStatus(_A)
class _H3cWIPSDevStatRxUnicastByte_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxUnicastByte_Type.__name__=_D
_H3cWIPSDevStatRxUnicastByte_Object=MibTableColumn
h3cWIPSDevStatRxUnicastByte=_H3cWIPSDevStatRxUnicastByte_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,34),_H3cWIPSDevStatRxUnicastByte_Type())
h3cWIPSDevStatRxUnicastByte.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxUnicastByte.setStatus(_A)
class _H3cWIPSDevStatRxMgmt_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxMgmt_Type.__name__=_D
_H3cWIPSDevStatRxMgmt_Object=MibTableColumn
h3cWIPSDevStatRxMgmt=_H3cWIPSDevStatRxMgmt_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,35),_H3cWIPSDevStatRxMgmt_Type())
h3cWIPSDevStatRxMgmt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxMgmt.setStatus(_A)
class _H3cWIPSDevStatRxCtrl_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxCtrl_Type.__name__=_D
_H3cWIPSDevStatRxCtrl_Object=MibTableColumn
h3cWIPSDevStatRxCtrl=_H3cWIPSDevStatRxCtrl_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,36),_H3cWIPSDevStatRxCtrl_Type())
h3cWIPSDevStatRxCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxCtrl.setStatus(_A)
class _H3cWIPSDevStatRxData_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxData_Type.__name__=_D
_H3cWIPSDevStatRxData_Object=MibTableColumn
h3cWIPSDevStatRxData=_H3cWIPSDevStatRxData_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,37),_H3cWIPSDevStatRxData_Type())
h3cWIPSDevStatRxData.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxData.setStatus(_A)
class _H3cWIPSDevStatRxRTS_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxRTS_Type.__name__=_D
_H3cWIPSDevStatRxRTS_Object=MibTableColumn
h3cWIPSDevStatRxRTS=_H3cWIPSDevStatRxRTS_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,38),_H3cWIPSDevStatRxRTS_Type())
h3cWIPSDevStatRxRTS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxRTS.setStatus(_A)
class _H3cWIPSDevStatRxCTS_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxCTS_Type.__name__=_D
_H3cWIPSDevStatRxCTS_Object=MibTableColumn
h3cWIPSDevStatRxCTS=_H3cWIPSDevStatRxCTS_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,39),_H3cWIPSDevStatRxCTS_Type())
h3cWIPSDevStatRxCTS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxCTS.setStatus(_A)
class _H3cWIPSDevStatRxProbeRequest_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxProbeRequest_Type.__name__=_D
_H3cWIPSDevStatRxProbeRequest_Object=MibTableColumn
h3cWIPSDevStatRxProbeRequest=_H3cWIPSDevStatRxProbeRequest_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,40),_H3cWIPSDevStatRxProbeRequest_Type())
h3cWIPSDevStatRxProbeRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxProbeRequest.setStatus(_A)
class _H3cWIPSDevStatRxProbeResponse_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxProbeResponse_Type.__name__=_D
_H3cWIPSDevStatRxProbeResponse_Object=MibTableColumn
h3cWIPSDevStatRxProbeResponse=_H3cWIPSDevStatRxProbeResponse_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,41),_H3cWIPSDevStatRxProbeResponse_Type())
h3cWIPSDevStatRxProbeResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxProbeResponse.setStatus(_A)
class _H3cWIPSDevStatRxFragment_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxFragment_Type.__name__=_D
_H3cWIPSDevStatRxFragment_Object=MibTableColumn
h3cWIPSDevStatRxFragment=_H3cWIPSDevStatRxFragment_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,42),_H3cWIPSDevStatRxFragment_Type())
h3cWIPSDevStatRxFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxFragment.setStatus(_A)
class _H3cWIPSDevStatRxRetry_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxRetry_Type.__name__=_D
_H3cWIPSDevStatRxRetry_Object=MibTableColumn
h3cWIPSDevStatRxRetry=_H3cWIPSDevStatRxRetry_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,43),_H3cWIPSDevStatRxRetry_Type())
h3cWIPSDevStatRxRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxRetry.setStatus(_A)
class _H3cWIPSDevStatRxAssoRequest_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxAssoRequest_Type.__name__=_D
_H3cWIPSDevStatRxAssoRequest_Object=MibTableColumn
h3cWIPSDevStatRxAssoRequest=_H3cWIPSDevStatRxAssoRequest_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,44),_H3cWIPSDevStatRxAssoRequest_Type())
h3cWIPSDevStatRxAssoRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxAssoRequest.setStatus(_A)
class _H3cWIPSDevStatRxAssoResponse_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxAssoResponse_Type.__name__=_D
_H3cWIPSDevStatRxAssoResponse_Object=MibTableColumn
h3cWIPSDevStatRxAssoResponse=_H3cWIPSDevStatRxAssoResponse_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,45),_H3cWIPSDevStatRxAssoResponse_Type())
h3cWIPSDevStatRxAssoResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxAssoResponse.setStatus(_A)
class _H3cWIPSDevStatRxDisassoc_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxDisassoc_Type.__name__=_D
_H3cWIPSDevStatRxDisassoc_Object=MibTableColumn
h3cWIPSDevStatRxDisassoc=_H3cWIPSDevStatRxDisassoc_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,46),_H3cWIPSDevStatRxDisassoc_Type())
h3cWIPSDevStatRxDisassoc.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxDisassoc.setStatus(_A)
class _H3cWIPSDevStatRxAuth_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxAuth_Type.__name__=_D
_H3cWIPSDevStatRxAuth_Object=MibTableColumn
h3cWIPSDevStatRxAuth=_H3cWIPSDevStatRxAuth_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,47),_H3cWIPSDevStatRxAuth_Type())
h3cWIPSDevStatRxAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxAuth.setStatus(_A)
class _H3cWIPSDevStatRxDeauth_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxDeauth_Type.__name__=_D
_H3cWIPSDevStatRxDeauth_Object=MibTableColumn
h3cWIPSDevStatRxDeauth=_H3cWIPSDevStatRxDeauth_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,48),_H3cWIPSDevStatRxDeauth_Type())
h3cWIPSDevStatRxDeauth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxDeauth.setStatus(_A)
class _H3cWIPSDevStatRxEAPSuccess_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxEAPSuccess_Type.__name__=_D
_H3cWIPSDevStatRxEAPSuccess_Object=MibTableColumn
h3cWIPSDevStatRxEAPSuccess=_H3cWIPSDevStatRxEAPSuccess_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,49),_H3cWIPSDevStatRxEAPSuccess_Type())
h3cWIPSDevStatRxEAPSuccess.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxEAPSuccess.setStatus(_A)
class _H3cWIPSDevStatRxEAPFailure_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxEAPFailure_Type.__name__=_D
_H3cWIPSDevStatRxEAPFailure_Object=MibTableColumn
h3cWIPSDevStatRxEAPFailure=_H3cWIPSDevStatRxEAPFailure_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,50),_H3cWIPSDevStatRxEAPFailure_Type())
h3cWIPSDevStatRxEAPFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxEAPFailure.setStatus(_A)
class _H3cWIPSDevStatRxEAPOLStart_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxEAPOLStart_Type.__name__=_D
_H3cWIPSDevStatRxEAPOLStart_Object=MibTableColumn
h3cWIPSDevStatRxEAPOLStart=_H3cWIPSDevStatRxEAPOLStart_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,51),_H3cWIPSDevStatRxEAPOLStart_Type())
h3cWIPSDevStatRxEAPOLStart.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxEAPOLStart.setStatus(_A)
class _H3cWIPSDevStatRxEAPOLLogoff_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxEAPOLLogoff_Type.__name__=_D
_H3cWIPSDevStatRxEAPOLLogoff_Object=MibTableColumn
h3cWIPSDevStatRxEAPOLLogoff=_H3cWIPSDevStatRxEAPOLLogoff_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,52),_H3cWIPSDevStatRxEAPOLLogoff_Type())
h3cWIPSDevStatRxEAPOLLogoff.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxEAPOLLogoff.setStatus(_A)
class _H3cWIPSDevStatRxMalformed_Type(Counter64):defaultValue=0
_H3cWIPSDevStatRxMalformed_Type.__name__=_D
_H3cWIPSDevStatRxMalformed_Object=MibTableColumn
h3cWIPSDevStatRxMalformed=_H3cWIPSDevStatRxMalformed_Object((1,3,6,1,4,1,2011,10,2,118,2,14,1,53),_H3cWIPSDevStatRxMalformed_Type())
h3cWIPSDevStatRxMalformed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDevStatRxMalformed.setStatus(_A)
_H3cWIPSCtmDeviceTable_Object=MibTable
h3cWIPSCtmDeviceTable=_H3cWIPSCtmDeviceTable_Object((1,3,6,1,4,1,2011,10,2,118,2,15))
if mibBuilder.loadTexts:h3cWIPSCtmDeviceTable.setStatus(_A)
_H3cWIPSCtmDeviceEntry_Object=MibTableRow
h3cWIPSCtmDeviceEntry=_H3cWIPSCtmDeviceEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,15,1))
h3cWIPSCtmDeviceEntry.setIndexNames((0,_E,_AZ),(0,_E,_Aa))
if mibBuilder.loadTexts:h3cWIPSCtmDeviceEntry.setStatus(_A)
class _H3cWIPSCtmDeviceVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSCtmDeviceVSD_Type.__name__=_H
_H3cWIPSCtmDeviceVSD_Object=MibTableColumn
h3cWIPSCtmDeviceVSD=_H3cWIPSCtmDeviceVSD_Object((1,3,6,1,4,1,2011,10,2,118,2,15,1,1),_H3cWIPSCtmDeviceVSD_Type())
h3cWIPSCtmDeviceVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSCtmDeviceVSD.setStatus(_A)
_H3cWIPSCtmDeviceMAC_Type=MacAddress
_H3cWIPSCtmDeviceMAC_Object=MibTableColumn
h3cWIPSCtmDeviceMAC=_H3cWIPSCtmDeviceMAC_Object((1,3,6,1,4,1,2011,10,2,118,2,15,1,2),_H3cWIPSCtmDeviceMAC_Type())
h3cWIPSCtmDeviceMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSCtmDeviceMAC.setStatus(_A)
class _H3cWIPSCtmDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_f,2),('staticAnddynamic',3)))
_H3cWIPSCtmDeviceType_Type.__name__=_F
_H3cWIPSCtmDeviceType_Object=MibTableColumn
h3cWIPSCtmDeviceType=_H3cWIPSCtmDeviceType_Object((1,3,6,1,4,1,2011,10,2,118,2,15,1,3),_H3cWIPSCtmDeviceType_Type())
h3cWIPSCtmDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmDeviceType.setStatus(_A)
class _H3cWIPSCtmDeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_M,0),('idle',1),('pending',2),('action',3)))
_H3cWIPSCtmDeviceState_Type.__name__=_F
_H3cWIPSCtmDeviceState_Object=MibTableColumn
h3cWIPSCtmDeviceState=_H3cWIPSCtmDeviceState_Object((1,3,6,1,4,1,2011,10,2,118,2,15,1,4),_H3cWIPSCtmDeviceState_Type())
h3cWIPSCtmDeviceState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmDeviceState.setStatus(_A)
_H3cWIPSCtmDeviceStartTime_Type=TimeTicks
_H3cWIPSCtmDeviceStartTime_Object=MibTableColumn
h3cWIPSCtmDeviceStartTime=_H3cWIPSCtmDeviceStartTime_Object((1,3,6,1,4,1,2011,10,2,118,2,15,1,5),_H3cWIPSCtmDeviceStartTime_Type())
h3cWIPSCtmDeviceStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmDeviceStartTime.setStatus(_A)
_H3cWIPSCtmDeviceCategory_Type=H3cWIPSDeviceCategoryType
_H3cWIPSCtmDeviceCategory_Object=MibTableColumn
h3cWIPSCtmDeviceCategory=_H3cWIPSCtmDeviceCategory_Object((1,3,6,1,4,1,2011,10,2,118,2,15,1,6),_H3cWIPSCtmDeviceCategory_Type())
h3cWIPSCtmDeviceCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmDeviceCategory.setStatus(_A)
_H3cWIPSCtmDeviceChl_Type=Unsigned32
_H3cWIPSCtmDeviceChl_Object=MibTableColumn
h3cWIPSCtmDeviceChl=_H3cWIPSCtmDeviceChl_Object((1,3,6,1,4,1,2011,10,2,118,2,15,1,7),_H3cWIPSCtmDeviceChl_Type())
h3cWIPSCtmDeviceChl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmDeviceChl.setStatus(_A)
class _H3cWIPSCtmDevicePrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_H3cWIPSCtmDevicePrecedence_Type.__name__=_F
_H3cWIPSCtmDevicePrecedence_Object=MibTableColumn
h3cWIPSCtmDevicePrecedence=_H3cWIPSCtmDevicePrecedence_Object((1,3,6,1,4,1,2011,10,2,118,2,15,1,8),_H3cWIPSCtmDevicePrecedence_Type())
h3cWIPSCtmDevicePrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSCtmDevicePrecedence.setStatus(_A)
_H3cWIPSMalPktStatTable_Object=MibTable
h3cWIPSMalPktStatTable=_H3cWIPSMalPktStatTable_Object((1,3,6,1,4,1,2011,10,2,118,2,16))
if mibBuilder.loadTexts:h3cWIPSMalPktStatTable.setStatus(_A)
_H3cWIPSMalPktStatEntry_Object=MibTableRow
h3cWIPSMalPktStatEntry=_H3cWIPSMalPktStatEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1))
h3cWIPSMalPktStatEntry.setIndexNames((0,_E,_Ab))
if mibBuilder.loadTexts:h3cWIPSMalPktStatEntry.setStatus(_A)
class _H3cWIPSMalPktStatSensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cWIPSMalPktStatSensorName_Type.__name__=_H
_H3cWIPSMalPktStatSensorName_Object=MibTableColumn
h3cWIPSMalPktStatSensorName=_H3cWIPSMalPktStatSensorName_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,1),_H3cWIPSMalPktStatSensorName_Type())
h3cWIPSMalPktStatSensorName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSMalPktStatSensorName.setStatus(_A)
class _H3cWIPSMalPktStatInvalidIELength_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatInvalidIELength_Type.__name__=_D
_H3cWIPSMalPktStatInvalidIELength_Object=MibTableColumn
h3cWIPSMalPktStatInvalidIELength=_H3cWIPSMalPktStatInvalidIELength_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,2),_H3cWIPSMalPktStatInvalidIELength_Type())
h3cWIPSMalPktStatInvalidIELength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatInvalidIELength.setStatus(_A)
class _H3cWIPSMalPktStatDuplicatedIE_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatDuplicatedIE_Type.__name__=_D
_H3cWIPSMalPktStatDuplicatedIE_Object=MibTableColumn
h3cWIPSMalPktStatDuplicatedIE=_H3cWIPSMalPktStatDuplicatedIE_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,3),_H3cWIPSMalPktStatDuplicatedIE_Type())
h3cWIPSMalPktStatDuplicatedIE.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatDuplicatedIE.setStatus(_A)
class _H3cWIPSMalPktStatRedundantIE_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatRedundantIE_Type.__name__=_D
_H3cWIPSMalPktStatRedundantIE_Object=MibTableColumn
h3cWIPSMalPktStatRedundantIE=_H3cWIPSMalPktStatRedundantIE_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,4),_H3cWIPSMalPktStatRedundantIE_Type())
h3cWIPSMalPktStatRedundantIE.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatRedundantIE.setStatus(_A)
class _H3cWIPSMalPktStatInvalidPktLength_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatInvalidPktLength_Type.__name__=_D
_H3cWIPSMalPktStatInvalidPktLength_Object=MibTableColumn
h3cWIPSMalPktStatInvalidPktLength=_H3cWIPSMalPktStatInvalidPktLength_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,5),_H3cWIPSMalPktStatInvalidPktLength_Type())
h3cWIPSMalPktStatInvalidPktLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatInvalidPktLength.setStatus(_A)
class _H3cWIPSMalPktStatIllegalIBSSESS_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatIllegalIBSSESS_Type.__name__=_D
_H3cWIPSMalPktStatIllegalIBSSESS_Object=MibTableColumn
h3cWIPSMalPktStatIllegalIBSSESS=_H3cWIPSMalPktStatIllegalIBSSESS_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,6),_H3cWIPSMalPktStatIllegalIBSSESS_Type())
h3cWIPSMalPktStatIllegalIBSSESS.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatIllegalIBSSESS.setStatus(_A)
class _H3cWIPSMalPktStatInvalidSourceAddr_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatInvalidSourceAddr_Type.__name__=_D
_H3cWIPSMalPktStatInvalidSourceAddr_Object=MibTableColumn
h3cWIPSMalPktStatInvalidSourceAddr=_H3cWIPSMalPktStatInvalidSourceAddr_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,7),_H3cWIPSMalPktStatInvalidSourceAddr_Type())
h3cWIPSMalPktStatInvalidSourceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatInvalidSourceAddr.setStatus(_A)
class _H3cWIPSMalPktStatOverflowEAPOLKey_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatOverflowEAPOLKey_Type.__name__=_D
_H3cWIPSMalPktStatOverflowEAPOLKey_Object=MibTableColumn
h3cWIPSMalPktStatOverflowEAPOLKey=_H3cWIPSMalPktStatOverflowEAPOLKey_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,8),_H3cWIPSMalPktStatOverflowEAPOLKey_Type())
h3cWIPSMalPktStatOverflowEAPOLKey.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatOverflowEAPOLKey.setStatus(_A)
class _H3cWIPSMalPktStatMalAuth_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatMalAuth_Type.__name__=_D
_H3cWIPSMalPktStatMalAuth_Object=MibTableColumn
h3cWIPSMalPktStatMalAuth=_H3cWIPSMalPktStatMalAuth_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,9),_H3cWIPSMalPktStatMalAuth_Type())
h3cWIPSMalPktStatMalAuth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatMalAuth.setStatus(_A)
class _H3cWIPSMalPktStatMalAssoReq_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatMalAssoReq_Type.__name__=_D
_H3cWIPSMalPktStatMalAssoReq_Object=MibTableColumn
h3cWIPSMalPktStatMalAssoReq=_H3cWIPSMalPktStatMalAssoReq_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,10),_H3cWIPSMalPktStatMalAssoReq_Type())
h3cWIPSMalPktStatMalAssoReq.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatMalAssoReq.setStatus(_A)
class _H3cWIPSMalPktStatMalHTIE_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatMalHTIE_Type.__name__=_D
_H3cWIPSMalPktStatMalHTIE_Object=MibTableColumn
h3cWIPSMalPktStatMalHTIE=_H3cWIPSMalPktStatMalHTIE_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,11),_H3cWIPSMalPktStatMalHTIE_Type())
h3cWIPSMalPktStatMalHTIE.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatMalHTIE.setStatus(_A)
class _H3cWIPSMalPktStatLargeDuration_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatLargeDuration_Type.__name__=_D
_H3cWIPSMalPktStatLargeDuration_Object=MibTableColumn
h3cWIPSMalPktStatLargeDuration=_H3cWIPSMalPktStatLargeDuration_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,12),_H3cWIPSMalPktStatLargeDuration_Type())
h3cWIPSMalPktStatLargeDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatLargeDuration.setStatus(_A)
class _H3cWIPSMalPktStatNULLProbeRes_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatNULLProbeRes_Type.__name__=_D
_H3cWIPSMalPktStatNULLProbeRes_Object=MibTableColumn
h3cWIPSMalPktStatNULLProbeRes=_H3cWIPSMalPktStatNULLProbeRes_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,13),_H3cWIPSMalPktStatNULLProbeRes_Type())
h3cWIPSMalPktStatNULLProbeRes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatNULLProbeRes.setStatus(_A)
class _H3cWIPSMalPktStatInvalidDeAuthCode_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatInvalidDeAuthCode_Type.__name__=_D
_H3cWIPSMalPktStatInvalidDeAuthCode_Object=MibTableColumn
h3cWIPSMalPktStatInvalidDeAuthCode=_H3cWIPSMalPktStatInvalidDeAuthCode_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,14),_H3cWIPSMalPktStatInvalidDeAuthCode_Type())
h3cWIPSMalPktStatInvalidDeAuthCode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatInvalidDeAuthCode.setStatus(_A)
class _H3cWIPSMalPktStatInvalidDisAssoCode_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatInvalidDisAssoCode_Type.__name__=_D
_H3cWIPSMalPktStatInvalidDisAssoCode_Object=MibTableColumn
h3cWIPSMalPktStatInvalidDisAssoCode=_H3cWIPSMalPktStatInvalidDisAssoCode_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,15),_H3cWIPSMalPktStatInvalidDisAssoCode_Type())
h3cWIPSMalPktStatInvalidDisAssoCode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatInvalidDisAssoCode.setStatus(_A)
class _H3cWIPSMalPktStatOverflowSSID_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatOverflowSSID_Type.__name__=_D
_H3cWIPSMalPktStatOverflowSSID_Object=MibTableColumn
h3cWIPSMalPktStatOverflowSSID=_H3cWIPSMalPktStatOverflowSSID_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,16),_H3cWIPSMalPktStatOverflowSSID_Type())
h3cWIPSMalPktStatOverflowSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatOverflowSSID.setStatus(_A)
class _H3cWIPSMalPktStatFatajack_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatFatajack_Type.__name__=_D
_H3cWIPSMalPktStatFatajack_Object=MibTableColumn
h3cWIPSMalPktStatFatajack=_H3cWIPSMalPktStatFatajack_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,17),_H3cWIPSMalPktStatFatajack_Type())
h3cWIPSMalPktStatFatajack.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatFatajack.setStatus(_A)
class _H3cWIPSMalPktStatInvalidChannel_Type(Counter64):defaultValue=0
_H3cWIPSMalPktStatInvalidChannel_Type.__name__=_D
_H3cWIPSMalPktStatInvalidChannel_Object=MibTableColumn
h3cWIPSMalPktStatInvalidChannel=_H3cWIPSMalPktStatInvalidChannel_Object((1,3,6,1,4,1,2011,10,2,118,2,16,1,18),_H3cWIPSMalPktStatInvalidChannel_Type())
h3cWIPSMalPktStatInvalidChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSMalPktStatInvalidChannel.setStatus(_A)
_H3cWIPSDctUnassocStaTable_Object=MibTable
h3cWIPSDctUnassocStaTable=_H3cWIPSDctUnassocStaTable_Object((1,3,6,1,4,1,2011,10,2,118,2,17))
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaTable.setStatus(_A)
_H3cWIPSDctUnassocStaEntry_Object=MibTableRow
h3cWIPSDctUnassocStaEntry=_H3cWIPSDctUnassocStaEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1))
h3cWIPSDctUnassocStaEntry.setIndexNames((0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaEntry.setStatus(_A)
class _H3cWIPSDctUnassocStaVSD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cWIPSDctUnassocStaVSD_Type.__name__=_H
_H3cWIPSDctUnassocStaVSD_Object=MibTableColumn
h3cWIPSDctUnassocStaVSD=_H3cWIPSDctUnassocStaVSD_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,1),_H3cWIPSDctUnassocStaVSD_Type())
h3cWIPSDctUnassocStaVSD.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaVSD.setStatus(_A)
_H3cWIPSDctUnassocStaMac_Type=MacAddress
_H3cWIPSDctUnassocStaMac_Object=MibTableColumn
h3cWIPSDctUnassocStaMac=_H3cWIPSDctUnassocStaMac_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,2),_H3cWIPSDctUnassocStaMac_Type())
h3cWIPSDctUnassocStaMac.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaMac.setStatus(_A)
_H3cWIPSDctUnassocStaCategory_Type=H3cWIPSClientCategoryType
_H3cWIPSDctUnassocStaCategory_Object=MibTableColumn
h3cWIPSDctUnassocStaCategory=_H3cWIPSDctUnassocStaCategory_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,3),_H3cWIPSDctUnassocStaCategory_Type())
h3cWIPSDctUnassocStaCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaCategory.setStatus(_A)
_H3cWIPSDctUnassocStaRadioType_Type=Unsigned32
_H3cWIPSDctUnassocStaRadioType_Object=MibTableColumn
h3cWIPSDctUnassocStaRadioType=_H3cWIPSDctUnassocStaRadioType_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,4),_H3cWIPSDctUnassocStaRadioType_Type())
h3cWIPSDctUnassocStaRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaRadioType.setStatus(_A)
_H3cWIPSDctUnassocStaIsCountered_Type=TruthValue
_H3cWIPSDctUnassocStaIsCountered_Object=MibTableColumn
h3cWIPSDctUnassocStaIsCountered=_H3cWIPSDctUnassocStaIsCountered_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,5),_H3cWIPSDctUnassocStaIsCountered_Type())
h3cWIPSDctUnassocStaIsCountered.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaIsCountered.setStatus(_A)
class _H3cWIPSDctUnassocStaAdd2BlackList_Type(TruthValue):defaultValue=2
_H3cWIPSDctUnassocStaAdd2BlackList_Type.__name__=_K
_H3cWIPSDctUnassocStaAdd2BlackList_Object=MibTableColumn
h3cWIPSDctUnassocStaAdd2BlackList=_H3cWIPSDctUnassocStaAdd2BlackList_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,6),_H3cWIPSDctUnassocStaAdd2BlackList_Type())
h3cWIPSDctUnassocStaAdd2BlackList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaAdd2BlackList.setStatus(_A)
class _H3cWIPSDctUnassocStaAdd2WhiteList_Type(TruthValue):defaultValue=2
_H3cWIPSDctUnassocStaAdd2WhiteList_Type.__name__=_K
_H3cWIPSDctUnassocStaAdd2WhiteList_Object=MibTableColumn
h3cWIPSDctUnassocStaAdd2WhiteList=_H3cWIPSDctUnassocStaAdd2WhiteList_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,7),_H3cWIPSDctUnassocStaAdd2WhiteList_Type())
h3cWIPSDctUnassocStaAdd2WhiteList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaAdd2WhiteList.setStatus(_A)
class _H3cWIPSDctUnassocStaAdd2IgnoreList_Type(TruthValue):defaultValue=2
_H3cWIPSDctUnassocStaAdd2IgnoreList_Type.__name__=_K
_H3cWIPSDctUnassocStaAdd2IgnoreList_Object=MibTableColumn
h3cWIPSDctUnassocStaAdd2IgnoreList=_H3cWIPSDctUnassocStaAdd2IgnoreList_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,8),_H3cWIPSDctUnassocStaAdd2IgnoreList_Type())
h3cWIPSDctUnassocStaAdd2IgnoreList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaAdd2IgnoreList.setStatus(_A)
class _H3cWIPSDctUnassocStaAdd2CtmList_Type(TruthValue):defaultValue=2
_H3cWIPSDctUnassocStaAdd2CtmList_Type.__name__=_K
_H3cWIPSDctUnassocStaAdd2CtmList_Object=MibTableColumn
h3cWIPSDctUnassocStaAdd2CtmList=_H3cWIPSDctUnassocStaAdd2CtmList_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,9),_H3cWIPSDctUnassocStaAdd2CtmList_Type())
h3cWIPSDctUnassocStaAdd2CtmList.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaAdd2CtmList.setStatus(_A)
_H3cWIPSDctUnassocStaFirstDctTm_Type=TimeTicks
_H3cWIPSDctUnassocStaFirstDctTm_Object=MibTableColumn
h3cWIPSDctUnassocStaFirstDctTm=_H3cWIPSDctUnassocStaFirstDctTm_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,10),_H3cWIPSDctUnassocStaFirstDctTm_Type())
h3cWIPSDctUnassocStaFirstDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaFirstDctTm.setStatus(_A)
_H3cWIPSDctUnassocStaLastDctTm_Type=TimeTicks
_H3cWIPSDctUnassocStaLastDctTm_Object=MibTableColumn
h3cWIPSDctUnassocStaLastDctTm=_H3cWIPSDctUnassocStaLastDctTm_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,11),_H3cWIPSDctUnassocStaLastDctTm_Type())
h3cWIPSDctUnassocStaLastDctTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaLastDctTm.setStatus(_A)
_H3cWIPSDctUnassocStaRptSensorNum_Type=Integer32
_H3cWIPSDctUnassocStaRptSensorNum_Object=MibTableColumn
h3cWIPSDctUnassocStaRptSensorNum=_H3cWIPSDctUnassocStaRptSensorNum_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,12),_H3cWIPSDctUnassocStaRptSensorNum_Type())
h3cWIPSDctUnassocStaRptSensorNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaRptSensorNum.setStatus(_A)
class _H3cWIPSDctUnassocStaState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_AF,1),(_AG,2),(_AH,3),(_AI,4),(_AJ,5),(_AK,6),(_AL,7)))
_H3cWIPSDctUnassocStaState_Type.__name__=_F
_H3cWIPSDctUnassocStaState_Object=MibTableColumn
h3cWIPSDctUnassocStaState=_H3cWIPSDctUnassocStaState_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,13),_H3cWIPSDctUnassocStaState_Type())
h3cWIPSDctUnassocStaState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaState.setStatus(_A)
class _H3cWIPSDctUnassocStaVendor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cWIPSDctUnassocStaVendor_Type.__name__=_H
_H3cWIPSDctUnassocStaVendor_Object=MibTableColumn
h3cWIPSDctUnassocStaVendor=_H3cWIPSDctUnassocStaVendor_Object((1,3,6,1,4,1,2011,10,2,118,2,17,1,14),_H3cWIPSDctUnassocStaVendor_Type())
h3cWIPSDctUnassocStaVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaVendor.setStatus(_A)
_H3cWIPSDctUnassocStaRptSensorTable_Object=MibTable
h3cWIPSDctUnassocStaRptSensorTable=_H3cWIPSDctUnassocStaRptSensorTable_Object((1,3,6,1,4,1,2011,10,2,118,2,18))
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaRptSensorTable.setStatus(_A)
_H3cWIPSDctUnassocStaRptSensorEntry_Object=MibTableRow
h3cWIPSDctUnassocStaRptSensorEntry=_H3cWIPSDctUnassocStaRptSensorEntry_Object((1,3,6,1,4,1,2011,10,2,118,2,18,1))
h3cWIPSDctUnassocStaRptSensorEntry.setIndexNames((0,_E,_g),(0,_E,_h),(0,_E,_Ac))
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaRptSensorEntry.setStatus(_A)
class _H3cWIPSDctUnassocStaRtpSensorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cWIPSDctUnassocStaRtpSensorName_Type.__name__=_H
_H3cWIPSDctUnassocStaRtpSensorName_Object=MibTableColumn
h3cWIPSDctUnassocStaRtpSensorName=_H3cWIPSDctUnassocStaRtpSensorName_Object((1,3,6,1,4,1,2011,10,2,118,2,18,1,1),_H3cWIPSDctUnassocStaRtpSensorName_Type())
h3cWIPSDctUnassocStaRtpSensorName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaRtpSensorName.setStatus(_A)
class _H3cWIPSDctUnassocStaRptSensorRadioId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_H3cWIPSDctUnassocStaRptSensorRadioId_Type.__name__=_F
_H3cWIPSDctUnassocStaRptSensorRadioId_Object=MibTableColumn
h3cWIPSDctUnassocStaRptSensorRadioId=_H3cWIPSDctUnassocStaRptSensorRadioId_Object((1,3,6,1,4,1,2011,10,2,118,2,18,1,2),_H3cWIPSDctUnassocStaRptSensorRadioId_Type())
h3cWIPSDctUnassocStaRptSensorRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaRptSensorRadioId.setStatus(_A)
_H3cWIPSDctUnassocStaRptRSSI_Type=Integer32
_H3cWIPSDctUnassocStaRptRSSI_Object=MibTableColumn
h3cWIPSDctUnassocStaRptRSSI=_H3cWIPSDctUnassocStaRptRSSI_Object((1,3,6,1,4,1,2011,10,2,118,2,18,1,3),_H3cWIPSDctUnassocStaRptRSSI_Type())
h3cWIPSDctUnassocStaRptRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaRptRSSI.setStatus(_A)
_H3cWIPSDctUnassocStaLastRptTm_Type=TimeTicks
_H3cWIPSDctUnassocStaLastRptTm_Object=MibTableColumn
h3cWIPSDctUnassocStaLastRptTm=_H3cWIPSDctUnassocStaLastRptTm_Object((1,3,6,1,4,1,2011,10,2,118,2,18,1,4),_H3cWIPSDctUnassocStaLastRptTm_Type())
h3cWIPSDctUnassocStaLastRptTm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cWIPSDctUnassocStaLastRptTm.setStatus(_A)
_H3cWIPSNotifyGroup_ObjectIdentity=ObjectIdentity
h3cWIPSNotifyGroup=_H3cWIPSNotifyGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,118,3))
mibBuilder.exportSymbols(_E,**{'H3cWIPSRadioType':H3cWIPSRadioType,'H3cWIPSDevStatus':H3cWIPSDevStatus,_AC:H3cWIPSDevCategoryWay,'H3cWIPSDeviceCategoryType':H3cWIPSDeviceCategoryType,'H3cWIPSAPCategoryType':H3cWIPSAPCategoryType,'H3cWIPSClientCategoryType':H3cWIPSClientCategoryType,'H3cWIPSChannel':H3cWIPSChannel,'H3cWIPSEncryptMethod':H3cWIPSEncryptMethod,'H3cWIPSAuthMethod':H3cWIPSAuthMethod,'H3cWIPSAPClassifyType':H3cWIPSAPClassifyType,_y:H3cWIPSAPSecurityType,'h3cWIPS':h3cWIPS,'h3cWIPSConfigGroup':h3cWIPSConfigGroup,'h3cWIPSGlobalConfigGroup':h3cWIPSGlobalConfigGroup,'h3cWIPSEnable':h3cWIPSEnable,'h3cWIPSSensorLicenseNum':h3cWIPSSensorLicenseNum,'h3cWIPSBlocklistAction':h3cWIPSBlocklistAction,'h3cWIPSAPInactiveTime':h3cWIPSAPInactiveTime,'h3cWIPSSTAInactiveTime':h3cWIPSSTAInactiveTime,'h3cWIPSDevAgingTime':h3cWIPSDevAgingTime,'h3cWIPSStatisticPeriod':h3cWIPSStatisticPeriod,'h3cWIPSReclassificationPeriod':h3cWIPSReclassificationPeriod,'h3cWIPSResetAllTrustList':h3cWIPSResetAllTrustList,'h3cWIPSResetAllBlockList':h3cWIPSResetAllBlockList,'h3cWIPSResetAllIgnoreList':h3cWIPSResetAllIgnoreList,'h3cWIPSResetAllCtmList':h3cWIPSResetAllCtmList,'h3cWIPSPermitChlBitMap':h3cWIPSPermitChlBitMap,'h3cWIPSDynamicTrustListAgingTime':h3cWIPSDynamicTrustListAgingTime,'h3cWIPSDevUpdateTime':h3cWIPSDevUpdateTime,'h3cWIPSADOSEnable':h3cWIPSADOSEnable,'h3cWIPSAccessFlowScanEnable':h3cWIPSAccessFlowScanEnable,'h3cWIPSVsdConfigGroup':h3cWIPSVsdConfigGroup,'h3cWIPSVsdTable':h3cWIPSVsdTable,'h3cWIPSVsdEntry':h3cWIPSVsdEntry,_N:h3cWIPSVsdNameCfg,'h3cWIPSVsdRowStatus':h3cWIPSVsdRowStatus,'h3cWIPSVsdAtkDctPolicyNameCfg':h3cWIPSVsdAtkDctPolicyNameCfg,'h3cWIPSVsdCtmPolicyNameCfg':h3cWIPSVsdCtmPolicyNameCfg,'h3cWIPSVsdSigPolicyNameCfg':h3cWIPSVsdSigPolicyNameCfg,'h3cWIPSVsdMalPktPolicyNameCfg':h3cWIPSVsdMalPktPolicyNameCfg,'h3cWIPSRule2VsdTable':h3cWIPSRule2VsdTable,'h3cWIPSRule2VsdEntry':h3cWIPSRule2VsdEntry,_p:h3cWIPSRule2VsdAPClaRuleNameCfg,'h3cWIPSRule2VsdRowStatus':h3cWIPSRule2VsdRowStatus,'h3cWIPSRule2VsdPrecedence':h3cWIPSRule2VsdPrecedence,'h3cWIPSSensor2VsdTable':h3cWIPSSensor2VsdTable,'h3cWIPSSensor2VsdEntry':h3cWIPSSensor2VsdEntry,_V:h3cWIPSSensorNameCfg,'h3cWIPSSensor2VsdRowStatus':h3cWIPSSensor2VsdRowStatus,'h3cWIPSSensorState':h3cWIPSSensorState,'h3cWIPSSensorRadioTable':h3cWIPSSensorRadioTable,'h3cWIPSSensorRadioEntry':h3cWIPSSensorRadioEntry,_q:h3cWIPSSensorRadioRadioId,'h3cWIPSSensorRadioScanMode':h3cWIPSSensorRadioScanMode,'h3cWIPSAPClaRuleTable':h3cWIPSAPClaRuleTable,'h3cWIPSAPClaRuleEntry':h3cWIPSAPClaRuleEntry,_v:h3cWIPSAPClaRuleName,'h3cWIPSAPClaRowStatus':h3cWIPSAPClaRowStatus,'h3cWIPSAPClaSeverityLevel':h3cWIPSAPClaSeverityLevel,'h3cWIPSAPClaRuleMatchAll':h3cWIPSAPClaRuleMatchAll,'h3cWIPSAPClaType':h3cWIPSAPClaType,'h3cWIPSAPClaSubRuleSSIDOperator':h3cWIPSAPClaSubRuleSSIDOperator,'h3cWIPSAPClaSubRuleSSIDCase':h3cWIPSAPClaSubRuleSSIDCase,'h3cWIPSAPClaSubRuleSSID':h3cWIPSAPClaSubRuleSSID,'h3cWIPSSecurityType':h3cWIPSSecurityType,'h3cWIPSSecurityTypeMatch':h3cWIPSSecurityTypeMatch,'h3cWIPSAPAuthType':h3cWIPSAPAuthType,'h3cWIPSMaxRSSIValue':h3cWIPSMaxRSSIValue,'h3cWIPSMinRSSIValue':h3cWIPSMinRSSIValue,'h3cWIPSMaxDuration':h3cWIPSMaxDuration,'h3cWIPSMinDuration':h3cWIPSMinDuration,'h3cWIPSMaxAPNum':h3cWIPSMaxAPNum,'h3cWIPSMinAPNum':h3cWIPSMinAPNum,'h3cWIPSMaxClientNum':h3cWIPSMaxClientNum,'h3cWIPSMinClientNum':h3cWIPSMinClientNum,'h3cWIPSOUIInfo':h3cWIPSOUIInfo,'h3cWIPSVendorInfo':h3cWIPSVendorInfo,'h3cWIPSAPAuthTypeMatch':h3cWIPSAPAuthTypeMatch,'h3cWIPSAtkDctPolicyCfgGroup':h3cWIPSAtkDctPolicyCfgGroup,'h3cWIPSAtkDctPolicyCfgSupportSet':h3cWIPSAtkDctPolicyCfgSupportSet,'h3cWIPSAtkDctPolicyCfgTable':h3cWIPSAtkDctPolicyCfgTable,'h3cWIPSAtkDctPolicyCfgEntry':h3cWIPSAtkDctPolicyCfgEntry,_z:h3cWIPSAtkDctPolicyName,'h3cWIPSAtkDctPolicyCfgRowStatus':h3cWIPSAtkDctPolicyCfgRowStatus,'h3cWIPSAtkDctPolicyBitString':h3cWIPSAtkDctPolicyBitString,'h3cWIPSAtkDctPolicyAPFloodQT':h3cWIPSAtkDctPolicyAPFloodQT,'h3cWIPSAtkDctPolicyAPSpoofQT':h3cWIPSAtkDctPolicyAPSpoofQT,'h3cWIPSAtkDctPolicyCliSpoofQT':h3cWIPSAtkDctPolicyCliSpoofQT,'h3cWIPSAtkDctPolicyDosAssoQT':h3cWIPSAtkDctPolicyDosAssoQT,'h3cWIPSAtkDctPolicyDosAuthQT':h3cWIPSAtkDctPolicyDosAuthQT,'h3cWIPSAtkDctPolicyDosEAPOLStartQT':h3cWIPSAtkDctPolicyDosEAPOLStartQT,'h3cWIPSAtkDctPolicyDosReAssoQT':h3cWIPSAtkDctPolicyDosReAssoQT,'h3cWIPSAtkDctPolicyWeakIVQT':h3cWIPSAtkDctPolicyWeakIVQT,'h3cWIPSAtkDctPolicyInvalidOUIAction':h3cWIPSAtkDctPolicyInvalidOUIAction,'h3cWIPSAtkDctPolicyUnencryptedAuthApQT':h3cWIPSAtkDctPolicyUnencryptedAuthApQT,'h3cWIPSAtkDctPolicyUnencryptedAuthClientQT':h3cWIPSAtkDctPolicyUnencryptedAuthClientQT,'h3cWIPSAtkDctPolicyPSAttackQT':h3cWIPSAtkDctPolicyPSAttackQT,'h3cWIPSAtkDctPolicyPSAttackMinOffPacket':h3cWIPSAtkDctPolicyPSAttackMinOffPacket,'h3cWIPSAtkDctPolicyPSAttackOnOffPercent':h3cWIPSAtkDctPolicyPSAttackOnOffPercent,'h3cWIPSAtkDctPolicyApImpersonationQT':h3cWIPSAtkDctPolicyApImpersonationQT,'h3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold':h3cWIPSAtkDctPolicyApImpersonationBeaconIncThreshold,'h3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime':h3cWIPSAtkDctPolicyApImpersonationBeaconIncWaitTime,'h3cWIPSAtkDctPolicySoftApConvertTime':h3cWIPSAtkDctPolicySoftApConvertTime,'h3cWIPSStaticCtmListCfgTable':h3cWIPSStaticCtmListCfgTable,'h3cWIPSStaticCtmListCfgEntry':h3cWIPSStaticCtmListCfgEntry,_A0:h3cWIPSStaticCtmListMAC,'h3cWIPSStaticCtmListRowStatus':h3cWIPSStaticCtmListRowStatus,'h3cWIPSStaticBlockListCfgTable':h3cWIPSStaticBlockListCfgTable,'h3cWIPSStaticBlockListCfgEntry':h3cWIPSStaticBlockListCfgEntry,_A1:h3cWIPSStaticBlockListMAC,'h3cWIPSStaticBlockListRowStatus':h3cWIPSStaticBlockListRowStatus,'h3cWIPSStaticTrustListCfgTable':h3cWIPSStaticTrustListCfgTable,'h3cWIPSStaticTrustListCfgEntry':h3cWIPSStaticTrustListCfgEntry,_A2:h3cWIPSStaticTrustListMAC,'h3cWIPSStaticTrustListRowStatus':h3cWIPSStaticTrustListRowStatus,'h3cWIPSIgnoreListCfgTable':h3cWIPSIgnoreListCfgTable,'h3cWIPSIgnoreListCfgEntry':h3cWIPSIgnoreListCfgEntry,_A3:h3cWIPSIgnoreListMAC,'h3cWIPSIgnoreListRowStatus':h3cWIPSIgnoreListRowStatus,'h3cWIPSDctModeTable':h3cWIPSDctModeTable,'h3cWIPSDctModeEntry':h3cWIPSDctModeEntry,_A4:h3cWIPSDctModeAPName,_A5:h3cWIPSDctModeRadio,'h3cWIPSDctModeScanMode':h3cWIPSDctModeScanMode,'h3cWIPSDctModeRowStatus':h3cWIPSDctModeRowStatus,'h3cWIPSSigConfigGroup':h3cWIPSSigConfigGroup,'h3cWIPSSigPolicyTable':h3cWIPSSigPolicyTable,'h3cWIPSSigPolicyEntry':h3cWIPSSigPolicyEntry,_W:h3cWIPSSigPolicyNameCfg,'h3cWIPSSigPolicyRowStatus':h3cWIPSSigPolicyRowStatus,'h3cWIPSSigRule2PolicyTable':h3cWIPSSigRule2PolicyTable,'h3cWIPSSigRule2PolicyEntry':h3cWIPSSigRule2PolicyEntry,_A6:h3cWIPSSigRule2PolicySigRuleIDCfg,'h3cWIPSSigRule2PolicyRowStatus':h3cWIPSSigRule2PolicyRowStatus,'h3cWIPSSigRule2PolicyPrecedence':h3cWIPSSigRule2PolicyPrecedence,'h3cWIPSSigRuleTable':h3cWIPSSigRuleTable,'h3cWIPSSigRuleEntry':h3cWIPSSigRuleEntry,_X:h3cWIPSSigRuleName,'h3cWIPSSigRuleID':h3cWIPSSigRuleID,'h3cWIPSSigRuleRowStatus':h3cWIPSSigRuleRowStatus,'h3cWIPSSigSubRuleMatchAll':h3cWIPSSigSubRuleMatchAll,'h3cWIPSSigRuleDctPeriod':h3cWIPSSigRuleDctPeriod,'h3cWIPSSigRuleTrackMethod':h3cWIPSSigRuleTrackMethod,'h3cWIPSSigRuleDctThresholdPerMAC':h3cWIPSSigRuleDctThresholdPerMAC,'h3cWIPSSigRuleDctThresholdPerSig':h3cWIPSSigRuleDctThresholdPerSig,'h3cWIPSSigRuleActionEvtLevel':h3cWIPSSigRuleActionEvtLevel,'h3cWIPSSigRuleQuietTime':h3cWIPSSigRuleQuietTime,'h3cWIPSSigSubRuleFrameType':h3cWIPSSigSubRuleFrameType,'h3cWIPSSigSubRuleFrameSubType':h3cWIPSSigSubRuleFrameSubType,'h3cWIPSSigSubRuleMac':h3cWIPSSigSubRuleMac,'h3cWIPSSigSubRuleMacType':h3cWIPSSigSubRuleMacType,'h3cWIPSSigSubRuleSeqNumMin':h3cWIPSSigSubRuleSeqNumMin,'h3cWIPSSigSubRuleSeqNumMax':h3cWIPSSigSubRuleSeqNumMax,'h3cWIPSSigSubRuleSSIDLenMin':h3cWIPSSigSubRuleSSIDLenMin,'h3cWIPSSigSubRuleSSIDLenMax':h3cWIPSSigSubRuleSSIDLenMax,'h3cWIPSSigSubRuleSSID':h3cWIPSSigSubRuleSSID,'h3cWIPSSigSubRuleSSIDOpe':h3cWIPSSigSubRuleSSIDOpe,'h3cWIPSSigSubRuleSSIDCase':h3cWIPSSigSubRuleSSIDCase,'h3cWIPSSigSubRulePatternTable':h3cWIPSSigSubRulePatternTable,'h3cWIPSSigSubRulePatternEntry':h3cWIPSSigSubRulePatternEntry,_A7:h3cWIPSSigSubRulePatternID,'h3cWIPSSigSubRuleRowStatus':h3cWIPSSigSubRuleRowStatus,'h3cWIPSSigSubRulePatternName':h3cWIPSSigSubRulePatternName,'h3cWIPSSigSubRulePatternOffset':h3cWIPSSigSubRulePatternOffset,'h3cWIPSSigSubRulePatternMask':h3cWIPSSigSubRulePatternMask,'h3cWIPSSigSubRulePatternValueMin':h3cWIPSSigSubRulePatternValueMin,'h3cWIPSSigSubRulePatternValueMax':h3cWIPSSigSubRulePatternValueMax,'h3cWIPSSigSubRulePatternFromPayload':h3cWIPSSigSubRulePatternFromPayload,'h3cWIPSCtmConfigGroup':h3cWIPSCtmConfigGroup,'h3cWIPSCtmPolicyCfgSupportSet':h3cWIPSCtmPolicyCfgSupportSet,'h3cWIPSCtmPolicyTable':h3cWIPSCtmPolicyTable,'h3cWIPSCtmPolicyEntry':h3cWIPSCtmPolicyEntry,_Y:h3cWIPSCtmPolicyName,'h3cWIPSCtmPolicyCfgRowStatus':h3cWIPSCtmPolicyCfgRowStatus,'h3cWIPSCtmPolicyBitString':h3cWIPSCtmPolicyBitString,'h3cWIPSCtmPolicyFixedChl':h3cWIPSCtmPolicyFixedChl,'h3cWIPSCtmPolicyRogueAPPre':h3cWIPSCtmPolicyRogueAPPre,'h3cWIPSCtmPolicyPtRogueAPPre':h3cWIPSCtmPolicyPtRogueAPPre,'h3cWIPSCtmPolicyMisconfAPPre':h3cWIPSCtmPolicyMisconfAPPre,'h3cWIPSCtmPolicyExternalAPPre':h3cWIPSCtmPolicyExternalAPPre,'h3cWIPSCtmPolicyPtExternalAPPre':h3cWIPSCtmPolicyPtExternalAPPre,'h3cWIPSCtmPolicyUncateAPPre':h3cWIPSCtmPolicyUncateAPPre,'h3cWIPSCtmPolicyPtAuthAPPre':h3cWIPSCtmPolicyPtAuthAPPre,'h3cWIPSCtmPolicyMisassoStaPre':h3cWIPSCtmPolicyMisassoStaPre,'h3cWIPSCtmPolicyUncateStaPre':h3cWIPSCtmPolicyUncateStaPre,'h3cWIPSCtmPolicyUnauthStaPre':h3cWIPSCtmPolicyUnauthStaPre,'h3cWIPSCtmPolicyDevListTable':h3cWIPSCtmPolicyDevListTable,'h3cWIPSCtmPolicyDevListEntry':h3cWIPSCtmPolicyDevListEntry,_A8:h3cWIPSCtmPolicyDevMAC,'h3cWIPSCtmPolicyDevRowStatus':h3cWIPSCtmPolicyDevRowStatus,'h3cWIPSMalPktDctConfigGroup':h3cWIPSMalPktDctConfigGroup,'h3cWIPSMalPktDctCfgLogSupportSet':h3cWIPSMalPktDctCfgLogSupportSet,'h3cWIPSMalPktDctCfgTrapSupportSet':h3cWIPSMalPktDctCfgTrapSupportSet,'h3cWIPSMalPktDctPolicyTable':h3cWIPSMalPktDctPolicyTable,'h3cWIPSMalPktDctPolicyEntry':h3cWIPSMalPktDctPolicyEntry,_A9:h3cWIPSMalPktDctPolicyName,'h3cWIPSMalPktDctPolicyCfgRowStatus':h3cWIPSMalPktDctPolicyCfgRowStatus,'h3cWIPSMalPktDctPolicyLogBitString':h3cWIPSMalPktDctPolicyLogBitString,'h3cWIPSMalPktDctPolicyTrapBitString':h3cWIPSMalPktDctPolicyTrapBitString,'h3cWIPSMalPktDctPolicyDurationThreshold':h3cWIPSMalPktDctPolicyDurationThreshold,'h3cWIPSMalPktDctPolicyQuietTime':h3cWIPSMalPktDctPolicyQuietTime,'h3cWIPSStaticTrustOUIListCfgTable':h3cWIPSStaticTrustOUIListCfgTable,'h3cWIPSStaticTrustOUIListCfgEntry':h3cWIPSStaticTrustOUIListCfgEntry,_AA:h3cWIPSStaticTrustOUIListOUI,'h3cWIPSStaticTrustOUIListRowStatus':h3cWIPSStaticTrustOUIListRowStatus,'h3cWIPSStaticTrustVendorListCfgTable':h3cWIPSStaticTrustVendorListCfgTable,'h3cWIPSStaticTrustVendorListCfgEntry':h3cWIPSStaticTrustVendorListCfgEntry,_AB:h3cWIPSStaticTrustVendorListVendor,'h3cWIPSStaticTrustVendorListRowStatus':h3cWIPSStaticTrustVendorListRowStatus,'h3cWIPSDetectGroup':h3cWIPSDetectGroup,'h3cWIPSDctAPTable':h3cWIPSDctAPTable,'h3cWIPSDctAPEntry':h3cWIPSDctAPEntry,_Q:h3cWIPSDctAPVSD,_R:h3cWIPSDctAPBSSID,'h3cWIPSDctAPRunningTime':h3cWIPSDctAPRunningTime,'h3cWIPSDctAPRunTmLastUpdateTm':h3cWIPSDctAPRunTmLastUpdateTm,'h3cWIPSDctAPIsCountered':h3cWIPSDctAPIsCountered,'h3cWIPSDctAPWorkChannel':h3cWIPSDctAPWorkChannel,'h3cWIPSDctAPRadioType':h3cWIPSDctAPRadioType,'h3cWIPSDctAPAuthMethod':h3cWIPSDctAPAuthMethod,'h3cWIPSDctAPEncryptMethod':h3cWIPSDctAPEncryptMethod,'h3cWIPSDctAPSecurity':h3cWIPSDctAPSecurity,'h3cWIPSDctAPSeverityLevel':h3cWIPSDctAPSeverityLevel,'h3cWIPSDctAPLastDctTm':h3cWIPSDctAPLastDctTm,'h3cWIPSDctAPFirstDctTm':h3cWIPSDctAPFirstDctTm,'h3cWIPSDctAPAdd2BlackList':h3cWIPSDctAPAdd2BlackList,'h3cWIPSDctAPAdd2WhiteList':h3cWIPSDctAPAdd2WhiteList,'h3cWIPSDctAPAdd2IgnoreList':h3cWIPSDctAPAdd2IgnoreList,'h3cWIPSDctAPAdd2CtmList':h3cWIPSDctAPAdd2CtmList,'h3cWIPSDctAPCategory':h3cWIPSDctAPCategory,'h3cWIPSDctAPCategoryWay':h3cWIPSDctAPCategoryWay,'h3cWIPSDctAPStatus':h3cWIPSDctAPStatus,'h3cWIPSDctAPSSID':h3cWIPSDctAPSSID,'h3cWIPSDctAPAttachStaNum':h3cWIPSDctAPAttachStaNum,'h3cWIPSDctAPRptSensorNum':h3cWIPSDctAPRptSensorNum,'h3cWIPSDctAPVendor':h3cWIPSDctAPVendor,'h3cWIPSDctAPAttachStaTable':h3cWIPSDctAPAttachStaTable,'h3cWIPSDctAPAttachStaEntry':h3cWIPSDctAPAttachStaEntry,_AD:h3cWIPSDctAPAttachStaMac,'h3cWIPSDctAPAttachStaRowStatus':h3cWIPSDctAPAttachStaRowStatus,'h3cWIPSDctAPRptSensorTable':h3cWIPSDctAPRptSensorTable,'h3cWIPSDctAPRptSensorEntry':h3cWIPSDctAPRptSensorEntry,_AE:h3cWIPSDctAPRptSensorName,'h3cWIPSDctAPRptSensorRadioId':h3cWIPSDctAPRptSensorRadioId,'h3cWIPSDctAPRptRSSI':h3cWIPSDctAPRptRSSI,'h3cWIPSDctAPLastRptTm':h3cWIPSDctAPLastRptTm,'h3cWIPSDctStaTable':h3cWIPSDctStaTable,'h3cWIPSDctStaEntry':h3cWIPSDctStaEntry,_Z:h3cWIPSDctStaVSD,_a:h3cWIPSDctStaMac,'h3cWIPSDctStaAssocBSSID':h3cWIPSDctStaAssocBSSID,'h3cWIPSDctStaStatus':h3cWIPSDctStaStatus,'h3cWIPSDctStaCategory':h3cWIPSDctStaCategory,'h3cWIPSDctStaRadioType':h3cWIPSDctStaRadioType,'h3cWIPSDctStaWorkChannel':h3cWIPSDctStaWorkChannel,'h3cWIPSDctStaIsCountered':h3cWIPSDctStaIsCountered,'h3cWIPSDctStaAdd2BlackList':h3cWIPSDctStaAdd2BlackList,'h3cWIPSDctStaAdd2WhiteList':h3cWIPSDctStaAdd2WhiteList,'h3cWIPSDctStaAdd2IgnoreList':h3cWIPSDctStaAdd2IgnoreList,'h3cWIPSDctStaAdd2CtmList':h3cWIPSDctStaAdd2CtmList,'h3cWIPSDctStaFirstDctTm':h3cWIPSDctStaFirstDctTm,'h3cWIPSDctStaLastDctTm':h3cWIPSDctStaLastDctTm,'h3cWIPSDctStaRptSensorNum':h3cWIPSDctStaRptSensorNum,'h3cWIPSDctStaState':h3cWIPSDctStaState,'h3cWIPSDctStaVendor':h3cWIPSDctStaVendor,'h3cWIPSDctStaRptSensorTable':h3cWIPSDctStaRptSensorTable,'h3cWIPSDctStaRptSensorEntry':h3cWIPSDctStaRptSensorEntry,_AM:h3cWIPSDctStaRtpSensorName,'h3cWIPSDctStaRptSensorRadioId':h3cWIPSDctStaRptSensorRadioId,'h3cWIPSDctStaRptRSSI':h3cWIPSDctStaRptRSSI,'h3cWIPSDctStaLastRptTm':h3cWIPSDctStaLastRptTm,'h3cWIPSDctSSIDTable':h3cWIPSDctSSIDTable,'h3cWIPSDctSSIDEntry':h3cWIPSDctSSIDEntry,_b:h3cWIPSDctNetworkVSD,_c:h3cWIPSDctNetworkSSID,_d:h3cWIPSDctNetworkCfg,'h3cWIPSDctNetworkFirstRptTm':h3cWIPSDctNetworkFirstRptTm,'h3cWIPSDctNetworkLastRptTm':h3cWIPSDctNetworkLastRptTm,'h3cWIPSDctNetworkStatus':h3cWIPSDctNetworkStatus,'h3cWIPSDctNetworkSSIDHide':h3cWIPSDctNetworkSSIDHide,'h3cWIPSDctNetworkBSSNum':h3cWIPSDctNetworkBSSNum,'h3cWIPSDctSSIDBSSTable':h3cWIPSDctSSIDBSSTable,'h3cWIPSDctSSIDBSSEntry':h3cWIPSDctSSIDBSSEntry,_AN:h3cWIPSDctNetworkBSSID,'h3cWIPSDctNetworkBSSWorkChl':h3cWIPSDctNetworkBSSWorkChl,'h3cWIPSDctNetworkBSSStaNum':h3cWIPSDctNetworkBSSStaNum,'h3cWIPSBlockListTable':h3cWIPSBlockListTable,'h3cWIPSBlockListEntry':h3cWIPSBlockListEntry,_AO:h3cWIPSBlockListMacAddress,'h3cWIPSBlockListStatus':h3cWIPSBlockListStatus,'h3cWIPSChannelTable':h3cWIPSChannelTable,'h3cWIPSChannelEntry':h3cWIPSChannelEntry,_AQ:h3cWIPSChannelNum,'h3cWIPSChannelRadioType':h3cWIPSChannelRadioType,'h3cWIPSChannelIsPermitted':h3cWIPSChannelIsPermitted,'h3cWIPSChannelLastRptTm':h3cWIPSChannelLastRptTm,'h3cWIPSCountermeasureListTable':h3cWIPSCountermeasureListTable,'h3cWIPSCountermeasureListEntry':h3cWIPSCountermeasureListEntry,_AR:h3cWIPSCtmListMacAddress,'h3cWIPSCtmListLastestWorkChl':h3cWIPSCtmListLastestWorkChl,'h3cWIPSCtmListFirstTm':h3cWIPSCtmListFirstTm,'h3cWIPSCtmListLastTm':h3cWIPSCtmListLastTm,'h3cWIPSCtmListQurCnt':h3cWIPSCtmListQurCnt,'h3cWIPSCtmListSensorNum':h3cWIPSCtmListSensorNum,'h3cWIPSIgnoreListTable':h3cWIPSIgnoreListTable,'h3cWIPSIgnoreListEntry':h3cWIPSIgnoreListEntry,_AS:h3cWIPSIgnoreListMacAddress,'h3cWIPSIgnoreListFirstIgnoreTm':h3cWIPSIgnoreListFirstIgnoreTm,'h3cWIPSIgnoreListLastIgnoreTm':h3cWIPSIgnoreListLastIgnoreTm,'h3cWIPSIgnoreListIgnoreCnt':h3cWIPSIgnoreListIgnoreCnt,'h3cWIPSTrustListTable':h3cWIPSTrustListTable,'h3cWIPSTrustListEntry':h3cWIPSTrustListEntry,_AT:h3cWIPSTrustListMacAddress,'h3cWIPSTrustListStatus':h3cWIPSTrustListStatus,'h3cWIPSChlStatTable':h3cWIPSChlStatTable,'h3cWIPSChlStatEntry':h3cWIPSChlStatEntry,_AU:h3cWIPSChlStatSensorMacAddr,_AV:h3cWIPSChlStatChannel,'h3cWIPSChlStatTotalPkt':h3cWIPSChlStatTotalPkt,'h3cWIPSChlStatTotalByte':h3cWIPSChlStatTotalByte,'h3cWIPSChlStatBmcastPkt':h3cWIPSChlStatBmcastPkt,'h3cWIPSChlStatBmcastByte':h3cWIPSChlStatBmcastByte,'h3cWIPSChlStatUnicastPkt':h3cWIPSChlStatUnicastPkt,'h3cWIPSChlStatUnicastByte':h3cWIPSChlStatUnicastByte,'h3cWIPSChlStatManagement':h3cWIPSChlStatManagement,'h3cWIPSChlStatControl':h3cWIPSChlStatControl,'h3cWIPSChlStatData':h3cWIPSChlStatData,'h3cWIPSChlStatBeacon':h3cWIPSChlStatBeacon,'h3cWIPSChlStatRTS':h3cWIPSChlStatRTS,'h3cWIPSChlStatCTS':h3cWIPSChlStatCTS,'h3cWIPSChlStatProbeRequest':h3cWIPSChlStatProbeRequest,'h3cWIPSChlStatProbeResponse':h3cWIPSChlStatProbeResponse,'h3cWIPSChlStatFragment':h3cWIPSChlStatFragment,'h3cWIPSChlStatRetry':h3cWIPSChlStatRetry,'h3cWIPSChlStatEapSuccess':h3cWIPSChlStatEapSuccess,'h3cWIPSChlStatEapFailure':h3cWIPSChlStatEapFailure,'h3cWIPSChlStatEapolStart':h3cWIPSChlStatEapolStart,'h3cWIPSChlStatEapolLogoff':h3cWIPSChlStatEapolLogoff,'h3cWIPSChlStatAssocRequest':h3cWIPSChlStatAssocRequest,'h3cWIPSChlStatAssocResponse':h3cWIPSChlStatAssocResponse,'h3cWIPSChlStatUnicastDisassoc':h3cWIPSChlStatUnicastDisassoc,'h3cWIPSChlStatBroadcastDisassoc':h3cWIPSChlStatBroadcastDisassoc,'h3cWIPSChlStatAuthentication':h3cWIPSChlStatAuthentication,'h3cWIPSChlStatUnicastDeauthen':h3cWIPSChlStatUnicastDeauthen,'h3cWIPSChlStatBroadcastDeauthen':h3cWIPSChlStatBroadcastDeauthen,'h3cWIPSChlStatMalformed':h3cWIPSChlStatMalformed,'h3cWIPSDevStatTable':h3cWIPSDevStatTable,'h3cWIPSDevStatEntry':h3cWIPSDevStatEntry,_AW:h3cWIPSDevStatSensorMacAddr,_AX:h3cWIPSDevStatDevMacAddress,_AY:h3cWIPSDevStatChannel,'h3cWIPSDevStatTxTotalPkt':h3cWIPSDevStatTxTotalPkt,'h3cWIPSDevStatTxTotalByte':h3cWIPSDevStatTxTotalByte,'h3cWIPSDevStatTxBMcastPkt':h3cWIPSDevStatTxBMcastPkt,'h3cWIPSDevStatTxBMcastByte':h3cWIPSDevStatTxBMcastByte,'h3cWIPSDevStatTxUnicastPkt':h3cWIPSDevStatTxUnicastPkt,'h3cWIPSDevStatTxUnicastByte':h3cWIPSDevStatTxUnicastByte,'h3cWIPSDevStatTxMgmt':h3cWIPSDevStatTxMgmt,'h3cWIPSDevStatTxCtrl':h3cWIPSDevStatTxCtrl,'h3cWIPSDevStatTxData':h3cWIPSDevStatTxData,'h3cWIPSDevStatTxBeacon':h3cWIPSDevStatTxBeacon,'h3cWIPSDevStatTxRTS':h3cWIPSDevStatTxRTS,'h3cWIPSDevStatTxProbeRequest':h3cWIPSDevStatTxProbeRequest,'h3cWIPSDevStatTxProbeResponse':h3cWIPSDevStatTxProbeResponse,'h3cWIPSDevStatTxFragment':h3cWIPSDevStatTxFragment,'h3cWIPSDevStatTxRetry':h3cWIPSDevStatTxRetry,'h3cWIPSDevStatTxAssocRequest':h3cWIPSDevStatTxAssocRequest,'h3cWIPSDevStatTxAssocResponse':h3cWIPSDevStatTxAssocResponse,'h3cWIPSDevStatTxUnicastDisassoc':h3cWIPSDevStatTxUnicastDisassoc,'h3cWIPSDevStatTxBcastDisassoc':h3cWIPSDevStatTxBcastDisassoc,'h3cWIPSDevStatTxAuth':h3cWIPSDevStatTxAuth,'h3cWIPSDevStatTxUnicastDeauth':h3cWIPSDevStatTxUnicastDeauth,'h3cWIPSDevStatTxBcastDeauth':h3cWIPSDevStatTxBcastDeauth,'h3cWIPSDevStatTxEAPSuccess':h3cWIPSDevStatTxEAPSuccess,'h3cWIPSDevStatTxEAPFailure':h3cWIPSDevStatTxEAPFailure,'h3cWIPSDevStatTxEAPOLStart':h3cWIPSDevStatTxEAPOLStart,'h3cWIPSDevStatTxEAPOLLogOff':h3cWIPSDevStatTxEAPOLLogOff,'h3cWIPSDevStatTxMalformed':h3cWIPSDevStatTxMalformed,'h3cWIPSDevStatRxTotalPkt':h3cWIPSDevStatRxTotalPkt,'h3cWIPSDevStatRxTotalByte':h3cWIPSDevStatRxTotalByte,'h3cWIPSDevStatRxUnicastPkt':h3cWIPSDevStatRxUnicastPkt,'h3cWIPSDevStatRxUnicastByte':h3cWIPSDevStatRxUnicastByte,'h3cWIPSDevStatRxMgmt':h3cWIPSDevStatRxMgmt,'h3cWIPSDevStatRxCtrl':h3cWIPSDevStatRxCtrl,'h3cWIPSDevStatRxData':h3cWIPSDevStatRxData,'h3cWIPSDevStatRxRTS':h3cWIPSDevStatRxRTS,'h3cWIPSDevStatRxCTS':h3cWIPSDevStatRxCTS,'h3cWIPSDevStatRxProbeRequest':h3cWIPSDevStatRxProbeRequest,'h3cWIPSDevStatRxProbeResponse':h3cWIPSDevStatRxProbeResponse,'h3cWIPSDevStatRxFragment':h3cWIPSDevStatRxFragment,'h3cWIPSDevStatRxRetry':h3cWIPSDevStatRxRetry,'h3cWIPSDevStatRxAssoRequest':h3cWIPSDevStatRxAssoRequest,'h3cWIPSDevStatRxAssoResponse':h3cWIPSDevStatRxAssoResponse,'h3cWIPSDevStatRxDisassoc':h3cWIPSDevStatRxDisassoc,'h3cWIPSDevStatRxAuth':h3cWIPSDevStatRxAuth,'h3cWIPSDevStatRxDeauth':h3cWIPSDevStatRxDeauth,'h3cWIPSDevStatRxEAPSuccess':h3cWIPSDevStatRxEAPSuccess,'h3cWIPSDevStatRxEAPFailure':h3cWIPSDevStatRxEAPFailure,'h3cWIPSDevStatRxEAPOLStart':h3cWIPSDevStatRxEAPOLStart,'h3cWIPSDevStatRxEAPOLLogoff':h3cWIPSDevStatRxEAPOLLogoff,'h3cWIPSDevStatRxMalformed':h3cWIPSDevStatRxMalformed,'h3cWIPSCtmDeviceTable':h3cWIPSCtmDeviceTable,'h3cWIPSCtmDeviceEntry':h3cWIPSCtmDeviceEntry,_AZ:h3cWIPSCtmDeviceVSD,_Aa:h3cWIPSCtmDeviceMAC,'h3cWIPSCtmDeviceType':h3cWIPSCtmDeviceType,'h3cWIPSCtmDeviceState':h3cWIPSCtmDeviceState,'h3cWIPSCtmDeviceStartTime':h3cWIPSCtmDeviceStartTime,'h3cWIPSCtmDeviceCategory':h3cWIPSCtmDeviceCategory,'h3cWIPSCtmDeviceChl':h3cWIPSCtmDeviceChl,'h3cWIPSCtmDevicePrecedence':h3cWIPSCtmDevicePrecedence,'h3cWIPSMalPktStatTable':h3cWIPSMalPktStatTable,'h3cWIPSMalPktStatEntry':h3cWIPSMalPktStatEntry,_Ab:h3cWIPSMalPktStatSensorName,'h3cWIPSMalPktStatInvalidIELength':h3cWIPSMalPktStatInvalidIELength,'h3cWIPSMalPktStatDuplicatedIE':h3cWIPSMalPktStatDuplicatedIE,'h3cWIPSMalPktStatRedundantIE':h3cWIPSMalPktStatRedundantIE,'h3cWIPSMalPktStatInvalidPktLength':h3cWIPSMalPktStatInvalidPktLength,'h3cWIPSMalPktStatIllegalIBSSESS':h3cWIPSMalPktStatIllegalIBSSESS,'h3cWIPSMalPktStatInvalidSourceAddr':h3cWIPSMalPktStatInvalidSourceAddr,'h3cWIPSMalPktStatOverflowEAPOLKey':h3cWIPSMalPktStatOverflowEAPOLKey,'h3cWIPSMalPktStatMalAuth':h3cWIPSMalPktStatMalAuth,'h3cWIPSMalPktStatMalAssoReq':h3cWIPSMalPktStatMalAssoReq,'h3cWIPSMalPktStatMalHTIE':h3cWIPSMalPktStatMalHTIE,'h3cWIPSMalPktStatLargeDuration':h3cWIPSMalPktStatLargeDuration,'h3cWIPSMalPktStatNULLProbeRes':h3cWIPSMalPktStatNULLProbeRes,'h3cWIPSMalPktStatInvalidDeAuthCode':h3cWIPSMalPktStatInvalidDeAuthCode,'h3cWIPSMalPktStatInvalidDisAssoCode':h3cWIPSMalPktStatInvalidDisAssoCode,'h3cWIPSMalPktStatOverflowSSID':h3cWIPSMalPktStatOverflowSSID,'h3cWIPSMalPktStatFatajack':h3cWIPSMalPktStatFatajack,'h3cWIPSMalPktStatInvalidChannel':h3cWIPSMalPktStatInvalidChannel,'h3cWIPSDctUnassocStaTable':h3cWIPSDctUnassocStaTable,'h3cWIPSDctUnassocStaEntry':h3cWIPSDctUnassocStaEntry,_g:h3cWIPSDctUnassocStaVSD,_h:h3cWIPSDctUnassocStaMac,'h3cWIPSDctUnassocStaCategory':h3cWIPSDctUnassocStaCategory,'h3cWIPSDctUnassocStaRadioType':h3cWIPSDctUnassocStaRadioType,'h3cWIPSDctUnassocStaIsCountered':h3cWIPSDctUnassocStaIsCountered,'h3cWIPSDctUnassocStaAdd2BlackList':h3cWIPSDctUnassocStaAdd2BlackList,'h3cWIPSDctUnassocStaAdd2WhiteList':h3cWIPSDctUnassocStaAdd2WhiteList,'h3cWIPSDctUnassocStaAdd2IgnoreList':h3cWIPSDctUnassocStaAdd2IgnoreList,'h3cWIPSDctUnassocStaAdd2CtmList':h3cWIPSDctUnassocStaAdd2CtmList,'h3cWIPSDctUnassocStaFirstDctTm':h3cWIPSDctUnassocStaFirstDctTm,'h3cWIPSDctUnassocStaLastDctTm':h3cWIPSDctUnassocStaLastDctTm,'h3cWIPSDctUnassocStaRptSensorNum':h3cWIPSDctUnassocStaRptSensorNum,'h3cWIPSDctUnassocStaState':h3cWIPSDctUnassocStaState,'h3cWIPSDctUnassocStaVendor':h3cWIPSDctUnassocStaVendor,'h3cWIPSDctUnassocStaRptSensorTable':h3cWIPSDctUnassocStaRptSensorTable,'h3cWIPSDctUnassocStaRptSensorEntry':h3cWIPSDctUnassocStaRptSensorEntry,_Ac:h3cWIPSDctUnassocStaRtpSensorName,'h3cWIPSDctUnassocStaRptSensorRadioId':h3cWIPSDctUnassocStaRptSensorRadioId,'h3cWIPSDctUnassocStaRptRSSI':h3cWIPSDctUnassocStaRptRSSI,'h3cWIPSDctUnassocStaLastRptTm':h3cWIPSDctUnassocStaLastRptTm,'h3cWIPSNotifyGroup':h3cWIPSNotifyGroup})