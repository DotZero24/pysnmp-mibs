_AO='dellNetIfNotificationGroup'
_AN='dellNetIfTransceiverDataGroup'
_AM='dellNetIfStatsGroup'
_AL='dellNetIfParamsGroup'
_AK='dellNetIfAlarmFastRetrain'
_AJ='dellNetIfAlarmHighBerClr'
_AI='dellNetIfAlarmHighBer'
_AH='dellNetIfTransTransmitBiasCurrentLane4'
_AG='dellNetIfTransTransmitBiasCurrentLane3'
_AF='dellNetIfTransTransmitBiasCurrentLane2'
_AE='dellNetIfTransTransmitBiasCurrentLane1'
_AD='dellNetIfTransVoltage'
_AC='dellNetIfTransTemperature'
_AB='dellNetIfTransReceivePowerLane4'
_AA='dellNetIfTransReceivePowerLane3'
_A9='dellNetIfTransReceivePowerLane2'
_A8='dellNetIfTransReceivePowerLane1'
_A7='dellNetIfTransTransmitPowerLane4'
_A6='dellNetIfTransTransmitPowerLane3'
_A5='dellNetIfTransTransmitPowerLane2'
_A4='dellNetIfTransTransmitPowerLane1'
_A3='dellNetIfTransSerialNumber'
_A2='dellNetIfTransPartNumber'
_A1='dellNetIfTransVendorName'
_A0='dellNetIfTransOpticsType'
_z='dellNetIfTransOpticsPresent'
_y='dellNetIfTransPort'
_x='dellNetIfTransDeviceName'
_w='dellNetIfOutCentRate'
_v='dellNetIfInCentRate'
_u='dellNetIfLastDiscontinuityTime'
_t='dellNetIfOutThrottles'
_s='dellNetIfOutOver1023BytePkts'
_r='dellNetIfOut512To1023BytePkts'
_q='dellNetIfOut256To511BytePkts'
_p='dellNetIfOut128To255BytePkts'
_o='dellNetIfOut65To127BytePkts'
_n='dellNetIfOut64BytePkts'
_m='dellNetIfOutWredDrops'
_l='dellNetIfOutCollisions'
_k='dellNetIfOutUnicasts'
_j='dellNetIfOutUnderruns'
_i='dellNetIfOutVlanPkts'
_h='dellNetIfInOverruns'
_g='dellNetIfInCRC'
_f='dellNetIfInGiants'
_e='dellNetIfInRunts'
_d='dellNetIfInThrottles'
_c='dellNetIfInOver1023BytePkts'
_b='dellNetIfIn512To1023BytePkts'
_a='dellNetIfIn256To511BytePkts'
_Z='dellNetIfIn128To255BytePkts'
_Y='dellNetIfIn65To127BytePkts'
_X='dellNetIfIn64BytePkts'
_W='dellNetIfInVlanPkts'
_V='dellNetIfPortListBitPos'
_U='dellNetIfSpeed'
_T='dellNetIfRateInterval'
_S='dellNetIfAdminStatus'
_R='dellNetIfDescr'
_Q='dellNetIfTxFlowCtrl'
_P='dellNetIfRxFlowCtrl'
_O='dellNetIfQueueingStrategy'
_N='dellNetIfDuplexMode'
_M='dellNetIfIpMtu'
_L='DisplayString'
_K='Unsigned32'
_J='mA'
_I='Integer32'
_H='ifIndex'
_G='IF-MIB'
_F='dBm'
_E='read-write'
_D='OctetString'
_C='read-only'
_B='DELL-NETWORKING-IF-EXTENSION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
dellNetIfExtensionMib=ModuleIdentity((1,3,6,1,4,1,6027,3,11))
if mibBuilder.loadTexts:dellNetIfExtensionMib.setRevisions(('2014-08-12 12:00','2012-03-06 12:00','2010-08-11 12:00','2010-08-10 12:00'))
_DellNetIfExtensionMibObject_ObjectIdentity=ObjectIdentity
dellNetIfExtensionMibObject=_DellNetIfExtensionMibObject_ObjectIdentity((1,3,6,1,4,1,6027,3,11,1))
_DellNetIfExtensionParams_ObjectIdentity=ObjectIdentity
dellNetIfExtensionParams=_DellNetIfExtensionParams_ObjectIdentity((1,3,6,1,4,1,6027,3,11,1,1))
_DellNetIfTable_Object=MibTable
dellNetIfTable=_DellNetIfTable_Object((1,3,6,1,4,1,6027,3,11,1,1,1))
if mibBuilder.loadTexts:dellNetIfTable.setStatus(_A)
_DellNetIfEntry_Object=MibTableRow
dellNetIfEntry=_DellNetIfEntry_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1))
dellNetIfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dellNetIfEntry.setStatus(_A)
class _DellNetIfIpMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(594,9252))
_DellNetIfIpMtu_Type.__name__=_K
_DellNetIfIpMtu_Object=MibTableColumn
dellNetIfIpMtu=_DellNetIfIpMtu_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,1),_DellNetIfIpMtu_Type())
dellNetIfIpMtu.setMaxAccess(_E)
if mibBuilder.loadTexts:dellNetIfIpMtu.setStatus(_A)
class _DellNetIfDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('half',1),('full',2),('auto',3)))
_DellNetIfDuplexMode_Type.__name__=_I
_DellNetIfDuplexMode_Object=MibTableColumn
dellNetIfDuplexMode=_DellNetIfDuplexMode_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,2),_DellNetIfDuplexMode_Type())
dellNetIfDuplexMode.setMaxAccess(_E)
if mibBuilder.loadTexts:dellNetIfDuplexMode.setStatus(_A)
class _DellNetIfQueueingStrategy_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DellNetIfQueueingStrategy_Type.__name__=_L
_DellNetIfQueueingStrategy_Object=MibTableColumn
dellNetIfQueueingStrategy=_DellNetIfQueueingStrategy_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,3),_DellNetIfQueueingStrategy_Type())
dellNetIfQueueingStrategy.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfQueueingStrategy.setStatus(_A)
_DellNetIfRxFlowCtrl_Type=TruthValue
_DellNetIfRxFlowCtrl_Object=MibTableColumn
dellNetIfRxFlowCtrl=_DellNetIfRxFlowCtrl_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,4),_DellNetIfRxFlowCtrl_Type())
dellNetIfRxFlowCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:dellNetIfRxFlowCtrl.setStatus(_A)
_DellNetIfTxFlowCtrl_Type=TruthValue
_DellNetIfTxFlowCtrl_Object=MibTableColumn
dellNetIfTxFlowCtrl=_DellNetIfTxFlowCtrl_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,5),_DellNetIfTxFlowCtrl_Type())
dellNetIfTxFlowCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:dellNetIfTxFlowCtrl.setStatus(_A)
class _DellNetIfDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfDescr_Type.__name__=_D
_DellNetIfDescr_Object=MibTableColumn
dellNetIfDescr=_DellNetIfDescr_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,6),_DellNetIfDescr_Type())
dellNetIfDescr.setMaxAccess(_E)
if mibBuilder.loadTexts:dellNetIfDescr.setStatus(_A)
class _DellNetIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_DellNetIfAdminStatus_Type.__name__=_I
_DellNetIfAdminStatus_Object=MibTableColumn
dellNetIfAdminStatus=_DellNetIfAdminStatus_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,7),_DellNetIfAdminStatus_Type())
dellNetIfAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dellNetIfAdminStatus.setStatus(_A)
class _DellNetIfRateInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,299))
_DellNetIfRateInterval_Type.__name__=_K
_DellNetIfRateInterval_Object=MibTableColumn
dellNetIfRateInterval=_DellNetIfRateInterval_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,8),_DellNetIfRateInterval_Type())
dellNetIfRateInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:dellNetIfRateInterval.setStatus(_A)
class _DellNetIfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,100,1000)));namedValues=NamedValues(*(('auto',1),('tenMbps',10),('hundredMbps',100),('thousandMbps',1000)))
_DellNetIfSpeed_Type.__name__=_I
_DellNetIfSpeed_Object=MibTableColumn
dellNetIfSpeed=_DellNetIfSpeed_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,9),_DellNetIfSpeed_Type())
dellNetIfSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:dellNetIfSpeed.setStatus(_A)
_DellNetIfPortListBitPos_Type=Integer32
_DellNetIfPortListBitPos_Object=MibTableColumn
dellNetIfPortListBitPos=_DellNetIfPortListBitPos_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,10),_DellNetIfPortListBitPos_Type())
dellNetIfPortListBitPos.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfPortListBitPos.setStatus(_A)
_DellNetIfExtensionStats_ObjectIdentity=ObjectIdentity
dellNetIfExtensionStats=_DellNetIfExtensionStats_ObjectIdentity((1,3,6,1,4,1,6027,3,11,1,2))
_DellNetIfStaticsTable_Object=MibTable
dellNetIfStaticsTable=_DellNetIfStaticsTable_Object((1,3,6,1,4,1,6027,3,11,1,2,1))
if mibBuilder.loadTexts:dellNetIfStaticsTable.setStatus(_A)
_DellNetIfStaticsEntry_Object=MibTableRow
dellNetIfStaticsEntry=_DellNetIfStaticsEntry_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1))
dellNetIfStaticsEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dellNetIfStaticsEntry.setStatus(_A)
_DellNetIfInVlanPkts_Type=Counter64
_DellNetIfInVlanPkts_Object=MibTableColumn
dellNetIfInVlanPkts=_DellNetIfInVlanPkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,1),_DellNetIfInVlanPkts_Type())
dellNetIfInVlanPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfInVlanPkts.setStatus(_A)
_DellNetIfIn64BytePkts_Type=Counter64
_DellNetIfIn64BytePkts_Object=MibTableColumn
dellNetIfIn64BytePkts=_DellNetIfIn64BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,2),_DellNetIfIn64BytePkts_Type())
dellNetIfIn64BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfIn64BytePkts.setStatus(_A)
_DellNetIfIn65To127BytePkts_Type=Counter64
_DellNetIfIn65To127BytePkts_Object=MibTableColumn
dellNetIfIn65To127BytePkts=_DellNetIfIn65To127BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,3),_DellNetIfIn65To127BytePkts_Type())
dellNetIfIn65To127BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfIn65To127BytePkts.setStatus(_A)
_DellNetIfIn128To255BytePkts_Type=Counter64
_DellNetIfIn128To255BytePkts_Object=MibTableColumn
dellNetIfIn128To255BytePkts=_DellNetIfIn128To255BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,4),_DellNetIfIn128To255BytePkts_Type())
dellNetIfIn128To255BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfIn128To255BytePkts.setStatus(_A)
_DellNetIfIn256To511BytePkts_Type=Counter64
_DellNetIfIn256To511BytePkts_Object=MibTableColumn
dellNetIfIn256To511BytePkts=_DellNetIfIn256To511BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,5),_DellNetIfIn256To511BytePkts_Type())
dellNetIfIn256To511BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfIn256To511BytePkts.setStatus(_A)
_DellNetIfIn512To1023BytePkts_Type=Counter64
_DellNetIfIn512To1023BytePkts_Object=MibTableColumn
dellNetIfIn512To1023BytePkts=_DellNetIfIn512To1023BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,6),_DellNetIfIn512To1023BytePkts_Type())
dellNetIfIn512To1023BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfIn512To1023BytePkts.setStatus(_A)
_DellNetIfInOver1023BytePkts_Type=Counter64
_DellNetIfInOver1023BytePkts_Object=MibTableColumn
dellNetIfInOver1023BytePkts=_DellNetIfInOver1023BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,7),_DellNetIfInOver1023BytePkts_Type())
dellNetIfInOver1023BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfInOver1023BytePkts.setStatus(_A)
_DellNetIfInThrottles_Type=Counter64
_DellNetIfInThrottles_Object=MibTableColumn
dellNetIfInThrottles=_DellNetIfInThrottles_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,8),_DellNetIfInThrottles_Type())
dellNetIfInThrottles.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfInThrottles.setStatus(_A)
_DellNetIfInRunts_Type=Counter64
_DellNetIfInRunts_Object=MibTableColumn
dellNetIfInRunts=_DellNetIfInRunts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,9),_DellNetIfInRunts_Type())
dellNetIfInRunts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfInRunts.setStatus(_A)
_DellNetIfInGiants_Type=Counter64
_DellNetIfInGiants_Object=MibTableColumn
dellNetIfInGiants=_DellNetIfInGiants_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,10),_DellNetIfInGiants_Type())
dellNetIfInGiants.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfInGiants.setStatus(_A)
_DellNetIfInCRC_Type=Counter64
_DellNetIfInCRC_Object=MibTableColumn
dellNetIfInCRC=_DellNetIfInCRC_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,11),_DellNetIfInCRC_Type())
dellNetIfInCRC.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfInCRC.setStatus(_A)
_DellNetIfInOverruns_Type=Counter64
_DellNetIfInOverruns_Object=MibTableColumn
dellNetIfInOverruns=_DellNetIfInOverruns_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,12),_DellNetIfInOverruns_Type())
dellNetIfInOverruns.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfInOverruns.setStatus(_A)
_DellNetIfOutVlanPkts_Type=Counter64
_DellNetIfOutVlanPkts_Object=MibTableColumn
dellNetIfOutVlanPkts=_DellNetIfOutVlanPkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,13),_DellNetIfOutVlanPkts_Type())
dellNetIfOutVlanPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOutVlanPkts.setStatus(_A)
_DellNetIfOutUnderruns_Type=Counter64
_DellNetIfOutUnderruns_Object=MibTableColumn
dellNetIfOutUnderruns=_DellNetIfOutUnderruns_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,14),_DellNetIfOutUnderruns_Type())
dellNetIfOutUnderruns.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOutUnderruns.setStatus(_A)
_DellNetIfOutUnicasts_Type=Counter64
_DellNetIfOutUnicasts_Object=MibTableColumn
dellNetIfOutUnicasts=_DellNetIfOutUnicasts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,15),_DellNetIfOutUnicasts_Type())
dellNetIfOutUnicasts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOutUnicasts.setStatus(_A)
_DellNetIfOutCollisions_Type=Counter64
_DellNetIfOutCollisions_Object=MibTableColumn
dellNetIfOutCollisions=_DellNetIfOutCollisions_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,16),_DellNetIfOutCollisions_Type())
dellNetIfOutCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOutCollisions.setStatus(_A)
_DellNetIfOutWredDrops_Type=Counter64
_DellNetIfOutWredDrops_Object=MibTableColumn
dellNetIfOutWredDrops=_DellNetIfOutWredDrops_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,17),_DellNetIfOutWredDrops_Type())
dellNetIfOutWredDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOutWredDrops.setStatus(_A)
_DellNetIfOut64BytePkts_Type=Counter64
_DellNetIfOut64BytePkts_Object=MibTableColumn
dellNetIfOut64BytePkts=_DellNetIfOut64BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,18),_DellNetIfOut64BytePkts_Type())
dellNetIfOut64BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOut64BytePkts.setStatus(_A)
_DellNetIfOut65To127BytePkts_Type=Counter64
_DellNetIfOut65To127BytePkts_Object=MibTableColumn
dellNetIfOut65To127BytePkts=_DellNetIfOut65To127BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,19),_DellNetIfOut65To127BytePkts_Type())
dellNetIfOut65To127BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOut65To127BytePkts.setStatus(_A)
_DellNetIfOut128To255BytePkts_Type=Counter64
_DellNetIfOut128To255BytePkts_Object=MibTableColumn
dellNetIfOut128To255BytePkts=_DellNetIfOut128To255BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,20),_DellNetIfOut128To255BytePkts_Type())
dellNetIfOut128To255BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOut128To255BytePkts.setStatus(_A)
_DellNetIfOut256To511BytePkts_Type=Counter64
_DellNetIfOut256To511BytePkts_Object=MibTableColumn
dellNetIfOut256To511BytePkts=_DellNetIfOut256To511BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,21),_DellNetIfOut256To511BytePkts_Type())
dellNetIfOut256To511BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOut256To511BytePkts.setStatus(_A)
_DellNetIfOut512To1023BytePkts_Type=Counter64
_DellNetIfOut512To1023BytePkts_Object=MibTableColumn
dellNetIfOut512To1023BytePkts=_DellNetIfOut512To1023BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,22),_DellNetIfOut512To1023BytePkts_Type())
dellNetIfOut512To1023BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOut512To1023BytePkts.setStatus(_A)
_DellNetIfOutOver1023BytePkts_Type=Counter64
_DellNetIfOutOver1023BytePkts_Object=MibTableColumn
dellNetIfOutOver1023BytePkts=_DellNetIfOutOver1023BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,23),_DellNetIfOutOver1023BytePkts_Type())
dellNetIfOutOver1023BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOutOver1023BytePkts.setStatus(_A)
_DellNetIfOutThrottles_Type=Counter64
_DellNetIfOutThrottles_Object=MibTableColumn
dellNetIfOutThrottles=_DellNetIfOutThrottles_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,24),_DellNetIfOutThrottles_Type())
dellNetIfOutThrottles.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOutThrottles.setStatus(_A)
_DellNetIfLastDiscontinuityTime_Type=TimeStamp
_DellNetIfLastDiscontinuityTime_Object=MibTableColumn
dellNetIfLastDiscontinuityTime=_DellNetIfLastDiscontinuityTime_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,25),_DellNetIfLastDiscontinuityTime_Type())
dellNetIfLastDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfLastDiscontinuityTime.setStatus(_A)
class _DellNetIfInCentRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DellNetIfInCentRate_Type.__name__=_I
_DellNetIfInCentRate_Object=MibTableColumn
dellNetIfInCentRate=_DellNetIfInCentRate_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,26),_DellNetIfInCentRate_Type())
dellNetIfInCentRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfInCentRate.setStatus(_A)
class _DellNetIfOutCentRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DellNetIfOutCentRate_Type.__name__=_I
_DellNetIfOutCentRate_Object=MibTableColumn
dellNetIfOutCentRate=_DellNetIfOutCentRate_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,27),_DellNetIfOutCentRate_Type())
dellNetIfOutCentRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfOutCentRate.setStatus(_A)
_DellNetIfTransceiverData_ObjectIdentity=ObjectIdentity
dellNetIfTransceiverData=_DellNetIfTransceiverData_ObjectIdentity((1,3,6,1,4,1,6027,3,11,1,3))
_DellNetIfTransceiverDataTable_Object=MibTable
dellNetIfTransceiverDataTable=_DellNetIfTransceiverDataTable_Object((1,3,6,1,4,1,6027,3,11,1,3,1))
if mibBuilder.loadTexts:dellNetIfTransceiverDataTable.setStatus(_A)
_DellNetIfTransceiverDataEntry_Object=MibTableRow
dellNetIfTransceiverDataEntry=_DellNetIfTransceiverDataEntry_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1))
dellNetIfTransceiverDataEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dellNetIfTransceiverDataEntry.setStatus(_A)
class _DellNetIfTransDeviceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransDeviceName_Type.__name__=_D
_DellNetIfTransDeviceName_Object=MibTableColumn
dellNetIfTransDeviceName=_DellNetIfTransDeviceName_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,1),_DellNetIfTransDeviceName_Type())
dellNetIfTransDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransDeviceName.setStatus(_A)
class _DellNetIfTransPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransPort_Type.__name__=_D
_DellNetIfTransPort_Object=MibTableColumn
dellNetIfTransPort=_DellNetIfTransPort_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,2),_DellNetIfTransPort_Type())
dellNetIfTransPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransPort.setStatus(_A)
_DellNetIfTransOpticsPresent_Type=TruthValue
_DellNetIfTransOpticsPresent_Object=MibTableColumn
dellNetIfTransOpticsPresent=_DellNetIfTransOpticsPresent_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,3),_DellNetIfTransOpticsPresent_Type())
dellNetIfTransOpticsPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransOpticsPresent.setStatus(_A)
class _DellNetIfTransOpticsType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransOpticsType_Type.__name__=_D
_DellNetIfTransOpticsType_Object=MibTableColumn
dellNetIfTransOpticsType=_DellNetIfTransOpticsType_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,4),_DellNetIfTransOpticsType_Type())
dellNetIfTransOpticsType.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransOpticsType.setStatus(_A)
class _DellNetIfTransVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransVendorName_Type.__name__=_D
_DellNetIfTransVendorName_Object=MibTableColumn
dellNetIfTransVendorName=_DellNetIfTransVendorName_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,5),_DellNetIfTransVendorName_Type())
dellNetIfTransVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransVendorName.setStatus(_A)
class _DellNetIfTransPartNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransPartNumber_Type.__name__=_D
_DellNetIfTransPartNumber_Object=MibTableColumn
dellNetIfTransPartNumber=_DellNetIfTransPartNumber_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,6),_DellNetIfTransPartNumber_Type())
dellNetIfTransPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransPartNumber.setStatus(_A)
class _DellNetIfTransSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransSerialNumber_Type.__name__=_D
_DellNetIfTransSerialNumber_Object=MibTableColumn
dellNetIfTransSerialNumber=_DellNetIfTransSerialNumber_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,7),_DellNetIfTransSerialNumber_Type())
dellNetIfTransSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransSerialNumber.setStatus(_A)
class _DellNetIfTransTransmitPowerLane1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransTransmitPowerLane1_Type.__name__=_D
_DellNetIfTransTransmitPowerLane1_Object=MibTableColumn
dellNetIfTransTransmitPowerLane1=_DellNetIfTransTransmitPowerLane1_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,8),_DellNetIfTransTransmitPowerLane1_Type())
dellNetIfTransTransmitPowerLane1.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransTransmitPowerLane1.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransTransmitPowerLane1.setUnits(_F)
class _DellNetIfTransTransmitPowerLane2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransTransmitPowerLane2_Type.__name__=_D
_DellNetIfTransTransmitPowerLane2_Object=MibTableColumn
dellNetIfTransTransmitPowerLane2=_DellNetIfTransTransmitPowerLane2_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,9),_DellNetIfTransTransmitPowerLane2_Type())
dellNetIfTransTransmitPowerLane2.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransTransmitPowerLane2.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransTransmitPowerLane2.setUnits(_F)
class _DellNetIfTransTransmitPowerLane3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransTransmitPowerLane3_Type.__name__=_D
_DellNetIfTransTransmitPowerLane3_Object=MibTableColumn
dellNetIfTransTransmitPowerLane3=_DellNetIfTransTransmitPowerLane3_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,10),_DellNetIfTransTransmitPowerLane3_Type())
dellNetIfTransTransmitPowerLane3.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransTransmitPowerLane3.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransTransmitPowerLane3.setUnits(_F)
class _DellNetIfTransTransmitPowerLane4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransTransmitPowerLane4_Type.__name__=_D
_DellNetIfTransTransmitPowerLane4_Object=MibTableColumn
dellNetIfTransTransmitPowerLane4=_DellNetIfTransTransmitPowerLane4_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,11),_DellNetIfTransTransmitPowerLane4_Type())
dellNetIfTransTransmitPowerLane4.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransTransmitPowerLane4.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransTransmitPowerLane4.setUnits(_F)
class _DellNetIfTransReceivePowerLane1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransReceivePowerLane1_Type.__name__=_D
_DellNetIfTransReceivePowerLane1_Object=MibTableColumn
dellNetIfTransReceivePowerLane1=_DellNetIfTransReceivePowerLane1_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,12),_DellNetIfTransReceivePowerLane1_Type())
dellNetIfTransReceivePowerLane1.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransReceivePowerLane1.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransReceivePowerLane1.setUnits(_F)
class _DellNetIfTransReceivePowerLane2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransReceivePowerLane2_Type.__name__=_D
_DellNetIfTransReceivePowerLane2_Object=MibTableColumn
dellNetIfTransReceivePowerLane2=_DellNetIfTransReceivePowerLane2_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,13),_DellNetIfTransReceivePowerLane2_Type())
dellNetIfTransReceivePowerLane2.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransReceivePowerLane2.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransReceivePowerLane2.setUnits(_F)
class _DellNetIfTransReceivePowerLane3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransReceivePowerLane3_Type.__name__=_D
_DellNetIfTransReceivePowerLane3_Object=MibTableColumn
dellNetIfTransReceivePowerLane3=_DellNetIfTransReceivePowerLane3_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,14),_DellNetIfTransReceivePowerLane3_Type())
dellNetIfTransReceivePowerLane3.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransReceivePowerLane3.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransReceivePowerLane3.setUnits(_F)
class _DellNetIfTransReceivePowerLane4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransReceivePowerLane4_Type.__name__=_D
_DellNetIfTransReceivePowerLane4_Object=MibTableColumn
dellNetIfTransReceivePowerLane4=_DellNetIfTransReceivePowerLane4_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,15),_DellNetIfTransReceivePowerLane4_Type())
dellNetIfTransReceivePowerLane4.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransReceivePowerLane4.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransReceivePowerLane4.setUnits(_F)
class _DellNetIfTransTemperature_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransTemperature_Type.__name__=_D
_DellNetIfTransTemperature_Object=MibTableColumn
dellNetIfTransTemperature=_DellNetIfTransTemperature_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,16),_DellNetIfTransTemperature_Type())
dellNetIfTransTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransTemperature.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransTemperature.setUnits('degree Celsius')
class _DellNetIfTransVoltage_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransVoltage_Type.__name__=_D
_DellNetIfTransVoltage_Object=MibTableColumn
dellNetIfTransVoltage=_DellNetIfTransVoltage_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,17),_DellNetIfTransVoltage_Type())
dellNetIfTransVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransVoltage.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransVoltage.setUnits('volts')
class _DellNetIfTransTransmitBiasCurrentLane1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransTransmitBiasCurrentLane1_Type.__name__=_D
_DellNetIfTransTransmitBiasCurrentLane1_Object=MibTableColumn
dellNetIfTransTransmitBiasCurrentLane1=_DellNetIfTransTransmitBiasCurrentLane1_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,18),_DellNetIfTransTransmitBiasCurrentLane1_Type())
dellNetIfTransTransmitBiasCurrentLane1.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransTransmitBiasCurrentLane1.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransTransmitBiasCurrentLane1.setUnits(_J)
class _DellNetIfTransTransmitBiasCurrentLane2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransTransmitBiasCurrentLane2_Type.__name__=_D
_DellNetIfTransTransmitBiasCurrentLane2_Object=MibTableColumn
dellNetIfTransTransmitBiasCurrentLane2=_DellNetIfTransTransmitBiasCurrentLane2_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,19),_DellNetIfTransTransmitBiasCurrentLane2_Type())
dellNetIfTransTransmitBiasCurrentLane2.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransTransmitBiasCurrentLane2.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransTransmitBiasCurrentLane2.setUnits(_J)
class _DellNetIfTransTransmitBiasCurrentLane3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransTransmitBiasCurrentLane3_Type.__name__=_D
_DellNetIfTransTransmitBiasCurrentLane3_Object=MibTableColumn
dellNetIfTransTransmitBiasCurrentLane3=_DellNetIfTransTransmitBiasCurrentLane3_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,20),_DellNetIfTransTransmitBiasCurrentLane3_Type())
dellNetIfTransTransmitBiasCurrentLane3.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransTransmitBiasCurrentLane3.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransTransmitBiasCurrentLane3.setUnits(_J)
class _DellNetIfTransTransmitBiasCurrentLane4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_DellNetIfTransTransmitBiasCurrentLane4_Type.__name__=_D
_DellNetIfTransTransmitBiasCurrentLane4_Object=MibTableColumn
dellNetIfTransTransmitBiasCurrentLane4=_DellNetIfTransTransmitBiasCurrentLane4_Object((1,3,6,1,4,1,6027,3,11,1,3,1,1,21),_DellNetIfTransTransmitBiasCurrentLane4_Type())
dellNetIfTransTransmitBiasCurrentLane4.setMaxAccess(_C)
if mibBuilder.loadTexts:dellNetIfTransTransmitBiasCurrentLane4.setStatus(_A)
if mibBuilder.loadTexts:dellNetIfTransTransmitBiasCurrentLane4.setUnits(_J)
_DellNetIfAlarmObjects_ObjectIdentity=ObjectIdentity
dellNetIfAlarmObjects=_DellNetIfAlarmObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,11,1,4))
_DellNetIfAlarmMibNotifications_ObjectIdentity=ObjectIdentity
dellNetIfAlarmMibNotifications=_DellNetIfAlarmMibNotifications_ObjectIdentity((1,3,6,1,4,1,6027,3,11,1,4,1))
_DellNetIfExtensionMibConformance_ObjectIdentity=ObjectIdentity
dellNetIfExtensionMibConformance=_DellNetIfExtensionMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,11,2))
_DellNetIfExtensionMibCompliances_ObjectIdentity=ObjectIdentity
dellNetIfExtensionMibCompliances=_DellNetIfExtensionMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,11,2,1))
_DellNetIfExtensionMibGroups_ObjectIdentity=ObjectIdentity
dellNetIfExtensionMibGroups=_DellNetIfExtensionMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,11,2,2))
dellNetIfParamsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,11,2,2,1))
dellNetIfParamsGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:dellNetIfParamsGroup.setStatus(_A)
dellNetIfStatsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,11,2,2,2))
dellNetIfStatsGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:dellNetIfStatsGroup.setStatus(_A)
dellNetIfTransceiverDataGroup=ObjectGroup((1,3,6,1,4,1,6027,3,11,2,2,3))
dellNetIfTransceiverDataGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:dellNetIfTransceiverDataGroup.setStatus(_A)
dellNetIfAlarmHighBer=NotificationType((1,3,6,1,4,1,6027,3,11,1,4,1,1))
dellNetIfAlarmHighBer.setObjects((_G,_H))
if mibBuilder.loadTexts:dellNetIfAlarmHighBer.setStatus(_A)
dellNetIfAlarmHighBerClr=NotificationType((1,3,6,1,4,1,6027,3,11,1,4,1,2))
dellNetIfAlarmHighBerClr.setObjects((_G,_H))
if mibBuilder.loadTexts:dellNetIfAlarmHighBerClr.setStatus(_A)
dellNetIfAlarmFastRetrain=NotificationType((1,3,6,1,4,1,6027,3,11,1,4,1,3))
dellNetIfAlarmFastRetrain.setObjects((_G,_H))
if mibBuilder.loadTexts:dellNetIfAlarmFastRetrain.setStatus(_A)
dellNetIfNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,11,2,2,4))
dellNetIfNotificationGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:dellNetIfNotificationGroup.setStatus(_A)
dellNetIfExtensionMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,11,2,1,1))
dellNetIfExtensionMibCompliance.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:dellNetIfExtensionMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dellNetIfExtensionMib':dellNetIfExtensionMib,'dellNetIfExtensionMibObject':dellNetIfExtensionMibObject,'dellNetIfExtensionParams':dellNetIfExtensionParams,'dellNetIfTable':dellNetIfTable,'dellNetIfEntry':dellNetIfEntry,_M:dellNetIfIpMtu,_N:dellNetIfDuplexMode,_O:dellNetIfQueueingStrategy,_P:dellNetIfRxFlowCtrl,_Q:dellNetIfTxFlowCtrl,_R:dellNetIfDescr,_S:dellNetIfAdminStatus,_T:dellNetIfRateInterval,_U:dellNetIfSpeed,_V:dellNetIfPortListBitPos,'dellNetIfExtensionStats':dellNetIfExtensionStats,'dellNetIfStaticsTable':dellNetIfStaticsTable,'dellNetIfStaticsEntry':dellNetIfStaticsEntry,_W:dellNetIfInVlanPkts,_X:dellNetIfIn64BytePkts,_Y:dellNetIfIn65To127BytePkts,_Z:dellNetIfIn128To255BytePkts,_a:dellNetIfIn256To511BytePkts,_b:dellNetIfIn512To1023BytePkts,_c:dellNetIfInOver1023BytePkts,_d:dellNetIfInThrottles,_e:dellNetIfInRunts,_f:dellNetIfInGiants,_g:dellNetIfInCRC,_h:dellNetIfInOverruns,_i:dellNetIfOutVlanPkts,_j:dellNetIfOutUnderruns,_k:dellNetIfOutUnicasts,_l:dellNetIfOutCollisions,_m:dellNetIfOutWredDrops,_n:dellNetIfOut64BytePkts,_o:dellNetIfOut65To127BytePkts,_p:dellNetIfOut128To255BytePkts,_q:dellNetIfOut256To511BytePkts,_r:dellNetIfOut512To1023BytePkts,_s:dellNetIfOutOver1023BytePkts,_t:dellNetIfOutThrottles,_u:dellNetIfLastDiscontinuityTime,_v:dellNetIfInCentRate,_w:dellNetIfOutCentRate,'dellNetIfTransceiverData':dellNetIfTransceiverData,'dellNetIfTransceiverDataTable':dellNetIfTransceiverDataTable,'dellNetIfTransceiverDataEntry':dellNetIfTransceiverDataEntry,_x:dellNetIfTransDeviceName,_y:dellNetIfTransPort,_z:dellNetIfTransOpticsPresent,_A0:dellNetIfTransOpticsType,_A1:dellNetIfTransVendorName,_A2:dellNetIfTransPartNumber,_A3:dellNetIfTransSerialNumber,_A4:dellNetIfTransTransmitPowerLane1,_A5:dellNetIfTransTransmitPowerLane2,_A6:dellNetIfTransTransmitPowerLane3,_A7:dellNetIfTransTransmitPowerLane4,_A8:dellNetIfTransReceivePowerLane1,_A9:dellNetIfTransReceivePowerLane2,_AA:dellNetIfTransReceivePowerLane3,_AB:dellNetIfTransReceivePowerLane4,_AC:dellNetIfTransTemperature,_AD:dellNetIfTransVoltage,_AE:dellNetIfTransTransmitBiasCurrentLane1,_AF:dellNetIfTransTransmitBiasCurrentLane2,_AG:dellNetIfTransTransmitBiasCurrentLane3,_AH:dellNetIfTransTransmitBiasCurrentLane4,'dellNetIfAlarmObjects':dellNetIfAlarmObjects,'dellNetIfAlarmMibNotifications':dellNetIfAlarmMibNotifications,_AI:dellNetIfAlarmHighBer,_AJ:dellNetIfAlarmHighBerClr,_AK:dellNetIfAlarmFastRetrain,'dellNetIfExtensionMibConformance':dellNetIfExtensionMibConformance,'dellNetIfExtensionMibCompliances':dellNetIfExtensionMibCompliances,'dellNetIfExtensionMibCompliance':dellNetIfExtensionMibCompliance,'dellNetIfExtensionMibGroups':dellNetIfExtensionMibGroups,_AL:dellNetIfParamsGroup,_AM:dellNetIfStatsGroup,_AN:dellNetIfTransceiverDataGroup,_AO:dellNetIfNotificationGroup})