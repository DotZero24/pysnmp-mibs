_w='f10IfStatsGroup'
_v='f10IfParamsGroup'
_u='f10IfOutCentRate'
_t='f10IfInCentRate'
_s='f10IfLastDiscontinuityTime'
_r='f10IfOutThrottles'
_q='f10IfOutOver1023BytePkts'
_p='f10IfOut512To1023BytePkts'
_o='f10IfOut256To511BytePkts'
_n='f10IfOut128To255BytePkts'
_m='f10IfOut65To127BytePkts'
_l='f10IfOut64BytePkts'
_k='f10IfOutWredDrops'
_j='f10IfOutCollisions'
_i='f10IfOutUnicasts'
_h='f10IfOutUnderruns'
_g='f10IfOutVlanPkts'
_f='f10IfInOverruns'
_e='f10IfInCRC'
_d='f10IfInGiants'
_c='f10IfInRunts'
_b='f10IfInThrottles'
_a='f10IfInOver1023BytePkts'
_Z='f10IfIn512To1023BytePkts'
_Y='f10IfIn256To511BytePkts'
_X='f10IfIn128To255BytePkts'
_W='f10ifIn65To127BytePkts'
_V='f10IfIn64BytePkts'
_U='f10IfInVlanPkts'
_T='f10IfPortListBitPos'
_S='f10IfSpeed'
_R='f10IfRateInterval'
_Q='f10IfAdminStatus'
_P='f10IfDescr'
_O='f10IfTxFlowCtrl'
_N='f10IfRxFlowCtrl'
_M='f10IfQueueingStrategy'
_L='f10IfDuplexMode'
_K='f10IfIpMtu'
_J='DisplayString'
_I='OctetString'
_H='Unsigned32'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='F10-IF-EXTENSION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
f10IfExtensionMib=ModuleIdentity((1,3,6,1,4,1,6027,3,11))
if mibBuilder.loadTexts:f10IfExtensionMib.setRevisions(('2014-08-12 12:00','2012-03-06 12:00','2010-08-11 12:00','2010-08-10 12:00'))
_F10IfExtensionMibObject_ObjectIdentity=ObjectIdentity
f10IfExtensionMibObject=_F10IfExtensionMibObject_ObjectIdentity((1,3,6,1,4,1,6027,3,11,1))
_F10IfExtensionParams_ObjectIdentity=ObjectIdentity
f10IfExtensionParams=_F10IfExtensionParams_ObjectIdentity((1,3,6,1,4,1,6027,3,11,1,1))
_F10IfTable_Object=MibTable
f10IfTable=_F10IfTable_Object((1,3,6,1,4,1,6027,3,11,1,1,1))
if mibBuilder.loadTexts:f10IfTable.setStatus(_A)
_F10IfEntry_Object=MibTableRow
f10IfEntry=_F10IfEntry_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1))
f10IfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:f10IfEntry.setStatus(_A)
class _F10IfIpMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(594,9252))
_F10IfIpMtu_Type.__name__=_H
_F10IfIpMtu_Object=MibTableColumn
f10IfIpMtu=_F10IfIpMtu_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,1),_F10IfIpMtu_Type())
f10IfIpMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:f10IfIpMtu.setStatus(_A)
class _F10IfDuplexMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('half',1),('full',2),('auto',3)))
_F10IfDuplexMode_Type.__name__=_E
_F10IfDuplexMode_Object=MibTableColumn
f10IfDuplexMode=_F10IfDuplexMode_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,2),_F10IfDuplexMode_Type())
f10IfDuplexMode.setMaxAccess(_D)
if mibBuilder.loadTexts:f10IfDuplexMode.setStatus(_A)
class _F10IfQueueingStrategy_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_F10IfQueueingStrategy_Type.__name__=_J
_F10IfQueueingStrategy_Object=MibTableColumn
f10IfQueueingStrategy=_F10IfQueueingStrategy_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,3),_F10IfQueueingStrategy_Type())
f10IfQueueingStrategy.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfQueueingStrategy.setStatus(_A)
_F10IfRxFlowCtrl_Type=TruthValue
_F10IfRxFlowCtrl_Object=MibTableColumn
f10IfRxFlowCtrl=_F10IfRxFlowCtrl_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,4),_F10IfRxFlowCtrl_Type())
f10IfRxFlowCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:f10IfRxFlowCtrl.setStatus(_A)
_F10IfTxFlowCtrl_Type=TruthValue
_F10IfTxFlowCtrl_Object=MibTableColumn
f10IfTxFlowCtrl=_F10IfTxFlowCtrl_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,5),_F10IfTxFlowCtrl_Type())
f10IfTxFlowCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:f10IfTxFlowCtrl.setStatus(_A)
class _F10IfDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,241))
_F10IfDescr_Type.__name__=_I
_F10IfDescr_Object=MibTableColumn
f10IfDescr=_F10IfDescr_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,6),_F10IfDescr_Type())
f10IfDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:f10IfDescr.setStatus(_A)
class _F10IfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_F10IfAdminStatus_Type.__name__=_E
_F10IfAdminStatus_Object=MibTableColumn
f10IfAdminStatus=_F10IfAdminStatus_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,7),_F10IfAdminStatus_Type())
f10IfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:f10IfAdminStatus.setStatus(_A)
class _F10IfRateInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,299))
_F10IfRateInterval_Type.__name__=_H
_F10IfRateInterval_Object=MibTableColumn
f10IfRateInterval=_F10IfRateInterval_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,8),_F10IfRateInterval_Type())
f10IfRateInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:f10IfRateInterval.setStatus(_A)
class _F10IfSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,100,1000)));namedValues=NamedValues(*(('auto',1),('tenMbps',10),('hundredMbps',100),('thousandMbps',1000)))
_F10IfSpeed_Type.__name__=_E
_F10IfSpeed_Object=MibTableColumn
f10IfSpeed=_F10IfSpeed_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,9),_F10IfSpeed_Type())
f10IfSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:f10IfSpeed.setStatus(_A)
_F10IfPortListBitPos_Type=Integer32
_F10IfPortListBitPos_Object=MibTableColumn
f10IfPortListBitPos=_F10IfPortListBitPos_Object((1,3,6,1,4,1,6027,3,11,1,1,1,1,10),_F10IfPortListBitPos_Type())
f10IfPortListBitPos.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfPortListBitPos.setStatus(_A)
_F10IfExtensionStats_ObjectIdentity=ObjectIdentity
f10IfExtensionStats=_F10IfExtensionStats_ObjectIdentity((1,3,6,1,4,1,6027,3,11,1,2))
_F10IfStaticsTable_Object=MibTable
f10IfStaticsTable=_F10IfStaticsTable_Object((1,3,6,1,4,1,6027,3,11,1,2,1))
if mibBuilder.loadTexts:f10IfStaticsTable.setStatus(_A)
_F10IfStaticsEntry_Object=MibTableRow
f10IfStaticsEntry=_F10IfStaticsEntry_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1))
f10IfStaticsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:f10IfStaticsEntry.setStatus(_A)
_F10IfInVlanPkts_Type=Counter64
_F10IfInVlanPkts_Object=MibTableColumn
f10IfInVlanPkts=_F10IfInVlanPkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,1),_F10IfInVlanPkts_Type())
f10IfInVlanPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfInVlanPkts.setStatus(_A)
_F10IfIn64BytePkts_Type=Counter64
_F10IfIn64BytePkts_Object=MibTableColumn
f10IfIn64BytePkts=_F10IfIn64BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,2),_F10IfIn64BytePkts_Type())
f10IfIn64BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfIn64BytePkts.setStatus(_A)
_F10ifIn65To127BytePkts_Type=Counter64
_F10ifIn65To127BytePkts_Object=MibTableColumn
f10ifIn65To127BytePkts=_F10ifIn65To127BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,3),_F10ifIn65To127BytePkts_Type())
f10ifIn65To127BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10ifIn65To127BytePkts.setStatus(_A)
_F10IfIn128To255BytePkts_Type=Counter64
_F10IfIn128To255BytePkts_Object=MibTableColumn
f10IfIn128To255BytePkts=_F10IfIn128To255BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,4),_F10IfIn128To255BytePkts_Type())
f10IfIn128To255BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfIn128To255BytePkts.setStatus(_A)
_F10IfIn256To511BytePkts_Type=Counter64
_F10IfIn256To511BytePkts_Object=MibTableColumn
f10IfIn256To511BytePkts=_F10IfIn256To511BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,5),_F10IfIn256To511BytePkts_Type())
f10IfIn256To511BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfIn256To511BytePkts.setStatus(_A)
_F10IfIn512To1023BytePkts_Type=Counter64
_F10IfIn512To1023BytePkts_Object=MibTableColumn
f10IfIn512To1023BytePkts=_F10IfIn512To1023BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,6),_F10IfIn512To1023BytePkts_Type())
f10IfIn512To1023BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfIn512To1023BytePkts.setStatus(_A)
_F10IfInOver1023BytePkts_Type=Counter64
_F10IfInOver1023BytePkts_Object=MibTableColumn
f10IfInOver1023BytePkts=_F10IfInOver1023BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,7),_F10IfInOver1023BytePkts_Type())
f10IfInOver1023BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfInOver1023BytePkts.setStatus(_A)
_F10IfInThrottles_Type=Counter64
_F10IfInThrottles_Object=MibTableColumn
f10IfInThrottles=_F10IfInThrottles_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,8),_F10IfInThrottles_Type())
f10IfInThrottles.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfInThrottles.setStatus(_A)
_F10IfInRunts_Type=Counter64
_F10IfInRunts_Object=MibTableColumn
f10IfInRunts=_F10IfInRunts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,9),_F10IfInRunts_Type())
f10IfInRunts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfInRunts.setStatus(_A)
_F10IfInGiants_Type=Counter64
_F10IfInGiants_Object=MibTableColumn
f10IfInGiants=_F10IfInGiants_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,10),_F10IfInGiants_Type())
f10IfInGiants.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfInGiants.setStatus(_A)
_F10IfInCRC_Type=Counter64
_F10IfInCRC_Object=MibTableColumn
f10IfInCRC=_F10IfInCRC_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,11),_F10IfInCRC_Type())
f10IfInCRC.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfInCRC.setStatus(_A)
_F10IfInOverruns_Type=Counter64
_F10IfInOverruns_Object=MibTableColumn
f10IfInOverruns=_F10IfInOverruns_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,12),_F10IfInOverruns_Type())
f10IfInOverruns.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfInOverruns.setStatus(_A)
_F10IfOutVlanPkts_Type=Counter64
_F10IfOutVlanPkts_Object=MibTableColumn
f10IfOutVlanPkts=_F10IfOutVlanPkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,13),_F10IfOutVlanPkts_Type())
f10IfOutVlanPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOutVlanPkts.setStatus(_A)
_F10IfOutUnderruns_Type=Counter64
_F10IfOutUnderruns_Object=MibTableColumn
f10IfOutUnderruns=_F10IfOutUnderruns_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,14),_F10IfOutUnderruns_Type())
f10IfOutUnderruns.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOutUnderruns.setStatus(_A)
_F10IfOutUnicasts_Type=Counter64
_F10IfOutUnicasts_Object=MibTableColumn
f10IfOutUnicasts=_F10IfOutUnicasts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,15),_F10IfOutUnicasts_Type())
f10IfOutUnicasts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOutUnicasts.setStatus(_A)
_F10IfOutCollisions_Type=Counter64
_F10IfOutCollisions_Object=MibTableColumn
f10IfOutCollisions=_F10IfOutCollisions_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,16),_F10IfOutCollisions_Type())
f10IfOutCollisions.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOutCollisions.setStatus(_A)
_F10IfOutWredDrops_Type=Counter64
_F10IfOutWredDrops_Object=MibTableColumn
f10IfOutWredDrops=_F10IfOutWredDrops_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,17),_F10IfOutWredDrops_Type())
f10IfOutWredDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOutWredDrops.setStatus(_A)
_F10IfOut64BytePkts_Type=Counter64
_F10IfOut64BytePkts_Object=MibTableColumn
f10IfOut64BytePkts=_F10IfOut64BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,18),_F10IfOut64BytePkts_Type())
f10IfOut64BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOut64BytePkts.setStatus(_A)
_F10IfOut65To127BytePkts_Type=Counter64
_F10IfOut65To127BytePkts_Object=MibTableColumn
f10IfOut65To127BytePkts=_F10IfOut65To127BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,19),_F10IfOut65To127BytePkts_Type())
f10IfOut65To127BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOut65To127BytePkts.setStatus(_A)
_F10IfOut128To255BytePkts_Type=Counter64
_F10IfOut128To255BytePkts_Object=MibTableColumn
f10IfOut128To255BytePkts=_F10IfOut128To255BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,20),_F10IfOut128To255BytePkts_Type())
f10IfOut128To255BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOut128To255BytePkts.setStatus(_A)
_F10IfOut256To511BytePkts_Type=Counter64
_F10IfOut256To511BytePkts_Object=MibTableColumn
f10IfOut256To511BytePkts=_F10IfOut256To511BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,21),_F10IfOut256To511BytePkts_Type())
f10IfOut256To511BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOut256To511BytePkts.setStatus(_A)
_F10IfOut512To1023BytePkts_Type=Counter64
_F10IfOut512To1023BytePkts_Object=MibTableColumn
f10IfOut512To1023BytePkts=_F10IfOut512To1023BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,22),_F10IfOut512To1023BytePkts_Type())
f10IfOut512To1023BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOut512To1023BytePkts.setStatus(_A)
_F10IfOutOver1023BytePkts_Type=Counter64
_F10IfOutOver1023BytePkts_Object=MibTableColumn
f10IfOutOver1023BytePkts=_F10IfOutOver1023BytePkts_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,23),_F10IfOutOver1023BytePkts_Type())
f10IfOutOver1023BytePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOutOver1023BytePkts.setStatus(_A)
_F10IfOutThrottles_Type=Counter64
_F10IfOutThrottles_Object=MibTableColumn
f10IfOutThrottles=_F10IfOutThrottles_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,24),_F10IfOutThrottles_Type())
f10IfOutThrottles.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOutThrottles.setStatus(_A)
_F10IfLastDiscontinuityTime_Type=TimeStamp
_F10IfLastDiscontinuityTime_Object=MibTableColumn
f10IfLastDiscontinuityTime=_F10IfLastDiscontinuityTime_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,25),_F10IfLastDiscontinuityTime_Type())
f10IfLastDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfLastDiscontinuityTime.setStatus(_A)
class _F10IfInCentRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_F10IfInCentRate_Type.__name__=_E
_F10IfInCentRate_Object=MibTableColumn
f10IfInCentRate=_F10IfInCentRate_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,26),_F10IfInCentRate_Type())
f10IfInCentRate.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfInCentRate.setStatus(_A)
class _F10IfOutCentRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_F10IfOutCentRate_Type.__name__=_E
_F10IfOutCentRate_Object=MibTableColumn
f10IfOutCentRate=_F10IfOutCentRate_Object((1,3,6,1,4,1,6027,3,11,1,2,1,1,27),_F10IfOutCentRate_Type())
f10IfOutCentRate.setMaxAccess(_C)
if mibBuilder.loadTexts:f10IfOutCentRate.setStatus(_A)
_F10IfExtensionMibConformance_ObjectIdentity=ObjectIdentity
f10IfExtensionMibConformance=_F10IfExtensionMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,11,2))
_F10IfExtensionMibCompliances_ObjectIdentity=ObjectIdentity
f10IfExtensionMibCompliances=_F10IfExtensionMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,11,2,1))
_F10IfExtensionMibGroups_ObjectIdentity=ObjectIdentity
f10IfExtensionMibGroups=_F10IfExtensionMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,11,2,2))
f10IfParamsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,11,2,2,1))
f10IfParamsGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:f10IfParamsGroup.setStatus(_A)
f10IfStatsGroup=ObjectGroup((1,3,6,1,4,1,6027,3,11,2,2,2))
f10IfStatsGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:f10IfStatsGroup.setStatus(_A)
f10IfExtensionMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,11,2,1,1))
f10IfExtensionMibCompliance.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:f10IfExtensionMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'f10IfExtensionMib':f10IfExtensionMib,'f10IfExtensionMibObject':f10IfExtensionMibObject,'f10IfExtensionParams':f10IfExtensionParams,'f10IfTable':f10IfTable,'f10IfEntry':f10IfEntry,_K:f10IfIpMtu,_L:f10IfDuplexMode,_M:f10IfQueueingStrategy,_N:f10IfRxFlowCtrl,_O:f10IfTxFlowCtrl,_P:f10IfDescr,_Q:f10IfAdminStatus,_R:f10IfRateInterval,_S:f10IfSpeed,_T:f10IfPortListBitPos,'f10IfExtensionStats':f10IfExtensionStats,'f10IfStaticsTable':f10IfStaticsTable,'f10IfStaticsEntry':f10IfStaticsEntry,_U:f10IfInVlanPkts,_V:f10IfIn64BytePkts,_W:f10ifIn65To127BytePkts,_X:f10IfIn128To255BytePkts,_Y:f10IfIn256To511BytePkts,_Z:f10IfIn512To1023BytePkts,_a:f10IfInOver1023BytePkts,_b:f10IfInThrottles,_c:f10IfInRunts,_d:f10IfInGiants,_e:f10IfInCRC,_f:f10IfInOverruns,_g:f10IfOutVlanPkts,_h:f10IfOutUnderruns,_i:f10IfOutUnicasts,_j:f10IfOutCollisions,_k:f10IfOutWredDrops,_l:f10IfOut64BytePkts,_m:f10IfOut65To127BytePkts,_n:f10IfOut128To255BytePkts,_o:f10IfOut256To511BytePkts,_p:f10IfOut512To1023BytePkts,_q:f10IfOutOver1023BytePkts,_r:f10IfOutThrottles,_s:f10IfLastDiscontinuityTime,_t:f10IfInCentRate,_u:f10IfOutCentRate,'f10IfExtensionMibConformance':f10IfExtensionMibConformance,'f10IfExtensionMibCompliances':f10IfExtensionMibCompliances,'f10IfExtensionMibCompliance':f10IfExtensionMibCompliance,'f10IfExtensionMibGroups':f10IfExtensionMibGroups,_v:f10IfParamsGroup,_w:f10IfStatsGroup})