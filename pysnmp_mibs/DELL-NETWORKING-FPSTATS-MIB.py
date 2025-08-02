_a='dellNetFpXPENumber'
_Z='dellNetFpEgrQComType'
_Y='dellNetIfPrioIndex'
_X='dellNetFpStackPortIndex'
_W='Indications'
_V='Requests'
_U='dynamic'
_T='static'
_S='dellNetFpCOSIndex'
_R='dellNetFpIfPerPGIndex'
_Q='dellNetFpIfPerCOSNumber'
_P='dellNetFpPerPortPGIndex'
_O='OctetString'
_N='dellNetFpPerPortCOSNumber'
_M='dellNetFpPortPipe'
_L='dellNetPrioIndex'
_K='dellNetProcessorDeviceType'
_J='dellNetProcessorDeviceIndex'
_I='Integer32'
_H='deprecated'
_G='ifIndex'
_F='IF-MIB'
_E='DELL-NETWORKING-FPSTATS-MIB'
_D='not-accessible'
_C='obsolete'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
DellNetDeviceType,=mibBuilder.importSymbols('DELL-NETWORKING-TC','DellNetDeviceType')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dellNetFpStatsMib=ModuleIdentity((1,3,6,1,4,1,6027,3,27))
if mibBuilder.loadTexts:dellNetFpStatsMib.setRevisions(('2014-09-04 12:00',))
class ComType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
class QState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('drop',2)))
_DellNetFpStatsObjects_ObjectIdentity=ObjectIdentity
dellNetFpStatsObjects=_DellNetFpStatsObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,27,1))
_DellNetFpCpuDataPlaneTable_Object=MibTable
dellNetFpCpuDataPlaneTable=_DellNetFpCpuDataPlaneTable_Object((1,3,6,1,4,1,6027,3,27,1,1))
if mibBuilder.loadTexts:dellNetFpCpuDataPlaneTable.setStatus(_A)
_DellNetFpCpuDataPlaneStatsEntry_Object=MibTableRow
dellNetFpCpuDataPlaneStatsEntry=_DellNetFpCpuDataPlaneStatsEntry_Object((1,3,6,1,4,1,6027,3,27,1,1,1))
dellNetFpCpuDataPlaneStatsEntry.setIndexNames((0,_E,_K),(0,_E,_J))
if mibBuilder.loadTexts:dellNetFpCpuDataPlaneStatsEntry.setStatus(_A)
_DellNetProcessorDeviceType_Type=DellNetDeviceType
_DellNetProcessorDeviceType_Object=MibTableColumn
dellNetProcessorDeviceType=_DellNetProcessorDeviceType_Object((1,3,6,1,4,1,6027,3,27,1,1,1,1),_DellNetProcessorDeviceType_Type())
dellNetProcessorDeviceType.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetProcessorDeviceType.setStatus(_A)
_DellNetProcessorDeviceIndex_Type=Integer32
_DellNetProcessorDeviceIndex_Object=MibTableColumn
dellNetProcessorDeviceIndex=_DellNetProcessorDeviceIndex_Object((1,3,6,1,4,1,6027,3,27,1,1,1,2),_DellNetProcessorDeviceIndex_Type())
dellNetProcessorDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetProcessorDeviceIndex.setStatus(_A)
_DellNetFpRxHandle_Type=Integer32
_DellNetFpRxHandle_Object=MibTableColumn
dellNetFpRxHandle=_DellNetFpRxHandle_Object((1,3,6,1,4,1,6027,3,27,1,1,1,3),_DellNetFpRxHandle_Type())
dellNetFpRxHandle.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxHandle.setStatus(_A)
_DellNetFpNoMhdr_Type=Integer32
_DellNetFpNoMhdr_Object=MibTableColumn
dellNetFpNoMhdr=_DellNetFpNoMhdr_Object((1,3,6,1,4,1,6027,3,27,1,1,1,4),_DellNetFpNoMhdr_Type())
dellNetFpNoMhdr.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpNoMhdr.setStatus(_A)
_DellNetFpNoMBuf_Type=Integer32
_DellNetFpNoMBuf_Object=MibTableColumn
dellNetFpNoMBuf=_DellNetFpNoMBuf_Object((1,3,6,1,4,1,6027,3,27,1,1,1,5),_DellNetFpNoMBuf_Type())
dellNetFpNoMBuf.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpNoMBuf.setStatus(_A)
_DellNetFpNoClus_Type=Integer32
_DellNetFpNoClus_Object=MibTableColumn
dellNetFpNoClus=_DellNetFpNoClus_Object((1,3,6,1,4,1,6027,3,27,1,1,1,6),_DellNetFpNoClus_Type())
dellNetFpNoClus.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpNoClus.setStatus(_A)
_DellNetFpRecvd_Type=Integer32
_DellNetFpRecvd_Object=MibTableColumn
dellNetFpRecvd=_DellNetFpRecvd_Object((1,3,6,1,4,1,6027,3,27,1,1,1,7),_DellNetFpRecvd_Type())
dellNetFpRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRecvd.setStatus(_A)
_DellNetFpDropped_Type=Integer32
_DellNetFpDropped_Object=MibTableColumn
dellNetFpDropped=_DellNetFpDropped_Object((1,3,6,1,4,1,6027,3,27,1,1,1,8),_DellNetFpDropped_Type())
dellNetFpDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpDropped.setStatus(_A)
_DellNetFpRecvToNet_Type=Integer32
_DellNetFpRecvToNet_Object=MibTableColumn
dellNetFpRecvToNet=_DellNetFpRecvToNet_Object((1,3,6,1,4,1,6027,3,27,1,1,1,9),_DellNetFpRecvToNet_Type())
dellNetFpRecvToNet.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRecvToNet.setStatus(_A)
_DellNetFpRxError_Type=Integer32
_DellNetFpRxError_Object=MibTableColumn
dellNetFpRxError=_DellNetFpRxError_Object((1,3,6,1,4,1,6027,3,27,1,1,1,10),_DellNetFpRxError_Type())
dellNetFpRxError.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxError.setStatus(_A)
_DellNetFpRxDatapathError_Type=Integer32
_DellNetFpRxDatapathError_Object=MibTableColumn
dellNetFpRxDatapathError=_DellNetFpRxDatapathError_Object((1,3,6,1,4,1,6027,3,27,1,1,1,11),_DellNetFpRxDatapathError_Type())
dellNetFpRxDatapathError.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxDatapathError.setStatus(_A)
_DellNetFpRxPktCOS0_Type=Integer32
_DellNetFpRxPktCOS0_Object=MibTableColumn
dellNetFpRxPktCOS0=_DellNetFpRxPktCOS0_Object((1,3,6,1,4,1,6027,3,27,1,1,1,12),_DellNetFpRxPktCOS0_Type())
dellNetFpRxPktCOS0.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktCOS0.setStatus(_H)
_DellNetFpRxPktCOS1_Type=Integer32
_DellNetFpRxPktCOS1_Object=MibTableColumn
dellNetFpRxPktCOS1=_DellNetFpRxPktCOS1_Object((1,3,6,1,4,1,6027,3,27,1,1,1,13),_DellNetFpRxPktCOS1_Type())
dellNetFpRxPktCOS1.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktCOS1.setStatus(_H)
_DellNetFpRxPktCOS2_Type=Integer32
_DellNetFpRxPktCOS2_Object=MibTableColumn
dellNetFpRxPktCOS2=_DellNetFpRxPktCOS2_Object((1,3,6,1,4,1,6027,3,27,1,1,1,14),_DellNetFpRxPktCOS2_Type())
dellNetFpRxPktCOS2.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktCOS2.setStatus(_H)
_DellNetFpRxPktCOS3_Type=Integer32
_DellNetFpRxPktCOS3_Object=MibTableColumn
dellNetFpRxPktCOS3=_DellNetFpRxPktCOS3_Object((1,3,6,1,4,1,6027,3,27,1,1,1,15),_DellNetFpRxPktCOS3_Type())
dellNetFpRxPktCOS3.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktCOS3.setStatus(_H)
_DellNetFpRxPktCOS4_Type=Integer32
_DellNetFpRxPktCOS4_Object=MibTableColumn
dellNetFpRxPktCOS4=_DellNetFpRxPktCOS4_Object((1,3,6,1,4,1,6027,3,27,1,1,1,16),_DellNetFpRxPktCOS4_Type())
dellNetFpRxPktCOS4.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktCOS4.setStatus(_H)
_DellNetFpRxPktCOS5_Type=Integer32
_DellNetFpRxPktCOS5_Object=MibTableColumn
dellNetFpRxPktCOS5=_DellNetFpRxPktCOS5_Object((1,3,6,1,4,1,6027,3,27,1,1,1,17),_DellNetFpRxPktCOS5_Type())
dellNetFpRxPktCOS5.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktCOS5.setStatus(_H)
_DellNetFpRxPktCOS6_Type=Integer32
_DellNetFpRxPktCOS6_Object=MibTableColumn
dellNetFpRxPktCOS6=_DellNetFpRxPktCOS6_Object((1,3,6,1,4,1,6027,3,27,1,1,1,18),_DellNetFpRxPktCOS6_Type())
dellNetFpRxPktCOS6.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktCOS6.setStatus(_H)
_DellNetFpRxPktCOS7_Type=Integer32
_DellNetFpRxPktCOS7_Object=MibTableColumn
dellNetFpRxPktCOS7=_DellNetFpRxPktCOS7_Object((1,3,6,1,4,1,6027,3,27,1,1,1,19),_DellNetFpRxPktCOS7_Type())
dellNetFpRxPktCOS7.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktCOS7.setStatus(_H)
_DellNetFpRxPktUnit0_Type=Integer32
_DellNetFpRxPktUnit0_Object=MibTableColumn
dellNetFpRxPktUnit0=_DellNetFpRxPktUnit0_Object((1,3,6,1,4,1,6027,3,27,1,1,1,20),_DellNetFpRxPktUnit0_Type())
dellNetFpRxPktUnit0.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktUnit0.setStatus(_A)
_DellNetFpRxPktUnit1_Type=Integer32
_DellNetFpRxPktUnit1_Object=MibTableColumn
dellNetFpRxPktUnit1=_DellNetFpRxPktUnit1_Object((1,3,6,1,4,1,6027,3,27,1,1,1,21),_DellNetFpRxPktUnit1_Type())
dellNetFpRxPktUnit1.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktUnit1.setStatus(_A)
_DellNetFpRxPktUnit2_Type=Integer32
_DellNetFpRxPktUnit2_Object=MibTableColumn
dellNetFpRxPktUnit2=_DellNetFpRxPktUnit2_Object((1,3,6,1,4,1,6027,3,27,1,1,1,22),_DellNetFpRxPktUnit2_Type())
dellNetFpRxPktUnit2.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktUnit2.setStatus(_A)
_DellNetFpRxPktUnit3_Type=Integer32
_DellNetFpRxPktUnit3_Object=MibTableColumn
dellNetFpRxPktUnit3=_DellNetFpRxPktUnit3_Object((1,3,6,1,4,1,6027,3,27,1,1,1,23),_DellNetFpRxPktUnit3_Type())
dellNetFpRxPktUnit3.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktUnit3.setStatus(_A)
_DellNetFpTransmitted_Type=Integer32
_DellNetFpTransmitted_Object=MibTableColumn
dellNetFpTransmitted=_DellNetFpTransmitted_Object((1,3,6,1,4,1,6027,3,27,1,1,1,24),_DellNetFpTransmitted_Type())
dellNetFpTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTransmitted.setStatus(_A)
_DellNetFpTxRequested_Type=Integer32
_DellNetFpTxRequested_Object=MibTableColumn
dellNetFpTxRequested=_DellNetFpTxRequested_Object((1,3,6,1,4,1,6027,3,27,1,1,1,25),_DellNetFpTxRequested_Type())
dellNetFpTxRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxRequested.setStatus(_A)
_DellNetFpNoTxDesc_Type=Integer32
_DellNetFpNoTxDesc_Object=MibTableColumn
dellNetFpNoTxDesc=_DellNetFpNoTxDesc_Object((1,3,6,1,4,1,6027,3,27,1,1,1,26),_DellNetFpNoTxDesc_Type())
dellNetFpNoTxDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpNoTxDesc.setStatus(_A)
_DellNetFpTxError_Type=Integer32
_DellNetFpTxError_Object=MibTableColumn
dellNetFpTxError=_DellNetFpTxError_Object((1,3,6,1,4,1,6027,3,27,1,1,1,27),_DellNetFpTxError_Type())
dellNetFpTxError.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxError.setStatus(_A)
_DellNetFpTxReqTooLarge_Type=Integer32
_DellNetFpTxReqTooLarge_Object=MibTableColumn
dellNetFpTxReqTooLarge=_DellNetFpTxReqTooLarge_Object((1,3,6,1,4,1,6027,3,27,1,1,1,28),_DellNetFpTxReqTooLarge_Type())
dellNetFpTxReqTooLarge.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxReqTooLarge.setStatus(_A)
_DellNetFpTxInternalError_Type=Integer32
_DellNetFpTxInternalError_Object=MibTableColumn
dellNetFpTxInternalError=_DellNetFpTxInternalError_Object((1,3,6,1,4,1,6027,3,27,1,1,1,29),_DellNetFpTxInternalError_Type())
dellNetFpTxInternalError.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxInternalError.setStatus(_A)
_DellNetFpTxDatapathErr_Type=Integer32
_DellNetFpTxDatapathErr_Object=MibTableColumn
dellNetFpTxDatapathErr=_DellNetFpTxDatapathErr_Object((1,3,6,1,4,1,6027,3,27,1,1,1,30),_DellNetFpTxDatapathErr_Type())
dellNetFpTxDatapathErr.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxDatapathErr.setStatus(_A)
_DellNetFpTxPktCOS0_Type=Integer32
_DellNetFpTxPktCOS0_Object=MibTableColumn
dellNetFpTxPktCOS0=_DellNetFpTxPktCOS0_Object((1,3,6,1,4,1,6027,3,27,1,1,1,31),_DellNetFpTxPktCOS0_Type())
dellNetFpTxPktCOS0.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktCOS0.setStatus(_H)
_DellNetFpTxPktCOS1_Type=Integer32
_DellNetFpTxPktCOS1_Object=MibTableColumn
dellNetFpTxPktCOS1=_DellNetFpTxPktCOS1_Object((1,3,6,1,4,1,6027,3,27,1,1,1,32),_DellNetFpTxPktCOS1_Type())
dellNetFpTxPktCOS1.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktCOS1.setStatus(_H)
_DellNetFpTxPktCOS2_Type=Integer32
_DellNetFpTxPktCOS2_Object=MibTableColumn
dellNetFpTxPktCOS2=_DellNetFpTxPktCOS2_Object((1,3,6,1,4,1,6027,3,27,1,1,1,33),_DellNetFpTxPktCOS2_Type())
dellNetFpTxPktCOS2.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktCOS2.setStatus(_H)
_DellNetFpTxPktCOS3_Type=Integer32
_DellNetFpTxPktCOS3_Object=MibTableColumn
dellNetFpTxPktCOS3=_DellNetFpTxPktCOS3_Object((1,3,6,1,4,1,6027,3,27,1,1,1,34),_DellNetFpTxPktCOS3_Type())
dellNetFpTxPktCOS3.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktCOS3.setStatus(_H)
_DellNetFpTxPktCOS4_Type=Integer32
_DellNetFpTxPktCOS4_Object=MibTableColumn
dellNetFpTxPktCOS4=_DellNetFpTxPktCOS4_Object((1,3,6,1,4,1,6027,3,27,1,1,1,35),_DellNetFpTxPktCOS4_Type())
dellNetFpTxPktCOS4.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktCOS4.setStatus(_H)
_DellNetFpTxPktCOS5_Type=Integer32
_DellNetFpTxPktCOS5_Object=MibTableColumn
dellNetFpTxPktCOS5=_DellNetFpTxPktCOS5_Object((1,3,6,1,4,1,6027,3,27,1,1,1,36),_DellNetFpTxPktCOS5_Type())
dellNetFpTxPktCOS5.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktCOS5.setStatus(_H)
_DellNetFpTxPktCOS6_Type=Integer32
_DellNetFpTxPktCOS6_Object=MibTableColumn
dellNetFpTxPktCOS6=_DellNetFpTxPktCOS6_Object((1,3,6,1,4,1,6027,3,27,1,1,1,37),_DellNetFpTxPktCOS6_Type())
dellNetFpTxPktCOS6.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktCOS6.setStatus(_H)
_DellNetFpTxPktCOS7_Type=Integer32
_DellNetFpTxPktCOS7_Object=MibTableColumn
dellNetFpTxPktCOS7=_DellNetFpTxPktCOS7_Object((1,3,6,1,4,1,6027,3,27,1,1,1,38),_DellNetFpTxPktCOS7_Type())
dellNetFpTxPktCOS7.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktCOS7.setStatus(_H)
_DellNetFpTxPktUnit0_Type=Integer32
_DellNetFpTxPktUnit0_Object=MibTableColumn
dellNetFpTxPktUnit0=_DellNetFpTxPktUnit0_Object((1,3,6,1,4,1,6027,3,27,1,1,1,39),_DellNetFpTxPktUnit0_Type())
dellNetFpTxPktUnit0.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktUnit0.setStatus(_A)
_DellNetFpTxPktUnit1_Type=Integer32
_DellNetFpTxPktUnit1_Object=MibTableColumn
dellNetFpTxPktUnit1=_DellNetFpTxPktUnit1_Object((1,3,6,1,4,1,6027,3,27,1,1,1,40),_DellNetFpTxPktUnit1_Type())
dellNetFpTxPktUnit1.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktUnit1.setStatus(_A)
_DellNetFpTxPktUnit2_Type=Integer32
_DellNetFpTxPktUnit2_Object=MibTableColumn
dellNetFpTxPktUnit2=_DellNetFpTxPktUnit2_Object((1,3,6,1,4,1,6027,3,27,1,1,1,41),_DellNetFpTxPktUnit2_Type())
dellNetFpTxPktUnit2.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktUnit2.setStatus(_A)
_DellNetFpTxPktUnit3_Type=Integer32
_DellNetFpTxPktUnit3_Object=MibTableColumn
dellNetFpTxPktUnit3=_DellNetFpTxPktUnit3_Object((1,3,6,1,4,1,6027,3,27,1,1,1,42),_DellNetFpTxPktUnit3_Type())
dellNetFpTxPktUnit3.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktUnit3.setStatus(_A)
_DellNetFpCpuPartyBusTable_Object=MibTable
dellNetFpCpuPartyBusTable=_DellNetFpCpuPartyBusTable_Object((1,3,6,1,4,1,6027,3,27,1,2))
if mibBuilder.loadTexts:dellNetFpCpuPartyBusTable.setStatus(_A)
_DellNetFpCpuPartyBusStatsEntry_Object=MibTableRow
dellNetFpCpuPartyBusStatsEntry=_DellNetFpCpuPartyBusStatsEntry_Object((1,3,6,1,4,1,6027,3,27,1,2,1))
dellNetFpCpuPartyBusStatsEntry.setIndexNames((0,_E,_K),(0,_E,_J))
if mibBuilder.loadTexts:dellNetFpCpuPartyBusStatsEntry.setStatus(_A)
_DellNetFpPartyBusInputPackets_Type=Counter32
_DellNetFpPartyBusInputPackets_Object=MibTableColumn
dellNetFpPartyBusInputPackets=_DellNetFpPartyBusInputPackets_Object((1,3,6,1,4,1,6027,3,27,1,2,1,1),_DellNetFpPartyBusInputPackets_Type())
dellNetFpPartyBusInputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPartyBusInputPackets.setStatus(_A)
_DellNetFpPartyBusInputBytes_Type=Counter32
_DellNetFpPartyBusInputBytes_Object=MibTableColumn
dellNetFpPartyBusInputBytes=_DellNetFpPartyBusInputBytes_Object((1,3,6,1,4,1,6027,3,27,1,2,1,2),_DellNetFpPartyBusInputBytes_Type())
dellNetFpPartyBusInputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPartyBusInputBytes.setStatus(_A)
_DellNetFpPartyBusInputDropped_Type=Counter32
_DellNetFpPartyBusInputDropped_Object=MibTableColumn
dellNetFpPartyBusInputDropped=_DellNetFpPartyBusInputDropped_Object((1,3,6,1,4,1,6027,3,27,1,2,1,3),_DellNetFpPartyBusInputDropped_Type())
dellNetFpPartyBusInputDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPartyBusInputDropped.setStatus(_A)
_DellNetFpPartyBusInputError_Type=Counter32
_DellNetFpPartyBusInputError_Object=MibTableColumn
dellNetFpPartyBusInputError=_DellNetFpPartyBusInputError_Object((1,3,6,1,4,1,6027,3,27,1,2,1,4),_DellNetFpPartyBusInputError_Type())
dellNetFpPartyBusInputError.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPartyBusInputError.setStatus(_A)
_DellNetFpPartyBusOutputPackets_Type=Counter32
_DellNetFpPartyBusOutputPackets_Object=MibTableColumn
dellNetFpPartyBusOutputPackets=_DellNetFpPartyBusOutputPackets_Object((1,3,6,1,4,1,6027,3,27,1,2,1,5),_DellNetFpPartyBusOutputPackets_Type())
dellNetFpPartyBusOutputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPartyBusOutputPackets.setStatus(_A)
_DellNetFpPartyBusOutputBytes_Type=Counter32
_DellNetFpPartyBusOutputBytes_Object=MibTableColumn
dellNetFpPartyBusOutputBytes=_DellNetFpPartyBusOutputBytes_Object((1,3,6,1,4,1,6027,3,27,1,2,1,6),_DellNetFpPartyBusOutputBytes_Type())
dellNetFpPartyBusOutputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPartyBusOutputBytes.setStatus(_A)
_DellNetFpPartyBusOutputError_Type=Counter32
_DellNetFpPartyBusOutputError_Object=MibTableColumn
dellNetFpPartyBusOutputError=_DellNetFpPartyBusOutputError_Object((1,3,6,1,4,1,6027,3,27,1,2,1,7),_DellNetFpPartyBusOutputError_Type())
dellNetFpPartyBusOutputError.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPartyBusOutputError.setStatus(_A)
_DellNetFpDropsTable_Object=MibTable
dellNetFpDropsTable=_DellNetFpDropsTable_Object((1,3,6,1,4,1,6027,3,27,1,3))
if mibBuilder.loadTexts:dellNetFpDropsTable.setStatus(_A)
_DellNetFpDropsEntry_Object=MibTableRow
dellNetFpDropsEntry=_DellNetFpDropsEntry_Object((1,3,6,1,4,1,6027,3,27,1,3,1))
dellNetFpDropsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dellNetFpDropsEntry.setStatus(_A)
_DellNetFpIngressDrops_Type=Counter64
_DellNetFpIngressDrops_Object=MibTableColumn
dellNetFpIngressDrops=_DellNetFpIngressDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,1),_DellNetFpIngressDrops_Type())
dellNetFpIngressDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngressDrops.setStatus(_A)
_DellNetFpIngIBPCBPFullDrops_Type=Counter64
_DellNetFpIngIBPCBPFullDrops_Object=MibTableColumn
dellNetFpIngIBPCBPFullDrops=_DellNetFpIngIBPCBPFullDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,2),_DellNetFpIngIBPCBPFullDrops_Type())
dellNetFpIngIBPCBPFullDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngIBPCBPFullDrops.setStatus(_A)
_DellNetFpIngPortSTPnotFwdDrops_Type=Counter64
_DellNetFpIngPortSTPnotFwdDrops_Object=MibTableColumn
dellNetFpIngPortSTPnotFwdDrops=_DellNetFpIngPortSTPnotFwdDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,3),_DellNetFpIngPortSTPnotFwdDrops_Type())
dellNetFpIngPortSTPnotFwdDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngPortSTPnotFwdDrops.setStatus(_A)
_DellNetFpIngIPv4L3Discards_Type=Counter64
_DellNetFpIngIPv4L3Discards_Object=MibTableColumn
dellNetFpIngIPv4L3Discards=_DellNetFpIngIPv4L3Discards_Object((1,3,6,1,4,1,6027,3,27,1,3,1,4),_DellNetFpIngIPv4L3Discards_Type())
dellNetFpIngIPv4L3Discards.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngIPv4L3Discards.setStatus(_A)
_DellNetFpIngPolicyDiscards_Type=Counter64
_DellNetFpIngPolicyDiscards_Object=MibTableColumn
dellNetFpIngPolicyDiscards=_DellNetFpIngPolicyDiscards_Object((1,3,6,1,4,1,6027,3,27,1,3,1,5),_DellNetFpIngPolicyDiscards_Type())
dellNetFpIngPolicyDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngPolicyDiscards.setStatus(_A)
_DellNetFpIngPacketsDroppedByDELLNETFP_Type=Counter64
_DellNetFpIngPacketsDroppedByDELLNETFP_Object=MibTableColumn
dellNetFpIngPacketsDroppedByDELLNETFP=_DellNetFpIngPacketsDroppedByDELLNETFP_Object((1,3,6,1,4,1,6027,3,27,1,3,1,6),_DellNetFpIngPacketsDroppedByDELLNETFP_Type())
dellNetFpIngPacketsDroppedByDELLNETFP.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngPacketsDroppedByDELLNETFP.setStatus(_A)
_DellNetFpIngL2L3Drops_Type=Counter64
_DellNetFpIngL2L3Drops_Object=MibTableColumn
dellNetFpIngL2L3Drops=_DellNetFpIngL2L3Drops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,7),_DellNetFpIngL2L3Drops_Type())
dellNetFpIngL2L3Drops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngL2L3Drops.setStatus(_A)
_DellNetFpIngPortBitMapZeroDrops_Type=Counter64
_DellNetFpIngPortBitMapZeroDrops_Object=MibTableColumn
dellNetFpIngPortBitMapZeroDrops=_DellNetFpIngPortBitMapZeroDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,8),_DellNetFpIngPortBitMapZeroDrops_Type())
dellNetFpIngPortBitMapZeroDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngPortBitMapZeroDrops.setStatus(_A)
_DellNetFpIngRxVLANDrops_Type=Counter64
_DellNetFpIngRxVLANDrops_Object=MibTableColumn
dellNetFpIngRxVLANDrops=_DellNetFpIngRxVLANDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,9),_DellNetFpIngRxVLANDrops_Type())
dellNetFpIngRxVLANDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngRxVLANDrops.setStatus(_A)
_DellNetFpIngressFCSDrops_Type=Counter64
_DellNetFpIngressFCSDrops_Object=MibTableColumn
dellNetFpIngressFCSDrops=_DellNetFpIngressFCSDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,10),_DellNetFpIngressFCSDrops_Type())
dellNetFpIngressFCSDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngressFCSDrops.setStatus(_A)
_DellNetFpIngressMTUExceeds_Type=Counter64
_DellNetFpIngressMTUExceeds_Object=MibTableColumn
dellNetFpIngressMTUExceeds=_DellNetFpIngressMTUExceeds_Object((1,3,6,1,4,1,6027,3,27,1,3,1,11),_DellNetFpIngressMTUExceeds_Type())
dellNetFpIngressMTUExceeds.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngressMTUExceeds.setStatus(_A)
_DellNetFpMMUHOLDrops_Type=Counter64
_DellNetFpMMUHOLDrops_Object=MibTableColumn
dellNetFpMMUHOLDrops=_DellNetFpMMUHOLDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,12),_DellNetFpMMUHOLDrops_Type())
dellNetFpMMUHOLDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpMMUHOLDrops.setStatus(_A)
_DellNetFpMMUTxPurgeCellErr_Type=Counter64
_DellNetFpMMUTxPurgeCellErr_Object=MibTableColumn
dellNetFpMMUTxPurgeCellErr=_DellNetFpMMUTxPurgeCellErr_Object((1,3,6,1,4,1,6027,3,27,1,3,1,13),_DellNetFpMMUTxPurgeCellErr_Type())
dellNetFpMMUTxPurgeCellErr.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpMMUTxPurgeCellErr.setStatus(_A)
_DellNetFpMMUAgedDrops_Type=Counter64
_DellNetFpMMUAgedDrops_Object=MibTableColumn
dellNetFpMMUAgedDrops=_DellNetFpMMUAgedDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,14),_DellNetFpMMUAgedDrops_Type())
dellNetFpMMUAgedDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpMMUAgedDrops.setStatus(_A)
_DellNetFpEgressFCSDrops_Type=Counter64
_DellNetFpEgressFCSDrops_Object=MibTableColumn
dellNetFpEgressFCSDrops=_DellNetFpEgressFCSDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,15),_DellNetFpEgressFCSDrops_Type())
dellNetFpEgressFCSDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgressFCSDrops.setStatus(_A)
_DellNetFpEgIPv4L3UCAgedDrops_Type=Counter64
_DellNetFpEgIPv4L3UCAgedDrops_Object=MibTableColumn
dellNetFpEgIPv4L3UCAgedDrops=_DellNetFpEgIPv4L3UCAgedDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,16),_DellNetFpEgIPv4L3UCAgedDrops_Type())
dellNetFpEgIPv4L3UCAgedDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgIPv4L3UCAgedDrops.setStatus(_A)
_DellNetFpEgTTLThresholdDrops_Type=Counter64
_DellNetFpEgTTLThresholdDrops_Object=MibTableColumn
dellNetFpEgTTLThresholdDrops=_DellNetFpEgTTLThresholdDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,17),_DellNetFpEgTTLThresholdDrops_Type())
dellNetFpEgTTLThresholdDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgTTLThresholdDrops.setStatus(_A)
_DellNetFpEgInvalidVLANCounterDrops_Type=Counter64
_DellNetFpEgInvalidVLANCounterDrops_Object=MibTableColumn
dellNetFpEgInvalidVLANCounterDrops=_DellNetFpEgInvalidVLANCounterDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,18),_DellNetFpEgInvalidVLANCounterDrops_Type())
dellNetFpEgInvalidVLANCounterDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgInvalidVLANCounterDrops.setStatus(_A)
_DellNetFpEgL2MCDrops_Type=Counter64
_DellNetFpEgL2MCDrops_Object=MibTableColumn
dellNetFpEgL2MCDrops=_DellNetFpEgL2MCDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,19),_DellNetFpEgL2MCDrops_Type())
dellNetFpEgL2MCDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgL2MCDrops.setStatus(_A)
_DellNetFpEgPktDropsOfAnyCondition_Type=Counter64
_DellNetFpEgPktDropsOfAnyCondition_Object=MibTableColumn
dellNetFpEgPktDropsOfAnyCondition=_DellNetFpEgPktDropsOfAnyCondition_Object((1,3,6,1,4,1,6027,3,27,1,3,1,20),_DellNetFpEgPktDropsOfAnyCondition_Type())
dellNetFpEgPktDropsOfAnyCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgPktDropsOfAnyCondition.setStatus(_A)
_DellNetFpEgHgMacUnderFlow_Type=Counter64
_DellNetFpEgHgMacUnderFlow_Object=MibTableColumn
dellNetFpEgHgMacUnderFlow=_DellNetFpEgHgMacUnderFlow_Object((1,3,6,1,4,1,6027,3,27,1,3,1,21),_DellNetFpEgHgMacUnderFlow_Type())
dellNetFpEgHgMacUnderFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgHgMacUnderFlow.setStatus(_A)
_DellNetFpEgTxErrPktCounter_Type=Counter64
_DellNetFpEgTxErrPktCounter_Object=MibTableColumn
dellNetFpEgTxErrPktCounter=_DellNetFpEgTxErrPktCounter_Object((1,3,6,1,4,1,6027,3,27,1,3,1,22),_DellNetFpEgTxErrPktCounter_Type())
dellNetFpEgTxErrPktCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgTxErrPktCounter.setStatus(_A)
_DellNetFpFlowControlDrops_Type=Counter64
_DellNetFpFlowControlDrops_Object=MibTableColumn
dellNetFpFlowControlDrops=_DellNetFpFlowControlDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,23),_DellNetFpFlowControlDrops_Type())
dellNetFpFlowControlDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpFlowControlDrops.setStatus(_A)
_DellNetFpIngressDropsBytes_Type=Counter64
_DellNetFpIngressDropsBytes_Object=MibTableColumn
dellNetFpIngressDropsBytes=_DellNetFpIngressDropsBytes_Object((1,3,6,1,4,1,6027,3,27,1,3,1,24),_DellNetFpIngressDropsBytes_Type())
dellNetFpIngressDropsBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngressDropsBytes.setStatus(_A)
_DellNetFpIngressFECBitErrors_Type=Counter64
_DellNetFpIngressFECBitErrors_Object=MibTableColumn
dellNetFpIngressFECBitErrors=_DellNetFpIngressFECBitErrors_Object((1,3,6,1,4,1,6027,3,27,1,3,1,25),_DellNetFpIngressFECBitErrors_Type())
dellNetFpIngressFECBitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngressFECBitErrors.setStatus(_A)
_DellNetFpIngressFECUncorrectedCodeWords_Type=Counter64
_DellNetFpIngressFECUncorrectedCodeWords_Object=MibTableColumn
dellNetFpIngressFECUncorrectedCodeWords=_DellNetFpIngressFECUncorrectedCodeWords_Object((1,3,6,1,4,1,6027,3,27,1,3,1,26),_DellNetFpIngressFECUncorrectedCodeWords_Type())
dellNetFpIngressFECUncorrectedCodeWords.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngressFECUncorrectedCodeWords.setStatus(_A)
class _DellNetFpIngressPreFECBitErrorRatio_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_DellNetFpIngressPreFECBitErrorRatio_Type.__name__=_O
_DellNetFpIngressPreFECBitErrorRatio_Object=MibTableColumn
dellNetFpIngressPreFECBitErrorRatio=_DellNetFpIngressPreFECBitErrorRatio_Object((1,3,6,1,4,1,6027,3,27,1,3,1,27),_DellNetFpIngressPreFECBitErrorRatio_Type())
dellNetFpIngressPreFECBitErrorRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngressPreFECBitErrorRatio.setStatus(_A)
class _DellNetFpIngressFCSErrorRatio_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_DellNetFpIngressFCSErrorRatio_Type.__name__=_O
_DellNetFpIngressFCSErrorRatio_Object=MibTableColumn
dellNetFpIngressFCSErrorRatio=_DellNetFpIngressFCSErrorRatio_Object((1,3,6,1,4,1,6027,3,27,1,3,1,28),_DellNetFpIngressFCSErrorRatio_Type())
dellNetFpIngressFCSErrorRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngressFCSErrorRatio.setStatus(_A)
_DellNetFpWredGreenDrops_Type=Counter64
_DellNetFpWredGreenDrops_Object=MibTableColumn
dellNetFpWredGreenDrops=_DellNetFpWredGreenDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,29),_DellNetFpWredGreenDrops_Type())
dellNetFpWredGreenDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpWredGreenDrops.setStatus(_A)
_DellNetFpWredYellowDrops_Type=Counter64
_DellNetFpWredYellowDrops_Object=MibTableColumn
dellNetFpWredYellowDrops=_DellNetFpWredYellowDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,30),_DellNetFpWredYellowDrops_Type())
dellNetFpWredYellowDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpWredYellowDrops.setStatus(_A)
_DellNetFpWredOutOfProfileDrops_Type=Counter64
_DellNetFpWredOutOfProfileDrops_Object=MibTableColumn
dellNetFpWredOutOfProfileDrops=_DellNetFpWredOutOfProfileDrops_Object((1,3,6,1,4,1,6027,3,27,1,3,1,31),_DellNetFpWredOutOfProfileDrops_Type())
dellNetFpWredOutOfProfileDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpWredOutOfProfileDrops.setStatus(_A)
_DellNetFpPacketBufferTable_Object=MibTable
dellNetFpPacketBufferTable=_DellNetFpPacketBufferTable_Object((1,3,6,1,4,1,6027,3,27,1,4))
if mibBuilder.loadTexts:dellNetFpPacketBufferTable.setStatus(_A)
_DellNetFpPacketBufferEntry_Object=MibTableRow
dellNetFpPacketBufferEntry=_DellNetFpPacketBufferEntry_Object((1,3,6,1,4,1,6027,3,27,1,4,1))
dellNetFpPacketBufferEntry.setIndexNames((0,_E,_K),(0,_E,_J),(0,_E,_M))
if mibBuilder.loadTexts:dellNetFpPacketBufferEntry.setStatus(_A)
class _DellNetFpPortPipe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_DellNetFpPortPipe_Type.__name__=_I
_DellNetFpPortPipe_Object=MibTableColumn
dellNetFpPortPipe=_DellNetFpPortPipe_Object((1,3,6,1,4,1,6027,3,27,1,4,1,1),_DellNetFpPortPipe_Type())
dellNetFpPortPipe.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpPortPipe.setStatus(_A)
_DellNetFpTotalPacketBuffer_Type=Counter32
_DellNetFpTotalPacketBuffer_Object=MibTableColumn
dellNetFpTotalPacketBuffer=_DellNetFpTotalPacketBuffer_Object((1,3,6,1,4,1,6027,3,27,1,4,1,2),_DellNetFpTotalPacketBuffer_Type())
dellNetFpTotalPacketBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTotalPacketBuffer.setStatus(_A)
_DellNetFpCurrentAvailBuffer_Type=Counter32
_DellNetFpCurrentAvailBuffer_Object=MibTableColumn
dellNetFpCurrentAvailBuffer=_DellNetFpCurrentAvailBuffer_Object((1,3,6,1,4,1,6027,3,27,1,4,1,3),_DellNetFpCurrentAvailBuffer_Type())
dellNetFpCurrentAvailBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCurrentAvailBuffer.setStatus(_A)
_DellNetFpPacketBufferAlloc_Type=Counter32
_DellNetFpPacketBufferAlloc_Object=MibTableColumn
dellNetFpPacketBufferAlloc=_DellNetFpPacketBufferAlloc_Object((1,3,6,1,4,1,6027,3,27,1,4,1,4),_DellNetFpPacketBufferAlloc_Type())
dellNetFpPacketBufferAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPacketBufferAlloc.setStatus(_A)
_DellNetFpStatsPerPortTable_Object=MibTable
dellNetFpStatsPerPortTable=_DellNetFpStatsPerPortTable_Object((1,3,6,1,4,1,6027,3,27,1,5))
if mibBuilder.loadTexts:dellNetFpStatsPerPortTable.setStatus(_A)
_DellNetFpStatsPerPortEntry_Object=MibTableRow
dellNetFpStatsPerPortEntry=_DellNetFpStatsPerPortEntry_Object((1,3,6,1,4,1,6027,3,27,1,5,1))
dellNetFpStatsPerPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dellNetFpStatsPerPortEntry.setStatus(_A)
_DellNetFpCurrentUsagePerPort_Type=Counter32
_DellNetFpCurrentUsagePerPort_Object=MibTableColumn
dellNetFpCurrentUsagePerPort=_DellNetFpCurrentUsagePerPort_Object((1,3,6,1,4,1,6027,3,27,1,5,1,1),_DellNetFpCurrentUsagePerPort_Type())
dellNetFpCurrentUsagePerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCurrentUsagePerPort.setStatus(_A)
_DellNetFpDefaultPacketBuffAlloc_Type=Counter32
_DellNetFpDefaultPacketBuffAlloc_Object=MibTableColumn
dellNetFpDefaultPacketBuffAlloc=_DellNetFpDefaultPacketBuffAlloc_Object((1,3,6,1,4,1,6027,3,27,1,5,1,2),_DellNetFpDefaultPacketBuffAlloc_Type())
dellNetFpDefaultPacketBuffAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpDefaultPacketBuffAlloc.setStatus(_A)
_DellNetFpMaxLimitPerPort_Type=Counter32
_DellNetFpMaxLimitPerPort_Object=MibTableColumn
dellNetFpMaxLimitPerPort=_DellNetFpMaxLimitPerPort_Object((1,3,6,1,4,1,6027,3,27,1,5,1,3),_DellNetFpMaxLimitPerPort_Type())
dellNetFpMaxLimitPerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpMaxLimitPerPort.setStatus(_A)
_DellNetFpStatsPerCOSTable_Object=MibTable
dellNetFpStatsPerCOSTable=_DellNetFpStatsPerCOSTable_Object((1,3,6,1,4,1,6027,3,27,1,6))
if mibBuilder.loadTexts:dellNetFpStatsPerCOSTable.setStatus(_A)
_DellNetFpStatsPerCOSEntry_Object=MibTableRow
dellNetFpStatsPerCOSEntry=_DellNetFpStatsPerCOSEntry_Object((1,3,6,1,4,1,6027,3,27,1,6,1))
dellNetFpStatsPerCOSEntry.setIndexNames((0,_F,_G),(0,_E,_N))
if mibBuilder.loadTexts:dellNetFpStatsPerCOSEntry.setStatus(_A)
class _DellNetFpPerPortCOSNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,21))
_DellNetFpPerPortCOSNumber_Type.__name__=_I
_DellNetFpPerPortCOSNumber_Object=MibTableColumn
dellNetFpPerPortCOSNumber=_DellNetFpPerPortCOSNumber_Object((1,3,6,1,4,1,6027,3,27,1,6,1,1),_DellNetFpPerPortCOSNumber_Type())
dellNetFpPerPortCOSNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpPerPortCOSNumber.setStatus(_A)
_DellNetFpCurrentUsagePerCOS_Type=Counter32
_DellNetFpCurrentUsagePerCOS_Object=MibTableColumn
dellNetFpCurrentUsagePerCOS=_DellNetFpCurrentUsagePerCOS_Object((1,3,6,1,4,1,6027,3,27,1,6,1,2),_DellNetFpCurrentUsagePerCOS_Type())
dellNetFpCurrentUsagePerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCurrentUsagePerCOS.setStatus(_A)
_DellNetFpDefaultPacketBuffAllocPerCOS_Type=Counter32
_DellNetFpDefaultPacketBuffAllocPerCOS_Object=MibTableColumn
dellNetFpDefaultPacketBuffAllocPerCOS=_DellNetFpDefaultPacketBuffAllocPerCOS_Object((1,3,6,1,4,1,6027,3,27,1,6,1,3),_DellNetFpDefaultPacketBuffAllocPerCOS_Type())
dellNetFpDefaultPacketBuffAllocPerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpDefaultPacketBuffAllocPerCOS.setStatus(_A)
_DellNetFpMaxLimitPerCOS_Type=Counter32
_DellNetFpMaxLimitPerCOS_Object=MibTableColumn
dellNetFpMaxLimitPerCOS=_DellNetFpMaxLimitPerCOS_Object((1,3,6,1,4,1,6027,3,27,1,6,1,4),_DellNetFpMaxLimitPerCOS_Type())
dellNetFpMaxLimitPerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpMaxLimitPerCOS.setStatus(_A)
_DellNetFpHOLDropsPerCOS_Type=Counter64
_DellNetFpHOLDropsPerCOS_Object=MibTableColumn
dellNetFpHOLDropsPerCOS=_DellNetFpHOLDropsPerCOS_Object((1,3,6,1,4,1,6027,3,27,1,6,1,5),_DellNetFpHOLDropsPerCOS_Type())
dellNetFpHOLDropsPerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpHOLDropsPerCOS.setStatus(_A)
_DellNetFpCpuDataPlaneCOSTable_Object=MibTable
dellNetFpCpuDataPlaneCOSTable=_DellNetFpCpuDataPlaneCOSTable_Object((1,3,6,1,4,1,6027,3,27,1,7))
if mibBuilder.loadTexts:dellNetFpCpuDataPlaneCOSTable.setStatus(_A)
_DellNetFpCpuDataPlaneCOSEntry_Object=MibTableRow
dellNetFpCpuDataPlaneCOSEntry=_DellNetFpCpuDataPlaneCOSEntry_Object((1,3,6,1,4,1,6027,3,27,1,7,1))
dellNetFpCpuDataPlaneCOSEntry.setIndexNames((0,_E,_K),(0,_E,_J),(0,_E,_S))
if mibBuilder.loadTexts:dellNetFpCpuDataPlaneCOSEntry.setStatus(_A)
class _DellNetFpCOSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_DellNetFpCOSIndex_Type.__name__=_I
_DellNetFpCOSIndex_Object=MibTableColumn
dellNetFpCOSIndex=_DellNetFpCOSIndex_Object((1,3,6,1,4,1,6027,3,27,1,7,1,1),_DellNetFpCOSIndex_Type())
dellNetFpCOSIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpCOSIndex.setStatus(_A)
_DellNetFpRxPktCOS_Type=Counter32
_DellNetFpRxPktCOS_Object=MibTableColumn
dellNetFpRxPktCOS=_DellNetFpRxPktCOS_Object((1,3,6,1,4,1,6027,3,27,1,7,1,2),_DellNetFpRxPktCOS_Type())
dellNetFpRxPktCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpRxPktCOS.setStatus(_A)
_DellNetFpTxPktCOS_Type=Counter32
_DellNetFpTxPktCOS_Object=MibTableColumn
dellNetFpTxPktCOS=_DellNetFpTxPktCOS_Object((1,3,6,1,4,1,6027,3,27,1,7,1,3),_DellNetFpTxPktCOS_Type())
dellNetFpTxPktCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTxPktCOS.setStatus(_A)
_DellNetFpEgrQBuffSnapshotTable_Object=MibTable
dellNetFpEgrQBuffSnapshotTable=_DellNetFpEgrQBuffSnapshotTable_Object((1,3,6,1,4,1,6027,3,27,1,8))
if mibBuilder.loadTexts:dellNetFpEgrQBuffSnapshotTable.setStatus(_A)
_DellNetFpEgrQBuffSnapshotEntry_Object=MibTableRow
dellNetFpEgrQBuffSnapshotEntry=_DellNetFpEgrQBuffSnapshotEntry_Object((1,3,6,1,4,1,6027,3,27,1,8,1))
dellNetFpEgrQBuffSnapshotEntry.setIndexNames((0,_F,_G),(0,_E,_N))
if mibBuilder.loadTexts:dellNetFpEgrQBuffSnapshotEntry.setStatus(_A)
_DellNetFpEgrQTotBuffCells_Type=Counter32
_DellNetFpEgrQTotBuffCells_Object=MibTableColumn
dellNetFpEgrQTotBuffCells=_DellNetFpEgrQTotBuffCells_Object((1,3,6,1,4,1,6027,3,27,1,8,1,1),_DellNetFpEgrQTotBuffCells_Type())
dellNetFpEgrQTotBuffCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgrQTotBuffCells.setStatus(_A)
_DellNetFpIngPgBuffSnapshotTable_Object=MibTable
dellNetFpIngPgBuffSnapshotTable=_DellNetFpIngPgBuffSnapshotTable_Object((1,3,6,1,4,1,6027,3,27,1,9))
if mibBuilder.loadTexts:dellNetFpIngPgBuffSnapshotTable.setStatus(_A)
_DellNetFpIngPgBuffSnapshotEntry_Object=MibTableRow
dellNetFpIngPgBuffSnapshotEntry=_DellNetFpIngPgBuffSnapshotEntry_Object((1,3,6,1,4,1,6027,3,27,1,9,1))
dellNetFpIngPgBuffSnapshotEntry.setIndexNames((0,_F,_G),(0,_E,_P))
if mibBuilder.loadTexts:dellNetFpIngPgBuffSnapshotEntry.setStatus(_A)
_DellNetFpPerPortPGIndex_Type=Integer32
_DellNetFpPerPortPGIndex_Object=MibTableColumn
dellNetFpPerPortPGIndex=_DellNetFpPerPortPGIndex_Object((1,3,6,1,4,1,6027,3,27,1,9,1,1),_DellNetFpPerPortPGIndex_Type())
dellNetFpPerPortPGIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpPerPortPGIndex.setStatus(_A)
_DellNetFpIngSharedCells_Type=Counter32
_DellNetFpIngSharedCells_Object=MibTableColumn
dellNetFpIngSharedCells=_DellNetFpIngSharedCells_Object((1,3,6,1,4,1,6027,3,27,1,9,1,2),_DellNetFpIngSharedCells_Type())
dellNetFpIngSharedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngSharedCells.setStatus(_A)
_DellNetFpIngHeadroomCells_Type=Counter32
_DellNetFpIngHeadroomCells_Object=MibTableColumn
dellNetFpIngHeadroomCells=_DellNetFpIngHeadroomCells_Object((1,3,6,1,4,1,6027,3,27,1,9,1,3),_DellNetFpIngHeadroomCells_Type())
dellNetFpIngHeadroomCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpIngHeadroomCells.setStatus(_A)
_DellNetFpStatsPerPgTable_Object=MibTable
dellNetFpStatsPerPgTable=_DellNetFpStatsPerPgTable_Object((1,3,6,1,4,1,6027,3,27,1,10))
if mibBuilder.loadTexts:dellNetFpStatsPerPgTable.setStatus(_A)
_DellNetFpStatsPerPgEntry_Object=MibTableRow
dellNetFpStatsPerPgEntry=_DellNetFpStatsPerPgEntry_Object((1,3,6,1,4,1,6027,3,27,1,10,1))
dellNetFpStatsPerPgEntry.setIndexNames((0,_F,_G),(0,_E,_P))
if mibBuilder.loadTexts:dellNetFpStatsPerPgEntry.setStatus(_A)
_DellNetFpStatsPgLimitMinCells_Type=Integer32
_DellNetFpStatsPgLimitMinCells_Object=MibTableColumn
dellNetFpStatsPgLimitMinCells=_DellNetFpStatsPgLimitMinCells_Object((1,3,6,1,4,1,6027,3,27,1,10,1,1),_DellNetFpStatsPgLimitMinCells_Type())
dellNetFpStatsPgLimitMinCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpStatsPgLimitMinCells.setStatus(_A)
_DellNetFpStatsPgSharedCells_Type=Integer32
_DellNetFpStatsPgSharedCells_Object=MibTableColumn
dellNetFpStatsPgSharedCells=_DellNetFpStatsPgSharedCells_Object((1,3,6,1,4,1,6027,3,27,1,10,1,2),_DellNetFpStatsPgSharedCells_Type())
dellNetFpStatsPgSharedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpStatsPgSharedCells.setStatus(_A)
class _DellNetFpStatsPgSharedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_DellNetFpStatsPgSharedMode_Type.__name__=_I
_DellNetFpStatsPgSharedMode_Object=MibTableColumn
dellNetFpStatsPgSharedMode=_DellNetFpStatsPgSharedMode_Object((1,3,6,1,4,1,6027,3,27,1,10,1,3),_DellNetFpStatsPgSharedMode_Type())
dellNetFpStatsPgSharedMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpStatsPgSharedMode.setStatus(_A)
_DellNetFpStatsPgHdrmCells_Type=Integer32
_DellNetFpStatsPgHdrmCells_Object=MibTableColumn
dellNetFpStatsPgHdrmCells=_DellNetFpStatsPgHdrmCells_Object((1,3,6,1,4,1,6027,3,27,1,10,1,4),_DellNetFpStatsPgHdrmCells_Type())
dellNetFpStatsPgHdrmCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpStatsPgHdrmCells.setStatus(_A)
_DellNetFpStatsPgCounterMinCells_Type=Counter32
_DellNetFpStatsPgCounterMinCells_Object=MibTableColumn
dellNetFpStatsPgCounterMinCells=_DellNetFpStatsPgCounterMinCells_Object((1,3,6,1,4,1,6027,3,27,1,10,1,5),_DellNetFpStatsPgCounterMinCells_Type())
dellNetFpStatsPgCounterMinCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpStatsPgCounterMinCells.setStatus(_A)
_DellNetFpStatsPgCounterSharedCells_Type=Counter32
_DellNetFpStatsPgCounterSharedCells_Object=MibTableColumn
dellNetFpStatsPgCounterSharedCells=_DellNetFpStatsPgCounterSharedCells_Object((1,3,6,1,4,1,6027,3,27,1,10,1,6),_DellNetFpStatsPgCounterSharedCells_Type())
dellNetFpStatsPgCounterSharedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpStatsPgCounterSharedCells.setStatus(_A)
_DellNetFpStatsPgCounterHdrmCells_Type=Counter32
_DellNetFpStatsPgCounterHdrmCells_Object=MibTableColumn
dellNetFpStatsPgCounterHdrmCells=_DellNetFpStatsPgCounterHdrmCells_Object((1,3,6,1,4,1,6027,3,27,1,10,1,7),_DellNetFpStatsPgCounterHdrmCells_Type())
dellNetFpStatsPgCounterHdrmCells.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpStatsPgCounterHdrmCells.setStatus(_A)
_DellNetPfcPerPrioTable_Object=MibTable
dellNetPfcPerPrioTable=_DellNetPfcPerPrioTable_Object((1,3,6,1,4,1,6027,3,27,1,11))
if mibBuilder.loadTexts:dellNetPfcPerPrioTable.setStatus(_A)
_DellNetPfcPerPrioEntry_Object=MibTableRow
dellNetPfcPerPrioEntry=_DellNetPfcPerPrioEntry_Object((1,3,6,1,4,1,6027,3,27,1,11,1))
dellNetPfcPerPrioEntry.setIndexNames((0,_F,_G),(0,_E,_L))
if mibBuilder.loadTexts:dellNetPfcPerPrioEntry.setStatus(_A)
class _DellNetPrioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_DellNetPrioIndex_Type.__name__=_I
_DellNetPrioIndex_Object=MibTableColumn
dellNetPrioIndex=_DellNetPrioIndex_Object((1,3,6,1,4,1,6027,3,27,1,11,1,1),_DellNetPrioIndex_Type())
dellNetPrioIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetPrioIndex.setStatus(_A)
_DellNetPfcPerPrioRequests_Type=Counter64
_DellNetPfcPerPrioRequests_Object=MibTableColumn
dellNetPfcPerPrioRequests=_DellNetPfcPerPrioRequests_Object((1,3,6,1,4,1,6027,3,27,1,11,1,2),_DellNetPfcPerPrioRequests_Type())
dellNetPfcPerPrioRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetPfcPerPrioRequests.setStatus(_A)
if mibBuilder.loadTexts:dellNetPfcPerPrioRequests.setUnits(_V)
_DellNetPfcPerPrioIndications_Type=Counter64
_DellNetPfcPerPrioIndications_Object=MibTableColumn
dellNetPfcPerPrioIndications=_DellNetPfcPerPrioIndications_Object((1,3,6,1,4,1,6027,3,27,1,11,1,3),_DellNetPfcPerPrioIndications_Type())
dellNetPfcPerPrioIndications.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetPfcPerPrioIndications.setStatus(_A)
if mibBuilder.loadTexts:dellNetPfcPerPrioIndications.setUnits(_W)
_DellNetFpCpuPartyBusPortStatsTable_Object=MibTable
dellNetFpCpuPartyBusPortStatsTable=_DellNetFpCpuPartyBusPortStatsTable_Object((1,3,6,1,4,1,6027,3,27,1,12))
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsTable.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsEntry_Object=MibTableRow
dellNetFpCpuPartyBusPortStatsEntry=_DellNetFpCpuPartyBusPortStatsEntry_Object((1,3,6,1,4,1,6027,3,27,1,12,1))
dellNetFpCpuPartyBusPortStatsEntry.setIndexNames((0,_E,_K),(0,_E,_J),(0,_E,_X))
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsEntry.setStatus(_A)
class _DellNetFpStackPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,192))
_DellNetFpStackPortIndex_Type.__name__=_I
_DellNetFpStackPortIndex_Object=MibTableColumn
dellNetFpStackPortIndex=_DellNetFpStackPortIndex_Object((1,3,6,1,4,1,6027,3,27,1,12,1,1),_DellNetFpStackPortIndex_Type())
dellNetFpStackPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpStackPortIndex.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutOctets_Type=Counter64
_DellNetFpCpuPartyBusPortStatsOutOctets_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutOctets=_DellNetFpCpuPartyBusPortStatsOutOctets_Object((1,3,6,1,4,1,6027,3,27,1,12,1,2),_DellNetFpCpuPartyBusPortStatsOutOctets_Type())
dellNetFpCpuPartyBusPortStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutOctets.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutDropPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutDropPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutDropPkts=_DellNetFpCpuPartyBusPortStatsOutDropPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,3),_DellNetFpCpuPartyBusPortStatsOutDropPkts_Type())
dellNetFpCpuPartyBusPortStatsOutDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutDropPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutCOS0Pkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutCOS0Pkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutCOS0Pkts=_DellNetFpCpuPartyBusPortStatsOutCOS0Pkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,4),_DellNetFpCpuPartyBusPortStatsOutCOS0Pkts_Type())
dellNetFpCpuPartyBusPortStatsOutCOS0Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutCOS0Pkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutCOS1Pkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutCOS1Pkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutCOS1Pkts=_DellNetFpCpuPartyBusPortStatsOutCOS1Pkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,5),_DellNetFpCpuPartyBusPortStatsOutCOS1Pkts_Type())
dellNetFpCpuPartyBusPortStatsOutCOS1Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutCOS1Pkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutCOS2Pkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutCOS2Pkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutCOS2Pkts=_DellNetFpCpuPartyBusPortStatsOutCOS2Pkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,6),_DellNetFpCpuPartyBusPortStatsOutCOS2Pkts_Type())
dellNetFpCpuPartyBusPortStatsOutCOS2Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutCOS2Pkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutCOS3Pkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutCOS3Pkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutCOS3Pkts=_DellNetFpCpuPartyBusPortStatsOutCOS3Pkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,7),_DellNetFpCpuPartyBusPortStatsOutCOS3Pkts_Type())
dellNetFpCpuPartyBusPortStatsOutCOS3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutCOS3Pkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutCOS4Pkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutCOS4Pkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutCOS4Pkts=_DellNetFpCpuPartyBusPortStatsOutCOS4Pkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,8),_DellNetFpCpuPartyBusPortStatsOutCOS4Pkts_Type())
dellNetFpCpuPartyBusPortStatsOutCOS4Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutCOS4Pkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutCOS5Pkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutCOS5Pkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutCOS5Pkts=_DellNetFpCpuPartyBusPortStatsOutCOS5Pkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,9),_DellNetFpCpuPartyBusPortStatsOutCOS5Pkts_Type())
dellNetFpCpuPartyBusPortStatsOutCOS5Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutCOS5Pkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutUnicastPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutUnicastPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutUnicastPkts=_DellNetFpCpuPartyBusPortStatsOutUnicastPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,10),_DellNetFpCpuPartyBusPortStatsOutUnicastPkts_Type())
dellNetFpCpuPartyBusPortStatsOutUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutUnicastPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutMulticastPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutMulticastPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutMulticastPkts=_DellNetFpCpuPartyBusPortStatsOutMulticastPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,11),_DellNetFpCpuPartyBusPortStatsOutMulticastPkts_Type())
dellNetFpCpuPartyBusPortStatsOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutMulticastPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutBroadcastPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutBroadcastPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutBroadcastPkts=_DellNetFpCpuPartyBusPortStatsOutBroadcastPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,12),_DellNetFpCpuPartyBusPortStatsOutBroadcastPkts_Type())
dellNetFpCpuPartyBusPortStatsOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutBroadcastPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutPausePkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutPausePkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutPausePkts=_DellNetFpCpuPartyBusPortStatsOutPausePkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,13),_DellNetFpCpuPartyBusPortStatsOutPausePkts_Type())
dellNetFpCpuPartyBusPortStatsOutPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutPausePkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutCollisions_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutCollisions_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutCollisions=_DellNetFpCpuPartyBusPortStatsOutCollisions_Object((1,3,6,1,4,1,6027,3,27,1,12,1,14),_DellNetFpCpuPartyBusPortStatsOutCollisions_Type())
dellNetFpCpuPartyBusPortStatsOutCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutCollisions.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutSingleCollisions_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutSingleCollisions_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutSingleCollisions=_DellNetFpCpuPartyBusPortStatsOutSingleCollisions_Object((1,3,6,1,4,1,6027,3,27,1,12,1,15),_DellNetFpCpuPartyBusPortStatsOutSingleCollisions_Type())
dellNetFpCpuPartyBusPortStatsOutSingleCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutSingleCollisions.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutMultiCollisions_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutMultiCollisions_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutMultiCollisions=_DellNetFpCpuPartyBusPortStatsOutMultiCollisions_Object((1,3,6,1,4,1,6027,3,27,1,12,1,16),_DellNetFpCpuPartyBusPortStatsOutMultiCollisions_Type())
dellNetFpCpuPartyBusPortStatsOutMultiCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutMultiCollisions.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutLateCollisions_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutLateCollisions_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutLateCollisions=_DellNetFpCpuPartyBusPortStatsOutLateCollisions_Object((1,3,6,1,4,1,6027,3,27,1,12,1,17),_DellNetFpCpuPartyBusPortStatsOutLateCollisions_Type())
dellNetFpCpuPartyBusPortStatsOutLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutLateCollisions.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutExcessCollisions_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutExcessCollisions_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutExcessCollisions=_DellNetFpCpuPartyBusPortStatsOutExcessCollisions_Object((1,3,6,1,4,1,6027,3,27,1,12,1,18),_DellNetFpCpuPartyBusPortStatsOutExcessCollisions_Type())
dellNetFpCpuPartyBusPortStatsOutExcessCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutExcessCollisions.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutDeferred_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutDeferred_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutDeferred=_DellNetFpCpuPartyBusPortStatsOutDeferred_Object((1,3,6,1,4,1,6027,3,27,1,12,1,19),_DellNetFpCpuPartyBusPortStatsOutDeferred_Type())
dellNetFpCpuPartyBusPortStatsOutDeferred.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutDeferred.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsOutDiscarded_Type=Counter32
_DellNetFpCpuPartyBusPortStatsOutDiscarded_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsOutDiscarded=_DellNetFpCpuPartyBusPortStatsOutDiscarded_Object((1,3,6,1,4,1,6027,3,27,1,12,1,20),_DellNetFpCpuPartyBusPortStatsOutDiscarded_Type())
dellNetFpCpuPartyBusPortStatsOutDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsOutDiscarded.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInOctets_Type=Counter64
_DellNetFpCpuPartyBusPortStatsInOctets_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInOctets=_DellNetFpCpuPartyBusPortStatsInOctets_Object((1,3,6,1,4,1,6027,3,27,1,12,1,21),_DellNetFpCpuPartyBusPortStatsInOctets_Type())
dellNetFpCpuPartyBusPortStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInOctets.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInUndersizePkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInUndersizePkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInUndersizePkts=_DellNetFpCpuPartyBusPortStatsInUndersizePkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,22),_DellNetFpCpuPartyBusPortStatsInUndersizePkts_Type())
dellNetFpCpuPartyBusPortStatsInUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInUndersizePkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInOversizePkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInOversizePkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInOversizePkts=_DellNetFpCpuPartyBusPortStatsInOversizePkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,23),_DellNetFpCpuPartyBusPortStatsInOversizePkts_Type())
dellNetFpCpuPartyBusPortStatsInOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInOversizePkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInPausePkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInPausePkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInPausePkts=_DellNetFpCpuPartyBusPortStatsInPausePkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,24),_DellNetFpCpuPartyBusPortStatsInPausePkts_Type())
dellNetFpCpuPartyBusPortStatsInPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInPausePkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsIn64OctetPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsIn64OctetPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsIn64OctetPkts=_DellNetFpCpuPartyBusPortStatsIn64OctetPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,25),_DellNetFpCpuPartyBusPortStatsIn64OctetPkts_Type())
dellNetFpCpuPartyBusPortStatsIn64OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsIn64OctetPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsIn65To127OctetPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsIn65To127OctetPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsIn65To127OctetPkts=_DellNetFpCpuPartyBusPortStatsIn65To127OctetPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,26),_DellNetFpCpuPartyBusPortStatsIn65To127OctetPkts_Type())
dellNetFpCpuPartyBusPortStatsIn65To127OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsIn65To127OctetPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsIn128To255OctetPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsIn128To255OctetPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsIn128To255OctetPkts=_DellNetFpCpuPartyBusPortStatsIn128To255OctetPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,27),_DellNetFpCpuPartyBusPortStatsIn128To255OctetPkts_Type())
dellNetFpCpuPartyBusPortStatsIn128To255OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsIn128To255OctetPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsIn256To511OctetPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsIn256To511OctetPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsIn256To511OctetPkts=_DellNetFpCpuPartyBusPortStatsIn256To511OctetPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,28),_DellNetFpCpuPartyBusPortStatsIn256To511OctetPkts_Type())
dellNetFpCpuPartyBusPortStatsIn256To511OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsIn256To511OctetPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsIn512To1023OctetPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsIn512To1023OctetPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsIn512To1023OctetPkts=_DellNetFpCpuPartyBusPortStatsIn512To1023OctetPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,29),_DellNetFpCpuPartyBusPortStatsIn512To1023OctetPkts_Type())
dellNetFpCpuPartyBusPortStatsIn512To1023OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsIn512To1023OctetPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsIn1024ToMaxOctetPkts=_DellNetFpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,30),_DellNetFpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Type())
dellNetFpCpuPartyBusPortStatsIn1024ToMaxOctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsIn1024ToMaxOctetPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInJabbers_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInJabbers_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInJabbers=_DellNetFpCpuPartyBusPortStatsInJabbers_Object((1,3,6,1,4,1,6027,3,27,1,12,1,31),_DellNetFpCpuPartyBusPortStatsInJabbers_Type())
dellNetFpCpuPartyBusPortStatsInJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInJabbers.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInAlignErrors_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInAlignErrors_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInAlignErrors=_DellNetFpCpuPartyBusPortStatsInAlignErrors_Object((1,3,6,1,4,1,6027,3,27,1,12,1,32),_DellNetFpCpuPartyBusPortStatsInAlignErrors_Type())
dellNetFpCpuPartyBusPortStatsInAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInAlignErrors.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInFcsErrors_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInFcsErrors_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInFcsErrors=_DellNetFpCpuPartyBusPortStatsInFcsErrors_Object((1,3,6,1,4,1,6027,3,27,1,12,1,33),_DellNetFpCpuPartyBusPortStatsInFcsErrors_Type())
dellNetFpCpuPartyBusPortStatsInFcsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInFcsErrors.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInGoodOctets_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInGoodOctets_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInGoodOctets=_DellNetFpCpuPartyBusPortStatsInGoodOctets_Object((1,3,6,1,4,1,6027,3,27,1,12,1,34),_DellNetFpCpuPartyBusPortStatsInGoodOctets_Type())
dellNetFpCpuPartyBusPortStatsInGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInGoodOctets.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInDropPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInDropPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInDropPkts=_DellNetFpCpuPartyBusPortStatsInDropPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,35),_DellNetFpCpuPartyBusPortStatsInDropPkts_Type())
dellNetFpCpuPartyBusPortStatsInDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInDropPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInUnicastPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInUnicastPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInUnicastPkts=_DellNetFpCpuPartyBusPortStatsInUnicastPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,36),_DellNetFpCpuPartyBusPortStatsInUnicastPkts_Type())
dellNetFpCpuPartyBusPortStatsInUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInUnicastPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInMulticastPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInMulticastPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInMulticastPkts=_DellNetFpCpuPartyBusPortStatsInMulticastPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,37),_DellNetFpCpuPartyBusPortStatsInMulticastPkts_Type())
dellNetFpCpuPartyBusPortStatsInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInMulticastPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInBroadcastPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInBroadcastPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInBroadcastPkts=_DellNetFpCpuPartyBusPortStatsInBroadcastPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,38),_DellNetFpCpuPartyBusPortStatsInBroadcastPkts_Type())
dellNetFpCpuPartyBusPortStatsInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInBroadcastPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInSrcAddrChanges_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInSrcAddrChanges_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInSrcAddrChanges=_DellNetFpCpuPartyBusPortStatsInSrcAddrChanges_Object((1,3,6,1,4,1,6027,3,27,1,12,1,39),_DellNetFpCpuPartyBusPortStatsInSrcAddrChanges_Type())
dellNetFpCpuPartyBusPortStatsInSrcAddrChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInSrcAddrChanges.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInFragments_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInFragments_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInFragments=_DellNetFpCpuPartyBusPortStatsInFragments_Object((1,3,6,1,4,1,6027,3,27,1,12,1,40),_DellNetFpCpuPartyBusPortStatsInFragments_Type())
dellNetFpCpuPartyBusPortStatsInFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInFragments.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInJumboPkts_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInJumboPkts_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInJumboPkts=_DellNetFpCpuPartyBusPortStatsInJumboPkts_Object((1,3,6,1,4,1,6027,3,27,1,12,1,41),_DellNetFpCpuPartyBusPortStatsInJumboPkts_Type())
dellNetFpCpuPartyBusPortStatsInJumboPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInJumboPkts.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInSymbolErrors_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInSymbolErrors_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInSymbolErrors=_DellNetFpCpuPartyBusPortStatsInSymbolErrors_Object((1,3,6,1,4,1,6027,3,27,1,12,1,42),_DellNetFpCpuPartyBusPortStatsInSymbolErrors_Type())
dellNetFpCpuPartyBusPortStatsInSymbolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInSymbolErrors.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInInRangeErrors_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInInRangeErrors_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInInRangeErrors=_DellNetFpCpuPartyBusPortStatsInInRangeErrors_Object((1,3,6,1,4,1,6027,3,27,1,12,1,43),_DellNetFpCpuPartyBusPortStatsInInRangeErrors_Type())
dellNetFpCpuPartyBusPortStatsInInRangeErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInInRangeErrors.setStatus(_A)
_DellNetFpCpuPartyBusPortStatsInOutRangeErrors_Type=Counter32
_DellNetFpCpuPartyBusPortStatsInOutRangeErrors_Object=MibTableColumn
dellNetFpCpuPartyBusPortStatsInOutRangeErrors=_DellNetFpCpuPartyBusPortStatsInOutRangeErrors_Object((1,3,6,1,4,1,6027,3,27,1,12,1,44),_DellNetFpCpuPartyBusPortStatsInOutRangeErrors_Type())
dellNetFpCpuPartyBusPortStatsInOutRangeErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpCpuPartyBusPortStatsInOutRangeErrors.setStatus(_A)
_DellNetFpDropsIfTable_Object=MibTable
dellNetFpDropsIfTable=_DellNetFpDropsIfTable_Object((1,3,6,1,4,1,6027,3,27,1,13))
if mibBuilder.loadTexts:dellNetFpDropsIfTable.setStatus(_C)
_DellNetFpDropsIfEntry_Object=MibTableRow
dellNetFpDropsIfEntry=_DellNetFpDropsIfEntry_Object((1,3,6,1,4,1,6027,3,27,1,13,1))
dellNetFpDropsIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dellNetFpDropsIfEntry.setStatus(_C)
_DellNetFpIfIngressDrops_Type=Counter64
_DellNetFpIfIngressDrops_Object=MibTableColumn
dellNetFpIfIngressDrops=_DellNetFpIfIngressDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,1),_DellNetFpIfIngressDrops_Type())
dellNetFpIfIngressDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngressDrops.setStatus(_C)
_DellNetFpIfIngIBPCBPFullDrops_Type=Counter64
_DellNetFpIfIngIBPCBPFullDrops_Object=MibTableColumn
dellNetFpIfIngIBPCBPFullDrops=_DellNetFpIfIngIBPCBPFullDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,2),_DellNetFpIfIngIBPCBPFullDrops_Type())
dellNetFpIfIngIBPCBPFullDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngIBPCBPFullDrops.setStatus(_C)
_DellNetFpIfIngPortSTPnotFwdDrops_Type=Counter64
_DellNetFpIfIngPortSTPnotFwdDrops_Object=MibTableColumn
dellNetFpIfIngPortSTPnotFwdDrops=_DellNetFpIfIngPortSTPnotFwdDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,3),_DellNetFpIfIngPortSTPnotFwdDrops_Type())
dellNetFpIfIngPortSTPnotFwdDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngPortSTPnotFwdDrops.setStatus(_C)
_DellNetFpIfIngIPv4L3Discards_Type=Counter64
_DellNetFpIfIngIPv4L3Discards_Object=MibTableColumn
dellNetFpIfIngIPv4L3Discards=_DellNetFpIfIngIPv4L3Discards_Object((1,3,6,1,4,1,6027,3,27,1,13,1,4),_DellNetFpIfIngIPv4L3Discards_Type())
dellNetFpIfIngIPv4L3Discards.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngIPv4L3Discards.setStatus(_C)
_DellNetFpIfIngPolicyDiscards_Type=Counter64
_DellNetFpIfIngPolicyDiscards_Object=MibTableColumn
dellNetFpIfIngPolicyDiscards=_DellNetFpIfIngPolicyDiscards_Object((1,3,6,1,4,1,6027,3,27,1,13,1,5),_DellNetFpIfIngPolicyDiscards_Type())
dellNetFpIfIngPolicyDiscards.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngPolicyDiscards.setStatus(_C)
_DellNetFpIfIngPacketsDroppedByFP_Type=Counter64
_DellNetFpIfIngPacketsDroppedByFP_Object=MibTableColumn
dellNetFpIfIngPacketsDroppedByFP=_DellNetFpIfIngPacketsDroppedByFP_Object((1,3,6,1,4,1,6027,3,27,1,13,1,6),_DellNetFpIfIngPacketsDroppedByFP_Type())
dellNetFpIfIngPacketsDroppedByFP.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngPacketsDroppedByFP.setStatus(_C)
_DellNetFpIfIngL2L3Drops_Type=Counter64
_DellNetFpIfIngL2L3Drops_Object=MibTableColumn
dellNetFpIfIngL2L3Drops=_DellNetFpIfIngL2L3Drops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,7),_DellNetFpIfIngL2L3Drops_Type())
dellNetFpIfIngL2L3Drops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngL2L3Drops.setStatus(_C)
_DellNetFpIfIngPortBitMapZeroDrops_Type=Counter64
_DellNetFpIfIngPortBitMapZeroDrops_Object=MibTableColumn
dellNetFpIfIngPortBitMapZeroDrops=_DellNetFpIfIngPortBitMapZeroDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,8),_DellNetFpIfIngPortBitMapZeroDrops_Type())
dellNetFpIfIngPortBitMapZeroDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngPortBitMapZeroDrops.setStatus(_C)
_DellNetFpIfIngRxVLANDrops_Type=Counter64
_DellNetFpIfIngRxVLANDrops_Object=MibTableColumn
dellNetFpIfIngRxVLANDrops=_DellNetFpIfIngRxVLANDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,9),_DellNetFpIfIngRxVLANDrops_Type())
dellNetFpIfIngRxVLANDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngRxVLANDrops.setStatus(_C)
_DellNetFpIfIngressFCSDrops_Type=Counter64
_DellNetFpIfIngressFCSDrops_Object=MibTableColumn
dellNetFpIfIngressFCSDrops=_DellNetFpIfIngressFCSDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,10),_DellNetFpIfIngressFCSDrops_Type())
dellNetFpIfIngressFCSDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngressFCSDrops.setStatus(_C)
_DellNetFpIfIngressMTUExceeds_Type=Counter64
_DellNetFpIfIngressMTUExceeds_Object=MibTableColumn
dellNetFpIfIngressMTUExceeds=_DellNetFpIfIngressMTUExceeds_Object((1,3,6,1,4,1,6027,3,27,1,13,1,11),_DellNetFpIfIngressMTUExceeds_Type())
dellNetFpIfIngressMTUExceeds.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngressMTUExceeds.setStatus(_C)
_DellNetFpIfMMUHOLDrops_Type=Counter64
_DellNetFpIfMMUHOLDrops_Object=MibTableColumn
dellNetFpIfMMUHOLDrops=_DellNetFpIfMMUHOLDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,12),_DellNetFpIfMMUHOLDrops_Type())
dellNetFpIfMMUHOLDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfMMUHOLDrops.setStatus(_C)
_DellNetFpIfMMUTxPurgeCellErr_Type=Counter64
_DellNetFpIfMMUTxPurgeCellErr_Object=MibTableColumn
dellNetFpIfMMUTxPurgeCellErr=_DellNetFpIfMMUTxPurgeCellErr_Object((1,3,6,1,4,1,6027,3,27,1,13,1,13),_DellNetFpIfMMUTxPurgeCellErr_Type())
dellNetFpIfMMUTxPurgeCellErr.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfMMUTxPurgeCellErr.setStatus(_C)
_DellNetFpIfMMUAgedDrops_Type=Counter64
_DellNetFpIfMMUAgedDrops_Object=MibTableColumn
dellNetFpIfMMUAgedDrops=_DellNetFpIfMMUAgedDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,14),_DellNetFpIfMMUAgedDrops_Type())
dellNetFpIfMMUAgedDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfMMUAgedDrops.setStatus(_C)
_DellNetFpIfEgressFCSDrops_Type=Counter64
_DellNetFpIfEgressFCSDrops_Object=MibTableColumn
dellNetFpIfEgressFCSDrops=_DellNetFpIfEgressFCSDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,15),_DellNetFpIfEgressFCSDrops_Type())
dellNetFpIfEgressFCSDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfEgressFCSDrops.setStatus(_C)
_DellNetFpIfEgIPv4L3UCAgedDrops_Type=Counter64
_DellNetFpIfEgIPv4L3UCAgedDrops_Object=MibTableColumn
dellNetFpIfEgIPv4L3UCAgedDrops=_DellNetFpIfEgIPv4L3UCAgedDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,16),_DellNetFpIfEgIPv4L3UCAgedDrops_Type())
dellNetFpIfEgIPv4L3UCAgedDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfEgIPv4L3UCAgedDrops.setStatus(_C)
_DellNetFpIfEgTTLThresholdDrops_Type=Counter64
_DellNetFpIfEgTTLThresholdDrops_Object=MibTableColumn
dellNetFpIfEgTTLThresholdDrops=_DellNetFpIfEgTTLThresholdDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,17),_DellNetFpIfEgTTLThresholdDrops_Type())
dellNetFpIfEgTTLThresholdDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfEgTTLThresholdDrops.setStatus(_C)
_DellNetFpIfEgInvalidVLANCounterDrops_Type=Counter64
_DellNetFpIfEgInvalidVLANCounterDrops_Object=MibTableColumn
dellNetFpIfEgInvalidVLANCounterDrops=_DellNetFpIfEgInvalidVLANCounterDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,18),_DellNetFpIfEgInvalidVLANCounterDrops_Type())
dellNetFpIfEgInvalidVLANCounterDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfEgInvalidVLANCounterDrops.setStatus(_C)
_DellNetFpIfEgL2MCDrops_Type=Counter64
_DellNetFpIfEgL2MCDrops_Object=MibTableColumn
dellNetFpIfEgL2MCDrops=_DellNetFpIfEgL2MCDrops_Object((1,3,6,1,4,1,6027,3,27,1,13,1,19),_DellNetFpIfEgL2MCDrops_Type())
dellNetFpIfEgL2MCDrops.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfEgL2MCDrops.setStatus(_C)
_DellNetFpIfEgPktDropsOfAnyCondition_Type=Counter64
_DellNetFpIfEgPktDropsOfAnyCondition_Object=MibTableColumn
dellNetFpIfEgPktDropsOfAnyCondition=_DellNetFpIfEgPktDropsOfAnyCondition_Object((1,3,6,1,4,1,6027,3,27,1,13,1,20),_DellNetFpIfEgPktDropsOfAnyCondition_Type())
dellNetFpIfEgPktDropsOfAnyCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfEgPktDropsOfAnyCondition.setStatus(_C)
_DellNetFpIfEgHgMacUnderFlow_Type=Counter64
_DellNetFpIfEgHgMacUnderFlow_Object=MibTableColumn
dellNetFpIfEgHgMacUnderFlow=_DellNetFpIfEgHgMacUnderFlow_Object((1,3,6,1,4,1,6027,3,27,1,13,1,21),_DellNetFpIfEgHgMacUnderFlow_Type())
dellNetFpIfEgHgMacUnderFlow.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfEgHgMacUnderFlow.setStatus(_C)
_DellNetFpIfEgTxErrPktCounter_Type=Counter64
_DellNetFpIfEgTxErrPktCounter_Object=MibTableColumn
dellNetFpIfEgTxErrPktCounter=_DellNetFpIfEgTxErrPktCounter_Object((1,3,6,1,4,1,6027,3,27,1,13,1,22),_DellNetFpIfEgTxErrPktCounter_Type())
dellNetFpIfEgTxErrPktCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfEgTxErrPktCounter.setStatus(_C)
_DellNetFpStatsPerIfTable_Object=MibTable
dellNetFpStatsPerIfTable=_DellNetFpStatsPerIfTable_Object((1,3,6,1,4,1,6027,3,27,1,14))
if mibBuilder.loadTexts:dellNetFpStatsPerIfTable.setStatus(_C)
_DellNetFpStatsPerIfEntry_Object=MibTableRow
dellNetFpStatsPerIfEntry=_DellNetFpStatsPerIfEntry_Object((1,3,6,1,4,1,6027,3,27,1,14,1))
dellNetFpStatsPerIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dellNetFpStatsPerIfEntry.setStatus(_C)
_DellNetFpIfCurrentUsagePerPort_Type=Counter32
_DellNetFpIfCurrentUsagePerPort_Object=MibTableColumn
dellNetFpIfCurrentUsagePerPort=_DellNetFpIfCurrentUsagePerPort_Object((1,3,6,1,4,1,6027,3,27,1,14,1,1),_DellNetFpIfCurrentUsagePerPort_Type())
dellNetFpIfCurrentUsagePerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfCurrentUsagePerPort.setStatus(_C)
_DellNetFpIfDefaultPacketBuffAlloc_Type=Counter32
_DellNetFpIfDefaultPacketBuffAlloc_Object=MibTableColumn
dellNetFpIfDefaultPacketBuffAlloc=_DellNetFpIfDefaultPacketBuffAlloc_Object((1,3,6,1,4,1,6027,3,27,1,14,1,2),_DellNetFpIfDefaultPacketBuffAlloc_Type())
dellNetFpIfDefaultPacketBuffAlloc.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfDefaultPacketBuffAlloc.setStatus(_C)
_DellNetFpIfMaxLimitPerPort_Type=Counter32
_DellNetFpIfMaxLimitPerPort_Object=MibTableColumn
dellNetFpIfMaxLimitPerPort=_DellNetFpIfMaxLimitPerPort_Object((1,3,6,1,4,1,6027,3,27,1,14,1,3),_DellNetFpIfMaxLimitPerPort_Type())
dellNetFpIfMaxLimitPerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfMaxLimitPerPort.setStatus(_C)
_DellNetFpStatsPerIfCOSTable_Object=MibTable
dellNetFpStatsPerIfCOSTable=_DellNetFpStatsPerIfCOSTable_Object((1,3,6,1,4,1,6027,3,27,1,15))
if mibBuilder.loadTexts:dellNetFpStatsPerIfCOSTable.setStatus(_C)
_DellNetFpStatsPerIfCOSEntry_Object=MibTableRow
dellNetFpStatsPerIfCOSEntry=_DellNetFpStatsPerIfCOSEntry_Object((1,3,6,1,4,1,6027,3,27,1,15,1))
dellNetFpStatsPerIfCOSEntry.setIndexNames((0,_F,_G),(0,_E,_Q))
if mibBuilder.loadTexts:dellNetFpStatsPerIfCOSEntry.setStatus(_C)
class _DellNetFpIfPerCOSNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,21))
_DellNetFpIfPerCOSNumber_Type.__name__=_I
_DellNetFpIfPerCOSNumber_Object=MibTableColumn
dellNetFpIfPerCOSNumber=_DellNetFpIfPerCOSNumber_Object((1,3,6,1,4,1,6027,3,27,1,15,1,1),_DellNetFpIfPerCOSNumber_Type())
dellNetFpIfPerCOSNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfPerCOSNumber.setStatus(_C)
_DellNetFpIfCurrentUsagePerCOS_Type=Counter32
_DellNetFpIfCurrentUsagePerCOS_Object=MibTableColumn
dellNetFpIfCurrentUsagePerCOS=_DellNetFpIfCurrentUsagePerCOS_Object((1,3,6,1,4,1,6027,3,27,1,15,1,2),_DellNetFpIfCurrentUsagePerCOS_Type())
dellNetFpIfCurrentUsagePerCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfCurrentUsagePerCOS.setStatus(_C)
_DellNetFpIfDefaultPacketBuffAllocPerCOS_Type=Counter32
_DellNetFpIfDefaultPacketBuffAllocPerCOS_Object=MibTableColumn
dellNetFpIfDefaultPacketBuffAllocPerCOS=_DellNetFpIfDefaultPacketBuffAllocPerCOS_Object((1,3,6,1,4,1,6027,3,27,1,15,1,3),_DellNetFpIfDefaultPacketBuffAllocPerCOS_Type())
dellNetFpIfDefaultPacketBuffAllocPerCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfDefaultPacketBuffAllocPerCOS.setStatus(_C)
_DellNetFpIfMaxLimitPerCOS_Type=Counter32
_DellNetFpIfMaxLimitPerCOS_Object=MibTableColumn
dellNetFpIfMaxLimitPerCOS=_DellNetFpIfMaxLimitPerCOS_Object((1,3,6,1,4,1,6027,3,27,1,15,1,4),_DellNetFpIfMaxLimitPerCOS_Type())
dellNetFpIfMaxLimitPerCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfMaxLimitPerCOS.setStatus(_C)
_DellNetFpIfHOLDropsPerCOS_Type=Counter64
_DellNetFpIfHOLDropsPerCOS_Object=MibTableColumn
dellNetFpIfHOLDropsPerCOS=_DellNetFpIfHOLDropsPerCOS_Object((1,3,6,1,4,1,6027,3,27,1,15,1,5),_DellNetFpIfHOLDropsPerCOS_Type())
dellNetFpIfHOLDropsPerCOS.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfHOLDropsPerCOS.setStatus(_C)
_DellNetFpEgrQBuffSnapshotIfTable_Object=MibTable
dellNetFpEgrQBuffSnapshotIfTable=_DellNetFpEgrQBuffSnapshotIfTable_Object((1,3,6,1,4,1,6027,3,27,1,16))
if mibBuilder.loadTexts:dellNetFpEgrQBuffSnapshotIfTable.setStatus(_C)
_DellNetFpEgrQBuffSnapshotIfEntry_Object=MibTableRow
dellNetFpEgrQBuffSnapshotIfEntry=_DellNetFpEgrQBuffSnapshotIfEntry_Object((1,3,6,1,4,1,6027,3,27,1,16,1))
dellNetFpEgrQBuffSnapshotIfEntry.setIndexNames((0,_F,_G),(0,_E,_Q))
if mibBuilder.loadTexts:dellNetFpEgrQBuffSnapshotIfEntry.setStatus(_C)
_DellNetFpIfEgrQTotBuffCells_Type=Counter32
_DellNetFpIfEgrQTotBuffCells_Object=MibTableColumn
dellNetFpIfEgrQTotBuffCells=_DellNetFpIfEgrQTotBuffCells_Object((1,3,6,1,4,1,6027,3,27,1,16,1,1),_DellNetFpIfEgrQTotBuffCells_Type())
dellNetFpIfEgrQTotBuffCells.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfEgrQTotBuffCells.setStatus(_C)
_DellNetFpIngPgBuffSnapshotIfTable_Object=MibTable
dellNetFpIngPgBuffSnapshotIfTable=_DellNetFpIngPgBuffSnapshotIfTable_Object((1,3,6,1,4,1,6027,3,27,1,17))
if mibBuilder.loadTexts:dellNetFpIngPgBuffSnapshotIfTable.setStatus(_C)
_DellNetFpIngPgBuffSnapshotIfEntry_Object=MibTableRow
dellNetFpIngPgBuffSnapshotIfEntry=_DellNetFpIngPgBuffSnapshotIfEntry_Object((1,3,6,1,4,1,6027,3,27,1,17,1))
dellNetFpIngPgBuffSnapshotIfEntry.setIndexNames((0,_F,_G),(0,_E,_R))
if mibBuilder.loadTexts:dellNetFpIngPgBuffSnapshotIfEntry.setStatus(_C)
_DellNetFpIfPerPGIndex_Type=Integer32
_DellNetFpIfPerPGIndex_Object=MibTableColumn
dellNetFpIfPerPGIndex=_DellNetFpIfPerPGIndex_Object((1,3,6,1,4,1,6027,3,27,1,17,1,1),_DellNetFpIfPerPGIndex_Type())
dellNetFpIfPerPGIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfPerPGIndex.setStatus(_C)
_DellNetFpIfIngSharedCells_Type=Counter32
_DellNetFpIfIngSharedCells_Object=MibTableColumn
dellNetFpIfIngSharedCells=_DellNetFpIfIngSharedCells_Object((1,3,6,1,4,1,6027,3,27,1,17,1,2),_DellNetFpIfIngSharedCells_Type())
dellNetFpIfIngSharedCells.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngSharedCells.setStatus(_C)
_DellNetFpIfIngHeadroomCells_Type=Counter32
_DellNetFpIfIngHeadroomCells_Object=MibTableColumn
dellNetFpIfIngHeadroomCells=_DellNetFpIfIngHeadroomCells_Object((1,3,6,1,4,1,6027,3,27,1,17,1,3),_DellNetFpIfIngHeadroomCells_Type())
dellNetFpIfIngHeadroomCells.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfIngHeadroomCells.setStatus(_C)
_DellNetFpStatsPerPgIfTable_Object=MibTable
dellNetFpStatsPerPgIfTable=_DellNetFpStatsPerPgIfTable_Object((1,3,6,1,4,1,6027,3,27,1,18))
if mibBuilder.loadTexts:dellNetFpStatsPerPgIfTable.setStatus(_C)
_DellNetFpStatsPerPgIfEntry_Object=MibTableRow
dellNetFpStatsPerPgIfEntry=_DellNetFpStatsPerPgIfEntry_Object((1,3,6,1,4,1,6027,3,27,1,18,1))
dellNetFpStatsPerPgIfEntry.setIndexNames((0,_F,_G),(0,_E,_R))
if mibBuilder.loadTexts:dellNetFpStatsPerPgIfEntry.setStatus(_C)
_DellNetFpIfStatsPgLimitMinCells_Type=Integer32
_DellNetFpIfStatsPgLimitMinCells_Object=MibTableColumn
dellNetFpIfStatsPgLimitMinCells=_DellNetFpIfStatsPgLimitMinCells_Object((1,3,6,1,4,1,6027,3,27,1,18,1,1),_DellNetFpIfStatsPgLimitMinCells_Type())
dellNetFpIfStatsPgLimitMinCells.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfStatsPgLimitMinCells.setStatus(_C)
_DellNetFpIfStatsPgSharedCells_Type=Integer32
_DellNetFpIfStatsPgSharedCells_Object=MibTableColumn
dellNetFpIfStatsPgSharedCells=_DellNetFpIfStatsPgSharedCells_Object((1,3,6,1,4,1,6027,3,27,1,18,1,2),_DellNetFpIfStatsPgSharedCells_Type())
dellNetFpIfStatsPgSharedCells.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfStatsPgSharedCells.setStatus(_C)
class _DellNetFpIfStatsPgSharedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_U,1)))
_DellNetFpIfStatsPgSharedMode_Type.__name__=_I
_DellNetFpIfStatsPgSharedMode_Object=MibTableColumn
dellNetFpIfStatsPgSharedMode=_DellNetFpIfStatsPgSharedMode_Object((1,3,6,1,4,1,6027,3,27,1,18,1,3),_DellNetFpIfStatsPgSharedMode_Type())
dellNetFpIfStatsPgSharedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfStatsPgSharedMode.setStatus(_C)
_DellNetFpIfStatsPgHdrmCells_Type=Integer32
_DellNetFpIfStatsPgHdrmCells_Object=MibTableColumn
dellNetFpIfStatsPgHdrmCells=_DellNetFpIfStatsPgHdrmCells_Object((1,3,6,1,4,1,6027,3,27,1,18,1,4),_DellNetFpIfStatsPgHdrmCells_Type())
dellNetFpIfStatsPgHdrmCells.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfStatsPgHdrmCells.setStatus(_C)
_DellNetFpIfStatsPgCounterMinCells_Type=Counter32
_DellNetFpIfStatsPgCounterMinCells_Object=MibTableColumn
dellNetFpIfStatsPgCounterMinCells=_DellNetFpIfStatsPgCounterMinCells_Object((1,3,6,1,4,1,6027,3,27,1,18,1,5),_DellNetFpIfStatsPgCounterMinCells_Type())
dellNetFpIfStatsPgCounterMinCells.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfStatsPgCounterMinCells.setStatus(_C)
_DellNetFpIfStatsPgCounterSharedCells_Type=Counter32
_DellNetFpIfStatsPgCounterSharedCells_Object=MibTableColumn
dellNetFpIfStatsPgCounterSharedCells=_DellNetFpIfStatsPgCounterSharedCells_Object((1,3,6,1,4,1,6027,3,27,1,18,1,6),_DellNetFpIfStatsPgCounterSharedCells_Type())
dellNetFpIfStatsPgCounterSharedCells.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfStatsPgCounterSharedCells.setStatus(_C)
_DellNetFpIfStatsPgCounterHdrmCells_Type=Counter32
_DellNetFpIfStatsPgCounterHdrmCells_Object=MibTableColumn
dellNetFpIfStatsPgCounterHdrmCells=_DellNetFpIfStatsPgCounterHdrmCells_Object((1,3,6,1,4,1,6027,3,27,1,18,1,7),_DellNetFpIfStatsPgCounterHdrmCells_Type())
dellNetFpIfStatsPgCounterHdrmCells.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpIfStatsPgCounterHdrmCells.setStatus(_C)
_DellNetPfcPerPrioIfTable_Object=MibTable
dellNetPfcPerPrioIfTable=_DellNetPfcPerPrioIfTable_Object((1,3,6,1,4,1,6027,3,27,1,19))
if mibBuilder.loadTexts:dellNetPfcPerPrioIfTable.setStatus(_C)
_DellNetPfcPerPrioIfEntry_Object=MibTableRow
dellNetPfcPerPrioIfEntry=_DellNetPfcPerPrioIfEntry_Object((1,3,6,1,4,1,6027,3,27,1,19,1))
dellNetPfcPerPrioIfEntry.setIndexNames((0,_F,_G),(0,_E,_Y))
if mibBuilder.loadTexts:dellNetPfcPerPrioIfEntry.setStatus(_C)
class _DellNetIfPrioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_DellNetIfPrioIndex_Type.__name__=_I
_DellNetIfPrioIndex_Object=MibTableColumn
dellNetIfPrioIndex=_DellNetIfPrioIndex_Object((1,3,6,1,4,1,6027,3,27,1,19,1,1),_DellNetIfPrioIndex_Type())
dellNetIfPrioIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetIfPrioIndex.setStatus(_C)
_DellNetIfPfcPerPrioRequests_Type=Counter64
_DellNetIfPfcPerPrioRequests_Object=MibTableColumn
dellNetIfPfcPerPrioRequests=_DellNetIfPfcPerPrioRequests_Object((1,3,6,1,4,1,6027,3,27,1,19,1,2),_DellNetIfPfcPerPrioRequests_Type())
dellNetIfPfcPerPrioRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetIfPfcPerPrioRequests.setStatus(_C)
if mibBuilder.loadTexts:dellNetIfPfcPerPrioRequests.setUnits(_V)
_DellNetIfPfcPerPrioIndications_Type=Counter64
_DellNetIfPfcPerPrioIndications_Object=MibTableColumn
dellNetIfPfcPerPrioIndications=_DellNetIfPfcPerPrioIndications_Object((1,3,6,1,4,1,6027,3,27,1,19,1,3),_DellNetIfPfcPerPrioIndications_Type())
dellNetIfPfcPerPrioIndications.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetIfPfcPerPrioIndications.setStatus(_C)
if mibBuilder.loadTexts:dellNetIfPfcPerPrioIndications.setUnits(_W)
_DellNetFpEgrQIfCounterTable_Object=MibTable
dellNetFpEgrQIfCounterTable=_DellNetFpEgrQIfCounterTable_Object((1,3,6,1,4,1,6027,3,27,1,20))
if mibBuilder.loadTexts:dellNetFpEgrQIfCounterTable.setStatus(_A)
_DellNetFpEgrQIfCounterEntry_Object=MibTableRow
dellNetFpEgrQIfCounterEntry=_DellNetFpEgrQIfCounterEntry_Object((1,3,6,1,4,1,6027,3,27,1,20,1))
dellNetFpEgrQIfCounterEntry.setIndexNames((0,_F,_G),(0,_E,_Z),(0,_E,_N))
if mibBuilder.loadTexts:dellNetFpEgrQIfCounterEntry.setStatus(_A)
_DellNetFpEgrQComType_Type=ComType
_DellNetFpEgrQComType_Object=MibTableColumn
dellNetFpEgrQComType=_DellNetFpEgrQComType_Object((1,3,6,1,4,1,6027,3,27,1,20,1,1),_DellNetFpEgrQComType_Type())
dellNetFpEgrQComType.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpEgrQComType.setStatus(_A)
_DellNetFpEgrQTxPackets_Type=Counter64
_DellNetFpEgrQTxPackets_Object=MibTableColumn
dellNetFpEgrQTxPackets=_DellNetFpEgrQTxPackets_Object((1,3,6,1,4,1,6027,3,27,1,20,1,2),_DellNetFpEgrQTxPackets_Type())
dellNetFpEgrQTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgrQTxPackets.setStatus(_A)
_DellNetFpEgrQTxBytes_Type=Counter64
_DellNetFpEgrQTxBytes_Object=MibTableColumn
dellNetFpEgrQTxBytes=_DellNetFpEgrQTxBytes_Object((1,3,6,1,4,1,6027,3,27,1,20,1,3),_DellNetFpEgrQTxBytes_Type())
dellNetFpEgrQTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgrQTxBytes.setStatus(_A)
_DellNetFpEgrQDroppedPackets_Type=Counter64
_DellNetFpEgrQDroppedPackets_Object=MibTableColumn
dellNetFpEgrQDroppedPackets=_DellNetFpEgrQDroppedPackets_Object((1,3,6,1,4,1,6027,3,27,1,20,1,4),_DellNetFpEgrQDroppedPackets_Type())
dellNetFpEgrQDroppedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgrQDroppedPackets.setStatus(_A)
_DellNetFpEgrQDroppedBytes_Type=Counter64
_DellNetFpEgrQDroppedBytes_Object=MibTableColumn
dellNetFpEgrQDroppedBytes=_DellNetFpEgrQDroppedBytes_Object((1,3,6,1,4,1,6027,3,27,1,20,1,5),_DellNetFpEgrQDroppedBytes_Type())
dellNetFpEgrQDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgrQDroppedBytes.setStatus(_A)
_DellNetFpEgrQTxPacketsRate_Type=Counter64
_DellNetFpEgrQTxPacketsRate_Object=MibTableColumn
dellNetFpEgrQTxPacketsRate=_DellNetFpEgrQTxPacketsRate_Object((1,3,6,1,4,1,6027,3,27,1,20,1,6),_DellNetFpEgrQTxPacketsRate_Type())
dellNetFpEgrQTxPacketsRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgrQTxPacketsRate.setStatus(_A)
_DellNetFpEgrQTxBytesRate_Type=Counter64
_DellNetFpEgrQTxBytesRate_Object=MibTableColumn
dellNetFpEgrQTxBytesRate=_DellNetFpEgrQTxBytesRate_Object((1,3,6,1,4,1,6027,3,27,1,20,1,7),_DellNetFpEgrQTxBytesRate_Type())
dellNetFpEgrQTxBytesRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgrQTxBytesRate.setStatus(_A)
_DellNetFpEgrQDroppedPacketsRate_Type=Counter64
_DellNetFpEgrQDroppedPacketsRate_Object=MibTableColumn
dellNetFpEgrQDroppedPacketsRate=_DellNetFpEgrQDroppedPacketsRate_Object((1,3,6,1,4,1,6027,3,27,1,20,1,8),_DellNetFpEgrQDroppedPacketsRate_Type())
dellNetFpEgrQDroppedPacketsRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgrQDroppedPacketsRate.setStatus(_A)
_DellNetFpEgrQDroppedBytesRate_Type=Counter64
_DellNetFpEgrQDroppedBytesRate_Object=MibTableColumn
dellNetFpEgrQDroppedBytesRate=_DellNetFpEgrQDroppedBytesRate_Object((1,3,6,1,4,1,6027,3,27,1,20,1,9),_DellNetFpEgrQDroppedBytesRate_Type())
dellNetFpEgrQDroppedBytesRate.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEgrQDroppedBytesRate.setStatus(_A)
_DellNetFpPfcStormControl_ObjectIdentity=ObjectIdentity
dellNetFpPfcStormControl=_DellNetFpPfcStormControl_ObjectIdentity((1,3,6,1,4,1,6027,3,27,1,21))
_DellNetFpPfcStormControlStatus_ObjectIdentity=ObjectIdentity
dellNetFpPfcStormControlStatus=_DellNetFpPfcStormControlStatus_ObjectIdentity((1,3,6,1,4,1,6027,3,27,1,21,1))
_DellNetFpPfcStormControlStatusTable_Object=MibTable
dellNetFpPfcStormControlStatusTable=_DellNetFpPfcStormControlStatusTable_Object((1,3,6,1,4,1,6027,3,27,1,21,1,1))
if mibBuilder.loadTexts:dellNetFpPfcStormControlStatusTable.setStatus(_A)
_DellNetFpPfcStormControlStatusEntry_Object=MibTableRow
dellNetFpPfcStormControlStatusEntry=_DellNetFpPfcStormControlStatusEntry_Object((1,3,6,1,4,1,6027,3,27,1,21,1,1,1))
dellNetFpPfcStormControlStatusEntry.setIndexNames((0,_F,_G),(0,_E,_L))
if mibBuilder.loadTexts:dellNetFpPfcStormControlStatusEntry.setStatus(_A)
_DellNetFpPfcStormControlQueueState_Type=QState
_DellNetFpPfcStormControlQueueState_Object=MibTableColumn
dellNetFpPfcStormControlQueueState=_DellNetFpPfcStormControlQueueState_Object((1,3,6,1,4,1,6027,3,27,1,21,1,1,1,1),_DellNetFpPfcStormControlQueueState_Type())
dellNetFpPfcStormControlQueueState.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcStormControlQueueState.setStatus(_A)
_DellNetFpPfcStormControlDurationInDiscardState_Type=Counter64
_DellNetFpPfcStormControlDurationInDiscardState_Object=MibTableColumn
dellNetFpPfcStormControlDurationInDiscardState=_DellNetFpPfcStormControlDurationInDiscardState_Object((1,3,6,1,4,1,6027,3,27,1,21,1,1,1,2),_DellNetFpPfcStormControlDurationInDiscardState_Type())
dellNetFpPfcStormControlDurationInDiscardState.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcStormControlDurationInDiscardState.setStatus(_A)
_DellNetFpPfcStormControlDroppedPacketsIngress_Type=Counter64
_DellNetFpPfcStormControlDroppedPacketsIngress_Object=MibTableColumn
dellNetFpPfcStormControlDroppedPacketsIngress=_DellNetFpPfcStormControlDroppedPacketsIngress_Object((1,3,6,1,4,1,6027,3,27,1,21,1,1,1,3),_DellNetFpPfcStormControlDroppedPacketsIngress_Type())
dellNetFpPfcStormControlDroppedPacketsIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcStormControlDroppedPacketsIngress.setStatus(_A)
_DellNetFpPfcStormControlDroppedPacketsEgress_Type=Counter64
_DellNetFpPfcStormControlDroppedPacketsEgress_Object=MibTableColumn
dellNetFpPfcStormControlDroppedPacketsEgress=_DellNetFpPfcStormControlDroppedPacketsEgress_Object((1,3,6,1,4,1,6027,3,27,1,21,1,1,1,4),_DellNetFpPfcStormControlDroppedPacketsEgress_Type())
dellNetFpPfcStormControlDroppedPacketsEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcStormControlDroppedPacketsEgress.setStatus(_A)
_DellNetFpPfcStormControlCumulativeDroppedPacketsIngress_Type=Counter64
_DellNetFpPfcStormControlCumulativeDroppedPacketsIngress_Object=MibTableColumn
dellNetFpPfcStormControlCumulativeDroppedPacketsIngress=_DellNetFpPfcStormControlCumulativeDroppedPacketsIngress_Object((1,3,6,1,4,1,6027,3,27,1,21,1,1,1,5),_DellNetFpPfcStormControlCumulativeDroppedPacketsIngress_Type())
dellNetFpPfcStormControlCumulativeDroppedPacketsIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcStormControlCumulativeDroppedPacketsIngress.setStatus(_A)
_DellNetFpPfcStormControlCumulativeDroppedPacketsEgress_Type=Counter64
_DellNetFpPfcStormControlCumulativeDroppedPacketsEgress_Object=MibTableColumn
dellNetFpPfcStormControlCumulativeDroppedPacketsEgress=_DellNetFpPfcStormControlCumulativeDroppedPacketsEgress_Object((1,3,6,1,4,1,6027,3,27,1,21,1,1,1,6),_DellNetFpPfcStormControlCumulativeDroppedPacketsEgress_Type())
dellNetFpPfcStormControlCumulativeDroppedPacketsEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcStormControlCumulativeDroppedPacketsEgress.setStatus(_A)
_DellNetFpPfcStormControlStatistics_ObjectIdentity=ObjectIdentity
dellNetFpPfcStormControlStatistics=_DellNetFpPfcStormControlStatistics_ObjectIdentity((1,3,6,1,4,1,6027,3,27,1,21,2))
_DellNetFpPfcStormControlStatisticsTable_Object=MibTable
dellNetFpPfcStormControlStatisticsTable=_DellNetFpPfcStormControlStatisticsTable_Object((1,3,6,1,4,1,6027,3,27,1,21,2,1))
if mibBuilder.loadTexts:dellNetFpPfcStormControlStatisticsTable.setStatus(_A)
_DellNetFpPfcStormControlStatisticsEntry_Object=MibTableRow
dellNetFpPfcStormControlStatisticsEntry=_DellNetFpPfcStormControlStatisticsEntry_Object((1,3,6,1,4,1,6027,3,27,1,21,2,1,1))
dellNetFpPfcStormControlStatisticsEntry.setIndexNames((0,_F,_G),(0,_E,_L))
if mibBuilder.loadTexts:dellNetFpPfcStormControlStatisticsEntry.setStatus(_A)
_DellNetFpPfcStormControlDiscardStateCount_Type=Counter32
_DellNetFpPfcStormControlDiscardStateCount_Object=MibTableColumn
dellNetFpPfcStormControlDiscardStateCount=_DellNetFpPfcStormControlDiscardStateCount_Object((1,3,6,1,4,1,6027,3,27,1,21,2,1,1,1),_DellNetFpPfcStormControlDiscardStateCount_Type())
dellNetFpPfcStormControlDiscardStateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcStormControlDiscardStateCount.setStatus(_A)
_DellNetFpPfcStormControlDiscardStateForcedClearCount_Type=Counter32
_DellNetFpPfcStormControlDiscardStateForcedClearCount_Object=MibTableColumn
dellNetFpPfcStormControlDiscardStateForcedClearCount=_DellNetFpPfcStormControlDiscardStateForcedClearCount_Object((1,3,6,1,4,1,6027,3,27,1,21,2,1,1,2),_DellNetFpPfcStormControlDiscardStateForcedClearCount_Type())
dellNetFpPfcStormControlDiscardStateForcedClearCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcStormControlDiscardStateForcedClearCount.setStatus(_A)
_DellNetFpPfcStormControlDiscardStateNorxPfcClearCount_Type=Counter32
_DellNetFpPfcStormControlDiscardStateNorxPfcClearCount_Object=MibTableColumn
dellNetFpPfcStormControlDiscardStateNorxPfcClearCount=_DellNetFpPfcStormControlDiscardStateNorxPfcClearCount_Object((1,3,6,1,4,1,6027,3,27,1,21,2,1,1,3),_DellNetFpPfcStormControlDiscardStateNorxPfcClearCount_Type())
dellNetFpPfcStormControlDiscardStateNorxPfcClearCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcStormControlDiscardStateNorxPfcClearCount.setStatus(_A)
_DellNetFpPfcL2DlfDropCounterTable_Object=MibTable
dellNetFpPfcL2DlfDropCounterTable=_DellNetFpPfcL2DlfDropCounterTable_Object((1,3,6,1,4,1,6027,3,27,1,22))
if mibBuilder.loadTexts:dellNetFpPfcL2DlfDropCounterTable.setStatus(_A)
_DellNetFpPfcL2DlfDropCounterEntry_Object=MibTableRow
dellNetFpPfcL2DlfDropCounterEntry=_DellNetFpPfcL2DlfDropCounterEntry_Object((1,3,6,1,4,1,6027,3,27,1,22,1))
dellNetFpPfcL2DlfDropCounterEntry.setIndexNames((0,_E,_J),(0,_E,_M),(0,_E,_L))
if mibBuilder.loadTexts:dellNetFpPfcL2DlfDropCounterEntry.setStatus(_A)
_DellNetFpPfcL2DlfDropCounters_Type=Counter64
_DellNetFpPfcL2DlfDropCounters_Object=MibTableColumn
dellNetFpPfcL2DlfDropCounters=_DellNetFpPfcL2DlfDropCounters_Object((1,3,6,1,4,1,6027,3,27,1,22,1,1),_DellNetFpPfcL2DlfDropCounters_Type())
dellNetFpPfcL2DlfDropCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpPfcL2DlfDropCounters.setStatus(_A)
_DellNetFpServicePoolBufferSizeTable_Object=MibTable
dellNetFpServicePoolBufferSizeTable=_DellNetFpServicePoolBufferSizeTable_Object((1,3,6,1,4,1,6027,3,27,1,23))
if mibBuilder.loadTexts:dellNetFpServicePoolBufferSizeTable.setStatus(_A)
_DellNetFpServicePoolBufferSizeEntry_Object=MibTableRow
dellNetFpServicePoolBufferSizeEntry=_DellNetFpServicePoolBufferSizeEntry_Object((1,3,6,1,4,1,6027,3,27,1,23,1))
dellNetFpServicePoolBufferSizeEntry.setIndexNames((0,_E,_J),(0,_E,_M),(0,_E,_a))
if mibBuilder.loadTexts:dellNetFpServicePoolBufferSizeEntry.setStatus(_A)
_DellNetFpXPENumber_Type=Counter32
_DellNetFpXPENumber_Object=MibTableColumn
dellNetFpXPENumber=_DellNetFpXPENumber_Object((1,3,6,1,4,1,6027,3,27,1,23,1,1),_DellNetFpXPENumber_Type())
dellNetFpXPENumber.setMaxAccess(_D)
if mibBuilder.loadTexts:dellNetFpXPENumber.setStatus(_A)
_DellNetFpLossyServicePoolConfiguredBuffSize_Type=Counter32
_DellNetFpLossyServicePoolConfiguredBuffSize_Object=MibTableColumn
dellNetFpLossyServicePoolConfiguredBuffSize=_DellNetFpLossyServicePoolConfiguredBuffSize_Object((1,3,6,1,4,1,6027,3,27,1,23,1,2),_DellNetFpLossyServicePoolConfiguredBuffSize_Type())
dellNetFpLossyServicePoolConfiguredBuffSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpLossyServicePoolConfiguredBuffSize.setStatus(_A)
_DellNetFpLossyServicePoolUsedBuffSize_Type=Counter32
_DellNetFpLossyServicePoolUsedBuffSize_Object=MibTableColumn
dellNetFpLossyServicePoolUsedBuffSize=_DellNetFpLossyServicePoolUsedBuffSize_Object((1,3,6,1,4,1,6027,3,27,1,23,1,3),_DellNetFpLossyServicePoolUsedBuffSize_Type())
dellNetFpLossyServicePoolUsedBuffSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpLossyServicePoolUsedBuffSize.setStatus(_A)
_DellNetFpLosslessServicePoolConfiguredBuffSize_Type=Counter32
_DellNetFpLosslessServicePoolConfiguredBuffSize_Object=MibTableColumn
dellNetFpLosslessServicePoolConfiguredBuffSize=_DellNetFpLosslessServicePoolConfiguredBuffSize_Object((1,3,6,1,4,1,6027,3,27,1,23,1,4),_DellNetFpLosslessServicePoolConfiguredBuffSize_Type())
dellNetFpLosslessServicePoolConfiguredBuffSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpLosslessServicePoolConfiguredBuffSize.setStatus(_A)
_DellNetFpLosslessServicePoolUsedBuffSize_Type=Counter32
_DellNetFpLosslessServicePoolUsedBuffSize_Object=MibTableColumn
dellNetFpLosslessServicePoolUsedBuffSize=_DellNetFpLosslessServicePoolUsedBuffSize_Object((1,3,6,1,4,1,6027,3,27,1,23,1,5),_DellNetFpLosslessServicePoolUsedBuffSize_Type())
dellNetFpLosslessServicePoolUsedBuffSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpLosslessServicePoolUsedBuffSize.setStatus(_A)
_DellNetFpEcnPacketsTable_Object=MibTable
dellNetFpEcnPacketsTable=_DellNetFpEcnPacketsTable_Object((1,3,6,1,4,1,6027,3,27,1,24))
if mibBuilder.loadTexts:dellNetFpEcnPacketsTable.setStatus(_A)
_DellNetFpEcnPacketsEntry_Object=MibTableRow
dellNetFpEcnPacketsEntry=_DellNetFpEcnPacketsEntry_Object((1,3,6,1,4,1,6027,3,27,1,24,1))
dellNetFpEcnPacketsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dellNetFpEcnPacketsEntry.setStatus(_A)
_DellNetFpEcnMarkedTxPkts_Type=Counter32
_DellNetFpEcnMarkedTxPkts_Object=MibTableColumn
dellNetFpEcnMarkedTxPkts=_DellNetFpEcnMarkedTxPkts_Object((1,3,6,1,4,1,6027,3,27,1,24,1,1),_DellNetFpEcnMarkedTxPkts_Type())
dellNetFpEcnMarkedTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpEcnMarkedTxPkts.setStatus(_A)
_DellNetFpTotalDropPktsOnEcnEnabledQueues_Type=Counter64
_DellNetFpTotalDropPktsOnEcnEnabledQueues_Object=MibTableColumn
dellNetFpTotalDropPktsOnEcnEnabledQueues=_DellNetFpTotalDropPktsOnEcnEnabledQueues_Object((1,3,6,1,4,1,6027,3,27,1,24,1,2),_DellNetFpTotalDropPktsOnEcnEnabledQueues_Type())
dellNetFpTotalDropPktsOnEcnEnabledQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:dellNetFpTotalDropPktsOnEcnEnabledQueues.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ComType':ComType,'QState':QState,'dellNetFpStatsMib':dellNetFpStatsMib,'dellNetFpStatsObjects':dellNetFpStatsObjects,'dellNetFpCpuDataPlaneTable':dellNetFpCpuDataPlaneTable,'dellNetFpCpuDataPlaneStatsEntry':dellNetFpCpuDataPlaneStatsEntry,_K:dellNetProcessorDeviceType,_J:dellNetProcessorDeviceIndex,'dellNetFpRxHandle':dellNetFpRxHandle,'dellNetFpNoMhdr':dellNetFpNoMhdr,'dellNetFpNoMBuf':dellNetFpNoMBuf,'dellNetFpNoClus':dellNetFpNoClus,'dellNetFpRecvd':dellNetFpRecvd,'dellNetFpDropped':dellNetFpDropped,'dellNetFpRecvToNet':dellNetFpRecvToNet,'dellNetFpRxError':dellNetFpRxError,'dellNetFpRxDatapathError':dellNetFpRxDatapathError,'dellNetFpRxPktCOS0':dellNetFpRxPktCOS0,'dellNetFpRxPktCOS1':dellNetFpRxPktCOS1,'dellNetFpRxPktCOS2':dellNetFpRxPktCOS2,'dellNetFpRxPktCOS3':dellNetFpRxPktCOS3,'dellNetFpRxPktCOS4':dellNetFpRxPktCOS4,'dellNetFpRxPktCOS5':dellNetFpRxPktCOS5,'dellNetFpRxPktCOS6':dellNetFpRxPktCOS6,'dellNetFpRxPktCOS7':dellNetFpRxPktCOS7,'dellNetFpRxPktUnit0':dellNetFpRxPktUnit0,'dellNetFpRxPktUnit1':dellNetFpRxPktUnit1,'dellNetFpRxPktUnit2':dellNetFpRxPktUnit2,'dellNetFpRxPktUnit3':dellNetFpRxPktUnit3,'dellNetFpTransmitted':dellNetFpTransmitted,'dellNetFpTxRequested':dellNetFpTxRequested,'dellNetFpNoTxDesc':dellNetFpNoTxDesc,'dellNetFpTxError':dellNetFpTxError,'dellNetFpTxReqTooLarge':dellNetFpTxReqTooLarge,'dellNetFpTxInternalError':dellNetFpTxInternalError,'dellNetFpTxDatapathErr':dellNetFpTxDatapathErr,'dellNetFpTxPktCOS0':dellNetFpTxPktCOS0,'dellNetFpTxPktCOS1':dellNetFpTxPktCOS1,'dellNetFpTxPktCOS2':dellNetFpTxPktCOS2,'dellNetFpTxPktCOS3':dellNetFpTxPktCOS3,'dellNetFpTxPktCOS4':dellNetFpTxPktCOS4,'dellNetFpTxPktCOS5':dellNetFpTxPktCOS5,'dellNetFpTxPktCOS6':dellNetFpTxPktCOS6,'dellNetFpTxPktCOS7':dellNetFpTxPktCOS7,'dellNetFpTxPktUnit0':dellNetFpTxPktUnit0,'dellNetFpTxPktUnit1':dellNetFpTxPktUnit1,'dellNetFpTxPktUnit2':dellNetFpTxPktUnit2,'dellNetFpTxPktUnit3':dellNetFpTxPktUnit3,'dellNetFpCpuPartyBusTable':dellNetFpCpuPartyBusTable,'dellNetFpCpuPartyBusStatsEntry':dellNetFpCpuPartyBusStatsEntry,'dellNetFpPartyBusInputPackets':dellNetFpPartyBusInputPackets,'dellNetFpPartyBusInputBytes':dellNetFpPartyBusInputBytes,'dellNetFpPartyBusInputDropped':dellNetFpPartyBusInputDropped,'dellNetFpPartyBusInputError':dellNetFpPartyBusInputError,'dellNetFpPartyBusOutputPackets':dellNetFpPartyBusOutputPackets,'dellNetFpPartyBusOutputBytes':dellNetFpPartyBusOutputBytes,'dellNetFpPartyBusOutputError':dellNetFpPartyBusOutputError,'dellNetFpDropsTable':dellNetFpDropsTable,'dellNetFpDropsEntry':dellNetFpDropsEntry,'dellNetFpIngressDrops':dellNetFpIngressDrops,'dellNetFpIngIBPCBPFullDrops':dellNetFpIngIBPCBPFullDrops,'dellNetFpIngPortSTPnotFwdDrops':dellNetFpIngPortSTPnotFwdDrops,'dellNetFpIngIPv4L3Discards':dellNetFpIngIPv4L3Discards,'dellNetFpIngPolicyDiscards':dellNetFpIngPolicyDiscards,'dellNetFpIngPacketsDroppedByDELLNETFP':dellNetFpIngPacketsDroppedByDELLNETFP,'dellNetFpIngL2L3Drops':dellNetFpIngL2L3Drops,'dellNetFpIngPortBitMapZeroDrops':dellNetFpIngPortBitMapZeroDrops,'dellNetFpIngRxVLANDrops':dellNetFpIngRxVLANDrops,'dellNetFpIngressFCSDrops':dellNetFpIngressFCSDrops,'dellNetFpIngressMTUExceeds':dellNetFpIngressMTUExceeds,'dellNetFpMMUHOLDrops':dellNetFpMMUHOLDrops,'dellNetFpMMUTxPurgeCellErr':dellNetFpMMUTxPurgeCellErr,'dellNetFpMMUAgedDrops':dellNetFpMMUAgedDrops,'dellNetFpEgressFCSDrops':dellNetFpEgressFCSDrops,'dellNetFpEgIPv4L3UCAgedDrops':dellNetFpEgIPv4L3UCAgedDrops,'dellNetFpEgTTLThresholdDrops':dellNetFpEgTTLThresholdDrops,'dellNetFpEgInvalidVLANCounterDrops':dellNetFpEgInvalidVLANCounterDrops,'dellNetFpEgL2MCDrops':dellNetFpEgL2MCDrops,'dellNetFpEgPktDropsOfAnyCondition':dellNetFpEgPktDropsOfAnyCondition,'dellNetFpEgHgMacUnderFlow':dellNetFpEgHgMacUnderFlow,'dellNetFpEgTxErrPktCounter':dellNetFpEgTxErrPktCounter,'dellNetFpFlowControlDrops':dellNetFpFlowControlDrops,'dellNetFpIngressDropsBytes':dellNetFpIngressDropsBytes,'dellNetFpIngressFECBitErrors':dellNetFpIngressFECBitErrors,'dellNetFpIngressFECUncorrectedCodeWords':dellNetFpIngressFECUncorrectedCodeWords,'dellNetFpIngressPreFECBitErrorRatio':dellNetFpIngressPreFECBitErrorRatio,'dellNetFpIngressFCSErrorRatio':dellNetFpIngressFCSErrorRatio,'dellNetFpWredGreenDrops':dellNetFpWredGreenDrops,'dellNetFpWredYellowDrops':dellNetFpWredYellowDrops,'dellNetFpWredOutOfProfileDrops':dellNetFpWredOutOfProfileDrops,'dellNetFpPacketBufferTable':dellNetFpPacketBufferTable,'dellNetFpPacketBufferEntry':dellNetFpPacketBufferEntry,_M:dellNetFpPortPipe,'dellNetFpTotalPacketBuffer':dellNetFpTotalPacketBuffer,'dellNetFpCurrentAvailBuffer':dellNetFpCurrentAvailBuffer,'dellNetFpPacketBufferAlloc':dellNetFpPacketBufferAlloc,'dellNetFpStatsPerPortTable':dellNetFpStatsPerPortTable,'dellNetFpStatsPerPortEntry':dellNetFpStatsPerPortEntry,'dellNetFpCurrentUsagePerPort':dellNetFpCurrentUsagePerPort,'dellNetFpDefaultPacketBuffAlloc':dellNetFpDefaultPacketBuffAlloc,'dellNetFpMaxLimitPerPort':dellNetFpMaxLimitPerPort,'dellNetFpStatsPerCOSTable':dellNetFpStatsPerCOSTable,'dellNetFpStatsPerCOSEntry':dellNetFpStatsPerCOSEntry,_N:dellNetFpPerPortCOSNumber,'dellNetFpCurrentUsagePerCOS':dellNetFpCurrentUsagePerCOS,'dellNetFpDefaultPacketBuffAllocPerCOS':dellNetFpDefaultPacketBuffAllocPerCOS,'dellNetFpMaxLimitPerCOS':dellNetFpMaxLimitPerCOS,'dellNetFpHOLDropsPerCOS':dellNetFpHOLDropsPerCOS,'dellNetFpCpuDataPlaneCOSTable':dellNetFpCpuDataPlaneCOSTable,'dellNetFpCpuDataPlaneCOSEntry':dellNetFpCpuDataPlaneCOSEntry,_S:dellNetFpCOSIndex,'dellNetFpRxPktCOS':dellNetFpRxPktCOS,'dellNetFpTxPktCOS':dellNetFpTxPktCOS,'dellNetFpEgrQBuffSnapshotTable':dellNetFpEgrQBuffSnapshotTable,'dellNetFpEgrQBuffSnapshotEntry':dellNetFpEgrQBuffSnapshotEntry,'dellNetFpEgrQTotBuffCells':dellNetFpEgrQTotBuffCells,'dellNetFpIngPgBuffSnapshotTable':dellNetFpIngPgBuffSnapshotTable,'dellNetFpIngPgBuffSnapshotEntry':dellNetFpIngPgBuffSnapshotEntry,_P:dellNetFpPerPortPGIndex,'dellNetFpIngSharedCells':dellNetFpIngSharedCells,'dellNetFpIngHeadroomCells':dellNetFpIngHeadroomCells,'dellNetFpStatsPerPgTable':dellNetFpStatsPerPgTable,'dellNetFpStatsPerPgEntry':dellNetFpStatsPerPgEntry,'dellNetFpStatsPgLimitMinCells':dellNetFpStatsPgLimitMinCells,'dellNetFpStatsPgSharedCells':dellNetFpStatsPgSharedCells,'dellNetFpStatsPgSharedMode':dellNetFpStatsPgSharedMode,'dellNetFpStatsPgHdrmCells':dellNetFpStatsPgHdrmCells,'dellNetFpStatsPgCounterMinCells':dellNetFpStatsPgCounterMinCells,'dellNetFpStatsPgCounterSharedCells':dellNetFpStatsPgCounterSharedCells,'dellNetFpStatsPgCounterHdrmCells':dellNetFpStatsPgCounterHdrmCells,'dellNetPfcPerPrioTable':dellNetPfcPerPrioTable,'dellNetPfcPerPrioEntry':dellNetPfcPerPrioEntry,_L:dellNetPrioIndex,'dellNetPfcPerPrioRequests':dellNetPfcPerPrioRequests,'dellNetPfcPerPrioIndications':dellNetPfcPerPrioIndications,'dellNetFpCpuPartyBusPortStatsTable':dellNetFpCpuPartyBusPortStatsTable,'dellNetFpCpuPartyBusPortStatsEntry':dellNetFpCpuPartyBusPortStatsEntry,_X:dellNetFpStackPortIndex,'dellNetFpCpuPartyBusPortStatsOutOctets':dellNetFpCpuPartyBusPortStatsOutOctets,'dellNetFpCpuPartyBusPortStatsOutDropPkts':dellNetFpCpuPartyBusPortStatsOutDropPkts,'dellNetFpCpuPartyBusPortStatsOutCOS0Pkts':dellNetFpCpuPartyBusPortStatsOutCOS0Pkts,'dellNetFpCpuPartyBusPortStatsOutCOS1Pkts':dellNetFpCpuPartyBusPortStatsOutCOS1Pkts,'dellNetFpCpuPartyBusPortStatsOutCOS2Pkts':dellNetFpCpuPartyBusPortStatsOutCOS2Pkts,'dellNetFpCpuPartyBusPortStatsOutCOS3Pkts':dellNetFpCpuPartyBusPortStatsOutCOS3Pkts,'dellNetFpCpuPartyBusPortStatsOutCOS4Pkts':dellNetFpCpuPartyBusPortStatsOutCOS4Pkts,'dellNetFpCpuPartyBusPortStatsOutCOS5Pkts':dellNetFpCpuPartyBusPortStatsOutCOS5Pkts,'dellNetFpCpuPartyBusPortStatsOutUnicastPkts':dellNetFpCpuPartyBusPortStatsOutUnicastPkts,'dellNetFpCpuPartyBusPortStatsOutMulticastPkts':dellNetFpCpuPartyBusPortStatsOutMulticastPkts,'dellNetFpCpuPartyBusPortStatsOutBroadcastPkts':dellNetFpCpuPartyBusPortStatsOutBroadcastPkts,'dellNetFpCpuPartyBusPortStatsOutPausePkts':dellNetFpCpuPartyBusPortStatsOutPausePkts,'dellNetFpCpuPartyBusPortStatsOutCollisions':dellNetFpCpuPartyBusPortStatsOutCollisions,'dellNetFpCpuPartyBusPortStatsOutSingleCollisions':dellNetFpCpuPartyBusPortStatsOutSingleCollisions,'dellNetFpCpuPartyBusPortStatsOutMultiCollisions':dellNetFpCpuPartyBusPortStatsOutMultiCollisions,'dellNetFpCpuPartyBusPortStatsOutLateCollisions':dellNetFpCpuPartyBusPortStatsOutLateCollisions,'dellNetFpCpuPartyBusPortStatsOutExcessCollisions':dellNetFpCpuPartyBusPortStatsOutExcessCollisions,'dellNetFpCpuPartyBusPortStatsOutDeferred':dellNetFpCpuPartyBusPortStatsOutDeferred,'dellNetFpCpuPartyBusPortStatsOutDiscarded':dellNetFpCpuPartyBusPortStatsOutDiscarded,'dellNetFpCpuPartyBusPortStatsInOctets':dellNetFpCpuPartyBusPortStatsInOctets,'dellNetFpCpuPartyBusPortStatsInUndersizePkts':dellNetFpCpuPartyBusPortStatsInUndersizePkts,'dellNetFpCpuPartyBusPortStatsInOversizePkts':dellNetFpCpuPartyBusPortStatsInOversizePkts,'dellNetFpCpuPartyBusPortStatsInPausePkts':dellNetFpCpuPartyBusPortStatsInPausePkts,'dellNetFpCpuPartyBusPortStatsIn64OctetPkts':dellNetFpCpuPartyBusPortStatsIn64OctetPkts,'dellNetFpCpuPartyBusPortStatsIn65To127OctetPkts':dellNetFpCpuPartyBusPortStatsIn65To127OctetPkts,'dellNetFpCpuPartyBusPortStatsIn128To255OctetPkts':dellNetFpCpuPartyBusPortStatsIn128To255OctetPkts,'dellNetFpCpuPartyBusPortStatsIn256To511OctetPkts':dellNetFpCpuPartyBusPortStatsIn256To511OctetPkts,'dellNetFpCpuPartyBusPortStatsIn512To1023OctetPkts':dellNetFpCpuPartyBusPortStatsIn512To1023OctetPkts,'dellNetFpCpuPartyBusPortStatsIn1024ToMaxOctetPkts':dellNetFpCpuPartyBusPortStatsIn1024ToMaxOctetPkts,'dellNetFpCpuPartyBusPortStatsInJabbers':dellNetFpCpuPartyBusPortStatsInJabbers,'dellNetFpCpuPartyBusPortStatsInAlignErrors':dellNetFpCpuPartyBusPortStatsInAlignErrors,'dellNetFpCpuPartyBusPortStatsInFcsErrors':dellNetFpCpuPartyBusPortStatsInFcsErrors,'dellNetFpCpuPartyBusPortStatsInGoodOctets':dellNetFpCpuPartyBusPortStatsInGoodOctets,'dellNetFpCpuPartyBusPortStatsInDropPkts':dellNetFpCpuPartyBusPortStatsInDropPkts,'dellNetFpCpuPartyBusPortStatsInUnicastPkts':dellNetFpCpuPartyBusPortStatsInUnicastPkts,'dellNetFpCpuPartyBusPortStatsInMulticastPkts':dellNetFpCpuPartyBusPortStatsInMulticastPkts,'dellNetFpCpuPartyBusPortStatsInBroadcastPkts':dellNetFpCpuPartyBusPortStatsInBroadcastPkts,'dellNetFpCpuPartyBusPortStatsInSrcAddrChanges':dellNetFpCpuPartyBusPortStatsInSrcAddrChanges,'dellNetFpCpuPartyBusPortStatsInFragments':dellNetFpCpuPartyBusPortStatsInFragments,'dellNetFpCpuPartyBusPortStatsInJumboPkts':dellNetFpCpuPartyBusPortStatsInJumboPkts,'dellNetFpCpuPartyBusPortStatsInSymbolErrors':dellNetFpCpuPartyBusPortStatsInSymbolErrors,'dellNetFpCpuPartyBusPortStatsInInRangeErrors':dellNetFpCpuPartyBusPortStatsInInRangeErrors,'dellNetFpCpuPartyBusPortStatsInOutRangeErrors':dellNetFpCpuPartyBusPortStatsInOutRangeErrors,'dellNetFpDropsIfTable':dellNetFpDropsIfTable,'dellNetFpDropsIfEntry':dellNetFpDropsIfEntry,'dellNetFpIfIngressDrops':dellNetFpIfIngressDrops,'dellNetFpIfIngIBPCBPFullDrops':dellNetFpIfIngIBPCBPFullDrops,'dellNetFpIfIngPortSTPnotFwdDrops':dellNetFpIfIngPortSTPnotFwdDrops,'dellNetFpIfIngIPv4L3Discards':dellNetFpIfIngIPv4L3Discards,'dellNetFpIfIngPolicyDiscards':dellNetFpIfIngPolicyDiscards,'dellNetFpIfIngPacketsDroppedByFP':dellNetFpIfIngPacketsDroppedByFP,'dellNetFpIfIngL2L3Drops':dellNetFpIfIngL2L3Drops,'dellNetFpIfIngPortBitMapZeroDrops':dellNetFpIfIngPortBitMapZeroDrops,'dellNetFpIfIngRxVLANDrops':dellNetFpIfIngRxVLANDrops,'dellNetFpIfIngressFCSDrops':dellNetFpIfIngressFCSDrops,'dellNetFpIfIngressMTUExceeds':dellNetFpIfIngressMTUExceeds,'dellNetFpIfMMUHOLDrops':dellNetFpIfMMUHOLDrops,'dellNetFpIfMMUTxPurgeCellErr':dellNetFpIfMMUTxPurgeCellErr,'dellNetFpIfMMUAgedDrops':dellNetFpIfMMUAgedDrops,'dellNetFpIfEgressFCSDrops':dellNetFpIfEgressFCSDrops,'dellNetFpIfEgIPv4L3UCAgedDrops':dellNetFpIfEgIPv4L3UCAgedDrops,'dellNetFpIfEgTTLThresholdDrops':dellNetFpIfEgTTLThresholdDrops,'dellNetFpIfEgInvalidVLANCounterDrops':dellNetFpIfEgInvalidVLANCounterDrops,'dellNetFpIfEgL2MCDrops':dellNetFpIfEgL2MCDrops,'dellNetFpIfEgPktDropsOfAnyCondition':dellNetFpIfEgPktDropsOfAnyCondition,'dellNetFpIfEgHgMacUnderFlow':dellNetFpIfEgHgMacUnderFlow,'dellNetFpIfEgTxErrPktCounter':dellNetFpIfEgTxErrPktCounter,'dellNetFpStatsPerIfTable':dellNetFpStatsPerIfTable,'dellNetFpStatsPerIfEntry':dellNetFpStatsPerIfEntry,'dellNetFpIfCurrentUsagePerPort':dellNetFpIfCurrentUsagePerPort,'dellNetFpIfDefaultPacketBuffAlloc':dellNetFpIfDefaultPacketBuffAlloc,'dellNetFpIfMaxLimitPerPort':dellNetFpIfMaxLimitPerPort,'dellNetFpStatsPerIfCOSTable':dellNetFpStatsPerIfCOSTable,'dellNetFpStatsPerIfCOSEntry':dellNetFpStatsPerIfCOSEntry,_Q:dellNetFpIfPerCOSNumber,'dellNetFpIfCurrentUsagePerCOS':dellNetFpIfCurrentUsagePerCOS,'dellNetFpIfDefaultPacketBuffAllocPerCOS':dellNetFpIfDefaultPacketBuffAllocPerCOS,'dellNetFpIfMaxLimitPerCOS':dellNetFpIfMaxLimitPerCOS,'dellNetFpIfHOLDropsPerCOS':dellNetFpIfHOLDropsPerCOS,'dellNetFpEgrQBuffSnapshotIfTable':dellNetFpEgrQBuffSnapshotIfTable,'dellNetFpEgrQBuffSnapshotIfEntry':dellNetFpEgrQBuffSnapshotIfEntry,'dellNetFpIfEgrQTotBuffCells':dellNetFpIfEgrQTotBuffCells,'dellNetFpIngPgBuffSnapshotIfTable':dellNetFpIngPgBuffSnapshotIfTable,'dellNetFpIngPgBuffSnapshotIfEntry':dellNetFpIngPgBuffSnapshotIfEntry,_R:dellNetFpIfPerPGIndex,'dellNetFpIfIngSharedCells':dellNetFpIfIngSharedCells,'dellNetFpIfIngHeadroomCells':dellNetFpIfIngHeadroomCells,'dellNetFpStatsPerPgIfTable':dellNetFpStatsPerPgIfTable,'dellNetFpStatsPerPgIfEntry':dellNetFpStatsPerPgIfEntry,'dellNetFpIfStatsPgLimitMinCells':dellNetFpIfStatsPgLimitMinCells,'dellNetFpIfStatsPgSharedCells':dellNetFpIfStatsPgSharedCells,'dellNetFpIfStatsPgSharedMode':dellNetFpIfStatsPgSharedMode,'dellNetFpIfStatsPgHdrmCells':dellNetFpIfStatsPgHdrmCells,'dellNetFpIfStatsPgCounterMinCells':dellNetFpIfStatsPgCounterMinCells,'dellNetFpIfStatsPgCounterSharedCells':dellNetFpIfStatsPgCounterSharedCells,'dellNetFpIfStatsPgCounterHdrmCells':dellNetFpIfStatsPgCounterHdrmCells,'dellNetPfcPerPrioIfTable':dellNetPfcPerPrioIfTable,'dellNetPfcPerPrioIfEntry':dellNetPfcPerPrioIfEntry,_Y:dellNetIfPrioIndex,'dellNetIfPfcPerPrioRequests':dellNetIfPfcPerPrioRequests,'dellNetIfPfcPerPrioIndications':dellNetIfPfcPerPrioIndications,'dellNetFpEgrQIfCounterTable':dellNetFpEgrQIfCounterTable,'dellNetFpEgrQIfCounterEntry':dellNetFpEgrQIfCounterEntry,_Z:dellNetFpEgrQComType,'dellNetFpEgrQTxPackets':dellNetFpEgrQTxPackets,'dellNetFpEgrQTxBytes':dellNetFpEgrQTxBytes,'dellNetFpEgrQDroppedPackets':dellNetFpEgrQDroppedPackets,'dellNetFpEgrQDroppedBytes':dellNetFpEgrQDroppedBytes,'dellNetFpEgrQTxPacketsRate':dellNetFpEgrQTxPacketsRate,'dellNetFpEgrQTxBytesRate':dellNetFpEgrQTxBytesRate,'dellNetFpEgrQDroppedPacketsRate':dellNetFpEgrQDroppedPacketsRate,'dellNetFpEgrQDroppedBytesRate':dellNetFpEgrQDroppedBytesRate,'dellNetFpPfcStormControl':dellNetFpPfcStormControl,'dellNetFpPfcStormControlStatus':dellNetFpPfcStormControlStatus,'dellNetFpPfcStormControlStatusTable':dellNetFpPfcStormControlStatusTable,'dellNetFpPfcStormControlStatusEntry':dellNetFpPfcStormControlStatusEntry,'dellNetFpPfcStormControlQueueState':dellNetFpPfcStormControlQueueState,'dellNetFpPfcStormControlDurationInDiscardState':dellNetFpPfcStormControlDurationInDiscardState,'dellNetFpPfcStormControlDroppedPacketsIngress':dellNetFpPfcStormControlDroppedPacketsIngress,'dellNetFpPfcStormControlDroppedPacketsEgress':dellNetFpPfcStormControlDroppedPacketsEgress,'dellNetFpPfcStormControlCumulativeDroppedPacketsIngress':dellNetFpPfcStormControlCumulativeDroppedPacketsIngress,'dellNetFpPfcStormControlCumulativeDroppedPacketsEgress':dellNetFpPfcStormControlCumulativeDroppedPacketsEgress,'dellNetFpPfcStormControlStatistics':dellNetFpPfcStormControlStatistics,'dellNetFpPfcStormControlStatisticsTable':dellNetFpPfcStormControlStatisticsTable,'dellNetFpPfcStormControlStatisticsEntry':dellNetFpPfcStormControlStatisticsEntry,'dellNetFpPfcStormControlDiscardStateCount':dellNetFpPfcStormControlDiscardStateCount,'dellNetFpPfcStormControlDiscardStateForcedClearCount':dellNetFpPfcStormControlDiscardStateForcedClearCount,'dellNetFpPfcStormControlDiscardStateNorxPfcClearCount':dellNetFpPfcStormControlDiscardStateNorxPfcClearCount,'dellNetFpPfcL2DlfDropCounterTable':dellNetFpPfcL2DlfDropCounterTable,'dellNetFpPfcL2DlfDropCounterEntry':dellNetFpPfcL2DlfDropCounterEntry,'dellNetFpPfcL2DlfDropCounters':dellNetFpPfcL2DlfDropCounters,'dellNetFpServicePoolBufferSizeTable':dellNetFpServicePoolBufferSizeTable,'dellNetFpServicePoolBufferSizeEntry':dellNetFpServicePoolBufferSizeEntry,_a:dellNetFpXPENumber,'dellNetFpLossyServicePoolConfiguredBuffSize':dellNetFpLossyServicePoolConfiguredBuffSize,'dellNetFpLossyServicePoolUsedBuffSize':dellNetFpLossyServicePoolUsedBuffSize,'dellNetFpLosslessServicePoolConfiguredBuffSize':dellNetFpLosslessServicePoolConfiguredBuffSize,'dellNetFpLosslessServicePoolUsedBuffSize':dellNetFpLosslessServicePoolUsedBuffSize,'dellNetFpEcnPacketsTable':dellNetFpEcnPacketsTable,'dellNetFpEcnPacketsEntry':dellNetFpEcnPacketsEntry,'dellNetFpEcnMarkedTxPkts':dellNetFpEcnMarkedTxPkts,'dellNetFpTotalDropPktsOnEcnEnabledQueues':dellNetFpTotalDropPktsOnEcnEnabledQueues})