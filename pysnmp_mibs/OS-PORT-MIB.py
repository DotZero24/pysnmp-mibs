_Bb='osPortNotificationsGroup'
_Ba='osPortMandatoryGroup'
_BZ='osPortRecovery'
_BY='osPortIsolation'
_BX='osPortSfpAutoDetectErr'
_BW='osPortSfpI2cRecovery'
_BV='osPortSfpI2cFailure'
_BU='osPortSfpRemoved'
_BT='osPortSfpInserted'
_BS='osPortMgmtDisabled'
_BR='osPortMgmtEnabled'
_BQ='osPortFloodLimitRate'
_BP='osPortFloodLimitTypes'
_BO='osPortCntEgressClear'
_BN='osPortEgressCounter'
_BM='osPortEthType'
_BL='osPortCntRecvBadBytes'
_BK='osPortCntLateCollisions'
_BJ='osPortCntRecvAbove1023octsPacks'
_BI='osPortCntRecv512to1023octsPacks'
_BH='osPortCntRecv256to511octsPacks'
_BG='osPortCntRecv128to255octsPacks'
_BF='osPortCntRecv65to127octsPacks'
_BE='osPortCntRecvUpTo64octsPacks'
_BD='osPortCntRecvAndSentCollisions'
_BC='osPortCntRecvJabberPacks'
_BB='osPortCntRecvFragmentPacks'
_BA='osPortCntRecvLongPacks'
_B9='osPortCntRecvShortPacks'
_B8='osPortCntRecvCRCorAlignmentErrs'
_B7='osPortCntSentMultiPacks'
_B6='osPortCntSentBroadPacks'
_B5='osPortCntSentUniPacks'
_B4='osPortCntSentPacks'
_B3='osPortCntSentBytes'
_B2='osPortCntRecvMultiPacks'
_B1='osPortCntRecvBroadPacks'
_B0='osPortCntRecvUniPacks'
_A_='osPortCntRecvPacks'
_Az='osPortCntRecvBytes'
_Ay='osPortCntClearAll'
_Ax='osPortTrunkTearDown'
_Aw='osPortTrunkHigherThreshold'
_Av='osPortTrunkLowerThreshold'
_Au='osPortTrunkFastSwitchover'
_At='osPortTrunkRevertive'
_As='osPortTrunkMaxPortBundle'
_Ar='osPortCntEgressClearAll'
_Aq='osPortTrunkLastError'
_Ap='osPortTrunkNumOfMembers'
_Ao='osPortTrunkAdminStatus'
_An='osPortTrunkMembers'
_Am='osPortTrunkIndexId'
_Al='osPortBuffersWRED'
_Ak='osPortBuffersShared'
_Aj='osBuffersProfileWredThresholdRed'
_Ai='osBuffersProfileWredThresholdYellow'
_Ah='osBuffersProfileWredThresholdGreen'
_Ag='osBuffersProfileBuffersRed'
_Af='osBuffersProfileBuffersYellow'
_Ae='osBuffersProfileBuffersGreen'
_Ad='osBuffersProfileDescriptorsRed'
_Ac='osBuffersProfileDescriptorsYellow'
_Ab='osBuffersProfileDescriptorsGreen'
_Aa='osPortShapeMaxBurstSize'
_AZ='osPortShapeMinBurstSize'
_AY='osPortShapeMaxRate'
_AX='osPortShapeMinRate'
_AW='osPortShapeCapability'
_AV='osPortShapeAdminStatus'
_AU='osPortShapeLocked'
_AT='osPortShapeLastError'
_AS='osPortShapeBurstSize'
_AR='osPortShapeRate'
_AQ='osPortEthType2'
_AP='osPortEthType1'
_AO='osPortIfType'
_AN='osPortLanType'
_AM='osPortOperMediaSelect'
_AL='osPortAdminMediaSelect'
_AK='osPortL2CtrlPVST'
_AJ='osPortL2CtrlCDP'
_AI='osPortL2CtrlVTP'
_AH='osPortL2CtrlPAGP'
_AG='osPortL2CtrlDTP'
_AF='osPortL2CtrlLLDP'
_AE='osPortL2CtrlELMI'
_AD='osPortL2CtrlLinkOAM'
_AC='osPortL2CtrlPause'
_AB='osPortL2CtrlGVRP'
_AA='osPortL2CtrlSTP'
_A9='osPortL2CtrlLACP'
_A8='osPortL2CtrlDot1x'
_A7='osPortTagDefaultTag'
_A6='osPortTagType'
_A5='osPortRemarkingDei'
_A4='osPortQosTrust'
_A3='osPortQosMarkingVpt'
_A2='osPortMtuSize'
_A1='osPortLacpOperState'
_A0='osPortLacpAdminMode'
_z='osPortTrunkIndex'
_y='osPortBuffersProfileIndex'
_x='osPortBlockReason'
_w='osPortAdminState'
_v='osPortDuplex'
_u='osPortOperSpeed'
_t='osPortAdminSpeed'
_s='osPortLink'
_r='osPortCfgMaxTrunkId'
_q='osPortCfgMaxNumberOfSl'
_p='osPortCfgBaseTrunkPortIndex'
_o='osPortCfgMaxNumberOfPort'
_n='osPortCfgSupport'
_m='osPortCntEntry'
_l='osPortEgressValueType'
_k='osPortEgressUnits'
_j='osBufferProfileIndex'
_i='osPortShapeQId'
_h='sfpAutoDetect'
_g='sfpPlus'
_f='copper'
_e='sfp100'
_d='notApplicable'
_c='BuffersProfileIndex'
_b='DisplayString'
_a='Gauge32'
_Z='osPortMflgMac'
_Y='osPortLastError'
_X='Percentage'
_W='osBufferProfileServiceLevel'
_V='osPortTrunkId'
_U='KBytes'
_T='kilobits per second'
_S='osPortShapeDir'
_R='disabled'
_Q='clear'
_P='TruthValue'
_O='Bits'
_N='OctetString'
_M='enabled'
_L='osPortOperState'
_K='osPortDescription'
_J='osPortIndex'
_I='none'
_H='not-accessible'
_G='other'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='OS-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanIdOrNone,=mibBuilder.importSymbols('IEEE8021-CFM-MIB','VlanIdOrNone')
PortIndex,PortIndexOrNone,PortList,oaOptiSwitch=mibBuilder.importSymbols('OS-COMMON-TC-MIB','PortIndex','PortIndexOrNone','PortList','oaOptiSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_O,'Counter32','Counter64',_a,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_b,'MacAddress','PhysAddress','TextualConvention',_P)
osPort=ModuleIdentity((1,3,6,1,4,1,6926,2,1))
if mibBuilder.loadTexts:osPort.setRevisions(('2020-08-27 00:00','2019-12-26 00:00','2019-07-23 00:00','2018-12-09 00:00','2015-04-30 00:00','2014-06-09 00:00','2014-02-11 00:00','2013-09-17 00:00','2012-09-23 00:00','2012-06-24 00:00','2012-05-29 00:00','2010-11-02 00:00','2010-10-20 00:00','2010-08-05 00:00','2010-04-18 00:00','2008-01-08 00:00'))
class SupportValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSupported',1),('supported',2)))
class BuffersProfileIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
class L2CtrlProcess(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('drop',2),('peer',3),('tunnel',4)))
class PortEntryValidator(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
class LastError(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,160))
_OsPortNotifications_ObjectIdentity=ObjectIdentity
osPortNotifications=_OsPortNotifications_ObjectIdentity((1,3,6,1,4,1,6926,2,1,0))
_OsPortCfg_ObjectIdentity=ObjectIdentity
osPortCfg=_OsPortCfg_ObjectIdentity((1,3,6,1,4,1,6926,2,1,1))
_OsPortCfgSupport_Type=SupportValue
_OsPortCfgSupport_Object=MibScalar
osPortCfgSupport=_OsPortCfgSupport_Object((1,3,6,1,4,1,6926,2,1,1,1),_OsPortCfgSupport_Type())
osPortCfgSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCfgSupport.setStatus(_A)
_OsPortCfgMaxNumberOfPort_Type=PortIndex
_OsPortCfgMaxNumberOfPort_Object=MibScalar
osPortCfgMaxNumberOfPort=_OsPortCfgMaxNumberOfPort_Object((1,3,6,1,4,1,6926,2,1,1,2),_OsPortCfgMaxNumberOfPort_Type())
osPortCfgMaxNumberOfPort.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCfgMaxNumberOfPort.setStatus(_A)
_OsPortCfgBaseTrunkPortIndex_Type=PortIndex
_OsPortCfgBaseTrunkPortIndex_Object=MibScalar
osPortCfgBaseTrunkPortIndex=_OsPortCfgBaseTrunkPortIndex_Object((1,3,6,1,4,1,6926,2,1,1,3),_OsPortCfgBaseTrunkPortIndex_Type())
osPortCfgBaseTrunkPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCfgBaseTrunkPortIndex.setStatus(_A)
class _OsPortCfgMaxNumberOfSl_Type(Unsigned32):defaultValue=8;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8190))
_OsPortCfgMaxNumberOfSl_Type.__name__=_F
_OsPortCfgMaxNumberOfSl_Object=MibScalar
osPortCfgMaxNumberOfSl=_OsPortCfgMaxNumberOfSl_Object((1,3,6,1,4,1,6926,2,1,1,4),_OsPortCfgMaxNumberOfSl_Type())
osPortCfgMaxNumberOfSl.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCfgMaxNumberOfSl.setStatus(_A)
class _OsPortCfgMaxTrunkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_OsPortCfgMaxTrunkId_Type.__name__=_E
_OsPortCfgMaxTrunkId_Object=MibScalar
osPortCfgMaxTrunkId=_OsPortCfgMaxTrunkId_Object((1,3,6,1,4,1,6926,2,1,1,5),_OsPortCfgMaxTrunkId_Type())
osPortCfgMaxTrunkId.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCfgMaxTrunkId.setStatus(_A)
_OsPortTrunkLastError_Type=LastError
_OsPortTrunkLastError_Object=MibScalar
osPortTrunkLastError=_OsPortTrunkLastError_Object((1,3,6,1,4,1,6926,2,1,1,12),_OsPortTrunkLastError_Type())
osPortTrunkLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortTrunkLastError.setStatus(_A)
class _OsPortCntEgressClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_Q,2)))
_OsPortCntEgressClearAll_Type.__name__=_E
_OsPortCntEgressClearAll_Object=MibScalar
osPortCntEgressClearAll=_OsPortCntEgressClearAll_Object((1,3,6,1,4,1,6926,2,1,1,13),_OsPortCntEgressClearAll_Type())
osPortCntEgressClearAll.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortCntEgressClearAll.setStatus(_A)
_OsPortTable_Object=MibTable
osPortTable=_OsPortTable_Object((1,3,6,1,4,1,6926,2,1,2))
if mibBuilder.loadTexts:osPortTable.setStatus(_A)
_OsPortEntry_Object=MibTableRow
osPortEntry=_OsPortEntry_Object((1,3,6,1,4,1,6926,2,1,2,1))
osPortEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:osPortEntry.setStatus(_A)
_OsPortIndex_Type=PortIndex
_OsPortIndex_Object=MibTableColumn
osPortIndex=_OsPortIndex_Object((1,3,6,1,4,1,6926,2,1,2,1,1),_OsPortIndex_Type())
osPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:osPortIndex.setStatus(_A)
class _OsPortDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_OsPortDescription_Type.__name__=_b
_OsPortDescription_Object=MibTableColumn
osPortDescription=_OsPortDescription_Object((1,3,6,1,4,1,6926,2,1,2,1,3),_OsPortDescription_Type())
osPortDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortDescription.setStatus(_A)
_OsPortLink_Type=TruthValue
_OsPortLink_Object=MibTableColumn
osPortLink=_OsPortLink_Object((1,3,6,1,4,1,6926,2,1,2,1,5),_OsPortLink_Type())
osPortLink.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortLink.setStatus(_A)
class _OsPortAdminSpeed_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,1),('auto',2),('s10',3),('s100',4),('s1000',5),('s10000',6),('s2500',7)))
_OsPortAdminSpeed_Type.__name__=_E
_OsPortAdminSpeed_Object=MibTableColumn
osPortAdminSpeed=_OsPortAdminSpeed_Object((1,3,6,1,4,1,6926,2,1,2,1,6),_OsPortAdminSpeed_Type())
osPortAdminSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortAdminSpeed.setStatus(_A)
_OsPortOperSpeed_Type=Gauge32
_OsPortOperSpeed_Object=MibTableColumn
osPortOperSpeed=_OsPortOperSpeed_Object((1,3,6,1,4,1,6926,2,1,2,1,7),_OsPortOperSpeed_Type())
osPortOperSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortOperSpeed.setStatus(_A)
class _OsPortDuplex_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_G,1),('full',3),('half',4)))
_OsPortDuplex_Type.__name__=_E
_OsPortDuplex_Object=MibTableColumn
osPortDuplex=_OsPortDuplex_Object((1,3,6,1,4,1,6926,2,1,2,1,9),_OsPortDuplex_Type())
osPortDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortDuplex.setStatus(_A)
class _OsPortAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('enable',2),('disableByMgmt',3)))
_OsPortAdminState_Type.__name__=_E
_OsPortAdminState_Object=MibTableColumn
osPortAdminState=_OsPortAdminState_Object((1,3,6,1,4,1,6926,2,1,2,1,10),_OsPortAdminState_Type())
osPortAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortAdminState.setStatus(_A)
class _OsPortOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*((_G,1),(_M,2),('disabledByMgmt',3),('disabledByReboot',4),('isolatedByLinkFlapGuard',5),('isolatedByLinkReflection',6),('isolatedByLinkProtection',7),('isolatedByStpLinkReflection',8),('isolatedByHotSwap',9),('isolatedByHa',10),('isolatedByStpPortLoop',11),('isolatedByStpOverRate',12),('isolatedByEthoamOverRate',13),('isolatedByEfmOverRate',14),('isolatedByDot1xOverRate',15),('isolatedByDot1agOverRate',16),('isolatedByLacpOverRate',17),('isolatedByAhOverRate',18),('isolatedByUdld',19),('isolatedByShdslLinkDown',20),('isolatedByL2TpOverRate',21),('isolatedByTdmLinkProtection',22),('isolatedByMplsLinkProtection',23),('isolatedByMacFlapLoopGuard',24)))
_OsPortOperState_Type.__name__=_E
_OsPortOperState_Object=MibTableColumn
osPortOperState=_OsPortOperState_Object((1,3,6,1,4,1,6926,2,1,2,1,11),_OsPortOperState_Type())
osPortOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortOperState.setStatus(_A)
class _OsPortBlockReason_Type(Bits):namedValues=NamedValues(*((_G,0),('reserve',1),(_M,2),('blockedByStp',3),('blockedByDot1X',4),('blockedByLacp',5),('blockedByAh',6),('blockedByErp',7)))
_OsPortBlockReason_Type.__name__=_O
_OsPortBlockReason_Object=MibTableColumn
osPortBlockReason=_OsPortBlockReason_Object((1,3,6,1,4,1,6926,2,1,2,1,12),_OsPortBlockReason_Type())
osPortBlockReason.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortBlockReason.setStatus(_A)
class _OsPortBuffersProfileIndex_Type(BuffersProfileIndex):defaultValue=1
_OsPortBuffersProfileIndex_Type.__name__=_c
_OsPortBuffersProfileIndex_Object=MibTableColumn
osPortBuffersProfileIndex=_OsPortBuffersProfileIndex_Object((1,3,6,1,4,1,6926,2,1,2,1,50),_OsPortBuffersProfileIndex_Type())
osPortBuffersProfileIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortBuffersProfileIndex.setStatus(_A)
_OsPortTrunkIndex_Type=PortIndexOrNone
_OsPortTrunkIndex_Object=MibTableColumn
osPortTrunkIndex=_OsPortTrunkIndex_Object((1,3,6,1,4,1,6926,2,1,2,1,60),_OsPortTrunkIndex_Type())
osPortTrunkIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortTrunkIndex.setStatus(_A)
class _OsPortLacpAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),(_R,2),('active',3),('passive',4),('rapid',5)))
_OsPortLacpAdminMode_Type.__name__=_E
_OsPortLacpAdminMode_Object=MibTableColumn
osPortLacpAdminMode=_OsPortLacpAdminMode_Object((1,3,6,1,4,1,6926,2,1,2,1,61),_OsPortLacpAdminMode_Type())
osPortLacpAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortLacpAdminMode.setStatus(_A)
class _OsPortLacpOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('nonLacp',2),('blocked',3),(_M,4)))
_OsPortLacpOperState_Type.__name__=_E
_OsPortLacpOperState_Object=MibTableColumn
osPortLacpOperState=_OsPortLacpOperState_Object((1,3,6,1,4,1,6926,2,1,2,1,62),_OsPortLacpOperState_Type())
osPortLacpOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortLacpOperState.setStatus(_A)
class _OsPortMtuSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,16000))
_OsPortMtuSize_Type.__name__=_F
_OsPortMtuSize_Object=MibTableColumn
osPortMtuSize=_OsPortMtuSize_Object((1,3,6,1,4,1,6926,2,1,2,1,66),_OsPortMtuSize_Type())
osPortMtuSize.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortMtuSize.setStatus(_A)
class _OsPortQosMarkingVpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('vpt',2),('dscp',3),('vptdscp',4),(_I,5)))
_OsPortQosMarkingVpt_Type.__name__=_E
_OsPortQosMarkingVpt_Object=MibTableColumn
osPortQosMarkingVpt=_OsPortQosMarkingVpt_Object((1,3,6,1,4,1,6926,2,1,2,1,70),_OsPortQosMarkingVpt_Type())
osPortQosMarkingVpt.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortQosMarkingVpt.setStatus(_A)
class _OsPortQosTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('l2',2),('l3',3),('l2l3',4),('port',5)))
_OsPortQosTrust_Type.__name__=_E
_OsPortQosTrust_Object=MibTableColumn
osPortQosTrust=_OsPortQosTrust_Object((1,3,6,1,4,1,6926,2,1,2,1,71),_OsPortQosTrust_Type())
osPortQosTrust.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortQosTrust.setStatus(_A)
class _OsPortRemarkingDei_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('preserveDei',1),('remarkDei',2)))
_OsPortRemarkingDei_Type.__name__=_E
_OsPortRemarkingDei_Object=MibTableColumn
osPortRemarkingDei=_OsPortRemarkingDei_Object((1,3,6,1,4,1,6926,2,1,2,1,72),_OsPortRemarkingDei_Type())
osPortRemarkingDei.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortRemarkingDei.setStatus(_A)
class _OsPortSl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8190))
_OsPortSl_Type.__name__=_F
_OsPortSl_Object=MibTableColumn
osPortSl=_OsPortSl_Object((1,3,6,1,4,1,6926,2,1,2,1,78),_OsPortSl_Type())
osPortSl.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortSl.setStatus(_A)
class _OsPortTagType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),('tagged',2),('untaggedSingleVlan',3),('untaggedMultiVlans',4),('hybrid',5),('qInQ',6)))
_OsPortTagType_Type.__name__=_E
_OsPortTagType_Object=MibTableColumn
osPortTagType=_OsPortTagType_Object((1,3,6,1,4,1,6926,2,1,2,1,80),_OsPortTagType_Type())
osPortTagType.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortTagType.setStatus(_A)
_OsPortTagDefaultTag_Type=VlanIdOrNone
_OsPortTagDefaultTag_Object=MibTableColumn
osPortTagDefaultTag=_OsPortTagDefaultTag_Object((1,3,6,1,4,1,6926,2,1,2,1,81),_OsPortTagDefaultTag_Type())
osPortTagDefaultTag.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortTagDefaultTag.setStatus(_A)
_OsPortL2CtrlDot1x_Type=L2CtrlProcess
_OsPortL2CtrlDot1x_Object=MibTableColumn
osPortL2CtrlDot1x=_OsPortL2CtrlDot1x_Object((1,3,6,1,4,1,6926,2,1,2,1,83),_OsPortL2CtrlDot1x_Type())
osPortL2CtrlDot1x.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortL2CtrlDot1x.setStatus(_A)
_OsPortL2CtrlLACP_Type=L2CtrlProcess
_OsPortL2CtrlLACP_Object=MibTableColumn
osPortL2CtrlLACP=_OsPortL2CtrlLACP_Object((1,3,6,1,4,1,6926,2,1,2,1,84),_OsPortL2CtrlLACP_Type())
osPortL2CtrlLACP.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortL2CtrlLACP.setStatus(_A)
_OsPortL2CtrlSTP_Type=L2CtrlProcess
_OsPortL2CtrlSTP_Object=MibTableColumn
osPortL2CtrlSTP=_OsPortL2CtrlSTP_Object((1,3,6,1,4,1,6926,2,1,2,1,85),_OsPortL2CtrlSTP_Type())
osPortL2CtrlSTP.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortL2CtrlSTP.setStatus(_A)
_OsPortL2CtrlGVRP_Type=L2CtrlProcess
_OsPortL2CtrlGVRP_Object=MibTableColumn
osPortL2CtrlGVRP=_OsPortL2CtrlGVRP_Object((1,3,6,1,4,1,6926,2,1,2,1,86),_OsPortL2CtrlGVRP_Type())
osPortL2CtrlGVRP.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortL2CtrlGVRP.setStatus(_A)
_OsPortL2CtrlPause_Type=L2CtrlProcess
_OsPortL2CtrlPause_Object=MibTableColumn
osPortL2CtrlPause=_OsPortL2CtrlPause_Object((1,3,6,1,4,1,6926,2,1,2,1,87),_OsPortL2CtrlPause_Type())
osPortL2CtrlPause.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortL2CtrlPause.setStatus(_A)
_OsPortL2CtrlLinkOAM_Type=L2CtrlProcess
_OsPortL2CtrlLinkOAM_Object=MibTableColumn
osPortL2CtrlLinkOAM=_OsPortL2CtrlLinkOAM_Object((1,3,6,1,4,1,6926,2,1,2,1,88),_OsPortL2CtrlLinkOAM_Type())
osPortL2CtrlLinkOAM.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortL2CtrlLinkOAM.setStatus(_A)
_OsPortL2CtrlELMI_Type=L2CtrlProcess
_OsPortL2CtrlELMI_Object=MibTableColumn
osPortL2CtrlELMI=_OsPortL2CtrlELMI_Object((1,3,6,1,4,1,6926,2,1,2,1,89),_OsPortL2CtrlELMI_Type())
osPortL2CtrlELMI.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortL2CtrlELMI.setStatus(_A)
_OsPortL2CtrlLLDP_Type=L2CtrlProcess
_OsPortL2CtrlLLDP_Object=MibTableColumn
osPortL2CtrlLLDP=_OsPortL2CtrlLLDP_Object((1,3,6,1,4,1,6926,2,1,2,1,90),_OsPortL2CtrlLLDP_Type())
osPortL2CtrlLLDP.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortL2CtrlLLDP.setStatus(_A)
_OsPortL2CtrlDTP_Type=L2CtrlProcess
_OsPortL2CtrlDTP_Object=MibTableColumn
osPortL2CtrlDTP=_OsPortL2CtrlDTP_Object((1,3,6,1,4,1,6926,2,1,2,1,91),_OsPortL2CtrlDTP_Type())
osPortL2CtrlDTP.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortL2CtrlDTP.setStatus(_A)
_OsPortL2CtrlPAGP_Type=L2CtrlProcess
_OsPortL2CtrlPAGP_Object=MibTableColumn
osPortL2CtrlPAGP=_OsPortL2CtrlPAGP_Object((1,3,6,1,4,1,6926,2,1,2,1,92),_OsPortL2CtrlPAGP_Type())
osPortL2CtrlPAGP.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortL2CtrlPAGP.setStatus(_A)
_OsPortL2CtrlVTP_Type=L2CtrlProcess
_OsPortL2CtrlVTP_Object=MibTableColumn
osPortL2CtrlVTP=_OsPortL2CtrlVTP_Object((1,3,6,1,4,1,6926,2,1,2,1,95),_OsPortL2CtrlVTP_Type())
osPortL2CtrlVTP.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortL2CtrlVTP.setStatus(_A)
_OsPortL2CtrlCDP_Type=L2CtrlProcess
_OsPortL2CtrlCDP_Object=MibTableColumn
osPortL2CtrlCDP=_OsPortL2CtrlCDP_Object((1,3,6,1,4,1,6926,2,1,2,1,96),_OsPortL2CtrlCDP_Type())
osPortL2CtrlCDP.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortL2CtrlCDP.setStatus(_A)
_OsPortL2CtrlPVST_Type=L2CtrlProcess
_OsPortL2CtrlPVST_Object=MibTableColumn
osPortL2CtrlPVST=_OsPortL2CtrlPVST_Object((1,3,6,1,4,1,6926,2,1,2,1,97),_OsPortL2CtrlPVST_Type())
osPortL2CtrlPVST.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortL2CtrlPVST.setStatus(_A)
class _OsPortAdminMediaSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_d,1),('sfp',2),(_e,3),(_f,4),('auto',5),('sgmii',6),(_g,7),(_h,8)))
_OsPortAdminMediaSelect_Type.__name__=_E
_OsPortAdminMediaSelect_Object=MibTableColumn
osPortAdminMediaSelect=_OsPortAdminMediaSelect_Object((1,3,6,1,4,1,6926,2,1,2,1,98),_OsPortAdminMediaSelect_Type())
osPortAdminMediaSelect.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortAdminMediaSelect.setStatus(_A)
class _OsPortOperMediaSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,7,8)));namedValues=NamedValues(*((_d,1),('sfp',2),(_e,3),(_f,4),('sgmii',6),(_g,7),(_h,8)))
_OsPortOperMediaSelect_Type.__name__=_E
_OsPortOperMediaSelect_Object=MibTableColumn
osPortOperMediaSelect=_OsPortOperMediaSelect_Object((1,3,6,1,4,1,6926,2,1,2,1,99),_OsPortOperMediaSelect_Type())
osPortOperMediaSelect.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortOperMediaSelect.setStatus(_A)
class _OsPortLanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_I,1),('eth10',2),('eth100',3),('eth10or100',4),('eth100B',5),('eth1000B',6),('atmLane',7),('eth100Grp',8),('eth10or100Grp',9),('fddi',10),('eth100or1000',11),('eth10hpna',12),('eth100or1000amp',13),('eth10or100overVDSL',14),('eth1000',15),('eth10or100or1000',16),('eth10000',17),('ethLAG',18),('eth1000or10000',19)))
_OsPortLanType_Type.__name__=_E
_OsPortLanType_Object=MibTableColumn
osPortLanType=_OsPortLanType_Object((1,3,6,1,4,1,6926,2,1,2,1,100),_OsPortLanType_Type())
osPortLanType.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortLanType.setStatus(_A)
class _OsPortIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37)));namedValues=NamedValues(*(('aui',1),('tp',2),('auiTp',3),('tpfd',4),('coax',5),('foMm',6),('foSm',7),(_I,8),('foSxM',9),('foLxM',10),('foLxS1',11),('foLxS2',12),('foLxS3',13),('foM',14),('foMX',15),('foS1',16),('foS2',17),('foS3',18),('foLxS4',19),('foLxS5',20),('foS4',21),('foS5',22),('foM10',23),('foGMX',24),('foS1A',25),('foPAL',26),('foXFP',27),('foSFPtp',28),('foSFP',29),('foSFPfoSFP100FXtp',30),('foSFP100FX',31),('foSFPfoSFP100FX',32),('foSFPdirect',33),('tpSHDSL',34),('portTrunk',35),('internalPort',36),('foSFPplus',37)))
_OsPortIfType_Type.__name__=_E
_OsPortIfType_Object=MibTableColumn
osPortIfType=_OsPortIfType_Object((1,3,6,1,4,1,6926,2,1,2,1,101),_OsPortIfType_Type())
osPortIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortIfType.setStatus(_A)
_OsPortLastError_Type=LastError
_OsPortLastError_Object=MibTableColumn
osPortLastError=_OsPortLastError_Object((1,3,6,1,4,1,6926,2,1,2,1,102),_OsPortLastError_Type())
osPortLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortLastError.setStatus(_A)
_OsPortShapeTable_Object=MibTable
osPortShapeTable=_OsPortShapeTable_Object((1,3,6,1,4,1,6926,2,1,3))
if mibBuilder.loadTexts:osPortShapeTable.setStatus(_A)
_OsPortShapeEntry_Object=MibTableRow
osPortShapeEntry=_OsPortShapeEntry_Object((1,3,6,1,4,1,6926,2,1,3,1))
osPortShapeEntry.setIndexNames((0,_B,_J),(0,_B,_S),(0,_B,_i))
if mibBuilder.loadTexts:osPortShapeEntry.setStatus(_A)
class _OsPortShapeDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('egressShaping',1),('ingressShaping',2)))
_OsPortShapeDir_Type.__name__=_E
_OsPortShapeDir_Object=MibTableColumn
osPortShapeDir=_OsPortShapeDir_Object((1,3,6,1,4,1,6926,2,1,3,1,3),_OsPortShapeDir_Type())
osPortShapeDir.setMaxAccess(_H)
if mibBuilder.loadTexts:osPortShapeDir.setStatus(_A)
class _OsPortShapeQId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8190),ValueRangeConstraint(8191,8191))
_OsPortShapeQId_Type.__name__=_F
_OsPortShapeQId_Object=MibTableColumn
osPortShapeQId=_OsPortShapeQId_Object((1,3,6,1,4,1,6926,2,1,3,1,4),_OsPortShapeQId_Type())
osPortShapeQId.setMaxAccess(_H)
if mibBuilder.loadTexts:osPortShapeQId.setStatus(_A)
_OsPortShapeRate_Type=Gauge32
_OsPortShapeRate_Object=MibTableColumn
osPortShapeRate=_OsPortShapeRate_Object((1,3,6,1,4,1,6926,2,1,3,1,6),_OsPortShapeRate_Type())
osPortShapeRate.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortShapeRate.setStatus(_A)
if mibBuilder.loadTexts:osPortShapeRate.setUnits(_T)
_OsPortShapeBurstSize_Type=Gauge32
_OsPortShapeBurstSize_Object=MibTableColumn
osPortShapeBurstSize=_OsPortShapeBurstSize_Object((1,3,6,1,4,1,6926,2,1,3,1,7),_OsPortShapeBurstSize_Type())
osPortShapeBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortShapeBurstSize.setStatus(_A)
if mibBuilder.loadTexts:osPortShapeBurstSize.setUnits(_U)
_OsPortShapeLastError_Type=LastError
_OsPortShapeLastError_Object=MibTableColumn
osPortShapeLastError=_OsPortShapeLastError_Object((1,3,6,1,4,1,6926,2,1,3,1,8),_OsPortShapeLastError_Type())
osPortShapeLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortShapeLastError.setStatus(_A)
_OsPortShapeLocked_Type=TruthValue
_OsPortShapeLocked_Object=MibTableColumn
osPortShapeLocked=_OsPortShapeLocked_Object((1,3,6,1,4,1,6926,2,1,3,1,15),_OsPortShapeLocked_Type())
osPortShapeLocked.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortShapeLocked.setStatus(_A)
_OsPortShapeAdminStatus_Type=PortEntryValidator
_OsPortShapeAdminStatus_Object=MibTableColumn
osPortShapeAdminStatus=_OsPortShapeAdminStatus_Object((1,3,6,1,4,1,6926,2,1,3,1,17),_OsPortShapeAdminStatus_Type())
osPortShapeAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortShapeAdminStatus.setStatus(_A)
_OsPortTrunkTable_Object=MibTable
osPortTrunkTable=_OsPortTrunkTable_Object((1,3,6,1,4,1,6926,2,1,4))
if mibBuilder.loadTexts:osPortTrunkTable.setStatus(_A)
_OsPortTrunkEntry_Object=MibTableRow
osPortTrunkEntry=_OsPortTrunkEntry_Object((1,3,6,1,4,1,6926,2,1,4,1))
osPortTrunkEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:osPortTrunkEntry.setStatus(_A)
class _OsPortTrunkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_OsPortTrunkId_Type.__name__=_E
_OsPortTrunkId_Object=MibTableColumn
osPortTrunkId=_OsPortTrunkId_Object((1,3,6,1,4,1,6926,2,1,4,1,3),_OsPortTrunkId_Type())
osPortTrunkId.setMaxAccess(_H)
if mibBuilder.loadTexts:osPortTrunkId.setStatus(_A)
_OsPortTrunkIndexId_Type=Integer32
_OsPortTrunkIndexId_Object=MibTableColumn
osPortTrunkIndexId=_OsPortTrunkIndexId_Object((1,3,6,1,4,1,6926,2,1,4,1,4),_OsPortTrunkIndexId_Type())
osPortTrunkIndexId.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortTrunkIndexId.setStatus(_A)
_OsPortTrunkMembers_Type=PortList
_OsPortTrunkMembers_Object=MibTableColumn
osPortTrunkMembers=_OsPortTrunkMembers_Object((1,3,6,1,4,1,6926,2,1,4,1,5),_OsPortTrunkMembers_Type())
osPortTrunkMembers.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortTrunkMembers.setStatus(_A)
_OsPortTrunkAdminStatus_Type=PortEntryValidator
_OsPortTrunkAdminStatus_Object=MibTableColumn
osPortTrunkAdminStatus=_OsPortTrunkAdminStatus_Object((1,3,6,1,4,1,6926,2,1,4,1,6),_OsPortTrunkAdminStatus_Type())
osPortTrunkAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortTrunkAdminStatus.setStatus(_A)
_OsPortTrunkNumOfMembers_Type=Integer32
_OsPortTrunkNumOfMembers_Object=MibTableColumn
osPortTrunkNumOfMembers=_OsPortTrunkNumOfMembers_Object((1,3,6,1,4,1,6926,2,1,4,1,7),_OsPortTrunkNumOfMembers_Type())
osPortTrunkNumOfMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortTrunkNumOfMembers.setStatus(_A)
_OsPortCntTable_Object=MibTable
osPortCntTable=_OsPortCntTable_Object((1,3,6,1,4,1,6926,2,1,5))
if mibBuilder.loadTexts:osPortCntTable.setStatus(_A)
_OsPortCntEntry_Object=MibTableRow
osPortCntEntry=_OsPortCntEntry_Object((1,3,6,1,4,1,6926,2,1,5,1))
if mibBuilder.loadTexts:osPortCntEntry.setStatus(_A)
class _OsPortCntClearAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_Q,2)))
_OsPortCntClearAll_Type.__name__=_E
_OsPortCntClearAll_Object=MibTableColumn
osPortCntClearAll=_OsPortCntClearAll_Object((1,3,6,1,4,1,6926,2,1,5,1,2),_OsPortCntClearAll_Type())
osPortCntClearAll.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortCntClearAll.setStatus(_A)
_OsPortCntRecvBytes_Type=Counter64
_OsPortCntRecvBytes_Object=MibTableColumn
osPortCntRecvBytes=_OsPortCntRecvBytes_Object((1,3,6,1,4,1,6926,2,1,5,1,3),_OsPortCntRecvBytes_Type())
osPortCntRecvBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvBytes.setStatus(_A)
_OsPortCntRecvPacks_Type=Counter64
_OsPortCntRecvPacks_Object=MibTableColumn
osPortCntRecvPacks=_OsPortCntRecvPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,4),_OsPortCntRecvPacks_Type())
osPortCntRecvPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvPacks.setStatus(_A)
_OsPortCntRecvUniPacks_Type=Counter64
_OsPortCntRecvUniPacks_Object=MibTableColumn
osPortCntRecvUniPacks=_OsPortCntRecvUniPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,5),_OsPortCntRecvUniPacks_Type())
osPortCntRecvUniPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvUniPacks.setStatus(_A)
_OsPortCntRecvBroadPacks_Type=Counter64
_OsPortCntRecvBroadPacks_Object=MibTableColumn
osPortCntRecvBroadPacks=_OsPortCntRecvBroadPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,6),_OsPortCntRecvBroadPacks_Type())
osPortCntRecvBroadPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvBroadPacks.setStatus(_A)
_OsPortCntRecvMultiPacks_Type=Counter64
_OsPortCntRecvMultiPacks_Object=MibTableColumn
osPortCntRecvMultiPacks=_OsPortCntRecvMultiPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,7),_OsPortCntRecvMultiPacks_Type())
osPortCntRecvMultiPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvMultiPacks.setStatus(_A)
_OsPortCntSentBytes_Type=Counter64
_OsPortCntSentBytes_Object=MibTableColumn
osPortCntSentBytes=_OsPortCntSentBytes_Object((1,3,6,1,4,1,6926,2,1,5,1,8),_OsPortCntSentBytes_Type())
osPortCntSentBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntSentBytes.setStatus(_A)
_OsPortCntSentPacks_Type=Counter64
_OsPortCntSentPacks_Object=MibTableColumn
osPortCntSentPacks=_OsPortCntSentPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,9),_OsPortCntSentPacks_Type())
osPortCntSentPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntSentPacks.setStatus(_A)
_OsPortCntSentUniPacks_Type=Counter64
_OsPortCntSentUniPacks_Object=MibTableColumn
osPortCntSentUniPacks=_OsPortCntSentUniPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,10),_OsPortCntSentUniPacks_Type())
osPortCntSentUniPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntSentUniPacks.setStatus(_A)
_OsPortCntSentBroadPacks_Type=Counter64
_OsPortCntSentBroadPacks_Object=MibTableColumn
osPortCntSentBroadPacks=_OsPortCntSentBroadPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,11),_OsPortCntSentBroadPacks_Type())
osPortCntSentBroadPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntSentBroadPacks.setStatus(_A)
_OsPortCntSentMultiPacks_Type=Counter64
_OsPortCntSentMultiPacks_Object=MibTableColumn
osPortCntSentMultiPacks=_OsPortCntSentMultiPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,12),_OsPortCntSentMultiPacks_Type())
osPortCntSentMultiPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntSentMultiPacks.setStatus(_A)
_OsPortCntRecvCRCorAlignmentErrs_Type=Counter64
_OsPortCntRecvCRCorAlignmentErrs_Object=MibTableColumn
osPortCntRecvCRCorAlignmentErrs=_OsPortCntRecvCRCorAlignmentErrs_Object((1,3,6,1,4,1,6926,2,1,5,1,13),_OsPortCntRecvCRCorAlignmentErrs_Type())
osPortCntRecvCRCorAlignmentErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvCRCorAlignmentErrs.setStatus(_A)
_OsPortCntRecvShortPacks_Type=Counter64
_OsPortCntRecvShortPacks_Object=MibTableColumn
osPortCntRecvShortPacks=_OsPortCntRecvShortPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,14),_OsPortCntRecvShortPacks_Type())
osPortCntRecvShortPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvShortPacks.setStatus(_A)
_OsPortCntRecvLongPacks_Type=Counter64
_OsPortCntRecvLongPacks_Object=MibTableColumn
osPortCntRecvLongPacks=_OsPortCntRecvLongPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,15),_OsPortCntRecvLongPacks_Type())
osPortCntRecvLongPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvLongPacks.setStatus(_A)
_OsPortCntRecvFragmentPacks_Type=Counter64
_OsPortCntRecvFragmentPacks_Object=MibTableColumn
osPortCntRecvFragmentPacks=_OsPortCntRecvFragmentPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,16),_OsPortCntRecvFragmentPacks_Type())
osPortCntRecvFragmentPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvFragmentPacks.setStatus(_A)
_OsPortCntRecvJabberPacks_Type=Counter64
_OsPortCntRecvJabberPacks_Object=MibTableColumn
osPortCntRecvJabberPacks=_OsPortCntRecvJabberPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,17),_OsPortCntRecvJabberPacks_Type())
osPortCntRecvJabberPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvJabberPacks.setStatus(_A)
_OsPortCntRecvAndSentCollisions_Type=Counter64
_OsPortCntRecvAndSentCollisions_Object=MibTableColumn
osPortCntRecvAndSentCollisions=_OsPortCntRecvAndSentCollisions_Object((1,3,6,1,4,1,6926,2,1,5,1,18),_OsPortCntRecvAndSentCollisions_Type())
osPortCntRecvAndSentCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvAndSentCollisions.setStatus(_A)
_OsPortCntRecvUpTo64octsPacks_Type=Counter64
_OsPortCntRecvUpTo64octsPacks_Object=MibTableColumn
osPortCntRecvUpTo64octsPacks=_OsPortCntRecvUpTo64octsPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,19),_OsPortCntRecvUpTo64octsPacks_Type())
osPortCntRecvUpTo64octsPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvUpTo64octsPacks.setStatus(_A)
_OsPortCntRecv65to127octsPacks_Type=Counter64
_OsPortCntRecv65to127octsPacks_Object=MibTableColumn
osPortCntRecv65to127octsPacks=_OsPortCntRecv65to127octsPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,20),_OsPortCntRecv65to127octsPacks_Type())
osPortCntRecv65to127octsPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecv65to127octsPacks.setStatus(_A)
_OsPortCntRecv128to255octsPacks_Type=Counter64
_OsPortCntRecv128to255octsPacks_Object=MibTableColumn
osPortCntRecv128to255octsPacks=_OsPortCntRecv128to255octsPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,22),_OsPortCntRecv128to255octsPacks_Type())
osPortCntRecv128to255octsPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecv128to255octsPacks.setStatus(_A)
_OsPortCntRecv256to511octsPacks_Type=Counter64
_OsPortCntRecv256to511octsPacks_Object=MibTableColumn
osPortCntRecv256to511octsPacks=_OsPortCntRecv256to511octsPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,23),_OsPortCntRecv256to511octsPacks_Type())
osPortCntRecv256to511octsPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecv256to511octsPacks.setStatus(_A)
_OsPortCntRecv512to1023octsPacks_Type=Counter64
_OsPortCntRecv512to1023octsPacks_Object=MibTableColumn
osPortCntRecv512to1023octsPacks=_OsPortCntRecv512to1023octsPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,24),_OsPortCntRecv512to1023octsPacks_Type())
osPortCntRecv512to1023octsPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecv512to1023octsPacks.setStatus(_A)
_OsPortCntRecvAbove1023octsPacks_Type=Counter64
_OsPortCntRecvAbove1023octsPacks_Object=MibTableColumn
osPortCntRecvAbove1023octsPacks=_OsPortCntRecvAbove1023octsPacks_Object((1,3,6,1,4,1,6926,2,1,5,1,25),_OsPortCntRecvAbove1023octsPacks_Type())
osPortCntRecvAbove1023octsPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvAbove1023octsPacks.setStatus(_A)
_OsPortCntLateCollisions_Type=Counter64
_OsPortCntLateCollisions_Object=MibTableColumn
osPortCntLateCollisions=_OsPortCntLateCollisions_Object((1,3,6,1,4,1,6926,2,1,5,1,41),_OsPortCntLateCollisions_Type())
osPortCntLateCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntLateCollisions.setStatus(_A)
_OsPortCntRecvBadBytes_Type=Counter64
_OsPortCntRecvBadBytes_Object=MibTableColumn
osPortCntRecvBadBytes=_OsPortCntRecvBadBytes_Object((1,3,6,1,4,1,6926,2,1,5,1,42),_OsPortCntRecvBadBytes_Type())
osPortCntRecvBadBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortCntRecvBadBytes.setStatus(_A)
class _OsPortCntEgressClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_Q,2)))
_OsPortCntEgressClear_Type.__name__=_E
_OsPortCntEgressClear_Object=MibTableColumn
osPortCntEgressClear=_OsPortCntEgressClear_Object((1,3,6,1,4,1,6926,2,1,5,1,43),_OsPortCntEgressClear_Type())
osPortCntEgressClear.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortCntEgressClear.setStatus(_A)
_OsPortShapeParametersTable_Object=MibTable
osPortShapeParametersTable=_OsPortShapeParametersTable_Object((1,3,6,1,4,1,6926,2,1,6))
if mibBuilder.loadTexts:osPortShapeParametersTable.setStatus(_A)
_OsPortShapeParametersEntry_Object=MibTableRow
osPortShapeParametersEntry=_OsPortShapeParametersEntry_Object((1,3,6,1,4,1,6926,2,1,6,1))
osPortShapeParametersEntry.setIndexNames((0,_B,_J),(0,_B,_S))
if mibBuilder.loadTexts:osPortShapeParametersEntry.setStatus(_A)
class _OsPortShapeCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notAvailable',1),('available',2)))
_OsPortShapeCapability_Type.__name__=_E
_OsPortShapeCapability_Object=MibTableColumn
osPortShapeCapability=_OsPortShapeCapability_Object((1,3,6,1,4,1,6926,2,1,6,1,1),_OsPortShapeCapability_Type())
osPortShapeCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortShapeCapability.setStatus(_A)
_OsPortShapeMinRate_Type=Gauge32
_OsPortShapeMinRate_Object=MibTableColumn
osPortShapeMinRate=_OsPortShapeMinRate_Object((1,3,6,1,4,1,6926,2,1,6,1,2),_OsPortShapeMinRate_Type())
osPortShapeMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortShapeMinRate.setStatus(_A)
if mibBuilder.loadTexts:osPortShapeMinRate.setUnits(_T)
_OsPortShapeMaxRate_Type=Gauge32
_OsPortShapeMaxRate_Object=MibTableColumn
osPortShapeMaxRate=_OsPortShapeMaxRate_Object((1,3,6,1,4,1,6926,2,1,6,1,3),_OsPortShapeMaxRate_Type())
osPortShapeMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortShapeMaxRate.setStatus(_A)
if mibBuilder.loadTexts:osPortShapeMaxRate.setUnits(_T)
_OsPortShapeMinBurstSize_Type=Gauge32
_OsPortShapeMinBurstSize_Object=MibTableColumn
osPortShapeMinBurstSize=_OsPortShapeMinBurstSize_Object((1,3,6,1,4,1,6926,2,1,6,1,4),_OsPortShapeMinBurstSize_Type())
osPortShapeMinBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortShapeMinBurstSize.setStatus(_A)
if mibBuilder.loadTexts:osPortShapeMinBurstSize.setUnits(_U)
_OsPortShapeMaxBurstSize_Type=Gauge32
_OsPortShapeMaxBurstSize_Object=MibTableColumn
osPortShapeMaxBurstSize=_OsPortShapeMaxBurstSize_Object((1,3,6,1,4,1,6926,2,1,6,1,5),_OsPortShapeMaxBurstSize_Type())
osPortShapeMaxBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortShapeMaxBurstSize.setStatus(_A)
if mibBuilder.loadTexts:osPortShapeMaxBurstSize.setUnits(_U)
_OsPortBuffersProfileTable_Object=MibTable
osPortBuffersProfileTable=_OsPortBuffersProfileTable_Object((1,3,6,1,4,1,6926,2,1,7))
if mibBuilder.loadTexts:osPortBuffersProfileTable.setStatus(_A)
_OsPortBuffersProfileEntry_Object=MibTableRow
osPortBuffersProfileEntry=_OsPortBuffersProfileEntry_Object((1,3,6,1,4,1,6926,2,1,7,1))
osPortBuffersProfileEntry.setIndexNames((0,_B,_j),(0,_B,_W))
if mibBuilder.loadTexts:osPortBuffersProfileEntry.setStatus(_A)
_OsBufferProfileIndex_Type=BuffersProfileIndex
_OsBufferProfileIndex_Object=MibTableColumn
osBufferProfileIndex=_OsBufferProfileIndex_Object((1,3,6,1,4,1,6926,2,1,7,1,1),_OsBufferProfileIndex_Type())
osBufferProfileIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:osBufferProfileIndex.setStatus(_A)
class _OsBufferProfileServiceLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OsBufferProfileServiceLevel_Type.__name__=_F
_OsBufferProfileServiceLevel_Object=MibTableColumn
osBufferProfileServiceLevel=_OsBufferProfileServiceLevel_Object((1,3,6,1,4,1,6926,2,1,7,1,2),_OsBufferProfileServiceLevel_Type())
osBufferProfileServiceLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:osBufferProfileServiceLevel.setStatus(_A)
class _OsBuffersProfileDescriptorsGreen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_OsBuffersProfileDescriptorsGreen_Type.__name__=_F
_OsBuffersProfileDescriptorsGreen_Object=MibTableColumn
osBuffersProfileDescriptorsGreen=_OsBuffersProfileDescriptorsGreen_Object((1,3,6,1,4,1,6926,2,1,7,1,3),_OsBuffersProfileDescriptorsGreen_Type())
osBuffersProfileDescriptorsGreen.setMaxAccess(_D)
if mibBuilder.loadTexts:osBuffersProfileDescriptorsGreen.setStatus(_A)
class _OsBuffersProfileDescriptorsYellow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_OsBuffersProfileDescriptorsYellow_Type.__name__=_F
_OsBuffersProfileDescriptorsYellow_Object=MibTableColumn
osBuffersProfileDescriptorsYellow=_OsBuffersProfileDescriptorsYellow_Object((1,3,6,1,4,1,6926,2,1,7,1,4),_OsBuffersProfileDescriptorsYellow_Type())
osBuffersProfileDescriptorsYellow.setMaxAccess(_D)
if mibBuilder.loadTexts:osBuffersProfileDescriptorsYellow.setStatus(_A)
class _OsBuffersProfileDescriptorsRed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_OsBuffersProfileDescriptorsRed_Type.__name__=_F
_OsBuffersProfileDescriptorsRed_Object=MibTableColumn
osBuffersProfileDescriptorsRed=_OsBuffersProfileDescriptorsRed_Object((1,3,6,1,4,1,6926,2,1,7,1,5),_OsBuffersProfileDescriptorsRed_Type())
osBuffersProfileDescriptorsRed.setMaxAccess(_D)
if mibBuilder.loadTexts:osBuffersProfileDescriptorsRed.setStatus(_A)
class _OsBuffersProfileBuffersGreen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_OsBuffersProfileBuffersGreen_Type.__name__=_F
_OsBuffersProfileBuffersGreen_Object=MibTableColumn
osBuffersProfileBuffersGreen=_OsBuffersProfileBuffersGreen_Object((1,3,6,1,4,1,6926,2,1,7,1,6),_OsBuffersProfileBuffersGreen_Type())
osBuffersProfileBuffersGreen.setMaxAccess(_D)
if mibBuilder.loadTexts:osBuffersProfileBuffersGreen.setStatus(_A)
class _OsBuffersProfileBuffersYellow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_OsBuffersProfileBuffersYellow_Type.__name__=_F
_OsBuffersProfileBuffersYellow_Object=MibTableColumn
osBuffersProfileBuffersYellow=_OsBuffersProfileBuffersYellow_Object((1,3,6,1,4,1,6926,2,1,7,1,7),_OsBuffersProfileBuffersYellow_Type())
osBuffersProfileBuffersYellow.setMaxAccess(_D)
if mibBuilder.loadTexts:osBuffersProfileBuffersYellow.setStatus(_A)
class _OsBuffersProfileBuffersRed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_OsBuffersProfileBuffersRed_Type.__name__=_F
_OsBuffersProfileBuffersRed_Object=MibTableColumn
osBuffersProfileBuffersRed=_OsBuffersProfileBuffersRed_Object((1,3,6,1,4,1,6926,2,1,7,1,8),_OsBuffersProfileBuffersRed_Type())
osBuffersProfileBuffersRed.setMaxAccess(_D)
if mibBuilder.loadTexts:osBuffersProfileBuffersRed.setStatus(_A)
class _OsBuffersProfileWredThresholdGreen_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_OsBuffersProfileWredThresholdGreen_Type.__name__=_F
_OsBuffersProfileWredThresholdGreen_Object=MibTableColumn
osBuffersProfileWredThresholdGreen=_OsBuffersProfileWredThresholdGreen_Object((1,3,6,1,4,1,6926,2,1,7,1,9),_OsBuffersProfileWredThresholdGreen_Type())
osBuffersProfileWredThresholdGreen.setMaxAccess(_D)
if mibBuilder.loadTexts:osBuffersProfileWredThresholdGreen.setStatus(_A)
if mibBuilder.loadTexts:osBuffersProfileWredThresholdGreen.setUnits(_X)
class _OsBuffersProfileWredThresholdYellow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_OsBuffersProfileWredThresholdYellow_Type.__name__=_F
_OsBuffersProfileWredThresholdYellow_Object=MibTableColumn
osBuffersProfileWredThresholdYellow=_OsBuffersProfileWredThresholdYellow_Object((1,3,6,1,4,1,6926,2,1,7,1,10),_OsBuffersProfileWredThresholdYellow_Type())
osBuffersProfileWredThresholdYellow.setMaxAccess(_D)
if mibBuilder.loadTexts:osBuffersProfileWredThresholdYellow.setStatus(_A)
if mibBuilder.loadTexts:osBuffersProfileWredThresholdYellow.setUnits(_X)
class _OsBuffersProfileWredThresholdRed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_OsBuffersProfileWredThresholdRed_Type.__name__=_F
_OsBuffersProfileWredThresholdRed_Object=MibTableColumn
osBuffersProfileWredThresholdRed=_OsBuffersProfileWredThresholdRed_Object((1,3,6,1,4,1,6926,2,1,7,1,11),_OsBuffersProfileWredThresholdRed_Type())
osBuffersProfileWredThresholdRed.setMaxAccess(_D)
if mibBuilder.loadTexts:osBuffersProfileWredThresholdRed.setStatus(_A)
if mibBuilder.loadTexts:osBuffersProfileWredThresholdRed.setUnits(_X)
_OsPortBuffersCfg_ObjectIdentity=ObjectIdentity
osPortBuffersCfg=_OsPortBuffersCfg_ObjectIdentity((1,3,6,1,4,1,6926,2,1,8))
class _OsPortBuffersShared_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_M,2)))
_OsPortBuffersShared_Type.__name__=_E
_OsPortBuffersShared_Object=MibScalar
osPortBuffersShared=_OsPortBuffersShared_Object((1,3,6,1,4,1,6926,2,1,8,1),_OsPortBuffersShared_Type())
osPortBuffersShared.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortBuffersShared.setStatus(_A)
class _OsPortBuffersWRED_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_M,2)))
_OsPortBuffersWRED_Type.__name__=_E
_OsPortBuffersWRED_Object=MibScalar
osPortBuffersWRED=_OsPortBuffersWRED_Object((1,3,6,1,4,1,6926,2,1,8,2),_OsPortBuffersWRED_Type())
osPortBuffersWRED.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortBuffersWRED.setStatus(_A)
_OsPortEthTypeTable_Object=MibTable
osPortEthTypeTable=_OsPortEthTypeTable_Object((1,3,6,1,4,1,6926,2,1,9))
if mibBuilder.loadTexts:osPortEthTypeTable.setStatus(_A)
_OsPortEthTypeEntry_Object=MibTableRow
osPortEthTypeEntry=_OsPortEthTypeEntry_Object((1,3,6,1,4,1,6926,2,1,9,1))
osPortEthTypeEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:osPortEthTypeEntry.setStatus(_A)
class _OsPortEthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('coreEth1',1),('coreEth2',2)))
_OsPortEthType_Type.__name__=_E
_OsPortEthType_Object=MibTableColumn
osPortEthType=_OsPortEthType_Object((1,3,6,1,4,1,6926,2,1,9,1,1),_OsPortEthType_Type())
osPortEthType.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortEthType.setStatus(_A)
_OsPortEgressCntTable_Object=MibTable
osPortEgressCntTable=_OsPortEgressCntTable_Object((1,3,6,1,4,1,6926,2,1,10))
if mibBuilder.loadTexts:osPortEgressCntTable.setStatus(_A)
_OsPortEgressCntEntry_Object=MibTableRow
osPortEgressCntEntry=_OsPortEgressCntEntry_Object((1,3,6,1,4,1,6926,2,1,10,1))
osPortEgressCntEntry.setIndexNames((0,_B,_J),(0,_B,_W),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:osPortEgressCntEntry.setStatus(_A)
class _OsPortEgressUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bytes',1),('packets',2)))
_OsPortEgressUnits_Type.__name__=_E
_OsPortEgressUnits_Object=MibTableColumn
osPortEgressUnits=_OsPortEgressUnits_Object((1,3,6,1,4,1,6926,2,1,10,1,3),_OsPortEgressUnits_Type())
osPortEgressUnits.setMaxAccess(_H)
if mibBuilder.loadTexts:osPortEgressUnits.setStatus(_A)
class _OsPortEgressValueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pass',1),('passOther',2),('passGreen',3),('drop',4),('dropOther',5),('dropGreen',6)))
_OsPortEgressValueType_Type.__name__=_E
_OsPortEgressValueType_Object=MibTableColumn
osPortEgressValueType=_OsPortEgressValueType_Object((1,3,6,1,4,1,6926,2,1,10,1,4),_OsPortEgressValueType_Type())
osPortEgressValueType.setMaxAccess(_H)
if mibBuilder.loadTexts:osPortEgressValueType.setStatus(_A)
_OsPortEgressCounter_Type=Counter64
_OsPortEgressCounter_Object=MibTableColumn
osPortEgressCounter=_OsPortEgressCounter_Object((1,3,6,1,4,1,6926,2,1,10,1,5),_OsPortEgressCounter_Type())
osPortEgressCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortEgressCounter.setStatus(_A)
_OsPortTrunkExtTable_Object=MibTable
osPortTrunkExtTable=_OsPortTrunkExtTable_Object((1,3,6,1,4,1,6926,2,1,14))
if mibBuilder.loadTexts:osPortTrunkExtTable.setStatus(_A)
_OsPortTrunkExtEntry_Object=MibTableRow
osPortTrunkExtEntry=_OsPortTrunkExtEntry_Object((1,3,6,1,4,1,6926,2,1,14,1))
osPortTrunkExtEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:osPortTrunkExtEntry.setStatus(_A)
class _OsPortTrunkMaxPortBundle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OsPortTrunkMaxPortBundle_Type.__name__=_E
_OsPortTrunkMaxPortBundle_Object=MibTableColumn
osPortTrunkMaxPortBundle=_OsPortTrunkMaxPortBundle_Object((1,3,6,1,4,1,6926,2,1,14,1,3),_OsPortTrunkMaxPortBundle_Type())
osPortTrunkMaxPortBundle.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortTrunkMaxPortBundle.setStatus(_A)
class _OsPortTrunkRevertive_Type(TruthValue):defaultValue=2
_OsPortTrunkRevertive_Type.__name__=_P
_OsPortTrunkRevertive_Object=MibTableColumn
osPortTrunkRevertive=_OsPortTrunkRevertive_Object((1,3,6,1,4,1,6926,2,1,14,1,4),_OsPortTrunkRevertive_Type())
osPortTrunkRevertive.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortTrunkRevertive.setStatus(_A)
class _OsPortTrunkFastSwitchover_Type(TruthValue):defaultValue=2
_OsPortTrunkFastSwitchover_Type.__name__=_P
_OsPortTrunkFastSwitchover_Object=MibTableColumn
osPortTrunkFastSwitchover=_OsPortTrunkFastSwitchover_Object((1,3,6,1,4,1,6926,2,1,14,1,5),_OsPortTrunkFastSwitchover_Type())
osPortTrunkFastSwitchover.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortTrunkFastSwitchover.setStatus(_A)
class _OsPortTrunkLowerThreshold_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OsPortTrunkLowerThreshold_Type.__name__=_E
_OsPortTrunkLowerThreshold_Object=MibTableColumn
osPortTrunkLowerThreshold=_OsPortTrunkLowerThreshold_Object((1,3,6,1,4,1,6926,2,1,14,1,6),_OsPortTrunkLowerThreshold_Type())
osPortTrunkLowerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortTrunkLowerThreshold.setStatus(_A)
class _OsPortTrunkHigherThreshold_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OsPortTrunkHigherThreshold_Type.__name__=_E
_OsPortTrunkHigherThreshold_Object=MibTableColumn
osPortTrunkHigherThreshold=_OsPortTrunkHigherThreshold_Object((1,3,6,1,4,1,6926,2,1,14,1,7),_OsPortTrunkHigherThreshold_Type())
osPortTrunkHigherThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortTrunkHigherThreshold.setStatus(_A)
_OsPortTrunkTearDown_Type=TruthValue
_OsPortTrunkTearDown_Object=MibTableColumn
osPortTrunkTearDown=_OsPortTrunkTearDown_Object((1,3,6,1,4,1,6926,2,1,14,1,17),_OsPortTrunkTearDown_Type())
osPortTrunkTearDown.setMaxAccess(_C)
if mibBuilder.loadTexts:osPortTrunkTearDown.setStatus(_A)
_OsPortFloodLimitTable_Object=MibTable
osPortFloodLimitTable=_OsPortFloodLimitTable_Object((1,3,6,1,4,1,6926,2,1,15))
if mibBuilder.loadTexts:osPortFloodLimitTable.setStatus(_A)
_OsPortFloodLimitEntry_Object=MibTableRow
osPortFloodLimitEntry=_OsPortFloodLimitEntry_Object((1,3,6,1,4,1,6926,2,1,15,1))
osPortFloodLimitEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:osPortFloodLimitEntry.setStatus(_A)
class _OsPortFloodLimitTypes_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('unknownUnicast',0),('multicast',1),('broadcast',2),('tcpSyn',3),('reserved',4),('deleteAll',5)))
_OsPortFloodLimitTypes_Type.__name__=_O
_OsPortFloodLimitTypes_Object=MibTableColumn
osPortFloodLimitTypes=_OsPortFloodLimitTypes_Object((1,3,6,1,4,1,6926,2,1,15,1,5),_OsPortFloodLimitTypes_Type())
osPortFloodLimitTypes.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortFloodLimitTypes.setStatus(_A)
class _OsPortFloodLimitRate_Type(Gauge32):defaultValue=0;subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_OsPortFloodLimitRate_Type.__name__=_a
_OsPortFloodLimitRate_Object=MibTableColumn
osPortFloodLimitRate=_OsPortFloodLimitRate_Object((1,3,6,1,4,1,6926,2,1,15,1,6),_OsPortFloodLimitRate_Type())
osPortFloodLimitRate.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortFloodLimitRate.setStatus(_A)
if mibBuilder.loadTexts:osPortFloodLimitRate.setUnits('Kbits/sec')
_OsPortGen_ObjectIdentity=ObjectIdentity
osPortGen=_OsPortGen_ObjectIdentity((1,3,6,1,4,1,6926,2,1,70))
_OsPortMflgMac_Type=MacAddress
_OsPortMflgMac_Object=MibScalar
osPortMflgMac=_OsPortMflgMac_Object((1,3,6,1,4,1,6926,2,1,70,3),_OsPortMflgMac_Type())
osPortMflgMac.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:osPortMflgMac.setStatus(_A)
_OsPortConformance_ObjectIdentity=ObjectIdentity
osPortConformance=_OsPortConformance_ObjectIdentity((1,3,6,1,4,1,6926,2,1,101))
_OsPortMIBCompliances_ObjectIdentity=ObjectIdentity
osPortMIBCompliances=_OsPortMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6926,2,1,101,1))
_OsPortMIBGroups_ObjectIdentity=ObjectIdentity
osPortMIBGroups=_OsPortMIBGroups_ObjectIdentity((1,3,6,1,4,1,6926,2,1,101,2))
_OsPortCoreEgressEth_ObjectIdentity=ObjectIdentity
osPortCoreEgressEth=_OsPortCoreEgressEth_ObjectIdentity((1,3,6,1,4,1,6926,2,1,102))
class _OsPortEthType1_Type(OctetString):defaultHexValue='8100';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_OsPortEthType1_Type.__name__=_N
_OsPortEthType1_Object=MibScalar
osPortEthType1=_OsPortEthType1_Object((1,3,6,1,4,1,6926,2,1,102,1),_OsPortEthType1_Type())
osPortEthType1.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortEthType1.setStatus(_A)
class _OsPortEthType2_Type(OctetString):defaultHexValue='8100';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_OsPortEthType2_Type.__name__=_N
_OsPortEthType2_Object=MibScalar
osPortEthType2=_OsPortEthType2_Object((1,3,6,1,4,1,6926,2,1,102,2),_OsPortEthType2_Type())
osPortEthType2.setMaxAccess(_D)
if mibBuilder.loadTexts:osPortEthType2.setStatus(_A)
osPortEntry.registerAugmentions((_B,_m))
osPortCntEntry.setIndexNames(*osPortEntry.getIndexNames())
osPortMandatoryGroup=ObjectGroup((1,3,6,1,4,1,6926,2,1,101,2,1))
osPortMandatoryGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_K),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_L),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,'osPortSl'),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_Y),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Z),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_BN),(_B,_BO),(_B,_BP),(_B,_BQ)))
if mibBuilder.loadTexts:osPortMandatoryGroup.setStatus(_A)
osPortMgmtEnabled=NotificationType((1,3,6,1,4,1,6926,2,1,0,1))
osPortMgmtEnabled.setObjects((_B,_K))
if mibBuilder.loadTexts:osPortMgmtEnabled.setStatus(_A)
osPortMgmtDisabled=NotificationType((1,3,6,1,4,1,6926,2,1,0,2))
osPortMgmtDisabled.setObjects((_B,_K))
if mibBuilder.loadTexts:osPortMgmtDisabled.setStatus(_A)
osPortSfpInserted=NotificationType((1,3,6,1,4,1,6926,2,1,0,3))
osPortSfpInserted.setObjects((_B,_K))
if mibBuilder.loadTexts:osPortSfpInserted.setStatus(_A)
osPortSfpRemoved=NotificationType((1,3,6,1,4,1,6926,2,1,0,4))
osPortSfpRemoved.setObjects((_B,_K))
if mibBuilder.loadTexts:osPortSfpRemoved.setStatus(_A)
osPortSfpI2cFailure=NotificationType((1,3,6,1,4,1,6926,2,1,0,5))
osPortSfpI2cFailure.setObjects((_B,_L))
if mibBuilder.loadTexts:osPortSfpI2cFailure.setStatus(_A)
osPortSfpI2cRecovery=NotificationType((1,3,6,1,4,1,6926,2,1,0,6))
osPortSfpI2cRecovery.setObjects((_B,_L))
if mibBuilder.loadTexts:osPortSfpI2cRecovery.setStatus(_A)
osPortSfpAutoDetectErr=NotificationType((1,3,6,1,4,1,6926,2,1,0,7))
osPortSfpAutoDetectErr.setObjects((_B,_Y))
if mibBuilder.loadTexts:osPortSfpAutoDetectErr.setStatus(_A)
osPortIsolation=NotificationType((1,3,6,1,4,1,6926,2,1,0,8))
osPortIsolation.setObjects(*((_B,_L),(_B,_Z)))
if mibBuilder.loadTexts:osPortIsolation.setStatus(_A)
osPortRecovery=NotificationType((1,3,6,1,4,1,6926,2,1,0,9))
osPortRecovery.setObjects((_B,_L))
if mibBuilder.loadTexts:osPortRecovery.setStatus(_A)
osPortNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6926,2,1,101,2,2))
osPortNotificationsGroup.setObjects(*((_B,_BR),(_B,_BS),(_B,_BT),(_B,_BU),(_B,_BV),(_B,_BW),(_B,_BX),(_B,_BY),(_B,_BZ)))
if mibBuilder.loadTexts:osPortNotificationsGroup.setStatus(_A)
osPortMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6926,2,1,101,1,1))
osPortMIBCompliance.setObjects(*((_B,_Ba),(_B,_Bb)))
if mibBuilder.loadTexts:osPortMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SupportValue':SupportValue,_c:BuffersProfileIndex,'L2CtrlProcess':L2CtrlProcess,'PortEntryValidator':PortEntryValidator,'LastError':LastError,'osPort':osPort,'osPortNotifications':osPortNotifications,_BR:osPortMgmtEnabled,_BS:osPortMgmtDisabled,_BT:osPortSfpInserted,_BU:osPortSfpRemoved,_BV:osPortSfpI2cFailure,_BW:osPortSfpI2cRecovery,_BX:osPortSfpAutoDetectErr,_BY:osPortIsolation,_BZ:osPortRecovery,'osPortCfg':osPortCfg,_n:osPortCfgSupport,_o:osPortCfgMaxNumberOfPort,_p:osPortCfgBaseTrunkPortIndex,_q:osPortCfgMaxNumberOfSl,_r:osPortCfgMaxTrunkId,_Aq:osPortTrunkLastError,_Ar:osPortCntEgressClearAll,'osPortTable':osPortTable,'osPortEntry':osPortEntry,_J:osPortIndex,_K:osPortDescription,_s:osPortLink,_t:osPortAdminSpeed,_u:osPortOperSpeed,_v:osPortDuplex,_w:osPortAdminState,_L:osPortOperState,_x:osPortBlockReason,_y:osPortBuffersProfileIndex,_z:osPortTrunkIndex,_A0:osPortLacpAdminMode,_A1:osPortLacpOperState,_A2:osPortMtuSize,_A3:osPortQosMarkingVpt,_A4:osPortQosTrust,_A5:osPortRemarkingDei,'osPortSl':osPortSl,_A6:osPortTagType,_A7:osPortTagDefaultTag,_A8:osPortL2CtrlDot1x,_A9:osPortL2CtrlLACP,_AA:osPortL2CtrlSTP,_AB:osPortL2CtrlGVRP,_AC:osPortL2CtrlPause,_AD:osPortL2CtrlLinkOAM,_AE:osPortL2CtrlELMI,_AF:osPortL2CtrlLLDP,_AG:osPortL2CtrlDTP,_AH:osPortL2CtrlPAGP,_AI:osPortL2CtrlVTP,_AJ:osPortL2CtrlCDP,_AK:osPortL2CtrlPVST,_AL:osPortAdminMediaSelect,_AM:osPortOperMediaSelect,_AN:osPortLanType,_AO:osPortIfType,_Y:osPortLastError,'osPortShapeTable':osPortShapeTable,'osPortShapeEntry':osPortShapeEntry,_S:osPortShapeDir,_i:osPortShapeQId,_AR:osPortShapeRate,_AS:osPortShapeBurstSize,_AT:osPortShapeLastError,_AU:osPortShapeLocked,_AV:osPortShapeAdminStatus,'osPortTrunkTable':osPortTrunkTable,'osPortTrunkEntry':osPortTrunkEntry,_V:osPortTrunkId,_Am:osPortTrunkIndexId,_An:osPortTrunkMembers,_Ao:osPortTrunkAdminStatus,_Ap:osPortTrunkNumOfMembers,'osPortCntTable':osPortCntTable,_m:osPortCntEntry,_Ay:osPortCntClearAll,_Az:osPortCntRecvBytes,_A_:osPortCntRecvPacks,_B0:osPortCntRecvUniPacks,_B1:osPortCntRecvBroadPacks,_B2:osPortCntRecvMultiPacks,_B3:osPortCntSentBytes,_B4:osPortCntSentPacks,_B5:osPortCntSentUniPacks,_B6:osPortCntSentBroadPacks,_B7:osPortCntSentMultiPacks,_B8:osPortCntRecvCRCorAlignmentErrs,_B9:osPortCntRecvShortPacks,_BA:osPortCntRecvLongPacks,_BB:osPortCntRecvFragmentPacks,_BC:osPortCntRecvJabberPacks,_BD:osPortCntRecvAndSentCollisions,_BE:osPortCntRecvUpTo64octsPacks,_BF:osPortCntRecv65to127octsPacks,_BG:osPortCntRecv128to255octsPacks,_BH:osPortCntRecv256to511octsPacks,_BI:osPortCntRecv512to1023octsPacks,_BJ:osPortCntRecvAbove1023octsPacks,_BK:osPortCntLateCollisions,_BL:osPortCntRecvBadBytes,_BO:osPortCntEgressClear,'osPortShapeParametersTable':osPortShapeParametersTable,'osPortShapeParametersEntry':osPortShapeParametersEntry,_AW:osPortShapeCapability,_AX:osPortShapeMinRate,_AY:osPortShapeMaxRate,_AZ:osPortShapeMinBurstSize,_Aa:osPortShapeMaxBurstSize,'osPortBuffersProfileTable':osPortBuffersProfileTable,'osPortBuffersProfileEntry':osPortBuffersProfileEntry,_j:osBufferProfileIndex,_W:osBufferProfileServiceLevel,_Ab:osBuffersProfileDescriptorsGreen,_Ac:osBuffersProfileDescriptorsYellow,_Ad:osBuffersProfileDescriptorsRed,_Ae:osBuffersProfileBuffersGreen,_Af:osBuffersProfileBuffersYellow,_Ag:osBuffersProfileBuffersRed,_Ah:osBuffersProfileWredThresholdGreen,_Ai:osBuffersProfileWredThresholdYellow,_Aj:osBuffersProfileWredThresholdRed,'osPortBuffersCfg':osPortBuffersCfg,_Ak:osPortBuffersShared,_Al:osPortBuffersWRED,'osPortEthTypeTable':osPortEthTypeTable,'osPortEthTypeEntry':osPortEthTypeEntry,_BM:osPortEthType,'osPortEgressCntTable':osPortEgressCntTable,'osPortEgressCntEntry':osPortEgressCntEntry,_k:osPortEgressUnits,_l:osPortEgressValueType,_BN:osPortEgressCounter,'osPortTrunkExtTable':osPortTrunkExtTable,'osPortTrunkExtEntry':osPortTrunkExtEntry,_As:osPortTrunkMaxPortBundle,_At:osPortTrunkRevertive,_Au:osPortTrunkFastSwitchover,_Av:osPortTrunkLowerThreshold,_Aw:osPortTrunkHigherThreshold,_Ax:osPortTrunkTearDown,'osPortFloodLimitTable':osPortFloodLimitTable,'osPortFloodLimitEntry':osPortFloodLimitEntry,_BP:osPortFloodLimitTypes,_BQ:osPortFloodLimitRate,'osPortGen':osPortGen,_Z:osPortMflgMac,'osPortConformance':osPortConformance,'osPortMIBCompliances':osPortMIBCompliances,'osPortMIBCompliance':osPortMIBCompliance,'osPortMIBGroups':osPortMIBGroups,_Ba:osPortMandatoryGroup,_Bb:osPortNotificationsGroup,'osPortCoreEgressEth':osPortCoreEgressEth,_AP:osPortEthType1,_AQ:osPortEthType2})