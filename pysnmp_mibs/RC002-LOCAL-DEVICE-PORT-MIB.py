_AG='rcftSimpleModuleStatus'
_AF='rcftDS1PortFaultPassIndicator'
_AE='rcftSHDSLPortESThreshold'
_AD='rcftSHDSLPortLOLKThreshold'
_AC='rcftSHDSLPortLOSWThreshold'
_AB='rcftSHDSLPortLOSThreshold'
_AA='rcftSHDSLPortAttenuationThreshold'
_A9='rcftSHDSLPortSNRThreshold'
_A8='rcftEthFePortStatus'
_A7='rcftSlotVCGStatisticEntry'
_A6='rcftDS1StatisticEntry'
_A5='rcftDS3E3StatisticEntry'
_A4='rcftEthFeStatisticEntry'
_A3='rcftEthFxStatisticEntry'
_A2='rcftSlotVLANIndex'
_A1='rcftSlotVCGIndex'
_A0='rcftPortIndex'
_z='rcftSimpleModuleIndex'
_y='rcftDataPortIndex'
_x='rcftVideoPortIndex'
_w='rcftDS1PortIndex'
_v='rcftDS3E3PortIndex'
_u='rcftAudioPortIndex'
_t='rcftSHDSLPortIntervalDayNumber'
_s='rcftSHDSLPortIntervalNumber'
_r='rcftV35PortIndex'
_q='rcftE1PortIndex'
_p='rcftPdhPortIndex'
_o='rcftEthFePortIndex'
_n='unknown-type'
_m='optical-S15'
_l='optical-SS35'
_k='optical-SS34'
_j='optical-SS25'
_i='optical-SS23'
_h='optical-SS15'
_g='optical-SS13'
_f='optical-S3'
_e='optical-S2'
_d='optical-S1'
_c='optical-M'
_b='unkkown'
_a='rcftEthFxPortIndex'
_Z='rcftE1PortErrorRate'
_Y='rcftEthFxPortSFPInfo'
_X='rcftSlotVCGMemberAlarmStatus'
_W='rcftVideoPortStatus'
_V='rcftSlotToRVCGMemberAlarmStatus'
_U='rcftSHDSLPortAlarmStatus'
_T='rcftSHDSLPortIndex'
_S='rcftEthFxPortStatus'
_R='rcftE1PortAlarmStatus'
_Q='rcftSlotVCGAlarmStatus'
_P='rcfT1PortAlarmStatus'
_O='rcftPdhPortAlarmStatus'
_N='rcftEthFxPortSFPDiagnoWarningStatus'
_M='rcftEthFxPortSFPDiagnoAlarmStatus'
_L='Integer32'
_K='OctetString'
_J='rcftDS1PortAlarmStatus'
_I='rcftV35PortAlarmStatus'
_H='rcftDS3E3PortAlarmStatus'
_G='rcftSlotIndex'
_F='rcftChassisIndex'
_E='RAISECOM-RCFT-MIB'
_D='read-write'
_C='RC002-LOCAL-DEVICE-PORT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rcftChassisIndex,rcftMibObjects,rcftSlotIndex,rcftSlotStat=mibBuilder.importSymbols(_E,_F,'rcftMibObjects',_G,'rcftSlotStat')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
rcftSlotPortMib=ModuleIdentity((1,3,6,1,4,1,8886,2,1,5,10))
if mibBuilder.loadTexts:rcftSlotPortMib.setRevisions(('1909-01-19 00:00','1909-03-17 00:00','1909-05-14 00:00','1909-05-15 00:00','1909-05-19 00:00','1909-05-26 00:00','1909-05-27 16:00','1909-06-09 16:00','1909-06-17 16:00','1909-07-02 16:00','1909-07-17 16:00','1909-08-28 00:00','1909-09-09 00:00','1909-09-18 00:00','1909-09-27 00:00','1909-10-30 09:48','1909-12-21 14:18','1909-12-21 00:00','1912-01-10 14:31'))
_RcftEthPortMib_ObjectIdentity=ObjectIdentity
rcftEthPortMib=_RcftEthPortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,1))
_RcftEthFxPortMib_ObjectIdentity=ObjectIdentity
rcftEthFxPortMib=_RcftEthFxPortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,1,1))
_RcftEthFxPortObjects_ObjectIdentity=ObjectIdentity
rcftEthFxPortObjects=_RcftEthFxPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,1,1,1))
_RcftEthFxPortTable_Object=MibTable
rcftEthFxPortTable=_RcftEthFxPortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1))
if mibBuilder.loadTexts:rcftEthFxPortTable.setStatus(_A)
_RcftEthFxPortEntry_Object=MibTableRow
rcftEthFxPortEntry=_RcftEthFxPortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1))
rcftEthFxPortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_a))
if mibBuilder.loadTexts:rcftEthFxPortEntry.setStatus(_A)
_RcftEthFxPortIndex_Type=Integer32
_RcftEthFxPortIndex_Object=MibTableColumn
rcftEthFxPortIndex=_RcftEthFxPortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,1),_RcftEthFxPortIndex_Type())
rcftEthFxPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortIndex.setStatus(_A)
_RcftEthFxPortStatus_Type=Integer32
_RcftEthFxPortStatus_Object=MibTableColumn
rcftEthFxPortStatus=_RcftEthFxPortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,2),_RcftEthFxPortStatus_Type())
rcftEthFxPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFxPortStatus.setStatus(_A)
class _RcftEthFxPortModuleMaxSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('stm16',1),('stm8',2),('stm4',3),('stm1',4)))
_RcftEthFxPortModuleMaxSpeed_Type.__name__=_L
_RcftEthFxPortModuleMaxSpeed_Object=MibTableColumn
rcftEthFxPortModuleMaxSpeed=_RcftEthFxPortModuleMaxSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,3),_RcftEthFxPortModuleMaxSpeed_Type())
rcftEthFxPortModuleMaxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortModuleMaxSpeed.setStatus(_A)
class _RcftEthFxPortConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_b,1),('rj45',2),('sc',3),('style1',4),('style2',5),('bnctnc',6),('coaheader',7),('jack',8),('lc',9),('mtrj',10),('mu',11),('sg',12),('opticalpigtail',13),('hssdc2',14),('copperpigtail',15)))
_RcftEthFxPortConnectorType_Type.__name__=_L
_RcftEthFxPortConnectorType_Object=MibTableColumn
rcftEthFxPortConnectorType=_RcftEthFxPortConnectorType_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,4),_RcftEthFxPortConnectorType_Type())
rcftEthFxPortConnectorType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortConnectorType.setStatus(_A)
class _RcftEthFxPortTransmitMedia_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,15)));namedValues=NamedValues(*((_b,1),('singleMode9um',2),('multiMode50um',3),('multiMode62point5um',4),('copperline',15)))
_RcftEthFxPortTransmitMedia_Type.__name__=_L
_RcftEthFxPortTransmitMedia_Object=MibTableColumn
rcftEthFxPortTransmitMedia=_RcftEthFxPortTransmitMedia_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,5),_RcftEthFxPortTransmitMedia_Type())
rcftEthFxPortTransmitMedia.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortTransmitMedia.setStatus(_A)
_RcftEthFxPortModuleWaveLen_Type=Integer32
_RcftEthFxPortModuleWaveLen_Object=MibTableColumn
rcftEthFxPortModuleWaveLen=_RcftEthFxPortModuleWaveLen_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,6),_RcftEthFxPortModuleWaveLen_Type())
rcftEthFxPortModuleWaveLen.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortModuleWaveLen.setStatus(_A)
class _RcftEthFxPortModuleManufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftEthFxPortModuleManufacturer_Type.__name__=_K
_RcftEthFxPortModuleManufacturer_Object=MibTableColumn
rcftEthFxPortModuleManufacturer=_RcftEthFxPortModuleManufacturer_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,7),_RcftEthFxPortModuleManufacturer_Type())
rcftEthFxPortModuleManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortModuleManufacturer.setStatus(_A)
class _RcftEthFxPortModuleDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftEthFxPortModuleDescr_Type.__name__=_K
_RcftEthFxPortModuleDescr_Object=MibTableColumn
rcftEthFxPortModuleDescr=_RcftEthFxPortModuleDescr_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,8),_RcftEthFxPortModuleDescr_Type())
rcftEthFxPortModuleDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortModuleDescr.setStatus(_A)
class _RcftEthFxPortModuleVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_RcftEthFxPortModuleVersion_Type.__name__=_K
_RcftEthFxPortModuleVersion_Object=MibTableColumn
rcftEthFxPortModuleVersion=_RcftEthFxPortModuleVersion_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,9),_RcftEthFxPortModuleVersion_Type())
rcftEthFxPortModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortModuleVersion.setStatus(_A)
class _RcftEthFxPortModuleSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_RcftEthFxPortModuleSerialNumber_Type.__name__=_K
_RcftEthFxPortModuleSerialNumber_Object=MibTableColumn
rcftEthFxPortModuleSerialNumber=_RcftEthFxPortModuleSerialNumber_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,10),_RcftEthFxPortModuleSerialNumber_Type())
rcftEthFxPortModuleSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortModuleSerialNumber.setStatus(_A)
class _RcftEthFxPortModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,12,15,100)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7),(_j,8),(_k,9),(_l,10),(_m,12),('optical_SFP',15),(_n,100)))
_RcftEthFxPortModuleType_Type.__name__=_L
_RcftEthFxPortModuleType_Object=MibTableColumn
rcftEthFxPortModuleType=_RcftEthFxPortModuleType_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,11),_RcftEthFxPortModuleType_Type())
rcftEthFxPortModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortModuleType.setStatus(_A)
_RcftEthFxPortRxRestrictSpeed_Type=Integer32
_RcftEthFxPortRxRestrictSpeed_Object=MibTableColumn
rcftEthFxPortRxRestrictSpeed=_RcftEthFxPortRxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,12),_RcftEthFxPortRxRestrictSpeed_Type())
rcftEthFxPortRxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFxPortRxRestrictSpeed.setStatus(_A)
_RcftEthFxPortTxRestrictSpeed_Type=Integer32
_RcftEthFxPortTxRestrictSpeed_Object=MibTableColumn
rcftEthFxPortTxRestrictSpeed=_RcftEthFxPortTxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,13),_RcftEthFxPortTxRestrictSpeed_Type())
rcftEthFxPortTxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFxPortTxRestrictSpeed.setStatus(_A)
_RcftEthFxPortRestrictSpeedStep_Type=Integer32
_RcftEthFxPortRestrictSpeedStep_Object=MibTableColumn
rcftEthFxPortRestrictSpeedStep=_RcftEthFxPortRestrictSpeedStep_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,14),_RcftEthFxPortRestrictSpeedStep_Type())
rcftEthFxPortRestrictSpeedStep.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortRestrictSpeedStep.setStatus(_A)
class _RcftEthFxPortLoopOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ethFxinsideLoopEnable',1),('ethFxinsideLoopDisable',2),('ethFxLoopbackTest',3)))
_RcftEthFxPortLoopOrder_Type.__name__=_L
_RcftEthFxPortLoopOrder_Object=MibTableColumn
rcftEthFxPortLoopOrder=_RcftEthFxPortLoopOrder_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,15),_RcftEthFxPortLoopOrder_Type())
rcftEthFxPortLoopOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFxPortLoopOrder.setStatus(_A)
class _RcftEthFxPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,100)));namedValues=NamedValues(*(('ethFxPortoutsideLoop',1),('ethFxPortnormal',100)))
_RcftEthFxPortLoopStatus_Type.__name__=_L
_RcftEthFxPortLoopStatus_Object=MibTableColumn
rcftEthFxPortLoopStatus=_RcftEthFxPortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,16),_RcftEthFxPortLoopStatus_Type())
rcftEthFxPortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortLoopStatus.setStatus(_A)
_RcftEthFxPortSFPDiagnoInfo_Type=Integer32
_RcftEthFxPortSFPDiagnoInfo_Object=MibTableColumn
rcftEthFxPortSFPDiagnoInfo=_RcftEthFxPortSFPDiagnoInfo_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,17),_RcftEthFxPortSFPDiagnoInfo_Type())
rcftEthFxPortSFPDiagnoInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortSFPDiagnoInfo.setStatus(_A)
_RcftEthFxPortSFPDiagnoAlarmStatus_Type=Integer32
_RcftEthFxPortSFPDiagnoAlarmStatus_Object=MibTableColumn
rcftEthFxPortSFPDiagnoAlarmStatus=_RcftEthFxPortSFPDiagnoAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,18),_RcftEthFxPortSFPDiagnoAlarmStatus_Type())
rcftEthFxPortSFPDiagnoAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortSFPDiagnoAlarmStatus.setStatus(_A)
_RcftEthFxPortSFPDiagnoWarningStatus_Type=Integer32
_RcftEthFxPortSFPDiagnoWarningStatus_Object=MibTableColumn
rcftEthFxPortSFPDiagnoWarningStatus=_RcftEthFxPortSFPDiagnoWarningStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,19),_RcftEthFxPortSFPDiagnoWarningStatus_Type())
rcftEthFxPortSFPDiagnoWarningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortSFPDiagnoWarningStatus.setStatus(_A)
_RcftEthFxPortTranDistance_Type=Integer32
_RcftEthFxPortTranDistance_Object=MibTableColumn
rcftEthFxPortTranDistance=_RcftEthFxPortTranDistance_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,20),_RcftEthFxPortTranDistance_Type())
rcftEthFxPortTranDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortTranDistance.setStatus(_A)
class _RcftEthFxPortSFPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('utp',1),('fiber',2)))
_RcftEthFxPortSFPType_Type.__name__=_L
_RcftEthFxPortSFPType_Object=MibTableColumn
rcftEthFxPortSFPType=_RcftEthFxPortSFPType_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,21),_RcftEthFxPortSFPType_Type())
rcftEthFxPortSFPType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortSFPType.setStatus(_A)
_RcftEthFxPortSFPInfo_Type=Integer32
_RcftEthFxPortSFPInfo_Object=MibTableColumn
rcftEthFxPortSFPInfo=_RcftEthFxPortSFPInfo_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,22),_RcftEthFxPortSFPInfo_Type())
rcftEthFxPortSFPInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxPortSFPInfo.setStatus(_A)
_RcftEthFxPortPVID_Type=Integer32
_RcftEthFxPortPVID_Object=MibTableColumn
rcftEthFxPortPVID=_RcftEthFxPortPVID_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,23),_RcftEthFxPortPVID_Type())
rcftEthFxPortPVID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFxPortPVID.setStatus(_A)
_RcftEthFxPorttag_Type=Integer32
_RcftEthFxPorttag_Object=MibTableColumn
rcftEthFxPorttag=_RcftEthFxPorttag_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,24),_RcftEthFxPorttag_Type())
rcftEthFxPorttag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFxPorttag.setStatus(_A)
_RcftEthFxPortCOS_Type=Integer32
_RcftEthFxPortCOS_Object=MibTableColumn
rcftEthFxPortCOS=_RcftEthFxPortCOS_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,1,1,1,25),_RcftEthFxPortCOS_Type())
rcftEthFxPortCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFxPortCOS.setStatus(_A)
_RcftEthFxPortPerformance_ObjectIdentity=ObjectIdentity
rcftEthFxPortPerformance=_RcftEthFxPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,1,1,2))
_RcftEthFxStatisticTable_Object=MibTable
rcftEthFxStatisticTable=_RcftEthFxStatisticTable_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1))
if mibBuilder.loadTexts:rcftEthFxStatisticTable.setStatus(_A)
_RcftEthFxStatisticEntry_Object=MibTableRow
rcftEthFxStatisticEntry=_RcftEthFxStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1))
if mibBuilder.loadTexts:rcftEthFxStatisticEntry.setStatus(_A)
_RcftEthFxTxPackets_Type=Counter32
_RcftEthFxTxPackets_Object=MibTableColumn
rcftEthFxTxPackets=_RcftEthFxTxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1,1),_RcftEthFxTxPackets_Type())
rcftEthFxTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxTxPackets.setStatus(_A)
_RcftEthFxRxPackets_Type=Counter32
_RcftEthFxRxPackets_Object=MibTableColumn
rcftEthFxRxPackets=_RcftEthFxRxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1,2),_RcftEthFxRxPackets_Type())
rcftEthFxRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxRxPackets.setStatus(_A)
_RcftEthFxTxErrPackets_Type=Counter32
_RcftEthFxTxErrPackets_Object=MibTableColumn
rcftEthFxTxErrPackets=_RcftEthFxTxErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1,3),_RcftEthFxTxErrPackets_Type())
rcftEthFxTxErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxTxErrPackets.setStatus(_A)
_RcftEthFxRxErrPackets_Type=Counter32
_RcftEthFxRxErrPackets_Object=MibTableColumn
rcftEthFxRxErrPackets=_RcftEthFxRxErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1,4),_RcftEthFxRxErrPackets_Type())
rcftEthFxRxErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxRxErrPackets.setStatus(_A)
_RcftEthFxFluxTimer_Type=Counter32
_RcftEthFxFluxTimer_Object=MibTableColumn
rcftEthFxFluxTimer=_RcftEthFxFluxTimer_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1,5),_RcftEthFxFluxTimer_Type())
rcftEthFxFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxFluxTimer.setStatus(_A)
_RcftEthFxRxBytes_Type=Counter32
_RcftEthFxRxBytes_Object=MibTableColumn
rcftEthFxRxBytes=_RcftEthFxRxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1,6),_RcftEthFxRxBytes_Type())
rcftEthFxRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxRxBytes.setStatus(_A)
_RcftEthFxTxBytes_Type=Counter32
_RcftEthFxTxBytes_Object=MibTableColumn
rcftEthFxTxBytes=_RcftEthFxTxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1,7),_RcftEthFxTxBytes_Type())
rcftEthFxTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFxTxBytes.setStatus(_A)
_RcftEthFx64RxBytes_Type=Counter64
_RcftEthFx64RxBytes_Object=MibTableColumn
rcftEthFx64RxBytes=_RcftEthFx64RxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1,8),_RcftEthFx64RxBytes_Type())
rcftEthFx64RxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFx64RxBytes.setStatus(_A)
_RcftEthFx64TxBytes_Type=Counter64
_RcftEthFx64TxBytes_Object=MibTableColumn
rcftEthFx64TxBytes=_RcftEthFx64TxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,1,1,2,1,1,9),_RcftEthFx64TxBytes_Type())
rcftEthFx64TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFx64TxBytes.setStatus(_A)
_RcftEthFxPortTraps_ObjectIdentity=ObjectIdentity
rcftEthFxPortTraps=_RcftEthFxPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,1,1,10))
_RcftEthFePortMib_ObjectIdentity=ObjectIdentity
rcftEthFePortMib=_RcftEthFePortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,1,2))
_RcftEthFePortObjects_ObjectIdentity=ObjectIdentity
rcftEthFePortObjects=_RcftEthFePortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,1,2,1))
_RcftEthFePortTable_Object=MibTable
rcftEthFePortTable=_RcftEthFePortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1))
if mibBuilder.loadTexts:rcftEthFePortTable.setStatus(_A)
_RcftEthFePortEntry_Object=MibTableRow
rcftEthFePortEntry=_RcftEthFePortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1))
rcftEthFePortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_o))
if mibBuilder.loadTexts:rcftEthFePortEntry.setStatus(_A)
_RcftEthFePortIndex_Type=Integer32
_RcftEthFePortIndex_Object=MibTableColumn
rcftEthFePortIndex=_RcftEthFePortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,1),_RcftEthFePortIndex_Type())
rcftEthFePortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFePortIndex.setStatus(_A)
_RcftEthFePortStatus_Type=Integer32
_RcftEthFePortStatus_Object=MibTableColumn
rcftEthFePortStatus=_RcftEthFePortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,2),_RcftEthFePortStatus_Type())
rcftEthFePortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFePortStatus.setStatus(_A)
_RcftEthFePortRxRestrictSpeed_Type=Integer32
_RcftEthFePortRxRestrictSpeed_Object=MibTableColumn
rcftEthFePortRxRestrictSpeed=_RcftEthFePortRxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,3),_RcftEthFePortRxRestrictSpeed_Type())
rcftEthFePortRxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFePortRxRestrictSpeed.setStatus(_A)
_RcftEthFePortTxRestrictSpeed_Type=Integer32
_RcftEthFePortTxRestrictSpeed_Object=MibTableColumn
rcftEthFePortTxRestrictSpeed=_RcftEthFePortTxRestrictSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,4),_RcftEthFePortTxRestrictSpeed_Type())
rcftEthFePortTxRestrictSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFePortTxRestrictSpeed.setStatus(_A)
_RcftEthFePortRestrictSpeedStep_Type=Integer32
_RcftEthFePortRestrictSpeedStep_Object=MibTableColumn
rcftEthFePortRestrictSpeedStep=_RcftEthFePortRestrictSpeedStep_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,5),_RcftEthFePortRestrictSpeedStep_Type())
rcftEthFePortRestrictSpeedStep.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFePortRestrictSpeedStep.setStatus(_A)
_RcftEthFePortOrder_Type=Integer32
_RcftEthFePortOrder_Object=MibTableColumn
rcftEthFePortOrder=_RcftEthFePortOrder_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,6),_RcftEthFePortOrder_Type())
rcftEthFePortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFePortOrder.setStatus(_A)
_RcftEthFePortPosition_Type=Integer32
_RcftEthFePortPosition_Object=MibTableColumn
rcftEthFePortPosition=_RcftEthFePortPosition_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,7),_RcftEthFePortPosition_Type())
rcftEthFePortPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFePortPosition.setStatus(_A)
_RcftEthFePortPVID_Type=Integer32
_RcftEthFePortPVID_Object=MibTableColumn
rcftEthFePortPVID=_RcftEthFePortPVID_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,8),_RcftEthFePortPVID_Type())
rcftEthFePortPVID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFePortPVID.setStatus(_A)
_RcftEthFePorttag_Type=Integer32
_RcftEthFePorttag_Object=MibTableColumn
rcftEthFePorttag=_RcftEthFePorttag_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,9),_RcftEthFePorttag_Type())
rcftEthFePorttag.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFePorttag.setStatus(_A)
_RcftEthFePortCOS_Type=Integer32
_RcftEthFePortCOS_Object=MibTableColumn
rcftEthFePortCOS=_RcftEthFePortCOS_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,1,1,1,10),_RcftEthFePortCOS_Type())
rcftEthFePortCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftEthFePortCOS.setStatus(_A)
_RcftEthFePortPerformance_ObjectIdentity=ObjectIdentity
rcftEthFePortPerformance=_RcftEthFePortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,1,2,2))
_RcftEthFeStatisticTable_Object=MibTable
rcftEthFeStatisticTable=_RcftEthFeStatisticTable_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,2,1))
if mibBuilder.loadTexts:rcftEthFeStatisticTable.setStatus(_A)
_RcftEthFeStatisticEntry_Object=MibTableRow
rcftEthFeStatisticEntry=_RcftEthFeStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,2,1,1))
if mibBuilder.loadTexts:rcftEthFeStatisticEntry.setStatus(_A)
_RcftEthFeTxPackets_Type=Counter32
_RcftEthFeTxPackets_Object=MibTableColumn
rcftEthFeTxPackets=_RcftEthFeTxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,2,1,1,1),_RcftEthFeTxPackets_Type())
rcftEthFeTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFeTxPackets.setStatus(_A)
_RcftEthFeTxBytes_Type=Counter32
_RcftEthFeTxBytes_Object=MibTableColumn
rcftEthFeTxBytes=_RcftEthFeTxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,2,1,1,2),_RcftEthFeTxBytes_Type())
rcftEthFeTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFeTxBytes.setStatus(_A)
_RcftEthFeTxFailurePackets_Type=Counter32
_RcftEthFeTxFailurePackets_Object=MibTableColumn
rcftEthFeTxFailurePackets=_RcftEthFeTxFailurePackets_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,2,1,1,3),_RcftEthFeTxFailurePackets_Type())
rcftEthFeTxFailurePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFeTxFailurePackets.setStatus(_A)
_RcftEthFeRxPackets_Type=Counter32
_RcftEthFeRxPackets_Object=MibTableColumn
rcftEthFeRxPackets=_RcftEthFeRxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,2,1,1,4),_RcftEthFeRxPackets_Type())
rcftEthFeRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFeRxPackets.setStatus(_A)
_RcftEthFeRxBytes_Type=Counter32
_RcftEthFeRxBytes_Object=MibTableColumn
rcftEthFeRxBytes=_RcftEthFeRxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,2,1,1,5),_RcftEthFeRxBytes_Type())
rcftEthFeRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFeRxBytes.setStatus(_A)
_RcftEthFeRxErrorPackets_Type=Counter32
_RcftEthFeRxErrorPackets_Object=MibTableColumn
rcftEthFeRxErrorPackets=_RcftEthFeRxErrorPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,2,1,1,6),_RcftEthFeRxErrorPackets_Type())
rcftEthFeRxErrorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFeRxErrorPackets.setStatus(_A)
_RcftEthFeFluxTimer_Type=Counter32
_RcftEthFeFluxTimer_Object=MibTableColumn
rcftEthFeFluxTimer=_RcftEthFeFluxTimer_Object((1,3,6,1,4,1,8886,2,1,5,10,1,2,2,1,1,7),_RcftEthFeFluxTimer_Type())
rcftEthFeFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftEthFeFluxTimer.setStatus(_A)
_RcftEthFePortTraps_ObjectIdentity=ObjectIdentity
rcftEthFePortTraps=_RcftEthFePortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,1,2,10))
_RcftPdhPortMib_ObjectIdentity=ObjectIdentity
rcftPdhPortMib=_RcftPdhPortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,2))
_RcftPdhPortObjects_ObjectIdentity=ObjectIdentity
rcftPdhPortObjects=_RcftPdhPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,2,1))
_RcftPdhPortTable_Object=MibTable
rcftPdhPortTable=_RcftPdhPortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1))
if mibBuilder.loadTexts:rcftPdhPortTable.setStatus(_A)
_RcftPdhPortEntry_Object=MibTableRow
rcftPdhPortEntry=_RcftPdhPortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1))
rcftPdhPortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_p))
if mibBuilder.loadTexts:rcftPdhPortEntry.setStatus(_A)
_RcftPdhPortIndex_Type=Integer32
_RcftPdhPortIndex_Object=MibTableColumn
rcftPdhPortIndex=_RcftPdhPortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,1),_RcftPdhPortIndex_Type())
rcftPdhPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPdhPortIndex.setStatus(_A)
_RcftPdhPortAlarmStatus_Type=Integer32
_RcftPdhPortAlarmStatus_Object=MibTableColumn
rcftPdhPortAlarmStatus=_RcftPdhPortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,2),_RcftPdhPortAlarmStatus_Type())
rcftPdhPortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPdhPortAlarmStatus.setStatus(_A)
_RcftPdhPortStatus_Type=Integer32
_RcftPdhPortStatus_Object=MibTableColumn
rcftPdhPortStatus=_RcftPdhPortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,3),_RcftPdhPortStatus_Type())
rcftPdhPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftPdhPortStatus.setStatus(_A)
_RcftPdhPortECSCnt_Type=Integer32
_RcftPdhPortECSCnt_Object=MibTableColumn
rcftPdhPortECSCnt=_RcftPdhPortECSCnt_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,4),_RcftPdhPortECSCnt_Type())
rcftPdhPortECSCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPdhPortECSCnt.setStatus(_A)
_RcftPdhPortSECSCnt_Type=Integer32
_RcftPdhPortSECSCnt_Object=MibTableColumn
rcftPdhPortSECSCnt=_RcftPdhPortSECSCnt_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,5),_RcftPdhPortSECSCnt_Type())
rcftPdhPortSECSCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPdhPortSECSCnt.setStatus(_A)
class _RcftPdhPortModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,12,15,23,50,51,52,53,100)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7),(_j,8),(_k,9),(_l,10),(_m,12),('optical-SFP',15),('optical-SS24',23),('optical-S1FC',50),('optical-S1A',51),('optical-S2A',52),('optical-S3A',53),(_n,100)))
_RcftPdhPortModuleType_Type.__name__=_L
_RcftPdhPortModuleType_Object=MibTableColumn
rcftPdhPortModuleType=_RcftPdhPortModuleType_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,6),_RcftPdhPortModuleType_Type())
rcftPdhPortModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPdhPortModuleType.setStatus(_A)
_RcftPdhPortLoopStatus_Type=Integer32
_RcftPdhPortLoopStatus_Object=MibTableColumn
rcftPdhPortLoopStatus=_RcftPdhPortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,7),_RcftPdhPortLoopStatus_Type())
rcftPdhPortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPdhPortLoopStatus.setStatus(_A)
_RcftPdhPortOrder_Type=Integer32
_RcftPdhPortOrder_Object=MibTableColumn
rcftPdhPortOrder=_RcftPdhPortOrder_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,8),_RcftPdhPortOrder_Type())
rcftPdhPortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftPdhPortOrder.setStatus(_A)
_RcftPdhPortBertStatus_Type=Integer32
_RcftPdhPortBertStatus_Object=MibTableColumn
rcftPdhPortBertStatus=_RcftPdhPortBertStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,9),_RcftPdhPortBertStatus_Type())
rcftPdhPortBertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPdhPortBertStatus.setStatus(_A)
_RcftPdhPortBertErrCode_Type=Unsigned32
_RcftPdhPortBertErrCode_Object=MibTableColumn
rcftPdhPortBertErrCode=_RcftPdhPortBertErrCode_Object((1,3,6,1,4,1,8886,2,1,5,10,2,1,1,1,10),_RcftPdhPortBertErrCode_Type())
rcftPdhPortBertErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPdhPortBertErrCode.setStatus(_A)
_RcftPdhPortPerformance_ObjectIdentity=ObjectIdentity
rcftPdhPortPerformance=_RcftPdhPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,2,2))
_RcftPdhPortTraps_ObjectIdentity=ObjectIdentity
rcftPdhPortTraps=_RcftPdhPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,2,10))
_RcftE1PortMib_ObjectIdentity=ObjectIdentity
rcftE1PortMib=_RcftE1PortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,3))
_RcftE1PortObjects_ObjectIdentity=ObjectIdentity
rcftE1PortObjects=_RcftE1PortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,3,1))
_RcftE1PortTable_Object=MibTable
rcftE1PortTable=_RcftE1PortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1))
if mibBuilder.loadTexts:rcftE1PortTable.setStatus(_A)
_RcftE1PortEntry_Object=MibTableRow
rcftE1PortEntry=_RcftE1PortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1))
rcftE1PortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_q))
if mibBuilder.loadTexts:rcftE1PortEntry.setStatus(_A)
_RcftE1PortIndex_Type=Integer32
_RcftE1PortIndex_Object=MibTableColumn
rcftE1PortIndex=_RcftE1PortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,1),_RcftE1PortIndex_Type())
rcftE1PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1PortIndex.setStatus(_A)
_RcftE1PortAlarmStatus_Type=Integer32
_RcftE1PortAlarmStatus_Object=MibTableColumn
rcftE1PortAlarmStatus=_RcftE1PortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,2),_RcftE1PortAlarmStatus_Type())
rcftE1PortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1PortAlarmStatus.setStatus(_A)
_RcftE1PortStatus_Type=Integer32
_RcftE1PortStatus_Object=MibTableColumn
rcftE1PortStatus=_RcftE1PortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,3),_RcftE1PortStatus_Type())
rcftE1PortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftE1PortStatus.setStatus(_A)
_RcftE1TimeSlots_Type=Integer32
_RcftE1TimeSlots_Object=MibTableColumn
rcftE1TimeSlots=_RcftE1TimeSlots_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,4),_RcftE1TimeSlots_Type())
rcftE1TimeSlots.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftE1TimeSlots.setStatus(_A)
_RcftE1TS0Mode_Type=Integer32
_RcftE1TS0Mode_Object=MibTableColumn
rcftE1TS0Mode=_RcftE1TS0Mode_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,5),_RcftE1TS0Mode_Type())
rcftE1TS0Mode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftE1TS0Mode.setStatus(_A)
_RcftE1IdleCode_Type=Integer32
_RcftE1IdleCode_Object=MibTableColumn
rcftE1IdleCode=_RcftE1IdleCode_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,6),_RcftE1IdleCode_Type())
rcftE1IdleCode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftE1IdleCode.setStatus(_A)
class _RcftE1LoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('localDoubleLoopEnable',1),('localDoubleLoopDisable',2),('remoteDoubleLoopEnable',3),('remoteDoubleLoopDisable',4)))
_RcftE1LoopStatus_Type.__name__=_L
_RcftE1LoopStatus_Object=MibTableColumn
rcftE1LoopStatus=_RcftE1LoopStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,7),_RcftE1LoopStatus_Type())
rcftE1LoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1LoopStatus.setStatus(_A)
_RcftE1Order_Type=Integer32
_RcftE1Order_Object=MibTableColumn
rcftE1Order=_RcftE1Order_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,8),_RcftE1Order_Type())
rcftE1Order.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftE1Order.setStatus(_A)
_RcftE1PortType_Type=Integer32
_RcftE1PortType_Object=MibTableColumn
rcftE1PortType=_RcftE1PortType_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,9),_RcftE1PortType_Type())
rcftE1PortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1PortType.setStatus(_A)
_RcftE1BertStatus_Type=Integer32
_RcftE1BertStatus_Object=MibTableColumn
rcftE1BertStatus=_RcftE1BertStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,10),_RcftE1BertStatus_Type())
rcftE1BertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftE1BertStatus.setStatus(_A)
_RcftE1BertTime_Type=Unsigned32
_RcftE1BertTime_Object=MibTableColumn
rcftE1BertTime=_RcftE1BertTime_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,11),_RcftE1BertTime_Type())
rcftE1BertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1BertTime.setStatus(_A)
_RcftE1BertErrCode_Type=Unsigned32
_RcftE1BertErrCode_Object=MibTableColumn
rcftE1BertErrCode=_RcftE1BertErrCode_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,12),_RcftE1BertErrCode_Type())
rcftE1BertErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1BertErrCode.setStatus(_A)
_RcftE1BertUnusedTime_Type=Unsigned32
_RcftE1BertUnusedTime_Object=MibTableColumn
rcftE1BertUnusedTime=_RcftE1BertUnusedTime_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,13),_RcftE1BertUnusedTime_Type())
rcftE1BertUnusedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1BertUnusedTime.setStatus(_A)
_RcftE1BertPortSpeed_Type=Unsigned32
_RcftE1BertPortSpeed_Object=MibTableColumn
rcftE1BertPortSpeed=_RcftE1BertPortSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,14),_RcftE1BertPortSpeed_Type())
rcftE1BertPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1BertPortSpeed.setStatus(_A)
_RcftE1BertCodeType_Type=Integer32
_RcftE1BertCodeType_Object=MibTableColumn
rcftE1BertCodeType=_RcftE1BertCodeType_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,15),_RcftE1BertCodeType_Type())
rcftE1BertCodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftE1BertCodeType.setStatus(_A)
_RcftE1BertCodeNum_Type=Integer32
_RcftE1BertCodeNum_Object=MibTableColumn
rcftE1BertCodeNum=_RcftE1BertCodeNum_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,16),_RcftE1BertCodeNum_Type())
rcftE1BertCodeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftE1BertCodeNum.setStatus(_A)
_RcftE1AlarmRejest_Type=Integer32
_RcftE1AlarmRejest_Object=MibTableColumn
rcftE1AlarmRejest=_RcftE1AlarmRejest_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,17),_RcftE1AlarmRejest_Type())
rcftE1AlarmRejest.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1AlarmRejest.setStatus(_A)
_RcfT1PortAlarmStatus_Type=Integer32
_RcfT1PortAlarmStatus_Object=MibTableColumn
rcfT1PortAlarmStatus=_RcfT1PortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,18),_RcfT1PortAlarmStatus_Type())
rcfT1PortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcfT1PortAlarmStatus.setStatus(_A)
_RcftE1PortVCGNumber_Type=Integer32
_RcftE1PortVCGNumber_Object=MibTableColumn
rcftE1PortVCGNumber=_RcftE1PortVCGNumber_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,19),_RcftE1PortVCGNumber_Type())
rcftE1PortVCGNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1PortVCGNumber.setStatus(_A)
_RcftE1PortErrorRate_Type=Integer32
_RcftE1PortErrorRate_Object=MibTableColumn
rcftE1PortErrorRate=_RcftE1PortErrorRate_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,20),_RcftE1PortErrorRate_Type())
rcftE1PortErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1PortErrorRate.setStatus(_A)
_RcftE1PortESCont_Type=Integer32
_RcftE1PortESCont_Object=MibTableColumn
rcftE1PortESCont=_RcftE1PortESCont_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,21),_RcftE1PortESCont_Type())
rcftE1PortESCont.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1PortESCont.setStatus(_A)
_RcftE1PortSESCont_Type=Integer32
_RcftE1PortSESCont_Object=MibTableColumn
rcftE1PortSESCont=_RcftE1PortSESCont_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,22),_RcftE1PortSESCont_Type())
rcftE1PortSESCont.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1PortSESCont.setStatus(_A)
_RcftE1PortToRNumber_Type=Integer32
_RcftE1PortToRNumber_Object=MibTableColumn
rcftE1PortToRNumber=_RcftE1PortToRNumber_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,23),_RcftE1PortToRNumber_Type())
rcftE1PortToRNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1PortToRNumber.setStatus(_A)
_RcftE1CVCnt_Type=Integer32
_RcftE1CVCnt_Object=MibTableColumn
rcftE1CVCnt=_RcftE1CVCnt_Object((1,3,6,1,4,1,8886,2,1,5,10,3,1,1,1,24),_RcftE1CVCnt_Type())
rcftE1CVCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftE1CVCnt.setStatus(_A)
_RcftE1PortPerformance_ObjectIdentity=ObjectIdentity
rcftE1PortPerformance=_RcftE1PortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,3,2))
_RcftE1PortTraps_ObjectIdentity=ObjectIdentity
rcftE1PortTraps=_RcftE1PortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,3,10))
_RcftV35PortMib_ObjectIdentity=ObjectIdentity
rcftV35PortMib=_RcftV35PortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,4))
_RcftV35PortObjects_ObjectIdentity=ObjectIdentity
rcftV35PortObjects=_RcftV35PortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,4,1))
_RcftV35PortTable_Object=MibTable
rcftV35PortTable=_RcftV35PortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1))
if mibBuilder.loadTexts:rcftV35PortTable.setStatus(_A)
_RcftV35PortEntry_Object=MibTableRow
rcftV35PortEntry=_RcftV35PortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1))
rcftV35PortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_r))
if mibBuilder.loadTexts:rcftV35PortEntry.setStatus(_A)
_RcftV35PortIndex_Type=Integer32
_RcftV35PortIndex_Object=MibTableColumn
rcftV35PortIndex=_RcftV35PortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,1),_RcftV35PortIndex_Type())
rcftV35PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftV35PortIndex.setStatus(_A)
_RcftV35PortAlarmStatus_Type=Integer32
_RcftV35PortAlarmStatus_Object=MibTableColumn
rcftV35PortAlarmStatus=_RcftV35PortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,2),_RcftV35PortAlarmStatus_Type())
rcftV35PortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftV35PortAlarmStatus.setStatus(_A)
_RcftV35PortStatus_Type=Integer32
_RcftV35PortStatus_Object=MibTableColumn
rcftV35PortStatus=_RcftV35PortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,3),_RcftV35PortStatus_Type())
rcftV35PortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftV35PortStatus.setStatus(_A)
_RcftV35PortSpeed_Type=Unsigned32
_RcftV35PortSpeed_Object=MibTableColumn
rcftV35PortSpeed=_RcftV35PortSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,4),_RcftV35PortSpeed_Type())
rcftV35PortSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftV35PortSpeed.setStatus(_A)
_RcftV35PortBertStatus_Type=Integer32
_RcftV35PortBertStatus_Object=MibTableColumn
rcftV35PortBertStatus=_RcftV35PortBertStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,5),_RcftV35PortBertStatus_Type())
rcftV35PortBertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftV35PortBertStatus.setStatus(_A)
_RcftV35PortBertTime_Type=Unsigned32
_RcftV35PortBertTime_Object=MibTableColumn
rcftV35PortBertTime=_RcftV35PortBertTime_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,6),_RcftV35PortBertTime_Type())
rcftV35PortBertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftV35PortBertTime.setStatus(_A)
_RcftV35PortBertErrCode_Type=Unsigned32
_RcftV35PortBertErrCode_Object=MibTableColumn
rcftV35PortBertErrCode=_RcftV35PortBertErrCode_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,7),_RcftV35PortBertErrCode_Type())
rcftV35PortBertErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftV35PortBertErrCode.setStatus(_A)
_RcftV35PortBertUnusedTime_Type=Unsigned32
_RcftV35PortBertUnusedTime_Object=MibTableColumn
rcftV35PortBertUnusedTime=_RcftV35PortBertUnusedTime_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,8),_RcftV35PortBertUnusedTime_Type())
rcftV35PortBertUnusedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftV35PortBertUnusedTime.setStatus(_A)
_RcftV35PortBertPortSpeed_Type=Unsigned32
_RcftV35PortBertPortSpeed_Object=MibTableColumn
rcftV35PortBertPortSpeed=_RcftV35PortBertPortSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,9),_RcftV35PortBertPortSpeed_Type())
rcftV35PortBertPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftV35PortBertPortSpeed.setStatus(_A)
_RcftV35PortBertCodeType_Type=Integer32
_RcftV35PortBertCodeType_Object=MibTableColumn
rcftV35PortBertCodeType=_RcftV35PortBertCodeType_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,10),_RcftV35PortBertCodeType_Type())
rcftV35PortBertCodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftV35PortBertCodeType.setStatus(_A)
_RcftV35PortBertCodeNum_Type=Integer32
_RcftV35PortBertCodeNum_Object=MibTableColumn
rcftV35PortBertCodeNum=_RcftV35PortBertCodeNum_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,11),_RcftV35PortBertCodeNum_Type())
rcftV35PortBertCodeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftV35PortBertCodeNum.setStatus(_A)
_RcftV35PortLoopStatus_Type=Integer32
_RcftV35PortLoopStatus_Object=MibTableColumn
rcftV35PortLoopStatus=_RcftV35PortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,12),_RcftV35PortLoopStatus_Type())
rcftV35PortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftV35PortLoopStatus.setStatus(_A)
_RcftV35PortOrder_Type=Integer32
_RcftV35PortOrder_Object=MibTableColumn
rcftV35PortOrder=_RcftV35PortOrder_Object((1,3,6,1,4,1,8886,2,1,5,10,4,1,1,1,13),_RcftV35PortOrder_Type())
rcftV35PortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftV35PortOrder.setStatus(_A)
_RcftV35PortPerformance_ObjectIdentity=ObjectIdentity
rcftV35PortPerformance=_RcftV35PortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,4,2))
_RcftV35PortTraps_ObjectIdentity=ObjectIdentity
rcftV35PortTraps=_RcftV35PortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,4,10))
_RcftSHDSLPortMib_ObjectIdentity=ObjectIdentity
rcftSHDSLPortMib=_RcftSHDSLPortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,5))
_RcftSHDSLPortObjects_ObjectIdentity=ObjectIdentity
rcftSHDSLPortObjects=_RcftSHDSLPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,5,1))
_RcftSHDSLPortTable_Object=MibTable
rcftSHDSLPortTable=_RcftSHDSLPortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1))
if mibBuilder.loadTexts:rcftSHDSLPortTable.setStatus(_A)
_RcftSHDSLPortEntry_Object=MibTableRow
rcftSHDSLPortEntry=_RcftSHDSLPortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1))
rcftSHDSLPortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_T))
if mibBuilder.loadTexts:rcftSHDSLPortEntry.setStatus(_A)
_RcftSHDSLPortIndex_Type=Integer32
_RcftSHDSLPortIndex_Object=MibTableColumn
rcftSHDSLPortIndex=_RcftSHDSLPortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,1),_RcftSHDSLPortIndex_Type())
rcftSHDSLPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIndex.setStatus(_A)
_RcftSHDSLPortAlarmStatus_Type=Integer32
_RcftSHDSLPortAlarmStatus_Object=MibTableColumn
rcftSHDSLPortAlarmStatus=_RcftSHDSLPortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,2),_RcftSHDSLPortAlarmStatus_Type())
rcftSHDSLPortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortAlarmStatus.setStatus(_A)
_RcftSHDSLPortStatus_Type=Integer32
_RcftSHDSLPortStatus_Object=MibTableColumn
rcftSHDSLPortStatus=_RcftSHDSLPortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,3),_RcftSHDSLPortStatus_Type())
rcftSHDSLPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortStatus.setStatus(_A)
_RcftSHDSLPortCapableSpeed_Type=Integer32
_RcftSHDSLPortCapableSpeed_Object=MibTableColumn
rcftSHDSLPortCapableSpeed=_RcftSHDSLPortCapableSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,4),_RcftSHDSLPortCapableSpeed_Type())
rcftSHDSLPortCapableSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCapableSpeed.setStatus(_A)
_RcftSHDSLPortWorkSpeed_Type=Integer32
_RcftSHDSLPortWorkSpeed_Object=MibTableColumn
rcftSHDSLPortWorkSpeed=_RcftSHDSLPortWorkSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,5),_RcftSHDSLPortWorkSpeed_Type())
rcftSHDSLPortWorkSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortWorkSpeed.setStatus(_A)
_RcftSHDSLPortProbeMaxSpeed_Type=Integer32
_RcftSHDSLPortProbeMaxSpeed_Object=MibTableColumn
rcftSHDSLPortProbeMaxSpeed=_RcftSHDSLPortProbeMaxSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,6),_RcftSHDSLPortProbeMaxSpeed_Type())
rcftSHDSLPortProbeMaxSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortProbeMaxSpeed.setStatus(_A)
_RcftSHDSLPortProbeMinSpeed_Type=Integer32
_RcftSHDSLPortProbeMinSpeed_Object=MibTableColumn
rcftSHDSLPortProbeMinSpeed=_RcftSHDSLPortProbeMinSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,7),_RcftSHDSLPortProbeMinSpeed_Type())
rcftSHDSLPortProbeMinSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortProbeMinSpeed.setStatus(_A)
_RcftSDHSLPortSNR_Type=Integer32
_RcftSDHSLPortSNR_Object=MibTableColumn
rcftSDHSLPortSNR=_RcftSDHSLPortSNR_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,8),_RcftSDHSLPortSNR_Type())
rcftSDHSLPortSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSDHSLPortSNR.setStatus(_A)
_RcftSHDSLPortConfigSNR_Type=Integer32
_RcftSHDSLPortConfigSNR_Object=MibTableColumn
rcftSHDSLPortConfigSNR=_RcftSHDSLPortConfigSNR_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,9),_RcftSHDSLPortConfigSNR_Type())
rcftSHDSLPortConfigSNR.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortConfigSNR.setStatus(_A)
_RcftSHDSLPortSNRThreshold_Type=Integer32
_RcftSHDSLPortSNRThreshold_Object=MibTableColumn
rcftSHDSLPortSNRThreshold=_RcftSHDSLPortSNRThreshold_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,10),_RcftSHDSLPortSNRThreshold_Type())
rcftSHDSLPortSNRThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortSNRThreshold.setStatus(_A)
_RcftSHDSLPortAttenuation_Type=Integer32
_RcftSHDSLPortAttenuation_Object=MibTableColumn
rcftSHDSLPortAttenuation=_RcftSHDSLPortAttenuation_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,11),_RcftSHDSLPortAttenuation_Type())
rcftSHDSLPortAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortAttenuation.setStatus(_A)
_RcftSHDSLPortAttenuationThreshold_Type=Integer32
_RcftSHDSLPortAttenuationThreshold_Object=MibTableColumn
rcftSHDSLPortAttenuationThreshold=_RcftSHDSLPortAttenuationThreshold_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,12),_RcftSHDSLPortAttenuationThreshold_Type())
rcftSHDSLPortAttenuationThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortAttenuationThreshold.setStatus(_A)
_RcftSHDSLPortPBO_Type=Integer32
_RcftSHDSLPortPBO_Object=MibTableColumn
rcftSHDSLPortPBO=_RcftSHDSLPortPBO_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,13),_RcftSHDSLPortPBO_Type())
rcftSHDSLPortPBO.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortPBO.setStatus(_A)
_RcftSHDSLPortLOSThreshold_Type=Integer32
_RcftSHDSLPortLOSThreshold_Object=MibTableColumn
rcftSHDSLPortLOSThreshold=_RcftSHDSLPortLOSThreshold_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,14),_RcftSHDSLPortLOSThreshold_Type())
rcftSHDSLPortLOSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortLOSThreshold.setStatus(_A)
_RcftSHDSLPortLOSWThreshold_Type=Integer32
_RcftSHDSLPortLOSWThreshold_Object=MibTableColumn
rcftSHDSLPortLOSWThreshold=_RcftSHDSLPortLOSWThreshold_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,15),_RcftSHDSLPortLOSWThreshold_Type())
rcftSHDSLPortLOSWThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortLOSWThreshold.setStatus(_A)
_RcftSHDSLPortLOLKThreshold_Type=Integer32
_RcftSHDSLPortLOLKThreshold_Object=MibTableColumn
rcftSHDSLPortLOLKThreshold=_RcftSHDSLPortLOLKThreshold_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,16),_RcftSHDSLPortLOLKThreshold_Type())
rcftSHDSLPortLOLKThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortLOLKThreshold.setStatus(_A)
_RcftSHDSLPortESThreshold_Type=Integer32
_RcftSHDSLPortESThreshold_Object=MibTableColumn
rcftSHDSLPortESThreshold=_RcftSHDSLPortESThreshold_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,17),_RcftSHDSLPortESThreshold_Type())
rcftSHDSLPortESThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortESThreshold.setStatus(_A)
class _RcftSHDSLPortLoopStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,100)));namedValues=NamedValues(*(('insideLoop',1),('outsideLoop',2),('doubleloop',3),('normal',100)))
_RcftSHDSLPortLoopStatus_Type.__name__=_L
_RcftSHDSLPortLoopStatus_Object=MibTableColumn
rcftSHDSLPortLoopStatus=_RcftSHDSLPortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,18),_RcftSHDSLPortLoopStatus_Type())
rcftSHDSLPortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortLoopStatus.setStatus(_A)
_RcftSHDSLPortAttenuationInitThreshhold_Type=Integer32
_RcftSHDSLPortAttenuationInitThreshhold_Object=MibTableColumn
rcftSHDSLPortAttenuationInitThreshhold=_RcftSHDSLPortAttenuationInitThreshhold_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,19),_RcftSHDSLPortAttenuationInitThreshhold_Type())
rcftSHDSLPortAttenuationInitThreshhold.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortAttenuationInitThreshhold.setStatus(_A)
_RcftSHDSLPortBertStatus_Type=Integer32
_RcftSHDSLPortBertStatus_Object=MibTableColumn
rcftSHDSLPortBertStatus=_RcftSHDSLPortBertStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,20),_RcftSHDSLPortBertStatus_Type())
rcftSHDSLPortBertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortBertStatus.setStatus(_A)
_RcftSHDSLPortBertTime_Type=Unsigned32
_RcftSHDSLPortBertTime_Object=MibTableColumn
rcftSHDSLPortBertTime=_RcftSHDSLPortBertTime_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,21),_RcftSHDSLPortBertTime_Type())
rcftSHDSLPortBertTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortBertTime.setStatus(_A)
_RcftSHDSLPortBertErrCode_Type=Unsigned32
_RcftSHDSLPortBertErrCode_Object=MibTableColumn
rcftSHDSLPortBertErrCode=_RcftSHDSLPortBertErrCode_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,22),_RcftSHDSLPortBertErrCode_Type())
rcftSHDSLPortBertErrCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortBertErrCode.setStatus(_A)
_RcftSHDSLPortBertUnusedTime_Type=Unsigned32
_RcftSHDSLPortBertUnusedTime_Object=MibTableColumn
rcftSHDSLPortBertUnusedTime=_RcftSHDSLPortBertUnusedTime_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,23),_RcftSHDSLPortBertUnusedTime_Type())
rcftSHDSLPortBertUnusedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortBertUnusedTime.setStatus(_A)
_RcftSHDSLPortBertPortSpeed_Type=Unsigned32
_RcftSHDSLPortBertPortSpeed_Object=MibTableColumn
rcftSHDSLPortBertPortSpeed=_RcftSHDSLPortBertPortSpeed_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,24),_RcftSHDSLPortBertPortSpeed_Type())
rcftSHDSLPortBertPortSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortBertPortSpeed.setStatus(_A)
_RcftSHDSLPortBertCodeType_Type=Integer32
_RcftSHDSLPortBertCodeType_Object=MibTableColumn
rcftSHDSLPortBertCodeType=_RcftSHDSLPortBertCodeType_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,25),_RcftSHDSLPortBertCodeType_Type())
rcftSHDSLPortBertCodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortBertCodeType.setStatus(_A)
_RcftSHDSLPortBertCodeNum_Type=Integer32
_RcftSHDSLPortBertCodeNum_Object=MibTableColumn
rcftSHDSLPortBertCodeNum=_RcftSHDSLPortBertCodeNum_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,26),_RcftSHDSLPortBertCodeNum_Type())
rcftSHDSLPortBertCodeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortBertCodeNum.setStatus(_A)
_RcftSHDSLPortOrder_Type=Integer32
_RcftSHDSLPortOrder_Object=MibTableColumn
rcftSHDSLPortOrder=_RcftSHDSLPortOrder_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,27),_RcftSHDSLPortOrder_Type())
rcftSHDSLPortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortOrder.setStatus(_A)
_RcftSHDSLPortOrderTimeParameter_Type=Integer32
_RcftSHDSLPortOrderTimeParameter_Object=MibTableColumn
rcftSHDSLPortOrderTimeParameter=_RcftSHDSLPortOrderTimeParameter_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,28),_RcftSHDSLPortOrderTimeParameter_Type())
rcftSHDSLPortOrderTimeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortOrderTimeParameter.setStatus(_A)
_RcftSHDSLPortOrderModeParameter_Type=Integer32
_RcftSHDSLPortOrderModeParameter_Object=MibTableColumn
rcftSHDSLPortOrderModeParameter=_RcftSHDSLPortOrderModeParameter_Object((1,3,6,1,4,1,8886,2,1,5,10,5,1,1,1,29),_RcftSHDSLPortOrderModeParameter_Type())
rcftSHDSLPortOrderModeParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSHDSLPortOrderModeParameter.setStatus(_A)
_RcftSHDSLPortPerformance_ObjectIdentity=ObjectIdentity
rcftSHDSLPortPerformance=_RcftSHDSLPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,5,2))
_RcftSHDSLPortCurrentTable_Object=MibTable
rcftSHDSLPortCurrentTable=_RcftSHDSLPortCurrentTable_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1))
if mibBuilder.loadTexts:rcftSHDSLPortCurrentTable.setStatus(_A)
_RcftSHDSLPortCurrentEntry_Object=MibTableRow
rcftSHDSLPortCurrentEntry=_RcftSHDSLPortCurrentEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1))
rcftSHDSLPortCurrentEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_T))
if mibBuilder.loadTexts:rcftSHDSLPortCurrentEntry.setStatus(_A)
_RcftSHDSLPortCurrentLOSTimes_Type=Integer32
_RcftSHDSLPortCurrentLOSTimes_Object=MibTableColumn
rcftSHDSLPortCurrentLOSTimes=_RcftSHDSLPortCurrentLOSTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,1),_RcftSHDSLPortCurrentLOSTimes_Type())
rcftSHDSLPortCurrentLOSTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentLOSTimes.setStatus(_A)
_RcftSHDSLPortCurrentLOSWTimes_Type=Integer32
_RcftSHDSLPortCurrentLOSWTimes_Object=MibTableColumn
rcftSHDSLPortCurrentLOSWTimes=_RcftSHDSLPortCurrentLOSWTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,2),_RcftSHDSLPortCurrentLOSWTimes_Type())
rcftSHDSLPortCurrentLOSWTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentLOSWTimes.setStatus(_A)
_RcftSHDSLPortCurrentLOLKTimes_Type=Integer32
_RcftSHDSLPortCurrentLOLKTimes_Object=MibTableColumn
rcftSHDSLPortCurrentLOLKTimes=_RcftSHDSLPortCurrentLOLKTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,3),_RcftSHDSLPortCurrentLOLKTimes_Type())
rcftSHDSLPortCurrentLOLKTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentLOLKTimes.setStatus(_A)
_RcftSHDSLPortCurrentCVTimes_Type=Integer32
_RcftSHDSLPortCurrentCVTimes_Object=MibTableColumn
rcftSHDSLPortCurrentCVTimes=_RcftSHDSLPortCurrentCVTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,4),_RcftSHDSLPortCurrentCVTimes_Type())
rcftSHDSLPortCurrentCVTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentCVTimes.setStatus(_A)
_RcftSHDSLPortCurrentES_Type=Integer32
_RcftSHDSLPortCurrentES_Object=MibTableColumn
rcftSHDSLPortCurrentES=_RcftSHDSLPortCurrentES_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,5),_RcftSHDSLPortCurrentES_Type())
rcftSHDSLPortCurrentES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentES.setStatus(_A)
_RcftSHDSLPortCurrentSES_Type=Integer32
_RcftSHDSLPortCurrentSES_Object=MibTableColumn
rcftSHDSLPortCurrentSES=_RcftSHDSLPortCurrentSES_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,6),_RcftSHDSLPortCurrentSES_Type())
rcftSHDSLPortCurrentSES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentSES.setStatus(_A)
_RcftSHDSLPortCurrentUAS_Type=Integer32
_RcftSHDSLPortCurrentUAS_Object=MibTableColumn
rcftSHDSLPortCurrentUAS=_RcftSHDSLPortCurrentUAS_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,7),_RcftSHDSLPortCurrentUAS_Type())
rcftSHDSLPortCurrentUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentUAS.setStatus(_A)
_RcftSHDSLPortCurrentLOSWS_Type=Integer32
_RcftSHDSLPortCurrentLOSWS_Object=MibTableColumn
rcftSHDSLPortCurrentLOSWS=_RcftSHDSLPortCurrentLOSWS_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,8),_RcftSHDSLPortCurrentLOSWS_Type())
rcftSHDSLPortCurrentLOSWS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentLOSWS.setStatus(_A)
_RcftSHDSLPortCurrentLOFTimes_Type=Integer32
_RcftSHDSLPortCurrentLOFTimes_Object=MibTableColumn
rcftSHDSLPortCurrentLOFTimes=_RcftSHDSLPortCurrentLOFTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,9),_RcftSHDSLPortCurrentLOFTimes_Type())
rcftSHDSLPortCurrentLOFTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentLOFTimes.setStatus(_A)
_RcftSHDSLPortCurrentCRCTimes_Type=Integer32
_RcftSHDSLPortCurrentCRCTimes_Object=MibTableColumn
rcftSHDSLPortCurrentCRCTimes=_RcftSHDSLPortCurrentCRCTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,1,1,10),_RcftSHDSLPortCurrentCRCTimes_Type())
rcftSHDSLPortCurrentCRCTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentCRCTimes.setStatus(_A)
_RcftSHDSLPortIntervalTable_Object=MibTable
rcftSHDSLPortIntervalTable=_RcftSHDSLPortIntervalTable_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2))
if mibBuilder.loadTexts:rcftSHDSLPortIntervalTable.setStatus(_A)
_RcftSHDSLPortIntervalEntry_Object=MibTableRow
rcftSHDSLPortIntervalEntry=_RcftSHDSLPortIntervalEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1))
rcftSHDSLPortIntervalEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_T),(0,_C,_s))
if mibBuilder.loadTexts:rcftSHDSLPortIntervalEntry.setStatus(_A)
_RcftSHDSLPortIntervalNumber_Type=Integer32
_RcftSHDSLPortIntervalNumber_Object=MibTableColumn
rcftSHDSLPortIntervalNumber=_RcftSHDSLPortIntervalNumber_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,1),_RcftSHDSLPortIntervalNumber_Type())
rcftSHDSLPortIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalNumber.setStatus(_A)
_RcftSHDSLPortIntervalLOSTimes_Type=Integer32
_RcftSHDSLPortIntervalLOSTimes_Object=MibTableColumn
rcftSHDSLPortIntervalLOSTimes=_RcftSHDSLPortIntervalLOSTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,2),_RcftSHDSLPortIntervalLOSTimes_Type())
rcftSHDSLPortIntervalLOSTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalLOSTimes.setStatus(_A)
_RcftSHDSLPortIntervalLOSWTimes_Type=Integer32
_RcftSHDSLPortIntervalLOSWTimes_Object=MibTableColumn
rcftSHDSLPortIntervalLOSWTimes=_RcftSHDSLPortIntervalLOSWTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,3),_RcftSHDSLPortIntervalLOSWTimes_Type())
rcftSHDSLPortIntervalLOSWTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalLOSWTimes.setStatus(_A)
_RcftSHDSLPortIntervalLOLKTimes_Type=Integer32
_RcftSHDSLPortIntervalLOLKTimes_Object=MibTableColumn
rcftSHDSLPortIntervalLOLKTimes=_RcftSHDSLPortIntervalLOLKTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,4),_RcftSHDSLPortIntervalLOLKTimes_Type())
rcftSHDSLPortIntervalLOLKTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalLOLKTimes.setStatus(_A)
_RcftSHDSLPortIntervalCVTimes_Type=Integer32
_RcftSHDSLPortIntervalCVTimes_Object=MibTableColumn
rcftSHDSLPortIntervalCVTimes=_RcftSHDSLPortIntervalCVTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,5),_RcftSHDSLPortIntervalCVTimes_Type())
rcftSHDSLPortIntervalCVTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalCVTimes.setStatus(_A)
_RcftSHDSLPortIntervalES_Type=Integer32
_RcftSHDSLPortIntervalES_Object=MibTableColumn
rcftSHDSLPortIntervalES=_RcftSHDSLPortIntervalES_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,6),_RcftSHDSLPortIntervalES_Type())
rcftSHDSLPortIntervalES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalES.setStatus(_A)
_RcftSHDSLPortIntervalSES_Type=Integer32
_RcftSHDSLPortIntervalSES_Object=MibTableColumn
rcftSHDSLPortIntervalSES=_RcftSHDSLPortIntervalSES_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,7),_RcftSHDSLPortIntervalSES_Type())
rcftSHDSLPortIntervalSES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalSES.setStatus(_A)
_RcftSHDSLPortIntervalUAS_Type=Integer32
_RcftSHDSLPortIntervalUAS_Object=MibTableColumn
rcftSHDSLPortIntervalUAS=_RcftSHDSLPortIntervalUAS_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,8),_RcftSHDSLPortIntervalUAS_Type())
rcftSHDSLPortIntervalUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalUAS.setStatus(_A)
_RcftSHDSLPortIntervalLOSWS_Type=Integer32
_RcftSHDSLPortIntervalLOSWS_Object=MibTableColumn
rcftSHDSLPortIntervalLOSWS=_RcftSHDSLPortIntervalLOSWS_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,9),_RcftSHDSLPortIntervalLOSWS_Type())
rcftSHDSLPortIntervalLOSWS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalLOSWS.setStatus(_A)
_RcftSHDSLPortIntervalLOFTimes_Type=Integer32
_RcftSHDSLPortIntervalLOFTimes_Object=MibTableColumn
rcftSHDSLPortIntervalLOFTimes=_RcftSHDSLPortIntervalLOFTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,10),_RcftSHDSLPortIntervalLOFTimes_Type())
rcftSHDSLPortIntervalLOFTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalLOFTimes.setStatus(_A)
_RcftSHDSLPortIntervalCRCTimes_Type=Integer32
_RcftSHDSLPortIntervalCRCTimes_Object=MibTableColumn
rcftSHDSLPortIntervalCRCTimes=_RcftSHDSLPortIntervalCRCTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,2,1,11),_RcftSHDSLPortIntervalCRCTimes_Type())
rcftSHDSLPortIntervalCRCTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalCRCTimes.setStatus(_A)
_RcftSHDSLPortCurrentDayTable_Object=MibTable
rcftSHDSLPortCurrentDayTable=_RcftSHDSLPortCurrentDayTable_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3))
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayTable.setStatus(_A)
_RcftSHDSLPortCurrentDayEntry_Object=MibTableRow
rcftSHDSLPortCurrentDayEntry=_RcftSHDSLPortCurrentDayEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1))
rcftSHDSLPortCurrentDayEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_T))
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayEntry.setStatus(_A)
_RcftSHDSLPortCurrentDayLOSTimes_Type=Integer32
_RcftSHDSLPortCurrentDayLOSTimes_Object=MibTableColumn
rcftSHDSLPortCurrentDayLOSTimes=_RcftSHDSLPortCurrentDayLOSTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,1),_RcftSHDSLPortCurrentDayLOSTimes_Type())
rcftSHDSLPortCurrentDayLOSTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayLOSTimes.setStatus(_A)
_RcftSHDSLPortCurrentDayLOSWTimes_Type=Integer32
_RcftSHDSLPortCurrentDayLOSWTimes_Object=MibTableColumn
rcftSHDSLPortCurrentDayLOSWTimes=_RcftSHDSLPortCurrentDayLOSWTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,2),_RcftSHDSLPortCurrentDayLOSWTimes_Type())
rcftSHDSLPortCurrentDayLOSWTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayLOSWTimes.setStatus(_A)
_RcftSHDSLPortCurrentDayLOLKTimes_Type=Integer32
_RcftSHDSLPortCurrentDayLOLKTimes_Object=MibTableColumn
rcftSHDSLPortCurrentDayLOLKTimes=_RcftSHDSLPortCurrentDayLOLKTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,3),_RcftSHDSLPortCurrentDayLOLKTimes_Type())
rcftSHDSLPortCurrentDayLOLKTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayLOLKTimes.setStatus(_A)
_RcftSHDSLPortCurrentDayCVTimes_Type=Integer32
_RcftSHDSLPortCurrentDayCVTimes_Object=MibTableColumn
rcftSHDSLPortCurrentDayCVTimes=_RcftSHDSLPortCurrentDayCVTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,4),_RcftSHDSLPortCurrentDayCVTimes_Type())
rcftSHDSLPortCurrentDayCVTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayCVTimes.setStatus(_A)
_RcftSHDSLPortCurrentDayES_Type=Integer32
_RcftSHDSLPortCurrentDayES_Object=MibTableColumn
rcftSHDSLPortCurrentDayES=_RcftSHDSLPortCurrentDayES_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,5),_RcftSHDSLPortCurrentDayES_Type())
rcftSHDSLPortCurrentDayES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayES.setStatus(_A)
_RcftSHDSLPortCurrentDaySES_Type=Integer32
_RcftSHDSLPortCurrentDaySES_Object=MibTableColumn
rcftSHDSLPortCurrentDaySES=_RcftSHDSLPortCurrentDaySES_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,6),_RcftSHDSLPortCurrentDaySES_Type())
rcftSHDSLPortCurrentDaySES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDaySES.setStatus(_A)
_RcftSHDSLPortCurrentDayUAS_Type=Integer32
_RcftSHDSLPortCurrentDayUAS_Object=MibTableColumn
rcftSHDSLPortCurrentDayUAS=_RcftSHDSLPortCurrentDayUAS_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,7),_RcftSHDSLPortCurrentDayUAS_Type())
rcftSHDSLPortCurrentDayUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayUAS.setStatus(_A)
_RcftSHDSLPortCurrentDayLOSWS_Type=Integer32
_RcftSHDSLPortCurrentDayLOSWS_Object=MibTableColumn
rcftSHDSLPortCurrentDayLOSWS=_RcftSHDSLPortCurrentDayLOSWS_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,8),_RcftSHDSLPortCurrentDayLOSWS_Type())
rcftSHDSLPortCurrentDayLOSWS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayLOSWS.setStatus(_A)
_RcftSHDSLPortCurrentDayLOFTimes_Type=Integer32
_RcftSHDSLPortCurrentDayLOFTimes_Object=MibTableColumn
rcftSHDSLPortCurrentDayLOFTimes=_RcftSHDSLPortCurrentDayLOFTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,9),_RcftSHDSLPortCurrentDayLOFTimes_Type())
rcftSHDSLPortCurrentDayLOFTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayLOFTimes.setStatus(_A)
_RcftSHDSLPortCurrentDayCRCTimes_Type=Integer32
_RcftSHDSLPortCurrentDayCRCTimes_Object=MibTableColumn
rcftSHDSLPortCurrentDayCRCTimes=_RcftSHDSLPortCurrentDayCRCTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,3,1,10),_RcftSHDSLPortCurrentDayCRCTimes_Type())
rcftSHDSLPortCurrentDayCRCTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortCurrentDayCRCTimes.setStatus(_A)
_RcftSHDSLPortIntervalDayTable_Object=MibTable
rcftSHDSLPortIntervalDayTable=_RcftSHDSLPortIntervalDayTable_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4))
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayTable.setStatus(_A)
_RcftSHDSLPortIntervalDayEntry_Object=MibTableRow
rcftSHDSLPortIntervalDayEntry=_RcftSHDSLPortIntervalDayEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1))
rcftSHDSLPortIntervalDayEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_T),(0,_C,_t))
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayEntry.setStatus(_A)
_RcftSHDSLPortIntervalDayNumber_Type=Integer32
_RcftSHDSLPortIntervalDayNumber_Object=MibTableColumn
rcftSHDSLPortIntervalDayNumber=_RcftSHDSLPortIntervalDayNumber_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,1),_RcftSHDSLPortIntervalDayNumber_Type())
rcftSHDSLPortIntervalDayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayNumber.setStatus(_A)
_RcftSHDSLPortIntervalDayLOSTimes_Type=Integer32
_RcftSHDSLPortIntervalDayLOSTimes_Object=MibTableColumn
rcftSHDSLPortIntervalDayLOSTimes=_RcftSHDSLPortIntervalDayLOSTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,2),_RcftSHDSLPortIntervalDayLOSTimes_Type())
rcftSHDSLPortIntervalDayLOSTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayLOSTimes.setStatus(_A)
_RcftSHDSLPortIntervalDayLOSWTimes_Type=Integer32
_RcftSHDSLPortIntervalDayLOSWTimes_Object=MibTableColumn
rcftSHDSLPortIntervalDayLOSWTimes=_RcftSHDSLPortIntervalDayLOSWTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,3),_RcftSHDSLPortIntervalDayLOSWTimes_Type())
rcftSHDSLPortIntervalDayLOSWTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayLOSWTimes.setStatus(_A)
_RcftSHDSLPortIntervalDayLOLKTimes_Type=Integer32
_RcftSHDSLPortIntervalDayLOLKTimes_Object=MibTableColumn
rcftSHDSLPortIntervalDayLOLKTimes=_RcftSHDSLPortIntervalDayLOLKTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,4),_RcftSHDSLPortIntervalDayLOLKTimes_Type())
rcftSHDSLPortIntervalDayLOLKTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayLOLKTimes.setStatus(_A)
_RcftSHDSLPortIntervalDayCVTimes_Type=Integer32
_RcftSHDSLPortIntervalDayCVTimes_Object=MibTableColumn
rcftSHDSLPortIntervalDayCVTimes=_RcftSHDSLPortIntervalDayCVTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,5),_RcftSHDSLPortIntervalDayCVTimes_Type())
rcftSHDSLPortIntervalDayCVTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayCVTimes.setStatus(_A)
_RcftSHDSLPortIntervalDayES_Type=Integer32
_RcftSHDSLPortIntervalDayES_Object=MibTableColumn
rcftSHDSLPortIntervalDayES=_RcftSHDSLPortIntervalDayES_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,6),_RcftSHDSLPortIntervalDayES_Type())
rcftSHDSLPortIntervalDayES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayES.setStatus(_A)
_RcftSHDSLPortIntervalDaySES_Type=Integer32
_RcftSHDSLPortIntervalDaySES_Object=MibTableColumn
rcftSHDSLPortIntervalDaySES=_RcftSHDSLPortIntervalDaySES_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,7),_RcftSHDSLPortIntervalDaySES_Type())
rcftSHDSLPortIntervalDaySES.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDaySES.setStatus(_A)
_RcftSHDSLPortIntervalDayUAS_Type=Integer32
_RcftSHDSLPortIntervalDayUAS_Object=MibTableColumn
rcftSHDSLPortIntervalDayUAS=_RcftSHDSLPortIntervalDayUAS_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,8),_RcftSHDSLPortIntervalDayUAS_Type())
rcftSHDSLPortIntervalDayUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayUAS.setStatus(_A)
_RcftSHDSLPortIntervalDayLOSWS_Type=Integer32
_RcftSHDSLPortIntervalDayLOSWS_Object=MibTableColumn
rcftSHDSLPortIntervalDayLOSWS=_RcftSHDSLPortIntervalDayLOSWS_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,9),_RcftSHDSLPortIntervalDayLOSWS_Type())
rcftSHDSLPortIntervalDayLOSWS.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayLOSWS.setStatus(_A)
_RcftSHDSLPortIntervalDayLOFTimes_Type=Integer32
_RcftSHDSLPortIntervalDayLOFTimes_Object=MibTableColumn
rcftSHDSLPortIntervalDayLOFTimes=_RcftSHDSLPortIntervalDayLOFTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,10),_RcftSHDSLPortIntervalDayLOFTimes_Type())
rcftSHDSLPortIntervalDayLOFTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayLOFTimes.setStatus(_A)
_RcftSHDSLPortIntervalDayCRCTimes_Type=Integer32
_RcftSHDSLPortIntervalDayCRCTimes_Object=MibTableColumn
rcftSHDSLPortIntervalDayCRCTimes=_RcftSHDSLPortIntervalDayCRCTimes_Object((1,3,6,1,4,1,8886,2,1,5,10,5,2,4,1,11),_RcftSHDSLPortIntervalDayCRCTimes_Type())
rcftSHDSLPortIntervalDayCRCTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSHDSLPortIntervalDayCRCTimes.setStatus(_A)
_RcftSHDSLPortTraps_ObjectIdentity=ObjectIdentity
rcftSHDSLPortTraps=_RcftSHDSLPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,5,10))
_RcftAudioPortMib_ObjectIdentity=ObjectIdentity
rcftAudioPortMib=_RcftAudioPortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,6))
_RcftAudioPortObjects_ObjectIdentity=ObjectIdentity
rcftAudioPortObjects=_RcftAudioPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,6,1))
_RcftAudioPortTable_Object=MibTable
rcftAudioPortTable=_RcftAudioPortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,6,1,1))
if mibBuilder.loadTexts:rcftAudioPortTable.setStatus(_A)
_RcftAudioPortEntry_Object=MibTableRow
rcftAudioPortEntry=_RcftAudioPortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,6,1,1,1))
rcftAudioPortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_u))
if mibBuilder.loadTexts:rcftAudioPortEntry.setStatus(_A)
_RcftAudioPortIndex_Type=Integer32
_RcftAudioPortIndex_Object=MibTableColumn
rcftAudioPortIndex=_RcftAudioPortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,6,1,1,1,1),_RcftAudioPortIndex_Type())
rcftAudioPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftAudioPortIndex.setStatus(_A)
_RcftAudioPortStatus_Type=Integer32
_RcftAudioPortStatus_Object=MibTableColumn
rcftAudioPortStatus=_RcftAudioPortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,6,1,1,1,2),_RcftAudioPortStatus_Type())
rcftAudioPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftAudioPortStatus.setStatus(_A)
_RcftAudioPortPosition_Type=Integer32
_RcftAudioPortPosition_Object=MibTableColumn
rcftAudioPortPosition=_RcftAudioPortPosition_Object((1,3,6,1,4,1,8886,2,1,5,10,6,1,1,1,3),_RcftAudioPortPosition_Type())
rcftAudioPortPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftAudioPortPosition.setStatus(_A)
_RcftAudioPortType_Type=Integer32
_RcftAudioPortType_Object=MibTableColumn
rcftAudioPortType=_RcftAudioPortType_Object((1,3,6,1,4,1,8886,2,1,5,10,6,1,1,1,4),_RcftAudioPortType_Type())
rcftAudioPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftAudioPortType.setStatus(_A)
_RcftAudioPortPerformance_ObjectIdentity=ObjectIdentity
rcftAudioPortPerformance=_RcftAudioPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,6,2))
_RcftAudioPortTraps_ObjectIdentity=ObjectIdentity
rcftAudioPortTraps=_RcftAudioPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,6,10))
_RcftDS3E3PortMib_ObjectIdentity=ObjectIdentity
rcftDS3E3PortMib=_RcftDS3E3PortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,7))
_RcftDS3E3PortObjects_ObjectIdentity=ObjectIdentity
rcftDS3E3PortObjects=_RcftDS3E3PortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,7,1))
_RcftDS3E3PortTable_Object=MibTable
rcftDS3E3PortTable=_RcftDS3E3PortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,7,1,1))
if mibBuilder.loadTexts:rcftDS3E3PortTable.setStatus(_A)
_RcftDS3E3PortEntry_Object=MibTableRow
rcftDS3E3PortEntry=_RcftDS3E3PortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,7,1,1,1))
rcftDS3E3PortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_v))
if mibBuilder.loadTexts:rcftDS3E3PortEntry.setStatus(_A)
_RcftDS3E3PortIndex_Type=Integer32
_RcftDS3E3PortIndex_Object=MibTableColumn
rcftDS3E3PortIndex=_RcftDS3E3PortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,7,1,1,1,1),_RcftDS3E3PortIndex_Type())
rcftDS3E3PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3PortIndex.setStatus(_A)
_RcftDS3E3PortAlarmStatus_Type=Integer32
_RcftDS3E3PortAlarmStatus_Object=MibTableColumn
rcftDS3E3PortAlarmStatus=_RcftDS3E3PortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,7,1,1,1,2),_RcftDS3E3PortAlarmStatus_Type())
rcftDS3E3PortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3PortAlarmStatus.setStatus(_A)
_RcftDS3E3PortStatus_Type=Integer32
_RcftDS3E3PortStatus_Object=MibTableColumn
rcftDS3E3PortStatus=_RcftDS3E3PortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,7,1,1,1,3),_RcftDS3E3PortStatus_Type())
rcftDS3E3PortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftDS3E3PortStatus.setStatus(_A)
_RcftDS3E3PortESCont_Type=Integer32
_RcftDS3E3PortESCont_Object=MibTableColumn
rcftDS3E3PortESCont=_RcftDS3E3PortESCont_Object((1,3,6,1,4,1,8886,2,1,5,10,7,1,1,1,4),_RcftDS3E3PortESCont_Type())
rcftDS3E3PortESCont.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3PortESCont.setStatus(_A)
_RcftDS3E3PortLoopStatus_Type=Integer32
_RcftDS3E3PortLoopStatus_Object=MibTableColumn
rcftDS3E3PortLoopStatus=_RcftDS3E3PortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,7,1,1,1,5),_RcftDS3E3PortLoopStatus_Type())
rcftDS3E3PortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3PortLoopStatus.setStatus(_A)
_RcftDS3E3PortOrder_Type=Integer32
_RcftDS3E3PortOrder_Object=MibTableColumn
rcftDS3E3PortOrder=_RcftDS3E3PortOrder_Object((1,3,6,1,4,1,8886,2,1,5,10,7,1,1,1,6),_RcftDS3E3PortOrder_Type())
rcftDS3E3PortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftDS3E3PortOrder.setStatus(_A)
_RcftDS3E3PortPerformance_ObjectIdentity=ObjectIdentity
rcftDS3E3PortPerformance=_RcftDS3E3PortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,7,2))
_RcftDS3E3StatisticTable_Object=MibTable
rcftDS3E3StatisticTable=_RcftDS3E3StatisticTable_Object((1,3,6,1,4,1,8886,2,1,5,10,7,2,1))
if mibBuilder.loadTexts:rcftDS3E3StatisticTable.setStatus(_A)
_RcftDS3E3StatisticEntry_Object=MibTableRow
rcftDS3E3StatisticEntry=_RcftDS3E3StatisticEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,7,2,1,1))
if mibBuilder.loadTexts:rcftDS3E3StatisticEntry.setStatus(_A)
_RcftDS3E3TxPackets_Type=Counter32
_RcftDS3E3TxPackets_Object=MibTableColumn
rcftDS3E3TxPackets=_RcftDS3E3TxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,7,2,1,1,1),_RcftDS3E3TxPackets_Type())
rcftDS3E3TxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3TxPackets.setStatus(_A)
_RcftDS3E3TxBytes_Type=Counter32
_RcftDS3E3TxBytes_Object=MibTableColumn
rcftDS3E3TxBytes=_RcftDS3E3TxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,7,2,1,1,2),_RcftDS3E3TxBytes_Type())
rcftDS3E3TxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3TxBytes.setStatus(_A)
_RcftDS3E3TxFailurePackets_Type=Counter32
_RcftDS3E3TxFailurePackets_Object=MibTableColumn
rcftDS3E3TxFailurePackets=_RcftDS3E3TxFailurePackets_Object((1,3,6,1,4,1,8886,2,1,5,10,7,2,1,1,3),_RcftDS3E3TxFailurePackets_Type())
rcftDS3E3TxFailurePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3TxFailurePackets.setStatus(_A)
_RcftDS3E3RxPackets_Type=Counter32
_RcftDS3E3RxPackets_Object=MibTableColumn
rcftDS3E3RxPackets=_RcftDS3E3RxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,7,2,1,1,4),_RcftDS3E3RxPackets_Type())
rcftDS3E3RxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3RxPackets.setStatus(_A)
_RcftDS3E3RxBytes_Type=Counter32
_RcftDS3E3RxBytes_Object=MibTableColumn
rcftDS3E3RxBytes=_RcftDS3E3RxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,7,2,1,1,5),_RcftDS3E3RxBytes_Type())
rcftDS3E3RxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3RxBytes.setStatus(_A)
_RcftDS3E3RxErrorPackets_Type=Counter32
_RcftDS3E3RxErrorPackets_Object=MibTableColumn
rcftDS3E3RxErrorPackets=_RcftDS3E3RxErrorPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,7,2,1,1,6),_RcftDS3E3RxErrorPackets_Type())
rcftDS3E3RxErrorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3RxErrorPackets.setStatus(_A)
_RcftDS3E3FluxTimer_Type=Counter32
_RcftDS3E3FluxTimer_Object=MibTableColumn
rcftDS3E3FluxTimer=_RcftDS3E3FluxTimer_Object((1,3,6,1,4,1,8886,2,1,5,10,7,2,1,1,7),_RcftDS3E3FluxTimer_Type())
rcftDS3E3FluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS3E3FluxTimer.setStatus(_A)
_RcftDS3E3PortTraps_ObjectIdentity=ObjectIdentity
rcftDS3E3PortTraps=_RcftDS3E3PortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,7,10))
_RcftDS1PortMib_ObjectIdentity=ObjectIdentity
rcftDS1PortMib=_RcftDS1PortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,8))
_RcftDS1PortObjects_ObjectIdentity=ObjectIdentity
rcftDS1PortObjects=_RcftDS1PortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,8,1))
_RcftDS1PortTable_Object=MibTable
rcftDS1PortTable=_RcftDS1PortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1))
if mibBuilder.loadTexts:rcftDS1PortTable.setStatus(_A)
_RcftDS1PortEntry_Object=MibTableRow
rcftDS1PortEntry=_RcftDS1PortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1))
rcftDS1PortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_w))
if mibBuilder.loadTexts:rcftDS1PortEntry.setStatus(_A)
_RcftDS1PortIndex_Type=Integer32
_RcftDS1PortIndex_Object=MibTableColumn
rcftDS1PortIndex=_RcftDS1PortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,1),_RcftDS1PortIndex_Type())
rcftDS1PortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortIndex.setStatus(_A)
_RcftDS1PortAlarmStatus_Type=Integer32
_RcftDS1PortAlarmStatus_Object=MibTableColumn
rcftDS1PortAlarmStatus=_RcftDS1PortAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,2),_RcftDS1PortAlarmStatus_Type())
rcftDS1PortAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortAlarmStatus.setStatus(_A)
_RcftDS1PortStatus_Type=Integer32
_RcftDS1PortStatus_Object=MibTableColumn
rcftDS1PortStatus=_RcftDS1PortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,3),_RcftDS1PortStatus_Type())
rcftDS1PortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftDS1PortStatus.setStatus(_A)
_RcftDS1PortBertStatus_Type=Integer32
_RcftDS1PortBertStatus_Object=MibTableColumn
rcftDS1PortBertStatus=_RcftDS1PortBertStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,4),_RcftDS1PortBertStatus_Type())
rcftDS1PortBertStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortBertStatus.setStatus(_A)
_RcftDS1PortESCont_Type=Integer32
_RcftDS1PortESCont_Object=MibTableColumn
rcftDS1PortESCont=_RcftDS1PortESCont_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,5),_RcftDS1PortESCont_Type())
rcftDS1PortESCont.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortESCont.setStatus(_A)
_RcftDS1PortSESCont_Type=Integer32
_RcftDS1PortSESCont_Object=MibTableColumn
rcftDS1PortSESCont=_RcftDS1PortSESCont_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,6),_RcftDS1PortSESCont_Type())
rcftDS1PortSESCont.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortSESCont.setStatus(_A)
_RcftDS1PortLoopStatus_Type=Integer32
_RcftDS1PortLoopStatus_Object=MibTableColumn
rcftDS1PortLoopStatus=_RcftDS1PortLoopStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,7),_RcftDS1PortLoopStatus_Type())
rcftDS1PortLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortLoopStatus.setStatus(_A)
_RcftDS1PortOrder_Type=Integer32
_RcftDS1PortOrder_Object=MibTableColumn
rcftDS1PortOrder=_RcftDS1PortOrder_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,8),_RcftDS1PortOrder_Type())
rcftDS1PortOrder.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftDS1PortOrder.setStatus(_A)
_RcftDS1PortTranLength_Type=Integer32
_RcftDS1PortTranLength_Object=MibTableColumn
rcftDS1PortTranLength=_RcftDS1PortTranLength_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,9),_RcftDS1PortTranLength_Type())
rcftDS1PortTranLength.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftDS1PortTranLength.setStatus(_A)
_RcftDS1PortFaultPassIndicator_Type=Integer32
_RcftDS1PortFaultPassIndicator_Object=MibTableColumn
rcftDS1PortFaultPassIndicator=_RcftDS1PortFaultPassIndicator_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,10),_RcftDS1PortFaultPassIndicator_Type())
rcftDS1PortFaultPassIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortFaultPassIndicator.setStatus(_A)
_RcftDS1PortframeType_Type=Integer32
_RcftDS1PortframeType_Object=MibTableColumn
rcftDS1PortframeType=_RcftDS1PortframeType_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,11),_RcftDS1PortframeType_Type())
rcftDS1PortframeType.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftDS1PortframeType.setStatus(_A)
_RcftDS1PortChannel_Type=Integer32
_RcftDS1PortChannel_Object=MibTableColumn
rcftDS1PortChannel=_RcftDS1PortChannel_Object((1,3,6,1,4,1,8886,2,1,5,10,8,1,1,1,12),_RcftDS1PortChannel_Type())
rcftDS1PortChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftDS1PortChannel.setStatus(_A)
_RcftDS1PortPerformance_ObjectIdentity=ObjectIdentity
rcftDS1PortPerformance=_RcftDS1PortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,8,2))
_RcftDS1StatisticTable_Object=MibTable
rcftDS1StatisticTable=_RcftDS1StatisticTable_Object((1,3,6,1,4,1,8886,2,1,5,10,8,2,1))
if mibBuilder.loadTexts:rcftDS1StatisticTable.setStatus(_A)
_RcftDS1StatisticEntry_Object=MibTableRow
rcftDS1StatisticEntry=_RcftDS1StatisticEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,8,2,1,1))
if mibBuilder.loadTexts:rcftDS1StatisticEntry.setStatus(_A)
_RcftDS1PortTxPackets_Type=Counter32
_RcftDS1PortTxPackets_Object=MibTableColumn
rcftDS1PortTxPackets=_RcftDS1PortTxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,8,2,1,1,1),_RcftDS1PortTxPackets_Type())
rcftDS1PortTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortTxPackets.setStatus(_A)
_RcftDS1PortTxBytes_Type=Counter32
_RcftDS1PortTxBytes_Object=MibTableColumn
rcftDS1PortTxBytes=_RcftDS1PortTxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,8,2,1,1,2),_RcftDS1PortTxBytes_Type())
rcftDS1PortTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortTxBytes.setStatus(_A)
_RcftDS1PortTxFailurePackets_Type=Counter32
_RcftDS1PortTxFailurePackets_Object=MibTableColumn
rcftDS1PortTxFailurePackets=_RcftDS1PortTxFailurePackets_Object((1,3,6,1,4,1,8886,2,1,5,10,8,2,1,1,3),_RcftDS1PortTxFailurePackets_Type())
rcftDS1PortTxFailurePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortTxFailurePackets.setStatus(_A)
_RcftDS1PortRxPackets_Type=Counter32
_RcftDS1PortRxPackets_Object=MibTableColumn
rcftDS1PortRxPackets=_RcftDS1PortRxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,8,2,1,1,4),_RcftDS1PortRxPackets_Type())
rcftDS1PortRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortRxPackets.setStatus(_A)
_RcftDS1PortRxBytes_Type=Counter32
_RcftDS1PortRxBytes_Object=MibTableColumn
rcftDS1PortRxBytes=_RcftDS1PortRxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,8,2,1,1,5),_RcftDS1PortRxBytes_Type())
rcftDS1PortRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortRxBytes.setStatus(_A)
_RcftDS1PortRxErrorPackets_Type=Counter32
_RcftDS1PortRxErrorPackets_Object=MibTableColumn
rcftDS1PortRxErrorPackets=_RcftDS1PortRxErrorPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,8,2,1,1,6),_RcftDS1PortRxErrorPackets_Type())
rcftDS1PortRxErrorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortRxErrorPackets.setStatus(_A)
_RcftDS1PortFluxTimer_Type=Counter32
_RcftDS1PortFluxTimer_Object=MibTableColumn
rcftDS1PortFluxTimer=_RcftDS1PortFluxTimer_Object((1,3,6,1,4,1,8886,2,1,5,10,8,2,1,1,7),_RcftDS1PortFluxTimer_Type())
rcftDS1PortFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDS1PortFluxTimer.setStatus(_A)
_RcftDS1PortTraps_ObjectIdentity=ObjectIdentity
rcftDS1PortTraps=_RcftDS1PortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,8,10))
_RcftVideoPortMib_ObjectIdentity=ObjectIdentity
rcftVideoPortMib=_RcftVideoPortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,9))
_RcftVideoPortObjects_ObjectIdentity=ObjectIdentity
rcftVideoPortObjects=_RcftVideoPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,9,1))
_RcftVideoPortTable_Object=MibTable
rcftVideoPortTable=_RcftVideoPortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,9,1,1))
if mibBuilder.loadTexts:rcftVideoPortTable.setStatus(_A)
_RcftVideoPortEntry_Object=MibTableRow
rcftVideoPortEntry=_RcftVideoPortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,9,1,1,1))
rcftVideoPortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_x))
if mibBuilder.loadTexts:rcftVideoPortEntry.setStatus(_A)
_RcftVideoPortIndex_Type=Integer32
_RcftVideoPortIndex_Object=MibTableColumn
rcftVideoPortIndex=_RcftVideoPortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,9,1,1,1,1),_RcftVideoPortIndex_Type())
rcftVideoPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVideoPortIndex.setStatus(_A)
_RcftVideoPortStatus_Type=Integer32
_RcftVideoPortStatus_Object=MibTableColumn
rcftVideoPortStatus=_RcftVideoPortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,9,1,1,1,2),_RcftVideoPortStatus_Type())
rcftVideoPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftVideoPortStatus.setStatus(_A)
_RcftVideoPortPosition_Type=Integer32
_RcftVideoPortPosition_Object=MibTableColumn
rcftVideoPortPosition=_RcftVideoPortPosition_Object((1,3,6,1,4,1,8886,2,1,5,10,9,1,1,1,3),_RcftVideoPortPosition_Type())
rcftVideoPortPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVideoPortPosition.setStatus(_A)
_RcftVideoPortSourceID_Type=Integer32
_RcftVideoPortSourceID_Object=MibTableColumn
rcftVideoPortSourceID=_RcftVideoPortSourceID_Object((1,3,6,1,4,1,8886,2,1,5,10,9,1,1,1,4),_RcftVideoPortSourceID_Type())
rcftVideoPortSourceID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftVideoPortSourceID.setStatus(_A)
_RcftVideoPortPerformance_ObjectIdentity=ObjectIdentity
rcftVideoPortPerformance=_RcftVideoPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,9,2))
_RcftVideoPortTraps_ObjectIdentity=ObjectIdentity
rcftVideoPortTraps=_RcftVideoPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,9,10))
_RcftDataPortMib_ObjectIdentity=ObjectIdentity
rcftDataPortMib=_RcftDataPortMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,10))
_RcftDataPortObjects_ObjectIdentity=ObjectIdentity
rcftDataPortObjects=_RcftDataPortObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,10,1))
_RcftDataPortTable_Object=MibTable
rcftDataPortTable=_RcftDataPortTable_Object((1,3,6,1,4,1,8886,2,1,5,10,10,1,1))
if mibBuilder.loadTexts:rcftDataPortTable.setStatus(_A)
_RcftDataPortEntry_Object=MibTableRow
rcftDataPortEntry=_RcftDataPortEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,10,1,1,1))
rcftDataPortEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_y))
if mibBuilder.loadTexts:rcftDataPortEntry.setStatus(_A)
_RcftDataPortIndex_Type=Integer32
_RcftDataPortIndex_Object=MibTableColumn
rcftDataPortIndex=_RcftDataPortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,10,1,1,1,1),_RcftDataPortIndex_Type())
rcftDataPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDataPortIndex.setStatus(_A)
_RcftDataPortStatus_Type=Integer32
_RcftDataPortStatus_Object=MibTableColumn
rcftDataPortStatus=_RcftDataPortStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,10,1,1,1,2),_RcftDataPortStatus_Type())
rcftDataPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftDataPortStatus.setStatus(_A)
_RcftDataPortPosition_Type=Integer32
_RcftDataPortPosition_Object=MibTableColumn
rcftDataPortPosition=_RcftDataPortPosition_Object((1,3,6,1,4,1,8886,2,1,5,10,10,1,1,1,3),_RcftDataPortPosition_Type())
rcftDataPortPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDataPortPosition.setStatus(_A)
_RcftDataPortType_Type=Integer32
_RcftDataPortType_Object=MibTableColumn
rcftDataPortType=_RcftDataPortType_Object((1,3,6,1,4,1,8886,2,1,5,10,10,1,1,1,4),_RcftDataPortType_Type())
rcftDataPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftDataPortType.setStatus(_A)
_RcftDataPortPerformance_ObjectIdentity=ObjectIdentity
rcftDataPortPerformance=_RcftDataPortPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,10,2))
_RcftDataPortTraps_ObjectIdentity=ObjectIdentity
rcftDataPortTraps=_RcftDataPortTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,10,10))
_RcftSimpleModuleMib_ObjectIdentity=ObjectIdentity
rcftSimpleModuleMib=_RcftSimpleModuleMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,11))
_RcftSimpleModuleObjects_ObjectIdentity=ObjectIdentity
rcftSimpleModuleObjects=_RcftSimpleModuleObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,11,1))
_RcftSimpleModuleTable_Object=MibTable
rcftSimpleModuleTable=_RcftSimpleModuleTable_Object((1,3,6,1,4,1,8886,2,1,5,10,11,1,1))
if mibBuilder.loadTexts:rcftSimpleModuleTable.setStatus(_A)
_RcftSimpleModuleEntry_Object=MibTableRow
rcftSimpleModuleEntry=_RcftSimpleModuleEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,11,1,1,1))
rcftSimpleModuleEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_z))
if mibBuilder.loadTexts:rcftSimpleModuleEntry.setStatus(_A)
_RcftSimpleModuleIndex_Type=Integer32
_RcftSimpleModuleIndex_Object=MibTableColumn
rcftSimpleModuleIndex=_RcftSimpleModuleIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,11,1,1,1,1),_RcftSimpleModuleIndex_Type())
rcftSimpleModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSimpleModuleIndex.setStatus(_A)
_RcftSimpleModuleExist_Type=Integer32
_RcftSimpleModuleExist_Object=MibTableColumn
rcftSimpleModuleExist=_RcftSimpleModuleExist_Object((1,3,6,1,4,1,8886,2,1,5,10,11,1,1,1,2),_RcftSimpleModuleExist_Type())
rcftSimpleModuleExist.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSimpleModuleExist.setStatus(_A)
_RcftSimpleModulePosition_Type=Integer32
_RcftSimpleModulePosition_Object=MibTableColumn
rcftSimpleModulePosition=_RcftSimpleModulePosition_Object((1,3,6,1,4,1,8886,2,1,5,10,11,1,1,1,3),_RcftSimpleModulePosition_Type())
rcftSimpleModulePosition.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSimpleModulePosition.setStatus(_A)
_RcftSimpleModuleStatus_Type=Integer32
_RcftSimpleModuleStatus_Object=MibTableColumn
rcftSimpleModuleStatus=_RcftSimpleModuleStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,11,1,1,1,4),_RcftSimpleModuleStatus_Type())
rcftSimpleModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSimpleModuleStatus.setStatus(_A)
_RcftSimpleModuleType_Type=Integer32
_RcftSimpleModuleType_Object=MibTableColumn
rcftSimpleModuleType=_RcftSimpleModuleType_Object((1,3,6,1,4,1,8886,2,1,5,10,11,1,1,1,5),_RcftSimpleModuleType_Type())
rcftSimpleModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSimpleModuleType.setStatus(_A)
_RcftSimpleModulePerformance_ObjectIdentity=ObjectIdentity
rcftSimpleModulePerformance=_RcftSimpleModulePerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,11,2))
_RcftSimpleModuleTraps_ObjectIdentity=ObjectIdentity
rcftSimpleModuleTraps=_RcftSimpleModuleTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,11,10))
_RcftSlotPerformaceMib_ObjectIdentity=ObjectIdentity
rcftSlotPerformaceMib=_RcftSlotPerformaceMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,12))
_RcftSlotPerformance_ObjectIdentity=ObjectIdentity
rcftSlotPerformance=_RcftSlotPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,12,1))
_RcftSlotStatisticTable_Object=MibTable
rcftSlotStatisticTable=_RcftSlotStatisticTable_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1))
if mibBuilder.loadTexts:rcftSlotStatisticTable.setStatus(_A)
_RcftSlotStatisticEntry_Object=MibTableRow
rcftSlotStatisticEntry=_RcftSlotStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1))
rcftSlotStatisticEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_A0))
if mibBuilder.loadTexts:rcftSlotStatisticEntry.setStatus(_A)
_RcftPortIndex_Type=Integer32
_RcftPortIndex_Object=MibTableColumn
rcftPortIndex=_RcftPortIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,1),_RcftPortIndex_Type())
rcftPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPortIndex.setStatus(_A)
_RcftPortType_Type=Integer32
_RcftPortType_Object=MibTableColumn
rcftPortType=_RcftPortType_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,2),_RcftPortType_Type())
rcftPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftPortType.setStatus(_A)
_RcftRxPackets_Type=Counter32
_RcftRxPackets_Object=MibTableColumn
rcftRxPackets=_RcftRxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,3),_RcftRxPackets_Type())
rcftRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRxPackets.setStatus(_A)
_RcftRxLosPackets_Type=Counter32
_RcftRxLosPackets_Object=MibTableColumn
rcftRxLosPackets=_RcftRxLosPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,4),_RcftRxLosPackets_Type())
rcftRxLosPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRxLosPackets.setStatus(_A)
_RcftRxPreabErrPackets_Type=Counter32
_RcftRxPreabErrPackets_Object=MibTableColumn
rcftRxPreabErrPackets=_RcftRxPreabErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,5),_RcftRxPreabErrPackets_Type())
rcftRxPreabErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRxPreabErrPackets.setStatus(_A)
_RcftRxFCSErrPackets_Type=Counter32
_RcftRxFCSErrPackets_Object=MibTableColumn
rcftRxFCSErrPackets=_RcftRxFCSErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,6),_RcftRxFCSErrPackets_Type())
rcftRxFCSErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRxFCSErrPackets.setStatus(_A)
_RcftRxUnderSizePackets_Type=Counter32
_RcftRxUnderSizePackets_Object=MibTableColumn
rcftRxUnderSizePackets=_RcftRxUnderSizePackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,7),_RcftRxUnderSizePackets_Type())
rcftRxUnderSizePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRxUnderSizePackets.setStatus(_A)
_RcftRxOverSizePackets_Type=Counter32
_RcftRxOverSizePackets_Object=MibTableColumn
rcftRxOverSizePackets=_RcftRxOverSizePackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,8),_RcftRxOverSizePackets_Type())
rcftRxOverSizePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRxOverSizePackets.setStatus(_A)
_RcftRxPausePackets_Type=Counter32
_RcftRxPausePackets_Object=MibTableColumn
rcftRxPausePackets=_RcftRxPausePackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,9),_RcftRxPausePackets_Type())
rcftRxPausePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRxPausePackets.setStatus(_A)
_RcftRxOamPackets_Type=Counter32
_RcftRxOamPackets_Object=MibTableColumn
rcftRxOamPackets=_RcftRxOamPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,10),_RcftRxOamPackets_Type())
rcftRxOamPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRxOamPackets.setStatus(_A)
_RcftRxBytes_Type=Counter32
_RcftRxBytes_Object=MibTableColumn
rcftRxBytes=_RcftRxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,11),_RcftRxBytes_Type())
rcftRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftRxBytes.setStatus(_A)
_RcftTxPackets_Type=Counter32
_RcftTxPackets_Object=MibTableColumn
rcftTxPackets=_RcftTxPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,12),_RcftTxPackets_Type())
rcftTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftTxPackets.setStatus(_A)
_RcftTxFCSErrPackets_Type=Counter32
_RcftTxFCSErrPackets_Object=MibTableColumn
rcftTxFCSErrPackets=_RcftTxFCSErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,13),_RcftTxFCSErrPackets_Type())
rcftTxFCSErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftTxFCSErrPackets.setStatus(_A)
_RcftTxPausePackets_Type=Counter32
_RcftTxPausePackets_Object=MibTableColumn
rcftTxPausePackets=_RcftTxPausePackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,14),_RcftTxPausePackets_Type())
rcftTxPausePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftTxPausePackets.setStatus(_A)
_RcftTxOamPackets_Type=Counter32
_RcftTxOamPackets_Object=MibTableColumn
rcftTxOamPackets=_RcftTxOamPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,15),_RcftTxOamPackets_Type())
rcftTxOamPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftTxOamPackets.setStatus(_A)
_RcftTxBytes_Type=Counter32
_RcftTxBytes_Object=MibTableColumn
rcftTxBytes=_RcftTxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,16),_RcftTxBytes_Type())
rcftTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftTxBytes.setStatus(_A)
_RcftFluxTimer_Type=Counter32
_RcftFluxTimer_Object=MibTableColumn
rcftFluxTimer=_RcftFluxTimer_Object((1,3,6,1,4,1,8886,2,1,5,10,12,1,1,1,17),_RcftFluxTimer_Type())
rcftFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftFluxTimer.setStatus(_A)
_RcftSlotVCGMib_ObjectIdentity=ObjectIdentity
rcftSlotVCGMib=_RcftSlotVCGMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,13))
_RcftSlotVCGObjects_ObjectIdentity=ObjectIdentity
rcftSlotVCGObjects=_RcftSlotVCGObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,13,1))
_RcftSlotVCGTable_Object=MibTable
rcftSlotVCGTable=_RcftSlotVCGTable_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1))
if mibBuilder.loadTexts:rcftSlotVCGTable.setStatus(_A)
_RcftSlotVCGEntry_Object=MibTableRow
rcftSlotVCGEntry=_RcftSlotVCGEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1))
rcftSlotVCGEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_A1))
if mibBuilder.loadTexts:rcftSlotVCGEntry.setStatus(_A)
_RcftSlotVCGIndex_Type=Integer32
_RcftSlotVCGIndex_Object=MibTableColumn
rcftSlotVCGIndex=_RcftSlotVCGIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,1),_RcftSlotVCGIndex_Type())
rcftSlotVCGIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGIndex.setStatus(_A)
_RcftSlotVCGStatus_Type=Integer32
_RcftSlotVCGStatus_Object=MibTableColumn
rcftSlotVCGStatus=_RcftSlotVCGStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,2),_RcftSlotVCGStatus_Type())
rcftSlotVCGStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVCGStatus.setStatus(_A)
_RcftSlotVCGLoopStatus_Type=Integer32
_RcftSlotVCGLoopStatus_Object=MibTableColumn
rcftSlotVCGLoopStatus=_RcftSlotVCGLoopStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,3),_RcftSlotVCGLoopStatus_Type())
rcftSlotVCGLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGLoopStatus.setStatus(_A)
_RcftSlotVCGLcasXPR_Type=Integer32
_RcftSlotVCGLcasXPR_Object=MibTableColumn
rcftSlotVCGLcasXPR=_RcftSlotVCGLcasXPR_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,4),_RcftSlotVCGLcasXPR_Type())
rcftSlotVCGLcasXPR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGLcasXPR.setStatus(_A)
_RcftSlotVCGLcasXAR_Type=Integer32
_RcftSlotVCGLcasXAR_Object=MibTableColumn
rcftSlotVCGLcasXAR=_RcftSlotVCGLcasXAR_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,5),_RcftSlotVCGLcasXAR_Type())
rcftSlotVCGLcasXAR.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGLcasXAR.setStatus(_A)
_RcftSlotVCGLcasXPT_Type=Integer32
_RcftSlotVCGLcasXPT_Object=MibTableColumn
rcftSlotVCGLcasXPT=_RcftSlotVCGLcasXPT_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,6),_RcftSlotVCGLcasXPT_Type())
rcftSlotVCGLcasXPT.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGLcasXPT.setStatus(_A)
_RcftSlotVCGLcasXAT_Type=Integer32
_RcftSlotVCGLcasXAT_Object=MibTableColumn
rcftSlotVCGLcasXAT=_RcftSlotVCGLcasXAT_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,7),_RcftSlotVCGLcasXAT_Type())
rcftSlotVCGLcasXAT.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGLcasXAT.setStatus(_A)
_RcftSlotVCGAlarmStatus_Type=Integer32
_RcftSlotVCGAlarmStatus_Object=MibTableColumn
rcftSlotVCGAlarmStatus=_RcftSlotVCGAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,8),_RcftSlotVCGAlarmStatus_Type())
rcftSlotVCGAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGAlarmStatus.setStatus(_A)
_RcftSlotVCGTxISPTPID_Type=Integer32
_RcftSlotVCGTxISPTPID_Object=MibTableColumn
rcftSlotVCGTxISPTPID=_RcftSlotVCGTxISPTPID_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,9),_RcftSlotVCGTxISPTPID_Type())
rcftSlotVCGTxISPTPID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVCGTxISPTPID.setStatus(_A)
_RcftSlotVCGRxISPTPID_Type=Integer32
_RcftSlotVCGRxISPTPID_Object=MibTableColumn
rcftSlotVCGRxISPTPID=_RcftSlotVCGRxISPTPID_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,10),_RcftSlotVCGRxISPTPID_Type())
rcftSlotVCGRxISPTPID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVCGRxISPTPID.setStatus(_A)
_RcftSlotVCGBaseCoS_Type=Integer32
_RcftSlotVCGBaseCoS_Object=MibTableColumn
rcftSlotVCGBaseCoS=_RcftSlotVCGBaseCoS_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,11),_RcftSlotVCGBaseCoS_Type())
rcftSlotVCGBaseCoS.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVCGBaseCoS.setStatus(_A)
_RcftSlotVCGVLANID_Type=Integer32
_RcftSlotVCGVLANID_Object=MibTableColumn
rcftSlotVCGVLANID=_RcftSlotVCGVLANID_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,12),_RcftSlotVCGVLANID_Type())
rcftSlotVCGVLANID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVCGVLANID.setStatus(_A)
class _RcftSlotVCGMemberList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftSlotVCGMemberList_Type.__name__=_K
_RcftSlotVCGMemberList_Object=MibTableColumn
rcftSlotVCGMemberList=_RcftSlotVCGMemberList_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,13),_RcftSlotVCGMemberList_Type())
rcftSlotVCGMemberList.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVCGMemberList.setStatus(_A)
class _RcftSlotToRVCGMemberList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftSlotToRVCGMemberList_Type.__name__=_K
_RcftSlotToRVCGMemberList_Object=MibTableColumn
rcftSlotToRVCGMemberList=_RcftSlotToRVCGMemberList_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,14),_RcftSlotToRVCGMemberList_Type())
rcftSlotToRVCGMemberList.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotToRVCGMemberList.setStatus(_A)
class _RcftSlotVCGMemberStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftSlotVCGMemberStatus_Type.__name__=_K
_RcftSlotVCGMemberStatus_Object=MibTableColumn
rcftSlotVCGMemberStatus=_RcftSlotVCGMemberStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,15),_RcftSlotVCGMemberStatus_Type())
rcftSlotVCGMemberStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVCGMemberStatus.setStatus(_A)
class _RcftSlotVCGMemberRxCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftSlotVCGMemberRxCode_Type.__name__=_K
_RcftSlotVCGMemberRxCode_Object=MibTableColumn
rcftSlotVCGMemberRxCode=_RcftSlotVCGMemberRxCode_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,16),_RcftSlotVCGMemberRxCode_Type())
rcftSlotVCGMemberRxCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGMemberRxCode.setStatus(_A)
class _RcftSlotVCGMemberTxCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftSlotVCGMemberTxCode_Type.__name__=_K
_RcftSlotVCGMemberTxCode_Object=MibTableColumn
rcftSlotVCGMemberTxCode=_RcftSlotVCGMemberTxCode_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,17),_RcftSlotVCGMemberTxCode_Type())
rcftSlotVCGMemberTxCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGMemberTxCode.setStatus(_A)
class _RcftSlotVCGMemberAlarmStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftSlotVCGMemberAlarmStatus_Type.__name__=_K
_RcftSlotVCGMemberAlarmStatus_Object=MibTableColumn
rcftSlotVCGMemberAlarmStatus=_RcftSlotVCGMemberAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,18),_RcftSlotVCGMemberAlarmStatus_Type())
rcftSlotVCGMemberAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVCGMemberAlarmStatus.setStatus(_A)
class _RcftSlotToRVCGMemberAlarmStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_RcftSlotToRVCGMemberAlarmStatus_Type.__name__=_K
_RcftSlotToRVCGMemberAlarmStatus_Object=MibTableColumn
rcftSlotToRVCGMemberAlarmStatus=_RcftSlotToRVCGMemberAlarmStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,13,1,1,1,19),_RcftSlotToRVCGMemberAlarmStatus_Type())
rcftSlotToRVCGMemberAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotToRVCGMemberAlarmStatus.setStatus(_A)
_RcftSlotVCGPerformance_ObjectIdentity=ObjectIdentity
rcftSlotVCGPerformance=_RcftSlotVCGPerformance_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,13,2))
_RcftSlotVCGStatisticTable_Object=MibTable
rcftSlotVCGStatisticTable=_RcftSlotVCGStatisticTable_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1))
if mibBuilder.loadTexts:rcftSlotVCGStatisticTable.setStatus(_A)
_RcftSlotVCGStatisticEntry_Object=MibTableRow
rcftSlotVCGStatisticEntry=_RcftSlotVCGStatisticEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1))
if mibBuilder.loadTexts:rcftSlotVCGStatisticEntry.setStatus(_A)
_RcftVCGRxClientPackets_Type=Counter32
_RcftVCGRxClientPackets_Object=MibTableColumn
rcftVCGRxClientPackets=_RcftVCGRxClientPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,1),_RcftVCGRxClientPackets_Type())
rcftVCGRxClientPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxClientPackets.setStatus(_A)
_RcftVCGRxIdlePackets_Type=Counter32
_RcftVCGRxIdlePackets_Object=MibTableColumn
rcftVCGRxIdlePackets=_RcftVCGRxIdlePackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,2),_RcftVCGRxIdlePackets_Type())
rcftVCGRxIdlePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxIdlePackets.setStatus(_A)
_RcftVCGRxMgmntPackets_Type=Counter32
_RcftVCGRxMgmntPackets_Object=MibTableColumn
rcftVCGRxMgmntPackets=_RcftVCGRxMgmntPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,3),_RcftVCGRxMgmntPackets_Type())
rcftVCGRxMgmntPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxMgmntPackets.setStatus(_A)
_RcftVCGRxFCSErrMgmntPackets_Type=Counter32
_RcftVCGRxFCSErrMgmntPackets_Object=MibTableColumn
rcftVCGRxFCSErrMgmntPackets=_RcftVCGRxFCSErrMgmntPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,4),_RcftVCGRxFCSErrMgmntPackets_Type())
rcftVCGRxFCSErrMgmntPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxFCSErrMgmntPackets.setStatus(_A)
_RcftVCGRxLenErrPackets_Type=Counter32
_RcftVCGRxLenErrPackets_Object=MibTableColumn
rcftVCGRxLenErrPackets=_RcftVCGRxLenErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,5),_RcftVCGRxLenErrPackets_Type())
rcftVCGRxLenErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxLenErrPackets.setStatus(_A)
_RcftVCGRxFCSErrClientPackets_Type=Counter32
_RcftVCGRxFCSErrClientPackets_Object=MibTableColumn
rcftVCGRxFCSErrClientPackets=_RcftVCGRxFCSErrClientPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,6),_RcftVCGRxFCSErrClientPackets_Type())
rcftVCGRxFCSErrClientPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxFCSErrClientPackets.setStatus(_A)
_RcftVCGRxThecErrPackets_Type=Counter32
_RcftVCGRxThecErrPackets_Object=MibTableColumn
rcftVCGRxThecErrPackets=_RcftVCGRxThecErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,7),_RcftVCGRxThecErrPackets_Type())
rcftVCGRxThecErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxThecErrPackets.setStatus(_A)
_RcftVCGRxEhecErrPackets_Type=Counter32
_RcftVCGRxEhecErrPackets_Object=MibTableColumn
rcftVCGRxEhecErrPackets=_RcftVCGRxEhecErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,8),_RcftVCGRxEhecErrPackets_Type())
rcftVCGRxEhecErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxEhecErrPackets.setStatus(_A)
_RcftVCGRxCIDErrPackets_Type=Counter32
_RcftVCGRxCIDErrPackets_Object=MibTableColumn
rcftVCGRxCIDErrPackets=_RcftVCGRxCIDErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,9),_RcftVCGRxCIDErrPackets_Type())
rcftVCGRxCIDErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxCIDErrPackets.setStatus(_A)
_RcftVCGRxSpareErrPackets_Type=Counter32
_RcftVCGRxSpareErrPackets_Object=MibTableColumn
rcftVCGRxSpareErrPackets=_RcftVCGRxSpareErrPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,10),_RcftVCGRxSpareErrPackets_Type())
rcftVCGRxSpareErrPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxSpareErrPackets.setStatus(_A)
_RcftVCGRxChecCorPackets_Type=Counter32
_RcftVCGRxChecCorPackets_Object=MibTableColumn
rcftVCGRxChecCorPackets=_RcftVCGRxChecCorPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,11),_RcftVCGRxChecCorPackets_Type())
rcftVCGRxChecCorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxChecCorPackets.setStatus(_A)
_RcftVCGRxThecCorPackets_Type=Counter32
_RcftVCGRxThecCorPackets_Object=MibTableColumn
rcftVCGRxThecCorPackets=_RcftVCGRxThecCorPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,12),_RcftVCGRxThecCorPackets_Type())
rcftVCGRxThecCorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxThecCorPackets.setStatus(_A)
_RcftVCGRxEhecCorPackets_Type=Counter32
_RcftVCGRxEhecCorPackets_Object=MibTableColumn
rcftVCGRxEhecCorPackets=_RcftVCGRxEhecCorPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,13),_RcftVCGRxEhecCorPackets_Type())
rcftVCGRxEhecCorPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxEhecCorPackets.setStatus(_A)
_RcftVCGRxBytes_Type=Counter32
_RcftVCGRxBytes_Object=MibTableColumn
rcftVCGRxBytes=_RcftVCGRxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,14),_RcftVCGRxBytes_Type())
rcftVCGRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGRxBytes.setStatus(_A)
_RcftVCGTxClientPackets_Type=Counter32
_RcftVCGTxClientPackets_Object=MibTableColumn
rcftVCGTxClientPackets=_RcftVCGTxClientPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,15),_RcftVCGTxClientPackets_Type())
rcftVCGTxClientPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGTxClientPackets.setStatus(_A)
_RcftVCGTxIdlePackets_Type=Counter32
_RcftVCGTxIdlePackets_Object=MibTableColumn
rcftVCGTxIdlePackets=_RcftVCGTxIdlePackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,16),_RcftVCGTxIdlePackets_Type())
rcftVCGTxIdlePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGTxIdlePackets.setStatus(_A)
_RcftVCGTxMgmntPackets_Type=Counter32
_RcftVCGTxMgmntPackets_Object=MibTableColumn
rcftVCGTxMgmntPackets=_RcftVCGTxMgmntPackets_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,17),_RcftVCGTxMgmntPackets_Type())
rcftVCGTxMgmntPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGTxMgmntPackets.setStatus(_A)
_RcftVCGTxBytes_Type=Counter32
_RcftVCGTxBytes_Object=MibTableColumn
rcftVCGTxBytes=_RcftVCGTxBytes_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,18),_RcftVCGTxBytes_Type())
rcftVCGTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGTxBytes.setStatus(_A)
_RcftVCGFluxTimer_Type=Counter32
_RcftVCGFluxTimer_Object=MibTableColumn
rcftVCGFluxTimer=_RcftVCGFluxTimer_Object((1,3,6,1,4,1,8886,2,1,5,10,13,2,1,1,19),_RcftVCGFluxTimer_Type())
rcftVCGFluxTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftVCGFluxTimer.setStatus(_A)
_RcftSlotVCGTraps_ObjectIdentity=ObjectIdentity
rcftSlotVCGTraps=_RcftSlotVCGTraps_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,13,10))
_RcftSlotVLANMib_ObjectIdentity=ObjectIdentity
rcftSlotVLANMib=_RcftSlotVLANMib_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,14))
_RcftSlotVLANObjects_ObjectIdentity=ObjectIdentity
rcftSlotVLANObjects=_RcftSlotVLANObjects_ObjectIdentity((1,3,6,1,4,1,8886,2,1,5,10,14,1))
_RcftSlotVLANTable_Object=MibTable
rcftSlotVLANTable=_RcftSlotVLANTable_Object((1,3,6,1,4,1,8886,2,1,5,10,14,1,1))
if mibBuilder.loadTexts:rcftSlotVLANTable.setStatus(_A)
_RcftSlotVLANEntry_Object=MibTableRow
rcftSlotVLANEntry=_RcftSlotVLANEntry_Object((1,3,6,1,4,1,8886,2,1,5,10,14,1,1,1))
rcftSlotVLANEntry.setIndexNames((0,_E,_F),(0,_E,_G),(0,_C,_A2))
if mibBuilder.loadTexts:rcftSlotVLANEntry.setStatus(_A)
_RcftSlotVLANIndex_Type=Integer32
_RcftSlotVLANIndex_Object=MibTableColumn
rcftSlotVLANIndex=_RcftSlotVLANIndex_Object((1,3,6,1,4,1,8886,2,1,5,10,14,1,1,1,1),_RcftSlotVLANIndex_Type())
rcftSlotVLANIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcftSlotVLANIndex.setStatus(_A)
_RcftSlotVLANStatus_Type=Integer32
_RcftSlotVLANStatus_Object=MibTableColumn
rcftSlotVLANStatus=_RcftSlotVLANStatus_Object((1,3,6,1,4,1,8886,2,1,5,10,14,1,1,1,2),_RcftSlotVLANStatus_Type())
rcftSlotVLANStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVLANStatus.setStatus(_A)
_RcftSlotVLANmember_Type=Integer32
_RcftSlotVLANmember_Object=MibTableColumn
rcftSlotVLANmember=_RcftSlotVLANmember_Object((1,3,6,1,4,1,8886,2,1,5,10,14,1,1,1,3),_RcftSlotVLANmember_Type())
rcftSlotVLANmember.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVLANmember.setStatus(_A)
_RcftSlotVID_Type=Integer32
_RcftSlotVID_Object=MibTableColumn
rcftSlotVID=_RcftSlotVID_Object((1,3,6,1,4,1,8886,2,1,5,10,14,1,1,1,4),_RcftSlotVID_Type())
rcftSlotVID.setMaxAccess(_D)
if mibBuilder.loadTexts:rcftSlotVID.setStatus(_A)
rcftEthFxPortEntry.registerAugmentions((_C,_A3))
rcftEthFxStatisticEntry.setIndexNames(*rcftEthFxPortEntry.getIndexNames())
rcftEthFePortEntry.registerAugmentions((_C,_A4))
rcftEthFeStatisticEntry.setIndexNames(*rcftEthFePortEntry.getIndexNames())
rcftDS3E3PortEntry.registerAugmentions((_C,_A5))
rcftDS3E3StatisticEntry.setIndexNames(*rcftDS3E3PortEntry.getIndexNames())
rcftDS1PortEntry.registerAugmentions((_C,_A6))
rcftDS1StatisticEntry.setIndexNames(*rcftDS1PortEntry.getIndexNames())
rcftSlotVCGEntry.registerAugmentions((_C,_A7))
rcftSlotVCGStatisticEntry.setIndexNames(*rcftSlotVCGEntry.getIndexNames())
rcftEthFxPortLinkTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,1))
rcftEthFxPortLinkTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftEthFxPortLinkTrap.setStatus(_A)
rcftEthFxPortExitTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,2))
rcftEthFxPortExitTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftEthFxPortExitTrap.setStatus(_A)
rcftEthFxPortTempHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,3))
rcftEthFxPortTempHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortTempHighTrap.setStatus(_A)
rcftEthFxPortTempLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,4))
rcftEthFxPortTempLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortTempLowTrap.setStatus(_A)
rcftEthFxPortVoltageHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,5))
rcftEthFxPortVoltageHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortVoltageHighTrap.setStatus(_A)
rcftEthFxPortVoltageLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,6))
rcftEthFxPortVoltageLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortVoltageLowTrap.setStatus(_A)
rcftEthFxPortOffsetCurrHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,7))
rcftEthFxPortOffsetCurrHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortOffsetCurrHighTrap.setStatus(_A)
rcftEthFxPortOffsetCurrLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,8))
rcftEthFxPortOffsetCurrLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortOffsetCurrLowTrap.setStatus(_A)
rcftEthFxPortSendPowerHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,9))
rcftEthFxPortSendPowerHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortSendPowerHighTrap.setStatus(_A)
rcftEthFxPortSendPowerLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,10))
rcftEthFxPortSendPowerLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortSendPowerLowTrap.setStatus(_A)
rcftEthFxPortRecvPowerHighTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,11))
rcftEthFxPortRecvPowerHighTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortRecvPowerHighTrap.setStatus(_A)
rcftEthFxPortRecvPowerLowTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,12))
rcftEthFxPortRecvPowerLowTrap.setObjects((_C,_M))
if mibBuilder.loadTexts:rcftEthFxPortRecvPowerLowTrap.setStatus(_A)
rcftEthFxPortTempHighWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,13))
rcftEthFxPortTempHighWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortTempHighWarningTrap.setStatus(_A)
rcftEthFxPortTempLowWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,14))
rcftEthFxPortTempLowWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortTempLowWarningTrap.setStatus(_A)
rcftEthFxPortVoltageHighWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,15))
rcftEthFxPortVoltageHighWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortVoltageHighWarningTrap.setStatus(_A)
rcftEthFxPortVoltageLowWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,16))
rcftEthFxPortVoltageLowWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortVoltageLowWarningTrap.setStatus(_A)
rcftEthFxPortOffsetCurrHighWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,17))
rcftEthFxPortOffsetCurrHighWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortOffsetCurrHighWarningTrap.setStatus(_A)
rcftEthFxPortOffsetCurrLowWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,18))
rcftEthFxPortOffsetCurrLowWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortOffsetCurrLowWarningTrap.setStatus(_A)
rcftEthFxPortSendPowerHighWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,19))
rcftEthFxPortSendPowerHighWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortSendPowerHighWarningTrap.setStatus(_A)
rcftEthFxPortSendPowerLowWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,20))
rcftEthFxPortSendPowerLowWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortSendPowerLowWarningTrap.setStatus(_A)
rcftEthFxPortRecvPowerHighWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,21))
rcftEthFxPortRecvPowerHighWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortRecvPowerHighWarningTrap.setStatus(_A)
rcftEthFxPortRecvPowerLowWarningTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,22))
rcftEthFxPortRecvPowerLowWarningTrap.setObjects((_C,_N))
if mibBuilder.loadTexts:rcftEthFxPortRecvPowerLowWarningTrap.setStatus(_A)
rcftEthFxPortSDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,23))
rcftEthFxPortSDTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftEthFxPortSDTrap.setStatus(_A)
rcftEthFxPortRemotePowerDownTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,24))
rcftEthFxPortRemotePowerDownTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftEthFxPortRemotePowerDownTrap.setStatus(_A)
rcftEthFxPortLaserTxfaultTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,25))
rcftEthFxPortLaserTxfaultTrap.setObjects((_C,_Y))
if mibBuilder.loadTexts:rcftEthFxPortLaserTxfaultTrap.setStatus(_A)
rcftEthFxPortInputSignalLosTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,26))
rcftEthFxPortInputSignalLosTrap.setObjects((_C,_Y))
if mibBuilder.loadTexts:rcftEthFxPortInputSignalLosTrap.setStatus(_A)
rcftEthFxPortLOLTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,27))
rcftEthFxPortLOLTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftEthFxPortLOLTrap.setStatus(_A)
rcftEthFxPortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,1,10,28))
rcftEthFxPortLOSTrap.setObjects((_C,_S))
if mibBuilder.loadTexts:rcftEthFxPortLOSTrap.setStatus(_A)
rcftEthFePortLinkTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,1,2,10,1))
rcftEthFePortLinkTrap.setObjects((_C,_A8))
if mibBuilder.loadTexts:rcftEthFePortLinkTrap.setStatus(_A)
rcftPdhPortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,2,10,1))
rcftPdhPortLOSTrap.setObjects((_C,_O))
if mibBuilder.loadTexts:rcftPdhPortLOSTrap.setStatus(_A)
rcftPdhPortLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,2,10,2))
rcftPdhPortLOFTrap.setObjects((_C,_O))
if mibBuilder.loadTexts:rcftPdhPortLOFTrap.setStatus(_A)
rcftPdhPortE3Trap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,2,10,3))
rcftPdhPortE3Trap.setObjects((_C,_O))
if mibBuilder.loadTexts:rcftPdhPortE3Trap.setStatus(_A)
rcftPdhPortE6Trap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,2,10,4))
rcftPdhPortE6Trap.setObjects((_C,_O))
if mibBuilder.loadTexts:rcftPdhPortE6Trap.setStatus(_A)
rcftPdhPortToRLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,2,10,5))
rcftPdhPortToRLOSTrap.setObjects((_C,_O))
if mibBuilder.loadTexts:rcftPdhPortToRLOSTrap.setStatus(_A)
rcftPdhPortToRLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,2,10,6))
rcftPdhPortToRLOFTrap.setObjects((_C,_O))
if mibBuilder.loadTexts:rcftPdhPortToRLOFTrap.setStatus(_A)
rcftPdhPortToRE3Trap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,2,10,7))
rcftPdhPortToRE3Trap.setObjects((_C,_O))
if mibBuilder.loadTexts:rcftPdhPortToRE3Trap.setStatus(_A)
rcftPdhPortToRE6Trap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,2,10,8))
rcftPdhPortToRE6Trap.setObjects((_C,_O))
if mibBuilder.loadTexts:rcftPdhPortToRE6Trap.setStatus(_A)
rcftPdhPortToRPowerDown=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,2,10,9))
rcftPdhPortToRPowerDown.setObjects((_C,_O))
if mibBuilder.loadTexts:rcftPdhPortToRPowerDown.setStatus(_A)
rcftE1PortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,1))
rcftE1PortLOSTrap.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftE1PortLOSTrap.setStatus(_A)
rcftE1PortAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,2))
rcftE1PortAISTrap.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftE1PortAISTrap.setStatus(_A)
rcftE1PortCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,3))
rcftE1PortCVTrap.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftE1PortCVTrap.setStatus(_A)
rcftE1PortLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,4))
rcftE1PortLOFTrap.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftE1PortLOFTrap.setStatus(_A)
rcftE1PortLOMFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,5))
rcftE1PortLOMFTrap.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftE1PortLOMFTrap.setStatus(_A)
rcftE1PortCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,6))
rcftE1PortCRCTrap.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftE1PortCRCTrap.setStatus(_A)
rcftE1PortToRLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,7))
rcftE1PortToRLOSTrap.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftE1PortToRLOSTrap.setStatus(_A)
rcftT1PortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,8))
rcftT1PortLOSTrap.setObjects((_C,_P))
if mibBuilder.loadTexts:rcftT1PortLOSTrap.setStatus(_A)
rcftT1PortAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,9))
rcftT1PortAISTrap.setObjects((_C,_P))
if mibBuilder.loadTexts:rcftT1PortAISTrap.setStatus(_A)
rcftE1PortTSDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,10))
rcftE1PortTSDTrap.setObjects((_C,_P))
if mibBuilder.loadTexts:rcftE1PortTSDTrap.setStatus(_A)
rcftE1PortTransErrorCodeMore10E_3=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,11))
rcftE1PortTransErrorCodeMore10E_3.setObjects((_C,_Z))
if mibBuilder.loadTexts:rcftE1PortTransErrorCodeMore10E_3.setStatus(_A)
rcftE1PortTransErrorCodeMore10E_6=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,12))
rcftE1PortTransErrorCodeMore10E_6.setObjects((_C,_Z))
if mibBuilder.loadTexts:rcftE1PortTransErrorCodeMore10E_6.setStatus(_A)
rcftE1PortRDITrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,13))
rcftE1PortRDITrap.setObjects((_C,_P))
if mibBuilder.loadTexts:rcftE1PortRDITrap.setStatus(_A)
rcftE1PortToRAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,14))
rcftE1PortToRAISTrap.setObjects((_C,_P))
if mibBuilder.loadTexts:rcftE1PortToRAISTrap.setStatus(_A)
rcftE1PortToRLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,15))
rcftE1PortToRLOFTrap.setObjects((_C,_P))
if mibBuilder.loadTexts:rcftE1PortToRLOFTrap.setStatus(_A)
rcftE1PortToRCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,16))
rcftE1PortToRCRCTrap.setObjects((_C,_P))
if mibBuilder.loadTexts:rcftE1PortToRCRCTrap.setStatus(_A)
rcftE1PortToRTSDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,17))
rcftE1PortToRTSDTrap.setObjects((_C,_P))
if mibBuilder.loadTexts:rcftE1PortToRTSDTrap.setStatus(_A)
rcftE1PortToRLOMFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,18))
rcftE1PortToRLOMFTrap.setObjects((_C,_P))
if mibBuilder.loadTexts:rcftE1PortToRLOMFTrap.setStatus(_A)
rcftE1PortTransErrorCodeMoreToR10E_3=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,3,10,19))
rcftE1PortTransErrorCodeMoreToR10E_3.setObjects((_C,_R))
if mibBuilder.loadTexts:rcftE1PortTransErrorCodeMoreToR10E_3.setStatus(_A)
rcftV35PortDCDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,1))
rcftV35PortDCDTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortDCDTrap.setStatus(_A)
rcftV35PortCTSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,2))
rcftV35PortCTSTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortCTSTrap.setStatus(_A)
rcftV35PortDTRTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,3))
rcftV35PortDTRTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortDTRTrap.setStatus(_A)
rcftV35PortRTSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,4))
rcftV35PortRTSTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortRTSTrap.setStatus(_A)
rcftV35PortCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,5))
rcftV35PortCRCTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortCRCTrap.setStatus(_A)
rcftV35PortPATTTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,6))
rcftV35PortPATTTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortPATTTrap.setStatus(_A)
rcftV35PortLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,7))
rcftV35PortLOFTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortLOFTrap.setStatus(_A)
rcftV35PortCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,8))
rcftV35PortCVTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortCVTrap.setStatus(_A)
rcftV35PortAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,9))
rcftV35PortAISTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortAISTrap.setStatus(_A)
rcftV35PortToRLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,10))
rcftV35PortToRLOFTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortToRLOFTrap.setStatus(_A)
rcftV35PortToRCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,11))
rcftV35PortToRCVTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortToRCVTrap.setStatus(_A)
rcftV35PortToRAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,12))
rcftV35PortToRAISTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortToRAISTrap.setStatus(_A)
rcftV35PortDSRTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,4,10,13))
rcftV35PortDSRTrap.setObjects((_C,_I))
if mibBuilder.loadTexts:rcftV35PortDSRTrap.setStatus(_A)
rcftSHDSLPortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,1))
rcftSHDSLPortLOSTrap.setObjects((_C,_U))
if mibBuilder.loadTexts:rcftSHDSLPortLOSTrap.setStatus(_A)
rcftSHDSLPortLOSWTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,2))
rcftSHDSLPortLOSWTrap.setObjects((_C,_U))
if mibBuilder.loadTexts:rcftSHDSLPortLOSWTrap.setStatus(_A)
rcftSHDSLPortLINKTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,3))
rcftSHDSLPortLINKTrap.setObjects((_C,_U))
if mibBuilder.loadTexts:rcftSHDSLPortLINKTrap.setStatus(_A)
rcftSHDSLPortFECTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,4))
rcftSHDSLPortFECTrap.setObjects((_C,_U))
if mibBuilder.loadTexts:rcftSHDSLPortFECTrap.setStatus(_A)
rcftSHDSLPortCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,5))
rcftSHDSLPortCRCTrap.setObjects((_C,_U))
if mibBuilder.loadTexts:rcftSHDSLPortCRCTrap.setStatus(_A)
rcftSHDSLPortSNRThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,6))
rcftSHDSLPortSNRThresholdTrap.setObjects((_C,_A9))
if mibBuilder.loadTexts:rcftSHDSLPortSNRThresholdTrap.setStatus(_A)
rcftSHDSLPortAttenuationThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,7))
rcftSHDSLPortAttenuationThresholdTrap.setObjects((_C,_AA))
if mibBuilder.loadTexts:rcftSHDSLPortAttenuationThresholdTrap.setStatus(_A)
rcftSHDSLPortLOSThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,8))
rcftSHDSLPortLOSThresholdTrap.setObjects((_C,_AB))
if mibBuilder.loadTexts:rcftSHDSLPortLOSThresholdTrap.setStatus(_A)
rcftSHDSLPortLOSWThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,9))
rcftSHDSLPortLOSWThresholdTrap.setObjects((_C,_AC))
if mibBuilder.loadTexts:rcftSHDSLPortLOSWThresholdTrap.setStatus(_A)
rcftSHDSLPortLOLKThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,10))
rcftSHDSLPortLOLKThresholdTrap.setObjects((_C,_AD))
if mibBuilder.loadTexts:rcftSHDSLPortLOLKThresholdTrap.setStatus(_A)
rcftSHDSLPortESThresholdTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,5,10,11))
rcftSHDSLPortESThresholdTrap.setObjects((_C,_AE))
if mibBuilder.loadTexts:rcftSHDSLPortESThresholdTrap.setStatus(_A)
rcftDS3E3PortAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,1))
rcftDS3E3PortAISTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortAISTrap.setStatus(_A)
rcftDS3E3PortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,2))
rcftDS3E3PortLOSTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortLOSTrap.setStatus(_A)
rcftDS3E3PortLOLTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,3))
rcftDS3E3PortLOLTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortLOLTrap.setStatus(_A)
rcftDS3E3PortDMOTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,4))
rcftDS3E3PortDMOTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortDMOTrap.setStatus(_A)
rcftDS3E3PortCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,5))
rcftDS3E3PortCVTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortCVTrap.setStatus(_A)
rcftDS3E3PortCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,6))
rcftDS3E3PortCRCTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortCRCTrap.setStatus(_A)
rcftDS3E3PortToRAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,7))
rcftDS3E3PortToRAISTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortToRAISTrap.setStatus(_A)
rcftDS3E3PortToRLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,8))
rcftDS3E3PortToRLOSTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortToRLOSTrap.setStatus(_A)
rcftDS3E3PortToRLOLTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,9))
rcftDS3E3PortToRLOLTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortToRLOLTrap.setStatus(_A)
rcftDS3E3PortToRDMOTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,10))
rcftDS3E3PortToRDMOTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortToRDMOTrap.setStatus(_A)
rcftDS3E3PortToRCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,11))
rcftDS3E3PortToRCVTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortToRCVTrap.setStatus(_A)
rcftDS3E3PortToRCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,12))
rcftDS3E3PortToRCRCTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortToRCRCTrap.setStatus(_A)
rcftDS3E3PortLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,13))
rcftDS3E3PortLOFTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortLOFTrap.setStatus(_A)
rcftDS3E3PortToRLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,14))
rcftDS3E3PortToRLOFTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortToRLOFTrap.setStatus(_A)
rcftDS3E3PortRAITrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,15))
rcftDS3E3PortRAITrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortRAITrap.setStatus(_A)
rcftDS3E3PortToRRAITrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,16))
rcftDS3E3PortToRRAITrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortToRRAITrap.setStatus(_A)
rcftDS3E3PortOOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,17))
rcftDS3E3PortOOFTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortOOFTrap.setStatus(_A)
rcftDS3E3PortToROOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,7,10,18))
rcftDS3E3PortToROOFTrap.setObjects((_C,_H))
if mibBuilder.loadTexts:rcftDS3E3PortToROOFTrap.setStatus(_A)
rcftDS1PortAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,1))
rcftDS1PortAISTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortAISTrap.setStatus(_A)
rcftDS1PortLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,2))
rcftDS1PortLOSTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortLOSTrap.setStatus(_A)
rcftDS1PortToRAISTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,3))
rcftDS1PortToRAISTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortToRAISTrap.setStatus(_A)
rcftDS1PortToRLOSTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,4))
rcftDS1PortToRLOSTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortToRLOSTrap.setStatus(_A)
rcftDS1PortLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,5))
rcftDS1PortLOFTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortLOFTrap.setStatus(_A)
rcftDS1PortCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,6))
rcftDS1PortCRCTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortCRCTrap.setStatus(_A)
rcftDS1PortToRLOFTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,7))
rcftDS1PortToRLOFTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortToRLOFTrap.setStatus(_A)
rcftDS1PortToRCRCTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,8))
rcftDS1PortToRCRCTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortToRCRCTrap.setStatus(_A)
rcftDS1PortFaultPassIndicatorTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,9))
rcftDS1PortFaultPassIndicatorTrap.setObjects((_C,_AF))
if mibBuilder.loadTexts:rcftDS1PortFaultPassIndicatorTrap.setStatus(_A)
rcftDS1PortDMOTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,10))
rcftDS1PortDMOTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortDMOTrap.setStatus(_A)
rcftDS1PortCVTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,11))
rcftDS1PortCVTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortCVTrap.setStatus(_A)
rcftDS1PortYELTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,12))
rcftDS1PortYELTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortYELTrap.setStatus(_A)
rcftDS1PortREDTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,8,10,13))
rcftDS1PortREDTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:rcftDS1PortREDTrap.setStatus(_A)
rcftVideoPortSignalLosTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,9,10,1))
rcftVideoPortSignalLosTrap.setObjects((_C,_W))
if mibBuilder.loadTexts:rcftVideoPortSignalLosTrap.setStatus(_A)
rcftVideoPortSignalInLosTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,9,10,2))
rcftVideoPortSignalInLosTrap.setObjects((_C,_W))
if mibBuilder.loadTexts:rcftVideoPortSignalInLosTrap.setStatus(_A)
rcftVideoPortSignalOutLosTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,9,10,3))
rcftVideoPortSignalOutLosTrap.setObjects((_C,_W))
if mibBuilder.loadTexts:rcftVideoPortSignalOutLosTrap.setStatus(_A)
rcftSimpleModuleShutDownTrap=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,11,10,1))
rcftSimpleModuleShutDownTrap.setObjects((_C,_AG))
if mibBuilder.loadTexts:rcftSimpleModuleShutDownTrap.setStatus(_A)
rcftSlotVCGGIDTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,1))
rcftSlotVCGGIDTraps.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftSlotVCGGIDTraps.setStatus(_A)
rcftSlotVCGLOATraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,2))
rcftSlotVCGLOATraps.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftSlotVCGLOATraps.setStatus(_A)
rcftSlotVCGLFDTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,3))
rcftSlotVCGLFDTraps.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftSlotVCGLFDTraps.setStatus(_A)
rcftSlotVCGCSFTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,4))
rcftSlotVCGCSFTraps.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftSlotVCGCSFTraps.setStatus(_A)
rcftSlotVCGTLCTTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,5))
rcftSlotVCGTLCTTraps.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftSlotVCGTLCTTraps.setStatus(_A)
rcftSlotVCGTLCRTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,6))
rcftSlotVCGTLCRTraps.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftSlotVCGTLCRTraps.setStatus(_A)
rcftSlotVCGToRGIDTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,7))
rcftSlotVCGToRGIDTraps.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftSlotVCGToRGIDTraps.setStatus(_A)
rcftSlotVCGToRLOATraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,8))
rcftSlotVCGToRLOATraps.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftSlotVCGToRLOATraps.setStatus(_A)
rcftSlotVCGToRLFDTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,9))
rcftSlotVCGToRLFDTraps.setObjects((_C,_Q))
if mibBuilder.loadTexts:rcftSlotVCGToRLFDTraps.setStatus(_A)
rcftSlotVCGMemberLOMTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,10))
rcftSlotVCGMemberLOMTraps.setObjects((_C,_X))
if mibBuilder.loadTexts:rcftSlotVCGMemberLOMTraps.setStatus(_A)
rcftSlotVCGMemberSQMTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,11))
rcftSlotVCGMemberSQMTraps.setObjects((_C,_X))
if mibBuilder.loadTexts:rcftSlotVCGMemberSQMTraps.setStatus(_A)
rcftSlotVCGMemberCRCTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,12))
rcftSlotVCGMemberCRCTraps.setObjects((_C,_X))
if mibBuilder.loadTexts:rcftSlotVCGMemberCRCTraps.setStatus(_A)
rcftSlotVCGMemberLOATraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,13))
rcftSlotVCGMemberLOATraps.setObjects((_C,_V))
if mibBuilder.loadTexts:rcftSlotVCGMemberLOATraps.setStatus(_A)
rcftSlotVCGToRMemberLOMTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,14))
rcftSlotVCGToRMemberLOMTraps.setObjects((_C,_V))
if mibBuilder.loadTexts:rcftSlotVCGToRMemberLOMTraps.setStatus(_A)
rcftSlotVCGToRMemberSQMTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,15))
rcftSlotVCGToRMemberSQMTraps.setObjects((_C,_V))
if mibBuilder.loadTexts:rcftSlotVCGToRMemberSQMTraps.setStatus(_A)
rcftSlotVCGToRMemberCRCTraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,16))
rcftSlotVCGToRMemberCRCTraps.setObjects((_C,_V))
if mibBuilder.loadTexts:rcftSlotVCGToRMemberCRCTraps.setStatus(_A)
rcftSlotVCGToRMemberLOATraps=NotificationType((1,3,6,1,4,1,8886,2,1,5,10,13,10,17))
rcftSlotVCGToRMemberLOATraps.setObjects((_C,_V))
if mibBuilder.loadTexts:rcftSlotVCGToRMemberLOATraps.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcftSlotPortMib':rcftSlotPortMib,'rcftEthPortMib':rcftEthPortMib,'rcftEthFxPortMib':rcftEthFxPortMib,'rcftEthFxPortObjects':rcftEthFxPortObjects,'rcftEthFxPortTable':rcftEthFxPortTable,'rcftEthFxPortEntry':rcftEthFxPortEntry,_a:rcftEthFxPortIndex,_S:rcftEthFxPortStatus,'rcftEthFxPortModuleMaxSpeed':rcftEthFxPortModuleMaxSpeed,'rcftEthFxPortConnectorType':rcftEthFxPortConnectorType,'rcftEthFxPortTransmitMedia':rcftEthFxPortTransmitMedia,'rcftEthFxPortModuleWaveLen':rcftEthFxPortModuleWaveLen,'rcftEthFxPortModuleManufacturer':rcftEthFxPortModuleManufacturer,'rcftEthFxPortModuleDescr':rcftEthFxPortModuleDescr,'rcftEthFxPortModuleVersion':rcftEthFxPortModuleVersion,'rcftEthFxPortModuleSerialNumber':rcftEthFxPortModuleSerialNumber,'rcftEthFxPortModuleType':rcftEthFxPortModuleType,'rcftEthFxPortRxRestrictSpeed':rcftEthFxPortRxRestrictSpeed,'rcftEthFxPortTxRestrictSpeed':rcftEthFxPortTxRestrictSpeed,'rcftEthFxPortRestrictSpeedStep':rcftEthFxPortRestrictSpeedStep,'rcftEthFxPortLoopOrder':rcftEthFxPortLoopOrder,'rcftEthFxPortLoopStatus':rcftEthFxPortLoopStatus,'rcftEthFxPortSFPDiagnoInfo':rcftEthFxPortSFPDiagnoInfo,_M:rcftEthFxPortSFPDiagnoAlarmStatus,_N:rcftEthFxPortSFPDiagnoWarningStatus,'rcftEthFxPortTranDistance':rcftEthFxPortTranDistance,'rcftEthFxPortSFPType':rcftEthFxPortSFPType,_Y:rcftEthFxPortSFPInfo,'rcftEthFxPortPVID':rcftEthFxPortPVID,'rcftEthFxPorttag':rcftEthFxPorttag,'rcftEthFxPortCOS':rcftEthFxPortCOS,'rcftEthFxPortPerformance':rcftEthFxPortPerformance,'rcftEthFxStatisticTable':rcftEthFxStatisticTable,_A3:rcftEthFxStatisticEntry,'rcftEthFxTxPackets':rcftEthFxTxPackets,'rcftEthFxRxPackets':rcftEthFxRxPackets,'rcftEthFxTxErrPackets':rcftEthFxTxErrPackets,'rcftEthFxRxErrPackets':rcftEthFxRxErrPackets,'rcftEthFxFluxTimer':rcftEthFxFluxTimer,'rcftEthFxRxBytes':rcftEthFxRxBytes,'rcftEthFxTxBytes':rcftEthFxTxBytes,'rcftEthFx64RxBytes':rcftEthFx64RxBytes,'rcftEthFx64TxBytes':rcftEthFx64TxBytes,'rcftEthFxPortTraps':rcftEthFxPortTraps,'rcftEthFxPortLinkTrap':rcftEthFxPortLinkTrap,'rcftEthFxPortExitTrap':rcftEthFxPortExitTrap,'rcftEthFxPortTempHighTrap':rcftEthFxPortTempHighTrap,'rcftEthFxPortTempLowTrap':rcftEthFxPortTempLowTrap,'rcftEthFxPortVoltageHighTrap':rcftEthFxPortVoltageHighTrap,'rcftEthFxPortVoltageLowTrap':rcftEthFxPortVoltageLowTrap,'rcftEthFxPortOffsetCurrHighTrap':rcftEthFxPortOffsetCurrHighTrap,'rcftEthFxPortOffsetCurrLowTrap':rcftEthFxPortOffsetCurrLowTrap,'rcftEthFxPortSendPowerHighTrap':rcftEthFxPortSendPowerHighTrap,'rcftEthFxPortSendPowerLowTrap':rcftEthFxPortSendPowerLowTrap,'rcftEthFxPortRecvPowerHighTrap':rcftEthFxPortRecvPowerHighTrap,'rcftEthFxPortRecvPowerLowTrap':rcftEthFxPortRecvPowerLowTrap,'rcftEthFxPortTempHighWarningTrap':rcftEthFxPortTempHighWarningTrap,'rcftEthFxPortTempLowWarningTrap':rcftEthFxPortTempLowWarningTrap,'rcftEthFxPortVoltageHighWarningTrap':rcftEthFxPortVoltageHighWarningTrap,'rcftEthFxPortVoltageLowWarningTrap':rcftEthFxPortVoltageLowWarningTrap,'rcftEthFxPortOffsetCurrHighWarningTrap':rcftEthFxPortOffsetCurrHighWarningTrap,'rcftEthFxPortOffsetCurrLowWarningTrap':rcftEthFxPortOffsetCurrLowWarningTrap,'rcftEthFxPortSendPowerHighWarningTrap':rcftEthFxPortSendPowerHighWarningTrap,'rcftEthFxPortSendPowerLowWarningTrap':rcftEthFxPortSendPowerLowWarningTrap,'rcftEthFxPortRecvPowerHighWarningTrap':rcftEthFxPortRecvPowerHighWarningTrap,'rcftEthFxPortRecvPowerLowWarningTrap':rcftEthFxPortRecvPowerLowWarningTrap,'rcftEthFxPortSDTrap':rcftEthFxPortSDTrap,'rcftEthFxPortRemotePowerDownTrap':rcftEthFxPortRemotePowerDownTrap,'rcftEthFxPortLaserTxfaultTrap':rcftEthFxPortLaserTxfaultTrap,'rcftEthFxPortInputSignalLosTrap':rcftEthFxPortInputSignalLosTrap,'rcftEthFxPortLOLTrap':rcftEthFxPortLOLTrap,'rcftEthFxPortLOSTrap':rcftEthFxPortLOSTrap,'rcftEthFePortMib':rcftEthFePortMib,'rcftEthFePortObjects':rcftEthFePortObjects,'rcftEthFePortTable':rcftEthFePortTable,'rcftEthFePortEntry':rcftEthFePortEntry,_o:rcftEthFePortIndex,_A8:rcftEthFePortStatus,'rcftEthFePortRxRestrictSpeed':rcftEthFePortRxRestrictSpeed,'rcftEthFePortTxRestrictSpeed':rcftEthFePortTxRestrictSpeed,'rcftEthFePortRestrictSpeedStep':rcftEthFePortRestrictSpeedStep,'rcftEthFePortOrder':rcftEthFePortOrder,'rcftEthFePortPosition':rcftEthFePortPosition,'rcftEthFePortPVID':rcftEthFePortPVID,'rcftEthFePorttag':rcftEthFePorttag,'rcftEthFePortCOS':rcftEthFePortCOS,'rcftEthFePortPerformance':rcftEthFePortPerformance,'rcftEthFeStatisticTable':rcftEthFeStatisticTable,_A4:rcftEthFeStatisticEntry,'rcftEthFeTxPackets':rcftEthFeTxPackets,'rcftEthFeTxBytes':rcftEthFeTxBytes,'rcftEthFeTxFailurePackets':rcftEthFeTxFailurePackets,'rcftEthFeRxPackets':rcftEthFeRxPackets,'rcftEthFeRxBytes':rcftEthFeRxBytes,'rcftEthFeRxErrorPackets':rcftEthFeRxErrorPackets,'rcftEthFeFluxTimer':rcftEthFeFluxTimer,'rcftEthFePortTraps':rcftEthFePortTraps,'rcftEthFePortLinkTrap':rcftEthFePortLinkTrap,'rcftPdhPortMib':rcftPdhPortMib,'rcftPdhPortObjects':rcftPdhPortObjects,'rcftPdhPortTable':rcftPdhPortTable,'rcftPdhPortEntry':rcftPdhPortEntry,_p:rcftPdhPortIndex,_O:rcftPdhPortAlarmStatus,'rcftPdhPortStatus':rcftPdhPortStatus,'rcftPdhPortECSCnt':rcftPdhPortECSCnt,'rcftPdhPortSECSCnt':rcftPdhPortSECSCnt,'rcftPdhPortModuleType':rcftPdhPortModuleType,'rcftPdhPortLoopStatus':rcftPdhPortLoopStatus,'rcftPdhPortOrder':rcftPdhPortOrder,'rcftPdhPortBertStatus':rcftPdhPortBertStatus,'rcftPdhPortBertErrCode':rcftPdhPortBertErrCode,'rcftPdhPortPerformance':rcftPdhPortPerformance,'rcftPdhPortTraps':rcftPdhPortTraps,'rcftPdhPortLOSTrap':rcftPdhPortLOSTrap,'rcftPdhPortLOFTrap':rcftPdhPortLOFTrap,'rcftPdhPortE3Trap':rcftPdhPortE3Trap,'rcftPdhPortE6Trap':rcftPdhPortE6Trap,'rcftPdhPortToRLOSTrap':rcftPdhPortToRLOSTrap,'rcftPdhPortToRLOFTrap':rcftPdhPortToRLOFTrap,'rcftPdhPortToRE3Trap':rcftPdhPortToRE3Trap,'rcftPdhPortToRE6Trap':rcftPdhPortToRE6Trap,'rcftPdhPortToRPowerDown':rcftPdhPortToRPowerDown,'rcftE1PortMib':rcftE1PortMib,'rcftE1PortObjects':rcftE1PortObjects,'rcftE1PortTable':rcftE1PortTable,'rcftE1PortEntry':rcftE1PortEntry,_q:rcftE1PortIndex,_R:rcftE1PortAlarmStatus,'rcftE1PortStatus':rcftE1PortStatus,'rcftE1TimeSlots':rcftE1TimeSlots,'rcftE1TS0Mode':rcftE1TS0Mode,'rcftE1IdleCode':rcftE1IdleCode,'rcftE1LoopStatus':rcftE1LoopStatus,'rcftE1Order':rcftE1Order,'rcftE1PortType':rcftE1PortType,'rcftE1BertStatus':rcftE1BertStatus,'rcftE1BertTime':rcftE1BertTime,'rcftE1BertErrCode':rcftE1BertErrCode,'rcftE1BertUnusedTime':rcftE1BertUnusedTime,'rcftE1BertPortSpeed':rcftE1BertPortSpeed,'rcftE1BertCodeType':rcftE1BertCodeType,'rcftE1BertCodeNum':rcftE1BertCodeNum,'rcftE1AlarmRejest':rcftE1AlarmRejest,_P:rcfT1PortAlarmStatus,'rcftE1PortVCGNumber':rcftE1PortVCGNumber,_Z:rcftE1PortErrorRate,'rcftE1PortESCont':rcftE1PortESCont,'rcftE1PortSESCont':rcftE1PortSESCont,'rcftE1PortToRNumber':rcftE1PortToRNumber,'rcftE1CVCnt':rcftE1CVCnt,'rcftE1PortPerformance':rcftE1PortPerformance,'rcftE1PortTraps':rcftE1PortTraps,'rcftE1PortLOSTrap':rcftE1PortLOSTrap,'rcftE1PortAISTrap':rcftE1PortAISTrap,'rcftE1PortCVTrap':rcftE1PortCVTrap,'rcftE1PortLOFTrap':rcftE1PortLOFTrap,'rcftE1PortLOMFTrap':rcftE1PortLOMFTrap,'rcftE1PortCRCTrap':rcftE1PortCRCTrap,'rcftE1PortToRLOSTrap':rcftE1PortToRLOSTrap,'rcftT1PortLOSTrap':rcftT1PortLOSTrap,'rcftT1PortAISTrap':rcftT1PortAISTrap,'rcftE1PortTSDTrap':rcftE1PortTSDTrap,'rcftE1PortTransErrorCodeMore10E-3':rcftE1PortTransErrorCodeMore10E_3,'rcftE1PortTransErrorCodeMore10E-6':rcftE1PortTransErrorCodeMore10E_6,'rcftE1PortRDITrap':rcftE1PortRDITrap,'rcftE1PortToRAISTrap':rcftE1PortToRAISTrap,'rcftE1PortToRLOFTrap':rcftE1PortToRLOFTrap,'rcftE1PortToRCRCTrap':rcftE1PortToRCRCTrap,'rcftE1PortToRTSDTrap':rcftE1PortToRTSDTrap,'rcftE1PortToRLOMFTrap':rcftE1PortToRLOMFTrap,'rcftE1PortTransErrorCodeMoreToR10E-3':rcftE1PortTransErrorCodeMoreToR10E_3,'rcftV35PortMib':rcftV35PortMib,'rcftV35PortObjects':rcftV35PortObjects,'rcftV35PortTable':rcftV35PortTable,'rcftV35PortEntry':rcftV35PortEntry,_r:rcftV35PortIndex,_I:rcftV35PortAlarmStatus,'rcftV35PortStatus':rcftV35PortStatus,'rcftV35PortSpeed':rcftV35PortSpeed,'rcftV35PortBertStatus':rcftV35PortBertStatus,'rcftV35PortBertTime':rcftV35PortBertTime,'rcftV35PortBertErrCode':rcftV35PortBertErrCode,'rcftV35PortBertUnusedTime':rcftV35PortBertUnusedTime,'rcftV35PortBertPortSpeed':rcftV35PortBertPortSpeed,'rcftV35PortBertCodeType':rcftV35PortBertCodeType,'rcftV35PortBertCodeNum':rcftV35PortBertCodeNum,'rcftV35PortLoopStatus':rcftV35PortLoopStatus,'rcftV35PortOrder':rcftV35PortOrder,'rcftV35PortPerformance':rcftV35PortPerformance,'rcftV35PortTraps':rcftV35PortTraps,'rcftV35PortDCDTrap':rcftV35PortDCDTrap,'rcftV35PortCTSTrap':rcftV35PortCTSTrap,'rcftV35PortDTRTrap':rcftV35PortDTRTrap,'rcftV35PortRTSTrap':rcftV35PortRTSTrap,'rcftV35PortCRCTrap':rcftV35PortCRCTrap,'rcftV35PortPATTTrap':rcftV35PortPATTTrap,'rcftV35PortLOFTrap':rcftV35PortLOFTrap,'rcftV35PortCVTrap':rcftV35PortCVTrap,'rcftV35PortAISTrap':rcftV35PortAISTrap,'rcftV35PortToRLOFTrap':rcftV35PortToRLOFTrap,'rcftV35PortToRCVTrap':rcftV35PortToRCVTrap,'rcftV35PortToRAISTrap':rcftV35PortToRAISTrap,'rcftV35PortDSRTrap':rcftV35PortDSRTrap,'rcftSHDSLPortMib':rcftSHDSLPortMib,'rcftSHDSLPortObjects':rcftSHDSLPortObjects,'rcftSHDSLPortTable':rcftSHDSLPortTable,'rcftSHDSLPortEntry':rcftSHDSLPortEntry,_T:rcftSHDSLPortIndex,_U:rcftSHDSLPortAlarmStatus,'rcftSHDSLPortStatus':rcftSHDSLPortStatus,'rcftSHDSLPortCapableSpeed':rcftSHDSLPortCapableSpeed,'rcftSHDSLPortWorkSpeed':rcftSHDSLPortWorkSpeed,'rcftSHDSLPortProbeMaxSpeed':rcftSHDSLPortProbeMaxSpeed,'rcftSHDSLPortProbeMinSpeed':rcftSHDSLPortProbeMinSpeed,'rcftSDHSLPortSNR':rcftSDHSLPortSNR,'rcftSHDSLPortConfigSNR':rcftSHDSLPortConfigSNR,_A9:rcftSHDSLPortSNRThreshold,'rcftSHDSLPortAttenuation':rcftSHDSLPortAttenuation,_AA:rcftSHDSLPortAttenuationThreshold,'rcftSHDSLPortPBO':rcftSHDSLPortPBO,_AB:rcftSHDSLPortLOSThreshold,_AC:rcftSHDSLPortLOSWThreshold,_AD:rcftSHDSLPortLOLKThreshold,_AE:rcftSHDSLPortESThreshold,'rcftSHDSLPortLoopStatus':rcftSHDSLPortLoopStatus,'rcftSHDSLPortAttenuationInitThreshhold':rcftSHDSLPortAttenuationInitThreshhold,'rcftSHDSLPortBertStatus':rcftSHDSLPortBertStatus,'rcftSHDSLPortBertTime':rcftSHDSLPortBertTime,'rcftSHDSLPortBertErrCode':rcftSHDSLPortBertErrCode,'rcftSHDSLPortBertUnusedTime':rcftSHDSLPortBertUnusedTime,'rcftSHDSLPortBertPortSpeed':rcftSHDSLPortBertPortSpeed,'rcftSHDSLPortBertCodeType':rcftSHDSLPortBertCodeType,'rcftSHDSLPortBertCodeNum':rcftSHDSLPortBertCodeNum,'rcftSHDSLPortOrder':rcftSHDSLPortOrder,'rcftSHDSLPortOrderTimeParameter':rcftSHDSLPortOrderTimeParameter,'rcftSHDSLPortOrderModeParameter':rcftSHDSLPortOrderModeParameter,'rcftSHDSLPortPerformance':rcftSHDSLPortPerformance,'rcftSHDSLPortCurrentTable':rcftSHDSLPortCurrentTable,'rcftSHDSLPortCurrentEntry':rcftSHDSLPortCurrentEntry,'rcftSHDSLPortCurrentLOSTimes':rcftSHDSLPortCurrentLOSTimes,'rcftSHDSLPortCurrentLOSWTimes':rcftSHDSLPortCurrentLOSWTimes,'rcftSHDSLPortCurrentLOLKTimes':rcftSHDSLPortCurrentLOLKTimes,'rcftSHDSLPortCurrentCVTimes':rcftSHDSLPortCurrentCVTimes,'rcftSHDSLPortCurrentES':rcftSHDSLPortCurrentES,'rcftSHDSLPortCurrentSES':rcftSHDSLPortCurrentSES,'rcftSHDSLPortCurrentUAS':rcftSHDSLPortCurrentUAS,'rcftSHDSLPortCurrentLOSWS':rcftSHDSLPortCurrentLOSWS,'rcftSHDSLPortCurrentLOFTimes':rcftSHDSLPortCurrentLOFTimes,'rcftSHDSLPortCurrentCRCTimes':rcftSHDSLPortCurrentCRCTimes,'rcftSHDSLPortIntervalTable':rcftSHDSLPortIntervalTable,'rcftSHDSLPortIntervalEntry':rcftSHDSLPortIntervalEntry,_s:rcftSHDSLPortIntervalNumber,'rcftSHDSLPortIntervalLOSTimes':rcftSHDSLPortIntervalLOSTimes,'rcftSHDSLPortIntervalLOSWTimes':rcftSHDSLPortIntervalLOSWTimes,'rcftSHDSLPortIntervalLOLKTimes':rcftSHDSLPortIntervalLOLKTimes,'rcftSHDSLPortIntervalCVTimes':rcftSHDSLPortIntervalCVTimes,'rcftSHDSLPortIntervalES':rcftSHDSLPortIntervalES,'rcftSHDSLPortIntervalSES':rcftSHDSLPortIntervalSES,'rcftSHDSLPortIntervalUAS':rcftSHDSLPortIntervalUAS,'rcftSHDSLPortIntervalLOSWS':rcftSHDSLPortIntervalLOSWS,'rcftSHDSLPortIntervalLOFTimes':rcftSHDSLPortIntervalLOFTimes,'rcftSHDSLPortIntervalCRCTimes':rcftSHDSLPortIntervalCRCTimes,'rcftSHDSLPortCurrentDayTable':rcftSHDSLPortCurrentDayTable,'rcftSHDSLPortCurrentDayEntry':rcftSHDSLPortCurrentDayEntry,'rcftSHDSLPortCurrentDayLOSTimes':rcftSHDSLPortCurrentDayLOSTimes,'rcftSHDSLPortCurrentDayLOSWTimes':rcftSHDSLPortCurrentDayLOSWTimes,'rcftSHDSLPortCurrentDayLOLKTimes':rcftSHDSLPortCurrentDayLOLKTimes,'rcftSHDSLPortCurrentDayCVTimes':rcftSHDSLPortCurrentDayCVTimes,'rcftSHDSLPortCurrentDayES':rcftSHDSLPortCurrentDayES,'rcftSHDSLPortCurrentDaySES':rcftSHDSLPortCurrentDaySES,'rcftSHDSLPortCurrentDayUAS':rcftSHDSLPortCurrentDayUAS,'rcftSHDSLPortCurrentDayLOSWS':rcftSHDSLPortCurrentDayLOSWS,'rcftSHDSLPortCurrentDayLOFTimes':rcftSHDSLPortCurrentDayLOFTimes,'rcftSHDSLPortCurrentDayCRCTimes':rcftSHDSLPortCurrentDayCRCTimes,'rcftSHDSLPortIntervalDayTable':rcftSHDSLPortIntervalDayTable,'rcftSHDSLPortIntervalDayEntry':rcftSHDSLPortIntervalDayEntry,_t:rcftSHDSLPortIntervalDayNumber,'rcftSHDSLPortIntervalDayLOSTimes':rcftSHDSLPortIntervalDayLOSTimes,'rcftSHDSLPortIntervalDayLOSWTimes':rcftSHDSLPortIntervalDayLOSWTimes,'rcftSHDSLPortIntervalDayLOLKTimes':rcftSHDSLPortIntervalDayLOLKTimes,'rcftSHDSLPortIntervalDayCVTimes':rcftSHDSLPortIntervalDayCVTimes,'rcftSHDSLPortIntervalDayES':rcftSHDSLPortIntervalDayES,'rcftSHDSLPortIntervalDaySES':rcftSHDSLPortIntervalDaySES,'rcftSHDSLPortIntervalDayUAS':rcftSHDSLPortIntervalDayUAS,'rcftSHDSLPortIntervalDayLOSWS':rcftSHDSLPortIntervalDayLOSWS,'rcftSHDSLPortIntervalDayLOFTimes':rcftSHDSLPortIntervalDayLOFTimes,'rcftSHDSLPortIntervalDayCRCTimes':rcftSHDSLPortIntervalDayCRCTimes,'rcftSHDSLPortTraps':rcftSHDSLPortTraps,'rcftSHDSLPortLOSTrap':rcftSHDSLPortLOSTrap,'rcftSHDSLPortLOSWTrap':rcftSHDSLPortLOSWTrap,'rcftSHDSLPortLINKTrap':rcftSHDSLPortLINKTrap,'rcftSHDSLPortFECTrap':rcftSHDSLPortFECTrap,'rcftSHDSLPortCRCTrap':rcftSHDSLPortCRCTrap,'rcftSHDSLPortSNRThresholdTrap':rcftSHDSLPortSNRThresholdTrap,'rcftSHDSLPortAttenuationThresholdTrap':rcftSHDSLPortAttenuationThresholdTrap,'rcftSHDSLPortLOSThresholdTrap':rcftSHDSLPortLOSThresholdTrap,'rcftSHDSLPortLOSWThresholdTrap':rcftSHDSLPortLOSWThresholdTrap,'rcftSHDSLPortLOLKThresholdTrap':rcftSHDSLPortLOLKThresholdTrap,'rcftSHDSLPortESThresholdTrap':rcftSHDSLPortESThresholdTrap,'rcftAudioPortMib':rcftAudioPortMib,'rcftAudioPortObjects':rcftAudioPortObjects,'rcftAudioPortTable':rcftAudioPortTable,'rcftAudioPortEntry':rcftAudioPortEntry,_u:rcftAudioPortIndex,'rcftAudioPortStatus':rcftAudioPortStatus,'rcftAudioPortPosition':rcftAudioPortPosition,'rcftAudioPortType':rcftAudioPortType,'rcftAudioPortPerformance':rcftAudioPortPerformance,'rcftAudioPortTraps':rcftAudioPortTraps,'rcftDS3E3PortMib':rcftDS3E3PortMib,'rcftDS3E3PortObjects':rcftDS3E3PortObjects,'rcftDS3E3PortTable':rcftDS3E3PortTable,'rcftDS3E3PortEntry':rcftDS3E3PortEntry,_v:rcftDS3E3PortIndex,_H:rcftDS3E3PortAlarmStatus,'rcftDS3E3PortStatus':rcftDS3E3PortStatus,'rcftDS3E3PortESCont':rcftDS3E3PortESCont,'rcftDS3E3PortLoopStatus':rcftDS3E3PortLoopStatus,'rcftDS3E3PortOrder':rcftDS3E3PortOrder,'rcftDS3E3PortPerformance':rcftDS3E3PortPerformance,'rcftDS3E3StatisticTable':rcftDS3E3StatisticTable,_A5:rcftDS3E3StatisticEntry,'rcftDS3E3TxPackets':rcftDS3E3TxPackets,'rcftDS3E3TxBytes':rcftDS3E3TxBytes,'rcftDS3E3TxFailurePackets':rcftDS3E3TxFailurePackets,'rcftDS3E3RxPackets':rcftDS3E3RxPackets,'rcftDS3E3RxBytes':rcftDS3E3RxBytes,'rcftDS3E3RxErrorPackets':rcftDS3E3RxErrorPackets,'rcftDS3E3FluxTimer':rcftDS3E3FluxTimer,'rcftDS3E3PortTraps':rcftDS3E3PortTraps,'rcftDS3E3PortAISTrap':rcftDS3E3PortAISTrap,'rcftDS3E3PortLOSTrap':rcftDS3E3PortLOSTrap,'rcftDS3E3PortLOLTrap':rcftDS3E3PortLOLTrap,'rcftDS3E3PortDMOTrap':rcftDS3E3PortDMOTrap,'rcftDS3E3PortCVTrap':rcftDS3E3PortCVTrap,'rcftDS3E3PortCRCTrap':rcftDS3E3PortCRCTrap,'rcftDS3E3PortToRAISTrap':rcftDS3E3PortToRAISTrap,'rcftDS3E3PortToRLOSTrap':rcftDS3E3PortToRLOSTrap,'rcftDS3E3PortToRLOLTrap':rcftDS3E3PortToRLOLTrap,'rcftDS3E3PortToRDMOTrap':rcftDS3E3PortToRDMOTrap,'rcftDS3E3PortToRCVTrap':rcftDS3E3PortToRCVTrap,'rcftDS3E3PortToRCRCTrap':rcftDS3E3PortToRCRCTrap,'rcftDS3E3PortLOFTrap':rcftDS3E3PortLOFTrap,'rcftDS3E3PortToRLOFTrap':rcftDS3E3PortToRLOFTrap,'rcftDS3E3PortRAITrap':rcftDS3E3PortRAITrap,'rcftDS3E3PortToRRAITrap':rcftDS3E3PortToRRAITrap,'rcftDS3E3PortOOFTrap':rcftDS3E3PortOOFTrap,'rcftDS3E3PortToROOFTrap':rcftDS3E3PortToROOFTrap,'rcftDS1PortMib':rcftDS1PortMib,'rcftDS1PortObjects':rcftDS1PortObjects,'rcftDS1PortTable':rcftDS1PortTable,'rcftDS1PortEntry':rcftDS1PortEntry,_w:rcftDS1PortIndex,_J:rcftDS1PortAlarmStatus,'rcftDS1PortStatus':rcftDS1PortStatus,'rcftDS1PortBertStatus':rcftDS1PortBertStatus,'rcftDS1PortESCont':rcftDS1PortESCont,'rcftDS1PortSESCont':rcftDS1PortSESCont,'rcftDS1PortLoopStatus':rcftDS1PortLoopStatus,'rcftDS1PortOrder':rcftDS1PortOrder,'rcftDS1PortTranLength':rcftDS1PortTranLength,_AF:rcftDS1PortFaultPassIndicator,'rcftDS1PortframeType':rcftDS1PortframeType,'rcftDS1PortChannel':rcftDS1PortChannel,'rcftDS1PortPerformance':rcftDS1PortPerformance,'rcftDS1StatisticTable':rcftDS1StatisticTable,_A6:rcftDS1StatisticEntry,'rcftDS1PortTxPackets':rcftDS1PortTxPackets,'rcftDS1PortTxBytes':rcftDS1PortTxBytes,'rcftDS1PortTxFailurePackets':rcftDS1PortTxFailurePackets,'rcftDS1PortRxPackets':rcftDS1PortRxPackets,'rcftDS1PortRxBytes':rcftDS1PortRxBytes,'rcftDS1PortRxErrorPackets':rcftDS1PortRxErrorPackets,'rcftDS1PortFluxTimer':rcftDS1PortFluxTimer,'rcftDS1PortTraps':rcftDS1PortTraps,'rcftDS1PortAISTrap':rcftDS1PortAISTrap,'rcftDS1PortLOSTrap':rcftDS1PortLOSTrap,'rcftDS1PortToRAISTrap':rcftDS1PortToRAISTrap,'rcftDS1PortToRLOSTrap':rcftDS1PortToRLOSTrap,'rcftDS1PortLOFTrap':rcftDS1PortLOFTrap,'rcftDS1PortCRCTrap':rcftDS1PortCRCTrap,'rcftDS1PortToRLOFTrap':rcftDS1PortToRLOFTrap,'rcftDS1PortToRCRCTrap':rcftDS1PortToRCRCTrap,'rcftDS1PortFaultPassIndicatorTrap':rcftDS1PortFaultPassIndicatorTrap,'rcftDS1PortDMOTrap':rcftDS1PortDMOTrap,'rcftDS1PortCVTrap':rcftDS1PortCVTrap,'rcftDS1PortYELTrap':rcftDS1PortYELTrap,'rcftDS1PortREDTrap':rcftDS1PortREDTrap,'rcftVideoPortMib':rcftVideoPortMib,'rcftVideoPortObjects':rcftVideoPortObjects,'rcftVideoPortTable':rcftVideoPortTable,'rcftVideoPortEntry':rcftVideoPortEntry,_x:rcftVideoPortIndex,_W:rcftVideoPortStatus,'rcftVideoPortPosition':rcftVideoPortPosition,'rcftVideoPortSourceID':rcftVideoPortSourceID,'rcftVideoPortPerformance':rcftVideoPortPerformance,'rcftVideoPortTraps':rcftVideoPortTraps,'rcftVideoPortSignalLosTrap':rcftVideoPortSignalLosTrap,'rcftVideoPortSignalInLosTrap':rcftVideoPortSignalInLosTrap,'rcftVideoPortSignalOutLosTrap':rcftVideoPortSignalOutLosTrap,'rcftDataPortMib':rcftDataPortMib,'rcftDataPortObjects':rcftDataPortObjects,'rcftDataPortTable':rcftDataPortTable,'rcftDataPortEntry':rcftDataPortEntry,_y:rcftDataPortIndex,'rcftDataPortStatus':rcftDataPortStatus,'rcftDataPortPosition':rcftDataPortPosition,'rcftDataPortType':rcftDataPortType,'rcftDataPortPerformance':rcftDataPortPerformance,'rcftDataPortTraps':rcftDataPortTraps,'rcftSimpleModuleMib':rcftSimpleModuleMib,'rcftSimpleModuleObjects':rcftSimpleModuleObjects,'rcftSimpleModuleTable':rcftSimpleModuleTable,'rcftSimpleModuleEntry':rcftSimpleModuleEntry,_z:rcftSimpleModuleIndex,'rcftSimpleModuleExist':rcftSimpleModuleExist,'rcftSimpleModulePosition':rcftSimpleModulePosition,_AG:rcftSimpleModuleStatus,'rcftSimpleModuleType':rcftSimpleModuleType,'rcftSimpleModulePerformance':rcftSimpleModulePerformance,'rcftSimpleModuleTraps':rcftSimpleModuleTraps,'rcftSimpleModuleShutDownTrap':rcftSimpleModuleShutDownTrap,'rcftSlotPerformaceMib':rcftSlotPerformaceMib,'rcftSlotPerformance':rcftSlotPerformance,'rcftSlotStatisticTable':rcftSlotStatisticTable,'rcftSlotStatisticEntry':rcftSlotStatisticEntry,_A0:rcftPortIndex,'rcftPortType':rcftPortType,'rcftRxPackets':rcftRxPackets,'rcftRxLosPackets':rcftRxLosPackets,'rcftRxPreabErrPackets':rcftRxPreabErrPackets,'rcftRxFCSErrPackets':rcftRxFCSErrPackets,'rcftRxUnderSizePackets':rcftRxUnderSizePackets,'rcftRxOverSizePackets':rcftRxOverSizePackets,'rcftRxPausePackets':rcftRxPausePackets,'rcftRxOamPackets':rcftRxOamPackets,'rcftRxBytes':rcftRxBytes,'rcftTxPackets':rcftTxPackets,'rcftTxFCSErrPackets':rcftTxFCSErrPackets,'rcftTxPausePackets':rcftTxPausePackets,'rcftTxOamPackets':rcftTxOamPackets,'rcftTxBytes':rcftTxBytes,'rcftFluxTimer':rcftFluxTimer,'rcftSlotVCGMib':rcftSlotVCGMib,'rcftSlotVCGObjects':rcftSlotVCGObjects,'rcftSlotVCGTable':rcftSlotVCGTable,'rcftSlotVCGEntry':rcftSlotVCGEntry,_A1:rcftSlotVCGIndex,'rcftSlotVCGStatus':rcftSlotVCGStatus,'rcftSlotVCGLoopStatus':rcftSlotVCGLoopStatus,'rcftSlotVCGLcasXPR':rcftSlotVCGLcasXPR,'rcftSlotVCGLcasXAR':rcftSlotVCGLcasXAR,'rcftSlotVCGLcasXPT':rcftSlotVCGLcasXPT,'rcftSlotVCGLcasXAT':rcftSlotVCGLcasXAT,_Q:rcftSlotVCGAlarmStatus,'rcftSlotVCGTxISPTPID':rcftSlotVCGTxISPTPID,'rcftSlotVCGRxISPTPID':rcftSlotVCGRxISPTPID,'rcftSlotVCGBaseCoS':rcftSlotVCGBaseCoS,'rcftSlotVCGVLANID':rcftSlotVCGVLANID,'rcftSlotVCGMemberList':rcftSlotVCGMemberList,'rcftSlotToRVCGMemberList':rcftSlotToRVCGMemberList,'rcftSlotVCGMemberStatus':rcftSlotVCGMemberStatus,'rcftSlotVCGMemberRxCode':rcftSlotVCGMemberRxCode,'rcftSlotVCGMemberTxCode':rcftSlotVCGMemberTxCode,_X:rcftSlotVCGMemberAlarmStatus,_V:rcftSlotToRVCGMemberAlarmStatus,'rcftSlotVCGPerformance':rcftSlotVCGPerformance,'rcftSlotVCGStatisticTable':rcftSlotVCGStatisticTable,_A7:rcftSlotVCGStatisticEntry,'rcftVCGRxClientPackets':rcftVCGRxClientPackets,'rcftVCGRxIdlePackets':rcftVCGRxIdlePackets,'rcftVCGRxMgmntPackets':rcftVCGRxMgmntPackets,'rcftVCGRxFCSErrMgmntPackets':rcftVCGRxFCSErrMgmntPackets,'rcftVCGRxLenErrPackets':rcftVCGRxLenErrPackets,'rcftVCGRxFCSErrClientPackets':rcftVCGRxFCSErrClientPackets,'rcftVCGRxThecErrPackets':rcftVCGRxThecErrPackets,'rcftVCGRxEhecErrPackets':rcftVCGRxEhecErrPackets,'rcftVCGRxCIDErrPackets':rcftVCGRxCIDErrPackets,'rcftVCGRxSpareErrPackets':rcftVCGRxSpareErrPackets,'rcftVCGRxChecCorPackets':rcftVCGRxChecCorPackets,'rcftVCGRxThecCorPackets':rcftVCGRxThecCorPackets,'rcftVCGRxEhecCorPackets':rcftVCGRxEhecCorPackets,'rcftVCGRxBytes':rcftVCGRxBytes,'rcftVCGTxClientPackets':rcftVCGTxClientPackets,'rcftVCGTxIdlePackets':rcftVCGTxIdlePackets,'rcftVCGTxMgmntPackets':rcftVCGTxMgmntPackets,'rcftVCGTxBytes':rcftVCGTxBytes,'rcftVCGFluxTimer':rcftVCGFluxTimer,'rcftSlotVCGTraps':rcftSlotVCGTraps,'rcftSlotVCGGIDTraps':rcftSlotVCGGIDTraps,'rcftSlotVCGLOATraps':rcftSlotVCGLOATraps,'rcftSlotVCGLFDTraps':rcftSlotVCGLFDTraps,'rcftSlotVCGCSFTraps':rcftSlotVCGCSFTraps,'rcftSlotVCGTLCTTraps':rcftSlotVCGTLCTTraps,'rcftSlotVCGTLCRTraps':rcftSlotVCGTLCRTraps,'rcftSlotVCGToRGIDTraps':rcftSlotVCGToRGIDTraps,'rcftSlotVCGToRLOATraps':rcftSlotVCGToRLOATraps,'rcftSlotVCGToRLFDTraps':rcftSlotVCGToRLFDTraps,'rcftSlotVCGMemberLOMTraps':rcftSlotVCGMemberLOMTraps,'rcftSlotVCGMemberSQMTraps':rcftSlotVCGMemberSQMTraps,'rcftSlotVCGMemberCRCTraps':rcftSlotVCGMemberCRCTraps,'rcftSlotVCGMemberLOATraps':rcftSlotVCGMemberLOATraps,'rcftSlotVCGToRMemberLOMTraps':rcftSlotVCGToRMemberLOMTraps,'rcftSlotVCGToRMemberSQMTraps':rcftSlotVCGToRMemberSQMTraps,'rcftSlotVCGToRMemberCRCTraps':rcftSlotVCGToRMemberCRCTraps,'rcftSlotVCGToRMemberLOATraps':rcftSlotVCGToRMemberLOATraps,'rcftSlotVLANMib':rcftSlotVLANMib,'rcftSlotVLANObjects':rcftSlotVLANObjects,'rcftSlotVLANTable':rcftSlotVLANTable,'rcftSlotVLANEntry':rcftSlotVLANEntry,_A2:rcftSlotVLANIndex,'rcftSlotVLANStatus':rcftSlotVLANStatus,'rcftSlotVLANmember':rcftSlotVLANmember,'rcftSlotVID':rcftSlotVID})