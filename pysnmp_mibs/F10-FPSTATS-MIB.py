_W='fpEgrQComType'
_V='ifPrioIndex'
_U='Indications'
_T='Requests'
_S='prioIndex'
_R='dynamic'
_Q='static'
_P='fpCOSIndex'
_O='fpPortPipe'
_N='fpIfPerPGIndex'
_M='fpIfPerCOSNumber'
_L='fpPerPortPGIndex'
_K='fpPerPortCOSNumber'
_J='fpStackPortIndex'
_I='ifIndex'
_H='IF-MIB'
_G='not-accessible'
_F='Integer32'
_E='fpStackUnitIndex'
_D='deprecated'
_C='F10-FPSTATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f10Mgmt,=mibBuilder.importSymbols('FORCE10-SMI','f10Mgmt')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
f10FpStatsMib=ModuleIdentity((1,3,6,1,4,1,6027,3,16))
if mibBuilder.loadTexts:f10FpStatsMib.setRevisions(('2013-02-20 12:00','2011-03-22 12:48'))
class ComType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_F10FpStatsObject_ObjectIdentity=ObjectIdentity
f10FpStatsObject=_F10FpStatsObject_ObjectIdentity((1,3,6,1,4,1,6027,3,16,1))
_FpStatsObjects_ObjectIdentity=ObjectIdentity
fpStatsObjects=_FpStatsObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,16,1,1))
_FpCpuDataPlaneTable_Object=MibTable
fpCpuDataPlaneTable=_FpCpuDataPlaneTable_Object((1,3,6,1,4,1,6027,3,16,1,1,1))
if mibBuilder.loadTexts:fpCpuDataPlaneTable.setStatus(_A)
_FpCpuDataPlaneStatsEntry_Object=MibTableRow
fpCpuDataPlaneStatsEntry=_FpCpuDataPlaneStatsEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1))
fpCpuDataPlaneStatsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:fpCpuDataPlaneStatsEntry.setStatus(_A)
class _FpStackUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_FpStackUnitIndex_Type.__name__=_F
_FpStackUnitIndex_Object=MibTableColumn
fpStackUnitIndex=_FpStackUnitIndex_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,1),_FpStackUnitIndex_Type())
fpStackUnitIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fpStackUnitIndex.setStatus(_A)
_FpRxHandle_Type=Integer32
_FpRxHandle_Object=MibTableColumn
fpRxHandle=_FpRxHandle_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,2),_FpRxHandle_Type())
fpRxHandle.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxHandle.setStatus(_A)
_FpNoMhdr_Type=Integer32
_FpNoMhdr_Object=MibTableColumn
fpNoMhdr=_FpNoMhdr_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,3),_FpNoMhdr_Type())
fpNoMhdr.setMaxAccess(_B)
if mibBuilder.loadTexts:fpNoMhdr.setStatus(_A)
_FpNoMBuf_Type=Integer32
_FpNoMBuf_Object=MibTableColumn
fpNoMBuf=_FpNoMBuf_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,4),_FpNoMBuf_Type())
fpNoMBuf.setMaxAccess(_B)
if mibBuilder.loadTexts:fpNoMBuf.setStatus(_A)
_FpNoClus_Type=Integer32
_FpNoClus_Object=MibTableColumn
fpNoClus=_FpNoClus_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,5),_FpNoClus_Type())
fpNoClus.setMaxAccess(_B)
if mibBuilder.loadTexts:fpNoClus.setStatus(_A)
_FpRecvd_Type=Integer32
_FpRecvd_Object=MibTableColumn
fpRecvd=_FpRecvd_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,6),_FpRecvd_Type())
fpRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRecvd.setStatus(_A)
_FpDropped_Type=Integer32
_FpDropped_Object=MibTableColumn
fpDropped=_FpDropped_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,7),_FpDropped_Type())
fpDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fpDropped.setStatus(_A)
_FpRecvToNet_Type=Integer32
_FpRecvToNet_Object=MibTableColumn
fpRecvToNet=_FpRecvToNet_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,8),_FpRecvToNet_Type())
fpRecvToNet.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRecvToNet.setStatus(_A)
_FpRxError_Type=Integer32
_FpRxError_Object=MibTableColumn
fpRxError=_FpRxError_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,9),_FpRxError_Type())
fpRxError.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxError.setStatus(_A)
_FpRxDatapathError_Type=Integer32
_FpRxDatapathError_Object=MibTableColumn
fpRxDatapathError=_FpRxDatapathError_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,10),_FpRxDatapathError_Type())
fpRxDatapathError.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxDatapathError.setStatus(_A)
_FpRxPktCOS0_Type=Integer32
_FpRxPktCOS0_Object=MibTableColumn
fpRxPktCOS0=_FpRxPktCOS0_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,11),_FpRxPktCOS0_Type())
fpRxPktCOS0.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktCOS0.setStatus(_D)
_FpRxPktCOS1_Type=Integer32
_FpRxPktCOS1_Object=MibTableColumn
fpRxPktCOS1=_FpRxPktCOS1_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,12),_FpRxPktCOS1_Type())
fpRxPktCOS1.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktCOS1.setStatus(_D)
_FpRxPktCOS2_Type=Integer32
_FpRxPktCOS2_Object=MibTableColumn
fpRxPktCOS2=_FpRxPktCOS2_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,13),_FpRxPktCOS2_Type())
fpRxPktCOS2.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktCOS2.setStatus(_D)
_FpRxPktCOS3_Type=Integer32
_FpRxPktCOS3_Object=MibTableColumn
fpRxPktCOS3=_FpRxPktCOS3_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,14),_FpRxPktCOS3_Type())
fpRxPktCOS3.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktCOS3.setStatus(_D)
_FpRxPktCOS4_Type=Integer32
_FpRxPktCOS4_Object=MibTableColumn
fpRxPktCOS4=_FpRxPktCOS4_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,15),_FpRxPktCOS4_Type())
fpRxPktCOS4.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktCOS4.setStatus(_D)
_FpRxPktCOS5_Type=Integer32
_FpRxPktCOS5_Object=MibTableColumn
fpRxPktCOS5=_FpRxPktCOS5_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,16),_FpRxPktCOS5_Type())
fpRxPktCOS5.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktCOS5.setStatus(_D)
_FpRxPktCOS6_Type=Integer32
_FpRxPktCOS6_Object=MibTableColumn
fpRxPktCOS6=_FpRxPktCOS6_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,17),_FpRxPktCOS6_Type())
fpRxPktCOS6.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktCOS6.setStatus(_D)
_FpRxPktCOS7_Type=Integer32
_FpRxPktCOS7_Object=MibTableColumn
fpRxPktCOS7=_FpRxPktCOS7_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,18),_FpRxPktCOS7_Type())
fpRxPktCOS7.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktCOS7.setStatus(_D)
_FpRxPktUnit0_Type=Integer32
_FpRxPktUnit0_Object=MibTableColumn
fpRxPktUnit0=_FpRxPktUnit0_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,19),_FpRxPktUnit0_Type())
fpRxPktUnit0.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktUnit0.setStatus(_A)
_FpRxPktUnit1_Type=Integer32
_FpRxPktUnit1_Object=MibTableColumn
fpRxPktUnit1=_FpRxPktUnit1_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,20),_FpRxPktUnit1_Type())
fpRxPktUnit1.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktUnit1.setStatus(_A)
_FpRxPktUnit2_Type=Integer32
_FpRxPktUnit2_Object=MibTableColumn
fpRxPktUnit2=_FpRxPktUnit2_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,21),_FpRxPktUnit2_Type())
fpRxPktUnit2.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktUnit2.setStatus(_A)
_FpRxPktUnit3_Type=Integer32
_FpRxPktUnit3_Object=MibTableColumn
fpRxPktUnit3=_FpRxPktUnit3_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,22),_FpRxPktUnit3_Type())
fpRxPktUnit3.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktUnit3.setStatus(_A)
_FpTransmitted_Type=Integer32
_FpTransmitted_Object=MibTableColumn
fpTransmitted=_FpTransmitted_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,23),_FpTransmitted_Type())
fpTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTransmitted.setStatus(_A)
_FpTxRequested_Type=Integer32
_FpTxRequested_Object=MibTableColumn
fpTxRequested=_FpTxRequested_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,24),_FpTxRequested_Type())
fpTxRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxRequested.setStatus(_A)
_FpNoTxDesc_Type=Integer32
_FpNoTxDesc_Object=MibTableColumn
fpNoTxDesc=_FpNoTxDesc_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,25),_FpNoTxDesc_Type())
fpNoTxDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:fpNoTxDesc.setStatus(_A)
_FpTxError_Type=Integer32
_FpTxError_Object=MibTableColumn
fpTxError=_FpTxError_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,26),_FpTxError_Type())
fpTxError.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxError.setStatus(_A)
_FpTxReqTooLarge_Type=Integer32
_FpTxReqTooLarge_Object=MibTableColumn
fpTxReqTooLarge=_FpTxReqTooLarge_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,27),_FpTxReqTooLarge_Type())
fpTxReqTooLarge.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxReqTooLarge.setStatus(_A)
_FpTxInternalError_Type=Integer32
_FpTxInternalError_Object=MibTableColumn
fpTxInternalError=_FpTxInternalError_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,28),_FpTxInternalError_Type())
fpTxInternalError.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxInternalError.setStatus(_A)
_FpTxDatapathErr_Type=Integer32
_FpTxDatapathErr_Object=MibTableColumn
fpTxDatapathErr=_FpTxDatapathErr_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,29),_FpTxDatapathErr_Type())
fpTxDatapathErr.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxDatapathErr.setStatus(_A)
_FpTxPktCOS0_Type=Integer32
_FpTxPktCOS0_Object=MibTableColumn
fpTxPktCOS0=_FpTxPktCOS0_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,30),_FpTxPktCOS0_Type())
fpTxPktCOS0.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktCOS0.setStatus(_D)
_FpTxPktCOS1_Type=Integer32
_FpTxPktCOS1_Object=MibTableColumn
fpTxPktCOS1=_FpTxPktCOS1_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,31),_FpTxPktCOS1_Type())
fpTxPktCOS1.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktCOS1.setStatus(_D)
_FpTxPktCOS2_Type=Integer32
_FpTxPktCOS2_Object=MibTableColumn
fpTxPktCOS2=_FpTxPktCOS2_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,32),_FpTxPktCOS2_Type())
fpTxPktCOS2.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktCOS2.setStatus(_D)
_FpTxPktCOS3_Type=Integer32
_FpTxPktCOS3_Object=MibTableColumn
fpTxPktCOS3=_FpTxPktCOS3_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,33),_FpTxPktCOS3_Type())
fpTxPktCOS3.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktCOS3.setStatus(_D)
_FpTxPktCOS4_Type=Integer32
_FpTxPktCOS4_Object=MibTableColumn
fpTxPktCOS4=_FpTxPktCOS4_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,34),_FpTxPktCOS4_Type())
fpTxPktCOS4.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktCOS4.setStatus(_D)
_FpTxPktCOS5_Type=Integer32
_FpTxPktCOS5_Object=MibTableColumn
fpTxPktCOS5=_FpTxPktCOS5_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,35),_FpTxPktCOS5_Type())
fpTxPktCOS5.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktCOS5.setStatus(_D)
_FpTxPktCOS6_Type=Integer32
_FpTxPktCOS6_Object=MibTableColumn
fpTxPktCOS6=_FpTxPktCOS6_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,36),_FpTxPktCOS6_Type())
fpTxPktCOS6.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktCOS6.setStatus(_D)
_FpTxPktCOS7_Type=Integer32
_FpTxPktCOS7_Object=MibTableColumn
fpTxPktCOS7=_FpTxPktCOS7_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,37),_FpTxPktCOS7_Type())
fpTxPktCOS7.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktCOS7.setStatus(_D)
_FpTxPktUnit0_Type=Integer32
_FpTxPktUnit0_Object=MibTableColumn
fpTxPktUnit0=_FpTxPktUnit0_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,38),_FpTxPktUnit0_Type())
fpTxPktUnit0.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktUnit0.setStatus(_A)
_FpTxPktUnit1_Type=Integer32
_FpTxPktUnit1_Object=MibTableColumn
fpTxPktUnit1=_FpTxPktUnit1_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,39),_FpTxPktUnit1_Type())
fpTxPktUnit1.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktUnit1.setStatus(_A)
_FpTxPktUnit2_Type=Integer32
_FpTxPktUnit2_Object=MibTableColumn
fpTxPktUnit2=_FpTxPktUnit2_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,40),_FpTxPktUnit2_Type())
fpTxPktUnit2.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktUnit2.setStatus(_A)
_FpTxPktUnit3_Type=Integer32
_FpTxPktUnit3_Object=MibTableColumn
fpTxPktUnit3=_FpTxPktUnit3_Object((1,3,6,1,4,1,6027,3,16,1,1,1,1,41),_FpTxPktUnit3_Type())
fpTxPktUnit3.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktUnit3.setStatus(_A)
_FpCpuPartyBusTable_Object=MibTable
fpCpuPartyBusTable=_FpCpuPartyBusTable_Object((1,3,6,1,4,1,6027,3,16,1,1,2))
if mibBuilder.loadTexts:fpCpuPartyBusTable.setStatus(_A)
_FpCpuPartyBusStatsEntry_Object=MibTableRow
fpCpuPartyBusStatsEntry=_FpCpuPartyBusStatsEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,2,1))
fpCpuPartyBusStatsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:fpCpuPartyBusStatsEntry.setStatus(_A)
_FpPartyBusInputPackets_Type=Counter32
_FpPartyBusInputPackets_Object=MibTableColumn
fpPartyBusInputPackets=_FpPartyBusInputPackets_Object((1,3,6,1,4,1,6027,3,16,1,1,2,1,1),_FpPartyBusInputPackets_Type())
fpPartyBusInputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fpPartyBusInputPackets.setStatus(_A)
_FpPartyBusInputBytes_Type=Counter32
_FpPartyBusInputBytes_Object=MibTableColumn
fpPartyBusInputBytes=_FpPartyBusInputBytes_Object((1,3,6,1,4,1,6027,3,16,1,1,2,1,2),_FpPartyBusInputBytes_Type())
fpPartyBusInputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fpPartyBusInputBytes.setStatus(_A)
_FpPartyBusInputDropped_Type=Counter32
_FpPartyBusInputDropped_Object=MibTableColumn
fpPartyBusInputDropped=_FpPartyBusInputDropped_Object((1,3,6,1,4,1,6027,3,16,1,1,2,1,3),_FpPartyBusInputDropped_Type())
fpPartyBusInputDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fpPartyBusInputDropped.setStatus(_A)
_FpPartyBusInputError_Type=Counter32
_FpPartyBusInputError_Object=MibTableColumn
fpPartyBusInputError=_FpPartyBusInputError_Object((1,3,6,1,4,1,6027,3,16,1,1,2,1,4),_FpPartyBusInputError_Type())
fpPartyBusInputError.setMaxAccess(_B)
if mibBuilder.loadTexts:fpPartyBusInputError.setStatus(_A)
_FpPartyBusOutputPackets_Type=Counter32
_FpPartyBusOutputPackets_Object=MibTableColumn
fpPartyBusOutputPackets=_FpPartyBusOutputPackets_Object((1,3,6,1,4,1,6027,3,16,1,1,2,1,5),_FpPartyBusOutputPackets_Type())
fpPartyBusOutputPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fpPartyBusOutputPackets.setStatus(_A)
_FpPartyBusOutputBytes_Type=Counter32
_FpPartyBusOutputBytes_Object=MibTableColumn
fpPartyBusOutputBytes=_FpPartyBusOutputBytes_Object((1,3,6,1,4,1,6027,3,16,1,1,2,1,6),_FpPartyBusOutputBytes_Type())
fpPartyBusOutputBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fpPartyBusOutputBytes.setStatus(_A)
_FpPartyBusOutputError_Type=Counter32
_FpPartyBusOutputError_Object=MibTableColumn
fpPartyBusOutputError=_FpPartyBusOutputError_Object((1,3,6,1,4,1,6027,3,16,1,1,2,1,7),_FpPartyBusOutputError_Type())
fpPartyBusOutputError.setMaxAccess(_B)
if mibBuilder.loadTexts:fpPartyBusOutputError.setStatus(_A)
_FpDropsTable_Object=MibTable
fpDropsTable=_FpDropsTable_Object((1,3,6,1,4,1,6027,3,16,1,1,3))
if mibBuilder.loadTexts:fpDropsTable.setStatus(_A)
_FpDropsEntry_Object=MibTableRow
fpDropsEntry=_FpDropsEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1))
fpDropsEntry.setIndexNames((0,_C,_E),(0,_C,_J))
if mibBuilder.loadTexts:fpDropsEntry.setStatus(_A)
class _FpStackPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,192))
_FpStackPortIndex_Type.__name__=_F
_FpStackPortIndex_Object=MibTableColumn
fpStackPortIndex=_FpStackPortIndex_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,1),_FpStackPortIndex_Type())
fpStackPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fpStackPortIndex.setStatus(_A)
_FpIngressDrops_Type=Counter64
_FpIngressDrops_Object=MibTableColumn
fpIngressDrops=_FpIngressDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,2),_FpIngressDrops_Type())
fpIngressDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngressDrops.setStatus(_A)
_FpIngIBPCBPFullDrops_Type=Counter64
_FpIngIBPCBPFullDrops_Object=MibTableColumn
fpIngIBPCBPFullDrops=_FpIngIBPCBPFullDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,3),_FpIngIBPCBPFullDrops_Type())
fpIngIBPCBPFullDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngIBPCBPFullDrops.setStatus(_A)
_FpIngPortSTPnotFwdDrops_Type=Counter64
_FpIngPortSTPnotFwdDrops_Object=MibTableColumn
fpIngPortSTPnotFwdDrops=_FpIngPortSTPnotFwdDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,4),_FpIngPortSTPnotFwdDrops_Type())
fpIngPortSTPnotFwdDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngPortSTPnotFwdDrops.setStatus(_A)
_FpIngIPv4L3Discards_Type=Counter64
_FpIngIPv4L3Discards_Object=MibTableColumn
fpIngIPv4L3Discards=_FpIngIPv4L3Discards_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,5),_FpIngIPv4L3Discards_Type())
fpIngIPv4L3Discards.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngIPv4L3Discards.setStatus(_A)
_FpIngPolicyDiscards_Type=Counter64
_FpIngPolicyDiscards_Object=MibTableColumn
fpIngPolicyDiscards=_FpIngPolicyDiscards_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,6),_FpIngPolicyDiscards_Type())
fpIngPolicyDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngPolicyDiscards.setStatus(_A)
_FpIngPacketsDroppedByFP_Type=Counter64
_FpIngPacketsDroppedByFP_Object=MibTableColumn
fpIngPacketsDroppedByFP=_FpIngPacketsDroppedByFP_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,7),_FpIngPacketsDroppedByFP_Type())
fpIngPacketsDroppedByFP.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngPacketsDroppedByFP.setStatus(_A)
_FpIngL2L3Drops_Type=Counter64
_FpIngL2L3Drops_Object=MibTableColumn
fpIngL2L3Drops=_FpIngL2L3Drops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,8),_FpIngL2L3Drops_Type())
fpIngL2L3Drops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngL2L3Drops.setStatus(_A)
_FpIngPortBitMapZeroDrops_Type=Counter64
_FpIngPortBitMapZeroDrops_Object=MibTableColumn
fpIngPortBitMapZeroDrops=_FpIngPortBitMapZeroDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,9),_FpIngPortBitMapZeroDrops_Type())
fpIngPortBitMapZeroDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngPortBitMapZeroDrops.setStatus(_A)
_FpIngRxVLANDrops_Type=Counter64
_FpIngRxVLANDrops_Object=MibTableColumn
fpIngRxVLANDrops=_FpIngRxVLANDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,10),_FpIngRxVLANDrops_Type())
fpIngRxVLANDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngRxVLANDrops.setStatus(_A)
_FpIngressFCSDrops_Type=Counter64
_FpIngressFCSDrops_Object=MibTableColumn
fpIngressFCSDrops=_FpIngressFCSDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,11),_FpIngressFCSDrops_Type())
fpIngressFCSDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngressFCSDrops.setStatus(_A)
_FpIngressMTUExceeds_Type=Counter64
_FpIngressMTUExceeds_Object=MibTableColumn
fpIngressMTUExceeds=_FpIngressMTUExceeds_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,12),_FpIngressMTUExceeds_Type())
fpIngressMTUExceeds.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngressMTUExceeds.setStatus(_A)
_FpMMUHOLDrops_Type=Counter64
_FpMMUHOLDrops_Object=MibTableColumn
fpMMUHOLDrops=_FpMMUHOLDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,13),_FpMMUHOLDrops_Type())
fpMMUHOLDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpMMUHOLDrops.setStatus(_A)
_FpMMUTxPurgeCellErr_Type=Counter64
_FpMMUTxPurgeCellErr_Object=MibTableColumn
fpMMUTxPurgeCellErr=_FpMMUTxPurgeCellErr_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,14),_FpMMUTxPurgeCellErr_Type())
fpMMUTxPurgeCellErr.setMaxAccess(_B)
if mibBuilder.loadTexts:fpMMUTxPurgeCellErr.setStatus(_A)
_FpMMUAgedDrops_Type=Counter64
_FpMMUAgedDrops_Object=MibTableColumn
fpMMUAgedDrops=_FpMMUAgedDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,15),_FpMMUAgedDrops_Type())
fpMMUAgedDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpMMUAgedDrops.setStatus(_A)
_FpEgressFCSDrops_Type=Counter64
_FpEgressFCSDrops_Object=MibTableColumn
fpEgressFCSDrops=_FpEgressFCSDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,16),_FpEgressFCSDrops_Type())
fpEgressFCSDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgressFCSDrops.setStatus(_A)
_FpEgIPv4L3UCAgedDrops_Type=Counter64
_FpEgIPv4L3UCAgedDrops_Object=MibTableColumn
fpEgIPv4L3UCAgedDrops=_FpEgIPv4L3UCAgedDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,17),_FpEgIPv4L3UCAgedDrops_Type())
fpEgIPv4L3UCAgedDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgIPv4L3UCAgedDrops.setStatus(_A)
_FpEgTTLThresholdDrops_Type=Counter64
_FpEgTTLThresholdDrops_Object=MibTableColumn
fpEgTTLThresholdDrops=_FpEgTTLThresholdDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,18),_FpEgTTLThresholdDrops_Type())
fpEgTTLThresholdDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgTTLThresholdDrops.setStatus(_A)
_FpEgInvalidVLANCounterDrops_Type=Counter64
_FpEgInvalidVLANCounterDrops_Object=MibTableColumn
fpEgInvalidVLANCounterDrops=_FpEgInvalidVLANCounterDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,19),_FpEgInvalidVLANCounterDrops_Type())
fpEgInvalidVLANCounterDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgInvalidVLANCounterDrops.setStatus(_A)
_FpEgL2MCDrops_Type=Counter64
_FpEgL2MCDrops_Object=MibTableColumn
fpEgL2MCDrops=_FpEgL2MCDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,20),_FpEgL2MCDrops_Type())
fpEgL2MCDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgL2MCDrops.setStatus(_A)
_FpEgPktDropsOfAnyCondition_Type=Counter64
_FpEgPktDropsOfAnyCondition_Object=MibTableColumn
fpEgPktDropsOfAnyCondition=_FpEgPktDropsOfAnyCondition_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,21),_FpEgPktDropsOfAnyCondition_Type())
fpEgPktDropsOfAnyCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgPktDropsOfAnyCondition.setStatus(_A)
_FpEgHgMacUnderFlow_Type=Counter64
_FpEgHgMacUnderFlow_Object=MibTableColumn
fpEgHgMacUnderFlow=_FpEgHgMacUnderFlow_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,22),_FpEgHgMacUnderFlow_Type())
fpEgHgMacUnderFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgHgMacUnderFlow.setStatus(_A)
_FpEgTxErrPktCounter_Type=Counter64
_FpEgTxErrPktCounter_Object=MibTableColumn
fpEgTxErrPktCounter=_FpEgTxErrPktCounter_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,23),_FpEgTxErrPktCounter_Type())
fpEgTxErrPktCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgTxErrPktCounter.setStatus(_A)
_FpFlowControlDrops_Type=Counter64
_FpFlowControlDrops_Object=MibTableColumn
fpFlowControlDrops=_FpFlowControlDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,3,1,24),_FpFlowControlDrops_Type())
fpFlowControlDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpFlowControlDrops.setStatus(_A)
_FpPacketBufferTable_Object=MibTable
fpPacketBufferTable=_FpPacketBufferTable_Object((1,3,6,1,4,1,6027,3,16,1,1,4))
if mibBuilder.loadTexts:fpPacketBufferTable.setStatus(_A)
_FpPacketBufferEntry_Object=MibTableRow
fpPacketBufferEntry=_FpPacketBufferEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,4,1))
fpPacketBufferEntry.setIndexNames((0,_C,_E),(0,_C,_O))
if mibBuilder.loadTexts:fpPacketBufferEntry.setStatus(_A)
class _FpPortPipe_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_FpPortPipe_Type.__name__=_F
_FpPortPipe_Object=MibTableColumn
fpPortPipe=_FpPortPipe_Object((1,3,6,1,4,1,6027,3,16,1,1,4,1,1),_FpPortPipe_Type())
fpPortPipe.setMaxAccess(_G)
if mibBuilder.loadTexts:fpPortPipe.setStatus(_A)
_FpTotalPacketBuffer_Type=Counter32
_FpTotalPacketBuffer_Object=MibTableColumn
fpTotalPacketBuffer=_FpTotalPacketBuffer_Object((1,3,6,1,4,1,6027,3,16,1,1,4,1,2),_FpTotalPacketBuffer_Type())
fpTotalPacketBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTotalPacketBuffer.setStatus(_A)
_FpCurrentAvailBuffer_Type=Counter32
_FpCurrentAvailBuffer_Object=MibTableColumn
fpCurrentAvailBuffer=_FpCurrentAvailBuffer_Object((1,3,6,1,4,1,6027,3,16,1,1,4,1,3),_FpCurrentAvailBuffer_Type())
fpCurrentAvailBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCurrentAvailBuffer.setStatus(_A)
_FpPacketBufferAlloc_Type=Counter32
_FpPacketBufferAlloc_Object=MibTableColumn
fpPacketBufferAlloc=_FpPacketBufferAlloc_Object((1,3,6,1,4,1,6027,3,16,1,1,4,1,4),_FpPacketBufferAlloc_Type())
fpPacketBufferAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:fpPacketBufferAlloc.setStatus(_A)
_FpStatsPerPortTable_Object=MibTable
fpStatsPerPortTable=_FpStatsPerPortTable_Object((1,3,6,1,4,1,6027,3,16,1,1,5))
if mibBuilder.loadTexts:fpStatsPerPortTable.setStatus(_A)
_FpStatsPerPortEntry_Object=MibTableRow
fpStatsPerPortEntry=_FpStatsPerPortEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,5,1))
fpStatsPerPortEntry.setIndexNames((0,_C,_E),(0,_C,_J))
if mibBuilder.loadTexts:fpStatsPerPortEntry.setStatus(_A)
_FpCurrentUsagePerPort_Type=Counter32
_FpCurrentUsagePerPort_Object=MibTableColumn
fpCurrentUsagePerPort=_FpCurrentUsagePerPort_Object((1,3,6,1,4,1,6027,3,16,1,1,5,1,1),_FpCurrentUsagePerPort_Type())
fpCurrentUsagePerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCurrentUsagePerPort.setStatus(_A)
_FpDefaultPacketBuffAlloc_Type=Counter32
_FpDefaultPacketBuffAlloc_Object=MibTableColumn
fpDefaultPacketBuffAlloc=_FpDefaultPacketBuffAlloc_Object((1,3,6,1,4,1,6027,3,16,1,1,5,1,2),_FpDefaultPacketBuffAlloc_Type())
fpDefaultPacketBuffAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:fpDefaultPacketBuffAlloc.setStatus(_A)
_FpMaxLimitPerPort_Type=Counter32
_FpMaxLimitPerPort_Object=MibTableColumn
fpMaxLimitPerPort=_FpMaxLimitPerPort_Object((1,3,6,1,4,1,6027,3,16,1,1,5,1,3),_FpMaxLimitPerPort_Type())
fpMaxLimitPerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fpMaxLimitPerPort.setStatus(_A)
_FpStatsPerCOSTable_Object=MibTable
fpStatsPerCOSTable=_FpStatsPerCOSTable_Object((1,3,6,1,4,1,6027,3,16,1,1,6))
if mibBuilder.loadTexts:fpStatsPerCOSTable.setStatus(_A)
_FpStatsPerCOSEntry_Object=MibTableRow
fpStatsPerCOSEntry=_FpStatsPerCOSEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,6,1))
fpStatsPerCOSEntry.setIndexNames((0,_C,_E),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:fpStatsPerCOSEntry.setStatus(_A)
class _FpPerPortCOSNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,21))
_FpPerPortCOSNumber_Type.__name__=_F
_FpPerPortCOSNumber_Object=MibTableColumn
fpPerPortCOSNumber=_FpPerPortCOSNumber_Object((1,3,6,1,4,1,6027,3,16,1,1,6,1,1),_FpPerPortCOSNumber_Type())
fpPerPortCOSNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:fpPerPortCOSNumber.setStatus(_A)
_FpCurrentUsagePerCOS_Type=Counter32
_FpCurrentUsagePerCOS_Object=MibTableColumn
fpCurrentUsagePerCOS=_FpCurrentUsagePerCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,6,1,2),_FpCurrentUsagePerCOS_Type())
fpCurrentUsagePerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCurrentUsagePerCOS.setStatus(_A)
_FpDefaultPacketBuffAllocPerCOS_Type=Counter32
_FpDefaultPacketBuffAllocPerCOS_Object=MibTableColumn
fpDefaultPacketBuffAllocPerCOS=_FpDefaultPacketBuffAllocPerCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,6,1,3),_FpDefaultPacketBuffAllocPerCOS_Type())
fpDefaultPacketBuffAllocPerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpDefaultPacketBuffAllocPerCOS.setStatus(_A)
_FpMaxLimitPerCOS_Type=Counter32
_FpMaxLimitPerCOS_Object=MibTableColumn
fpMaxLimitPerCOS=_FpMaxLimitPerCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,6,1,4),_FpMaxLimitPerCOS_Type())
fpMaxLimitPerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpMaxLimitPerCOS.setStatus(_A)
_FpHOLDropsPerCOS_Type=Counter64
_FpHOLDropsPerCOS_Object=MibTableColumn
fpHOLDropsPerCOS=_FpHOLDropsPerCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,6,1,5),_FpHOLDropsPerCOS_Type())
fpHOLDropsPerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpHOLDropsPerCOS.setStatus(_A)
_FpCpuDataPlaneCOSTable_Object=MibTable
fpCpuDataPlaneCOSTable=_FpCpuDataPlaneCOSTable_Object((1,3,6,1,4,1,6027,3,16,1,1,7))
if mibBuilder.loadTexts:fpCpuDataPlaneCOSTable.setStatus(_A)
_FpCpuDataPlaneCOSEntry_Object=MibTableRow
fpCpuDataPlaneCOSEntry=_FpCpuDataPlaneCOSEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,7,1))
fpCpuDataPlaneCOSEntry.setIndexNames((0,_C,_E),(0,_C,_P))
if mibBuilder.loadTexts:fpCpuDataPlaneCOSEntry.setStatus(_A)
class _FpCOSIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,11))
_FpCOSIndex_Type.__name__=_F
_FpCOSIndex_Object=MibTableColumn
fpCOSIndex=_FpCOSIndex_Object((1,3,6,1,4,1,6027,3,16,1,1,7,1,1),_FpCOSIndex_Type())
fpCOSIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fpCOSIndex.setStatus(_A)
_FpRxPktCOS_Type=Counter32
_FpRxPktCOS_Object=MibTableColumn
fpRxPktCOS=_FpRxPktCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,7,1,2),_FpRxPktCOS_Type())
fpRxPktCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpRxPktCOS.setStatus(_A)
_FpTxPktCOS_Type=Counter32
_FpTxPktCOS_Object=MibTableColumn
fpTxPktCOS=_FpTxPktCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,7,1,3),_FpTxPktCOS_Type())
fpTxPktCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpTxPktCOS.setStatus(_A)
_FpEgrQBuffSnapshotTable_Object=MibTable
fpEgrQBuffSnapshotTable=_FpEgrQBuffSnapshotTable_Object((1,3,6,1,4,1,6027,3,16,1,1,8))
if mibBuilder.loadTexts:fpEgrQBuffSnapshotTable.setStatus(_A)
_FpEgrQBuffSnapshotEntry_Object=MibTableRow
fpEgrQBuffSnapshotEntry=_FpEgrQBuffSnapshotEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,8,1))
fpEgrQBuffSnapshotEntry.setIndexNames((0,_C,_E),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:fpEgrQBuffSnapshotEntry.setStatus(_A)
_FpEgrQTotBuffCells_Type=Counter32
_FpEgrQTotBuffCells_Object=MibTableColumn
fpEgrQTotBuffCells=_FpEgrQTotBuffCells_Object((1,3,6,1,4,1,6027,3,16,1,1,8,1,1),_FpEgrQTotBuffCells_Type())
fpEgrQTotBuffCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgrQTotBuffCells.setStatus(_A)
_FpIngPgBuffSnapshotTable_Object=MibTable
fpIngPgBuffSnapshotTable=_FpIngPgBuffSnapshotTable_Object((1,3,6,1,4,1,6027,3,16,1,1,9))
if mibBuilder.loadTexts:fpIngPgBuffSnapshotTable.setStatus(_A)
_FpIngPgBuffSnapshotEntry_Object=MibTableRow
fpIngPgBuffSnapshotEntry=_FpIngPgBuffSnapshotEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,9,1))
fpIngPgBuffSnapshotEntry.setIndexNames((0,_C,_E),(0,_C,_J),(0,_C,_L))
if mibBuilder.loadTexts:fpIngPgBuffSnapshotEntry.setStatus(_A)
_FpPerPortPGIndex_Type=Integer32
_FpPerPortPGIndex_Object=MibTableColumn
fpPerPortPGIndex=_FpPerPortPGIndex_Object((1,3,6,1,4,1,6027,3,16,1,1,9,1,1),_FpPerPortPGIndex_Type())
fpPerPortPGIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fpPerPortPGIndex.setStatus(_A)
_FpIngSharedCells_Type=Counter32
_FpIngSharedCells_Object=MibTableColumn
fpIngSharedCells=_FpIngSharedCells_Object((1,3,6,1,4,1,6027,3,16,1,1,9,1,2),_FpIngSharedCells_Type())
fpIngSharedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngSharedCells.setStatus(_A)
_FpIngHeadroomCells_Type=Counter32
_FpIngHeadroomCells_Object=MibTableColumn
fpIngHeadroomCells=_FpIngHeadroomCells_Object((1,3,6,1,4,1,6027,3,16,1,1,9,1,3),_FpIngHeadroomCells_Type())
fpIngHeadroomCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIngHeadroomCells.setStatus(_A)
_FpStatsPerPgTable_Object=MibTable
fpStatsPerPgTable=_FpStatsPerPgTable_Object((1,3,6,1,4,1,6027,3,16,1,1,10))
if mibBuilder.loadTexts:fpStatsPerPgTable.setStatus(_A)
_FpStatsPerPgEntry_Object=MibTableRow
fpStatsPerPgEntry=_FpStatsPerPgEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,10,1))
fpStatsPerPgEntry.setIndexNames((0,_C,_E),(0,_C,_J),(0,_C,_L))
if mibBuilder.loadTexts:fpStatsPerPgEntry.setStatus(_A)
_FpStatsPgLimitMinCells_Type=Integer32
_FpStatsPgLimitMinCells_Object=MibTableColumn
fpStatsPgLimitMinCells=_FpStatsPgLimitMinCells_Object((1,3,6,1,4,1,6027,3,16,1,1,10,1,1),_FpStatsPgLimitMinCells_Type())
fpStatsPgLimitMinCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpStatsPgLimitMinCells.setStatus(_A)
_FpStatsPgSharedCells_Type=Integer32
_FpStatsPgSharedCells_Object=MibTableColumn
fpStatsPgSharedCells=_FpStatsPgSharedCells_Object((1,3,6,1,4,1,6027,3,16,1,1,10,1,2),_FpStatsPgSharedCells_Type())
fpStatsPgSharedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpStatsPgSharedCells.setStatus(_A)
class _FpStatsPgSharedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_FpStatsPgSharedMode_Type.__name__=_F
_FpStatsPgSharedMode_Object=MibTableColumn
fpStatsPgSharedMode=_FpStatsPgSharedMode_Object((1,3,6,1,4,1,6027,3,16,1,1,10,1,3),_FpStatsPgSharedMode_Type())
fpStatsPgSharedMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fpStatsPgSharedMode.setStatus(_A)
_FpStatsPgHdrmCells_Type=Integer32
_FpStatsPgHdrmCells_Object=MibTableColumn
fpStatsPgHdrmCells=_FpStatsPgHdrmCells_Object((1,3,6,1,4,1,6027,3,16,1,1,10,1,4),_FpStatsPgHdrmCells_Type())
fpStatsPgHdrmCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpStatsPgHdrmCells.setStatus(_A)
_FpStatsPgCounterMinCells_Type=Counter32
_FpStatsPgCounterMinCells_Object=MibTableColumn
fpStatsPgCounterMinCells=_FpStatsPgCounterMinCells_Object((1,3,6,1,4,1,6027,3,16,1,1,10,1,5),_FpStatsPgCounterMinCells_Type())
fpStatsPgCounterMinCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpStatsPgCounterMinCells.setStatus(_A)
_FpStatsPgCounterSharedCells_Type=Counter32
_FpStatsPgCounterSharedCells_Object=MibTableColumn
fpStatsPgCounterSharedCells=_FpStatsPgCounterSharedCells_Object((1,3,6,1,4,1,6027,3,16,1,1,10,1,6),_FpStatsPgCounterSharedCells_Type())
fpStatsPgCounterSharedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpStatsPgCounterSharedCells.setStatus(_A)
_FpStatsPgCounterHdrmCells_Type=Counter32
_FpStatsPgCounterHdrmCells_Object=MibTableColumn
fpStatsPgCounterHdrmCells=_FpStatsPgCounterHdrmCells_Object((1,3,6,1,4,1,6027,3,16,1,1,10,1,7),_FpStatsPgCounterHdrmCells_Type())
fpStatsPgCounterHdrmCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpStatsPgCounterHdrmCells.setStatus(_A)
_PfcPerPrioTable_Object=MibTable
pfcPerPrioTable=_PfcPerPrioTable_Object((1,3,6,1,4,1,6027,3,16,1,1,11))
if mibBuilder.loadTexts:pfcPerPrioTable.setStatus(_A)
_PfcPerPrioEntry_Object=MibTableRow
pfcPerPrioEntry=_PfcPerPrioEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,11,1))
pfcPerPrioEntry.setIndexNames((0,_C,_E),(0,_C,_J),(0,_C,_S))
if mibBuilder.loadTexts:pfcPerPrioEntry.setStatus(_A)
class _PrioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_PrioIndex_Type.__name__=_F
_PrioIndex_Object=MibTableColumn
prioIndex=_PrioIndex_Object((1,3,6,1,4,1,6027,3,16,1,1,11,1,1),_PrioIndex_Type())
prioIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:prioIndex.setStatus(_A)
_PfcPerPrioRequests_Type=Counter64
_PfcPerPrioRequests_Object=MibTableColumn
pfcPerPrioRequests=_PfcPerPrioRequests_Object((1,3,6,1,4,1,6027,3,16,1,1,11,1,2),_PfcPerPrioRequests_Type())
pfcPerPrioRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:pfcPerPrioRequests.setStatus(_A)
if mibBuilder.loadTexts:pfcPerPrioRequests.setUnits(_T)
_PfcPerPrioIndications_Type=Counter64
_PfcPerPrioIndications_Object=MibTableColumn
pfcPerPrioIndications=_PfcPerPrioIndications_Object((1,3,6,1,4,1,6027,3,16,1,1,11,1,3),_PfcPerPrioIndications_Type())
pfcPerPrioIndications.setMaxAccess(_B)
if mibBuilder.loadTexts:pfcPerPrioIndications.setStatus(_A)
if mibBuilder.loadTexts:pfcPerPrioIndications.setUnits(_U)
_FpCpuPartyBusPortStatsTable_Object=MibTable
fpCpuPartyBusPortStatsTable=_FpCpuPartyBusPortStatsTable_Object((1,3,6,1,4,1,6027,3,16,1,1,12))
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsTable.setStatus(_A)
_FpCpuPartyBusPortStatsEntry_Object=MibTableRow
fpCpuPartyBusPortStatsEntry=_FpCpuPartyBusPortStatsEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1))
fpCpuPartyBusPortStatsEntry.setIndexNames((0,_C,_E),(0,_C,_J))
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsEntry.setStatus(_A)
_FpCpuPartyBusPortStatsOutOctets_Type=Counter64
_FpCpuPartyBusPortStatsOutOctets_Object=MibTableColumn
fpCpuPartyBusPortStatsOutOctets=_FpCpuPartyBusPortStatsOutOctets_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,1),_FpCpuPartyBusPortStatsOutOctets_Type())
fpCpuPartyBusPortStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutOctets.setStatus(_A)
_FpCpuPartyBusPortStatsOutDropPkts_Type=Counter32
_FpCpuPartyBusPortStatsOutDropPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutDropPkts=_FpCpuPartyBusPortStatsOutDropPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,2),_FpCpuPartyBusPortStatsOutDropPkts_Type())
fpCpuPartyBusPortStatsOutDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutDropPkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutCOS0Pkts_Type=Counter32
_FpCpuPartyBusPortStatsOutCOS0Pkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutCOS0Pkts=_FpCpuPartyBusPortStatsOutCOS0Pkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,3),_FpCpuPartyBusPortStatsOutCOS0Pkts_Type())
fpCpuPartyBusPortStatsOutCOS0Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutCOS0Pkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutCOS1Pkts_Type=Counter32
_FpCpuPartyBusPortStatsOutCOS1Pkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutCOS1Pkts=_FpCpuPartyBusPortStatsOutCOS1Pkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,4),_FpCpuPartyBusPortStatsOutCOS1Pkts_Type())
fpCpuPartyBusPortStatsOutCOS1Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutCOS1Pkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutCOS2Pkts_Type=Counter32
_FpCpuPartyBusPortStatsOutCOS2Pkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutCOS2Pkts=_FpCpuPartyBusPortStatsOutCOS2Pkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,5),_FpCpuPartyBusPortStatsOutCOS2Pkts_Type())
fpCpuPartyBusPortStatsOutCOS2Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutCOS2Pkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutCOS3Pkts_Type=Counter32
_FpCpuPartyBusPortStatsOutCOS3Pkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutCOS3Pkts=_FpCpuPartyBusPortStatsOutCOS3Pkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,6),_FpCpuPartyBusPortStatsOutCOS3Pkts_Type())
fpCpuPartyBusPortStatsOutCOS3Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutCOS3Pkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutCOS4Pkts_Type=Counter32
_FpCpuPartyBusPortStatsOutCOS4Pkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutCOS4Pkts=_FpCpuPartyBusPortStatsOutCOS4Pkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,7),_FpCpuPartyBusPortStatsOutCOS4Pkts_Type())
fpCpuPartyBusPortStatsOutCOS4Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutCOS4Pkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutCOS5Pkts_Type=Counter32
_FpCpuPartyBusPortStatsOutCOS5Pkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutCOS5Pkts=_FpCpuPartyBusPortStatsOutCOS5Pkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,8),_FpCpuPartyBusPortStatsOutCOS5Pkts_Type())
fpCpuPartyBusPortStatsOutCOS5Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutCOS5Pkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutUnicastPkts_Type=Counter32
_FpCpuPartyBusPortStatsOutUnicastPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutUnicastPkts=_FpCpuPartyBusPortStatsOutUnicastPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,9),_FpCpuPartyBusPortStatsOutUnicastPkts_Type())
fpCpuPartyBusPortStatsOutUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutUnicastPkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutMulticastPkts_Type=Counter32
_FpCpuPartyBusPortStatsOutMulticastPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutMulticastPkts=_FpCpuPartyBusPortStatsOutMulticastPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,10),_FpCpuPartyBusPortStatsOutMulticastPkts_Type())
fpCpuPartyBusPortStatsOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutMulticastPkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutBroadcastPkts_Type=Counter32
_FpCpuPartyBusPortStatsOutBroadcastPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutBroadcastPkts=_FpCpuPartyBusPortStatsOutBroadcastPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,11),_FpCpuPartyBusPortStatsOutBroadcastPkts_Type())
fpCpuPartyBusPortStatsOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutBroadcastPkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutPausePkts_Type=Counter32
_FpCpuPartyBusPortStatsOutPausePkts_Object=MibTableColumn
fpCpuPartyBusPortStatsOutPausePkts=_FpCpuPartyBusPortStatsOutPausePkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,12),_FpCpuPartyBusPortStatsOutPausePkts_Type())
fpCpuPartyBusPortStatsOutPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutPausePkts.setStatus(_A)
_FpCpuPartyBusPortStatsOutCollisions_Type=Counter32
_FpCpuPartyBusPortStatsOutCollisions_Object=MibTableColumn
fpCpuPartyBusPortStatsOutCollisions=_FpCpuPartyBusPortStatsOutCollisions_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,13),_FpCpuPartyBusPortStatsOutCollisions_Type())
fpCpuPartyBusPortStatsOutCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutCollisions.setStatus(_A)
_FpCpuPartyBusPortStatsOutSingleCollisions_Type=Counter32
_FpCpuPartyBusPortStatsOutSingleCollisions_Object=MibTableColumn
fpCpuPartyBusPortStatsOutSingleCollisions=_FpCpuPartyBusPortStatsOutSingleCollisions_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,14),_FpCpuPartyBusPortStatsOutSingleCollisions_Type())
fpCpuPartyBusPortStatsOutSingleCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutSingleCollisions.setStatus(_A)
_FpCpuPartyBusPortStatsOutMultiCollisions_Type=Counter32
_FpCpuPartyBusPortStatsOutMultiCollisions_Object=MibTableColumn
fpCpuPartyBusPortStatsOutMultiCollisions=_FpCpuPartyBusPortStatsOutMultiCollisions_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,15),_FpCpuPartyBusPortStatsOutMultiCollisions_Type())
fpCpuPartyBusPortStatsOutMultiCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutMultiCollisions.setStatus(_A)
_FpCpuPartyBusPortStatsOutLateCollisions_Type=Counter32
_FpCpuPartyBusPortStatsOutLateCollisions_Object=MibTableColumn
fpCpuPartyBusPortStatsOutLateCollisions=_FpCpuPartyBusPortStatsOutLateCollisions_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,16),_FpCpuPartyBusPortStatsOutLateCollisions_Type())
fpCpuPartyBusPortStatsOutLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutLateCollisions.setStatus(_A)
_FpCpuPartyBusPortStatsOutExcessCollisions_Type=Counter32
_FpCpuPartyBusPortStatsOutExcessCollisions_Object=MibTableColumn
fpCpuPartyBusPortStatsOutExcessCollisions=_FpCpuPartyBusPortStatsOutExcessCollisions_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,17),_FpCpuPartyBusPortStatsOutExcessCollisions_Type())
fpCpuPartyBusPortStatsOutExcessCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutExcessCollisions.setStatus(_A)
_FpCpuPartyBusPortStatsOutDeferred_Type=Counter32
_FpCpuPartyBusPortStatsOutDeferred_Object=MibTableColumn
fpCpuPartyBusPortStatsOutDeferred=_FpCpuPartyBusPortStatsOutDeferred_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,18),_FpCpuPartyBusPortStatsOutDeferred_Type())
fpCpuPartyBusPortStatsOutDeferred.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutDeferred.setStatus(_A)
_FpCpuPartyBusPortStatsOutDiscarded_Type=Counter32
_FpCpuPartyBusPortStatsOutDiscarded_Object=MibTableColumn
fpCpuPartyBusPortStatsOutDiscarded=_FpCpuPartyBusPortStatsOutDiscarded_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,19),_FpCpuPartyBusPortStatsOutDiscarded_Type())
fpCpuPartyBusPortStatsOutDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsOutDiscarded.setStatus(_A)
_FpCpuPartyBusPortStatsInOctets_Type=Counter64
_FpCpuPartyBusPortStatsInOctets_Object=MibTableColumn
fpCpuPartyBusPortStatsInOctets=_FpCpuPartyBusPortStatsInOctets_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,20),_FpCpuPartyBusPortStatsInOctets_Type())
fpCpuPartyBusPortStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInOctets.setStatus(_A)
_FpCpuPartyBusPortStatsInUndersizePkts_Type=Counter32
_FpCpuPartyBusPortStatsInUndersizePkts_Object=MibTableColumn
fpCpuPartyBusPortStatsInUndersizePkts=_FpCpuPartyBusPortStatsInUndersizePkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,21),_FpCpuPartyBusPortStatsInUndersizePkts_Type())
fpCpuPartyBusPortStatsInUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInUndersizePkts.setStatus(_A)
_FpCpuPartyBusPortStatsInOversizePkts_Type=Counter32
_FpCpuPartyBusPortStatsInOversizePkts_Object=MibTableColumn
fpCpuPartyBusPortStatsInOversizePkts=_FpCpuPartyBusPortStatsInOversizePkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,22),_FpCpuPartyBusPortStatsInOversizePkts_Type())
fpCpuPartyBusPortStatsInOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInOversizePkts.setStatus(_A)
_FpCpuPartyBusPortStatsInPausePkts_Type=Counter32
_FpCpuPartyBusPortStatsInPausePkts_Object=MibTableColumn
fpCpuPartyBusPortStatsInPausePkts=_FpCpuPartyBusPortStatsInPausePkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,23),_FpCpuPartyBusPortStatsInPausePkts_Type())
fpCpuPartyBusPortStatsInPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInPausePkts.setStatus(_A)
_FpCpuPartyBusPortStatsIn64OctetPkts_Type=Counter32
_FpCpuPartyBusPortStatsIn64OctetPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsIn64OctetPkts=_FpCpuPartyBusPortStatsIn64OctetPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,24),_FpCpuPartyBusPortStatsIn64OctetPkts_Type())
fpCpuPartyBusPortStatsIn64OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsIn64OctetPkts.setStatus(_A)
_FpCpuPartyBusPortStatsIn65To127OctetPkts_Type=Counter32
_FpCpuPartyBusPortStatsIn65To127OctetPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsIn65To127OctetPkts=_FpCpuPartyBusPortStatsIn65To127OctetPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,25),_FpCpuPartyBusPortStatsIn65To127OctetPkts_Type())
fpCpuPartyBusPortStatsIn65To127OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsIn65To127OctetPkts.setStatus(_A)
_FpCpuPartyBusPortStatsIn128To255OctetPkts_Type=Counter32
_FpCpuPartyBusPortStatsIn128To255OctetPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsIn128To255OctetPkts=_FpCpuPartyBusPortStatsIn128To255OctetPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,26),_FpCpuPartyBusPortStatsIn128To255OctetPkts_Type())
fpCpuPartyBusPortStatsIn128To255OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsIn128To255OctetPkts.setStatus(_A)
_FpCpuPartyBusPortStatsIn256To511OctetPkts_Type=Counter32
_FpCpuPartyBusPortStatsIn256To511OctetPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsIn256To511OctetPkts=_FpCpuPartyBusPortStatsIn256To511OctetPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,27),_FpCpuPartyBusPortStatsIn256To511OctetPkts_Type())
fpCpuPartyBusPortStatsIn256To511OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsIn256To511OctetPkts.setStatus(_A)
_FpCpuPartyBusPortStatsIn512To1023OctetPkts_Type=Counter32
_FpCpuPartyBusPortStatsIn512To1023OctetPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsIn512To1023OctetPkts=_FpCpuPartyBusPortStatsIn512To1023OctetPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,28),_FpCpuPartyBusPortStatsIn512To1023OctetPkts_Type())
fpCpuPartyBusPortStatsIn512To1023OctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsIn512To1023OctetPkts.setStatus(_A)
_FpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Type=Counter32
_FpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts=_FpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,29),_FpCpuPartyBusPortStatsIn1024ToMaxOctetPkts_Type())
fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts.setStatus(_A)
_FpCpuPartyBusPortStatsInJabbers_Type=Counter32
_FpCpuPartyBusPortStatsInJabbers_Object=MibTableColumn
fpCpuPartyBusPortStatsInJabbers=_FpCpuPartyBusPortStatsInJabbers_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,30),_FpCpuPartyBusPortStatsInJabbers_Type())
fpCpuPartyBusPortStatsInJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInJabbers.setStatus(_A)
_FpCpuPartyBusPortStatsInAlignErrors_Type=Counter32
_FpCpuPartyBusPortStatsInAlignErrors_Object=MibTableColumn
fpCpuPartyBusPortStatsInAlignErrors=_FpCpuPartyBusPortStatsInAlignErrors_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,31),_FpCpuPartyBusPortStatsInAlignErrors_Type())
fpCpuPartyBusPortStatsInAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInAlignErrors.setStatus(_A)
_FpCpuPartyBusPortStatsInFcsErrors_Type=Counter32
_FpCpuPartyBusPortStatsInFcsErrors_Object=MibTableColumn
fpCpuPartyBusPortStatsInFcsErrors=_FpCpuPartyBusPortStatsInFcsErrors_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,32),_FpCpuPartyBusPortStatsInFcsErrors_Type())
fpCpuPartyBusPortStatsInFcsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInFcsErrors.setStatus(_A)
_FpCpuPartyBusPortStatsInGoodOctets_Type=Counter32
_FpCpuPartyBusPortStatsInGoodOctets_Object=MibTableColumn
fpCpuPartyBusPortStatsInGoodOctets=_FpCpuPartyBusPortStatsInGoodOctets_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,33),_FpCpuPartyBusPortStatsInGoodOctets_Type())
fpCpuPartyBusPortStatsInGoodOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInGoodOctets.setStatus(_A)
_FpCpuPartyBusPortStatsInDropPkts_Type=Counter32
_FpCpuPartyBusPortStatsInDropPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsInDropPkts=_FpCpuPartyBusPortStatsInDropPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,34),_FpCpuPartyBusPortStatsInDropPkts_Type())
fpCpuPartyBusPortStatsInDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInDropPkts.setStatus(_A)
_FpCpuPartyBusPortStatsInUnicastPkts_Type=Counter32
_FpCpuPartyBusPortStatsInUnicastPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsInUnicastPkts=_FpCpuPartyBusPortStatsInUnicastPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,35),_FpCpuPartyBusPortStatsInUnicastPkts_Type())
fpCpuPartyBusPortStatsInUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInUnicastPkts.setStatus(_A)
_FpCpuPartyBusPortStatsInMulticastPkts_Type=Counter32
_FpCpuPartyBusPortStatsInMulticastPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsInMulticastPkts=_FpCpuPartyBusPortStatsInMulticastPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,36),_FpCpuPartyBusPortStatsInMulticastPkts_Type())
fpCpuPartyBusPortStatsInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInMulticastPkts.setStatus(_A)
_FpCpuPartyBusPortStatsInBroadcastPkts_Type=Counter32
_FpCpuPartyBusPortStatsInBroadcastPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsInBroadcastPkts=_FpCpuPartyBusPortStatsInBroadcastPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,37),_FpCpuPartyBusPortStatsInBroadcastPkts_Type())
fpCpuPartyBusPortStatsInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInBroadcastPkts.setStatus(_A)
_FpCpuPartyBusPortStatsInSrcAddrChanges_Type=Counter32
_FpCpuPartyBusPortStatsInSrcAddrChanges_Object=MibTableColumn
fpCpuPartyBusPortStatsInSrcAddrChanges=_FpCpuPartyBusPortStatsInSrcAddrChanges_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,38),_FpCpuPartyBusPortStatsInSrcAddrChanges_Type())
fpCpuPartyBusPortStatsInSrcAddrChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInSrcAddrChanges.setStatus(_A)
_FpCpuPartyBusPortStatsInFragments_Type=Counter32
_FpCpuPartyBusPortStatsInFragments_Object=MibTableColumn
fpCpuPartyBusPortStatsInFragments=_FpCpuPartyBusPortStatsInFragments_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,39),_FpCpuPartyBusPortStatsInFragments_Type())
fpCpuPartyBusPortStatsInFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInFragments.setStatus(_A)
_FpCpuPartyBusPortStatsInJumboPkts_Type=Counter32
_FpCpuPartyBusPortStatsInJumboPkts_Object=MibTableColumn
fpCpuPartyBusPortStatsInJumboPkts=_FpCpuPartyBusPortStatsInJumboPkts_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,40),_FpCpuPartyBusPortStatsInJumboPkts_Type())
fpCpuPartyBusPortStatsInJumboPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInJumboPkts.setStatus(_A)
_FpCpuPartyBusPortStatsInSymbolErrors_Type=Counter32
_FpCpuPartyBusPortStatsInSymbolErrors_Object=MibTableColumn
fpCpuPartyBusPortStatsInSymbolErrors=_FpCpuPartyBusPortStatsInSymbolErrors_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,41),_FpCpuPartyBusPortStatsInSymbolErrors_Type())
fpCpuPartyBusPortStatsInSymbolErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInSymbolErrors.setStatus(_A)
_FpCpuPartyBusPortStatsInInRangeErrors_Type=Counter32
_FpCpuPartyBusPortStatsInInRangeErrors_Object=MibTableColumn
fpCpuPartyBusPortStatsInInRangeErrors=_FpCpuPartyBusPortStatsInInRangeErrors_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,42),_FpCpuPartyBusPortStatsInInRangeErrors_Type())
fpCpuPartyBusPortStatsInInRangeErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInInRangeErrors.setStatus(_A)
_FpCpuPartyBusPortStatsInOutRangeErrors_Type=Counter32
_FpCpuPartyBusPortStatsInOutRangeErrors_Object=MibTableColumn
fpCpuPartyBusPortStatsInOutRangeErrors=_FpCpuPartyBusPortStatsInOutRangeErrors_Object((1,3,6,1,4,1,6027,3,16,1,1,12,1,43),_FpCpuPartyBusPortStatsInOutRangeErrors_Type())
fpCpuPartyBusPortStatsInOutRangeErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:fpCpuPartyBusPortStatsInOutRangeErrors.setStatus(_A)
_FpDropsIfTable_Object=MibTable
fpDropsIfTable=_FpDropsIfTable_Object((1,3,6,1,4,1,6027,3,16,1,1,13))
if mibBuilder.loadTexts:fpDropsIfTable.setStatus(_A)
_FpDropsIfEntry_Object=MibTableRow
fpDropsIfEntry=_FpDropsIfEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1))
fpDropsIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:fpDropsIfEntry.setStatus(_A)
_FpIfIngressDrops_Type=Counter64
_FpIfIngressDrops_Object=MibTableColumn
fpIfIngressDrops=_FpIfIngressDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,1),_FpIfIngressDrops_Type())
fpIfIngressDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngressDrops.setStatus(_A)
_FpIfIngIBPCBPFullDrops_Type=Counter64
_FpIfIngIBPCBPFullDrops_Object=MibTableColumn
fpIfIngIBPCBPFullDrops=_FpIfIngIBPCBPFullDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,2),_FpIfIngIBPCBPFullDrops_Type())
fpIfIngIBPCBPFullDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngIBPCBPFullDrops.setStatus(_A)
_FpIfIngPortSTPnotFwdDrops_Type=Counter64
_FpIfIngPortSTPnotFwdDrops_Object=MibTableColumn
fpIfIngPortSTPnotFwdDrops=_FpIfIngPortSTPnotFwdDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,3),_FpIfIngPortSTPnotFwdDrops_Type())
fpIfIngPortSTPnotFwdDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngPortSTPnotFwdDrops.setStatus(_A)
_FpIfIngIPv4L3Discards_Type=Counter64
_FpIfIngIPv4L3Discards_Object=MibTableColumn
fpIfIngIPv4L3Discards=_FpIfIngIPv4L3Discards_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,4),_FpIfIngIPv4L3Discards_Type())
fpIfIngIPv4L3Discards.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngIPv4L3Discards.setStatus(_A)
_FpIfIngPolicyDiscards_Type=Counter64
_FpIfIngPolicyDiscards_Object=MibTableColumn
fpIfIngPolicyDiscards=_FpIfIngPolicyDiscards_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,5),_FpIfIngPolicyDiscards_Type())
fpIfIngPolicyDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngPolicyDiscards.setStatus(_A)
_FpIfIngPacketsDroppedByFP_Type=Counter64
_FpIfIngPacketsDroppedByFP_Object=MibTableColumn
fpIfIngPacketsDroppedByFP=_FpIfIngPacketsDroppedByFP_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,6),_FpIfIngPacketsDroppedByFP_Type())
fpIfIngPacketsDroppedByFP.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngPacketsDroppedByFP.setStatus(_A)
_FpIfIngL2L3Drops_Type=Counter64
_FpIfIngL2L3Drops_Object=MibTableColumn
fpIfIngL2L3Drops=_FpIfIngL2L3Drops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,7),_FpIfIngL2L3Drops_Type())
fpIfIngL2L3Drops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngL2L3Drops.setStatus(_A)
_FpIfIngPortBitMapZeroDrops_Type=Counter64
_FpIfIngPortBitMapZeroDrops_Object=MibTableColumn
fpIfIngPortBitMapZeroDrops=_FpIfIngPortBitMapZeroDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,8),_FpIfIngPortBitMapZeroDrops_Type())
fpIfIngPortBitMapZeroDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngPortBitMapZeroDrops.setStatus(_A)
_FpIfIngRxVLANDrops_Type=Counter64
_FpIfIngRxVLANDrops_Object=MibTableColumn
fpIfIngRxVLANDrops=_FpIfIngRxVLANDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,9),_FpIfIngRxVLANDrops_Type())
fpIfIngRxVLANDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngRxVLANDrops.setStatus(_A)
_FpIfIngressFCSDrops_Type=Counter64
_FpIfIngressFCSDrops_Object=MibTableColumn
fpIfIngressFCSDrops=_FpIfIngressFCSDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,10),_FpIfIngressFCSDrops_Type())
fpIfIngressFCSDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngressFCSDrops.setStatus(_A)
_FpIfIngressMTUExceeds_Type=Counter64
_FpIfIngressMTUExceeds_Object=MibTableColumn
fpIfIngressMTUExceeds=_FpIfIngressMTUExceeds_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,11),_FpIfIngressMTUExceeds_Type())
fpIfIngressMTUExceeds.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngressMTUExceeds.setStatus(_A)
_FpIfMMUHOLDrops_Type=Counter64
_FpIfMMUHOLDrops_Object=MibTableColumn
fpIfMMUHOLDrops=_FpIfMMUHOLDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,12),_FpIfMMUHOLDrops_Type())
fpIfMMUHOLDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfMMUHOLDrops.setStatus(_A)
_FpIfMMUTxPurgeCellErr_Type=Counter64
_FpIfMMUTxPurgeCellErr_Object=MibTableColumn
fpIfMMUTxPurgeCellErr=_FpIfMMUTxPurgeCellErr_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,13),_FpIfMMUTxPurgeCellErr_Type())
fpIfMMUTxPurgeCellErr.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfMMUTxPurgeCellErr.setStatus(_A)
_FpIfMMUAgedDrops_Type=Counter64
_FpIfMMUAgedDrops_Object=MibTableColumn
fpIfMMUAgedDrops=_FpIfMMUAgedDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,14),_FpIfMMUAgedDrops_Type())
fpIfMMUAgedDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfMMUAgedDrops.setStatus(_A)
_FpIfEgressFCSDrops_Type=Counter64
_FpIfEgressFCSDrops_Object=MibTableColumn
fpIfEgressFCSDrops=_FpIfEgressFCSDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,15),_FpIfEgressFCSDrops_Type())
fpIfEgressFCSDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfEgressFCSDrops.setStatus(_A)
_FpIfEgIPv4L3UCAgedDrops_Type=Counter64
_FpIfEgIPv4L3UCAgedDrops_Object=MibTableColumn
fpIfEgIPv4L3UCAgedDrops=_FpIfEgIPv4L3UCAgedDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,16),_FpIfEgIPv4L3UCAgedDrops_Type())
fpIfEgIPv4L3UCAgedDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfEgIPv4L3UCAgedDrops.setStatus(_A)
_FpIfEgTTLThresholdDrops_Type=Counter64
_FpIfEgTTLThresholdDrops_Object=MibTableColumn
fpIfEgTTLThresholdDrops=_FpIfEgTTLThresholdDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,17),_FpIfEgTTLThresholdDrops_Type())
fpIfEgTTLThresholdDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfEgTTLThresholdDrops.setStatus(_A)
_FpIfEgInvalidVLANCounterDrops_Type=Counter64
_FpIfEgInvalidVLANCounterDrops_Object=MibTableColumn
fpIfEgInvalidVLANCounterDrops=_FpIfEgInvalidVLANCounterDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,18),_FpIfEgInvalidVLANCounterDrops_Type())
fpIfEgInvalidVLANCounterDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfEgInvalidVLANCounterDrops.setStatus(_A)
_FpIfEgL2MCDrops_Type=Counter64
_FpIfEgL2MCDrops_Object=MibTableColumn
fpIfEgL2MCDrops=_FpIfEgL2MCDrops_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,19),_FpIfEgL2MCDrops_Type())
fpIfEgL2MCDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfEgL2MCDrops.setStatus(_A)
_FpIfEgPktDropsOfAnyCondition_Type=Counter64
_FpIfEgPktDropsOfAnyCondition_Object=MibTableColumn
fpIfEgPktDropsOfAnyCondition=_FpIfEgPktDropsOfAnyCondition_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,20),_FpIfEgPktDropsOfAnyCondition_Type())
fpIfEgPktDropsOfAnyCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfEgPktDropsOfAnyCondition.setStatus(_A)
_FpIfEgHgMacUnderFlow_Type=Counter64
_FpIfEgHgMacUnderFlow_Object=MibTableColumn
fpIfEgHgMacUnderFlow=_FpIfEgHgMacUnderFlow_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,21),_FpIfEgHgMacUnderFlow_Type())
fpIfEgHgMacUnderFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfEgHgMacUnderFlow.setStatus(_A)
_FpIfEgTxErrPktCounter_Type=Counter64
_FpIfEgTxErrPktCounter_Object=MibTableColumn
fpIfEgTxErrPktCounter=_FpIfEgTxErrPktCounter_Object((1,3,6,1,4,1,6027,3,16,1,1,13,1,22),_FpIfEgTxErrPktCounter_Type())
fpIfEgTxErrPktCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfEgTxErrPktCounter.setStatus(_A)
_FpStatsPerIfTable_Object=MibTable
fpStatsPerIfTable=_FpStatsPerIfTable_Object((1,3,6,1,4,1,6027,3,16,1,1,14))
if mibBuilder.loadTexts:fpStatsPerIfTable.setStatus(_A)
_FpStatsPerIfEntry_Object=MibTableRow
fpStatsPerIfEntry=_FpStatsPerIfEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,14,1))
fpStatsPerIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:fpStatsPerIfEntry.setStatus(_A)
_FpIfCurrentUsagePerPort_Type=Counter32
_FpIfCurrentUsagePerPort_Object=MibTableColumn
fpIfCurrentUsagePerPort=_FpIfCurrentUsagePerPort_Object((1,3,6,1,4,1,6027,3,16,1,1,14,1,1),_FpIfCurrentUsagePerPort_Type())
fpIfCurrentUsagePerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfCurrentUsagePerPort.setStatus(_A)
_FpIfDefaultPacketBuffAlloc_Type=Counter32
_FpIfDefaultPacketBuffAlloc_Object=MibTableColumn
fpIfDefaultPacketBuffAlloc=_FpIfDefaultPacketBuffAlloc_Object((1,3,6,1,4,1,6027,3,16,1,1,14,1,2),_FpIfDefaultPacketBuffAlloc_Type())
fpIfDefaultPacketBuffAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfDefaultPacketBuffAlloc.setStatus(_A)
_FpIfMaxLimitPerPort_Type=Counter32
_FpIfMaxLimitPerPort_Object=MibTableColumn
fpIfMaxLimitPerPort=_FpIfMaxLimitPerPort_Object((1,3,6,1,4,1,6027,3,16,1,1,14,1,3),_FpIfMaxLimitPerPort_Type())
fpIfMaxLimitPerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfMaxLimitPerPort.setStatus(_A)
_FpStatsPerIfCOSTable_Object=MibTable
fpStatsPerIfCOSTable=_FpStatsPerIfCOSTable_Object((1,3,6,1,4,1,6027,3,16,1,1,15))
if mibBuilder.loadTexts:fpStatsPerIfCOSTable.setStatus(_A)
_FpStatsPerIfCOSEntry_Object=MibTableRow
fpStatsPerIfCOSEntry=_FpStatsPerIfCOSEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,15,1))
fpStatsPerIfCOSEntry.setIndexNames((0,_H,_I),(0,_C,_M))
if mibBuilder.loadTexts:fpStatsPerIfCOSEntry.setStatus(_A)
class _FpIfPerCOSNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,21))
_FpIfPerCOSNumber_Type.__name__=_F
_FpIfPerCOSNumber_Object=MibTableColumn
fpIfPerCOSNumber=_FpIfPerCOSNumber_Object((1,3,6,1,4,1,6027,3,16,1,1,15,1,1),_FpIfPerCOSNumber_Type())
fpIfPerCOSNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:fpIfPerCOSNumber.setStatus(_A)
_FpIfCurrentUsagePerCOS_Type=Counter32
_FpIfCurrentUsagePerCOS_Object=MibTableColumn
fpIfCurrentUsagePerCOS=_FpIfCurrentUsagePerCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,15,1,2),_FpIfCurrentUsagePerCOS_Type())
fpIfCurrentUsagePerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfCurrentUsagePerCOS.setStatus(_A)
_FpIfDefaultPacketBuffAllocPerCOS_Type=Counter32
_FpIfDefaultPacketBuffAllocPerCOS_Object=MibTableColumn
fpIfDefaultPacketBuffAllocPerCOS=_FpIfDefaultPacketBuffAllocPerCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,15,1,3),_FpIfDefaultPacketBuffAllocPerCOS_Type())
fpIfDefaultPacketBuffAllocPerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfDefaultPacketBuffAllocPerCOS.setStatus(_A)
_FpIfMaxLimitPerCOS_Type=Counter32
_FpIfMaxLimitPerCOS_Object=MibTableColumn
fpIfMaxLimitPerCOS=_FpIfMaxLimitPerCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,15,1,4),_FpIfMaxLimitPerCOS_Type())
fpIfMaxLimitPerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfMaxLimitPerCOS.setStatus(_A)
_FpIfHOLDropsPerCOS_Type=Counter64
_FpIfHOLDropsPerCOS_Object=MibTableColumn
fpIfHOLDropsPerCOS=_FpIfHOLDropsPerCOS_Object((1,3,6,1,4,1,6027,3,16,1,1,15,1,5),_FpIfHOLDropsPerCOS_Type())
fpIfHOLDropsPerCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfHOLDropsPerCOS.setStatus(_A)
_FpEgrQBuffSnapshotIfTable_Object=MibTable
fpEgrQBuffSnapshotIfTable=_FpEgrQBuffSnapshotIfTable_Object((1,3,6,1,4,1,6027,3,16,1,1,16))
if mibBuilder.loadTexts:fpEgrQBuffSnapshotIfTable.setStatus(_A)
_FpEgrQBuffSnapshotIfEntry_Object=MibTableRow
fpEgrQBuffSnapshotIfEntry=_FpEgrQBuffSnapshotIfEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,16,1))
fpEgrQBuffSnapshotIfEntry.setIndexNames((0,_H,_I),(0,_C,_M))
if mibBuilder.loadTexts:fpEgrQBuffSnapshotIfEntry.setStatus(_A)
_FpIfEgrQTotBuffCells_Type=Counter32
_FpIfEgrQTotBuffCells_Object=MibTableColumn
fpIfEgrQTotBuffCells=_FpIfEgrQTotBuffCells_Object((1,3,6,1,4,1,6027,3,16,1,1,16,1,1),_FpIfEgrQTotBuffCells_Type())
fpIfEgrQTotBuffCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfEgrQTotBuffCells.setStatus(_A)
_FpIngPgBuffSnapshotIfTable_Object=MibTable
fpIngPgBuffSnapshotIfTable=_FpIngPgBuffSnapshotIfTable_Object((1,3,6,1,4,1,6027,3,16,1,1,17))
if mibBuilder.loadTexts:fpIngPgBuffSnapshotIfTable.setStatus(_A)
_FpIngPgBuffSnapshotIfEntry_Object=MibTableRow
fpIngPgBuffSnapshotIfEntry=_FpIngPgBuffSnapshotIfEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,17,1))
fpIngPgBuffSnapshotIfEntry.setIndexNames((0,_H,_I),(0,_C,_N))
if mibBuilder.loadTexts:fpIngPgBuffSnapshotIfEntry.setStatus(_A)
_FpIfPerPGIndex_Type=Integer32
_FpIfPerPGIndex_Object=MibTableColumn
fpIfPerPGIndex=_FpIfPerPGIndex_Object((1,3,6,1,4,1,6027,3,16,1,1,17,1,1),_FpIfPerPGIndex_Type())
fpIfPerPGIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fpIfPerPGIndex.setStatus(_A)
_FpIfIngSharedCells_Type=Counter32
_FpIfIngSharedCells_Object=MibTableColumn
fpIfIngSharedCells=_FpIfIngSharedCells_Object((1,3,6,1,4,1,6027,3,16,1,1,17,1,2),_FpIfIngSharedCells_Type())
fpIfIngSharedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngSharedCells.setStatus(_A)
_FpIfIngHeadroomCells_Type=Counter32
_FpIfIngHeadroomCells_Object=MibTableColumn
fpIfIngHeadroomCells=_FpIfIngHeadroomCells_Object((1,3,6,1,4,1,6027,3,16,1,1,17,1,3),_FpIfIngHeadroomCells_Type())
fpIfIngHeadroomCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfIngHeadroomCells.setStatus(_A)
_FpStatsPerPgIfTable_Object=MibTable
fpStatsPerPgIfTable=_FpStatsPerPgIfTable_Object((1,3,6,1,4,1,6027,3,16,1,1,18))
if mibBuilder.loadTexts:fpStatsPerPgIfTable.setStatus(_A)
_FpStatsPerPgIfEntry_Object=MibTableRow
fpStatsPerPgIfEntry=_FpStatsPerPgIfEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,18,1))
fpStatsPerPgIfEntry.setIndexNames((0,_H,_I),(0,_C,_N))
if mibBuilder.loadTexts:fpStatsPerPgIfEntry.setStatus(_A)
_FpIfStatsPgLimitMinCells_Type=Integer32
_FpIfStatsPgLimitMinCells_Object=MibTableColumn
fpIfStatsPgLimitMinCells=_FpIfStatsPgLimitMinCells_Object((1,3,6,1,4,1,6027,3,16,1,1,18,1,1),_FpIfStatsPgLimitMinCells_Type())
fpIfStatsPgLimitMinCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfStatsPgLimitMinCells.setStatus(_A)
_FpIfStatsPgSharedCells_Type=Integer32
_FpIfStatsPgSharedCells_Object=MibTableColumn
fpIfStatsPgSharedCells=_FpIfStatsPgSharedCells_Object((1,3,6,1,4,1,6027,3,16,1,1,18,1,2),_FpIfStatsPgSharedCells_Type())
fpIfStatsPgSharedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfStatsPgSharedCells.setStatus(_A)
class _FpIfStatsPgSharedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_FpIfStatsPgSharedMode_Type.__name__=_F
_FpIfStatsPgSharedMode_Object=MibTableColumn
fpIfStatsPgSharedMode=_FpIfStatsPgSharedMode_Object((1,3,6,1,4,1,6027,3,16,1,1,18,1,3),_FpIfStatsPgSharedMode_Type())
fpIfStatsPgSharedMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfStatsPgSharedMode.setStatus(_A)
_FpIfStatsPgHdrmCells_Type=Integer32
_FpIfStatsPgHdrmCells_Object=MibTableColumn
fpIfStatsPgHdrmCells=_FpIfStatsPgHdrmCells_Object((1,3,6,1,4,1,6027,3,16,1,1,18,1,4),_FpIfStatsPgHdrmCells_Type())
fpIfStatsPgHdrmCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfStatsPgHdrmCells.setStatus(_A)
_FpIfStatsPgCounterMinCells_Type=Counter32
_FpIfStatsPgCounterMinCells_Object=MibTableColumn
fpIfStatsPgCounterMinCells=_FpIfStatsPgCounterMinCells_Object((1,3,6,1,4,1,6027,3,16,1,1,18,1,5),_FpIfStatsPgCounterMinCells_Type())
fpIfStatsPgCounterMinCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfStatsPgCounterMinCells.setStatus(_A)
_FpIfStatsPgCounterSharedCells_Type=Counter32
_FpIfStatsPgCounterSharedCells_Object=MibTableColumn
fpIfStatsPgCounterSharedCells=_FpIfStatsPgCounterSharedCells_Object((1,3,6,1,4,1,6027,3,16,1,1,18,1,6),_FpIfStatsPgCounterSharedCells_Type())
fpIfStatsPgCounterSharedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfStatsPgCounterSharedCells.setStatus(_A)
_FpIfStatsPgCounterHdrmCells_Type=Counter32
_FpIfStatsPgCounterHdrmCells_Object=MibTableColumn
fpIfStatsPgCounterHdrmCells=_FpIfStatsPgCounterHdrmCells_Object((1,3,6,1,4,1,6027,3,16,1,1,18,1,7),_FpIfStatsPgCounterHdrmCells_Type())
fpIfStatsPgCounterHdrmCells.setMaxAccess(_B)
if mibBuilder.loadTexts:fpIfStatsPgCounterHdrmCells.setStatus(_A)
_PfcPerPrioIfTable_Object=MibTable
pfcPerPrioIfTable=_PfcPerPrioIfTable_Object((1,3,6,1,4,1,6027,3,16,1,1,19))
if mibBuilder.loadTexts:pfcPerPrioIfTable.setStatus(_A)
_PfcPerPrioIfEntry_Object=MibTableRow
pfcPerPrioIfEntry=_PfcPerPrioIfEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,19,1))
pfcPerPrioIfEntry.setIndexNames((0,_H,_I),(0,_C,_V))
if mibBuilder.loadTexts:pfcPerPrioIfEntry.setStatus(_A)
class _IfPrioIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IfPrioIndex_Type.__name__=_F
_IfPrioIndex_Object=MibTableColumn
ifPrioIndex=_IfPrioIndex_Object((1,3,6,1,4,1,6027,3,16,1,1,19,1,1),_IfPrioIndex_Type())
ifPrioIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:ifPrioIndex.setStatus(_A)
_IfPfcPerPrioRequests_Type=Counter64
_IfPfcPerPrioRequests_Object=MibTableColumn
ifPfcPerPrioRequests=_IfPfcPerPrioRequests_Object((1,3,6,1,4,1,6027,3,16,1,1,19,1,2),_IfPfcPerPrioRequests_Type())
ifPfcPerPrioRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPfcPerPrioRequests.setStatus(_A)
if mibBuilder.loadTexts:ifPfcPerPrioRequests.setUnits(_T)
_IfPfcPerPrioIndications_Type=Counter64
_IfPfcPerPrioIndications_Object=MibTableColumn
ifPfcPerPrioIndications=_IfPfcPerPrioIndications_Object((1,3,6,1,4,1,6027,3,16,1,1,19,1,3),_IfPfcPerPrioIndications_Type())
ifPfcPerPrioIndications.setMaxAccess(_B)
if mibBuilder.loadTexts:ifPfcPerPrioIndications.setStatus(_A)
if mibBuilder.loadTexts:ifPfcPerPrioIndications.setUnits(_U)
_FpEgrQIfCounterTable_Object=MibTable
fpEgrQIfCounterTable=_FpEgrQIfCounterTable_Object((1,3,6,1,4,1,6027,3,16,1,1,20))
if mibBuilder.loadTexts:fpEgrQIfCounterTable.setStatus(_A)
_FpEgrQIfCounterEntry_Object=MibTableRow
fpEgrQIfCounterEntry=_FpEgrQIfCounterEntry_Object((1,3,6,1,4,1,6027,3,16,1,1,20,1))
fpEgrQIfCounterEntry.setIndexNames((0,_H,_I),(0,_C,_W),(0,_C,_K))
if mibBuilder.loadTexts:fpEgrQIfCounterEntry.setStatus(_A)
_FpEgrQComType_Type=ComType
_FpEgrQComType_Object=MibTableColumn
fpEgrQComType=_FpEgrQComType_Object((1,3,6,1,4,1,6027,3,16,1,1,20,1,1),_FpEgrQComType_Type())
fpEgrQComType.setMaxAccess(_G)
if mibBuilder.loadTexts:fpEgrQComType.setStatus(_A)
_FpEgrQTxPackets_Type=Counter64
_FpEgrQTxPackets_Object=MibTableColumn
fpEgrQTxPackets=_FpEgrQTxPackets_Object((1,3,6,1,4,1,6027,3,16,1,1,20,1,2),_FpEgrQTxPackets_Type())
fpEgrQTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgrQTxPackets.setStatus(_A)
_FpEgrQTxBytes_Type=Counter64
_FpEgrQTxBytes_Object=MibTableColumn
fpEgrQTxBytes=_FpEgrQTxBytes_Object((1,3,6,1,4,1,6027,3,16,1,1,20,1,3),_FpEgrQTxBytes_Type())
fpEgrQTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgrQTxBytes.setStatus(_A)
_FpEgrQDroppedPackets_Type=Counter64
_FpEgrQDroppedPackets_Object=MibTableColumn
fpEgrQDroppedPackets=_FpEgrQDroppedPackets_Object((1,3,6,1,4,1,6027,3,16,1,1,20,1,4),_FpEgrQDroppedPackets_Type())
fpEgrQDroppedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgrQDroppedPackets.setStatus(_A)
_FpEgrQDroppedBytes_Type=Counter64
_FpEgrQDroppedBytes_Object=MibTableColumn
fpEgrQDroppedBytes=_FpEgrQDroppedBytes_Object((1,3,6,1,4,1,6027,3,16,1,1,20,1,5),_FpEgrQDroppedBytes_Type())
fpEgrQDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:fpEgrQDroppedBytes.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ComType':ComType,'f10FpStatsMib':f10FpStatsMib,'f10FpStatsObject':f10FpStatsObject,'fpStatsObjects':fpStatsObjects,'fpCpuDataPlaneTable':fpCpuDataPlaneTable,'fpCpuDataPlaneStatsEntry':fpCpuDataPlaneStatsEntry,_E:fpStackUnitIndex,'fpRxHandle':fpRxHandle,'fpNoMhdr':fpNoMhdr,'fpNoMBuf':fpNoMBuf,'fpNoClus':fpNoClus,'fpRecvd':fpRecvd,'fpDropped':fpDropped,'fpRecvToNet':fpRecvToNet,'fpRxError':fpRxError,'fpRxDatapathError':fpRxDatapathError,'fpRxPktCOS0':fpRxPktCOS0,'fpRxPktCOS1':fpRxPktCOS1,'fpRxPktCOS2':fpRxPktCOS2,'fpRxPktCOS3':fpRxPktCOS3,'fpRxPktCOS4':fpRxPktCOS4,'fpRxPktCOS5':fpRxPktCOS5,'fpRxPktCOS6':fpRxPktCOS6,'fpRxPktCOS7':fpRxPktCOS7,'fpRxPktUnit0':fpRxPktUnit0,'fpRxPktUnit1':fpRxPktUnit1,'fpRxPktUnit2':fpRxPktUnit2,'fpRxPktUnit3':fpRxPktUnit3,'fpTransmitted':fpTransmitted,'fpTxRequested':fpTxRequested,'fpNoTxDesc':fpNoTxDesc,'fpTxError':fpTxError,'fpTxReqTooLarge':fpTxReqTooLarge,'fpTxInternalError':fpTxInternalError,'fpTxDatapathErr':fpTxDatapathErr,'fpTxPktCOS0':fpTxPktCOS0,'fpTxPktCOS1':fpTxPktCOS1,'fpTxPktCOS2':fpTxPktCOS2,'fpTxPktCOS3':fpTxPktCOS3,'fpTxPktCOS4':fpTxPktCOS4,'fpTxPktCOS5':fpTxPktCOS5,'fpTxPktCOS6':fpTxPktCOS6,'fpTxPktCOS7':fpTxPktCOS7,'fpTxPktUnit0':fpTxPktUnit0,'fpTxPktUnit1':fpTxPktUnit1,'fpTxPktUnit2':fpTxPktUnit2,'fpTxPktUnit3':fpTxPktUnit3,'fpCpuPartyBusTable':fpCpuPartyBusTable,'fpCpuPartyBusStatsEntry':fpCpuPartyBusStatsEntry,'fpPartyBusInputPackets':fpPartyBusInputPackets,'fpPartyBusInputBytes':fpPartyBusInputBytes,'fpPartyBusInputDropped':fpPartyBusInputDropped,'fpPartyBusInputError':fpPartyBusInputError,'fpPartyBusOutputPackets':fpPartyBusOutputPackets,'fpPartyBusOutputBytes':fpPartyBusOutputBytes,'fpPartyBusOutputError':fpPartyBusOutputError,'fpDropsTable':fpDropsTable,'fpDropsEntry':fpDropsEntry,_J:fpStackPortIndex,'fpIngressDrops':fpIngressDrops,'fpIngIBPCBPFullDrops':fpIngIBPCBPFullDrops,'fpIngPortSTPnotFwdDrops':fpIngPortSTPnotFwdDrops,'fpIngIPv4L3Discards':fpIngIPv4L3Discards,'fpIngPolicyDiscards':fpIngPolicyDiscards,'fpIngPacketsDroppedByFP':fpIngPacketsDroppedByFP,'fpIngL2L3Drops':fpIngL2L3Drops,'fpIngPortBitMapZeroDrops':fpIngPortBitMapZeroDrops,'fpIngRxVLANDrops':fpIngRxVLANDrops,'fpIngressFCSDrops':fpIngressFCSDrops,'fpIngressMTUExceeds':fpIngressMTUExceeds,'fpMMUHOLDrops':fpMMUHOLDrops,'fpMMUTxPurgeCellErr':fpMMUTxPurgeCellErr,'fpMMUAgedDrops':fpMMUAgedDrops,'fpEgressFCSDrops':fpEgressFCSDrops,'fpEgIPv4L3UCAgedDrops':fpEgIPv4L3UCAgedDrops,'fpEgTTLThresholdDrops':fpEgTTLThresholdDrops,'fpEgInvalidVLANCounterDrops':fpEgInvalidVLANCounterDrops,'fpEgL2MCDrops':fpEgL2MCDrops,'fpEgPktDropsOfAnyCondition':fpEgPktDropsOfAnyCondition,'fpEgHgMacUnderFlow':fpEgHgMacUnderFlow,'fpEgTxErrPktCounter':fpEgTxErrPktCounter,'fpFlowControlDrops':fpFlowControlDrops,'fpPacketBufferTable':fpPacketBufferTable,'fpPacketBufferEntry':fpPacketBufferEntry,_O:fpPortPipe,'fpTotalPacketBuffer':fpTotalPacketBuffer,'fpCurrentAvailBuffer':fpCurrentAvailBuffer,'fpPacketBufferAlloc':fpPacketBufferAlloc,'fpStatsPerPortTable':fpStatsPerPortTable,'fpStatsPerPortEntry':fpStatsPerPortEntry,'fpCurrentUsagePerPort':fpCurrentUsagePerPort,'fpDefaultPacketBuffAlloc':fpDefaultPacketBuffAlloc,'fpMaxLimitPerPort':fpMaxLimitPerPort,'fpStatsPerCOSTable':fpStatsPerCOSTable,'fpStatsPerCOSEntry':fpStatsPerCOSEntry,_K:fpPerPortCOSNumber,'fpCurrentUsagePerCOS':fpCurrentUsagePerCOS,'fpDefaultPacketBuffAllocPerCOS':fpDefaultPacketBuffAllocPerCOS,'fpMaxLimitPerCOS':fpMaxLimitPerCOS,'fpHOLDropsPerCOS':fpHOLDropsPerCOS,'fpCpuDataPlaneCOSTable':fpCpuDataPlaneCOSTable,'fpCpuDataPlaneCOSEntry':fpCpuDataPlaneCOSEntry,_P:fpCOSIndex,'fpRxPktCOS':fpRxPktCOS,'fpTxPktCOS':fpTxPktCOS,'fpEgrQBuffSnapshotTable':fpEgrQBuffSnapshotTable,'fpEgrQBuffSnapshotEntry':fpEgrQBuffSnapshotEntry,'fpEgrQTotBuffCells':fpEgrQTotBuffCells,'fpIngPgBuffSnapshotTable':fpIngPgBuffSnapshotTable,'fpIngPgBuffSnapshotEntry':fpIngPgBuffSnapshotEntry,_L:fpPerPortPGIndex,'fpIngSharedCells':fpIngSharedCells,'fpIngHeadroomCells':fpIngHeadroomCells,'fpStatsPerPgTable':fpStatsPerPgTable,'fpStatsPerPgEntry':fpStatsPerPgEntry,'fpStatsPgLimitMinCells':fpStatsPgLimitMinCells,'fpStatsPgSharedCells':fpStatsPgSharedCells,'fpStatsPgSharedMode':fpStatsPgSharedMode,'fpStatsPgHdrmCells':fpStatsPgHdrmCells,'fpStatsPgCounterMinCells':fpStatsPgCounterMinCells,'fpStatsPgCounterSharedCells':fpStatsPgCounterSharedCells,'fpStatsPgCounterHdrmCells':fpStatsPgCounterHdrmCells,'pfcPerPrioTable':pfcPerPrioTable,'pfcPerPrioEntry':pfcPerPrioEntry,_S:prioIndex,'pfcPerPrioRequests':pfcPerPrioRequests,'pfcPerPrioIndications':pfcPerPrioIndications,'fpCpuPartyBusPortStatsTable':fpCpuPartyBusPortStatsTable,'fpCpuPartyBusPortStatsEntry':fpCpuPartyBusPortStatsEntry,'fpCpuPartyBusPortStatsOutOctets':fpCpuPartyBusPortStatsOutOctets,'fpCpuPartyBusPortStatsOutDropPkts':fpCpuPartyBusPortStatsOutDropPkts,'fpCpuPartyBusPortStatsOutCOS0Pkts':fpCpuPartyBusPortStatsOutCOS0Pkts,'fpCpuPartyBusPortStatsOutCOS1Pkts':fpCpuPartyBusPortStatsOutCOS1Pkts,'fpCpuPartyBusPortStatsOutCOS2Pkts':fpCpuPartyBusPortStatsOutCOS2Pkts,'fpCpuPartyBusPortStatsOutCOS3Pkts':fpCpuPartyBusPortStatsOutCOS3Pkts,'fpCpuPartyBusPortStatsOutCOS4Pkts':fpCpuPartyBusPortStatsOutCOS4Pkts,'fpCpuPartyBusPortStatsOutCOS5Pkts':fpCpuPartyBusPortStatsOutCOS5Pkts,'fpCpuPartyBusPortStatsOutUnicastPkts':fpCpuPartyBusPortStatsOutUnicastPkts,'fpCpuPartyBusPortStatsOutMulticastPkts':fpCpuPartyBusPortStatsOutMulticastPkts,'fpCpuPartyBusPortStatsOutBroadcastPkts':fpCpuPartyBusPortStatsOutBroadcastPkts,'fpCpuPartyBusPortStatsOutPausePkts':fpCpuPartyBusPortStatsOutPausePkts,'fpCpuPartyBusPortStatsOutCollisions':fpCpuPartyBusPortStatsOutCollisions,'fpCpuPartyBusPortStatsOutSingleCollisions':fpCpuPartyBusPortStatsOutSingleCollisions,'fpCpuPartyBusPortStatsOutMultiCollisions':fpCpuPartyBusPortStatsOutMultiCollisions,'fpCpuPartyBusPortStatsOutLateCollisions':fpCpuPartyBusPortStatsOutLateCollisions,'fpCpuPartyBusPortStatsOutExcessCollisions':fpCpuPartyBusPortStatsOutExcessCollisions,'fpCpuPartyBusPortStatsOutDeferred':fpCpuPartyBusPortStatsOutDeferred,'fpCpuPartyBusPortStatsOutDiscarded':fpCpuPartyBusPortStatsOutDiscarded,'fpCpuPartyBusPortStatsInOctets':fpCpuPartyBusPortStatsInOctets,'fpCpuPartyBusPortStatsInUndersizePkts':fpCpuPartyBusPortStatsInUndersizePkts,'fpCpuPartyBusPortStatsInOversizePkts':fpCpuPartyBusPortStatsInOversizePkts,'fpCpuPartyBusPortStatsInPausePkts':fpCpuPartyBusPortStatsInPausePkts,'fpCpuPartyBusPortStatsIn64OctetPkts':fpCpuPartyBusPortStatsIn64OctetPkts,'fpCpuPartyBusPortStatsIn65To127OctetPkts':fpCpuPartyBusPortStatsIn65To127OctetPkts,'fpCpuPartyBusPortStatsIn128To255OctetPkts':fpCpuPartyBusPortStatsIn128To255OctetPkts,'fpCpuPartyBusPortStatsIn256To511OctetPkts':fpCpuPartyBusPortStatsIn256To511OctetPkts,'fpCpuPartyBusPortStatsIn512To1023OctetPkts':fpCpuPartyBusPortStatsIn512To1023OctetPkts,'fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts':fpCpuPartyBusPortStatsIn1024ToMaxOctetPkts,'fpCpuPartyBusPortStatsInJabbers':fpCpuPartyBusPortStatsInJabbers,'fpCpuPartyBusPortStatsInAlignErrors':fpCpuPartyBusPortStatsInAlignErrors,'fpCpuPartyBusPortStatsInFcsErrors':fpCpuPartyBusPortStatsInFcsErrors,'fpCpuPartyBusPortStatsInGoodOctets':fpCpuPartyBusPortStatsInGoodOctets,'fpCpuPartyBusPortStatsInDropPkts':fpCpuPartyBusPortStatsInDropPkts,'fpCpuPartyBusPortStatsInUnicastPkts':fpCpuPartyBusPortStatsInUnicastPkts,'fpCpuPartyBusPortStatsInMulticastPkts':fpCpuPartyBusPortStatsInMulticastPkts,'fpCpuPartyBusPortStatsInBroadcastPkts':fpCpuPartyBusPortStatsInBroadcastPkts,'fpCpuPartyBusPortStatsInSrcAddrChanges':fpCpuPartyBusPortStatsInSrcAddrChanges,'fpCpuPartyBusPortStatsInFragments':fpCpuPartyBusPortStatsInFragments,'fpCpuPartyBusPortStatsInJumboPkts':fpCpuPartyBusPortStatsInJumboPkts,'fpCpuPartyBusPortStatsInSymbolErrors':fpCpuPartyBusPortStatsInSymbolErrors,'fpCpuPartyBusPortStatsInInRangeErrors':fpCpuPartyBusPortStatsInInRangeErrors,'fpCpuPartyBusPortStatsInOutRangeErrors':fpCpuPartyBusPortStatsInOutRangeErrors,'fpDropsIfTable':fpDropsIfTable,'fpDropsIfEntry':fpDropsIfEntry,'fpIfIngressDrops':fpIfIngressDrops,'fpIfIngIBPCBPFullDrops':fpIfIngIBPCBPFullDrops,'fpIfIngPortSTPnotFwdDrops':fpIfIngPortSTPnotFwdDrops,'fpIfIngIPv4L3Discards':fpIfIngIPv4L3Discards,'fpIfIngPolicyDiscards':fpIfIngPolicyDiscards,'fpIfIngPacketsDroppedByFP':fpIfIngPacketsDroppedByFP,'fpIfIngL2L3Drops':fpIfIngL2L3Drops,'fpIfIngPortBitMapZeroDrops':fpIfIngPortBitMapZeroDrops,'fpIfIngRxVLANDrops':fpIfIngRxVLANDrops,'fpIfIngressFCSDrops':fpIfIngressFCSDrops,'fpIfIngressMTUExceeds':fpIfIngressMTUExceeds,'fpIfMMUHOLDrops':fpIfMMUHOLDrops,'fpIfMMUTxPurgeCellErr':fpIfMMUTxPurgeCellErr,'fpIfMMUAgedDrops':fpIfMMUAgedDrops,'fpIfEgressFCSDrops':fpIfEgressFCSDrops,'fpIfEgIPv4L3UCAgedDrops':fpIfEgIPv4L3UCAgedDrops,'fpIfEgTTLThresholdDrops':fpIfEgTTLThresholdDrops,'fpIfEgInvalidVLANCounterDrops':fpIfEgInvalidVLANCounterDrops,'fpIfEgL2MCDrops':fpIfEgL2MCDrops,'fpIfEgPktDropsOfAnyCondition':fpIfEgPktDropsOfAnyCondition,'fpIfEgHgMacUnderFlow':fpIfEgHgMacUnderFlow,'fpIfEgTxErrPktCounter':fpIfEgTxErrPktCounter,'fpStatsPerIfTable':fpStatsPerIfTable,'fpStatsPerIfEntry':fpStatsPerIfEntry,'fpIfCurrentUsagePerPort':fpIfCurrentUsagePerPort,'fpIfDefaultPacketBuffAlloc':fpIfDefaultPacketBuffAlloc,'fpIfMaxLimitPerPort':fpIfMaxLimitPerPort,'fpStatsPerIfCOSTable':fpStatsPerIfCOSTable,'fpStatsPerIfCOSEntry':fpStatsPerIfCOSEntry,_M:fpIfPerCOSNumber,'fpIfCurrentUsagePerCOS':fpIfCurrentUsagePerCOS,'fpIfDefaultPacketBuffAllocPerCOS':fpIfDefaultPacketBuffAllocPerCOS,'fpIfMaxLimitPerCOS':fpIfMaxLimitPerCOS,'fpIfHOLDropsPerCOS':fpIfHOLDropsPerCOS,'fpEgrQBuffSnapshotIfTable':fpEgrQBuffSnapshotIfTable,'fpEgrQBuffSnapshotIfEntry':fpEgrQBuffSnapshotIfEntry,'fpIfEgrQTotBuffCells':fpIfEgrQTotBuffCells,'fpIngPgBuffSnapshotIfTable':fpIngPgBuffSnapshotIfTable,'fpIngPgBuffSnapshotIfEntry':fpIngPgBuffSnapshotIfEntry,_N:fpIfPerPGIndex,'fpIfIngSharedCells':fpIfIngSharedCells,'fpIfIngHeadroomCells':fpIfIngHeadroomCells,'fpStatsPerPgIfTable':fpStatsPerPgIfTable,'fpStatsPerPgIfEntry':fpStatsPerPgIfEntry,'fpIfStatsPgLimitMinCells':fpIfStatsPgLimitMinCells,'fpIfStatsPgSharedCells':fpIfStatsPgSharedCells,'fpIfStatsPgSharedMode':fpIfStatsPgSharedMode,'fpIfStatsPgHdrmCells':fpIfStatsPgHdrmCells,'fpIfStatsPgCounterMinCells':fpIfStatsPgCounterMinCells,'fpIfStatsPgCounterSharedCells':fpIfStatsPgCounterSharedCells,'fpIfStatsPgCounterHdrmCells':fpIfStatsPgCounterHdrmCells,'pfcPerPrioIfTable':pfcPerPrioIfTable,'pfcPerPrioIfEntry':pfcPerPrioIfEntry,_V:ifPrioIndex,'ifPfcPerPrioRequests':ifPfcPerPrioRequests,'ifPfcPerPrioIndications':ifPfcPerPrioIndications,'fpEgrQIfCounterTable':fpEgrQIfCounterTable,'fpEgrQIfCounterEntry':fpEgrQIfCounterEntry,_W:fpEgrQComType,'fpEgrQTxPackets':fpEgrQTxPackets,'fpEgrQTxBytes':fpEgrQTxBytes,'fpEgrQDroppedPackets':fpEgrQDroppedPackets,'fpEgrQDroppedBytes':fpEgrQDroppedBytes})