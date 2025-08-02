_A1='ciscoObmiMIBM500ObjectGroup'
_A0='ciscoObmiMIBMainObjectGroup'
_z='cObmiM500CommandOverWrt'
_y='cObmiM500CommandTimeout'
_x='cObmiM500CommandParityErr'
_w='cObmiM500TelemetryReqParityErr'
_v='cObmiM500CommandOverWrts'
_u='cObmiM500HWParityErr'
_t='cObmiM500CommandErrs'
_s='cObmiM500TelemetryErrs'
_r='cObmiM500TelemetrySent'
_q='cObmiM500CommandsRcvd'
_p='cObmiM500LastActiveBus'
_o='cObmiM500BusBLOS'
_n='cObmiM500BusALOS'
_m='cObmiM500TxCtlQOverRun'
_l='cObmiM500TxQ1UnderRun'
_k='cObmiM500TxQ0UnderRun'
_j='cObmiM500RxQOverRun'
_i='cObmiM500TxTransportErrFrames'
_h='cObmiM500TxEchoFrames'
_g='cObmiM500TxAbortFrames'
_f='cObmiM500TxBytes'
_e='cObmiM500TxFrames'
_d='cObmiM500RxUnknownOpFrames'
_c='cObmiM500RxTransportErrFrames'
_b='cObmiM500RxResetFrames'
_a='cObmiM500RxEchoFrames'
_Z='cObmiM500RxAbortFrames'
_Y='cObmiM500RxBytes'
_X='cObmiM500RxFrames'
_W='cObmiHeartBeatPending'
_V='cObmiHeartBeatSent'
_U='cObmiTelemetryPending'
_T='cObmiTelemetryDemandSent'
_S='cObmiTelemetrySent'
_R='cObmiCommandDropped'
_Q='cObmiCommandPending'
_P='cObmiCommandProcessedInvalid'
_O='cObmiCommandSets'
_N='cObmiCommandGets'
_M='cObmiCommandProcessedTotal'
_L='cObmiCommandRx'
_K='cObmiBusName'
_J='cObmiHeartBeatPort'
_I='not-accessible'
_H='Unsigned32'
_G='Words'
_F='cObmiBusID'
_E='Frames'
_D='Messages'
_C='read-only'
_B='CISCO-OBMI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoObmiMIB=ModuleIdentity((1,3,6,1,4,1,9,9,698))
if mibBuilder.loadTexts:ciscoObmiMIB.setRevisions(('2009-05-28 00:00',))
_CiscoObmiMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoObmiMIBNotifs=_CiscoObmiMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,698,0))
_CiscoObmiMIBObjects_ObjectIdentity=ObjectIdentity
ciscoObmiMIBObjects=_CiscoObmiMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,698,1))
_CObmiTransportTable_Object=MibTable
cObmiTransportTable=_CObmiTransportTable_Object((1,3,6,1,4,1,9,9,698,1,2))
if mibBuilder.loadTexts:cObmiTransportTable.setStatus(_A)
_CObmiTransportEntry_Object=MibTableRow
cObmiTransportEntry=_CObmiTransportEntry_Object((1,3,6,1,4,1,9,9,698,1,2,1))
cObmiTransportEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cObmiTransportEntry.setStatus(_A)
class _CObmiBusID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CObmiBusID_Type.__name__=_H
_CObmiBusID_Object=MibTableColumn
cObmiBusID=_CObmiBusID_Object((1,3,6,1,4,1,9,9,698,1,2,1,1),_CObmiBusID_Type())
cObmiBusID.setMaxAccess(_I)
if mibBuilder.loadTexts:cObmiBusID.setStatus(_A)
_CObmiBusName_Type=DisplayString
_CObmiBusName_Object=MibTableColumn
cObmiBusName=_CObmiBusName_Object((1,3,6,1,4,1,9,9,698,1,2,1,2),_CObmiBusName_Type())
cObmiBusName.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiBusName.setStatus(_A)
_CObmiCommandRx_Type=Counter32
_CObmiCommandRx_Object=MibTableColumn
cObmiCommandRx=_CObmiCommandRx_Object((1,3,6,1,4,1,9,9,698,1,2,1,3),_CObmiCommandRx_Type())
cObmiCommandRx.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiCommandRx.setStatus(_A)
if mibBuilder.loadTexts:cObmiCommandRx.setUnits(_D)
_CObmiCommandProcessedTotal_Type=Counter32
_CObmiCommandProcessedTotal_Object=MibTableColumn
cObmiCommandProcessedTotal=_CObmiCommandProcessedTotal_Object((1,3,6,1,4,1,9,9,698,1,2,1,4),_CObmiCommandProcessedTotal_Type())
cObmiCommandProcessedTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiCommandProcessedTotal.setStatus(_A)
if mibBuilder.loadTexts:cObmiCommandProcessedTotal.setUnits(_D)
_CObmiCommandGets_Type=Counter32
_CObmiCommandGets_Object=MibTableColumn
cObmiCommandGets=_CObmiCommandGets_Object((1,3,6,1,4,1,9,9,698,1,2,1,5),_CObmiCommandGets_Type())
cObmiCommandGets.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiCommandGets.setStatus(_A)
if mibBuilder.loadTexts:cObmiCommandGets.setUnits(_D)
_CObmiCommandSets_Type=Counter32
_CObmiCommandSets_Object=MibTableColumn
cObmiCommandSets=_CObmiCommandSets_Object((1,3,6,1,4,1,9,9,698,1,2,1,6),_CObmiCommandSets_Type())
cObmiCommandSets.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiCommandSets.setStatus(_A)
if mibBuilder.loadTexts:cObmiCommandSets.setUnits(_D)
_CObmiCommandProcessedInvalid_Type=Counter32
_CObmiCommandProcessedInvalid_Object=MibTableColumn
cObmiCommandProcessedInvalid=_CObmiCommandProcessedInvalid_Object((1,3,6,1,4,1,9,9,698,1,2,1,7),_CObmiCommandProcessedInvalid_Type())
cObmiCommandProcessedInvalid.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiCommandProcessedInvalid.setStatus(_A)
if mibBuilder.loadTexts:cObmiCommandProcessedInvalid.setUnits(_D)
_CObmiCommandPending_Type=Gauge32
_CObmiCommandPending_Object=MibTableColumn
cObmiCommandPending=_CObmiCommandPending_Object((1,3,6,1,4,1,9,9,698,1,2,1,8),_CObmiCommandPending_Type())
cObmiCommandPending.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiCommandPending.setStatus(_A)
if mibBuilder.loadTexts:cObmiCommandPending.setUnits(_D)
_CObmiCommandDropped_Type=Counter32
_CObmiCommandDropped_Object=MibTableColumn
cObmiCommandDropped=_CObmiCommandDropped_Object((1,3,6,1,4,1,9,9,698,1,2,1,9),_CObmiCommandDropped_Type())
cObmiCommandDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiCommandDropped.setStatus(_A)
if mibBuilder.loadTexts:cObmiCommandDropped.setUnits(_D)
_CObmiTelemetrySent_Type=Counter32
_CObmiTelemetrySent_Object=MibTableColumn
cObmiTelemetrySent=_CObmiTelemetrySent_Object((1,3,6,1,4,1,9,9,698,1,2,1,10),_CObmiTelemetrySent_Type())
cObmiTelemetrySent.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiTelemetrySent.setStatus(_A)
if mibBuilder.loadTexts:cObmiTelemetrySent.setUnits(_D)
_CObmiTelemetryDemandSent_Type=Counter32
_CObmiTelemetryDemandSent_Object=MibTableColumn
cObmiTelemetryDemandSent=_CObmiTelemetryDemandSent_Object((1,3,6,1,4,1,9,9,698,1,2,1,11),_CObmiTelemetryDemandSent_Type())
cObmiTelemetryDemandSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiTelemetryDemandSent.setStatus(_A)
if mibBuilder.loadTexts:cObmiTelemetryDemandSent.setUnits(_D)
_CObmiTelemetryPending_Type=Gauge32
_CObmiTelemetryPending_Object=MibTableColumn
cObmiTelemetryPending=_CObmiTelemetryPending_Object((1,3,6,1,4,1,9,9,698,1,2,1,12),_CObmiTelemetryPending_Type())
cObmiTelemetryPending.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiTelemetryPending.setStatus(_A)
if mibBuilder.loadTexts:cObmiTelemetryPending.setUnits(_D)
_CObmiTransportHeartBeatTable_Object=MibTable
cObmiTransportHeartBeatTable=_CObmiTransportHeartBeatTable_Object((1,3,6,1,4,1,9,9,698,1,3))
if mibBuilder.loadTexts:cObmiTransportHeartBeatTable.setStatus(_A)
_CObmiTransportHeartBeatEntry_Object=MibTableRow
cObmiTransportHeartBeatEntry=_CObmiTransportHeartBeatEntry_Object((1,3,6,1,4,1,9,9,698,1,3,1))
cObmiTransportHeartBeatEntry.setIndexNames((0,_B,_F),(0,_B,_J))
if mibBuilder.loadTexts:cObmiTransportHeartBeatEntry.setStatus(_A)
class _CObmiHeartBeatPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CObmiHeartBeatPort_Type.__name__=_H
_CObmiHeartBeatPort_Object=MibTableColumn
cObmiHeartBeatPort=_CObmiHeartBeatPort_Object((1,3,6,1,4,1,9,9,698,1,3,1,1),_CObmiHeartBeatPort_Type())
cObmiHeartBeatPort.setMaxAccess(_I)
if mibBuilder.loadTexts:cObmiHeartBeatPort.setStatus(_A)
_CObmiHeartBeatSent_Type=Counter32
_CObmiHeartBeatSent_Object=MibTableColumn
cObmiHeartBeatSent=_CObmiHeartBeatSent_Object((1,3,6,1,4,1,9,9,698,1,3,1,2),_CObmiHeartBeatSent_Type())
cObmiHeartBeatSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiHeartBeatSent.setStatus(_A)
if mibBuilder.loadTexts:cObmiHeartBeatSent.setUnits(_D)
_CObmiHeartBeatPending_Type=Gauge32
_CObmiHeartBeatPending_Object=MibTableColumn
cObmiHeartBeatPending=_CObmiHeartBeatPending_Object((1,3,6,1,4,1,9,9,698,1,3,1,3),_CObmiHeartBeatPending_Type())
cObmiHeartBeatPending.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiHeartBeatPending.setStatus(_A)
if mibBuilder.loadTexts:cObmiHeartBeatPending.setUnits(_D)
_CObmiM500FramingTable_Object=MibTable
cObmiM500FramingTable=_CObmiM500FramingTable_Object((1,3,6,1,4,1,9,9,698,1,4))
if mibBuilder.loadTexts:cObmiM500FramingTable.setStatus(_A)
_CObmiM500FramingEntry_Object=MibTableRow
cObmiM500FramingEntry=_CObmiM500FramingEntry_Object((1,3,6,1,4,1,9,9,698,1,4,1))
cObmiM500FramingEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cObmiM500FramingEntry.setStatus(_A)
_CObmiM500RxFrames_Type=Counter32
_CObmiM500RxFrames_Object=MibTableColumn
cObmiM500RxFrames=_CObmiM500RxFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,1),_CObmiM500RxFrames_Type())
cObmiM500RxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500RxFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500RxFrames.setUnits(_E)
_CObmiM500RxBytes_Type=Counter32
_CObmiM500RxBytes_Object=MibTableColumn
cObmiM500RxBytes=_CObmiM500RxBytes_Object((1,3,6,1,4,1,9,9,698,1,4,1,2),_CObmiM500RxBytes_Type())
cObmiM500RxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500RxBytes.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500RxBytes.setUnits('Bytes')
_CObmiM500RxAbortFrames_Type=Counter32
_CObmiM500RxAbortFrames_Object=MibTableColumn
cObmiM500RxAbortFrames=_CObmiM500RxAbortFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,3),_CObmiM500RxAbortFrames_Type())
cObmiM500RxAbortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500RxAbortFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500RxAbortFrames.setUnits(_E)
_CObmiM500RxEchoFrames_Type=Counter32
_CObmiM500RxEchoFrames_Object=MibTableColumn
cObmiM500RxEchoFrames=_CObmiM500RxEchoFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,4),_CObmiM500RxEchoFrames_Type())
cObmiM500RxEchoFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500RxEchoFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500RxEchoFrames.setUnits(_E)
_CObmiM500RxResetFrames_Type=Counter32
_CObmiM500RxResetFrames_Object=MibTableColumn
cObmiM500RxResetFrames=_CObmiM500RxResetFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,5),_CObmiM500RxResetFrames_Type())
cObmiM500RxResetFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500RxResetFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500RxResetFrames.setUnits(_E)
_CObmiM500RxTransportErrFrames_Type=Counter32
_CObmiM500RxTransportErrFrames_Object=MibTableColumn
cObmiM500RxTransportErrFrames=_CObmiM500RxTransportErrFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,6),_CObmiM500RxTransportErrFrames_Type())
cObmiM500RxTransportErrFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500RxTransportErrFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500RxTransportErrFrames.setUnits(_E)
_CObmiM500RxUnknownOpFrames_Type=Counter32
_CObmiM500RxUnknownOpFrames_Object=MibTableColumn
cObmiM500RxUnknownOpFrames=_CObmiM500RxUnknownOpFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,7),_CObmiM500RxUnknownOpFrames_Type())
cObmiM500RxUnknownOpFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500RxUnknownOpFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500RxUnknownOpFrames.setUnits(_E)
_CObmiM500TxFrames_Type=Counter32
_CObmiM500TxFrames_Object=MibTableColumn
cObmiM500TxFrames=_CObmiM500TxFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,8),_CObmiM500TxFrames_Type())
cObmiM500TxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TxFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TxFrames.setUnits(_E)
_CObmiM500TxBytes_Type=Counter32
_CObmiM500TxBytes_Object=MibTableColumn
cObmiM500TxBytes=_CObmiM500TxBytes_Object((1,3,6,1,4,1,9,9,698,1,4,1,9),_CObmiM500TxBytes_Type())
cObmiM500TxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TxBytes.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TxBytes.setUnits(_E)
_CObmiM500TxAbortFrames_Type=Counter32
_CObmiM500TxAbortFrames_Object=MibTableColumn
cObmiM500TxAbortFrames=_CObmiM500TxAbortFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,10),_CObmiM500TxAbortFrames_Type())
cObmiM500TxAbortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TxAbortFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TxAbortFrames.setUnits(_E)
_CObmiM500TxEchoFrames_Type=Counter32
_CObmiM500TxEchoFrames_Object=MibTableColumn
cObmiM500TxEchoFrames=_CObmiM500TxEchoFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,11),_CObmiM500TxEchoFrames_Type())
cObmiM500TxEchoFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TxEchoFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TxEchoFrames.setUnits(_E)
_CObmiM500TxTransportErrFrames_Type=Counter32
_CObmiM500TxTransportErrFrames_Object=MibTableColumn
cObmiM500TxTransportErrFrames=_CObmiM500TxTransportErrFrames_Object((1,3,6,1,4,1,9,9,698,1,4,1,12),_CObmiM500TxTransportErrFrames_Type())
cObmiM500TxTransportErrFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TxTransportErrFrames.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TxTransportErrFrames.setUnits(_E)
_CObmiM500RxQOverRun_Type=Counter32
_CObmiM500RxQOverRun_Object=MibTableColumn
cObmiM500RxQOverRun=_CObmiM500RxQOverRun_Object((1,3,6,1,4,1,9,9,698,1,4,1,13),_CObmiM500RxQOverRun_Type())
cObmiM500RxQOverRun.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500RxQOverRun.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500RxQOverRun.setUnits(_D)
_CObmiM500TxQ0UnderRun_Type=Counter32
_CObmiM500TxQ0UnderRun_Object=MibTableColumn
cObmiM500TxQ0UnderRun=_CObmiM500TxQ0UnderRun_Object((1,3,6,1,4,1,9,9,698,1,4,1,14),_CObmiM500TxQ0UnderRun_Type())
cObmiM500TxQ0UnderRun.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TxQ0UnderRun.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TxQ0UnderRun.setUnits(_D)
_CObmiM500TxQ1UnderRun_Type=Counter32
_CObmiM500TxQ1UnderRun_Object=MibTableColumn
cObmiM500TxQ1UnderRun=_CObmiM500TxQ1UnderRun_Object((1,3,6,1,4,1,9,9,698,1,4,1,15),_CObmiM500TxQ1UnderRun_Type())
cObmiM500TxQ1UnderRun.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TxQ1UnderRun.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TxQ1UnderRun.setUnits(_D)
_CObmiM500TxCtlQOverRun_Type=Counter32
_CObmiM500TxCtlQOverRun_Object=MibTableColumn
cObmiM500TxCtlQOverRun=_CObmiM500TxCtlQOverRun_Object((1,3,6,1,4,1,9,9,698,1,4,1,16),_CObmiM500TxCtlQOverRun_Type())
cObmiM500TxCtlQOverRun.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TxCtlQOverRun.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TxCtlQOverRun.setUnits(_D)
_CObmiM500PhyTable_Object=MibTable
cObmiM500PhyTable=_CObmiM500PhyTable_Object((1,3,6,1,4,1,9,9,698,1,5))
if mibBuilder.loadTexts:cObmiM500PhyTable.setStatus(_A)
_CObmiM500PhyEntry_Object=MibTableRow
cObmiM500PhyEntry=_CObmiM500PhyEntry_Object((1,3,6,1,4,1,9,9,698,1,5,1))
cObmiM500PhyEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cObmiM500PhyEntry.setStatus(_A)
_CObmiM500BusALOS_Type=TruthValue
_CObmiM500BusALOS_Object=MibTableColumn
cObmiM500BusALOS=_CObmiM500BusALOS_Object((1,3,6,1,4,1,9,9,698,1,5,1,1),_CObmiM500BusALOS_Type())
cObmiM500BusALOS.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500BusALOS.setStatus(_A)
_CObmiM500BusBLOS_Type=TruthValue
_CObmiM500BusBLOS_Object=MibTableColumn
cObmiM500BusBLOS=_CObmiM500BusBLOS_Object((1,3,6,1,4,1,9,9,698,1,5,1,2),_CObmiM500BusBLOS_Type())
cObmiM500BusBLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500BusBLOS.setStatus(_A)
class _CObmiM500LastActiveBus_Type(Bits):namedValues=NamedValues(*(('a',0),('b',1)))
_CObmiM500LastActiveBus_Type.__name__='Bits'
_CObmiM500LastActiveBus_Object=MibTableColumn
cObmiM500LastActiveBus=_CObmiM500LastActiveBus_Object((1,3,6,1,4,1,9,9,698,1,5,1,3),_CObmiM500LastActiveBus_Type())
cObmiM500LastActiveBus.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500LastActiveBus.setStatus(_A)
_CObmiM500CommandsRcvd_Type=Counter32
_CObmiM500CommandsRcvd_Object=MibTableColumn
cObmiM500CommandsRcvd=_CObmiM500CommandsRcvd_Object((1,3,6,1,4,1,9,9,698,1,5,1,4),_CObmiM500CommandsRcvd_Type())
cObmiM500CommandsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500CommandsRcvd.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500CommandsRcvd.setUnits(_G)
_CObmiM500TelemetrySent_Type=Counter32
_CObmiM500TelemetrySent_Object=MibTableColumn
cObmiM500TelemetrySent=_CObmiM500TelemetrySent_Object((1,3,6,1,4,1,9,9,698,1,5,1,5),_CObmiM500TelemetrySent_Type())
cObmiM500TelemetrySent.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TelemetrySent.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TelemetrySent.setUnits(_G)
_CObmiM500TelemetryErrs_Type=Counter32
_CObmiM500TelemetryErrs_Object=MibTableColumn
cObmiM500TelemetryErrs=_CObmiM500TelemetryErrs_Object((1,3,6,1,4,1,9,9,698,1,5,1,6),_CObmiM500TelemetryErrs_Type())
cObmiM500TelemetryErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TelemetryErrs.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500TelemetryErrs.setUnits(_G)
_CObmiM500CommandErrs_Type=Counter32
_CObmiM500CommandErrs_Object=MibTableColumn
cObmiM500CommandErrs=_CObmiM500CommandErrs_Object((1,3,6,1,4,1,9,9,698,1,5,1,7),_CObmiM500CommandErrs_Type())
cObmiM500CommandErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500CommandErrs.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500CommandErrs.setUnits(_G)
_CObmiM500CommandOverWrts_Type=Counter32
_CObmiM500CommandOverWrts_Object=MibTableColumn
cObmiM500CommandOverWrts=_CObmiM500CommandOverWrts_Object((1,3,6,1,4,1,9,9,698,1,5,1,8),_CObmiM500CommandOverWrts_Type())
cObmiM500CommandOverWrts.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500CommandOverWrts.setStatus(_A)
if mibBuilder.loadTexts:cObmiM500CommandOverWrts.setUnits(_G)
_CObmiM500HWParityErr_Type=TruthValue
_CObmiM500HWParityErr_Object=MibTableColumn
cObmiM500HWParityErr=_CObmiM500HWParityErr_Object((1,3,6,1,4,1,9,9,698,1,5,1,9),_CObmiM500HWParityErr_Type())
cObmiM500HWParityErr.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500HWParityErr.setStatus(_A)
_CObmiM500TelemetryReqParityErr_Type=TruthValue
_CObmiM500TelemetryReqParityErr_Object=MibTableColumn
cObmiM500TelemetryReqParityErr=_CObmiM500TelemetryReqParityErr_Object((1,3,6,1,4,1,9,9,698,1,5,1,10),_CObmiM500TelemetryReqParityErr_Type())
cObmiM500TelemetryReqParityErr.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500TelemetryReqParityErr.setStatus(_A)
_CObmiM500CommandParityErr_Type=TruthValue
_CObmiM500CommandParityErr_Object=MibTableColumn
cObmiM500CommandParityErr=_CObmiM500CommandParityErr_Object((1,3,6,1,4,1,9,9,698,1,5,1,11),_CObmiM500CommandParityErr_Type())
cObmiM500CommandParityErr.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500CommandParityErr.setStatus(_A)
_CObmiM500CommandTimeout_Type=TruthValue
_CObmiM500CommandTimeout_Object=MibTableColumn
cObmiM500CommandTimeout=_CObmiM500CommandTimeout_Object((1,3,6,1,4,1,9,9,698,1,5,1,12),_CObmiM500CommandTimeout_Type())
cObmiM500CommandTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500CommandTimeout.setStatus(_A)
_CObmiM500CommandOverWrt_Type=TruthValue
_CObmiM500CommandOverWrt_Object=MibTableColumn
cObmiM500CommandOverWrt=_CObmiM500CommandOverWrt_Object((1,3,6,1,4,1,9,9,698,1,5,1,13),_CObmiM500CommandOverWrt_Type())
cObmiM500CommandOverWrt.setMaxAccess(_C)
if mibBuilder.loadTexts:cObmiM500CommandOverWrt.setStatus(_A)
_CiscoObmiMIBConform_ObjectIdentity=ObjectIdentity
ciscoObmiMIBConform=_CiscoObmiMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,698,2))
_CiscoObmiMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoObmiMIBCompliances=_CiscoObmiMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,698,2,1))
_CiscoObmiMIBGroups_ObjectIdentity=ObjectIdentity
ciscoObmiMIBGroups=_CiscoObmiMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,698,2,2))
ciscoObmiMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,698,2,2,1))
ciscoObmiMIBMainObjectGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ciscoObmiMIBMainObjectGroup.setStatus(_A)
ciscoObmiMIBM500ObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,698,2,2,2))
ciscoObmiMIBM500ObjectGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ciscoObmiMIBM500ObjectGroup.setStatus(_A)
ciscoObmiMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,698,2,1,1))
ciscoObmiMIBCompliance.setObjects(*((_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ciscoObmiMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoObmiMIB':ciscoObmiMIB,'ciscoObmiMIBNotifs':ciscoObmiMIBNotifs,'ciscoObmiMIBObjects':ciscoObmiMIBObjects,'cObmiTransportTable':cObmiTransportTable,'cObmiTransportEntry':cObmiTransportEntry,_F:cObmiBusID,_K:cObmiBusName,_L:cObmiCommandRx,_M:cObmiCommandProcessedTotal,_N:cObmiCommandGets,_O:cObmiCommandSets,_P:cObmiCommandProcessedInvalid,_Q:cObmiCommandPending,_R:cObmiCommandDropped,_S:cObmiTelemetrySent,_T:cObmiTelemetryDemandSent,_U:cObmiTelemetryPending,'cObmiTransportHeartBeatTable':cObmiTransportHeartBeatTable,'cObmiTransportHeartBeatEntry':cObmiTransportHeartBeatEntry,_J:cObmiHeartBeatPort,_V:cObmiHeartBeatSent,_W:cObmiHeartBeatPending,'cObmiM500FramingTable':cObmiM500FramingTable,'cObmiM500FramingEntry':cObmiM500FramingEntry,_X:cObmiM500RxFrames,_Y:cObmiM500RxBytes,_Z:cObmiM500RxAbortFrames,_a:cObmiM500RxEchoFrames,_b:cObmiM500RxResetFrames,_c:cObmiM500RxTransportErrFrames,_d:cObmiM500RxUnknownOpFrames,_e:cObmiM500TxFrames,_f:cObmiM500TxBytes,_g:cObmiM500TxAbortFrames,_h:cObmiM500TxEchoFrames,_i:cObmiM500TxTransportErrFrames,_j:cObmiM500RxQOverRun,_k:cObmiM500TxQ0UnderRun,_l:cObmiM500TxQ1UnderRun,_m:cObmiM500TxCtlQOverRun,'cObmiM500PhyTable':cObmiM500PhyTable,'cObmiM500PhyEntry':cObmiM500PhyEntry,_n:cObmiM500BusALOS,_o:cObmiM500BusBLOS,_p:cObmiM500LastActiveBus,_q:cObmiM500CommandsRcvd,_r:cObmiM500TelemetrySent,_s:cObmiM500TelemetryErrs,_t:cObmiM500CommandErrs,_v:cObmiM500CommandOverWrts,_u:cObmiM500HWParityErr,_w:cObmiM500TelemetryReqParityErr,_x:cObmiM500CommandParityErr,_y:cObmiM500CommandTimeout,_z:cObmiM500CommandOverWrt,'ciscoObmiMIBConform':ciscoObmiMIBConform,'ciscoObmiMIBCompliances':ciscoObmiMIBCompliances,'ciscoObmiMIBCompliance':ciscoObmiMIBCompliance,'ciscoObmiMIBGroups':ciscoObmiMIBGroups,_A0:ciscoObmiMIBMainObjectGroup,_A1:ciscoObmiMIBM500ObjectGroup})