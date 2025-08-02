_B6='zxGponUnCfgSnOntRtd'
_B5='zxGponUnCfgSnOntPsw'
_B4='zxGponUnCfgSnOntRID'
_B3='zxGponUnCfgSnOntSN'
_B2='zxGponSpoofingConflictPort'
_B1='zxGponSpoofingVlan'
_B0='zxGponSpoofingMac'
_A_='zxGponSpoofingPort'
_Az='zxGponOltTxPowerAbnormalInformReason'
_Ay='zxGponOltRxPowerAbnormalInformiReason'
_Ax='zxGponGemPortUNIMACBriPortFilterTableMacAddr'
_Aw='zxGponGemPortIWTPMACBriPortFilterTableMacAddr'
_Av='zxOnuTrafficMgmtUnitTcontIdx'
_Au='zxGponThresholdDataProfileIndex'
_At='zxGponTrafficProfileIndex'
_As='zxGponBWProfileIndex'
_Ar='zxGponGemTrafficDescriptorsMeIdIdx'
_Aq='zxGponTrafficScheduleIndex'
_Ap='zxGponPriorQueueAlarmIndex'
_Ao='zxGponPriorQueueIndex'
_An='bidirectional'
_Am='zxGponGemIWTPAlarmIndex'
_Al='zxGponGemIWTPInfoMeIdIdx'
_Ak='zxGponCESSPInfoMeIdIdx'
_Aj='zxGponPPTPCesUniTPID'
_Ai='zxGponIpPortCfgDataMeIdIdx'
_Ah='forwarded'
_Ag='zxGponIpRouterSPInfoMeIdIdx'
_Af='zxGponMACBriPortAddrMacAddr'
_Ae='zxGponMACBriPortFilterTableMacAddr'
_Ad='zxGponUniInfoIndex'
_Ac='tagFrmToVal'
_Ab='dscpTo8021p'
_Aa='zxGpon8021pMapperMeIdIdx'
_AZ='zxGponTcontInfoIndex'
_AY='zxGponAniInfoIndex'
_AX='zxGponProtectionDataIndex'
_AW='zxGponThresholdDataIndex'
_AV='OntEquipmentId'
_AU='zxGponOnt2Index'
_AT='OntVersionId'
_AS='OntVendorId'
_AR='zxGponOntIndex'
_AQ='zxGponEthSwitchVlanId'
_AP='zxGponEthTypeVlanMapEthType'
_AO='zxGpon8021xOnOffIdx'
_AN='zxGponDownBroadcastFloodVlanId'
_AM='zxGponDsBFPortIdInfoIdx'
_AL='zxGponMulticastIdx'
_AK='zxGponMulticastVlanId'
_AJ='zxGponMulticastAddress'
_AI='zxGponStaticMulticastIdx'
_AH='zxGponStaticMultiPortIdInfoIdx'
_AG='o6-operation'
_AF='o5-ranging'
_AE='o4-serialnumber'
_AD='o3-powersetup'
_AC='o2-standby'
_AB='o1-initial'
_AA='zxGponUnCfgSnIdx'
_A9='omciready'
_A8='zxGponGetValidIdxTableNameIdx'
_A7='ZxOntList'
_A6='zxGponSCBMCastOntSetIdx'
_A5='zxGponSCBMCastGroupIdx'
_A4='bidirection'
_A3='DateAndTime'
_A2='Unsigned32'
_A1='zxGponTrapEventString'
_A0='zxGponOltTxPowerAlarmReason'
_z='zxGponOltRxPowerAlarmiReason'
_y='zxGponGemPPPMHDInfoMeIdIdx'
_x='zxGponGemPNCTPInfoMeIdIdx'
_w='llc'
_v='atmvc'
_u='deactivate'
_t='activate'
_s='discarded'
_r='other'
_q='both'
_p='toolow'
_o='toohigh'
_n='down'
_m='up'
_l='lan'
_k='filter'
_j='zxGponMACBriPortCfgDataMeIdIdx'
_i='Timeout'
_h='zxGponMACBSPInfoMeIdIdx'
_g='wrr'
_f='OntSerialNumber'
_e='zxGponMgmtPonSlotId'
_d='ZxIndexList'
_c='none'
_b='ZxPortIdList'
_a='zxGponPPTPEthInfoTPID'
_Z='atm'
_Y='forward'
_X='ZxGponRecordName'
_W='TruthValue'
_V='disabled'
_U='enabled'
_T='neCreate'
_S='nmsCreate'
_R='disable'
_Q='enable'
_P='zxGponGemPortIdx'
_O='OctetString'
_N='read-create'
_M='zxGponOntDevMgmtDescription'
_L='zxGponOntDevMgmtName'
_K='not-accessible'
_J='zxGponOntDevMgmtTypeName'
_I='zxGponMgmtPonOnuId'
_H='ifIndex'
_G='IF-MIB'
_F='zxGponMgmtPonOltId'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='ZXGPON-SERVICE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A2,'enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_A3,'DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_W)
zxGponRootMib=ModuleIdentity((1,3,6,1,4,1,3902,1012,3))
if mibBuilder.loadTexts:zxGponRootMib.setRevisions(('2006-09-27 00:00',))
class Timeout(Integer32):0
class OntVendorId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class OntVersionId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
class OntSerialNumber(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class OntEquipmentId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
class ZxGponRecordName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class ZxOntList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class ZxPortIdList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class ZxIndexList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZxEnterpriseMib_ObjectIdentity=ObjectIdentity
zxEnterpriseMib=_ZxEnterpriseMib_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxPON_ObjectIdentity=ObjectIdentity
zxPON=_ZxPON_ObjectIdentity((1,3,6,1,4,1,3902,1012))
_ZxGponMgmtIndex_ObjectIdentity=ObjectIdentity
zxGponMgmtIndex=_ZxGponMgmtIndex_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,1))
_ZxGponOltOnuTable_Object=MibTable
zxGponOltOnuTable=_ZxGponOltOnuTable_Object((1,3,6,1,4,1,3902,1012,3,1,1))
if mibBuilder.loadTexts:zxGponOltOnuTable.setStatus(_A)
_ZxGponOltOnuEntry_Object=MibTableRow
zxGponOltOnuEntry=_ZxGponOltOnuEntry_Object((1,3,6,1,4,1,3902,1012,3,1,1,1))
zxGponOltOnuEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOltOnuEntry.setStatus(_A)
_ZxGponMgmtPonOltId_Type=Integer32
_ZxGponMgmtPonOltId_Object=MibTableColumn
zxGponMgmtPonOltId=_ZxGponMgmtPonOltId_Object((1,3,6,1,4,1,3902,1012,3,1,1,1,1),_ZxGponMgmtPonOltId_Type())
zxGponMgmtPonOltId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMgmtPonOltId.setStatus(_A)
_ZxGponMgmtPonOnuId_Type=Integer32
_ZxGponMgmtPonOnuId_Object=MibTableColumn
zxGponMgmtPonOnuId=_ZxGponMgmtPonOnuId_Object((1,3,6,1,4,1,3902,1012,3,1,1,1,2),_ZxGponMgmtPonOnuId_Type())
zxGponMgmtPonOnuId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMgmtPonOnuId.setStatus(_A)
_ZxGponMgmtPonEntryStatus_Type=RowStatus
_ZxGponMgmtPonEntryStatus_Object=MibTableColumn
zxGponMgmtPonEntryStatus=_ZxGponMgmtPonEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,1,1,1,3),_ZxGponMgmtPonEntryStatus_Type())
zxGponMgmtPonEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponMgmtPonEntryStatus.setStatus(_A)
class _ZxAnGponRevision_Type(Bits):namedValues=NamedValues(('gemportUpQueue',0))
_ZxAnGponRevision_Type.__name__='Bits'
_ZxAnGponRevision_Object=MibScalar
zxAnGponRevision=_ZxAnGponRevision_Object((1,3,6,1,4,1,3902,1012,3,2),_ZxAnGponRevision_Type())
zxAnGponRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnGponRevision.setStatus(_A)
_ZxGponPrivateGlobal_ObjectIdentity=ObjectIdentity
zxGponPrivateGlobal=_ZxGponPrivateGlobal_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,11))
_ZxGponOltDevInfoTable_Object=MibTable
zxGponOltDevInfoTable=_ZxGponOltDevInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,1))
if mibBuilder.loadTexts:zxGponOltDevInfoTable.setStatus(_A)
_ZxGponOltDevInfoEntry_Object=MibTableRow
zxGponOltDevInfoEntry=_ZxGponOltDevInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,1,1))
zxGponOltDevInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltDevInfoEntry.setStatus(_A)
_ZxGponDbaEnable_Type=TruthValue
_ZxGponDbaEnable_Object=MibTableColumn
zxGponDbaEnable=_ZxGponDbaEnable_Object((1,3,6,1,4,1,3902,1012,3,11,1,1,1),_ZxGponDbaEnable_Type())
zxGponDbaEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDbaEnable.setStatus(_A)
_ZxGponFECTable_Object=MibTable
zxGponFECTable=_ZxGponFECTable_Object((1,3,6,1,4,1,3902,1012,3,11,3))
if mibBuilder.loadTexts:zxGponFECTable.setStatus(_A)
_ZxGponFECEntry_Object=MibTableRow
zxGponFECEntry=_ZxGponFECEntry_Object((1,3,6,1,4,1,3902,1012,3,11,3,1))
zxGponFECEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponFECEntry.setStatus(_A)
class _ZxGponFECMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),('downstream',2),('upstream',3),(_A4,4)))
_ZxGponFECMode_Type.__name__=_E
_ZxGponFECMode_Object=MibTableColumn
zxGponFECMode=_ZxGponFECMode_Object((1,3,6,1,4,1,3902,1012,3,11,3,1,1),_ZxGponFECMode_Type())
zxGponFECMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponFECMode.setStatus(_A)
_ZxGponRTDTable_Object=MibTable
zxGponRTDTable=_ZxGponRTDTable_Object((1,3,6,1,4,1,3902,1012,3,11,4))
if mibBuilder.loadTexts:zxGponRTDTable.setStatus(_A)
_ZxGponRTDEntry_Object=MibTableRow
zxGponRTDEntry=_ZxGponRTDEntry_Object((1,3,6,1,4,1,3902,1012,3,11,4,1))
zxGponRTDEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponRTDEntry.setStatus(_A)
_ZxGponRTDEqd_Type=Integer32
_ZxGponRTDEqd_Object=MibTableColumn
zxGponRTDEqd=_ZxGponRTDEqd_Object((1,3,6,1,4,1,3902,1012,3,11,4,1,1),_ZxGponRTDEqd_Type())
zxGponRTDEqd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponRTDEqd.setStatus(_A)
_ZxGponRTDDistance_Type=Integer32
_ZxGponRTDDistance_Object=MibTableColumn
zxGponRTDDistance=_ZxGponRTDDistance_Object((1,3,6,1,4,1,3902,1012,3,11,4,1,2),_ZxGponRTDDistance_Type())
zxGponRTDDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponRTDDistance.setStatus(_A)
_ZxGponRangeTable_Object=MibTable
zxGponRangeTable=_ZxGponRangeTable_Object((1,3,6,1,4,1,3902,1012,3,11,5))
if mibBuilder.loadTexts:zxGponRangeTable.setStatus(_A)
_ZxGponRangeEntry_Object=MibTableRow
zxGponRangeEntry=_ZxGponRangeEntry_Object((1,3,6,1,4,1,3902,1012,3,11,5,1))
zxGponRangeEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponRangeEntry.setStatus(_A)
class _ZxGponRangeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mode0',1),('mode1',2),('mode2',3)))
_ZxGponRangeMode_Type.__name__=_E
_ZxGponRangeMode_Object=MibTableColumn
zxGponRangeMode=_ZxGponRangeMode_Object((1,3,6,1,4,1,3902,1012,3,11,5,1,1),_ZxGponRangeMode_Type())
zxGponRangeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponRangeMode.setStatus(_A)
_ZxGponRangeBase_Type=Integer32
_ZxGponRangeBase_Object=MibTableColumn
zxGponRangeBase=_ZxGponRangeBase_Object((1,3,6,1,4,1,3902,1012,3,11,5,1,2),_ZxGponRangeBase_Type())
zxGponRangeBase.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponRangeBase.setStatus(_A)
if mibBuilder.loadTexts:zxGponRangeBase.setUnits('100m')
_ZxGponRangeDiff_Type=Integer32
_ZxGponRangeDiff_Object=MibTableColumn
zxGponRangeDiff=_ZxGponRangeDiff_Object((1,3,6,1,4,1,3902,1012,3,11,5,1,3),_ZxGponRangeDiff_Type())
zxGponRangeDiff.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponRangeDiff.setStatus(_A)
if mibBuilder.loadTexts:zxGponRangeDiff.setUnits('100m')
class _ZxGponRangeCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),('step',2)))
_ZxGponRangeCapability_Type.__name__=_E
_ZxGponRangeCapability_Object=MibTableColumn
zxGponRangeCapability=_ZxGponRangeCapability_Object((1,3,6,1,4,1,3902,1012,3,11,5,1,4),_ZxGponRangeCapability_Type())
zxGponRangeCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponRangeCapability.setStatus(_A)
_ZxGponPonFloodBandwidthInfoTable_Object=MibTable
zxGponPonFloodBandwidthInfoTable=_ZxGponPonFloodBandwidthInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,9))
if mibBuilder.loadTexts:zxGponPonFloodBandwidthInfoTable.setStatus(_A)
_ZxGponPonFloodBandwidthInfoEntry_Object=MibTableRow
zxGponPonFloodBandwidthInfoEntry=_ZxGponPonFloodBandwidthInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,9,1))
zxGponPonFloodBandwidthInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponPonFloodBandwidthInfoEntry.setStatus(_A)
_ZxGponPonFloodBandwidth_Type=Unsigned32
_ZxGponPonFloodBandwidth_Object=MibTableColumn
zxGponPonFloodBandwidth=_ZxGponPonFloodBandwidth_Object((1,3,6,1,4,1,3902,1012,3,11,9,1,1),_ZxGponPonFloodBandwidth_Type())
zxGponPonFloodBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonFloodBandwidth.setStatus(_A)
_ZxGponPonMCastBandwidthInfoTable_Object=MibTable
zxGponPonMCastBandwidthInfoTable=_ZxGponPonMCastBandwidthInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,10))
if mibBuilder.loadTexts:zxGponPonMCastBandwidthInfoTable.setStatus(_A)
_ZxGponPonMCastBandwidthInfoEntry_Object=MibTableRow
zxGponPonMCastBandwidthInfoEntry=_ZxGponPonMCastBandwidthInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,10,1))
zxGponPonMCastBandwidthInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponPonMCastBandwidthInfoEntry.setStatus(_A)
_ZxGponPonMCastTotalBandwidth_Type=Unsigned32
_ZxGponPonMCastTotalBandwidth_Object=MibTableColumn
zxGponPonMCastTotalBandwidth=_ZxGponPonMCastTotalBandwidth_Object((1,3,6,1,4,1,3902,1012,3,11,10,1,1),_ZxGponPonMCastTotalBandwidth_Type())
zxGponPonMCastTotalBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonMCastTotalBandwidth.setStatus(_A)
_ZxGponSCBMCastGroupTable_Object=MibTable
zxGponSCBMCastGroupTable=_ZxGponSCBMCastGroupTable_Object((1,3,6,1,4,1,3902,1012,3,11,11))
if mibBuilder.loadTexts:zxGponSCBMCastGroupTable.setStatus(_A)
_ZxGponSCBMCastGroupEntry_Object=MibTableRow
zxGponSCBMCastGroupEntry=_ZxGponSCBMCastGroupEntry_Object((1,3,6,1,4,1,3902,1012,3,11,11,1))
zxGponSCBMCastGroupEntry.setIndexNames((0,_B,_A5))
if mibBuilder.loadTexts:zxGponSCBMCastGroupEntry.setStatus(_A)
_ZxGponSCBMCastGroupIdx_Type=Integer32
_ZxGponSCBMCastGroupIdx_Object=MibTableColumn
zxGponSCBMCastGroupIdx=_ZxGponSCBMCastGroupIdx_Object((1,3,6,1,4,1,3902,1012,3,11,11,1,1),_ZxGponSCBMCastGroupIdx_Type())
zxGponSCBMCastGroupIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponSCBMCastGroupIdx.setStatus(_A)
class _ZxGponSCBMCastGroupName_Type(ZxGponRecordName):subtypeSpec=ZxGponRecordName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxGponSCBMCastGroupName_Type.__name__=_X
_ZxGponSCBMCastGroupName_Object=MibTableColumn
zxGponSCBMCastGroupName=_ZxGponSCBMCastGroupName_Object((1,3,6,1,4,1,3902,1012,3,11,11,1,2),_ZxGponSCBMCastGroupName_Type())
zxGponSCBMCastGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponSCBMCastGroupName.setStatus(_A)
_ZxGponSCBMCastMgmtPortID_Type=Integer32
_ZxGponSCBMCastMgmtPortID_Object=MibTableColumn
zxGponSCBMCastMgmtPortID=_ZxGponSCBMCastMgmtPortID_Object((1,3,6,1,4,1,3902,1012,3,11,11,1,3),_ZxGponSCBMCastMgmtPortID_Type())
zxGponSCBMCastMgmtPortID.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponSCBMCastMgmtPortID.setStatus(_A)
_ZxGponSCBMCastGroupDownBWPtr_Type=Integer32
_ZxGponSCBMCastGroupDownBWPtr_Object=MibTableColumn
zxGponSCBMCastGroupDownBWPtr=_ZxGponSCBMCastGroupDownBWPtr_Object((1,3,6,1,4,1,3902,1012,3,11,11,1,4),_ZxGponSCBMCastGroupDownBWPtr_Type())
zxGponSCBMCastGroupDownBWPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponSCBMCastGroupDownBWPtr.setStatus(_A)
_ZxGponSCBMCastRealPortID_Type=Integer32
_ZxGponSCBMCastRealPortID_Object=MibTableColumn
zxGponSCBMCastRealPortID=_ZxGponSCBMCastRealPortID_Object((1,3,6,1,4,1,3902,1012,3,11,11,1,5),_ZxGponSCBMCastRealPortID_Type())
zxGponSCBMCastRealPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSCBMCastRealPortID.setStatus(_A)
class _ZxGponSCBMCastOntListIdx_Type(ZxIndexList):subtypeSpec=ZxIndexList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ZxGponSCBMCastOntListIdx_Type.__name__=_d
_ZxGponSCBMCastOntListIdx_Object=MibTableColumn
zxGponSCBMCastOntListIdx=_ZxGponSCBMCastOntListIdx_Object((1,3,6,1,4,1,3902,1012,3,11,11,1,6),_ZxGponSCBMCastOntListIdx_Type())
zxGponSCBMCastOntListIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSCBMCastOntListIdx.setStatus(_A)
_ZxGponSCBMCastEntryStatus_Type=RowStatus
_ZxGponSCBMCastEntryStatus_Object=MibTableColumn
zxGponSCBMCastEntryStatus=_ZxGponSCBMCastEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,11,11,1,7),_ZxGponSCBMCastEntryStatus_Type())
zxGponSCBMCastEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponSCBMCastEntryStatus.setStatus(_A)
_ZxGponSCBMCastOntTable_Object=MibTable
zxGponSCBMCastOntTable=_ZxGponSCBMCastOntTable_Object((1,3,6,1,4,1,3902,1012,3,11,12))
if mibBuilder.loadTexts:zxGponSCBMCastOntTable.setStatus(_A)
_ZxGponSCBMCastOntEntry_Object=MibTableRow
zxGponSCBMCastOntEntry=_ZxGponSCBMCastOntEntry_Object((1,3,6,1,4,1,3902,1012,3,11,12,1))
zxGponSCBMCastOntEntry.setIndexNames((0,_B,_A6))
if mibBuilder.loadTexts:zxGponSCBMCastOntEntry.setStatus(_A)
_ZxGponSCBMCastOntSetIdx_Type=Integer32
_ZxGponSCBMCastOntSetIdx_Object=MibTableColumn
zxGponSCBMCastOntSetIdx=_ZxGponSCBMCastOntSetIdx_Object((1,3,6,1,4,1,3902,1012,3,11,12,1,1),_ZxGponSCBMCastOntSetIdx_Type())
zxGponSCBMCastOntSetIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponSCBMCastOntSetIdx.setStatus(_A)
_ZxGponSCBMCastOntSetGroupIdx_Type=Integer32
_ZxGponSCBMCastOntSetGroupIdx_Object=MibTableColumn
zxGponSCBMCastOntSetGroupIdx=_ZxGponSCBMCastOntSetGroupIdx_Object((1,3,6,1,4,1,3902,1012,3,11,12,1,2),_ZxGponSCBMCastOntSetGroupIdx_Type())
zxGponSCBMCastOntSetGroupIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponSCBMCastOntSetGroupIdx.setStatus(_A)
class _ZxGponSCBMCastOntList_Type(ZxOntList):subtypeSpec=ZxOntList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ZxGponSCBMCastOntList_Type.__name__=_A7
_ZxGponSCBMCastOntList_Object=MibTableColumn
zxGponSCBMCastOntList=_ZxGponSCBMCastOntList_Object((1,3,6,1,4,1,3902,1012,3,11,12,1,3),_ZxGponSCBMCastOntList_Type())
zxGponSCBMCastOntList.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponSCBMCastOntList.setStatus(_A)
_ZxGponSCBMCastOntEntryStatus_Type=RowStatus
_ZxGponSCBMCastOntEntryStatus_Object=MibTableColumn
zxGponSCBMCastOntEntryStatus=_ZxGponSCBMCastOntEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,11,12,1,4),_ZxGponSCBMCastOntEntryStatus_Type())
zxGponSCBMCastOntEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponSCBMCastOntEntryStatus.setStatus(_A)
_ZxGponPonBroadCastBandwidthInfoTable_Object=MibTable
zxGponPonBroadCastBandwidthInfoTable=_ZxGponPonBroadCastBandwidthInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,13))
if mibBuilder.loadTexts:zxGponPonBroadCastBandwidthInfoTable.setStatus(_A)
_ZxGponPonBroadCastBandwidthInfoEntry_Object=MibTableRow
zxGponPonBroadCastBandwidthInfoEntry=_ZxGponPonBroadCastBandwidthInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,13,1))
zxGponPonBroadCastBandwidthInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponPonBroadCastBandwidthInfoEntry.setStatus(_A)
_ZxGponPonBroadCastBandwidth_Type=Integer32
_ZxGponPonBroadCastBandwidth_Object=MibTableColumn
zxGponPonBroadCastBandwidth=_ZxGponPonBroadCastBandwidth_Object((1,3,6,1,4,1,3902,1012,3,11,13,1,1),_ZxGponPonBroadCastBandwidth_Type())
zxGponPonBroadCastBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonBroadCastBandwidth.setStatus(_A)
_ZxGponPonPeakBandwidthInfoTable_Object=MibTable
zxGponPonPeakBandwidthInfoTable=_ZxGponPonPeakBandwidthInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,14))
if mibBuilder.loadTexts:zxGponPonPeakBandwidthInfoTable.setStatus(_A)
_ZxGponPonPeakBandwidthInfoEntry_Object=MibTableRow
zxGponPonPeakBandwidthInfoEntry=_ZxGponPonPeakBandwidthInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,14,1))
zxGponPonPeakBandwidthInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponPonPeakBandwidthInfoEntry.setStatus(_A)
_ZxGponPonPeakBandwidth_Type=Integer32
_ZxGponPonPeakBandwidth_Object=MibTableColumn
zxGponPonPeakBandwidth=_ZxGponPonPeakBandwidth_Object((1,3,6,1,4,1,3902,1012,3,11,14,1,1),_ZxGponPonPeakBandwidth_Type())
zxGponPonPeakBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonPeakBandwidth.setStatus(_A)
_ZxGponGetValidIdxTable_Object=MibTable
zxGponGetValidIdxTable=_ZxGponGetValidIdxTable_Object((1,3,6,1,4,1,3902,1012,3,11,16))
if mibBuilder.loadTexts:zxGponGetValidIdxTable.setStatus(_A)
_ZxGponGetValidIdxEntry_Object=MibTableRow
zxGponGetValidIdxEntry=_ZxGponGetValidIdxEntry_Object((1,3,6,1,4,1,3902,1012,3,11,16,1))
zxGponGetValidIdxEntry.setIndexNames((0,_B,_A8),(0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGetValidIdxEntry.setStatus(_A)
_ZxGponGetValidIdxTableNameIdx_Type=Integer32
_ZxGponGetValidIdxTableNameIdx_Object=MibTableColumn
zxGponGetValidIdxTableNameIdx=_ZxGponGetValidIdxTableNameIdx_Object((1,3,6,1,4,1,3902,1012,3,11,16,1,1),_ZxGponGetValidIdxTableNameIdx_Type())
zxGponGetValidIdxTableNameIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponGetValidIdxTableNameIdx.setStatus(_A)
_ZxGponGetValidIdxvalue_Type=Integer32
_ZxGponGetValidIdxvalue_Object=MibTableColumn
zxGponGetValidIdxvalue=_ZxGponGetValidIdxvalue_Object((1,3,6,1,4,1,3902,1012,3,11,16,1,2),_ZxGponGetValidIdxvalue_Type())
zxGponGetValidIdxvalue.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGetValidIdxvalue.setStatus(_A)
_ZxGponSpiIfPmTable_Object=MibTable
zxGponSpiIfPmTable=_ZxGponSpiIfPmTable_Object((1,3,6,1,4,1,3902,1012,3,11,20))
if mibBuilder.loadTexts:zxGponSpiIfPmTable.setStatus(_A)
_ZxGponSpiIfPmEntry_Object=MibTableRow
zxGponSpiIfPmEntry=_ZxGponSpiIfPmEntry_Object((1,3,6,1,4,1,3902,1012,3,11,20,1))
zxGponSpiIfPmEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponSpiIfPmEntry.setStatus(_A)
_ZxGponSpiIfRxFrm_Type=Counter64
_ZxGponSpiIfRxFrm_Object=MibTableColumn
zxGponSpiIfRxFrm=_ZxGponSpiIfRxFrm_Object((1,3,6,1,4,1,3902,1012,3,11,20,1,1),_ZxGponSpiIfRxFrm_Type())
zxGponSpiIfRxFrm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpiIfRxFrm.setStatus(_A)
_ZxGponSpiIfRxByte_Type=Counter64
_ZxGponSpiIfRxByte_Object=MibTableColumn
zxGponSpiIfRxByte=_ZxGponSpiIfRxByte_Object((1,3,6,1,4,1,3902,1012,3,11,20,1,2),_ZxGponSpiIfRxByte_Type())
zxGponSpiIfRxByte.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpiIfRxByte.setStatus(_A)
_ZxGponSpiIfRxDiscardFrm_Type=Counter64
_ZxGponSpiIfRxDiscardFrm_Object=MibTableColumn
zxGponSpiIfRxDiscardFrm=_ZxGponSpiIfRxDiscardFrm_Object((1,3,6,1,4,1,3902,1012,3,11,20,1,3),_ZxGponSpiIfRxDiscardFrm_Type())
zxGponSpiIfRxDiscardFrm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpiIfRxDiscardFrm.setStatus(_A)
_ZxGponSpiIfRxDiscardByte_Type=Counter64
_ZxGponSpiIfRxDiscardByte_Object=MibTableColumn
zxGponSpiIfRxDiscardByte=_ZxGponSpiIfRxDiscardByte_Object((1,3,6,1,4,1,3902,1012,3,11,20,1,4),_ZxGponSpiIfRxDiscardByte_Type())
zxGponSpiIfRxDiscardByte.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpiIfRxDiscardByte.setStatus(_A)
_ZxGponSpiIfTxFrm_Type=Counter64
_ZxGponSpiIfTxFrm_Object=MibTableColumn
zxGponSpiIfTxFrm=_ZxGponSpiIfTxFrm_Object((1,3,6,1,4,1,3902,1012,3,11,20,1,5),_ZxGponSpiIfTxFrm_Type())
zxGponSpiIfTxFrm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpiIfTxFrm.setStatus(_A)
_ZxGponSpiIfTxByte_Type=Counter64
_ZxGponSpiIfTxByte_Object=MibTableColumn
zxGponSpiIfTxByte=_ZxGponSpiIfTxByte_Object((1,3,6,1,4,1,3902,1012,3,11,20,1,6),_ZxGponSpiIfTxByte_Type())
zxGponSpiIfTxByte.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpiIfTxByte.setStatus(_A)
_ZxGponSpiIfTxDiscardFrm_Type=Counter64
_ZxGponSpiIfTxDiscardFrm_Object=MibTableColumn
zxGponSpiIfTxDiscardFrm=_ZxGponSpiIfTxDiscardFrm_Object((1,3,6,1,4,1,3902,1012,3,11,20,1,7),_ZxGponSpiIfTxDiscardFrm_Type())
zxGponSpiIfTxDiscardFrm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpiIfTxDiscardFrm.setStatus(_A)
_ZxGponSpiIfTxDiscardByte_Type=Counter64
_ZxGponSpiIfTxDiscardByte_Object=MibTableColumn
zxGponSpiIfTxDiscardByte=_ZxGponSpiIfTxDiscardByte_Object((1,3,6,1,4,1,3902,1012,3,11,20,1,8),_ZxGponSpiIfTxDiscardByte_Type())
zxGponSpiIfTxDiscardByte.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpiIfTxDiscardByte.setStatus(_A)
_ZxGponPonScheduleModeInfoTable_Object=MibTable
zxGponPonScheduleModeInfoTable=_ZxGponPonScheduleModeInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,21))
if mibBuilder.loadTexts:zxGponPonScheduleModeInfoTable.setStatus(_A)
_ZxGponPonScheduleModeInfoEntry_Object=MibTableRow
zxGponPonScheduleModeInfoEntry=_ZxGponPonScheduleModeInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,21,1))
zxGponPonScheduleModeInfoEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:zxGponPonScheduleModeInfoEntry.setStatus(_A)
_ZxGponMgmtPonSlotId_Type=Integer32
_ZxGponMgmtPonSlotId_Object=MibTableColumn
zxGponMgmtPonSlotId=_ZxGponMgmtPonSlotId_Object((1,3,6,1,4,1,3902,1012,3,11,21,1,1),_ZxGponMgmtPonSlotId_Type())
zxGponMgmtPonSlotId.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponMgmtPonSlotId.setStatus(_A)
_ZxGponPonScheduleMode_Type=Integer32
_ZxGponPonScheduleMode_Object=MibTableColumn
zxGponPonScheduleMode=_ZxGponPonScheduleMode_Object((1,3,6,1,4,1,3902,1012,3,11,21,1,2),_ZxGponPonScheduleMode_Type())
zxGponPonScheduleMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonScheduleMode.setStatus(_A)
_ZxGponPon802Dot1pMapInfoTable_Object=MibTable
zxGponPon802Dot1pMapInfoTable=_ZxGponPon802Dot1pMapInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,22))
if mibBuilder.loadTexts:zxGponPon802Dot1pMapInfoTable.setStatus(_A)
_ZxGponPon802Dot1pMapInfoEntry_Object=MibTableRow
zxGponPon802Dot1pMapInfoEntry=_ZxGponPon802Dot1pMapInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,22,1))
zxGponPon802Dot1pMapInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponPon802Dot1pMapInfoEntry.setStatus(_A)
_ZxGponPonDot1pMapQueue0_Type=Integer32
_ZxGponPonDot1pMapQueue0_Object=MibTableColumn
zxGponPonDot1pMapQueue0=_ZxGponPonDot1pMapQueue0_Object((1,3,6,1,4,1,3902,1012,3,11,22,1,1),_ZxGponPonDot1pMapQueue0_Type())
zxGponPonDot1pMapQueue0.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonDot1pMapQueue0.setStatus(_A)
_ZxGponPonDot1pMapQueue1_Type=Integer32
_ZxGponPonDot1pMapQueue1_Object=MibTableColumn
zxGponPonDot1pMapQueue1=_ZxGponPonDot1pMapQueue1_Object((1,3,6,1,4,1,3902,1012,3,11,22,1,2),_ZxGponPonDot1pMapQueue1_Type())
zxGponPonDot1pMapQueue1.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonDot1pMapQueue1.setStatus(_A)
_ZxGponPonDot1pMapQueue2_Type=Integer32
_ZxGponPonDot1pMapQueue2_Object=MibTableColumn
zxGponPonDot1pMapQueue2=_ZxGponPonDot1pMapQueue2_Object((1,3,6,1,4,1,3902,1012,3,11,22,1,3),_ZxGponPonDot1pMapQueue2_Type())
zxGponPonDot1pMapQueue2.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonDot1pMapQueue2.setStatus(_A)
_ZxGponPonDot1pMapQueue3_Type=Integer32
_ZxGponPonDot1pMapQueue3_Object=MibTableColumn
zxGponPonDot1pMapQueue3=_ZxGponPonDot1pMapQueue3_Object((1,3,6,1,4,1,3902,1012,3,11,22,1,4),_ZxGponPonDot1pMapQueue3_Type())
zxGponPonDot1pMapQueue3.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonDot1pMapQueue3.setStatus(_A)
_ZxGponPonDot1pMapQueue4_Type=Integer32
_ZxGponPonDot1pMapQueue4_Object=MibTableColumn
zxGponPonDot1pMapQueue4=_ZxGponPonDot1pMapQueue4_Object((1,3,6,1,4,1,3902,1012,3,11,22,1,5),_ZxGponPonDot1pMapQueue4_Type())
zxGponPonDot1pMapQueue4.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonDot1pMapQueue4.setStatus(_A)
_ZxGponPonDot1pMapQueue5_Type=Integer32
_ZxGponPonDot1pMapQueue5_Object=MibTableColumn
zxGponPonDot1pMapQueue5=_ZxGponPonDot1pMapQueue5_Object((1,3,6,1,4,1,3902,1012,3,11,22,1,6),_ZxGponPonDot1pMapQueue5_Type())
zxGponPonDot1pMapQueue5.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonDot1pMapQueue5.setStatus(_A)
_ZxGponPonDot1pMapQueue6_Type=Integer32
_ZxGponPonDot1pMapQueue6_Object=MibTableColumn
zxGponPonDot1pMapQueue6=_ZxGponPonDot1pMapQueue6_Object((1,3,6,1,4,1,3902,1012,3,11,22,1,7),_ZxGponPonDot1pMapQueue6_Type())
zxGponPonDot1pMapQueue6.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonDot1pMapQueue6.setStatus(_A)
_ZxGponPonDot1pMapQueue7_Type=Integer32
_ZxGponPonDot1pMapQueue7_Object=MibTableColumn
zxGponPonDot1pMapQueue7=_ZxGponPonDot1pMapQueue7_Object((1,3,6,1,4,1,3902,1012,3,11,22,1,8),_ZxGponPonDot1pMapQueue7_Type())
zxGponPonDot1pMapQueue7.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonDot1pMapQueue7.setStatus(_A)
_ZxGponPonWeightMgmtInfoTable_Object=MibTable
zxGponPonWeightMgmtInfoTable=_ZxGponPonWeightMgmtInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,23))
if mibBuilder.loadTexts:zxGponPonWeightMgmtInfoTable.setStatus(_A)
_ZxGponPonWeightMgmtInfoEntry_Object=MibTableRow
zxGponPonWeightMgmtInfoEntry=_ZxGponPonWeightMgmtInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,23,1))
zxGponPonWeightMgmtInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponPonWeightMgmtInfoEntry.setStatus(_A)
_ZxGponPonWeightMgmtQueue0_Type=Integer32
_ZxGponPonWeightMgmtQueue0_Object=MibTableColumn
zxGponPonWeightMgmtQueue0=_ZxGponPonWeightMgmtQueue0_Object((1,3,6,1,4,1,3902,1012,3,11,23,1,1),_ZxGponPonWeightMgmtQueue0_Type())
zxGponPonWeightMgmtQueue0.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonWeightMgmtQueue0.setStatus(_A)
_ZxGponPonWeightMgmtQueue1_Type=Integer32
_ZxGponPonWeightMgmtQueue1_Object=MibTableColumn
zxGponPonWeightMgmtQueue1=_ZxGponPonWeightMgmtQueue1_Object((1,3,6,1,4,1,3902,1012,3,11,23,1,2),_ZxGponPonWeightMgmtQueue1_Type())
zxGponPonWeightMgmtQueue1.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonWeightMgmtQueue1.setStatus(_A)
_ZxGponPonWeightMgmtQueue2_Type=Integer32
_ZxGponPonWeightMgmtQueue2_Object=MibTableColumn
zxGponPonWeightMgmtQueue2=_ZxGponPonWeightMgmtQueue2_Object((1,3,6,1,4,1,3902,1012,3,11,23,1,3),_ZxGponPonWeightMgmtQueue2_Type())
zxGponPonWeightMgmtQueue2.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonWeightMgmtQueue2.setStatus(_A)
_ZxGponPonWeightMgmtQueue3_Type=Integer32
_ZxGponPonWeightMgmtQueue3_Object=MibTableColumn
zxGponPonWeightMgmtQueue3=_ZxGponPonWeightMgmtQueue3_Object((1,3,6,1,4,1,3902,1012,3,11,23,1,4),_ZxGponPonWeightMgmtQueue3_Type())
zxGponPonWeightMgmtQueue3.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonWeightMgmtQueue3.setStatus(_A)
_ZxGponPonWeightMgmtQueue4_Type=Integer32
_ZxGponPonWeightMgmtQueue4_Object=MibTableColumn
zxGponPonWeightMgmtQueue4=_ZxGponPonWeightMgmtQueue4_Object((1,3,6,1,4,1,3902,1012,3,11,23,1,5),_ZxGponPonWeightMgmtQueue4_Type())
zxGponPonWeightMgmtQueue4.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonWeightMgmtQueue4.setStatus(_A)
_ZxGponPonWeightMgmtQueue5_Type=Integer32
_ZxGponPonWeightMgmtQueue5_Object=MibTableColumn
zxGponPonWeightMgmtQueue5=_ZxGponPonWeightMgmtQueue5_Object((1,3,6,1,4,1,3902,1012,3,11,23,1,6),_ZxGponPonWeightMgmtQueue5_Type())
zxGponPonWeightMgmtQueue5.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonWeightMgmtQueue5.setStatus(_A)
_ZxGponPonWeightMgmtQueue6_Type=Integer32
_ZxGponPonWeightMgmtQueue6_Object=MibTableColumn
zxGponPonWeightMgmtQueue6=_ZxGponPonWeightMgmtQueue6_Object((1,3,6,1,4,1,3902,1012,3,11,23,1,7),_ZxGponPonWeightMgmtQueue6_Type())
zxGponPonWeightMgmtQueue6.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonWeightMgmtQueue6.setStatus(_A)
_ZxGponPonWeightMgmtQueue7_Type=Integer32
_ZxGponPonWeightMgmtQueue7_Object=MibTableColumn
zxGponPonWeightMgmtQueue7=_ZxGponPonWeightMgmtQueue7_Object((1,3,6,1,4,1,3902,1012,3,11,23,1,8),_ZxGponPonWeightMgmtQueue7_Type())
zxGponPonWeightMgmtQueue7.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPonWeightMgmtQueue7.setStatus(_A)
_ZxGponFloodBroadCastEnableInfoTable_Object=MibTable
zxGponFloodBroadCastEnableInfoTable=_ZxGponFloodBroadCastEnableInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,24))
if mibBuilder.loadTexts:zxGponFloodBroadCastEnableInfoTable.setStatus(_A)
_ZxGponFloodBroadCastEnableInfoEntry_Object=MibTableRow
zxGponFloodBroadCastEnableInfoEntry=_ZxGponFloodBroadCastEnableInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,24,1))
zxGponFloodBroadCastEnableInfoEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:zxGponFloodBroadCastEnableInfoEntry.setStatus(_A)
_ZxGponFloodEnable_Type=Integer32
_ZxGponFloodEnable_Object=MibTableColumn
zxGponFloodEnable=_ZxGponFloodEnable_Object((1,3,6,1,4,1,3902,1012,3,11,24,1,1),_ZxGponFloodEnable_Type())
zxGponFloodEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponFloodEnable.setStatus(_A)
_ZxGponBroadcastEnable_Type=Integer32
_ZxGponBroadcastEnable_Object=MibTableColumn
zxGponBroadcastEnable=_ZxGponBroadcastEnable_Object((1,3,6,1,4,1,3902,1012,3,11,24,1,2),_ZxGponBroadcastEnable_Type())
zxGponBroadcastEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBroadcastEnable.setStatus(_A)
_ZxGponSlotOpticalDetectInfoTable_Object=MibTable
zxGponSlotOpticalDetectInfoTable=_ZxGponSlotOpticalDetectInfoTable_Object((1,3,6,1,4,1,3902,1012,3,11,25))
if mibBuilder.loadTexts:zxGponSlotOpticalDetectInfoTable.setStatus(_A)
_ZxGponSlotOpticalDetectInfoEntry_Object=MibTableRow
zxGponSlotOpticalDetectInfoEntry=_ZxGponSlotOpticalDetectInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,11,25,1))
zxGponSlotOpticalDetectInfoEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:zxGponSlotOpticalDetectInfoEntry.setStatus(_A)
_ZxGponSlotOpticalDetect_Type=TruthValue
_ZxGponSlotOpticalDetect_Object=MibTableColumn
zxGponSlotOpticalDetect=_ZxGponSlotOpticalDetect_Object((1,3,6,1,4,1,3902,1012,3,11,25,1,1),_ZxGponSlotOpticalDetect_Type())
zxGponSlotOpticalDetect.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponSlotOpticalDetect.setStatus(_A)
class _ZxGponPortLocOnuIdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('onusn',1),('onuid',2),('onuname',3)))
_ZxGponPortLocOnuIdFormat_Type.__name__=_E
_ZxGponPortLocOnuIdFormat_Object=MibScalar
zxGponPortLocOnuIdFormat=_ZxGponPortLocOnuIdFormat_Object((1,3,6,1,4,1,3902,1012,3,11,40),_ZxGponPortLocOnuIdFormat_Type())
zxGponPortLocOnuIdFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPortLocOnuIdFormat.setStatus(_A)
_ZxGponStandardOlt_ObjectIdentity=ObjectIdentity
zxGponStandardOlt=_ZxGponStandardOlt_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,12))
_ZxGponOltInfoTable_Object=MibTable
zxGponOltInfoTable=_ZxGponOltInfoTable_Object((1,3,6,1,4,1,3902,1012,3,12,1))
if mibBuilder.loadTexts:zxGponOltInfoTable.setStatus(_A)
_ZxGponOltInfoEntry_Object=MibTableRow
zxGponOltInfoEntry=_ZxGponOltInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,12,1,1))
zxGponOltInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltInfoEntry.setStatus(_A)
class _ZxGponOltInfoPONTransRateType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('ratetype1',1),('ratetype2',2),('ratetype3',3),('ratetype4',4),('ratetype5',5),('ratetype6',6),('ratetype7',7)))
_ZxGponOltInfoPONTransRateType_Type.__name__=_E
_ZxGponOltInfoPONTransRateType_Object=MibTableColumn
zxGponOltInfoPONTransRateType=_ZxGponOltInfoPONTransRateType_Object((1,3,6,1,4,1,3902,1012,3,12,1,1,1),_ZxGponOltInfoPONTransRateType_Type())
zxGponOltInfoPONTransRateType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltInfoPONTransRateType.setStatus(_A)
_ZxGponOltInfoOpticalTransceiverType_Type=Integer32
_ZxGponOltInfoOpticalTransceiverType_Object=MibTableColumn
zxGponOltInfoOpticalTransceiverType=_ZxGponOltInfoOpticalTransceiverType_Object((1,3,6,1,4,1,3902,1012,3,12,1,1,2),_ZxGponOltInfoOpticalTransceiverType_Type())
zxGponOltInfoOpticalTransceiverType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltInfoOpticalTransceiverType.setStatus(_A)
_ZxGponOltInfoOntMgmtMode_Type=Integer32
_ZxGponOltInfoOntMgmtMode_Object=MibTableColumn
zxGponOltInfoOntMgmtMode=_ZxGponOltInfoOntMgmtMode_Object((1,3,6,1,4,1,3902,1012,3,12,1,1,3),_ZxGponOltInfoOntMgmtMode_Type())
zxGponOltInfoOntMgmtMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltInfoOntMgmtMode.setStatus(_A)
_ZxGponOltInfoCurrentStatus_Type=Integer32
_ZxGponOltInfoCurrentStatus_Object=MibTableColumn
zxGponOltInfoCurrentStatus=_ZxGponOltInfoCurrentStatus_Object((1,3,6,1,4,1,3902,1012,3,12,1,1,4),_ZxGponOltInfoCurrentStatus_Type())
zxGponOltInfoCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltInfoCurrentStatus.setStatus(_A)
class _ZxGponOltInfoFECEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponOltInfoFECEnable_Type.__name__=_E
_ZxGponOltInfoFECEnable_Object=MibTableColumn
zxGponOltInfoFECEnable=_ZxGponOltInfoFECEnable_Object((1,3,6,1,4,1,3902,1012,3,12,1,1,5),_ZxGponOltInfoFECEnable_Type())
zxGponOltInfoFECEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltInfoFECEnable.setStatus(_A)
class _ZxGponOltInfoDBAEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponOltInfoDBAEnable_Type.__name__=_E
_ZxGponOltInfoDBAEnable_Object=MibTableColumn
zxGponOltInfoDBAEnable=_ZxGponOltInfoDBAEnable_Object((1,3,6,1,4,1,3902,1012,3,12,1,1,6),_ZxGponOltInfoDBAEnable_Type())
zxGponOltInfoDBAEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltInfoDBAEnable.setStatus(_A)
_ZxGponOltStatisticInfoTable_Object=MibTable
zxGponOltStatisticInfoTable=_ZxGponOltStatisticInfoTable_Object((1,3,6,1,4,1,3902,1012,3,12,2))
if mibBuilder.loadTexts:zxGponOltStatisticInfoTable.setStatus(_A)
_ZxGponOltStatisticInfoEntry_Object=MibTableRow
zxGponOltStatisticInfoEntry=_ZxGponOltStatisticInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,12,2,1))
zxGponOltStatisticInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltStatisticInfoEntry.setStatus(_A)
_ZxGponOltStatisticInfoSuperframeCounter_Type=Counter64
_ZxGponOltStatisticInfoSuperframeCounter_Object=MibTableColumn
zxGponOltStatisticInfoSuperframeCounter=_ZxGponOltStatisticInfoSuperframeCounter_Object((1,3,6,1,4,1,3902,1012,3,12,2,1,1),_ZxGponOltStatisticInfoSuperframeCounter_Type())
zxGponOltStatisticInfoSuperframeCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltStatisticInfoSuperframeCounter.setStatus(_A)
_ZxGponOltStatisticInfoBIPCounter_Type=Counter64
_ZxGponOltStatisticInfoBIPCounter_Object=MibTableColumn
zxGponOltStatisticInfoBIPCounter=_ZxGponOltStatisticInfoBIPCounter_Object((1,3,6,1,4,1,3902,1012,3,12,2,1,2),_ZxGponOltStatisticInfoBIPCounter_Type())
zxGponOltStatisticInfoBIPCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltStatisticInfoBIPCounter.setStatus(_A)
_ZxGponDownFrameInfoTable_Object=MibTable
zxGponDownFrameInfoTable=_ZxGponDownFrameInfoTable_Object((1,3,6,1,4,1,3902,1012,3,12,3))
if mibBuilder.loadTexts:zxGponDownFrameInfoTable.setStatus(_A)
_ZxGponDownFrameInfoEntry_Object=MibTableRow
zxGponDownFrameInfoEntry=_ZxGponDownFrameInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,12,3,1))
zxGponDownFrameInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponDownFrameInfoEntry.setStatus(_A)
class _ZxGponDownFrameInfoServices_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),('gem',2),(_q,3)))
_ZxGponDownFrameInfoServices_Type.__name__=_E
_ZxGponDownFrameInfoServices_Object=MibTableColumn
zxGponDownFrameInfoServices=_ZxGponDownFrameInfoServices_Object((1,3,6,1,4,1,3902,1012,3,12,3,1,1),_ZxGponDownFrameInfoServices_Type())
zxGponDownFrameInfoServices.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDownFrameInfoServices.setStatus(_A)
_ZxGponDownFrameInfoSIMinGranularity_Type=Integer32
_ZxGponDownFrameInfoSIMinGranularity_Object=MibTableColumn
zxGponDownFrameInfoSIMinGranularity=_ZxGponDownFrameInfoSIMinGranularity_Object((1,3,6,1,4,1,3902,1012,3,12,3,1,2),_ZxGponDownFrameInfoSIMinGranularity_Type())
zxGponDownFrameInfoSIMinGranularity.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDownFrameInfoSIMinGranularity.setStatus(_A)
class _ZxGponDownFrameInfoDbaMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sr',1),('nsr',2)))
_ZxGponDownFrameInfoDbaMethod_Type.__name__=_E
_ZxGponDownFrameInfoDbaMethod_Object=MibTableColumn
zxGponDownFrameInfoDbaMethod=_ZxGponDownFrameInfoDbaMethod_Object((1,3,6,1,4,1,3902,1012,3,12,3,1,3),_ZxGponDownFrameInfoDbaMethod_Type())
zxGponDownFrameInfoDbaMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDownFrameInfoDbaMethod.setStatus(_A)
_ZxGponDownFrameInfoScramblingEnable_Type=TruthValue
_ZxGponDownFrameInfoScramblingEnable_Object=MibTableColumn
zxGponDownFrameInfoScramblingEnable=_ZxGponDownFrameInfoScramblingEnable_Object((1,3,6,1,4,1,3902,1012,3,12,3,1,4),_ZxGponDownFrameInfoScramblingEnable_Type())
zxGponDownFrameInfoScramblingEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDownFrameInfoScramblingEnable.setStatus(_A)
_ZxGponDownFrameInfoFECEnable_Type=TruthValue
_ZxGponDownFrameInfoFECEnable_Object=MibTableColumn
zxGponDownFrameInfoFECEnable=_ZxGponDownFrameInfoFECEnable_Object((1,3,6,1,4,1,3902,1012,3,12,3,1,5),_ZxGponDownFrameInfoFECEnable_Type())
zxGponDownFrameInfoFECEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDownFrameInfoFECEnable.setStatus(_A)
class _ZxGponDownFrameInfoOnuSendDBRuMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notsend',1),('mode0',2),('mode1',3),('mode2',4)))
_ZxGponDownFrameInfoOnuSendDBRuMode_Type.__name__=_E
_ZxGponDownFrameInfoOnuSendDBRuMode_Object=MibTableColumn
zxGponDownFrameInfoOnuSendDBRuMode=_ZxGponDownFrameInfoOnuSendDBRuMode_Object((1,3,6,1,4,1,3902,1012,3,12,3,1,6),_ZxGponDownFrameInfoOnuSendDBRuMode_Type())
zxGponDownFrameInfoOnuSendDBRuMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDownFrameInfoOnuSendDBRuMode.setStatus(_A)
_ZxGponOltPmStatisticInfoTable_Object=MibTable
zxGponOltPmStatisticInfoTable=_ZxGponOltPmStatisticInfoTable_Object((1,3,6,1,4,1,3902,1012,3,12,4))
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoTable.setStatus(_A)
_ZxGponOltPmStatisticInfoEntry_Object=MibTableRow
zxGponOltPmStatisticInfoEntry=_ZxGponOltPmStatisticInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,12,4,1))
zxGponOltPmStatisticInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoEntry.setStatus(_A)
_ZxGponOltPmStatisticInfoGemPacketTx_Type=Integer32
_ZxGponOltPmStatisticInfoGemPacketTx_Object=MibTableColumn
zxGponOltPmStatisticInfoGemPacketTx=_ZxGponOltPmStatisticInfoGemPacketTx_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,1),_ZxGponOltPmStatisticInfoGemPacketTx_Type())
zxGponOltPmStatisticInfoGemPacketTx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoGemPacketTx.setStatus(_A)
_ZxGponOltPmStatisticInfoGemPacketRxCorIdle_Type=Integer32
_ZxGponOltPmStatisticInfoGemPacketRxCorIdle_Object=MibTableColumn
zxGponOltPmStatisticInfoGemPacketRxCorIdle=_ZxGponOltPmStatisticInfoGemPacketRxCorIdle_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,2),_ZxGponOltPmStatisticInfoGemPacketRxCorIdle_Type())
zxGponOltPmStatisticInfoGemPacketRxCorIdle.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoGemPacketRxCorIdle.setStatus(_A)
_ZxGponOltPmStatisticInfoGemPacketRxCorNoIdle_Type=Integer32
_ZxGponOltPmStatisticInfoGemPacketRxCorNoIdle_Object=MibTableColumn
zxGponOltPmStatisticInfoGemPacketRxCorNoIdle=_ZxGponOltPmStatisticInfoGemPacketRxCorNoIdle_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,3),_ZxGponOltPmStatisticInfoGemPacketRxCorNoIdle_Type())
zxGponOltPmStatisticInfoGemPacketRxCorNoIdle.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoGemPacketRxCorNoIdle.setStatus(_A)
_ZxGponOltPmStatisticInfoGemPacketRxErr_Type=Integer32
_ZxGponOltPmStatisticInfoGemPacketRxErr_Object=MibTableColumn
zxGponOltPmStatisticInfoGemPacketRxErr=_ZxGponOltPmStatisticInfoGemPacketRxErr_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,4),_ZxGponOltPmStatisticInfoGemPacketRxErr_Type())
zxGponOltPmStatisticInfoGemPacketRxErr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoGemPacketRxErr.setStatus(_A)
_ZxGponOltPmStatisticInfoGemPayloadBytesRx_Type=Integer32
_ZxGponOltPmStatisticInfoGemPayloadBytesRx_Object=MibTableColumn
zxGponOltPmStatisticInfoGemPayloadBytesRx=_ZxGponOltPmStatisticInfoGemPayloadBytesRx_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,5),_ZxGponOltPmStatisticInfoGemPayloadBytesRx_Type())
zxGponOltPmStatisticInfoGemPayloadBytesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoGemPayloadBytesRx.setStatus(_A)
_ZxGponOltPmStatisticInfoEthPacketTx_Type=Integer32
_ZxGponOltPmStatisticInfoEthPacketTx_Object=MibTableColumn
zxGponOltPmStatisticInfoEthPacketTx=_ZxGponOltPmStatisticInfoEthPacketTx_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,6),_ZxGponOltPmStatisticInfoEthPacketTx_Type())
zxGponOltPmStatisticInfoEthPacketTx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoEthPacketTx.setStatus(_A)
_ZxGponOltPmStatisticInfoEthPacketRxCor_Type=Integer32
_ZxGponOltPmStatisticInfoEthPacketRxCor_Object=MibTableColumn
zxGponOltPmStatisticInfoEthPacketRxCor=_ZxGponOltPmStatisticInfoEthPacketRxCor_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,7),_ZxGponOltPmStatisticInfoEthPacketRxCor_Type())
zxGponOltPmStatisticInfoEthPacketRxCor.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoEthPacketRxCor.setStatus(_A)
_ZxGponOltPmStatisticInfoEthPacketRxErr_Type=Integer32
_ZxGponOltPmStatisticInfoEthPacketRxErr_Object=MibTableColumn
zxGponOltPmStatisticInfoEthPacketRxErr=_ZxGponOltPmStatisticInfoEthPacketRxErr_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,8),_ZxGponOltPmStatisticInfoEthPacketRxErr_Type())
zxGponOltPmStatisticInfoEthPacketRxErr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoEthPacketRxErr.setStatus(_A)
_ZxGponOltPmStatisticInfoOmciPacketTx_Type=Integer32
_ZxGponOltPmStatisticInfoOmciPacketTx_Object=MibTableColumn
zxGponOltPmStatisticInfoOmciPacketTx=_ZxGponOltPmStatisticInfoOmciPacketTx_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,9),_ZxGponOltPmStatisticInfoOmciPacketTx_Type())
zxGponOltPmStatisticInfoOmciPacketTx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoOmciPacketTx.setStatus(_A)
_ZxGponOltPmStatisticInfoOmciPacketRxCor_Type=Integer32
_ZxGponOltPmStatisticInfoOmciPacketRxCor_Object=MibTableColumn
zxGponOltPmStatisticInfoOmciPacketRxCor=_ZxGponOltPmStatisticInfoOmciPacketRxCor_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,10),_ZxGponOltPmStatisticInfoOmciPacketRxCor_Type())
zxGponOltPmStatisticInfoOmciPacketRxCor.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoOmciPacketRxCor.setStatus(_A)
_ZxGponOltPmStatisticInfoOmciPacketRxErr_Type=Integer32
_ZxGponOltPmStatisticInfoOmciPacketRxErr_Object=MibTableColumn
zxGponOltPmStatisticInfoOmciPacketRxErr=_ZxGponOltPmStatisticInfoOmciPacketRxErr_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,11),_ZxGponOltPmStatisticInfoOmciPacketRxErr_Type())
zxGponOltPmStatisticInfoOmciPacketRxErr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoOmciPacketRxErr.setStatus(_A)
_ZxGponOltPmStatisticInfoPloamTx_Type=Integer32
_ZxGponOltPmStatisticInfoPloamTx_Object=MibTableColumn
zxGponOltPmStatisticInfoPloamTx=_ZxGponOltPmStatisticInfoPloamTx_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,12),_ZxGponOltPmStatisticInfoPloamTx_Type())
zxGponOltPmStatisticInfoPloamTx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoPloamTx.setStatus(_A)
_ZxGponOltPmStatisticInfoPloamRxCor_Type=Integer32
_ZxGponOltPmStatisticInfoPloamRxCor_Object=MibTableColumn
zxGponOltPmStatisticInfoPloamRxCor=_ZxGponOltPmStatisticInfoPloamRxCor_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,13),_ZxGponOltPmStatisticInfoPloamRxCor_Type())
zxGponOltPmStatisticInfoPloamRxCor.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoPloamRxCor.setStatus(_A)
_ZxGponOltPmStatisticInfoPloamRxErr_Type=Integer32
_ZxGponOltPmStatisticInfoPloamRxErr_Object=MibTableColumn
zxGponOltPmStatisticInfoPloamRxErr=_ZxGponOltPmStatisticInfoPloamRxErr_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,14),_ZxGponOltPmStatisticInfoPloamRxErr_Type())
zxGponOltPmStatisticInfoPloamRxErr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoPloamRxErr.setStatus(_A)
_ZxGponOltPmStatisticInfoERR_Type=Integer32
_ZxGponOltPmStatisticInfoERR_Object=MibTableColumn
zxGponOltPmStatisticInfoERR=_ZxGponOltPmStatisticInfoERR_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,15),_ZxGponOltPmStatisticInfoERR_Type())
zxGponOltPmStatisticInfoERR.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoERR.setStatus(_A)
_ZxGponOltPmStatisticInfoREI_Type=Integer32
_ZxGponOltPmStatisticInfoREI_Object=MibTableColumn
zxGponOltPmStatisticInfoREI=_ZxGponOltPmStatisticInfoREI_Object((1,3,6,1,4,1,3902,1012,3,12,4,1,16),_ZxGponOltPmStatisticInfoREI_Type())
zxGponOltPmStatisticInfoREI.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisticInfoREI.setStatus(_A)
_ZxGponFindOnuTimerTable_Object=MibTable
zxGponFindOnuTimerTable=_ZxGponFindOnuTimerTable_Object((1,3,6,1,4,1,3902,1012,3,12,7))
if mibBuilder.loadTexts:zxGponFindOnuTimerTable.setStatus(_A)
_ZxGponFindOnuTimerEntry_Object=MibTableRow
zxGponFindOnuTimerEntry=_ZxGponFindOnuTimerEntry_Object((1,3,6,1,4,1,3902,1012,3,12,7,1))
zxGponFindOnuTimerEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponFindOnuTimerEntry.setStatus(_A)
_ZxGPonFindOnuTimerNewOnt_Type=Integer32
_ZxGPonFindOnuTimerNewOnt_Object=MibTableColumn
zxGPonFindOnuTimerNewOnt=_ZxGPonFindOnuTimerNewOnt_Object((1,3,6,1,4,1,3902,1012,3,12,7,1,1),_ZxGPonFindOnuTimerNewOnt_Type())
zxGPonFindOnuTimerNewOnt.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGPonFindOnuTimerNewOnt.setStatus(_A)
_ZxGponFindOnuTimerMissingOnt_Type=Integer32
_ZxGponFindOnuTimerMissingOnt_Object=MibTableColumn
zxGponFindOnuTimerMissingOnt=_ZxGponFindOnuTimerMissingOnt_Object((1,3,6,1,4,1,3902,1012,3,12,7,1,2),_ZxGponFindOnuTimerMissingOnt_Type())
zxGponFindOnuTimerMissingOnt.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponFindOnuTimerMissingOnt.setStatus(_A)
_ZxGPonFindOnuTimerOpenWindowFrame_Type=Integer32
_ZxGPonFindOnuTimerOpenWindowFrame_Object=MibTableColumn
zxGPonFindOnuTimerOpenWindowFrame=_ZxGPonFindOnuTimerOpenWindowFrame_Object((1,3,6,1,4,1,3902,1012,3,12,7,1,3),_ZxGPonFindOnuTimerOpenWindowFrame_Type())
zxGPonFindOnuTimerOpenWindowFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGPonFindOnuTimerOpenWindowFrame.setStatus(_A)
_ZxGponOltAlarmTable_Object=MibTable
zxGponOltAlarmTable=_ZxGponOltAlarmTable_Object((1,3,6,1,4,1,3902,1012,3,12,8))
if mibBuilder.loadTexts:zxGponOltAlarmTable.setStatus(_A)
_ZxGponOltAlarmEntry_Object=MibTableRow
zxGponOltAlarmEntry=_ZxGponOltAlarmEntry_Object((1,3,6,1,4,1,3902,1012,3,12,8,1))
zxGponOltAlarmEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltAlarmEntry.setStatus(_A)
_ZxGPonOltAlarmLos_Type=TruthValue
_ZxGPonOltAlarmLos_Object=MibTableColumn
zxGPonOltAlarmLos=_ZxGPonOltAlarmLos_Object((1,3,6,1,4,1,3902,1012,3,12,8,1,1),_ZxGPonOltAlarmLos_Type())
zxGPonOltAlarmLos.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGPonOltAlarmLos.setStatus(_A)
_ZxGponOltAlarmLosMask_Type=TruthValue
_ZxGponOltAlarmLosMask_Object=MibTableColumn
zxGponOltAlarmLosMask=_ZxGponOltAlarmLosMask_Object((1,3,6,1,4,1,3902,1012,3,12,8,1,2),_ZxGponOltAlarmLosMask_Type())
zxGponOltAlarmLosMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltAlarmLosMask.setStatus(_A)
_ZxGponOltAlarmTF_Type=TruthValue
_ZxGponOltAlarmTF_Object=MibTableColumn
zxGponOltAlarmTF=_ZxGponOltAlarmTF_Object((1,3,6,1,4,1,3902,1012,3,12,8,1,3),_ZxGponOltAlarmTF_Type())
zxGponOltAlarmTF.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltAlarmTF.setStatus(_A)
_ZxGponOltAlarmTFMask_Type=TruthValue
_ZxGponOltAlarmTFMask_Object=MibTableColumn
zxGponOltAlarmTFMask=_ZxGponOltAlarmTFMask_Object((1,3,6,1,4,1,3902,1012,3,12,8,1,4),_ZxGponOltAlarmTFMask_Type())
zxGponOltAlarmTFMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltAlarmTFMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideTable_Object=MibTable
zxGponOntUpAlarmOltSideTable=_ZxGponOntUpAlarmOltSideTable_Object((1,3,6,1,4,1,3902,1012,3,12,9))
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideTable.setStatus(_A)
_ZxGponOntUpAlarmOltSideEntry_Object=MibTableRow
zxGponOntUpAlarmOltSideEntry=_ZxGponOntUpAlarmOltSideEntry_Object((1,3,6,1,4,1,3902,1012,3,12,9,1))
zxGponOntUpAlarmOltSideEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideEntry.setStatus(_A)
_ZxGponOntUpAlarmOltSideLOSui_Type=TruthValue
_ZxGponOntUpAlarmOltSideLOSui_Object=MibTableColumn
zxGponOntUpAlarmOltSideLOSui=_ZxGponOntUpAlarmOltSideLOSui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,1),_ZxGponOntUpAlarmOltSideLOSui_Type())
zxGponOntUpAlarmOltSideLOSui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLOSui.setStatus(_A)
_ZxGponOntUpAlarmOltSideLOSuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideLOSuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideLOSuiMask=_ZxGponOntUpAlarmOltSideLOSuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,2),_ZxGponOntUpAlarmOltSideLOSuiMask_Type())
zxGponOntUpAlarmOltSideLOSuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLOSuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideLOFui_Type=TruthValue
_ZxGponOntUpAlarmOltSideLOFui_Object=MibTableColumn
zxGponOntUpAlarmOltSideLOFui=_ZxGponOntUpAlarmOltSideLOFui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,3),_ZxGponOntUpAlarmOltSideLOFui_Type())
zxGponOntUpAlarmOltSideLOFui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLOFui.setStatus(_A)
_ZxGponOntUpAlarmOltSideLOFuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideLOFuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideLOFuiMask=_ZxGponOntUpAlarmOltSideLOFuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,4),_ZxGponOntUpAlarmOltSideLOFuiMask_Type())
zxGponOntUpAlarmOltSideLOFuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLOFuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideDOWui_Type=TruthValue
_ZxGponOntUpAlarmOltSideDOWui_Object=MibTableColumn
zxGponOntUpAlarmOltSideDOWui=_ZxGponOntUpAlarmOltSideDOWui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,5),_ZxGponOntUpAlarmOltSideDOWui_Type())
zxGponOntUpAlarmOltSideDOWui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideDOWui.setStatus(_A)
_ZxGponOntUpAlarmOltSideDOWuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideDOWuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideDOWuiMask=_ZxGponOntUpAlarmOltSideDOWuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,6),_ZxGponOntUpAlarmOltSideDOWuiMask_Type())
zxGponOntUpAlarmOltSideDOWuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideDOWuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideSFui_Type=TruthValue
_ZxGponOntUpAlarmOltSideSFui_Object=MibTableColumn
zxGponOntUpAlarmOltSideSFui=_ZxGponOntUpAlarmOltSideSFui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,7),_ZxGponOntUpAlarmOltSideSFui_Type())
zxGponOntUpAlarmOltSideSFui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideSFui.setStatus(_A)
_ZxGponOntUpAlarmOltSideSFuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideSFuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideSFuiMask=_ZxGponOntUpAlarmOltSideSFuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,8),_ZxGponOntUpAlarmOltSideSFuiMask_Type())
zxGponOntUpAlarmOltSideSFuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideSFuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideSDui_Type=TruthValue
_ZxGponOntUpAlarmOltSideSDui_Object=MibTableColumn
zxGponOntUpAlarmOltSideSDui=_ZxGponOntUpAlarmOltSideSDui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,9),_ZxGponOntUpAlarmOltSideSDui_Type())
zxGponOntUpAlarmOltSideSDui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideSDui.setStatus(_A)
_ZxGponOntUpAlarmOltSideSDuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideSDuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideSDuiMask=_ZxGponOntUpAlarmOltSideSDuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,10),_ZxGponOntUpAlarmOltSideSDuiMask_Type())
zxGponOntUpAlarmOltSideSDuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideSDuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideLCDAui_Type=TruthValue
_ZxGponOntUpAlarmOltSideLCDAui_Object=MibTableColumn
zxGponOntUpAlarmOltSideLCDAui=_ZxGponOntUpAlarmOltSideLCDAui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,11),_ZxGponOntUpAlarmOltSideLCDAui_Type())
zxGponOntUpAlarmOltSideLCDAui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLCDAui.setStatus(_A)
_ZxGponOntUpAlarmOltSideLCDAuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideLCDAuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideLCDAuiMask=_ZxGponOntUpAlarmOltSideLCDAuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,12),_ZxGponOntUpAlarmOltSideLCDAuiMask_Type())
zxGponOntUpAlarmOltSideLCDAuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLCDAuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideLCDGui_Type=TruthValue
_ZxGponOntUpAlarmOltSideLCDGui_Object=MibTableColumn
zxGponOntUpAlarmOltSideLCDGui=_ZxGponOntUpAlarmOltSideLCDGui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,13),_ZxGponOntUpAlarmOltSideLCDGui_Type())
zxGponOntUpAlarmOltSideLCDGui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLCDGui.setStatus(_A)
_ZxGponOntUpAlarmOltSideLCDGuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideLCDGuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideLCDGuiMask=_ZxGponOntUpAlarmOltSideLCDGuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,14),_ZxGponOntUpAlarmOltSideLCDGuiMask_Type())
zxGponOntUpAlarmOltSideLCDGuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLCDGuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideRDIui_Type=TruthValue
_ZxGponOntUpAlarmOltSideRDIui_Object=MibTableColumn
zxGponOntUpAlarmOltSideRDIui=_ZxGponOntUpAlarmOltSideRDIui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,15),_ZxGponOntUpAlarmOltSideRDIui_Type())
zxGponOntUpAlarmOltSideRDIui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideRDIui.setStatus(_A)
_ZxGponOntUpAlarmOltSideRDIuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideRDIuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideRDIuiMask=_ZxGponOntUpAlarmOltSideRDIuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,16),_ZxGponOntUpAlarmOltSideRDIuiMask_Type())
zxGponOntUpAlarmOltSideRDIuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideRDIuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideSUFui_Type=TruthValue
_ZxGponOntUpAlarmOltSideSUFui_Object=MibTableColumn
zxGponOntUpAlarmOltSideSUFui=_ZxGponOntUpAlarmOltSideSUFui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,17),_ZxGponOntUpAlarmOltSideSUFui_Type())
zxGponOntUpAlarmOltSideSUFui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideSUFui.setStatus(_A)
_ZxGponOntUpAlarmOltSideSUFuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideSUFuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideSUFuiMask=_ZxGponOntUpAlarmOltSideSUFuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,18),_ZxGponOntUpAlarmOltSideSUFuiMask_Type())
zxGponOntUpAlarmOltSideSUFuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideSUFuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideDFui_Type=TruthValue
_ZxGponOntUpAlarmOltSideDFui_Object=MibTableColumn
zxGponOntUpAlarmOltSideDFui=_ZxGponOntUpAlarmOltSideDFui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,19),_ZxGponOntUpAlarmOltSideDFui_Type())
zxGponOntUpAlarmOltSideDFui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideDFui.setStatus(_A)
_ZxGponOntUpAlarmOltSideDFuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideDFuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideDFuiMask=_ZxGponOntUpAlarmOltSideDFuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,20),_ZxGponOntUpAlarmOltSideDFuiMask_Type())
zxGponOntUpAlarmOltSideDFuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideDFuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideLOAui_Type=TruthValue
_ZxGponOntUpAlarmOltSideLOAui_Object=MibTableColumn
zxGponOntUpAlarmOltSideLOAui=_ZxGponOntUpAlarmOltSideLOAui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,21),_ZxGponOntUpAlarmOltSideLOAui_Type())
zxGponOntUpAlarmOltSideLOAui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLOAui.setStatus(_A)
_ZxGponOntUpAlarmOltSideLOAuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideLOAuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideLOAuiMask=_ZxGponOntUpAlarmOltSideLOAuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,22),_ZxGponOntUpAlarmOltSideLOAuiMask_Type())
zxGponOntUpAlarmOltSideLOAuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLOAuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideDGui_Type=TruthValue
_ZxGponOntUpAlarmOltSideDGui_Object=MibTableColumn
zxGponOntUpAlarmOltSideDGui=_ZxGponOntUpAlarmOltSideDGui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,23),_ZxGponOntUpAlarmOltSideDGui_Type())
zxGponOntUpAlarmOltSideDGui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideDGui.setStatus(_A)
_ZxGponOntUpAlarmOltSideDGuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideDGuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideDGuiMask=_ZxGponOntUpAlarmOltSideDGuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,24),_ZxGponOntUpAlarmOltSideDGuiMask_Type())
zxGponOntUpAlarmOltSideDGuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideDGuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideLOAMui_Type=TruthValue
_ZxGponOntUpAlarmOltSideLOAMui_Object=MibTableColumn
zxGponOntUpAlarmOltSideLOAMui=_ZxGponOntUpAlarmOltSideLOAMui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,25),_ZxGponOntUpAlarmOltSideLOAMui_Type())
zxGponOntUpAlarmOltSideLOAMui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLOAMui.setStatus(_A)
_ZxGponOntUpAlarmOltSideLOAMuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideLOAMuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideLOAMuiMask=_ZxGponOntUpAlarmOltSideLOAMuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,26),_ZxGponOntUpAlarmOltSideLOAMuiMask_Type())
zxGponOntUpAlarmOltSideLOAMuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideLOAMuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideMEMui_Type=TruthValue
_ZxGponOntUpAlarmOltSideMEMui_Object=MibTableColumn
zxGponOntUpAlarmOltSideMEMui=_ZxGponOntUpAlarmOltSideMEMui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,27),_ZxGponOntUpAlarmOltSideMEMui_Type())
zxGponOntUpAlarmOltSideMEMui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideMEMui.setStatus(_A)
_ZxGponOntUpAlarmOltSideMEMuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideMEMuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideMEMuiMask=_ZxGponOntUpAlarmOltSideMEMuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,28),_ZxGponOntUpAlarmOltSideMEMuiMask_Type())
zxGponOntUpAlarmOltSideMEMuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideMEMuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSideMISui_Type=TruthValue
_ZxGponOntUpAlarmOltSideMISui_Object=MibTableColumn
zxGponOntUpAlarmOltSideMISui=_ZxGponOntUpAlarmOltSideMISui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,29),_ZxGponOntUpAlarmOltSideMISui_Type())
zxGponOntUpAlarmOltSideMISui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideMISui.setStatus(_A)
_ZxGponOntUpAlarmOltSideMISuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSideMISuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSideMISuiMask=_ZxGponOntUpAlarmOltSideMISuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,30),_ZxGponOntUpAlarmOltSideMISuiMask_Type())
zxGponOntUpAlarmOltSideMISuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSideMISuiMask.setStatus(_A)
_ZxGponOntUpAlarmOltSidePEEui_Type=TruthValue
_ZxGponOntUpAlarmOltSidePEEui_Object=MibTableColumn
zxGponOntUpAlarmOltSidePEEui=_ZxGponOntUpAlarmOltSidePEEui_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,31),_ZxGponOntUpAlarmOltSidePEEui_Type())
zxGponOntUpAlarmOltSidePEEui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSidePEEui.setStatus(_A)
_ZxGponOntUpAlarmOltSidePEEuiMask_Type=TruthValue
_ZxGponOntUpAlarmOltSidePEEuiMask_Object=MibTableColumn
zxGponOntUpAlarmOltSidePEEuiMask=_ZxGponOntUpAlarmOltSidePEEuiMask_Object((1,3,6,1,4,1,3902,1012,3,12,9,1,32),_ZxGponOntUpAlarmOltSidePEEuiMask_Type())
zxGponOntUpAlarmOltSidePEEuiMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntUpAlarmOltSidePEEuiMask.setStatus(_A)
_ZxGponBerDowThresholdTable_Object=MibTable
zxGponBerDowThresholdTable=_ZxGponBerDowThresholdTable_Object((1,3,6,1,4,1,3902,1012,3,12,10))
if mibBuilder.loadTexts:zxGponBerDowThresholdTable.setStatus(_A)
_ZxGponBerDowThresholdEntry_Object=MibTableRow
zxGponBerDowThresholdEntry=_ZxGponBerDowThresholdEntry_Object((1,3,6,1,4,1,3902,1012,3,12,10,1))
zxGponBerDowThresholdEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponBerDowThresholdEntry.setStatus(_A)
_ZxGponBerDowThresholdSDui_Type=Integer32
_ZxGponBerDowThresholdSDui_Object=MibTableColumn
zxGponBerDowThresholdSDui=_ZxGponBerDowThresholdSDui_Object((1,3,6,1,4,1,3902,1012,3,12,10,1,1),_ZxGponBerDowThresholdSDui_Type())
zxGponBerDowThresholdSDui.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBerDowThresholdSDui.setStatus(_A)
_ZxGponBerDowThresholdSFui_Type=Integer32
_ZxGponBerDowThresholdSFui_Object=MibTableColumn
zxGponBerDowThresholdSFui=_ZxGponBerDowThresholdSFui_Object((1,3,6,1,4,1,3902,1012,3,12,10,1,2),_ZxGponBerDowThresholdSFui_Type())
zxGponBerDowThresholdSFui.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBerDowThresholdSFui.setStatus(_A)
_ZxGponBerDowThresholdDOWi_Type=Integer32
_ZxGponBerDowThresholdDOWi_Object=MibTableColumn
zxGponBerDowThresholdDOWi=_ZxGponBerDowThresholdDOWi_Object((1,3,6,1,4,1,3902,1012,3,12,10,1,3),_ZxGponBerDowThresholdDOWi_Type())
zxGponBerDowThresholdDOWi.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBerDowThresholdDOWi.setStatus(_A)
_ZxGponOntUpPmOltSideTable_Object=MibTable
zxGponOntUpPmOltSideTable=_ZxGponOntUpPmOltSideTable_Object((1,3,6,1,4,1,3902,1012,3,12,11))
if mibBuilder.loadTexts:zxGponOntUpPmOltSideTable.setStatus(_A)
_ZxGponOntUpPmOltSideEntry_Object=MibTableRow
zxGponOntUpPmOltSideEntry=_ZxGponOntUpPmOltSideEntry_Object((1,3,6,1,4,1,3902,1012,3,12,11,1))
zxGponOntUpPmOltSideEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntUpPmOltSideEntry.setStatus(_A)
_ZxGponOntUpPmOltSideERRui_Type=Counter64
_ZxGponOntUpPmOltSideERRui_Object=MibTableColumn
zxGponOntUpPmOltSideERRui=_ZxGponOntUpPmOltSideERRui_Object((1,3,6,1,4,1,3902,1012,3,12,11,1,1),_ZxGponOntUpPmOltSideERRui_Type())
zxGponOntUpPmOltSideERRui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpPmOltSideERRui.setStatus(_A)
_ZxGponOntUpPmOltSideREIui_Type=Counter64
_ZxGponOntUpPmOltSideREIui_Object=MibTableColumn
zxGponOntUpPmOltSideREIui=_ZxGponOntUpPmOltSideREIui_Object((1,3,6,1,4,1,3902,1012,3,12,11,1,2),_ZxGponOntUpPmOltSideREIui_Type())
zxGponOntUpPmOltSideREIui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpPmOltSideREIui.setStatus(_A)
_ZxGponOntUpPmOltSideCorrNIdleGemFramesui_Type=Counter64
_ZxGponOntUpPmOltSideCorrNIdleGemFramesui_Object=MibTableColumn
zxGponOntUpPmOltSideCorrNIdleGemFramesui=_ZxGponOntUpPmOltSideCorrNIdleGemFramesui_Object((1,3,6,1,4,1,3902,1012,3,12,11,1,3),_ZxGponOntUpPmOltSideCorrNIdleGemFramesui_Type())
zxGponOntUpPmOltSideCorrNIdleGemFramesui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpPmOltSideCorrNIdleGemFramesui.setStatus(_A)
_ZxGponOntUpPmOltSideCorrIdleGemFramesui_Type=Counter64
_ZxGponOntUpPmOltSideCorrIdleGemFramesui_Object=MibTableColumn
zxGponOntUpPmOltSideCorrIdleGemFramesui=_ZxGponOntUpPmOltSideCorrIdleGemFramesui_Object((1,3,6,1,4,1,3902,1012,3,12,11,1,4),_ZxGponOntUpPmOltSideCorrIdleGemFramesui_Type())
zxGponOntUpPmOltSideCorrIdleGemFramesui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpPmOltSideCorrIdleGemFramesui.setStatus(_A)
_ZxGponOntUpPmOltSideErroredGemFramesui_Type=Counter64
_ZxGponOntUpPmOltSideErroredGemFramesui_Object=MibTableColumn
zxGponOntUpPmOltSideErroredGemFramesui=_ZxGponOntUpPmOltSideErroredGemFramesui_Object((1,3,6,1,4,1,3902,1012,3,12,11,1,5),_ZxGponOntUpPmOltSideErroredGemFramesui_Type())
zxGponOntUpPmOltSideErroredGemFramesui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpPmOltSideErroredGemFramesui.setStatus(_A)
_ZxGponOntUpPmOltSideGemPayloadBytesui_Type=Counter64
_ZxGponOntUpPmOltSideGemPayloadBytesui_Object=MibTableColumn
zxGponOntUpPmOltSideGemPayloadBytesui=_ZxGponOntUpPmOltSideGemPayloadBytesui_Object((1,3,6,1,4,1,3902,1012,3,12,11,1,6),_ZxGponOntUpPmOltSideGemPayloadBytesui_Type())
zxGponOntUpPmOltSideGemPayloadBytesui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpPmOltSideGemPayloadBytesui.setStatus(_A)
_ZxGponOntUpPmOltSideCorrectEthFramesui_Type=Counter64
_ZxGponOntUpPmOltSideCorrectEthFramesui_Object=MibTableColumn
zxGponOntUpPmOltSideCorrectEthFramesui=_ZxGponOntUpPmOltSideCorrectEthFramesui_Object((1,3,6,1,4,1,3902,1012,3,12,11,1,7),_ZxGponOntUpPmOltSideCorrectEthFramesui_Type())
zxGponOntUpPmOltSideCorrectEthFramesui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpPmOltSideCorrectEthFramesui.setStatus(_A)
_ZxGponOntUpPmOltSideErroredEthFramesui_Type=Counter64
_ZxGponOntUpPmOltSideErroredEthFramesui_Object=MibTableColumn
zxGponOntUpPmOltSideErroredEthFramesui=_ZxGponOntUpPmOltSideErroredEthFramesui_Object((1,3,6,1,4,1,3902,1012,3,12,11,1,8),_ZxGponOntUpPmOltSideErroredEthFramesui_Type())
zxGponOntUpPmOltSideErroredEthFramesui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpPmOltSideErroredEthFramesui.setStatus(_A)
_ZxGponOntUpPmOltSideTotalOmciFramesui_Type=Counter64
_ZxGponOntUpPmOltSideTotalOmciFramesui_Object=MibTableColumn
zxGponOntUpPmOltSideTotalOmciFramesui=_ZxGponOntUpPmOltSideTotalOmciFramesui_Object((1,3,6,1,4,1,3902,1012,3,12,11,1,9),_ZxGponOntUpPmOltSideTotalOmciFramesui_Type())
zxGponOntUpPmOltSideTotalOmciFramesui.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUpPmOltSideTotalOmciFramesui.setStatus(_A)
_ZxGponOltUpPmTable_Object=MibTable
zxGponOltUpPmTable=_ZxGponOltUpPmTable_Object((1,3,6,1,4,1,3902,1012,3,12,12))
if mibBuilder.loadTexts:zxGponOltUpPmTable.setStatus(_A)
_ZxGponOltUpPmEntry_Object=MibTableRow
zxGponOltUpPmEntry=_ZxGponOltUpPmEntry_Object((1,3,6,1,4,1,3902,1012,3,12,12,1))
zxGponOltUpPmEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltUpPmEntry.setStatus(_A)
_ZxGponOltUpPmERRu_Type=Counter64
_ZxGponOltUpPmERRu_Object=MibTableColumn
zxGponOltUpPmERRu=_ZxGponOltUpPmERRu_Object((1,3,6,1,4,1,3902,1012,3,12,12,1,1),_ZxGponOltUpPmERRu_Type())
zxGponOltUpPmERRu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltUpPmERRu.setStatus(_A)
_ZxGponOltUpPmREIu_Type=Counter64
_ZxGponOltUpPmREIu_Object=MibTableColumn
zxGponOltUpPmREIu=_ZxGponOltUpPmREIu_Object((1,3,6,1,4,1,3902,1012,3,12,12,1,2),_ZxGponOltUpPmREIu_Type())
zxGponOltUpPmREIu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltUpPmREIu.setStatus(_A)
_ZxGponOltUpPmCorrNIdleGemFramesu_Type=Counter64
_ZxGponOltUpPmCorrNIdleGemFramesu_Object=MibTableColumn
zxGponOltUpPmCorrNIdleGemFramesu=_ZxGponOltUpPmCorrNIdleGemFramesu_Object((1,3,6,1,4,1,3902,1012,3,12,12,1,3),_ZxGponOltUpPmCorrNIdleGemFramesu_Type())
zxGponOltUpPmCorrNIdleGemFramesu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltUpPmCorrNIdleGemFramesu.setStatus(_A)
_ZxGponOltUpPmCorrIdleGemFramesu_Type=Counter64
_ZxGponOltUpPmCorrIdleGemFramesu_Object=MibTableColumn
zxGponOltUpPmCorrIdleGemFramesu=_ZxGponOltUpPmCorrIdleGemFramesu_Object((1,3,6,1,4,1,3902,1012,3,12,12,1,4),_ZxGponOltUpPmCorrIdleGemFramesu_Type())
zxGponOltUpPmCorrIdleGemFramesu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltUpPmCorrIdleGemFramesu.setStatus(_A)
_ZxGponOltUpPmErroredGemFramesu_Type=Counter64
_ZxGponOltUpPmErroredGemFramesu_Object=MibTableColumn
zxGponOltUpPmErroredGemFramesu=_ZxGponOltUpPmErroredGemFramesu_Object((1,3,6,1,4,1,3902,1012,3,12,12,1,5),_ZxGponOltUpPmErroredGemFramesu_Type())
zxGponOltUpPmErroredGemFramesu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltUpPmErroredGemFramesu.setStatus(_A)
_ZxGponOltUpPmGemPayloadBytesu_Type=Counter64
_ZxGponOltUpPmGemPayloadBytesu_Object=MibTableColumn
zxGponOltUpPmGemPayloadBytesu=_ZxGponOltUpPmGemPayloadBytesu_Object((1,3,6,1,4,1,3902,1012,3,12,12,1,6),_ZxGponOltUpPmGemPayloadBytesu_Type())
zxGponOltUpPmGemPayloadBytesu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltUpPmGemPayloadBytesu.setStatus(_A)
_ZxGponOltUpPmCorrectEthFramesu_Type=Counter64
_ZxGponOltUpPmCorrectEthFramesu_Object=MibTableColumn
zxGponOltUpPmCorrectEthFramesu=_ZxGponOltUpPmCorrectEthFramesu_Object((1,3,6,1,4,1,3902,1012,3,12,12,1,7),_ZxGponOltUpPmCorrectEthFramesu_Type())
zxGponOltUpPmCorrectEthFramesu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltUpPmCorrectEthFramesu.setStatus(_A)
_ZxGponOltUpPmErroredEthFramesu_Type=Counter64
_ZxGponOltUpPmErroredEthFramesu_Object=MibTableColumn
zxGponOltUpPmErroredEthFramesu=_ZxGponOltUpPmErroredEthFramesu_Object((1,3,6,1,4,1,3902,1012,3,12,12,1,8),_ZxGponOltUpPmErroredEthFramesu_Type())
zxGponOltUpPmErroredEthFramesu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltUpPmErroredEthFramesu.setStatus(_A)
_ZxGponOltUpPmTotalOmciFramesu_Type=Counter64
_ZxGponOltUpPmTotalOmciFramesu_Object=MibTableColumn
zxGponOltUpPmTotalOmciFramesu=_ZxGponOltUpPmTotalOmciFramesu_Object((1,3,6,1,4,1,3902,1012,3,12,12,1,9),_ZxGponOltUpPmTotalOmciFramesu_Type())
zxGponOltUpPmTotalOmciFramesu.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltUpPmTotalOmciFramesu.setStatus(_A)
_ZxGponOltPmStatisRealtimeInfoTable_Object=MibTable
zxGponOltPmStatisRealtimeInfoTable=_ZxGponOltPmStatisRealtimeInfoTable_Object((1,3,6,1,4,1,3902,1012,3,12,13))
if mibBuilder.loadTexts:zxGponOltPmStatisRealtimeInfoTable.setStatus(_A)
_ZxGponOltPmStatisRealtimeInfoEntry_Object=MibTableRow
zxGponOltPmStatisRealtimeInfoEntry=_ZxGponOltPmStatisRealtimeInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,12,13,1))
zxGponOltPmStatisRealtimeInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltPmStatisRealtimeInfoEntry.setStatus(_A)
_ZxGponOltPmStatisInfoCorrectNonIdleGemFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisInfoCorrectNonIdleGemFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisInfoCorrectNonIdleGemFramesUpstream=_ZxGponOltPmStatisInfoCorrectNonIdleGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,1),_ZxGponOltPmStatisInfoCorrectNonIdleGemFramesUpstream_Type())
zxGponOltPmStatisInfoCorrectNonIdleGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoCorrectNonIdleGemFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisInfoCorrectIdleGemFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisInfoCorrectIdleGemFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisInfoCorrectIdleGemFramesUpstream=_ZxGponOltPmStatisInfoCorrectIdleGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,2),_ZxGponOltPmStatisInfoCorrectIdleGemFramesUpstream_Type())
zxGponOltPmStatisInfoCorrectIdleGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoCorrectIdleGemFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisInfoErroredGemFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisInfoErroredGemFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisInfoErroredGemFramesUpstream=_ZxGponOltPmStatisInfoErroredGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,3),_ZxGponOltPmStatisInfoErroredGemFramesUpstream_Type())
zxGponOltPmStatisInfoErroredGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoErroredGemFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisInfoGemPayloadBytesUpstream_Type=Unsigned32
_ZxGponOltPmStatisInfoGemPayloadBytesUpstream_Object=MibTableColumn
zxGponOltPmStatisInfoGemPayloadBytesUpstream=_ZxGponOltPmStatisInfoGemPayloadBytesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,4),_ZxGponOltPmStatisInfoGemPayloadBytesUpstream_Type())
zxGponOltPmStatisInfoGemPayloadBytesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoGemPayloadBytesUpstream.setStatus(_A)
_ZxGponOltPmStatisInfoCorrectEthernetFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisInfoCorrectEthernetFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisInfoCorrectEthernetFramesUpstream=_ZxGponOltPmStatisInfoCorrectEthernetFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,5),_ZxGponOltPmStatisInfoCorrectEthernetFramesUpstream_Type())
zxGponOltPmStatisInfoCorrectEthernetFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoCorrectEthernetFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisInfoErroredEthernetFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisInfoErroredEthernetFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisInfoErroredEthernetFramesUpstream=_ZxGponOltPmStatisInfoErroredEthernetFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,6),_ZxGponOltPmStatisInfoErroredEthernetFramesUpstream_Type())
zxGponOltPmStatisInfoErroredEthernetFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoErroredEthernetFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisInfoTotalOmciFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisInfoTotalOmciFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisInfoTotalOmciFramesUpstream=_ZxGponOltPmStatisInfoTotalOmciFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,7),_ZxGponOltPmStatisInfoTotalOmciFramesUpstream_Type())
zxGponOltPmStatisInfoTotalOmciFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoTotalOmciFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisInfoERR_Type=Unsigned32
_ZxGponOltPmStatisInfoERR_Object=MibTableColumn
zxGponOltPmStatisInfoERR=_ZxGponOltPmStatisInfoERR_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,8),_ZxGponOltPmStatisInfoERR_Type())
zxGponOltPmStatisInfoERR.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoERR.setStatus(_A)
_ZxGponOltPmStatisInfoREI_Type=Unsigned32
_ZxGponOltPmStatisInfoREI_Object=MibTableColumn
zxGponOltPmStatisInfoREI=_ZxGponOltPmStatisInfoREI_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,9),_ZxGponOltPmStatisInfoREI_Type())
zxGponOltPmStatisInfoREI.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoREI.setStatus(_A)
_ZxGponOltPmStatisInfoValidEthernetPacketDownstream_Type=Unsigned32
_ZxGponOltPmStatisInfoValidEthernetPacketDownstream_Object=MibTableColumn
zxGponOltPmStatisInfoValidEthernetPacketDownstream=_ZxGponOltPmStatisInfoValidEthernetPacketDownstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,10),_ZxGponOltPmStatisInfoValidEthernetPacketDownstream_Type())
zxGponOltPmStatisInfoValidEthernetPacketDownstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoValidEthernetPacketDownstream.setStatus(_A)
_ZxGponOltPmStatisInfoCpuPacketDownstream_Type=Unsigned32
_ZxGponOltPmStatisInfoCpuPacketDownstream_Object=MibTableColumn
zxGponOltPmStatisInfoCpuPacketDownstream=_ZxGponOltPmStatisInfoCpuPacketDownstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,11),_ZxGponOltPmStatisInfoCpuPacketDownstream_Type())
zxGponOltPmStatisInfoCpuPacketDownstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoCpuPacketDownstream.setStatus(_A)
_ZxGponOltPmStatisInfoPloamDownstream_Type=Unsigned32
_ZxGponOltPmStatisInfoPloamDownstream_Object=MibTableColumn
zxGponOltPmStatisInfoPloamDownstream=_ZxGponOltPmStatisInfoPloamDownstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,12),_ZxGponOltPmStatisInfoPloamDownstream_Type())
zxGponOltPmStatisInfoPloamDownstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoPloamDownstream.setStatus(_A)
_ZxGponOltPmStatisInfoPloamUpstream_Type=Unsigned32
_ZxGponOltPmStatisInfoPloamUpstream_Object=MibTableColumn
zxGponOltPmStatisInfoPloamUpstream=_ZxGponOltPmStatisInfoPloamUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,13),_ZxGponOltPmStatisInfoPloamUpstream_Type())
zxGponOltPmStatisInfoPloamUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoPloamUpstream.setStatus(_A)
_ZxGponOltPmStatisInfoInvalidPacketUpstream_Type=Unsigned32
_ZxGponOltPmStatisInfoInvalidPacketUpstream_Object=MibTableColumn
zxGponOltPmStatisInfoInvalidPacketUpstream=_ZxGponOltPmStatisInfoInvalidPacketUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,13,1,14),_ZxGponOltPmStatisInfoInvalidPacketUpstream_Type())
zxGponOltPmStatisInfoInvalidPacketUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisInfoInvalidPacketUpstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoTable_Object=MibTable
zxGponOltPmStatisHistoryInfoTable=_ZxGponOltPmStatisHistoryInfoTable_Object((1,3,6,1,4,1,3902,1012,3,12,14))
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoTable.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoEntry_Object=MibTableRow
zxGponOltPmStatisHistoryInfoEntry=_ZxGponOltPmStatisHistoryInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,12,14,1))
zxGponOltPmStatisHistoryInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoEntry.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream=_ZxGponOltPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,1),_ZxGponOltPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream_Type())
zxGponOltPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoCorrectIdleGemFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoCorrectIdleGemFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoCorrectIdleGemFramesUpstream=_ZxGponOltPmStatisHistoryInfoCorrectIdleGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,2),_ZxGponOltPmStatisHistoryInfoCorrectIdleGemFramesUpstream_Type())
zxGponOltPmStatisHistoryInfoCorrectIdleGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoCorrectIdleGemFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoErroredGemFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoErroredGemFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoErroredGemFramesUpstream=_ZxGponOltPmStatisHistoryInfoErroredGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,3),_ZxGponOltPmStatisHistoryInfoErroredGemFramesUpstream_Type())
zxGponOltPmStatisHistoryInfoErroredGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoErroredGemFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoGemPayloadBytesUpstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoGemPayloadBytesUpstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoGemPayloadBytesUpstream=_ZxGponOltPmStatisHistoryInfoGemPayloadBytesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,4),_ZxGponOltPmStatisHistoryInfoGemPayloadBytesUpstream_Type())
zxGponOltPmStatisHistoryInfoGemPayloadBytesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoGemPayloadBytesUpstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoCorrectEthernetFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoCorrectEthernetFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoCorrectEthernetFramesUpstream=_ZxGponOltPmStatisHistoryInfoCorrectEthernetFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,5),_ZxGponOltPmStatisHistoryInfoCorrectEthernetFramesUpstream_Type())
zxGponOltPmStatisHistoryInfoCorrectEthernetFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoCorrectEthernetFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoErroredEthernetFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoErroredEthernetFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoErroredEthernetFramesUpstream=_ZxGponOltPmStatisHistoryInfoErroredEthernetFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,6),_ZxGponOltPmStatisHistoryInfoErroredEthernetFramesUpstream_Type())
zxGponOltPmStatisHistoryInfoErroredEthernetFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoErroredEthernetFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoTotalOmciFramesUpstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoTotalOmciFramesUpstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoTotalOmciFramesUpstream=_ZxGponOltPmStatisHistoryInfoTotalOmciFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,7),_ZxGponOltPmStatisHistoryInfoTotalOmciFramesUpstream_Type())
zxGponOltPmStatisHistoryInfoTotalOmciFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoTotalOmciFramesUpstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoERR_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoERR_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoERR=_ZxGponOltPmStatisHistoryInfoERR_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,8),_ZxGponOltPmStatisHistoryInfoERR_Type())
zxGponOltPmStatisHistoryInfoERR.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoERR.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoREI_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoREI_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoREI=_ZxGponOltPmStatisHistoryInfoREI_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,9),_ZxGponOltPmStatisHistoryInfoREI_Type())
zxGponOltPmStatisHistoryInfoREI.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoREI.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoValidEthernetPacketDownstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoValidEthernetPacketDownstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoValidEthernetPacketDownstream=_ZxGponOltPmStatisHistoryInfoValidEthernetPacketDownstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,10),_ZxGponOltPmStatisHistoryInfoValidEthernetPacketDownstream_Type())
zxGponOltPmStatisHistoryInfoValidEthernetPacketDownstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoValidEthernetPacketDownstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoCpuPacketDownstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoCpuPacketDownstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoCpuPacketDownstream=_ZxGponOltPmStatisHistoryInfoCpuPacketDownstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,11),_ZxGponOltPmStatisHistoryInfoCpuPacketDownstream_Type())
zxGponOltPmStatisHistoryInfoCpuPacketDownstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoCpuPacketDownstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoPloamDownstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoPloamDownstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoPloamDownstream=_ZxGponOltPmStatisHistoryInfoPloamDownstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,12),_ZxGponOltPmStatisHistoryInfoPloamDownstream_Type())
zxGponOltPmStatisHistoryInfoPloamDownstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoPloamDownstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoPloamUpstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoPloamUpstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoPloamUpstream=_ZxGponOltPmStatisHistoryInfoPloamUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,13),_ZxGponOltPmStatisHistoryInfoPloamUpstream_Type())
zxGponOltPmStatisHistoryInfoPloamUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoPloamUpstream.setStatus(_A)
_ZxGponOltPmStatisHistoryInfoInvalidPacketUpstream_Type=Unsigned32
_ZxGponOltPmStatisHistoryInfoInvalidPacketUpstream_Object=MibTableColumn
zxGponOltPmStatisHistoryInfoInvalidPacketUpstream=_ZxGponOltPmStatisHistoryInfoInvalidPacketUpstream_Object((1,3,6,1,4,1,3902,1012,3,12,14,1,14),_ZxGponOltPmStatisHistoryInfoInvalidPacketUpstream_Type())
zxGponOltPmStatisHistoryInfoInvalidPacketUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPmStatisHistoryInfoInvalidPacketUpstream.setStatus(_A)
_ZxGponPrivateOlt_ObjectIdentity=ObjectIdentity
zxGponPrivateOlt=_ZxGponPrivateOlt_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,13))
_ZxGponOltPonInfoTable_Object=MibTable
zxGponOltPonInfoTable=_ZxGponOltPonInfoTable_Object((1,3,6,1,4,1,3902,1012,3,13,1))
if mibBuilder.loadTexts:zxGponOltPonInfoTable.setStatus(_A)
_ZxGponOltPonInfoEntry_Object=MibTableRow
zxGponOltPonInfoEntry=_ZxGponOltPonInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,13,1,1))
zxGponOltPonInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltPonInfoEntry.setStatus(_A)
class _ZxGponOltPonName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_ZxGponOltPonName_Type.__name__=_O
_ZxGponOltPonName_Object=MibTableColumn
zxGponOltPonName=_ZxGponOltPonName_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,1),_ZxGponOltPonName_Type())
zxGponOltPonName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltPonName.setStatus(_A)
class _ZxGponOltPonDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(127,127));fixedLength=127
_ZxGponOltPonDescription_Type.__name__=_O
_ZxGponOltPonDescription_Object=MibTableColumn
zxGponOltPonDescription=_ZxGponOltPonDescription_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,2),_ZxGponOltPonDescription_Type())
zxGponOltPonDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltPonDescription.setStatus(_A)
class _ZxGPonOltPonOntDefaultState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deactive',1),(_A9,2)))
_ZxGPonOltPonOntDefaultState_Type.__name__=_E
_ZxGPonOltPonOntDefaultState_Object=MibTableColumn
zxGPonOltPonOntDefaultState=_ZxGPonOltPonOntDefaultState_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,3),_ZxGPonOltPonOntDefaultState_Type())
zxGPonOltPonOntDefaultState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGPonOltPonOntDefaultState.setStatus(_A)
class _ZxGPonOltPonOntDefaultPwMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonePw',1),('force',2)))
_ZxGPonOltPonOntDefaultPwMode_Type.__name__=_E
_ZxGPonOltPonOntDefaultPwMode_Object=MibTableColumn
zxGPonOltPonOntDefaultPwMode=_ZxGPonOltPonOntDefaultPwMode_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,4),_ZxGPonOltPonOntDefaultPwMode_Type())
zxGPonOltPonOntDefaultPwMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGPonOltPonOntDefaultPwMode.setStatus(_A)
class _ZxGPonOltPonOntDefaultPw_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_ZxGPonOltPonOntDefaultPw_Type.__name__=_O
_ZxGPonOltPonOntDefaultPw_Object=MibTableColumn
zxGPonOltPonOntDefaultPw=_ZxGPonOltPonOntDefaultPw_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,5),_ZxGPonOltPonOntDefaultPw_Type())
zxGPonOltPonOntDefaultPw.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGPonOltPonOntDefaultPw.setStatus(_A)
class _ZxGPonOltPonOntAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sn',1),('regid',2)))
_ZxGPonOltPonOntAuthMode_Type.__name__=_E
_ZxGPonOltPonOntAuthMode_Object=MibTableColumn
zxGPonOltPonOntAuthMode=_ZxGPonOltPonOntAuthMode_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,6),_ZxGPonOltPonOntAuthMode_Type())
zxGPonOltPonOntAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGPonOltPonOntAuthMode.setStatus(_A)
class _ZxGPonOltPonOntSnAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('learn',1),('provision',2)))
_ZxGPonOltPonOntSnAuthMode_Type.__name__=_E
_ZxGPonOltPonOntSnAuthMode_Object=MibTableColumn
zxGPonOltPonOntSnAuthMode=_ZxGPonOltPonOntSnAuthMode_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,7),_ZxGPonOltPonOntSnAuthMode_Type())
zxGPonOltPonOntSnAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGPonOltPonOntSnAuthMode.setStatus(_A)
class _ZxGPonOltPonOntSnMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxGPonOltPonOntSnMask_Type.__name__=_O
_ZxGPonOltPonOntSnMask_Object=MibTableColumn
zxGPonOltPonOntSnMask=_ZxGPonOltPonOntSnMask_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,8),_ZxGPonOltPonOntSnMask_Type())
zxGPonOltPonOntSnMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGPonOltPonOntSnMask.setStatus(_A)
_ZxGponOltPonOmccPortBase_Type=Integer32
_ZxGponOltPonOmccPortBase_Object=MibTableColumn
zxGponOltPonOmccPortBase=_ZxGponOltPonOmccPortBase_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,9),_ZxGponOltPonOmccPortBase_Type())
zxGponOltPonOmccPortBase.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltPonOmccPortBase.setStatus(_A)
class _ZxGPonOltPonAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGPonOltPonAdminState_Type.__name__=_E
_ZxGPonOltPonAdminState_Object=MibTableColumn
zxGPonOltPonAdminState=_ZxGPonOltPonAdminState_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,10),_ZxGPonOltPonAdminState_Type())
zxGPonOltPonAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGPonOltPonAdminState.setStatus(_A)
class _ZxGPonOltPonOperState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGPonOltPonOperState_Type.__name__=_E
_ZxGPonOltPonOperState_Object=MibTableColumn
zxGPonOltPonOperState=_ZxGPonOltPonOperState_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,11),_ZxGPonOltPonOperState_Type())
zxGPonOltPonOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGPonOltPonOperState.setStatus(_A)
_ZxGponOltPonSupportMaxOnts_Type=Integer32
_ZxGponOltPonSupportMaxOnts_Object=MibTableColumn
zxGponOltPonSupportMaxOnts=_ZxGponOltPonSupportMaxOnts_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,12),_ZxGponOltPonSupportMaxOnts_Type())
zxGponOltPonSupportMaxOnts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPonSupportMaxOnts.setStatus(_A)
_ZxGponOltPonRealLegalOnts_Type=Integer32
_ZxGponOltPonRealLegalOnts_Object=MibTableColumn
zxGponOltPonRealLegalOnts=_ZxGponOltPonRealLegalOnts_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,13),_ZxGponOltPonRealLegalOnts_Type())
zxGponOltPonRealLegalOnts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPonRealLegalOnts.setStatus(_A)
_ZxGponOltPonRealIllegalOnts_Type=Integer32
_ZxGponOltPonRealIllegalOnts_Object=MibTableColumn
zxGponOltPonRealIllegalOnts=_ZxGponOltPonRealIllegalOnts_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,14),_ZxGponOltPonRealIllegalOnts_Type())
zxGponOltPonRealIllegalOnts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPonRealIllegalOnts.setStatus(_A)
_ZxGponOltPonSupportMaxTConts_Type=Integer32
_ZxGponOltPonSupportMaxTConts_Object=MibTableColumn
zxGponOltPonSupportMaxTConts=_ZxGponOltPonSupportMaxTConts_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,15),_ZxGponOltPonSupportMaxTConts_Type())
zxGponOltPonSupportMaxTConts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPonSupportMaxTConts.setStatus(_A)
_ZxGponOltPonRealUsedTConts_Type=Integer32
_ZxGponOltPonRealUsedTConts_Object=MibTableColumn
zxGponOltPonRealUsedTConts=_ZxGponOltPonRealUsedTConts_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,16),_ZxGponOltPonRealUsedTConts_Type())
zxGponOltPonRealUsedTConts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPonRealUsedTConts.setStatus(_A)
class _ZxGponOltPonOntConfigureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configured',1),('noconfigured',2)))
_ZxGponOltPonOntConfigureStatus_Type.__name__=_E
_ZxGponOltPonOntConfigureStatus_Object=MibTableColumn
zxGponOltPonOntConfigureStatus=_ZxGponOltPonOntConfigureStatus_Object((1,3,6,1,4,1,3902,1012,3,13,1,1,17),_ZxGponOltPonOntConfigureStatus_Type())
zxGponOltPonOntConfigureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltPonOntConfigureStatus.setStatus(_A)
_ZxGponOltMgmtOperTable_Object=MibTable
zxGponOltMgmtOperTable=_ZxGponOltMgmtOperTable_Object((1,3,6,1,4,1,3902,1012,3,13,2))
if mibBuilder.loadTexts:zxGponOltMgmtOperTable.setStatus(_A)
_ZxGponOltMgmtOperEntry_Object=MibTableRow
zxGponOltMgmtOperEntry=_ZxGponOltMgmtOperEntry_Object((1,3,6,1,4,1,3902,1012,3,13,2,1))
zxGponOltMgmtOperEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltMgmtOperEntry.setStatus(_A)
_ZxGponOltReset_Type=TruthValue
_ZxGponOltReset_Object=MibTableColumn
zxGponOltReset=_ZxGponOltReset_Object((1,3,6,1,4,1,3902,1012,3,13,2,1,1),_ZxGponOltReset_Type())
zxGponOltReset.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltReset.setStatus(_A)
_ZxGponOltOff_Type=TruthValue
_ZxGponOltOff_Object=MibTableColumn
zxGponOltOff=_ZxGponOltOff_Object((1,3,6,1,4,1,3902,1012,3,13,2,1,2),_ZxGponOltOff_Type())
zxGponOltOff.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltOff.setStatus(_A)
_ZxGponOltOpticalDetectOnce_Type=TruthValue
_ZxGponOltOpticalDetectOnce_Object=MibTableColumn
zxGponOltOpticalDetectOnce=_ZxGponOltOpticalDetectOnce_Object((1,3,6,1,4,1,3902,1012,3,13,2,1,3),_ZxGponOltOpticalDetectOnce_Type())
zxGponOltOpticalDetectOnce.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltOpticalDetectOnce.setStatus(_A)
_ZxGponUnCfgSnOntInfoTable_Object=MibTable
zxGponUnCfgSnOntInfoTable=_ZxGponUnCfgSnOntInfoTable_Object((1,3,6,1,4,1,3902,1012,3,13,3))
if mibBuilder.loadTexts:zxGponUnCfgSnOntInfoTable.setStatus(_A)
_ZxGponUnCfgSnOntInfoEntry_Object=MibTableRow
zxGponUnCfgSnOntInfoEntry=_ZxGponUnCfgSnOntInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,13,3,1))
zxGponUnCfgSnOntInfoEntry.setIndexNames((0,_B,_F),(0,_B,_AA))
if mibBuilder.loadTexts:zxGponUnCfgSnOntInfoEntry.setStatus(_A)
_ZxGponUnCfgSnIdx_Type=Integer32
_ZxGponUnCfgSnIdx_Object=MibTableColumn
zxGponUnCfgSnIdx=_ZxGponUnCfgSnIdx_Object((1,3,6,1,4,1,3902,1012,3,13,3,1,1),_ZxGponUnCfgSnIdx_Type())
zxGponUnCfgSnIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponUnCfgSnIdx.setStatus(_A)
class _ZxGponUnCfgSnOntSN_Type(OntSerialNumber):subtypeSpec=OntSerialNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxGponUnCfgSnOntSN_Type.__name__=_f
_ZxGponUnCfgSnOntSN_Object=MibTableColumn
zxGponUnCfgSnOntSN=_ZxGponUnCfgSnOntSN_Object((1,3,6,1,4,1,3902,1012,3,13,3,1,2),_ZxGponUnCfgSnOntSN_Type())
zxGponUnCfgSnOntSN.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponUnCfgSnOntSN.setStatus(_A)
class _ZxGponUnCfgSnOntRID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ZxGponUnCfgSnOntRID_Type.__name__=_O
_ZxGponUnCfgSnOntRID_Object=MibTableColumn
zxGponUnCfgSnOntRID=_ZxGponUnCfgSnOntRID_Object((1,3,6,1,4,1,3902,1012,3,13,3,1,3),_ZxGponUnCfgSnOntRID_Type())
zxGponUnCfgSnOntRID.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponUnCfgSnOntRID.setStatus(_A)
_ZxGponUnCfgSnOntRtd_Type=Integer32
_ZxGponUnCfgSnOntRtd_Object=MibTableColumn
zxGponUnCfgSnOntRtd=_ZxGponUnCfgSnOntRtd_Object((1,3,6,1,4,1,3902,1012,3,13,3,1,4),_ZxGponUnCfgSnOntRtd_Type())
zxGponUnCfgSnOntRtd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponUnCfgSnOntRtd.setStatus(_A)
class _ZxGponUnCfgSnOntPsw_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_ZxGponUnCfgSnOntPsw_Type.__name__=_O
_ZxGponUnCfgSnOntPsw_Object=MibTableColumn
zxGponUnCfgSnOntPsw=_ZxGponUnCfgSnOntPsw_Object((1,3,6,1,4,1,3902,1012,3,13,3,1,5),_ZxGponUnCfgSnOntPsw_Type())
zxGponUnCfgSnOntPsw.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponUnCfgSnOntPsw.setStatus(_A)
class _ZxGponUnCfgSnOntState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_AB,1),(_AC,2),(_AD,3),(_AE,4),(_AF,5),(_AG,6),('o7-popup',7)))
_ZxGponUnCfgSnOntState_Type.__name__=_E
_ZxGponUnCfgSnOntState_Object=MibTableColumn
zxGponUnCfgSnOntState=_ZxGponUnCfgSnOntState_Object((1,3,6,1,4,1,3902,1012,3,13,3,1,6),_ZxGponUnCfgSnOntState_Type())
zxGponUnCfgSnOntState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponUnCfgSnOntState.setStatus(_A)
class _ZxGponUnCfgSnOntTime_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxGponUnCfgSnOntTime_Type.__name__=_A3
_ZxGponUnCfgSnOntTime_Object=MibTableColumn
zxGponUnCfgSnOntTime=_ZxGponUnCfgSnOntTime_Object((1,3,6,1,4,1,3902,1012,3,13,3,1,7),_ZxGponUnCfgSnOntTime_Type())
zxGponUnCfgSnOntTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponUnCfgSnOntTime.setStatus(_A)
_ZxGponOmccInfoTable_Object=MibTable
zxGponOmccInfoTable=_ZxGponOmccInfoTable_Object((1,3,6,1,4,1,3902,1012,3,13,4))
if mibBuilder.loadTexts:zxGponOmccInfoTable.setStatus(_A)
_ZxGponOmccInfoEntry_Object=MibTableRow
zxGponOmccInfoEntry=_ZxGponOmccInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,13,4,1))
zxGponOmccInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOmccInfoEntry.setStatus(_A)
_ZxGponOmccChannelNum_Type=Integer32
_ZxGponOmccChannelNum_Object=MibTableColumn
zxGponOmccChannelNum=_ZxGponOmccChannelNum_Object((1,3,6,1,4,1,3902,1012,3,13,4,1,1),_ZxGponOmccChannelNum_Type())
zxGponOmccChannelNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOmccChannelNum.setStatus(_A)
_ZxGponOmccChannelBandwidth_Type=Integer32
_ZxGponOmccChannelBandwidth_Object=MibTableColumn
zxGponOmccChannelBandwidth=_ZxGponOmccChannelBandwidth_Object((1,3,6,1,4,1,3902,1012,3,13,4,1,2),_ZxGponOmccChannelBandwidth_Type())
zxGponOmccChannelBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOmccChannelBandwidth.setStatus(_A)
class _ZxGponOmccChannelAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponOmccChannelAdminState_Type.__name__=_E
_ZxGponOmccChannelAdminState_Object=MibTableColumn
zxGponOmccChannelAdminState=_ZxGponOmccChannelAdminState_Object((1,3,6,1,4,1,3902,1012,3,13,4,1,3),_ZxGponOmccChannelAdminState_Type())
zxGponOmccChannelAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOmccChannelAdminState.setStatus(_A)
class _ZxGponOmccChannelOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponOmccChannelOpState_Type.__name__=_E
_ZxGponOmccChannelOpState_Object=MibTableColumn
zxGponOmccChannelOpState=_ZxGponOmccChannelOpState_Object((1,3,6,1,4,1,3902,1012,3,13,4,1,4),_ZxGponOmccChannelOpState_Type())
zxGponOmccChannelOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOmccChannelOpState.setStatus(_A)
_ZxGponOltBitErrTable_Object=MibTable
zxGponOltBitErrTable=_ZxGponOltBitErrTable_Object((1,3,6,1,4,1,3902,1012,3,13,5))
if mibBuilder.loadTexts:zxGponOltBitErrTable.setStatus(_A)
_ZxGponOltBitErrEntry_Object=MibTableRow
zxGponOltBitErrEntry=_ZxGponOltBitErrEntry_Object((1,3,6,1,4,1,3902,1012,3,13,5,1))
zxGponOltBitErrEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltBitErrEntry.setStatus(_A)
class _ZxGponOltUpBerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponOltUpBerEnable_Type.__name__=_E
_ZxGponOltUpBerEnable_Object=MibTableColumn
zxGponOltUpBerEnable=_ZxGponOltUpBerEnable_Object((1,3,6,1,4,1,3902,1012,3,13,5,1,1),_ZxGponOltUpBerEnable_Type())
zxGponOltUpBerEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltUpBerEnable.setStatus(_A)
_ZxGponOltUpBerCalcInterval_Type=Integer32
_ZxGponOltUpBerCalcInterval_Object=MibTableColumn
zxGponOltUpBerCalcInterval=_ZxGponOltUpBerCalcInterval_Object((1,3,6,1,4,1,3902,1012,3,13,5,1,2),_ZxGponOltUpBerCalcInterval_Type())
zxGponOltUpBerCalcInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltUpBerCalcInterval.setStatus(_A)
class _ZxGponOltDownBerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponOltDownBerEnable_Type.__name__=_E
_ZxGponOltDownBerEnable_Object=MibTableColumn
zxGponOltDownBerEnable=_ZxGponOltDownBerEnable_Object((1,3,6,1,4,1,3902,1012,3,13,5,1,3),_ZxGponOltDownBerEnable_Type())
zxGponOltDownBerEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltDownBerEnable.setStatus(_A)
_ZxGponOltDownBerCalcInterval_Type=Integer32
_ZxGponOltDownBerCalcInterval_Object=MibTableColumn
zxGponOltDownBerCalcInterval=_ZxGponOltDownBerCalcInterval_Object((1,3,6,1,4,1,3902,1012,3,13,5,1,4),_ZxGponOltDownBerCalcInterval_Type())
zxGponOltDownBerCalcInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltDownBerCalcInterval.setStatus(_A)
_ZxGponOltUpSfThreshold_Type=Integer32
_ZxGponOltUpSfThreshold_Object=MibTableColumn
zxGponOltUpSfThreshold=_ZxGponOltUpSfThreshold_Object((1,3,6,1,4,1,3902,1012,3,13,5,1,5),_ZxGponOltUpSfThreshold_Type())
zxGponOltUpSfThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltUpSfThreshold.setStatus(_A)
_ZxGponOltUpSdThreshold_Type=Integer32
_ZxGponOltUpSdThreshold_Object=MibTableColumn
zxGponOltUpSdThreshold=_ZxGponOltUpSdThreshold_Object((1,3,6,1,4,1,3902,1012,3,13,5,1,6),_ZxGponOltUpSdThreshold_Type())
zxGponOltUpSdThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltUpSdThreshold.setStatus(_A)
_ZxGponStaticMultiPortIdInfoTable_Object=MibTable
zxGponStaticMultiPortIdInfoTable=_ZxGponStaticMultiPortIdInfoTable_Object((1,3,6,1,4,1,3902,1012,3,13,10))
if mibBuilder.loadTexts:zxGponStaticMultiPortIdInfoTable.setStatus(_A)
_ZxGponStaticMultiPortIdInfoEntry_Object=MibTableRow
zxGponStaticMultiPortIdInfoEntry=_ZxGponStaticMultiPortIdInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,13,10,1))
zxGponStaticMultiPortIdInfoEntry.setIndexNames((0,_B,_AH))
if mibBuilder.loadTexts:zxGponStaticMultiPortIdInfoEntry.setStatus(_A)
_ZxGponStaticMultiPortIdInfoIdx_Type=Integer32
_ZxGponStaticMultiPortIdInfoIdx_Object=MibTableColumn
zxGponStaticMultiPortIdInfoIdx=_ZxGponStaticMultiPortIdInfoIdx_Object((1,3,6,1,4,1,3902,1012,3,13,10,1,1),_ZxGponStaticMultiPortIdInfoIdx_Type())
zxGponStaticMultiPortIdInfoIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponStaticMultiPortIdInfoIdx.setStatus(_A)
class _ZxGponStaticMultiPortIdList_Type(ZxPortIdList):subtypeSpec=ZxPortIdList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ZxGponStaticMultiPortIdList_Type.__name__=_b
_ZxGponStaticMultiPortIdList_Object=MibTableColumn
zxGponStaticMultiPortIdList=_ZxGponStaticMultiPortIdList_Object((1,3,6,1,4,1,3902,1012,3,13,10,1,2),_ZxGponStaticMultiPortIdList_Type())
zxGponStaticMultiPortIdList.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponStaticMultiPortIdList.setStatus(_A)
_ZxGponStaticMultiAddrIdx_Type=Integer32
_ZxGponStaticMultiAddrIdx_Object=MibTableColumn
zxGponStaticMultiAddrIdx=_ZxGponStaticMultiAddrIdx_Object((1,3,6,1,4,1,3902,1012,3,13,10,1,3),_ZxGponStaticMultiAddrIdx_Type())
zxGponStaticMultiAddrIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponStaticMultiAddrIdx.setStatus(_A)
_ZxGponStaticMultiPortIdStatus_Type=RowStatus
_ZxGponStaticMultiPortIdStatus_Object=MibTableColumn
zxGponStaticMultiPortIdStatus=_ZxGponStaticMultiPortIdStatus_Object((1,3,6,1,4,1,3902,1012,3,13,10,1,4),_ZxGponStaticMultiPortIdStatus_Type())
zxGponStaticMultiPortIdStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponStaticMultiPortIdStatus.setStatus(_A)
_ZxGponStaticMulticastAddressTable_Object=MibTable
zxGponStaticMulticastAddressTable=_ZxGponStaticMulticastAddressTable_Object((1,3,6,1,4,1,3902,1012,3,13,11))
if mibBuilder.loadTexts:zxGponStaticMulticastAddressTable.setStatus(_A)
_ZxGponStaticMulticastAddressEntry_Object=MibTableRow
zxGponStaticMulticastAddressEntry=_ZxGponStaticMulticastAddressEntry_Object((1,3,6,1,4,1,3902,1012,3,13,11,1))
zxGponStaticMulticastAddressEntry.setIndexNames((0,_B,_AI))
if mibBuilder.loadTexts:zxGponStaticMulticastAddressEntry.setStatus(_A)
_ZxGponStaticMulticastIdx_Type=Integer32
_ZxGponStaticMulticastIdx_Object=MibTableColumn
zxGponStaticMulticastIdx=_ZxGponStaticMulticastIdx_Object((1,3,6,1,4,1,3902,1012,3,13,11,1,1),_ZxGponStaticMulticastIdx_Type())
zxGponStaticMulticastIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponStaticMulticastIdx.setStatus(_A)
_ZxGponStaticMulticastAddress_Type=MacAddress
_ZxGponStaticMulticastAddress_Object=MibTableColumn
zxGponStaticMulticastAddress=_ZxGponStaticMulticastAddress_Object((1,3,6,1,4,1,3902,1012,3,13,11,1,2),_ZxGponStaticMulticastAddress_Type())
zxGponStaticMulticastAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponStaticMulticastAddress.setStatus(_A)
_ZxGponStaticMulticastVlanId_Type=VlanId
_ZxGponStaticMulticastVlanId_Object=MibTableColumn
zxGponStaticMulticastVlanId=_ZxGponStaticMulticastVlanId_Object((1,3,6,1,4,1,3902,1012,3,13,11,1,3),_ZxGponStaticMulticastVlanId_Type())
zxGponStaticMulticastVlanId.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponStaticMulticastVlanId.setStatus(_A)
class _ZxGponStaticMulticastPortIdIdx_Type(ZxIndexList):subtypeSpec=ZxIndexList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ZxGponStaticMulticastPortIdIdx_Type.__name__=_d
_ZxGponStaticMulticastPortIdIdx_Object=MibTableColumn
zxGponStaticMulticastPortIdIdx=_ZxGponStaticMulticastPortIdIdx_Object((1,3,6,1,4,1,3902,1012,3,13,11,1,4),_ZxGponStaticMulticastPortIdIdx_Type())
zxGponStaticMulticastPortIdIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponStaticMulticastPortIdIdx.setStatus(_A)
class _ZxGponStaticMulticastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_r,1),('invalid',2),('permanent',3),('deleteOnReset',4),('deleteOnTimeout',5)))
_ZxGponStaticMulticastStatus_Type.__name__=_E
_ZxGponStaticMulticastStatus_Object=MibTableColumn
zxGponStaticMulticastStatus=_ZxGponStaticMulticastStatus_Object((1,3,6,1,4,1,3902,1012,3,13,11,1,5),_ZxGponStaticMulticastStatus_Type())
zxGponStaticMulticastStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponStaticMulticastStatus.setStatus(_A)
_ZxGponMulticastAddressTable_Object=MibTable
zxGponMulticastAddressTable=_ZxGponMulticastAddressTable_Object((1,3,6,1,4,1,3902,1012,3,13,12))
if mibBuilder.loadTexts:zxGponMulticastAddressTable.setStatus(_A)
_ZxGponMulticastAddressEntry_Object=MibTableRow
zxGponMulticastAddressEntry=_ZxGponMulticastAddressEntry_Object((1,3,6,1,4,1,3902,1012,3,13,12,1))
zxGponMulticastAddressEntry.setIndexNames((0,_B,_AJ),(0,_B,_AK),(0,_B,_AL))
if mibBuilder.loadTexts:zxGponMulticastAddressEntry.setStatus(_A)
_ZxGponMulticastAddress_Type=MacAddress
_ZxGponMulticastAddress_Object=MibTableColumn
zxGponMulticastAddress=_ZxGponMulticastAddress_Object((1,3,6,1,4,1,3902,1012,3,13,12,1,1),_ZxGponMulticastAddress_Type())
zxGponMulticastAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponMulticastAddress.setStatus(_A)
_ZxGponMulticastVlanId_Type=VlanId
_ZxGponMulticastVlanId_Object=MibTableColumn
zxGponMulticastVlanId=_ZxGponMulticastVlanId_Object((1,3,6,1,4,1,3902,1012,3,13,12,1,2),_ZxGponMulticastVlanId_Type())
zxGponMulticastVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponMulticastVlanId.setStatus(_A)
_ZxGponMulticastIdx_Type=Integer32
_ZxGponMulticastIdx_Object=MibTableColumn
zxGponMulticastIdx=_ZxGponMulticastIdx_Object((1,3,6,1,4,1,3902,1012,3,13,12,1,3),_ZxGponMulticastIdx_Type())
zxGponMulticastIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponMulticastIdx.setStatus(_A)
class _ZxGponMulticastPortIdIdx_Type(ZxPortIdList):subtypeSpec=ZxPortIdList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ZxGponMulticastPortIdIdx_Type.__name__=_b
_ZxGponMulticastPortIdIdx_Object=MibTableColumn
zxGponMulticastPortIdIdx=_ZxGponMulticastPortIdIdx_Object((1,3,6,1,4,1,3902,1012,3,13,12,1,4),_ZxGponMulticastPortIdIdx_Type())
zxGponMulticastPortIdIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMulticastPortIdIdx.setStatus(_A)
class _ZxGponMulticastStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_r,1),('invalid',2),('learned',3),('self',4),('mgmt',5),('learnedAndMgmt',6)))
_ZxGponMulticastStatus_Type.__name__=_E
_ZxGponMulticastStatus_Object=MibTableColumn
zxGponMulticastStatus=_ZxGponMulticastStatus_Object((1,3,6,1,4,1,3902,1012,3,13,12,1,5),_ZxGponMulticastStatus_Type())
zxGponMulticastStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMulticastStatus.setStatus(_A)
_ZxGponDsBFPortIdInfoTable_Object=MibTable
zxGponDsBFPortIdInfoTable=_ZxGponDsBFPortIdInfoTable_Object((1,3,6,1,4,1,3902,1012,3,13,13))
if mibBuilder.loadTexts:zxGponDsBFPortIdInfoTable.setStatus(_A)
_ZxGponDsBFPortIdInfoEntry_Object=MibTableRow
zxGponDsBFPortIdInfoEntry=_ZxGponDsBFPortIdInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,13,13,1))
zxGponDsBFPortIdInfoEntry.setIndexNames((0,_B,_AM))
if mibBuilder.loadTexts:zxGponDsBFPortIdInfoEntry.setStatus(_A)
_ZxGponDsBFPortIdInfoIdx_Type=Integer32
_ZxGponDsBFPortIdInfoIdx_Object=MibTableColumn
zxGponDsBFPortIdInfoIdx=_ZxGponDsBFPortIdInfoIdx_Object((1,3,6,1,4,1,3902,1012,3,13,13,1,1),_ZxGponDsBFPortIdInfoIdx_Type())
zxGponDsBFPortIdInfoIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponDsBFPortIdInfoIdx.setStatus(_A)
class _ZxGponDsBFPortIdInfoList_Type(ZxPortIdList):subtypeSpec=ZxPortIdList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ZxGponDsBFPortIdInfoList_Type.__name__=_b
_ZxGponDsBFPortIdInfoList_Object=MibTableColumn
zxGponDsBFPortIdInfoList=_ZxGponDsBFPortIdInfoList_Object((1,3,6,1,4,1,3902,1012,3,13,13,1,2),_ZxGponDsBFPortIdInfoList_Type())
zxGponDsBFPortIdInfoList.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDsBFPortIdInfoList.setStatus(_A)
_ZxGponDsBFPortIdInfoVlanIdx_Type=Integer32
_ZxGponDsBFPortIdInfoVlanIdx_Object=MibTableColumn
zxGponDsBFPortIdInfoVlanIdx=_ZxGponDsBFPortIdInfoVlanIdx_Object((1,3,6,1,4,1,3902,1012,3,13,13,1,3),_ZxGponDsBFPortIdInfoVlanIdx_Type())
zxGponDsBFPortIdInfoVlanIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDsBFPortIdInfoVlanIdx.setStatus(_A)
_ZxGponDsBFPortIdInfoStatus_Type=RowStatus
_ZxGponDsBFPortIdInfoStatus_Object=MibTableColumn
zxGponDsBFPortIdInfoStatus=_ZxGponDsBFPortIdInfoStatus_Object((1,3,6,1,4,1,3902,1012,3,13,13,1,4),_ZxGponDsBFPortIdInfoStatus_Type())
zxGponDsBFPortIdInfoStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponDsBFPortIdInfoStatus.setStatus(_A)
_ZxGponDownBroadcastFloodTable_Object=MibTable
zxGponDownBroadcastFloodTable=_ZxGponDownBroadcastFloodTable_Object((1,3,6,1,4,1,3902,1012,3,13,14))
if mibBuilder.loadTexts:zxGponDownBroadcastFloodTable.setStatus(_A)
_ZxGponDownBroadcastFloodEntry_Object=MibTableRow
zxGponDownBroadcastFloodEntry=_ZxGponDownBroadcastFloodEntry_Object((1,3,6,1,4,1,3902,1012,3,13,14,1))
zxGponDownBroadcastFloodEntry.setIndexNames((0,_B,_AN))
if mibBuilder.loadTexts:zxGponDownBroadcastFloodEntry.setStatus(_A)
_ZxGponDownBroadcastFloodVlanId_Type=VlanId
_ZxGponDownBroadcastFloodVlanId_Object=MibTableColumn
zxGponDownBroadcastFloodVlanId=_ZxGponDownBroadcastFloodVlanId_Object((1,3,6,1,4,1,3902,1012,3,13,14,1,1),_ZxGponDownBroadcastFloodVlanId_Type())
zxGponDownBroadcastFloodVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponDownBroadcastFloodVlanId.setStatus(_A)
class _ZxGponDownBroadcastFloodPortList_Type(ZxIndexList):subtypeSpec=ZxIndexList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ZxGponDownBroadcastFloodPortList_Type.__name__=_d
_ZxGponDownBroadcastFloodPortList_Object=MibTableColumn
zxGponDownBroadcastFloodPortList=_ZxGponDownBroadcastFloodPortList_Object((1,3,6,1,4,1,3902,1012,3,13,14,1,2),_ZxGponDownBroadcastFloodPortList_Type())
zxGponDownBroadcastFloodPortList.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponDownBroadcastFloodPortList.setStatus(_A)
_ZxGponDownBroadcastFloodEntryStatus_Type=RowStatus
_ZxGponDownBroadcastFloodEntryStatus_Object=MibTableColumn
zxGponDownBroadcastFloodEntryStatus=_ZxGponDownBroadcastFloodEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,13,14,1,3),_ZxGponDownBroadcastFloodEntryStatus_Type())
zxGponDownBroadcastFloodEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponDownBroadcastFloodEntryStatus.setStatus(_A)
_ZxGpon8021xOnOffTable_Object=MibTable
zxGpon8021xOnOffTable=_ZxGpon8021xOnOffTable_Object((1,3,6,1,4,1,3902,1012,3,13,15))
if mibBuilder.loadTexts:zxGpon8021xOnOffTable.setStatus(_A)
_ZxGpon8021xOnOffEntry_Object=MibTableRow
zxGpon8021xOnOffEntry=_ZxGpon8021xOnOffEntry_Object((1,3,6,1,4,1,3902,1012,3,13,15,1))
zxGpon8021xOnOffEntry.setIndexNames((0,_B,_AO))
if mibBuilder.loadTexts:zxGpon8021xOnOffEntry.setStatus(_A)
_ZxGpon8021xOnOffIdx_Type=Integer32
_ZxGpon8021xOnOffIdx_Object=MibTableColumn
zxGpon8021xOnOffIdx=_ZxGpon8021xOnOffIdx_Object((1,3,6,1,4,1,3902,1012,3,13,15,1,1),_ZxGpon8021xOnOffIdx_Type())
zxGpon8021xOnOffIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGpon8021xOnOffIdx.setStatus(_A)
class _ZxGpon8021xOnOffPortId_Type(ZxPortIdList):subtypeSpec=ZxPortIdList.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ZxGpon8021xOnOffPortId_Type.__name__=_b
_ZxGpon8021xOnOffPortId_Object=MibTableColumn
zxGpon8021xOnOffPortId=_ZxGpon8021xOnOffPortId_Object((1,3,6,1,4,1,3902,1012,3,13,15,1,2),_ZxGpon8021xOnOffPortId_Type())
zxGpon8021xOnOffPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021xOnOffPortId.setStatus(_A)
class _ZxGpon8021xOnOffEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_ZxGpon8021xOnOffEnable_Type.__name__=_E
_ZxGpon8021xOnOffEnable_Object=MibTableColumn
zxGpon8021xOnOffEnable=_ZxGpon8021xOnOffEnable_Object((1,3,6,1,4,1,3902,1012,3,13,15,1,3),_ZxGpon8021xOnOffEnable_Type())
zxGpon8021xOnOffEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021xOnOffEnable.setStatus(_A)
_ZxGponOltLoopbackTestInfoTable_Object=MibTable
zxGponOltLoopbackTestInfoTable=_ZxGponOltLoopbackTestInfoTable_Object((1,3,6,1,4,1,3902,1012,3,13,16))
if mibBuilder.loadTexts:zxGponOltLoopbackTestInfoTable.setStatus(_A)
_ZxGponOltLoopbackTestInfoEntry_Object=MibTableRow
zxGponOltLoopbackTestInfoEntry=_ZxGponOltLoopbackTestInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,13,16,1))
zxGponOltLoopbackTestInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltLoopbackTestInfoEntry.setStatus(_A)
_ZxGponOltLoopbackTestStart_Type=Integer32
_ZxGponOltLoopbackTestStart_Object=MibTableColumn
zxGponOltLoopbackTestStart=_ZxGponOltLoopbackTestStart_Object((1,3,6,1,4,1,3902,1012,3,13,16,1,1),_ZxGponOltLoopbackTestStart_Type())
zxGponOltLoopbackTestStart.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltLoopbackTestStart.setStatus(_A)
_ZxGponOltEthSwitchTable_Object=MibTable
zxGponOltEthSwitchTable=_ZxGponOltEthSwitchTable_Object((1,3,6,1,4,1,3902,1012,3,13,17))
if mibBuilder.loadTexts:zxGponOltEthSwitchTable.setStatus(_A)
_ZxGponOltEthSwitchEntry_Object=MibTableRow
zxGponOltEthSwitchEntry=_ZxGponOltEthSwitchEntry_Object((1,3,6,1,4,1,3902,1012,3,13,17,1))
zxGponOltEthSwitchEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltEthSwitchEntry.setStatus(_A)
class _ZxGponEthSwitchProtectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_ZxGponEthSwitchProtectState_Type.__name__=_E
_ZxGponEthSwitchProtectState_Object=MibTableColumn
zxGponEthSwitchProtectState=_ZxGponEthSwitchProtectState_Object((1,3,6,1,4,1,3902,1012,3,13,17,1,1),_ZxGponEthSwitchProtectState_Type())
zxGponEthSwitchProtectState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponEthSwitchProtectState.setStatus(_A)
_ZxGponOltScbPortTable_Object=MibTable
zxGponOltScbPortTable=_ZxGponOltScbPortTable_Object((1,3,6,1,4,1,3902,1012,3,13,18))
if mibBuilder.loadTexts:zxGponOltScbPortTable.setStatus(_A)
_ZxGponOltScbPortEntry_Object=MibTableRow
zxGponOltScbPortEntry=_ZxGponOltScbPortEntry_Object((1,3,6,1,4,1,3902,1012,3,13,18,1))
zxGponOltScbPortEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:zxGponOltScbPortEntry.setStatus(_A)
class _ZxGponOltScbPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(65,4095))
_ZxGponOltScbPort_Type.__name__=_E
_ZxGponOltScbPort_Object=MibTableColumn
zxGponOltScbPort=_ZxGponOltScbPort_Object((1,3,6,1,4,1,3902,1012,3,13,18,1,1),_ZxGponOltScbPort_Type())
zxGponOltScbPort.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOltScbPort.setStatus(_A)
_ZxGponEthTypeVlanMapTable_Object=MibTable
zxGponEthTypeVlanMapTable=_ZxGponEthTypeVlanMapTable_Object((1,3,6,1,4,1,3902,1012,3,13,19))
if mibBuilder.loadTexts:zxGponEthTypeVlanMapTable.setStatus(_A)
_ZxGponEthTypeVlanMapEntry_Object=MibTableRow
zxGponEthTypeVlanMapEntry=_ZxGponEthTypeVlanMapEntry_Object((1,3,6,1,4,1,3902,1012,3,13,19,1))
zxGponEthTypeVlanMapEntry.setIndexNames((0,_B,_F),(0,_B,_AP))
if mibBuilder.loadTexts:zxGponEthTypeVlanMapEntry.setStatus(_A)
_ZxGponEthTypeVlanMapEthType_Type=Integer32
_ZxGponEthTypeVlanMapEthType_Object=MibTableColumn
zxGponEthTypeVlanMapEthType=_ZxGponEthTypeVlanMapEthType_Object((1,3,6,1,4,1,3902,1012,3,13,19,1,1),_ZxGponEthTypeVlanMapEthType_Type())
zxGponEthTypeVlanMapEthType.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponEthTypeVlanMapEthType.setStatus(_A)
_ZxGponEthTypeVlanMapVlanId_Type=VlanId
_ZxGponEthTypeVlanMapVlanId_Object=MibTableColumn
zxGponEthTypeVlanMapVlanId=_ZxGponEthTypeVlanMapVlanId_Object((1,3,6,1,4,1,3902,1012,3,13,19,1,2),_ZxGponEthTypeVlanMapVlanId_Type())
zxGponEthTypeVlanMapVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponEthTypeVlanMapVlanId.setStatus(_A)
_ZxGponEthTypeVlanMapEntryStatus_Type=RowStatus
_ZxGponEthTypeVlanMapEntryStatus_Object=MibTableColumn
zxGponEthTypeVlanMapEntryStatus=_ZxGponEthTypeVlanMapEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,13,19,1,50),_ZxGponEthTypeVlanMapEntryStatus_Type())
zxGponEthTypeVlanMapEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponEthTypeVlanMapEntryStatus.setStatus(_A)
_ZxGponOltEthVlanSwitchTable_Object=MibTable
zxGponOltEthVlanSwitchTable=_ZxGponOltEthVlanSwitchTable_Object((1,3,6,1,4,1,3902,1012,3,13,20))
if mibBuilder.loadTexts:zxGponOltEthVlanSwitchTable.setStatus(_A)
_ZxGponOltEthVlanSwitchEntry_Object=MibTableRow
zxGponOltEthVlanSwitchEntry=_ZxGponOltEthVlanSwitchEntry_Object((1,3,6,1,4,1,3902,1012,3,13,20,1))
zxGponOltEthVlanSwitchEntry.setIndexNames((0,_B,_F),(0,_B,_AQ))
if mibBuilder.loadTexts:zxGponOltEthVlanSwitchEntry.setStatus(_A)
_ZxGponEthSwitchVlanId_Type=VlanId
_ZxGponEthSwitchVlanId_Object=MibTableColumn
zxGponEthSwitchVlanId=_ZxGponEthSwitchVlanId_Object((1,3,6,1,4,1,3902,1012,3,13,20,1,1),_ZxGponEthSwitchVlanId_Type())
zxGponEthSwitchVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponEthSwitchVlanId.setStatus(_A)
_ZxGponEthVlanSwitchRowStatus_Type=RowStatus
_ZxGponEthVlanSwitchRowStatus_Object=MibTableColumn
zxGponEthVlanSwitchRowStatus=_ZxGponEthVlanSwitchRowStatus_Object((1,3,6,1,4,1,3902,1012,3,13,20,1,2),_ZxGponEthVlanSwitchRowStatus_Type())
zxGponEthVlanSwitchRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponEthVlanSwitchRowStatus.setStatus(_A)
_ZxGponOntEquipMgmt_ObjectIdentity=ObjectIdentity
zxGponOntEquipMgmt=_ZxGponOntEquipMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,21))
_ZxGponOntStatusInfoTable_Object=MibTable
zxGponOntStatusInfoTable=_ZxGponOntStatusInfoTable_Object((1,3,6,1,4,1,3902,1012,3,21,1))
if mibBuilder.loadTexts:zxGponOntStatusInfoTable.setStatus(_A)
_ZxGponOntStatusInfoEntry_Object=MibTableRow
zxGponOntStatusInfoEntry=_ZxGponOntStatusInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,21,1,1))
zxGponOntStatusInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_AR))
if mibBuilder.loadTexts:zxGponOntStatusInfoEntry.setStatus(_A)
_ZxGponOntIndex_Type=Integer32
_ZxGponOntIndex_Object=MibTableColumn
zxGponOntIndex=_ZxGponOntIndex_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,1),_ZxGponOntIndex_Type())
zxGponOntIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponOntIndex.setStatus(_A)
_ZxGponOntMeId_Type=Integer32
_ZxGponOntMeId_Object=MibTableColumn
zxGponOntMeId=_ZxGponOntMeId_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,2),_ZxGponOntMeId_Type())
zxGponOntMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntMeId.setStatus(_A)
class _ZxGponOntVendorId_Type(OntVendorId):subtypeSpec=OntVendorId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ZxGponOntVendorId_Type.__name__=_AS
_ZxGponOntVendorId_Object=MibTableColumn
zxGponOntVendorId=_ZxGponOntVendorId_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,3),_ZxGponOntVendorId_Type())
zxGponOntVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntVendorId.setStatus(_A)
class _ZxGponOntVersionId_Type(OntVersionId):subtypeSpec=OntVersionId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,14));fixedLength=14
_ZxGponOntVersionId_Type.__name__=_AT
_ZxGponOntVersionId_Object=MibTableColumn
zxGponOntVersionId=_ZxGponOntVersionId_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,4),_ZxGponOntVersionId_Type())
zxGponOntVersionId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntVersionId.setStatus(_A)
class _ZxGponOntSnId_Type(OntSerialNumber):subtypeSpec=OntSerialNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxGponOntSnId_Type.__name__=_f
_ZxGponOntSnId_Object=MibTableColumn
zxGponOntSnId=_ZxGponOntSnId_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,5),_ZxGponOntSnId_Type())
zxGponOntSnId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntSnId.setStatus(_A)
class _ZxGponOntTrafficMgmtOpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('usSchedulerPriMech',1),('usMaxTraffic',2)))
_ZxGponOntTrafficMgmtOpt_Type.__name__=_E
_ZxGponOntTrafficMgmtOpt_Object=MibTableColumn
zxGponOntTrafficMgmtOpt=_ZxGponOntTrafficMgmtOpt_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,6),_ZxGponOntTrafficMgmtOpt_Type())
zxGponOntTrafficMgmtOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntTrafficMgmtOpt.setStatus(_A)
class _ZxGponOntVpVcConnFunOpt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('vp',2),('vpvc',3)))
_ZxGponOntVpVcConnFunOpt_Type.__name__=_E
_ZxGponOntVpVcConnFunOpt_Object=MibTableColumn
zxGponOntVpVcConnFunOpt=_ZxGponOntVpVcConnFunOpt_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,7),_ZxGponOntVpVcConnFunOpt_Type())
zxGponOntVpVcConnFunOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntVpVcConnFunOpt.setStatus(_A)
_ZxGponOntBatteryBackup_Type=TruthValue
_ZxGponOntBatteryBackup_Object=MibTableColumn
zxGponOntBatteryBackup=_ZxGponOntBatteryBackup_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,8),_ZxGponOntBatteryBackup_Type())
zxGponOntBatteryBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntBatteryBackup.setStatus(_A)
class _ZxGponOntAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponOntAdminStatus_Type.__name__=_E
_ZxGponOntAdminStatus_Object=MibTableColumn
zxGponOntAdminStatus=_ZxGponOntAdminStatus_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,9),_ZxGponOntAdminStatus_Type())
zxGponOntAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntAdminStatus.setStatus(_A)
class _ZxGponOntOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponOntOperStatus_Type.__name__=_E
_ZxGponOntOperStatus_Object=MibTableColumn
zxGponOntOperStatus=_ZxGponOntOperStatus_Object((1,3,6,1,4,1,3902,1012,3,21,1,1,10),_ZxGponOntOperStatus_Type())
zxGponOntOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntOperStatus.setStatus(_A)
_ZxGponOntAlarmTable_Object=MibTable
zxGponOntAlarmTable=_ZxGponOntAlarmTable_Object((1,3,6,1,4,1,3902,1012,3,21,2))
if mibBuilder.loadTexts:zxGponOntAlarmTable.setStatus(_A)
_ZxGponOntAlarmEntry_Object=MibTableRow
zxGponOntAlarmEntry=_ZxGponOntAlarmEntry_Object((1,3,6,1,4,1,3902,1012,3,21,2,1))
zxGponOntAlarmEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntAlarmEntry.setStatus(_A)
_ZxGponOntEquipmentAlarm_Type=TruthValue
_ZxGponOntEquipmentAlarm_Object=MibTableColumn
zxGponOntEquipmentAlarm=_ZxGponOntEquipmentAlarm_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,1),_ZxGponOntEquipmentAlarm_Type())
zxGponOntEquipmentAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntEquipmentAlarm.setStatus(_A)
class _ZxGponOntEquipmentAlarmMask_Type(TruthValue):defaultValue=2
_ZxGponOntEquipmentAlarmMask_Type.__name__=_W
_ZxGponOntEquipmentAlarmMask_Object=MibTableColumn
zxGponOntEquipmentAlarmMask=_ZxGponOntEquipmentAlarmMask_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,2),_ZxGponOntEquipmentAlarmMask_Type())
zxGponOntEquipmentAlarmMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntEquipmentAlarmMask.setStatus(_A)
_ZxGponOntPoweringAlarm_Type=TruthValue
_ZxGponOntPoweringAlarm_Object=MibTableColumn
zxGponOntPoweringAlarm=_ZxGponOntPoweringAlarm_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,3),_ZxGponOntPoweringAlarm_Type())
zxGponOntPoweringAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPoweringAlarm.setStatus(_A)
class _ZxGponOntPoweringAlarmMask_Type(TruthValue):defaultValue=2
_ZxGponOntPoweringAlarmMask_Type.__name__=_W
_ZxGponOntPoweringAlarmMask_Object=MibTableColumn
zxGponOntPoweringAlarmMask=_ZxGponOntPoweringAlarmMask_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,4),_ZxGponOntPoweringAlarmMask_Type())
zxGponOntPoweringAlarmMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntPoweringAlarmMask.setStatus(_A)
_ZxGponOntBatteryMissing_Type=TruthValue
_ZxGponOntBatteryMissing_Object=MibTableColumn
zxGponOntBatteryMissing=_ZxGponOntBatteryMissing_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,5),_ZxGponOntBatteryMissing_Type())
zxGponOntBatteryMissing.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntBatteryMissing.setStatus(_A)
class _ZxGponOntBatteryMissingMask_Type(TruthValue):defaultValue=2
_ZxGponOntBatteryMissingMask_Type.__name__=_W
_ZxGponOntBatteryMissingMask_Object=MibTableColumn
zxGponOntBatteryMissingMask=_ZxGponOntBatteryMissingMask_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,6),_ZxGponOntBatteryMissingMask_Type())
zxGponOntBatteryMissingMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntBatteryMissingMask.setStatus(_A)
_ZxGponOntBatteryFailure_Type=TruthValue
_ZxGponOntBatteryFailure_Object=MibTableColumn
zxGponOntBatteryFailure=_ZxGponOntBatteryFailure_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,7),_ZxGponOntBatteryFailure_Type())
zxGponOntBatteryFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntBatteryFailure.setStatus(_A)
class _ZxGponOntBatteryFailureMask_Type(TruthValue):defaultValue=2
_ZxGponOntBatteryFailureMask_Type.__name__=_W
_ZxGponOntBatteryFailureMask_Object=MibTableColumn
zxGponOntBatteryFailureMask=_ZxGponOntBatteryFailureMask_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,8),_ZxGponOntBatteryFailureMask_Type())
zxGponOntBatteryFailureMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntBatteryFailureMask.setStatus(_A)
_ZxGponOntBatteryLow_Type=TruthValue
_ZxGponOntBatteryLow_Object=MibTableColumn
zxGponOntBatteryLow=_ZxGponOntBatteryLow_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,9),_ZxGponOntBatteryLow_Type())
zxGponOntBatteryLow.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntBatteryLow.setStatus(_A)
class _ZxGponOntBatteryLowMask_Type(TruthValue):defaultValue=2
_ZxGponOntBatteryLowMask_Type.__name__=_W
_ZxGponOntBatteryLowMask_Object=MibTableColumn
zxGponOntBatteryLowMask=_ZxGponOntBatteryLowMask_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,10),_ZxGponOntBatteryLowMask_Type())
zxGponOntBatteryLowMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntBatteryLowMask.setStatus(_A)
_ZxGponOntPhysicalIntrusionAlarm_Type=TruthValue
_ZxGponOntPhysicalIntrusionAlarm_Object=MibTableColumn
zxGponOntPhysicalIntrusionAlarm=_ZxGponOntPhysicalIntrusionAlarm_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,11),_ZxGponOntPhysicalIntrusionAlarm_Type())
zxGponOntPhysicalIntrusionAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPhysicalIntrusionAlarm.setStatus(_A)
class _ZxGponOntPhysicalIntrusionAlarmMask_Type(TruthValue):defaultValue=2
_ZxGponOntPhysicalIntrusionAlarmMask_Type.__name__=_W
_ZxGponOntPhysicalIntrusionAlarmMask_Object=MibTableColumn
zxGponOntPhysicalIntrusionAlarmMask=_ZxGponOntPhysicalIntrusionAlarmMask_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,12),_ZxGponOntPhysicalIntrusionAlarmMask_Type())
zxGponOntPhysicalIntrusionAlarmMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntPhysicalIntrusionAlarmMask.setStatus(_A)
_ZxGponOntONTSelfTestFailure_Type=TruthValue
_ZxGponOntONTSelfTestFailure_Object=MibTableColumn
zxGponOntONTSelfTestFailure=_ZxGponOntONTSelfTestFailure_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,13),_ZxGponOntONTSelfTestFailure_Type())
zxGponOntONTSelfTestFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntONTSelfTestFailure.setStatus(_A)
class _ZxGponOntONTSelfTestFailureMask_Type(TruthValue):defaultValue=2
_ZxGponOntONTSelfTestFailureMask_Type.__name__=_W
_ZxGponOntONTSelfTestFailureMask_Object=MibTableColumn
zxGponOntONTSelfTestFailureMask=_ZxGponOntONTSelfTestFailureMask_Object((1,3,6,1,4,1,3902,1012,3,21,2,1,14),_ZxGponOntONTSelfTestFailureMask_Type())
zxGponOntONTSelfTestFailureMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntONTSelfTestFailureMask.setStatus(_A)
_ZxGponOntActionsTable_Object=MibTable
zxGponOntActionsTable=_ZxGponOntActionsTable_Object((1,3,6,1,4,1,3902,1012,3,21,3))
if mibBuilder.loadTexts:zxGponOntActionsTable.setStatus(_A)
_ZxGponOntActionsEntry_Object=MibTableRow
zxGponOntActionsEntry=_ZxGponOntActionsEntry_Object((1,3,6,1,4,1,3902,1012,3,21,3,1))
zxGponOntActionsEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntActionsEntry.setStatus(_A)
class _ZxGponOntReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reboot',1))
_ZxGponOntReboot_Type.__name__=_E
_ZxGponOntReboot_Object=MibTableColumn
zxGponOntReboot=_ZxGponOntReboot_Object((1,3,6,1,4,1,3902,1012,3,21,3,1,1),_ZxGponOntReboot_Type())
zxGponOntReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntReboot.setStatus(_A)
class _ZxGponOntTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('test',1))
_ZxGponOntTest_Type.__name__=_E
_ZxGponOntTest_Object=MibTableColumn
zxGponOntTest=_ZxGponOntTest_Object((1,3,6,1,4,1,3902,1012,3,21,3,1,2),_ZxGponOntTest_Type())
zxGponOntTest.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntTest.setStatus(_A)
class _ZxGponOntSyncTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('synctime',1))
_ZxGponOntSyncTime_Type.__name__=_E
_ZxGponOntSyncTime_Object=MibTableColumn
zxGponOntSyncTime=_ZxGponOntSyncTime_Object((1,3,6,1,4,1,3902,1012,3,21,3,1,3),_ZxGponOntSyncTime_Type())
zxGponOntSyncTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntSyncTime.setStatus(_A)
class _ZxGponOntMibReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('mibRest',1))
_ZxGponOntMibReset_Type.__name__=_E
_ZxGponOntMibReset_Object=MibTableColumn
zxGponOntMibReset=_ZxGponOntMibReset_Object((1,3,6,1,4,1,3902,1012,3,21,3,1,4),_ZxGponOntMibReset_Type())
zxGponOntMibReset.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntMibReset.setStatus(_A)
_ZxGponOntTestResult_Type=Integer32
_ZxGponOntTestResult_Object=MibTableColumn
zxGponOntTestResult=_ZxGponOntTestResult_Object((1,3,6,1,4,1,3902,1012,3,21,3,1,5),_ZxGponOntTestResult_Type())
zxGponOntTestResult.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntTestResult.setStatus(_A)
_ZxGponOnt2StatusInfoTable_Object=MibTable
zxGponOnt2StatusInfoTable=_ZxGponOnt2StatusInfoTable_Object((1,3,6,1,4,1,3902,1012,3,21,4))
if mibBuilder.loadTexts:zxGponOnt2StatusInfoTable.setStatus(_A)
_ZxGponOnt2StatusInfoEntry_Object=MibTableRow
zxGponOnt2StatusInfoEntry=_ZxGponOnt2StatusInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,21,4,1))
zxGponOnt2StatusInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_AU))
if mibBuilder.loadTexts:zxGponOnt2StatusInfoEntry.setStatus(_A)
_ZxGponOnt2Index_Type=Integer32
_ZxGponOnt2Index_Object=MibTableColumn
zxGponOnt2Index=_ZxGponOnt2Index_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,1),_ZxGponOnt2Index_Type())
zxGponOnt2Index.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponOnt2Index.setStatus(_A)
_ZxGponOnt2MeId_Type=Integer32
_ZxGponOnt2MeId_Object=MibTableColumn
zxGponOnt2MeId=_ZxGponOnt2MeId_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,2),_ZxGponOnt2MeId_Type())
zxGponOnt2MeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnt2MeId.setStatus(_A)
class _ZxGponOnt2EquipmentId_Type(OntEquipmentId):subtypeSpec=OntEquipmentId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_ZxGponOnt2EquipmentId_Type.__name__=_AV
_ZxGponOnt2EquipmentId_Object=MibTableColumn
zxGponOnt2EquipmentId=_ZxGponOnt2EquipmentId_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,3),_ZxGponOnt2EquipmentId_Type())
zxGponOnt2EquipmentId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnt2EquipmentId.setStatus(_A)
_ZxGponOnt2OMCCVersion_Type=Integer32
_ZxGponOnt2OMCCVersion_Object=MibTableColumn
zxGponOnt2OMCCVersion=_ZxGponOnt2OMCCVersion_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,4),_ZxGponOnt2OMCCVersion_Type())
zxGponOnt2OMCCVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnt2OMCCVersion.setStatus(_A)
_ZxGponOnt2VendorProdCode_Type=Integer32
_ZxGponOnt2VendorProdCode_Object=MibTableColumn
zxGponOnt2VendorProdCode=_ZxGponOnt2VendorProdCode_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,5),_ZxGponOnt2VendorProdCode_Type())
zxGponOnt2VendorProdCode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnt2VendorProdCode.setStatus(_A)
class _ZxGponOnt2SecurityCapab_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxGponOnt2SecurityCapab_Type.__name__=_E
_ZxGponOnt2SecurityCapab_Object=MibTableColumn
zxGponOnt2SecurityCapab=_ZxGponOnt2SecurityCapab_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,6),_ZxGponOnt2SecurityCapab_Type())
zxGponOnt2SecurityCapab.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnt2SecurityCapab.setStatus(_A)
class _ZxGponOnt2SecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxGponOnt2SecurityMode_Type.__name__=_E
_ZxGponOnt2SecurityMode_Object=MibTableColumn
zxGponOnt2SecurityMode=_ZxGponOnt2SecurityMode_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,7),_ZxGponOnt2SecurityMode_Type())
zxGponOnt2SecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnt2SecurityMode.setStatus(_A)
class _ZxGponOnt2TotalPriQueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_ZxGponOnt2TotalPriQueNum_Type.__name__=_E
_ZxGponOnt2TotalPriQueNum_Object=MibTableColumn
zxGponOnt2TotalPriQueNum=_ZxGponOnt2TotalPriQueNum_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,8),_ZxGponOnt2TotalPriQueNum_Type())
zxGponOnt2TotalPriQueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnt2TotalPriQueNum.setStatus(_A)
class _ZxGponOnt2TotalTrafSchedNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxGponOnt2TotalTrafSchedNum_Type.__name__=_E
_ZxGponOnt2TotalTrafSchedNum_Object=MibTableColumn
zxGponOnt2TotalTrafSchedNum=_ZxGponOnt2TotalTrafSchedNum_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,9),_ZxGponOnt2TotalTrafSchedNum_Type())
zxGponOnt2TotalTrafSchedNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnt2TotalTrafSchedNum.setStatus(_A)
class _ZxGponOnt2Mode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),('gem',2),('dual',3)))
_ZxGponOnt2Mode_Type.__name__=_E
_ZxGponOnt2Mode_Object=MibTableColumn
zxGponOnt2Mode=_ZxGponOnt2Mode_Object((1,3,6,1,4,1,3902,1012,3,21,4,1,10),_ZxGponOnt2Mode_Type())
zxGponOnt2Mode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnt2Mode.setStatus(_A)
_ZxGponThresholdDataTable_Object=MibTable
zxGponThresholdDataTable=_ZxGponThresholdDataTable_Object((1,3,6,1,4,1,3902,1012,3,21,11))
if mibBuilder.loadTexts:zxGponThresholdDataTable.setStatus(_A)
_ZxGponThresholdDataEntry_Object=MibTableRow
zxGponThresholdDataEntry=_ZxGponThresholdDataEntry_Object((1,3,6,1,4,1,3902,1012,3,21,11,1))
zxGponThresholdDataEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_AW))
if mibBuilder.loadTexts:zxGponThresholdDataEntry.setStatus(_A)
_ZxGponThresholdDataIndex_Type=Integer32
_ZxGponThresholdDataIndex_Object=MibTableColumn
zxGponThresholdDataIndex=_ZxGponThresholdDataIndex_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,1),_ZxGponThresholdDataIndex_Type())
zxGponThresholdDataIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponThresholdDataIndex.setStatus(_A)
_ZxGponThresholdDataMeId_Type=Integer32
_ZxGponThresholdDataMeId_Object=MibTableColumn
zxGponThresholdDataMeId=_ZxGponThresholdDataMeId_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,2),_ZxGponThresholdDataMeId_Type())
zxGponThresholdDataMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponThresholdDataMeId.setStatus(_A)
_ZxGponThresholdDataValue1_Type=Unsigned32
_ZxGponThresholdDataValue1_Object=MibTableColumn
zxGponThresholdDataValue1=_ZxGponThresholdDataValue1_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,3),_ZxGponThresholdDataValue1_Type())
zxGponThresholdDataValue1.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue1.setStatus(_A)
_ZxGponThresholdDataValue2_Type=Unsigned32
_ZxGponThresholdDataValue2_Object=MibTableColumn
zxGponThresholdDataValue2=_ZxGponThresholdDataValue2_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,4),_ZxGponThresholdDataValue2_Type())
zxGponThresholdDataValue2.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue2.setStatus(_A)
_ZxGponThresholdDataValue3_Type=Unsigned32
_ZxGponThresholdDataValue3_Object=MibTableColumn
zxGponThresholdDataValue3=_ZxGponThresholdDataValue3_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,5),_ZxGponThresholdDataValue3_Type())
zxGponThresholdDataValue3.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue3.setStatus(_A)
_ZxGponThresholdDataValue4_Type=Unsigned32
_ZxGponThresholdDataValue4_Object=MibTableColumn
zxGponThresholdDataValue4=_ZxGponThresholdDataValue4_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,6),_ZxGponThresholdDataValue4_Type())
zxGponThresholdDataValue4.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue4.setStatus(_A)
_ZxGponThresholdDataValue5_Type=Unsigned32
_ZxGponThresholdDataValue5_Object=MibTableColumn
zxGponThresholdDataValue5=_ZxGponThresholdDataValue5_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,7),_ZxGponThresholdDataValue5_Type())
zxGponThresholdDataValue5.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue5.setStatus(_A)
_ZxGponThresholdDataValue6_Type=Unsigned32
_ZxGponThresholdDataValue6_Object=MibTableColumn
zxGponThresholdDataValue6=_ZxGponThresholdDataValue6_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,8),_ZxGponThresholdDataValue6_Type())
zxGponThresholdDataValue6.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue6.setStatus(_A)
_ZxGponThresholdDataValue7_Type=Unsigned32
_ZxGponThresholdDataValue7_Object=MibTableColumn
zxGponThresholdDataValue7=_ZxGponThresholdDataValue7_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,9),_ZxGponThresholdDataValue7_Type())
zxGponThresholdDataValue7.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue7.setStatus(_A)
_ZxGponThresholdDataValue8_Type=Unsigned32
_ZxGponThresholdDataValue8_Object=MibTableColumn
zxGponThresholdDataValue8=_ZxGponThresholdDataValue8_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,10),_ZxGponThresholdDataValue8_Type())
zxGponThresholdDataValue8.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue8.setStatus(_A)
_ZxGponThresholdDataValue9_Type=Unsigned32
_ZxGponThresholdDataValue9_Object=MibTableColumn
zxGponThresholdDataValue9=_ZxGponThresholdDataValue9_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,11),_ZxGponThresholdDataValue9_Type())
zxGponThresholdDataValue9.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue9.setStatus(_A)
_ZxGponThresholdDataValue10_Type=Unsigned32
_ZxGponThresholdDataValue10_Object=MibTableColumn
zxGponThresholdDataValue10=_ZxGponThresholdDataValue10_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,12),_ZxGponThresholdDataValue10_Type())
zxGponThresholdDataValue10.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue10.setStatus(_A)
_ZxGponThresholdDataValue11_Type=Unsigned32
_ZxGponThresholdDataValue11_Object=MibTableColumn
zxGponThresholdDataValue11=_ZxGponThresholdDataValue11_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,13),_ZxGponThresholdDataValue11_Type())
zxGponThresholdDataValue11.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue11.setStatus(_A)
_ZxGponThresholdDataValue12_Type=Unsigned32
_ZxGponThresholdDataValue12_Object=MibTableColumn
zxGponThresholdDataValue12=_ZxGponThresholdDataValue12_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,14),_ZxGponThresholdDataValue12_Type())
zxGponThresholdDataValue12.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue12.setStatus(_A)
_ZxGponThresholdDataValue13_Type=Unsigned32
_ZxGponThresholdDataValue13_Object=MibTableColumn
zxGponThresholdDataValue13=_ZxGponThresholdDataValue13_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,15),_ZxGponThresholdDataValue13_Type())
zxGponThresholdDataValue13.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue13.setStatus(_A)
_ZxGponThresholdDataValue14_Type=Unsigned32
_ZxGponThresholdDataValue14_Object=MibTableColumn
zxGponThresholdDataValue14=_ZxGponThresholdDataValue14_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,16),_ZxGponThresholdDataValue14_Type())
zxGponThresholdDataValue14.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataValue14.setStatus(_A)
_ZxGponThresholdDataCreateUsedIdx_Type=Integer32
_ZxGponThresholdDataCreateUsedIdx_Object=MibTableColumn
zxGponThresholdDataCreateUsedIdx=_ZxGponThresholdDataCreateUsedIdx_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,17),_ZxGponThresholdDataCreateUsedIdx_Type())
zxGponThresholdDataCreateUsedIdx.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataCreateUsedIdx.setStatus(_A)
_ZxGponThresholdDataModifyMatchIdx_Type=Integer32
_ZxGponThresholdDataModifyMatchIdx_Object=MibTableColumn
zxGponThresholdDataModifyMatchIdx=_ZxGponThresholdDataModifyMatchIdx_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,18),_ZxGponThresholdDataModifyMatchIdx_Type())
zxGponThresholdDataModifyMatchIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponThresholdDataModifyMatchIdx.setStatus(_A)
class _ZxGponThresholdDataModifyFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_ZxGponThresholdDataModifyFlag_Type.__name__=_E
_ZxGponThresholdDataModifyFlag_Object=MibTableColumn
zxGponThresholdDataModifyFlag=_ZxGponThresholdDataModifyFlag_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,19),_ZxGponThresholdDataModifyFlag_Type())
zxGponThresholdDataModifyFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponThresholdDataModifyFlag.setStatus(_A)
_ZxGponThresholdDataEntryStatus_Type=RowStatus
_ZxGponThresholdDataEntryStatus_Object=MibTableColumn
zxGponThresholdDataEntryStatus=_ZxGponThresholdDataEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,21,11,1,20),_ZxGponThresholdDataEntryStatus_Type())
zxGponThresholdDataEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataEntryStatus.setStatus(_A)
_ZxGponProtectionDataTable_Object=MibTable
zxGponProtectionDataTable=_ZxGponProtectionDataTable_Object((1,3,6,1,4,1,3902,1012,3,21,13))
if mibBuilder.loadTexts:zxGponProtectionDataTable.setStatus(_A)
_ZxGponProtectionDataEntry_Object=MibTableRow
zxGponProtectionDataEntry=_ZxGponProtectionDataEntry_Object((1,3,6,1,4,1,3902,1012,3,21,13,1))
zxGponProtectionDataEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_AX))
if mibBuilder.loadTexts:zxGponProtectionDataEntry.setStatus(_A)
_ZxGponProtectionDataIndex_Type=Integer32
_ZxGponProtectionDataIndex_Object=MibTableColumn
zxGponProtectionDataIndex=_ZxGponProtectionDataIndex_Object((1,3,6,1,4,1,3902,1012,3,21,13,1,1),_ZxGponProtectionDataIndex_Type())
zxGponProtectionDataIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponProtectionDataIndex.setStatus(_A)
_ZxGponProtectionDataMeId_Type=Integer32
_ZxGponProtectionDataMeId_Object=MibTableColumn
zxGponProtectionDataMeId=_ZxGponProtectionDataMeId_Object((1,3,6,1,4,1,3902,1012,3,21,13,1,2),_ZxGponProtectionDataMeId_Type())
zxGponProtectionDataMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponProtectionDataMeId.setStatus(_A)
_ZxGponProtectionDataWorkingAni_Type=Integer32
_ZxGponProtectionDataWorkingAni_Object=MibTableColumn
zxGponProtectionDataWorkingAni=_ZxGponProtectionDataWorkingAni_Object((1,3,6,1,4,1,3902,1012,3,21,13,1,3),_ZxGponProtectionDataWorkingAni_Type())
zxGponProtectionDataWorkingAni.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponProtectionDataWorkingAni.setStatus(_A)
_ZxGponProtectionDataProtectionAni_Type=Integer32
_ZxGponProtectionDataProtectionAni_Object=MibTableColumn
zxGponProtectionDataProtectionAni=_ZxGponProtectionDataProtectionAni_Object((1,3,6,1,4,1,3902,1012,3,21,13,1,4),_ZxGponProtectionDataProtectionAni_Type())
zxGponProtectionDataProtectionAni.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponProtectionDataProtectionAni.setStatus(_A)
class _ZxGponProtectionDataProtectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('oneplusone',1),('oneratioone1',2),('oneratioone2',3)))
_ZxGponProtectionDataProtectionType_Type.__name__=_E
_ZxGponProtectionDataProtectionType_Object=MibTableColumn
zxGponProtectionDataProtectionType=_ZxGponProtectionDataProtectionType_Object((1,3,6,1,4,1,3902,1012,3,21,13,1,5),_ZxGponProtectionDataProtectionType_Type())
zxGponProtectionDataProtectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponProtectionDataProtectionType.setStatus(_A)
_ZxGponProtectionDataRevertive_Type=TruthValue
_ZxGponProtectionDataRevertive_Object=MibTableColumn
zxGponProtectionDataRevertive=_ZxGponProtectionDataRevertive_Object((1,3,6,1,4,1,3902,1012,3,21,13,1,6),_ZxGponProtectionDataRevertive_Type())
zxGponProtectionDataRevertive.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponProtectionDataRevertive.setStatus(_A)
class _ZxGponProtectionDataWTT_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxGponProtectionDataWTT_Type.__name__=_E
_ZxGponProtectionDataWTT_Object=MibTableColumn
zxGponProtectionDataWTT=_ZxGponProtectionDataWTT_Object((1,3,6,1,4,1,3902,1012,3,21,13,1,7),_ZxGponProtectionDataWTT_Type())
zxGponProtectionDataWTT.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponProtectionDataWTT.setStatus(_A)
class _ZxGponProtectionDataSGT_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxGponProtectionDataSGT_Type.__name__=_E
_ZxGponProtectionDataSGT_Object=MibTableColumn
zxGponProtectionDataSGT=_ZxGponProtectionDataSGT_Object((1,3,6,1,4,1,3902,1012,3,21,13,1,8),_ZxGponProtectionDataSGT_Type())
zxGponProtectionDataSGT.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponProtectionDataSGT.setStatus(_A)
_ZxGponAniMgmt_ObjectIdentity=ObjectIdentity
zxGponAniMgmt=_ZxGponAniMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,22))
_ZxGponAniInfoTable_Object=MibTable
zxGponAniInfoTable=_ZxGponAniInfoTable_Object((1,3,6,1,4,1,3902,1012,3,22,1))
if mibBuilder.loadTexts:zxGponAniInfoTable.setStatus(_A)
_ZxGponAniInfoEntry_Object=MibTableRow
zxGponAniInfoEntry=_ZxGponAniInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,22,1,1))
zxGponAniInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_AY))
if mibBuilder.loadTexts:zxGponAniInfoEntry.setStatus(_A)
_ZxGponAniInfoIndex_Type=Integer32
_ZxGponAniInfoIndex_Object=MibTableColumn
zxGponAniInfoIndex=_ZxGponAniInfoIndex_Object((1,3,6,1,4,1,3902,1012,3,22,1,1,1),_ZxGponAniInfoIndex_Type())
zxGponAniInfoIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponAniInfoIndex.setStatus(_A)
_ZxGponAniInfoMeId_Type=Integer32
_ZxGponAniInfoMeId_Object=MibTableColumn
zxGponAniInfoMeId=_ZxGponAniInfoMeId_Object((1,3,6,1,4,1,3902,1012,3,22,1,1,2),_ZxGponAniInfoMeId_Type())
zxGponAniInfoMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponAniInfoMeId.setStatus(_A)
_ZxGponAniInfoSRIndication_Type=TruthValue
_ZxGponAniInfoSRIndication_Object=MibTableColumn
zxGponAniInfoSRIndication=_ZxGponAniInfoSRIndication_Object((1,3,6,1,4,1,3902,1012,3,22,1,1,3),_ZxGponAniInfoSRIndication_Type())
zxGponAniInfoSRIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponAniInfoSRIndication.setStatus(_A)
_ZxGponAniInfoTotalTcontNumber_Type=Integer32
_ZxGponAniInfoTotalTcontNumber_Object=MibTableColumn
zxGponAniInfoTotalTcontNumber=_ZxGponAniInfoTotalTcontNumber_Object((1,3,6,1,4,1,3902,1012,3,22,1,1,4),_ZxGponAniInfoTotalTcontNumber_Type())
zxGponAniInfoTotalTcontNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponAniInfoTotalTcontNumber.setStatus(_A)
_ZxGponAniInfoGemBlockLength_Type=Integer32
_ZxGponAniInfoGemBlockLength_Object=MibTableColumn
zxGponAniInfoGemBlockLength=_ZxGponAniInfoGemBlockLength_Object((1,3,6,1,4,1,3902,1012,3,22,1,1,5),_ZxGponAniInfoGemBlockLength_Type())
zxGponAniInfoGemBlockLength.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponAniInfoGemBlockLength.setStatus(_A)
class _ZxGponAniInfoPiggybackDbaReporting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('mode0Only',1),('mode01',2),('mode02',3),('mode012',4),('modeNotSupport',5)))
_ZxGponAniInfoPiggybackDbaReporting_Type.__name__=_E
_ZxGponAniInfoPiggybackDbaReporting_Object=MibTableColumn
zxGponAniInfoPiggybackDbaReporting=_ZxGponAniInfoPiggybackDbaReporting_Object((1,3,6,1,4,1,3902,1012,3,22,1,1,6),_ZxGponAniInfoPiggybackDbaReporting_Type())
zxGponAniInfoPiggybackDbaReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponAniInfoPiggybackDbaReporting.setStatus(_A)
class _ZxGponAniInfoWholeOnuDbaReporting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wholeDbaReportNotSupport',1),('wholeDbaReportSupport',2)))
_ZxGponAniInfoWholeOnuDbaReporting_Type.__name__=_E
_ZxGponAniInfoWholeOnuDbaReporting_Object=MibTableColumn
zxGponAniInfoWholeOnuDbaReporting=_ZxGponAniInfoWholeOnuDbaReporting_Object((1,3,6,1,4,1,3902,1012,3,22,1,1,7),_ZxGponAniInfoWholeOnuDbaReporting_Type())
zxGponAniInfoWholeOnuDbaReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponAniInfoWholeOnuDbaReporting.setStatus(_A)
_ZxGponAniInfoSFThreshold_Type=Integer32
_ZxGponAniInfoSFThreshold_Object=MibTableColumn
zxGponAniInfoSFThreshold=_ZxGponAniInfoSFThreshold_Object((1,3,6,1,4,1,3902,1012,3,22,1,1,8),_ZxGponAniInfoSFThreshold_Type())
zxGponAniInfoSFThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponAniInfoSFThreshold.setStatus(_A)
_ZxGponAniInfoSDThreshold_Type=Integer32
_ZxGponAniInfoSDThreshold_Object=MibTableColumn
zxGponAniInfoSDThreshold=_ZxGponAniInfoSDThreshold_Object((1,3,6,1,4,1,3902,1012,3,22,1,1,9),_ZxGponAniInfoSDThreshold_Type())
zxGponAniInfoSDThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponAniInfoSDThreshold.setStatus(_A)
_ZxGponTcontInfoTable_Object=MibTable
zxGponTcontInfoTable=_ZxGponTcontInfoTable_Object((1,3,6,1,4,1,3902,1012,3,22,3))
if mibBuilder.loadTexts:zxGponTcontInfoTable.setStatus(_A)
_ZxGponTcontInfoEntry_Object=MibTableRow
zxGponTcontInfoEntry=_ZxGponTcontInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,22,3,1))
zxGponTcontInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_AZ))
if mibBuilder.loadTexts:zxGponTcontInfoEntry.setStatus(_A)
_ZxGponTcontInfoIndex_Type=Integer32
_ZxGponTcontInfoIndex_Object=MibTableColumn
zxGponTcontInfoIndex=_ZxGponTcontInfoIndex_Object((1,3,6,1,4,1,3902,1012,3,22,3,1,1),_ZxGponTcontInfoIndex_Type())
zxGponTcontInfoIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponTcontInfoIndex.setStatus(_A)
_ZxGponTcontInfoMeId_Type=Integer32
_ZxGponTcontInfoMeId_Object=MibTableColumn
zxGponTcontInfoMeId=_ZxGponTcontInfoMeId_Object((1,3,6,1,4,1,3902,1012,3,22,3,1,2),_ZxGponTcontInfoMeId_Type())
zxGponTcontInfoMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTcontInfoMeId.setStatus(_A)
_ZxGponTcontInfoAllocID_Type=Integer32
_ZxGponTcontInfoAllocID_Object=MibTableColumn
zxGponTcontInfoAllocID=_ZxGponTcontInfoAllocID_Object((1,3,6,1,4,1,3902,1012,3,22,3,1,3),_ZxGponTcontInfoAllocID_Type())
zxGponTcontInfoAllocID.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponTcontInfoAllocID.setStatus(_A)
class _ZxGponTcontInfoModeIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('modeAtm',1),('modeGem',2)))
_ZxGponTcontInfoModeIndicator_Type.__name__=_E
_ZxGponTcontInfoModeIndicator_Object=MibTableColumn
zxGponTcontInfoModeIndicator=_ZxGponTcontInfoModeIndicator_Object((1,3,6,1,4,1,3902,1012,3,22,3,1,4),_ZxGponTcontInfoModeIndicator_Type())
zxGponTcontInfoModeIndicator.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTcontInfoModeIndicator.setStatus(_A)
class _ZxGponTcontInfoPolicy_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hol',1),(_g,2),('null',3)))
_ZxGponTcontInfoPolicy_Type.__name__=_E
_ZxGponTcontInfoPolicy_Object=MibTableColumn
zxGponTcontInfoPolicy=_ZxGponTcontInfoPolicy_Object((1,3,6,1,4,1,3902,1012,3,22,3,1,5),_ZxGponTcontInfoPolicy_Type())
zxGponTcontInfoPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTcontInfoPolicy.setStatus(_A)
_ZxGponUniMgmt_ObjectIdentity=ObjectIdentity
zxGponUniMgmt=_ZxGponUniMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,23))
_ZxGpon8021pMapperTable_Object=MibTable
zxGpon8021pMapperTable=_ZxGpon8021pMapperTable_Object((1,3,6,1,4,1,3902,1012,3,23,1))
if mibBuilder.loadTexts:zxGpon8021pMapperTable.setStatus(_A)
_ZxGpon8021pMapperEntry_Object=MibTableRow
zxGpon8021pMapperEntry=_ZxGpon8021pMapperEntry_Object((1,3,6,1,4,1,3902,1012,3,23,1,1))
zxGpon8021pMapperEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Aa))
if mibBuilder.loadTexts:zxGpon8021pMapperEntry.setStatus(_A)
_ZxGpon8021pMapperMeIdIdx_Type=Integer32
_ZxGpon8021pMapperMeIdIdx_Object=MibTableColumn
zxGpon8021pMapperMeIdIdx=_ZxGpon8021pMapperMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,1),_ZxGpon8021pMapperMeIdIdx_Type())
zxGpon8021pMapperMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGpon8021pMapperMeIdIdx.setStatus(_A)
_ZxGpon8021pMapperPptpUniPtr_Type=Integer32
_ZxGpon8021pMapperPptpUniPtr_Object=MibTableColumn
zxGpon8021pMapperPptpUniPtr=_ZxGpon8021pMapperPptpUniPtr_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,2),_ZxGpon8021pMapperPptpUniPtr_Type())
zxGpon8021pMapperPptpUniPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperPptpUniPtr.setStatus(_A)
_ZxGpon8021pMapperPri0IwTpPtr_Type=Integer32
_ZxGpon8021pMapperPri0IwTpPtr_Object=MibTableColumn
zxGpon8021pMapperPri0IwTpPtr=_ZxGpon8021pMapperPri0IwTpPtr_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,3),_ZxGpon8021pMapperPri0IwTpPtr_Type())
zxGpon8021pMapperPri0IwTpPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperPri0IwTpPtr.setStatus(_A)
_ZxGpon8021pMapperPri1IwTpPtr_Type=Integer32
_ZxGpon8021pMapperPri1IwTpPtr_Object=MibTableColumn
zxGpon8021pMapperPri1IwTpPtr=_ZxGpon8021pMapperPri1IwTpPtr_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,4),_ZxGpon8021pMapperPri1IwTpPtr_Type())
zxGpon8021pMapperPri1IwTpPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperPri1IwTpPtr.setStatus(_A)
_ZxGpon8021pMapperPri2IwTpPtr_Type=Integer32
_ZxGpon8021pMapperPri2IwTpPtr_Object=MibTableColumn
zxGpon8021pMapperPri2IwTpPtr=_ZxGpon8021pMapperPri2IwTpPtr_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,5),_ZxGpon8021pMapperPri2IwTpPtr_Type())
zxGpon8021pMapperPri2IwTpPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperPri2IwTpPtr.setStatus(_A)
_ZxGpon8021pMapperPri3IwTpPtr_Type=Integer32
_ZxGpon8021pMapperPri3IwTpPtr_Object=MibTableColumn
zxGpon8021pMapperPri3IwTpPtr=_ZxGpon8021pMapperPri3IwTpPtr_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,6),_ZxGpon8021pMapperPri3IwTpPtr_Type())
zxGpon8021pMapperPri3IwTpPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperPri3IwTpPtr.setStatus(_A)
_ZxGpon8021pMapperPri4IwTpPtr_Type=Integer32
_ZxGpon8021pMapperPri4IwTpPtr_Object=MibTableColumn
zxGpon8021pMapperPri4IwTpPtr=_ZxGpon8021pMapperPri4IwTpPtr_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,7),_ZxGpon8021pMapperPri4IwTpPtr_Type())
zxGpon8021pMapperPri4IwTpPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperPri4IwTpPtr.setStatus(_A)
_ZxGpon8021pMapperPri5IwTpPtr_Type=Integer32
_ZxGpon8021pMapperPri5IwTpPtr_Object=MibTableColumn
zxGpon8021pMapperPri5IwTpPtr=_ZxGpon8021pMapperPri5IwTpPtr_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,8),_ZxGpon8021pMapperPri5IwTpPtr_Type())
zxGpon8021pMapperPri5IwTpPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperPri5IwTpPtr.setStatus(_A)
_ZxGpon8021pMapperPri6IwTpPtr_Type=Integer32
_ZxGpon8021pMapperPri6IwTpPtr_Object=MibTableColumn
zxGpon8021pMapperPri6IwTpPtr=_ZxGpon8021pMapperPri6IwTpPtr_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,9),_ZxGpon8021pMapperPri6IwTpPtr_Type())
zxGpon8021pMapperPri6IwTpPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperPri6IwTpPtr.setStatus(_A)
_ZxGpon8021pMapperPri7IwTpPtr_Type=Integer32
_ZxGpon8021pMapperPri7IwTpPtr_Object=MibTableColumn
zxGpon8021pMapperPri7IwTpPtr=_ZxGpon8021pMapperPri7IwTpPtr_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,10),_ZxGpon8021pMapperPri7IwTpPtr_Type())
zxGpon8021pMapperPri7IwTpPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperPri7IwTpPtr.setStatus(_A)
class _ZxGpon8021pMapperUntagFrmInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Ab,1),(_Ac,2)))
_ZxGpon8021pMapperUntagFrmInd_Type.__name__=_E
_ZxGpon8021pMapperUntagFrmInd_Object=MibTableColumn
zxGpon8021pMapperUntagFrmInd=_ZxGpon8021pMapperUntagFrmInd_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,11),_ZxGpon8021pMapperUntagFrmInd_Type())
zxGpon8021pMapperUntagFrmInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperUntagFrmInd.setStatus(_A)
class _ZxGpon8021pMapperDscpTo8021pPri_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxGpon8021pMapperDscpTo8021pPri_Type.__name__=_O
_ZxGpon8021pMapperDscpTo8021pPri_Object=MibTableColumn
zxGpon8021pMapperDscpTo8021pPri=_ZxGpon8021pMapperDscpTo8021pPri_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,12),_ZxGpon8021pMapperDscpTo8021pPri_Type())
zxGpon8021pMapperDscpTo8021pPri.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperDscpTo8021pPri.setStatus(_A)
_ZxGpon8021pMapperDefaultPri_Type=Integer32
_ZxGpon8021pMapperDefaultPri_Object=MibTableColumn
zxGpon8021pMapperDefaultPri=_ZxGpon8021pMapperDefaultPri_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,13),_ZxGpon8021pMapperDefaultPri_Type())
zxGpon8021pMapperDefaultPri.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGpon8021pMapperDefaultPri.setStatus(_A)
class _ZxGpon8021pMapperMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGpon8021pMapperMgmtCtrlFlag_Type.__name__=_E
_ZxGpon8021pMapperMgmtCtrlFlag_Object=MibTableColumn
zxGpon8021pMapperMgmtCtrlFlag=_ZxGpon8021pMapperMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,14),_ZxGpon8021pMapperMgmtCtrlFlag_Type())
zxGpon8021pMapperMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGpon8021pMapperMgmtCtrlFlag.setStatus(_A)
_ZxGpon8021pMapperEntryStatus_Type=RowStatus
_ZxGpon8021pMapperEntryStatus_Object=MibTableColumn
zxGpon8021pMapperEntryStatus=_ZxGpon8021pMapperEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,23,1,1,15),_ZxGpon8021pMapperEntryStatus_Type())
zxGpon8021pMapperEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGpon8021pMapperEntryStatus.setStatus(_A)
_ZxGponUniInfoTable_Object=MibTable
zxGponUniInfoTable=_ZxGponUniInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,2))
if mibBuilder.loadTexts:zxGponUniInfoTable.setStatus(_A)
_ZxGponUniInfoEntry_Object=MibTableRow
zxGponUniInfoEntry=_ZxGponUniInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,2,1))
zxGponUniInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Ad))
if mibBuilder.loadTexts:zxGponUniInfoEntry.setStatus(_A)
_ZxGponUniInfoIndex_Type=Integer32
_ZxGponUniInfoIndex_Object=MibTableColumn
zxGponUniInfoIndex=_ZxGponUniInfoIndex_Object((1,3,6,1,4,1,3902,1012,3,23,2,1,1),_ZxGponUniInfoIndex_Type())
zxGponUniInfoIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponUniInfoIndex.setStatus(_A)
_ZxGponUniInfoMeId_Type=Integer32
_ZxGponUniInfoMeId_Object=MibTableColumn
zxGponUniInfoMeId=_ZxGponUniInfoMeId_Object((1,3,6,1,4,1,3902,1012,3,23,2,1,2),_ZxGponUniInfoMeId_Type())
zxGponUniInfoMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponUniInfoMeId.setStatus(_A)
_ZxGponUniInfoCfgOption_Type=Integer32
_ZxGponUniInfoCfgOption_Object=MibTableColumn
zxGponUniInfoCfgOption=_ZxGponUniInfoCfgOption_Object((1,3,6,1,4,1,3902,1012,3,23,2,1,3),_ZxGponUniInfoCfgOption_Type())
zxGponUniInfoCfgOption.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponUniInfoCfgOption.setStatus(_A)
class _ZxGponUniInfoAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_ZxGponUniInfoAdminState_Type.__name__=_E
_ZxGponUniInfoAdminState_Object=MibTableColumn
zxGponUniInfoAdminState=_ZxGponUniInfoAdminState_Object((1,3,6,1,4,1,3902,1012,3,23,2,1,4),_ZxGponUniInfoAdminState_Type())
zxGponUniInfoAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponUniInfoAdminState.setStatus(_A)
_EthernetUniMib_ObjectIdentity=ObjectIdentity
ethernetUniMib=_EthernetUniMib_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,23,8))
_ZxGponPPTPEthUniInfoTable_Object=MibTable
zxGponPPTPEthUniInfoTable=_ZxGponPPTPEthUniInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,8,1))
if mibBuilder.loadTexts:zxGponPPTPEthUniInfoTable.setStatus(_A)
_ZxGponPPTPEthUniInfoEntry_Object=MibTableRow
zxGponPPTPEthUniInfoEntry=_ZxGponPPTPEthUniInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1))
zxGponPPTPEthUniInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_a))
if mibBuilder.loadTexts:zxGponPPTPEthUniInfoEntry.setStatus(_A)
_ZxGponPPTPEthInfoTPID_Type=Integer32
_ZxGponPPTPEthInfoTPID_Object=MibTableColumn
zxGponPPTPEthInfoTPID=_ZxGponPPTPEthInfoTPID_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,1),_ZxGponPPTPEthInfoTPID_Type())
zxGponPPTPEthInfoTPID.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponPPTPEthInfoTPID.setStatus(_A)
_ZxGponPPTPEthInfoMeId_Type=Integer32
_ZxGponPPTPEthInfoMeId_Object=MibTableColumn
zxGponPPTPEthInfoMeId=_ZxGponPPTPEthInfoMeId_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,2),_ZxGponPPTPEthInfoMeId_Type())
zxGponPPTPEthInfoMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPPTPEthInfoMeId.setStatus(_A)
class _ZxGponPPTPEthInfoExpectedType_Type(Integer32):defaultValue=0
_ZxGponPPTPEthInfoExpectedType_Type.__name__=_E
_ZxGponPPTPEthInfoExpectedType_Object=MibTableColumn
zxGponPPTPEthInfoExpectedType=_ZxGponPPTPEthInfoExpectedType_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,3),_ZxGponPPTPEthInfoExpectedType_Type())
zxGponPPTPEthInfoExpectedType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoExpectedType.setStatus(_A)
_ZxGponPPTPEthInfoSensedType_Type=Integer32
_ZxGponPPTPEthInfoSensedType_Object=MibTableColumn
zxGponPPTPEthInfoSensedType=_ZxGponPPTPEthInfoSensedType_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,4),_ZxGponPPTPEthInfoSensedType_Type())
zxGponPPTPEthInfoSensedType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPPTPEthInfoSensedType.setStatus(_A)
_ZxGponPPTPEthInfoAutoDetectCfg_Type=Integer32
_ZxGponPPTPEthInfoAutoDetectCfg_Object=MibTableColumn
zxGponPPTPEthInfoAutoDetectCfg=_ZxGponPPTPEthInfoAutoDetectCfg_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,5),_ZxGponPPTPEthInfoAutoDetectCfg_Type())
zxGponPPTPEthInfoAutoDetectCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoAutoDetectCfg.setStatus(_A)
class _ZxGponPPTPEthInfoEthLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('loop',2)))
_ZxGponPPTPEthInfoEthLoopback_Type.__name__=_E
_ZxGponPPTPEthInfoEthLoopback_Object=MibTableColumn
zxGponPPTPEthInfoEthLoopback=_ZxGponPPTPEthInfoEthLoopback_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,6),_ZxGponPPTPEthInfoEthLoopback_Type())
zxGponPPTPEthInfoEthLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoEthLoopback.setStatus(_A)
class _ZxGponPPTPEthInfoAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_ZxGponPPTPEthInfoAdminState_Type.__name__=_E
_ZxGponPPTPEthInfoAdminState_Object=MibTableColumn
zxGponPPTPEthInfoAdminState=_ZxGponPPTPEthInfoAdminState_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,7),_ZxGponPPTPEthInfoAdminState_Type())
zxGponPPTPEthInfoAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoAdminState.setStatus(_A)
class _ZxGponPPTPEthInfoOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_ZxGponPPTPEthInfoOperationalState_Type.__name__=_E
_ZxGponPPTPEthInfoOperationalState_Object=MibTableColumn
zxGponPPTPEthInfoOperationalState=_ZxGponPPTPEthInfoOperationalState_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,8),_ZxGponPPTPEthInfoOperationalState_Type())
zxGponPPTPEthInfoOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPPTPEthInfoOperationalState.setStatus(_A)
class _ZxGponPPTPEthInfoDuplexSpeedInd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('autonegotiate',1),('half-10',2),('full-10',3),('half-100',4),('full-100',5),('full-1000',6)))
_ZxGponPPTPEthInfoDuplexSpeedInd_Type.__name__=_E
_ZxGponPPTPEthInfoDuplexSpeedInd_Object=MibTableColumn
zxGponPPTPEthInfoDuplexSpeedInd=_ZxGponPPTPEthInfoDuplexSpeedInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,9),_ZxGponPPTPEthInfoDuplexSpeedInd_Type())
zxGponPPTPEthInfoDuplexSpeedInd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPPTPEthInfoDuplexSpeedInd.setStatus(_A)
class _ZxGponPPTPEthInfoMaxFrameSize_Type(Integer32):defaultValue=1518
_ZxGponPPTPEthInfoMaxFrameSize_Type.__name__=_E
_ZxGponPPTPEthInfoMaxFrameSize_Object=MibTableColumn
zxGponPPTPEthInfoMaxFrameSize=_ZxGponPPTPEthInfoMaxFrameSize_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,10),_ZxGponPPTPEthInfoMaxFrameSize_Type())
zxGponPPTPEthInfoMaxFrameSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoMaxFrameSize.setStatus(_A)
class _ZxGponPPTPEthInfoDTEorDCEInd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dce',1),('dte',2)))
_ZxGponPPTPEthInfoDTEorDCEInd_Type.__name__=_E
_ZxGponPPTPEthInfoDTEorDCEInd_Object=MibTableColumn
zxGponPPTPEthInfoDTEorDCEInd=_ZxGponPPTPEthInfoDTEorDCEInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,11),_ZxGponPPTPEthInfoDTEorDCEInd_Type())
zxGponPPTPEthInfoDTEorDCEInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoDTEorDCEInd.setStatus(_A)
class _ZxGponPPTPEthInfoPauseTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxGponPPTPEthInfoPauseTime_Type.__name__=_E
_ZxGponPPTPEthInfoPauseTime_Object=MibTableColumn
zxGponPPTPEthInfoPauseTime=_ZxGponPPTPEthInfoPauseTime_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,12),_ZxGponPPTPEthInfoPauseTime_Type())
zxGponPPTPEthInfoPauseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoPauseTime.setStatus(_A)
class _ZxGponPPTPEthInfoBridgedorIPInd_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bridged',1),('iprouter',2),('auto',3)))
_ZxGponPPTPEthInfoBridgedorIPInd_Type.__name__=_E
_ZxGponPPTPEthInfoBridgedorIPInd_Object=MibTableColumn
zxGponPPTPEthInfoBridgedorIPInd=_ZxGponPPTPEthInfoBridgedorIPInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,13),_ZxGponPPTPEthInfoBridgedorIPInd_Type())
zxGponPPTPEthInfoBridgedorIPInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoBridgedorIPInd.setStatus(_A)
class _ZxGponPPTPEthInfoARC_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ZxGponPPTPEthInfoARC_Type.__name__=_E
_ZxGponPPTPEthInfoARC_Object=MibTableColumn
zxGponPPTPEthInfoARC=_ZxGponPPTPEthInfoARC_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,14),_ZxGponPPTPEthInfoARC_Type())
zxGponPPTPEthInfoARC.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoARC.setStatus(_A)
class _ZxGponPPTPEthInfoARCInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxGponPPTPEthInfoARCInterval_Type.__name__=_E
_ZxGponPPTPEthInfoARCInterval_Object=MibTableColumn
zxGponPPTPEthInfoARCInterval=_ZxGponPPTPEthInfoARCInterval_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,15),_ZxGponPPTPEthInfoARCInterval_Type())
zxGponPPTPEthInfoARCInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoARCInterval.setStatus(_A)
class _ZxGponPPTPEthInfoPppoeFilterEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_ZxGponPPTPEthInfoPppoeFilterEnable_Type.__name__=_E
_ZxGponPPTPEthInfoPppoeFilterEnable_Object=MibTableColumn
zxGponPPTPEthInfoPppoeFilterEnable=_ZxGponPPTPEthInfoPppoeFilterEnable_Object((1,3,6,1,4,1,3902,1012,3,23,8,1,1,16),_ZxGponPPTPEthInfoPppoeFilterEnable_Type())
zxGponPPTPEthInfoPppoeFilterEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPEthInfoPppoeFilterEnable.setStatus(_A)
_ZxGponMACBSPInfoTable_Object=MibTable
zxGponMACBSPInfoTable=_ZxGponMACBSPInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,8,2))
if mibBuilder.loadTexts:zxGponMACBSPInfoTable.setStatus(_A)
_ZxGponMACBSPInfoEntry_Object=MibTableRow
zxGponMACBSPInfoEntry=_ZxGponMACBSPInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1))
zxGponMACBSPInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_h))
if mibBuilder.loadTexts:zxGponMACBSPInfoEntry.setStatus(_A)
_ZxGponMACBSPInfoMeIdIdx_Type=Integer32
_ZxGponMACBSPInfoMeIdIdx_Object=MibTableColumn
zxGponMACBSPInfoMeIdIdx=_ZxGponMACBSPInfoMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,1),_ZxGponMACBSPInfoMeIdIdx_Type())
zxGponMACBSPInfoMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponMACBSPInfoMeIdIdx.setStatus(_A)
_ZxGponMACBSPInfoSTPInd_Type=TruthValue
_ZxGponMACBSPInfoSTPInd_Object=MibTableColumn
zxGponMACBSPInfoSTPInd=_ZxGponMACBSPInfoSTPInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,2),_ZxGponMACBSPInfoSTPInd_Type())
zxGponMACBSPInfoSTPInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBSPInfoSTPInd.setStatus(_A)
_ZxGponMACBSPInfoLearningInd_Type=TruthValue
_ZxGponMACBSPInfoLearningInd_Object=MibTableColumn
zxGponMACBSPInfoLearningInd=_ZxGponMACBSPInfoLearningInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,3),_ZxGponMACBSPInfoLearningInd_Type())
zxGponMACBSPInfoLearningInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBSPInfoLearningInd.setStatus(_A)
_ZxGponMACBSPInfoPortBInd_Type=TruthValue
_ZxGponMACBSPInfoPortBInd_Object=MibTableColumn
zxGponMACBSPInfoPortBInd=_ZxGponMACBSPInfoPortBInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,4),_ZxGponMACBSPInfoPortBInd_Type())
zxGponMACBSPInfoPortBInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBSPInfoPortBInd.setStatus(_A)
class _ZxGponMACBSPInfoPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxGponMACBSPInfoPriority_Type.__name__=_E
_ZxGponMACBSPInfoPriority_Object=MibTableColumn
zxGponMACBSPInfoPriority=_ZxGponMACBSPInfoPriority_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,5),_ZxGponMACBSPInfoPriority_Type())
zxGponMACBSPInfoPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBSPInfoPriority.setStatus(_A)
class _ZxGponMACBSPInfoMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_ZxGponMACBSPInfoMaxAge_Type.__name__=_i
_ZxGponMACBSPInfoMaxAge_Object=MibTableColumn
zxGponMACBSPInfoMaxAge=_ZxGponMACBSPInfoMaxAge_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,6),_ZxGponMACBSPInfoMaxAge_Type())
zxGponMACBSPInfoMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBSPInfoMaxAge.setStatus(_A)
class _ZxGponMACBSPInfoHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_ZxGponMACBSPInfoHelloTime_Type.__name__=_i
_ZxGponMACBSPInfoHelloTime_Object=MibTableColumn
zxGponMACBSPInfoHelloTime=_ZxGponMACBSPInfoHelloTime_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,7),_ZxGponMACBSPInfoHelloTime_Type())
zxGponMACBSPInfoHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBSPInfoHelloTime.setStatus(_A)
class _ZxGponMACBSPInfoForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_ZxGponMACBSPInfoForwardDelay_Type.__name__=_i
_ZxGponMACBSPInfoForwardDelay_Object=MibTableColumn
zxGponMACBSPInfoForwardDelay=_ZxGponMACBSPInfoForwardDelay_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,8),_ZxGponMACBSPInfoForwardDelay_Type())
zxGponMACBSPInfoForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBSPInfoForwardDelay.setStatus(_A)
class _ZxGponMACBSPInfoMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponMACBSPInfoMgmtCtrlFlag_Type.__name__=_E
_ZxGponMACBSPInfoMgmtCtrlFlag_Object=MibTableColumn
zxGponMACBSPInfoMgmtCtrlFlag=_ZxGponMACBSPInfoMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,9),_ZxGponMACBSPInfoMgmtCtrlFlag_Type())
zxGponMACBSPInfoMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBSPInfoMgmtCtrlFlag.setStatus(_A)
_ZxGponMACBSPInfoEntryStatus_Type=RowStatus
_ZxGponMACBSPInfoEntryStatus_Object=MibTableColumn
zxGponMACBSPInfoEntryStatus=_ZxGponMACBSPInfoEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,23,8,2,1,10),_ZxGponMACBSPInfoEntryStatus_Type())
zxGponMACBSPInfoEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponMACBSPInfoEntryStatus.setStatus(_A)
_ZxGponMACBridgeCfgDataInfoTable_Object=MibTable
zxGponMACBridgeCfgDataInfoTable=_ZxGponMACBridgeCfgDataInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,8,3))
if mibBuilder.loadTexts:zxGponMACBridgeCfgDataInfoTable.setStatus(_A)
_ZxGponMACBridgeCfgDataInfoEntry_Object=MibTableRow
zxGponMACBridgeCfgDataInfoEntry=_ZxGponMACBridgeCfgDataInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,8,3,1))
zxGponMACBridgeCfgDataInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_h))
if mibBuilder.loadTexts:zxGponMACBridgeCfgDataInfoEntry.setStatus(_A)
_ZxGponMACBCfgDataBridgeMACAddress_Type=MacAddress
_ZxGponMACBCfgDataBridgeMACAddress_Object=MibTableColumn
zxGponMACBCfgDataBridgeMACAddress=_ZxGponMACBCfgDataBridgeMACAddress_Object((1,3,6,1,4,1,3902,1012,3,23,8,3,1,1),_ZxGponMACBCfgDataBridgeMACAddress_Type())
zxGponMACBCfgDataBridgeMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBCfgDataBridgeMACAddress.setStatus(_A)
_ZxGponMACBCfgDataBridgePriority_Type=Integer32
_ZxGponMACBCfgDataBridgePriority_Object=MibTableColumn
zxGponMACBCfgDataBridgePriority=_ZxGponMACBCfgDataBridgePriority_Object((1,3,6,1,4,1,3902,1012,3,23,8,3,1,2),_ZxGponMACBCfgDataBridgePriority_Type())
zxGponMACBCfgDataBridgePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBCfgDataBridgePriority.setStatus(_A)
_ZxGponMACBCfgDataDesignatedRoot_Type=Integer32
_ZxGponMACBCfgDataDesignatedRoot_Object=MibTableColumn
zxGponMACBCfgDataDesignatedRoot=_ZxGponMACBCfgDataDesignatedRoot_Object((1,3,6,1,4,1,3902,1012,3,23,8,3,1,3),_ZxGponMACBCfgDataDesignatedRoot_Type())
zxGponMACBCfgDataDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBCfgDataDesignatedRoot.setStatus(_A)
_ZxGponMACBCfgDataRootPathCost_Type=Integer32
_ZxGponMACBCfgDataRootPathCost_Object=MibTableColumn
zxGponMACBCfgDataRootPathCost=_ZxGponMACBCfgDataRootPathCost_Object((1,3,6,1,4,1,3902,1012,3,23,8,3,1,4),_ZxGponMACBCfgDataRootPathCost_Type())
zxGponMACBCfgDataRootPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBCfgDataRootPathCost.setStatus(_A)
_ZxGponMACBCfgDataBridgePortCount_Type=Integer32
_ZxGponMACBCfgDataBridgePortCount_Object=MibTableColumn
zxGponMACBCfgDataBridgePortCount=_ZxGponMACBCfgDataBridgePortCount_Object((1,3,6,1,4,1,3902,1012,3,23,8,3,1,5),_ZxGponMACBCfgDataBridgePortCount_Type())
zxGponMACBCfgDataBridgePortCount.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBCfgDataBridgePortCount.setStatus(_A)
_ZxGponMACBCfgDataRootPortNum_Type=Integer32
_ZxGponMACBCfgDataRootPortNum_Object=MibTableColumn
zxGponMACBCfgDataRootPortNum=_ZxGponMACBCfgDataRootPortNum_Object((1,3,6,1,4,1,3902,1012,3,23,8,3,1,6),_ZxGponMACBCfgDataRootPortNum_Type())
zxGponMACBCfgDataRootPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBCfgDataRootPortNum.setStatus(_A)
_ZxGponMACBCfgDataHelloTime_Type=Integer32
_ZxGponMACBCfgDataHelloTime_Object=MibTableColumn
zxGponMACBCfgDataHelloTime=_ZxGponMACBCfgDataHelloTime_Object((1,3,6,1,4,1,3902,1012,3,23,8,3,1,7),_ZxGponMACBCfgDataHelloTime_Type())
zxGponMACBCfgDataHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBCfgDataHelloTime.setStatus(_A)
_ZxGponMACBCfgDataForwardDelay_Type=Integer32
_ZxGponMACBCfgDataForwardDelay_Object=MibTableColumn
zxGponMACBCfgDataForwardDelay=_ZxGponMACBCfgDataForwardDelay_Object((1,3,6,1,4,1,3902,1012,3,23,8,3,1,8),_ZxGponMACBCfgDataForwardDelay_Type())
zxGponMACBCfgDataForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBCfgDataForwardDelay.setStatus(_A)
_ZxGponMACBriPortCfgDataInfoTable_Object=MibTable
zxGponMACBriPortCfgDataInfoTable=_ZxGponMACBriPortCfgDataInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,8,4))
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataInfoTable.setStatus(_A)
_ZxGponMACBriPortCfgDataInfoEntry_Object=MibTableRow
zxGponMACBriPortCfgDataInfoEntry=_ZxGponMACBriPortCfgDataInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1))
zxGponMACBriPortCfgDataInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_j))
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataInfoEntry.setStatus(_A)
_ZxGponMACBriPortCfgDataMeIdIdx_Type=Integer32
_ZxGponMACBriPortCfgDataMeIdIdx_Object=MibTableColumn
zxGponMACBriPortCfgDataMeIdIdx=_ZxGponMACBriPortCfgDataMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,1),_ZxGponMACBriPortCfgDataMeIdIdx_Type())
zxGponMACBriPortCfgDataMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataMeIdIdx.setStatus(_A)
_ZxGponMACBriPortCfgDataBridgeIdPtr_Type=Integer32
_ZxGponMACBriPortCfgDataBridgeIdPtr_Object=MibTableColumn
zxGponMACBriPortCfgDataBridgeIdPtr=_ZxGponMACBriPortCfgDataBridgeIdPtr_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,2),_ZxGponMACBriPortCfgDataBridgeIdPtr_Type())
zxGponMACBriPortCfgDataBridgeIdPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataBridgeIdPtr.setStatus(_A)
_ZxGponMACBriPortCfgDataPortNum_Type=Integer32
_ZxGponMACBriPortCfgDataPortNum_Object=MibTableColumn
zxGponMACBriPortCfgDataPortNum=_ZxGponMACBriPortCfgDataPortNum_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,3),_ZxGponMACBriPortCfgDataPortNum_Type())
zxGponMACBriPortCfgDataPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataPortNum.setStatus(_A)
_ZxGponMACBriPortCfgDataTPType_Type=Integer32
_ZxGponMACBriPortCfgDataTPType_Object=MibTableColumn
zxGponMACBriPortCfgDataTPType=_ZxGponMACBriPortCfgDataTPType_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,4),_ZxGponMACBriPortCfgDataTPType_Type())
zxGponMACBriPortCfgDataTPType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataTPType.setStatus(_A)
_ZxGponMACBriPortCfgDataTPPointer_Type=Integer32
_ZxGponMACBriPortCfgDataTPPointer_Object=MibTableColumn
zxGponMACBriPortCfgDataTPPointer=_ZxGponMACBriPortCfgDataTPPointer_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,5),_ZxGponMACBriPortCfgDataTPPointer_Type())
zxGponMACBriPortCfgDataTPPointer.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataTPPointer.setStatus(_A)
_ZxGponMACBriPortCfgDataPortPriority_Type=Integer32
_ZxGponMACBriPortCfgDataPortPriority_Object=MibTableColumn
zxGponMACBriPortCfgDataPortPriority=_ZxGponMACBriPortCfgDataPortPriority_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,6),_ZxGponMACBriPortCfgDataPortPriority_Type())
zxGponMACBriPortCfgDataPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataPortPriority.setStatus(_A)
_ZxGponMACBriPortCfgDataPortPathCost_Type=Integer32
_ZxGponMACBriPortCfgDataPortPathCost_Object=MibTableColumn
zxGponMACBriPortCfgDataPortPathCost=_ZxGponMACBriPortCfgDataPortPathCost_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,7),_ZxGponMACBriPortCfgDataPortPathCost_Type())
zxGponMACBriPortCfgDataPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataPortPathCost.setStatus(_A)
_ZxGponMACBriPortCfgDataPortSpanTreeInd_Type=TruthValue
_ZxGponMACBriPortCfgDataPortSpanTreeInd_Object=MibTableColumn
zxGponMACBriPortCfgDataPortSpanTreeInd=_ZxGponMACBriPortCfgDataPortSpanTreeInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,8),_ZxGponMACBriPortCfgDataPortSpanTreeInd_Type())
zxGponMACBriPortCfgDataPortSpanTreeInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataPortSpanTreeInd.setStatus(_A)
_ZxGponMACBriPortCfgDataEncapMethod_Type=Integer32
_ZxGponMACBriPortCfgDataEncapMethod_Object=MibTableColumn
zxGponMACBriPortCfgDataEncapMethod=_ZxGponMACBriPortCfgDataEncapMethod_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,9),_ZxGponMACBriPortCfgDataEncapMethod_Type())
zxGponMACBriPortCfgDataEncapMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataEncapMethod.setStatus(_A)
class _ZxGponMACBriPortCfgDataLANFCSInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_s,2)))
_ZxGponMACBriPortCfgDataLANFCSInd_Type.__name__=_E
_ZxGponMACBriPortCfgDataLANFCSInd_Object=MibTableColumn
zxGponMACBriPortCfgDataLANFCSInd=_ZxGponMACBriPortCfgDataLANFCSInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,10),_ZxGponMACBriPortCfgDataLANFCSInd_Type())
zxGponMACBriPortCfgDataLANFCSInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataLANFCSInd.setStatus(_A)
class _ZxGponMACBriPortCfgDataMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponMACBriPortCfgDataMgmtCtrlFlag_Type.__name__=_E
_ZxGponMACBriPortCfgDataMgmtCtrlFlag_Object=MibTableColumn
zxGponMACBriPortCfgDataMgmtCtrlFlag=_ZxGponMACBriPortCfgDataMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,11),_ZxGponMACBriPortCfgDataMgmtCtrlFlag_Type())
zxGponMACBriPortCfgDataMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataMgmtCtrlFlag.setStatus(_A)
_ZxGponMACBriPortCfgDataEntryStatus_Type=RowStatus
_ZxGponMACBriPortCfgDataEntryStatus_Object=MibTableColumn
zxGponMACBriPortCfgDataEntryStatus=_ZxGponMACBriPortCfgDataEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,23,8,4,1,12),_ZxGponMACBriPortCfgDataEntryStatus_Type())
zxGponMACBriPortCfgDataEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataEntryStatus.setStatus(_A)
_ZxGponMACBriPortFilterTableInfoTable_Object=MibTable
zxGponMACBriPortFilterTableInfoTable=_ZxGponMACBriPortFilterTableInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,8,5))
if mibBuilder.loadTexts:zxGponMACBriPortFilterTableInfoTable.setStatus(_A)
_ZxGponMACBriPortFilterTableInfoEntry_Object=MibTableRow
zxGponMACBriPortFilterTableInfoEntry=_ZxGponMACBriPortFilterTableInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,8,5,1))
zxGponMACBriPortFilterTableInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_j),(0,_B,_Ae))
if mibBuilder.loadTexts:zxGponMACBriPortFilterTableInfoEntry.setStatus(_A)
_ZxGponMACBriPortFilterTableMacAddr_Type=MacAddress
_ZxGponMACBriPortFilterTableMacAddr_Object=MibTableColumn
zxGponMACBriPortFilterTableMacAddr=_ZxGponMACBriPortFilterTableMacAddr_Object((1,3,6,1,4,1,3902,1012,3,23,8,5,1,1),_ZxGponMACBriPortFilterTableMacAddr_Type())
zxGponMACBriPortFilterTableMacAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponMACBriPortFilterTableMacAddr.setStatus(_A)
class _ZxGponMACBriPortFilterTableAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_k,2)))
_ZxGponMACBriPortFilterTableAction_Type.__name__=_E
_ZxGponMACBriPortFilterTableAction_Object=MibTableColumn
zxGponMACBriPortFilterTableAction=_ZxGponMACBriPortFilterTableAction_Object((1,3,6,1,4,1,3902,1012,3,23,8,5,1,2),_ZxGponMACBriPortFilterTableAction_Type())
zxGponMACBriPortFilterTableAction.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortFilterTableAction.setStatus(_A)
_ZxGponMACBriPortFilterTableEntryStatus_Type=RowStatus
_ZxGponMACBriPortFilterTableEntryStatus_Object=MibTableColumn
zxGponMACBriPortFilterTableEntryStatus=_ZxGponMACBriPortFilterTableEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,23,8,5,1,3),_ZxGponMACBriPortFilterTableEntryStatus_Type())
zxGponMACBriPortFilterTableEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponMACBriPortFilterTableEntryStatus.setStatus(_A)
_ZxGponMACBriPortDesignationDataTable_Object=MibTable
zxGponMACBriPortDesignationDataTable=_ZxGponMACBriPortDesignationDataTable_Object((1,3,6,1,4,1,3902,1012,3,23,8,6))
if mibBuilder.loadTexts:zxGponMACBriPortDesignationDataTable.setStatus(_A)
_ZxGponMACBriPortDesignationDataEntry_Object=MibTableRow
zxGponMACBriPortDesignationDataEntry=_ZxGponMACBriPortDesignationDataEntry_Object((1,3,6,1,4,1,3902,1012,3,23,8,6,1))
zxGponMACBriPortDesignationDataEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_h))
if mibBuilder.loadTexts:zxGponMACBriPortDesignationDataEntry.setStatus(_A)
class _ZxGponMACBriPortDesignationDataRootCostPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_ZxGponMACBriPortDesignationDataRootCostPort_Type.__name__=_O
_ZxGponMACBriPortDesignationDataRootCostPort_Object=MibTableColumn
zxGponMACBriPortDesignationDataRootCostPort=_ZxGponMACBriPortDesignationDataRootCostPort_Object((1,3,6,1,4,1,3902,1012,3,23,8,6,1,1),_ZxGponMACBriPortDesignationDataRootCostPort_Type())
zxGponMACBriPortDesignationDataRootCostPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortDesignationDataRootCostPort.setStatus(_A)
_ZxGponMACBriPortDesignationDataPortState_Type=Integer32
_ZxGponMACBriPortDesignationDataPortState_Object=MibTableColumn
zxGponMACBriPortDesignationDataPortState=_ZxGponMACBriPortDesignationDataPortState_Object((1,3,6,1,4,1,3902,1012,3,23,8,6,1,2),_ZxGponMACBriPortDesignationDataPortState_Type())
zxGponMACBriPortDesignationDataPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortDesignationDataPortState.setStatus(_A)
_ZxGponMACBriPortAddrInfoTable_Object=MibTable
zxGponMACBriPortAddrInfoTable=_ZxGponMACBriPortAddrInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,8,7))
if mibBuilder.loadTexts:zxGponMACBriPortAddrInfoTable.setStatus(_A)
_ZxGponMACBriPortAddrInfoEntry_Object=MibTableRow
zxGponMACBriPortAddrInfoEntry=_ZxGponMACBriPortAddrInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,8,7,1))
zxGponMACBriPortAddrInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_j),(0,_B,_Af))
if mibBuilder.loadTexts:zxGponMACBriPortAddrInfoEntry.setStatus(_A)
_ZxGponMACBriPortAddrMacAddr_Type=MacAddress
_ZxGponMACBriPortAddrMacAddr_Object=MibTableColumn
zxGponMACBriPortAddrMacAddr=_ZxGponMACBriPortAddrMacAddr_Object((1,3,6,1,4,1,3902,1012,3,23,8,7,1,1),_ZxGponMACBriPortAddrMacAddr_Type())
zxGponMACBriPortAddrMacAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponMACBriPortAddrMacAddr.setStatus(_A)
class _ZxGponMACBriPortAddrAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_k,2)))
_ZxGponMACBriPortAddrAction_Type.__name__=_E
_ZxGponMACBriPortAddrAction_Object=MibTableColumn
zxGponMACBriPortAddrAction=_ZxGponMACBriPortAddrAction_Object((1,3,6,1,4,1,3902,1012,3,23,8,7,1,2),_ZxGponMACBriPortAddrAction_Type())
zxGponMACBriPortAddrAction.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortAddrAction.setStatus(_A)
class _ZxGponMACBriPortAddrDynStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_ZxGponMACBriPortAddrDynStatic_Type.__name__=_E
_ZxGponMACBriPortAddrDynStatic_Object=MibTableColumn
zxGponMACBriPortAddrDynStatic=_ZxGponMACBriPortAddrDynStatic_Object((1,3,6,1,4,1,3902,1012,3,23,8,7,1,3),_ZxGponMACBriPortAddrDynStatic_Type())
zxGponMACBriPortAddrDynStatic.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortAddrDynStatic.setStatus(_A)
_ZxGponMACBriPortAddrAgingTime_Type=Integer32
_ZxGponMACBriPortAddrAgingTime_Object=MibTableColumn
zxGponMACBriPortAddrAgingTime=_ZxGponMACBriPortAddrAgingTime_Object((1,3,6,1,4,1,3902,1012,3,23,8,7,1,4),_ZxGponMACBriPortAddrAgingTime_Type())
zxGponMACBriPortAddrAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortAddrAgingTime.setStatus(_A)
_ZxGponIpRouterSPInfoTable_Object=MibTable
zxGponIpRouterSPInfoTable=_ZxGponIpRouterSPInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,8,8))
if mibBuilder.loadTexts:zxGponIpRouterSPInfoTable.setStatus(_A)
_ZxGponIpRouterSPInfoEntry_Object=MibTableRow
zxGponIpRouterSPInfoEntry=_ZxGponIpRouterSPInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,8,8,1))
zxGponIpRouterSPInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Ag))
if mibBuilder.loadTexts:zxGponIpRouterSPInfoEntry.setStatus(_A)
_ZxGponIpRouterSPInfoMeIdIdx_Type=Integer32
_ZxGponIpRouterSPInfoMeIdIdx_Object=MibTableColumn
zxGponIpRouterSPInfoMeIdIdx=_ZxGponIpRouterSPInfoMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,23,8,8,1,1),_ZxGponIpRouterSPInfoMeIdIdx_Type())
zxGponIpRouterSPInfoMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponIpRouterSPInfoMeIdIdx.setStatus(_A)
_ZxGponIpRouterSPInfoForwardingInd_Type=TruthValue
_ZxGponIpRouterSPInfoForwardingInd_Object=MibTableColumn
zxGponIpRouterSPInfoForwardingInd=_ZxGponIpRouterSPInfoForwardingInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,8,1,2),_ZxGponIpRouterSPInfoForwardingInd_Type())
zxGponIpRouterSPInfoForwardingInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpRouterSPInfoForwardingInd.setStatus(_A)
_ZxGponIpRouterSPInfoProxyARPInd_Type=TruthValue
_ZxGponIpRouterSPInfoProxyARPInd_Object=MibTableColumn
zxGponIpRouterSPInfoProxyARPInd=_ZxGponIpRouterSPInfoProxyARPInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,8,1,3),_ZxGponIpRouterSPInfoProxyARPInd_Type())
zxGponIpRouterSPInfoProxyARPInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpRouterSPInfoProxyARPInd.setStatus(_A)
_ZxGponIpRouterSPInfoDirectedBroadcastInd_Type=TruthValue
_ZxGponIpRouterSPInfoDirectedBroadcastInd_Object=MibTableColumn
zxGponIpRouterSPInfoDirectedBroadcastInd=_ZxGponIpRouterSPInfoDirectedBroadcastInd_Object((1,3,6,1,4,1,3902,1012,3,23,8,8,1,4),_ZxGponIpRouterSPInfoDirectedBroadcastInd_Type())
zxGponIpRouterSPInfoDirectedBroadcastInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpRouterSPInfoDirectedBroadcastInd.setStatus(_A)
class _ZxGponIpRouterSPInfoUpstreamMulticastFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Ah,1),('filtered',2)))
_ZxGponIpRouterSPInfoUpstreamMulticastFiltering_Type.__name__=_E
_ZxGponIpRouterSPInfoUpstreamMulticastFiltering_Object=MibTableColumn
zxGponIpRouterSPInfoUpstreamMulticastFiltering=_ZxGponIpRouterSPInfoUpstreamMulticastFiltering_Object((1,3,6,1,4,1,3902,1012,3,23,8,8,1,5),_ZxGponIpRouterSPInfoUpstreamMulticastFiltering_Type())
zxGponIpRouterSPInfoUpstreamMulticastFiltering.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpRouterSPInfoUpstreamMulticastFiltering.setStatus(_A)
class _ZxGponIpRouterSPInfoDownstreamMulticastFiltering_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Ah,1),('filtered',2)))
_ZxGponIpRouterSPInfoDownstreamMulticastFiltering_Type.__name__=_E
_ZxGponIpRouterSPInfoDownstreamMulticastFiltering_Object=MibTableColumn
zxGponIpRouterSPInfoDownstreamMulticastFiltering=_ZxGponIpRouterSPInfoDownstreamMulticastFiltering_Object((1,3,6,1,4,1,3902,1012,3,23,8,8,1,6),_ZxGponIpRouterSPInfoDownstreamMulticastFiltering_Type())
zxGponIpRouterSPInfoDownstreamMulticastFiltering.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpRouterSPInfoDownstreamMulticastFiltering.setStatus(_A)
class _ZxGponIpRouterSPInfoMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponIpRouterSPInfoMgmtCtrlFlag_Type.__name__=_E
_ZxGponIpRouterSPInfoMgmtCtrlFlag_Object=MibTableColumn
zxGponIpRouterSPInfoMgmtCtrlFlag=_ZxGponIpRouterSPInfoMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,23,8,8,1,7),_ZxGponIpRouterSPInfoMgmtCtrlFlag_Type())
zxGponIpRouterSPInfoMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponIpRouterSPInfoMgmtCtrlFlag.setStatus(_A)
_ZxGponIpRouterSPInfoEntryStatus_Type=RowStatus
_ZxGponIpRouterSPInfoEntryStatus_Object=MibTableColumn
zxGponIpRouterSPInfoEntryStatus=_ZxGponIpRouterSPInfoEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,23,8,8,1,8),_ZxGponIpRouterSPInfoEntryStatus_Type())
zxGponIpRouterSPInfoEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponIpRouterSPInfoEntryStatus.setStatus(_A)
_ZxGponIpPortCfgDataInfoTable_Object=MibTable
zxGponIpPortCfgDataInfoTable=_ZxGponIpPortCfgDataInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,8,9))
if mibBuilder.loadTexts:zxGponIpPortCfgDataInfoTable.setStatus(_A)
_ZxGponIpPortCfgDataInfoEntry_Object=MibTableRow
zxGponIpPortCfgDataInfoEntry=_ZxGponIpPortCfgDataInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1))
zxGponIpPortCfgDataInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Ai))
if mibBuilder.loadTexts:zxGponIpPortCfgDataInfoEntry.setStatus(_A)
_ZxGponIpPortCfgDataMeIdIdx_Type=Integer32
_ZxGponIpPortCfgDataMeIdIdx_Object=MibTableColumn
zxGponIpPortCfgDataMeIdIdx=_ZxGponIpPortCfgDataMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,1),_ZxGponIpPortCfgDataMeIdIdx_Type())
zxGponIpPortCfgDataMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponIpPortCfgDataMeIdIdx.setStatus(_A)
_ZxGponIpPortCfgDataPortNum_Type=Integer32
_ZxGponIpPortCfgDataPortNum_Object=MibTableColumn
zxGponIpPortCfgDataPortNum=_ZxGponIpPortCfgDataPortNum_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,2),_ZxGponIpPortCfgDataPortNum_Type())
zxGponIpPortCfgDataPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataPortNum.setStatus(_A)
class _ZxGponIpPortCfgDataTPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_Z,2)))
_ZxGponIpPortCfgDataTPType_Type.__name__=_E
_ZxGponIpPortCfgDataTPType_Object=MibTableColumn
zxGponIpPortCfgDataTPType=_ZxGponIpPortCfgDataTPType_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,3),_ZxGponIpPortCfgDataTPType_Type())
zxGponIpPortCfgDataTPType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataTPType.setStatus(_A)
_ZxGponIpPortCfgDataTPPointer_Type=Integer32
_ZxGponIpPortCfgDataTPPointer_Object=MibTableColumn
zxGponIpPortCfgDataTPPointer=_ZxGponIpPortCfgDataTPPointer_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,4),_ZxGponIpPortCfgDataTPPointer_Type())
zxGponIpPortCfgDataTPPointer.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataTPPointer.setStatus(_A)
_ZxGponIpPortCfgDataPortAddress_Type=IpAddress
_ZxGponIpPortCfgDataPortAddress_Object=MibTableColumn
zxGponIpPortCfgDataPortAddress=_ZxGponIpPortCfgDataPortAddress_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,5),_ZxGponIpPortCfgDataPortAddress_Type())
zxGponIpPortCfgDataPortAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataPortAddress.setStatus(_A)
_ZxGponIpPortCfgDataPortMask_Type=IpAddress
_ZxGponIpPortCfgDataPortMask_Object=MibTableColumn
zxGponIpPortCfgDataPortMask=_ZxGponIpPortCfgDataPortMask_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,6),_ZxGponIpPortCfgDataPortMask_Type())
zxGponIpPortCfgDataPortMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataPortMask.setStatus(_A)
_ZxGponIpPortCfgDataUnnumbered_Type=TruthValue
_ZxGponIpPortCfgDataUnnumbered_Object=MibTableColumn
zxGponIpPortCfgDataUnnumbered=_ZxGponIpPortCfgDataUnnumbered_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,7),_ZxGponIpPortCfgDataUnnumbered_Type())
zxGponIpPortCfgDataUnnumbered.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataUnnumbered.setStatus(_A)
class _ZxGponIpPortCfgDataAdministrativeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),(_u,2)))
_ZxGponIpPortCfgDataAdministrativeState_Type.__name__=_E
_ZxGponIpPortCfgDataAdministrativeState_Object=MibTableColumn
zxGponIpPortCfgDataAdministrativeState=_ZxGponIpPortCfgDataAdministrativeState_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,8),_ZxGponIpPortCfgDataAdministrativeState_Type())
zxGponIpPortCfgDataAdministrativeState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataAdministrativeState.setStatus(_A)
class _ZxGponIpPortCfgDataPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_ZxGponIpPortCfgDataPortState_Type.__name__=_E
_ZxGponIpPortCfgDataPortState_Object=MibTableColumn
zxGponIpPortCfgDataPortState=_ZxGponIpPortCfgDataPortState_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,9),_ZxGponIpPortCfgDataPortState_Type())
zxGponIpPortCfgDataPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponIpPortCfgDataPortState.setStatus(_A)
_ZxGponIpPortCfgDataAllowRemoteAccess_Type=TruthValue
_ZxGponIpPortCfgDataAllowRemoteAccess_Object=MibTableColumn
zxGponIpPortCfgDataAllowRemoteAccess=_ZxGponIpPortCfgDataAllowRemoteAccess_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,10),_ZxGponIpPortCfgDataAllowRemoteAccess_Type())
zxGponIpPortCfgDataAllowRemoteAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataAllowRemoteAccess.setStatus(_A)
_ZxGponIpPortCfgDataRouterIdPointer_Type=Integer32
_ZxGponIpPortCfgDataRouterIdPointer_Object=MibTableColumn
zxGponIpPortCfgDataRouterIdPointer=_ZxGponIpPortCfgDataRouterIdPointer_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,11),_ZxGponIpPortCfgDataRouterIdPointer_Type())
zxGponIpPortCfgDataRouterIdPointer.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataRouterIdPointer.setStatus(_A)
_ZxGponIpPortCfgDataARPPointer_Type=Integer32
_ZxGponIpPortCfgDataARPPointer_Object=MibTableColumn
zxGponIpPortCfgDataARPPointer=_ZxGponIpPortCfgDataARPPointer_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,12),_ZxGponIpPortCfgDataARPPointer_Type())
zxGponIpPortCfgDataARPPointer.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataARPPointer.setStatus(_A)
class _ZxGponIpPortCfgDataEncapsulationMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_ZxGponIpPortCfgDataEncapsulationMethod_Type.__name__=_E
_ZxGponIpPortCfgDataEncapsulationMethod_Object=MibTableColumn
zxGponIpPortCfgDataEncapsulationMethod=_ZxGponIpPortCfgDataEncapsulationMethod_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,13),_ZxGponIpPortCfgDataEncapsulationMethod_Type())
zxGponIpPortCfgDataEncapsulationMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponIpPortCfgDataEncapsulationMethod.setStatus(_A)
class _ZxGponIpPortCfgDataMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponIpPortCfgDataMgmtCtrlFlag_Type.__name__=_E
_ZxGponIpPortCfgDataMgmtCtrlFlag_Object=MibTableColumn
zxGponIpPortCfgDataMgmtCtrlFlag=_ZxGponIpPortCfgDataMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,14),_ZxGponIpPortCfgDataMgmtCtrlFlag_Type())
zxGponIpPortCfgDataMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponIpPortCfgDataMgmtCtrlFlag.setStatus(_A)
_ZxGponIpPortCfgDataEntryStatus_Type=RowStatus
_ZxGponIpPortCfgDataEntryStatus_Object=MibTableColumn
zxGponIpPortCfgDataEntryStatus=_ZxGponIpPortCfgDataEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,23,8,9,1,15),_ZxGponIpPortCfgDataEntryStatus_Type())
zxGponIpPortCfgDataEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponIpPortCfgDataEntryStatus.setStatus(_A)
_CesUniMib_ObjectIdentity=ObjectIdentity
cesUniMib=_CesUniMib_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,23,9))
_ZxGponPPTPCesUniTable_Object=MibTable
zxGponPPTPCesUniTable=_ZxGponPPTPCesUniTable_Object((1,3,6,1,4,1,3902,1012,3,23,9,1))
if mibBuilder.loadTexts:zxGponPPTPCesUniTable.setStatus(_A)
_ZxGponPPTPCesUniEntry_Object=MibTableRow
zxGponPPTPCesUniEntry=_ZxGponPPTPCesUniEntry_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1))
zxGponPPTPCesUniEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Aj))
if mibBuilder.loadTexts:zxGponPPTPCesUniEntry.setStatus(_A)
_ZxGponPPTPCesUniTPID_Type=Integer32
_ZxGponPPTPCesUniTPID_Object=MibTableColumn
zxGponPPTPCesUniTPID=_ZxGponPPTPCesUniTPID_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,1),_ZxGponPPTPCesUniTPID_Type())
zxGponPPTPCesUniTPID.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponPPTPCesUniTPID.setStatus(_A)
_ZxGponPPTPCesUniMeId_Type=Integer32
_ZxGponPPTPCesUniMeId_Object=MibTableColumn
zxGponPPTPCesUniMeId=_ZxGponPPTPCesUniMeId_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,2),_ZxGponPPTPCesUniMeId_Type())
zxGponPPTPCesUniMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPPTPCesUniMeId.setStatus(_A)
class _ZxGponPPTPCesUniExpectedType_Type(Integer32):defaultValue=0
_ZxGponPPTPCesUniExpectedType_Type.__name__=_E
_ZxGponPPTPCesUniExpectedType_Object=MibTableColumn
zxGponPPTPCesUniExpectedType=_ZxGponPPTPCesUniExpectedType_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,3),_ZxGponPPTPCesUniExpectedType_Type())
zxGponPPTPCesUniExpectedType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPCesUniExpectedType.setStatus(_A)
_ZxGponPPTPCesUniSensedType_Type=Integer32
_ZxGponPPTPCesUniSensedType_Object=MibTableColumn
zxGponPPTPCesUniSensedType=_ZxGponPPTPCesUniSensedType_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,4),_ZxGponPPTPCesUniSensedType_Type())
zxGponPPTPCesUniSensedType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPPTPCesUniSensedType.setStatus(_A)
_ZxGponPPTPCesUniEesLoopback_Type=Integer32
_ZxGponPPTPCesUniEesLoopback_Object=MibTableColumn
zxGponPPTPCesUniEesLoopback=_ZxGponPPTPCesUniEesLoopback_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,5),_ZxGponPPTPCesUniEesLoopback_Type())
zxGponPPTPCesUniEesLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPCesUniEesLoopback.setStatus(_A)
class _ZxGponPPTPCesUniAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_ZxGponPPTPCesUniAdminState_Type.__name__=_E
_ZxGponPPTPCesUniAdminState_Object=MibTableColumn
zxGponPPTPCesUniAdminState=_ZxGponPPTPCesUniAdminState_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,6),_ZxGponPPTPCesUniAdminState_Type())
zxGponPPTPCesUniAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPCesUniAdminState.setStatus(_A)
class _ZxGponPPTPCesUniOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_ZxGponPPTPCesUniOperationalState_Type.__name__=_E
_ZxGponPPTPCesUniOperationalState_Object=MibTableColumn
zxGponPPTPCesUniOperationalState=_ZxGponPPTPCesUniOperationalState_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,7),_ZxGponPPTPCesUniOperationalState_Type())
zxGponPPTPCesUniOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPPTPCesUniOperationalState.setStatus(_A)
class _ZxGponPPTPCesUniDS1Framing_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('extendedSuperFrame',1),('superFrame',2),('unFrame',3),('g704',4),('jt-g704',5)))
_ZxGponPPTPCesUniDS1Framing_Type.__name__=_E
_ZxGponPPTPCesUniDS1Framing_Object=MibTableColumn
zxGponPPTPCesUniDS1Framing=_ZxGponPPTPCesUniDS1Framing_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,8),_ZxGponPPTPCesUniDS1Framing_Type())
zxGponPPTPCesUniDS1Framing.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPPTPCesUniDS1Framing.setStatus(_A)
class _ZxGponPPTPCesUniEncoding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('b8zs',1),('ami',2),('hdb3',3),('b3zs',4)))
_ZxGponPPTPCesUniEncoding_Type.__name__=_E
_ZxGponPPTPCesUniEncoding_Object=MibTableColumn
zxGponPPTPCesUniEncoding=_ZxGponPPTPCesUniEncoding_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,9),_ZxGponPPTPCesUniEncoding_Type())
zxGponPPTPCesUniEncoding.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPCesUniEncoding.setStatus(_A)
class _ZxGponPPTPCesUniLineLength_Type(Integer32):defaultValue=15
_ZxGponPPTPCesUniLineLength_Type.__name__=_E
_ZxGponPPTPCesUniLineLength_Object=MibTableColumn
zxGponPPTPCesUniLineLength=_ZxGponPPTPCesUniLineLength_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,10),_ZxGponPPTPCesUniLineLength_Type())
zxGponPPTPCesUniLineLength.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPCesUniLineLength.setStatus(_A)
class _ZxGponPPTPCesUniDS1Mode_Type(Integer32):defaultValue=0
_ZxGponPPTPCesUniDS1Mode_Type.__name__=_E
_ZxGponPPTPCesUniDS1Mode_Object=MibTableColumn
zxGponPPTPCesUniDS1Mode=_ZxGponPPTPCesUniDS1Mode_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,11),_ZxGponPPTPCesUniDS1Mode_Type())
zxGponPPTPCesUniDS1Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPCesUniDS1Mode.setStatus(_A)
class _ZxGponPPTPCesUniARC_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_ZxGponPPTPCesUniARC_Type.__name__=_E
_ZxGponPPTPCesUniARC_Object=MibTableColumn
zxGponPPTPCesUniARC=_ZxGponPPTPCesUniARC_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,12),_ZxGponPPTPCesUniARC_Type())
zxGponPPTPCesUniARC.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPCesUniARC.setStatus(_A)
class _ZxGponPPTPCesUniARCInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZxGponPPTPCesUniARCInterval_Type.__name__=_E
_ZxGponPPTPCesUniARCInterval_Object=MibTableColumn
zxGponPPTPCesUniARCInterval=_ZxGponPPTPCesUniARCInterval_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,13),_ZxGponPPTPCesUniARCInterval_Type())
zxGponPPTPCesUniARCInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPCesUniARCInterval.setStatus(_A)
_ZxGponPPTPCesUniLineType_Type=Integer32
_ZxGponPPTPCesUniLineType_Object=MibTableColumn
zxGponPPTPCesUniLineType=_ZxGponPPTPCesUniLineType_Object((1,3,6,1,4,1,3902,1012,3,23,9,1,1,14),_ZxGponPPTPCesUniLineType_Type())
zxGponPPTPCesUniLineType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPPTPCesUniLineType.setStatus(_A)
_ZxGponCESSPInfoTable_Object=MibTable
zxGponCESSPInfoTable=_ZxGponCESSPInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,9,2))
if mibBuilder.loadTexts:zxGponCESSPInfoTable.setStatus(_A)
_ZxGponCESSPInfoEntry_Object=MibTableRow
zxGponCESSPInfoEntry=_ZxGponCESSPInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,9,2,1))
zxGponCESSPInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Ak))
if mibBuilder.loadTexts:zxGponCESSPInfoEntry.setStatus(_A)
_ZxGponCESSPInfoMeIdIdx_Type=Integer32
_ZxGponCESSPInfoMeIdIdx_Object=MibTableColumn
zxGponCESSPInfoMeIdIdx=_ZxGponCESSPInfoMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,23,9,2,1,1),_ZxGponCESSPInfoMeIdIdx_Type())
zxGponCESSPInfoMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponCESSPInfoMeIdIdx.setStatus(_A)
_ZxGponCESSPInfoMBufferedCDVTolerance_Type=Integer32
_ZxGponCESSPInfoMBufferedCDVTolerance_Object=MibTableColumn
zxGponCESSPInfoMBufferedCDVTolerance=_ZxGponCESSPInfoMBufferedCDVTolerance_Object((1,3,6,1,4,1,3902,1012,3,23,9,2,1,2),_ZxGponCESSPInfoMBufferedCDVTolerance_Type())
zxGponCESSPInfoMBufferedCDVTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponCESSPInfoMBufferedCDVTolerance.setStatus(_A)
class _ZxGponCESSPInfoChannelAssociatedSignalling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('basic',1),('e1Cas',2),('sfCas',3),('ds1EsfCas',4),('j2Cas',5)))
_ZxGponCESSPInfoChannelAssociatedSignalling_Type.__name__=_E
_ZxGponCESSPInfoChannelAssociatedSignalling_Object=MibTableColumn
zxGponCESSPInfoChannelAssociatedSignalling=_ZxGponCESSPInfoChannelAssociatedSignalling_Object((1,3,6,1,4,1,3902,1012,3,23,9,2,1,3),_ZxGponCESSPInfoChannelAssociatedSignalling_Type())
zxGponCESSPInfoChannelAssociatedSignalling.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponCESSPInfoChannelAssociatedSignalling.setStatus(_A)
class _ZxGponCESSPInfoMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponCESSPInfoMgmtCtrlFlag_Type.__name__=_E
_ZxGponCESSPInfoMgmtCtrlFlag_Object=MibTableColumn
zxGponCESSPInfoMgmtCtrlFlag=_ZxGponCESSPInfoMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,23,9,2,1,4),_ZxGponCESSPInfoMgmtCtrlFlag_Type())
zxGponCESSPInfoMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponCESSPInfoMgmtCtrlFlag.setStatus(_A)
_ZxGponCESSPInfoEntryStatus_Type=RowStatus
_ZxGponCESSPInfoEntryStatus_Object=MibTableColumn
zxGponCESSPInfoEntryStatus=_ZxGponCESSPInfoEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,23,9,2,1,5),_ZxGponCESSPInfoEntryStatus_Type())
zxGponCESSPInfoEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponCESSPInfoEntryStatus.setStatus(_A)
_ZxGponGemIWTPInfoTable_Object=MibTable
zxGponGemIWTPInfoTable=_ZxGponGemIWTPInfoTable_Object((1,3,6,1,4,1,3902,1012,3,23,12))
if mibBuilder.loadTexts:zxGponGemIWTPInfoTable.setStatus(_A)
_ZxGponGemIWTPInfoEntry_Object=MibTableRow
zxGponGemIWTPInfoEntry=_ZxGponGemIWTPInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,23,12,1))
zxGponGemIWTPInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Al))
if mibBuilder.loadTexts:zxGponGemIWTPInfoEntry.setStatus(_A)
_ZxGponGemIWTPInfoMeIdIdx_Type=Integer32
_ZxGponGemIWTPInfoMeIdIdx_Object=MibTableColumn
zxGponGemIWTPInfoMeIdIdx=_ZxGponGemIWTPInfoMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,1),_ZxGponGemIWTPInfoMeIdIdx_Type())
zxGponGemIWTPInfoMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponGemIWTPInfoMeIdIdx.setStatus(_A)
_ZxGponGemIWTPInfoPNCTPConnectivityPtr_Type=Integer32
_ZxGponGemIWTPInfoPNCTPConnectivityPtr_Object=MibTableColumn
zxGponGemIWTPInfoPNCTPConnectivityPtr=_ZxGponGemIWTPInfoPNCTPConnectivityPtr_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,2),_ZxGponGemIWTPInfoPNCTPConnectivityPtr_Type())
zxGponGemIWTPInfoPNCTPConnectivityPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemIWTPInfoPNCTPConnectivityPtr.setStatus(_A)
class _ZxGponGemIWTPInfoIwOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ces',1),('bridge',2)))
_ZxGponGemIWTPInfoIwOption_Type.__name__=_E
_ZxGponGemIWTPInfoIwOption_Object=MibTableColumn
zxGponGemIWTPInfoIwOption=_ZxGponGemIWTPInfoIwOption_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,3),_ZxGponGemIWTPInfoIwOption_Type())
zxGponGemIWTPInfoIwOption.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemIWTPInfoIwOption.setStatus(_A)
_ZxGponGemIWTPInfoServiceProPtr_Type=Integer32
_ZxGponGemIWTPInfoServiceProPtr_Object=MibTableColumn
zxGponGemIWTPInfoServiceProPtr=_ZxGponGemIWTPInfoServiceProPtr_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,4),_ZxGponGemIWTPInfoServiceProPtr_Type())
zxGponGemIWTPInfoServiceProPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemIWTPInfoServiceProPtr.setStatus(_A)
_ZxGponGemIWTPInfoITPPtr_Type=Integer32
_ZxGponGemIWTPInfoITPPtr_Object=MibTableColumn
zxGponGemIWTPInfoITPPtr=_ZxGponGemIWTPInfoITPPtr_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,5),_ZxGponGemIWTPInfoITPPtr_Type())
zxGponGemIWTPInfoITPPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemIWTPInfoITPPtr.setStatus(_A)
_ZxGponGemIWTPInfoPPTPCounter_Type=Integer32
_ZxGponGemIWTPInfoPPTPCounter_Object=MibTableColumn
zxGponGemIWTPInfoPPTPCounter=_ZxGponGemIWTPInfoPPTPCounter_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,6),_ZxGponGemIWTPInfoPPTPCounter_Type())
zxGponGemIWTPInfoPPTPCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemIWTPInfoPPTPCounter.setStatus(_A)
class _ZxGponGemIWTPInfoOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_ZxGponGemIWTPInfoOpState_Type.__name__=_E
_ZxGponGemIWTPInfoOpState_Object=MibTableColumn
zxGponGemIWTPInfoOpState=_ZxGponGemIWTPInfoOpState_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,7),_ZxGponGemIWTPInfoOpState_Type())
zxGponGemIWTPInfoOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemIWTPInfoOpState.setStatus(_A)
_ZxGponGemIWTPInfoGALProPtr_Type=Integer32
_ZxGponGemIWTPInfoGALProPtr_Object=MibTableColumn
zxGponGemIWTPInfoGALProPtr=_ZxGponGemIWTPInfoGALProPtr_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,8),_ZxGponGemIWTPInfoGALProPtr_Type())
zxGponGemIWTPInfoGALProPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemIWTPInfoGALProPtr.setStatus(_A)
class _ZxGponGemIWTPInfoGEMLoopbackCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('loopback',2)))
_ZxGponGemIWTPInfoGEMLoopbackCfg_Type.__name__=_E
_ZxGponGemIWTPInfoGEMLoopbackCfg_Object=MibTableColumn
zxGponGemIWTPInfoGEMLoopbackCfg=_ZxGponGemIWTPInfoGEMLoopbackCfg_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,9),_ZxGponGemIWTPInfoGEMLoopbackCfg_Type())
zxGponGemIWTPInfoGEMLoopbackCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemIWTPInfoGEMLoopbackCfg.setStatus(_A)
class _ZxGponGemIWTPInfoMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponGemIWTPInfoMgmtCtrlFlag_Type.__name__=_E
_ZxGponGemIWTPInfoMgmtCtrlFlag_Object=MibTableColumn
zxGponGemIWTPInfoMgmtCtrlFlag=_ZxGponGemIWTPInfoMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,10),_ZxGponGemIWTPInfoMgmtCtrlFlag_Type())
zxGponGemIWTPInfoMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemIWTPInfoMgmtCtrlFlag.setStatus(_A)
_ZxGponGemIWTPInfoEntryStatus_Type=RowStatus
_ZxGponGemIWTPInfoEntryStatus_Object=MibTableColumn
zxGponGemIWTPInfoEntryStatus=_ZxGponGemIWTPInfoEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,23,12,1,11),_ZxGponGemIWTPInfoEntryStatus_Type())
zxGponGemIWTPInfoEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponGemIWTPInfoEntryStatus.setStatus(_A)
_ZxGponGemIWTPAlarmTable_Object=MibTable
zxGponGemIWTPAlarmTable=_ZxGponGemIWTPAlarmTable_Object((1,3,6,1,4,1,3902,1012,3,23,13))
if mibBuilder.loadTexts:zxGponGemIWTPAlarmTable.setStatus(_A)
_ZxGponGemIWTPAlarmEntry_Object=MibTableRow
zxGponGemIWTPAlarmEntry=_ZxGponGemIWTPAlarmEntry_Object((1,3,6,1,4,1,3902,1012,3,23,13,1))
zxGponGemIWTPAlarmEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Am))
if mibBuilder.loadTexts:zxGponGemIWTPAlarmEntry.setStatus(_A)
_ZxGponGemIWTPAlarmIndex_Type=Integer32
_ZxGponGemIWTPAlarmIndex_Object=MibTableColumn
zxGponGemIWTPAlarmIndex=_ZxGponGemIWTPAlarmIndex_Object((1,3,6,1,4,1,3902,1012,3,23,13,1,1),_ZxGponGemIWTPAlarmIndex_Type())
zxGponGemIWTPAlarmIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponGemIWTPAlarmIndex.setStatus(_A)
_ZxGponGemIWTPAlarmMeId_Type=Integer32
_ZxGponGemIWTPAlarmMeId_Object=MibTableColumn
zxGponGemIWTPAlarmMeId=_ZxGponGemIWTPAlarmMeId_Object((1,3,6,1,4,1,3902,1012,3,23,13,1,2),_ZxGponGemIWTPAlarmMeId_Type())
zxGponGemIWTPAlarmMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemIWTPAlarmMeId.setStatus(_A)
_ZxGponGemIWTPGFSAAlarm_Type=TruthValue
_ZxGponGemIWTPGFSAAlarm_Object=MibTableColumn
zxGponGemIWTPGFSAAlarm=_ZxGponGemIWTPGFSAAlarm_Object((1,3,6,1,4,1,3902,1012,3,23,13,1,3),_ZxGponGemIWTPGFSAAlarm_Type())
zxGponGemIWTPGFSAAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemIWTPGFSAAlarm.setStatus(_A)
_ZxGponGemIWTPGFSAAlarmMask_Type=TruthValue
_ZxGponGemIWTPGFSAAlarmMask_Object=MibTableColumn
zxGponGemIWTPGFSAAlarmMask=_ZxGponGemIWTPGFSAAlarmMask_Object((1,3,6,1,4,1,3902,1012,3,23,13,1,4),_ZxGponGemIWTPGFSAAlarmMask_Type())
zxGponGemIWTPGFSAAlarmMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemIWTPGFSAAlarmMask.setStatus(_A)
_ZxGponConnMgmt_ObjectIdentity=ObjectIdentity
zxGponConnMgmt=_ZxGponConnMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,24))
_ZxGponGemPNCTPInfoTable_Object=MibTable
zxGponGemPNCTPInfoTable=_ZxGponGemPNCTPInfoTable_Object((1,3,6,1,4,1,3902,1012,3,24,1))
if mibBuilder.loadTexts:zxGponGemPNCTPInfoTable.setStatus(_A)
_ZxGponGemPNCTPInfoEntry_Object=MibTableRow
zxGponGemPNCTPInfoEntry=_ZxGponGemPNCTPInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,24,1,1))
zxGponGemPNCTPInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_x))
if mibBuilder.loadTexts:zxGponGemPNCTPInfoEntry.setStatus(_A)
_ZxGponGemPNCTPInfoMeIdIdx_Type=Integer32
_ZxGponGemPNCTPInfoMeIdIdx_Object=MibTableColumn
zxGponGemPNCTPInfoMeIdIdx=_ZxGponGemPNCTPInfoMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,1),_ZxGponGemPNCTPInfoMeIdIdx_Type())
zxGponGemPNCTPInfoMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoMeIdIdx.setStatus(_A)
_ZxGponGemPNCTPInfoPortId_Type=Integer32
_ZxGponGemPNCTPInfoPortId_Object=MibTableColumn
zxGponGemPNCTPInfoPortId=_ZxGponGemPNCTPInfoPortId_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,2),_ZxGponGemPNCTPInfoPortId_Type())
zxGponGemPNCTPInfoPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoPortId.setStatus(_A)
_ZxGponGemPNCTPInfoPONTCAdapterGPtr_Type=Integer32
_ZxGponGemPNCTPInfoPONTCAdapterGPtr_Object=MibTableColumn
zxGponGemPNCTPInfoPONTCAdapterGPtr=_ZxGponGemPNCTPInfoPONTCAdapterGPtr_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,3),_ZxGponGemPNCTPInfoPONTCAdapterGPtr_Type())
zxGponGemPNCTPInfoPONTCAdapterGPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoPONTCAdapterGPtr.setStatus(_A)
class _ZxGponGemPNCTPInfoDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('uni2ani',1),('ani2uni',2),(_An,3)))
_ZxGponGemPNCTPInfoDirection_Type.__name__=_E
_ZxGponGemPNCTPInfoDirection_Object=MibTableColumn
zxGponGemPNCTPInfoDirection=_ZxGponGemPNCTPInfoDirection_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,4),_ZxGponGemPNCTPInfoDirection_Type())
zxGponGemPNCTPInfoDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoDirection.setStatus(_A)
_ZxGponGemPNCTPInfoPriorityUpstream_Type=Integer32
_ZxGponGemPNCTPInfoPriorityUpstream_Object=MibTableColumn
zxGponGemPNCTPInfoPriorityUpstream=_ZxGponGemPNCTPInfoPriorityUpstream_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,5),_ZxGponGemPNCTPInfoPriorityUpstream_Type())
zxGponGemPNCTPInfoPriorityUpstream.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoPriorityUpstream.setStatus(_A)
_ZxGponGemPNCTPInfoPriorityDownstream_Type=Integer32
_ZxGponGemPNCTPInfoPriorityDownstream_Object=MibTableColumn
zxGponGemPNCTPInfoPriorityDownstream=_ZxGponGemPNCTPInfoPriorityDownstream_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,6),_ZxGponGemPNCTPInfoPriorityDownstream_Type())
zxGponGemPNCTPInfoPriorityDownstream.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoPriorityDownstream.setStatus(_A)
_ZxGponGemPNCTPInfoTDescProfPtr_Type=Integer32
_ZxGponGemPNCTPInfoTDescProfPtr_Object=MibTableColumn
zxGponGemPNCTPInfoTDescProfPtr=_ZxGponGemPNCTPInfoTDescProfPtr_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,7),_ZxGponGemPNCTPInfoTDescProfPtr_Type())
zxGponGemPNCTPInfoTDescProfPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoTDescProfPtr.setStatus(_A)
_ZxGponGemPNCTPInfoUniCounter_Type=Integer32
_ZxGponGemPNCTPInfoUniCounter_Object=MibTableColumn
zxGponGemPNCTPInfoUniCounter=_ZxGponGemPNCTPInfoUniCounter_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,8),_ZxGponGemPNCTPInfoUniCounter_Type())
zxGponGemPNCTPInfoUniCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoUniCounter.setStatus(_A)
class _ZxGponGemPNCTPInfoMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponGemPNCTPInfoMgmtCtrlFlag_Type.__name__=_E
_ZxGponGemPNCTPInfoMgmtCtrlFlag_Object=MibTableColumn
zxGponGemPNCTPInfoMgmtCtrlFlag=_ZxGponGemPNCTPInfoMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,9),_ZxGponGemPNCTPInfoMgmtCtrlFlag_Type())
zxGponGemPNCTPInfoMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoMgmtCtrlFlag.setStatus(_A)
_ZxGponGemPNCTPInfoEntryStatus_Type=RowStatus
_ZxGponGemPNCTPInfoEntryStatus_Object=MibTableColumn
zxGponGemPNCTPInfoEntryStatus=_ZxGponGemPNCTPInfoEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,24,1,1,10),_ZxGponGemPNCTPInfoEntryStatus_Type())
zxGponGemPNCTPInfoEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponGemPNCTPInfoEntryStatus.setStatus(_A)
_ZxGponGemPNCTPAlarmCfgTable_Object=MibTable
zxGponGemPNCTPAlarmCfgTable=_ZxGponGemPNCTPAlarmCfgTable_Object((1,3,6,1,4,1,3902,1012,3,24,2))
if mibBuilder.loadTexts:zxGponGemPNCTPAlarmCfgTable.setStatus(_A)
_ZxGponGemPNCTPAlarmCfgEntry_Object=MibTableRow
zxGponGemPNCTPAlarmCfgEntry=_ZxGponGemPNCTPAlarmCfgEntry_Object((1,3,6,1,4,1,3902,1012,3,24,2,1))
zxGponGemPNCTPAlarmCfgEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_x))
if mibBuilder.loadTexts:zxGponGemPNCTPAlarmCfgEntry.setStatus(_A)
_ZxGponGemPNCTPAlarmCfgMeId_Type=Integer32
_ZxGponGemPNCTPAlarmCfgMeId_Object=MibTableColumn
zxGponGemPNCTPAlarmCfgMeId=_ZxGponGemPNCTPAlarmCfgMeId_Object((1,3,6,1,4,1,3902,1012,3,24,2,1,1),_ZxGponGemPNCTPAlarmCfgMeId_Type())
zxGponGemPNCTPAlarmCfgMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPNCTPAlarmCfgMeId.setStatus(_A)
_ZxGponGemPNCTPAlarmCfgE2eLossContinuity_Type=TruthValue
_ZxGponGemPNCTPAlarmCfgE2eLossContinuity_Object=MibTableColumn
zxGponGemPNCTPAlarmCfgE2eLossContinuity=_ZxGponGemPNCTPAlarmCfgE2eLossContinuity_Object((1,3,6,1,4,1,3902,1012,3,24,2,1,2),_ZxGponGemPNCTPAlarmCfgE2eLossContinuity_Type())
zxGponGemPNCTPAlarmCfgE2eLossContinuity.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPNCTPAlarmCfgE2eLossContinuity.setStatus(_A)
_ZxGponGemPNCTPAlarmCfgE2eLossContinuityMask_Type=TruthValue
_ZxGponGemPNCTPAlarmCfgE2eLossContinuityMask_Object=MibTableColumn
zxGponGemPNCTPAlarmCfgE2eLossContinuityMask=_ZxGponGemPNCTPAlarmCfgE2eLossContinuityMask_Object((1,3,6,1,4,1,3902,1012,3,24,2,1,3),_ZxGponGemPNCTPAlarmCfgE2eLossContinuityMask_Type())
zxGponGemPNCTPAlarmCfgE2eLossContinuityMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPNCTPAlarmCfgE2eLossContinuityMask.setStatus(_A)
_ZxGponGemPPPMHDInfoTable_Object=MibTable
zxGponGemPPPMHDInfoTable=_ZxGponGemPPPMHDInfoTable_Object((1,3,6,1,4,1,3902,1012,3,24,3))
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoTable.setStatus(_A)
_ZxGponGemPPPMHDInfoEntry_Object=MibTableRow
zxGponGemPPPMHDInfoEntry=_ZxGponGemPPPMHDInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,24,3,1))
zxGponGemPPPMHDInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_y))
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoEntry.setStatus(_A)
_ZxGponGemPPPMHDInfoMeIdIdx_Type=Integer32
_ZxGponGemPPPMHDInfoMeIdIdx_Object=MibTableColumn
zxGponGemPPPMHDInfoMeIdIdx=_ZxGponGemPPPMHDInfoMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,24,3,1,1),_ZxGponGemPPPMHDInfoMeIdIdx_Type())
zxGponGemPPPMHDInfoMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoMeIdIdx.setStatus(_A)
_ZxGponGemPPPMHDInfoIntervalEndTime_Type=Integer32
_ZxGponGemPPPMHDInfoIntervalEndTime_Object=MibTableColumn
zxGponGemPPPMHDInfoIntervalEndTime=_ZxGponGemPPPMHDInfoIntervalEndTime_Object((1,3,6,1,4,1,3902,1012,3,24,3,1,2),_ZxGponGemPPPMHDInfoIntervalEndTime_Type())
zxGponGemPPPMHDInfoIntervalEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoIntervalEndTime.setStatus(_A)
_ZxGponGemPPPMHDInfoThresholdDataID_Type=Integer32
_ZxGponGemPPPMHDInfoThresholdDataID_Object=MibTableColumn
zxGponGemPPPMHDInfoThresholdDataID=_ZxGponGemPPPMHDInfoThresholdDataID_Object((1,3,6,1,4,1,3902,1012,3,24,3,1,3),_ZxGponGemPPPMHDInfoThresholdDataID_Type())
zxGponGemPPPMHDInfoThresholdDataID.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoThresholdDataID.setStatus(_A)
_ZxGponGemPPPMHDInfoLostPackets_Type=Integer32
_ZxGponGemPPPMHDInfoLostPackets_Object=MibTableColumn
zxGponGemPPPMHDInfoLostPackets=_ZxGponGemPPPMHDInfoLostPackets_Object((1,3,6,1,4,1,3902,1012,3,24,3,1,4),_ZxGponGemPPPMHDInfoLostPackets_Type())
zxGponGemPPPMHDInfoLostPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoLostPackets.setStatus(_A)
_ZxGponGemPPPMHDInfoMisinsertedPackets_Type=Integer32
_ZxGponGemPPPMHDInfoMisinsertedPackets_Object=MibTableColumn
zxGponGemPPPMHDInfoMisinsertedPackets=_ZxGponGemPPPMHDInfoMisinsertedPackets_Object((1,3,6,1,4,1,3902,1012,3,24,3,1,5),_ZxGponGemPPPMHDInfoMisinsertedPackets_Type())
zxGponGemPPPMHDInfoMisinsertedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoMisinsertedPackets.setStatus(_A)
_ZxGponGemPPPMHDInfoReceivedPackets_Type=Integer32
_ZxGponGemPPPMHDInfoReceivedPackets_Object=MibTableColumn
zxGponGemPPPMHDInfoReceivedPackets=_ZxGponGemPPPMHDInfoReceivedPackets_Object((1,3,6,1,4,1,3902,1012,3,24,3,1,6),_ZxGponGemPPPMHDInfoReceivedPackets_Type())
zxGponGemPPPMHDInfoReceivedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoReceivedPackets.setStatus(_A)
_ZxGponGemPPPMHDInfoReceivedBlocks_Type=Integer32
_ZxGponGemPPPMHDInfoReceivedBlocks_Object=MibTableColumn
zxGponGemPPPMHDInfoReceivedBlocks=_ZxGponGemPPPMHDInfoReceivedBlocks_Object((1,3,6,1,4,1,3902,1012,3,24,3,1,7),_ZxGponGemPPPMHDInfoReceivedBlocks_Type())
zxGponGemPPPMHDInfoReceivedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoReceivedBlocks.setStatus(_A)
_ZxGponGemPPPMHDInfoTransmittedBlocks_Type=Integer32
_ZxGponGemPPPMHDInfoTransmittedBlocks_Object=MibTableColumn
zxGponGemPPPMHDInfoTransmittedBlocks=_ZxGponGemPPPMHDInfoTransmittedBlocks_Object((1,3,6,1,4,1,3902,1012,3,24,3,1,8),_ZxGponGemPPPMHDInfoTransmittedBlocks_Type())
zxGponGemPPPMHDInfoTransmittedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoTransmittedBlocks.setStatus(_A)
_ZxGponGemPPPMHDInfoImpairedBlocks_Type=Integer32
_ZxGponGemPPPMHDInfoImpairedBlocks_Object=MibTableColumn
zxGponGemPPPMHDInfoImpairedBlocks=_ZxGponGemPPPMHDInfoImpairedBlocks_Object((1,3,6,1,4,1,3902,1012,3,24,3,1,9),_ZxGponGemPPPMHDInfoImpairedBlocks_Type())
zxGponGemPPPMHDInfoImpairedBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDInfoImpairedBlocks.setStatus(_A)
_ZxGponGemPPPMHDAlarmCfgTable_Object=MibTable
zxGponGemPPPMHDAlarmCfgTable=_ZxGponGemPPPMHDAlarmCfgTable_Object((1,3,6,1,4,1,3902,1012,3,24,4))
if mibBuilder.loadTexts:zxGponGemPPPMHDAlarmCfgTable.setStatus(_A)
_ZxGponGemPPPMHDAlarmCfgEntry_Object=MibTableRow
zxGponGemPPPMHDAlarmCfgEntry=_ZxGponGemPPPMHDAlarmCfgEntry_Object((1,3,6,1,4,1,3902,1012,3,24,4,1))
zxGponGemPPPMHDAlarmCfgEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_y))
if mibBuilder.loadTexts:zxGponGemPPPMHDAlarmCfgEntry.setStatus(_A)
_ZxGponGemPPPMHDAlarmCfgMeId_Type=Integer32
_ZxGponGemPPPMHDAlarmCfgMeId_Object=MibTableColumn
zxGponGemPPPMHDAlarmCfgMeId=_ZxGponGemPPPMHDAlarmCfgMeId_Object((1,3,6,1,4,1,3902,1012,3,24,4,1,1),_ZxGponGemPPPMHDAlarmCfgMeId_Type())
zxGponGemPPPMHDAlarmCfgMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDAlarmCfgMeId.setStatus(_A)
_ZxGponGemPPPMHDAlarmCfgLosPkgs_Type=TruthValue
_ZxGponGemPPPMHDAlarmCfgLosPkgs_Object=MibTableColumn
zxGponGemPPPMHDAlarmCfgLosPkgs=_ZxGponGemPPPMHDAlarmCfgLosPkgs_Object((1,3,6,1,4,1,3902,1012,3,24,4,1,2),_ZxGponGemPPPMHDAlarmCfgLosPkgs_Type())
zxGponGemPPPMHDAlarmCfgLosPkgs.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDAlarmCfgLosPkgs.setStatus(_A)
_ZxGponGemPPPMHDAlarmCfgLosPkgsMask_Type=TruthValue
_ZxGponGemPPPMHDAlarmCfgLosPkgsMask_Object=MibTableColumn
zxGponGemPPPMHDAlarmCfgLosPkgsMask=_ZxGponGemPPPMHDAlarmCfgLosPkgsMask_Object((1,3,6,1,4,1,3902,1012,3,24,4,1,3),_ZxGponGemPPPMHDAlarmCfgLosPkgsMask_Type())
zxGponGemPPPMHDAlarmCfgLosPkgsMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPPPMHDAlarmCfgLosPkgsMask.setStatus(_A)
_ZxGponGemPPPMHDAlarmCfgMisInsertPkgs_Type=TruthValue
_ZxGponGemPPPMHDAlarmCfgMisInsertPkgs_Object=MibTableColumn
zxGponGemPPPMHDAlarmCfgMisInsertPkgs=_ZxGponGemPPPMHDAlarmCfgMisInsertPkgs_Object((1,3,6,1,4,1,3902,1012,3,24,4,1,4),_ZxGponGemPPPMHDAlarmCfgMisInsertPkgs_Type())
zxGponGemPPPMHDAlarmCfgMisInsertPkgs.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDAlarmCfgMisInsertPkgs.setStatus(_A)
_ZxGponGemPPPMHDAlarmCfgMisInsertPkgsMask_Type=TruthValue
_ZxGponGemPPPMHDAlarmCfgMisInsertPkgsMask_Object=MibTableColumn
zxGponGemPPPMHDAlarmCfgMisInsertPkgsMask=_ZxGponGemPPPMHDAlarmCfgMisInsertPkgsMask_Object((1,3,6,1,4,1,3902,1012,3,24,4,1,5),_ZxGponGemPPPMHDAlarmCfgMisInsertPkgsMask_Type())
zxGponGemPPPMHDAlarmCfgMisInsertPkgsMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPPPMHDAlarmCfgMisInsertPkgsMask.setStatus(_A)
_ZxGponGemPPPMHDAlarmCfgImpairBlks_Type=TruthValue
_ZxGponGemPPPMHDAlarmCfgImpairBlks_Object=MibTableColumn
zxGponGemPPPMHDAlarmCfgImpairBlks=_ZxGponGemPPPMHDAlarmCfgImpairBlks_Object((1,3,6,1,4,1,3902,1012,3,24,4,1,6),_ZxGponGemPPPMHDAlarmCfgImpairBlks_Type())
zxGponGemPPPMHDAlarmCfgImpairBlks.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPPPMHDAlarmCfgImpairBlks.setStatus(_A)
_ZxGponGemPPPMHDAlarmCfgImpairBlksMask_Type=TruthValue
_ZxGponGemPPPMHDAlarmCfgImpairBlksMask_Object=MibTableColumn
zxGponGemPPPMHDAlarmCfgImpairBlksMask=_ZxGponGemPPPMHDAlarmCfgImpairBlksMask_Object((1,3,6,1,4,1,3902,1012,3,24,4,1,7),_ZxGponGemPPPMHDAlarmCfgImpairBlksMask_Type())
zxGponGemPPPMHDAlarmCfgImpairBlksMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPPPMHDAlarmCfgImpairBlksMask.setStatus(_A)
_ZxGponTrafficMgmt_ObjectIdentity=ObjectIdentity
zxGponTrafficMgmt=_ZxGponTrafficMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,25))
_ZxGponPriorityQueueTable_Object=MibTable
zxGponPriorityQueueTable=_ZxGponPriorityQueueTable_Object((1,3,6,1,4,1,3902,1012,3,25,1))
if mibBuilder.loadTexts:zxGponPriorityQueueTable.setStatus(_A)
_ZxGponPriorityQueueEntry_Object=MibTableRow
zxGponPriorityQueueEntry=_ZxGponPriorityQueueEntry_Object((1,3,6,1,4,1,3902,1012,3,25,1,1))
zxGponPriorityQueueEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Ao))
if mibBuilder.loadTexts:zxGponPriorityQueueEntry.setStatus(_A)
_ZxGponPriorQueueIndex_Type=Integer32
_ZxGponPriorQueueIndex_Object=MibTableColumn
zxGponPriorQueueIndex=_ZxGponPriorQueueIndex_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,1),_ZxGponPriorQueueIndex_Type())
zxGponPriorQueueIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponPriorQueueIndex.setStatus(_A)
_ZxGponPriorQueueMeId_Type=Integer32
_ZxGponPriorQueueMeId_Object=MibTableColumn
zxGponPriorQueueMeId=_ZxGponPriorQueueMeId_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,2),_ZxGponPriorQueueMeId_Type())
zxGponPriorQueueMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPriorQueueMeId.setStatus(_A)
_ZxGponPriorQueueCfgOption_Type=Integer32
_ZxGponPriorQueueCfgOption_Object=MibTableColumn
zxGponPriorQueueCfgOption=_ZxGponPriorQueueCfgOption_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,3),_ZxGponPriorQueueCfgOption_Type())
zxGponPriorQueueCfgOption.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPriorQueueCfgOption.setStatus(_A)
_ZxGponPriorQueueMaxQueueSize_Type=Integer32
_ZxGponPriorQueueMaxQueueSize_Object=MibTableColumn
zxGponPriorQueueMaxQueueSize=_ZxGponPriorQueueMaxQueueSize_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,4),_ZxGponPriorQueueMaxQueueSize_Type())
zxGponPriorQueueMaxQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPriorQueueMaxQueueSize.setStatus(_A)
class _ZxGponPriorQueueAllocSize_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxGponPriorQueueAllocSize_Type.__name__=_E
_ZxGponPriorQueueAllocSize_Object=MibTableColumn
zxGponPriorQueueAllocSize=_ZxGponPriorQueueAllocSize_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,5),_ZxGponPriorQueueAllocSize_Type())
zxGponPriorQueueAllocSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueAllocSize.setStatus(_A)
class _ZxGponPriorQueueInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxGponPriorQueueInterval_Type.__name__=_E
_ZxGponPriorQueueInterval_Object=MibTableColumn
zxGponPriorQueueInterval=_ZxGponPriorQueueInterval_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,6),_ZxGponPriorQueueInterval_Type())
zxGponPriorQueueInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueInterval.setStatus(_A)
class _ZxGponPriorQueueBufOverflowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxGponPriorQueueBufOverflowThreshold_Type.__name__=_E
_ZxGponPriorQueueBufOverflowThreshold_Object=MibTableColumn
zxGponPriorQueueBufOverflowThreshold=_ZxGponPriorQueueBufOverflowThreshold_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,7),_ZxGponPriorQueueBufOverflowThreshold_Type())
zxGponPriorQueueBufOverflowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueBufOverflowThreshold.setStatus(_A)
_ZxGponPriorQueueRelatedPort_Type=Integer32
_ZxGponPriorQueueRelatedPort_Object=MibTableColumn
zxGponPriorQueueRelatedPort=_ZxGponPriorQueueRelatedPort_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,8),_ZxGponPriorQueueRelatedPort_Type())
zxGponPriorQueueRelatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPriorQueueRelatedPort.setStatus(_A)
_ZxGponPriorQueueTrafficSchedulerGPtr_Type=Integer32
_ZxGponPriorQueueTrafficSchedulerGPtr_Object=MibTableColumn
zxGponPriorQueueTrafficSchedulerGPtr=_ZxGponPriorQueueTrafficSchedulerGPtr_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,9),_ZxGponPriorQueueTrafficSchedulerGPtr_Type())
zxGponPriorQueueTrafficSchedulerGPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueTrafficSchedulerGPtr.setStatus(_A)
class _ZxGponPriorQueueWeight_Type(Integer32):defaultValue=1
_ZxGponPriorQueueWeight_Type.__name__=_E
_ZxGponPriorQueueWeight_Object=MibTableColumn
zxGponPriorQueueWeight=_ZxGponPriorQueueWeight_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,10),_ZxGponPriorQueueWeight_Type())
zxGponPriorQueueWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueWeight.setStatus(_A)
class _ZxGponPriorQueueBackPressureAdmin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponPriorQueueBackPressureAdmin_Type.__name__=_E
_ZxGponPriorQueueBackPressureAdmin_Object=MibTableColumn
zxGponPriorQueueBackPressureAdmin=_ZxGponPriorQueueBackPressureAdmin_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,11),_ZxGponPriorQueueBackPressureAdmin_Type())
zxGponPriorQueueBackPressureAdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueBackPressureAdmin.setStatus(_A)
class _ZxGponPriorQueueBackPressureTime_Type(Unsigned32):defaultValue=0
_ZxGponPriorQueueBackPressureTime_Type.__name__=_A2
_ZxGponPriorQueueBackPressureTime_Object=MibTableColumn
zxGponPriorQueueBackPressureTime=_ZxGponPriorQueueBackPressureTime_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,12),_ZxGponPriorQueueBackPressureTime_Type())
zxGponPriorQueueBackPressureTime.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueBackPressureTime.setStatus(_A)
_ZxGponPriorQueueBackPressAssertThresh_Type=Integer32
_ZxGponPriorQueueBackPressAssertThresh_Object=MibTableColumn
zxGponPriorQueueBackPressAssertThresh=_ZxGponPriorQueueBackPressAssertThresh_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,13),_ZxGponPriorQueueBackPressAssertThresh_Type())
zxGponPriorQueueBackPressAssertThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueBackPressAssertThresh.setStatus(_A)
_ZxGponPriorQueueBackPressClearThresh_Type=Integer32
_ZxGponPriorQueueBackPressClearThresh_Object=MibTableColumn
zxGponPriorQueueBackPressClearThresh=_ZxGponPriorQueueBackPressClearThresh_Object((1,3,6,1,4,1,3902,1012,3,25,1,1,14),_ZxGponPriorQueueBackPressClearThresh_Type())
zxGponPriorQueueBackPressClearThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueBackPressClearThresh.setStatus(_A)
_ZxGponPriorityQueueAlarmCfgTable_Object=MibTable
zxGponPriorityQueueAlarmCfgTable=_ZxGponPriorityQueueAlarmCfgTable_Object((1,3,6,1,4,1,3902,1012,3,25,2))
if mibBuilder.loadTexts:zxGponPriorityQueueAlarmCfgTable.setStatus(_A)
_ZxGponPriorityQueueAlarmCfgEntry_Object=MibTableRow
zxGponPriorityQueueAlarmCfgEntry=_ZxGponPriorityQueueAlarmCfgEntry_Object((1,3,6,1,4,1,3902,1012,3,25,2,1))
zxGponPriorityQueueAlarmCfgEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Ap))
if mibBuilder.loadTexts:zxGponPriorityQueueAlarmCfgEntry.setStatus(_A)
_ZxGponPriorQueueAlarmIndex_Type=Integer32
_ZxGponPriorQueueAlarmIndex_Object=MibTableColumn
zxGponPriorQueueAlarmIndex=_ZxGponPriorQueueAlarmIndex_Object((1,3,6,1,4,1,3902,1012,3,25,2,1,1),_ZxGponPriorQueueAlarmIndex_Type())
zxGponPriorQueueAlarmIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponPriorQueueAlarmIndex.setStatus(_A)
_ZxGponPriorQueueAlarmMeId_Type=Integer32
_ZxGponPriorQueueAlarmMeId_Object=MibTableColumn
zxGponPriorQueueAlarmMeId=_ZxGponPriorQueueAlarmMeId_Object((1,3,6,1,4,1,3902,1012,3,25,2,1,2),_ZxGponPriorQueueAlarmMeId_Type())
zxGponPriorQueueAlarmMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPriorQueueAlarmMeId.setStatus(_A)
_ZxGponPriorQueueAlarmCellLosThresh_Type=TruthValue
_ZxGponPriorQueueAlarmCellLosThresh_Object=MibTableColumn
zxGponPriorQueueAlarmCellLosThresh=_ZxGponPriorQueueAlarmCellLosThresh_Object((1,3,6,1,4,1,3902,1012,3,25,2,1,3),_ZxGponPriorQueueAlarmCellLosThresh_Type())
zxGponPriorQueueAlarmCellLosThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponPriorQueueAlarmCellLosThresh.setStatus(_A)
_ZxGponPriorQueueAlarmCellLosThreshMask_Type=TruthValue
_ZxGponPriorQueueAlarmCellLosThreshMask_Object=MibTableColumn
zxGponPriorQueueAlarmCellLosThreshMask=_ZxGponPriorQueueAlarmCellLosThreshMask_Object((1,3,6,1,4,1,3902,1012,3,25,2,1,4),_ZxGponPriorQueueAlarmCellLosThreshMask_Type())
zxGponPriorQueueAlarmCellLosThreshMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPriorQueueAlarmCellLosThreshMask.setStatus(_A)
_ZxGponTrafficScheduleTable_Object=MibTable
zxGponTrafficScheduleTable=_ZxGponTrafficScheduleTable_Object((1,3,6,1,4,1,3902,1012,3,25,3))
if mibBuilder.loadTexts:zxGponTrafficScheduleTable.setStatus(_A)
_ZxGponTrafficScheduleEntry_Object=MibTableRow
zxGponTrafficScheduleEntry=_ZxGponTrafficScheduleEntry_Object((1,3,6,1,4,1,3902,1012,3,25,3,1))
zxGponTrafficScheduleEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Aq))
if mibBuilder.loadTexts:zxGponTrafficScheduleEntry.setStatus(_A)
_ZxGponTrafficScheduleIndex_Type=Integer32
_ZxGponTrafficScheduleIndex_Object=MibTableColumn
zxGponTrafficScheduleIndex=_ZxGponTrafficScheduleIndex_Object((1,3,6,1,4,1,3902,1012,3,25,3,1,1),_ZxGponTrafficScheduleIndex_Type())
zxGponTrafficScheduleIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponTrafficScheduleIndex.setStatus(_A)
_ZxGponTrafficScheduleMeId_Type=Integer32
_ZxGponTrafficScheduleMeId_Object=MibTableColumn
zxGponTrafficScheduleMeId=_ZxGponTrafficScheduleMeId_Object((1,3,6,1,4,1,3902,1012,3,25,3,1,2),_ZxGponTrafficScheduleMeId_Type())
zxGponTrafficScheduleMeId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTrafficScheduleMeId.setStatus(_A)
_ZxGponTrafficScheduleTCountPtr_Type=Integer32
_ZxGponTrafficScheduleTCountPtr_Object=MibTableColumn
zxGponTrafficScheduleTCountPtr=_ZxGponTrafficScheduleTCountPtr_Object((1,3,6,1,4,1,3902,1012,3,25,3,1,3),_ZxGponTrafficScheduleTCountPtr_Type())
zxGponTrafficScheduleTCountPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTrafficScheduleTCountPtr.setStatus(_A)
_ZxGponTrafficScheduleOtherPtr_Type=Integer32
_ZxGponTrafficScheduleOtherPtr_Object=MibTableColumn
zxGponTrafficScheduleOtherPtr=_ZxGponTrafficScheduleOtherPtr_Object((1,3,6,1,4,1,3902,1012,3,25,3,1,4),_ZxGponTrafficScheduleOtherPtr_Type())
zxGponTrafficScheduleOtherPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTrafficScheduleOtherPtr.setStatus(_A)
class _ZxGponTrafficSchedulePolicy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hol',1),(_g,2),('null',3)))
_ZxGponTrafficSchedulePolicy_Type.__name__=_E
_ZxGponTrafficSchedulePolicy_Object=MibTableColumn
zxGponTrafficSchedulePolicy=_ZxGponTrafficSchedulePolicy_Object((1,3,6,1,4,1,3902,1012,3,25,3,1,5),_ZxGponTrafficSchedulePolicy_Type())
zxGponTrafficSchedulePolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTrafficSchedulePolicy.setStatus(_A)
class _ZxGponTrafficSchedulePriWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxGponTrafficSchedulePriWeight_Type.__name__=_E
_ZxGponTrafficSchedulePriWeight_Object=MibTableColumn
zxGponTrafficSchedulePriWeight=_ZxGponTrafficSchedulePriWeight_Object((1,3,6,1,4,1,3902,1012,3,25,3,1,6),_ZxGponTrafficSchedulePriWeight_Type())
zxGponTrafficSchedulePriWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponTrafficSchedulePriWeight.setStatus(_A)
_ZxGponGemTrafficDescriptorsTable_Object=MibTable
zxGponGemTrafficDescriptorsTable=_ZxGponGemTrafficDescriptorsTable_Object((1,3,6,1,4,1,3902,1012,3,25,4))
if mibBuilder.loadTexts:zxGponGemTrafficDescriptorsTable.setStatus(_A)
_ZxGponGemTrafficDescriptorsEntry_Object=MibTableRow
zxGponGemTrafficDescriptorsEntry=_ZxGponGemTrafficDescriptorsEntry_Object((1,3,6,1,4,1,3902,1012,3,25,4,1))
zxGponGemTrafficDescriptorsEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Ar))
if mibBuilder.loadTexts:zxGponGemTrafficDescriptorsEntry.setStatus(_A)
_ZxGponGemTrafficDescriptorsMeIdIdx_Type=Integer32
_ZxGponGemTrafficDescriptorsMeIdIdx_Object=MibTableColumn
zxGponGemTrafficDescriptorsMeIdIdx=_ZxGponGemTrafficDescriptorsMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,25,4,1,1),_ZxGponGemTrafficDescriptorsMeIdIdx_Type())
zxGponGemTrafficDescriptorsMeIdIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponGemTrafficDescriptorsMeIdIdx.setStatus(_A)
_ZxGponGemTrafficDescriptorsSIR_Type=Integer32
_ZxGponGemTrafficDescriptorsSIR_Object=MibTableColumn
zxGponGemTrafficDescriptorsSIR=_ZxGponGemTrafficDescriptorsSIR_Object((1,3,6,1,4,1,3902,1012,3,25,4,1,2),_ZxGponGemTrafficDescriptorsSIR_Type())
zxGponGemTrafficDescriptorsSIR.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemTrafficDescriptorsSIR.setStatus(_A)
_ZxGponGemTrafficDescriptorsPIR_Type=Integer32
_ZxGponGemTrafficDescriptorsPIR_Object=MibTableColumn
zxGponGemTrafficDescriptorsPIR=_ZxGponGemTrafficDescriptorsPIR_Object((1,3,6,1,4,1,3902,1012,3,25,4,1,3),_ZxGponGemTrafficDescriptorsPIR_Type())
zxGponGemTrafficDescriptorsPIR.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemTrafficDescriptorsPIR.setStatus(_A)
class _ZxGponGemTrafficDescriptorsMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponGemTrafficDescriptorsMgmtCtrlFlag_Type.__name__=_E
_ZxGponGemTrafficDescriptorsMgmtCtrlFlag_Object=MibTableColumn
zxGponGemTrafficDescriptorsMgmtCtrlFlag=_ZxGponGemTrafficDescriptorsMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,25,4,1,4),_ZxGponGemTrafficDescriptorsMgmtCtrlFlag_Type())
zxGponGemTrafficDescriptorsMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemTrafficDescriptorsMgmtCtrlFlag.setStatus(_A)
_ZxGponGemTrafficDescriptorsEntryStatus_Type=RowStatus
_ZxGponGemTrafficDescriptorsEntryStatus_Object=MibTableColumn
zxGponGemTrafficDescriptorsEntryStatus=_ZxGponGemTrafficDescriptorsEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,25,4,1,5),_ZxGponGemTrafficDescriptorsEntryStatus_Type())
zxGponGemTrafficDescriptorsEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponGemTrafficDescriptorsEntryStatus.setStatus(_A)
_ZxGponProfileMgmt_ObjectIdentity=ObjectIdentity
zxGponProfileMgmt=_ZxGponProfileMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,26))
_ZxGponBandwidthProfileTable_Object=MibTable
zxGponBandwidthProfileTable=_ZxGponBandwidthProfileTable_Object((1,3,6,1,4,1,3902,1012,3,26,1))
if mibBuilder.loadTexts:zxGponBandwidthProfileTable.setStatus(_A)
_ZxGponBandwidthProfileEntry_Object=MibTableRow
zxGponBandwidthProfileEntry=_ZxGponBandwidthProfileEntry_Object((1,3,6,1,4,1,3902,1012,3,26,1,1))
zxGponBandwidthProfileEntry.setIndexNames((0,_B,_As))
if mibBuilder.loadTexts:zxGponBandwidthProfileEntry.setStatus(_A)
_ZxGponBWProfileIndex_Type=Integer32
_ZxGponBWProfileIndex_Object=MibTableColumn
zxGponBWProfileIndex=_ZxGponBWProfileIndex_Object((1,3,6,1,4,1,3902,1012,3,26,1,1,1),_ZxGponBWProfileIndex_Type())
zxGponBWProfileIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponBWProfileIndex.setStatus(_A)
class _ZxGponBWProfileName_Type(ZxGponRecordName):subtypeSpec=ZxGponRecordName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxGponBWProfileName_Type.__name__=_X
_ZxGponBWProfileName_Object=MibTableColumn
zxGponBWProfileName=_ZxGponBWProfileName_Object((1,3,6,1,4,1,3902,1012,3,26,1,1,2),_ZxGponBWProfileName_Type())
zxGponBWProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBWProfileName.setStatus(_A)
_ZxGponBWProfileFixed_Type=Integer32
_ZxGponBWProfileFixed_Object=MibTableColumn
zxGponBWProfileFixed=_ZxGponBWProfileFixed_Object((1,3,6,1,4,1,3902,1012,3,26,1,1,3),_ZxGponBWProfileFixed_Type())
zxGponBWProfileFixed.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBWProfileFixed.setStatus(_A)
_ZxGponBWProfileAssured_Type=Integer32
_ZxGponBWProfileAssured_Object=MibTableColumn
zxGponBWProfileAssured=_ZxGponBWProfileAssured_Object((1,3,6,1,4,1,3902,1012,3,26,1,1,4),_ZxGponBWProfileAssured_Type())
zxGponBWProfileAssured.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBWProfileAssured.setStatus(_A)
_ZxGponBWProfileMaximum_Type=Integer32
_ZxGponBWProfileMaximum_Object=MibTableColumn
zxGponBWProfileMaximum=_ZxGponBWProfileMaximum_Object((1,3,6,1,4,1,3902,1012,3,26,1,1,5),_ZxGponBWProfileMaximum_Type())
zxGponBWProfileMaximum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBWProfileMaximum.setStatus(_A)
class _ZxGponBWProfileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('type1',1),('type2',2),('type3',3),('type4',4),('type5',5)))
_ZxGponBWProfileType_Type.__name__=_E
_ZxGponBWProfileType_Object=MibTableColumn
zxGponBWProfileType=_ZxGponBWProfileType_Object((1,3,6,1,4,1,3902,1012,3,26,1,1,6),_ZxGponBWProfileType_Type())
zxGponBWProfileType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBWProfileType.setStatus(_A)
_ZxGponBWProfileRefCnt_Type=Integer32
_ZxGponBWProfileRefCnt_Object=MibTableColumn
zxGponBWProfileRefCnt=_ZxGponBWProfileRefCnt_Object((1,3,6,1,4,1,3902,1012,3,26,1,1,7),_ZxGponBWProfileRefCnt_Type())
zxGponBWProfileRefCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponBWProfileRefCnt.setStatus(_A)
_ZxGponBWProfileEntryStatus_Type=RowStatus
_ZxGponBWProfileEntryStatus_Object=MibTableColumn
zxGponBWProfileEntryStatus=_ZxGponBWProfileEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,26,1,1,8),_ZxGponBWProfileEntryStatus_Type())
zxGponBWProfileEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponBWProfileEntryStatus.setStatus(_A)
_ZxGponTrafficProfileTable_Object=MibTable
zxGponTrafficProfileTable=_ZxGponTrafficProfileTable_Object((1,3,6,1,4,1,3902,1012,3,26,2))
if mibBuilder.loadTexts:zxGponTrafficProfileTable.setStatus(_A)
_ZxGponTrafficProfileEntry_Object=MibTableRow
zxGponTrafficProfileEntry=_ZxGponTrafficProfileEntry_Object((1,3,6,1,4,1,3902,1012,3,26,2,1))
zxGponTrafficProfileEntry.setIndexNames((0,_B,_At))
if mibBuilder.loadTexts:zxGponTrafficProfileEntry.setStatus(_A)
_ZxGponTrafficProfileIndex_Type=Integer32
_ZxGponTrafficProfileIndex_Object=MibTableColumn
zxGponTrafficProfileIndex=_ZxGponTrafficProfileIndex_Object((1,3,6,1,4,1,3902,1012,3,26,2,1,1),_ZxGponTrafficProfileIndex_Type())
zxGponTrafficProfileIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponTrafficProfileIndex.setStatus(_A)
class _ZxGponTrafficProfileName_Type(ZxGponRecordName):subtypeSpec=ZxGponRecordName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxGponTrafficProfileName_Type.__name__=_X
_ZxGponTrafficProfileName_Object=MibTableColumn
zxGponTrafficProfileName=_ZxGponTrafficProfileName_Object((1,3,6,1,4,1,3902,1012,3,26,2,1,2),_ZxGponTrafficProfileName_Type())
zxGponTrafficProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponTrafficProfileName.setStatus(_A)
_ZxGponTrafficProfileSir_Type=Integer32
_ZxGponTrafficProfileSir_Object=MibTableColumn
zxGponTrafficProfileSir=_ZxGponTrafficProfileSir_Object((1,3,6,1,4,1,3902,1012,3,26,2,1,3),_ZxGponTrafficProfileSir_Type())
zxGponTrafficProfileSir.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponTrafficProfileSir.setStatus(_A)
_ZxGponTrafficProfilePir_Type=Integer32
_ZxGponTrafficProfilePir_Object=MibTableColumn
zxGponTrafficProfilePir=_ZxGponTrafficProfilePir_Object((1,3,6,1,4,1,3902,1012,3,26,2,1,4),_ZxGponTrafficProfilePir_Type())
zxGponTrafficProfilePir.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponTrafficProfilePir.setStatus(_A)
_ZxGponTrafficProfileRefCnt_Type=Integer32
_ZxGponTrafficProfileRefCnt_Object=MibTableColumn
zxGponTrafficProfileRefCnt=_ZxGponTrafficProfileRefCnt_Object((1,3,6,1,4,1,3902,1012,3,26,2,1,5),_ZxGponTrafficProfileRefCnt_Type())
zxGponTrafficProfileRefCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTrafficProfileRefCnt.setStatus(_A)
_ZxGponTrafficProfileEntryStatus_Type=RowStatus
_ZxGponTrafficProfileEntryStatus_Object=MibTableColumn
zxGponTrafficProfileEntryStatus=_ZxGponTrafficProfileEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,26,2,1,6),_ZxGponTrafficProfileEntryStatus_Type())
zxGponTrafficProfileEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponTrafficProfileEntryStatus.setStatus(_A)
_ZxGponThresholdDataProfileTable_Object=MibTable
zxGponThresholdDataProfileTable=_ZxGponThresholdDataProfileTable_Object((1,3,6,1,4,1,3902,1012,3,26,3))
if mibBuilder.loadTexts:zxGponThresholdDataProfileTable.setStatus(_A)
_ZxGponThresholdDataProfileEntry_Object=MibTableRow
zxGponThresholdDataProfileEntry=_ZxGponThresholdDataProfileEntry_Object((1,3,6,1,4,1,3902,1012,3,26,3,1))
zxGponThresholdDataProfileEntry.setIndexNames((0,_B,_Au))
if mibBuilder.loadTexts:zxGponThresholdDataProfileEntry.setStatus(_A)
_ZxGponThresholdDataProfileIndex_Type=Integer32
_ZxGponThresholdDataProfileIndex_Object=MibTableColumn
zxGponThresholdDataProfileIndex=_ZxGponThresholdDataProfileIndex_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,1),_ZxGponThresholdDataProfileIndex_Type())
zxGponThresholdDataProfileIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponThresholdDataProfileIndex.setStatus(_A)
class _ZxGponThresholdDataProfileName_Type(ZxGponRecordName):subtypeSpec=ZxGponRecordName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxGponThresholdDataProfileName_Type.__name__=_X
_ZxGponThresholdDataProfileName_Object=MibTableColumn
zxGponThresholdDataProfileName=_ZxGponThresholdDataProfileName_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,2),_ZxGponThresholdDataProfileName_Type())
zxGponThresholdDataProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileName.setStatus(_A)
_ZxGponThresholdDataProfileVal1_Type=Unsigned32
_ZxGponThresholdDataProfileVal1_Object=MibTableColumn
zxGponThresholdDataProfileVal1=_ZxGponThresholdDataProfileVal1_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,3),_ZxGponThresholdDataProfileVal1_Type())
zxGponThresholdDataProfileVal1.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal1.setStatus(_A)
_ZxGponThresholdDataProfileVal2_Type=Unsigned32
_ZxGponThresholdDataProfileVal2_Object=MibTableColumn
zxGponThresholdDataProfileVal2=_ZxGponThresholdDataProfileVal2_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,4),_ZxGponThresholdDataProfileVal2_Type())
zxGponThresholdDataProfileVal2.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal2.setStatus(_A)
_ZxGponThresholdDataProfileVal3_Type=Unsigned32
_ZxGponThresholdDataProfileVal3_Object=MibTableColumn
zxGponThresholdDataProfileVal3=_ZxGponThresholdDataProfileVal3_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,5),_ZxGponThresholdDataProfileVal3_Type())
zxGponThresholdDataProfileVal3.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal3.setStatus(_A)
_ZxGponThresholdDataProfileVal4_Type=Unsigned32
_ZxGponThresholdDataProfileVal4_Object=MibTableColumn
zxGponThresholdDataProfileVal4=_ZxGponThresholdDataProfileVal4_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,6),_ZxGponThresholdDataProfileVal4_Type())
zxGponThresholdDataProfileVal4.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal4.setStatus(_A)
_ZxGponThresholdDataProfileVal5_Type=Unsigned32
_ZxGponThresholdDataProfileVal5_Object=MibTableColumn
zxGponThresholdDataProfileVal5=_ZxGponThresholdDataProfileVal5_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,7),_ZxGponThresholdDataProfileVal5_Type())
zxGponThresholdDataProfileVal5.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal5.setStatus(_A)
_ZxGponThresholdDataProfileVal6_Type=Unsigned32
_ZxGponThresholdDataProfileVal6_Object=MibTableColumn
zxGponThresholdDataProfileVal6=_ZxGponThresholdDataProfileVal6_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,8),_ZxGponThresholdDataProfileVal6_Type())
zxGponThresholdDataProfileVal6.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal6.setStatus(_A)
_ZxGponThresholdDataProfileVal7_Type=Unsigned32
_ZxGponThresholdDataProfileVal7_Object=MibTableColumn
zxGponThresholdDataProfileVal7=_ZxGponThresholdDataProfileVal7_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,9),_ZxGponThresholdDataProfileVal7_Type())
zxGponThresholdDataProfileVal7.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal7.setStatus(_A)
_ZxGponThresholdDataProfileVal8_Type=Unsigned32
_ZxGponThresholdDataProfileVal8_Object=MibTableColumn
zxGponThresholdDataProfileVal8=_ZxGponThresholdDataProfileVal8_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,10),_ZxGponThresholdDataProfileVal8_Type())
zxGponThresholdDataProfileVal8.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal8.setStatus(_A)
_ZxGponThresholdDataProfileVal9_Type=Unsigned32
_ZxGponThresholdDataProfileVal9_Object=MibTableColumn
zxGponThresholdDataProfileVal9=_ZxGponThresholdDataProfileVal9_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,11),_ZxGponThresholdDataProfileVal9_Type())
zxGponThresholdDataProfileVal9.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal9.setStatus(_A)
_ZxGponThresholdDataProfileVal10_Type=Unsigned32
_ZxGponThresholdDataProfileVal10_Object=MibTableColumn
zxGponThresholdDataProfileVal10=_ZxGponThresholdDataProfileVal10_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,12),_ZxGponThresholdDataProfileVal10_Type())
zxGponThresholdDataProfileVal10.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal10.setStatus(_A)
_ZxGponThresholdDataProfileVal11_Type=Unsigned32
_ZxGponThresholdDataProfileVal11_Object=MibTableColumn
zxGponThresholdDataProfileVal11=_ZxGponThresholdDataProfileVal11_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,13),_ZxGponThresholdDataProfileVal11_Type())
zxGponThresholdDataProfileVal11.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal11.setStatus(_A)
_ZxGponThresholdDataProfileVal12_Type=Unsigned32
_ZxGponThresholdDataProfileVal12_Object=MibTableColumn
zxGponThresholdDataProfileVal12=_ZxGponThresholdDataProfileVal12_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,14),_ZxGponThresholdDataProfileVal12_Type())
zxGponThresholdDataProfileVal12.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal12.setStatus(_A)
_ZxGponThresholdDataProfileVal13_Type=Unsigned32
_ZxGponThresholdDataProfileVal13_Object=MibTableColumn
zxGponThresholdDataProfileVal13=_ZxGponThresholdDataProfileVal13_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,15),_ZxGponThresholdDataProfileVal13_Type())
zxGponThresholdDataProfileVal13.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal13.setStatus(_A)
_ZxGponThresholdDataProfileVal14_Type=Unsigned32
_ZxGponThresholdDataProfileVal14_Object=MibTableColumn
zxGponThresholdDataProfileVal14=_ZxGponThresholdDataProfileVal14_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,16),_ZxGponThresholdDataProfileVal14_Type())
zxGponThresholdDataProfileVal14.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponThresholdDataProfileVal14.setStatus(_A)
_ZxGponThresholdDataProfileRefCnt_Type=Integer32
_ZxGponThresholdDataProfileRefCnt_Object=MibTableColumn
zxGponThresholdDataProfileRefCnt=_ZxGponThresholdDataProfileRefCnt_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,17),_ZxGponThresholdDataProfileRefCnt_Type())
zxGponThresholdDataProfileRefCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponThresholdDataProfileRefCnt.setStatus(_A)
_ZxGponThresholdDataProfileEntryStatus_Type=RowStatus
_ZxGponThresholdDataProfileEntryStatus_Object=MibTableColumn
zxGponThresholdDataProfileEntryStatus=_ZxGponThresholdDataProfileEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,26,3,1,18),_ZxGponThresholdDataProfileEntryStatus_Type())
zxGponThresholdDataProfileEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponThresholdDataProfileEntryStatus.setStatus(_A)
_ZxGponStandardOnu_ObjectIdentity=ObjectIdentity
zxGponStandardOnu=_ZxGponStandardOnu_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,27))
_ZxGponOnuEncryptTable_Object=MibTable
zxGponOnuEncryptTable=_ZxGponOnuEncryptTable_Object((1,3,6,1,4,1,3902,1012,3,27,3))
if mibBuilder.loadTexts:zxGponOnuEncryptTable.setStatus(_A)
_ZxGponOnuEncryptEntry_Object=MibTableRow
zxGponOnuEncryptEntry=_ZxGponOnuEncryptEntry_Object((1,3,6,1,4,1,3902,1012,3,27,3,1))
zxGponOnuEncryptEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOnuEncryptEntry.setStatus(_A)
class _ZxGponOnuEncryptDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('us',1),('ds',2),(_q,3)))
_ZxGponOnuEncryptDir_Type.__name__=_E
_ZxGponOnuEncryptDir_Object=MibTableColumn
zxGponOnuEncryptDir=_ZxGponOnuEncryptDir_Object((1,3,6,1,4,1,3902,1012,3,27,3,1,1),_ZxGponOnuEncryptDir_Type())
zxGponOnuEncryptDir.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuEncryptDir.setStatus(_A)
class _ZxGponOnuEncryptEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_ZxGponOnuEncryptEnable_Type.__name__=_E
_ZxGponOnuEncryptEnable_Object=MibTableColumn
zxGponOnuEncryptEnable=_ZxGponOnuEncryptEnable_Object((1,3,6,1,4,1,3902,1012,3,27,3,1,2),_ZxGponOnuEncryptEnable_Type())
zxGponOnuEncryptEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuEncryptEnable.setStatus(_A)
class _ZxGponOnuEncryptMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aes',1),(_r,2)))
_ZxGponOnuEncryptMode_Type.__name__=_E
_ZxGponOnuEncryptMode_Object=MibTableColumn
zxGponOnuEncryptMode=_ZxGponOnuEncryptMode_Object((1,3,6,1,4,1,3902,1012,3,27,3,1,3),_ZxGponOnuEncryptMode_Type())
zxGponOnuEncryptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuEncryptMode.setStatus(_A)
_ZxGponPortIdEncryptTable_Object=MibTable
zxGponPortIdEncryptTable=_ZxGponPortIdEncryptTable_Object((1,3,6,1,4,1,3902,1012,3,27,4))
if mibBuilder.loadTexts:zxGponPortIdEncryptTable.setStatus(_A)
_ZxGponPortIdEncryptEntry_Object=MibTableRow
zxGponPortIdEncryptEntry=_ZxGponPortIdEncryptEntry_Object((1,3,6,1,4,1,3902,1012,3,27,4,1))
zxGponPortIdEncryptEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponPortIdEncryptEntry.setStatus(_A)
_ZxGponPortIdEncryptEnable_Type=TruthValue
_ZxGponPortIdEncryptEnable_Object=MibTableColumn
zxGponPortIdEncryptEnable=_ZxGponPortIdEncryptEnable_Object((1,3,6,1,4,1,3902,1012,3,27,4,1,1),_ZxGponPortIdEncryptEnable_Type())
zxGponPortIdEncryptEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponPortIdEncryptEnable.setStatus(_A)
_ZxGponOnuAlarmStatusTable_Object=MibTable
zxGponOnuAlarmStatusTable=_ZxGponOnuAlarmStatusTable_Object((1,3,6,1,4,1,3902,1012,3,27,6))
if mibBuilder.loadTexts:zxGponOnuAlarmStatusTable.setStatus(_A)
_ZxGponOnuAlarmStatusEntry_Object=MibTableRow
zxGponOnuAlarmStatusEntry=_ZxGponOnuAlarmStatusEntry_Object((1,3,6,1,4,1,3902,1012,3,27,6,1))
zxGponOnuAlarmStatusEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOnuAlarmStatusEntry.setStatus(_A)
_ZxGponOnuAlarmLOSd_Type=TruthValue
_ZxGponOnuAlarmLOSd_Object=MibTableColumn
zxGponOnuAlarmLOSd=_ZxGponOnuAlarmLOSd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,1),_ZxGponOnuAlarmLOSd_Type())
zxGponOnuAlarmLOSd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmLOSd.setStatus(_A)
_ZxGponOnuAlarmLOSdMask_Type=TruthValue
_ZxGponOnuAlarmLOSdMask_Object=MibTableColumn
zxGponOnuAlarmLOSdMask=_ZxGponOnuAlarmLOSdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,2),_ZxGponOnuAlarmLOSdMask_Type())
zxGponOnuAlarmLOSdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmLOSdMask.setStatus(_A)
_ZxGponOnuAlarmLOFd_Type=TruthValue
_ZxGponOnuAlarmLOFd_Object=MibTableColumn
zxGponOnuAlarmLOFd=_ZxGponOnuAlarmLOFd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,3),_ZxGponOnuAlarmLOFd_Type())
zxGponOnuAlarmLOFd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmLOFd.setStatus(_A)
_ZxGponOnuAlarmLOFdMask_Type=TruthValue
_ZxGponOnuAlarmLOFdMask_Object=MibTableColumn
zxGponOnuAlarmLOFdMask=_ZxGponOnuAlarmLOFdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,4),_ZxGponOnuAlarmLOFdMask_Type())
zxGponOnuAlarmLOFdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmLOFdMask.setStatus(_A)
_ZxGponOnuAlarmSFd_Type=TruthValue
_ZxGponOnuAlarmSFd_Object=MibTableColumn
zxGponOnuAlarmSFd=_ZxGponOnuAlarmSFd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,5),_ZxGponOnuAlarmSFd_Type())
zxGponOnuAlarmSFd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmSFd.setStatus(_A)
_ZxGponOnuAlarmSFdMask_Type=TruthValue
_ZxGponOnuAlarmSFdMask_Object=MibTableColumn
zxGponOnuAlarmSFdMask=_ZxGponOnuAlarmSFdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,6),_ZxGponOnuAlarmSFdMask_Type())
zxGponOnuAlarmSFdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmSFdMask.setStatus(_A)
_ZxGponOnuAlarmSDd_Type=TruthValue
_ZxGponOnuAlarmSDd_Object=MibTableColumn
zxGponOnuAlarmSDd=_ZxGponOnuAlarmSDd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,7),_ZxGponOnuAlarmSDd_Type())
zxGponOnuAlarmSDd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmSDd.setStatus(_A)
_ZxGponOnuAlarmSDdMask_Type=TruthValue
_ZxGponOnuAlarmSDdMask_Object=MibTableColumn
zxGponOnuAlarmSDdMask=_ZxGponOnuAlarmSDdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,8),_ZxGponOnuAlarmSDdMask_Type())
zxGponOnuAlarmSDdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmSDdMask.setStatus(_A)
_ZxGponOnuAlarmLCDAd_Type=TruthValue
_ZxGponOnuAlarmLCDAd_Object=MibTableColumn
zxGponOnuAlarmLCDAd=_ZxGponOnuAlarmLCDAd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,9),_ZxGponOnuAlarmLCDAd_Type())
zxGponOnuAlarmLCDAd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmLCDAd.setStatus(_A)
_ZxGponOnuAlarmLCDAdMask_Type=TruthValue
_ZxGponOnuAlarmLCDAdMask_Object=MibTableColumn
zxGponOnuAlarmLCDAdMask=_ZxGponOnuAlarmLCDAdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,10),_ZxGponOnuAlarmLCDAdMask_Type())
zxGponOnuAlarmLCDAdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmLCDAdMask.setStatus(_A)
_ZxGponOnuAlarmLCDGd_Type=TruthValue
_ZxGponOnuAlarmLCDGd_Object=MibTableColumn
zxGponOnuAlarmLCDGd=_ZxGponOnuAlarmLCDGd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,11),_ZxGponOnuAlarmLCDGd_Type())
zxGponOnuAlarmLCDGd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmLCDGd.setStatus(_A)
_ZxGponOnuAlarmLCDGdMask_Type=TruthValue
_ZxGponOnuAlarmLCDGdMask_Object=MibTableColumn
zxGponOnuAlarmLCDGdMask=_ZxGponOnuAlarmLCDGdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,12),_ZxGponOnuAlarmLCDGdMask_Type())
zxGponOnuAlarmLCDGdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmLCDGdMask.setStatus(_A)
_ZxGponOnuAlarmTFd_Type=TruthValue
_ZxGponOnuAlarmTFd_Object=MibTableColumn
zxGponOnuAlarmTFd=_ZxGponOnuAlarmTFd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,13),_ZxGponOnuAlarmTFd_Type())
zxGponOnuAlarmTFd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmTFd.setStatus(_A)
_ZxGponOnuAlarmTFdMask_Type=TruthValue
_ZxGponOnuAlarmTFdMask_Object=MibTableColumn
zxGponOnuAlarmTFdMask=_ZxGponOnuAlarmTFdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,14),_ZxGponOnuAlarmTFdMask_Type())
zxGponOnuAlarmTFdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmTFdMask.setStatus(_A)
_ZxGponOnuAlarmSUFd_Type=TruthValue
_ZxGponOnuAlarmSUFd_Object=MibTableColumn
zxGponOnuAlarmSUFd=_ZxGponOnuAlarmSUFd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,15),_ZxGponOnuAlarmSUFd_Type())
zxGponOnuAlarmSUFd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmSUFd.setStatus(_A)
_ZxGponOnuAlarmSUFdMask_Type=TruthValue
_ZxGponOnuAlarmSUFdMask_Object=MibTableColumn
zxGponOnuAlarmSUFdMask=_ZxGponOnuAlarmSUFdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,16),_ZxGponOnuAlarmSUFdMask_Type())
zxGponOnuAlarmSUFdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmSUFdMask.setStatus(_A)
_ZxGponOnuAlarmMEMd_Type=TruthValue
_ZxGponOnuAlarmMEMd_Object=MibTableColumn
zxGponOnuAlarmMEMd=_ZxGponOnuAlarmMEMd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,17),_ZxGponOnuAlarmMEMd_Type())
zxGponOnuAlarmMEMd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmMEMd.setStatus(_A)
_ZxGponOnuAlarmMEMdMask_Type=TruthValue
_ZxGponOnuAlarmMEMdMask_Object=MibTableColumn
zxGponOnuAlarmMEMdMask=_ZxGponOnuAlarmMEMdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,18),_ZxGponOnuAlarmMEMdMask_Type())
zxGponOnuAlarmMEMdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmMEMdMask.setStatus(_A)
_ZxGponOnuAlarmDACTd_Type=TruthValue
_ZxGponOnuAlarmDACTd_Object=MibTableColumn
zxGponOnuAlarmDACTd=_ZxGponOnuAlarmDACTd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,19),_ZxGponOnuAlarmDACTd_Type())
zxGponOnuAlarmDACTd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmDACTd.setStatus(_A)
_ZxGponOnuAlarmDACTdMask_Type=TruthValue
_ZxGponOnuAlarmDACTdMask_Object=MibTableColumn
zxGponOnuAlarmDACTdMask=_ZxGponOnuAlarmDACTdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,20),_ZxGponOnuAlarmDACTdMask_Type())
zxGponOnuAlarmDACTdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmDACTdMask.setStatus(_A)
_ZxGponOnuAlarmDISd_Type=TruthValue
_ZxGponOnuAlarmDISd_Object=MibTableColumn
zxGponOnuAlarmDISd=_ZxGponOnuAlarmDISd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,21),_ZxGponOnuAlarmDISd_Type())
zxGponOnuAlarmDISd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmDISd.setStatus(_A)
_ZxGponOnuAlarmDISdMask_Type=TruthValue
_ZxGponOnuAlarmDISdMask_Object=MibTableColumn
zxGponOnuAlarmDISdMask=_ZxGponOnuAlarmDISdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,22),_ZxGponOnuAlarmDISdMask_Type())
zxGponOnuAlarmDISdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmDISdMask.setStatus(_A)
_ZxGponOnuAlarmMISd_Type=TruthValue
_ZxGponOnuAlarmMISd_Object=MibTableColumn
zxGponOnuAlarmMISd=_ZxGponOnuAlarmMISd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,23),_ZxGponOnuAlarmMISd_Type())
zxGponOnuAlarmMISd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmMISd.setStatus(_A)
_ZxGponOnuAlarmMISdMask_Type=TruthValue
_ZxGponOnuAlarmMISdMask_Object=MibTableColumn
zxGponOnuAlarmMISdMask=_ZxGponOnuAlarmMISdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,24),_ZxGponOnuAlarmMISdMask_Type())
zxGponOnuAlarmMISdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmMISdMask.setStatus(_A)
_ZxGponOnuAlarmPEEd_Type=TruthValue
_ZxGponOnuAlarmPEEd_Object=MibTableColumn
zxGponOnuAlarmPEEd=_ZxGponOnuAlarmPEEd_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,25),_ZxGponOnuAlarmPEEd_Type())
zxGponOnuAlarmPEEd.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmPEEd.setStatus(_A)
_ZxGponOnuAlarmPEEdMask_Type=TruthValue
_ZxGponOnuAlarmPEEdMask_Object=MibTableColumn
zxGponOnuAlarmPEEdMask=_ZxGponOnuAlarmPEEdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,26),_ZxGponOnuAlarmPEEdMask_Type())
zxGponOnuAlarmPEEdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmPEEdMask.setStatus(_A)
_ZxGponOnuAlarmRDId_Type=TruthValue
_ZxGponOnuAlarmRDId_Object=MibTableColumn
zxGponOnuAlarmRDId=_ZxGponOnuAlarmRDId_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,27),_ZxGponOnuAlarmRDId_Type())
zxGponOnuAlarmRDId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuAlarmRDId.setStatus(_A)
_ZxGponOnuAlarmRDIdMask_Type=TruthValue
_ZxGponOnuAlarmRDIdMask_Object=MibTableColumn
zxGponOnuAlarmRDIdMask=_ZxGponOnuAlarmRDIdMask_Object((1,3,6,1,4,1,3902,1012,3,27,6,1,28),_ZxGponOnuAlarmRDIdMask_Type())
zxGponOnuAlarmRDIdMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuAlarmRDIdMask.setStatus(_A)
_ZxGponSignalThresholdTable_Object=MibTable
zxGponSignalThresholdTable=_ZxGponSignalThresholdTable_Object((1,3,6,1,4,1,3902,1012,3,27,7))
if mibBuilder.loadTexts:zxGponSignalThresholdTable.setStatus(_A)
_ZxGponSignalThresholdEntry_Object=MibTableRow
zxGponSignalThresholdEntry=_ZxGponSignalThresholdEntry_Object((1,3,6,1,4,1,3902,1012,3,27,7,1))
zxGponSignalThresholdEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponSignalThresholdEntry.setStatus(_A)
_ZxGponSignalThresholdSDd_Type=Integer32
_ZxGponSignalThresholdSDd_Object=MibTableColumn
zxGponSignalThresholdSDd=_ZxGponSignalThresholdSDd_Object((1,3,6,1,4,1,3902,1012,3,27,7,1,1),_ZxGponSignalThresholdSDd_Type())
zxGponSignalThresholdSDd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponSignalThresholdSDd.setStatus(_A)
_ZxGponSignalThresholdSFd_Type=Integer32
_ZxGponSignalThresholdSFd_Object=MibTableColumn
zxGponSignalThresholdSFd=_ZxGponSignalThresholdSFd_Object((1,3,6,1,4,1,3902,1012,3,27,7,1,2),_ZxGponSignalThresholdSFd_Type())
zxGponSignalThresholdSFd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponSignalThresholdSFd.setStatus(_A)
_ZxGponOnuPerfStatisticTable_Object=MibTable
zxGponOnuPerfStatisticTable=_ZxGponOnuPerfStatisticTable_Object((1,3,6,1,4,1,3902,1012,3,27,8))
if mibBuilder.loadTexts:zxGponOnuPerfStatisticTable.setStatus(_A)
_ZxGponOnuPerfStatisticEntry_Object=MibTableRow
zxGponOnuPerfStatisticEntry=_ZxGponOnuPerfStatisticEntry_Object((1,3,6,1,4,1,3902,1012,3,27,8,1))
zxGponOnuPerfStatisticEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOnuPerfStatisticEntry.setStatus(_A)
_ZxGponOnuPerfStatERRdCounter_Type=Counter64
_ZxGponOnuPerfStatERRdCounter_Object=MibTableColumn
zxGponOnuPerfStatERRdCounter=_ZxGponOnuPerfStatERRdCounter_Object((1,3,6,1,4,1,3902,1012,3,27,8,1,1),_ZxGponOnuPerfStatERRdCounter_Type())
zxGponOnuPerfStatERRdCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuPerfStatERRdCounter.setStatus(_A)
_ZxGponOnuPerfStatBIPErrCounter_Type=Counter64
_ZxGponOnuPerfStatBIPErrCounter_Object=MibTableColumn
zxGponOnuPerfStatBIPErrCounter=_ZxGponOnuPerfStatBIPErrCounter_Object((1,3,6,1,4,1,3902,1012,3,27,8,1,2),_ZxGponOnuPerfStatBIPErrCounter_Type())
zxGponOnuPerfStatBIPErrCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOnuPerfStatBIPErrCounter.setStatus(_A)
_ZxGponOnuWeightTable_Object=MibTable
zxGponOnuWeightTable=_ZxGponOnuWeightTable_Object((1,3,6,1,4,1,3902,1012,3,27,9))
if mibBuilder.loadTexts:zxGponOnuWeightTable.setStatus(_A)
_ZxGponOnuWeightEntry_Object=MibTableRow
zxGponOnuWeightEntry=_ZxGponOnuWeightEntry_Object((1,3,6,1,4,1,3902,1012,3,27,9,1))
zxGponOnuWeightEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOnuWeightEntry.setStatus(_A)
class _ZxGponOnuSchedulemode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_c,0),('sp',1),(_g,2)))
_ZxGponOnuSchedulemode_Type.__name__=_E
_ZxGponOnuSchedulemode_Object=MibTableColumn
zxGponOnuSchedulemode=_ZxGponOnuSchedulemode_Object((1,3,6,1,4,1,3902,1012,3,27,9,1,1),_ZxGponOnuSchedulemode_Type())
zxGponOnuSchedulemode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuSchedulemode.setStatus(_A)
_ZxGponOnuCos1Weight_Type=Integer32
_ZxGponOnuCos1Weight_Object=MibTableColumn
zxGponOnuCos1Weight=_ZxGponOnuCos1Weight_Object((1,3,6,1,4,1,3902,1012,3,27,9,1,2),_ZxGponOnuCos1Weight_Type())
zxGponOnuCos1Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuCos1Weight.setStatus(_A)
_ZxGponOnuCos2Weight_Type=Integer32
_ZxGponOnuCos2Weight_Object=MibTableColumn
zxGponOnuCos2Weight=_ZxGponOnuCos2Weight_Object((1,3,6,1,4,1,3902,1012,3,27,9,1,3),_ZxGponOnuCos2Weight_Type())
zxGponOnuCos2Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuCos2Weight.setStatus(_A)
_ZxGponOnuCos3Weight_Type=Integer32
_ZxGponOnuCos3Weight_Object=MibTableColumn
zxGponOnuCos3Weight=_ZxGponOnuCos3Weight_Object((1,3,6,1,4,1,3902,1012,3,27,9,1,4),_ZxGponOnuCos3Weight_Type())
zxGponOnuCos3Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuCos3Weight.setStatus(_A)
_ZxGponOnuCos4Weight_Type=Integer32
_ZxGponOnuCos4Weight_Object=MibTableColumn
zxGponOnuCos4Weight=_ZxGponOnuCos4Weight_Object((1,3,6,1,4,1,3902,1012,3,27,9,1,5),_ZxGponOnuCos4Weight_Type())
zxGponOnuCos4Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuCos4Weight.setStatus(_A)
_ZxGponOnuDownTrafficPtr_Type=Integer32
_ZxGponOnuDownTrafficPtr_Object=MibTableColumn
zxGponOnuDownTrafficPtr=_ZxGponOnuDownTrafficPtr_Object((1,3,6,1,4,1,3902,1012,3,27,9,1,6),_ZxGponOnuDownTrafficPtr_Type())
zxGponOnuDownTrafficPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOnuDownTrafficPtr.setStatus(_A)
_ZxGponPrivateOnu_ObjectIdentity=ObjectIdentity
zxGponPrivateOnu=_ZxGponPrivateOnu_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,28))
_ZxGponOntDevMgmtTable_Object=MibTable
zxGponOntDevMgmtTable=_ZxGponOntDevMgmtTable_Object((1,3,6,1,4,1,3902,1012,3,28,1))
if mibBuilder.loadTexts:zxGponOntDevMgmtTable.setStatus(_A)
_ZxGponOntDevMgmtEntry_Object=MibTableRow
zxGponOntDevMgmtEntry=_ZxGponOntDevMgmtEntry_Object((1,3,6,1,4,1,3902,1012,3,28,1,1))
zxGponOntDevMgmtEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntDevMgmtEntry.setStatus(_A)
class _ZxGponOntDevMgmtTypeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxGponOntDevMgmtTypeName_Type.__name__=_O
_ZxGponOntDevMgmtTypeName_Object=MibTableColumn
zxGponOntDevMgmtTypeName=_ZxGponOntDevMgmtTypeName_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,1),_ZxGponOntDevMgmtTypeName_Type())
zxGponOntDevMgmtTypeName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntDevMgmtTypeName.setStatus(_A)
class _ZxGponOntDevMgmtName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZxGponOntDevMgmtName_Type.__name__=_O
_ZxGponOntDevMgmtName_Object=MibTableColumn
zxGponOntDevMgmtName=_ZxGponOntDevMgmtName_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,2),_ZxGponOntDevMgmtName_Type())
zxGponOntDevMgmtName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntDevMgmtName.setStatus(_A)
class _ZxGponOntDevMgmtDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(127,127));fixedLength=127
_ZxGponOntDevMgmtDescription_Type.__name__=_O
_ZxGponOntDevMgmtDescription_Object=MibTableColumn
zxGponOntDevMgmtDescription=_ZxGponOntDevMgmtDescription_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,3),_ZxGponOntDevMgmtDescription_Type())
zxGponOntDevMgmtDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntDevMgmtDescription.setStatus(_A)
class _ZxGponOntDevMgmtRegisterId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_ZxGponOntDevMgmtRegisterId_Type.__name__=_O
_ZxGponOntDevMgmtRegisterId_Object=MibTableColumn
zxGponOntDevMgmtRegisterId=_ZxGponOntDevMgmtRegisterId_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,4),_ZxGponOntDevMgmtRegisterId_Type())
zxGponOntDevMgmtRegisterId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntDevMgmtRegisterId.setStatus(_A)
class _ZxGponOntDevMgmtProvisionSn_Type(OntSerialNumber):subtypeSpec=OntSerialNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxGponOntDevMgmtProvisionSn_Type.__name__=_f
_ZxGponOntDevMgmtProvisionSn_Object=MibTableColumn
zxGponOntDevMgmtProvisionSn=_ZxGponOntDevMgmtProvisionSn_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,5),_ZxGponOntDevMgmtProvisionSn_Type())
zxGponOntDevMgmtProvisionSn.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntDevMgmtProvisionSn.setStatus(_A)
class _ZxGponOntDevMgmtPwMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonePw',1),('force',2)))
_ZxGponOntDevMgmtPwMode_Type.__name__=_E
_ZxGponOntDevMgmtPwMode_Object=MibTableColumn
zxGponOntDevMgmtPwMode=_ZxGponOntDevMgmtPwMode_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,6),_ZxGponOntDevMgmtPwMode_Type())
zxGponOntDevMgmtPwMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntDevMgmtPwMode.setStatus(_A)
class _ZxGponOntDevMgmtPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_ZxGponOntDevMgmtPassword_Type.__name__=_O
_ZxGponOntDevMgmtPassword_Object=MibTableColumn
zxGponOntDevMgmtPassword=_ZxGponOntDevMgmtPassword_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,7),_ZxGponOntDevMgmtPassword_Type())
zxGponOntDevMgmtPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntDevMgmtPassword.setStatus(_A)
class _ZxGponOntTargetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deactive',1),(_A9,2)))
_ZxGponOntTargetState_Type.__name__=_E
_ZxGponOntTargetState_Object=MibTableColumn
zxGponOntTargetState=_ZxGponOntTargetState_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,8),_ZxGponOntTargetState_Type())
zxGponOntTargetState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntTargetState.setStatus(_A)
_ZxGponOntDevMgmtEntryStatus_Type=RowStatus
_ZxGponOntDevMgmtEntryStatus_Object=MibTableColumn
zxGponOntDevMgmtEntryStatus=_ZxGponOntDevMgmtEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,9),_ZxGponOntDevMgmtEntryStatus_Type())
zxGponOntDevMgmtEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponOntDevMgmtEntryStatus.setStatus(_A)
_ZxGponOntIsAutoUpdate_Type=TruthValue
_ZxGponOntIsAutoUpdate_Object=MibTableColumn
zxGponOntIsAutoUpdate=_ZxGponOntIsAutoUpdate_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,10),_ZxGponOntIsAutoUpdate_Type())
zxGponOntIsAutoUpdate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntIsAutoUpdate.setStatus(_A)
class _ZxGponOntRegMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('regModeSn',1),('regModePw',2),('regModeSnPlusPw',3),('regModeId',4)))
_ZxGponOntRegMode_Type.__name__=_E
_ZxGponOntRegMode_Object=MibTableColumn
zxGponOntRegMode=_ZxGponOntRegMode_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,11),_ZxGponOntRegMode_Type())
zxGponOntRegMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntRegMode.setStatus(_A)
class _ZxGponOntRegId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ZxGponOntRegId_Type.__name__=_O
_ZxGponOntRegId_Object=MibTableColumn
zxGponOntRegId=_ZxGponOntRegId_Object((1,3,6,1,4,1,3902,1012,3,28,1,1,12),_ZxGponOntRegId_Type())
zxGponOntRegId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntRegId.setStatus(_A)
_ZxGponOntStateTable_Object=MibTable
zxGponOntStateTable=_ZxGponOntStateTable_Object((1,3,6,1,4,1,3902,1012,3,28,2))
if mibBuilder.loadTexts:zxGponOntStateTable.setStatus(_A)
_ZxGponOntStateEntry_Object=MibTableRow
zxGponOntStateEntry=_ZxGponOntStateEntry_Object((1,3,6,1,4,1,3902,1012,3,28,2,1))
zxGponOntStateEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntStateEntry.setStatus(_A)
class _ZxGponOntAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxGponOntAdminState_Type.__name__=_E
_ZxGponOntAdminState_Object=MibTableColumn
zxGponOntAdminState=_ZxGponOntAdminState_Object((1,3,6,1,4,1,3902,1012,3,28,2,1,1),_ZxGponOntAdminState_Type())
zxGponOntAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntAdminState.setStatus(_A)
_ZxGponOntOmccState_Type=TruthValue
_ZxGponOntOmccState_Object=MibTableColumn
zxGponOntOmccState=_ZxGponOntOmccState_Object((1,3,6,1,4,1,3902,1012,3,28,2,1,2),_ZxGponOntOmccState_Type())
zxGponOntOmccState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntOmccState.setStatus(_A)
class _ZxGponOntO1O7State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',0),(_AB,1),(_AC,2),(_AD,3),(_AE,4),(_AF,5),(_AG,6),('o7-popup',7)))
_ZxGponOntO1O7State_Type.__name__=_E
_ZxGponOntO1O7State_Object=MibTableColumn
zxGponOntO1O7State=_ZxGponOntO1O7State_Object((1,3,6,1,4,1,3902,1012,3,28,2,1,3),_ZxGponOntO1O7State_Type())
zxGponOntO1O7State.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntO1O7State.setStatus(_A)
class _ZxGponOntPhaseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('logging',0),('los',1),('syncMib',2),('working',3),('dyinggasp',4),('authFailed',5),('offline',6)))
_ZxGponOntPhaseState_Type.__name__=_E
_ZxGponOntPhaseState_Object=MibTableColumn
zxGponOntPhaseState=_ZxGponOntPhaseState_Object((1,3,6,1,4,1,3902,1012,3,28,2,1,4),_ZxGponOntPhaseState_Type())
zxGponOntPhaseState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPhaseState.setStatus(_A)
_ZxGponOntDevInfoTable_Object=MibTable
zxGponOntDevInfoTable=_ZxGponOntDevInfoTable_Object((1,3,6,1,4,1,3902,1012,3,28,3))
if mibBuilder.loadTexts:zxGponOntDevInfoTable.setStatus(_A)
_ZxGponOntDevInfoEntry_Object=MibTableRow
zxGponOntDevInfoEntry=_ZxGponOntDevInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,28,3,1))
zxGponOntDevInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntDevInfoEntry.setStatus(_A)
_ZxGponOntDevInfoSupportTcontNum_Type=Integer32
_ZxGponOntDevInfoSupportTcontNum_Object=MibTableColumn
zxGponOntDevInfoSupportTcontNum=_ZxGponOntDevInfoSupportTcontNum_Object((1,3,6,1,4,1,3902,1012,3,28,3,1,1),_ZxGponOntDevInfoSupportTcontNum_Type())
zxGponOntDevInfoSupportTcontNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntDevInfoSupportTcontNum.setStatus(_A)
_ZxGponOntDevInfoCurUsedTcontNum_Type=Integer32
_ZxGponOntDevInfoCurUsedTcontNum_Object=MibTableColumn
zxGponOntDevInfoCurUsedTcontNum=_ZxGponOntDevInfoCurUsedTcontNum_Object((1,3,6,1,4,1,3902,1012,3,28,3,1,2),_ZxGponOntDevInfoCurUsedTcontNum_Type())
zxGponOntDevInfoCurUsedTcontNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntDevInfoCurUsedTcontNum.setStatus(_A)
_ZxGponOntDevInfoSupportPortIdNum_Type=Integer32
_ZxGponOntDevInfoSupportPortIdNum_Object=MibTableColumn
zxGponOntDevInfoSupportPortIdNum=_ZxGponOntDevInfoSupportPortIdNum_Object((1,3,6,1,4,1,3902,1012,3,28,3,1,3),_ZxGponOntDevInfoSupportPortIdNum_Type())
zxGponOntDevInfoSupportPortIdNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntDevInfoSupportPortIdNum.setStatus(_A)
_ZxGponOntDevInfoCurUsedPortIdNum_Type=Integer32
_ZxGponOntDevInfoCurUsedPortIdNum_Object=MibTableColumn
zxGponOntDevInfoCurUsedPortIdNum=_ZxGponOntDevInfoCurUsedPortIdNum_Object((1,3,6,1,4,1,3902,1012,3,28,3,1,4),_ZxGponOntDevInfoCurUsedPortIdNum_Type())
zxGponOntDevInfoCurUsedPortIdNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntDevInfoCurUsedPortIdNum.setStatus(_A)
_ZxGponOntDevInfoPqNum_Type=Integer32
_ZxGponOntDevInfoPqNum_Object=MibTableColumn
zxGponOntDevInfoPqNum=_ZxGponOntDevInfoPqNum_Object((1,3,6,1,4,1,3902,1012,3,28,3,1,5),_ZxGponOntDevInfoPqNum_Type())
zxGponOntDevInfoPqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntDevInfoPqNum.setStatus(_A)
_ZxGponOntDevInfoTsNum_Type=Integer32
_ZxGponOntDevInfoTsNum_Object=MibTableColumn
zxGponOntDevInfoTsNum=_ZxGponOntDevInfoTsNum_Object((1,3,6,1,4,1,3902,1012,3,28,3,1,6),_ZxGponOntDevInfoTsNum_Type())
zxGponOntDevInfoTsNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntDevInfoTsNum.setStatus(_A)
_ZxGponOntDevInfoServiceType_Type=Integer32
_ZxGponOntDevInfoServiceType_Object=MibTableColumn
zxGponOntDevInfoServiceType=_ZxGponOntDevInfoServiceType_Object((1,3,6,1,4,1,3902,1012,3,28,3,1,7),_ZxGponOntDevInfoServiceType_Type())
zxGponOntDevInfoServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntDevInfoServiceType.setStatus(_A)
_ZxGponOntDevInfoRealOnuId_Type=Integer32
_ZxGponOntDevInfoRealOnuId_Object=MibTableColumn
zxGponOntDevInfoRealOnuId=_ZxGponOntDevInfoRealOnuId_Object((1,3,6,1,4,1,3902,1012,3,28,3,1,8),_ZxGponOntDevInfoRealOnuId_Type())
zxGponOntDevInfoRealOnuId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntDevInfoRealOnuId.setStatus(_A)
_ZxGponOntUniPortInfoTable_Object=MibTable
zxGponOntUniPortInfoTable=_ZxGponOntUniPortInfoTable_Object((1,3,6,1,4,1,3902,1012,3,28,4))
if mibBuilder.loadTexts:zxGponOntUniPortInfoTable.setStatus(_A)
_ZxGponOntUniPortInfoEntry_Object=MibTableRow
zxGponOntUniPortInfoEntry=_ZxGponOntUniPortInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,28,4,1))
zxGponOntUniPortInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntUniPortInfoEntry.setStatus(_A)
_ZxGponOntUniPortInfoTotalUniPorts_Type=Integer32
_ZxGponOntUniPortInfoTotalUniPorts_Object=MibTableColumn
zxGponOntUniPortInfoTotalUniPorts=_ZxGponOntUniPortInfoTotalUniPorts_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,1),_ZxGponOntUniPortInfoTotalUniPorts_Type())
zxGponOntUniPortInfoTotalUniPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoTotalUniPorts.setStatus(_A)
_ZxGponOntUniPortInfoE1Ports_Type=Integer32
_ZxGponOntUniPortInfoE1Ports_Object=MibTableColumn
zxGponOntUniPortInfoE1Ports=_ZxGponOntUniPortInfoE1Ports_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,2),_ZxGponOntUniPortInfoE1Ports_Type())
zxGponOntUniPortInfoE1Ports.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoE1Ports.setStatus(_A)
_ZxGponOntUniPortInfoT1Ports_Type=Integer32
_ZxGponOntUniPortInfoT1Ports_Object=MibTableColumn
zxGponOntUniPortInfoT1Ports=_ZxGponOntUniPortInfoT1Ports_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,3),_ZxGponOntUniPortInfoT1Ports_Type())
zxGponOntUniPortInfoT1Ports.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoT1Ports.setStatus(_A)
_ZxGponOntUniPortInfoSTMPorts_Type=Integer32
_ZxGponOntUniPortInfoSTMPorts_Object=MibTableColumn
zxGponOntUniPortInfoSTMPorts=_ZxGponOntUniPortInfoSTMPorts_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,4),_ZxGponOntUniPortInfoSTMPorts_Type())
zxGponOntUniPortInfoSTMPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoSTMPorts.setStatus(_A)
_ZxGponOntUniPortInfoPOTSPorts_Type=Integer32
_ZxGponOntUniPortInfoPOTSPorts_Object=MibTableColumn
zxGponOntUniPortInfoPOTSPorts=_ZxGponOntUniPortInfoPOTSPorts_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,5),_ZxGponOntUniPortInfoPOTSPorts_Type())
zxGponOntUniPortInfoPOTSPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoPOTSPorts.setStatus(_A)
_ZxGponOntUniPortInfoEthPorts_Type=Integer32
_ZxGponOntUniPortInfoEthPorts_Object=MibTableColumn
zxGponOntUniPortInfoEthPorts=_ZxGponOntUniPortInfoEthPorts_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,6),_ZxGponOntUniPortInfoEthPorts_Type())
zxGponOntUniPortInfoEthPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoEthPorts.setStatus(_A)
_ZxGponOntUniPortInfoRFPorts_Type=Integer32
_ZxGponOntUniPortInfoRFPorts_Object=MibTableColumn
zxGponOntUniPortInfoRFPorts=_ZxGponOntUniPortInfoRFPorts_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,7),_ZxGponOntUniPortInfoRFPorts_Type())
zxGponOntUniPortInfoRFPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoRFPorts.setStatus(_A)
_ZxGponOntUniPortInfoMoCAPorts_Type=Integer32
_ZxGponOntUniPortInfoMoCAPorts_Object=MibTableColumn
zxGponOntUniPortInfoMoCAPorts=_ZxGponOntUniPortInfoMoCAPorts_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,8),_ZxGponOntUniPortInfoMoCAPorts_Type())
zxGponOntUniPortInfoMoCAPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoMoCAPorts.setStatus(_A)
_ZxGponOntUniPortInfoWiFiPorts_Type=Integer32
_ZxGponOntUniPortInfoWiFiPorts_Object=MibTableColumn
zxGponOntUniPortInfoWiFiPorts=_ZxGponOntUniPortInfoWiFiPorts_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,9),_ZxGponOntUniPortInfoWiFiPorts_Type())
zxGponOntUniPortInfoWiFiPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoWiFiPorts.setStatus(_A)
_ZxGponOntUniPortInfoAdslPorts_Type=Integer32
_ZxGponOntUniPortInfoAdslPorts_Object=MibTableColumn
zxGponOntUniPortInfoAdslPorts=_ZxGponOntUniPortInfoAdslPorts_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,10),_ZxGponOntUniPortInfoAdslPorts_Type())
zxGponOntUniPortInfoAdslPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoAdslPorts.setStatus(_A)
_ZxGponOntUniPortInfoVdslPorts_Type=Integer32
_ZxGponOntUniPortInfoVdslPorts_Object=MibTableColumn
zxGponOntUniPortInfoVdslPorts=_ZxGponOntUniPortInfoVdslPorts_Object((1,3,6,1,4,1,3902,1012,3,28,4,1,11),_ZxGponOntUniPortInfoVdslPorts_Type())
zxGponOntUniPortInfoVdslPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntUniPortInfoVdslPorts.setStatus(_A)
_ZxGponOntPmStatisInfoTable_Object=MibTable
zxGponOntPmStatisInfoTable=_ZxGponOntPmStatisInfoTable_Object((1,3,6,1,4,1,3902,1012,3,28,5))
if mibBuilder.loadTexts:zxGponOntPmStatisInfoTable.setStatus(_A)
_ZxGponOntPmStatisInfoEntry_Object=MibTableRow
zxGponOntPmStatisInfoEntry=_ZxGponOntPmStatisInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,28,5,1))
zxGponOntPmStatisInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntPmStatisInfoEntry.setStatus(_A)
_ZxGponOntPmStatisInfoGemPacketTxLo_Type=Integer32
_ZxGponOntPmStatisInfoGemPacketTxLo_Object=MibTableColumn
zxGponOntPmStatisInfoGemPacketTxLo=_ZxGponOntPmStatisInfoGemPacketTxLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,1),_ZxGponOntPmStatisInfoGemPacketTxLo_Type())
zxGponOntPmStatisInfoGemPacketTxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoGemPacketTxLo.setStatus(_A)
_ZxGponOntPmStatisInfoGemPacketRxCorIdleLo_Type=Integer32
_ZxGponOntPmStatisInfoGemPacketRxCorIdleLo_Object=MibTableColumn
zxGponOntPmStatisInfoGemPacketRxCorIdleLo=_ZxGponOntPmStatisInfoGemPacketRxCorIdleLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,2),_ZxGponOntPmStatisInfoGemPacketRxCorIdleLo_Type())
zxGponOntPmStatisInfoGemPacketRxCorIdleLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoGemPacketRxCorIdleLo.setStatus(_A)
_ZxGponOntPmStatisInfoGemPacketRxCorNoIdleLo_Type=Integer32
_ZxGponOntPmStatisInfoGemPacketRxCorNoIdleLo_Object=MibTableColumn
zxGponOntPmStatisInfoGemPacketRxCorNoIdleLo=_ZxGponOntPmStatisInfoGemPacketRxCorNoIdleLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,3),_ZxGponOntPmStatisInfoGemPacketRxCorNoIdleLo_Type())
zxGponOntPmStatisInfoGemPacketRxCorNoIdleLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoGemPacketRxCorNoIdleLo.setStatus(_A)
_ZxGponOntPmStatisInfoGemPacketRxErrLo_Type=Integer32
_ZxGponOntPmStatisInfoGemPacketRxErrLo_Object=MibTableColumn
zxGponOntPmStatisInfoGemPacketRxErrLo=_ZxGponOntPmStatisInfoGemPacketRxErrLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,4),_ZxGponOntPmStatisInfoGemPacketRxErrLo_Type())
zxGponOntPmStatisInfoGemPacketRxErrLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoGemPacketRxErrLo.setStatus(_A)
_ZxGponOntPmStatisInfoGemPayloadBytesRxLo_Type=Integer32
_ZxGponOntPmStatisInfoGemPayloadBytesRxLo_Object=MibTableColumn
zxGponOntPmStatisInfoGemPayloadBytesRxLo=_ZxGponOntPmStatisInfoGemPayloadBytesRxLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,5),_ZxGponOntPmStatisInfoGemPayloadBytesRxLo_Type())
zxGponOntPmStatisInfoGemPayloadBytesRxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoGemPayloadBytesRxLo.setStatus(_A)
_ZxGponOntPmStatisInfoEthPacketTxLo_Type=Integer32
_ZxGponOntPmStatisInfoEthPacketTxLo_Object=MibTableColumn
zxGponOntPmStatisInfoEthPacketTxLo=_ZxGponOntPmStatisInfoEthPacketTxLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,6),_ZxGponOntPmStatisInfoEthPacketTxLo_Type())
zxGponOntPmStatisInfoEthPacketTxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoEthPacketTxLo.setStatus(_A)
_ZxGponOntPmStatisInfoEthPacketRxCorLo_Type=Integer32
_ZxGponOntPmStatisInfoEthPacketRxCorLo_Object=MibTableColumn
zxGponOntPmStatisInfoEthPacketRxCorLo=_ZxGponOntPmStatisInfoEthPacketRxCorLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,7),_ZxGponOntPmStatisInfoEthPacketRxCorLo_Type())
zxGponOntPmStatisInfoEthPacketRxCorLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoEthPacketRxCorLo.setStatus(_A)
_ZxGponOntPmStatisInfoEthPacketRxErrLo_Type=Integer32
_ZxGponOntPmStatisInfoEthPacketRxErrLo_Object=MibTableColumn
zxGponOntPmStatisInfoEthPacketRxErrLo=_ZxGponOntPmStatisInfoEthPacketRxErrLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,8),_ZxGponOntPmStatisInfoEthPacketRxErrLo_Type())
zxGponOntPmStatisInfoEthPacketRxErrLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoEthPacketRxErrLo.setStatus(_A)
_ZxGponOntPmStatisInfoOmciPacketTxLo_Type=Integer32
_ZxGponOntPmStatisInfoOmciPacketTxLo_Object=MibTableColumn
zxGponOntPmStatisInfoOmciPacketTxLo=_ZxGponOntPmStatisInfoOmciPacketTxLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,9),_ZxGponOntPmStatisInfoOmciPacketTxLo_Type())
zxGponOntPmStatisInfoOmciPacketTxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoOmciPacketTxLo.setStatus(_A)
_ZxGponOntPmStatisInfoOmciPacketRxLo_Type=Integer32
_ZxGponOntPmStatisInfoOmciPacketRxLo_Object=MibTableColumn
zxGponOntPmStatisInfoOmciPacketRxLo=_ZxGponOntPmStatisInfoOmciPacketRxLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,10),_ZxGponOntPmStatisInfoOmciPacketRxLo_Type())
zxGponOntPmStatisInfoOmciPacketRxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoOmciPacketRxLo.setStatus(_A)
_ZxGponOntPmStatisInfoOmciPacketRxCorLo_Type=Integer32
_ZxGponOntPmStatisInfoOmciPacketRxCorLo_Object=MibTableColumn
zxGponOntPmStatisInfoOmciPacketRxCorLo=_ZxGponOntPmStatisInfoOmciPacketRxCorLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,11),_ZxGponOntPmStatisInfoOmciPacketRxCorLo_Type())
zxGponOntPmStatisInfoOmciPacketRxCorLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoOmciPacketRxCorLo.setStatus(_A)
_ZxGponOntPmStatisInfoOmciPacketRxErrLo_Type=Integer32
_ZxGponOntPmStatisInfoOmciPacketRxErrLo_Object=MibTableColumn
zxGponOntPmStatisInfoOmciPacketRxErrLo=_ZxGponOntPmStatisInfoOmciPacketRxErrLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,12),_ZxGponOntPmStatisInfoOmciPacketRxErrLo_Type())
zxGponOntPmStatisInfoOmciPacketRxErrLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoOmciPacketRxErrLo.setStatus(_A)
_ZxGponOntPmStatisInfoPloamTxLo_Type=Integer32
_ZxGponOntPmStatisInfoPloamTxLo_Object=MibTableColumn
zxGponOntPmStatisInfoPloamTxLo=_ZxGponOntPmStatisInfoPloamTxLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,13),_ZxGponOntPmStatisInfoPloamTxLo_Type())
zxGponOntPmStatisInfoPloamTxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoPloamTxLo.setStatus(_A)
_ZxGponOntPmStatisInfoPloamRxCorLo_Type=Integer32
_ZxGponOntPmStatisInfoPloamRxCorLo_Object=MibTableColumn
zxGponOntPmStatisInfoPloamRxCorLo=_ZxGponOntPmStatisInfoPloamRxCorLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,14),_ZxGponOntPmStatisInfoPloamRxCorLo_Type())
zxGponOntPmStatisInfoPloamRxCorLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoPloamRxCorLo.setStatus(_A)
_ZxGponOntPmStatisInfoPloamRxErrLo_Type=Integer32
_ZxGponOntPmStatisInfoPloamRxErrLo_Object=MibTableColumn
zxGponOntPmStatisInfoPloamRxErrLo=_ZxGponOntPmStatisInfoPloamRxErrLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,15),_ZxGponOntPmStatisInfoPloamRxErrLo_Type())
zxGponOntPmStatisInfoPloamRxErrLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoPloamRxErrLo.setStatus(_A)
_ZxGponOntPmStatisInfoBipErrorRxLo_Type=Integer32
_ZxGponOntPmStatisInfoBipErrorRxLo_Object=MibTableColumn
zxGponOntPmStatisInfoBipErrorRxLo=_ZxGponOntPmStatisInfoBipErrorRxLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,16),_ZxGponOntPmStatisInfoBipErrorRxLo_Type())
zxGponOntPmStatisInfoBipErrorRxLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoBipErrorRxLo.setStatus(_A)
_ZxGponOntPmStatisInfoERRLo_Type=Integer32
_ZxGponOntPmStatisInfoERRLo_Object=MibTableColumn
zxGponOntPmStatisInfoERRLo=_ZxGponOntPmStatisInfoERRLo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,17),_ZxGponOntPmStatisInfoERRLo_Type())
zxGponOntPmStatisInfoERRLo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoERRLo.setStatus(_A)
_ZxGponOntPmStatisInfoREILo_Type=Integer32
_ZxGponOntPmStatisInfoREILo_Object=MibTableColumn
zxGponOntPmStatisInfoREILo=_ZxGponOntPmStatisInfoREILo_Object((1,3,6,1,4,1,3902,1012,3,28,5,1,18),_ZxGponOntPmStatisInfoREILo_Type())
zxGponOntPmStatisInfoREILo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoREILo.setStatus(_A)
_ZxGponOntPmStatisRealtimeInfoTable_Object=MibTable
zxGponOntPmStatisRealtimeInfoTable=_ZxGponOntPmStatisRealtimeInfoTable_Object((1,3,6,1,4,1,3902,1012,3,28,6))
if mibBuilder.loadTexts:zxGponOntPmStatisRealtimeInfoTable.setStatus(_A)
_ZxGponOntPmStatisRealtimeInfoEntry_Object=MibTableRow
zxGponOntPmStatisRealtimeInfoEntry=_ZxGponOntPmStatisRealtimeInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,28,6,1))
zxGponOntPmStatisRealtimeInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntPmStatisRealtimeInfoEntry.setStatus(_A)
_ZxGponOntPmStatisInfoCorrectNonIdleGemFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoCorrectNonIdleGemFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoCorrectNonIdleGemFramesUpstream=_ZxGponOntPmStatisInfoCorrectNonIdleGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,1),_ZxGponOntPmStatisInfoCorrectNonIdleGemFramesUpstream_Type())
zxGponOntPmStatisInfoCorrectNonIdleGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoCorrectNonIdleGemFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoCorrectIdleGemFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoCorrectIdleGemFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoCorrectIdleGemFramesUpstream=_ZxGponOntPmStatisInfoCorrectIdleGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,2),_ZxGponOntPmStatisInfoCorrectIdleGemFramesUpstream_Type())
zxGponOntPmStatisInfoCorrectIdleGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoCorrectIdleGemFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoErroredGemFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoErroredGemFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoErroredGemFramesUpstream=_ZxGponOntPmStatisInfoErroredGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,3),_ZxGponOntPmStatisInfoErroredGemFramesUpstream_Type())
zxGponOntPmStatisInfoErroredGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoErroredGemFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoGemPayloadBytesUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoGemPayloadBytesUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoGemPayloadBytesUpstream=_ZxGponOntPmStatisInfoGemPayloadBytesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,4),_ZxGponOntPmStatisInfoGemPayloadBytesUpstream_Type())
zxGponOntPmStatisInfoGemPayloadBytesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoGemPayloadBytesUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoCorrectEthernetFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoCorrectEthernetFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoCorrectEthernetFramesUpstream=_ZxGponOntPmStatisInfoCorrectEthernetFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,5),_ZxGponOntPmStatisInfoCorrectEthernetFramesUpstream_Type())
zxGponOntPmStatisInfoCorrectEthernetFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoCorrectEthernetFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoErroredEthernetFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoErroredEthernetFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoErroredEthernetFramesUpstream=_ZxGponOntPmStatisInfoErroredEthernetFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,6),_ZxGponOntPmStatisInfoErroredEthernetFramesUpstream_Type())
zxGponOntPmStatisInfoErroredEthernetFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoErroredEthernetFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoTotalOmciFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoTotalOmciFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoTotalOmciFramesUpstream=_ZxGponOntPmStatisInfoTotalOmciFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,7),_ZxGponOntPmStatisInfoTotalOmciFramesUpstream_Type())
zxGponOntPmStatisInfoTotalOmciFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoTotalOmciFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoERRi_Type=Unsigned32
_ZxGponOntPmStatisInfoERRi_Object=MibTableColumn
zxGponOntPmStatisInfoERRi=_ZxGponOntPmStatisInfoERRi_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,8),_ZxGponOntPmStatisInfoERRi_Type())
zxGponOntPmStatisInfoERRi.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoERRi.setStatus(_A)
_ZxGponOntPmStatisInfoREIi_Type=Unsigned32
_ZxGponOntPmStatisInfoREIi_Object=MibTableColumn
zxGponOntPmStatisInfoREIi=_ZxGponOntPmStatisInfoREIi_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,9),_ZxGponOntPmStatisInfoREIi_Type())
zxGponOntPmStatisInfoREIi.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoREIi.setStatus(_A)
_ZxGponOntPmStatisInfoUnreceivedBurstsUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoUnreceivedBurstsUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoUnreceivedBurstsUpstream=_ZxGponOntPmStatisInfoUnreceivedBurstsUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,10),_ZxGponOntPmStatisInfoUnreceivedBurstsUpstream_Type())
zxGponOntPmStatisInfoUnreceivedBurstsUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoUnreceivedBurstsUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoBipErrorUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoBipErrorUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoBipErrorUpstream=_ZxGponOntPmStatisInfoBipErrorUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,11),_ZxGponOntPmStatisInfoBipErrorUpstream_Type())
zxGponOntPmStatisInfoBipErrorUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoBipErrorUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoCorrectedBitsUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoCorrectedBitsUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoCorrectedBitsUpstream=_ZxGponOntPmStatisInfoCorrectedBitsUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,12),_ZxGponOntPmStatisInfoCorrectedBitsUpstream_Type())
zxGponOntPmStatisInfoCorrectedBitsUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoCorrectedBitsUpstream.setStatus(_A)
_ZxGponOntPmStatisInfoNotCorrectedWordsUpstream_Type=Unsigned32
_ZxGponOntPmStatisInfoNotCorrectedWordsUpstream_Object=MibTableColumn
zxGponOntPmStatisInfoNotCorrectedWordsUpstream=_ZxGponOntPmStatisInfoNotCorrectedWordsUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,6,1,13),_ZxGponOntPmStatisInfoNotCorrectedWordsUpstream_Type())
zxGponOntPmStatisInfoNotCorrectedWordsUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisInfoNotCorrectedWordsUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoTable_Object=MibTable
zxGponOntPmStatisHistoryInfoTable=_ZxGponOntPmStatisHistoryInfoTable_Object((1,3,6,1,4,1,3902,1012,3,28,7))
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoTable.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoEntry_Object=MibTableRow
zxGponOntPmStatisHistoryInfoEntry=_ZxGponOntPmStatisHistoryInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,28,7,1))
zxGponOntPmStatisHistoryInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoEntry.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream=_ZxGponOntPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,1),_ZxGponOntPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream_Type())
zxGponOntPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoCorrectIdleGemFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoCorrectIdleGemFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoCorrectIdleGemFramesUpstream=_ZxGponOntPmStatisHistoryInfoCorrectIdleGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,2),_ZxGponOntPmStatisHistoryInfoCorrectIdleGemFramesUpstream_Type())
zxGponOntPmStatisHistoryInfoCorrectIdleGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoCorrectIdleGemFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoErroredGemFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoErroredGemFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoErroredGemFramesUpstream=_ZxGponOntPmStatisHistoryInfoErroredGemFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,3),_ZxGponOntPmStatisHistoryInfoErroredGemFramesUpstream_Type())
zxGponOntPmStatisHistoryInfoErroredGemFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoErroredGemFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoGemPayloadBytesUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoGemPayloadBytesUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoGemPayloadBytesUpstream=_ZxGponOntPmStatisHistoryInfoGemPayloadBytesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,4),_ZxGponOntPmStatisHistoryInfoGemPayloadBytesUpstream_Type())
zxGponOntPmStatisHistoryInfoGemPayloadBytesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoGemPayloadBytesUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoCorrectEthernetFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoCorrectEthernetFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoCorrectEthernetFramesUpstream=_ZxGponOntPmStatisHistoryInfoCorrectEthernetFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,5),_ZxGponOntPmStatisHistoryInfoCorrectEthernetFramesUpstream_Type())
zxGponOntPmStatisHistoryInfoCorrectEthernetFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoCorrectEthernetFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoErroredEthernetFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoErroredEthernetFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoErroredEthernetFramesUpstream=_ZxGponOntPmStatisHistoryInfoErroredEthernetFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,6),_ZxGponOntPmStatisHistoryInfoErroredEthernetFramesUpstream_Type())
zxGponOntPmStatisHistoryInfoErroredEthernetFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoErroredEthernetFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoTotalOmciFramesUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoTotalOmciFramesUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoTotalOmciFramesUpstream=_ZxGponOntPmStatisHistoryInfoTotalOmciFramesUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,7),_ZxGponOntPmStatisHistoryInfoTotalOmciFramesUpstream_Type())
zxGponOntPmStatisHistoryInfoTotalOmciFramesUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoTotalOmciFramesUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoERRi_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoERRi_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoERRi=_ZxGponOntPmStatisHistoryInfoERRi_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,8),_ZxGponOntPmStatisHistoryInfoERRi_Type())
zxGponOntPmStatisHistoryInfoERRi.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoERRi.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoREIi_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoREIi_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoREIi=_ZxGponOntPmStatisHistoryInfoREIi_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,9),_ZxGponOntPmStatisHistoryInfoREIi_Type())
zxGponOntPmStatisHistoryInfoREIi.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoREIi.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoUnreceivedBurstsUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoUnreceivedBurstsUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoUnreceivedBurstsUpstream=_ZxGponOntPmStatisHistoryInfoUnreceivedBurstsUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,10),_ZxGponOntPmStatisHistoryInfoUnreceivedBurstsUpstream_Type())
zxGponOntPmStatisHistoryInfoUnreceivedBurstsUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoUnreceivedBurstsUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoBipErrorUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoBipErrorUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoBipErrorUpstream=_ZxGponOntPmStatisHistoryInfoBipErrorUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,11),_ZxGponOntPmStatisHistoryInfoBipErrorUpstream_Type())
zxGponOntPmStatisHistoryInfoBipErrorUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoBipErrorUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoCorrectedBitsUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoCorrectedBitsUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoCorrectedBitsUpstream=_ZxGponOntPmStatisHistoryInfoCorrectedBitsUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,12),_ZxGponOntPmStatisHistoryInfoCorrectedBitsUpstream_Type())
zxGponOntPmStatisHistoryInfoCorrectedBitsUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoCorrectedBitsUpstream.setStatus(_A)
_ZxGponOntPmStatisHistoryInfoNotCorrectedWordsUpstream_Type=Unsigned32
_ZxGponOntPmStatisHistoryInfoNotCorrectedWordsUpstream_Object=MibTableColumn
zxGponOntPmStatisHistoryInfoNotCorrectedWordsUpstream=_ZxGponOntPmStatisHistoryInfoNotCorrectedWordsUpstream_Object((1,3,6,1,4,1,3902,1012,3,28,7,1,13),_ZxGponOntPmStatisHistoryInfoNotCorrectedWordsUpstream_Type())
zxGponOntPmStatisHistoryInfoNotCorrectedWordsUpstream.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOntPmStatisHistoryInfoNotCorrectedWordsUpstream.setStatus(_A)
_ZxGponOntLoopbackTestInfoTable_Object=MibTable
zxGponOntLoopbackTestInfoTable=_ZxGponOntLoopbackTestInfoTable_Object((1,3,6,1,4,1,3902,1012,3,28,8))
if mibBuilder.loadTexts:zxGponOntLoopbackTestInfoTable.setStatus(_A)
_ZxGponOntLoopbackTestInfoEntry_Object=MibTableRow
zxGponOntLoopbackTestInfoEntry=_ZxGponOntLoopbackTestInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,28,8,1))
zxGponOntLoopbackTestInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I))
if mibBuilder.loadTexts:zxGponOntLoopbackTestInfoEntry.setStatus(_A)
_ZxGponOntLoopbackTestStart_Type=Integer32
_ZxGponOntLoopbackTestStart_Object=MibTableColumn
zxGponOntLoopbackTestStart=_ZxGponOntLoopbackTestStart_Object((1,3,6,1,4,1,3902,1012,3,28,8,1,1),_ZxGponOntLoopbackTestStart_Type())
zxGponOntLoopbackTestStart.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponOntLoopbackTestStart.setStatus(_A)
_ZxGponServiceMgmt_ObjectIdentity=ObjectIdentity
zxGponServiceMgmt=_ZxGponServiceMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,30))
_ZxOnuTrafficMgmtUnitTable_Object=MibTable
zxOnuTrafficMgmtUnitTable=_ZxOnuTrafficMgmtUnitTable_Object((1,3,6,1,4,1,3902,1012,3,30,1))
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitTable.setStatus(_A)
_ZxOnuTrafficMgmtUnitEntry_Object=MibTableRow
zxOnuTrafficMgmtUnitEntry=_ZxOnuTrafficMgmtUnitEntry_Object((1,3,6,1,4,1,3902,1012,3,30,1,1))
zxOnuTrafficMgmtUnitEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_Av))
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitEntry.setStatus(_A)
_ZxOnuTrafficMgmtUnitTcontIdx_Type=Integer32
_ZxOnuTrafficMgmtUnitTcontIdx_Object=MibTableColumn
zxOnuTrafficMgmtUnitTcontIdx=_ZxOnuTrafficMgmtUnitTcontIdx_Object((1,3,6,1,4,1,3902,1012,3,30,1,1,1),_ZxOnuTrafficMgmtUnitTcontIdx_Type())
zxOnuTrafficMgmtUnitTcontIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitTcontIdx.setStatus(_A)
class _ZxOnuTrafficMgmtUnitName_Type(ZxGponRecordName):subtypeSpec=ZxGponRecordName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxOnuTrafficMgmtUnitName_Type.__name__=_X
_ZxOnuTrafficMgmtUnitName_Object=MibTableColumn
zxOnuTrafficMgmtUnitName=_ZxOnuTrafficMgmtUnitName_Object((1,3,6,1,4,1,3902,1012,3,30,1,1,2),_ZxOnuTrafficMgmtUnitName_Type())
zxOnuTrafficMgmtUnitName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitName.setStatus(_A)
_ZxOnuTrafficMgmtUnitTcontUpBWIdxPtr_Type=Integer32
_ZxOnuTrafficMgmtUnitTcontUpBWIdxPtr_Object=MibTableColumn
zxOnuTrafficMgmtUnitTcontUpBWIdxPtr=_ZxOnuTrafficMgmtUnitTcontUpBWIdxPtr_Object((1,3,6,1,4,1,3902,1012,3,30,1,1,3),_ZxOnuTrafficMgmtUnitTcontUpBWIdxPtr_Type())
zxOnuTrafficMgmtUnitTcontUpBWIdxPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitTcontUpBWIdxPtr.setStatus(_A)
_ZxOnuTrafficMgmtUnitAllocId_Type=Integer32
_ZxOnuTrafficMgmtUnitAllocId_Object=MibTableColumn
zxOnuTrafficMgmtUnitAllocId=_ZxOnuTrafficMgmtUnitAllocId_Object((1,3,6,1,4,1,3902,1012,3,30,1,1,4),_ZxOnuTrafficMgmtUnitAllocId_Type())
zxOnuTrafficMgmtUnitAllocId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitAllocId.setStatus(_A)
_ZxOnuTrafficMgmtUnitUsedPortIdNum_Type=Integer32
_ZxOnuTrafficMgmtUnitUsedPortIdNum_Object=MibTableColumn
zxOnuTrafficMgmtUnitUsedPortIdNum=_ZxOnuTrafficMgmtUnitUsedPortIdNum_Object((1,3,6,1,4,1,3902,1012,3,30,1,1,5),_ZxOnuTrafficMgmtUnitUsedPortIdNum_Type())
zxOnuTrafficMgmtUnitUsedPortIdNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitUsedPortIdNum.setStatus(_A)
_ZxOnuTrafficMgmtUnitUsedFlowNum_Type=Integer32
_ZxOnuTrafficMgmtUnitUsedFlowNum_Object=MibTableColumn
zxOnuTrafficMgmtUnitUsedFlowNum=_ZxOnuTrafficMgmtUnitUsedFlowNum_Object((1,3,6,1,4,1,3902,1012,3,30,1,1,6),_ZxOnuTrafficMgmtUnitUsedFlowNum_Type())
zxOnuTrafficMgmtUnitUsedFlowNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitUsedFlowNum.setStatus(_A)
_ZxOnuTrafficMgmtUnitUsedCos_Type=Integer32
_ZxOnuTrafficMgmtUnitUsedCos_Object=MibTableColumn
zxOnuTrafficMgmtUnitUsedCos=_ZxOnuTrafficMgmtUnitUsedCos_Object((1,3,6,1,4,1,3902,1012,3,30,1,1,7),_ZxOnuTrafficMgmtUnitUsedCos_Type())
zxOnuTrafficMgmtUnitUsedCos.setMaxAccess(_C)
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitUsedCos.setStatus(_A)
_ZxOnuTrafficMgmtUnitEntryStatus_Type=RowStatus
_ZxOnuTrafficMgmtUnitEntryStatus_Object=MibTableColumn
zxOnuTrafficMgmtUnitEntryStatus=_ZxOnuTrafficMgmtUnitEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,30,1,1,8),_ZxOnuTrafficMgmtUnitEntryStatus_Type())
zxOnuTrafficMgmtUnitEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxOnuTrafficMgmtUnitEntryStatus.setStatus(_A)
_ZxGponGemPortTable_Object=MibTable
zxGponGemPortTable=_ZxGponGemPortTable_Object((1,3,6,1,4,1,3902,1012,3,30,2))
if mibBuilder.loadTexts:zxGponGemPortTable.setStatus(_A)
_ZxGponGemPortEntry_Object=MibTableRow
zxGponGemPortEntry=_ZxGponGemPortEntry_Object((1,3,6,1,4,1,3902,1012,3,30,2,1))
zxGponGemPortEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGemPortEntry.setStatus(_A)
_ZxGponGemPortIdx_Type=Integer32
_ZxGponGemPortIdx_Object=MibTableColumn
zxGponGemPortIdx=_ZxGponGemPortIdx_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,1),_ZxGponGemPortIdx_Type())
zxGponGemPortIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponGemPortIdx.setStatus(_A)
class _ZxGponGemPortName_Type(ZxGponRecordName):subtypeSpec=ZxGponRecordName.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ZxGponGemPortName_Type.__name__=_X
_ZxGponGemPortName_Object=MibTableColumn
zxGponGemPortName=_ZxGponGemPortName_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,2),_ZxGponGemPortName_Type())
zxGponGemPortName.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortName.setStatus(_A)
class _ZxGponGemPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_ZxGponGemPortType_Type.__name__=_E
_ZxGponGemPortType_Object=MibTableColumn
zxGponGemPortType=_ZxGponGemPortType_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,3),_ZxGponGemPortType_Type())
zxGponGemPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortType.setStatus(_A)
_ZxGponGemPortTcontIdx_Type=Integer32
_ZxGponGemPortTcontIdx_Object=MibTableColumn
zxGponGemPortTcontIdx=_ZxGponGemPortTcontIdx_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,4),_ZxGponGemPortTcontIdx_Type())
zxGponGemPortTcontIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortTcontIdx.setStatus(_A)
class _ZxGponGemPortDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),(_n,2),(_A4,3)))
_ZxGponGemPortDirection_Type.__name__=_E
_ZxGponGemPortDirection_Object=MibTableColumn
zxGponGemPortDirection=_ZxGponGemPortDirection_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,5),_ZxGponGemPortDirection_Type())
zxGponGemPortDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortDirection.setStatus(_A)
_ZxGponGemPortUpTrafficPtr_Type=Integer32
_ZxGponGemPortUpTrafficPtr_Object=MibTableColumn
zxGponGemPortUpTrafficPtr=_ZxGponGemPortUpTrafficPtr_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,6),_ZxGponGemPortUpTrafficPtr_Type())
zxGponGemPortUpTrafficPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortUpTrafficPtr.setStatus(_A)
_ZxGponGemPortDownTrafficPtr_Type=Integer32
_ZxGponGemPortDownTrafficPtr_Object=MibTableColumn
zxGponGemPortDownTrafficPtr=_ZxGponGemPortDownTrafficPtr_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,7),_ZxGponGemPortDownTrafficPtr_Type())
zxGponGemPortDownTrafficPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortDownTrafficPtr.setStatus(_A)
_ZxGponGemPortPortId_Type=Integer32
_ZxGponGemPortPortId_Object=MibTableColumn
zxGponGemPortPortId=_ZxGponGemPortPortId_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,8),_ZxGponGemPortPortId_Type())
zxGponGemPortPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPortId.setStatus(_A)
class _ZxGponGemPortDefaultCosType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cos0',1),('cos1',2),('cos2',3),('cos3',4)))
_ZxGponGemPortDefaultCosType_Type.__name__=_E
_ZxGponGemPortDefaultCosType_Object=MibTableColumn
zxGponGemPortDefaultCosType=_ZxGponGemPortDefaultCosType_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,9),_ZxGponGemPortDefaultCosType_Type())
zxGponGemPortDefaultCosType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortDefaultCosType.setStatus(_A)
_ZxGponGemPortEntryStatus_Type=RowStatus
_ZxGponGemPortEntryStatus_Object=MibTableColumn
zxGponGemPortEntryStatus=_ZxGponGemPortEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,10),_ZxGponGemPortEntryStatus_Type())
zxGponGemPortEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponGemPortEntryStatus.setStatus(_A)
_ZxGponGemPortUpQueue_Type=Integer32
_ZxGponGemPortUpQueue_Object=MibTableColumn
zxGponGemPortUpQueue=_ZxGponGemPortUpQueue_Object((1,3,6,1,4,1,3902,1012,3,30,2,1,11),_ZxGponGemPortUpQueue_Type())
zxGponGemPortUpQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortUpQueue.setStatus(_A)
_ZxGponGemPortBasicTable_Object=MibTable
zxGponGemPortBasicTable=_ZxGponGemPortBasicTable_Object((1,3,6,1,4,1,3902,1012,3,30,5))
if mibBuilder.loadTexts:zxGponGemPortBasicTable.setStatus(_A)
_ZxGponGemPortBasicEntry_Object=MibTableRow
zxGponGemPortBasicEntry=_ZxGponGemPortBasicEntry_Object((1,3,6,1,4,1,3902,1012,3,30,5,1))
zxGponGemPortBasicEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGemPortBasicEntry.setStatus(_A)
class _ZxGponGemBasicPNCTPInfoDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('uni2ani',1),('ani2uni',2),(_An,3)))
_ZxGponGemBasicPNCTPInfoDirection_Type.__name__=_E
_ZxGponGemBasicPNCTPInfoDirection_Object=MibTableColumn
zxGponGemBasicPNCTPInfoDirection=_ZxGponGemBasicPNCTPInfoDirection_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,1),_ZxGponGemBasicPNCTPInfoDirection_Type())
zxGponGemBasicPNCTPInfoDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemBasicPNCTPInfoDirection.setStatus(_A)
_ZxGponGemBasicPNCTPInfoPriorityUpstreamID_Type=Integer32
_ZxGponGemBasicPNCTPInfoPriorityUpstreamID_Object=MibTableColumn
zxGponGemBasicPNCTPInfoPriorityUpstreamID=_ZxGponGemBasicPNCTPInfoPriorityUpstreamID_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,2),_ZxGponGemBasicPNCTPInfoPriorityUpstreamID_Type())
zxGponGemBasicPNCTPInfoPriorityUpstreamID.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemBasicPNCTPInfoPriorityUpstreamID.setStatus(_A)
_ZxGponGemBasicPNCTPInfoPriorityDownstreamID_Type=Integer32
_ZxGponGemBasicPNCTPInfoPriorityDownstreamID_Object=MibTableColumn
zxGponGemBasicPNCTPInfoPriorityDownstreamID=_ZxGponGemBasicPNCTPInfoPriorityDownstreamID_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,3),_ZxGponGemBasicPNCTPInfoPriorityDownstreamID_Type())
zxGponGemBasicPNCTPInfoPriorityDownstreamID.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemBasicPNCTPInfoPriorityDownstreamID.setStatus(_A)
_ZxGponGemBasicPNCTPInfoUniCounter_Type=Integer32
_ZxGponGemBasicPNCTPInfoUniCounter_Object=MibTableColumn
zxGponGemBasicPNCTPInfoUniCounter=_ZxGponGemBasicPNCTPInfoUniCounter_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,4),_ZxGponGemBasicPNCTPInfoUniCounter_Type())
zxGponGemBasicPNCTPInfoUniCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemBasicPNCTPInfoUniCounter.setStatus(_A)
class _ZxGponGemBasicIWTPInfoIwOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6)));namedValues=NamedValues(*(('ces',1),('bridge',2),('mapper',6)))
_ZxGponGemBasicIWTPInfoIwOption_Type.__name__=_E
_ZxGponGemBasicIWTPInfoIwOption_Object=MibTableColumn
zxGponGemBasicIWTPInfoIwOption=_ZxGponGemBasicIWTPInfoIwOption_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,5),_ZxGponGemBasicIWTPInfoIwOption_Type())
zxGponGemBasicIWTPInfoIwOption.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemBasicIWTPInfoIwOption.setStatus(_A)
_ZxGponGemBasicIWTPInfoServiceProPtr_Type=Integer32
_ZxGponGemBasicIWTPInfoServiceProPtr_Object=MibTableColumn
zxGponGemBasicIWTPInfoServiceProPtr=_ZxGponGemBasicIWTPInfoServiceProPtr_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,6),_ZxGponGemBasicIWTPInfoServiceProPtr_Type())
zxGponGemBasicIWTPInfoServiceProPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemBasicIWTPInfoServiceProPtr.setStatus(_A)
_ZxGponGemBasicIWTPInfoPPTPCounter_Type=Integer32
_ZxGponGemBasicIWTPInfoPPTPCounter_Object=MibTableColumn
zxGponGemBasicIWTPInfoPPTPCounter=_ZxGponGemBasicIWTPInfoPPTPCounter_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,7),_ZxGponGemBasicIWTPInfoPPTPCounter_Type())
zxGponGemBasicIWTPInfoPPTPCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemBasicIWTPInfoPPTPCounter.setStatus(_A)
class _ZxGponGemBasicIWTPInfoOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_ZxGponGemBasicIWTPInfoOpState_Type.__name__=_E
_ZxGponGemBasicIWTPInfoOpState_Object=MibTableColumn
zxGponGemBasicIWTPInfoOpState=_ZxGponGemBasicIWTPInfoOpState_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,8),_ZxGponGemBasicIWTPInfoOpState_Type())
zxGponGemBasicIWTPInfoOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemBasicIWTPInfoOpState.setStatus(_A)
class _ZxGponBasicGALTDMProfileInfoFrameLossIntPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxGponBasicGALTDMProfileInfoFrameLossIntPeriod_Type.__name__=_E
_ZxGponBasicGALTDMProfileInfoFrameLossIntPeriod_Object=MibTableColumn
zxGponBasicGALTDMProfileInfoFrameLossIntPeriod=_ZxGponBasicGALTDMProfileInfoFrameLossIntPeriod_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,9),_ZxGponBasicGALTDMProfileInfoFrameLossIntPeriod_Type())
zxGponBasicGALTDMProfileInfoFrameLossIntPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBasicGALTDMProfileInfoFrameLossIntPeriod.setStatus(_A)
class _ZxGponBasicGALEthProfileInfoMaxPayloadSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxGponBasicGALEthProfileInfoMaxPayloadSize_Type.__name__=_E
_ZxGponBasicGALEthProfileInfoMaxPayloadSize_Object=MibTableColumn
zxGponBasicGALEthProfileInfoMaxPayloadSize=_ZxGponBasicGALEthProfileInfoMaxPayloadSize_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,10),_ZxGponBasicGALEthProfileInfoMaxPayloadSize_Type())
zxGponBasicGALEthProfileInfoMaxPayloadSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponBasicGALEthProfileInfoMaxPayloadSize.setStatus(_A)
class _ZxGponGemBasicMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponGemBasicMgmtCtrlFlag_Type.__name__=_E
_ZxGponGemBasicMgmtCtrlFlag_Object=MibTableColumn
zxGponGemBasicMgmtCtrlFlag=_ZxGponGemBasicMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,11),_ZxGponGemBasicMgmtCtrlFlag_Type())
zxGponGemBasicMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemBasicMgmtCtrlFlag.setStatus(_A)
_ZxGponGemBasicEntryStatus_Type=RowStatus
_ZxGponGemBasicEntryStatus_Object=MibTableColumn
zxGponGemBasicEntryStatus=_ZxGponGemBasicEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,30,5,1,12),_ZxGponGemBasicEntryStatus_Type())
zxGponGemBasicEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponGemBasicEntryStatus.setStatus(_A)
_ZxGponGemPortMACBridgeIWTPTable_Object=MibTable
zxGponGemPortMACBridgeIWTPTable=_ZxGponGemPortMACBridgeIWTPTable_Object((1,3,6,1,4,1,3902,1012,3,30,6))
if mibBuilder.loadTexts:zxGponGemPortMACBridgeIWTPTable.setStatus(_A)
_ZxGponGemPortMACBridgeIWTPEntry_Object=MibTableRow
zxGponGemPortMACBridgeIWTPEntry=_ZxGponGemPortMACBridgeIWTPEntry_Object((1,3,6,1,4,1,3902,1012,3,30,6,1))
zxGponGemPortMACBridgeIWTPEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGemPortMACBridgeIWTPEntry.setStatus(_A)
_ZxGponMACBriPortCfgDataIWTPMeIdIdx_Type=Integer32
_ZxGponMACBriPortCfgDataIWTPMeIdIdx_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPMeIdIdx=_ZxGponMACBriPortCfgDataIWTPMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,1),_ZxGponMACBriPortCfgDataIWTPMeIdIdx_Type())
zxGponMACBriPortCfgDataIWTPMeIdIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPMeIdIdx.setStatus(_A)
_ZxGponMACBriPortCfgDataIWTPPortNum_Type=Integer32
_ZxGponMACBriPortCfgDataIWTPPortNum_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPPortNum=_ZxGponMACBriPortCfgDataIWTPPortNum_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,2),_ZxGponMACBriPortCfgDataIWTPPortNum_Type())
zxGponMACBriPortCfgDataIWTPPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPPortNum.setStatus(_A)
class _ZxGponMACBriPortCfgDataIWTPTPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,5)));namedValues=NamedValues(*((_Z,2),('pri8021p',3),('gemiw',5)))
_ZxGponMACBriPortCfgDataIWTPTPType_Type.__name__=_E
_ZxGponMACBriPortCfgDataIWTPTPType_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPTPType=_ZxGponMACBriPortCfgDataIWTPTPType_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,3),_ZxGponMACBriPortCfgDataIWTPTPType_Type())
zxGponMACBriPortCfgDataIWTPTPType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPTPType.setStatus(_A)
class _ZxGponMACBriPortCfgDataIWTPPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxGponMACBriPortCfgDataIWTPPortPriority_Type.__name__=_E
_ZxGponMACBriPortCfgDataIWTPPortPriority_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPPortPriority=_ZxGponMACBriPortCfgDataIWTPPortPriority_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,4),_ZxGponMACBriPortCfgDataIWTPPortPriority_Type())
zxGponMACBriPortCfgDataIWTPPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPPortPriority.setStatus(_A)
class _ZxGponMACBriPortCfgDataIWTPPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxGponMACBriPortCfgDataIWTPPortPathCost_Type.__name__=_E
_ZxGponMACBriPortCfgDataIWTPPortPathCost_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPPortPathCost=_ZxGponMACBriPortCfgDataIWTPPortPathCost_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,5),_ZxGponMACBriPortCfgDataIWTPPortPathCost_Type())
zxGponMACBriPortCfgDataIWTPPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPPortPathCost.setStatus(_A)
_ZxGponMACBriPortCfgDataIWTPPortSpanTreeInd_Type=TruthValue
_ZxGponMACBriPortCfgDataIWTPPortSpanTreeInd_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPPortSpanTreeInd=_ZxGponMACBriPortCfgDataIWTPPortSpanTreeInd_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,6),_ZxGponMACBriPortCfgDataIWTPPortSpanTreeInd_Type())
zxGponMACBriPortCfgDataIWTPPortSpanTreeInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPPortSpanTreeInd.setStatus(_A)
_ZxGponMACBriPortCfgDataIWTPEncapMethod_Type=Integer32
_ZxGponMACBriPortCfgDataIWTPEncapMethod_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPEncapMethod=_ZxGponMACBriPortCfgDataIWTPEncapMethod_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,7),_ZxGponMACBriPortCfgDataIWTPEncapMethod_Type())
zxGponMACBriPortCfgDataIWTPEncapMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPEncapMethod.setStatus(_A)
class _ZxGponMACBriPortCfgDataIWTPLANFCSInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_s,2)))
_ZxGponMACBriPortCfgDataIWTPLANFCSInd_Type.__name__=_E
_ZxGponMACBriPortCfgDataIWTPLANFCSInd_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPLANFCSInd=_ZxGponMACBriPortCfgDataIWTPLANFCSInd_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,8),_ZxGponMACBriPortCfgDataIWTPLANFCSInd_Type())
zxGponMACBriPortCfgDataIWTPLANFCSInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPLANFCSInd.setStatus(_A)
class _ZxGponMACBriPortCfgDataIWTPMgmtCtrlFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ZxGponMACBriPortCfgDataIWTPMgmtCtrlFlag_Type.__name__=_E
_ZxGponMACBriPortCfgDataIWTPMgmtCtrlFlag_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPMgmtCtrlFlag=_ZxGponMACBriPortCfgDataIWTPMgmtCtrlFlag_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,9),_ZxGponMACBriPortCfgDataIWTPMgmtCtrlFlag_Type())
zxGponMACBriPortCfgDataIWTPMgmtCtrlFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPMgmtCtrlFlag.setStatus(_A)
_ZxGponMACBriPortCfgDataIWTPEntryStatus_Type=RowStatus
_ZxGponMACBriPortCfgDataIWTPEntryStatus_Object=MibTableColumn
zxGponMACBriPortCfgDataIWTPEntryStatus=_ZxGponMACBriPortCfgDataIWTPEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,30,6,1,10),_ZxGponMACBriPortCfgDataIWTPEntryStatus_Type())
zxGponMACBriPortCfgDataIWTPEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataIWTPEntryStatus.setStatus(_A)
_ZxGponGemPortMACBridgeUNITable_Object=MibTable
zxGponGemPortMACBridgeUNITable=_ZxGponGemPortMACBridgeUNITable_Object((1,3,6,1,4,1,3902,1012,3,30,7))
if mibBuilder.loadTexts:zxGponGemPortMACBridgeUNITable.setStatus(_A)
_ZxGponGemPortMACBridgeUNIEntry_Object=MibTableRow
zxGponGemPortMACBridgeUNIEntry=_ZxGponGemPortMACBridgeUNIEntry_Object((1,3,6,1,4,1,3902,1012,3,30,7,1))
zxGponGemPortMACBridgeUNIEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_a))
if mibBuilder.loadTexts:zxGponGemPortMACBridgeUNIEntry.setStatus(_A)
_ZxGponMACBriPortCfgDataUNIMeIdIdx_Type=Integer32
_ZxGponMACBriPortCfgDataUNIMeIdIdx_Object=MibTableColumn
zxGponMACBriPortCfgDataUNIMeIdIdx=_ZxGponMACBriPortCfgDataUNIMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,30,7,1,1),_ZxGponMACBriPortCfgDataUNIMeIdIdx_Type())
zxGponMACBriPortCfgDataUNIMeIdIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataUNIMeIdIdx.setStatus(_A)
_ZxGponMACBriPortCfgDataUNIPortNum_Type=Integer32
_ZxGponMACBriPortCfgDataUNIPortNum_Object=MibTableColumn
zxGponMACBriPortCfgDataUNIPortNum=_ZxGponMACBriPortCfgDataUNIPortNum_Object((1,3,6,1,4,1,3902,1012,3,30,7,1,2),_ZxGponMACBriPortCfgDataUNIPortNum_Type())
zxGponMACBriPortCfgDataUNIPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataUNIPortNum.setStatus(_A)
class _ZxGponMACBriPortCfgDataUNITPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_l,1))
_ZxGponMACBriPortCfgDataUNITPType_Type.__name__=_E
_ZxGponMACBriPortCfgDataUNITPType_Object=MibTableColumn
zxGponMACBriPortCfgDataUNITPType=_ZxGponMACBriPortCfgDataUNITPType_Object((1,3,6,1,4,1,3902,1012,3,30,7,1,3),_ZxGponMACBriPortCfgDataUNITPType_Type())
zxGponMACBriPortCfgDataUNITPType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataUNITPType.setStatus(_A)
class _ZxGponMACBriPortCfgDataUNIPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxGponMACBriPortCfgDataUNIPortPriority_Type.__name__=_E
_ZxGponMACBriPortCfgDataUNIPortPriority_Object=MibTableColumn
zxGponMACBriPortCfgDataUNIPortPriority=_ZxGponMACBriPortCfgDataUNIPortPriority_Object((1,3,6,1,4,1,3902,1012,3,30,7,1,4),_ZxGponMACBriPortCfgDataUNIPortPriority_Type())
zxGponMACBriPortCfgDataUNIPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataUNIPortPriority.setStatus(_A)
class _ZxGponMACBriPortCfgDataUNIPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxGponMACBriPortCfgDataUNIPortPathCost_Type.__name__=_E
_ZxGponMACBriPortCfgDataUNIPortPathCost_Object=MibTableColumn
zxGponMACBriPortCfgDataUNIPortPathCost=_ZxGponMACBriPortCfgDataUNIPortPathCost_Object((1,3,6,1,4,1,3902,1012,3,30,7,1,5),_ZxGponMACBriPortCfgDataUNIPortPathCost_Type())
zxGponMACBriPortCfgDataUNIPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataUNIPortPathCost.setStatus(_A)
_ZxGponMACBriPortCfgDataUNIPortSpanTreeInd_Type=TruthValue
_ZxGponMACBriPortCfgDataUNIPortSpanTreeInd_Object=MibTableColumn
zxGponMACBriPortCfgDataUNIPortSpanTreeInd=_ZxGponMACBriPortCfgDataUNIPortSpanTreeInd_Object((1,3,6,1,4,1,3902,1012,3,30,7,1,6),_ZxGponMACBriPortCfgDataUNIPortSpanTreeInd_Type())
zxGponMACBriPortCfgDataUNIPortSpanTreeInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataUNIPortSpanTreeInd.setStatus(_A)
_ZxGponMACBriPortCfgDataUNIEncapMethod_Type=Integer32
_ZxGponMACBriPortCfgDataUNIEncapMethod_Object=MibTableColumn
zxGponMACBriPortCfgDataUNIEncapMethod=_ZxGponMACBriPortCfgDataUNIEncapMethod_Object((1,3,6,1,4,1,3902,1012,3,30,7,1,7),_ZxGponMACBriPortCfgDataUNIEncapMethod_Type())
zxGponMACBriPortCfgDataUNIEncapMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataUNIEncapMethod.setStatus(_A)
class _ZxGponMACBriPortCfgDataUNILANFCSInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_s,2)))
_ZxGponMACBriPortCfgDataUNILANFCSInd_Type.__name__=_E
_ZxGponMACBriPortCfgDataUNILANFCSInd_Object=MibTableColumn
zxGponMACBriPortCfgDataUNILANFCSInd=_ZxGponMACBriPortCfgDataUNILANFCSInd_Object((1,3,6,1,4,1,3902,1012,3,30,7,1,8),_ZxGponMACBriPortCfgDataUNILANFCSInd_Type())
zxGponMACBriPortCfgDataUNILANFCSInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponMACBriPortCfgDataUNILANFCSInd.setStatus(_A)
_ZxGponGemPort8021pTable_Object=MibTable
zxGponGemPort8021pTable=_ZxGponGemPort8021pTable_Object((1,3,6,1,4,1,3902,1012,3,30,8))
if mibBuilder.loadTexts:zxGponGemPort8021pTable.setStatus(_A)
_ZxGponGemPort8021pEntry_Object=MibTableRow
zxGponGemPort8021pEntry=_ZxGponGemPort8021pEntry_Object((1,3,6,1,4,1,3902,1012,3,30,8,1))
zxGponGemPort8021pEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_a))
if mibBuilder.loadTexts:zxGponGemPort8021pEntry.setStatus(_A)
class _ZxGponGemPort8021pMapperUntagFrmInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Ab,1),(_Ac,2)))
_ZxGponGemPort8021pMapperUntagFrmInd_Type.__name__=_E
_ZxGponGemPort8021pMapperUntagFrmInd_Object=MibTableColumn
zxGponGemPort8021pMapperUntagFrmInd=_ZxGponGemPort8021pMapperUntagFrmInd_Object((1,3,6,1,4,1,3902,1012,3,30,8,1,1),_ZxGponGemPort8021pMapperUntagFrmInd_Type())
zxGponGemPort8021pMapperUntagFrmInd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPort8021pMapperUntagFrmInd.setStatus(_A)
class _ZxGponGemPort8021pMapperDscpTo8021pPri_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_ZxGponGemPort8021pMapperDscpTo8021pPri_Type.__name__=_O
_ZxGponGemPort8021pMapperDscpTo8021pPri_Object=MibTableColumn
zxGponGemPort8021pMapperDscpTo8021pPri=_ZxGponGemPort8021pMapperDscpTo8021pPri_Object((1,3,6,1,4,1,3902,1012,3,30,8,1,2),_ZxGponGemPort8021pMapperDscpTo8021pPri_Type())
zxGponGemPort8021pMapperDscpTo8021pPri.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPort8021pMapperDscpTo8021pPri.setStatus(_A)
_ZxGponGemPort8021pMapperDefaultPri_Type=Integer32
_ZxGponGemPort8021pMapperDefaultPri_Object=MibTableColumn
zxGponGemPort8021pMapperDefaultPri=_ZxGponGemPort8021pMapperDefaultPri_Object((1,3,6,1,4,1,3902,1012,3,30,8,1,3),_ZxGponGemPort8021pMapperDefaultPri_Type())
zxGponGemPort8021pMapperDefaultPri.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPort8021pMapperDefaultPri.setStatus(_A)
class _ZxGponGemPort8021pMapperTPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bridging-mapping',1),('ethernet',2),('ip-host-service',3)))
_ZxGponGemPort8021pMapperTPType_Type.__name__=_E
_ZxGponGemPort8021pMapperTPType_Object=MibTableColumn
zxGponGemPort8021pMapperTPType=_ZxGponGemPort8021pMapperTPType_Object((1,3,6,1,4,1,3902,1012,3,30,8,1,4),_ZxGponGemPort8021pMapperTPType_Type())
zxGponGemPort8021pMapperTPType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPort8021pMapperTPType.setStatus(_A)
_ZxGponGemPortStructuredCESTable_Object=MibTable
zxGponGemPortStructuredCESTable=_ZxGponGemPortStructuredCESTable_Object((1,3,6,1,4,1,3902,1012,3,30,9))
if mibBuilder.loadTexts:zxGponGemPortStructuredCESTable.setStatus(_A)
_ZxGponGemPortStructuredCESEntry_Object=MibTableRow
zxGponGemPortStructuredCESEntry=_ZxGponGemPortStructuredCESEntry_Object((1,3,6,1,4,1,3902,1012,3,30,9,1))
zxGponGemPortStructuredCESEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGemPortStructuredCESEntry.setStatus(_A)
_ZxGponLogicalSubportCTPMeIdIdx_Type=Integer32
_ZxGponLogicalSubportCTPMeIdIdx_Object=MibTableColumn
zxGponLogicalSubportCTPMeIdIdx=_ZxGponLogicalSubportCTPMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,30,9,1,1),_ZxGponLogicalSubportCTPMeIdIdx_Type())
zxGponLogicalSubportCTPMeIdIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponLogicalSubportCTPMeIdIdx.setStatus(_A)
class _ZxGponLogicalSubportCTPTimeSlots_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_ZxGponLogicalSubportCTPTimeSlots_Type.__name__=_O
_ZxGponLogicalSubportCTPTimeSlots_Object=MibTableColumn
zxGponLogicalSubportCTPTimeSlots=_ZxGponLogicalSubportCTPTimeSlots_Object((1,3,6,1,4,1,3902,1012,3,30,9,1,2),_ZxGponLogicalSubportCTPTimeSlots_Type())
zxGponLogicalSubportCTPTimeSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponLogicalSubportCTPTimeSlots.setStatus(_A)
_ZxGponGemPortIpRouterIWTPTable_Object=MibTable
zxGponGemPortIpRouterIWTPTable=_ZxGponGemPortIpRouterIWTPTable_Object((1,3,6,1,4,1,3902,1012,3,30,10))
if mibBuilder.loadTexts:zxGponGemPortIpRouterIWTPTable.setStatus(_A)
_ZxGponGemPortIpRouterIWTPEntry_Object=MibTableRow
zxGponGemPortIpRouterIWTPEntry=_ZxGponGemPortIpRouterIWTPEntry_Object((1,3,6,1,4,1,3902,1012,3,30,10,1))
zxGponGemPortIpRouterIWTPEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGemPortIpRouterIWTPEntry.setStatus(_A)
_ZxGponGemPortIpPortCfgDataIWTPMeIdIdx_Type=Integer32
_ZxGponGemPortIpPortCfgDataIWTPMeIdIdx_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPMeIdIdx=_ZxGponGemPortIpPortCfgDataIWTPMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,1),_ZxGponGemPortIpPortCfgDataIWTPMeIdIdx_Type())
zxGponGemPortIpPortCfgDataIWTPMeIdIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPMeIdIdx.setStatus(_A)
_ZxGponGemPortIpPortCfgDataIWTPPortNum_Type=Integer32
_ZxGponGemPortIpPortCfgDataIWTPPortNum_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPPortNum=_ZxGponGemPortIpPortCfgDataIWTPPortNum_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,2),_ZxGponGemPortIpPortCfgDataIWTPPortNum_Type())
zxGponGemPortIpPortCfgDataIWTPPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPPortNum.setStatus(_A)
class _ZxGponGemPortIpPortCfgDataIWTPTPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_Z,2)))
_ZxGponGemPortIpPortCfgDataIWTPTPType_Type.__name__=_E
_ZxGponGemPortIpPortCfgDataIWTPTPType_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPTPType=_ZxGponGemPortIpPortCfgDataIWTPTPType_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,3),_ZxGponGemPortIpPortCfgDataIWTPTPType_Type())
zxGponGemPortIpPortCfgDataIWTPTPType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPTPType.setStatus(_A)
_ZxGponGemPortIpPortCfgDataIWTPPortAddress_Type=IpAddress
_ZxGponGemPortIpPortCfgDataIWTPPortAddress_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPPortAddress=_ZxGponGemPortIpPortCfgDataIWTPPortAddress_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,4),_ZxGponGemPortIpPortCfgDataIWTPPortAddress_Type())
zxGponGemPortIpPortCfgDataIWTPPortAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPPortAddress.setStatus(_A)
_ZxGponGemPortIpPortCfgDataIWTPPortMask_Type=IpAddress
_ZxGponGemPortIpPortCfgDataIWTPPortMask_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPPortMask=_ZxGponGemPortIpPortCfgDataIWTPPortMask_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,5),_ZxGponGemPortIpPortCfgDataIWTPPortMask_Type())
zxGponGemPortIpPortCfgDataIWTPPortMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPPortMask.setStatus(_A)
_ZxGponGemPortIpPortCfgDataIWTPUnnumbered_Type=TruthValue
_ZxGponGemPortIpPortCfgDataIWTPUnnumbered_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPUnnumbered=_ZxGponGemPortIpPortCfgDataIWTPUnnumbered_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,6),_ZxGponGemPortIpPortCfgDataIWTPUnnumbered_Type())
zxGponGemPortIpPortCfgDataIWTPUnnumbered.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPUnnumbered.setStatus(_A)
class _ZxGponGemPortIpPortCfgDataIWTPAdministrativeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),(_u,2)))
_ZxGponGemPortIpPortCfgDataIWTPAdministrativeState_Type.__name__=_E
_ZxGponGemPortIpPortCfgDataIWTPAdministrativeState_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPAdministrativeState=_ZxGponGemPortIpPortCfgDataIWTPAdministrativeState_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,7),_ZxGponGemPortIpPortCfgDataIWTPAdministrativeState_Type())
zxGponGemPortIpPortCfgDataIWTPAdministrativeState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPAdministrativeState.setStatus(_A)
class _ZxGponGemPortIpPortCfgDataIWTPPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_ZxGponGemPortIpPortCfgDataIWTPPortState_Type.__name__=_E
_ZxGponGemPortIpPortCfgDataIWTPPortState_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPPortState=_ZxGponGemPortIpPortCfgDataIWTPPortState_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,8),_ZxGponGemPortIpPortCfgDataIWTPPortState_Type())
zxGponGemPortIpPortCfgDataIWTPPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPPortState.setStatus(_A)
_ZxGponGemPortIpPortCfgDataIWTPAllowRemoteAccess_Type=TruthValue
_ZxGponGemPortIpPortCfgDataIWTPAllowRemoteAccess_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPAllowRemoteAccess=_ZxGponGemPortIpPortCfgDataIWTPAllowRemoteAccess_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,9),_ZxGponGemPortIpPortCfgDataIWTPAllowRemoteAccess_Type())
zxGponGemPortIpPortCfgDataIWTPAllowRemoteAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPAllowRemoteAccess.setStatus(_A)
class _ZxGponGemPortIpPortCfgDataIWTPEncapsulationMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_ZxGponGemPortIpPortCfgDataIWTPEncapsulationMethod_Type.__name__=_E
_ZxGponGemPortIpPortCfgDataIWTPEncapsulationMethod_Object=MibTableColumn
zxGponGemPortIpPortCfgDataIWTPEncapsulationMethod=_ZxGponGemPortIpPortCfgDataIWTPEncapsulationMethod_Object((1,3,6,1,4,1,3902,1012,3,30,10,1,10),_ZxGponGemPortIpPortCfgDataIWTPEncapsulationMethod_Type())
zxGponGemPortIpPortCfgDataIWTPEncapsulationMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataIWTPEncapsulationMethod.setStatus(_A)
_ZxGponGemPortIpRouterUNITable_Object=MibTable
zxGponGemPortIpRouterUNITable=_ZxGponGemPortIpRouterUNITable_Object((1,3,6,1,4,1,3902,1012,3,30,11))
if mibBuilder.loadTexts:zxGponGemPortIpRouterUNITable.setStatus(_A)
_ZxGponGemPortIpRouterUNIEntry_Object=MibTableRow
zxGponGemPortIpRouterUNIEntry=_ZxGponGemPortIpRouterUNIEntry_Object((1,3,6,1,4,1,3902,1012,3,30,11,1))
zxGponGemPortIpRouterUNIEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_a))
if mibBuilder.loadTexts:zxGponGemPortIpRouterUNIEntry.setStatus(_A)
_ZxGponGemPortIpPortCfgDataUNIMeIdIdx_Type=Integer32
_ZxGponGemPortIpPortCfgDataUNIMeIdIdx_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNIMeIdIdx=_ZxGponGemPortIpPortCfgDataUNIMeIdIdx_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,1),_ZxGponGemPortIpPortCfgDataUNIMeIdIdx_Type())
zxGponGemPortIpPortCfgDataUNIMeIdIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNIMeIdIdx.setStatus(_A)
_ZxGponGemPortIpPortCfgDataUNIPortNum_Type=Integer32
_ZxGponGemPortIpPortCfgDataUNIPortNum_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNIPortNum=_ZxGponGemPortIpPortCfgDataUNIPortNum_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,2),_ZxGponGemPortIpPortCfgDataUNIPortNum_Type())
zxGponGemPortIpPortCfgDataUNIPortNum.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNIPortNum.setStatus(_A)
class _ZxGponGemPortIpPortCfgDataUNITPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_Z,2)))
_ZxGponGemPortIpPortCfgDataUNITPType_Type.__name__=_E
_ZxGponGemPortIpPortCfgDataUNITPType_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNITPType=_ZxGponGemPortIpPortCfgDataUNITPType_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,3),_ZxGponGemPortIpPortCfgDataUNITPType_Type())
zxGponGemPortIpPortCfgDataUNITPType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNITPType.setStatus(_A)
_ZxGponGemPortIpPortCfgDataUNIPortAddress_Type=IpAddress
_ZxGponGemPortIpPortCfgDataUNIPortAddress_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNIPortAddress=_ZxGponGemPortIpPortCfgDataUNIPortAddress_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,4),_ZxGponGemPortIpPortCfgDataUNIPortAddress_Type())
zxGponGemPortIpPortCfgDataUNIPortAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNIPortAddress.setStatus(_A)
_ZxGponGemPortIpPortCfgDataUNIPortMask_Type=IpAddress
_ZxGponGemPortIpPortCfgDataUNIPortMask_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNIPortMask=_ZxGponGemPortIpPortCfgDataUNIPortMask_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,5),_ZxGponGemPortIpPortCfgDataUNIPortMask_Type())
zxGponGemPortIpPortCfgDataUNIPortMask.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNIPortMask.setStatus(_A)
_ZxGponGemPortIpPortCfgDataUNIUnnumbered_Type=TruthValue
_ZxGponGemPortIpPortCfgDataUNIUnnumbered_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNIUnnumbered=_ZxGponGemPortIpPortCfgDataUNIUnnumbered_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,6),_ZxGponGemPortIpPortCfgDataUNIUnnumbered_Type())
zxGponGemPortIpPortCfgDataUNIUnnumbered.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNIUnnumbered.setStatus(_A)
class _ZxGponGemPortIpPortCfgDataUNIAdministrativeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_t,1),(_u,2)))
_ZxGponGemPortIpPortCfgDataUNIAdministrativeState_Type.__name__=_E
_ZxGponGemPortIpPortCfgDataUNIAdministrativeState_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNIAdministrativeState=_ZxGponGemPortIpPortCfgDataUNIAdministrativeState_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,7),_ZxGponGemPortIpPortCfgDataUNIAdministrativeState_Type())
zxGponGemPortIpPortCfgDataUNIAdministrativeState.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNIAdministrativeState.setStatus(_A)
class _ZxGponGemPortIpPortCfgDataUNIPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_n,2)))
_ZxGponGemPortIpPortCfgDataUNIPortState_Type.__name__=_E
_ZxGponGemPortIpPortCfgDataUNIPortState_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNIPortState=_ZxGponGemPortIpPortCfgDataUNIPortState_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,8),_ZxGponGemPortIpPortCfgDataUNIPortState_Type())
zxGponGemPortIpPortCfgDataUNIPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNIPortState.setStatus(_A)
_ZxGponGemPortIpPortCfgDataUNIAllowRemoteAccess_Type=TruthValue
_ZxGponGemPortIpPortCfgDataUNIAllowRemoteAccess_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNIAllowRemoteAccess=_ZxGponGemPortIpPortCfgDataUNIAllowRemoteAccess_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,9),_ZxGponGemPortIpPortCfgDataUNIAllowRemoteAccess_Type())
zxGponGemPortIpPortCfgDataUNIAllowRemoteAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNIAllowRemoteAccess.setStatus(_A)
class _ZxGponGemPortIpPortCfgDataUNIEncapsulationMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_w,2)))
_ZxGponGemPortIpPortCfgDataUNIEncapsulationMethod_Type.__name__=_E
_ZxGponGemPortIpPortCfgDataUNIEncapsulationMethod_Object=MibTableColumn
zxGponGemPortIpPortCfgDataUNIEncapsulationMethod=_ZxGponGemPortIpPortCfgDataUNIEncapsulationMethod_Object((1,3,6,1,4,1,3902,1012,3,30,11,1,10),_ZxGponGemPortIpPortCfgDataUNIEncapsulationMethod_Type())
zxGponGemPortIpPortCfgDataUNIEncapsulationMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIpPortCfgDataUNIEncapsulationMethod.setStatus(_A)
_ZxGponGemPortIWTPMACBriPortFilterTableInfoTable_Object=MibTable
zxGponGemPortIWTPMACBriPortFilterTableInfoTable=_ZxGponGemPortIWTPMACBriPortFilterTableInfoTable_Object((1,3,6,1,4,1,3902,1012,3,30,12))
if mibBuilder.loadTexts:zxGponGemPortIWTPMACBriPortFilterTableInfoTable.setStatus(_A)
_ZxGponGemPortIWTPMACBriPortFilterTableInfoEntry_Object=MibTableRow
zxGponGemPortIWTPMACBriPortFilterTableInfoEntry=_ZxGponGemPortIWTPMACBriPortFilterTableInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,30,12,1))
zxGponGemPortIWTPMACBriPortFilterTableInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P),(0,_B,_Aw))
if mibBuilder.loadTexts:zxGponGemPortIWTPMACBriPortFilterTableInfoEntry.setStatus(_A)
_ZxGponGemPortIWTPMACBriPortFilterTableMacAddr_Type=MacAddress
_ZxGponGemPortIWTPMACBriPortFilterTableMacAddr_Object=MibTableColumn
zxGponGemPortIWTPMACBriPortFilterTableMacAddr=_ZxGponGemPortIWTPMACBriPortFilterTableMacAddr_Object((1,3,6,1,4,1,3902,1012,3,30,12,1,1),_ZxGponGemPortIWTPMACBriPortFilterTableMacAddr_Type())
zxGponGemPortIWTPMACBriPortFilterTableMacAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponGemPortIWTPMACBriPortFilterTableMacAddr.setStatus(_A)
class _ZxGponGemPortIWTPMACBriPortFilterTableAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_k,2)))
_ZxGponGemPortIWTPMACBriPortFilterTableAction_Type.__name__=_E
_ZxGponGemPortIWTPMACBriPortFilterTableAction_Object=MibTableColumn
zxGponGemPortIWTPMACBriPortFilterTableAction=_ZxGponGemPortIWTPMACBriPortFilterTableAction_Object((1,3,6,1,4,1,3902,1012,3,30,12,1,2),_ZxGponGemPortIWTPMACBriPortFilterTableAction_Type())
zxGponGemPortIWTPMACBriPortFilterTableAction.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortIWTPMACBriPortFilterTableAction.setStatus(_A)
_ZxGponGemPortIWTPMACBriPortFilterTableEntryStatus_Type=RowStatus
_ZxGponGemPortIWTPMACBriPortFilterTableEntryStatus_Object=MibTableColumn
zxGponGemPortIWTPMACBriPortFilterTableEntryStatus=_ZxGponGemPortIWTPMACBriPortFilterTableEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,30,12,1,3),_ZxGponGemPortIWTPMACBriPortFilterTableEntryStatus_Type())
zxGponGemPortIWTPMACBriPortFilterTableEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponGemPortIWTPMACBriPortFilterTableEntryStatus.setStatus(_A)
_ZxGponGemPortUNIMACBriPortFilterTableInfoTable_Object=MibTable
zxGponGemPortUNIMACBriPortFilterTableInfoTable=_ZxGponGemPortUNIMACBriPortFilterTableInfoTable_Object((1,3,6,1,4,1,3902,1012,3,30,13))
if mibBuilder.loadTexts:zxGponGemPortUNIMACBriPortFilterTableInfoTable.setStatus(_A)
_ZxGponGemPortUNIMACBriPortFilterTableInfoEntry_Object=MibTableRow
zxGponGemPortUNIMACBriPortFilterTableInfoEntry=_ZxGponGemPortUNIMACBriPortFilterTableInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,30,13,1))
zxGponGemPortUNIMACBriPortFilterTableInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_a),(0,_B,_Ax))
if mibBuilder.loadTexts:zxGponGemPortUNIMACBriPortFilterTableInfoEntry.setStatus(_A)
_ZxGponGemPortUNIMACBriPortFilterTableMacAddr_Type=MacAddress
_ZxGponGemPortUNIMACBriPortFilterTableMacAddr_Object=MibTableColumn
zxGponGemPortUNIMACBriPortFilterTableMacAddr=_ZxGponGemPortUNIMACBriPortFilterTableMacAddr_Object((1,3,6,1,4,1,3902,1012,3,30,13,1,1),_ZxGponGemPortUNIMACBriPortFilterTableMacAddr_Type())
zxGponGemPortUNIMACBriPortFilterTableMacAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:zxGponGemPortUNIMACBriPortFilterTableMacAddr.setStatus(_A)
class _ZxGponGemPortUNIMACBriPortFilterTableAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_k,2)))
_ZxGponGemPortUNIMACBriPortFilterTableAction_Type.__name__=_E
_ZxGponGemPortUNIMACBriPortFilterTableAction_Object=MibTableColumn
zxGponGemPortUNIMACBriPortFilterTableAction=_ZxGponGemPortUNIMACBriPortFilterTableAction_Object((1,3,6,1,4,1,3902,1012,3,30,13,1,2),_ZxGponGemPortUNIMACBriPortFilterTableAction_Type())
zxGponGemPortUNIMACBriPortFilterTableAction.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortUNIMACBriPortFilterTableAction.setStatus(_A)
_ZxGponGemPortUNIMACBriPortFilterTableEntryStatus_Type=RowStatus
_ZxGponGemPortUNIMACBriPortFilterTableEntryStatus_Object=MibTableColumn
zxGponGemPortUNIMACBriPortFilterTableEntryStatus=_ZxGponGemPortUNIMACBriPortFilterTableEntryStatus_Object((1,3,6,1,4,1,3902,1012,3,30,13,1,3),_ZxGponGemPortUNIMACBriPortFilterTableEntryStatus_Type())
zxGponGemPortUNIMACBriPortFilterTableEntryStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:zxGponGemPortUNIMACBriPortFilterTableEntryStatus.setStatus(_A)
_ZxGponGemPortWeightTable_Object=MibTable
zxGponGemPortWeightTable=_ZxGponGemPortWeightTable_Object((1,3,6,1,4,1,3902,1012,3,30,14))
if mibBuilder.loadTexts:zxGponGemPortWeightTable.setStatus(_A)
_ZxGponGemPortWeightEntry_Object=MibTableRow
zxGponGemPortWeightEntry=_ZxGponGemPortWeightEntry_Object((1,3,6,1,4,1,3902,1012,3,30,14,1))
zxGponGemPortWeightEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGemPortWeightEntry.setStatus(_A)
class _ZxGponGemPortSchedulemode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_c,0),('sp',1),(_g,2)))
_ZxGponGemPortSchedulemode_Type.__name__=_E
_ZxGponGemPortSchedulemode_Object=MibTableColumn
zxGponGemPortSchedulemode=_ZxGponGemPortSchedulemode_Object((1,3,6,1,4,1,3902,1012,3,30,14,1,1),_ZxGponGemPortSchedulemode_Type())
zxGponGemPortSchedulemode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortSchedulemode.setStatus(_A)
_ZxGponGemPortCos1Weight_Type=Integer32
_ZxGponGemPortCos1Weight_Object=MibTableColumn
zxGponGemPortCos1Weight=_ZxGponGemPortCos1Weight_Object((1,3,6,1,4,1,3902,1012,3,30,14,1,2),_ZxGponGemPortCos1Weight_Type())
zxGponGemPortCos1Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortCos1Weight.setStatus(_A)
_ZxGponGemPortCos2Weight_Type=Integer32
_ZxGponGemPortCos2Weight_Object=MibTableColumn
zxGponGemPortCos2Weight=_ZxGponGemPortCos2Weight_Object((1,3,6,1,4,1,3902,1012,3,30,14,1,3),_ZxGponGemPortCos2Weight_Type())
zxGponGemPortCos2Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortCos2Weight.setStatus(_A)
_ZxGponGemPortCos3Weight_Type=Integer32
_ZxGponGemPortCos3Weight_Object=MibTableColumn
zxGponGemPortCos3Weight=_ZxGponGemPortCos3Weight_Object((1,3,6,1,4,1,3902,1012,3,30,14,1,4),_ZxGponGemPortCos3Weight_Type())
zxGponGemPortCos3Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortCos3Weight.setStatus(_A)
_ZxGponGemPortCos4Weight_Type=Integer32
_ZxGponGemPortCos4Weight_Object=MibTableColumn
zxGponGemPortCos4Weight=_ZxGponGemPortCos4Weight_Object((1,3,6,1,4,1,3902,1012,3,30,14,1,5),_ZxGponGemPortCos4Weight_Type())
zxGponGemPortCos4Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortCos4Weight.setStatus(_A)
_ZxGponGemPortPrioReGenTable_Object=MibTable
zxGponGemPortPrioReGenTable=_ZxGponGemPortPrioReGenTable_Object((1,3,6,1,4,1,3902,1012,3,30,20))
if mibBuilder.loadTexts:zxGponGemPortPrioReGenTable.setStatus(_A)
_ZxGponGemPortPrioReGenEntry_Object=MibTableRow
zxGponGemPortPrioReGenEntry=_ZxGponGemPortPrioReGenEntry_Object((1,3,6,1,4,1,3902,1012,3,30,20,1))
zxGponGemPortPrioReGenEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGemPortPrioReGenEntry.setStatus(_A)
class _ZxGponGemPortPrioReGenMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('svlan',1),('cvlan',2),(_q,3)))
_ZxGponGemPortPrioReGenMode_Type.__name__=_E
_ZxGponGemPortPrioReGenMode_Object=MibTableColumn
zxGponGemPortPrioReGenMode=_ZxGponGemPortPrioReGenMode_Object((1,3,6,1,4,1,3902,1012,3,30,20,1,1),_ZxGponGemPortPrioReGenMode_Type())
zxGponGemPortPrioReGenMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPrioReGenMode.setStatus(_A)
class _ZxGponGemPortPrioReGenMap0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxGponGemPortPrioReGenMap0_Type.__name__=_E
_ZxGponGemPortPrioReGenMap0_Object=MibTableColumn
zxGponGemPortPrioReGenMap0=_ZxGponGemPortPrioReGenMap0_Object((1,3,6,1,4,1,3902,1012,3,30,20,1,2),_ZxGponGemPortPrioReGenMap0_Type())
zxGponGemPortPrioReGenMap0.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPrioReGenMap0.setStatus(_A)
class _ZxGponGemPortPrioReGenMap1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxGponGemPortPrioReGenMap1_Type.__name__=_E
_ZxGponGemPortPrioReGenMap1_Object=MibTableColumn
zxGponGemPortPrioReGenMap1=_ZxGponGemPortPrioReGenMap1_Object((1,3,6,1,4,1,3902,1012,3,30,20,1,3),_ZxGponGemPortPrioReGenMap1_Type())
zxGponGemPortPrioReGenMap1.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPrioReGenMap1.setStatus(_A)
class _ZxGponGemPortPrioReGenMap2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxGponGemPortPrioReGenMap2_Type.__name__=_E
_ZxGponGemPortPrioReGenMap2_Object=MibTableColumn
zxGponGemPortPrioReGenMap2=_ZxGponGemPortPrioReGenMap2_Object((1,3,6,1,4,1,3902,1012,3,30,20,1,4),_ZxGponGemPortPrioReGenMap2_Type())
zxGponGemPortPrioReGenMap2.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPrioReGenMap2.setStatus(_A)
class _ZxGponGemPortPrioReGenMap3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxGponGemPortPrioReGenMap3_Type.__name__=_E
_ZxGponGemPortPrioReGenMap3_Object=MibTableColumn
zxGponGemPortPrioReGenMap3=_ZxGponGemPortPrioReGenMap3_Object((1,3,6,1,4,1,3902,1012,3,30,20,1,5),_ZxGponGemPortPrioReGenMap3_Type())
zxGponGemPortPrioReGenMap3.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPrioReGenMap3.setStatus(_A)
class _ZxGponGemPortPrioReGenMap4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxGponGemPortPrioReGenMap4_Type.__name__=_E
_ZxGponGemPortPrioReGenMap4_Object=MibTableColumn
zxGponGemPortPrioReGenMap4=_ZxGponGemPortPrioReGenMap4_Object((1,3,6,1,4,1,3902,1012,3,30,20,1,6),_ZxGponGemPortPrioReGenMap4_Type())
zxGponGemPortPrioReGenMap4.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPrioReGenMap4.setStatus(_A)
class _ZxGponGemPortPrioReGenMap5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxGponGemPortPrioReGenMap5_Type.__name__=_E
_ZxGponGemPortPrioReGenMap5_Object=MibTableColumn
zxGponGemPortPrioReGenMap5=_ZxGponGemPortPrioReGenMap5_Object((1,3,6,1,4,1,3902,1012,3,30,20,1,7),_ZxGponGemPortPrioReGenMap5_Type())
zxGponGemPortPrioReGenMap5.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPrioReGenMap5.setStatus(_A)
class _ZxGponGemPortPrioReGenMap6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxGponGemPortPrioReGenMap6_Type.__name__=_E
_ZxGponGemPortPrioReGenMap6_Object=MibTableColumn
zxGponGemPortPrioReGenMap6=_ZxGponGemPortPrioReGenMap6_Object((1,3,6,1,4,1,3902,1012,3,30,20,1,8),_ZxGponGemPortPrioReGenMap6_Type())
zxGponGemPortPrioReGenMap6.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPrioReGenMap6.setStatus(_A)
class _ZxGponGemPortPrioReGenMap7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxGponGemPortPrioReGenMap7_Type.__name__=_E
_ZxGponGemPortPrioReGenMap7_Object=MibTableColumn
zxGponGemPortPrioReGenMap7=_ZxGponGemPortPrioReGenMap7_Object((1,3,6,1,4,1,3902,1012,3,30,20,1,9),_ZxGponGemPortPrioReGenMap7_Type())
zxGponGemPortPrioReGenMap7.setMaxAccess(_D)
if mibBuilder.loadTexts:zxGponGemPortPrioReGenMap7.setStatus(_A)
_ZxGponGemPortStaticsTable_Object=MibTable
zxGponGemPortStaticsTable=_ZxGponGemPortStaticsTable_Object((1,3,6,1,4,1,3902,1012,3,30,21))
if mibBuilder.loadTexts:zxGponGemPortStaticsTable.setStatus(_A)
_ZxGponGemPortStaticsEntry_Object=MibTableRow
zxGponGemPortStaticsEntry=_ZxGponGemPortStaticsEntry_Object((1,3,6,1,4,1,3902,1012,3,30,21,1))
zxGponGemPortStaticsEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGemPortStaticsEntry.setStatus(_A)
_ZxGponGemPortUpUcastPkts_Type=Unsigned32
_ZxGponGemPortUpUcastPkts_Object=MibTableColumn
zxGponGemPortUpUcastPkts=_ZxGponGemPortUpUcastPkts_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,1),_ZxGponGemPortUpUcastPkts_Type())
zxGponGemPortUpUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpUcastPkts.setStatus(_A)
_ZxGponGemPortUpMcastPkts_Type=Unsigned32
_ZxGponGemPortUpMcastPkts_Object=MibTableColumn
zxGponGemPortUpMcastPkts=_ZxGponGemPortUpMcastPkts_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,2),_ZxGponGemPortUpMcastPkts_Type())
zxGponGemPortUpMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpMcastPkts.setStatus(_A)
_ZxGponGemPortUpBcastPkts_Type=Unsigned32
_ZxGponGemPortUpBcastPkts_Object=MibTableColumn
zxGponGemPortUpBcastPkts=_ZxGponGemPortUpBcastPkts_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,3),_ZxGponGemPortUpBcastPkts_Type())
zxGponGemPortUpBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpBcastPkts.setStatus(_A)
_ZxGponGemPortUpPassedBytes_Type=Unsigned32
_ZxGponGemPortUpPassedBytes_Object=MibTableColumn
zxGponGemPortUpPassedBytes=_ZxGponGemPortUpPassedBytes_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,4),_ZxGponGemPortUpPassedBytes_Type())
zxGponGemPortUpPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpPassedBytes.setStatus(_A)
_ZxGponGemPortUpDroppedPkts_Type=Unsigned32
_ZxGponGemPortUpDroppedPkts_Object=MibTableColumn
zxGponGemPortUpDroppedPkts=_ZxGponGemPortUpDroppedPkts_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,5),_ZxGponGemPortUpDroppedPkts_Type())
zxGponGemPortUpDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpDroppedPkts.setStatus(_A)
_ZxGponGemPortDownUcastPkts_Type=Unsigned32
_ZxGponGemPortDownUcastPkts_Object=MibTableColumn
zxGponGemPortDownUcastPkts=_ZxGponGemPortDownUcastPkts_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,6),_ZxGponGemPortDownUcastPkts_Type())
zxGponGemPortDownUcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownUcastPkts.setStatus(_A)
_ZxGponGemPortDownMcastPkts_Type=Unsigned32
_ZxGponGemPortDownMcastPkts_Object=MibTableColumn
zxGponGemPortDownMcastPkts=_ZxGponGemPortDownMcastPkts_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,7),_ZxGponGemPortDownMcastPkts_Type())
zxGponGemPortDownMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownMcastPkts.setStatus(_A)
_ZxGponGemPortDownBcastPkts_Type=Unsigned32
_ZxGponGemPortDownBcastPkts_Object=MibTableColumn
zxGponGemPortDownBcastPkts=_ZxGponGemPortDownBcastPkts_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,8),_ZxGponGemPortDownBcastPkts_Type())
zxGponGemPortDownBcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownBcastPkts.setStatus(_A)
_ZxGponGemPortDownPassedBytes_Type=Unsigned32
_ZxGponGemPortDownPassedBytes_Object=MibTableColumn
zxGponGemPortDownPassedBytes=_ZxGponGemPortDownPassedBytes_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,9),_ZxGponGemPortDownPassedBytes_Type())
zxGponGemPortDownPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownPassedBytes.setStatus(_A)
_ZxGponGemPortDownDroppedPkts_Type=Unsigned32
_ZxGponGemPortDownDroppedPkts_Object=MibTableColumn
zxGponGemPortDownDroppedPkts=_ZxGponGemPortDownDroppedPkts_Object((1,3,6,1,4,1,3902,1012,3,30,21,1,10),_ZxGponGemPortDownDroppedPkts_Type())
zxGponGemPortDownDroppedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownDroppedPkts.setStatus(_A)
_ZxGponGemPortStaticsHistoryInfoTable_Object=MibTable
zxGponGemPortStaticsHistoryInfoTable=_ZxGponGemPortStaticsHistoryInfoTable_Object((1,3,6,1,4,1,3902,1012,3,30,22))
if mibBuilder.loadTexts:zxGponGemPortStaticsHistoryInfoTable.setStatus(_A)
_ZxGponGemPortStaticsHistoryInfoEntry_Object=MibTableRow
zxGponGemPortStaticsHistoryInfoEntry=_ZxGponGemPortStaticsHistoryInfoEntry_Object((1,3,6,1,4,1,3902,1012,3,30,22,1))
zxGponGemPortStaticsHistoryInfoEntry.setIndexNames((0,_B,_F),(0,_B,_I),(0,_B,_P))
if mibBuilder.loadTexts:zxGponGemPortStaticsHistoryInfoEntry.setStatus(_A)
_ZxGponGemPortUpUcastPktsHistoryInfo_Type=Unsigned32
_ZxGponGemPortUpUcastPktsHistoryInfo_Object=MibTableColumn
zxGponGemPortUpUcastPktsHistoryInfo=_ZxGponGemPortUpUcastPktsHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,1),_ZxGponGemPortUpUcastPktsHistoryInfo_Type())
zxGponGemPortUpUcastPktsHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpUcastPktsHistoryInfo.setStatus(_A)
_ZxGponGemPortUpMcastPktsHistoryInfo_Type=Unsigned32
_ZxGponGemPortUpMcastPktsHistoryInfo_Object=MibTableColumn
zxGponGemPortUpMcastPktsHistoryInfo=_ZxGponGemPortUpMcastPktsHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,2),_ZxGponGemPortUpMcastPktsHistoryInfo_Type())
zxGponGemPortUpMcastPktsHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpMcastPktsHistoryInfo.setStatus(_A)
_ZxGponGemPortUpBcastPktsHistoryInfo_Type=Unsigned32
_ZxGponGemPortUpBcastPktsHistoryInfo_Object=MibTableColumn
zxGponGemPortUpBcastPktsHistoryInfo=_ZxGponGemPortUpBcastPktsHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,3),_ZxGponGemPortUpBcastPktsHistoryInfo_Type())
zxGponGemPortUpBcastPktsHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpBcastPktsHistoryInfo.setStatus(_A)
_ZxGponGemPortUpPassedBytesHistoryInfo_Type=Unsigned32
_ZxGponGemPortUpPassedBytesHistoryInfo_Object=MibTableColumn
zxGponGemPortUpPassedBytesHistoryInfo=_ZxGponGemPortUpPassedBytesHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,4),_ZxGponGemPortUpPassedBytesHistoryInfo_Type())
zxGponGemPortUpPassedBytesHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpPassedBytesHistoryInfo.setStatus(_A)
_ZxGponGemPortUpDroppedPktsHistoryInfo_Type=Unsigned32
_ZxGponGemPortUpDroppedPktsHistoryInfo_Object=MibTableColumn
zxGponGemPortUpDroppedPktsHistoryInfo=_ZxGponGemPortUpDroppedPktsHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,5),_ZxGponGemPortUpDroppedPktsHistoryInfo_Type())
zxGponGemPortUpDroppedPktsHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortUpDroppedPktsHistoryInfo.setStatus(_A)
_ZxGponGemPortDownUcastPktsHistoryInfo_Type=Unsigned32
_ZxGponGemPortDownUcastPktsHistoryInfo_Object=MibTableColumn
zxGponGemPortDownUcastPktsHistoryInfo=_ZxGponGemPortDownUcastPktsHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,6),_ZxGponGemPortDownUcastPktsHistoryInfo_Type())
zxGponGemPortDownUcastPktsHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownUcastPktsHistoryInfo.setStatus(_A)
_ZxGponGemPortDownMcastPktsHistoryInfo_Type=Unsigned32
_ZxGponGemPortDownMcastPktsHistoryInfo_Object=MibTableColumn
zxGponGemPortDownMcastPktsHistoryInfo=_ZxGponGemPortDownMcastPktsHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,7),_ZxGponGemPortDownMcastPktsHistoryInfo_Type())
zxGponGemPortDownMcastPktsHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownMcastPktsHistoryInfo.setStatus(_A)
_ZxGponGemPortDownBcastPktsHistoryInfo_Type=Unsigned32
_ZxGponGemPortDownBcastPktsHistoryInfo_Object=MibTableColumn
zxGponGemPortDownBcastPktsHistoryInfo=_ZxGponGemPortDownBcastPktsHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,8),_ZxGponGemPortDownBcastPktsHistoryInfo_Type())
zxGponGemPortDownBcastPktsHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownBcastPktsHistoryInfo.setStatus(_A)
_ZxGponGemPortDownPassedBytesHistoryInfo_Type=Unsigned32
_ZxGponGemPortDownPassedBytesHistoryInfo_Object=MibTableColumn
zxGponGemPortDownPassedBytesHistoryInfo=_ZxGponGemPortDownPassedBytesHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,9),_ZxGponGemPortDownPassedBytesHistoryInfo_Type())
zxGponGemPortDownPassedBytesHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownPassedBytesHistoryInfo.setStatus(_A)
_ZxGponGemPortDownDroppedPktsHistoryInfo_Type=Unsigned32
_ZxGponGemPortDownDroppedPktsHistoryInfo_Object=MibTableColumn
zxGponGemPortDownDroppedPktsHistoryInfo=_ZxGponGemPortDownDroppedPktsHistoryInfo_Object((1,3,6,1,4,1,3902,1012,3,30,22,1,10),_ZxGponGemPortDownDroppedPktsHistoryInfo_Type())
zxGponGemPortDownDroppedPktsHistoryInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponGemPortDownDroppedPktsHistoryInfo.setStatus(_A)
_ZxGponMacSpoofingObjects_ObjectIdentity=ObjectIdentity
zxGponMacSpoofingObjects=_ZxGponMacSpoofingObjects_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,40))
_ZxGponSpoofingPort_Type=Integer32
_ZxGponSpoofingPort_Object=MibScalar
zxGponSpoofingPort=_ZxGponSpoofingPort_Object((1,3,6,1,4,1,3902,1012,3,40,1),_ZxGponSpoofingPort_Type())
zxGponSpoofingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpoofingPort.setStatus(_A)
_ZxGponSpoofingMac_Type=MacAddress
_ZxGponSpoofingMac_Object=MibScalar
zxGponSpoofingMac=_ZxGponSpoofingMac_Object((1,3,6,1,4,1,3902,1012,3,40,2),_ZxGponSpoofingMac_Type())
zxGponSpoofingMac.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpoofingMac.setStatus(_A)
_ZxGponSpoofingVlan_Type=VlanId
_ZxGponSpoofingVlan_Object=MibScalar
zxGponSpoofingVlan=_ZxGponSpoofingVlan_Object((1,3,6,1,4,1,3902,1012,3,40,3),_ZxGponSpoofingVlan_Type())
zxGponSpoofingVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpoofingVlan.setStatus(_A)
_ZxGponSpoofingConflictPort_Type=Integer32
_ZxGponSpoofingConflictPort_Object=MibScalar
zxGponSpoofingConflictPort=_ZxGponSpoofingConflictPort_Object((1,3,6,1,4,1,3902,1012,3,40,4),_ZxGponSpoofingConflictPort_Type())
zxGponSpoofingConflictPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponSpoofingConflictPort.setStatus(_A)
_ZxGponTraps_ObjectIdentity=ObjectIdentity
zxGponTraps=_ZxGponTraps_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,45))
_ZxGponTrapsBindVar_ObjectIdentity=ObjectIdentity
zxGponTrapsBindVar=_ZxGponTrapsBindVar_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,45,1))
class _ZxGponOltRxPowerAlarmiReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_p,2)))
_ZxGponOltRxPowerAlarmiReason_Type.__name__=_E
_ZxGponOltRxPowerAlarmiReason_Object=MibScalar
zxGponOltRxPowerAlarmiReason=_ZxGponOltRxPowerAlarmiReason_Object((1,3,6,1,4,1,3902,1012,3,45,1,1),_ZxGponOltRxPowerAlarmiReason_Type())
zxGponOltRxPowerAlarmiReason.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltRxPowerAlarmiReason.setStatus(_A)
class _ZxGponOltRxPowerAbnormalInformiReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_p,2)))
_ZxGponOltRxPowerAbnormalInformiReason_Type.__name__=_E
_ZxGponOltRxPowerAbnormalInformiReason_Object=MibScalar
zxGponOltRxPowerAbnormalInformiReason=_ZxGponOltRxPowerAbnormalInformiReason_Object((1,3,6,1,4,1,3902,1012,3,45,1,2),_ZxGponOltRxPowerAbnormalInformiReason_Type())
zxGponOltRxPowerAbnormalInformiReason.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltRxPowerAbnormalInformiReason.setStatus(_A)
class _ZxGponOltTxPowerAlarmReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_p,2)))
_ZxGponOltTxPowerAlarmReason_Type.__name__=_E
_ZxGponOltTxPowerAlarmReason_Object=MibScalar
zxGponOltTxPowerAlarmReason=_ZxGponOltTxPowerAlarmReason_Object((1,3,6,1,4,1,3902,1012,3,45,1,3),_ZxGponOltTxPowerAlarmReason_Type())
zxGponOltTxPowerAlarmReason.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltTxPowerAlarmReason.setStatus(_A)
class _ZxGponOltTxPowerAbnormalInformReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_o,1),(_p,2)))
_ZxGponOltTxPowerAbnormalInformReason_Type.__name__=_E
_ZxGponOltTxPowerAbnormalInformReason_Object=MibScalar
zxGponOltTxPowerAbnormalInformReason=_ZxGponOltTxPowerAbnormalInformReason_Object((1,3,6,1,4,1,3902,1012,3,45,1,4),_ZxGponOltTxPowerAbnormalInformReason_Type())
zxGponOltTxPowerAbnormalInformReason.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponOltTxPowerAbnormalInformReason.setStatus(_A)
class _ZxGponTrapEventString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ZxGponTrapEventString_Type.__name__=_O
_ZxGponTrapEventString_Object=MibScalar
zxGponTrapEventString=_ZxGponTrapEventString_Object((1,3,6,1,4,1,3902,1012,3,45,1,5),_ZxGponTrapEventString_Type())
zxGponTrapEventString.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTrapEventString.setStatus(_A)
_ZxGponTermination_ObjectIdentity=ObjectIdentity
zxGponTermination=_ZxGponTermination_ObjectIdentity((1,3,6,1,4,1,3902,1012,3,100))
_ZxGponTerminationDummy_Type=Integer32
_ZxGponTerminationDummy_Object=MibScalar
zxGponTerminationDummy=_ZxGponTerminationDummy_Object((1,3,6,1,4,1,3902,1012,3,100,1),_ZxGponTerminationDummy_Type())
zxGponTerminationDummy.setMaxAccess(_C)
if mibBuilder.loadTexts:zxGponTerminationDummy.setStatus(_A)
zxGponOltLOSi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,101))
zxGponOltLOSi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLOSi.setStatus(_A)
zxGponOltLosiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,102))
zxGponOltLosiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLosiRestore.setStatus(_A)
zxGponOltLOFi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,103))
zxGponOltLOFi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLOFi.setStatus(_A)
zxGponOltLOFiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,104))
zxGponOltLOFiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLOFiRestore.setStatus(_A)
zxGponOltDOWi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,105))
zxGponOltDOWi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltDOWi.setStatus(_A)
zxGponOltDOWiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,106))
zxGponOltDOWiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltDOWiRestore.setStatus(_A)
zxGponOltSFi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,107))
zxGponOltSFi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltSFi.setStatus(_A)
zxGponOltSFiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,108))
zxGponOltSFiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltSFiRestore.setStatus(_A)
zxGponOltSDi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,109))
zxGponOltSDi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltSDi.setStatus(_A)
zxGponOltSDiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,110))
zxGponOltSDiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltSDiRestore.setStatus(_A)
zxGponOltLCDAi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,111))
zxGponOltLCDAi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLCDAi.setStatus(_A)
zxGponOltLCDAiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,112))
zxGponOltLCDAiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLCDAiRestore.setStatus(_A)
zxGponOltLCDGi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,113))
zxGponOltLCDGi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLCDGi.setStatus(_A)
zxGponOltLCDGiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,114))
zxGponOltLCDGiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLCDGiRestore.setStatus(_A)
zxGponOltRDIi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,115))
zxGponOltRDIi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltRDIi.setStatus(_A)
zxGponOltRDIiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,116))
zxGponOltRDIiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltRDIiRestore.setStatus(_A)
zxGponOltSUFi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,117))
zxGponOltSUFi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltSUFi.setStatus(_A)
zxGponOltSUFiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,118))
zxGponOltSUFiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltSUFiRestore.setStatus(_A)
zxGponOltDFi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,119))
zxGponOltDFi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltDFi.setStatus(_A)
zxGponOltDFiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,120))
zxGponOltDFiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltDFiRestore.setStatus(_A)
zxGponOltLOAi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,121))
zxGponOltLOAi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLOAi.setStatus(_A)
zxGponOltLOAiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,122))
zxGponOltLOAiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLOAiRestore.setStatus(_A)
zxGponOltDGi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,123))
zxGponOltDGi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltDGi.setStatus(_A)
zxGponOltDGiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,124))
zxGponOltDGiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltDGiRestore.setStatus(_A)
zxGponOltLOAMi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,125))
zxGponOltLOAMi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLOAMi.setStatus(_A)
zxGponOltLOAMiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,126))
zxGponOltLOAMiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltLOAMiRestore.setStatus(_A)
zxGponOltMEMi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,127))
zxGponOltMEMi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltMEMi.setStatus(_A)
zxGponOltMEMiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,128))
zxGponOltMEMiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltMEMiRestore.setStatus(_A)
zxGponOltMISi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,129))
zxGponOltMISi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltMISi.setStatus(_A)
zxGponOltMISiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,130))
zxGponOltMISiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltMISiRestore.setStatus(_A)
zxGponOltPEEi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,131))
zxGponOltPEEi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltPEEi.setStatus(_A)
zxGponOltPEEiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,132))
zxGponOltPEEiRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltPEEiRestore.setStatus(_A)
zxGponOntLOS=NotificationType((1,3,6,1,4,1,3902,1012,3,45,133))
zxGponOntLOS.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntLOS.setStatus(_A)
zxGponOntLOSRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,134))
zxGponOntLOSRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntLOSRestore.setStatus(_A)
zxGponOntLOF=NotificationType((1,3,6,1,4,1,3902,1012,3,45,135))
zxGponOntLOF.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntLOF.setStatus(_A)
zxGponOntLOFRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,136))
zxGponOntLOFRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntLOFRestore.setStatus(_A)
zxGponOntTF=NotificationType((1,3,6,1,4,1,3902,1012,3,45,137))
zxGponOntTF.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntTF.setStatus(_A)
zxGponOntTFRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,138))
zxGponOntTFRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntTFRestore.setStatus(_A)
zxGponOntSF=NotificationType((1,3,6,1,4,1,3902,1012,3,45,139))
zxGponOntSF.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntSF.setStatus(_A)
zxGponOntSFRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,140))
zxGponOntSFRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntSFRestore.setStatus(_A)
zxGponOntSD=NotificationType((1,3,6,1,4,1,3902,1012,3,45,141))
zxGponOntSD.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntSD.setStatus(_A)
zxGponOntSDRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,142))
zxGponOntSDRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntSDRestore.setStatus(_A)
zxGponOntLCDA=NotificationType((1,3,6,1,4,1,3902,1012,3,45,143))
zxGponOntLCDA.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntLCDA.setStatus(_A)
zxGponOntLCDARestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,144))
zxGponOntLCDARestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntLCDARestore.setStatus(_A)
zxGponOntLCDG=NotificationType((1,3,6,1,4,1,3902,1012,3,45,145))
zxGponOntLCDG.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntLCDG.setStatus(_A)
zxGponOntLCDGRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,146))
zxGponOntLCDGRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntLCDGRestore.setStatus(_A)
zxGponOntRDI=NotificationType((1,3,6,1,4,1,3902,1012,3,45,147))
zxGponOntRDI.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntRDI.setStatus(_A)
zxGponOntRDIRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,148))
zxGponOntRDIRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntRDIRestore.setStatus(_A)
zxGponOntSUF=NotificationType((1,3,6,1,4,1,3902,1012,3,45,149))
zxGponOntSUF.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntSUF.setStatus(_A)
zxGponOntSUFRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,150))
zxGponOntSUFRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntSUFRestore.setStatus(_A)
zxGponOntMEM=NotificationType((1,3,6,1,4,1,3902,1012,3,45,151))
zxGponOntMEM.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntMEM.setStatus(_A)
zxGponOntMEMRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,152))
zxGponOntMEMRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntMEMRestore.setStatus(_A)
zxGponOntDACT=NotificationType((1,3,6,1,4,1,3902,1012,3,45,153))
zxGponOntDACT.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntDACT.setStatus(_A)
zxGponOntDACTRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,154))
zxGponOntDACTRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntDACTRestore.setStatus(_A)
zxGponOntDIS=NotificationType((1,3,6,1,4,1,3902,1012,3,45,155))
zxGponOntDIS.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntDIS.setStatus(_A)
zxGponOntDISRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,156))
zxGponOntDISRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntDISRestore.setStatus(_A)
zxGponOntMIS=NotificationType((1,3,6,1,4,1,3902,1012,3,45,157))
zxGponOntMIS.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntMIS.setStatus(_A)
zxGponOntMISRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,158))
zxGponOntMISRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntMISRestore.setStatus(_A)
zxGponOntPee=NotificationType((1,3,6,1,4,1,3902,1012,3,45,159))
zxGponOntPee.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntPee.setStatus(_A)
zxGponOntPeeRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,160))
zxGponOntPeeRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntPeeRestore.setStatus(_A)
zxGponOltLOS=NotificationType((1,3,6,1,4,1,3902,1012,3,45,161))
zxGponOltLOS.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOltLOS.setStatus(_A)
zxGponOltLOSRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,162))
zxGponOltLOSRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOltLOSRestore.setStatus(_A)
zxGponOltLOF=NotificationType((1,3,6,1,4,1,3902,1012,3,45,163))
zxGponOltLOF.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOltLOF.setStatus(_A)
zxGponOltLOFRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,164))
zxGponOltLOFRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOltLOFRestore.setStatus(_A)
zxGponOntRegister=NotificationType((1,3,6,1,4,1,3902,1012,3,45,165))
zxGponOntRegister.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntRegister.setStatus(_A)
zxGponOntUnregister=NotificationType((1,3,6,1,4,1,3902,1012,3,45,166))
zxGponOntUnregister.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntUnregister.setStatus(_A)
zxGponOntAuthPass=NotificationType((1,3,6,1,4,1,3902,1012,3,45,167))
zxGponOntAuthPass.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntAuthPass.setStatus(_A)
zxGponOntAuthFailed=NotificationType((1,3,6,1,4,1,3902,1012,3,45,168))
zxGponOntAuthFailed.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOntAuthFailed.setStatus(_A)
zxPonFanOffLine=NotificationType((1,3,6,1,4,1,3902,1012,3,45,171))
zxPonFanOffLine.setObjects((_G,_H))
if mibBuilder.loadTexts:zxPonFanOffLine.setStatus(_A)
zxPonFanOffLineRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,172))
zxPonFanOffLineRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxPonFanOffLineRestore.setStatus(_A)
zxGponLinkOntDyingGasp=NotificationType((1,3,6,1,4,1,3902,1012,3,45,173))
zxGponLinkOntDyingGasp.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponLinkOntDyingGasp.setStatus(_A)
zxGponLinkOntDyingGaspRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,174))
zxGponLinkOntDyingGaspRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponLinkOntDyingGaspRestore.setStatus(_A)
zxGponOltRxPowerAlarmi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,175))
zxGponOltRxPowerAlarmi.setObjects(*((_G,_H),(_B,_z),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltRxPowerAlarmi.setStatus(_A)
zxGponOltRxPowerAlarmiRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,176))
zxGponOltRxPowerAlarmiRestore.setObjects(*((_G,_H),(_B,_z),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltRxPowerAlarmiRestore.setStatus(_A)
zxGponOltRxPowerAbnormalInformi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,177))
zxGponOltRxPowerAbnormalInformi.setObjects(*((_G,_H),(_B,_Ay),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltRxPowerAbnormalInformi.setStatus(_A)
zxGponOltRxPowerNormalInformi=NotificationType((1,3,6,1,4,1,3902,1012,3,45,178))
zxGponOltRxPowerNormalInformi.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltRxPowerNormalInformi.setStatus(_A)
zxGponOltTxPowerAlarm=NotificationType((1,3,6,1,4,1,3902,1012,3,45,179))
zxGponOltTxPowerAlarm.setObjects(*((_G,_H),(_B,_A0)))
if mibBuilder.loadTexts:zxGponOltTxPowerAlarm.setStatus(_A)
zxGponOltTxPowerAlarmRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,180))
zxGponOltTxPowerAlarmRestore.setObjects(*((_G,_H),(_B,_A0)))
if mibBuilder.loadTexts:zxGponOltTxPowerAlarmRestore.setStatus(_A)
zxGponOltTxPowerAbnormalInform=NotificationType((1,3,6,1,4,1,3902,1012,3,45,181))
zxGponOltTxPowerAbnormalInform.setObjects(*((_G,_H),(_B,_Az)))
if mibBuilder.loadTexts:zxGponOltTxPowerAbnormalInform.setStatus(_A)
zxGponOltTxPowerNormalInform=NotificationType((1,3,6,1,4,1,3902,1012,3,45,182))
zxGponOltTxPowerNormalInform.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltTxPowerNormalInform.setStatus(_A)
zxGponOltFakedSN=NotificationType((1,3,6,1,4,1,3902,1012,3,45,183))
zxGponOltFakedSN.setObjects(*((_G,_H),(_B,_A1),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOltFakedSN.setStatus(_A)
zxGponOnuConstantOptical=NotificationType((1,3,6,1,4,1,3902,1012,3,45,184))
zxGponOnuConstantOptical.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOnuConstantOptical.setStatus(_A)
zxGponOnuConstantOpticalRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,185))
zxGponOnuConstantOpticalRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOnuConstantOpticalRestore.setStatus(_A)
zxGponOnuFiberBending=NotificationType((1,3,6,1,4,1,3902,1012,3,45,186))
zxGponOnuFiberBending.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOnuFiberBending.setStatus(_A)
zxGponOnuFiberBendingRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,187))
zxGponOnuFiberBendingRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOnuFiberBendingRestore.setStatus(_A)
zxGponOnuOpticalTransceiverLos=NotificationType((1,3,6,1,4,1,3902,1012,3,45,188))
zxGponOnuOpticalTransceiverLos.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOnuOpticalTransceiverLos.setStatus(_A)
zxGponOnuOpticalTransceiverLosRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,189))
zxGponOnuOpticalTransceiverLosRestore.setObjects(*((_G,_H),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponOnuOpticalTransceiverLosRestore.setStatus(_A)
zxGponMacSpoofing=NotificationType((1,3,6,1,4,1,3902,1012,3,45,190))
zxGponMacSpoofing.setObjects(*((_G,_H),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_L),(_B,_J),(_B,_M)))
if mibBuilder.loadTexts:zxGponMacSpoofing.setStatus(_A)
zxGponUnauthOnuOnline=NotificationType((1,3,6,1,4,1,3902,1012,3,45,191))
zxGponUnauthOnuOnline.setObjects(*((_G,_H),(_B,_J),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6)))
if mibBuilder.loadTexts:zxGponUnauthOnuOnline.setStatus(_A)
zxGponOltTF=NotificationType((1,3,6,1,4,1,3902,1012,3,45,192))
zxGponOltTF.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOltTF.setStatus(_A)
zxGponOltTFRestore=NotificationType((1,3,6,1,4,1,3902,1012,3,45,193))
zxGponOltTFRestore.setObjects((_G,_H))
if mibBuilder.loadTexts:zxGponOltTFRestore.setStatus(_A)
zxGponOltFakedPassword=NotificationType((1,3,6,1,4,1,3902,1012,3,45,194))
zxGponOltFakedPassword.setObjects(*((_G,_H),(_B,_A1)))
if mibBuilder.loadTexts:zxGponOltFakedPassword.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_AS:OntVendorId,_AT:OntVersionId,_f:OntSerialNumber,_AV:OntEquipmentId,_X:ZxGponRecordName,_A7:ZxOntList,_b:ZxPortIdList,_d:ZxIndexList,'VlanId':VlanId,_i:Timeout,'zxEnterpriseMib':zxEnterpriseMib,'zxPON':zxPON,'zxGponRootMib':zxGponRootMib,'zxGponMgmtIndex':zxGponMgmtIndex,'zxGponOltOnuTable':zxGponOltOnuTable,'zxGponOltOnuEntry':zxGponOltOnuEntry,_F:zxGponMgmtPonOltId,_I:zxGponMgmtPonOnuId,'zxGponMgmtPonEntryStatus':zxGponMgmtPonEntryStatus,'zxAnGponRevision':zxAnGponRevision,'zxGponPrivateGlobal':zxGponPrivateGlobal,'zxGponOltDevInfoTable':zxGponOltDevInfoTable,'zxGponOltDevInfoEntry':zxGponOltDevInfoEntry,'zxGponDbaEnable':zxGponDbaEnable,'zxGponFECTable':zxGponFECTable,'zxGponFECEntry':zxGponFECEntry,'zxGponFECMode':zxGponFECMode,'zxGponRTDTable':zxGponRTDTable,'zxGponRTDEntry':zxGponRTDEntry,'zxGponRTDEqd':zxGponRTDEqd,'zxGponRTDDistance':zxGponRTDDistance,'zxGponRangeTable':zxGponRangeTable,'zxGponRangeEntry':zxGponRangeEntry,'zxGponRangeMode':zxGponRangeMode,'zxGponRangeBase':zxGponRangeBase,'zxGponRangeDiff':zxGponRangeDiff,'zxGponRangeCapability':zxGponRangeCapability,'zxGponPonFloodBandwidthInfoTable':zxGponPonFloodBandwidthInfoTable,'zxGponPonFloodBandwidthInfoEntry':zxGponPonFloodBandwidthInfoEntry,'zxGponPonFloodBandwidth':zxGponPonFloodBandwidth,'zxGponPonMCastBandwidthInfoTable':zxGponPonMCastBandwidthInfoTable,'zxGponPonMCastBandwidthInfoEntry':zxGponPonMCastBandwidthInfoEntry,'zxGponPonMCastTotalBandwidth':zxGponPonMCastTotalBandwidth,'zxGponSCBMCastGroupTable':zxGponSCBMCastGroupTable,'zxGponSCBMCastGroupEntry':zxGponSCBMCastGroupEntry,_A5:zxGponSCBMCastGroupIdx,'zxGponSCBMCastGroupName':zxGponSCBMCastGroupName,'zxGponSCBMCastMgmtPortID':zxGponSCBMCastMgmtPortID,'zxGponSCBMCastGroupDownBWPtr':zxGponSCBMCastGroupDownBWPtr,'zxGponSCBMCastRealPortID':zxGponSCBMCastRealPortID,'zxGponSCBMCastOntListIdx':zxGponSCBMCastOntListIdx,'zxGponSCBMCastEntryStatus':zxGponSCBMCastEntryStatus,'zxGponSCBMCastOntTable':zxGponSCBMCastOntTable,'zxGponSCBMCastOntEntry':zxGponSCBMCastOntEntry,_A6:zxGponSCBMCastOntSetIdx,'zxGponSCBMCastOntSetGroupIdx':zxGponSCBMCastOntSetGroupIdx,'zxGponSCBMCastOntList':zxGponSCBMCastOntList,'zxGponSCBMCastOntEntryStatus':zxGponSCBMCastOntEntryStatus,'zxGponPonBroadCastBandwidthInfoTable':zxGponPonBroadCastBandwidthInfoTable,'zxGponPonBroadCastBandwidthInfoEntry':zxGponPonBroadCastBandwidthInfoEntry,'zxGponPonBroadCastBandwidth':zxGponPonBroadCastBandwidth,'zxGponPonPeakBandwidthInfoTable':zxGponPonPeakBandwidthInfoTable,'zxGponPonPeakBandwidthInfoEntry':zxGponPonPeakBandwidthInfoEntry,'zxGponPonPeakBandwidth':zxGponPonPeakBandwidth,'zxGponGetValidIdxTable':zxGponGetValidIdxTable,'zxGponGetValidIdxEntry':zxGponGetValidIdxEntry,_A8:zxGponGetValidIdxTableNameIdx,'zxGponGetValidIdxvalue':zxGponGetValidIdxvalue,'zxGponSpiIfPmTable':zxGponSpiIfPmTable,'zxGponSpiIfPmEntry':zxGponSpiIfPmEntry,'zxGponSpiIfRxFrm':zxGponSpiIfRxFrm,'zxGponSpiIfRxByte':zxGponSpiIfRxByte,'zxGponSpiIfRxDiscardFrm':zxGponSpiIfRxDiscardFrm,'zxGponSpiIfRxDiscardByte':zxGponSpiIfRxDiscardByte,'zxGponSpiIfTxFrm':zxGponSpiIfTxFrm,'zxGponSpiIfTxByte':zxGponSpiIfTxByte,'zxGponSpiIfTxDiscardFrm':zxGponSpiIfTxDiscardFrm,'zxGponSpiIfTxDiscardByte':zxGponSpiIfTxDiscardByte,'zxGponPonScheduleModeInfoTable':zxGponPonScheduleModeInfoTable,'zxGponPonScheduleModeInfoEntry':zxGponPonScheduleModeInfoEntry,_e:zxGponMgmtPonSlotId,'zxGponPonScheduleMode':zxGponPonScheduleMode,'zxGponPon802Dot1pMapInfoTable':zxGponPon802Dot1pMapInfoTable,'zxGponPon802Dot1pMapInfoEntry':zxGponPon802Dot1pMapInfoEntry,'zxGponPonDot1pMapQueue0':zxGponPonDot1pMapQueue0,'zxGponPonDot1pMapQueue1':zxGponPonDot1pMapQueue1,'zxGponPonDot1pMapQueue2':zxGponPonDot1pMapQueue2,'zxGponPonDot1pMapQueue3':zxGponPonDot1pMapQueue3,'zxGponPonDot1pMapQueue4':zxGponPonDot1pMapQueue4,'zxGponPonDot1pMapQueue5':zxGponPonDot1pMapQueue5,'zxGponPonDot1pMapQueue6':zxGponPonDot1pMapQueue6,'zxGponPonDot1pMapQueue7':zxGponPonDot1pMapQueue7,'zxGponPonWeightMgmtInfoTable':zxGponPonWeightMgmtInfoTable,'zxGponPonWeightMgmtInfoEntry':zxGponPonWeightMgmtInfoEntry,'zxGponPonWeightMgmtQueue0':zxGponPonWeightMgmtQueue0,'zxGponPonWeightMgmtQueue1':zxGponPonWeightMgmtQueue1,'zxGponPonWeightMgmtQueue2':zxGponPonWeightMgmtQueue2,'zxGponPonWeightMgmtQueue3':zxGponPonWeightMgmtQueue3,'zxGponPonWeightMgmtQueue4':zxGponPonWeightMgmtQueue4,'zxGponPonWeightMgmtQueue5':zxGponPonWeightMgmtQueue5,'zxGponPonWeightMgmtQueue6':zxGponPonWeightMgmtQueue6,'zxGponPonWeightMgmtQueue7':zxGponPonWeightMgmtQueue7,'zxGponFloodBroadCastEnableInfoTable':zxGponFloodBroadCastEnableInfoTable,'zxGponFloodBroadCastEnableInfoEntry':zxGponFloodBroadCastEnableInfoEntry,'zxGponFloodEnable':zxGponFloodEnable,'zxGponBroadcastEnable':zxGponBroadcastEnable,'zxGponSlotOpticalDetectInfoTable':zxGponSlotOpticalDetectInfoTable,'zxGponSlotOpticalDetectInfoEntry':zxGponSlotOpticalDetectInfoEntry,'zxGponSlotOpticalDetect':zxGponSlotOpticalDetect,'zxGponPortLocOnuIdFormat':zxGponPortLocOnuIdFormat,'zxGponStandardOlt':zxGponStandardOlt,'zxGponOltInfoTable':zxGponOltInfoTable,'zxGponOltInfoEntry':zxGponOltInfoEntry,'zxGponOltInfoPONTransRateType':zxGponOltInfoPONTransRateType,'zxGponOltInfoOpticalTransceiverType':zxGponOltInfoOpticalTransceiverType,'zxGponOltInfoOntMgmtMode':zxGponOltInfoOntMgmtMode,'zxGponOltInfoCurrentStatus':zxGponOltInfoCurrentStatus,'zxGponOltInfoFECEnable':zxGponOltInfoFECEnable,'zxGponOltInfoDBAEnable':zxGponOltInfoDBAEnable,'zxGponOltStatisticInfoTable':zxGponOltStatisticInfoTable,'zxGponOltStatisticInfoEntry':zxGponOltStatisticInfoEntry,'zxGponOltStatisticInfoSuperframeCounter':zxGponOltStatisticInfoSuperframeCounter,'zxGponOltStatisticInfoBIPCounter':zxGponOltStatisticInfoBIPCounter,'zxGponDownFrameInfoTable':zxGponDownFrameInfoTable,'zxGponDownFrameInfoEntry':zxGponDownFrameInfoEntry,'zxGponDownFrameInfoServices':zxGponDownFrameInfoServices,'zxGponDownFrameInfoSIMinGranularity':zxGponDownFrameInfoSIMinGranularity,'zxGponDownFrameInfoDbaMethod':zxGponDownFrameInfoDbaMethod,'zxGponDownFrameInfoScramblingEnable':zxGponDownFrameInfoScramblingEnable,'zxGponDownFrameInfoFECEnable':zxGponDownFrameInfoFECEnable,'zxGponDownFrameInfoOnuSendDBRuMode':zxGponDownFrameInfoOnuSendDBRuMode,'zxGponOltPmStatisticInfoTable':zxGponOltPmStatisticInfoTable,'zxGponOltPmStatisticInfoEntry':zxGponOltPmStatisticInfoEntry,'zxGponOltPmStatisticInfoGemPacketTx':zxGponOltPmStatisticInfoGemPacketTx,'zxGponOltPmStatisticInfoGemPacketRxCorIdle':zxGponOltPmStatisticInfoGemPacketRxCorIdle,'zxGponOltPmStatisticInfoGemPacketRxCorNoIdle':zxGponOltPmStatisticInfoGemPacketRxCorNoIdle,'zxGponOltPmStatisticInfoGemPacketRxErr':zxGponOltPmStatisticInfoGemPacketRxErr,'zxGponOltPmStatisticInfoGemPayloadBytesRx':zxGponOltPmStatisticInfoGemPayloadBytesRx,'zxGponOltPmStatisticInfoEthPacketTx':zxGponOltPmStatisticInfoEthPacketTx,'zxGponOltPmStatisticInfoEthPacketRxCor':zxGponOltPmStatisticInfoEthPacketRxCor,'zxGponOltPmStatisticInfoEthPacketRxErr':zxGponOltPmStatisticInfoEthPacketRxErr,'zxGponOltPmStatisticInfoOmciPacketTx':zxGponOltPmStatisticInfoOmciPacketTx,'zxGponOltPmStatisticInfoOmciPacketRxCor':zxGponOltPmStatisticInfoOmciPacketRxCor,'zxGponOltPmStatisticInfoOmciPacketRxErr':zxGponOltPmStatisticInfoOmciPacketRxErr,'zxGponOltPmStatisticInfoPloamTx':zxGponOltPmStatisticInfoPloamTx,'zxGponOltPmStatisticInfoPloamRxCor':zxGponOltPmStatisticInfoPloamRxCor,'zxGponOltPmStatisticInfoPloamRxErr':zxGponOltPmStatisticInfoPloamRxErr,'zxGponOltPmStatisticInfoERR':zxGponOltPmStatisticInfoERR,'zxGponOltPmStatisticInfoREI':zxGponOltPmStatisticInfoREI,'zxGponFindOnuTimerTable':zxGponFindOnuTimerTable,'zxGponFindOnuTimerEntry':zxGponFindOnuTimerEntry,'zxGPonFindOnuTimerNewOnt':zxGPonFindOnuTimerNewOnt,'zxGponFindOnuTimerMissingOnt':zxGponFindOnuTimerMissingOnt,'zxGPonFindOnuTimerOpenWindowFrame':zxGPonFindOnuTimerOpenWindowFrame,'zxGponOltAlarmTable':zxGponOltAlarmTable,'zxGponOltAlarmEntry':zxGponOltAlarmEntry,'zxGPonOltAlarmLos':zxGPonOltAlarmLos,'zxGponOltAlarmLosMask':zxGponOltAlarmLosMask,'zxGponOltAlarmTF':zxGponOltAlarmTF,'zxGponOltAlarmTFMask':zxGponOltAlarmTFMask,'zxGponOntUpAlarmOltSideTable':zxGponOntUpAlarmOltSideTable,'zxGponOntUpAlarmOltSideEntry':zxGponOntUpAlarmOltSideEntry,'zxGponOntUpAlarmOltSideLOSui':zxGponOntUpAlarmOltSideLOSui,'zxGponOntUpAlarmOltSideLOSuiMask':zxGponOntUpAlarmOltSideLOSuiMask,'zxGponOntUpAlarmOltSideLOFui':zxGponOntUpAlarmOltSideLOFui,'zxGponOntUpAlarmOltSideLOFuiMask':zxGponOntUpAlarmOltSideLOFuiMask,'zxGponOntUpAlarmOltSideDOWui':zxGponOntUpAlarmOltSideDOWui,'zxGponOntUpAlarmOltSideDOWuiMask':zxGponOntUpAlarmOltSideDOWuiMask,'zxGponOntUpAlarmOltSideSFui':zxGponOntUpAlarmOltSideSFui,'zxGponOntUpAlarmOltSideSFuiMask':zxGponOntUpAlarmOltSideSFuiMask,'zxGponOntUpAlarmOltSideSDui':zxGponOntUpAlarmOltSideSDui,'zxGponOntUpAlarmOltSideSDuiMask':zxGponOntUpAlarmOltSideSDuiMask,'zxGponOntUpAlarmOltSideLCDAui':zxGponOntUpAlarmOltSideLCDAui,'zxGponOntUpAlarmOltSideLCDAuiMask':zxGponOntUpAlarmOltSideLCDAuiMask,'zxGponOntUpAlarmOltSideLCDGui':zxGponOntUpAlarmOltSideLCDGui,'zxGponOntUpAlarmOltSideLCDGuiMask':zxGponOntUpAlarmOltSideLCDGuiMask,'zxGponOntUpAlarmOltSideRDIui':zxGponOntUpAlarmOltSideRDIui,'zxGponOntUpAlarmOltSideRDIuiMask':zxGponOntUpAlarmOltSideRDIuiMask,'zxGponOntUpAlarmOltSideSUFui':zxGponOntUpAlarmOltSideSUFui,'zxGponOntUpAlarmOltSideSUFuiMask':zxGponOntUpAlarmOltSideSUFuiMask,'zxGponOntUpAlarmOltSideDFui':zxGponOntUpAlarmOltSideDFui,'zxGponOntUpAlarmOltSideDFuiMask':zxGponOntUpAlarmOltSideDFuiMask,'zxGponOntUpAlarmOltSideLOAui':zxGponOntUpAlarmOltSideLOAui,'zxGponOntUpAlarmOltSideLOAuiMask':zxGponOntUpAlarmOltSideLOAuiMask,'zxGponOntUpAlarmOltSideDGui':zxGponOntUpAlarmOltSideDGui,'zxGponOntUpAlarmOltSideDGuiMask':zxGponOntUpAlarmOltSideDGuiMask,'zxGponOntUpAlarmOltSideLOAMui':zxGponOntUpAlarmOltSideLOAMui,'zxGponOntUpAlarmOltSideLOAMuiMask':zxGponOntUpAlarmOltSideLOAMuiMask,'zxGponOntUpAlarmOltSideMEMui':zxGponOntUpAlarmOltSideMEMui,'zxGponOntUpAlarmOltSideMEMuiMask':zxGponOntUpAlarmOltSideMEMuiMask,'zxGponOntUpAlarmOltSideMISui':zxGponOntUpAlarmOltSideMISui,'zxGponOntUpAlarmOltSideMISuiMask':zxGponOntUpAlarmOltSideMISuiMask,'zxGponOntUpAlarmOltSidePEEui':zxGponOntUpAlarmOltSidePEEui,'zxGponOntUpAlarmOltSidePEEuiMask':zxGponOntUpAlarmOltSidePEEuiMask,'zxGponBerDowThresholdTable':zxGponBerDowThresholdTable,'zxGponBerDowThresholdEntry':zxGponBerDowThresholdEntry,'zxGponBerDowThresholdSDui':zxGponBerDowThresholdSDui,'zxGponBerDowThresholdSFui':zxGponBerDowThresholdSFui,'zxGponBerDowThresholdDOWi':zxGponBerDowThresholdDOWi,'zxGponOntUpPmOltSideTable':zxGponOntUpPmOltSideTable,'zxGponOntUpPmOltSideEntry':zxGponOntUpPmOltSideEntry,'zxGponOntUpPmOltSideERRui':zxGponOntUpPmOltSideERRui,'zxGponOntUpPmOltSideREIui':zxGponOntUpPmOltSideREIui,'zxGponOntUpPmOltSideCorrNIdleGemFramesui':zxGponOntUpPmOltSideCorrNIdleGemFramesui,'zxGponOntUpPmOltSideCorrIdleGemFramesui':zxGponOntUpPmOltSideCorrIdleGemFramesui,'zxGponOntUpPmOltSideErroredGemFramesui':zxGponOntUpPmOltSideErroredGemFramesui,'zxGponOntUpPmOltSideGemPayloadBytesui':zxGponOntUpPmOltSideGemPayloadBytesui,'zxGponOntUpPmOltSideCorrectEthFramesui':zxGponOntUpPmOltSideCorrectEthFramesui,'zxGponOntUpPmOltSideErroredEthFramesui':zxGponOntUpPmOltSideErroredEthFramesui,'zxGponOntUpPmOltSideTotalOmciFramesui':zxGponOntUpPmOltSideTotalOmciFramesui,'zxGponOltUpPmTable':zxGponOltUpPmTable,'zxGponOltUpPmEntry':zxGponOltUpPmEntry,'zxGponOltUpPmERRu':zxGponOltUpPmERRu,'zxGponOltUpPmREIu':zxGponOltUpPmREIu,'zxGponOltUpPmCorrNIdleGemFramesu':zxGponOltUpPmCorrNIdleGemFramesu,'zxGponOltUpPmCorrIdleGemFramesu':zxGponOltUpPmCorrIdleGemFramesu,'zxGponOltUpPmErroredGemFramesu':zxGponOltUpPmErroredGemFramesu,'zxGponOltUpPmGemPayloadBytesu':zxGponOltUpPmGemPayloadBytesu,'zxGponOltUpPmCorrectEthFramesu':zxGponOltUpPmCorrectEthFramesu,'zxGponOltUpPmErroredEthFramesu':zxGponOltUpPmErroredEthFramesu,'zxGponOltUpPmTotalOmciFramesu':zxGponOltUpPmTotalOmciFramesu,'zxGponOltPmStatisRealtimeInfoTable':zxGponOltPmStatisRealtimeInfoTable,'zxGponOltPmStatisRealtimeInfoEntry':zxGponOltPmStatisRealtimeInfoEntry,'zxGponOltPmStatisInfoCorrectNonIdleGemFramesUpstream':zxGponOltPmStatisInfoCorrectNonIdleGemFramesUpstream,'zxGponOltPmStatisInfoCorrectIdleGemFramesUpstream':zxGponOltPmStatisInfoCorrectIdleGemFramesUpstream,'zxGponOltPmStatisInfoErroredGemFramesUpstream':zxGponOltPmStatisInfoErroredGemFramesUpstream,'zxGponOltPmStatisInfoGemPayloadBytesUpstream':zxGponOltPmStatisInfoGemPayloadBytesUpstream,'zxGponOltPmStatisInfoCorrectEthernetFramesUpstream':zxGponOltPmStatisInfoCorrectEthernetFramesUpstream,'zxGponOltPmStatisInfoErroredEthernetFramesUpstream':zxGponOltPmStatisInfoErroredEthernetFramesUpstream,'zxGponOltPmStatisInfoTotalOmciFramesUpstream':zxGponOltPmStatisInfoTotalOmciFramesUpstream,'zxGponOltPmStatisInfoERR':zxGponOltPmStatisInfoERR,'zxGponOltPmStatisInfoREI':zxGponOltPmStatisInfoREI,'zxGponOltPmStatisInfoValidEthernetPacketDownstream':zxGponOltPmStatisInfoValidEthernetPacketDownstream,'zxGponOltPmStatisInfoCpuPacketDownstream':zxGponOltPmStatisInfoCpuPacketDownstream,'zxGponOltPmStatisInfoPloamDownstream':zxGponOltPmStatisInfoPloamDownstream,'zxGponOltPmStatisInfoPloamUpstream':zxGponOltPmStatisInfoPloamUpstream,'zxGponOltPmStatisInfoInvalidPacketUpstream':zxGponOltPmStatisInfoInvalidPacketUpstream,'zxGponOltPmStatisHistoryInfoTable':zxGponOltPmStatisHistoryInfoTable,'zxGponOltPmStatisHistoryInfoEntry':zxGponOltPmStatisHistoryInfoEntry,'zxGponOltPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream':zxGponOltPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream,'zxGponOltPmStatisHistoryInfoCorrectIdleGemFramesUpstream':zxGponOltPmStatisHistoryInfoCorrectIdleGemFramesUpstream,'zxGponOltPmStatisHistoryInfoErroredGemFramesUpstream':zxGponOltPmStatisHistoryInfoErroredGemFramesUpstream,'zxGponOltPmStatisHistoryInfoGemPayloadBytesUpstream':zxGponOltPmStatisHistoryInfoGemPayloadBytesUpstream,'zxGponOltPmStatisHistoryInfoCorrectEthernetFramesUpstream':zxGponOltPmStatisHistoryInfoCorrectEthernetFramesUpstream,'zxGponOltPmStatisHistoryInfoErroredEthernetFramesUpstream':zxGponOltPmStatisHistoryInfoErroredEthernetFramesUpstream,'zxGponOltPmStatisHistoryInfoTotalOmciFramesUpstream':zxGponOltPmStatisHistoryInfoTotalOmciFramesUpstream,'zxGponOltPmStatisHistoryInfoERR':zxGponOltPmStatisHistoryInfoERR,'zxGponOltPmStatisHistoryInfoREI':zxGponOltPmStatisHistoryInfoREI,'zxGponOltPmStatisHistoryInfoValidEthernetPacketDownstream':zxGponOltPmStatisHistoryInfoValidEthernetPacketDownstream,'zxGponOltPmStatisHistoryInfoCpuPacketDownstream':zxGponOltPmStatisHistoryInfoCpuPacketDownstream,'zxGponOltPmStatisHistoryInfoPloamDownstream':zxGponOltPmStatisHistoryInfoPloamDownstream,'zxGponOltPmStatisHistoryInfoPloamUpstream':zxGponOltPmStatisHistoryInfoPloamUpstream,'zxGponOltPmStatisHistoryInfoInvalidPacketUpstream':zxGponOltPmStatisHistoryInfoInvalidPacketUpstream,'zxGponPrivateOlt':zxGponPrivateOlt,'zxGponOltPonInfoTable':zxGponOltPonInfoTable,'zxGponOltPonInfoEntry':zxGponOltPonInfoEntry,'zxGponOltPonName':zxGponOltPonName,'zxGponOltPonDescription':zxGponOltPonDescription,'zxGPonOltPonOntDefaultState':zxGPonOltPonOntDefaultState,'zxGPonOltPonOntDefaultPwMode':zxGPonOltPonOntDefaultPwMode,'zxGPonOltPonOntDefaultPw':zxGPonOltPonOntDefaultPw,'zxGPonOltPonOntAuthMode':zxGPonOltPonOntAuthMode,'zxGPonOltPonOntSnAuthMode':zxGPonOltPonOntSnAuthMode,'zxGPonOltPonOntSnMask':zxGPonOltPonOntSnMask,'zxGponOltPonOmccPortBase':zxGponOltPonOmccPortBase,'zxGPonOltPonAdminState':zxGPonOltPonAdminState,'zxGPonOltPonOperState':zxGPonOltPonOperState,'zxGponOltPonSupportMaxOnts':zxGponOltPonSupportMaxOnts,'zxGponOltPonRealLegalOnts':zxGponOltPonRealLegalOnts,'zxGponOltPonRealIllegalOnts':zxGponOltPonRealIllegalOnts,'zxGponOltPonSupportMaxTConts':zxGponOltPonSupportMaxTConts,'zxGponOltPonRealUsedTConts':zxGponOltPonRealUsedTConts,'zxGponOltPonOntConfigureStatus':zxGponOltPonOntConfigureStatus,'zxGponOltMgmtOperTable':zxGponOltMgmtOperTable,'zxGponOltMgmtOperEntry':zxGponOltMgmtOperEntry,'zxGponOltReset':zxGponOltReset,'zxGponOltOff':zxGponOltOff,'zxGponOltOpticalDetectOnce':zxGponOltOpticalDetectOnce,'zxGponUnCfgSnOntInfoTable':zxGponUnCfgSnOntInfoTable,'zxGponUnCfgSnOntInfoEntry':zxGponUnCfgSnOntInfoEntry,_AA:zxGponUnCfgSnIdx,_B3:zxGponUnCfgSnOntSN,_B4:zxGponUnCfgSnOntRID,_B6:zxGponUnCfgSnOntRtd,_B5:zxGponUnCfgSnOntPsw,'zxGponUnCfgSnOntState':zxGponUnCfgSnOntState,'zxGponUnCfgSnOntTime':zxGponUnCfgSnOntTime,'zxGponOmccInfoTable':zxGponOmccInfoTable,'zxGponOmccInfoEntry':zxGponOmccInfoEntry,'zxGponOmccChannelNum':zxGponOmccChannelNum,'zxGponOmccChannelBandwidth':zxGponOmccChannelBandwidth,'zxGponOmccChannelAdminState':zxGponOmccChannelAdminState,'zxGponOmccChannelOpState':zxGponOmccChannelOpState,'zxGponOltBitErrTable':zxGponOltBitErrTable,'zxGponOltBitErrEntry':zxGponOltBitErrEntry,'zxGponOltUpBerEnable':zxGponOltUpBerEnable,'zxGponOltUpBerCalcInterval':zxGponOltUpBerCalcInterval,'zxGponOltDownBerEnable':zxGponOltDownBerEnable,'zxGponOltDownBerCalcInterval':zxGponOltDownBerCalcInterval,'zxGponOltUpSfThreshold':zxGponOltUpSfThreshold,'zxGponOltUpSdThreshold':zxGponOltUpSdThreshold,'zxGponStaticMultiPortIdInfoTable':zxGponStaticMultiPortIdInfoTable,'zxGponStaticMultiPortIdInfoEntry':zxGponStaticMultiPortIdInfoEntry,_AH:zxGponStaticMultiPortIdInfoIdx,'zxGponStaticMultiPortIdList':zxGponStaticMultiPortIdList,'zxGponStaticMultiAddrIdx':zxGponStaticMultiAddrIdx,'zxGponStaticMultiPortIdStatus':zxGponStaticMultiPortIdStatus,'zxGponStaticMulticastAddressTable':zxGponStaticMulticastAddressTable,'zxGponStaticMulticastAddressEntry':zxGponStaticMulticastAddressEntry,_AI:zxGponStaticMulticastIdx,'zxGponStaticMulticastAddress':zxGponStaticMulticastAddress,'zxGponStaticMulticastVlanId':zxGponStaticMulticastVlanId,'zxGponStaticMulticastPortIdIdx':zxGponStaticMulticastPortIdIdx,'zxGponStaticMulticastStatus':zxGponStaticMulticastStatus,'zxGponMulticastAddressTable':zxGponMulticastAddressTable,'zxGponMulticastAddressEntry':zxGponMulticastAddressEntry,_AJ:zxGponMulticastAddress,_AK:zxGponMulticastVlanId,_AL:zxGponMulticastIdx,'zxGponMulticastPortIdIdx':zxGponMulticastPortIdIdx,'zxGponMulticastStatus':zxGponMulticastStatus,'zxGponDsBFPortIdInfoTable':zxGponDsBFPortIdInfoTable,'zxGponDsBFPortIdInfoEntry':zxGponDsBFPortIdInfoEntry,_AM:zxGponDsBFPortIdInfoIdx,'zxGponDsBFPortIdInfoList':zxGponDsBFPortIdInfoList,'zxGponDsBFPortIdInfoVlanIdx':zxGponDsBFPortIdInfoVlanIdx,'zxGponDsBFPortIdInfoStatus':zxGponDsBFPortIdInfoStatus,'zxGponDownBroadcastFloodTable':zxGponDownBroadcastFloodTable,'zxGponDownBroadcastFloodEntry':zxGponDownBroadcastFloodEntry,_AN:zxGponDownBroadcastFloodVlanId,'zxGponDownBroadcastFloodPortList':zxGponDownBroadcastFloodPortList,'zxGponDownBroadcastFloodEntryStatus':zxGponDownBroadcastFloodEntryStatus,'zxGpon8021xOnOffTable':zxGpon8021xOnOffTable,'zxGpon8021xOnOffEntry':zxGpon8021xOnOffEntry,_AO:zxGpon8021xOnOffIdx,'zxGpon8021xOnOffPortId':zxGpon8021xOnOffPortId,'zxGpon8021xOnOffEnable':zxGpon8021xOnOffEnable,'zxGponOltLoopbackTestInfoTable':zxGponOltLoopbackTestInfoTable,'zxGponOltLoopbackTestInfoEntry':zxGponOltLoopbackTestInfoEntry,'zxGponOltLoopbackTestStart':zxGponOltLoopbackTestStart,'zxGponOltEthSwitchTable':zxGponOltEthSwitchTable,'zxGponOltEthSwitchEntry':zxGponOltEthSwitchEntry,'zxGponEthSwitchProtectState':zxGponEthSwitchProtectState,'zxGponOltScbPortTable':zxGponOltScbPortTable,'zxGponOltScbPortEntry':zxGponOltScbPortEntry,'zxGponOltScbPort':zxGponOltScbPort,'zxGponEthTypeVlanMapTable':zxGponEthTypeVlanMapTable,'zxGponEthTypeVlanMapEntry':zxGponEthTypeVlanMapEntry,_AP:zxGponEthTypeVlanMapEthType,'zxGponEthTypeVlanMapVlanId':zxGponEthTypeVlanMapVlanId,'zxGponEthTypeVlanMapEntryStatus':zxGponEthTypeVlanMapEntryStatus,'zxGponOltEthVlanSwitchTable':zxGponOltEthVlanSwitchTable,'zxGponOltEthVlanSwitchEntry':zxGponOltEthVlanSwitchEntry,_AQ:zxGponEthSwitchVlanId,'zxGponEthVlanSwitchRowStatus':zxGponEthVlanSwitchRowStatus,'zxGponOntEquipMgmt':zxGponOntEquipMgmt,'zxGponOntStatusInfoTable':zxGponOntStatusInfoTable,'zxGponOntStatusInfoEntry':zxGponOntStatusInfoEntry,_AR:zxGponOntIndex,'zxGponOntMeId':zxGponOntMeId,'zxGponOntVendorId':zxGponOntVendorId,'zxGponOntVersionId':zxGponOntVersionId,'zxGponOntSnId':zxGponOntSnId,'zxGponOntTrafficMgmtOpt':zxGponOntTrafficMgmtOpt,'zxGponOntVpVcConnFunOpt':zxGponOntVpVcConnFunOpt,'zxGponOntBatteryBackup':zxGponOntBatteryBackup,'zxGponOntAdminStatus':zxGponOntAdminStatus,'zxGponOntOperStatus':zxGponOntOperStatus,'zxGponOntAlarmTable':zxGponOntAlarmTable,'zxGponOntAlarmEntry':zxGponOntAlarmEntry,'zxGponOntEquipmentAlarm':zxGponOntEquipmentAlarm,'zxGponOntEquipmentAlarmMask':zxGponOntEquipmentAlarmMask,'zxGponOntPoweringAlarm':zxGponOntPoweringAlarm,'zxGponOntPoweringAlarmMask':zxGponOntPoweringAlarmMask,'zxGponOntBatteryMissing':zxGponOntBatteryMissing,'zxGponOntBatteryMissingMask':zxGponOntBatteryMissingMask,'zxGponOntBatteryFailure':zxGponOntBatteryFailure,'zxGponOntBatteryFailureMask':zxGponOntBatteryFailureMask,'zxGponOntBatteryLow':zxGponOntBatteryLow,'zxGponOntBatteryLowMask':zxGponOntBatteryLowMask,'zxGponOntPhysicalIntrusionAlarm':zxGponOntPhysicalIntrusionAlarm,'zxGponOntPhysicalIntrusionAlarmMask':zxGponOntPhysicalIntrusionAlarmMask,'zxGponOntONTSelfTestFailure':zxGponOntONTSelfTestFailure,'zxGponOntONTSelfTestFailureMask':zxGponOntONTSelfTestFailureMask,'zxGponOntActionsTable':zxGponOntActionsTable,'zxGponOntActionsEntry':zxGponOntActionsEntry,'zxGponOntReboot':zxGponOntReboot,'zxGponOntTest':zxGponOntTest,'zxGponOntSyncTime':zxGponOntSyncTime,'zxGponOntMibReset':zxGponOntMibReset,'zxGponOntTestResult':zxGponOntTestResult,'zxGponOnt2StatusInfoTable':zxGponOnt2StatusInfoTable,'zxGponOnt2StatusInfoEntry':zxGponOnt2StatusInfoEntry,_AU:zxGponOnt2Index,'zxGponOnt2MeId':zxGponOnt2MeId,'zxGponOnt2EquipmentId':zxGponOnt2EquipmentId,'zxGponOnt2OMCCVersion':zxGponOnt2OMCCVersion,'zxGponOnt2VendorProdCode':zxGponOnt2VendorProdCode,'zxGponOnt2SecurityCapab':zxGponOnt2SecurityCapab,'zxGponOnt2SecurityMode':zxGponOnt2SecurityMode,'zxGponOnt2TotalPriQueNum':zxGponOnt2TotalPriQueNum,'zxGponOnt2TotalTrafSchedNum':zxGponOnt2TotalTrafSchedNum,'zxGponOnt2Mode':zxGponOnt2Mode,'zxGponThresholdDataTable':zxGponThresholdDataTable,'zxGponThresholdDataEntry':zxGponThresholdDataEntry,_AW:zxGponThresholdDataIndex,'zxGponThresholdDataMeId':zxGponThresholdDataMeId,'zxGponThresholdDataValue1':zxGponThresholdDataValue1,'zxGponThresholdDataValue2':zxGponThresholdDataValue2,'zxGponThresholdDataValue3':zxGponThresholdDataValue3,'zxGponThresholdDataValue4':zxGponThresholdDataValue4,'zxGponThresholdDataValue5':zxGponThresholdDataValue5,'zxGponThresholdDataValue6':zxGponThresholdDataValue6,'zxGponThresholdDataValue7':zxGponThresholdDataValue7,'zxGponThresholdDataValue8':zxGponThresholdDataValue8,'zxGponThresholdDataValue9':zxGponThresholdDataValue9,'zxGponThresholdDataValue10':zxGponThresholdDataValue10,'zxGponThresholdDataValue11':zxGponThresholdDataValue11,'zxGponThresholdDataValue12':zxGponThresholdDataValue12,'zxGponThresholdDataValue13':zxGponThresholdDataValue13,'zxGponThresholdDataValue14':zxGponThresholdDataValue14,'zxGponThresholdDataCreateUsedIdx':zxGponThresholdDataCreateUsedIdx,'zxGponThresholdDataModifyMatchIdx':zxGponThresholdDataModifyMatchIdx,'zxGponThresholdDataModifyFlag':zxGponThresholdDataModifyFlag,'zxGponThresholdDataEntryStatus':zxGponThresholdDataEntryStatus,'zxGponProtectionDataTable':zxGponProtectionDataTable,'zxGponProtectionDataEntry':zxGponProtectionDataEntry,_AX:zxGponProtectionDataIndex,'zxGponProtectionDataMeId':zxGponProtectionDataMeId,'zxGponProtectionDataWorkingAni':zxGponProtectionDataWorkingAni,'zxGponProtectionDataProtectionAni':zxGponProtectionDataProtectionAni,'zxGponProtectionDataProtectionType':zxGponProtectionDataProtectionType,'zxGponProtectionDataRevertive':zxGponProtectionDataRevertive,'zxGponProtectionDataWTT':zxGponProtectionDataWTT,'zxGponProtectionDataSGT':zxGponProtectionDataSGT,'zxGponAniMgmt':zxGponAniMgmt,'zxGponAniInfoTable':zxGponAniInfoTable,'zxGponAniInfoEntry':zxGponAniInfoEntry,_AY:zxGponAniInfoIndex,'zxGponAniInfoMeId':zxGponAniInfoMeId,'zxGponAniInfoSRIndication':zxGponAniInfoSRIndication,'zxGponAniInfoTotalTcontNumber':zxGponAniInfoTotalTcontNumber,'zxGponAniInfoGemBlockLength':zxGponAniInfoGemBlockLength,'zxGponAniInfoPiggybackDbaReporting':zxGponAniInfoPiggybackDbaReporting,'zxGponAniInfoWholeOnuDbaReporting':zxGponAniInfoWholeOnuDbaReporting,'zxGponAniInfoSFThreshold':zxGponAniInfoSFThreshold,'zxGponAniInfoSDThreshold':zxGponAniInfoSDThreshold,'zxGponTcontInfoTable':zxGponTcontInfoTable,'zxGponTcontInfoEntry':zxGponTcontInfoEntry,_AZ:zxGponTcontInfoIndex,'zxGponTcontInfoMeId':zxGponTcontInfoMeId,'zxGponTcontInfoAllocID':zxGponTcontInfoAllocID,'zxGponTcontInfoModeIndicator':zxGponTcontInfoModeIndicator,'zxGponTcontInfoPolicy':zxGponTcontInfoPolicy,'zxGponUniMgmt':zxGponUniMgmt,'zxGpon8021pMapperTable':zxGpon8021pMapperTable,'zxGpon8021pMapperEntry':zxGpon8021pMapperEntry,_Aa:zxGpon8021pMapperMeIdIdx,'zxGpon8021pMapperPptpUniPtr':zxGpon8021pMapperPptpUniPtr,'zxGpon8021pMapperPri0IwTpPtr':zxGpon8021pMapperPri0IwTpPtr,'zxGpon8021pMapperPri1IwTpPtr':zxGpon8021pMapperPri1IwTpPtr,'zxGpon8021pMapperPri2IwTpPtr':zxGpon8021pMapperPri2IwTpPtr,'zxGpon8021pMapperPri3IwTpPtr':zxGpon8021pMapperPri3IwTpPtr,'zxGpon8021pMapperPri4IwTpPtr':zxGpon8021pMapperPri4IwTpPtr,'zxGpon8021pMapperPri5IwTpPtr':zxGpon8021pMapperPri5IwTpPtr,'zxGpon8021pMapperPri6IwTpPtr':zxGpon8021pMapperPri6IwTpPtr,'zxGpon8021pMapperPri7IwTpPtr':zxGpon8021pMapperPri7IwTpPtr,'zxGpon8021pMapperUntagFrmInd':zxGpon8021pMapperUntagFrmInd,'zxGpon8021pMapperDscpTo8021pPri':zxGpon8021pMapperDscpTo8021pPri,'zxGpon8021pMapperDefaultPri':zxGpon8021pMapperDefaultPri,'zxGpon8021pMapperMgmtCtrlFlag':zxGpon8021pMapperMgmtCtrlFlag,'zxGpon8021pMapperEntryStatus':zxGpon8021pMapperEntryStatus,'zxGponUniInfoTable':zxGponUniInfoTable,'zxGponUniInfoEntry':zxGponUniInfoEntry,_Ad:zxGponUniInfoIndex,'zxGponUniInfoMeId':zxGponUniInfoMeId,'zxGponUniInfoCfgOption':zxGponUniInfoCfgOption,'zxGponUniInfoAdminState':zxGponUniInfoAdminState,'ethernetUniMib':ethernetUniMib,'zxGponPPTPEthUniInfoTable':zxGponPPTPEthUniInfoTable,'zxGponPPTPEthUniInfoEntry':zxGponPPTPEthUniInfoEntry,_a:zxGponPPTPEthInfoTPID,'zxGponPPTPEthInfoMeId':zxGponPPTPEthInfoMeId,'zxGponPPTPEthInfoExpectedType':zxGponPPTPEthInfoExpectedType,'zxGponPPTPEthInfoSensedType':zxGponPPTPEthInfoSensedType,'zxGponPPTPEthInfoAutoDetectCfg':zxGponPPTPEthInfoAutoDetectCfg,'zxGponPPTPEthInfoEthLoopback':zxGponPPTPEthInfoEthLoopback,'zxGponPPTPEthInfoAdminState':zxGponPPTPEthInfoAdminState,'zxGponPPTPEthInfoOperationalState':zxGponPPTPEthInfoOperationalState,'zxGponPPTPEthInfoDuplexSpeedInd':zxGponPPTPEthInfoDuplexSpeedInd,'zxGponPPTPEthInfoMaxFrameSize':zxGponPPTPEthInfoMaxFrameSize,'zxGponPPTPEthInfoDTEorDCEInd':zxGponPPTPEthInfoDTEorDCEInd,'zxGponPPTPEthInfoPauseTime':zxGponPPTPEthInfoPauseTime,'zxGponPPTPEthInfoBridgedorIPInd':zxGponPPTPEthInfoBridgedorIPInd,'zxGponPPTPEthInfoARC':zxGponPPTPEthInfoARC,'zxGponPPTPEthInfoARCInterval':zxGponPPTPEthInfoARCInterval,'zxGponPPTPEthInfoPppoeFilterEnable':zxGponPPTPEthInfoPppoeFilterEnable,'zxGponMACBSPInfoTable':zxGponMACBSPInfoTable,'zxGponMACBSPInfoEntry':zxGponMACBSPInfoEntry,_h:zxGponMACBSPInfoMeIdIdx,'zxGponMACBSPInfoSTPInd':zxGponMACBSPInfoSTPInd,'zxGponMACBSPInfoLearningInd':zxGponMACBSPInfoLearningInd,'zxGponMACBSPInfoPortBInd':zxGponMACBSPInfoPortBInd,'zxGponMACBSPInfoPriority':zxGponMACBSPInfoPriority,'zxGponMACBSPInfoMaxAge':zxGponMACBSPInfoMaxAge,'zxGponMACBSPInfoHelloTime':zxGponMACBSPInfoHelloTime,'zxGponMACBSPInfoForwardDelay':zxGponMACBSPInfoForwardDelay,'zxGponMACBSPInfoMgmtCtrlFlag':zxGponMACBSPInfoMgmtCtrlFlag,'zxGponMACBSPInfoEntryStatus':zxGponMACBSPInfoEntryStatus,'zxGponMACBridgeCfgDataInfoTable':zxGponMACBridgeCfgDataInfoTable,'zxGponMACBridgeCfgDataInfoEntry':zxGponMACBridgeCfgDataInfoEntry,'zxGponMACBCfgDataBridgeMACAddress':zxGponMACBCfgDataBridgeMACAddress,'zxGponMACBCfgDataBridgePriority':zxGponMACBCfgDataBridgePriority,'zxGponMACBCfgDataDesignatedRoot':zxGponMACBCfgDataDesignatedRoot,'zxGponMACBCfgDataRootPathCost':zxGponMACBCfgDataRootPathCost,'zxGponMACBCfgDataBridgePortCount':zxGponMACBCfgDataBridgePortCount,'zxGponMACBCfgDataRootPortNum':zxGponMACBCfgDataRootPortNum,'zxGponMACBCfgDataHelloTime':zxGponMACBCfgDataHelloTime,'zxGponMACBCfgDataForwardDelay':zxGponMACBCfgDataForwardDelay,'zxGponMACBriPortCfgDataInfoTable':zxGponMACBriPortCfgDataInfoTable,'zxGponMACBriPortCfgDataInfoEntry':zxGponMACBriPortCfgDataInfoEntry,_j:zxGponMACBriPortCfgDataMeIdIdx,'zxGponMACBriPortCfgDataBridgeIdPtr':zxGponMACBriPortCfgDataBridgeIdPtr,'zxGponMACBriPortCfgDataPortNum':zxGponMACBriPortCfgDataPortNum,'zxGponMACBriPortCfgDataTPType':zxGponMACBriPortCfgDataTPType,'zxGponMACBriPortCfgDataTPPointer':zxGponMACBriPortCfgDataTPPointer,'zxGponMACBriPortCfgDataPortPriority':zxGponMACBriPortCfgDataPortPriority,'zxGponMACBriPortCfgDataPortPathCost':zxGponMACBriPortCfgDataPortPathCost,'zxGponMACBriPortCfgDataPortSpanTreeInd':zxGponMACBriPortCfgDataPortSpanTreeInd,'zxGponMACBriPortCfgDataEncapMethod':zxGponMACBriPortCfgDataEncapMethod,'zxGponMACBriPortCfgDataLANFCSInd':zxGponMACBriPortCfgDataLANFCSInd,'zxGponMACBriPortCfgDataMgmtCtrlFlag':zxGponMACBriPortCfgDataMgmtCtrlFlag,'zxGponMACBriPortCfgDataEntryStatus':zxGponMACBriPortCfgDataEntryStatus,'zxGponMACBriPortFilterTableInfoTable':zxGponMACBriPortFilterTableInfoTable,'zxGponMACBriPortFilterTableInfoEntry':zxGponMACBriPortFilterTableInfoEntry,_Ae:zxGponMACBriPortFilterTableMacAddr,'zxGponMACBriPortFilterTableAction':zxGponMACBriPortFilterTableAction,'zxGponMACBriPortFilterTableEntryStatus':zxGponMACBriPortFilterTableEntryStatus,'zxGponMACBriPortDesignationDataTable':zxGponMACBriPortDesignationDataTable,'zxGponMACBriPortDesignationDataEntry':zxGponMACBriPortDesignationDataEntry,'zxGponMACBriPortDesignationDataRootCostPort':zxGponMACBriPortDesignationDataRootCostPort,'zxGponMACBriPortDesignationDataPortState':zxGponMACBriPortDesignationDataPortState,'zxGponMACBriPortAddrInfoTable':zxGponMACBriPortAddrInfoTable,'zxGponMACBriPortAddrInfoEntry':zxGponMACBriPortAddrInfoEntry,_Af:zxGponMACBriPortAddrMacAddr,'zxGponMACBriPortAddrAction':zxGponMACBriPortAddrAction,'zxGponMACBriPortAddrDynStatic':zxGponMACBriPortAddrDynStatic,'zxGponMACBriPortAddrAgingTime':zxGponMACBriPortAddrAgingTime,'zxGponIpRouterSPInfoTable':zxGponIpRouterSPInfoTable,'zxGponIpRouterSPInfoEntry':zxGponIpRouterSPInfoEntry,_Ag:zxGponIpRouterSPInfoMeIdIdx,'zxGponIpRouterSPInfoForwardingInd':zxGponIpRouterSPInfoForwardingInd,'zxGponIpRouterSPInfoProxyARPInd':zxGponIpRouterSPInfoProxyARPInd,'zxGponIpRouterSPInfoDirectedBroadcastInd':zxGponIpRouterSPInfoDirectedBroadcastInd,'zxGponIpRouterSPInfoUpstreamMulticastFiltering':zxGponIpRouterSPInfoUpstreamMulticastFiltering,'zxGponIpRouterSPInfoDownstreamMulticastFiltering':zxGponIpRouterSPInfoDownstreamMulticastFiltering,'zxGponIpRouterSPInfoMgmtCtrlFlag':zxGponIpRouterSPInfoMgmtCtrlFlag,'zxGponIpRouterSPInfoEntryStatus':zxGponIpRouterSPInfoEntryStatus,'zxGponIpPortCfgDataInfoTable':zxGponIpPortCfgDataInfoTable,'zxGponIpPortCfgDataInfoEntry':zxGponIpPortCfgDataInfoEntry,_Ai:zxGponIpPortCfgDataMeIdIdx,'zxGponIpPortCfgDataPortNum':zxGponIpPortCfgDataPortNum,'zxGponIpPortCfgDataTPType':zxGponIpPortCfgDataTPType,'zxGponIpPortCfgDataTPPointer':zxGponIpPortCfgDataTPPointer,'zxGponIpPortCfgDataPortAddress':zxGponIpPortCfgDataPortAddress,'zxGponIpPortCfgDataPortMask':zxGponIpPortCfgDataPortMask,'zxGponIpPortCfgDataUnnumbered':zxGponIpPortCfgDataUnnumbered,'zxGponIpPortCfgDataAdministrativeState':zxGponIpPortCfgDataAdministrativeState,'zxGponIpPortCfgDataPortState':zxGponIpPortCfgDataPortState,'zxGponIpPortCfgDataAllowRemoteAccess':zxGponIpPortCfgDataAllowRemoteAccess,'zxGponIpPortCfgDataRouterIdPointer':zxGponIpPortCfgDataRouterIdPointer,'zxGponIpPortCfgDataARPPointer':zxGponIpPortCfgDataARPPointer,'zxGponIpPortCfgDataEncapsulationMethod':zxGponIpPortCfgDataEncapsulationMethod,'zxGponIpPortCfgDataMgmtCtrlFlag':zxGponIpPortCfgDataMgmtCtrlFlag,'zxGponIpPortCfgDataEntryStatus':zxGponIpPortCfgDataEntryStatus,'cesUniMib':cesUniMib,'zxGponPPTPCesUniTable':zxGponPPTPCesUniTable,'zxGponPPTPCesUniEntry':zxGponPPTPCesUniEntry,_Aj:zxGponPPTPCesUniTPID,'zxGponPPTPCesUniMeId':zxGponPPTPCesUniMeId,'zxGponPPTPCesUniExpectedType':zxGponPPTPCesUniExpectedType,'zxGponPPTPCesUniSensedType':zxGponPPTPCesUniSensedType,'zxGponPPTPCesUniEesLoopback':zxGponPPTPCesUniEesLoopback,'zxGponPPTPCesUniAdminState':zxGponPPTPCesUniAdminState,'zxGponPPTPCesUniOperationalState':zxGponPPTPCesUniOperationalState,'zxGponPPTPCesUniDS1Framing':zxGponPPTPCesUniDS1Framing,'zxGponPPTPCesUniEncoding':zxGponPPTPCesUniEncoding,'zxGponPPTPCesUniLineLength':zxGponPPTPCesUniLineLength,'zxGponPPTPCesUniDS1Mode':zxGponPPTPCesUniDS1Mode,'zxGponPPTPCesUniARC':zxGponPPTPCesUniARC,'zxGponPPTPCesUniARCInterval':zxGponPPTPCesUniARCInterval,'zxGponPPTPCesUniLineType':zxGponPPTPCesUniLineType,'zxGponCESSPInfoTable':zxGponCESSPInfoTable,'zxGponCESSPInfoEntry':zxGponCESSPInfoEntry,_Ak:zxGponCESSPInfoMeIdIdx,'zxGponCESSPInfoMBufferedCDVTolerance':zxGponCESSPInfoMBufferedCDVTolerance,'zxGponCESSPInfoChannelAssociatedSignalling':zxGponCESSPInfoChannelAssociatedSignalling,'zxGponCESSPInfoMgmtCtrlFlag':zxGponCESSPInfoMgmtCtrlFlag,'zxGponCESSPInfoEntryStatus':zxGponCESSPInfoEntryStatus,'zxGponGemIWTPInfoTable':zxGponGemIWTPInfoTable,'zxGponGemIWTPInfoEntry':zxGponGemIWTPInfoEntry,_Al:zxGponGemIWTPInfoMeIdIdx,'zxGponGemIWTPInfoPNCTPConnectivityPtr':zxGponGemIWTPInfoPNCTPConnectivityPtr,'zxGponGemIWTPInfoIwOption':zxGponGemIWTPInfoIwOption,'zxGponGemIWTPInfoServiceProPtr':zxGponGemIWTPInfoServiceProPtr,'zxGponGemIWTPInfoITPPtr':zxGponGemIWTPInfoITPPtr,'zxGponGemIWTPInfoPPTPCounter':zxGponGemIWTPInfoPPTPCounter,'zxGponGemIWTPInfoOpState':zxGponGemIWTPInfoOpState,'zxGponGemIWTPInfoGALProPtr':zxGponGemIWTPInfoGALProPtr,'zxGponGemIWTPInfoGEMLoopbackCfg':zxGponGemIWTPInfoGEMLoopbackCfg,'zxGponGemIWTPInfoMgmtCtrlFlag':zxGponGemIWTPInfoMgmtCtrlFlag,'zxGponGemIWTPInfoEntryStatus':zxGponGemIWTPInfoEntryStatus,'zxGponGemIWTPAlarmTable':zxGponGemIWTPAlarmTable,'zxGponGemIWTPAlarmEntry':zxGponGemIWTPAlarmEntry,_Am:zxGponGemIWTPAlarmIndex,'zxGponGemIWTPAlarmMeId':zxGponGemIWTPAlarmMeId,'zxGponGemIWTPGFSAAlarm':zxGponGemIWTPGFSAAlarm,'zxGponGemIWTPGFSAAlarmMask':zxGponGemIWTPGFSAAlarmMask,'zxGponConnMgmt':zxGponConnMgmt,'zxGponGemPNCTPInfoTable':zxGponGemPNCTPInfoTable,'zxGponGemPNCTPInfoEntry':zxGponGemPNCTPInfoEntry,_x:zxGponGemPNCTPInfoMeIdIdx,'zxGponGemPNCTPInfoPortId':zxGponGemPNCTPInfoPortId,'zxGponGemPNCTPInfoPONTCAdapterGPtr':zxGponGemPNCTPInfoPONTCAdapterGPtr,'zxGponGemPNCTPInfoDirection':zxGponGemPNCTPInfoDirection,'zxGponGemPNCTPInfoPriorityUpstream':zxGponGemPNCTPInfoPriorityUpstream,'zxGponGemPNCTPInfoPriorityDownstream':zxGponGemPNCTPInfoPriorityDownstream,'zxGponGemPNCTPInfoTDescProfPtr':zxGponGemPNCTPInfoTDescProfPtr,'zxGponGemPNCTPInfoUniCounter':zxGponGemPNCTPInfoUniCounter,'zxGponGemPNCTPInfoMgmtCtrlFlag':zxGponGemPNCTPInfoMgmtCtrlFlag,'zxGponGemPNCTPInfoEntryStatus':zxGponGemPNCTPInfoEntryStatus,'zxGponGemPNCTPAlarmCfgTable':zxGponGemPNCTPAlarmCfgTable,'zxGponGemPNCTPAlarmCfgEntry':zxGponGemPNCTPAlarmCfgEntry,'zxGponGemPNCTPAlarmCfgMeId':zxGponGemPNCTPAlarmCfgMeId,'zxGponGemPNCTPAlarmCfgE2eLossContinuity':zxGponGemPNCTPAlarmCfgE2eLossContinuity,'zxGponGemPNCTPAlarmCfgE2eLossContinuityMask':zxGponGemPNCTPAlarmCfgE2eLossContinuityMask,'zxGponGemPPPMHDInfoTable':zxGponGemPPPMHDInfoTable,'zxGponGemPPPMHDInfoEntry':zxGponGemPPPMHDInfoEntry,_y:zxGponGemPPPMHDInfoMeIdIdx,'zxGponGemPPPMHDInfoIntervalEndTime':zxGponGemPPPMHDInfoIntervalEndTime,'zxGponGemPPPMHDInfoThresholdDataID':zxGponGemPPPMHDInfoThresholdDataID,'zxGponGemPPPMHDInfoLostPackets':zxGponGemPPPMHDInfoLostPackets,'zxGponGemPPPMHDInfoMisinsertedPackets':zxGponGemPPPMHDInfoMisinsertedPackets,'zxGponGemPPPMHDInfoReceivedPackets':zxGponGemPPPMHDInfoReceivedPackets,'zxGponGemPPPMHDInfoReceivedBlocks':zxGponGemPPPMHDInfoReceivedBlocks,'zxGponGemPPPMHDInfoTransmittedBlocks':zxGponGemPPPMHDInfoTransmittedBlocks,'zxGponGemPPPMHDInfoImpairedBlocks':zxGponGemPPPMHDInfoImpairedBlocks,'zxGponGemPPPMHDAlarmCfgTable':zxGponGemPPPMHDAlarmCfgTable,'zxGponGemPPPMHDAlarmCfgEntry':zxGponGemPPPMHDAlarmCfgEntry,'zxGponGemPPPMHDAlarmCfgMeId':zxGponGemPPPMHDAlarmCfgMeId,'zxGponGemPPPMHDAlarmCfgLosPkgs':zxGponGemPPPMHDAlarmCfgLosPkgs,'zxGponGemPPPMHDAlarmCfgLosPkgsMask':zxGponGemPPPMHDAlarmCfgLosPkgsMask,'zxGponGemPPPMHDAlarmCfgMisInsertPkgs':zxGponGemPPPMHDAlarmCfgMisInsertPkgs,'zxGponGemPPPMHDAlarmCfgMisInsertPkgsMask':zxGponGemPPPMHDAlarmCfgMisInsertPkgsMask,'zxGponGemPPPMHDAlarmCfgImpairBlks':zxGponGemPPPMHDAlarmCfgImpairBlks,'zxGponGemPPPMHDAlarmCfgImpairBlksMask':zxGponGemPPPMHDAlarmCfgImpairBlksMask,'zxGponTrafficMgmt':zxGponTrafficMgmt,'zxGponPriorityQueueTable':zxGponPriorityQueueTable,'zxGponPriorityQueueEntry':zxGponPriorityQueueEntry,_Ao:zxGponPriorQueueIndex,'zxGponPriorQueueMeId':zxGponPriorQueueMeId,'zxGponPriorQueueCfgOption':zxGponPriorQueueCfgOption,'zxGponPriorQueueMaxQueueSize':zxGponPriorQueueMaxQueueSize,'zxGponPriorQueueAllocSize':zxGponPriorQueueAllocSize,'zxGponPriorQueueInterval':zxGponPriorQueueInterval,'zxGponPriorQueueBufOverflowThreshold':zxGponPriorQueueBufOverflowThreshold,'zxGponPriorQueueRelatedPort':zxGponPriorQueueRelatedPort,'zxGponPriorQueueTrafficSchedulerGPtr':zxGponPriorQueueTrafficSchedulerGPtr,'zxGponPriorQueueWeight':zxGponPriorQueueWeight,'zxGponPriorQueueBackPressureAdmin':zxGponPriorQueueBackPressureAdmin,'zxGponPriorQueueBackPressureTime':zxGponPriorQueueBackPressureTime,'zxGponPriorQueueBackPressAssertThresh':zxGponPriorQueueBackPressAssertThresh,'zxGponPriorQueueBackPressClearThresh':zxGponPriorQueueBackPressClearThresh,'zxGponPriorityQueueAlarmCfgTable':zxGponPriorityQueueAlarmCfgTable,'zxGponPriorityQueueAlarmCfgEntry':zxGponPriorityQueueAlarmCfgEntry,_Ap:zxGponPriorQueueAlarmIndex,'zxGponPriorQueueAlarmMeId':zxGponPriorQueueAlarmMeId,'zxGponPriorQueueAlarmCellLosThresh':zxGponPriorQueueAlarmCellLosThresh,'zxGponPriorQueueAlarmCellLosThreshMask':zxGponPriorQueueAlarmCellLosThreshMask,'zxGponTrafficScheduleTable':zxGponTrafficScheduleTable,'zxGponTrafficScheduleEntry':zxGponTrafficScheduleEntry,_Aq:zxGponTrafficScheduleIndex,'zxGponTrafficScheduleMeId':zxGponTrafficScheduleMeId,'zxGponTrafficScheduleTCountPtr':zxGponTrafficScheduleTCountPtr,'zxGponTrafficScheduleOtherPtr':zxGponTrafficScheduleOtherPtr,'zxGponTrafficSchedulePolicy':zxGponTrafficSchedulePolicy,'zxGponTrafficSchedulePriWeight':zxGponTrafficSchedulePriWeight,'zxGponGemTrafficDescriptorsTable':zxGponGemTrafficDescriptorsTable,'zxGponGemTrafficDescriptorsEntry':zxGponGemTrafficDescriptorsEntry,_Ar:zxGponGemTrafficDescriptorsMeIdIdx,'zxGponGemTrafficDescriptorsSIR':zxGponGemTrafficDescriptorsSIR,'zxGponGemTrafficDescriptorsPIR':zxGponGemTrafficDescriptorsPIR,'zxGponGemTrafficDescriptorsMgmtCtrlFlag':zxGponGemTrafficDescriptorsMgmtCtrlFlag,'zxGponGemTrafficDescriptorsEntryStatus':zxGponGemTrafficDescriptorsEntryStatus,'zxGponProfileMgmt':zxGponProfileMgmt,'zxGponBandwidthProfileTable':zxGponBandwidthProfileTable,'zxGponBandwidthProfileEntry':zxGponBandwidthProfileEntry,_As:zxGponBWProfileIndex,'zxGponBWProfileName':zxGponBWProfileName,'zxGponBWProfileFixed':zxGponBWProfileFixed,'zxGponBWProfileAssured':zxGponBWProfileAssured,'zxGponBWProfileMaximum':zxGponBWProfileMaximum,'zxGponBWProfileType':zxGponBWProfileType,'zxGponBWProfileRefCnt':zxGponBWProfileRefCnt,'zxGponBWProfileEntryStatus':zxGponBWProfileEntryStatus,'zxGponTrafficProfileTable':zxGponTrafficProfileTable,'zxGponTrafficProfileEntry':zxGponTrafficProfileEntry,_At:zxGponTrafficProfileIndex,'zxGponTrafficProfileName':zxGponTrafficProfileName,'zxGponTrafficProfileSir':zxGponTrafficProfileSir,'zxGponTrafficProfilePir':zxGponTrafficProfilePir,'zxGponTrafficProfileRefCnt':zxGponTrafficProfileRefCnt,'zxGponTrafficProfileEntryStatus':zxGponTrafficProfileEntryStatus,'zxGponThresholdDataProfileTable':zxGponThresholdDataProfileTable,'zxGponThresholdDataProfileEntry':zxGponThresholdDataProfileEntry,_Au:zxGponThresholdDataProfileIndex,'zxGponThresholdDataProfileName':zxGponThresholdDataProfileName,'zxGponThresholdDataProfileVal1':zxGponThresholdDataProfileVal1,'zxGponThresholdDataProfileVal2':zxGponThresholdDataProfileVal2,'zxGponThresholdDataProfileVal3':zxGponThresholdDataProfileVal3,'zxGponThresholdDataProfileVal4':zxGponThresholdDataProfileVal4,'zxGponThresholdDataProfileVal5':zxGponThresholdDataProfileVal5,'zxGponThresholdDataProfileVal6':zxGponThresholdDataProfileVal6,'zxGponThresholdDataProfileVal7':zxGponThresholdDataProfileVal7,'zxGponThresholdDataProfileVal8':zxGponThresholdDataProfileVal8,'zxGponThresholdDataProfileVal9':zxGponThresholdDataProfileVal9,'zxGponThresholdDataProfileVal10':zxGponThresholdDataProfileVal10,'zxGponThresholdDataProfileVal11':zxGponThresholdDataProfileVal11,'zxGponThresholdDataProfileVal12':zxGponThresholdDataProfileVal12,'zxGponThresholdDataProfileVal13':zxGponThresholdDataProfileVal13,'zxGponThresholdDataProfileVal14':zxGponThresholdDataProfileVal14,'zxGponThresholdDataProfileRefCnt':zxGponThresholdDataProfileRefCnt,'zxGponThresholdDataProfileEntryStatus':zxGponThresholdDataProfileEntryStatus,'zxGponStandardOnu':zxGponStandardOnu,'zxGponOnuEncryptTable':zxGponOnuEncryptTable,'zxGponOnuEncryptEntry':zxGponOnuEncryptEntry,'zxGponOnuEncryptDir':zxGponOnuEncryptDir,'zxGponOnuEncryptEnable':zxGponOnuEncryptEnable,'zxGponOnuEncryptMode':zxGponOnuEncryptMode,'zxGponPortIdEncryptTable':zxGponPortIdEncryptTable,'zxGponPortIdEncryptEntry':zxGponPortIdEncryptEntry,'zxGponPortIdEncryptEnable':zxGponPortIdEncryptEnable,'zxGponOnuAlarmStatusTable':zxGponOnuAlarmStatusTable,'zxGponOnuAlarmStatusEntry':zxGponOnuAlarmStatusEntry,'zxGponOnuAlarmLOSd':zxGponOnuAlarmLOSd,'zxGponOnuAlarmLOSdMask':zxGponOnuAlarmLOSdMask,'zxGponOnuAlarmLOFd':zxGponOnuAlarmLOFd,'zxGponOnuAlarmLOFdMask':zxGponOnuAlarmLOFdMask,'zxGponOnuAlarmSFd':zxGponOnuAlarmSFd,'zxGponOnuAlarmSFdMask':zxGponOnuAlarmSFdMask,'zxGponOnuAlarmSDd':zxGponOnuAlarmSDd,'zxGponOnuAlarmSDdMask':zxGponOnuAlarmSDdMask,'zxGponOnuAlarmLCDAd':zxGponOnuAlarmLCDAd,'zxGponOnuAlarmLCDAdMask':zxGponOnuAlarmLCDAdMask,'zxGponOnuAlarmLCDGd':zxGponOnuAlarmLCDGd,'zxGponOnuAlarmLCDGdMask':zxGponOnuAlarmLCDGdMask,'zxGponOnuAlarmTFd':zxGponOnuAlarmTFd,'zxGponOnuAlarmTFdMask':zxGponOnuAlarmTFdMask,'zxGponOnuAlarmSUFd':zxGponOnuAlarmSUFd,'zxGponOnuAlarmSUFdMask':zxGponOnuAlarmSUFdMask,'zxGponOnuAlarmMEMd':zxGponOnuAlarmMEMd,'zxGponOnuAlarmMEMdMask':zxGponOnuAlarmMEMdMask,'zxGponOnuAlarmDACTd':zxGponOnuAlarmDACTd,'zxGponOnuAlarmDACTdMask':zxGponOnuAlarmDACTdMask,'zxGponOnuAlarmDISd':zxGponOnuAlarmDISd,'zxGponOnuAlarmDISdMask':zxGponOnuAlarmDISdMask,'zxGponOnuAlarmMISd':zxGponOnuAlarmMISd,'zxGponOnuAlarmMISdMask':zxGponOnuAlarmMISdMask,'zxGponOnuAlarmPEEd':zxGponOnuAlarmPEEd,'zxGponOnuAlarmPEEdMask':zxGponOnuAlarmPEEdMask,'zxGponOnuAlarmRDId':zxGponOnuAlarmRDId,'zxGponOnuAlarmRDIdMask':zxGponOnuAlarmRDIdMask,'zxGponSignalThresholdTable':zxGponSignalThresholdTable,'zxGponSignalThresholdEntry':zxGponSignalThresholdEntry,'zxGponSignalThresholdSDd':zxGponSignalThresholdSDd,'zxGponSignalThresholdSFd':zxGponSignalThresholdSFd,'zxGponOnuPerfStatisticTable':zxGponOnuPerfStatisticTable,'zxGponOnuPerfStatisticEntry':zxGponOnuPerfStatisticEntry,'zxGponOnuPerfStatERRdCounter':zxGponOnuPerfStatERRdCounter,'zxGponOnuPerfStatBIPErrCounter':zxGponOnuPerfStatBIPErrCounter,'zxGponOnuWeightTable':zxGponOnuWeightTable,'zxGponOnuWeightEntry':zxGponOnuWeightEntry,'zxGponOnuSchedulemode':zxGponOnuSchedulemode,'zxGponOnuCos1Weight':zxGponOnuCos1Weight,'zxGponOnuCos2Weight':zxGponOnuCos2Weight,'zxGponOnuCos3Weight':zxGponOnuCos3Weight,'zxGponOnuCos4Weight':zxGponOnuCos4Weight,'zxGponOnuDownTrafficPtr':zxGponOnuDownTrafficPtr,'zxGponPrivateOnu':zxGponPrivateOnu,'zxGponOntDevMgmtTable':zxGponOntDevMgmtTable,'zxGponOntDevMgmtEntry':zxGponOntDevMgmtEntry,_J:zxGponOntDevMgmtTypeName,_L:zxGponOntDevMgmtName,_M:zxGponOntDevMgmtDescription,'zxGponOntDevMgmtRegisterId':zxGponOntDevMgmtRegisterId,'zxGponOntDevMgmtProvisionSn':zxGponOntDevMgmtProvisionSn,'zxGponOntDevMgmtPwMode':zxGponOntDevMgmtPwMode,'zxGponOntDevMgmtPassword':zxGponOntDevMgmtPassword,'zxGponOntTargetState':zxGponOntTargetState,'zxGponOntDevMgmtEntryStatus':zxGponOntDevMgmtEntryStatus,'zxGponOntIsAutoUpdate':zxGponOntIsAutoUpdate,'zxGponOntRegMode':zxGponOntRegMode,'zxGponOntRegId':zxGponOntRegId,'zxGponOntStateTable':zxGponOntStateTable,'zxGponOntStateEntry':zxGponOntStateEntry,'zxGponOntAdminState':zxGponOntAdminState,'zxGponOntOmccState':zxGponOntOmccState,'zxGponOntO1O7State':zxGponOntO1O7State,'zxGponOntPhaseState':zxGponOntPhaseState,'zxGponOntDevInfoTable':zxGponOntDevInfoTable,'zxGponOntDevInfoEntry':zxGponOntDevInfoEntry,'zxGponOntDevInfoSupportTcontNum':zxGponOntDevInfoSupportTcontNum,'zxGponOntDevInfoCurUsedTcontNum':zxGponOntDevInfoCurUsedTcontNum,'zxGponOntDevInfoSupportPortIdNum':zxGponOntDevInfoSupportPortIdNum,'zxGponOntDevInfoCurUsedPortIdNum':zxGponOntDevInfoCurUsedPortIdNum,'zxGponOntDevInfoPqNum':zxGponOntDevInfoPqNum,'zxGponOntDevInfoTsNum':zxGponOntDevInfoTsNum,'zxGponOntDevInfoServiceType':zxGponOntDevInfoServiceType,'zxGponOntDevInfoRealOnuId':zxGponOntDevInfoRealOnuId,'zxGponOntUniPortInfoTable':zxGponOntUniPortInfoTable,'zxGponOntUniPortInfoEntry':zxGponOntUniPortInfoEntry,'zxGponOntUniPortInfoTotalUniPorts':zxGponOntUniPortInfoTotalUniPorts,'zxGponOntUniPortInfoE1Ports':zxGponOntUniPortInfoE1Ports,'zxGponOntUniPortInfoT1Ports':zxGponOntUniPortInfoT1Ports,'zxGponOntUniPortInfoSTMPorts':zxGponOntUniPortInfoSTMPorts,'zxGponOntUniPortInfoPOTSPorts':zxGponOntUniPortInfoPOTSPorts,'zxGponOntUniPortInfoEthPorts':zxGponOntUniPortInfoEthPorts,'zxGponOntUniPortInfoRFPorts':zxGponOntUniPortInfoRFPorts,'zxGponOntUniPortInfoMoCAPorts':zxGponOntUniPortInfoMoCAPorts,'zxGponOntUniPortInfoWiFiPorts':zxGponOntUniPortInfoWiFiPorts,'zxGponOntUniPortInfoAdslPorts':zxGponOntUniPortInfoAdslPorts,'zxGponOntUniPortInfoVdslPorts':zxGponOntUniPortInfoVdslPorts,'zxGponOntPmStatisInfoTable':zxGponOntPmStatisInfoTable,'zxGponOntPmStatisInfoEntry':zxGponOntPmStatisInfoEntry,'zxGponOntPmStatisInfoGemPacketTxLo':zxGponOntPmStatisInfoGemPacketTxLo,'zxGponOntPmStatisInfoGemPacketRxCorIdleLo':zxGponOntPmStatisInfoGemPacketRxCorIdleLo,'zxGponOntPmStatisInfoGemPacketRxCorNoIdleLo':zxGponOntPmStatisInfoGemPacketRxCorNoIdleLo,'zxGponOntPmStatisInfoGemPacketRxErrLo':zxGponOntPmStatisInfoGemPacketRxErrLo,'zxGponOntPmStatisInfoGemPayloadBytesRxLo':zxGponOntPmStatisInfoGemPayloadBytesRxLo,'zxGponOntPmStatisInfoEthPacketTxLo':zxGponOntPmStatisInfoEthPacketTxLo,'zxGponOntPmStatisInfoEthPacketRxCorLo':zxGponOntPmStatisInfoEthPacketRxCorLo,'zxGponOntPmStatisInfoEthPacketRxErrLo':zxGponOntPmStatisInfoEthPacketRxErrLo,'zxGponOntPmStatisInfoOmciPacketTxLo':zxGponOntPmStatisInfoOmciPacketTxLo,'zxGponOntPmStatisInfoOmciPacketRxLo':zxGponOntPmStatisInfoOmciPacketRxLo,'zxGponOntPmStatisInfoOmciPacketRxCorLo':zxGponOntPmStatisInfoOmciPacketRxCorLo,'zxGponOntPmStatisInfoOmciPacketRxErrLo':zxGponOntPmStatisInfoOmciPacketRxErrLo,'zxGponOntPmStatisInfoPloamTxLo':zxGponOntPmStatisInfoPloamTxLo,'zxGponOntPmStatisInfoPloamRxCorLo':zxGponOntPmStatisInfoPloamRxCorLo,'zxGponOntPmStatisInfoPloamRxErrLo':zxGponOntPmStatisInfoPloamRxErrLo,'zxGponOntPmStatisInfoBipErrorRxLo':zxGponOntPmStatisInfoBipErrorRxLo,'zxGponOntPmStatisInfoERRLo':zxGponOntPmStatisInfoERRLo,'zxGponOntPmStatisInfoREILo':zxGponOntPmStatisInfoREILo,'zxGponOntPmStatisRealtimeInfoTable':zxGponOntPmStatisRealtimeInfoTable,'zxGponOntPmStatisRealtimeInfoEntry':zxGponOntPmStatisRealtimeInfoEntry,'zxGponOntPmStatisInfoCorrectNonIdleGemFramesUpstream':zxGponOntPmStatisInfoCorrectNonIdleGemFramesUpstream,'zxGponOntPmStatisInfoCorrectIdleGemFramesUpstream':zxGponOntPmStatisInfoCorrectIdleGemFramesUpstream,'zxGponOntPmStatisInfoErroredGemFramesUpstream':zxGponOntPmStatisInfoErroredGemFramesUpstream,'zxGponOntPmStatisInfoGemPayloadBytesUpstream':zxGponOntPmStatisInfoGemPayloadBytesUpstream,'zxGponOntPmStatisInfoCorrectEthernetFramesUpstream':zxGponOntPmStatisInfoCorrectEthernetFramesUpstream,'zxGponOntPmStatisInfoErroredEthernetFramesUpstream':zxGponOntPmStatisInfoErroredEthernetFramesUpstream,'zxGponOntPmStatisInfoTotalOmciFramesUpstream':zxGponOntPmStatisInfoTotalOmciFramesUpstream,'zxGponOntPmStatisInfoERRi':zxGponOntPmStatisInfoERRi,'zxGponOntPmStatisInfoREIi':zxGponOntPmStatisInfoREIi,'zxGponOntPmStatisInfoUnreceivedBurstsUpstream':zxGponOntPmStatisInfoUnreceivedBurstsUpstream,'zxGponOntPmStatisInfoBipErrorUpstream':zxGponOntPmStatisInfoBipErrorUpstream,'zxGponOntPmStatisInfoCorrectedBitsUpstream':zxGponOntPmStatisInfoCorrectedBitsUpstream,'zxGponOntPmStatisInfoNotCorrectedWordsUpstream':zxGponOntPmStatisInfoNotCorrectedWordsUpstream,'zxGponOntPmStatisHistoryInfoTable':zxGponOntPmStatisHistoryInfoTable,'zxGponOntPmStatisHistoryInfoEntry':zxGponOntPmStatisHistoryInfoEntry,'zxGponOntPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream':zxGponOntPmStatisHistoryInfoCorrectNonIdleGemFramesUpstream,'zxGponOntPmStatisHistoryInfoCorrectIdleGemFramesUpstream':zxGponOntPmStatisHistoryInfoCorrectIdleGemFramesUpstream,'zxGponOntPmStatisHistoryInfoErroredGemFramesUpstream':zxGponOntPmStatisHistoryInfoErroredGemFramesUpstream,'zxGponOntPmStatisHistoryInfoGemPayloadBytesUpstream':zxGponOntPmStatisHistoryInfoGemPayloadBytesUpstream,'zxGponOntPmStatisHistoryInfoCorrectEthernetFramesUpstream':zxGponOntPmStatisHistoryInfoCorrectEthernetFramesUpstream,'zxGponOntPmStatisHistoryInfoErroredEthernetFramesUpstream':zxGponOntPmStatisHistoryInfoErroredEthernetFramesUpstream,'zxGponOntPmStatisHistoryInfoTotalOmciFramesUpstream':zxGponOntPmStatisHistoryInfoTotalOmciFramesUpstream,'zxGponOntPmStatisHistoryInfoERRi':zxGponOntPmStatisHistoryInfoERRi,'zxGponOntPmStatisHistoryInfoREIi':zxGponOntPmStatisHistoryInfoREIi,'zxGponOntPmStatisHistoryInfoUnreceivedBurstsUpstream':zxGponOntPmStatisHistoryInfoUnreceivedBurstsUpstream,'zxGponOntPmStatisHistoryInfoBipErrorUpstream':zxGponOntPmStatisHistoryInfoBipErrorUpstream,'zxGponOntPmStatisHistoryInfoCorrectedBitsUpstream':zxGponOntPmStatisHistoryInfoCorrectedBitsUpstream,'zxGponOntPmStatisHistoryInfoNotCorrectedWordsUpstream':zxGponOntPmStatisHistoryInfoNotCorrectedWordsUpstream,'zxGponOntLoopbackTestInfoTable':zxGponOntLoopbackTestInfoTable,'zxGponOntLoopbackTestInfoEntry':zxGponOntLoopbackTestInfoEntry,'zxGponOntLoopbackTestStart':zxGponOntLoopbackTestStart,'zxGponServiceMgmt':zxGponServiceMgmt,'zxOnuTrafficMgmtUnitTable':zxOnuTrafficMgmtUnitTable,'zxOnuTrafficMgmtUnitEntry':zxOnuTrafficMgmtUnitEntry,_Av:zxOnuTrafficMgmtUnitTcontIdx,'zxOnuTrafficMgmtUnitName':zxOnuTrafficMgmtUnitName,'zxOnuTrafficMgmtUnitTcontUpBWIdxPtr':zxOnuTrafficMgmtUnitTcontUpBWIdxPtr,'zxOnuTrafficMgmtUnitAllocId':zxOnuTrafficMgmtUnitAllocId,'zxOnuTrafficMgmtUnitUsedPortIdNum':zxOnuTrafficMgmtUnitUsedPortIdNum,'zxOnuTrafficMgmtUnitUsedFlowNum':zxOnuTrafficMgmtUnitUsedFlowNum,'zxOnuTrafficMgmtUnitUsedCos':zxOnuTrafficMgmtUnitUsedCos,'zxOnuTrafficMgmtUnitEntryStatus':zxOnuTrafficMgmtUnitEntryStatus,'zxGponGemPortTable':zxGponGemPortTable,'zxGponGemPortEntry':zxGponGemPortEntry,_P:zxGponGemPortIdx,'zxGponGemPortName':zxGponGemPortName,'zxGponGemPortType':zxGponGemPortType,'zxGponGemPortTcontIdx':zxGponGemPortTcontIdx,'zxGponGemPortDirection':zxGponGemPortDirection,'zxGponGemPortUpTrafficPtr':zxGponGemPortUpTrafficPtr,'zxGponGemPortDownTrafficPtr':zxGponGemPortDownTrafficPtr,'zxGponGemPortPortId':zxGponGemPortPortId,'zxGponGemPortDefaultCosType':zxGponGemPortDefaultCosType,'zxGponGemPortEntryStatus':zxGponGemPortEntryStatus,'zxGponGemPortUpQueue':zxGponGemPortUpQueue,'zxGponGemPortBasicTable':zxGponGemPortBasicTable,'zxGponGemPortBasicEntry':zxGponGemPortBasicEntry,'zxGponGemBasicPNCTPInfoDirection':zxGponGemBasicPNCTPInfoDirection,'zxGponGemBasicPNCTPInfoPriorityUpstreamID':zxGponGemBasicPNCTPInfoPriorityUpstreamID,'zxGponGemBasicPNCTPInfoPriorityDownstreamID':zxGponGemBasicPNCTPInfoPriorityDownstreamID,'zxGponGemBasicPNCTPInfoUniCounter':zxGponGemBasicPNCTPInfoUniCounter,'zxGponGemBasicIWTPInfoIwOption':zxGponGemBasicIWTPInfoIwOption,'zxGponGemBasicIWTPInfoServiceProPtr':zxGponGemBasicIWTPInfoServiceProPtr,'zxGponGemBasicIWTPInfoPPTPCounter':zxGponGemBasicIWTPInfoPPTPCounter,'zxGponGemBasicIWTPInfoOpState':zxGponGemBasicIWTPInfoOpState,'zxGponBasicGALTDMProfileInfoFrameLossIntPeriod':zxGponBasicGALTDMProfileInfoFrameLossIntPeriod,'zxGponBasicGALEthProfileInfoMaxPayloadSize':zxGponBasicGALEthProfileInfoMaxPayloadSize,'zxGponGemBasicMgmtCtrlFlag':zxGponGemBasicMgmtCtrlFlag,'zxGponGemBasicEntryStatus':zxGponGemBasicEntryStatus,'zxGponGemPortMACBridgeIWTPTable':zxGponGemPortMACBridgeIWTPTable,'zxGponGemPortMACBridgeIWTPEntry':zxGponGemPortMACBridgeIWTPEntry,'zxGponMACBriPortCfgDataIWTPMeIdIdx':zxGponMACBriPortCfgDataIWTPMeIdIdx,'zxGponMACBriPortCfgDataIWTPPortNum':zxGponMACBriPortCfgDataIWTPPortNum,'zxGponMACBriPortCfgDataIWTPTPType':zxGponMACBriPortCfgDataIWTPTPType,'zxGponMACBriPortCfgDataIWTPPortPriority':zxGponMACBriPortCfgDataIWTPPortPriority,'zxGponMACBriPortCfgDataIWTPPortPathCost':zxGponMACBriPortCfgDataIWTPPortPathCost,'zxGponMACBriPortCfgDataIWTPPortSpanTreeInd':zxGponMACBriPortCfgDataIWTPPortSpanTreeInd,'zxGponMACBriPortCfgDataIWTPEncapMethod':zxGponMACBriPortCfgDataIWTPEncapMethod,'zxGponMACBriPortCfgDataIWTPLANFCSInd':zxGponMACBriPortCfgDataIWTPLANFCSInd,'zxGponMACBriPortCfgDataIWTPMgmtCtrlFlag':zxGponMACBriPortCfgDataIWTPMgmtCtrlFlag,'zxGponMACBriPortCfgDataIWTPEntryStatus':zxGponMACBriPortCfgDataIWTPEntryStatus,'zxGponGemPortMACBridgeUNITable':zxGponGemPortMACBridgeUNITable,'zxGponGemPortMACBridgeUNIEntry':zxGponGemPortMACBridgeUNIEntry,'zxGponMACBriPortCfgDataUNIMeIdIdx':zxGponMACBriPortCfgDataUNIMeIdIdx,'zxGponMACBriPortCfgDataUNIPortNum':zxGponMACBriPortCfgDataUNIPortNum,'zxGponMACBriPortCfgDataUNITPType':zxGponMACBriPortCfgDataUNITPType,'zxGponMACBriPortCfgDataUNIPortPriority':zxGponMACBriPortCfgDataUNIPortPriority,'zxGponMACBriPortCfgDataUNIPortPathCost':zxGponMACBriPortCfgDataUNIPortPathCost,'zxGponMACBriPortCfgDataUNIPortSpanTreeInd':zxGponMACBriPortCfgDataUNIPortSpanTreeInd,'zxGponMACBriPortCfgDataUNIEncapMethod':zxGponMACBriPortCfgDataUNIEncapMethod,'zxGponMACBriPortCfgDataUNILANFCSInd':zxGponMACBriPortCfgDataUNILANFCSInd,'zxGponGemPort8021pTable':zxGponGemPort8021pTable,'zxGponGemPort8021pEntry':zxGponGemPort8021pEntry,'zxGponGemPort8021pMapperUntagFrmInd':zxGponGemPort8021pMapperUntagFrmInd,'zxGponGemPort8021pMapperDscpTo8021pPri':zxGponGemPort8021pMapperDscpTo8021pPri,'zxGponGemPort8021pMapperDefaultPri':zxGponGemPort8021pMapperDefaultPri,'zxGponGemPort8021pMapperTPType':zxGponGemPort8021pMapperTPType,'zxGponGemPortStructuredCESTable':zxGponGemPortStructuredCESTable,'zxGponGemPortStructuredCESEntry':zxGponGemPortStructuredCESEntry,'zxGponLogicalSubportCTPMeIdIdx':zxGponLogicalSubportCTPMeIdIdx,'zxGponLogicalSubportCTPTimeSlots':zxGponLogicalSubportCTPTimeSlots,'zxGponGemPortIpRouterIWTPTable':zxGponGemPortIpRouterIWTPTable,'zxGponGemPortIpRouterIWTPEntry':zxGponGemPortIpRouterIWTPEntry,'zxGponGemPortIpPortCfgDataIWTPMeIdIdx':zxGponGemPortIpPortCfgDataIWTPMeIdIdx,'zxGponGemPortIpPortCfgDataIWTPPortNum':zxGponGemPortIpPortCfgDataIWTPPortNum,'zxGponGemPortIpPortCfgDataIWTPTPType':zxGponGemPortIpPortCfgDataIWTPTPType,'zxGponGemPortIpPortCfgDataIWTPPortAddress':zxGponGemPortIpPortCfgDataIWTPPortAddress,'zxGponGemPortIpPortCfgDataIWTPPortMask':zxGponGemPortIpPortCfgDataIWTPPortMask,'zxGponGemPortIpPortCfgDataIWTPUnnumbered':zxGponGemPortIpPortCfgDataIWTPUnnumbered,'zxGponGemPortIpPortCfgDataIWTPAdministrativeState':zxGponGemPortIpPortCfgDataIWTPAdministrativeState,'zxGponGemPortIpPortCfgDataIWTPPortState':zxGponGemPortIpPortCfgDataIWTPPortState,'zxGponGemPortIpPortCfgDataIWTPAllowRemoteAccess':zxGponGemPortIpPortCfgDataIWTPAllowRemoteAccess,'zxGponGemPortIpPortCfgDataIWTPEncapsulationMethod':zxGponGemPortIpPortCfgDataIWTPEncapsulationMethod,'zxGponGemPortIpRouterUNITable':zxGponGemPortIpRouterUNITable,'zxGponGemPortIpRouterUNIEntry':zxGponGemPortIpRouterUNIEntry,'zxGponGemPortIpPortCfgDataUNIMeIdIdx':zxGponGemPortIpPortCfgDataUNIMeIdIdx,'zxGponGemPortIpPortCfgDataUNIPortNum':zxGponGemPortIpPortCfgDataUNIPortNum,'zxGponGemPortIpPortCfgDataUNITPType':zxGponGemPortIpPortCfgDataUNITPType,'zxGponGemPortIpPortCfgDataUNIPortAddress':zxGponGemPortIpPortCfgDataUNIPortAddress,'zxGponGemPortIpPortCfgDataUNIPortMask':zxGponGemPortIpPortCfgDataUNIPortMask,'zxGponGemPortIpPortCfgDataUNIUnnumbered':zxGponGemPortIpPortCfgDataUNIUnnumbered,'zxGponGemPortIpPortCfgDataUNIAdministrativeState':zxGponGemPortIpPortCfgDataUNIAdministrativeState,'zxGponGemPortIpPortCfgDataUNIPortState':zxGponGemPortIpPortCfgDataUNIPortState,'zxGponGemPortIpPortCfgDataUNIAllowRemoteAccess':zxGponGemPortIpPortCfgDataUNIAllowRemoteAccess,'zxGponGemPortIpPortCfgDataUNIEncapsulationMethod':zxGponGemPortIpPortCfgDataUNIEncapsulationMethod,'zxGponGemPortIWTPMACBriPortFilterTableInfoTable':zxGponGemPortIWTPMACBriPortFilterTableInfoTable,'zxGponGemPortIWTPMACBriPortFilterTableInfoEntry':zxGponGemPortIWTPMACBriPortFilterTableInfoEntry,_Aw:zxGponGemPortIWTPMACBriPortFilterTableMacAddr,'zxGponGemPortIWTPMACBriPortFilterTableAction':zxGponGemPortIWTPMACBriPortFilterTableAction,'zxGponGemPortIWTPMACBriPortFilterTableEntryStatus':zxGponGemPortIWTPMACBriPortFilterTableEntryStatus,'zxGponGemPortUNIMACBriPortFilterTableInfoTable':zxGponGemPortUNIMACBriPortFilterTableInfoTable,'zxGponGemPortUNIMACBriPortFilterTableInfoEntry':zxGponGemPortUNIMACBriPortFilterTableInfoEntry,_Ax:zxGponGemPortUNIMACBriPortFilterTableMacAddr,'zxGponGemPortUNIMACBriPortFilterTableAction':zxGponGemPortUNIMACBriPortFilterTableAction,'zxGponGemPortUNIMACBriPortFilterTableEntryStatus':zxGponGemPortUNIMACBriPortFilterTableEntryStatus,'zxGponGemPortWeightTable':zxGponGemPortWeightTable,'zxGponGemPortWeightEntry':zxGponGemPortWeightEntry,'zxGponGemPortSchedulemode':zxGponGemPortSchedulemode,'zxGponGemPortCos1Weight':zxGponGemPortCos1Weight,'zxGponGemPortCos2Weight':zxGponGemPortCos2Weight,'zxGponGemPortCos3Weight':zxGponGemPortCos3Weight,'zxGponGemPortCos4Weight':zxGponGemPortCos4Weight,'zxGponGemPortPrioReGenTable':zxGponGemPortPrioReGenTable,'zxGponGemPortPrioReGenEntry':zxGponGemPortPrioReGenEntry,'zxGponGemPortPrioReGenMode':zxGponGemPortPrioReGenMode,'zxGponGemPortPrioReGenMap0':zxGponGemPortPrioReGenMap0,'zxGponGemPortPrioReGenMap1':zxGponGemPortPrioReGenMap1,'zxGponGemPortPrioReGenMap2':zxGponGemPortPrioReGenMap2,'zxGponGemPortPrioReGenMap3':zxGponGemPortPrioReGenMap3,'zxGponGemPortPrioReGenMap4':zxGponGemPortPrioReGenMap4,'zxGponGemPortPrioReGenMap5':zxGponGemPortPrioReGenMap5,'zxGponGemPortPrioReGenMap6':zxGponGemPortPrioReGenMap6,'zxGponGemPortPrioReGenMap7':zxGponGemPortPrioReGenMap7,'zxGponGemPortStaticsTable':zxGponGemPortStaticsTable,'zxGponGemPortStaticsEntry':zxGponGemPortStaticsEntry,'zxGponGemPortUpUcastPkts':zxGponGemPortUpUcastPkts,'zxGponGemPortUpMcastPkts':zxGponGemPortUpMcastPkts,'zxGponGemPortUpBcastPkts':zxGponGemPortUpBcastPkts,'zxGponGemPortUpPassedBytes':zxGponGemPortUpPassedBytes,'zxGponGemPortUpDroppedPkts':zxGponGemPortUpDroppedPkts,'zxGponGemPortDownUcastPkts':zxGponGemPortDownUcastPkts,'zxGponGemPortDownMcastPkts':zxGponGemPortDownMcastPkts,'zxGponGemPortDownBcastPkts':zxGponGemPortDownBcastPkts,'zxGponGemPortDownPassedBytes':zxGponGemPortDownPassedBytes,'zxGponGemPortDownDroppedPkts':zxGponGemPortDownDroppedPkts,'zxGponGemPortStaticsHistoryInfoTable':zxGponGemPortStaticsHistoryInfoTable,'zxGponGemPortStaticsHistoryInfoEntry':zxGponGemPortStaticsHistoryInfoEntry,'zxGponGemPortUpUcastPktsHistoryInfo':zxGponGemPortUpUcastPktsHistoryInfo,'zxGponGemPortUpMcastPktsHistoryInfo':zxGponGemPortUpMcastPktsHistoryInfo,'zxGponGemPortUpBcastPktsHistoryInfo':zxGponGemPortUpBcastPktsHistoryInfo,'zxGponGemPortUpPassedBytesHistoryInfo':zxGponGemPortUpPassedBytesHistoryInfo,'zxGponGemPortUpDroppedPktsHistoryInfo':zxGponGemPortUpDroppedPktsHistoryInfo,'zxGponGemPortDownUcastPktsHistoryInfo':zxGponGemPortDownUcastPktsHistoryInfo,'zxGponGemPortDownMcastPktsHistoryInfo':zxGponGemPortDownMcastPktsHistoryInfo,'zxGponGemPortDownBcastPktsHistoryInfo':zxGponGemPortDownBcastPktsHistoryInfo,'zxGponGemPortDownPassedBytesHistoryInfo':zxGponGemPortDownPassedBytesHistoryInfo,'zxGponGemPortDownDroppedPktsHistoryInfo':zxGponGemPortDownDroppedPktsHistoryInfo,'zxGponMacSpoofingObjects':zxGponMacSpoofingObjects,_A_:zxGponSpoofingPort,_B0:zxGponSpoofingMac,_B1:zxGponSpoofingVlan,_B2:zxGponSpoofingConflictPort,'zxGponTraps':zxGponTraps,'zxGponTrapsBindVar':zxGponTrapsBindVar,_z:zxGponOltRxPowerAlarmiReason,_Ay:zxGponOltRxPowerAbnormalInformiReason,_A0:zxGponOltTxPowerAlarmReason,_Az:zxGponOltTxPowerAbnormalInformReason,_A1:zxGponTrapEventString,'zxGponOltLOSi':zxGponOltLOSi,'zxGponOltLosiRestore':zxGponOltLosiRestore,'zxGponOltLOFi':zxGponOltLOFi,'zxGponOltLOFiRestore':zxGponOltLOFiRestore,'zxGponOltDOWi':zxGponOltDOWi,'zxGponOltDOWiRestore':zxGponOltDOWiRestore,'zxGponOltSFi':zxGponOltSFi,'zxGponOltSFiRestore':zxGponOltSFiRestore,'zxGponOltSDi':zxGponOltSDi,'zxGponOltSDiRestore':zxGponOltSDiRestore,'zxGponOltLCDAi':zxGponOltLCDAi,'zxGponOltLCDAiRestore':zxGponOltLCDAiRestore,'zxGponOltLCDGi':zxGponOltLCDGi,'zxGponOltLCDGiRestore':zxGponOltLCDGiRestore,'zxGponOltRDIi':zxGponOltRDIi,'zxGponOltRDIiRestore':zxGponOltRDIiRestore,'zxGponOltSUFi':zxGponOltSUFi,'zxGponOltSUFiRestore':zxGponOltSUFiRestore,'zxGponOltDFi':zxGponOltDFi,'zxGponOltDFiRestore':zxGponOltDFiRestore,'zxGponOltLOAi':zxGponOltLOAi,'zxGponOltLOAiRestore':zxGponOltLOAiRestore,'zxGponOltDGi':zxGponOltDGi,'zxGponOltDGiRestore':zxGponOltDGiRestore,'zxGponOltLOAMi':zxGponOltLOAMi,'zxGponOltLOAMiRestore':zxGponOltLOAMiRestore,'zxGponOltMEMi':zxGponOltMEMi,'zxGponOltMEMiRestore':zxGponOltMEMiRestore,'zxGponOltMISi':zxGponOltMISi,'zxGponOltMISiRestore':zxGponOltMISiRestore,'zxGponOltPEEi':zxGponOltPEEi,'zxGponOltPEEiRestore':zxGponOltPEEiRestore,'zxGponOntLOS':zxGponOntLOS,'zxGponOntLOSRestore':zxGponOntLOSRestore,'zxGponOntLOF':zxGponOntLOF,'zxGponOntLOFRestore':zxGponOntLOFRestore,'zxGponOntTF':zxGponOntTF,'zxGponOntTFRestore':zxGponOntTFRestore,'zxGponOntSF':zxGponOntSF,'zxGponOntSFRestore':zxGponOntSFRestore,'zxGponOntSD':zxGponOntSD,'zxGponOntSDRestore':zxGponOntSDRestore,'zxGponOntLCDA':zxGponOntLCDA,'zxGponOntLCDARestore':zxGponOntLCDARestore,'zxGponOntLCDG':zxGponOntLCDG,'zxGponOntLCDGRestore':zxGponOntLCDGRestore,'zxGponOntRDI':zxGponOntRDI,'zxGponOntRDIRestore':zxGponOntRDIRestore,'zxGponOntSUF':zxGponOntSUF,'zxGponOntSUFRestore':zxGponOntSUFRestore,'zxGponOntMEM':zxGponOntMEM,'zxGponOntMEMRestore':zxGponOntMEMRestore,'zxGponOntDACT':zxGponOntDACT,'zxGponOntDACTRestore':zxGponOntDACTRestore,'zxGponOntDIS':zxGponOntDIS,'zxGponOntDISRestore':zxGponOntDISRestore,'zxGponOntMIS':zxGponOntMIS,'zxGponOntMISRestore':zxGponOntMISRestore,'zxGponOntPee':zxGponOntPee,'zxGponOntPeeRestore':zxGponOntPeeRestore,'zxGponOltLOS':zxGponOltLOS,'zxGponOltLOSRestore':zxGponOltLOSRestore,'zxGponOltLOF':zxGponOltLOF,'zxGponOltLOFRestore':zxGponOltLOFRestore,'zxGponOntRegister':zxGponOntRegister,'zxGponOntUnregister':zxGponOntUnregister,'zxGponOntAuthPass':zxGponOntAuthPass,'zxGponOntAuthFailed':zxGponOntAuthFailed,'zxPonFanOffLine':zxPonFanOffLine,'zxPonFanOffLineRestore':zxPonFanOffLineRestore,'zxGponLinkOntDyingGasp':zxGponLinkOntDyingGasp,'zxGponLinkOntDyingGaspRestore':zxGponLinkOntDyingGaspRestore,'zxGponOltRxPowerAlarmi':zxGponOltRxPowerAlarmi,'zxGponOltRxPowerAlarmiRestore':zxGponOltRxPowerAlarmiRestore,'zxGponOltRxPowerAbnormalInformi':zxGponOltRxPowerAbnormalInformi,'zxGponOltRxPowerNormalInformi':zxGponOltRxPowerNormalInformi,'zxGponOltTxPowerAlarm':zxGponOltTxPowerAlarm,'zxGponOltTxPowerAlarmRestore':zxGponOltTxPowerAlarmRestore,'zxGponOltTxPowerAbnormalInform':zxGponOltTxPowerAbnormalInform,'zxGponOltTxPowerNormalInform':zxGponOltTxPowerNormalInform,'zxGponOltFakedSN':zxGponOltFakedSN,'zxGponOnuConstantOptical':zxGponOnuConstantOptical,'zxGponOnuConstantOpticalRestore':zxGponOnuConstantOpticalRestore,'zxGponOnuFiberBending':zxGponOnuFiberBending,'zxGponOnuFiberBendingRestore':zxGponOnuFiberBendingRestore,'zxGponOnuOpticalTransceiverLos':zxGponOnuOpticalTransceiverLos,'zxGponOnuOpticalTransceiverLosRestore':zxGponOnuOpticalTransceiverLosRestore,'zxGponMacSpoofing':zxGponMacSpoofing,'zxGponUnauthOnuOnline':zxGponUnauthOnuOnline,'zxGponOltTF':zxGponOltTF,'zxGponOltTFRestore':zxGponOltTFRestore,'zxGponOltFakedPassword':zxGponOltFakedPassword,'zxGponTermination':zxGponTermination,'zxGponTerminationDummy':zxGponTerminationDummy})