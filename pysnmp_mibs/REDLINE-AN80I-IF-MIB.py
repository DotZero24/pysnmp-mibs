_Ad='redlineAn80iIfNotificationGroup'
_Ac='redlineAn80iIfPmpGroup'
_Ab='redlineAn80iIfPtpGroup'
_Aa='an80iIfRegistrationOKTrap'
_AZ='an80iIfRegistrationFailedTrap'
_AY='an80iIfPmpConnULPacketsDisc'
_AX='an80iIfPmpConnULPacketsRx'
_AW='an80iIfPmpConnULPacketsTx'
_AV='an80iIfPmpConnDLPacketsDisc'
_AU='an80iIfPmpConnDLPacketsRx'
_AT='an80iIfPmpConnDLPacketsTx'
_AS='an80iIfPmpConnULQos'
_AR='an80iIfPmpConnDLQos'
_AQ='an80iIfPmpConnDefParenGroup'
_AP='an80iIfPmpConnDefParentLink'
_AO='an80iIfPmpConnDefPriority'
_AN='an80iIfPmpConnVlanId'
_AM='an80iIfPmpConnTaggingControl'
_AL='an80iIfPmpConnName'
_AK='an80iIfPmpGroupPacketDisc'
_AJ='an80iIfPmpGroupPacketsTx'
_AI='an80iIfPmpGroupQosLevel'
_AH='an80iIfPmpGroupSCEtherControl'
_AG='an80iIfPmpGroupDefPriority'
_AF='an80iIfPmpGroupVlanId'
_AE='an80iIfPmpGroupTaggingControl'
_AD='an80iIfPmpGroupName'
_AC='an80iIfPmpLinkULBlksDisc'
_AB='an80iIfPmpLinkULBlksRetr'
_AA='an80iIfPmpLinkULBlksTot'
_A9='an80iIfPmpLinkULLostFrm'
_A8='an80iIfPmpLinkULSinAdr'
_A7='an80iIfPmpLinkULRssi'
_A6='an80iIfPmpLinkCurrULUncBurstRate'
_A5='an80iIfPmpLinkDLBlksDisc'
_A4='an80iIfPmpLinkDLBlksRetr'
_A3='an80iIfPmpLinkDLBlksTot'
_A2='an80iIfPmpLinkDLLostFrm'
_A1='an80iIfPmpLinkDLSinAdr'
_A0='an80iIfPmpLinkCurrDLUncBurstRate'
_z='an80iIfPmpLinkUpTime'
_y='an80iIfRegPmpLinkConns'
_x='an80iIfPmpLinkStatusCode'
_w='an80iIfPmpLinkStatus'
_v='an80iIfPmpLinkDLBurstRate'
_u='an80iIfPmpLinkULBurstRate'
_t='an80iIfPmpLinkPeerMacAddress'
_s='an80iIfPmpLinkName'
_r='an80iIfLastRegistLinkId'
_q='an80iIfDenyMacAddress'
_p='an80iIfLinkName'
_o='an80iIfCalcLinkDst'
_n='an80iIfAvrSinAdr'
_m='an80iIfRssiMax'
_l='an80iIfRssiMean'
_k='an80iIfRssiMin'
_j='an80iIfTxPacketsDisc'
_i='an80iIfTxPacketsReTx'
_h='an80iIfTxPackets'
_g='an80iIfRxPacketsDisc'
_f='an80iIfRxPacketsReTx'
_e='an80iIfRxPackets'
_d='an80iIfPtpLinkStatus'
_c='an80iIfCurrUncodedBurstRate'
_b='an80iIfLinkLength'
_a='an80iIfLinkLenMode'
_Z='an80iIfPacketRetransControl'
_Y='an80iIfEncryptionKey'
_X='an80iIfUncodedBurstRate'
_W='an80iIfAdaptiveMod'
_V='an80iIfModReduction'
_U='an80iIfEncryptionControl'
_T='disable'
_S='enable'
_R='tagged'
_Q='passThrough'
_P='disabled'
_O='enabled'
_N='an80iIfLastRegistMacAddress'
_M='an80iIfLastMissedMacAddress'
_L='an80iIfPmpConnId'
_K='an80iIfPmpGroupId'
_J='not-accessible'
_I='an80iIfPmpLinkId'
_H='an80iIfPmpLinkLostCount'
_G='DisplayString'
_F='read-write'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='REDLINE-AN80I-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
redlineTransmission,=mibBuilder.importSymbols('REDLINE-MIB','redlineTransmission')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention')
redlineAn80iIfMib=ModuleIdentity((1,3,6,1,4,1,10728,2,10,2))
if mibBuilder.loadTexts:redlineAn80iIfMib.setRevisions(('2005-11-28 15:43',))
_RedlineAn80iIfTrapDefinitions_ObjectIdentity=ObjectIdentity
redlineAn80iIfTrapDefinitions=_RedlineAn80iIfTrapDefinitions_ObjectIdentity((1,3,6,1,4,1,10728,2,10,2,0))
_RedlineAn80iIfPtpObjects_ObjectIdentity=ObjectIdentity
redlineAn80iIfPtpObjects=_RedlineAn80iIfPtpObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,10,2,1))
_RedlineAn80iIfPtpLinkConfig_ObjectIdentity=ObjectIdentity
redlineAn80iIfPtpLinkConfig=_RedlineAn80iIfPtpLinkConfig_ObjectIdentity((1,3,6,1,4,1,10728,2,10,2,1,1))
class _An80iIfEncryptionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('off',1),('redline',2),('aes128',3),('aes192',4),('aes256',5)))
_An80iIfEncryptionControl_Type.__name__=_D
_An80iIfEncryptionControl_Object=MibScalar
an80iIfEncryptionControl=_An80iIfEncryptionControl_Object((1,3,6,1,4,1,10728,2,10,2,1,1,1),_An80iIfEncryptionControl_Type())
an80iIfEncryptionControl.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfEncryptionControl.setStatus(_A)
class _An80iIfModReduction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_An80iIfModReduction_Type.__name__=_D
_An80iIfModReduction_Object=MibScalar
an80iIfModReduction=_An80iIfModReduction_Object((1,3,6,1,4,1,10728,2,10,2,1,1,2),_An80iIfModReduction_Type())
an80iIfModReduction.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfModReduction.setStatus(_A)
class _An80iIfAdaptiveMod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_An80iIfAdaptiveMod_Type.__name__=_D
_An80iIfAdaptiveMod_Object=MibScalar
an80iIfAdaptiveMod=_An80iIfAdaptiveMod_Object((1,3,6,1,4,1,10728,2,10,2,1,1,3),_An80iIfAdaptiveMod_Type())
an80iIfAdaptiveMod.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfAdaptiveMod.setStatus(_A)
class _An80iIfUncodedBurstRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_An80iIfUncodedBurstRate_Type.__name__=_D
_An80iIfUncodedBurstRate_Object=MibScalar
an80iIfUncodedBurstRate=_An80iIfUncodedBurstRate_Object((1,3,6,1,4,1,10728,2,10,2,1,1,4),_An80iIfUncodedBurstRate_Type())
an80iIfUncodedBurstRate.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfUncodedBurstRate.setStatus(_A)
_An80iIfEncryptionKey_Type=OctetString
_An80iIfEncryptionKey_Object=MibScalar
an80iIfEncryptionKey=_An80iIfEncryptionKey_Object((1,3,6,1,4,1,10728,2,10,2,1,1,5),_An80iIfEncryptionKey_Type())
an80iIfEncryptionKey.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfEncryptionKey.setStatus(_A)
class _An80iIfPacketRetransControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_An80iIfPacketRetransControl_Type.__name__=_D
_An80iIfPacketRetransControl_Object=MibScalar
an80iIfPacketRetransControl=_An80iIfPacketRetransControl_Object((1,3,6,1,4,1,10728,2,10,2,1,1,6),_An80iIfPacketRetransControl_Type())
an80iIfPacketRetransControl.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfPacketRetransControl.setStatus(_A)
class _An80iIfLinkLenMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_An80iIfLinkLenMode_Type.__name__=_D
_An80iIfLinkLenMode_Object=MibScalar
an80iIfLinkLenMode=_An80iIfLinkLenMode_Object((1,3,6,1,4,1,10728,2,10,2,1,1,7),_An80iIfLinkLenMode_Type())
an80iIfLinkLenMode.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfLinkLenMode.setStatus(_A)
_An80iIfLinkLength_Type=Integer32
_An80iIfLinkLength_Object=MibScalar
an80iIfLinkLength=_An80iIfLinkLength_Object((1,3,6,1,4,1,10728,2,10,2,1,1,8),_An80iIfLinkLength_Type())
an80iIfLinkLength.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfLinkLength.setStatus(_A)
if mibBuilder.loadTexts:an80iIfLinkLength.setUnits('Km')
_An80iIfCalcLinkDst_Type=Integer32
_An80iIfCalcLinkDst_Object=MibScalar
an80iIfCalcLinkDst=_An80iIfCalcLinkDst_Object((1,3,6,1,4,1,10728,2,10,2,1,1,9),_An80iIfCalcLinkDst_Type())
an80iIfCalcLinkDst.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfCalcLinkDst.setStatus(_A)
if mibBuilder.loadTexts:an80iIfCalcLinkDst.setUnits('Km')
class _An80iIfLinkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_An80iIfLinkName_Type.__name__=_G
_An80iIfLinkName_Object=MibScalar
an80iIfLinkName=_An80iIfLinkName_Object((1,3,6,1,4,1,10728,2,10,2,1,1,10),_An80iIfLinkName_Type())
an80iIfLinkName.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfLinkName.setStatus(_A)
_RedlineAn80iIfPtpLinkStats_ObjectIdentity=ObjectIdentity
redlineAn80iIfPtpLinkStats=_RedlineAn80iIfPtpLinkStats_ObjectIdentity((1,3,6,1,4,1,10728,2,10,2,1,2))
_An80iIfCurrUncodedBurstRate_Type=Unsigned32
_An80iIfCurrUncodedBurstRate_Object=MibScalar
an80iIfCurrUncodedBurstRate=_An80iIfCurrUncodedBurstRate_Object((1,3,6,1,4,1,10728,2,10,2,1,2,1),_An80iIfCurrUncodedBurstRate_Type())
an80iIfCurrUncodedBurstRate.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfCurrUncodedBurstRate.setStatus(_A)
class _An80iIfPtpLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_An80iIfPtpLinkStatus_Type.__name__=_D
_An80iIfPtpLinkStatus_Object=MibScalar
an80iIfPtpLinkStatus=_An80iIfPtpLinkStatus_Object((1,3,6,1,4,1,10728,2,10,2,1,2,2),_An80iIfPtpLinkStatus_Type())
an80iIfPtpLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPtpLinkStatus.setStatus(_A)
_An80iIfRxPackets_Type=Counter64
_An80iIfRxPackets_Object=MibScalar
an80iIfRxPackets=_An80iIfRxPackets_Object((1,3,6,1,4,1,10728,2,10,2,1,2,3),_An80iIfRxPackets_Type())
an80iIfRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfRxPackets.setStatus(_A)
_An80iIfRxPacketsReTx_Type=Counter64
_An80iIfRxPacketsReTx_Object=MibScalar
an80iIfRxPacketsReTx=_An80iIfRxPacketsReTx_Object((1,3,6,1,4,1,10728,2,10,2,1,2,4),_An80iIfRxPacketsReTx_Type())
an80iIfRxPacketsReTx.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfRxPacketsReTx.setStatus(_A)
_An80iIfRxPacketsDisc_Type=Counter64
_An80iIfRxPacketsDisc_Object=MibScalar
an80iIfRxPacketsDisc=_An80iIfRxPacketsDisc_Object((1,3,6,1,4,1,10728,2,10,2,1,2,5),_An80iIfRxPacketsDisc_Type())
an80iIfRxPacketsDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfRxPacketsDisc.setStatus(_A)
_An80iIfTxPackets_Type=Counter64
_An80iIfTxPackets_Object=MibScalar
an80iIfTxPackets=_An80iIfTxPackets_Object((1,3,6,1,4,1,10728,2,10,2,1,2,6),_An80iIfTxPackets_Type())
an80iIfTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfTxPackets.setStatus(_A)
_An80iIfTxPacketsReTx_Type=Counter64
_An80iIfTxPacketsReTx_Object=MibScalar
an80iIfTxPacketsReTx=_An80iIfTxPacketsReTx_Object((1,3,6,1,4,1,10728,2,10,2,1,2,7),_An80iIfTxPacketsReTx_Type())
an80iIfTxPacketsReTx.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfTxPacketsReTx.setStatus(_A)
_An80iIfTxPacketsDisc_Type=Counter64
_An80iIfTxPacketsDisc_Object=MibScalar
an80iIfTxPacketsDisc=_An80iIfTxPacketsDisc_Object((1,3,6,1,4,1,10728,2,10,2,1,2,8),_An80iIfTxPacketsDisc_Type())
an80iIfTxPacketsDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfTxPacketsDisc.setStatus(_A)
_An80iIfRssiMin_Type=Integer32
_An80iIfRssiMin_Object=MibScalar
an80iIfRssiMin=_An80iIfRssiMin_Object((1,3,6,1,4,1,10728,2,10,2,1,2,9),_An80iIfRssiMin_Type())
an80iIfRssiMin.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfRssiMin.setStatus(_A)
_An80iIfRssiMean_Type=Integer32
_An80iIfRssiMean_Object=MibScalar
an80iIfRssiMean=_An80iIfRssiMean_Object((1,3,6,1,4,1,10728,2,10,2,1,2,10),_An80iIfRssiMean_Type())
an80iIfRssiMean.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfRssiMean.setStatus(_A)
_An80iIfRssiMax_Type=Integer32
_An80iIfRssiMax_Object=MibScalar
an80iIfRssiMax=_An80iIfRssiMax_Object((1,3,6,1,4,1,10728,2,10,2,1,2,11),_An80iIfRssiMax_Type())
an80iIfRssiMax.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfRssiMax.setStatus(_A)
_An80iIfAvrSinAdr_Type=Integer32
_An80iIfAvrSinAdr_Object=MibScalar
an80iIfAvrSinAdr=_An80iIfAvrSinAdr_Object((1,3,6,1,4,1,10728,2,10,2,1,2,12),_An80iIfAvrSinAdr_Type())
an80iIfAvrSinAdr.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfAvrSinAdr.setStatus(_A)
_RedlineAn80iIfPmpObjects_ObjectIdentity=ObjectIdentity
redlineAn80iIfPmpObjects=_RedlineAn80iIfPmpObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,10,2,2))
_RedlineAn80iIfPmpSsObjects_ObjectIdentity=ObjectIdentity
redlineAn80iIfPmpSsObjects=_RedlineAn80iIfPmpSsObjects_ObjectIdentity((1,3,6,1,4,1,10728,2,10,2,2,1))
_An80iIfLastMissedMacAddress_Type=MacAddress
_An80iIfLastMissedMacAddress_Object=MibScalar
an80iIfLastMissedMacAddress=_An80iIfLastMissedMacAddress_Object((1,3,6,1,4,1,10728,2,10,2,2,1,1),_An80iIfLastMissedMacAddress_Type())
an80iIfLastMissedMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfLastMissedMacAddress.setStatus(_A)
_An80iIfLastRegistMacAddress_Type=MacAddress
_An80iIfLastRegistMacAddress_Object=MibScalar
an80iIfLastRegistMacAddress=_An80iIfLastRegistMacAddress_Object((1,3,6,1,4,1,10728,2,10,2,2,1,2),_An80iIfLastRegistMacAddress_Type())
an80iIfLastRegistMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfLastRegistMacAddress.setStatus(_A)
_An80iIfDenyMacAddress_Type=MacAddress
_An80iIfDenyMacAddress_Object=MibScalar
an80iIfDenyMacAddress=_An80iIfDenyMacAddress_Object((1,3,6,1,4,1,10728,2,10,2,2,1,3),_An80iIfDenyMacAddress_Type())
an80iIfDenyMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:an80iIfDenyMacAddress.setStatus(_A)
class _An80iIfLastRegistLinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_An80iIfLastRegistLinkId_Type.__name__=_D
_An80iIfLastRegistLinkId_Object=MibScalar
an80iIfLastRegistLinkId=_An80iIfLastRegistLinkId_Object((1,3,6,1,4,1,10728,2,10,2,2,1,4),_An80iIfLastRegistLinkId_Type())
an80iIfLastRegistLinkId.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfLastRegistLinkId.setStatus(_A)
_An80iIfPmpLinkConfigTable_Object=MibTable
an80iIfPmpLinkConfigTable=_An80iIfPmpLinkConfigTable_Object((1,3,6,1,4,1,10728,2,10,2,2,2))
if mibBuilder.loadTexts:an80iIfPmpLinkConfigTable.setStatus(_A)
_An80iIfPmpLinkConfigEntry_Object=MibTableRow
an80iIfPmpLinkConfigEntry=_An80iIfPmpLinkConfigEntry_Object((1,3,6,1,4,1,10728,2,10,2,2,2,1))
an80iIfPmpLinkConfigEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:an80iIfPmpLinkConfigEntry.setStatus(_A)
class _An80iIfPmpLinkId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1023))
_An80iIfPmpLinkId_Type.__name__=_D
_An80iIfPmpLinkId_Object=MibTableColumn
an80iIfPmpLinkId=_An80iIfPmpLinkId_Object((1,3,6,1,4,1,10728,2,10,2,2,2,1,1),_An80iIfPmpLinkId_Type())
an80iIfPmpLinkId.setMaxAccess(_J)
if mibBuilder.loadTexts:an80iIfPmpLinkId.setStatus(_A)
class _An80iIfPmpLinkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_An80iIfPmpLinkName_Type.__name__=_G
_An80iIfPmpLinkName_Object=MibTableColumn
an80iIfPmpLinkName=_An80iIfPmpLinkName_Object((1,3,6,1,4,1,10728,2,10,2,2,2,1,2),_An80iIfPmpLinkName_Type())
an80iIfPmpLinkName.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpLinkName.setStatus(_A)
_An80iIfPmpLinkPeerMacAddress_Type=MacAddress
_An80iIfPmpLinkPeerMacAddress_Object=MibTableColumn
an80iIfPmpLinkPeerMacAddress=_An80iIfPmpLinkPeerMacAddress_Object((1,3,6,1,4,1,10728,2,10,2,2,2,1,3),_An80iIfPmpLinkPeerMacAddress_Type())
an80iIfPmpLinkPeerMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpLinkPeerMacAddress.setStatus(_A)
_An80iIfPmpLinkULBurstRate_Type=Unsigned32
_An80iIfPmpLinkULBurstRate_Object=MibTableColumn
an80iIfPmpLinkULBurstRate=_An80iIfPmpLinkULBurstRate_Object((1,3,6,1,4,1,10728,2,10,2,2,2,1,4),_An80iIfPmpLinkULBurstRate_Type())
an80iIfPmpLinkULBurstRate.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpLinkULBurstRate.setStatus(_A)
_An80iIfPmpLinkDLBurstRate_Type=Unsigned32
_An80iIfPmpLinkDLBurstRate_Object=MibTableColumn
an80iIfPmpLinkDLBurstRate=_An80iIfPmpLinkDLBurstRate_Object((1,3,6,1,4,1,10728,2,10,2,2,2,1,5),_An80iIfPmpLinkDLBurstRate_Type())
an80iIfPmpLinkDLBurstRate.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpLinkDLBurstRate.setStatus(_A)
_An80iIfPmpLinkConfigStatus_Type=RowStatus
_An80iIfPmpLinkConfigStatus_Object=MibTableColumn
an80iIfPmpLinkConfigStatus=_An80iIfPmpLinkConfigStatus_Object((1,3,6,1,4,1,10728,2,10,2,2,2,1,6),_An80iIfPmpLinkConfigStatus_Type())
an80iIfPmpLinkConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpLinkConfigStatus.setStatus(_A)
_An80iIfPmpLinkStatsTable_Object=MibTable
an80iIfPmpLinkStatsTable=_An80iIfPmpLinkStatsTable_Object((1,3,6,1,4,1,10728,2,10,2,2,3))
if mibBuilder.loadTexts:an80iIfPmpLinkStatsTable.setStatus(_A)
_An80iIfPmpLinkStatsEntry_Object=MibTableRow
an80iIfPmpLinkStatsEntry=_An80iIfPmpLinkStatsEntry_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1))
an80iIfPmpLinkStatsEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:an80iIfPmpLinkStatsEntry.setStatus(_A)
class _An80iIfPmpLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_An80iIfPmpLinkStatus_Type.__name__=_D
_An80iIfPmpLinkStatus_Object=MibTableColumn
an80iIfPmpLinkStatus=_An80iIfPmpLinkStatus_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,1),_An80iIfPmpLinkStatus_Type())
an80iIfPmpLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkStatus.setStatus(_A)
_An80iIfPmpLinkStatusCode_Type=Integer32
_An80iIfPmpLinkStatusCode_Object=MibTableColumn
an80iIfPmpLinkStatusCode=_An80iIfPmpLinkStatusCode_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,2),_An80iIfPmpLinkStatusCode_Type())
an80iIfPmpLinkStatusCode.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkStatusCode.setStatus(_A)
_An80iIfRegPmpLinkConns_Type=Integer32
_An80iIfRegPmpLinkConns_Object=MibTableColumn
an80iIfRegPmpLinkConns=_An80iIfRegPmpLinkConns_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,3),_An80iIfRegPmpLinkConns_Type())
an80iIfRegPmpLinkConns.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfRegPmpLinkConns.setStatus(_A)
_An80iIfPmpLinkUpTime_Type=TimeTicks
_An80iIfPmpLinkUpTime_Object=MibTableColumn
an80iIfPmpLinkUpTime=_An80iIfPmpLinkUpTime_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,4),_An80iIfPmpLinkUpTime_Type())
an80iIfPmpLinkUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkUpTime.setStatus(_A)
_An80iIfPmpLinkLostCount_Type=Counter32
_An80iIfPmpLinkLostCount_Object=MibTableColumn
an80iIfPmpLinkLostCount=_An80iIfPmpLinkLostCount_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,5),_An80iIfPmpLinkLostCount_Type())
an80iIfPmpLinkLostCount.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkLostCount.setStatus(_A)
_An80iIfPmpLinkCurrDLUncBurstRate_Type=Unsigned32
_An80iIfPmpLinkCurrDLUncBurstRate_Object=MibTableColumn
an80iIfPmpLinkCurrDLUncBurstRate=_An80iIfPmpLinkCurrDLUncBurstRate_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,6),_An80iIfPmpLinkCurrDLUncBurstRate_Type())
an80iIfPmpLinkCurrDLUncBurstRate.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkCurrDLUncBurstRate.setStatus(_A)
_An80iIfPmpLinkDLRssi_Type=Integer32
_An80iIfPmpLinkDLRssi_Object=MibTableColumn
an80iIfPmpLinkDLRssi=_An80iIfPmpLinkDLRssi_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,7),_An80iIfPmpLinkDLRssi_Type())
an80iIfPmpLinkDLRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkDLRssi.setStatus(_A)
_An80iIfPmpLinkDLSinAdr_Type=Integer32
_An80iIfPmpLinkDLSinAdr_Object=MibTableColumn
an80iIfPmpLinkDLSinAdr=_An80iIfPmpLinkDLSinAdr_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,8),_An80iIfPmpLinkDLSinAdr_Type())
an80iIfPmpLinkDLSinAdr.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkDLSinAdr.setStatus(_A)
_An80iIfPmpLinkDLLostFrm_Type=Counter64
_An80iIfPmpLinkDLLostFrm_Object=MibTableColumn
an80iIfPmpLinkDLLostFrm=_An80iIfPmpLinkDLLostFrm_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,9),_An80iIfPmpLinkDLLostFrm_Type())
an80iIfPmpLinkDLLostFrm.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkDLLostFrm.setStatus(_A)
_An80iIfPmpLinkDLBlksTot_Type=Counter64
_An80iIfPmpLinkDLBlksTot_Object=MibTableColumn
an80iIfPmpLinkDLBlksTot=_An80iIfPmpLinkDLBlksTot_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,10),_An80iIfPmpLinkDLBlksTot_Type())
an80iIfPmpLinkDLBlksTot.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkDLBlksTot.setStatus(_A)
_An80iIfPmpLinkDLBlksRetr_Type=Counter64
_An80iIfPmpLinkDLBlksRetr_Object=MibTableColumn
an80iIfPmpLinkDLBlksRetr=_An80iIfPmpLinkDLBlksRetr_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,11),_An80iIfPmpLinkDLBlksRetr_Type())
an80iIfPmpLinkDLBlksRetr.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkDLBlksRetr.setStatus(_A)
_An80iIfPmpLinkDLBlksDisc_Type=Counter64
_An80iIfPmpLinkDLBlksDisc_Object=MibTableColumn
an80iIfPmpLinkDLBlksDisc=_An80iIfPmpLinkDLBlksDisc_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,12),_An80iIfPmpLinkDLBlksDisc_Type())
an80iIfPmpLinkDLBlksDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkDLBlksDisc.setStatus(_A)
_An80iIfPmpLinkCurrULUncBurstRate_Type=Unsigned32
_An80iIfPmpLinkCurrULUncBurstRate_Object=MibTableColumn
an80iIfPmpLinkCurrULUncBurstRate=_An80iIfPmpLinkCurrULUncBurstRate_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,13),_An80iIfPmpLinkCurrULUncBurstRate_Type())
an80iIfPmpLinkCurrULUncBurstRate.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkCurrULUncBurstRate.setStatus(_A)
if mibBuilder.loadTexts:an80iIfPmpLinkCurrULUncBurstRate.setUnits('Mb/s')
_An80iIfPmpLinkULRssi_Type=Integer32
_An80iIfPmpLinkULRssi_Object=MibTableColumn
an80iIfPmpLinkULRssi=_An80iIfPmpLinkULRssi_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,14),_An80iIfPmpLinkULRssi_Type())
an80iIfPmpLinkULRssi.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkULRssi.setStatus(_A)
_An80iIfPmpLinkULSinAdr_Type=Integer32
_An80iIfPmpLinkULSinAdr_Object=MibTableColumn
an80iIfPmpLinkULSinAdr=_An80iIfPmpLinkULSinAdr_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,15),_An80iIfPmpLinkULSinAdr_Type())
an80iIfPmpLinkULSinAdr.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkULSinAdr.setStatus(_A)
_An80iIfPmpLinkULLostFrm_Type=Counter64
_An80iIfPmpLinkULLostFrm_Object=MibTableColumn
an80iIfPmpLinkULLostFrm=_An80iIfPmpLinkULLostFrm_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,16),_An80iIfPmpLinkULLostFrm_Type())
an80iIfPmpLinkULLostFrm.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkULLostFrm.setStatus(_A)
_An80iIfPmpLinkULBlksTot_Type=Counter64
_An80iIfPmpLinkULBlksTot_Object=MibTableColumn
an80iIfPmpLinkULBlksTot=_An80iIfPmpLinkULBlksTot_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,17),_An80iIfPmpLinkULBlksTot_Type())
an80iIfPmpLinkULBlksTot.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkULBlksTot.setStatus(_A)
_An80iIfPmpLinkULBlksRetr_Type=Counter64
_An80iIfPmpLinkULBlksRetr_Object=MibTableColumn
an80iIfPmpLinkULBlksRetr=_An80iIfPmpLinkULBlksRetr_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,18),_An80iIfPmpLinkULBlksRetr_Type())
an80iIfPmpLinkULBlksRetr.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkULBlksRetr.setStatus(_A)
_An80iIfPmpLinkULBlksDisc_Type=Counter64
_An80iIfPmpLinkULBlksDisc_Object=MibTableColumn
an80iIfPmpLinkULBlksDisc=_An80iIfPmpLinkULBlksDisc_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,19),_An80iIfPmpLinkULBlksDisc_Type())
an80iIfPmpLinkULBlksDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkULBlksDisc.setStatus(_A)
_An80iIfPmpLinkStatsStatus_Type=RowStatus
_An80iIfPmpLinkStatsStatus_Object=MibTableColumn
an80iIfPmpLinkStatsStatus=_An80iIfPmpLinkStatsStatus_Object((1,3,6,1,4,1,10728,2,10,2,2,3,1,20),_An80iIfPmpLinkStatsStatus_Type())
an80iIfPmpLinkStatsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpLinkStatsStatus.setStatus(_A)
_An80iIfPmpGroupConfigTable_Object=MibTable
an80iIfPmpGroupConfigTable=_An80iIfPmpGroupConfigTable_Object((1,3,6,1,4,1,10728,2,10,2,2,4))
if mibBuilder.loadTexts:an80iIfPmpGroupConfigTable.setStatus(_A)
_An80iIfPmpGroupConfigEntry_Object=MibTableRow
an80iIfPmpGroupConfigEntry=_An80iIfPmpGroupConfigEntry_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1))
an80iIfPmpGroupConfigEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:an80iIfPmpGroupConfigEntry.setStatus(_A)
class _An80iIfPmpGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1023))
_An80iIfPmpGroupId_Type.__name__=_D
_An80iIfPmpGroupId_Object=MibTableColumn
an80iIfPmpGroupId=_An80iIfPmpGroupId_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,1),_An80iIfPmpGroupId_Type())
an80iIfPmpGroupId.setMaxAccess(_J)
if mibBuilder.loadTexts:an80iIfPmpGroupId.setStatus(_A)
class _An80iIfPmpGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_An80iIfPmpGroupName_Type.__name__=_G
_An80iIfPmpGroupName_Object=MibTableColumn
an80iIfPmpGroupName=_An80iIfPmpGroupName_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,2),_An80iIfPmpGroupName_Type())
an80iIfPmpGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpGroupName.setStatus(_A)
class _An80iIfPmpGroupTaggingControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_An80iIfPmpGroupTaggingControl_Type.__name__=_D
_An80iIfPmpGroupTaggingControl_Object=MibTableColumn
an80iIfPmpGroupTaggingControl=_An80iIfPmpGroupTaggingControl_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,3),_An80iIfPmpGroupTaggingControl_Type())
an80iIfPmpGroupTaggingControl.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpGroupTaggingControl.setStatus(_A)
class _An80iIfPmpGroupVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_An80iIfPmpGroupVlanId_Type.__name__=_D
_An80iIfPmpGroupVlanId_Object=MibTableColumn
an80iIfPmpGroupVlanId=_An80iIfPmpGroupVlanId_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,4),_An80iIfPmpGroupVlanId_Type())
an80iIfPmpGroupVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpGroupVlanId.setStatus(_A)
class _An80iIfPmpGroupDefPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_An80iIfPmpGroupDefPriority_Type.__name__=_D
_An80iIfPmpGroupDefPriority_Object=MibTableColumn
an80iIfPmpGroupDefPriority=_An80iIfPmpGroupDefPriority_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,5),_An80iIfPmpGroupDefPriority_Type())
an80iIfPmpGroupDefPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpGroupDefPriority.setStatus(_A)
class _An80iIfPmpGroupSCEtherControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_An80iIfPmpGroupSCEtherControl_Type.__name__=_D
_An80iIfPmpGroupSCEtherControl_Object=MibTableColumn
an80iIfPmpGroupSCEtherControl=_An80iIfPmpGroupSCEtherControl_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,6),_An80iIfPmpGroupSCEtherControl_Type())
an80iIfPmpGroupSCEtherControl.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpGroupSCEtherControl.setStatus(_A)
class _An80iIfPmpGroupQosLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,53))
_An80iIfPmpGroupQosLevel_Type.__name__=_D
_An80iIfPmpGroupQosLevel_Object=MibTableColumn
an80iIfPmpGroupQosLevel=_An80iIfPmpGroupQosLevel_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,7),_An80iIfPmpGroupQosLevel_Type())
an80iIfPmpGroupQosLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpGroupQosLevel.setStatus(_A)
_An80iIfPmpGroupConfigStatus_Type=RowStatus
_An80iIfPmpGroupConfigStatus_Object=MibTableColumn
an80iIfPmpGroupConfigStatus=_An80iIfPmpGroupConfigStatus_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,8),_An80iIfPmpGroupConfigStatus_Type())
an80iIfPmpGroupConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpGroupConfigStatus.setStatus(_A)
class _An80iIfPmpGroupRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_An80iIfPmpGroupRate_Type.__name__=_D
_An80iIfPmpGroupRate_Object=MibTableColumn
an80iIfPmpGroupRate=_An80iIfPmpGroupRate_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,9),_An80iIfPmpGroupRate_Type())
an80iIfPmpGroupRate.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpGroupRate.setStatus(_A)
class _An80iIfPmpGroupSStoSSMulticast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_An80iIfPmpGroupSStoSSMulticast_Type.__name__=_D
_An80iIfPmpGroupSStoSSMulticast_Object=MibTableColumn
an80iIfPmpGroupSStoSSMulticast=_An80iIfPmpGroupSStoSSMulticast_Object((1,3,6,1,4,1,10728,2,10,2,2,4,1,10),_An80iIfPmpGroupSStoSSMulticast_Type())
an80iIfPmpGroupSStoSSMulticast.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpGroupSStoSSMulticast.setStatus(_A)
_An80iIfPmpGroupStatsTable_Object=MibTable
an80iIfPmpGroupStatsTable=_An80iIfPmpGroupStatsTable_Object((1,3,6,1,4,1,10728,2,10,2,2,5))
if mibBuilder.loadTexts:an80iIfPmpGroupStatsTable.setStatus(_A)
_An80iIfPmpGroupStatsEntry_Object=MibTableRow
an80iIfPmpGroupStatsEntry=_An80iIfPmpGroupStatsEntry_Object((1,3,6,1,4,1,10728,2,10,2,2,5,1))
an80iIfPmpGroupStatsEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:an80iIfPmpGroupStatsEntry.setStatus(_A)
_An80iIfPmpGroupPacketsTx_Type=Counter64
_An80iIfPmpGroupPacketsTx_Object=MibTableColumn
an80iIfPmpGroupPacketsTx=_An80iIfPmpGroupPacketsTx_Object((1,3,6,1,4,1,10728,2,10,2,2,5,1,1),_An80iIfPmpGroupPacketsTx_Type())
an80iIfPmpGroupPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpGroupPacketsTx.setStatus(_A)
_An80iIfPmpGroupPacketDisc_Type=Counter64
_An80iIfPmpGroupPacketDisc_Object=MibTableColumn
an80iIfPmpGroupPacketDisc=_An80iIfPmpGroupPacketDisc_Object((1,3,6,1,4,1,10728,2,10,2,2,5,1,2),_An80iIfPmpGroupPacketDisc_Type())
an80iIfPmpGroupPacketDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpGroupPacketDisc.setStatus(_A)
_An80iIfPmpGroupStatsStatus_Type=RowStatus
_An80iIfPmpGroupStatsStatus_Object=MibTableColumn
an80iIfPmpGroupStatsStatus=_An80iIfPmpGroupStatsStatus_Object((1,3,6,1,4,1,10728,2,10,2,2,5,1,3),_An80iIfPmpGroupStatsStatus_Type())
an80iIfPmpGroupStatsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpGroupStatsStatus.setStatus(_A)
_An80iIfPmpConnConfigTable_Object=MibTable
an80iIfPmpConnConfigTable=_An80iIfPmpConnConfigTable_Object((1,3,6,1,4,1,10728,2,10,2,2,6))
if mibBuilder.loadTexts:an80iIfPmpConnConfigTable.setStatus(_A)
_An80iIfPmpConnConfigEntry_Object=MibTableRow
an80iIfPmpConnConfigEntry=_An80iIfPmpConnConfigEntry_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1))
an80iIfPmpConnConfigEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:an80iIfPmpConnConfigEntry.setStatus(_A)
class _An80iIfPmpConnId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1023))
_An80iIfPmpConnId_Type.__name__=_D
_An80iIfPmpConnId_Object=MibTableColumn
an80iIfPmpConnId=_An80iIfPmpConnId_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,1),_An80iIfPmpConnId_Type())
an80iIfPmpConnId.setMaxAccess(_J)
if mibBuilder.loadTexts:an80iIfPmpConnId.setStatus(_A)
class _An80iIfPmpConnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_An80iIfPmpConnName_Type.__name__=_G
_An80iIfPmpConnName_Object=MibTableColumn
an80iIfPmpConnName=_An80iIfPmpConnName_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,2),_An80iIfPmpConnName_Type())
an80iIfPmpConnName.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpConnName.setStatus(_A)
class _An80iIfPmpConnTaggingControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_An80iIfPmpConnTaggingControl_Type.__name__=_D
_An80iIfPmpConnTaggingControl_Object=MibTableColumn
an80iIfPmpConnTaggingControl=_An80iIfPmpConnTaggingControl_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,3),_An80iIfPmpConnTaggingControl_Type())
an80iIfPmpConnTaggingControl.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpConnTaggingControl.setStatus(_A)
class _An80iIfPmpConnVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_An80iIfPmpConnVlanId_Type.__name__=_D
_An80iIfPmpConnVlanId_Object=MibTableColumn
an80iIfPmpConnVlanId=_An80iIfPmpConnVlanId_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,4),_An80iIfPmpConnVlanId_Type())
an80iIfPmpConnVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpConnVlanId.setStatus(_A)
class _An80iIfPmpConnDefPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_An80iIfPmpConnDefPriority_Type.__name__=_D
_An80iIfPmpConnDefPriority_Object=MibTableColumn
an80iIfPmpConnDefPriority=_An80iIfPmpConnDefPriority_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,5),_An80iIfPmpConnDefPriority_Type())
an80iIfPmpConnDefPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpConnDefPriority.setStatus(_A)
class _An80iIfPmpConnDefParentLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1023))
_An80iIfPmpConnDefParentLink_Type.__name__=_D
_An80iIfPmpConnDefParentLink_Object=MibTableColumn
an80iIfPmpConnDefParentLink=_An80iIfPmpConnDefParentLink_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,6),_An80iIfPmpConnDefParentLink_Type())
an80iIfPmpConnDefParentLink.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpConnDefParentLink.setStatus(_A)
class _An80iIfPmpConnDefParenGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1023))
_An80iIfPmpConnDefParenGroup_Type.__name__=_D
_An80iIfPmpConnDefParenGroup_Object=MibTableColumn
an80iIfPmpConnDefParenGroup=_An80iIfPmpConnDefParenGroup_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,7),_An80iIfPmpConnDefParenGroup_Type())
an80iIfPmpConnDefParenGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpConnDefParenGroup.setStatus(_A)
class _An80iIfPmpConnDLQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,53))
_An80iIfPmpConnDLQos_Type.__name__=_D
_An80iIfPmpConnDLQos_Object=MibTableColumn
an80iIfPmpConnDLQos=_An80iIfPmpConnDLQos_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,8),_An80iIfPmpConnDLQos_Type())
an80iIfPmpConnDLQos.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpConnDLQos.setStatus(_A)
class _An80iIfPmpConnULQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,53))
_An80iIfPmpConnULQos_Type.__name__=_D
_An80iIfPmpConnULQos_Object=MibTableColumn
an80iIfPmpConnULQos=_An80iIfPmpConnULQos_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,9),_An80iIfPmpConnULQos_Type())
an80iIfPmpConnULQos.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpConnULQos.setStatus(_A)
_An80iIfPmpConnConfigStatus_Type=RowStatus
_An80iIfPmpConnConfigStatus_Object=MibTableColumn
an80iIfPmpConnConfigStatus=_An80iIfPmpConnConfigStatus_Object((1,3,6,1,4,1,10728,2,10,2,2,6,1,10),_An80iIfPmpConnConfigStatus_Type())
an80iIfPmpConnConfigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:an80iIfPmpConnConfigStatus.setStatus(_A)
_An80iIfPmpConnStatsTable_Object=MibTable
an80iIfPmpConnStatsTable=_An80iIfPmpConnStatsTable_Object((1,3,6,1,4,1,10728,2,10,2,2,7))
if mibBuilder.loadTexts:an80iIfPmpConnStatsTable.setStatus(_A)
_An80iIfPmpConnStatsEntry_Object=MibTableRow
an80iIfPmpConnStatsEntry=_An80iIfPmpConnStatsEntry_Object((1,3,6,1,4,1,10728,2,10,2,2,7,1))
an80iIfPmpConnStatsEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:an80iIfPmpConnStatsEntry.setStatus(_A)
_An80iIfPmpConnDLPacketsTx_Type=Counter64
_An80iIfPmpConnDLPacketsTx_Object=MibTableColumn
an80iIfPmpConnDLPacketsTx=_An80iIfPmpConnDLPacketsTx_Object((1,3,6,1,4,1,10728,2,10,2,2,7,1,1),_An80iIfPmpConnDLPacketsTx_Type())
an80iIfPmpConnDLPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpConnDLPacketsTx.setStatus(_A)
_An80iIfPmpConnDLPacketsRx_Type=Counter64
_An80iIfPmpConnDLPacketsRx_Object=MibTableColumn
an80iIfPmpConnDLPacketsRx=_An80iIfPmpConnDLPacketsRx_Object((1,3,6,1,4,1,10728,2,10,2,2,7,1,2),_An80iIfPmpConnDLPacketsRx_Type())
an80iIfPmpConnDLPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpConnDLPacketsRx.setStatus(_A)
_An80iIfPmpConnDLPacketsDisc_Type=Counter64
_An80iIfPmpConnDLPacketsDisc_Object=MibTableColumn
an80iIfPmpConnDLPacketsDisc=_An80iIfPmpConnDLPacketsDisc_Object((1,3,6,1,4,1,10728,2,10,2,2,7,1,3),_An80iIfPmpConnDLPacketsDisc_Type())
an80iIfPmpConnDLPacketsDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpConnDLPacketsDisc.setStatus(_A)
_An80iIfPmpConnULPacketsTx_Type=Counter64
_An80iIfPmpConnULPacketsTx_Object=MibTableColumn
an80iIfPmpConnULPacketsTx=_An80iIfPmpConnULPacketsTx_Object((1,3,6,1,4,1,10728,2,10,2,2,7,1,4),_An80iIfPmpConnULPacketsTx_Type())
an80iIfPmpConnULPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpConnULPacketsTx.setStatus(_A)
_An80iIfPmpConnULPacketsRx_Type=Counter64
_An80iIfPmpConnULPacketsRx_Object=MibTableColumn
an80iIfPmpConnULPacketsRx=_An80iIfPmpConnULPacketsRx_Object((1,3,6,1,4,1,10728,2,10,2,2,7,1,5),_An80iIfPmpConnULPacketsRx_Type())
an80iIfPmpConnULPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpConnULPacketsRx.setStatus(_A)
_An80iIfPmpConnULPacketsDisc_Type=Counter64
_An80iIfPmpConnULPacketsDisc_Object=MibTableColumn
an80iIfPmpConnULPacketsDisc=_An80iIfPmpConnULPacketsDisc_Object((1,3,6,1,4,1,10728,2,10,2,2,7,1,6),_An80iIfPmpConnULPacketsDisc_Type())
an80iIfPmpConnULPacketsDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpConnULPacketsDisc.setStatus(_A)
_An80iIfPmpConnStatsStatus_Type=RowStatus
_An80iIfPmpConnStatsStatus_Object=MibTableColumn
an80iIfPmpConnStatsStatus=_An80iIfPmpConnStatsStatus_Object((1,3,6,1,4,1,10728,2,10,2,2,7,1,7),_An80iIfPmpConnStatsStatus_Type())
an80iIfPmpConnStatsStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:an80iIfPmpConnStatsStatus.setStatus(_A)
_RedlineAn80iIfConformance_ObjectIdentity=ObjectIdentity
redlineAn80iIfConformance=_RedlineAn80iIfConformance_ObjectIdentity((1,3,6,1,4,1,10728,2,10,2,4))
_RedlineAn80iIfGroups_ObjectIdentity=ObjectIdentity
redlineAn80iIfGroups=_RedlineAn80iIfGroups_ObjectIdentity((1,3,6,1,4,1,10728,2,10,2,4,1))
_RedlineAn80iIfCompls_ObjectIdentity=ObjectIdentity
redlineAn80iIfCompls=_RedlineAn80iIfCompls_ObjectIdentity((1,3,6,1,4,1,10728,2,10,2,4,2))
redlineAn80iIfPtpGroup=ObjectGroup((1,3,6,1,4,1,10728,2,10,2,4,1,1))
redlineAn80iIfPtpGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:redlineAn80iIfPtpGroup.setStatus(_A)
redlineAn80iIfPmpGroup=ObjectGroup((1,3,6,1,4,1,10728,2,10,2,4,1,2))
redlineAn80iIfPmpGroup.setObjects(*((_B,_M),(_B,_N),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_H),(_B,_z),(_B,_H),(_B,_A0),(_B,_H),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY)))
if mibBuilder.loadTexts:redlineAn80iIfPmpGroup.setStatus(_A)
an80iIfRegistrationFailedTrap=NotificationType((1,3,6,1,4,1,10728,2,10,2,0,1))
an80iIfRegistrationFailedTrap.setObjects((_B,_M))
if mibBuilder.loadTexts:an80iIfRegistrationFailedTrap.setStatus(_A)
an80iIfRegistrationOKTrap=NotificationType((1,3,6,1,4,1,10728,2,10,2,0,2))
an80iIfRegistrationOKTrap.setObjects((_B,_N))
if mibBuilder.loadTexts:an80iIfRegistrationOKTrap.setStatus(_A)
redlineAn80iIfNotificationGroup=NotificationGroup((1,3,6,1,4,1,10728,2,10,2,4,1,3))
redlineAn80iIfNotificationGroup.setObjects(*((_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:redlineAn80iIfNotificationGroup.setStatus(_A)
redlineAn80iIfCompliance=ModuleCompliance((1,3,6,1,4,1,10728,2,10,2,4,2,1))
redlineAn80iIfCompliance.setObjects(*((_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:redlineAn80iIfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'redlineAn80iIfMib':redlineAn80iIfMib,'redlineAn80iIfTrapDefinitions':redlineAn80iIfTrapDefinitions,_AZ:an80iIfRegistrationFailedTrap,_Aa:an80iIfRegistrationOKTrap,'redlineAn80iIfPtpObjects':redlineAn80iIfPtpObjects,'redlineAn80iIfPtpLinkConfig':redlineAn80iIfPtpLinkConfig,_U:an80iIfEncryptionControl,_V:an80iIfModReduction,_W:an80iIfAdaptiveMod,_X:an80iIfUncodedBurstRate,_Y:an80iIfEncryptionKey,_Z:an80iIfPacketRetransControl,_a:an80iIfLinkLenMode,_b:an80iIfLinkLength,_o:an80iIfCalcLinkDst,_p:an80iIfLinkName,'redlineAn80iIfPtpLinkStats':redlineAn80iIfPtpLinkStats,_c:an80iIfCurrUncodedBurstRate,_d:an80iIfPtpLinkStatus,_e:an80iIfRxPackets,_f:an80iIfRxPacketsReTx,_g:an80iIfRxPacketsDisc,_h:an80iIfTxPackets,_i:an80iIfTxPacketsReTx,_j:an80iIfTxPacketsDisc,_k:an80iIfRssiMin,_l:an80iIfRssiMean,_m:an80iIfRssiMax,_n:an80iIfAvrSinAdr,'redlineAn80iIfPmpObjects':redlineAn80iIfPmpObjects,'redlineAn80iIfPmpSsObjects':redlineAn80iIfPmpSsObjects,_M:an80iIfLastMissedMacAddress,_N:an80iIfLastRegistMacAddress,_q:an80iIfDenyMacAddress,_r:an80iIfLastRegistLinkId,'an80iIfPmpLinkConfigTable':an80iIfPmpLinkConfigTable,'an80iIfPmpLinkConfigEntry':an80iIfPmpLinkConfigEntry,_I:an80iIfPmpLinkId,_s:an80iIfPmpLinkName,_t:an80iIfPmpLinkPeerMacAddress,_u:an80iIfPmpLinkULBurstRate,_v:an80iIfPmpLinkDLBurstRate,'an80iIfPmpLinkConfigStatus':an80iIfPmpLinkConfigStatus,'an80iIfPmpLinkStatsTable':an80iIfPmpLinkStatsTable,'an80iIfPmpLinkStatsEntry':an80iIfPmpLinkStatsEntry,_w:an80iIfPmpLinkStatus,_x:an80iIfPmpLinkStatusCode,_y:an80iIfRegPmpLinkConns,_z:an80iIfPmpLinkUpTime,_H:an80iIfPmpLinkLostCount,_A0:an80iIfPmpLinkCurrDLUncBurstRate,'an80iIfPmpLinkDLRssi':an80iIfPmpLinkDLRssi,_A1:an80iIfPmpLinkDLSinAdr,_A2:an80iIfPmpLinkDLLostFrm,_A3:an80iIfPmpLinkDLBlksTot,_A4:an80iIfPmpLinkDLBlksRetr,_A5:an80iIfPmpLinkDLBlksDisc,_A6:an80iIfPmpLinkCurrULUncBurstRate,_A7:an80iIfPmpLinkULRssi,_A8:an80iIfPmpLinkULSinAdr,_A9:an80iIfPmpLinkULLostFrm,_AA:an80iIfPmpLinkULBlksTot,_AB:an80iIfPmpLinkULBlksRetr,_AC:an80iIfPmpLinkULBlksDisc,'an80iIfPmpLinkStatsStatus':an80iIfPmpLinkStatsStatus,'an80iIfPmpGroupConfigTable':an80iIfPmpGroupConfigTable,'an80iIfPmpGroupConfigEntry':an80iIfPmpGroupConfigEntry,_K:an80iIfPmpGroupId,_AD:an80iIfPmpGroupName,_AE:an80iIfPmpGroupTaggingControl,_AF:an80iIfPmpGroupVlanId,_AG:an80iIfPmpGroupDefPriority,_AH:an80iIfPmpGroupSCEtherControl,_AI:an80iIfPmpGroupQosLevel,'an80iIfPmpGroupConfigStatus':an80iIfPmpGroupConfigStatus,'an80iIfPmpGroupRate':an80iIfPmpGroupRate,'an80iIfPmpGroupSStoSSMulticast':an80iIfPmpGroupSStoSSMulticast,'an80iIfPmpGroupStatsTable':an80iIfPmpGroupStatsTable,'an80iIfPmpGroupStatsEntry':an80iIfPmpGroupStatsEntry,_AJ:an80iIfPmpGroupPacketsTx,_AK:an80iIfPmpGroupPacketDisc,'an80iIfPmpGroupStatsStatus':an80iIfPmpGroupStatsStatus,'an80iIfPmpConnConfigTable':an80iIfPmpConnConfigTable,'an80iIfPmpConnConfigEntry':an80iIfPmpConnConfigEntry,_L:an80iIfPmpConnId,_AL:an80iIfPmpConnName,_AM:an80iIfPmpConnTaggingControl,_AN:an80iIfPmpConnVlanId,_AO:an80iIfPmpConnDefPriority,_AP:an80iIfPmpConnDefParentLink,_AQ:an80iIfPmpConnDefParenGroup,_AR:an80iIfPmpConnDLQos,_AS:an80iIfPmpConnULQos,'an80iIfPmpConnConfigStatus':an80iIfPmpConnConfigStatus,'an80iIfPmpConnStatsTable':an80iIfPmpConnStatsTable,'an80iIfPmpConnStatsEntry':an80iIfPmpConnStatsEntry,_AT:an80iIfPmpConnDLPacketsTx,_AU:an80iIfPmpConnDLPacketsRx,_AV:an80iIfPmpConnDLPacketsDisc,_AW:an80iIfPmpConnULPacketsTx,_AX:an80iIfPmpConnULPacketsRx,_AY:an80iIfPmpConnULPacketsDisc,'an80iIfPmpConnStatsStatus':an80iIfPmpConnStatsStatus,'redlineAn80iIfConformance':redlineAn80iIfConformance,'redlineAn80iIfGroups':redlineAn80iIfGroups,_Ab:redlineAn80iIfPtpGroup,_Ac:redlineAn80iIfPmpGroup,_Ad:redlineAn80iIfNotificationGroup,'redlineAn80iIfCompls':redlineAn80iIfCompls,'redlineAn80iIfCompliance':redlineAn80iIfCompliance})