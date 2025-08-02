_n='ipadAtmFrf8SvcVciIndex'
_m='ipadAtmFrf8SvcVpiIndex'
_l='ipadAtmFrf8SvcIfIndex'
_k='ipadAtmFrf5DlciIndex'
_j='ipadAtmFrf5DlciVciIndex'
_i='ipadAtmFrf5DlciVpiIndex'
_h='ipadAtmFrf5DlciIfIndex'
_g='ipadAtmFrf5SvcVciIndex'
_f='ipadAtmFrf5SvcVpiIndex'
_e='ipadAtmFrf5SvcIfIndex'
_d='ipadAtmCesIndex'
_c='ipadAtmVccStatsPeriodIndex'
_b='ipadAtmVccStatsVciIndex'
_a='ipadAtmVccStatsVpiIndex'
_Z='ipadAtmVccStatsIndex'
_Y='sinkAndSource'
_X='source'
_W='loopback'
_V='ipadAtmVccVciIndex'
_U='ipadAtmVccVpiIndex'
_T='ipadAtmVccIndex'
_S='ipadAtmStatsPeriodIndex'
_R='ipadAtmStatsIndex'
_Q='clearStats'
_P='clearAlarms'
_O='ipadAtmIfIndex'
_N='mode2Const1'
_M='mode2Const0'
_L='enable'
_K='disable'
_J='DisplayString'
_I='inactive'
_H='mode1'
_G='active'
_F='other'
_E='IPAD-ATM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipad,=mibBuilder.importSymbols('IPADv2-MIB','ipad')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
ipadAtm=ModuleIdentity((1,3,6,1,4,1,321,100,1,25))
_IpadAtmParms_ObjectIdentity=ObjectIdentity
ipadAtmParms=_IpadAtmParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,25,1))
_IpadAtmTable_Object=MibTable
ipadAtmTable=_IpadAtmTable_Object((1,3,6,1,4,1,321,100,1,25,1,1))
if mibBuilder.loadTexts:ipadAtmTable.setStatus(_A)
_IpadAtmTableEntry_Object=MibTableRow
ipadAtmTableEntry=_IpadAtmTableEntry_Object((1,3,6,1,4,1,321,100,1,25,1,1,1))
ipadAtmTableEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:ipadAtmTableEntry.setStatus(_A)
_IpadAtmIfIndex_Type=Integer32
_IpadAtmIfIndex_Object=MibTableColumn
ipadAtmIfIndex=_IpadAtmIfIndex_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,1),_IpadAtmIfIndex_Type())
ipadAtmIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmIfIndex.setStatus(_A)
class _IpadAtmOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),('down',2),('upNoCellSync',3),('upCellSync',4)))
_IpadAtmOperStatus_Type.__name__=_C
_IpadAtmOperStatus_Object=MibTableColumn
ipadAtmOperStatus=_IpadAtmOperStatus_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,2),_IpadAtmOperStatus_Type())
ipadAtmOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmOperStatus.setStatus(_A)
_IpadAtmVccsOpenedOK_Type=Integer32
_IpadAtmVccsOpenedOK_Object=MibTableColumn
ipadAtmVccsOpenedOK=_IpadAtmVccsOpenedOK_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,3),_IpadAtmVccsOpenedOK_Type())
ipadAtmVccsOpenedOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccsOpenedOK.setStatus(_A)
_IpadAtmVccsNotOpened_Type=Integer32
_IpadAtmVccsNotOpened_Object=MibTableColumn
ipadAtmVccsNotOpened=_IpadAtmVccsNotOpened_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,4),_IpadAtmVccsNotOpened_Type())
ipadAtmVccsNotOpened.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccsNotOpened.setStatus(_A)
class _IpadAtmAlarmReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_IpadAtmAlarmReset_Type.__name__=_C
_IpadAtmAlarmReset_Object=MibTableColumn
ipadAtmAlarmReset=_IpadAtmAlarmReset_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,5),_IpadAtmAlarmReset_Type())
ipadAtmAlarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmAlarmReset.setStatus(_A)
class _IpadAtmOverSubscriptionFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_IpadAtmOverSubscriptionFactor_Type.__name__=_C
_IpadAtmOverSubscriptionFactor_Object=MibTableColumn
ipadAtmOverSubscriptionFactor=_IpadAtmOverSubscriptionFactor_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,6),_IpadAtmOverSubscriptionFactor_Type())
ipadAtmOverSubscriptionFactor.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmOverSubscriptionFactor.setStatus(_A)
_IpadAtmLineBandwidth_Type=Integer32
_IpadAtmLineBandwidth_Object=MibTableColumn
ipadAtmLineBandwidth=_IpadAtmLineBandwidth_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,7),_IpadAtmLineBandwidth_Type())
ipadAtmLineBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmLineBandwidth.setStatus(_A)
_IpadAtmAAL5Bandwidth_Type=Integer32
_IpadAtmAAL5Bandwidth_Object=MibTableColumn
ipadAtmAAL5Bandwidth=_IpadAtmAAL5Bandwidth_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,8),_IpadAtmAAL5Bandwidth_Type())
ipadAtmAAL5Bandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmAAL5Bandwidth.setStatus(_A)
_IpadAtmOverSubBandwidth_Type=Integer32
_IpadAtmOverSubBandwidth_Object=MibTableColumn
ipadAtmOverSubBandwidth=_IpadAtmOverSubBandwidth_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,9),_IpadAtmOverSubBandwidth_Type())
ipadAtmOverSubBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmOverSubBandwidth.setStatus(_A)
_IpadAtmCbrUsedBandwidth_Type=Integer32
_IpadAtmCbrUsedBandwidth_Object=MibTableColumn
ipadAtmCbrUsedBandwidth=_IpadAtmCbrUsedBandwidth_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,10),_IpadAtmCbrUsedBandwidth_Type())
ipadAtmCbrUsedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmCbrUsedBandwidth.setStatus(_A)
_IpadAtmVbrUsedBandwidth_Type=Integer32
_IpadAtmVbrUsedBandwidth_Object=MibTableColumn
ipadAtmVbrUsedBandwidth=_IpadAtmVbrUsedBandwidth_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,11),_IpadAtmVbrUsedBandwidth_Type())
ipadAtmVbrUsedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVbrUsedBandwidth.setStatus(_A)
_IpadAtmUbrUsedBandwidth_Type=Integer32
_IpadAtmUbrUsedBandwidth_Object=MibTableColumn
ipadAtmUbrUsedBandwidth=_IpadAtmUbrUsedBandwidth_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,12),_IpadAtmUbrUsedBandwidth_Type())
ipadAtmUbrUsedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmUbrUsedBandwidth.setStatus(_A)
_IpadAtmQos0Pcr_Type=Integer32
_IpadAtmQos0Pcr_Object=MibTableColumn
ipadAtmQos0Pcr=_IpadAtmQos0Pcr_Object((1,3,6,1,4,1,321,100,1,25,1,1,1,13),_IpadAtmQos0Pcr_Type())
ipadAtmQos0Pcr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmQos0Pcr.setStatus(_A)
_IpadAtmStatsParms_ObjectIdentity=ObjectIdentity
ipadAtmStatsParms=_IpadAtmStatsParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,25,2))
_IpadAtmStatsTable_Object=MibTable
ipadAtmStatsTable=_IpadAtmStatsTable_Object((1,3,6,1,4,1,321,100,1,25,2,1))
if mibBuilder.loadTexts:ipadAtmStatsTable.setStatus(_A)
_IpadAtmStatsTableEntry_Object=MibTableRow
ipadAtmStatsTableEntry=_IpadAtmStatsTableEntry_Object((1,3,6,1,4,1,321,100,1,25,2,1,1))
ipadAtmStatsTableEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:ipadAtmStatsTableEntry.setStatus(_A)
_IpadAtmStatsIndex_Type=Integer32
_IpadAtmStatsIndex_Object=MibTableColumn
ipadAtmStatsIndex=_IpadAtmStatsIndex_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,1),_IpadAtmStatsIndex_Type())
ipadAtmStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsIndex.setStatus(_A)
_IpadAtmStatsPeriodIndex_Type=Integer32
_IpadAtmStatsPeriodIndex_Object=MibTableColumn
ipadAtmStatsPeriodIndex=_IpadAtmStatsPeriodIndex_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,2),_IpadAtmStatsPeriodIndex_Type())
ipadAtmStatsPeriodIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsPeriodIndex.setStatus(_A)
_IpadAtmStatsTimeStamp_Type=TimeTicks
_IpadAtmStatsTimeStamp_Object=MibTableColumn
ipadAtmStatsTimeStamp=_IpadAtmStatsTimeStamp_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,3),_IpadAtmStatsTimeStamp_Type())
ipadAtmStatsTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsTimeStamp.setStatus(_A)
_IpadAtmStatsRxFramesOK_Type=Integer32
_IpadAtmStatsRxFramesOK_Object=MibTableColumn
ipadAtmStatsRxFramesOK=_IpadAtmStatsRxFramesOK_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,4),_IpadAtmStatsRxFramesOK_Type())
ipadAtmStatsRxFramesOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsRxFramesOK.setStatus(_A)
_IpadAtmStatsTxFramesOK_Type=Integer32
_IpadAtmStatsTxFramesOK_Object=MibTableColumn
ipadAtmStatsTxFramesOK=_IpadAtmStatsTxFramesOK_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,5),_IpadAtmStatsTxFramesOK_Type())
ipadAtmStatsTxFramesOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsTxFramesOK.setStatus(_A)
_IpadAtmStatsRxFramesError_Type=Integer32
_IpadAtmStatsRxFramesError_Object=MibTableColumn
ipadAtmStatsRxFramesError=_IpadAtmStatsRxFramesError_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,6),_IpadAtmStatsRxFramesError_Type())
ipadAtmStatsRxFramesError.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsRxFramesError.setStatus(_A)
_IpadAtmStatsTxFramesError_Type=Integer32
_IpadAtmStatsTxFramesError_Object=MibTableColumn
ipadAtmStatsTxFramesError=_IpadAtmStatsTxFramesError_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,7),_IpadAtmStatsTxFramesError_Type())
ipadAtmStatsTxFramesError.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsTxFramesError.setStatus(_A)
_IpadAtmStatsRxBytesOK_Type=Integer32
_IpadAtmStatsRxBytesOK_Object=MibTableColumn
ipadAtmStatsRxBytesOK=_IpadAtmStatsRxBytesOK_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,8),_IpadAtmStatsRxBytesOK_Type())
ipadAtmStatsRxBytesOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsRxBytesOK.setStatus(_A)
_IpadAtmStatsTxBytesOK_Type=Integer32
_IpadAtmStatsTxBytesOK_Object=MibTableColumn
ipadAtmStatsTxBytesOK=_IpadAtmStatsTxBytesOK_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,9),_IpadAtmStatsTxBytesOK_Type())
ipadAtmStatsTxBytesOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsTxBytesOK.setStatus(_A)
_IpadAtmStatsLostSync_Type=Integer32
_IpadAtmStatsLostSync_Object=MibTableColumn
ipadAtmStatsLostSync=_IpadAtmStatsLostSync_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,10),_IpadAtmStatsLostSync_Type())
ipadAtmStatsLostSync.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsLostSync.setStatus(_A)
_IpadAtmStatsOamCellsRx_Type=Integer32
_IpadAtmStatsOamCellsRx_Object=MibTableColumn
ipadAtmStatsOamCellsRx=_IpadAtmStatsOamCellsRx_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,11),_IpadAtmStatsOamCellsRx_Type())
ipadAtmStatsOamCellsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsOamCellsRx.setStatus(_A)
_IpadAtmStatsOamCellsTx_Type=Integer32
_IpadAtmStatsOamCellsTx_Object=MibTableColumn
ipadAtmStatsOamCellsTx=_IpadAtmStatsOamCellsTx_Object((1,3,6,1,4,1,321,100,1,25,2,1,1,12),_IpadAtmStatsOamCellsTx_Type())
ipadAtmStatsOamCellsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmStatsOamCellsTx.setStatus(_A)
_IpadAtmVccParms_ObjectIdentity=ObjectIdentity
ipadAtmVccParms=_IpadAtmVccParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,25,3))
_IpadAtmVccTable_Object=MibTable
ipadAtmVccTable=_IpadAtmVccTable_Object((1,3,6,1,4,1,321,100,1,25,3,1))
if mibBuilder.loadTexts:ipadAtmVccTable.setStatus(_A)
_IpadAtmVccTableEntry_Object=MibTableRow
ipadAtmVccTableEntry=_IpadAtmVccTableEntry_Object((1,3,6,1,4,1,321,100,1,25,3,1,1))
ipadAtmVccTableEntry.setIndexNames((0,_E,_T),(0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:ipadAtmVccTableEntry.setStatus(_A)
_IpadAtmVccIndex_Type=Integer32
_IpadAtmVccIndex_Object=MibTableColumn
ipadAtmVccIndex=_IpadAtmVccIndex_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,1),_IpadAtmVccIndex_Type())
ipadAtmVccIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccIndex.setStatus(_A)
_IpadAtmVccVpiIndex_Type=Integer32
_IpadAtmVccVpiIndex_Object=MibTableColumn
ipadAtmVccVpiIndex=_IpadAtmVccVpiIndex_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,2),_IpadAtmVccVpiIndex_Type())
ipadAtmVccVpiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccVpiIndex.setStatus(_A)
_IpadAtmVccVciIndex_Type=Integer32
_IpadAtmVccVciIndex_Object=MibTableColumn
ipadAtmVccVciIndex=_IpadAtmVccVciIndex_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,3),_IpadAtmVccVciIndex_Type())
ipadAtmVccVciIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccVciIndex.setStatus(_A)
class _IpadAtmVccEncapsulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),('serialPPPoA',2),('vcMux',3),('llcMux',4),('serialHDLCoA',5),('frf5',6),('frf8',7)))
_IpadAtmVccEncapsulationType_Type.__name__=_C
_IpadAtmVccEncapsulationType_Object=MibTableColumn
ipadAtmVccEncapsulationType=_IpadAtmVccEncapsulationType_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,4),_IpadAtmVccEncapsulationType_Type())
ipadAtmVccEncapsulationType.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmVccEncapsulationType.setStatus(_A)
class _IpadAtmVccTrafficType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_F,1),('cbr',2),('rtVbr',3),('nrtVbr',4),('abr',5),('ubr',6)))
_IpadAtmVccTrafficType_Type.__name__=_C
_IpadAtmVccTrafficType_Object=MibTableColumn
ipadAtmVccTrafficType=_IpadAtmVccTrafficType_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,5),_IpadAtmVccTrafficType_Type())
ipadAtmVccTrafficType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccTrafficType.setStatus(_A)
_IpadAtmVccChannelRate_Type=Integer32
_IpadAtmVccChannelRate_Object=MibTableColumn
ipadAtmVccChannelRate=_IpadAtmVccChannelRate_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,6),_IpadAtmVccChannelRate_Type())
ipadAtmVccChannelRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccChannelRate.setStatus(_A)
class _IpadAtmVccAlarmReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_P,2),(_Q,3)))
_IpadAtmVccAlarmReset_Type.__name__=_C
_IpadAtmVccAlarmReset_Object=MibTableColumn
ipadAtmVccAlarmReset=_IpadAtmVccAlarmReset_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,7),_IpadAtmVccAlarmReset_Type())
ipadAtmVccAlarmReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmVccAlarmReset.setStatus(_A)
_IpadAtmVccSLATimer_Type=Integer32
_IpadAtmVccSLATimer_Object=MibTableColumn
ipadAtmVccSLATimer=_IpadAtmVccSLATimer_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,8),_IpadAtmVccSLATimer_Type())
ipadAtmVccSLATimer.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmVccSLATimer.setStatus(_A)
_IpadAtmVccRemoteFramesOffered_Type=Integer32
_IpadAtmVccRemoteFramesOffered_Object=MibTableColumn
ipadAtmVccRemoteFramesOffered=_IpadAtmVccRemoteFramesOffered_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,9),_IpadAtmVccRemoteFramesOffered_Type())
ipadAtmVccRemoteFramesOffered.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccRemoteFramesOffered.setStatus(_A)
_IpadAtmVccFramesReceived_Type=Integer32
_IpadAtmVccFramesReceived_Object=MibTableColumn
ipadAtmVccFramesReceived=_IpadAtmVccFramesReceived_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,10),_IpadAtmVccFramesReceived_Type())
ipadAtmVccFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccFramesReceived.setStatus(_A)
_IpadAtmVccRemoteDataOffered_Type=Integer32
_IpadAtmVccRemoteDataOffered_Object=MibTableColumn
ipadAtmVccRemoteDataOffered=_IpadAtmVccRemoteDataOffered_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,11),_IpadAtmVccRemoteDataOffered_Type())
ipadAtmVccRemoteDataOffered.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccRemoteDataOffered.setStatus(_A)
_IpadAtmVccDataReceived_Type=Integer32
_IpadAtmVccDataReceived_Object=MibTableColumn
ipadAtmVccDataReceived=_IpadAtmVccDataReceived_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,12),_IpadAtmVccDataReceived_Type())
ipadAtmVccDataReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccDataReceived.setStatus(_A)
class _IpadAtmVccRemoteActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_I,2),(_G,3)))
_IpadAtmVccRemoteActive_Type.__name__=_C
_IpadAtmVccRemoteActive_Object=MibTableColumn
ipadAtmVccRemoteActive=_IpadAtmVccRemoteActive_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,13),_IpadAtmVccRemoteActive_Type())
ipadAtmVccRemoteActive.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccRemoteActive.setStatus(_A)
_IpadAtmVccRemoteVpi_Type=Integer32
_IpadAtmVccRemoteVpi_Object=MibTableColumn
ipadAtmVccRemoteVpi=_IpadAtmVccRemoteVpi_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,14),_IpadAtmVccRemoteVpi_Type())
ipadAtmVccRemoteVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccRemoteVpi.setStatus(_A)
_IpadAtmVccRemoteVci_Type=Integer32
_IpadAtmVccRemoteVci_Object=MibTableColumn
ipadAtmVccRemoteVci=_IpadAtmVccRemoteVci_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,15),_IpadAtmVccRemoteVci_Type())
ipadAtmVccRemoteVci.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccRemoteVci.setStatus(_A)
_IpadAtmVccRemoteIPAddress_Type=IpAddress
_IpadAtmVccRemoteIPAddress_Object=MibTableColumn
ipadAtmVccRemoteIPAddress=_IpadAtmVccRemoteIPAddress_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,16),_IpadAtmVccRemoteIPAddress_Type())
ipadAtmVccRemoteIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccRemoteIPAddress.setStatus(_A)
_IpadAtmVccRemoteUnitId_Type=DisplayString
_IpadAtmVccRemoteUnitId_Object=MibTableColumn
ipadAtmVccRemoteUnitId=_IpadAtmVccRemoteUnitId_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,17),_IpadAtmVccRemoteUnitId_Type())
ipadAtmVccRemoteUnitId.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccRemoteUnitId.setStatus(_A)
class _IpadAtmVccEtoeLoopbackCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('start',2),('stop',3)))
_IpadAtmVccEtoeLoopbackCommand_Type.__name__=_C
_IpadAtmVccEtoeLoopbackCommand_Object=MibTableColumn
ipadAtmVccEtoeLoopbackCommand=_IpadAtmVccEtoeLoopbackCommand_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,18),_IpadAtmVccEtoeLoopbackCommand_Type())
ipadAtmVccEtoeLoopbackCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmVccEtoeLoopbackCommand.setStatus(_A)
class _IpadAtmVccEtoeLoopbackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_W,3)))
_IpadAtmVccEtoeLoopbackState_Type.__name__=_C
_IpadAtmVccEtoeLoopbackState_Object=MibTableColumn
ipadAtmVccEtoeLoopbackState=_IpadAtmVccEtoeLoopbackState_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,19),_IpadAtmVccEtoeLoopbackState_Type())
ipadAtmVccEtoeLoopbackState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeLoopbackState.setStatus(_A)
_IpadAtmVccEtoeLoopbackCellsTx_Type=Integer32
_IpadAtmVccEtoeLoopbackCellsTx_Object=MibTableColumn
ipadAtmVccEtoeLoopbackCellsTx=_IpadAtmVccEtoeLoopbackCellsTx_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,20),_IpadAtmVccEtoeLoopbackCellsTx_Type())
ipadAtmVccEtoeLoopbackCellsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeLoopbackCellsTx.setStatus(_A)
_IpadAtmVccEtoeLoopbackCellsRx_Type=Integer32
_IpadAtmVccEtoeLoopbackCellsRx_Object=MibTableColumn
ipadAtmVccEtoeLoopbackCellsRx=_IpadAtmVccEtoeLoopbackCellsRx_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,21),_IpadAtmVccEtoeLoopbackCellsRx_Type())
ipadAtmVccEtoeLoopbackCellsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeLoopbackCellsRx.setStatus(_A)
_IpadAtmVccEtoeLoopbackRttMin_Type=Integer32
_IpadAtmVccEtoeLoopbackRttMin_Object=MibTableColumn
ipadAtmVccEtoeLoopbackRttMin=_IpadAtmVccEtoeLoopbackRttMin_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,22),_IpadAtmVccEtoeLoopbackRttMin_Type())
ipadAtmVccEtoeLoopbackRttMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeLoopbackRttMin.setStatus(_A)
_IpadAtmVccEtoeLoopbackRttMax_Type=Integer32
_IpadAtmVccEtoeLoopbackRttMax_Object=MibTableColumn
ipadAtmVccEtoeLoopbackRttMax=_IpadAtmVccEtoeLoopbackRttMax_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,23),_IpadAtmVccEtoeLoopbackRttMax_Type())
ipadAtmVccEtoeLoopbackRttMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeLoopbackRttMax.setStatus(_A)
_IpadAtmVccEtoeLoopbackRttAvg_Type=Integer32
_IpadAtmVccEtoeLoopbackRttAvg_Object=MibTableColumn
ipadAtmVccEtoeLoopbackRttAvg=_IpadAtmVccEtoeLoopbackRttAvg_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,24),_IpadAtmVccEtoeLoopbackRttAvg_Type())
ipadAtmVccEtoeLoopbackRttAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeLoopbackRttAvg.setStatus(_A)
class _IpadAtmVccSegLoopbackCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('start',2),('stop',3)))
_IpadAtmVccSegLoopbackCommand_Type.__name__=_C
_IpadAtmVccSegLoopbackCommand_Object=MibTableColumn
ipadAtmVccSegLoopbackCommand=_IpadAtmVccSegLoopbackCommand_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,25),_IpadAtmVccSegLoopbackCommand_Type())
ipadAtmVccSegLoopbackCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmVccSegLoopbackCommand.setStatus(_A)
class _IpadAtmVccSegLoopbackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_W,3)))
_IpadAtmVccSegLoopbackState_Type.__name__=_C
_IpadAtmVccSegLoopbackState_Object=MibTableColumn
ipadAtmVccSegLoopbackState=_IpadAtmVccSegLoopbackState_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,26),_IpadAtmVccSegLoopbackState_Type())
ipadAtmVccSegLoopbackState.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccSegLoopbackState.setStatus(_A)
_IpadAtmVccSegLoopbackCellsTx_Type=Integer32
_IpadAtmVccSegLoopbackCellsTx_Object=MibTableColumn
ipadAtmVccSegLoopbackCellsTx=_IpadAtmVccSegLoopbackCellsTx_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,27),_IpadAtmVccSegLoopbackCellsTx_Type())
ipadAtmVccSegLoopbackCellsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccSegLoopbackCellsTx.setStatus(_A)
_IpadAtmVccSegLoopbackCellsRx_Type=Integer32
_IpadAtmVccSegLoopbackCellsRx_Object=MibTableColumn
ipadAtmVccSegLoopbackCellsRx=_IpadAtmVccSegLoopbackCellsRx_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,28),_IpadAtmVccSegLoopbackCellsRx_Type())
ipadAtmVccSegLoopbackCellsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccSegLoopbackCellsRx.setStatus(_A)
_IpadAtmVccSegLoopbackRttMin_Type=Integer32
_IpadAtmVccSegLoopbackRttMin_Object=MibTableColumn
ipadAtmVccSegLoopbackRttMin=_IpadAtmVccSegLoopbackRttMin_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,29),_IpadAtmVccSegLoopbackRttMin_Type())
ipadAtmVccSegLoopbackRttMin.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccSegLoopbackRttMin.setStatus(_A)
_IpadAtmVccSegLoopbackRttMax_Type=Integer32
_IpadAtmVccSegLoopbackRttMax_Object=MibTableColumn
ipadAtmVccSegLoopbackRttMax=_IpadAtmVccSegLoopbackRttMax_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,30),_IpadAtmVccSegLoopbackRttMax_Type())
ipadAtmVccSegLoopbackRttMax.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccSegLoopbackRttMax.setStatus(_A)
_IpadAtmVccSegLoopbackRttAvg_Type=Integer32
_IpadAtmVccSegLoopbackRttAvg_Object=MibTableColumn
ipadAtmVccSegLoopbackRttAvg=_IpadAtmVccSegLoopbackRttAvg_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,31),_IpadAtmVccSegLoopbackRttAvg_Type())
ipadAtmVccSegLoopbackRttAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccSegLoopbackRttAvg.setStatus(_A)
class _IpadAtmVccEtoeContCheckCommand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('activate',2),('deactivate',3)))
_IpadAtmVccEtoeContCheckCommand_Type.__name__=_C
_IpadAtmVccEtoeContCheckCommand_Object=MibTableColumn
ipadAtmVccEtoeContCheckCommand=_IpadAtmVccEtoeContCheckCommand_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,32),_IpadAtmVccEtoeContCheckCommand_Type())
ipadAtmVccEtoeContCheckCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmVccEtoeContCheckCommand.setStatus(_A)
class _IpadAtmVccEtoeContCheckAutoActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_K,2),(_L,3)))
_IpadAtmVccEtoeContCheckAutoActivate_Type.__name__=_C
_IpadAtmVccEtoeContCheckAutoActivate_Object=MibTableColumn
ipadAtmVccEtoeContCheckAutoActivate=_IpadAtmVccEtoeContCheckAutoActivate_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,33),_IpadAtmVccEtoeContCheckAutoActivate_Type())
ipadAtmVccEtoeContCheckAutoActivate.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmVccEtoeContCheckAutoActivate.setStatus(_A)
class _IpadAtmVccEtoeContCheckType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('sink',2),(_X,3),(_Y,4)))
_IpadAtmVccEtoeContCheckType_Type.__name__=_C
_IpadAtmVccEtoeContCheckType_Object=MibTableColumn
ipadAtmVccEtoeContCheckType=_IpadAtmVccEtoeContCheckType_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,34),_IpadAtmVccEtoeContCheckType_Type())
ipadAtmVccEtoeContCheckType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeContCheckType.setStatus(_A)
class _IpadAtmVccEtoeContCheckTypeInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('sink',2),(_X,3),(_Y,4)))
_IpadAtmVccEtoeContCheckTypeInUse_Type.__name__=_C
_IpadAtmVccEtoeContCheckTypeInUse_Object=MibTableColumn
ipadAtmVccEtoeContCheckTypeInUse=_IpadAtmVccEtoeContCheckTypeInUse_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,35),_IpadAtmVccEtoeContCheckTypeInUse_Type())
ipadAtmVccEtoeContCheckTypeInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeContCheckTypeInUse.setStatus(_A)
class _IpadAtmVccEtoeContCheckStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ready',1),(_G,2),('activationFailed',3),('activating',4),('deactivating',5)))
_IpadAtmVccEtoeContCheckStatus_Type.__name__=_C
_IpadAtmVccEtoeContCheckStatus_Object=MibTableColumn
ipadAtmVccEtoeContCheckStatus=_IpadAtmVccEtoeContCheckStatus_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,36),_IpadAtmVccEtoeContCheckStatus_Type())
ipadAtmVccEtoeContCheckStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeContCheckStatus.setStatus(_A)
_IpadAtmVccEtoeContCheckCellsTx_Type=Integer32
_IpadAtmVccEtoeContCheckCellsTx_Object=MibTableColumn
ipadAtmVccEtoeContCheckCellsTx=_IpadAtmVccEtoeContCheckCellsTx_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,37),_IpadAtmVccEtoeContCheckCellsTx_Type())
ipadAtmVccEtoeContCheckCellsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeContCheckCellsTx.setStatus(_A)
_IpadAtmVccEtoeContCheckCellsRx_Type=Integer32
_IpadAtmVccEtoeContCheckCellsRx_Object=MibTableColumn
ipadAtmVccEtoeContCheckCellsRx=_IpadAtmVccEtoeContCheckCellsRx_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,38),_IpadAtmVccEtoeContCheckCellsRx_Type())
ipadAtmVccEtoeContCheckCellsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeContCheckCellsRx.setStatus(_A)
class _IpadAtmVccEtoeAisStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAis',1),('ais',2)))
_IpadAtmVccEtoeAisStatus_Type.__name__=_C
_IpadAtmVccEtoeAisStatus_Object=MibTableColumn
ipadAtmVccEtoeAisStatus=_IpadAtmVccEtoeAisStatus_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,39),_IpadAtmVccEtoeAisStatus_Type())
ipadAtmVccEtoeAisStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeAisStatus.setStatus(_A)
class _IpadAtmVccEtoeRdiStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noRdi',1),('rdi',2)))
_IpadAtmVccEtoeRdiStatus_Type.__name__=_C
_IpadAtmVccEtoeRdiStatus_Object=MibTableColumn
ipadAtmVccEtoeRdiStatus=_IpadAtmVccEtoeRdiStatus_Object((1,3,6,1,4,1,321,100,1,25,3,1,1,40),_IpadAtmVccEtoeRdiStatus_Type())
ipadAtmVccEtoeRdiStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccEtoeRdiStatus.setStatus(_A)
_IpadAtmVccStatsParms_ObjectIdentity=ObjectIdentity
ipadAtmVccStatsParms=_IpadAtmVccStatsParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,25,4))
_IpadAtmVccStatsTable_Object=MibTable
ipadAtmVccStatsTable=_IpadAtmVccStatsTable_Object((1,3,6,1,4,1,321,100,1,25,4,1))
if mibBuilder.loadTexts:ipadAtmVccStatsTable.setStatus(_A)
_IpadAtmVccStatsTableEntry_Object=MibTableRow
ipadAtmVccStatsTableEntry=_IpadAtmVccStatsTableEntry_Object((1,3,6,1,4,1,321,100,1,25,4,1,1))
ipadAtmVccStatsTableEntry.setIndexNames((0,_E,_Z),(0,_E,_a),(0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:ipadAtmVccStatsTableEntry.setStatus(_A)
_IpadAtmVccStatsIndex_Type=Integer32
_IpadAtmVccStatsIndex_Object=MibTableColumn
ipadAtmVccStatsIndex=_IpadAtmVccStatsIndex_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,1),_IpadAtmVccStatsIndex_Type())
ipadAtmVccStatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsIndex.setStatus(_A)
_IpadAtmVccStatsVpiIndex_Type=Integer32
_IpadAtmVccStatsVpiIndex_Object=MibTableColumn
ipadAtmVccStatsVpiIndex=_IpadAtmVccStatsVpiIndex_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,2),_IpadAtmVccStatsVpiIndex_Type())
ipadAtmVccStatsVpiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsVpiIndex.setStatus(_A)
_IpadAtmVccStatsVciIndex_Type=Integer32
_IpadAtmVccStatsVciIndex_Object=MibTableColumn
ipadAtmVccStatsVciIndex=_IpadAtmVccStatsVciIndex_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,3),_IpadAtmVccStatsVciIndex_Type())
ipadAtmVccStatsVciIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsVciIndex.setStatus(_A)
_IpadAtmVccStatsPeriodIndex_Type=Integer32
_IpadAtmVccStatsPeriodIndex_Object=MibTableColumn
ipadAtmVccStatsPeriodIndex=_IpadAtmVccStatsPeriodIndex_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,4),_IpadAtmVccStatsPeriodIndex_Type())
ipadAtmVccStatsPeriodIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsPeriodIndex.setStatus(_A)
_IpadAtmVccStatsTimeStamp_Type=TimeTicks
_IpadAtmVccStatsTimeStamp_Object=MibTableColumn
ipadAtmVccStatsTimeStamp=_IpadAtmVccStatsTimeStamp_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,5),_IpadAtmVccStatsTimeStamp_Type())
ipadAtmVccStatsTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsTimeStamp.setStatus(_A)
_IpadAtmVccStatsRxFramesOK_Type=Integer32
_IpadAtmVccStatsRxFramesOK_Object=MibTableColumn
ipadAtmVccStatsRxFramesOK=_IpadAtmVccStatsRxFramesOK_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,6),_IpadAtmVccStatsRxFramesOK_Type())
ipadAtmVccStatsRxFramesOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesOK.setStatus(_A)
_IpadAtmVccStatsTxFramesOK_Type=Integer32
_IpadAtmVccStatsTxFramesOK_Object=MibTableColumn
ipadAtmVccStatsTxFramesOK=_IpadAtmVccStatsTxFramesOK_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,7),_IpadAtmVccStatsTxFramesOK_Type())
ipadAtmVccStatsTxFramesOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsTxFramesOK.setStatus(_A)
_IpadAtmVccStatsRxFramesError_Type=Integer32
_IpadAtmVccStatsRxFramesError_Object=MibTableColumn
ipadAtmVccStatsRxFramesError=_IpadAtmVccStatsRxFramesError_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,8),_IpadAtmVccStatsRxFramesError_Type())
ipadAtmVccStatsRxFramesError.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesError.setStatus(_A)
_IpadAtmVccStatsTxFramesError_Type=Integer32
_IpadAtmVccStatsTxFramesError_Object=MibTableColumn
ipadAtmVccStatsTxFramesError=_IpadAtmVccStatsTxFramesError_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,9),_IpadAtmVccStatsTxFramesError_Type())
ipadAtmVccStatsTxFramesError.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsTxFramesError.setStatus(_A)
_IpadAtmVccStatsRxFramesCLP_Type=Integer32
_IpadAtmVccStatsRxFramesCLP_Object=MibTableColumn
ipadAtmVccStatsRxFramesCLP=_IpadAtmVccStatsRxFramesCLP_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,10),_IpadAtmVccStatsRxFramesCLP_Type())
ipadAtmVccStatsRxFramesCLP.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesCLP.setStatus(_A)
_IpadAtmVccStatsRxFramesCI_Type=Integer32
_IpadAtmVccStatsRxFramesCI_Object=MibTableColumn
ipadAtmVccStatsRxFramesCI=_IpadAtmVccStatsRxFramesCI_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,11),_IpadAtmVccStatsRxFramesCI_Type())
ipadAtmVccStatsRxFramesCI.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesCI.setStatus(_A)
_IpadAtmVccStatsRxFramesAbort_Type=Integer32
_IpadAtmVccStatsRxFramesAbort_Object=MibTableColumn
ipadAtmVccStatsRxFramesAbort=_IpadAtmVccStatsRxFramesAbort_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,12),_IpadAtmVccStatsRxFramesAbort_Type())
ipadAtmVccStatsRxFramesAbort.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesAbort.setStatus(_A)
_IpadAtmVccStatsRxFramesLenViolation_Type=Integer32
_IpadAtmVccStatsRxFramesLenViolation_Object=MibTableColumn
ipadAtmVccStatsRxFramesLenViolation=_IpadAtmVccStatsRxFramesLenViolation_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,13),_IpadAtmVccStatsRxFramesLenViolation_Type())
ipadAtmVccStatsRxFramesLenViolation.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesLenViolation.setStatus(_A)
_IpadAtmVccStatsRxFramesCRCError_Type=Integer32
_IpadAtmVccStatsRxFramesCRCError_Object=MibTableColumn
ipadAtmVccStatsRxFramesCRCError=_IpadAtmVccStatsRxFramesCRCError_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,14),_IpadAtmVccStatsRxFramesCRCError_Type())
ipadAtmVccStatsRxFramesCRCError.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesCRCError.setStatus(_A)
_IpadAtmVccStatsRxFramesTimeout_Type=Integer32
_IpadAtmVccStatsRxFramesTimeout_Object=MibTableColumn
ipadAtmVccStatsRxFramesTimeout=_IpadAtmVccStatsRxFramesTimeout_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,15),_IpadAtmVccStatsRxFramesTimeout_Type())
ipadAtmVccStatsRxFramesTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesTimeout.setStatus(_A)
_IpadAtmVccStatsRxFramesHCSError_Type=Integer32
_IpadAtmVccStatsRxFramesHCSError_Object=MibTableColumn
ipadAtmVccStatsRxFramesHCSError=_IpadAtmVccStatsRxFramesHCSError_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,16),_IpadAtmVccStatsRxFramesHCSError_Type())
ipadAtmVccStatsRxFramesHCSError.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesHCSError.setStatus(_A)
_IpadAtmVccStatsRxFramesNoBuffer_Type=Integer32
_IpadAtmVccStatsRxFramesNoBuffer_Object=MibTableColumn
ipadAtmVccStatsRxFramesNoBuffer=_IpadAtmVccStatsRxFramesNoBuffer_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,17),_IpadAtmVccStatsRxFramesNoBuffer_Type())
ipadAtmVccStatsRxFramesNoBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxFramesNoBuffer.setStatus(_A)
_IpadAtmVccStatsRxCellsOK_Type=Integer32
_IpadAtmVccStatsRxCellsOK_Object=MibTableColumn
ipadAtmVccStatsRxCellsOK=_IpadAtmVccStatsRxCellsOK_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,18),_IpadAtmVccStatsRxCellsOK_Type())
ipadAtmVccStatsRxCellsOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxCellsOK.setStatus(_A)
_IpadAtmVccStatsTxCellsOK_Type=Integer32
_IpadAtmVccStatsTxCellsOK_Object=MibTableColumn
ipadAtmVccStatsTxCellsOK=_IpadAtmVccStatsTxCellsOK_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,19),_IpadAtmVccStatsTxCellsOK_Type())
ipadAtmVccStatsTxCellsOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsTxCellsOK.setStatus(_A)
_IpadAtmVccStatsRxBytesOK_Type=Integer32
_IpadAtmVccStatsRxBytesOK_Object=MibTableColumn
ipadAtmVccStatsRxBytesOK=_IpadAtmVccStatsRxBytesOK_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,20),_IpadAtmVccStatsRxBytesOK_Type())
ipadAtmVccStatsRxBytesOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRxBytesOK.setStatus(_A)
_IpadAtmVccStatsTxBytesOK_Type=Integer32
_IpadAtmVccStatsTxBytesOK_Object=MibTableColumn
ipadAtmVccStatsTxBytesOK=_IpadAtmVccStatsTxBytesOK_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,21),_IpadAtmVccStatsTxBytesOK_Type())
ipadAtmVccStatsTxBytesOK.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsTxBytesOK.setStatus(_A)
_IpadAtmVccStatsDelayPeak_Type=Integer32
_IpadAtmVccStatsDelayPeak_Object=MibTableColumn
ipadAtmVccStatsDelayPeak=_IpadAtmVccStatsDelayPeak_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,22),_IpadAtmVccStatsDelayPeak_Type())
ipadAtmVccStatsDelayPeak.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsDelayPeak.setStatus(_A)
_IpadAtmVccStatsDelayAverage_Type=Integer32
_IpadAtmVccStatsDelayAverage_Object=MibTableColumn
ipadAtmVccStatsDelayAverage=_IpadAtmVccStatsDelayAverage_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,23),_IpadAtmVccStatsDelayAverage_Type())
ipadAtmVccStatsDelayAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsDelayAverage.setStatus(_A)
_IpadAtmVccStatsRoundTripTimeouts_Type=Integer32
_IpadAtmVccStatsRoundTripTimeouts_Object=MibTableColumn
ipadAtmVccStatsRoundTripTimeouts=_IpadAtmVccStatsRoundTripTimeouts_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,24),_IpadAtmVccStatsRoundTripTimeouts_Type())
ipadAtmVccStatsRoundTripTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRoundTripTimeouts.setStatus(_A)
_IpadAtmVccStatsRemoteFramesOffered_Type=Integer32
_IpadAtmVccStatsRemoteFramesOffered_Object=MibTableColumn
ipadAtmVccStatsRemoteFramesOffered=_IpadAtmVccStatsRemoteFramesOffered_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,25),_IpadAtmVccStatsRemoteFramesOffered_Type())
ipadAtmVccStatsRemoteFramesOffered.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRemoteFramesOffered.setStatus(_A)
_IpadAtmVccStatsFramesReceived_Type=Integer32
_IpadAtmVccStatsFramesReceived_Object=MibTableColumn
ipadAtmVccStatsFramesReceived=_IpadAtmVccStatsFramesReceived_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,26),_IpadAtmVccStatsFramesReceived_Type())
ipadAtmVccStatsFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsFramesReceived.setStatus(_A)
_IpadAtmVccStatsFDR_Type=DisplayString
_IpadAtmVccStatsFDR_Object=MibTableColumn
ipadAtmVccStatsFDR=_IpadAtmVccStatsFDR_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,27),_IpadAtmVccStatsFDR_Type())
ipadAtmVccStatsFDR.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsFDR.setStatus(_A)
_IpadAtmVccStatsRemoteDataOffered_Type=Integer32
_IpadAtmVccStatsRemoteDataOffered_Object=MibTableColumn
ipadAtmVccStatsRemoteDataOffered=_IpadAtmVccStatsRemoteDataOffered_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,28),_IpadAtmVccStatsRemoteDataOffered_Type())
ipadAtmVccStatsRemoteDataOffered.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsRemoteDataOffered.setStatus(_A)
_IpadAtmVccStatsDataReceived_Type=Integer32
_IpadAtmVccStatsDataReceived_Object=MibTableColumn
ipadAtmVccStatsDataReceived=_IpadAtmVccStatsDataReceived_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,29),_IpadAtmVccStatsDataReceived_Type())
ipadAtmVccStatsDataReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsDataReceived.setStatus(_A)
_IpadAtmVccStatsDDR_Type=DisplayString
_IpadAtmVccStatsDDR_Object=MibTableColumn
ipadAtmVccStatsDDR=_IpadAtmVccStatsDDR_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,30),_IpadAtmVccStatsDDR_Type())
ipadAtmVccStatsDDR.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsDDR.setStatus(_A)
_IpadAtmVccStatsUAS_Type=Integer32
_IpadAtmVccStatsUAS_Object=MibTableColumn
ipadAtmVccStatsUAS=_IpadAtmVccStatsUAS_Object((1,3,6,1,4,1,321,100,1,25,4,1,1,31),_IpadAtmVccStatsUAS_Type())
ipadAtmVccStatsUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmVccStatsUAS.setStatus(_A)
_IpadAtmCesParms_ObjectIdentity=ObjectIdentity
ipadAtmCesParms=_IpadAtmCesParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,25,5))
_IpadAtmCesTable_Object=MibTable
ipadAtmCesTable=_IpadAtmCesTable_Object((1,3,6,1,4,1,321,100,1,25,5,1))
if mibBuilder.loadTexts:ipadAtmCesTable.setStatus(_A)
_IpadAtmCesTableEntry_Object=MibTableRow
ipadAtmCesTableEntry=_IpadAtmCesTableEntry_Object((1,3,6,1,4,1,321,100,1,25,5,1,1))
ipadAtmCesTableEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:ipadAtmCesTableEntry.setStatus(_A)
_IpadAtmCesIndex_Type=Integer32
_IpadAtmCesIndex_Object=MibTableColumn
ipadAtmCesIndex=_IpadAtmCesIndex_Object((1,3,6,1,4,1,321,100,1,25,5,1,1,1),_IpadAtmCesIndex_Type())
ipadAtmCesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmCesIndex.setStatus(_A)
class _IpadAtmCesPayloadScrambling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_K,2),(_L,3)))
_IpadAtmCesPayloadScrambling_Type.__name__=_C
_IpadAtmCesPayloadScrambling_Object=MibTableColumn
ipadAtmCesPayloadScrambling=_IpadAtmCesPayloadScrambling_Object((1,3,6,1,4,1,321,100,1,25,5,1,1,2),_IpadAtmCesPayloadScrambling_Type())
ipadAtmCesPayloadScrambling.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmCesPayloadScrambling.setStatus(_A)
class _IpadAtmCesAutoChannelConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_K,2),(_L,3)))
_IpadAtmCesAutoChannelConfiguration_Type.__name__=_C
_IpadAtmCesAutoChannelConfiguration_Object=MibTableColumn
ipadAtmCesAutoChannelConfiguration=_IpadAtmCesAutoChannelConfiguration_Object((1,3,6,1,4,1,321,100,1,25,5,1,1,3),_IpadAtmCesAutoChannelConfiguration_Type())
ipadAtmCesAutoChannelConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmCesAutoChannelConfiguration.setStatus(_A)
_IpadAtmFrParms_ObjectIdentity=ObjectIdentity
ipadAtmFrParms=_IpadAtmFrParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,25,6))
_IpadAtmFrf5SvcTable_Object=MibTable
ipadAtmFrf5SvcTable=_IpadAtmFrf5SvcTable_Object((1,3,6,1,4,1,321,100,1,25,6,1))
if mibBuilder.loadTexts:ipadAtmFrf5SvcTable.setStatus(_A)
_IpadAtmFrf5SvcTableEntry_Object=MibTableRow
ipadAtmFrf5SvcTableEntry=_IpadAtmFrf5SvcTableEntry_Object((1,3,6,1,4,1,321,100,1,25,6,1,1))
ipadAtmFrf5SvcTableEntry.setIndexNames((0,_E,_e),(0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:ipadAtmFrf5SvcTableEntry.setStatus(_A)
_IpadAtmFrf5SvcIfIndex_Type=Integer32
_IpadAtmFrf5SvcIfIndex_Object=MibTableColumn
ipadAtmFrf5SvcIfIndex=_IpadAtmFrf5SvcIfIndex_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,1),_IpadAtmFrf5SvcIfIndex_Type())
ipadAtmFrf5SvcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5SvcIfIndex.setStatus(_A)
_IpadAtmFrf5SvcVpiIndex_Type=Integer32
_IpadAtmFrf5SvcVpiIndex_Object=MibTableColumn
ipadAtmFrf5SvcVpiIndex=_IpadAtmFrf5SvcVpiIndex_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,2),_IpadAtmFrf5SvcVpiIndex_Type())
ipadAtmFrf5SvcVpiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5SvcVpiIndex.setStatus(_A)
_IpadAtmFrf5SvcVciIndex_Type=Integer32
_IpadAtmFrf5SvcVciIndex_Object=MibTableColumn
ipadAtmFrf5SvcVciIndex=_IpadAtmFrf5SvcVciIndex_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,3),_IpadAtmFrf5SvcVciIndex_Type())
ipadAtmFrf5SvcVciIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5SvcVciIndex.setStatus(_A)
class _IpadAtmFrf5SvcDeToClpMappingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_M,2),(_N,3)))
_IpadAtmFrf5SvcDeToClpMappingMode_Type.__name__=_C
_IpadAtmFrf5SvcDeToClpMappingMode_Object=MibTableColumn
ipadAtmFrf5SvcDeToClpMappingMode=_IpadAtmFrf5SvcDeToClpMappingMode_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,4),_IpadAtmFrf5SvcDeToClpMappingMode_Type())
ipadAtmFrf5SvcDeToClpMappingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5SvcDeToClpMappingMode.setStatus(_A)
class _IpadAtmFrf5SvcClpToDeMappingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('mode2',2)))
_IpadAtmFrf5SvcClpToDeMappingMode_Type.__name__=_C
_IpadAtmFrf5SvcClpToDeMappingMode_Object=MibTableColumn
ipadAtmFrf5SvcClpToDeMappingMode=_IpadAtmFrf5SvcClpToDeMappingMode_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,5),_IpadAtmFrf5SvcClpToDeMappingMode_Type())
ipadAtmFrf5SvcClpToDeMappingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5SvcClpToDeMappingMode.setStatus(_A)
class _IpadAtmFrf5SvcN1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpadAtmFrf5SvcN1_Type.__name__=_C
_IpadAtmFrf5SvcN1_Object=MibTableColumn
ipadAtmFrf5SvcN1=_IpadAtmFrf5SvcN1_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,6),_IpadAtmFrf5SvcN1_Type())
ipadAtmFrf5SvcN1.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5SvcN1.setStatus(_A)
class _IpadAtmFrf5SvcN2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_IpadAtmFrf5SvcN2_Type.__name__=_C
_IpadAtmFrf5SvcN2_Object=MibTableColumn
ipadAtmFrf5SvcN2=_IpadAtmFrf5SvcN2_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,7),_IpadAtmFrf5SvcN2_Type())
ipadAtmFrf5SvcN2.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5SvcN2.setStatus(_A)
class _IpadAtmFrf5SvcN3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_IpadAtmFrf5SvcN3_Type.__name__=_C
_IpadAtmFrf5SvcN3_Object=MibTableColumn
ipadAtmFrf5SvcN3=_IpadAtmFrf5SvcN3_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,8),_IpadAtmFrf5SvcN3_Type())
ipadAtmFrf5SvcN3.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5SvcN3.setStatus(_A)
class _IpadAtmFrf5SvcT1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,240))
_IpadAtmFrf5SvcT1_Type.__name__=_C
_IpadAtmFrf5SvcT1_Object=MibTableColumn
ipadAtmFrf5SvcT1=_IpadAtmFrf5SvcT1_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,9),_IpadAtmFrf5SvcT1_Type())
ipadAtmFrf5SvcT1.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5SvcT1.setStatus(_A)
class _IpadAtmFrf5SvcT2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,245))
_IpadAtmFrf5SvcT2_Type.__name__=_C
_IpadAtmFrf5SvcT2_Object=MibTableColumn
ipadAtmFrf5SvcT2=_IpadAtmFrf5SvcT2_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,10),_IpadAtmFrf5SvcT2_Type())
ipadAtmFrf5SvcT2.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5SvcT2.setStatus(_A)
class _IpadAtmFrf5SvcActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('no',2),('yes',3)))
_IpadAtmFrf5SvcActive_Type.__name__=_C
_IpadAtmFrf5SvcActive_Object=MibTableColumn
ipadAtmFrf5SvcActive=_IpadAtmFrf5SvcActive_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,11),_IpadAtmFrf5SvcActive_Type())
ipadAtmFrf5SvcActive.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5SvcActive.setStatus(_A)
_IpadAtmFrf5SvcAddDLCI_Type=Integer32
_IpadAtmFrf5SvcAddDLCI_Object=MibTableColumn
ipadAtmFrf5SvcAddDLCI=_IpadAtmFrf5SvcAddDLCI_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,12),_IpadAtmFrf5SvcAddDLCI_Type())
ipadAtmFrf5SvcAddDLCI.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5SvcAddDLCI.setStatus(_A)
_IpadAtmFrf5SvcDeleteDLCI_Type=Integer32
_IpadAtmFrf5SvcDeleteDLCI_Object=MibTableColumn
ipadAtmFrf5SvcDeleteDLCI=_IpadAtmFrf5SvcDeleteDLCI_Object((1,3,6,1,4,1,321,100,1,25,6,1,1,13),_IpadAtmFrf5SvcDeleteDLCI_Type())
ipadAtmFrf5SvcDeleteDLCI.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5SvcDeleteDLCI.setStatus(_A)
_IpadAtmFrf5DlciTable_Object=MibTable
ipadAtmFrf5DlciTable=_IpadAtmFrf5DlciTable_Object((1,3,6,1,4,1,321,100,1,25,6,2))
if mibBuilder.loadTexts:ipadAtmFrf5DlciTable.setStatus(_A)
_IpadAtmFrf5DlciTableEntry_Object=MibTableRow
ipadAtmFrf5DlciTableEntry=_IpadAtmFrf5DlciTableEntry_Object((1,3,6,1,4,1,321,100,1,25,6,2,1))
ipadAtmFrf5DlciTableEntry.setIndexNames((0,_E,_h),(0,_E,_i),(0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:ipadAtmFrf5DlciTableEntry.setStatus(_A)
_IpadAtmFrf5DlciIfIndex_Type=Integer32
_IpadAtmFrf5DlciIfIndex_Object=MibTableColumn
ipadAtmFrf5DlciIfIndex=_IpadAtmFrf5DlciIfIndex_Object((1,3,6,1,4,1,321,100,1,25,6,2,1,1),_IpadAtmFrf5DlciIfIndex_Type())
ipadAtmFrf5DlciIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5DlciIfIndex.setStatus(_A)
_IpadAtmFrf5DlciVpiIndex_Type=Integer32
_IpadAtmFrf5DlciVpiIndex_Object=MibTableColumn
ipadAtmFrf5DlciVpiIndex=_IpadAtmFrf5DlciVpiIndex_Object((1,3,6,1,4,1,321,100,1,25,6,2,1,2),_IpadAtmFrf5DlciVpiIndex_Type())
ipadAtmFrf5DlciVpiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5DlciVpiIndex.setStatus(_A)
_IpadAtmFrf5DlciVciIndex_Type=Integer32
_IpadAtmFrf5DlciVciIndex_Object=MibTableColumn
ipadAtmFrf5DlciVciIndex=_IpadAtmFrf5DlciVciIndex_Object((1,3,6,1,4,1,321,100,1,25,6,2,1,3),_IpadAtmFrf5DlciVciIndex_Type())
ipadAtmFrf5DlciVciIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5DlciVciIndex.setStatus(_A)
_IpadAtmFrf5DlciIndex_Type=Integer32
_IpadAtmFrf5DlciIndex_Object=MibTableColumn
ipadAtmFrf5DlciIndex=_IpadAtmFrf5DlciIndex_Object((1,3,6,1,4,1,321,100,1,25,6,2,1,4),_IpadAtmFrf5DlciIndex_Type())
ipadAtmFrf5DlciIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5DlciIndex.setStatus(_A)
class _IpadAtmFrf5DlciEndpointName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_IpadAtmFrf5DlciEndpointName_Type.__name__=_J
_IpadAtmFrf5DlciEndpointName_Object=MibTableColumn
ipadAtmFrf5DlciEndpointName=_IpadAtmFrf5DlciEndpointName_Object((1,3,6,1,4,1,321,100,1,25,6,2,1,5),_IpadAtmFrf5DlciEndpointName_Type())
ipadAtmFrf5DlciEndpointName.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf5DlciEndpointName.setStatus(_A)
class _IpadAtmFrf5DlciStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('inactiveLearned',2),(_G,3),('activeLearned',4)))
_IpadAtmFrf5DlciStatus_Type.__name__=_C
_IpadAtmFrf5DlciStatus_Object=MibTableColumn
ipadAtmFrf5DlciStatus=_IpadAtmFrf5DlciStatus_Object((1,3,6,1,4,1,321,100,1,25,6,2,1,6),_IpadAtmFrf5DlciStatus_Type())
ipadAtmFrf5DlciStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5DlciStatus.setStatus(_A)
class _IpadAtmFrf5DlciCongestion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('no',2),('yes',3)))
_IpadAtmFrf5DlciCongestion_Type.__name__=_C
_IpadAtmFrf5DlciCongestion_Object=MibTableColumn
ipadAtmFrf5DlciCongestion=_IpadAtmFrf5DlciCongestion_Object((1,3,6,1,4,1,321,100,1,25,6,2,1,7),_IpadAtmFrf5DlciCongestion_Type())
ipadAtmFrf5DlciCongestion.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf5DlciCongestion.setStatus(_A)
_IpadAtmFrf8SvcTable_Object=MibTable
ipadAtmFrf8SvcTable=_IpadAtmFrf8SvcTable_Object((1,3,6,1,4,1,321,100,1,25,6,3))
if mibBuilder.loadTexts:ipadAtmFrf8SvcTable.setStatus(_A)
_IpadAtmFrf8SvcTableEntry_Object=MibTableRow
ipadAtmFrf8SvcTableEntry=_IpadAtmFrf8SvcTableEntry_Object((1,3,6,1,4,1,321,100,1,25,6,3,1))
ipadAtmFrf8SvcTableEntry.setIndexNames((0,_E,_l),(0,_E,_m),(0,_E,_n))
if mibBuilder.loadTexts:ipadAtmFrf8SvcTableEntry.setStatus(_A)
_IpadAtmFrf8SvcIfIndex_Type=Integer32
_IpadAtmFrf8SvcIfIndex_Object=MibTableColumn
ipadAtmFrf8SvcIfIndex=_IpadAtmFrf8SvcIfIndex_Object((1,3,6,1,4,1,321,100,1,25,6,3,1,1),_IpadAtmFrf8SvcIfIndex_Type())
ipadAtmFrf8SvcIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf8SvcIfIndex.setStatus(_A)
_IpadAtmFrf8SvcVpiIndex_Type=Integer32
_IpadAtmFrf8SvcVpiIndex_Object=MibTableColumn
ipadAtmFrf8SvcVpiIndex=_IpadAtmFrf8SvcVpiIndex_Object((1,3,6,1,4,1,321,100,1,25,6,3,1,2),_IpadAtmFrf8SvcVpiIndex_Type())
ipadAtmFrf8SvcVpiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf8SvcVpiIndex.setStatus(_A)
_IpadAtmFrf8SvcVciIndex_Type=Integer32
_IpadAtmFrf8SvcVciIndex_Object=MibTableColumn
ipadAtmFrf8SvcVciIndex=_IpadAtmFrf8SvcVciIndex_Object((1,3,6,1,4,1,321,100,1,25,6,3,1,3),_IpadAtmFrf8SvcVciIndex_Type())
ipadAtmFrf8SvcVciIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadAtmFrf8SvcVciIndex.setStatus(_A)
class _IpadAtmFrf8SvcDeToClpMappingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_M,2),(_N,3)))
_IpadAtmFrf8SvcDeToClpMappingMode_Type.__name__=_C
_IpadAtmFrf8SvcDeToClpMappingMode_Object=MibTableColumn
ipadAtmFrf8SvcDeToClpMappingMode=_IpadAtmFrf8SvcDeToClpMappingMode_Object((1,3,6,1,4,1,321,100,1,25,6,3,1,4),_IpadAtmFrf8SvcDeToClpMappingMode_Type())
ipadAtmFrf8SvcDeToClpMappingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf8SvcDeToClpMappingMode.setStatus(_A)
class _IpadAtmFrf8SvcClpToDeMappingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_M,2),(_N,3)))
_IpadAtmFrf8SvcClpToDeMappingMode_Type.__name__=_C
_IpadAtmFrf8SvcClpToDeMappingMode_Object=MibTableColumn
ipadAtmFrf8SvcClpToDeMappingMode=_IpadAtmFrf8SvcClpToDeMappingMode_Object((1,3,6,1,4,1,321,100,1,25,6,3,1,5),_IpadAtmFrf8SvcClpToDeMappingMode_Type())
ipadAtmFrf8SvcClpToDeMappingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf8SvcClpToDeMappingMode.setStatus(_A)
class _IpadAtmFrf8SvcCongestionMappingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('mode2',2)))
_IpadAtmFrf8SvcCongestionMappingMode_Type.__name__=_C
_IpadAtmFrf8SvcCongestionMappingMode_Object=MibTableColumn
ipadAtmFrf8SvcCongestionMappingMode=_IpadAtmFrf8SvcCongestionMappingMode_Object((1,3,6,1,4,1,321,100,1,25,6,3,1,6),_IpadAtmFrf8SvcCongestionMappingMode_Type())
ipadAtmFrf8SvcCongestionMappingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf8SvcCongestionMappingMode.setStatus(_A)
class _IpadAtmFrf8SvcEncapsulationMappingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('transparentMode',1),('translationMode',2)))
_IpadAtmFrf8SvcEncapsulationMappingMode_Type.__name__=_C
_IpadAtmFrf8SvcEncapsulationMappingMode_Object=MibTableColumn
ipadAtmFrf8SvcEncapsulationMappingMode=_IpadAtmFrf8SvcEncapsulationMappingMode_Object((1,3,6,1,4,1,321,100,1,25,6,3,1,7),_IpadAtmFrf8SvcEncapsulationMappingMode_Type())
ipadAtmFrf8SvcEncapsulationMappingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf8SvcEncapsulationMappingMode.setStatus(_A)
class _IpadAtmFrf8SvcEndpointName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_IpadAtmFrf8SvcEndpointName_Type.__name__=_J
_IpadAtmFrf8SvcEndpointName_Object=MibTableColumn
ipadAtmFrf8SvcEndpointName=_IpadAtmFrf8SvcEndpointName_Object((1,3,6,1,4,1,321,100,1,25,6,3,1,8),_IpadAtmFrf8SvcEndpointName_Type())
ipadAtmFrf8SvcEndpointName.setMaxAccess(_D)
if mibBuilder.loadTexts:ipadAtmFrf8SvcEndpointName.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ipadAtm':ipadAtm,'ipadAtmParms':ipadAtmParms,'ipadAtmTable':ipadAtmTable,'ipadAtmTableEntry':ipadAtmTableEntry,_O:ipadAtmIfIndex,'ipadAtmOperStatus':ipadAtmOperStatus,'ipadAtmVccsOpenedOK':ipadAtmVccsOpenedOK,'ipadAtmVccsNotOpened':ipadAtmVccsNotOpened,'ipadAtmAlarmReset':ipadAtmAlarmReset,'ipadAtmOverSubscriptionFactor':ipadAtmOverSubscriptionFactor,'ipadAtmLineBandwidth':ipadAtmLineBandwidth,'ipadAtmAAL5Bandwidth':ipadAtmAAL5Bandwidth,'ipadAtmOverSubBandwidth':ipadAtmOverSubBandwidth,'ipadAtmCbrUsedBandwidth':ipadAtmCbrUsedBandwidth,'ipadAtmVbrUsedBandwidth':ipadAtmVbrUsedBandwidth,'ipadAtmUbrUsedBandwidth':ipadAtmUbrUsedBandwidth,'ipadAtmQos0Pcr':ipadAtmQos0Pcr,'ipadAtmStatsParms':ipadAtmStatsParms,'ipadAtmStatsTable':ipadAtmStatsTable,'ipadAtmStatsTableEntry':ipadAtmStatsTableEntry,_R:ipadAtmStatsIndex,_S:ipadAtmStatsPeriodIndex,'ipadAtmStatsTimeStamp':ipadAtmStatsTimeStamp,'ipadAtmStatsRxFramesOK':ipadAtmStatsRxFramesOK,'ipadAtmStatsTxFramesOK':ipadAtmStatsTxFramesOK,'ipadAtmStatsRxFramesError':ipadAtmStatsRxFramesError,'ipadAtmStatsTxFramesError':ipadAtmStatsTxFramesError,'ipadAtmStatsRxBytesOK':ipadAtmStatsRxBytesOK,'ipadAtmStatsTxBytesOK':ipadAtmStatsTxBytesOK,'ipadAtmStatsLostSync':ipadAtmStatsLostSync,'ipadAtmStatsOamCellsRx':ipadAtmStatsOamCellsRx,'ipadAtmStatsOamCellsTx':ipadAtmStatsOamCellsTx,'ipadAtmVccParms':ipadAtmVccParms,'ipadAtmVccTable':ipadAtmVccTable,'ipadAtmVccTableEntry':ipadAtmVccTableEntry,_T:ipadAtmVccIndex,_U:ipadAtmVccVpiIndex,_V:ipadAtmVccVciIndex,'ipadAtmVccEncapsulationType':ipadAtmVccEncapsulationType,'ipadAtmVccTrafficType':ipadAtmVccTrafficType,'ipadAtmVccChannelRate':ipadAtmVccChannelRate,'ipadAtmVccAlarmReset':ipadAtmVccAlarmReset,'ipadAtmVccSLATimer':ipadAtmVccSLATimer,'ipadAtmVccRemoteFramesOffered':ipadAtmVccRemoteFramesOffered,'ipadAtmVccFramesReceived':ipadAtmVccFramesReceived,'ipadAtmVccRemoteDataOffered':ipadAtmVccRemoteDataOffered,'ipadAtmVccDataReceived':ipadAtmVccDataReceived,'ipadAtmVccRemoteActive':ipadAtmVccRemoteActive,'ipadAtmVccRemoteVpi':ipadAtmVccRemoteVpi,'ipadAtmVccRemoteVci':ipadAtmVccRemoteVci,'ipadAtmVccRemoteIPAddress':ipadAtmVccRemoteIPAddress,'ipadAtmVccRemoteUnitId':ipadAtmVccRemoteUnitId,'ipadAtmVccEtoeLoopbackCommand':ipadAtmVccEtoeLoopbackCommand,'ipadAtmVccEtoeLoopbackState':ipadAtmVccEtoeLoopbackState,'ipadAtmVccEtoeLoopbackCellsTx':ipadAtmVccEtoeLoopbackCellsTx,'ipadAtmVccEtoeLoopbackCellsRx':ipadAtmVccEtoeLoopbackCellsRx,'ipadAtmVccEtoeLoopbackRttMin':ipadAtmVccEtoeLoopbackRttMin,'ipadAtmVccEtoeLoopbackRttMax':ipadAtmVccEtoeLoopbackRttMax,'ipadAtmVccEtoeLoopbackRttAvg':ipadAtmVccEtoeLoopbackRttAvg,'ipadAtmVccSegLoopbackCommand':ipadAtmVccSegLoopbackCommand,'ipadAtmVccSegLoopbackState':ipadAtmVccSegLoopbackState,'ipadAtmVccSegLoopbackCellsTx':ipadAtmVccSegLoopbackCellsTx,'ipadAtmVccSegLoopbackCellsRx':ipadAtmVccSegLoopbackCellsRx,'ipadAtmVccSegLoopbackRttMin':ipadAtmVccSegLoopbackRttMin,'ipadAtmVccSegLoopbackRttMax':ipadAtmVccSegLoopbackRttMax,'ipadAtmVccSegLoopbackRttAvg':ipadAtmVccSegLoopbackRttAvg,'ipadAtmVccEtoeContCheckCommand':ipadAtmVccEtoeContCheckCommand,'ipadAtmVccEtoeContCheckAutoActivate':ipadAtmVccEtoeContCheckAutoActivate,'ipadAtmVccEtoeContCheckType':ipadAtmVccEtoeContCheckType,'ipadAtmVccEtoeContCheckTypeInUse':ipadAtmVccEtoeContCheckTypeInUse,'ipadAtmVccEtoeContCheckStatus':ipadAtmVccEtoeContCheckStatus,'ipadAtmVccEtoeContCheckCellsTx':ipadAtmVccEtoeContCheckCellsTx,'ipadAtmVccEtoeContCheckCellsRx':ipadAtmVccEtoeContCheckCellsRx,'ipadAtmVccEtoeAisStatus':ipadAtmVccEtoeAisStatus,'ipadAtmVccEtoeRdiStatus':ipadAtmVccEtoeRdiStatus,'ipadAtmVccStatsParms':ipadAtmVccStatsParms,'ipadAtmVccStatsTable':ipadAtmVccStatsTable,'ipadAtmVccStatsTableEntry':ipadAtmVccStatsTableEntry,_Z:ipadAtmVccStatsIndex,_a:ipadAtmVccStatsVpiIndex,_b:ipadAtmVccStatsVciIndex,_c:ipadAtmVccStatsPeriodIndex,'ipadAtmVccStatsTimeStamp':ipadAtmVccStatsTimeStamp,'ipadAtmVccStatsRxFramesOK':ipadAtmVccStatsRxFramesOK,'ipadAtmVccStatsTxFramesOK':ipadAtmVccStatsTxFramesOK,'ipadAtmVccStatsRxFramesError':ipadAtmVccStatsRxFramesError,'ipadAtmVccStatsTxFramesError':ipadAtmVccStatsTxFramesError,'ipadAtmVccStatsRxFramesCLP':ipadAtmVccStatsRxFramesCLP,'ipadAtmVccStatsRxFramesCI':ipadAtmVccStatsRxFramesCI,'ipadAtmVccStatsRxFramesAbort':ipadAtmVccStatsRxFramesAbort,'ipadAtmVccStatsRxFramesLenViolation':ipadAtmVccStatsRxFramesLenViolation,'ipadAtmVccStatsRxFramesCRCError':ipadAtmVccStatsRxFramesCRCError,'ipadAtmVccStatsRxFramesTimeout':ipadAtmVccStatsRxFramesTimeout,'ipadAtmVccStatsRxFramesHCSError':ipadAtmVccStatsRxFramesHCSError,'ipadAtmVccStatsRxFramesNoBuffer':ipadAtmVccStatsRxFramesNoBuffer,'ipadAtmVccStatsRxCellsOK':ipadAtmVccStatsRxCellsOK,'ipadAtmVccStatsTxCellsOK':ipadAtmVccStatsTxCellsOK,'ipadAtmVccStatsRxBytesOK':ipadAtmVccStatsRxBytesOK,'ipadAtmVccStatsTxBytesOK':ipadAtmVccStatsTxBytesOK,'ipadAtmVccStatsDelayPeak':ipadAtmVccStatsDelayPeak,'ipadAtmVccStatsDelayAverage':ipadAtmVccStatsDelayAverage,'ipadAtmVccStatsRoundTripTimeouts':ipadAtmVccStatsRoundTripTimeouts,'ipadAtmVccStatsRemoteFramesOffered':ipadAtmVccStatsRemoteFramesOffered,'ipadAtmVccStatsFramesReceived':ipadAtmVccStatsFramesReceived,'ipadAtmVccStatsFDR':ipadAtmVccStatsFDR,'ipadAtmVccStatsRemoteDataOffered':ipadAtmVccStatsRemoteDataOffered,'ipadAtmVccStatsDataReceived':ipadAtmVccStatsDataReceived,'ipadAtmVccStatsDDR':ipadAtmVccStatsDDR,'ipadAtmVccStatsUAS':ipadAtmVccStatsUAS,'ipadAtmCesParms':ipadAtmCesParms,'ipadAtmCesTable':ipadAtmCesTable,'ipadAtmCesTableEntry':ipadAtmCesTableEntry,_d:ipadAtmCesIndex,'ipadAtmCesPayloadScrambling':ipadAtmCesPayloadScrambling,'ipadAtmCesAutoChannelConfiguration':ipadAtmCesAutoChannelConfiguration,'ipadAtmFrParms':ipadAtmFrParms,'ipadAtmFrf5SvcTable':ipadAtmFrf5SvcTable,'ipadAtmFrf5SvcTableEntry':ipadAtmFrf5SvcTableEntry,_e:ipadAtmFrf5SvcIfIndex,_f:ipadAtmFrf5SvcVpiIndex,_g:ipadAtmFrf5SvcVciIndex,'ipadAtmFrf5SvcDeToClpMappingMode':ipadAtmFrf5SvcDeToClpMappingMode,'ipadAtmFrf5SvcClpToDeMappingMode':ipadAtmFrf5SvcClpToDeMappingMode,'ipadAtmFrf5SvcN1':ipadAtmFrf5SvcN1,'ipadAtmFrf5SvcN2':ipadAtmFrf5SvcN2,'ipadAtmFrf5SvcN3':ipadAtmFrf5SvcN3,'ipadAtmFrf5SvcT1':ipadAtmFrf5SvcT1,'ipadAtmFrf5SvcT2':ipadAtmFrf5SvcT2,'ipadAtmFrf5SvcActive':ipadAtmFrf5SvcActive,'ipadAtmFrf5SvcAddDLCI':ipadAtmFrf5SvcAddDLCI,'ipadAtmFrf5SvcDeleteDLCI':ipadAtmFrf5SvcDeleteDLCI,'ipadAtmFrf5DlciTable':ipadAtmFrf5DlciTable,'ipadAtmFrf5DlciTableEntry':ipadAtmFrf5DlciTableEntry,_h:ipadAtmFrf5DlciIfIndex,_i:ipadAtmFrf5DlciVpiIndex,_j:ipadAtmFrf5DlciVciIndex,_k:ipadAtmFrf5DlciIndex,'ipadAtmFrf5DlciEndpointName':ipadAtmFrf5DlciEndpointName,'ipadAtmFrf5DlciStatus':ipadAtmFrf5DlciStatus,'ipadAtmFrf5DlciCongestion':ipadAtmFrf5DlciCongestion,'ipadAtmFrf8SvcTable':ipadAtmFrf8SvcTable,'ipadAtmFrf8SvcTableEntry':ipadAtmFrf8SvcTableEntry,_l:ipadAtmFrf8SvcIfIndex,_m:ipadAtmFrf8SvcVpiIndex,_n:ipadAtmFrf8SvcVciIndex,'ipadAtmFrf8SvcDeToClpMappingMode':ipadAtmFrf8SvcDeToClpMappingMode,'ipadAtmFrf8SvcClpToDeMappingMode':ipadAtmFrf8SvcClpToDeMappingMode,'ipadAtmFrf8SvcCongestionMappingMode':ipadAtmFrf8SvcCongestionMappingMode,'ipadAtmFrf8SvcEncapsulationMappingMode':ipadAtmFrf8SvcEncapsulationMappingMode,'ipadAtmFrf8SvcEndpointName':ipadAtmFrf8SvcEndpointName})