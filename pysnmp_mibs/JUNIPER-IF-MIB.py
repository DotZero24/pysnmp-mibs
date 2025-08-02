_R='ifChassisPort'
_Q='ifChassisPic'
_P='ifChassisFpc'
_O='ifJnxInL2ChanErrors'
_N='ifJnxFcsErrors'
_M='ifJnxCrcErrors'
_L='ifChassisEntry'
_K='ifJnxEntry'
_J='fullDuplex'
_I='halfDuplex'
_H='others'
_G='2015-10-15 00:00'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='JUNIPER-IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
ifEntry,ifIndex=mibBuilder.importSymbols(_D,'ifEntry',_E)
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ifJnx=ModuleIdentity((1,3,6,1,4,1,2636,3,3))
if mibBuilder.loadTexts:ifJnx.setRevisions(('2011-05-10 00:00','2011-09-22 00:00','2007-06-05 00:00','2002-10-31 00:00','2001-06-21 00:00','2001-03-15 00:00',_G,_G,'2020-01-01 00:00','2020-09-19 00:00','2022-09-01 00:00'))
_IfJnxTable_Object=MibTable
ifJnxTable=_IfJnxTable_Object((1,3,6,1,4,1,2636,3,3,1))
if mibBuilder.loadTexts:ifJnxTable.setStatus(_A)
_IfJnxEntry_Object=MibTableRow
ifJnxEntry=_IfJnxEntry_Object((1,3,6,1,4,1,2636,3,3,1,1))
if mibBuilder.loadTexts:ifJnxEntry.setStatus(_A)
_IfIn1SecRate_Type=Gauge32
_IfIn1SecRate_Object=MibTableColumn
ifIn1SecRate=_IfIn1SecRate_Object((1,3,6,1,4,1,2636,3,3,1,1,1),_IfIn1SecRate_Type())
ifIn1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIn1SecRate.setStatus(_A)
_IfIn1SecOctets_Type=Gauge32
_IfIn1SecOctets_Object=MibTableColumn
ifIn1SecOctets=_IfIn1SecOctets_Object((1,3,6,1,4,1,2636,3,3,1,1,2),_IfIn1SecOctets_Type())
ifIn1SecOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIn1SecOctets.setStatus(_A)
_IfIn1SecPkts_Type=Gauge32
_IfIn1SecPkts_Object=MibTableColumn
ifIn1SecPkts=_IfIn1SecPkts_Object((1,3,6,1,4,1,2636,3,3,1,1,3),_IfIn1SecPkts_Type())
ifIn1SecPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifIn1SecPkts.setStatus(_A)
_IfOut1SecRate_Type=Gauge32
_IfOut1SecRate_Object=MibTableColumn
ifOut1SecRate=_IfOut1SecRate_Object((1,3,6,1,4,1,2636,3,3,1,1,4),_IfOut1SecRate_Type())
ifOut1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOut1SecRate.setStatus(_A)
_IfOut1SecOctets_Type=Gauge32
_IfOut1SecOctets_Object=MibTableColumn
ifOut1SecOctets=_IfOut1SecOctets_Object((1,3,6,1,4,1,2636,3,3,1,1,5),_IfOut1SecOctets_Type())
ifOut1SecOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOut1SecOctets.setStatus(_A)
_IfOut1SecPkts_Type=Gauge32
_IfOut1SecPkts_Object=MibTableColumn
ifOut1SecPkts=_IfOut1SecPkts_Object((1,3,6,1,4,1,2636,3,3,1,1,6),_IfOut1SecPkts_Type())
ifOut1SecPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifOut1SecPkts.setStatus(_A)
_IfHCIn1SecRate_Type=CounterBasedGauge64
_IfHCIn1SecRate_Object=MibTableColumn
ifHCIn1SecRate=_IfHCIn1SecRate_Object((1,3,6,1,4,1,2636,3,3,1,1,7),_IfHCIn1SecRate_Type())
ifHCIn1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCIn1SecRate.setStatus(_A)
_IfHCOut1SecRate_Type=CounterBasedGauge64
_IfHCOut1SecRate_Object=MibTableColumn
ifHCOut1SecRate=_IfHCOut1SecRate_Object((1,3,6,1,4,1,2636,3,3,1,1,8),_IfHCOut1SecRate_Type())
ifHCOut1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCOut1SecRate.setStatus(_A)
_IfJnxInErrors_Type=Counter64
_IfJnxInErrors_Object=MibTableColumn
ifJnxInErrors=_IfJnxInErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,9),_IfJnxInErrors_Type())
ifJnxInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInErrors.setStatus(_A)
_IfJnxInFrameErrors_Type=Counter64
_IfJnxInFrameErrors_Object=MibTableColumn
ifJnxInFrameErrors=_IfJnxInFrameErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,10),_IfJnxInFrameErrors_Type())
ifJnxInFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInFrameErrors.setStatus(_A)
_IfJnxInQDrops_Type=Counter64
_IfJnxInQDrops_Object=MibTableColumn
ifJnxInQDrops=_IfJnxInQDrops_Object((1,3,6,1,4,1,2636,3,3,1,1,11),_IfJnxInQDrops_Type())
ifJnxInQDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInQDrops.setStatus(_A)
_IfJnxInRunts_Type=Counter64
_IfJnxInRunts_Object=MibTableColumn
ifJnxInRunts=_IfJnxInRunts_Object((1,3,6,1,4,1,2636,3,3,1,1,12),_IfJnxInRunts_Type())
ifJnxInRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInRunts.setStatus(_A)
_IfJnxInGiants_Type=Counter64
_IfJnxInGiants_Object=MibTableColumn
ifJnxInGiants=_IfJnxInGiants_Object((1,3,6,1,4,1,2636,3,3,1,1,13),_IfJnxInGiants_Type())
ifJnxInGiants.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInGiants.setStatus(_A)
_IfJnxInDiscards_Type=Counter64
_IfJnxInDiscards_Object=MibTableColumn
ifJnxInDiscards=_IfJnxInDiscards_Object((1,3,6,1,4,1,2636,3,3,1,1,14),_IfJnxInDiscards_Type())
ifJnxInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInDiscards.setStatus(_A)
_IfJnxInHslCrcErrors_Type=Counter64
_IfJnxInHslCrcErrors_Object=MibTableColumn
ifJnxInHslCrcErrors=_IfJnxInHslCrcErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,15),_IfJnxInHslCrcErrors_Type())
ifJnxInHslCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInHslCrcErrors.setStatus(_A)
_IfJnxInHslFifoOverFlows_Type=Counter64
_IfJnxInHslFifoOverFlows_Object=MibTableColumn
ifJnxInHslFifoOverFlows=_IfJnxInHslFifoOverFlows_Object((1,3,6,1,4,1,2636,3,3,1,1,16),_IfJnxInHslFifoOverFlows_Type())
ifJnxInHslFifoOverFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInHslFifoOverFlows.setStatus(_A)
_IfJnxInL3Incompletes_Type=Counter64
_IfJnxInL3Incompletes_Object=MibTableColumn
ifJnxInL3Incompletes=_IfJnxInL3Incompletes_Object((1,3,6,1,4,1,2636,3,3,1,1,17),_IfJnxInL3Incompletes_Type())
ifJnxInL3Incompletes.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInL3Incompletes.setStatus(_A)
_IfJnxInL2ChanErrors_Type=Counter64
_IfJnxInL2ChanErrors_Object=MibTableColumn
ifJnxInL2ChanErrors=_IfJnxInL2ChanErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,18),_IfJnxInL2ChanErrors_Type())
ifJnxInL2ChanErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInL2ChanErrors.setStatus(_A)
_IfJnxInL2MismatchTimeouts_Type=Counter64
_IfJnxInL2MismatchTimeouts_Object=MibTableColumn
ifJnxInL2MismatchTimeouts=_IfJnxInL2MismatchTimeouts_Object((1,3,6,1,4,1,2636,3,3,1,1,19),_IfJnxInL2MismatchTimeouts_Type())
ifJnxInL2MismatchTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInL2MismatchTimeouts.setStatus(_A)
_IfJnxInInvalidVCs_Type=Counter64
_IfJnxInInvalidVCs_Object=MibTableColumn
ifJnxInInvalidVCs=_IfJnxInInvalidVCs_Object((1,3,6,1,4,1,2636,3,3,1,1,20),_IfJnxInInvalidVCs_Type())
ifJnxInInvalidVCs.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInInvalidVCs.setStatus(_A)
_IfJnxInFifoErrors_Type=Counter32
_IfJnxInFifoErrors_Object=MibTableColumn
ifJnxInFifoErrors=_IfJnxInFifoErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,21),_IfJnxInFifoErrors_Type())
ifJnxInFifoErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInFifoErrors.setStatus(_A)
_IfJnxBucketDrops_Type=Counter64
_IfJnxBucketDrops_Object=MibTableColumn
ifJnxBucketDrops=_IfJnxBucketDrops_Object((1,3,6,1,4,1,2636,3,3,1,1,22),_IfJnxBucketDrops_Type())
ifJnxBucketDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxBucketDrops.setStatus(_A)
_IfJnxSramErrors_Type=Counter32
_IfJnxSramErrors_Object=MibTableColumn
ifJnxSramErrors=_IfJnxSramErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,23),_IfJnxSramErrors_Type())
ifJnxSramErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxSramErrors.setStatus(_A)
_IfJnxOutErrors_Type=Counter64
_IfJnxOutErrors_Object=MibTableColumn
ifJnxOutErrors=_IfJnxOutErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,24),_IfJnxOutErrors_Type())
ifJnxOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutErrors.setStatus(_A)
_IfJnxCollisions_Type=Counter64
_IfJnxCollisions_Object=MibTableColumn
ifJnxCollisions=_IfJnxCollisions_Object((1,3,6,1,4,1,2636,3,3,1,1,25),_IfJnxCollisions_Type())
ifJnxCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxCollisions.setStatus(_A)
_IfJnxCarrierTrans_Type=Counter64
_IfJnxCarrierTrans_Object=MibTableColumn
ifJnxCarrierTrans=_IfJnxCarrierTrans_Object((1,3,6,1,4,1,2636,3,3,1,1,26),_IfJnxCarrierTrans_Type())
ifJnxCarrierTrans.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxCarrierTrans.setStatus(_A)
_IfJnxOutQDrops_Type=Counter64
_IfJnxOutQDrops_Object=MibTableColumn
ifJnxOutQDrops=_IfJnxOutQDrops_Object((1,3,6,1,4,1,2636,3,3,1,1,27),_IfJnxOutQDrops_Type())
ifJnxOutQDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutQDrops.setStatus(_A)
_IfJnxOutAgedErrors_Type=Counter64
_IfJnxOutAgedErrors_Object=MibTableColumn
ifJnxOutAgedErrors=_IfJnxOutAgedErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,28),_IfJnxOutAgedErrors_Type())
ifJnxOutAgedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutAgedErrors.setStatus(_A)
_IfJnxOutFifoErrors_Type=Counter32
_IfJnxOutFifoErrors_Object=MibTableColumn
ifJnxOutFifoErrors=_IfJnxOutFifoErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,29),_IfJnxOutFifoErrors_Type())
ifJnxOutFifoErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutFifoErrors.setStatus(_A)
_IfJnxOutHslFifoUnderFlows_Type=Counter64
_IfJnxOutHslFifoUnderFlows_Object=MibTableColumn
ifJnxOutHslFifoUnderFlows=_IfJnxOutHslFifoUnderFlows_Object((1,3,6,1,4,1,2636,3,3,1,1,30),_IfJnxOutHslFifoUnderFlows_Type())
ifJnxOutHslFifoUnderFlows.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutHslFifoUnderFlows.setStatus(_A)
_IfJnxOutHslCrcErrors_Type=Counter32
_IfJnxOutHslCrcErrors_Object=MibTableColumn
ifJnxOutHslCrcErrors=_IfJnxOutHslCrcErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,31),_IfJnxOutHslCrcErrors_Type())
ifJnxOutHslCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutHslCrcErrors.setStatus(_A)
_IfJnxCrcErrors_Type=Counter64
_IfJnxCrcErrors_Object=MibTableColumn
ifJnxCrcErrors=_IfJnxCrcErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,32),_IfJnxCrcErrors_Type())
ifJnxCrcErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxCrcErrors.setStatus(_A)
_IfJnxFcsErrors_Type=Counter64
_IfJnxFcsErrors_Object=MibTableColumn
ifJnxFcsErrors=_IfJnxFcsErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,33),_IfJnxFcsErrors_Type())
ifJnxFcsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxFcsErrors.setStatus(_A)
_IfHCIn1SecOctets_Type=CounterBasedGauge64
_IfHCIn1SecOctets_Object=MibTableColumn
ifHCIn1SecOctets=_IfHCIn1SecOctets_Object((1,3,6,1,4,1,2636,3,3,1,1,34),_IfHCIn1SecOctets_Type())
ifHCIn1SecOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCIn1SecOctets.setStatus(_A)
_IfHCOut1SecOctets_Type=CounterBasedGauge64
_IfHCOut1SecOctets_Object=MibTableColumn
ifHCOut1SecOctets=_IfHCOut1SecOctets_Object((1,3,6,1,4,1,2636,3,3,1,1,35),_IfHCOut1SecOctets_Type())
ifHCOut1SecOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifHCOut1SecOctets.setStatus(_A)
_IfJnxInputErrors_Type=Counter64
_IfJnxInputErrors_Object=MibTableColumn
ifJnxInputErrors=_IfJnxInputErrors_Object((1,3,6,1,4,1,2636,3,3,1,1,36),_IfJnxInputErrors_Type())
ifJnxInputErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInputErrors.setStatus(_A)
_IfJnxOutEcnMarkedPackets_Type=Counter64
_IfJnxOutEcnMarkedPackets_Object=MibTableColumn
ifJnxOutEcnMarkedPackets=_IfJnxOutEcnMarkedPackets_Object((1,3,6,1,4,1,2636,3,3,1,1,37),_IfJnxOutEcnMarkedPackets_Type())
ifJnxOutEcnMarkedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutEcnMarkedPackets.setStatus(_A)
_IfChassisTable_Object=MibTable
ifChassisTable=_IfChassisTable_Object((1,3,6,1,4,1,2636,3,3,2))
if mibBuilder.loadTexts:ifChassisTable.setStatus(_A)
_IfChassisEntry_Object=MibTableRow
ifChassisEntry=_IfChassisEntry_Object((1,3,6,1,4,1,2636,3,3,2,1))
if mibBuilder.loadTexts:ifChassisEntry.setStatus(_A)
_IfChassisFpc_Type=Integer32
_IfChassisFpc_Object=MibTableColumn
ifChassisFpc=_IfChassisFpc_Object((1,3,6,1,4,1,2636,3,3,2,1,1),_IfChassisFpc_Type())
ifChassisFpc.setMaxAccess(_B)
if mibBuilder.loadTexts:ifChassisFpc.setStatus(_A)
_IfChassisPic_Type=Integer32
_IfChassisPic_Object=MibTableColumn
ifChassisPic=_IfChassisPic_Object((1,3,6,1,4,1,2636,3,3,2,1,2),_IfChassisPic_Type())
ifChassisPic.setMaxAccess(_B)
if mibBuilder.loadTexts:ifChassisPic.setStatus(_A)
_IfChassisPort_Type=Integer32
_IfChassisPort_Object=MibTableColumn
ifChassisPort=_IfChassisPort_Object((1,3,6,1,4,1,2636,3,3,2,1,3),_IfChassisPort_Type())
ifChassisPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ifChassisPort.setStatus(_A)
_IfChassisChannel_Type=Integer32
_IfChassisChannel_Object=MibTableColumn
ifChassisChannel=_IfChassisChannel_Object((1,3,6,1,4,1,2636,3,3,2,1,4),_IfChassisChannel_Type())
ifChassisChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:ifChassisChannel.setStatus(_A)
_IfChassisLogicalUnit_Type=Unsigned32
_IfChassisLogicalUnit_Object=MibTableColumn
ifChassisLogicalUnit=_IfChassisLogicalUnit_Object((1,3,6,1,4,1,2636,3,3,2,1,5),_IfChassisLogicalUnit_Type())
ifChassisLogicalUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:ifChassisLogicalUnit.setStatus(_A)
_IfChassisPicIndex_Type=OctetString
_IfChassisPicIndex_Object=MibTableColumn
ifChassisPicIndex=_IfChassisPicIndex_Object((1,3,6,1,4,1,2636,3,3,2,1,6),_IfChassisPicIndex_Type())
ifChassisPicIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifChassisPicIndex.setStatus(_A)
_IfJnxNotification_ObjectIdentity=ObjectIdentity
ifJnxNotification=_IfJnxNotification_ObjectIdentity((1,3,6,1,4,1,2636,3,3,3))
_IfJnxNotificationPrefix_ObjectIdentity=ObjectIdentity
ifJnxNotificationPrefix=_IfJnxNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2636,3,3,3,0))
_IfJnxPolTable_Object=MibTable
ifJnxPolTable=_IfJnxPolTable_Object((1,3,6,1,4,1,2636,3,3,4))
if mibBuilder.loadTexts:ifJnxPolTable.setStatus(_A)
_IfJnxPolEntry_Object=MibTableRow
ifJnxPolEntry=_IfJnxPolEntry_Object((1,3,6,1,4,1,2636,3,3,4,1))
ifJnxPolEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ifJnxPolEntry.setStatus(_A)
_IfJnxInPolLowOctets_Type=Counter64
_IfJnxInPolLowOctets_Object=MibTableColumn
ifJnxInPolLowOctets=_IfJnxInPolLowOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,1),_IfJnxInPolLowOctets_Type())
ifJnxInPolLowOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolLowOctets.setStatus(_A)
_IfJnxInPolLowPkts_Type=Counter64
_IfJnxInPolLowPkts_Object=MibTableColumn
ifJnxInPolLowPkts=_IfJnxInPolLowPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,2),_IfJnxInPolLowPkts_Type())
ifJnxInPolLowPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolLowPkts.setStatus(_A)
_IfJnxInPolLow1SecRate_Type=Counter64
_IfJnxInPolLow1SecRate_Object=MibTableColumn
ifJnxInPolLow1SecRate=_IfJnxInPolLow1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,3),_IfJnxInPolLow1SecRate_Type())
ifJnxInPolLow1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolLow1SecRate.setStatus(_A)
_IfJnxInPolMLowOctets_Type=Counter64
_IfJnxInPolMLowOctets_Object=MibTableColumn
ifJnxInPolMLowOctets=_IfJnxInPolMLowOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,4),_IfJnxInPolMLowOctets_Type())
ifJnxInPolMLowOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolMLowOctets.setStatus(_A)
_IfJnxInPolMLowPkts_Type=Counter64
_IfJnxInPolMLowPkts_Object=MibTableColumn
ifJnxInPolMLowPkts=_IfJnxInPolMLowPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,5),_IfJnxInPolMLowPkts_Type())
ifJnxInPolMLowPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolMLowPkts.setStatus(_A)
_IfJnxInPolMLow1SecRate_Type=Counter64
_IfJnxInPolMLow1SecRate_Object=MibTableColumn
ifJnxInPolMLow1SecRate=_IfJnxInPolMLow1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,6),_IfJnxInPolMLow1SecRate_Type())
ifJnxInPolMLow1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolMLow1SecRate.setStatus(_A)
_IfJnxInPolMHighOctets_Type=Counter64
_IfJnxInPolMHighOctets_Object=MibTableColumn
ifJnxInPolMHighOctets=_IfJnxInPolMHighOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,7),_IfJnxInPolMHighOctets_Type())
ifJnxInPolMHighOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolMHighOctets.setStatus(_A)
_IfJnxInPolMHighPkts_Type=Counter64
_IfJnxInPolMHighPkts_Object=MibTableColumn
ifJnxInPolMHighPkts=_IfJnxInPolMHighPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,8),_IfJnxInPolMHighPkts_Type())
ifJnxInPolMHighPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolMHighPkts.setStatus(_A)
_IfJnxInPolMHigh1SecRate_Type=Counter64
_IfJnxInPolMHigh1SecRate_Object=MibTableColumn
ifJnxInPolMHigh1SecRate=_IfJnxInPolMHigh1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,9),_IfJnxInPolMHigh1SecRate_Type())
ifJnxInPolMHigh1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolMHigh1SecRate.setStatus(_A)
_IfJnxInPolHighOctets_Type=Counter64
_IfJnxInPolHighOctets_Object=MibTableColumn
ifJnxInPolHighOctets=_IfJnxInPolHighOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,10),_IfJnxInPolHighOctets_Type())
ifJnxInPolHighOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolHighOctets.setStatus(_A)
_IfJnxInPolHighPkts_Type=Counter64
_IfJnxInPolHighPkts_Object=MibTableColumn
ifJnxInPolHighPkts=_IfJnxInPolHighPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,11),_IfJnxInPolHighPkts_Type())
ifJnxInPolHighPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolHighPkts.setStatus(_A)
_IfJnxInPolHigh1SecRate_Type=Counter64
_IfJnxInPolHigh1SecRate_Object=MibTableColumn
ifJnxInPolHigh1SecRate=_IfJnxInPolHigh1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,12),_IfJnxInPolHigh1SecRate_Type())
ifJnxInPolHigh1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolHigh1SecRate.setStatus(_A)
_IfJnxInPolDropOctets_Type=Counter64
_IfJnxInPolDropOctets_Object=MibTableColumn
ifJnxInPolDropOctets=_IfJnxInPolDropOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,13),_IfJnxInPolDropOctets_Type())
ifJnxInPolDropOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolDropOctets.setStatus(_A)
_IfJnxInPolDropPkts_Type=Counter64
_IfJnxInPolDropPkts_Object=MibTableColumn
ifJnxInPolDropPkts=_IfJnxInPolDropPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,14),_IfJnxInPolDropPkts_Type())
ifJnxInPolDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolDropPkts.setStatus(_A)
_IfJnxInPolDrop1SecRate_Type=Counter64
_IfJnxInPolDrop1SecRate_Object=MibTableColumn
ifJnxInPolDrop1SecRate=_IfJnxInPolDrop1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,15),_IfJnxInPolDrop1SecRate_Type())
ifJnxInPolDrop1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxInPolDrop1SecRate.setStatus(_A)
_IfJnxOutPolLowOctets_Type=Counter64
_IfJnxOutPolLowOctets_Object=MibTableColumn
ifJnxOutPolLowOctets=_IfJnxOutPolLowOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,16),_IfJnxOutPolLowOctets_Type())
ifJnxOutPolLowOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolLowOctets.setStatus(_A)
_IfJnxOutPolLowPkts_Type=Counter64
_IfJnxOutPolLowPkts_Object=MibTableColumn
ifJnxOutPolLowPkts=_IfJnxOutPolLowPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,17),_IfJnxOutPolLowPkts_Type())
ifJnxOutPolLowPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolLowPkts.setStatus(_A)
_IfJnxOutPolLow1SecRate_Type=Counter64
_IfJnxOutPolLow1SecRate_Object=MibTableColumn
ifJnxOutPolLow1SecRate=_IfJnxOutPolLow1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,18),_IfJnxOutPolLow1SecRate_Type())
ifJnxOutPolLow1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolLow1SecRate.setStatus(_A)
_IfJnxOutPolMLowOctets_Type=Counter64
_IfJnxOutPolMLowOctets_Object=MibTableColumn
ifJnxOutPolMLowOctets=_IfJnxOutPolMLowOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,19),_IfJnxOutPolMLowOctets_Type())
ifJnxOutPolMLowOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolMLowOctets.setStatus(_A)
_IfJnxOutPolMLowPkts_Type=Counter64
_IfJnxOutPolMLowPkts_Object=MibTableColumn
ifJnxOutPolMLowPkts=_IfJnxOutPolMLowPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,20),_IfJnxOutPolMLowPkts_Type())
ifJnxOutPolMLowPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolMLowPkts.setStatus(_A)
_IfJnxOutPolMLow1SecRate_Type=Counter64
_IfJnxOutPolMLow1SecRate_Object=MibTableColumn
ifJnxOutPolMLow1SecRate=_IfJnxOutPolMLow1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,21),_IfJnxOutPolMLow1SecRate_Type())
ifJnxOutPolMLow1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolMLow1SecRate.setStatus(_A)
_IfJnxOutPolMHighOctets_Type=Counter64
_IfJnxOutPolMHighOctets_Object=MibTableColumn
ifJnxOutPolMHighOctets=_IfJnxOutPolMHighOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,22),_IfJnxOutPolMHighOctets_Type())
ifJnxOutPolMHighOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolMHighOctets.setStatus(_A)
_IfJnxOutPolMHighPkts_Type=Counter64
_IfJnxOutPolMHighPkts_Object=MibTableColumn
ifJnxOutPolMHighPkts=_IfJnxOutPolMHighPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,23),_IfJnxOutPolMHighPkts_Type())
ifJnxOutPolMHighPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolMHighPkts.setStatus(_A)
_IfJnxOutPolMHigh1SecRate_Type=Counter64
_IfJnxOutPolMHigh1SecRate_Object=MibTableColumn
ifJnxOutPolMHigh1SecRate=_IfJnxOutPolMHigh1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,24),_IfJnxOutPolMHigh1SecRate_Type())
ifJnxOutPolMHigh1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolMHigh1SecRate.setStatus(_A)
_IfJnxOutPolHighOctets_Type=Counter64
_IfJnxOutPolHighOctets_Object=MibTableColumn
ifJnxOutPolHighOctets=_IfJnxOutPolHighOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,25),_IfJnxOutPolHighOctets_Type())
ifJnxOutPolHighOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolHighOctets.setStatus(_A)
_IfJnxOutPolHighPkts_Type=Counter64
_IfJnxOutPolHighPkts_Object=MibTableColumn
ifJnxOutPolHighPkts=_IfJnxOutPolHighPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,26),_IfJnxOutPolHighPkts_Type())
ifJnxOutPolHighPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolHighPkts.setStatus(_A)
_IfJnxOutPolHigh1SecRate_Type=Counter64
_IfJnxOutPolHigh1SecRate_Object=MibTableColumn
ifJnxOutPolHigh1SecRate=_IfJnxOutPolHigh1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,27),_IfJnxOutPolHigh1SecRate_Type())
ifJnxOutPolHigh1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolHigh1SecRate.setStatus(_A)
_IfJnxOutPolDropOctets_Type=Counter64
_IfJnxOutPolDropOctets_Object=MibTableColumn
ifJnxOutPolDropOctets=_IfJnxOutPolDropOctets_Object((1,3,6,1,4,1,2636,3,3,4,1,28),_IfJnxOutPolDropOctets_Type())
ifJnxOutPolDropOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolDropOctets.setStatus(_A)
_IfJnxOutPolDropPkts_Type=Counter64
_IfJnxOutPolDropPkts_Object=MibTableColumn
ifJnxOutPolDropPkts=_IfJnxOutPolDropPkts_Object((1,3,6,1,4,1,2636,3,3,4,1,29),_IfJnxOutPolDropPkts_Type())
ifJnxOutPolDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolDropPkts.setStatus(_A)
_IfJnxOutPolDrop1SecRate_Type=Counter64
_IfJnxOutPolDrop1SecRate_Object=MibTableColumn
ifJnxOutPolDrop1SecRate=_IfJnxOutPolDrop1SecRate_Object((1,3,6,1,4,1,2636,3,3,4,1,30),_IfJnxOutPolDrop1SecRate_Type())
ifJnxOutPolDrop1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxOutPolDrop1SecRate.setStatus(_A)
_IfJnxMediaTable_Object=MibTable
ifJnxMediaTable=_IfJnxMediaTable_Object((1,3,6,1,4,1,2636,3,3,5))
if mibBuilder.loadTexts:ifJnxMediaTable.setStatus(_A)
_IfJnxMediaEntry_Object=MibTableRow
ifJnxMediaEntry=_IfJnxMediaEntry_Object((1,3,6,1,4,1,2636,3,3,5,1))
ifJnxMediaEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ifJnxMediaEntry.setStatus(_A)
class _IfJnxMediaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('copper',1),('fiber',2),(_H,3)))
_IfJnxMediaType_Type.__name__=_F
_IfJnxMediaType_Object=MibTableColumn
ifJnxMediaType=_IfJnxMediaType_Object((1,3,6,1,4,1,2636,3,3,5,1,1),_IfJnxMediaType_Type())
ifJnxMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaType.setStatus(_A)
_IfJnxMediaConfigSpeed_Type=Gauge32
_IfJnxMediaConfigSpeed_Object=MibTableColumn
ifJnxMediaConfigSpeed=_IfJnxMediaConfigSpeed_Object((1,3,6,1,4,1,2636,3,3,5,1,2),_IfJnxMediaConfigSpeed_Type())
ifJnxMediaConfigSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaConfigSpeed.setStatus(_A)
_IfJnxMediaSpeed_Type=Gauge32
_IfJnxMediaSpeed_Object=MibTableColumn
ifJnxMediaSpeed=_IfJnxMediaSpeed_Object((1,3,6,1,4,1,2636,3,3,5,1,3),_IfJnxMediaSpeed_Type())
ifJnxMediaSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaSpeed.setStatus(_A)
_IfJnxMediaMaxSpeed_Type=Gauge32
_IfJnxMediaMaxSpeed_Object=MibTableColumn
ifJnxMediaMaxSpeed=_IfJnxMediaMaxSpeed_Object((1,3,6,1,4,1,2636,3,3,5,1,4),_IfJnxMediaMaxSpeed_Type())
ifJnxMediaMaxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaMaxSpeed.setStatus(_A)
class _IfJnxMediaMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),(_H,3)))
_IfJnxMediaMode_Type.__name__=_F
_IfJnxMediaMode_Object=MibTableColumn
ifJnxMediaMode=_IfJnxMediaMode_Object((1,3,6,1,4,1,2636,3,3,5,1,5),_IfJnxMediaMode_Type())
ifJnxMediaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaMode.setStatus(_A)
class _IfJnxMediaConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('auto',3)))
_IfJnxMediaConfigMode_Type.__name__=_F
_IfJnxMediaConfigMode_Object=MibTableColumn
ifJnxMediaConfigMode=_IfJnxMediaConfigMode_Object((1,3,6,1,4,1,2636,3,3,5,1,6),_IfJnxMediaConfigMode_Type())
ifJnxMediaConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaConfigMode.setStatus(_A)
_IfJnxMediaAutoNegotiationEnabled_Type=TruthValue
_IfJnxMediaAutoNegotiationEnabled_Object=MibTableColumn
ifJnxMediaAutoNegotiationEnabled=_IfJnxMediaAutoNegotiationEnabled_Object((1,3,6,1,4,1,2636,3,3,5,1,7),_IfJnxMediaAutoNegotiationEnabled_Type())
ifJnxMediaAutoNegotiationEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaAutoNegotiationEnabled.setStatus(_A)
_IfJnxMediaLastFlap_Type=TimeTicks
_IfJnxMediaLastFlap_Object=MibTableColumn
ifJnxMediaLastFlap=_IfJnxMediaLastFlap_Object((1,3,6,1,4,1,2636,3,3,5,1,8),_IfJnxMediaLastFlap_Type())
ifJnxMediaLastFlap.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaLastFlap.setStatus(_A)
_IfJnxMediaLastUpdate_Type=TimeTicks
_IfJnxMediaLastUpdate_Object=MibTableColumn
ifJnxMediaLastUpdate=_IfJnxMediaLastUpdate_Object((1,3,6,1,4,1,2636,3,3,5,1,9),_IfJnxMediaLastUpdate_Type())
ifJnxMediaLastUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaLastUpdate.setStatus(_A)
_IfJnxMediaConfigHighSpeed_Type=Gauge32
_IfJnxMediaConfigHighSpeed_Object=MibTableColumn
ifJnxMediaConfigHighSpeed=_IfJnxMediaConfigHighSpeed_Object((1,3,6,1,4,1,2636,3,3,5,1,10),_IfJnxMediaConfigHighSpeed_Type())
ifJnxMediaConfigHighSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaConfigHighSpeed.setStatus(_A)
class _IfJnxMediaConfigSpeedMap_Type(Bits):namedValues=NamedValues(*(('auto',0),('mbps10',1),('mbps100',2),('mbps1000',3),('mbps2500',4),('mbps5000',5),('mbps10000',6),('mbps25000',7),('mbps40000',8),('mbps50000',9),('mbps100000',10)))
_IfJnxMediaConfigSpeedMap_Type.__name__='Bits'
_IfJnxMediaConfigSpeedMap_Object=MibTableColumn
ifJnxMediaConfigSpeedMap=_IfJnxMediaConfigSpeedMap_Object((1,3,6,1,4,1,2636,3,3,5,1,11),_IfJnxMediaConfigSpeedMap_Type())
ifJnxMediaConfigSpeedMap.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaConfigSpeedMap.setStatus(_A)
_IfJnxMediaHighSpeed_Type=Gauge32
_IfJnxMediaHighSpeed_Object=MibTableColumn
ifJnxMediaHighSpeed=_IfJnxMediaHighSpeed_Object((1,3,6,1,4,1,2636,3,3,5,1,12),_IfJnxMediaHighSpeed_Type())
ifJnxMediaHighSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxMediaHighSpeed.setStatus(_A)
_IfJnxTrafficStatsTable_Object=MibTable
ifJnxTrafficStatsTable=_IfJnxTrafficStatsTable_Object((1,3,6,1,4,1,2636,3,3,6))
if mibBuilder.loadTexts:ifJnxTrafficStatsTable.setStatus(_A)
_IfJnxTrafficStatsEntry_Object=MibTableRow
ifJnxTrafficStatsEntry=_IfJnxTrafficStatsEntry_Object((1,3,6,1,4,1,2636,3,3,6,1))
ifJnxTrafficStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ifJnxTrafficStatsEntry.setStatus(_A)
_IfJnxLocalV4InPkts_Type=Counter64
_IfJnxLocalV4InPkts_Object=MibTableColumn
ifJnxLocalV4InPkts=_IfJnxLocalV4InPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,1),_IfJnxLocalV4InPkts_Type())
ifJnxLocalV4InPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxLocalV4InPkts.setStatus(_A)
_IfJnxLocalV4InOctets_Type=Counter64
_IfJnxLocalV4InOctets_Object=MibTableColumn
ifJnxLocalV4InOctets=_IfJnxLocalV4InOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,2),_IfJnxLocalV4InOctets_Type())
ifJnxLocalV4InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxLocalV4InOctets.setStatus(_A)
_IfJnxLocalV4OutPkts_Type=Counter64
_IfJnxLocalV4OutPkts_Object=MibTableColumn
ifJnxLocalV4OutPkts=_IfJnxLocalV4OutPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,3),_IfJnxLocalV4OutPkts_Type())
ifJnxLocalV4OutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxLocalV4OutPkts.setStatus(_A)
_IfJnxLocalV4OutOctets_Type=Counter64
_IfJnxLocalV4OutOctets_Object=MibTableColumn
ifJnxLocalV4OutOctets=_IfJnxLocalV4OutOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,4),_IfJnxLocalV4OutOctets_Type())
ifJnxLocalV4OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxLocalV4OutOctets.setStatus(_A)
_IfJnxTransitV4InPkts_Type=Counter64
_IfJnxTransitV4InPkts_Object=MibTableColumn
ifJnxTransitV4InPkts=_IfJnxTransitV4InPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,5),_IfJnxTransitV4InPkts_Type())
ifJnxTransitV4InPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV4InPkts.setStatus(_A)
_IfJnxTransitV4InOctets_Type=Counter64
_IfJnxTransitV4InOctets_Object=MibTableColumn
ifJnxTransitV4InOctets=_IfJnxTransitV4InOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,6),_IfJnxTransitV4InOctets_Type())
ifJnxTransitV4InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV4InOctets.setStatus(_A)
_IfJnxTransitV4OutPkts_Type=Counter64
_IfJnxTransitV4OutPkts_Object=MibTableColumn
ifJnxTransitV4OutPkts=_IfJnxTransitV4OutPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,7),_IfJnxTransitV4OutPkts_Type())
ifJnxTransitV4OutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV4OutPkts.setStatus(_A)
_IfJnxTransitV4OutOctets_Type=Counter64
_IfJnxTransitV4OutOctets_Object=MibTableColumn
ifJnxTransitV4OutOctets=_IfJnxTransitV4OutOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,8),_IfJnxTransitV4OutOctets_Type())
ifJnxTransitV4OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV4OutOctets.setStatus(_A)
_IfJnxTransitV4In1SecRate_Type=CounterBasedGauge64
_IfJnxTransitV4In1SecRate_Object=MibTableColumn
ifJnxTransitV4In1SecRate=_IfJnxTransitV4In1SecRate_Object((1,3,6,1,4,1,2636,3,3,6,1,9),_IfJnxTransitV4In1SecRate_Type())
ifJnxTransitV4In1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV4In1SecRate.setStatus(_A)
_IfJnxTransitV4In1SecOctets_Type=CounterBasedGauge64
_IfJnxTransitV4In1SecOctets_Object=MibTableColumn
ifJnxTransitV4In1SecOctets=_IfJnxTransitV4In1SecOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,10),_IfJnxTransitV4In1SecOctets_Type())
ifJnxTransitV4In1SecOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV4In1SecOctets.setStatus(_A)
_IfJnxTransitV4Out1SecRate_Type=CounterBasedGauge64
_IfJnxTransitV4Out1SecRate_Object=MibTableColumn
ifJnxTransitV4Out1SecRate=_IfJnxTransitV4Out1SecRate_Object((1,3,6,1,4,1,2636,3,3,6,1,11),_IfJnxTransitV4Out1SecRate_Type())
ifJnxTransitV4Out1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV4Out1SecRate.setStatus(_A)
_IfJnxTransitV4Out1SecOctets_Type=CounterBasedGauge64
_IfJnxTransitV4Out1SecOctets_Object=MibTableColumn
ifJnxTransitV4Out1SecOctets=_IfJnxTransitV4Out1SecOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,12),_IfJnxTransitV4Out1SecOctets_Type())
ifJnxTransitV4Out1SecOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV4Out1SecOctets.setStatus(_A)
_IfJnxTrafficV4InPkts_Type=Counter64
_IfJnxTrafficV4InPkts_Object=MibTableColumn
ifJnxTrafficV4InPkts=_IfJnxTrafficV4InPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,13),_IfJnxTrafficV4InPkts_Type())
ifJnxTrafficV4InPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTrafficV4InPkts.setStatus(_A)
_IfJnxTrafficV4InOctets_Type=Counter64
_IfJnxTrafficV4InOctets_Object=MibTableColumn
ifJnxTrafficV4InOctets=_IfJnxTrafficV4InOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,14),_IfJnxTrafficV4InOctets_Type())
ifJnxTrafficV4InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTrafficV4InOctets.setStatus(_A)
_IfJnxTrafficV4OutPkts_Type=Counter64
_IfJnxTrafficV4OutPkts_Object=MibTableColumn
ifJnxTrafficV4OutPkts=_IfJnxTrafficV4OutPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,15),_IfJnxTrafficV4OutPkts_Type())
ifJnxTrafficV4OutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTrafficV4OutPkts.setStatus(_A)
_IfJnxTrafficV4OutOctets_Type=Counter64
_IfJnxTrafficV4OutOctets_Object=MibTableColumn
ifJnxTrafficV4OutOctets=_IfJnxTrafficV4OutOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,16),_IfJnxTrafficV4OutOctets_Type())
ifJnxTrafficV4OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTrafficV4OutOctets.setStatus(_A)
_IfJnxLocalV6InPkts_Type=Counter64
_IfJnxLocalV6InPkts_Object=MibTableColumn
ifJnxLocalV6InPkts=_IfJnxLocalV6InPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,17),_IfJnxLocalV6InPkts_Type())
ifJnxLocalV6InPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxLocalV6InPkts.setStatus(_A)
_IfJnxLocalV6InOctets_Type=Counter64
_IfJnxLocalV6InOctets_Object=MibTableColumn
ifJnxLocalV6InOctets=_IfJnxLocalV6InOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,18),_IfJnxLocalV6InOctets_Type())
ifJnxLocalV6InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxLocalV6InOctets.setStatus(_A)
_IfJnxLocalV6OutPkts_Type=Counter64
_IfJnxLocalV6OutPkts_Object=MibTableColumn
ifJnxLocalV6OutPkts=_IfJnxLocalV6OutPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,19),_IfJnxLocalV6OutPkts_Type())
ifJnxLocalV6OutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxLocalV6OutPkts.setStatus(_A)
_IfJnxLocalV6OutOctets_Type=Counter64
_IfJnxLocalV6OutOctets_Object=MibTableColumn
ifJnxLocalV6OutOctets=_IfJnxLocalV6OutOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,20),_IfJnxLocalV6OutOctets_Type())
ifJnxLocalV6OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxLocalV6OutOctets.setStatus(_A)
_IfJnxTransitV6InPkts_Type=Counter64
_IfJnxTransitV6InPkts_Object=MibTableColumn
ifJnxTransitV6InPkts=_IfJnxTransitV6InPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,21),_IfJnxTransitV6InPkts_Type())
ifJnxTransitV6InPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV6InPkts.setStatus(_A)
_IfJnxTransitV6InOctets_Type=Counter64
_IfJnxTransitV6InOctets_Object=MibTableColumn
ifJnxTransitV6InOctets=_IfJnxTransitV6InOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,22),_IfJnxTransitV6InOctets_Type())
ifJnxTransitV6InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV6InOctets.setStatus(_A)
_IfJnxTransitV6OutPkts_Type=Counter64
_IfJnxTransitV6OutPkts_Object=MibTableColumn
ifJnxTransitV6OutPkts=_IfJnxTransitV6OutPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,23),_IfJnxTransitV6OutPkts_Type())
ifJnxTransitV6OutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV6OutPkts.setStatus(_A)
_IfJnxTransitV6OutOctets_Type=Counter64
_IfJnxTransitV6OutOctets_Object=MibTableColumn
ifJnxTransitV6OutOctets=_IfJnxTransitV6OutOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,24),_IfJnxTransitV6OutOctets_Type())
ifJnxTransitV6OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV6OutOctets.setStatus(_A)
_IfJnxTransitV6In1SecRate_Type=CounterBasedGauge64
_IfJnxTransitV6In1SecRate_Object=MibTableColumn
ifJnxTransitV6In1SecRate=_IfJnxTransitV6In1SecRate_Object((1,3,6,1,4,1,2636,3,3,6,1,25),_IfJnxTransitV6In1SecRate_Type())
ifJnxTransitV6In1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV6In1SecRate.setStatus(_A)
_IfJnxTransitV6In1SecOctets_Type=CounterBasedGauge64
_IfJnxTransitV6In1SecOctets_Object=MibTableColumn
ifJnxTransitV6In1SecOctets=_IfJnxTransitV6In1SecOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,26),_IfJnxTransitV6In1SecOctets_Type())
ifJnxTransitV6In1SecOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV6In1SecOctets.setStatus(_A)
_IfJnxTransitV6Out1SecRate_Type=CounterBasedGauge64
_IfJnxTransitV6Out1SecRate_Object=MibTableColumn
ifJnxTransitV6Out1SecRate=_IfJnxTransitV6Out1SecRate_Object((1,3,6,1,4,1,2636,3,3,6,1,27),_IfJnxTransitV6Out1SecRate_Type())
ifJnxTransitV6Out1SecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV6Out1SecRate.setStatus(_A)
_IfJnxTransitV6Out1SecOctets_Type=CounterBasedGauge64
_IfJnxTransitV6Out1SecOctets_Object=MibTableColumn
ifJnxTransitV6Out1SecOctets=_IfJnxTransitV6Out1SecOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,28),_IfJnxTransitV6Out1SecOctets_Type())
ifJnxTransitV6Out1SecOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTransitV6Out1SecOctets.setStatus(_A)
_IfJnxTrafficV6InPkts_Type=Counter64
_IfJnxTrafficV6InPkts_Object=MibTableColumn
ifJnxTrafficV6InPkts=_IfJnxTrafficV6InPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,29),_IfJnxTrafficV6InPkts_Type())
ifJnxTrafficV6InPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTrafficV6InPkts.setStatus(_A)
_IfJnxTrafficV6InOctets_Type=Counter64
_IfJnxTrafficV6InOctets_Object=MibTableColumn
ifJnxTrafficV6InOctets=_IfJnxTrafficV6InOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,30),_IfJnxTrafficV6InOctets_Type())
ifJnxTrafficV6InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTrafficV6InOctets.setStatus(_A)
_IfJnxTrafficV6OutPkts_Type=Counter64
_IfJnxTrafficV6OutPkts_Object=MibTableColumn
ifJnxTrafficV6OutPkts=_IfJnxTrafficV6OutPkts_Object((1,3,6,1,4,1,2636,3,3,6,1,31),_IfJnxTrafficV6OutPkts_Type())
ifJnxTrafficV6OutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTrafficV6OutPkts.setStatus(_A)
_IfJnxTrafficV6OutOctets_Type=Counter64
_IfJnxTrafficV6OutOctets_Object=MibTableColumn
ifJnxTrafficV6OutOctets=_IfJnxTrafficV6OutOctets_Object((1,3,6,1,4,1,2636,3,3,6,1,32),_IfJnxTrafficV6OutOctets_Type())
ifJnxTrafficV6OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ifJnxTrafficV6OutOctets.setStatus(_A)
ifEntry.registerAugmentions((_C,_K))
ifJnxEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions((_C,_L))
ifChassisEntry.setIndexNames(*ifEntry.getIndexNames())
ifJnxErrors=NotificationType((1,3,6,1,4,1,2636,3,3,3,0,1))
ifJnxErrors.setObjects(*((_C,_M),(_C,_N)))
if mibBuilder.loadTexts:ifJnxErrors.setStatus(_A)
ifJnxL2Errors=NotificationType((1,3,6,1,4,1,2636,3,3,3,0,2))
ifJnxL2Errors.setObjects(*((_C,_O),(_C,_P),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:ifJnxL2Errors.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ifJnx':ifJnx,'ifJnxTable':ifJnxTable,_K:ifJnxEntry,'ifIn1SecRate':ifIn1SecRate,'ifIn1SecOctets':ifIn1SecOctets,'ifIn1SecPkts':ifIn1SecPkts,'ifOut1SecRate':ifOut1SecRate,'ifOut1SecOctets':ifOut1SecOctets,'ifOut1SecPkts':ifOut1SecPkts,'ifHCIn1SecRate':ifHCIn1SecRate,'ifHCOut1SecRate':ifHCOut1SecRate,'ifJnxInErrors':ifJnxInErrors,'ifJnxInFrameErrors':ifJnxInFrameErrors,'ifJnxInQDrops':ifJnxInQDrops,'ifJnxInRunts':ifJnxInRunts,'ifJnxInGiants':ifJnxInGiants,'ifJnxInDiscards':ifJnxInDiscards,'ifJnxInHslCrcErrors':ifJnxInHslCrcErrors,'ifJnxInHslFifoOverFlows':ifJnxInHslFifoOverFlows,'ifJnxInL3Incompletes':ifJnxInL3Incompletes,_O:ifJnxInL2ChanErrors,'ifJnxInL2MismatchTimeouts':ifJnxInL2MismatchTimeouts,'ifJnxInInvalidVCs':ifJnxInInvalidVCs,'ifJnxInFifoErrors':ifJnxInFifoErrors,'ifJnxBucketDrops':ifJnxBucketDrops,'ifJnxSramErrors':ifJnxSramErrors,'ifJnxOutErrors':ifJnxOutErrors,'ifJnxCollisions':ifJnxCollisions,'ifJnxCarrierTrans':ifJnxCarrierTrans,'ifJnxOutQDrops':ifJnxOutQDrops,'ifJnxOutAgedErrors':ifJnxOutAgedErrors,'ifJnxOutFifoErrors':ifJnxOutFifoErrors,'ifJnxOutHslFifoUnderFlows':ifJnxOutHslFifoUnderFlows,'ifJnxOutHslCrcErrors':ifJnxOutHslCrcErrors,_M:ifJnxCrcErrors,_N:ifJnxFcsErrors,'ifHCIn1SecOctets':ifHCIn1SecOctets,'ifHCOut1SecOctets':ifHCOut1SecOctets,'ifJnxInputErrors':ifJnxInputErrors,'ifJnxOutEcnMarkedPackets':ifJnxOutEcnMarkedPackets,'ifChassisTable':ifChassisTable,_L:ifChassisEntry,_P:ifChassisFpc,_Q:ifChassisPic,_R:ifChassisPort,'ifChassisChannel':ifChassisChannel,'ifChassisLogicalUnit':ifChassisLogicalUnit,'ifChassisPicIndex':ifChassisPicIndex,'ifJnxNotification':ifJnxNotification,'ifJnxNotificationPrefix':ifJnxNotificationPrefix,'ifJnxErrors':ifJnxErrors,'ifJnxL2Errors':ifJnxL2Errors,'ifJnxPolTable':ifJnxPolTable,'ifJnxPolEntry':ifJnxPolEntry,'ifJnxInPolLowOctets':ifJnxInPolLowOctets,'ifJnxInPolLowPkts':ifJnxInPolLowPkts,'ifJnxInPolLow1SecRate':ifJnxInPolLow1SecRate,'ifJnxInPolMLowOctets':ifJnxInPolMLowOctets,'ifJnxInPolMLowPkts':ifJnxInPolMLowPkts,'ifJnxInPolMLow1SecRate':ifJnxInPolMLow1SecRate,'ifJnxInPolMHighOctets':ifJnxInPolMHighOctets,'ifJnxInPolMHighPkts':ifJnxInPolMHighPkts,'ifJnxInPolMHigh1SecRate':ifJnxInPolMHigh1SecRate,'ifJnxInPolHighOctets':ifJnxInPolHighOctets,'ifJnxInPolHighPkts':ifJnxInPolHighPkts,'ifJnxInPolHigh1SecRate':ifJnxInPolHigh1SecRate,'ifJnxInPolDropOctets':ifJnxInPolDropOctets,'ifJnxInPolDropPkts':ifJnxInPolDropPkts,'ifJnxInPolDrop1SecRate':ifJnxInPolDrop1SecRate,'ifJnxOutPolLowOctets':ifJnxOutPolLowOctets,'ifJnxOutPolLowPkts':ifJnxOutPolLowPkts,'ifJnxOutPolLow1SecRate':ifJnxOutPolLow1SecRate,'ifJnxOutPolMLowOctets':ifJnxOutPolMLowOctets,'ifJnxOutPolMLowPkts':ifJnxOutPolMLowPkts,'ifJnxOutPolMLow1SecRate':ifJnxOutPolMLow1SecRate,'ifJnxOutPolMHighOctets':ifJnxOutPolMHighOctets,'ifJnxOutPolMHighPkts':ifJnxOutPolMHighPkts,'ifJnxOutPolMHigh1SecRate':ifJnxOutPolMHigh1SecRate,'ifJnxOutPolHighOctets':ifJnxOutPolHighOctets,'ifJnxOutPolHighPkts':ifJnxOutPolHighPkts,'ifJnxOutPolHigh1SecRate':ifJnxOutPolHigh1SecRate,'ifJnxOutPolDropOctets':ifJnxOutPolDropOctets,'ifJnxOutPolDropPkts':ifJnxOutPolDropPkts,'ifJnxOutPolDrop1SecRate':ifJnxOutPolDrop1SecRate,'ifJnxMediaTable':ifJnxMediaTable,'ifJnxMediaEntry':ifJnxMediaEntry,'ifJnxMediaType':ifJnxMediaType,'ifJnxMediaConfigSpeed':ifJnxMediaConfigSpeed,'ifJnxMediaSpeed':ifJnxMediaSpeed,'ifJnxMediaMaxSpeed':ifJnxMediaMaxSpeed,'ifJnxMediaMode':ifJnxMediaMode,'ifJnxMediaConfigMode':ifJnxMediaConfigMode,'ifJnxMediaAutoNegotiationEnabled':ifJnxMediaAutoNegotiationEnabled,'ifJnxMediaLastFlap':ifJnxMediaLastFlap,'ifJnxMediaLastUpdate':ifJnxMediaLastUpdate,'ifJnxMediaConfigHighSpeed':ifJnxMediaConfigHighSpeed,'ifJnxMediaConfigSpeedMap':ifJnxMediaConfigSpeedMap,'ifJnxMediaHighSpeed':ifJnxMediaHighSpeed,'ifJnxTrafficStatsTable':ifJnxTrafficStatsTable,'ifJnxTrafficStatsEntry':ifJnxTrafficStatsEntry,'ifJnxLocalV4InPkts':ifJnxLocalV4InPkts,'ifJnxLocalV4InOctets':ifJnxLocalV4InOctets,'ifJnxLocalV4OutPkts':ifJnxLocalV4OutPkts,'ifJnxLocalV4OutOctets':ifJnxLocalV4OutOctets,'ifJnxTransitV4InPkts':ifJnxTransitV4InPkts,'ifJnxTransitV4InOctets':ifJnxTransitV4InOctets,'ifJnxTransitV4OutPkts':ifJnxTransitV4OutPkts,'ifJnxTransitV4OutOctets':ifJnxTransitV4OutOctets,'ifJnxTransitV4In1SecRate':ifJnxTransitV4In1SecRate,'ifJnxTransitV4In1SecOctets':ifJnxTransitV4In1SecOctets,'ifJnxTransitV4Out1SecRate':ifJnxTransitV4Out1SecRate,'ifJnxTransitV4Out1SecOctets':ifJnxTransitV4Out1SecOctets,'ifJnxTrafficV4InPkts':ifJnxTrafficV4InPkts,'ifJnxTrafficV4InOctets':ifJnxTrafficV4InOctets,'ifJnxTrafficV4OutPkts':ifJnxTrafficV4OutPkts,'ifJnxTrafficV4OutOctets':ifJnxTrafficV4OutOctets,'ifJnxLocalV6InPkts':ifJnxLocalV6InPkts,'ifJnxLocalV6InOctets':ifJnxLocalV6InOctets,'ifJnxLocalV6OutPkts':ifJnxLocalV6OutPkts,'ifJnxLocalV6OutOctets':ifJnxLocalV6OutOctets,'ifJnxTransitV6InPkts':ifJnxTransitV6InPkts,'ifJnxTransitV6InOctets':ifJnxTransitV6InOctets,'ifJnxTransitV6OutPkts':ifJnxTransitV6OutPkts,'ifJnxTransitV6OutOctets':ifJnxTransitV6OutOctets,'ifJnxTransitV6In1SecRate':ifJnxTransitV6In1SecRate,'ifJnxTransitV6In1SecOctets':ifJnxTransitV6In1SecOctets,'ifJnxTransitV6Out1SecRate':ifJnxTransitV6Out1SecRate,'ifJnxTransitV6Out1SecOctets':ifJnxTransitV6Out1SecOctets,'ifJnxTrafficV6InPkts':ifJnxTrafficV6InPkts,'ifJnxTrafficV6InOctets':ifJnxTrafficV6InOctets,'ifJnxTrafficV6OutPkts':ifJnxTrafficV6OutPkts,'ifJnxTrafficV6OutOctets':ifJnxTrafficV6OutOctets})