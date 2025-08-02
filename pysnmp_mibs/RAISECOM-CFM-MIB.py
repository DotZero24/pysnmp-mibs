_A2='rcCfmPMDVFallingThreshold'
_A1='rcCfmPMDVRisingThreshold'
_A0='rcCfmPMDelayFallingThreshold'
_z='rcCfmPMDelayRisingThreshold'
_y='rcCfmPMFLRFallingThreshold'
_x='rcCfmPMFLRRisingThreshold'
_w='rcCfmMipExIfIndex'
_v='rcCfmMcastLbResultIndex'
_u='noActive'
_t='Active'
_s='rcCfmPMDVIntervalIndex'
_r='rcCfmPMDVIntervalPeriod'
_q='rcCfmPMDVCurrentPeriod'
_p='rcCfmPMDelayIntervalIndex'
_o='rcCfmPMDelayIntervalPeriod'
_n='rcCfmPMDelayCurrentPeriod'
_m='rcCfmPMFLRIntervalIndex'
_l='rcCfmPMFLRIntervalPeriod'
_k='rcCfmPMFLRCurrentPeriod'
_j='rcCfmMaMaVlanId'
_i='rcCfmMaMdLevel'
_h='rcCfmLtmDbTransactionId'
_g='rcCfmErrorCcmIndex'
_f='rcCfmErrorCcmRMepId'
_e='rcCfmIfIndex'
_d='dot1agCfmMaCompPrimaryVlanId'
_c='Dot1agCfmLowestAlarmPri'
_b='Dot1agCfmCcmInterval'
_a='VlanIdOrNone'
_Z='Dot1agCfmMDLevelOrNone'
_Y='dot1agCfmMepDbRMepIdentifier'
_X='OctetString'
_W='threshold1'
_V='threshold5PerHundrud'
_U='threshold2PerHundrud'
_T='threshold1PerHundrud'
_S='threshold5PerSouthend'
_R='threshold2PerSouthend'
_Q='threshold1PerSouthend'
_P='threshold0'
_O='TruthValue'
_N='EnableVar'
_M='not-accessible'
_L='dot1agCfmMepIdentifier'
_K='read-create'
_J='dot1agCfmMaIndex'
_I='dot1agCfmMdIndex'
_H='RAISECOM-CFM-MIB'
_G='Integer32'
_F='Unsigned32'
_E='read-write'
_D='IEEE8021-CFM-MIB'
_C='current'
_B='read-only'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_X,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmCcmInterval,Dot1agCfmLowestAlarmPri,Dot1agCfmMDLevel,Dot1agCfmMDLevelOrNone,Dot1agCfmMaintAssocName,Dot1agCfmMaintAssocNameType,Dot1agCfmMepDefects,Dot1agCfmMepId,dot1agCfmMaCompPrimaryVlanId,dot1agCfmMaIndex,dot1agCfmMdIndex,dot1agCfmMepDbRMepIdentifier,dot1agCfmMepIdentifier=mibBuilder.importSymbols(_D,_b,_c,'Dot1agCfmMDLevel',_Z,'Dot1agCfmMaintAssocName','Dot1agCfmMaintAssocNameType','Dot1agCfmMepDefects','Dot1agCfmMepId',_d,_J,_I,_Y,_L)
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
VlanId,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId',_a)
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_O)
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_N)
rcCfm=ModuleIdentity((1,3,6,1,4,1,8886,6,1,26))
if mibBuilder.loadTexts:rcCfm.setRevisions(('2007-11-02 00:00',))
_RcCfmBridge_ObjectIdentity=ObjectIdentity
rcCfmBridge=_RcCfmBridge_ObjectIdentity((1,3,6,1,4,1,8886,6,1,26,1))
class _RcCfmBridgeAdminCfm_Type(EnableVar):defaultValue=2
_RcCfmBridgeAdminCfm_Type.__name__=_N
_RcCfmBridgeAdminCfm_Object=MibScalar
rcCfmBridgeAdminCfm=_RcCfmBridgeAdminCfm_Object((1,3,6,1,4,1,8886,6,1,26,1,1),_RcCfmBridgeAdminCfm_Type())
rcCfmBridgeAdminCfm.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmBridgeAdminCfm.setStatus(_C)
class _RcCfmBridgeCcmDbArchiveHoldtime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcCfmBridgeCcmDbArchiveHoldtime_Type.__name__=_F
_RcCfmBridgeCcmDbArchiveHoldtime_Object=MibScalar
rcCfmBridgeCcmDbArchiveHoldtime=_RcCfmBridgeCcmDbArchiveHoldtime_Object((1,3,6,1,4,1,8886,6,1,26,1,2),_RcCfmBridgeCcmDbArchiveHoldtime_Type())
rcCfmBridgeCcmDbArchiveHoldtime.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmBridgeCcmDbArchiveHoldtime.setStatus(_C)
class _RcCfmBridgeTracerouteCacheEnable_Type(TruthValue):defaultValue=2
_RcCfmBridgeTracerouteCacheEnable_Type.__name__=_O
_RcCfmBridgeTracerouteCacheEnable_Object=MibScalar
rcCfmBridgeTracerouteCacheEnable=_RcCfmBridgeTracerouteCacheEnable_Object((1,3,6,1,4,1,8886,6,1,26,1,3),_RcCfmBridgeTracerouteCacheEnable_Type())
rcCfmBridgeTracerouteCacheEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmBridgeTracerouteCacheEnable.setStatus(_C)
class _RcCfmBridgeTracerouteCacheHoldtime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcCfmBridgeTracerouteCacheHoldtime_Type.__name__=_F
_RcCfmBridgeTracerouteCacheHoldtime_Object=MibScalar
rcCfmBridgeTracerouteCacheHoldtime=_RcCfmBridgeTracerouteCacheHoldtime_Object((1,3,6,1,4,1,8886,6,1,26,1,4),_RcCfmBridgeTracerouteCacheHoldtime_Type())
rcCfmBridgeTracerouteCacheHoldtime.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmBridgeTracerouteCacheHoldtime.setStatus(_C)
class _RcCfmBridgeTracerouteCacheSize_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_RcCfmBridgeTracerouteCacheSize_Type.__name__=_F
_RcCfmBridgeTracerouteCacheSize_Object=MibScalar
rcCfmBridgeTracerouteCacheSize=_RcCfmBridgeTracerouteCacheSize_Object((1,3,6,1,4,1,8886,6,1,26,1,5),_RcCfmBridgeTracerouteCacheSize_Type())
rcCfmBridgeTracerouteCacheSize.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmBridgeTracerouteCacheSize.setStatus(_C)
class _RcCfmBridgeTracerouteCacheClear_Type(TruthValue):defaultValue=2
_RcCfmBridgeTracerouteCacheClear_Type.__name__=_O
_RcCfmBridgeTracerouteCacheClear_Object=MibScalar
rcCfmBridgeTracerouteCacheClear=_RcCfmBridgeTracerouteCacheClear_Object((1,3,6,1,4,1,8886,6,1,26,1,6),_RcCfmBridgeTracerouteCacheClear_Type())
rcCfmBridgeTracerouteCacheClear.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmBridgeTracerouteCacheClear.setStatus(_C)
class _RcCfmBridgeTrapConfig_Type(Dot1agCfmLowestAlarmPri):defaultValue=6
_RcCfmBridgeTrapConfig_Type.__name__=_c
_RcCfmBridgeTrapConfig_Object=MibScalar
rcCfmBridgeTrapConfig=_RcCfmBridgeTrapConfig_Object((1,3,6,1,4,1,8886,6,1,26,1,7),_RcCfmBridgeTrapConfig_Type())
rcCfmBridgeTrapConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmBridgeTrapConfig.setStatus(_A)
class _RcCfmBridgeRmepAgeTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcCfmBridgeRmepAgeTime_Type.__name__=_F
_RcCfmBridgeRmepAgeTime_Object=MibScalar
rcCfmBridgeRmepAgeTime=_RcCfmBridgeRmepAgeTime_Object((1,3,6,1,4,1,8886,6,1,26,1,8),_RcCfmBridgeRmepAgeTime_Type())
rcCfmBridgeRmepAgeTime.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmBridgeRmepAgeTime.setStatus(_C)
class _RcCfmBridgeMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('multicast',1),('unicast',2)))
_RcCfmBridgeMode_Type.__name__=_G
_RcCfmBridgeMode_Object=MibScalar
rcCfmBridgeMode=_RcCfmBridgeMode_Object((1,3,6,1,4,1,8886,6,1,26,1,9),_RcCfmBridgeMode_Type())
rcCfmBridgeMode.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmBridgeMode.setStatus(_C)
class _RcCfmLinkVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_RcCfmLinkVlanList_Type.__name__=_X
_RcCfmLinkVlanList_Object=MibScalar
rcCfmLinkVlanList=_RcCfmLinkVlanList_Object((1,3,6,1,4,1,8886,6,1,26,1,10),_RcCfmLinkVlanList_Type())
rcCfmLinkVlanList.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmLinkVlanList.setStatus(_C)
_RcCfmIfTable_Object=MibTable
rcCfmIfTable=_RcCfmIfTable_Object((1,3,6,1,4,1,8886,6,1,26,2))
if mibBuilder.loadTexts:rcCfmIfTable.setStatus(_C)
_RcCfmIfEntry_Object=MibTableRow
rcCfmIfEntry=_RcCfmIfEntry_Object((1,3,6,1,4,1,8886,6,1,26,2,1))
rcCfmIfEntry.setIndexNames((0,_H,_e))
if mibBuilder.loadTexts:rcCfmIfEntry.setStatus(_C)
_RcCfmIfIndex_Type=InterfaceIndex
_RcCfmIfIndex_Object=MibTableColumn
rcCfmIfIndex=_RcCfmIfIndex_Object((1,3,6,1,4,1,8886,6,1,26,2,1,1),_RcCfmIfIndex_Type())
rcCfmIfIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmIfIndex.setStatus(_C)
class _RcCfmIfAdminCfm_Type(EnableVar):defaultValue=1
_RcCfmIfAdminCfm_Type.__name__=_N
_RcCfmIfAdminCfm_Object=MibTableColumn
rcCfmIfAdminCfm=_RcCfmIfAdminCfm_Object((1,3,6,1,4,1,8886,6,1,26,2,1,2),_RcCfmIfAdminCfm_Type())
rcCfmIfAdminCfm.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmIfAdminCfm.setStatus(_C)
_RcCfmIfMipLevel_Type=Dot1agCfmMDLevelOrNone
_RcCfmIfMipLevel_Object=MibTableColumn
rcCfmIfMipLevel=_RcCfmIfMipLevel_Object((1,3,6,1,4,1,8886,6,1,26,2,1,3),_RcCfmIfMipLevel_Type())
rcCfmIfMipLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmIfMipLevel.setStatus(_A)
_RcCfmMdTable_Object=MibTable
rcCfmMdTable=_RcCfmMdTable_Object((1,3,6,1,4,1,8886,6,1,26,3))
if mibBuilder.loadTexts:rcCfmMdTable.setStatus(_C)
_RcCfmMdEntry_Object=MibTableRow
rcCfmMdEntry=_RcCfmMdEntry_Object((1,3,6,1,4,1,8886,6,1,26,3,1))
rcCfmMdEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:rcCfmMdEntry.setStatus(_C)
class _RcCfmMdCcmRMpClear_Type(TruthValue):defaultValue=2
_RcCfmMdCcmRMpClear_Type.__name__=_O
_RcCfmMdCcmRMpClear_Object=MibTableColumn
rcCfmMdCcmRMpClear=_RcCfmMdCcmRMpClear_Object((1,3,6,1,4,1,8886,6,1,26,3,1,1),_RcCfmMdCcmRMpClear_Type())
rcCfmMdCcmRMpClear.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMdCcmRMpClear.setStatus(_C)
_RcCfmErrorCcmTable_Object=MibTable
rcCfmErrorCcmTable=_RcCfmErrorCcmTable_Object((1,3,6,1,4,1,8886,6,1,26,4))
if mibBuilder.loadTexts:rcCfmErrorCcmTable.setStatus(_C)
_RcCfmErrorCcmEntry_Object=MibTableRow
rcCfmErrorCcmEntry=_RcCfmErrorCcmEntry_Object((1,3,6,1,4,1,8886,6,1,26,4,1))
rcCfmErrorCcmEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_H,_f),(0,_H,_g))
if mibBuilder.loadTexts:rcCfmErrorCcmEntry.setStatus(_C)
_RcCfmErrorCcmRMepId_Type=Dot1agCfmMepId
_RcCfmErrorCcmRMepId_Object=MibTableColumn
rcCfmErrorCcmRMepId=_RcCfmErrorCcmRMepId_Object((1,3,6,1,4,1,8886,6,1,26,4,1,1),_RcCfmErrorCcmRMepId_Type())
rcCfmErrorCcmRMepId.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmErrorCcmRMepId.setStatus(_C)
class _RcCfmErrorCcmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RcCfmErrorCcmIndex_Type.__name__=_F
_RcCfmErrorCcmIndex_Object=MibTableColumn
rcCfmErrorCcmIndex=_RcCfmErrorCcmIndex_Object((1,3,6,1,4,1,8886,6,1,26,4,1,2),_RcCfmErrorCcmIndex_Type())
rcCfmErrorCcmIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmErrorCcmIndex.setStatus(_C)
_RcCfmErrorCcmLevel_Type=Dot1agCfmMDLevel
_RcCfmErrorCcmLevel_Object=MibTableColumn
rcCfmErrorCcmLevel=_RcCfmErrorCcmLevel_Object((1,3,6,1,4,1,8886,6,1,26,4,1,3),_RcCfmErrorCcmLevel_Type())
rcCfmErrorCcmLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmErrorCcmLevel.setStatus(_C)
_RcCfmErrorCcmVlan_Type=VlanIdOrNone
_RcCfmErrorCcmVlan_Object=MibTableColumn
rcCfmErrorCcmVlan=_RcCfmErrorCcmVlan_Object((1,3,6,1,4,1,8886,6,1,26,4,1,4),_RcCfmErrorCcmVlan_Type())
rcCfmErrorCcmVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmErrorCcmVlan.setStatus(_C)
class _RcCfmErrorCcmRecvMdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcCfmErrorCcmRecvMdName_Type.__name__=_X
_RcCfmErrorCcmRecvMdName_Object=MibTableColumn
rcCfmErrorCcmRecvMdName=_RcCfmErrorCcmRecvMdName_Object((1,3,6,1,4,1,8886,6,1,26,4,1,5),_RcCfmErrorCcmRecvMdName_Type())
rcCfmErrorCcmRecvMdName.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmErrorCcmRecvMdName.setStatus(_C)
class _RcCfmErrorCcmMaid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,44))
_RcCfmErrorCcmMaid_Type.__name__=_X
_RcCfmErrorCcmMaid_Object=MibTableColumn
rcCfmErrorCcmMaid=_RcCfmErrorCcmMaid_Object((1,3,6,1,4,1,8886,6,1,26,4,1,6),_RcCfmErrorCcmMaid_Type())
rcCfmErrorCcmMaid.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmErrorCcmMaid.setStatus(_C)
_RcCfmErrorCcmMacAddress_Type=MacAddress
_RcCfmErrorCcmMacAddress_Object=MibTableColumn
rcCfmErrorCcmMacAddress=_RcCfmErrorCcmMacAddress_Object((1,3,6,1,4,1,8886,6,1,26,4,1,7),_RcCfmErrorCcmMacAddress_Type())
rcCfmErrorCcmMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmErrorCcmMacAddress.setStatus(_C)
_RcCfmErrorCcmErrorType_Type=Dot1agCfmMepDefects
_RcCfmErrorCcmErrorType_Object=MibTableColumn
rcCfmErrorCcmErrorType=_RcCfmErrorCcmErrorType_Object((1,3,6,1,4,1,8886,6,1,26,4,1,8),_RcCfmErrorCcmErrorType_Type())
rcCfmErrorCcmErrorType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmErrorCcmErrorType.setStatus(_C)
class _RcCfmErrorCcmHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RcCfmErrorCcmHoldTime_Type.__name__=_F
_RcCfmErrorCcmHoldTime_Object=MibTableColumn
rcCfmErrorCcmHoldTime=_RcCfmErrorCcmHoldTime_Object((1,3,6,1,4,1,8886,6,1,26,4,1,9),_RcCfmErrorCcmHoldTime_Type())
rcCfmErrorCcmHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmErrorCcmHoldTime.setStatus(_C)
_RcCfmErrorCcmClear_Type=TruthValue
_RcCfmErrorCcmClear_Object=MibTableColumn
rcCfmErrorCcmClear=_RcCfmErrorCcmClear_Object((1,3,6,1,4,1,8886,6,1,26,4,1,10),_RcCfmErrorCcmClear_Type())
rcCfmErrorCcmClear.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmErrorCcmClear.setStatus(_C)
_RcCfmLtmDbTable_Object=MibTable
rcCfmLtmDbTable=_RcCfmLtmDbTable_Object((1,3,6,1,4,1,8886,6,1,26,5))
if mibBuilder.loadTexts:rcCfmLtmDbTable.setStatus(_C)
_RcCfmLtmDbEntry_Object=MibTableRow
rcCfmLtmDbEntry=_RcCfmLtmDbEntry_Object((1,3,6,1,4,1,8886,6,1,26,5,1))
rcCfmLtmDbEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_H,_h))
if mibBuilder.loadTexts:rcCfmLtmDbEntry.setStatus(_C)
class _RcCfmLtmDbTransactionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RcCfmLtmDbTransactionId_Type.__name__=_F
_RcCfmLtmDbTransactionId_Object=MibTableColumn
rcCfmLtmDbTransactionId=_RcCfmLtmDbTransactionId_Object((1,3,6,1,4,1,8886,6,1,26,5,1,1),_RcCfmLtmDbTransactionId_Type())
rcCfmLtmDbTransactionId.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmLtmDbTransactionId.setStatus(_C)
_RcCfmLtmDbTargetMacAddress_Type=MacAddress
_RcCfmLtmDbTargetMacAddress_Object=MibTableColumn
rcCfmLtmDbTargetMacAddress=_RcCfmLtmDbTargetMacAddress_Object((1,3,6,1,4,1,8886,6,1,26,5,1,2),_RcCfmLtmDbTargetMacAddress_Type())
rcCfmLtmDbTargetMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmLtmDbTargetMacAddress.setStatus(_C)
_RcCfmMepDbExTable_Object=MibTable
rcCfmMepDbExTable=_RcCfmMepDbExTable_Object((1,3,6,1,4,1,8886,6,1,26,6))
if mibBuilder.loadTexts:rcCfmMepDbExTable.setStatus(_C)
_RcCfmMepDbExEntry_Object=MibTableRow
rcCfmMepDbExEntry=_RcCfmMepDbExEntry_Object((1,3,6,1,4,1,8886,6,1,26,6,1))
rcCfmMepDbExEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_D,_Y))
if mibBuilder.loadTexts:rcCfmMepDbExEntry.setStatus(_C)
class _RcCfmMepDbExEntryHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RcCfmMepDbExEntryHoldTime_Type.__name__=_F
_RcCfmMepDbExEntryHoldTime_Object=MibTableColumn
rcCfmMepDbExEntryHoldTime=_RcCfmMepDbExEntryHoldTime_Object((1,3,6,1,4,1,8886,6,1,26,6,1,1),_RcCfmMepDbExEntryHoldTime_Type())
rcCfmMepDbExEntryHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMepDbExEntryHoldTime.setStatus(_C)
_RcCfmMaCciEnableTable_Object=MibTable
rcCfmMaCciEnableTable=_RcCfmMaCciEnableTable_Object((1,3,6,1,4,1,8886,6,1,26,7))
if mibBuilder.loadTexts:rcCfmMaCciEnableTable.setStatus(_A)
_RcCfmMaCciEnableEntry_Object=MibTableRow
rcCfmMaCciEnableEntry=_RcCfmMaCciEnableEntry_Object((1,3,6,1,4,1,8886,6,1,26,7,1))
rcCfmMaCciEnableEntry.setIndexNames((0,_H,_i),(0,_H,_j))
if mibBuilder.loadTexts:rcCfmMaCciEnableEntry.setStatus(_A)
_RcCfmMaMdLevel_Type=Dot1agCfmMDLevel
_RcCfmMaMdLevel_Object=MibTableColumn
rcCfmMaMdLevel=_RcCfmMaMdLevel_Object((1,3,6,1,4,1,8886,6,1,26,7,1,1),_RcCfmMaMdLevel_Type())
rcCfmMaMdLevel.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmMaMdLevel.setStatus(_A)
_RcCfmMaMaVlanId_Type=VlanIdOrNone
_RcCfmMaMaVlanId_Object=MibTableColumn
rcCfmMaMaVlanId=_RcCfmMaMaVlanId_Object((1,3,6,1,4,1,8886,6,1,26,7,1,2),_RcCfmMaMaVlanId_Type())
rcCfmMaMaVlanId.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmMaMaVlanId.setStatus(_A)
_RcCfmMaCciEnabled_Type=TruthValue
_RcCfmMaCciEnabled_Object=MibTableColumn
rcCfmMaCciEnabled=_RcCfmMaCciEnabled_Object((1,3,6,1,4,1,8886,6,1,26,7,1,3),_RcCfmMaCciEnabled_Type())
rcCfmMaCciEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaCciEnabled.setStatus(_A)
_RcCfmMepExTable_Object=MibTable
rcCfmMepExTable=_RcCfmMepExTable_Object((1,3,6,1,4,1,8886,6,1,26,8))
if mibBuilder.loadTexts:rcCfmMepExTable.setStatus(_C)
_RcCfmMepExEntry_Object=MibTableRow
rcCfmMepExEntry=_RcCfmMepExEntry_Object((1,3,6,1,4,1,8886,6,1,26,8,1))
rcCfmMepExEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L))
if mibBuilder.loadTexts:rcCfmMepExEntry.setStatus(_C)
class _RcCfmMepExLbrTimeoutNum_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_RcCfmMepExLbrTimeoutNum_Type.__name__=_F
_RcCfmMepExLbrTimeoutNum_Object=MibTableColumn
rcCfmMepExLbrTimeoutNum=_RcCfmMepExLbrTimeoutNum_Object((1,3,6,1,4,1,8886,6,1,26,8,1,1),_RcCfmMepExLbrTimeoutNum_Type())
rcCfmMepExLbrTimeoutNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMepExLbrTimeoutNum.setStatus(_C)
class _RcCfmMepExTransmitLbmDataTlvLen_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1484))
_RcCfmMepExTransmitLbmDataTlvLen_Type.__name__=_F
_RcCfmMepExTransmitLbmDataTlvLen_Object=MibTableColumn
rcCfmMepExTransmitLbmDataTlvLen=_RcCfmMepExTransmitLbmDataTlvLen_Object((1,3,6,1,4,1,8886,6,1,26,8,1,2),_RcCfmMepExTransmitLbmDataTlvLen_Type())
rcCfmMepExTransmitLbmDataTlvLen.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMepExTransmitLbmDataTlvLen.setStatus(_C)
class _RcCfmMepExLckAdmin_Type(EnableVar):defaultValue=2
_RcCfmMepExLckAdmin_Type.__name__=_N
_RcCfmMepExLckAdmin_Object=MibTableColumn
rcCfmMepExLckAdmin=_RcCfmMepExLckAdmin_Object((1,3,6,1,4,1,8886,6,1,26,8,1,3),_RcCfmMepExLckAdmin_Type())
rcCfmMepExLckAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMepExLckAdmin.setStatus(_C)
class _RcCfmMaExAisSuppressStatus_Type(Integer32):defaultValue=3
_RcCfmMaExAisSuppressStatus_Type.__name__=_G
_RcCfmMaExAisSuppressStatus_Object=MibTableColumn
rcCfmMaExAisSuppressStatus=_RcCfmMaExAisSuppressStatus_Object((1,3,6,1,4,1,8886,6,1,26,8,1,4),_RcCfmMaExAisSuppressStatus_Type())
rcCfmMaExAisSuppressStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExAisSuppressStatus.setStatus(_C)
class _RcCfmMaExAisSuppressAdmin_Type(EnableVar):defaultValue=1
_RcCfmMaExAisSuppressAdmin_Type.__name__=_N
_RcCfmMaExAisSuppressAdmin_Object=MibTableColumn
rcCfmMaExAisSuppressAdmin=_RcCfmMaExAisSuppressAdmin_Object((1,3,6,1,4,1,8886,6,1,26,8,1,5),_RcCfmMaExAisSuppressAdmin_Type())
rcCfmMaExAisSuppressAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaExAisSuppressAdmin.setStatus(_C)
class _RcCfmMepExPduPriority_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcCfmMepExPduPriority_Type.__name__=_G
_RcCfmMepExPduPriority_Object=MibTableColumn
rcCfmMepExPduPriority=_RcCfmMepExPduPriority_Object((1,3,6,1,4,1,8886,6,1,26,8,1,6),_RcCfmMepExPduPriority_Type())
rcCfmMepExPduPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMepExPduPriority.setStatus(_C)
class _RcCfmMepExPmAdmin_Type(EnableVar):defaultValue=2
_RcCfmMepExPmAdmin_Type.__name__=_N
_RcCfmMepExPmAdmin_Object=MibTableColumn
rcCfmMepExPmAdmin=_RcCfmMepExPmAdmin_Object((1,3,6,1,4,1,8886,6,1,26,8,1,7),_RcCfmMepExPmAdmin_Type())
rcCfmMepExPmAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMepExPmAdmin.setStatus(_C)
class _RcCfmMepExRdiAdmin_Type(EnableVar):defaultValue=2
_RcCfmMepExRdiAdmin_Type.__name__=_N
_RcCfmMepExRdiAdmin_Object=MibTableColumn
rcCfmMepExRdiAdmin=_RcCfmMepExRdiAdmin_Object((1,3,6,1,4,1,8886,6,1,26,8,1,8),_RcCfmMepExRdiAdmin_Type())
rcCfmMepExRdiAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMepExRdiAdmin.setStatus(_C)
_RcCfmMaMepListExTable_Object=MibTable
rcCfmMaMepListExTable=_RcCfmMaMepListExTable_Object((1,3,6,1,4,1,8886,6,1,26,9))
if mibBuilder.loadTexts:rcCfmMaMepListExTable.setStatus(_C)
_RcCfmMaMepListExEntry_Object=MibTableRow
rcCfmMaMepListExEntry=_RcCfmMaMepListExEntry_Object((1,3,6,1,4,1,8886,6,1,26,9,1))
rcCfmMaMepListExEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L))
if mibBuilder.loadTexts:rcCfmMaMepListExEntry.setStatus(_C)
class _RcCfmMaMepListType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('static-remote',2),('dynamic-remote',3)))
_RcCfmMaMepListType_Type.__name__=_G
_RcCfmMaMepListType_Object=MibTableColumn
rcCfmMaMepListType=_RcCfmMaMepListType_Object((1,3,6,1,4,1,8886,6,1,26,9,1,1),_RcCfmMaMepListType_Type())
rcCfmMaMepListType.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaMepListType.setStatus(_A)
_RcCfmMaMepListMacAddress_Type=MacAddress
_RcCfmMaMepListMacAddress_Object=MibTableColumn
rcCfmMaMepListMacAddress=_RcCfmMaMepListMacAddress_Object((1,3,6,1,4,1,8886,6,1,26,9,1,2),_RcCfmMaMepListMacAddress_Type())
rcCfmMaMepListMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaMepListMacAddress.setStatus(_C)
_RcCfmMaMepListIfIndex_Type=InterfaceIndex
_RcCfmMaMepListIfIndex_Object=MibTableColumn
rcCfmMaMepListIfIndex=_RcCfmMaMepListIfIndex_Object((1,3,6,1,4,1,8886,6,1,26,9,1,3),_RcCfmMaMepListIfIndex_Type())
rcCfmMaMepListIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaMepListIfIndex.setStatus(_C)
_RcCfmMaNetExTable_Object=MibTable
rcCfmMaNetExTable=_RcCfmMaNetExTable_Object((1,3,6,1,4,1,8886,6,1,26,10))
if mibBuilder.loadTexts:rcCfmMaNetExTable.setStatus(_C)
_RcCfmMaNetExEntry_Object=MibTableRow
rcCfmMaNetExEntry=_RcCfmMaNetExEntry_Object((1,3,6,1,4,1,8886,6,1,26,10,1))
rcCfmMaNetExEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:rcCfmMaNetExEntry.setStatus(_C)
_RcCfmMaNetRemoteMepLearnEnabled_Type=TruthValue
_RcCfmMaNetRemoteMepLearnEnabled_Object=MibTableColumn
rcCfmMaNetRemoteMepLearnEnabled=_RcCfmMaNetRemoteMepLearnEnabled_Object((1,3,6,1,4,1,8886,6,1,26,10,1,1),_RcCfmMaNetRemoteMepLearnEnabled_Type())
rcCfmMaNetRemoteMepLearnEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaNetRemoteMepLearnEnabled.setStatus(_A)
class _RcCfmMaNetCostumerVlan_Type(VlanIdOrNone):defaultValue=0
_RcCfmMaNetCostumerVlan_Type.__name__=_a
_RcCfmMaNetCostumerVlan_Object=MibTableColumn
rcCfmMaNetCostumerVlan=_RcCfmMaNetCostumerVlan_Object((1,3,6,1,4,1,8886,6,1,26,10,1,2),_RcCfmMaNetCostumerVlan_Type())
rcCfmMaNetCostumerVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaNetCostumerVlan.setStatus(_C)
class _RcCfmMaNetPduPriority_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcCfmMaNetPduPriority_Type.__name__=_F
_RcCfmMaNetPduPriority_Object=MibTableColumn
rcCfmMaNetPduPriority=_RcCfmMaNetPduPriority_Object((1,3,6,1,4,1,8886,6,1,26,10,1,3),_RcCfmMaNetPduPriority_Type())
rcCfmMaNetPduPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaNetPduPriority.setStatus(_C)
class _RcCfmMaNetRemoteMepLearnActive_Type(TruthValue):defaultValue=2
_RcCfmMaNetRemoteMepLearnActive_Type.__name__=_O
_RcCfmMaNetRemoteMepLearnActive_Object=MibTableColumn
rcCfmMaNetRemoteMepLearnActive=_RcCfmMaNetRemoteMepLearnActive_Object((1,3,6,1,4,1,8886,6,1,26,10,1,4),_RcCfmMaNetRemoteMepLearnActive_Type())
rcCfmMaNetRemoteMepLearnActive.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaNetRemoteMepLearnActive.setStatus(_C)
class _RcCfmMaNetCcCheckEnabled_Type(TruthValue):defaultValue=2
_RcCfmMaNetCcCheckEnabled_Type.__name__=_O
_RcCfmMaNetCcCheckEnabled_Object=MibTableColumn
rcCfmMaNetCcCheckEnabled=_RcCfmMaNetCcCheckEnabled_Object((1,3,6,1,4,1,8886,6,1,26,10,1,5),_RcCfmMaNetCcCheckEnabled_Type())
rcCfmMaNetCcCheckEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaNetCcCheckEnabled.setStatus(_C)
_RcCfmPMTable_Object=MibTable
rcCfmPMTable=_RcCfmPMTable_Object((1,3,6,1,4,1,8886,6,1,26,11))
if mibBuilder.loadTexts:rcCfmPMTable.setStatus(_A)
_RcCfmPMEntry_Object=MibTableRow
rcCfmPMEntry=_RcCfmPMEntry_Object((1,3,6,1,4,1,8886,6,1,26,11,1))
rcCfmPMEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_D,_Y))
if mibBuilder.loadTexts:rcCfmPMEntry.setStatus(_A)
_RcCfmPMEnabled_Type=TruthValue
_RcCfmPMEnabled_Object=MibTableColumn
rcCfmPMEnabled=_RcCfmPMEnabled_Object((1,3,6,1,4,1,8886,6,1,26,11,1,1),_RcCfmPMEnabled_Type())
rcCfmPMEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMEnabled.setStatus(_A)
class _RcCfmPMDmmTxInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('intervalInvalid',0),('interval300Hz',1),('interval10ms',2),('interval100ms',3),('interval1s',4),('interval10s',5),('interval1min',6),('interval10min',7)))
_RcCfmPMDmmTxInterval_Type.__name__=_G
_RcCfmPMDmmTxInterval_Object=MibTableColumn
rcCfmPMDmmTxInterval=_RcCfmPMDmmTxInterval_Object((1,3,6,1,4,1,8886,6,1,26,11,1,2),_RcCfmPMDmmTxInterval_Type())
rcCfmPMDmmTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDmmTxInterval.setStatus(_A)
class _RcCfmPMDelayObjective_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCfmPMDelayObjective_Type.__name__=_F
_RcCfmPMDelayObjective_Object=MibTableColumn
rcCfmPMDelayObjective=_RcCfmPMDelayObjective_Object((1,3,6,1,4,1,8886,6,1,26,11,1,3),_RcCfmPMDelayObjective_Type())
rcCfmPMDelayObjective.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMDelayObjective.setStatus(_A)
class _RcCfmPMDVObjective_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCfmPMDVObjective_Type.__name__=_F
_RcCfmPMDVObjective_Object=MibTableColumn
rcCfmPMDVObjective=_RcCfmPMDVObjective_Object((1,3,6,1,4,1,8886,6,1,26,11,1,4),_RcCfmPMDVObjective_Type())
rcCfmPMDVObjective.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMDVObjective.setStatus(_A)
class _RcCfmPMFLRRisingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7)))
_RcCfmPMFLRRisingThreshold_Type.__name__=_G
_RcCfmPMFLRRisingThreshold_Object=MibTableColumn
rcCfmPMFLRRisingThreshold=_RcCfmPMFLRRisingThreshold_Object((1,3,6,1,4,1,8886,6,1,26,11,1,5),_RcCfmPMFLRRisingThreshold_Type())
rcCfmPMFLRRisingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMFLRRisingThreshold.setStatus(_A)
class _RcCfmPMFLRFallingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7)))
_RcCfmPMFLRFallingThreshold_Type.__name__=_G
_RcCfmPMFLRFallingThreshold_Object=MibTableColumn
rcCfmPMFLRFallingThreshold=_RcCfmPMFLRFallingThreshold_Object((1,3,6,1,4,1,8886,6,1,26,11,1,6),_RcCfmPMFLRFallingThreshold_Type())
rcCfmPMFLRFallingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMFLRFallingThreshold.setStatus(_A)
class _RcCfmPMDelayRisingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7)))
_RcCfmPMDelayRisingThreshold_Type.__name__=_G
_RcCfmPMDelayRisingThreshold_Object=MibTableColumn
rcCfmPMDelayRisingThreshold=_RcCfmPMDelayRisingThreshold_Object((1,3,6,1,4,1,8886,6,1,26,11,1,7),_RcCfmPMDelayRisingThreshold_Type())
rcCfmPMDelayRisingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMDelayRisingThreshold.setStatus(_A)
class _RcCfmPMDelayFallingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7)))
_RcCfmPMDelayFallingThreshold_Type.__name__=_G
_RcCfmPMDelayFallingThreshold_Object=MibTableColumn
rcCfmPMDelayFallingThreshold=_RcCfmPMDelayFallingThreshold_Object((1,3,6,1,4,1,8886,6,1,26,11,1,8),_RcCfmPMDelayFallingThreshold_Type())
rcCfmPMDelayFallingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMDelayFallingThreshold.setStatus(_A)
class _RcCfmPMDVRisingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7)))
_RcCfmPMDVRisingThreshold_Type.__name__=_G
_RcCfmPMDVRisingThreshold_Object=MibTableColumn
rcCfmPMDVRisingThreshold=_RcCfmPMDVRisingThreshold_Object((1,3,6,1,4,1,8886,6,1,26,11,1,9),_RcCfmPMDVRisingThreshold_Type())
rcCfmPMDVRisingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMDVRisingThreshold.setStatus(_A)
class _RcCfmPMDVFallingThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6),(_W,7)))
_RcCfmPMDVFallingThreshold_Type.__name__=_G
_RcCfmPMDVFallingThreshold_Object=MibTableColumn
rcCfmPMDVFallingThreshold=_RcCfmPMDVFallingThreshold_Object((1,3,6,1,4,1,8886,6,1,26,11,1,10),_RcCfmPMDVFallingThreshold_Type())
rcCfmPMDVFallingThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMDVFallingThreshold.setStatus(_A)
class _RcCfmPMStatiticsClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('all',0),('frame-loss-ratio',1),('delay',2),('delay-variation',3)))
_RcCfmPMStatiticsClear_Type.__name__=_G
_RcCfmPMStatiticsClear_Object=MibTableColumn
rcCfmPMStatiticsClear=_RcCfmPMStatiticsClear_Object((1,3,6,1,4,1,8886,6,1,26,11,1,11),_RcCfmPMStatiticsClear_Type())
rcCfmPMStatiticsClear.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMStatiticsClear.setStatus(_A)
_RcCfmPMTrapSendEnable_Type=TruthValue
_RcCfmPMTrapSendEnable_Object=MibTableColumn
rcCfmPMTrapSendEnable=_RcCfmPMTrapSendEnable_Object((1,3,6,1,4,1,8886,6,1,26,11,1,12),_RcCfmPMTrapSendEnable_Type())
rcCfmPMTrapSendEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMTrapSendEnable.setStatus(_A)
class _RcCfmPMThroughputTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_RcCfmPMThroughputTimeout_Type.__name__=_F
_RcCfmPMThroughputTimeout_Object=MibTableColumn
rcCfmPMThroughputTimeout=_RcCfmPMThroughputTimeout_Object((1,3,6,1,4,1,8886,6,1,26,11,1,13),_RcCfmPMThroughputTimeout_Type())
rcCfmPMThroughputTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMThroughputTimeout.setStatus(_A)
class _RcCfmPMThroughputObject_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(125,1000000))
_RcCfmPMThroughputObject_Type.__name__=_F
_RcCfmPMThroughputObject_Object=MibTableColumn
rcCfmPMThroughputObject=_RcCfmPMThroughputObject_Object((1,3,6,1,4,1,8886,6,1,26,11,1,14),_RcCfmPMThroughputObject_Type())
rcCfmPMThroughputObject.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMThroughputObject.setStatus(_A)
class _RcCfmPMThroughputPduLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('length64',0),('length128',1),('length256',2),('length512',3),('length1024',4),('length1280',5),('length1518',6)))
_RcCfmPMThroughputPduLength_Type.__name__=_G
_RcCfmPMThroughputPduLength_Object=MibTableColumn
rcCfmPMThroughputPduLength=_RcCfmPMThroughputPduLength_Object((1,3,6,1,4,1,8886,6,1,26,11,1,15),_RcCfmPMThroughputPduLength_Type())
rcCfmPMThroughputPduLength.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMThroughputPduLength.setStatus(_A)
_RcCfmPMThroughputEnable_Type=TruthValue
_RcCfmPMThroughputEnable_Object=MibTableColumn
rcCfmPMThroughputEnable=_RcCfmPMThroughputEnable_Object((1,3,6,1,4,1,8886,6,1,26,11,1,16),_RcCfmPMThroughputEnable_Type())
rcCfmPMThroughputEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMThroughputEnable.setStatus(_A)
_RcCfmPMRowStatus_Type=RowStatus
_RcCfmPMRowStatus_Object=MibTableColumn
rcCfmPMRowStatus=_RcCfmPMRowStatus_Object((1,3,6,1,4,1,8886,6,1,26,11,1,17),_RcCfmPMRowStatus_Type())
rcCfmPMRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmPMRowStatus.setStatus(_A)
_RcCfmPMFLRTotalTable_Object=MibTable
rcCfmPMFLRTotalTable=_RcCfmPMFLRTotalTable_Object((1,3,6,1,4,1,8886,6,1,26,12))
if mibBuilder.loadTexts:rcCfmPMFLRTotalTable.setStatus(_A)
_RcCfmPMFLRTotalEntry_Object=MibTableRow
rcCfmPMFLRTotalEntry=_RcCfmPMFLRTotalEntry_Object((1,3,6,1,4,1,8886,6,1,26,12,1))
rcCfmPMFLRTotalEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L))
if mibBuilder.loadTexts:rcCfmPMFLRTotalEntry.setStatus(_A)
_RcCfmPMFLRTotalElapsedTime_Type=Unsigned32
_RcCfmPMFLRTotalElapsedTime_Object=MibTableColumn
rcCfmPMFLRTotalElapsedTime=_RcCfmPMFLRTotalElapsedTime_Object((1,3,6,1,4,1,8886,6,1,26,12,1,1),_RcCfmPMFLRTotalElapsedTime_Type())
rcCfmPMFLRTotalElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRTotalElapsedTime.setStatus(_A)
_RcCfmPMFLRTotalFarEndTxCounter_Type=Unsigned32
_RcCfmPMFLRTotalFarEndTxCounter_Object=MibTableColumn
rcCfmPMFLRTotalFarEndTxCounter=_RcCfmPMFLRTotalFarEndTxCounter_Object((1,3,6,1,4,1,8886,6,1,26,12,1,2),_RcCfmPMFLRTotalFarEndTxCounter_Type())
rcCfmPMFLRTotalFarEndTxCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRTotalFarEndTxCounter.setStatus(_A)
_RcCfmPMFLRTotalFarEndLostCounter_Type=Unsigned32
_RcCfmPMFLRTotalFarEndLostCounter_Object=MibTableColumn
rcCfmPMFLRTotalFarEndLostCounter=_RcCfmPMFLRTotalFarEndLostCounter_Object((1,3,6,1,4,1,8886,6,1,26,12,1,3),_RcCfmPMFLRTotalFarEndLostCounter_Type())
rcCfmPMFLRTotalFarEndLostCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRTotalFarEndLostCounter.setStatus(_A)
class _RcCfmPMFLRTotalFarEndLossRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCfmPMFLRTotalFarEndLossRatio_Type.__name__=_F
_RcCfmPMFLRTotalFarEndLossRatio_Object=MibTableColumn
rcCfmPMFLRTotalFarEndLossRatio=_RcCfmPMFLRTotalFarEndLossRatio_Object((1,3,6,1,4,1,8886,6,1,26,12,1,4),_RcCfmPMFLRTotalFarEndLossRatio_Type())
rcCfmPMFLRTotalFarEndLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRTotalFarEndLossRatio.setStatus(_A)
_RcCfmPMFLRTotalFarEndUnaviableSecond_Type=Unsigned32
_RcCfmPMFLRTotalFarEndUnaviableSecond_Object=MibTableColumn
rcCfmPMFLRTotalFarEndUnaviableSecond=_RcCfmPMFLRTotalFarEndUnaviableSecond_Object((1,3,6,1,4,1,8886,6,1,26,12,1,5),_RcCfmPMFLRTotalFarEndUnaviableSecond_Type())
rcCfmPMFLRTotalFarEndUnaviableSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRTotalFarEndUnaviableSecond.setStatus(_A)
_RcCfmPMFLRTotalNearEndTxCounter_Type=Unsigned32
_RcCfmPMFLRTotalNearEndTxCounter_Object=MibTableColumn
rcCfmPMFLRTotalNearEndTxCounter=_RcCfmPMFLRTotalNearEndTxCounter_Object((1,3,6,1,4,1,8886,6,1,26,12,1,6),_RcCfmPMFLRTotalNearEndTxCounter_Type())
rcCfmPMFLRTotalNearEndTxCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRTotalNearEndTxCounter.setStatus(_A)
_RcCfmPMFLRTotalNearEndLostCounter_Type=Unsigned32
_RcCfmPMFLRTotalNearEndLostCounter_Object=MibTableColumn
rcCfmPMFLRTotalNearEndLostCounter=_RcCfmPMFLRTotalNearEndLostCounter_Object((1,3,6,1,4,1,8886,6,1,26,12,1,7),_RcCfmPMFLRTotalNearEndLostCounter_Type())
rcCfmPMFLRTotalNearEndLostCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRTotalNearEndLostCounter.setStatus(_A)
class _RcCfmPMFLRTotalNearEndLossRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCfmPMFLRTotalNearEndLossRatio_Type.__name__=_F
_RcCfmPMFLRTotalNearEndLossRatio_Object=MibTableColumn
rcCfmPMFLRTotalNearEndLossRatio=_RcCfmPMFLRTotalNearEndLossRatio_Object((1,3,6,1,4,1,8886,6,1,26,12,1,8),_RcCfmPMFLRTotalNearEndLossRatio_Type())
rcCfmPMFLRTotalNearEndLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRTotalNearEndLossRatio.setStatus(_A)
_RcCfmPMFLRTotalNearEndUnaviableSecond_Type=Unsigned32
_RcCfmPMFLRTotalNearEndUnaviableSecond_Object=MibTableColumn
rcCfmPMFLRTotalNearEndUnaviableSecond=_RcCfmPMFLRTotalNearEndUnaviableSecond_Object((1,3,6,1,4,1,8886,6,1,26,12,1,9),_RcCfmPMFLRTotalNearEndUnaviableSecond_Type())
rcCfmPMFLRTotalNearEndUnaviableSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRTotalNearEndUnaviableSecond.setStatus(_A)
_RcCfmPMFLRCurrentTable_Object=MibTable
rcCfmPMFLRCurrentTable=_RcCfmPMFLRCurrentTable_Object((1,3,6,1,4,1,8886,6,1,26,13))
if mibBuilder.loadTexts:rcCfmPMFLRCurrentTable.setStatus(_A)
_RcCfmPMFLRCurrentEntry_Object=MibTableRow
rcCfmPMFLRCurrentEntry=_RcCfmPMFLRCurrentEntry_Object((1,3,6,1,4,1,8886,6,1,26,13,1))
rcCfmPMFLRCurrentEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_H,_k))
if mibBuilder.loadTexts:rcCfmPMFLRCurrentEntry.setStatus(_A)
class _RcCfmPMFLRCurrentPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rcCfmPMFLRCurrentPeriod15Minutes',1),('rcCfmPMFLRCurrentPeriod24Hours',2)))
_RcCfmPMFLRCurrentPeriod_Type.__name__=_G
_RcCfmPMFLRCurrentPeriod_Object=MibTableColumn
rcCfmPMFLRCurrentPeriod=_RcCfmPMFLRCurrentPeriod_Object((1,3,6,1,4,1,8886,6,1,26,13,1,1),_RcCfmPMFLRCurrentPeriod_Type())
rcCfmPMFLRCurrentPeriod.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmPMFLRCurrentPeriod.setStatus(_A)
_RcCfmPMFLRCurrentElapsedTime_Type=Unsigned32
_RcCfmPMFLRCurrentElapsedTime_Object=MibTableColumn
rcCfmPMFLRCurrentElapsedTime=_RcCfmPMFLRCurrentElapsedTime_Object((1,3,6,1,4,1,8886,6,1,26,13,1,2),_RcCfmPMFLRCurrentElapsedTime_Type())
rcCfmPMFLRCurrentElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRCurrentElapsedTime.setStatus(_A)
_RcCfmPMFLRCurrentFarEndTxFrameCounter_Type=Unsigned32
_RcCfmPMFLRCurrentFarEndTxFrameCounter_Object=MibTableColumn
rcCfmPMFLRCurrentFarEndTxFrameCounter=_RcCfmPMFLRCurrentFarEndTxFrameCounter_Object((1,3,6,1,4,1,8886,6,1,26,13,1,3),_RcCfmPMFLRCurrentFarEndTxFrameCounter_Type())
rcCfmPMFLRCurrentFarEndTxFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRCurrentFarEndTxFrameCounter.setStatus(_A)
_RcCfmPMFLRCurrentFarEndLostFrameCounter_Type=Unsigned32
_RcCfmPMFLRCurrentFarEndLostFrameCounter_Object=MibTableColumn
rcCfmPMFLRCurrentFarEndLostFrameCounter=_RcCfmPMFLRCurrentFarEndLostFrameCounter_Object((1,3,6,1,4,1,8886,6,1,26,13,1,4),_RcCfmPMFLRCurrentFarEndLostFrameCounter_Type())
rcCfmPMFLRCurrentFarEndLostFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRCurrentFarEndLostFrameCounter.setStatus(_A)
class _RcCfmPMFLRCurrentFarEndLossRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCfmPMFLRCurrentFarEndLossRatio_Type.__name__=_F
_RcCfmPMFLRCurrentFarEndLossRatio_Object=MibTableColumn
rcCfmPMFLRCurrentFarEndLossRatio=_RcCfmPMFLRCurrentFarEndLossRatio_Object((1,3,6,1,4,1,8886,6,1,26,13,1,5),_RcCfmPMFLRCurrentFarEndLossRatio_Type())
rcCfmPMFLRCurrentFarEndLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRCurrentFarEndLossRatio.setStatus(_A)
_RcCfmPMFLRCurrentNearEndTxFrameCounter_Type=Unsigned32
_RcCfmPMFLRCurrentNearEndTxFrameCounter_Object=MibTableColumn
rcCfmPMFLRCurrentNearEndTxFrameCounter=_RcCfmPMFLRCurrentNearEndTxFrameCounter_Object((1,3,6,1,4,1,8886,6,1,26,13,1,6),_RcCfmPMFLRCurrentNearEndTxFrameCounter_Type())
rcCfmPMFLRCurrentNearEndTxFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRCurrentNearEndTxFrameCounter.setStatus(_A)
_RcCfmPMFLRCurrentNearEndLostFrameCounter_Type=Unsigned32
_RcCfmPMFLRCurrentNearEndLostFrameCounter_Object=MibTableColumn
rcCfmPMFLRCurrentNearEndLostFrameCounter=_RcCfmPMFLRCurrentNearEndLostFrameCounter_Object((1,3,6,1,4,1,8886,6,1,26,13,1,7),_RcCfmPMFLRCurrentNearEndLostFrameCounter_Type())
rcCfmPMFLRCurrentNearEndLostFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRCurrentNearEndLostFrameCounter.setStatus(_A)
class _RcCfmPMFLRCurrentNearEndLossRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCfmPMFLRCurrentNearEndLossRatio_Type.__name__=_F
_RcCfmPMFLRCurrentNearEndLossRatio_Object=MibTableColumn
rcCfmPMFLRCurrentNearEndLossRatio=_RcCfmPMFLRCurrentNearEndLossRatio_Object((1,3,6,1,4,1,8886,6,1,26,13,1,8),_RcCfmPMFLRCurrentNearEndLossRatio_Type())
rcCfmPMFLRCurrentNearEndLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRCurrentNearEndLossRatio.setStatus(_A)
_RcCfmPMFLRIntervalTable_Object=MibTable
rcCfmPMFLRIntervalTable=_RcCfmPMFLRIntervalTable_Object((1,3,6,1,4,1,8886,6,1,26,14))
if mibBuilder.loadTexts:rcCfmPMFLRIntervalTable.setStatus(_A)
_RcCfmPMFLRIntervalEntry_Object=MibTableRow
rcCfmPMFLRIntervalEntry=_RcCfmPMFLRIntervalEntry_Object((1,3,6,1,4,1,8886,6,1,26,14,1))
rcCfmPMFLRIntervalEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_H,_l),(0,_H,_m))
if mibBuilder.loadTexts:rcCfmPMFLRIntervalEntry.setStatus(_A)
class _RcCfmPMFLRIntervalPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rcCfmPMFLRIntervalPeriod15Minutes',1),('rcCfmPMFLRIntervalPeriod24Hours',2)))
_RcCfmPMFLRIntervalPeriod_Type.__name__=_G
_RcCfmPMFLRIntervalPeriod_Object=MibTableColumn
rcCfmPMFLRIntervalPeriod=_RcCfmPMFLRIntervalPeriod_Object((1,3,6,1,4,1,8886,6,1,26,14,1,1),_RcCfmPMFLRIntervalPeriod_Type())
rcCfmPMFLRIntervalPeriod.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalPeriod.setStatus(_A)
_RcCfmPMFLRIntervalIndex_Type=Unsigned32
_RcCfmPMFLRIntervalIndex_Object=MibTableColumn
rcCfmPMFLRIntervalIndex=_RcCfmPMFLRIntervalIndex_Object((1,3,6,1,4,1,8886,6,1,26,14,1,2),_RcCfmPMFLRIntervalIndex_Type())
rcCfmPMFLRIntervalIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalIndex.setStatus(_A)
_RcCfmPMFLRIntervalPeerMepId_Type=Dot1agCfmMepId
_RcCfmPMFLRIntervalPeerMepId_Object=MibTableColumn
rcCfmPMFLRIntervalPeerMepId=_RcCfmPMFLRIntervalPeerMepId_Object((1,3,6,1,4,1,8886,6,1,26,14,1,3),_RcCfmPMFLRIntervalPeerMepId_Type())
rcCfmPMFLRIntervalPeerMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalPeerMepId.setStatus(_A)
_RcCfmPMFLRIntervalBeginTime_Type=Unsigned32
_RcCfmPMFLRIntervalBeginTime_Object=MibTableColumn
rcCfmPMFLRIntervalBeginTime=_RcCfmPMFLRIntervalBeginTime_Object((1,3,6,1,4,1,8886,6,1,26,14,1,4),_RcCfmPMFLRIntervalBeginTime_Type())
rcCfmPMFLRIntervalBeginTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalBeginTime.setStatus(_A)
_RcCfmPMFLRIntervalFarEndTxFrameCounter_Type=Unsigned32
_RcCfmPMFLRIntervalFarEndTxFrameCounter_Object=MibTableColumn
rcCfmPMFLRIntervalFarEndTxFrameCounter=_RcCfmPMFLRIntervalFarEndTxFrameCounter_Object((1,3,6,1,4,1,8886,6,1,26,14,1,5),_RcCfmPMFLRIntervalFarEndTxFrameCounter_Type())
rcCfmPMFLRIntervalFarEndTxFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalFarEndTxFrameCounter.setStatus(_A)
_RcCfmPMFLRIntervalFarEndLostFrameCounter_Type=Unsigned32
_RcCfmPMFLRIntervalFarEndLostFrameCounter_Object=MibTableColumn
rcCfmPMFLRIntervalFarEndLostFrameCounter=_RcCfmPMFLRIntervalFarEndLostFrameCounter_Object((1,3,6,1,4,1,8886,6,1,26,14,1,6),_RcCfmPMFLRIntervalFarEndLostFrameCounter_Type())
rcCfmPMFLRIntervalFarEndLostFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalFarEndLostFrameCounter.setStatus(_A)
class _RcCfmPMFLRIntervalFarEndLossRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCfmPMFLRIntervalFarEndLossRatio_Type.__name__=_F
_RcCfmPMFLRIntervalFarEndLossRatio_Object=MibTableColumn
rcCfmPMFLRIntervalFarEndLossRatio=_RcCfmPMFLRIntervalFarEndLossRatio_Object((1,3,6,1,4,1,8886,6,1,26,14,1,7),_RcCfmPMFLRIntervalFarEndLossRatio_Type())
rcCfmPMFLRIntervalFarEndLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalFarEndLossRatio.setStatus(_A)
_RcCfmPMFLRIntervalNearEndTxFrameCounter_Type=Unsigned32
_RcCfmPMFLRIntervalNearEndTxFrameCounter_Object=MibTableColumn
rcCfmPMFLRIntervalNearEndTxFrameCounter=_RcCfmPMFLRIntervalNearEndTxFrameCounter_Object((1,3,6,1,4,1,8886,6,1,26,14,1,8),_RcCfmPMFLRIntervalNearEndTxFrameCounter_Type())
rcCfmPMFLRIntervalNearEndTxFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalNearEndTxFrameCounter.setStatus(_A)
_RcCfmPMFLRIntervalNearEndLostFrameCounter_Type=Unsigned32
_RcCfmPMFLRIntervalNearEndLostFrameCounter_Object=MibTableColumn
rcCfmPMFLRIntervalNearEndLostFrameCounter=_RcCfmPMFLRIntervalNearEndLostFrameCounter_Object((1,3,6,1,4,1,8886,6,1,26,14,1,9),_RcCfmPMFLRIntervalNearEndLostFrameCounter_Type())
rcCfmPMFLRIntervalNearEndLostFrameCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalNearEndLostFrameCounter.setStatus(_A)
class _RcCfmPMFLRIntervalNearEndLossRatio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_RcCfmPMFLRIntervalNearEndLossRatio_Type.__name__=_F
_RcCfmPMFLRIntervalNearEndLossRatio_Object=MibTableColumn
rcCfmPMFLRIntervalNearEndLossRatio=_RcCfmPMFLRIntervalNearEndLossRatio_Object((1,3,6,1,4,1,8886,6,1,26,14,1,10),_RcCfmPMFLRIntervalNearEndLossRatio_Type())
rcCfmPMFLRIntervalNearEndLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMFLRIntervalNearEndLossRatio.setStatus(_A)
_RcCfmPMDelayCurrentTable_Object=MibTable
rcCfmPMDelayCurrentTable=_RcCfmPMDelayCurrentTable_Object((1,3,6,1,4,1,8886,6,1,26,15))
if mibBuilder.loadTexts:rcCfmPMDelayCurrentTable.setStatus(_A)
_RcCfmPMDelayCurrentEntry_Object=MibTableRow
rcCfmPMDelayCurrentEntry=_RcCfmPMDelayCurrentEntry_Object((1,3,6,1,4,1,8886,6,1,26,15,1))
rcCfmPMDelayCurrentEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_H,_n))
if mibBuilder.loadTexts:rcCfmPMDelayCurrentEntry.setStatus(_A)
class _RcCfmPMDelayCurrentPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rcCfmPMDelayCurrentPeriod15Minutes',1),('rcCfmPMDelayCurrentPeriod24Hours',2)))
_RcCfmPMDelayCurrentPeriod_Type.__name__=_G
_RcCfmPMDelayCurrentPeriod_Object=MibTableColumn
rcCfmPMDelayCurrentPeriod=_RcCfmPMDelayCurrentPeriod_Object((1,3,6,1,4,1,8886,6,1,26,15,1,1),_RcCfmPMDelayCurrentPeriod_Type())
rcCfmPMDelayCurrentPeriod.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentPeriod.setStatus(_A)
_RcCfmPMDelayCurrentFarEndAboveObjCounter_Type=Unsigned32
_RcCfmPMDelayCurrentFarEndAboveObjCounter_Object=MibTableColumn
rcCfmPMDelayCurrentFarEndAboveObjCounter=_RcCfmPMDelayCurrentFarEndAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,15,1,2),_RcCfmPMDelayCurrentFarEndAboveObjCounter_Type())
rcCfmPMDelayCurrentFarEndAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentFarEndAboveObjCounter.setStatus(_A)
_RcCfmPMDelayCurrentFarEndBelowObjCounter_Type=Unsigned32
_RcCfmPMDelayCurrentFarEndBelowObjCounter_Object=MibTableColumn
rcCfmPMDelayCurrentFarEndBelowObjCounter=_RcCfmPMDelayCurrentFarEndBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,15,1,3),_RcCfmPMDelayCurrentFarEndBelowObjCounter_Type())
rcCfmPMDelayCurrentFarEndBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentFarEndBelowObjCounter.setStatus(_A)
_RcCfmPMDelayCurrentFarEndMaxDelay_Type=Unsigned32
_RcCfmPMDelayCurrentFarEndMaxDelay_Object=MibTableColumn
rcCfmPMDelayCurrentFarEndMaxDelay=_RcCfmPMDelayCurrentFarEndMaxDelay_Object((1,3,6,1,4,1,8886,6,1,26,15,1,4),_RcCfmPMDelayCurrentFarEndMaxDelay_Type())
rcCfmPMDelayCurrentFarEndMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentFarEndMaxDelay.setStatus(_A)
_RcCfmPMDelayCurrentFarEndAvgDelay_Type=Unsigned32
_RcCfmPMDelayCurrentFarEndAvgDelay_Object=MibTableColumn
rcCfmPMDelayCurrentFarEndAvgDelay=_RcCfmPMDelayCurrentFarEndAvgDelay_Object((1,3,6,1,4,1,8886,6,1,26,15,1,5),_RcCfmPMDelayCurrentFarEndAvgDelay_Type())
rcCfmPMDelayCurrentFarEndAvgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentFarEndAvgDelay.setStatus(_A)
_RcCfmPMDelayCurrentFarEndMinDelay_Type=Unsigned32
_RcCfmPMDelayCurrentFarEndMinDelay_Object=MibTableColumn
rcCfmPMDelayCurrentFarEndMinDelay=_RcCfmPMDelayCurrentFarEndMinDelay_Object((1,3,6,1,4,1,8886,6,1,26,15,1,6),_RcCfmPMDelayCurrentFarEndMinDelay_Type())
rcCfmPMDelayCurrentFarEndMinDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentFarEndMinDelay.setStatus(_A)
_RcCfmPMDelayCurrentNearEndAboveObjCounter_Type=Unsigned32
_RcCfmPMDelayCurrentNearEndAboveObjCounter_Object=MibTableColumn
rcCfmPMDelayCurrentNearEndAboveObjCounter=_RcCfmPMDelayCurrentNearEndAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,15,1,7),_RcCfmPMDelayCurrentNearEndAboveObjCounter_Type())
rcCfmPMDelayCurrentNearEndAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentNearEndAboveObjCounter.setStatus(_A)
_RcCfmPMDelayCurrentNearEndBelowObjCounter_Type=Unsigned32
_RcCfmPMDelayCurrentNearEndBelowObjCounter_Object=MibTableColumn
rcCfmPMDelayCurrentNearEndBelowObjCounter=_RcCfmPMDelayCurrentNearEndBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,15,1,8),_RcCfmPMDelayCurrentNearEndBelowObjCounter_Type())
rcCfmPMDelayCurrentNearEndBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentNearEndBelowObjCounter.setStatus(_A)
_RcCfmPMDelayCurrentNearEndMaxDelay_Type=Unsigned32
_RcCfmPMDelayCurrentNearEndMaxDelay_Object=MibTableColumn
rcCfmPMDelayCurrentNearEndMaxDelay=_RcCfmPMDelayCurrentNearEndMaxDelay_Object((1,3,6,1,4,1,8886,6,1,26,15,1,9),_RcCfmPMDelayCurrentNearEndMaxDelay_Type())
rcCfmPMDelayCurrentNearEndMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentNearEndMaxDelay.setStatus(_A)
_RcCfmPMDelayCurrentNearEndAvgDelay_Type=Unsigned32
_RcCfmPMDelayCurrentNearEndAvgDelay_Object=MibTableColumn
rcCfmPMDelayCurrentNearEndAvgDelay=_RcCfmPMDelayCurrentNearEndAvgDelay_Object((1,3,6,1,4,1,8886,6,1,26,15,1,10),_RcCfmPMDelayCurrentNearEndAvgDelay_Type())
rcCfmPMDelayCurrentNearEndAvgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentNearEndAvgDelay.setStatus(_A)
_RcCfmPMDelayCurrentNearEndMinDelay_Type=Unsigned32
_RcCfmPMDelayCurrentNearEndMinDelay_Object=MibTableColumn
rcCfmPMDelayCurrentNearEndMinDelay=_RcCfmPMDelayCurrentNearEndMinDelay_Object((1,3,6,1,4,1,8886,6,1,26,15,1,11),_RcCfmPMDelayCurrentNearEndMinDelay_Type())
rcCfmPMDelayCurrentNearEndMinDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentNearEndMinDelay.setStatus(_A)
_RcCfmPMDelayCurrentRoundTripAboveObjCounter_Type=Unsigned32
_RcCfmPMDelayCurrentRoundTripAboveObjCounter_Object=MibTableColumn
rcCfmPMDelayCurrentRoundTripAboveObjCounter=_RcCfmPMDelayCurrentRoundTripAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,15,1,12),_RcCfmPMDelayCurrentRoundTripAboveObjCounter_Type())
rcCfmPMDelayCurrentRoundTripAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentRoundTripAboveObjCounter.setStatus(_A)
_RcCfmPMDelayCurrentRoundTripBelowObjCounter_Type=Unsigned32
_RcCfmPMDelayCurrentRoundTripBelowObjCounter_Object=MibTableColumn
rcCfmPMDelayCurrentRoundTripBelowObjCounter=_RcCfmPMDelayCurrentRoundTripBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,15,1,13),_RcCfmPMDelayCurrentRoundTripBelowObjCounter_Type())
rcCfmPMDelayCurrentRoundTripBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentRoundTripBelowObjCounter.setStatus(_A)
_RcCfmPMDelayCurrentRoundTripMaxDelay_Type=Unsigned32
_RcCfmPMDelayCurrentRoundTripMaxDelay_Object=MibTableColumn
rcCfmPMDelayCurrentRoundTripMaxDelay=_RcCfmPMDelayCurrentRoundTripMaxDelay_Object((1,3,6,1,4,1,8886,6,1,26,15,1,14),_RcCfmPMDelayCurrentRoundTripMaxDelay_Type())
rcCfmPMDelayCurrentRoundTripMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentRoundTripMaxDelay.setStatus(_A)
_RcCfmPMDelayCurrentRoundTripAvgDelay_Type=Unsigned32
_RcCfmPMDelayCurrentRoundTripAvgDelay_Object=MibTableColumn
rcCfmPMDelayCurrentRoundTripAvgDelay=_RcCfmPMDelayCurrentRoundTripAvgDelay_Object((1,3,6,1,4,1,8886,6,1,26,15,1,15),_RcCfmPMDelayCurrentRoundTripAvgDelay_Type())
rcCfmPMDelayCurrentRoundTripAvgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentRoundTripAvgDelay.setStatus(_A)
_RcCfmPMDelayCurrentRoundTripMinDelay_Type=Unsigned32
_RcCfmPMDelayCurrentRoundTripMinDelay_Object=MibTableColumn
rcCfmPMDelayCurrentRoundTripMinDelay=_RcCfmPMDelayCurrentRoundTripMinDelay_Object((1,3,6,1,4,1,8886,6,1,26,15,1,16),_RcCfmPMDelayCurrentRoundTripMinDelay_Type())
rcCfmPMDelayCurrentRoundTripMinDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayCurrentRoundTripMinDelay.setStatus(_A)
_RcCfmPMDelayIntervalTable_Object=MibTable
rcCfmPMDelayIntervalTable=_RcCfmPMDelayIntervalTable_Object((1,3,6,1,4,1,8886,6,1,26,16))
if mibBuilder.loadTexts:rcCfmPMDelayIntervalTable.setStatus(_A)
_RcCfmPMDelayIntervalEntry_Object=MibTableRow
rcCfmPMDelayIntervalEntry=_RcCfmPMDelayIntervalEntry_Object((1,3,6,1,4,1,8886,6,1,26,16,1))
rcCfmPMDelayIntervalEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_H,_o),(0,_H,_p))
if mibBuilder.loadTexts:rcCfmPMDelayIntervalEntry.setStatus(_A)
class _RcCfmPMDelayIntervalPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rcCfmPMDelayIntervalPeriod15Minutes',1),('rcCfmPMDelayIntervalPeriod24Hours',2)))
_RcCfmPMDelayIntervalPeriod_Type.__name__=_G
_RcCfmPMDelayIntervalPeriod_Object=MibTableColumn
rcCfmPMDelayIntervalPeriod=_RcCfmPMDelayIntervalPeriod_Object((1,3,6,1,4,1,8886,6,1,26,16,1,1),_RcCfmPMDelayIntervalPeriod_Type())
rcCfmPMDelayIntervalPeriod.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalPeriod.setStatus(_A)
_RcCfmPMDelayIntervalIndex_Type=Unsigned32
_RcCfmPMDelayIntervalIndex_Object=MibTableColumn
rcCfmPMDelayIntervalIndex=_RcCfmPMDelayIntervalIndex_Object((1,3,6,1,4,1,8886,6,1,26,16,1,2),_RcCfmPMDelayIntervalIndex_Type())
rcCfmPMDelayIntervalIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalIndex.setStatus(_A)
_RcCfmPMDelayIntervalBeginTime_Type=Unsigned32
_RcCfmPMDelayIntervalBeginTime_Object=MibTableColumn
rcCfmPMDelayIntervalBeginTime=_RcCfmPMDelayIntervalBeginTime_Object((1,3,6,1,4,1,8886,6,1,26,16,1,3),_RcCfmPMDelayIntervalBeginTime_Type())
rcCfmPMDelayIntervalBeginTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalBeginTime.setStatus(_A)
_RcCfmPMDelayIntervalPeerMepId_Type=Dot1agCfmMepId
_RcCfmPMDelayIntervalPeerMepId_Object=MibTableColumn
rcCfmPMDelayIntervalPeerMepId=_RcCfmPMDelayIntervalPeerMepId_Object((1,3,6,1,4,1,8886,6,1,26,16,1,4),_RcCfmPMDelayIntervalPeerMepId_Type())
rcCfmPMDelayIntervalPeerMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalPeerMepId.setStatus(_A)
_RcCfmPMDelayIntervalFarEndAboveObjCounter_Type=Unsigned32
_RcCfmPMDelayIntervalFarEndAboveObjCounter_Object=MibTableColumn
rcCfmPMDelayIntervalFarEndAboveObjCounter=_RcCfmPMDelayIntervalFarEndAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,16,1,5),_RcCfmPMDelayIntervalFarEndAboveObjCounter_Type())
rcCfmPMDelayIntervalFarEndAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalFarEndAboveObjCounter.setStatus(_A)
_RcCfmPMDelayIntervalFarEndBelowObjCounter_Type=Unsigned32
_RcCfmPMDelayIntervalFarEndBelowObjCounter_Object=MibTableColumn
rcCfmPMDelayIntervalFarEndBelowObjCounter=_RcCfmPMDelayIntervalFarEndBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,16,1,6),_RcCfmPMDelayIntervalFarEndBelowObjCounter_Type())
rcCfmPMDelayIntervalFarEndBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalFarEndBelowObjCounter.setStatus(_A)
_RcCfmPMDelayIntervalFarEndMaxDelay_Type=Unsigned32
_RcCfmPMDelayIntervalFarEndMaxDelay_Object=MibTableColumn
rcCfmPMDelayIntervalFarEndMaxDelay=_RcCfmPMDelayIntervalFarEndMaxDelay_Object((1,3,6,1,4,1,8886,6,1,26,16,1,7),_RcCfmPMDelayIntervalFarEndMaxDelay_Type())
rcCfmPMDelayIntervalFarEndMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalFarEndMaxDelay.setStatus(_A)
_RcCfmPMDelayIntervalFarEndAvgDelay_Type=Unsigned32
_RcCfmPMDelayIntervalFarEndAvgDelay_Object=MibTableColumn
rcCfmPMDelayIntervalFarEndAvgDelay=_RcCfmPMDelayIntervalFarEndAvgDelay_Object((1,3,6,1,4,1,8886,6,1,26,16,1,8),_RcCfmPMDelayIntervalFarEndAvgDelay_Type())
rcCfmPMDelayIntervalFarEndAvgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalFarEndAvgDelay.setStatus(_A)
_RcCfmPMDelayIntervalFarEndMinDelay_Type=Unsigned32
_RcCfmPMDelayIntervalFarEndMinDelay_Object=MibTableColumn
rcCfmPMDelayIntervalFarEndMinDelay=_RcCfmPMDelayIntervalFarEndMinDelay_Object((1,3,6,1,4,1,8886,6,1,26,16,1,9),_RcCfmPMDelayIntervalFarEndMinDelay_Type())
rcCfmPMDelayIntervalFarEndMinDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalFarEndMinDelay.setStatus(_A)
_RcCfmPMDelayIntervalNearEndAboveObjCounter_Type=Unsigned32
_RcCfmPMDelayIntervalNearEndAboveObjCounter_Object=MibTableColumn
rcCfmPMDelayIntervalNearEndAboveObjCounter=_RcCfmPMDelayIntervalNearEndAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,16,1,10),_RcCfmPMDelayIntervalNearEndAboveObjCounter_Type())
rcCfmPMDelayIntervalNearEndAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalNearEndAboveObjCounter.setStatus(_A)
_RcCfmPMDelayIntervalNearEndBelowObjCounter_Type=Unsigned32
_RcCfmPMDelayIntervalNearEndBelowObjCounter_Object=MibTableColumn
rcCfmPMDelayIntervalNearEndBelowObjCounter=_RcCfmPMDelayIntervalNearEndBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,16,1,11),_RcCfmPMDelayIntervalNearEndBelowObjCounter_Type())
rcCfmPMDelayIntervalNearEndBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalNearEndBelowObjCounter.setStatus(_A)
_RcCfmPMDelayIntervalNearEndMaxDelay_Type=Unsigned32
_RcCfmPMDelayIntervalNearEndMaxDelay_Object=MibTableColumn
rcCfmPMDelayIntervalNearEndMaxDelay=_RcCfmPMDelayIntervalNearEndMaxDelay_Object((1,3,6,1,4,1,8886,6,1,26,16,1,12),_RcCfmPMDelayIntervalNearEndMaxDelay_Type())
rcCfmPMDelayIntervalNearEndMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalNearEndMaxDelay.setStatus(_C)
_RcCfmPMDelayIntervalNearEndAvgDelay_Type=Unsigned32
_RcCfmPMDelayIntervalNearEndAvgDelay_Object=MibTableColumn
rcCfmPMDelayIntervalNearEndAvgDelay=_RcCfmPMDelayIntervalNearEndAvgDelay_Object((1,3,6,1,4,1,8886,6,1,26,16,1,13),_RcCfmPMDelayIntervalNearEndAvgDelay_Type())
rcCfmPMDelayIntervalNearEndAvgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalNearEndAvgDelay.setStatus(_A)
_RcCfmPMDelayIntervalNearEndMinDelay_Type=Unsigned32
_RcCfmPMDelayIntervalNearEndMinDelay_Object=MibTableColumn
rcCfmPMDelayIntervalNearEndMinDelay=_RcCfmPMDelayIntervalNearEndMinDelay_Object((1,3,6,1,4,1,8886,6,1,26,16,1,14),_RcCfmPMDelayIntervalNearEndMinDelay_Type())
rcCfmPMDelayIntervalNearEndMinDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalNearEndMinDelay.setStatus(_A)
_RcCfmPMDelayIntervalRoundTripAboveObjCounter_Type=Unsigned32
_RcCfmPMDelayIntervalRoundTripAboveObjCounter_Object=MibTableColumn
rcCfmPMDelayIntervalRoundTripAboveObjCounter=_RcCfmPMDelayIntervalRoundTripAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,16,1,15),_RcCfmPMDelayIntervalRoundTripAboveObjCounter_Type())
rcCfmPMDelayIntervalRoundTripAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalRoundTripAboveObjCounter.setStatus(_A)
_RcCfmPMDelayIntervalRoundTripBelowObjCounter_Type=Unsigned32
_RcCfmPMDelayIntervalRoundTripBelowObjCounter_Object=MibTableColumn
rcCfmPMDelayIntervalRoundTripBelowObjCounter=_RcCfmPMDelayIntervalRoundTripBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,16,1,16),_RcCfmPMDelayIntervalRoundTripBelowObjCounter_Type())
rcCfmPMDelayIntervalRoundTripBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalRoundTripBelowObjCounter.setStatus(_A)
_RcCfmPMDelayIntervalRoundTripMaxDelay_Type=Unsigned32
_RcCfmPMDelayIntervalRoundTripMaxDelay_Object=MibTableColumn
rcCfmPMDelayIntervalRoundTripMaxDelay=_RcCfmPMDelayIntervalRoundTripMaxDelay_Object((1,3,6,1,4,1,8886,6,1,26,16,1,17),_RcCfmPMDelayIntervalRoundTripMaxDelay_Type())
rcCfmPMDelayIntervalRoundTripMaxDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalRoundTripMaxDelay.setStatus(_A)
_RcCfmPMDelayIntervalRoundTripAvgDelay_Type=Unsigned32
_RcCfmPMDelayIntervalRoundTripAvgDelay_Object=MibTableColumn
rcCfmPMDelayIntervalRoundTripAvgDelay=_RcCfmPMDelayIntervalRoundTripAvgDelay_Object((1,3,6,1,4,1,8886,6,1,26,16,1,18),_RcCfmPMDelayIntervalRoundTripAvgDelay_Type())
rcCfmPMDelayIntervalRoundTripAvgDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalRoundTripAvgDelay.setStatus(_A)
_RcCfmPMDelayIntervalRoundTripMinDelay_Type=Unsigned32
_RcCfmPMDelayIntervalRoundTripMinDelay_Object=MibTableColumn
rcCfmPMDelayIntervalRoundTripMinDelay=_RcCfmPMDelayIntervalRoundTripMinDelay_Object((1,3,6,1,4,1,8886,6,1,26,16,1,19),_RcCfmPMDelayIntervalRoundTripMinDelay_Type())
rcCfmPMDelayIntervalRoundTripMinDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDelayIntervalRoundTripMinDelay.setStatus(_A)
_RcCfmPMDVCurrentTable_Object=MibTable
rcCfmPMDVCurrentTable=_RcCfmPMDVCurrentTable_Object((1,3,6,1,4,1,8886,6,1,26,17))
if mibBuilder.loadTexts:rcCfmPMDVCurrentTable.setStatus(_A)
_RcCfmPMDVCurrentEntry_Object=MibTableRow
rcCfmPMDVCurrentEntry=_RcCfmPMDVCurrentEntry_Object((1,3,6,1,4,1,8886,6,1,26,17,1))
rcCfmPMDVCurrentEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_H,_q))
if mibBuilder.loadTexts:rcCfmPMDVCurrentEntry.setStatus(_A)
class _RcCfmPMDVCurrentPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rcCfmPMDVCurrentPeriod15Minutes',1),('rcCfmPMDVCurrentPeriod24Hours',2)))
_RcCfmPMDVCurrentPeriod_Type.__name__=_G
_RcCfmPMDVCurrentPeriod_Object=MibTableColumn
rcCfmPMDVCurrentPeriod=_RcCfmPMDVCurrentPeriod_Object((1,3,6,1,4,1,8886,6,1,26,17,1,1),_RcCfmPMDVCurrentPeriod_Type())
rcCfmPMDVCurrentPeriod.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmPMDVCurrentPeriod.setStatus(_A)
_RcCfmPMDVCurrentFarEndAboveObjCounter_Type=Unsigned32
_RcCfmPMDVCurrentFarEndAboveObjCounter_Object=MibTableColumn
rcCfmPMDVCurrentFarEndAboveObjCounter=_RcCfmPMDVCurrentFarEndAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,17,1,2),_RcCfmPMDVCurrentFarEndAboveObjCounter_Type())
rcCfmPMDVCurrentFarEndAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentFarEndAboveObjCounter.setStatus(_A)
_RcCfmPMDVCurrentFarEndBelowObjCounter_Type=Unsigned32
_RcCfmPMDVCurrentFarEndBelowObjCounter_Object=MibTableColumn
rcCfmPMDVCurrentFarEndBelowObjCounter=_RcCfmPMDVCurrentFarEndBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,17,1,3),_RcCfmPMDVCurrentFarEndBelowObjCounter_Type())
rcCfmPMDVCurrentFarEndBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentFarEndBelowObjCounter.setStatus(_A)
_RcCfmPMDVCurrentFarEndMaxDv_Type=Unsigned32
_RcCfmPMDVCurrentFarEndMaxDv_Object=MibTableColumn
rcCfmPMDVCurrentFarEndMaxDv=_RcCfmPMDVCurrentFarEndMaxDv_Object((1,3,6,1,4,1,8886,6,1,26,17,1,4),_RcCfmPMDVCurrentFarEndMaxDv_Type())
rcCfmPMDVCurrentFarEndMaxDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentFarEndMaxDv.setStatus(_A)
_RcCfmPMDVCurrentFarEndAvgDv_Type=Unsigned32
_RcCfmPMDVCurrentFarEndAvgDv_Object=MibTableColumn
rcCfmPMDVCurrentFarEndAvgDv=_RcCfmPMDVCurrentFarEndAvgDv_Object((1,3,6,1,4,1,8886,6,1,26,17,1,5),_RcCfmPMDVCurrentFarEndAvgDv_Type())
rcCfmPMDVCurrentFarEndAvgDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentFarEndAvgDv.setStatus(_A)
_RcCfmPMDVCurrentNearEndAboveObjCounter_Type=Unsigned32
_RcCfmPMDVCurrentNearEndAboveObjCounter_Object=MibTableColumn
rcCfmPMDVCurrentNearEndAboveObjCounter=_RcCfmPMDVCurrentNearEndAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,17,1,6),_RcCfmPMDVCurrentNearEndAboveObjCounter_Type())
rcCfmPMDVCurrentNearEndAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentNearEndAboveObjCounter.setStatus(_A)
_RcCfmPMDVCurrentNearEndBelowObjCounter_Type=Unsigned32
_RcCfmPMDVCurrentNearEndBelowObjCounter_Object=MibTableColumn
rcCfmPMDVCurrentNearEndBelowObjCounter=_RcCfmPMDVCurrentNearEndBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,17,1,7),_RcCfmPMDVCurrentNearEndBelowObjCounter_Type())
rcCfmPMDVCurrentNearEndBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentNearEndBelowObjCounter.setStatus(_A)
_RcCfmPMDVCurrentNearEndMaxDv_Type=Unsigned32
_RcCfmPMDVCurrentNearEndMaxDv_Object=MibTableColumn
rcCfmPMDVCurrentNearEndMaxDv=_RcCfmPMDVCurrentNearEndMaxDv_Object((1,3,6,1,4,1,8886,6,1,26,17,1,8),_RcCfmPMDVCurrentNearEndMaxDv_Type())
rcCfmPMDVCurrentNearEndMaxDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentNearEndMaxDv.setStatus(_A)
_RcCfmPMDVCurrentNearEndAvgDv_Type=Unsigned32
_RcCfmPMDVCurrentNearEndAvgDv_Object=MibTableColumn
rcCfmPMDVCurrentNearEndAvgDv=_RcCfmPMDVCurrentNearEndAvgDv_Object((1,3,6,1,4,1,8886,6,1,26,17,1,9),_RcCfmPMDVCurrentNearEndAvgDv_Type())
rcCfmPMDVCurrentNearEndAvgDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentNearEndAvgDv.setStatus(_A)
_RcCfmPMDVCurrentRoundTripAboveObjCounter_Type=Unsigned32
_RcCfmPMDVCurrentRoundTripAboveObjCounter_Object=MibTableColumn
rcCfmPMDVCurrentRoundTripAboveObjCounter=_RcCfmPMDVCurrentRoundTripAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,17,1,10),_RcCfmPMDVCurrentRoundTripAboveObjCounter_Type())
rcCfmPMDVCurrentRoundTripAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentRoundTripAboveObjCounter.setStatus(_A)
_RcCfmPMDVCurrentRoundTripBelowObjCounter_Type=Unsigned32
_RcCfmPMDVCurrentRoundTripBelowObjCounter_Object=MibTableColumn
rcCfmPMDVCurrentRoundTripBelowObjCounter=_RcCfmPMDVCurrentRoundTripBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,17,1,11),_RcCfmPMDVCurrentRoundTripBelowObjCounter_Type())
rcCfmPMDVCurrentRoundTripBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentRoundTripBelowObjCounter.setStatus(_A)
_RcCfmPMDVCurrentRoundTripMaxDv_Type=Unsigned32
_RcCfmPMDVCurrentRoundTripMaxDv_Object=MibTableColumn
rcCfmPMDVCurrentRoundTripMaxDv=_RcCfmPMDVCurrentRoundTripMaxDv_Object((1,3,6,1,4,1,8886,6,1,26,17,1,12),_RcCfmPMDVCurrentRoundTripMaxDv_Type())
rcCfmPMDVCurrentRoundTripMaxDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentRoundTripMaxDv.setStatus(_A)
_RcCfmPMDVCurrentRoundTripAvgDv_Type=Unsigned32
_RcCfmPMDVCurrentRoundTripAvgDv_Object=MibTableColumn
rcCfmPMDVCurrentRoundTripAvgDv=_RcCfmPMDVCurrentRoundTripAvgDv_Object((1,3,6,1,4,1,8886,6,1,26,17,1,13),_RcCfmPMDVCurrentRoundTripAvgDv_Type())
rcCfmPMDVCurrentRoundTripAvgDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVCurrentRoundTripAvgDv.setStatus(_A)
_RcCfmPMDVIntervalTable_Object=MibTable
rcCfmPMDVIntervalTable=_RcCfmPMDVIntervalTable_Object((1,3,6,1,4,1,8886,6,1,26,18))
if mibBuilder.loadTexts:rcCfmPMDVIntervalTable.setStatus(_A)
_RcCfmPMDVIntervalEntry_Object=MibTableRow
rcCfmPMDVIntervalEntry=_RcCfmPMDVIntervalEntry_Object((1,3,6,1,4,1,8886,6,1,26,18,1))
rcCfmPMDVIntervalEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_H,_r),(0,_H,_s))
if mibBuilder.loadTexts:rcCfmPMDVIntervalEntry.setStatus(_A)
class _RcCfmPMDVIntervalPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rcCfmPMDVIntervalPeriod15Minutes',1),('rcCfmPMDVIntervalPeriod24Hours',2)))
_RcCfmPMDVIntervalPeriod_Type.__name__=_G
_RcCfmPMDVIntervalPeriod_Object=MibTableColumn
rcCfmPMDVIntervalPeriod=_RcCfmPMDVIntervalPeriod_Object((1,3,6,1,4,1,8886,6,1,26,18,1,1),_RcCfmPMDVIntervalPeriod_Type())
rcCfmPMDVIntervalPeriod.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmPMDVIntervalPeriod.setStatus(_A)
_RcCfmPMDVIntervalIndex_Type=Unsigned32
_RcCfmPMDVIntervalIndex_Object=MibTableColumn
rcCfmPMDVIntervalIndex=_RcCfmPMDVIntervalIndex_Object((1,3,6,1,4,1,8886,6,1,26,18,1,2),_RcCfmPMDVIntervalIndex_Type())
rcCfmPMDVIntervalIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:rcCfmPMDVIntervalIndex.setStatus(_A)
_RcCfmPMDVIntervalBeginTime_Type=Unsigned32
_RcCfmPMDVIntervalBeginTime_Object=MibTableColumn
rcCfmPMDVIntervalBeginTime=_RcCfmPMDVIntervalBeginTime_Object((1,3,6,1,4,1,8886,6,1,26,18,1,3),_RcCfmPMDVIntervalBeginTime_Type())
rcCfmPMDVIntervalBeginTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalBeginTime.setStatus(_A)
_RcCfmPMDVIntervalPeerMepId_Type=Dot1agCfmMepId
_RcCfmPMDVIntervalPeerMepId_Object=MibTableColumn
rcCfmPMDVIntervalPeerMepId=_RcCfmPMDVIntervalPeerMepId_Object((1,3,6,1,4,1,8886,6,1,26,18,1,4),_RcCfmPMDVIntervalPeerMepId_Type())
rcCfmPMDVIntervalPeerMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalPeerMepId.setStatus(_A)
_RcCfmPMDVIntervalFarEndAboveObjCounter_Type=Unsigned32
_RcCfmPMDVIntervalFarEndAboveObjCounter_Object=MibTableColumn
rcCfmPMDVIntervalFarEndAboveObjCounter=_RcCfmPMDVIntervalFarEndAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,18,1,5),_RcCfmPMDVIntervalFarEndAboveObjCounter_Type())
rcCfmPMDVIntervalFarEndAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalFarEndAboveObjCounter.setStatus(_A)
_RcCfmPMDVIntervalFarEndBelowObjCounter_Type=Unsigned32
_RcCfmPMDVIntervalFarEndBelowObjCounter_Object=MibTableColumn
rcCfmPMDVIntervalFarEndBelowObjCounter=_RcCfmPMDVIntervalFarEndBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,18,1,6),_RcCfmPMDVIntervalFarEndBelowObjCounter_Type())
rcCfmPMDVIntervalFarEndBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalFarEndBelowObjCounter.setStatus(_A)
_RcCfmPMDVIntervalFarEndMaxDv_Type=Unsigned32
_RcCfmPMDVIntervalFarEndMaxDv_Object=MibTableColumn
rcCfmPMDVIntervalFarEndMaxDv=_RcCfmPMDVIntervalFarEndMaxDv_Object((1,3,6,1,4,1,8886,6,1,26,18,1,7),_RcCfmPMDVIntervalFarEndMaxDv_Type())
rcCfmPMDVIntervalFarEndMaxDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalFarEndMaxDv.setStatus(_A)
_RcCfmPMDVIntervalFarEndAvgDv_Type=Unsigned32
_RcCfmPMDVIntervalFarEndAvgDv_Object=MibTableColumn
rcCfmPMDVIntervalFarEndAvgDv=_RcCfmPMDVIntervalFarEndAvgDv_Object((1,3,6,1,4,1,8886,6,1,26,18,1,8),_RcCfmPMDVIntervalFarEndAvgDv_Type())
rcCfmPMDVIntervalFarEndAvgDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalFarEndAvgDv.setStatus(_A)
_RcCfmPMDVIntervalNearEndAboveObjCounter_Type=Unsigned32
_RcCfmPMDVIntervalNearEndAboveObjCounter_Object=MibTableColumn
rcCfmPMDVIntervalNearEndAboveObjCounter=_RcCfmPMDVIntervalNearEndAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,18,1,9),_RcCfmPMDVIntervalNearEndAboveObjCounter_Type())
rcCfmPMDVIntervalNearEndAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalNearEndAboveObjCounter.setStatus(_A)
_RcCfmPMDVIntervalNearEndBelowObjCounter_Type=Unsigned32
_RcCfmPMDVIntervalNearEndBelowObjCounter_Object=MibTableColumn
rcCfmPMDVIntervalNearEndBelowObjCounter=_RcCfmPMDVIntervalNearEndBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,18,1,10),_RcCfmPMDVIntervalNearEndBelowObjCounter_Type())
rcCfmPMDVIntervalNearEndBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalNearEndBelowObjCounter.setStatus(_A)
_RcCfmPMDVIntervalNearEndMaxDv_Type=Unsigned32
_RcCfmPMDVIntervalNearEndMaxDv_Object=MibTableColumn
rcCfmPMDVIntervalNearEndMaxDv=_RcCfmPMDVIntervalNearEndMaxDv_Object((1,3,6,1,4,1,8886,6,1,26,18,1,11),_RcCfmPMDVIntervalNearEndMaxDv_Type())
rcCfmPMDVIntervalNearEndMaxDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalNearEndMaxDv.setStatus(_A)
_RcCfmPMDVIntervalNearEndAvgDv_Type=Unsigned32
_RcCfmPMDVIntervalNearEndAvgDv_Object=MibTableColumn
rcCfmPMDVIntervalNearEndAvgDv=_RcCfmPMDVIntervalNearEndAvgDv_Object((1,3,6,1,4,1,8886,6,1,26,18,1,12),_RcCfmPMDVIntervalNearEndAvgDv_Type())
rcCfmPMDVIntervalNearEndAvgDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalNearEndAvgDv.setStatus(_A)
_RcCfmPMDVIntervalRoundTripAboveObjCounter_Type=Unsigned32
_RcCfmPMDVIntervalRoundTripAboveObjCounter_Object=MibTableColumn
rcCfmPMDVIntervalRoundTripAboveObjCounter=_RcCfmPMDVIntervalRoundTripAboveObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,18,1,13),_RcCfmPMDVIntervalRoundTripAboveObjCounter_Type())
rcCfmPMDVIntervalRoundTripAboveObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalRoundTripAboveObjCounter.setStatus(_A)
_RcCfmPMDVIntervalRoundTripBelowObjCounter_Type=Unsigned32
_RcCfmPMDVIntervalRoundTripBelowObjCounter_Object=MibTableColumn
rcCfmPMDVIntervalRoundTripBelowObjCounter=_RcCfmPMDVIntervalRoundTripBelowObjCounter_Object((1,3,6,1,4,1,8886,6,1,26,18,1,14),_RcCfmPMDVIntervalRoundTripBelowObjCounter_Type())
rcCfmPMDVIntervalRoundTripBelowObjCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalRoundTripBelowObjCounter.setStatus(_A)
_RcCfmPMDVIntervalRoundTripMaxDv_Type=Unsigned32
_RcCfmPMDVIntervalRoundTripMaxDv_Object=MibTableColumn
rcCfmPMDVIntervalRoundTripMaxDv=_RcCfmPMDVIntervalRoundTripMaxDv_Object((1,3,6,1,4,1,8886,6,1,26,18,1,15),_RcCfmPMDVIntervalRoundTripMaxDv_Type())
rcCfmPMDVIntervalRoundTripMaxDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalRoundTripMaxDv.setStatus(_A)
_RcCfmPMDVIntervalRoundTripAvgDv_Type=Unsigned32
_RcCfmPMDVIntervalRoundTripAvgDv_Object=MibTableColumn
rcCfmPMDVIntervalRoundTripAvgDv=_RcCfmPMDVIntervalRoundTripAvgDv_Object((1,3,6,1,4,1,8886,6,1,26,18,1,16),_RcCfmPMDVIntervalRoundTripAvgDv_Type())
rcCfmPMDVIntervalRoundTripAvgDv.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMDVIntervalRoundTripAvgDv.setStatus(_A)
_RcCfmPMThroughputTable_Object=MibTable
rcCfmPMThroughputTable=_RcCfmPMThroughputTable_Object((1,3,6,1,4,1,8886,6,1,26,19))
if mibBuilder.loadTexts:rcCfmPMThroughputTable.setStatus(_A)
_RcCfmPMThroughputEntry_Object=MibTableRow
rcCfmPMThroughputEntry=_RcCfmPMThroughputEntry_Object((1,3,6,1,4,1,8886,6,1,26,19,1))
rcCfmPMThroughputEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_D,_Y))
if mibBuilder.loadTexts:rcCfmPMThroughputEntry.setStatus(_A)
class _RcCfmPMThroughputTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('successed',0),('unknownReasonFailed',1),('localReourceConflict',2),('remoteResourceConflict',3),('vsxTimeOut',4)))
_RcCfmPMThroughputTestResult_Type.__name__=_G
_RcCfmPMThroughputTestResult_Object=MibTableColumn
rcCfmPMThroughputTestResult=_RcCfmPMThroughputTestResult_Object((1,3,6,1,4,1,8886,6,1,26,19,1,1),_RcCfmPMThroughputTestResult_Type())
rcCfmPMThroughputTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputTestResult.setStatus(_A)
class _RcCfmPMThroughputTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',0),('farEndStart',1),('farEndSend',2),('farEndTest',3),('nearEndStart',4),('nearEndTest',5),('nearEndClose',6)))
_RcCfmPMThroughputTestState_Type.__name__=_G
_RcCfmPMThroughputTestState_Object=MibTableColumn
rcCfmPMThroughputTestState=_RcCfmPMThroughputTestState_Object((1,3,6,1,4,1,8886,6,1,26,19,1,2),_RcCfmPMThroughputTestState_Type())
rcCfmPMThroughputTestState.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputTestState.setStatus(_A)
_RcCfmPMThroughputFarEndSendbps_Type=Counter64
_RcCfmPMThroughputFarEndSendbps_Object=MibTableColumn
rcCfmPMThroughputFarEndSendbps=_RcCfmPMThroughputFarEndSendbps_Object((1,3,6,1,4,1,8886,6,1,26,19,1,3),_RcCfmPMThroughputFarEndSendbps_Type())
rcCfmPMThroughputFarEndSendbps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputFarEndSendbps.setStatus(_A)
_RcCfmPMThroughputFarEndRecievebps_Type=Counter64
_RcCfmPMThroughputFarEndRecievebps_Object=MibTableColumn
rcCfmPMThroughputFarEndRecievebps=_RcCfmPMThroughputFarEndRecievebps_Object((1,3,6,1,4,1,8886,6,1,26,19,1,4),_RcCfmPMThroughputFarEndRecievebps_Type())
rcCfmPMThroughputFarEndRecievebps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputFarEndRecievebps.setStatus(_A)
_RcCfmPMThroughputFarEndSendpps_Type=Counter64
_RcCfmPMThroughputFarEndSendpps_Object=MibTableColumn
rcCfmPMThroughputFarEndSendpps=_RcCfmPMThroughputFarEndSendpps_Object((1,3,6,1,4,1,8886,6,1,26,19,1,5),_RcCfmPMThroughputFarEndSendpps_Type())
rcCfmPMThroughputFarEndSendpps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputFarEndSendpps.setStatus(_A)
_RcCfmPMThroughputFarEndRecievepps_Type=Counter64
_RcCfmPMThroughputFarEndRecievepps_Object=MibTableColumn
rcCfmPMThroughputFarEndRecievepps=_RcCfmPMThroughputFarEndRecievepps_Object((1,3,6,1,4,1,8886,6,1,26,19,1,6),_RcCfmPMThroughputFarEndRecievepps_Type())
rcCfmPMThroughputFarEndRecievepps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputFarEndRecievepps.setStatus(_A)
_RcCfmPMThroughputNearEndSendbps_Type=Counter64
_RcCfmPMThroughputNearEndSendbps_Object=MibTableColumn
rcCfmPMThroughputNearEndSendbps=_RcCfmPMThroughputNearEndSendbps_Object((1,3,6,1,4,1,8886,6,1,26,19,1,7),_RcCfmPMThroughputNearEndSendbps_Type())
rcCfmPMThroughputNearEndSendbps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputNearEndSendbps.setStatus(_A)
_RcCfmPMThroughputNearEndRecievebps_Type=Counter64
_RcCfmPMThroughputNearEndRecievebps_Object=MibTableColumn
rcCfmPMThroughputNearEndRecievebps=_RcCfmPMThroughputNearEndRecievebps_Object((1,3,6,1,4,1,8886,6,1,26,19,1,8),_RcCfmPMThroughputNearEndRecievebps_Type())
rcCfmPMThroughputNearEndRecievebps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputNearEndRecievebps.setStatus(_A)
_RcCfmPMThroughputNearEndSendpps_Type=Counter64
_RcCfmPMThroughputNearEndSendpps_Object=MibTableColumn
rcCfmPMThroughputNearEndSendpps=_RcCfmPMThroughputNearEndSendpps_Object((1,3,6,1,4,1,8886,6,1,26,19,1,9),_RcCfmPMThroughputNearEndSendpps_Type())
rcCfmPMThroughputNearEndSendpps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputNearEndSendpps.setStatus(_A)
_RcCfmPMThroughputNearEndRecievepps_Type=Counter64
_RcCfmPMThroughputNearEndRecievepps_Object=MibTableColumn
rcCfmPMThroughputNearEndRecievepps=_RcCfmPMThroughputNearEndRecievepps_Object((1,3,6,1,4,1,8886,6,1,26,19,1,10),_RcCfmPMThroughputNearEndRecievepps_Type())
rcCfmPMThroughputNearEndRecievepps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmPMThroughputNearEndRecievepps.setStatus(_A)
_RcCfmMaExTable_Object=MibTable
rcCfmMaExTable=_RcCfmMaExTable_Object((1,3,6,1,4,1,8886,6,1,26,20))
if mibBuilder.loadTexts:rcCfmMaExTable.setStatus(_C)
_RcCfmMaExEntry_Object=MibTableRow
rcCfmMaExEntry=_RcCfmMaExEntry_Object((1,3,6,1,4,1,8886,6,1,26,20,1))
rcCfmMaExEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:rcCfmMaExEntry.setStatus(_C)
_RcCfmMaExFormat_Type=Dot1agCfmMaintAssocNameType
_RcCfmMaExFormat_Object=MibTableColumn
rcCfmMaExFormat=_RcCfmMaExFormat_Object((1,3,6,1,4,1,8886,6,1,26,20,1,1),_RcCfmMaExFormat_Type())
rcCfmMaExFormat.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExFormat.setStatus(_C)
_RcCfmMaExName_Type=Dot1agCfmMaintAssocName
_RcCfmMaExName_Object=MibTableColumn
rcCfmMaExName=_RcCfmMaExName_Object((1,3,6,1,4,1,8886,6,1,26,20,1,2),_RcCfmMaExName_Type())
rcCfmMaExName.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExName.setStatus(_C)
class _RcCfmMaExVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_RcCfmMaExVlanList_Type.__name__=_X
_RcCfmMaExVlanList_Object=MibTableColumn
rcCfmMaExVlanList=_RcCfmMaExVlanList_Object((1,3,6,1,4,1,8886,6,1,26,20,1,3),_RcCfmMaExVlanList_Type())
rcCfmMaExVlanList.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExVlanList.setStatus(_C)
class _RcCfmMaExCcmInterval_Type(Dot1agCfmCcmInterval):defaultValue=4
_RcCfmMaExCcmInterval_Type.__name__=_b
_RcCfmMaExCcmInterval_Object=MibTableColumn
rcCfmMaExCcmInterval=_RcCfmMaExCcmInterval_Object((1,3,6,1,4,1,8886,6,1,26,20,1,4),_RcCfmMaExCcmInterval_Type())
rcCfmMaExCcmInterval.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExCcmInterval.setStatus(_C)
class _RcCfmMaExCostumerVlan_Type(VlanIdOrNone):defaultValue=0
_RcCfmMaExCostumerVlan_Type.__name__=_a
_RcCfmMaExCostumerVlan_Object=MibTableColumn
rcCfmMaExCostumerVlan=_RcCfmMaExCostumerVlan_Object((1,3,6,1,4,1,8886,6,1,26,20,1,5),_RcCfmMaExCostumerVlan_Type())
rcCfmMaExCostumerVlan.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExCostumerVlan.setStatus(_C)
class _RcCfmMaExPduPriority_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcCfmMaExPduPriority_Type.__name__=_F
_RcCfmMaExPduPriority_Object=MibTableColumn
rcCfmMaExPduPriority=_RcCfmMaExPduPriority_Object((1,3,6,1,4,1,8886,6,1,26,20,1,6),_RcCfmMaExPduPriority_Type())
rcCfmMaExPduPriority.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExPduPriority.setStatus(_C)
_RcCfmMaExRowStatus_Type=RowStatus
_RcCfmMaExRowStatus_Object=MibTableColumn
rcCfmMaExRowStatus=_RcCfmMaExRowStatus_Object((1,3,6,1,4,1,8886,6,1,26,20,1,7),_RcCfmMaExRowStatus_Type())
rcCfmMaExRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExRowStatus.setStatus(_C)
_RcCfmMaExPrimaryVlanId_Type=VlanIdOrNone
_RcCfmMaExPrimaryVlanId_Object=MibTableColumn
rcCfmMaExPrimaryVlanId=_RcCfmMaExPrimaryVlanId_Object((1,3,6,1,4,1,8886,6,1,26,20,1,8),_RcCfmMaExPrimaryVlanId_Type())
rcCfmMaExPrimaryVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExPrimaryVlanId.setStatus(_C)
class _RcCfmMaExMipAutocreateAdmin_Type(EnableVar):defaultValue=2
_RcCfmMaExMipAutocreateAdmin_Type.__name__=_N
_RcCfmMaExMipAutocreateAdmin_Object=MibTableColumn
rcCfmMaExMipAutocreateAdmin=_RcCfmMaExMipAutocreateAdmin_Object((1,3,6,1,4,1,8886,6,1,26,20,1,9),_RcCfmMaExMipAutocreateAdmin_Type())
rcCfmMaExMipAutocreateAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:rcCfmMaExMipAutocreateAdmin.setStatus(_C)
_RcCfmMaExAisTable_Object=MibTable
rcCfmMaExAisTable=_RcCfmMaExAisTable_Object((1,3,6,1,4,1,8886,6,1,26,21))
if mibBuilder.loadTexts:rcCfmMaExAisTable.setStatus(_C)
_RcCfmMaExAisEntry_Object=MibTableRow
rcCfmMaExAisEntry=_RcCfmMaExAisEntry_Object((1,3,6,1,4,1,8886,6,1,26,21,1))
rcCfmMaExAisEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:rcCfmMaExAisEntry.setStatus(_C)
class _RcCfmMaExAisEnable_Type(EnableVar):defaultValue=2
_RcCfmMaExAisEnable_Type.__name__=_N
_RcCfmMaExAisEnable_Object=MibTableColumn
rcCfmMaExAisEnable=_RcCfmMaExAisEnable_Object((1,3,6,1,4,1,8886,6,1,26,21,1,1),_RcCfmMaExAisEnable_Type())
rcCfmMaExAisEnable.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExAisEnable.setStatus(_C)
class _RcCfmMaExAisLevelAdmin_Type(Dot1agCfmMDLevelOrNone):defaultValue=-1
_RcCfmMaExAisLevelAdmin_Type.__name__=_Z
_RcCfmMaExAisLevelAdmin_Object=MibTableColumn
rcCfmMaExAisLevelAdmin=_RcCfmMaExAisLevelAdmin_Object((1,3,6,1,4,1,8886,6,1,26,21,1,2),_RcCfmMaExAisLevelAdmin_Type())
rcCfmMaExAisLevelAdmin.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExAisLevelAdmin.setStatus(_C)
_RcCfmMaExAisLevelOper_Type=Dot1agCfmMDLevelOrNone
_RcCfmMaExAisLevelOper_Object=MibTableColumn
rcCfmMaExAisLevelOper=_RcCfmMaExAisLevelOper_Object((1,3,6,1,4,1,8886,6,1,26,21,1,3),_RcCfmMaExAisLevelOper_Type())
rcCfmMaExAisLevelOper.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExAisLevelOper.setStatus(_C)
class _RcCfmMaExAisPeriod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,60)));namedValues=NamedValues(*(('aisPeriod1s',1),('aisPeriod60s',60)))
_RcCfmMaExAisPeriod_Type.__name__=_G
_RcCfmMaExAisPeriod_Object=MibTableColumn
rcCfmMaExAisPeriod=_RcCfmMaExAisPeriod_Object((1,3,6,1,4,1,8886,6,1,26,21,1,4),_RcCfmMaExAisPeriod_Type())
rcCfmMaExAisPeriod.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExAisPeriod.setStatus(_C)
class _RcCfmMaExAisStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),(_u,2)))
_RcCfmMaExAisStatus_Type.__name__=_G
_RcCfmMaExAisStatus_Object=MibTableColumn
rcCfmMaExAisStatus=_RcCfmMaExAisStatus_Object((1,3,6,1,4,1,8886,6,1,26,21,1,5),_RcCfmMaExAisStatus_Type())
rcCfmMaExAisStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExAisStatus.setStatus(_C)
class _RcCfmMaExAisAge_Type(Unsigned32):defaultValue=0
_RcCfmMaExAisAge_Type.__name__=_F
_RcCfmMaExAisAge_Object=MibTableColumn
rcCfmMaExAisAge=_RcCfmMaExAisAge_Object((1,3,6,1,4,1,8886,6,1,26,21,1,6),_RcCfmMaExAisAge_Type())
rcCfmMaExAisAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExAisAge.setStatus(_C)
class _RcCfmMaExAisStatisticsTx_Type(Unsigned32):defaultValue=0
_RcCfmMaExAisStatisticsTx_Type.__name__=_F
_RcCfmMaExAisStatisticsTx_Object=MibTableColumn
rcCfmMaExAisStatisticsTx=_RcCfmMaExAisStatisticsTx_Object((1,3,6,1,4,1,8886,6,1,26,21,1,7),_RcCfmMaExAisStatisticsTx_Type())
rcCfmMaExAisStatisticsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExAisStatisticsTx.setStatus(_C)
class _RcCfmMaExAisStatisticsRx_Type(Unsigned32):defaultValue=0
_RcCfmMaExAisStatisticsRx_Type.__name__=_F
_RcCfmMaExAisStatisticsRx_Object=MibTableColumn
rcCfmMaExAisStatisticsRx=_RcCfmMaExAisStatisticsRx_Object((1,3,6,1,4,1,8886,6,1,26,21,1,8),_RcCfmMaExAisStatisticsRx_Type())
rcCfmMaExAisStatisticsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExAisStatisticsRx.setStatus(_C)
_RcCfmMaExLckTable_Object=MibTable
rcCfmMaExLckTable=_RcCfmMaExLckTable_Object((1,3,6,1,4,1,8886,6,1,26,22))
if mibBuilder.loadTexts:rcCfmMaExLckTable.setStatus(_C)
_RcCfmMaExLckEntry_Object=MibTableRow
rcCfmMaExLckEntry=_RcCfmMaExLckEntry_Object((1,3,6,1,4,1,8886,6,1,26,22,1))
rcCfmMaExLckEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:rcCfmMaExLckEntry.setStatus(_C)
class _RcCfmMaExLckLevelAdmin_Type(Dot1agCfmMDLevelOrNone):defaultValue=-1
_RcCfmMaExLckLevelAdmin_Type.__name__=_Z
_RcCfmMaExLckLevelAdmin_Object=MibTableColumn
rcCfmMaExLckLevelAdmin=_RcCfmMaExLckLevelAdmin_Object((1,3,6,1,4,1,8886,6,1,26,22,1,1),_RcCfmMaExLckLevelAdmin_Type())
rcCfmMaExLckLevelAdmin.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExLckLevelAdmin.setStatus(_C)
_RcCfmMaExLckLevelOper_Type=Dot1agCfmMDLevelOrNone
_RcCfmMaExLckLevelOper_Object=MibTableColumn
rcCfmMaExLckLevelOper=_RcCfmMaExLckLevelOper_Object((1,3,6,1,4,1,8886,6,1,26,22,1,2),_RcCfmMaExLckLevelOper_Type())
rcCfmMaExLckLevelOper.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExLckLevelOper.setStatus(_C)
class _RcCfmMaExLckPeriod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,60)));namedValues=NamedValues(*(('lckPeriod1s',1),('lckPeriod60s',60)))
_RcCfmMaExLckPeriod_Type.__name__=_G
_RcCfmMaExLckPeriod_Object=MibTableColumn
rcCfmMaExLckPeriod=_RcCfmMaExLckPeriod_Object((1,3,6,1,4,1,8886,6,1,26,22,1,3),_RcCfmMaExLckPeriod_Type())
rcCfmMaExLckPeriod.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMaExLckPeriod.setStatus(_C)
class _RcCfmMaExLckStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),(_u,2)))
_RcCfmMaExLckStatus_Type.__name__=_G
_RcCfmMaExLckStatus_Object=MibTableColumn
rcCfmMaExLckStatus=_RcCfmMaExLckStatus_Object((1,3,6,1,4,1,8886,6,1,26,22,1,4),_RcCfmMaExLckStatus_Type())
rcCfmMaExLckStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExLckStatus.setStatus(_C)
class _RcCfmMaExLckAge_Type(Unsigned32):defaultValue=0
_RcCfmMaExLckAge_Type.__name__=_F
_RcCfmMaExLckAge_Object=MibTableColumn
rcCfmMaExLckAge=_RcCfmMaExLckAge_Object((1,3,6,1,4,1,8886,6,1,26,22,1,5),_RcCfmMaExLckAge_Type())
rcCfmMaExLckAge.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExLckAge.setStatus(_C)
class _RcCfmMaExLckStatisticsTx_Type(Unsigned32):defaultValue=0
_RcCfmMaExLckStatisticsTx_Type.__name__=_F
_RcCfmMaExLckStatisticsTx_Object=MibTableColumn
rcCfmMaExLckStatisticsTx=_RcCfmMaExLckStatisticsTx_Object((1,3,6,1,4,1,8886,6,1,26,22,1,6),_RcCfmMaExLckStatisticsTx_Type())
rcCfmMaExLckStatisticsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExLckStatisticsTx.setStatus(_C)
class _RcCfmMaExLckStatisticsRx_Type(Unsigned32):defaultValue=0
_RcCfmMaExLckStatisticsRx_Type.__name__=_F
_RcCfmMaExLckStatisticsRx_Object=MibTableColumn
rcCfmMaExLckStatisticsRx=_RcCfmMaExLckStatisticsRx_Object((1,3,6,1,4,1,8886,6,1,26,22,1,7),_RcCfmMaExLckStatisticsRx_Type())
rcCfmMaExLckStatisticsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMaExLckStatisticsRx.setStatus(_C)
_RcCfmNotifications_ObjectIdentity=ObjectIdentity
rcCfmNotifications=_RcCfmNotifications_ObjectIdentity((1,3,6,1,4,1,8886,6,1,26,23))
_RcCfmMulticastLbResultTable_Object=MibTable
rcCfmMulticastLbResultTable=_RcCfmMulticastLbResultTable_Object((1,3,6,1,4,1,8886,6,1,26,24))
if mibBuilder.loadTexts:rcCfmMulticastLbResultTable.setStatus(_C)
_RcCfmMulticastLbResultEntry_Object=MibTableRow
rcCfmMulticastLbResultEntry=_RcCfmMulticastLbResultEntry_Object((1,3,6,1,4,1,8886,6,1,26,24,1))
rcCfmMulticastLbResultEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_L),(0,_H,_v))
if mibBuilder.loadTexts:rcCfmMulticastLbResultEntry.setStatus(_C)
class _RcCfmMcastLbResultIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_RcCfmMcastLbResultIndex_Type.__name__=_F
_RcCfmMcastLbResultIndex_Object=MibTableColumn
rcCfmMcastLbResultIndex=_RcCfmMcastLbResultIndex_Object((1,3,6,1,4,1,8886,6,1,26,24,1,1),_RcCfmMcastLbResultIndex_Type())
rcCfmMcastLbResultIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMcastLbResultIndex.setStatus(_C)
class _RcCfmMcastLbResultRemoteMepId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_RcCfmMcastLbResultRemoteMepId_Type.__name__=_F
_RcCfmMcastLbResultRemoteMepId_Object=MibTableColumn
rcCfmMcastLbResultRemoteMepId=_RcCfmMcastLbResultRemoteMepId_Object((1,3,6,1,4,1,8886,6,1,26,24,1,2),_RcCfmMcastLbResultRemoteMepId_Type())
rcCfmMcastLbResultRemoteMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMcastLbResultRemoteMepId.setStatus(_C)
class _RcCfmMcastLbResultRecvPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcCfmMcastLbResultRecvPort_Type.__name__=_F
_RcCfmMcastLbResultRecvPort_Object=MibTableColumn
rcCfmMcastLbResultRecvPort=_RcCfmMcastLbResultRecvPort_Object((1,3,6,1,4,1,8886,6,1,26,24,1,3),_RcCfmMcastLbResultRecvPort_Type())
rcCfmMcastLbResultRecvPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMcastLbResultRecvPort.setStatus(_C)
_RcCfmMcastLbResultMacAddress_Type=MacAddress
_RcCfmMcastLbResultMacAddress_Object=MibTableColumn
rcCfmMcastLbResultMacAddress=_RcCfmMcastLbResultMacAddress_Object((1,3,6,1,4,1,8886,6,1,26,24,1,4),_RcCfmMcastLbResultMacAddress_Type())
rcCfmMcastLbResultMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMcastLbResultMacAddress.setStatus(_C)
_RcCfmMcastLbResultRtt_Type=Unsigned32
_RcCfmMcastLbResultRtt_Object=MibTableColumn
rcCfmMcastLbResultRtt=_RcCfmMcastLbResultRtt_Object((1,3,6,1,4,1,8886,6,1,26,24,1,5),_RcCfmMcastLbResultRtt_Type())
rcCfmMcastLbResultRtt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcCfmMcastLbResultRtt.setStatus(_C)
_RcCfmMipExTable_Object=MibTable
rcCfmMipExTable=_RcCfmMipExTable_Object((1,3,6,1,4,1,8886,6,1,26,25))
if mibBuilder.loadTexts:rcCfmMipExTable.setStatus(_C)
_RcCfmMipExEntry_Object=MibTableRow
rcCfmMipExEntry=_RcCfmMipExEntry_Object((1,3,6,1,4,1,8886,6,1,26,25,1))
rcCfmMipExEntry.setIndexNames((0,_D,_d),(0,_H,_w))
if mibBuilder.loadTexts:rcCfmMipExEntry.setStatus(_C)
_RcCfmMipExIfIndex_Type=Integer32
_RcCfmMipExIfIndex_Object=MibTableColumn
rcCfmMipExIfIndex=_RcCfmMipExIfIndex_Object((1,3,6,1,4,1,8886,6,1,26,25,1,1),_RcCfmMipExIfIndex_Type())
rcCfmMipExIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMipExIfIndex.setStatus(_C)
_RcCfmMipRowStatus_Type=RowStatus
_RcCfmMipRowStatus_Object=MibTableColumn
rcCfmMipRowStatus=_RcCfmMipRowStatus_Object((1,3,6,1,4,1,8886,6,1,26,25,1,2),_RcCfmMipRowStatus_Type())
rcCfmMipRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:rcCfmMipRowStatus.setStatus(_C)
rcCfmPmFLRRaisingThreshFaultAlarm=NotificationType((1,3,6,1,4,1,8886,6,1,26,23,1))
rcCfmPmFLRRaisingThreshFaultAlarm.setObjects((_H,_x))
if mibBuilder.loadTexts:rcCfmPmFLRRaisingThreshFaultAlarm.setStatus(_A)
rcCfmPmFLRFallingThreshFaultAlarm=NotificationType((1,3,6,1,4,1,8886,6,1,26,23,2))
rcCfmPmFLRFallingThreshFaultAlarm.setObjects((_H,_y))
if mibBuilder.loadTexts:rcCfmPmFLRFallingThreshFaultAlarm.setStatus(_A)
rcCfmPmDelayRisingThreshFaultAlarm=NotificationType((1,3,6,1,4,1,8886,6,1,26,23,3))
rcCfmPmDelayRisingThreshFaultAlarm.setObjects((_H,_z))
if mibBuilder.loadTexts:rcCfmPmDelayRisingThreshFaultAlarm.setStatus(_A)
rcCfmPmDelayFallingThreshFaultAlarm=NotificationType((1,3,6,1,4,1,8886,6,1,26,23,4))
rcCfmPmDelayFallingThreshFaultAlarm.setObjects((_H,_A0))
if mibBuilder.loadTexts:rcCfmPmDelayFallingThreshFaultAlarm.setStatus(_A)
rcCfmPmDVRisingThreshFaultAlarm=NotificationType((1,3,6,1,4,1,8886,6,1,26,23,5))
rcCfmPmDVRisingThreshFaultAlarm.setObjects((_H,_A1))
if mibBuilder.loadTexts:rcCfmPmDVRisingThreshFaultAlarm.setStatus(_A)
rcCfmPmDVFallingThreshFaultAlarm=NotificationType((1,3,6,1,4,1,8886,6,1,26,23,6))
rcCfmPmDVFallingThreshFaultAlarm.setObjects((_H,_A2))
if mibBuilder.loadTexts:rcCfmPmDVFallingThreshFaultAlarm.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'rcCfm':rcCfm,'rcCfmBridge':rcCfmBridge,'rcCfmBridgeAdminCfm':rcCfmBridgeAdminCfm,'rcCfmBridgeCcmDbArchiveHoldtime':rcCfmBridgeCcmDbArchiveHoldtime,'rcCfmBridgeTracerouteCacheEnable':rcCfmBridgeTracerouteCacheEnable,'rcCfmBridgeTracerouteCacheHoldtime':rcCfmBridgeTracerouteCacheHoldtime,'rcCfmBridgeTracerouteCacheSize':rcCfmBridgeTracerouteCacheSize,'rcCfmBridgeTracerouteCacheClear':rcCfmBridgeTracerouteCacheClear,'rcCfmBridgeTrapConfig':rcCfmBridgeTrapConfig,'rcCfmBridgeRmepAgeTime':rcCfmBridgeRmepAgeTime,'rcCfmBridgeMode':rcCfmBridgeMode,'rcCfmLinkVlanList':rcCfmLinkVlanList,'rcCfmIfTable':rcCfmIfTable,'rcCfmIfEntry':rcCfmIfEntry,_e:rcCfmIfIndex,'rcCfmIfAdminCfm':rcCfmIfAdminCfm,'rcCfmIfMipLevel':rcCfmIfMipLevel,'rcCfmMdTable':rcCfmMdTable,'rcCfmMdEntry':rcCfmMdEntry,'rcCfmMdCcmRMpClear':rcCfmMdCcmRMpClear,'rcCfmErrorCcmTable':rcCfmErrorCcmTable,'rcCfmErrorCcmEntry':rcCfmErrorCcmEntry,_f:rcCfmErrorCcmRMepId,_g:rcCfmErrorCcmIndex,'rcCfmErrorCcmLevel':rcCfmErrorCcmLevel,'rcCfmErrorCcmVlan':rcCfmErrorCcmVlan,'rcCfmErrorCcmRecvMdName':rcCfmErrorCcmRecvMdName,'rcCfmErrorCcmMaid':rcCfmErrorCcmMaid,'rcCfmErrorCcmMacAddress':rcCfmErrorCcmMacAddress,'rcCfmErrorCcmErrorType':rcCfmErrorCcmErrorType,'rcCfmErrorCcmHoldTime':rcCfmErrorCcmHoldTime,'rcCfmErrorCcmClear':rcCfmErrorCcmClear,'rcCfmLtmDbTable':rcCfmLtmDbTable,'rcCfmLtmDbEntry':rcCfmLtmDbEntry,_h:rcCfmLtmDbTransactionId,'rcCfmLtmDbTargetMacAddress':rcCfmLtmDbTargetMacAddress,'rcCfmMepDbExTable':rcCfmMepDbExTable,'rcCfmMepDbExEntry':rcCfmMepDbExEntry,'rcCfmMepDbExEntryHoldTime':rcCfmMepDbExEntryHoldTime,'rcCfmMaCciEnableTable':rcCfmMaCciEnableTable,'rcCfmMaCciEnableEntry':rcCfmMaCciEnableEntry,_i:rcCfmMaMdLevel,_j:rcCfmMaMaVlanId,'rcCfmMaCciEnabled':rcCfmMaCciEnabled,'rcCfmMepExTable':rcCfmMepExTable,'rcCfmMepExEntry':rcCfmMepExEntry,'rcCfmMepExLbrTimeoutNum':rcCfmMepExLbrTimeoutNum,'rcCfmMepExTransmitLbmDataTlvLen':rcCfmMepExTransmitLbmDataTlvLen,'rcCfmMepExLckAdmin':rcCfmMepExLckAdmin,'rcCfmMaExAisSuppressStatus':rcCfmMaExAisSuppressStatus,'rcCfmMaExAisSuppressAdmin':rcCfmMaExAisSuppressAdmin,'rcCfmMepExPduPriority':rcCfmMepExPduPriority,'rcCfmMepExPmAdmin':rcCfmMepExPmAdmin,'rcCfmMepExRdiAdmin':rcCfmMepExRdiAdmin,'rcCfmMaMepListExTable':rcCfmMaMepListExTable,'rcCfmMaMepListExEntry':rcCfmMaMepListExEntry,'rcCfmMaMepListType':rcCfmMaMepListType,'rcCfmMaMepListMacAddress':rcCfmMaMepListMacAddress,'rcCfmMaMepListIfIndex':rcCfmMaMepListIfIndex,'rcCfmMaNetExTable':rcCfmMaNetExTable,'rcCfmMaNetExEntry':rcCfmMaNetExEntry,'rcCfmMaNetRemoteMepLearnEnabled':rcCfmMaNetRemoteMepLearnEnabled,'rcCfmMaNetCostumerVlan':rcCfmMaNetCostumerVlan,'rcCfmMaNetPduPriority':rcCfmMaNetPduPriority,'rcCfmMaNetRemoteMepLearnActive':rcCfmMaNetRemoteMepLearnActive,'rcCfmMaNetCcCheckEnabled':rcCfmMaNetCcCheckEnabled,'rcCfmPMTable':rcCfmPMTable,'rcCfmPMEntry':rcCfmPMEntry,'rcCfmPMEnabled':rcCfmPMEnabled,'rcCfmPMDmmTxInterval':rcCfmPMDmmTxInterval,'rcCfmPMDelayObjective':rcCfmPMDelayObjective,'rcCfmPMDVObjective':rcCfmPMDVObjective,_x:rcCfmPMFLRRisingThreshold,_y:rcCfmPMFLRFallingThreshold,_z:rcCfmPMDelayRisingThreshold,_A0:rcCfmPMDelayFallingThreshold,_A1:rcCfmPMDVRisingThreshold,_A2:rcCfmPMDVFallingThreshold,'rcCfmPMStatiticsClear':rcCfmPMStatiticsClear,'rcCfmPMTrapSendEnable':rcCfmPMTrapSendEnable,'rcCfmPMThroughputTimeout':rcCfmPMThroughputTimeout,'rcCfmPMThroughputObject':rcCfmPMThroughputObject,'rcCfmPMThroughputPduLength':rcCfmPMThroughputPduLength,'rcCfmPMThroughputEnable':rcCfmPMThroughputEnable,'rcCfmPMRowStatus':rcCfmPMRowStatus,'rcCfmPMFLRTotalTable':rcCfmPMFLRTotalTable,'rcCfmPMFLRTotalEntry':rcCfmPMFLRTotalEntry,'rcCfmPMFLRTotalElapsedTime':rcCfmPMFLRTotalElapsedTime,'rcCfmPMFLRTotalFarEndTxCounter':rcCfmPMFLRTotalFarEndTxCounter,'rcCfmPMFLRTotalFarEndLostCounter':rcCfmPMFLRTotalFarEndLostCounter,'rcCfmPMFLRTotalFarEndLossRatio':rcCfmPMFLRTotalFarEndLossRatio,'rcCfmPMFLRTotalFarEndUnaviableSecond':rcCfmPMFLRTotalFarEndUnaviableSecond,'rcCfmPMFLRTotalNearEndTxCounter':rcCfmPMFLRTotalNearEndTxCounter,'rcCfmPMFLRTotalNearEndLostCounter':rcCfmPMFLRTotalNearEndLostCounter,'rcCfmPMFLRTotalNearEndLossRatio':rcCfmPMFLRTotalNearEndLossRatio,'rcCfmPMFLRTotalNearEndUnaviableSecond':rcCfmPMFLRTotalNearEndUnaviableSecond,'rcCfmPMFLRCurrentTable':rcCfmPMFLRCurrentTable,'rcCfmPMFLRCurrentEntry':rcCfmPMFLRCurrentEntry,_k:rcCfmPMFLRCurrentPeriod,'rcCfmPMFLRCurrentElapsedTime':rcCfmPMFLRCurrentElapsedTime,'rcCfmPMFLRCurrentFarEndTxFrameCounter':rcCfmPMFLRCurrentFarEndTxFrameCounter,'rcCfmPMFLRCurrentFarEndLostFrameCounter':rcCfmPMFLRCurrentFarEndLostFrameCounter,'rcCfmPMFLRCurrentFarEndLossRatio':rcCfmPMFLRCurrentFarEndLossRatio,'rcCfmPMFLRCurrentNearEndTxFrameCounter':rcCfmPMFLRCurrentNearEndTxFrameCounter,'rcCfmPMFLRCurrentNearEndLostFrameCounter':rcCfmPMFLRCurrentNearEndLostFrameCounter,'rcCfmPMFLRCurrentNearEndLossRatio':rcCfmPMFLRCurrentNearEndLossRatio,'rcCfmPMFLRIntervalTable':rcCfmPMFLRIntervalTable,'rcCfmPMFLRIntervalEntry':rcCfmPMFLRIntervalEntry,_l:rcCfmPMFLRIntervalPeriod,_m:rcCfmPMFLRIntervalIndex,'rcCfmPMFLRIntervalPeerMepId':rcCfmPMFLRIntervalPeerMepId,'rcCfmPMFLRIntervalBeginTime':rcCfmPMFLRIntervalBeginTime,'rcCfmPMFLRIntervalFarEndTxFrameCounter':rcCfmPMFLRIntervalFarEndTxFrameCounter,'rcCfmPMFLRIntervalFarEndLostFrameCounter':rcCfmPMFLRIntervalFarEndLostFrameCounter,'rcCfmPMFLRIntervalFarEndLossRatio':rcCfmPMFLRIntervalFarEndLossRatio,'rcCfmPMFLRIntervalNearEndTxFrameCounter':rcCfmPMFLRIntervalNearEndTxFrameCounter,'rcCfmPMFLRIntervalNearEndLostFrameCounter':rcCfmPMFLRIntervalNearEndLostFrameCounter,'rcCfmPMFLRIntervalNearEndLossRatio':rcCfmPMFLRIntervalNearEndLossRatio,'rcCfmPMDelayCurrentTable':rcCfmPMDelayCurrentTable,'rcCfmPMDelayCurrentEntry':rcCfmPMDelayCurrentEntry,_n:rcCfmPMDelayCurrentPeriod,'rcCfmPMDelayCurrentFarEndAboveObjCounter':rcCfmPMDelayCurrentFarEndAboveObjCounter,'rcCfmPMDelayCurrentFarEndBelowObjCounter':rcCfmPMDelayCurrentFarEndBelowObjCounter,'rcCfmPMDelayCurrentFarEndMaxDelay':rcCfmPMDelayCurrentFarEndMaxDelay,'rcCfmPMDelayCurrentFarEndAvgDelay':rcCfmPMDelayCurrentFarEndAvgDelay,'rcCfmPMDelayCurrentFarEndMinDelay':rcCfmPMDelayCurrentFarEndMinDelay,'rcCfmPMDelayCurrentNearEndAboveObjCounter':rcCfmPMDelayCurrentNearEndAboveObjCounter,'rcCfmPMDelayCurrentNearEndBelowObjCounter':rcCfmPMDelayCurrentNearEndBelowObjCounter,'rcCfmPMDelayCurrentNearEndMaxDelay':rcCfmPMDelayCurrentNearEndMaxDelay,'rcCfmPMDelayCurrentNearEndAvgDelay':rcCfmPMDelayCurrentNearEndAvgDelay,'rcCfmPMDelayCurrentNearEndMinDelay':rcCfmPMDelayCurrentNearEndMinDelay,'rcCfmPMDelayCurrentRoundTripAboveObjCounter':rcCfmPMDelayCurrentRoundTripAboveObjCounter,'rcCfmPMDelayCurrentRoundTripBelowObjCounter':rcCfmPMDelayCurrentRoundTripBelowObjCounter,'rcCfmPMDelayCurrentRoundTripMaxDelay':rcCfmPMDelayCurrentRoundTripMaxDelay,'rcCfmPMDelayCurrentRoundTripAvgDelay':rcCfmPMDelayCurrentRoundTripAvgDelay,'rcCfmPMDelayCurrentRoundTripMinDelay':rcCfmPMDelayCurrentRoundTripMinDelay,'rcCfmPMDelayIntervalTable':rcCfmPMDelayIntervalTable,'rcCfmPMDelayIntervalEntry':rcCfmPMDelayIntervalEntry,_o:rcCfmPMDelayIntervalPeriod,_p:rcCfmPMDelayIntervalIndex,'rcCfmPMDelayIntervalBeginTime':rcCfmPMDelayIntervalBeginTime,'rcCfmPMDelayIntervalPeerMepId':rcCfmPMDelayIntervalPeerMepId,'rcCfmPMDelayIntervalFarEndAboveObjCounter':rcCfmPMDelayIntervalFarEndAboveObjCounter,'rcCfmPMDelayIntervalFarEndBelowObjCounter':rcCfmPMDelayIntervalFarEndBelowObjCounter,'rcCfmPMDelayIntervalFarEndMaxDelay':rcCfmPMDelayIntervalFarEndMaxDelay,'rcCfmPMDelayIntervalFarEndAvgDelay':rcCfmPMDelayIntervalFarEndAvgDelay,'rcCfmPMDelayIntervalFarEndMinDelay':rcCfmPMDelayIntervalFarEndMinDelay,'rcCfmPMDelayIntervalNearEndAboveObjCounter':rcCfmPMDelayIntervalNearEndAboveObjCounter,'rcCfmPMDelayIntervalNearEndBelowObjCounter':rcCfmPMDelayIntervalNearEndBelowObjCounter,'rcCfmPMDelayIntervalNearEndMaxDelay':rcCfmPMDelayIntervalNearEndMaxDelay,'rcCfmPMDelayIntervalNearEndAvgDelay':rcCfmPMDelayIntervalNearEndAvgDelay,'rcCfmPMDelayIntervalNearEndMinDelay':rcCfmPMDelayIntervalNearEndMinDelay,'rcCfmPMDelayIntervalRoundTripAboveObjCounter':rcCfmPMDelayIntervalRoundTripAboveObjCounter,'rcCfmPMDelayIntervalRoundTripBelowObjCounter':rcCfmPMDelayIntervalRoundTripBelowObjCounter,'rcCfmPMDelayIntervalRoundTripMaxDelay':rcCfmPMDelayIntervalRoundTripMaxDelay,'rcCfmPMDelayIntervalRoundTripAvgDelay':rcCfmPMDelayIntervalRoundTripAvgDelay,'rcCfmPMDelayIntervalRoundTripMinDelay':rcCfmPMDelayIntervalRoundTripMinDelay,'rcCfmPMDVCurrentTable':rcCfmPMDVCurrentTable,'rcCfmPMDVCurrentEntry':rcCfmPMDVCurrentEntry,_q:rcCfmPMDVCurrentPeriod,'rcCfmPMDVCurrentFarEndAboveObjCounter':rcCfmPMDVCurrentFarEndAboveObjCounter,'rcCfmPMDVCurrentFarEndBelowObjCounter':rcCfmPMDVCurrentFarEndBelowObjCounter,'rcCfmPMDVCurrentFarEndMaxDv':rcCfmPMDVCurrentFarEndMaxDv,'rcCfmPMDVCurrentFarEndAvgDv':rcCfmPMDVCurrentFarEndAvgDv,'rcCfmPMDVCurrentNearEndAboveObjCounter':rcCfmPMDVCurrentNearEndAboveObjCounter,'rcCfmPMDVCurrentNearEndBelowObjCounter':rcCfmPMDVCurrentNearEndBelowObjCounter,'rcCfmPMDVCurrentNearEndMaxDv':rcCfmPMDVCurrentNearEndMaxDv,'rcCfmPMDVCurrentNearEndAvgDv':rcCfmPMDVCurrentNearEndAvgDv,'rcCfmPMDVCurrentRoundTripAboveObjCounter':rcCfmPMDVCurrentRoundTripAboveObjCounter,'rcCfmPMDVCurrentRoundTripBelowObjCounter':rcCfmPMDVCurrentRoundTripBelowObjCounter,'rcCfmPMDVCurrentRoundTripMaxDv':rcCfmPMDVCurrentRoundTripMaxDv,'rcCfmPMDVCurrentRoundTripAvgDv':rcCfmPMDVCurrentRoundTripAvgDv,'rcCfmPMDVIntervalTable':rcCfmPMDVIntervalTable,'rcCfmPMDVIntervalEntry':rcCfmPMDVIntervalEntry,_r:rcCfmPMDVIntervalPeriod,_s:rcCfmPMDVIntervalIndex,'rcCfmPMDVIntervalBeginTime':rcCfmPMDVIntervalBeginTime,'rcCfmPMDVIntervalPeerMepId':rcCfmPMDVIntervalPeerMepId,'rcCfmPMDVIntervalFarEndAboveObjCounter':rcCfmPMDVIntervalFarEndAboveObjCounter,'rcCfmPMDVIntervalFarEndBelowObjCounter':rcCfmPMDVIntervalFarEndBelowObjCounter,'rcCfmPMDVIntervalFarEndMaxDv':rcCfmPMDVIntervalFarEndMaxDv,'rcCfmPMDVIntervalFarEndAvgDv':rcCfmPMDVIntervalFarEndAvgDv,'rcCfmPMDVIntervalNearEndAboveObjCounter':rcCfmPMDVIntervalNearEndAboveObjCounter,'rcCfmPMDVIntervalNearEndBelowObjCounter':rcCfmPMDVIntervalNearEndBelowObjCounter,'rcCfmPMDVIntervalNearEndMaxDv':rcCfmPMDVIntervalNearEndMaxDv,'rcCfmPMDVIntervalNearEndAvgDv':rcCfmPMDVIntervalNearEndAvgDv,'rcCfmPMDVIntervalRoundTripAboveObjCounter':rcCfmPMDVIntervalRoundTripAboveObjCounter,'rcCfmPMDVIntervalRoundTripBelowObjCounter':rcCfmPMDVIntervalRoundTripBelowObjCounter,'rcCfmPMDVIntervalRoundTripMaxDv':rcCfmPMDVIntervalRoundTripMaxDv,'rcCfmPMDVIntervalRoundTripAvgDv':rcCfmPMDVIntervalRoundTripAvgDv,'rcCfmPMThroughputTable':rcCfmPMThroughputTable,'rcCfmPMThroughputEntry':rcCfmPMThroughputEntry,'rcCfmPMThroughputTestResult':rcCfmPMThroughputTestResult,'rcCfmPMThroughputTestState':rcCfmPMThroughputTestState,'rcCfmPMThroughputFarEndSendbps':rcCfmPMThroughputFarEndSendbps,'rcCfmPMThroughputFarEndRecievebps':rcCfmPMThroughputFarEndRecievebps,'rcCfmPMThroughputFarEndSendpps':rcCfmPMThroughputFarEndSendpps,'rcCfmPMThroughputFarEndRecievepps':rcCfmPMThroughputFarEndRecievepps,'rcCfmPMThroughputNearEndSendbps':rcCfmPMThroughputNearEndSendbps,'rcCfmPMThroughputNearEndRecievebps':rcCfmPMThroughputNearEndRecievebps,'rcCfmPMThroughputNearEndSendpps':rcCfmPMThroughputNearEndSendpps,'rcCfmPMThroughputNearEndRecievepps':rcCfmPMThroughputNearEndRecievepps,'rcCfmMaExTable':rcCfmMaExTable,'rcCfmMaExEntry':rcCfmMaExEntry,'rcCfmMaExFormat':rcCfmMaExFormat,'rcCfmMaExName':rcCfmMaExName,'rcCfmMaExVlanList':rcCfmMaExVlanList,'rcCfmMaExCcmInterval':rcCfmMaExCcmInterval,'rcCfmMaExCostumerVlan':rcCfmMaExCostumerVlan,'rcCfmMaExPduPriority':rcCfmMaExPduPriority,'rcCfmMaExRowStatus':rcCfmMaExRowStatus,'rcCfmMaExPrimaryVlanId':rcCfmMaExPrimaryVlanId,'rcCfmMaExMipAutocreateAdmin':rcCfmMaExMipAutocreateAdmin,'rcCfmMaExAisTable':rcCfmMaExAisTable,'rcCfmMaExAisEntry':rcCfmMaExAisEntry,'rcCfmMaExAisEnable':rcCfmMaExAisEnable,'rcCfmMaExAisLevelAdmin':rcCfmMaExAisLevelAdmin,'rcCfmMaExAisLevelOper':rcCfmMaExAisLevelOper,'rcCfmMaExAisPeriod':rcCfmMaExAisPeriod,'rcCfmMaExAisStatus':rcCfmMaExAisStatus,'rcCfmMaExAisAge':rcCfmMaExAisAge,'rcCfmMaExAisStatisticsTx':rcCfmMaExAisStatisticsTx,'rcCfmMaExAisStatisticsRx':rcCfmMaExAisStatisticsRx,'rcCfmMaExLckTable':rcCfmMaExLckTable,'rcCfmMaExLckEntry':rcCfmMaExLckEntry,'rcCfmMaExLckLevelAdmin':rcCfmMaExLckLevelAdmin,'rcCfmMaExLckLevelOper':rcCfmMaExLckLevelOper,'rcCfmMaExLckPeriod':rcCfmMaExLckPeriod,'rcCfmMaExLckStatus':rcCfmMaExLckStatus,'rcCfmMaExLckAge':rcCfmMaExLckAge,'rcCfmMaExLckStatisticsTx':rcCfmMaExLckStatisticsTx,'rcCfmMaExLckStatisticsRx':rcCfmMaExLckStatisticsRx,'rcCfmNotifications':rcCfmNotifications,'rcCfmPmFLRRaisingThreshFaultAlarm':rcCfmPmFLRRaisingThreshFaultAlarm,'rcCfmPmFLRFallingThreshFaultAlarm':rcCfmPmFLRFallingThreshFaultAlarm,'rcCfmPmDelayRisingThreshFaultAlarm':rcCfmPmDelayRisingThreshFaultAlarm,'rcCfmPmDelayFallingThreshFaultAlarm':rcCfmPmDelayFallingThreshFaultAlarm,'rcCfmPmDVRisingThreshFaultAlarm':rcCfmPmDVRisingThreshFaultAlarm,'rcCfmPmDVFallingThreshFaultAlarm':rcCfmPmDVFallingThreshFaultAlarm,'rcCfmMulticastLbResultTable':rcCfmMulticastLbResultTable,'rcCfmMulticastLbResultEntry':rcCfmMulticastLbResultEntry,_v:rcCfmMcastLbResultIndex,'rcCfmMcastLbResultRemoteMepId':rcCfmMcastLbResultRemoteMepId,'rcCfmMcastLbResultRecvPort':rcCfmMcastLbResultRecvPort,'rcCfmMcastLbResultMacAddress':rcCfmMcastLbResultMacAddress,'rcCfmMcastLbResultRtt':rcCfmMcastLbResultRtt,'rcCfmMipExTable':rcCfmMipExTable,'rcCfmMipExEntry':rcCfmMipExEntry,_w:rcCfmMipExIfIndex,'rcCfmMipRowStatus':rcCfmMipRowStatus})