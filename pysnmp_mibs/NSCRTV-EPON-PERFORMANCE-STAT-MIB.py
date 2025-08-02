_Z='perfStatsThresholdTypeIndex'
_Y='perfStatsThresholdPortIndex'
_X='perfStatsThresholdCardIndex'
_W='perfStatsThresholdDeviceIndex'
_V='stats24Index'
_U='stats24PortIndex'
_T='stats24CardIndex'
_S='stats24DeviceIndex'
_R='seconds'
_Q='stats15Index'
_P='stats15PortIndex'
_O='stats15CardIndex'
_N='stats15DeviceIndex'
_M='curStatsPortIndex'
_L='curStatsCardIndex'
_K='curStatsDeviceIndex'
_J='EponStats24HourRecordType'
_I='EponStats15MinRecordType'
_H='read-create'
_G='none'
_F='Integer32'
_E='read-write'
_D='not-accessible'
_C='NSCRTV-EPON-PERFORMANCE-STAT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AutoNegotiationTechAbility,EponAlarmCode,EponAlarmInstance,EponCardIndex,EponDeviceIndex,EponPortIndex,EponSeverityType,EponStats15MinRecordType,EponStats24HourRecordType,EponStatsThresholdType,TAddress,performanceStatisticObjects=mibBuilder.importSymbols('NSCRTV-EPONEOC-EPON-MIB','AutoNegotiationTechAbility','EponAlarmCode','EponAlarmInstance','EponCardIndex','EponDeviceIndex','EponPortIndex','EponSeverityType',_I,_J,'EponStatsThresholdType','TAddress','performanceStatisticObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
_CurStatsTable_Object=MibTable
curStatsTable=_CurStatsTable_Object((1,3,6,1,4,1,17409,2,3,10,1))
if mibBuilder.loadTexts:curStatsTable.setStatus(_A)
_CurStatsEntry_Object=MibTableRow
curStatsEntry=_CurStatsEntry_Object((1,3,6,1,4,1,17409,2,3,10,1,1))
curStatsEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:curStatsEntry.setStatus(_A)
_CurStatsDeviceIndex_Type=EponDeviceIndex
_CurStatsDeviceIndex_Object=MibTableColumn
curStatsDeviceIndex=_CurStatsDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,10,1,1,1),_CurStatsDeviceIndex_Type())
curStatsDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:curStatsDeviceIndex.setStatus(_A)
_CurStatsCardIndex_Type=EponCardIndex
_CurStatsCardIndex_Object=MibTableColumn
curStatsCardIndex=_CurStatsCardIndex_Object((1,3,6,1,4,1,17409,2,3,10,1,1,2),_CurStatsCardIndex_Type())
curStatsCardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:curStatsCardIndex.setStatus(_A)
_CurStatsPortIndex_Type=EponPortIndex
_CurStatsPortIndex_Object=MibTableColumn
curStatsPortIndex=_CurStatsPortIndex_Object((1,3,6,1,4,1,17409,2,3,10,1,1,3),_CurStatsPortIndex_Type())
curStatsPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:curStatsPortIndex.setStatus(_A)
_CurStatsInOctets_Type=Counter64
_CurStatsInOctets_Object=MibTableColumn
curStatsInOctets=_CurStatsInOctets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,4),_CurStatsInOctets_Type())
curStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInOctets.setStatus(_A)
_CurStatsInPkts_Type=Counter64
_CurStatsInPkts_Object=MibTableColumn
curStatsInPkts=_CurStatsInPkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,5),_CurStatsInPkts_Type())
curStatsInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInPkts.setStatus(_A)
_CurStatsInBroadcastPkts_Type=Counter64
_CurStatsInBroadcastPkts_Object=MibTableColumn
curStatsInBroadcastPkts=_CurStatsInBroadcastPkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,6),_CurStatsInBroadcastPkts_Type())
curStatsInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInBroadcastPkts.setStatus(_A)
_CurStatsInMulticastPkts_Type=Counter64
_CurStatsInMulticastPkts_Object=MibTableColumn
curStatsInMulticastPkts=_CurStatsInMulticastPkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,7),_CurStatsInMulticastPkts_Type())
curStatsInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInMulticastPkts.setStatus(_A)
_CurStatsInPkts64Octets_Type=Counter64
_CurStatsInPkts64Octets_Object=MibTableColumn
curStatsInPkts64Octets=_CurStatsInPkts64Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,8),_CurStatsInPkts64Octets_Type())
curStatsInPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInPkts64Octets.setStatus(_A)
_CurStatsInPkts65to127Octets_Type=Counter64
_CurStatsInPkts65to127Octets_Object=MibTableColumn
curStatsInPkts65to127Octets=_CurStatsInPkts65to127Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,9),_CurStatsInPkts65to127Octets_Type())
curStatsInPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInPkts65to127Octets.setStatus(_A)
_CurStatsInPkts128to255Octets_Type=Counter64
_CurStatsInPkts128to255Octets_Object=MibTableColumn
curStatsInPkts128to255Octets=_CurStatsInPkts128to255Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,10),_CurStatsInPkts128to255Octets_Type())
curStatsInPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInPkts128to255Octets.setStatus(_A)
_CurStatsInPkts256to511Octets_Type=Counter64
_CurStatsInPkts256to511Octets_Object=MibTableColumn
curStatsInPkts256to511Octets=_CurStatsInPkts256to511Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,11),_CurStatsInPkts256to511Octets_Type())
curStatsInPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInPkts256to511Octets.setStatus(_A)
_CurStatsInPkts512to1023Octets_Type=Counter64
_CurStatsInPkts512to1023Octets_Object=MibTableColumn
curStatsInPkts512to1023Octets=_CurStatsInPkts512to1023Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,12),_CurStatsInPkts512to1023Octets_Type())
curStatsInPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInPkts512to1023Octets.setStatus(_A)
_CurStatsInPkts1024to1518Octets_Type=Counter64
_CurStatsInPkts1024to1518Octets_Object=MibTableColumn
curStatsInPkts1024to1518Octets=_CurStatsInPkts1024to1518Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,13),_CurStatsInPkts1024to1518Octets_Type())
curStatsInPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInPkts1024to1518Octets.setStatus(_A)
_CurStatsInPkts1519to1522Octets_Type=Counter64
_CurStatsInPkts1519to1522Octets_Object=MibTableColumn
curStatsInPkts1519to1522Octets=_CurStatsInPkts1519to1522Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,14),_CurStatsInPkts1519to1522Octets_Type())
curStatsInPkts1519to1522Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInPkts1519to1522Octets.setStatus(_A)
_CurStatsInUndersizePkts_Type=Counter64
_CurStatsInUndersizePkts_Object=MibTableColumn
curStatsInUndersizePkts=_CurStatsInUndersizePkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,15),_CurStatsInUndersizePkts_Type())
curStatsInUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInUndersizePkts.setStatus(_A)
_CurStatsInOversizePkts_Type=Counter64
_CurStatsInOversizePkts_Object=MibTableColumn
curStatsInOversizePkts=_CurStatsInOversizePkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,16),_CurStatsInOversizePkts_Type())
curStatsInOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInOversizePkts.setStatus(_A)
_CurStatsInFragments_Type=Counter64
_CurStatsInFragments_Object=MibTableColumn
curStatsInFragments=_CurStatsInFragments_Object((1,3,6,1,4,1,17409,2,3,10,1,1,17),_CurStatsInFragments_Type())
curStatsInFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInFragments.setStatus(_A)
_CurStatsInMpcpFrames_Type=Counter64
_CurStatsInMpcpFrames_Object=MibTableColumn
curStatsInMpcpFrames=_CurStatsInMpcpFrames_Object((1,3,6,1,4,1,17409,2,3,10,1,1,18),_CurStatsInMpcpFrames_Type())
curStatsInMpcpFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInMpcpFrames.setStatus(_A)
_CurStatsInMpcpOctets_Type=Counter64
_CurStatsInMpcpOctets_Object=MibTableColumn
curStatsInMpcpOctets=_CurStatsInMpcpOctets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,19),_CurStatsInMpcpOctets_Type())
curStatsInMpcpOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInMpcpOctets.setStatus(_A)
_CurStatsInOAMFrames_Type=Counter64
_CurStatsInOAMFrames_Object=MibTableColumn
curStatsInOAMFrames=_CurStatsInOAMFrames_Object((1,3,6,1,4,1,17409,2,3,10,1,1,20),_CurStatsInOAMFrames_Type())
curStatsInOAMFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInOAMFrames.setStatus(_A)
_CurStatsInOAMOctets_Type=Counter64
_CurStatsInOAMOctets_Object=MibTableColumn
curStatsInOAMOctets=_CurStatsInOAMOctets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,21),_CurStatsInOAMOctets_Type())
curStatsInOAMOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInOAMOctets.setStatus(_A)
_CurStatsInCRCErrorPkts_Type=Counter64
_CurStatsInCRCErrorPkts_Object=MibTableColumn
curStatsInCRCErrorPkts=_CurStatsInCRCErrorPkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,22),_CurStatsInCRCErrorPkts_Type())
curStatsInCRCErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInCRCErrorPkts.setStatus(_A)
_CurStatsInDropEvents_Type=Counter64
_CurStatsInDropEvents_Object=MibTableColumn
curStatsInDropEvents=_CurStatsInDropEvents_Object((1,3,6,1,4,1,17409,2,3,10,1,1,23),_CurStatsInDropEvents_Type())
curStatsInDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInDropEvents.setStatus(_A)
_CurStatsInJabbers_Type=Counter64
_CurStatsInJabbers_Object=MibTableColumn
curStatsInJabbers=_CurStatsInJabbers_Object((1,3,6,1,4,1,17409,2,3,10,1,1,24),_CurStatsInJabbers_Type())
curStatsInJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInJabbers.setStatus(_A)
_CurStatsInCollision_Type=Counter64
_CurStatsInCollision_Object=MibTableColumn
curStatsInCollision=_CurStatsInCollision_Object((1,3,6,1,4,1,17409,2,3,10,1,1,25),_CurStatsInCollision_Type())
curStatsInCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsInCollision.setStatus(_A)
_CurStatsOutOctets_Type=Counter64
_CurStatsOutOctets_Object=MibTableColumn
curStatsOutOctets=_CurStatsOutOctets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,26),_CurStatsOutOctets_Type())
curStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutOctets.setStatus(_A)
_CurStatsOutPkts_Type=Counter64
_CurStatsOutPkts_Object=MibTableColumn
curStatsOutPkts=_CurStatsOutPkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,27),_CurStatsOutPkts_Type())
curStatsOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutPkts.setStatus(_A)
_CurStatsOutBroadcastPkts_Type=Counter64
_CurStatsOutBroadcastPkts_Object=MibTableColumn
curStatsOutBroadcastPkts=_CurStatsOutBroadcastPkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,28),_CurStatsOutBroadcastPkts_Type())
curStatsOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutBroadcastPkts.setStatus(_A)
_CurStatsOutMulticastPkts_Type=Counter64
_CurStatsOutMulticastPkts_Object=MibTableColumn
curStatsOutMulticastPkts=_CurStatsOutMulticastPkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,29),_CurStatsOutMulticastPkts_Type())
curStatsOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutMulticastPkts.setStatus(_A)
_CurStatsOutPkts64Octets_Type=Counter64
_CurStatsOutPkts64Octets_Object=MibTableColumn
curStatsOutPkts64Octets=_CurStatsOutPkts64Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,30),_CurStatsOutPkts64Octets_Type())
curStatsOutPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutPkts64Octets.setStatus(_A)
_CurStatsOutPkts65to127Octets_Type=Counter64
_CurStatsOutPkts65to127Octets_Object=MibTableColumn
curStatsOutPkts65to127Octets=_CurStatsOutPkts65to127Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,31),_CurStatsOutPkts65to127Octets_Type())
curStatsOutPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutPkts65to127Octets.setStatus(_A)
_CurStatsOutPkts128to255Octets_Type=Counter64
_CurStatsOutPkts128to255Octets_Object=MibTableColumn
curStatsOutPkts128to255Octets=_CurStatsOutPkts128to255Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,32),_CurStatsOutPkts128to255Octets_Type())
curStatsOutPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutPkts128to255Octets.setStatus(_A)
_CurStatsOutPkts256to511Octets_Type=Counter64
_CurStatsOutPkts256to511Octets_Object=MibTableColumn
curStatsOutPkts256to511Octets=_CurStatsOutPkts256to511Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,33),_CurStatsOutPkts256to511Octets_Type())
curStatsOutPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutPkts256to511Octets.setStatus(_A)
_CurStatsOutPkts512to1023Octets_Type=Counter64
_CurStatsOutPkts512to1023Octets_Object=MibTableColumn
curStatsOutPkts512to1023Octets=_CurStatsOutPkts512to1023Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,34),_CurStatsOutPkts512to1023Octets_Type())
curStatsOutPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutPkts512to1023Octets.setStatus(_A)
_CurStatsOutPkts1024to1518Octets_Type=Counter64
_CurStatsOutPkts1024to1518Octets_Object=MibTableColumn
curStatsOutPkts1024to1518Octets=_CurStatsOutPkts1024to1518Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,35),_CurStatsOutPkts1024to1518Octets_Type())
curStatsOutPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutPkts1024to1518Octets.setStatus(_A)
_CurStatsOutPkts1519o1522Octets_Type=Counter64
_CurStatsOutPkts1519o1522Octets_Object=MibTableColumn
curStatsOutPkts1519o1522Octets=_CurStatsOutPkts1519o1522Octets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,36),_CurStatsOutPkts1519o1522Octets_Type())
curStatsOutPkts1519o1522Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutPkts1519o1522Octets.setStatus(_A)
_CurStatsOutUndersizePkts_Type=Counter64
_CurStatsOutUndersizePkts_Object=MibTableColumn
curStatsOutUndersizePkts=_CurStatsOutUndersizePkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,37),_CurStatsOutUndersizePkts_Type())
curStatsOutUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutUndersizePkts.setStatus(_A)
_CurStatsOutOversizePkts_Type=Counter64
_CurStatsOutOversizePkts_Object=MibTableColumn
curStatsOutOversizePkts=_CurStatsOutOversizePkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,38),_CurStatsOutOversizePkts_Type())
curStatsOutOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutOversizePkts.setStatus(_A)
_CurStatsOutFragments_Type=Counter64
_CurStatsOutFragments_Object=MibTableColumn
curStatsOutFragments=_CurStatsOutFragments_Object((1,3,6,1,4,1,17409,2,3,10,1,1,39),_CurStatsOutFragments_Type())
curStatsOutFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutFragments.setStatus(_A)
_CurStatsOutMpcpFrames_Type=Counter64
_CurStatsOutMpcpFrames_Object=MibTableColumn
curStatsOutMpcpFrames=_CurStatsOutMpcpFrames_Object((1,3,6,1,4,1,17409,2,3,10,1,1,40),_CurStatsOutMpcpFrames_Type())
curStatsOutMpcpFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutMpcpFrames.setStatus(_A)
_CurStatsOutMpcpOctets_Type=Counter64
_CurStatsOutMpcpOctets_Object=MibTableColumn
curStatsOutMpcpOctets=_CurStatsOutMpcpOctets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,41),_CurStatsOutMpcpOctets_Type())
curStatsOutMpcpOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutMpcpOctets.setStatus(_A)
_CurStatsOutOAMFrames_Type=Counter64
_CurStatsOutOAMFrames_Object=MibTableColumn
curStatsOutOAMFrames=_CurStatsOutOAMFrames_Object((1,3,6,1,4,1,17409,2,3,10,1,1,42),_CurStatsOutOAMFrames_Type())
curStatsOutOAMFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutOAMFrames.setStatus(_A)
_CurStatsOutOAMOctets_Type=Counter64
_CurStatsOutOAMOctets_Object=MibTableColumn
curStatsOutOAMOctets=_CurStatsOutOAMOctets_Object((1,3,6,1,4,1,17409,2,3,10,1,1,43),_CurStatsOutOAMOctets_Type())
curStatsOutOAMOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutOAMOctets.setStatus(_A)
_CurStatsOutCRCErrorPkts_Type=Counter64
_CurStatsOutCRCErrorPkts_Object=MibTableColumn
curStatsOutCRCErrorPkts=_CurStatsOutCRCErrorPkts_Object((1,3,6,1,4,1,17409,2,3,10,1,1,44),_CurStatsOutCRCErrorPkts_Type())
curStatsOutCRCErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutCRCErrorPkts.setStatus(_A)
_CurStatsOutDropEvents_Type=Counter64
_CurStatsOutDropEvents_Object=MibTableColumn
curStatsOutDropEvents=_CurStatsOutDropEvents_Object((1,3,6,1,4,1,17409,2,3,10,1,1,45),_CurStatsOutDropEvents_Type())
curStatsOutDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutDropEvents.setStatus(_A)
_CurStatsOutJabbers_Type=Counter64
_CurStatsOutJabbers_Object=MibTableColumn
curStatsOutJabbers=_CurStatsOutJabbers_Object((1,3,6,1,4,1,17409,2,3,10,1,1,46),_CurStatsOutJabbers_Type())
curStatsOutJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutJabbers.setStatus(_A)
_CurStatsOutCollision_Type=Counter64
_CurStatsOutCollision_Object=MibTableColumn
curStatsOutCollision=_CurStatsOutCollision_Object((1,3,6,1,4,1,17409,2,3,10,1,1,47),_CurStatsOutCollision_Type())
curStatsOutCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:curStatsOutCollision.setStatus(_A)
class _CurStatsStatusAndAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('clean',2)))
_CurStatsStatusAndAction_Type.__name__=_F
_CurStatsStatusAndAction_Object=MibTableColumn
curStatsStatusAndAction=_CurStatsStatusAndAction_Object((1,3,6,1,4,1,17409,2,3,10,1,1,48),_CurStatsStatusAndAction_Type())
curStatsStatusAndAction.setMaxAccess(_E)
if mibBuilder.loadTexts:curStatsStatusAndAction.setStatus(_A)
_Stats15Table_Object=MibTable
stats15Table=_Stats15Table_Object((1,3,6,1,4,1,17409,2,3,10,2))
if mibBuilder.loadTexts:stats15Table.setStatus(_A)
_Stats15Entry_Object=MibTableRow
stats15Entry=_Stats15Entry_Object((1,3,6,1,4,1,17409,2,3,10,2,1))
stats15Entry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:stats15Entry.setStatus(_A)
_Stats15DeviceIndex_Type=EponDeviceIndex
_Stats15DeviceIndex_Object=MibTableColumn
stats15DeviceIndex=_Stats15DeviceIndex_Object((1,3,6,1,4,1,17409,2,3,10,2,1,1),_Stats15DeviceIndex_Type())
stats15DeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:stats15DeviceIndex.setStatus(_A)
_Stats15CardIndex_Type=EponCardIndex
_Stats15CardIndex_Object=MibTableColumn
stats15CardIndex=_Stats15CardIndex_Object((1,3,6,1,4,1,17409,2,3,10,2,1,2),_Stats15CardIndex_Type())
stats15CardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:stats15CardIndex.setStatus(_A)
_Stats15PortIndex_Type=EponPortIndex
_Stats15PortIndex_Object=MibTableColumn
stats15PortIndex=_Stats15PortIndex_Object((1,3,6,1,4,1,17409,2,3,10,2,1,3),_Stats15PortIndex_Type())
stats15PortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:stats15PortIndex.setStatus(_A)
_Stats15Index_Type=EponStats15MinRecordType
_Stats15Index_Object=MibTableColumn
stats15Index=_Stats15Index_Object((1,3,6,1,4,1,17409,2,3,10,2,1,4),_Stats15Index_Type())
stats15Index.setMaxAccess(_D)
if mibBuilder.loadTexts:stats15Index.setStatus(_A)
_Stats15InOctets_Type=Counter64
_Stats15InOctets_Object=MibTableColumn
stats15InOctets=_Stats15InOctets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,5),_Stats15InOctets_Type())
stats15InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InOctets.setStatus(_A)
_Stats15InPkts_Type=Counter64
_Stats15InPkts_Object=MibTableColumn
stats15InPkts=_Stats15InPkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,6),_Stats15InPkts_Type())
stats15InPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InPkts.setStatus(_A)
_Stats15InBroadcastPkts_Type=Counter64
_Stats15InBroadcastPkts_Object=MibTableColumn
stats15InBroadcastPkts=_Stats15InBroadcastPkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,7),_Stats15InBroadcastPkts_Type())
stats15InBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InBroadcastPkts.setStatus(_A)
_Stats15InMulticastPkts_Type=Counter64
_Stats15InMulticastPkts_Object=MibTableColumn
stats15InMulticastPkts=_Stats15InMulticastPkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,8),_Stats15InMulticastPkts_Type())
stats15InMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InMulticastPkts.setStatus(_A)
_Stats15InPkts64Octets_Type=Counter64
_Stats15InPkts64Octets_Object=MibTableColumn
stats15InPkts64Octets=_Stats15InPkts64Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,9),_Stats15InPkts64Octets_Type())
stats15InPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InPkts64Octets.setStatus(_A)
_Stats15InPkts65to127Octets_Type=Counter64
_Stats15InPkts65to127Octets_Object=MibTableColumn
stats15InPkts65to127Octets=_Stats15InPkts65to127Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,10),_Stats15InPkts65to127Octets_Type())
stats15InPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InPkts65to127Octets.setStatus(_A)
_Stats15InPkts128to255Octets_Type=Counter64
_Stats15InPkts128to255Octets_Object=MibTableColumn
stats15InPkts128to255Octets=_Stats15InPkts128to255Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,11),_Stats15InPkts128to255Octets_Type())
stats15InPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InPkts128to255Octets.setStatus(_A)
_Stats15InPkts256to511Octets_Type=Counter64
_Stats15InPkts256to511Octets_Object=MibTableColumn
stats15InPkts256to511Octets=_Stats15InPkts256to511Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,12),_Stats15InPkts256to511Octets_Type())
stats15InPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InPkts256to511Octets.setStatus(_A)
_Stats15InPkts512to1023Octets_Type=Counter64
_Stats15InPkts512to1023Octets_Object=MibTableColumn
stats15InPkts512to1023Octets=_Stats15InPkts512to1023Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,13),_Stats15InPkts512to1023Octets_Type())
stats15InPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InPkts512to1023Octets.setStatus(_A)
_Stats15InPkts1024to1518Octets_Type=Counter64
_Stats15InPkts1024to1518Octets_Object=MibTableColumn
stats15InPkts1024to1518Octets=_Stats15InPkts1024to1518Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,14),_Stats15InPkts1024to1518Octets_Type())
stats15InPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InPkts1024to1518Octets.setStatus(_A)
_Stats15InPkts1519to1522Octets_Type=Counter64
_Stats15InPkts1519to1522Octets_Object=MibTableColumn
stats15InPkts1519to1522Octets=_Stats15InPkts1519to1522Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,15),_Stats15InPkts1519to1522Octets_Type())
stats15InPkts1519to1522Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InPkts1519to1522Octets.setStatus(_A)
_Stats15InUndersizePkts_Type=Counter64
_Stats15InUndersizePkts_Object=MibTableColumn
stats15InUndersizePkts=_Stats15InUndersizePkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,16),_Stats15InUndersizePkts_Type())
stats15InUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InUndersizePkts.setStatus(_A)
_Stats15InOversizePkts_Type=Counter64
_Stats15InOversizePkts_Object=MibTableColumn
stats15InOversizePkts=_Stats15InOversizePkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,17),_Stats15InOversizePkts_Type())
stats15InOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InOversizePkts.setStatus(_A)
_Stats15InFragments_Type=Counter64
_Stats15InFragments_Object=MibTableColumn
stats15InFragments=_Stats15InFragments_Object((1,3,6,1,4,1,17409,2,3,10,2,1,18),_Stats15InFragments_Type())
stats15InFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InFragments.setStatus(_A)
_Stats15InMpcpFrames_Type=Counter64
_Stats15InMpcpFrames_Object=MibTableColumn
stats15InMpcpFrames=_Stats15InMpcpFrames_Object((1,3,6,1,4,1,17409,2,3,10,2,1,19),_Stats15InMpcpFrames_Type())
stats15InMpcpFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InMpcpFrames.setStatus(_A)
_Stats15InMpcpOctets_Type=Counter64
_Stats15InMpcpOctets_Object=MibTableColumn
stats15InMpcpOctets=_Stats15InMpcpOctets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,20),_Stats15InMpcpOctets_Type())
stats15InMpcpOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InMpcpOctets.setStatus(_A)
_Stats15InOAMFrames_Type=Counter64
_Stats15InOAMFrames_Object=MibTableColumn
stats15InOAMFrames=_Stats15InOAMFrames_Object((1,3,6,1,4,1,17409,2,3,10,2,1,21),_Stats15InOAMFrames_Type())
stats15InOAMFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InOAMFrames.setStatus(_A)
_Stats15InOAMOctets_Type=Counter64
_Stats15InOAMOctets_Object=MibTableColumn
stats15InOAMOctets=_Stats15InOAMOctets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,22),_Stats15InOAMOctets_Type())
stats15InOAMOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InOAMOctets.setStatus(_A)
_Stats15InCRCErrorPkts_Type=Counter64
_Stats15InCRCErrorPkts_Object=MibTableColumn
stats15InCRCErrorPkts=_Stats15InCRCErrorPkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,23),_Stats15InCRCErrorPkts_Type())
stats15InCRCErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InCRCErrorPkts.setStatus(_A)
_Stats15InDropEvents_Type=Counter64
_Stats15InDropEvents_Object=MibTableColumn
stats15InDropEvents=_Stats15InDropEvents_Object((1,3,6,1,4,1,17409,2,3,10,2,1,24),_Stats15InDropEvents_Type())
stats15InDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InDropEvents.setStatus(_A)
_Stats15InJabbers_Type=Counter64
_Stats15InJabbers_Object=MibTableColumn
stats15InJabbers=_Stats15InJabbers_Object((1,3,6,1,4,1,17409,2,3,10,2,1,25),_Stats15InJabbers_Type())
stats15InJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InJabbers.setStatus(_A)
_Stats15InCollision_Type=Counter64
_Stats15InCollision_Object=MibTableColumn
stats15InCollision=_Stats15InCollision_Object((1,3,6,1,4,1,17409,2,3,10,2,1,26),_Stats15InCollision_Type())
stats15InCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15InCollision.setStatus(_A)
_Stats15OutOctets_Type=Counter64
_Stats15OutOctets_Object=MibTableColumn
stats15OutOctets=_Stats15OutOctets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,27),_Stats15OutOctets_Type())
stats15OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutOctets.setStatus(_A)
_Stats15OutPkts_Type=Counter64
_Stats15OutPkts_Object=MibTableColumn
stats15OutPkts=_Stats15OutPkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,28),_Stats15OutPkts_Type())
stats15OutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutPkts.setStatus(_A)
_Stats15OutBroadcastPkts_Type=Counter64
_Stats15OutBroadcastPkts_Object=MibTableColumn
stats15OutBroadcastPkts=_Stats15OutBroadcastPkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,29),_Stats15OutBroadcastPkts_Type())
stats15OutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutBroadcastPkts.setStatus(_A)
_Stats15OutMulticastPkts_Type=Counter64
_Stats15OutMulticastPkts_Object=MibTableColumn
stats15OutMulticastPkts=_Stats15OutMulticastPkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,30),_Stats15OutMulticastPkts_Type())
stats15OutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutMulticastPkts.setStatus(_A)
_Stats15OutPkts64Octets_Type=Counter64
_Stats15OutPkts64Octets_Object=MibTableColumn
stats15OutPkts64Octets=_Stats15OutPkts64Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,31),_Stats15OutPkts64Octets_Type())
stats15OutPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutPkts64Octets.setStatus(_A)
_Stats15OutPkts65to127Octets_Type=Counter64
_Stats15OutPkts65to127Octets_Object=MibTableColumn
stats15OutPkts65to127Octets=_Stats15OutPkts65to127Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,32),_Stats15OutPkts65to127Octets_Type())
stats15OutPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutPkts65to127Octets.setStatus(_A)
_Stats15OutPkts128to255Octets_Type=Counter64
_Stats15OutPkts128to255Octets_Object=MibTableColumn
stats15OutPkts128to255Octets=_Stats15OutPkts128to255Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,33),_Stats15OutPkts128to255Octets_Type())
stats15OutPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutPkts128to255Octets.setStatus(_A)
_Stats15OutPkts256to511Octets_Type=Counter64
_Stats15OutPkts256to511Octets_Object=MibTableColumn
stats15OutPkts256to511Octets=_Stats15OutPkts256to511Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,34),_Stats15OutPkts256to511Octets_Type())
stats15OutPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutPkts256to511Octets.setStatus(_A)
_Stats15OutPkts512to1023Octets_Type=Counter64
_Stats15OutPkts512to1023Octets_Object=MibTableColumn
stats15OutPkts512to1023Octets=_Stats15OutPkts512to1023Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,35),_Stats15OutPkts512to1023Octets_Type())
stats15OutPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutPkts512to1023Octets.setStatus(_A)
_Stats15OutPkts1024to1518Octets_Type=Counter64
_Stats15OutPkts1024to1518Octets_Object=MibTableColumn
stats15OutPkts1024to1518Octets=_Stats15OutPkts1024to1518Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,36),_Stats15OutPkts1024to1518Octets_Type())
stats15OutPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutPkts1024to1518Octets.setStatus(_A)
_Stats15OutPkts1519o1522Octets_Type=Counter64
_Stats15OutPkts1519o1522Octets_Object=MibTableColumn
stats15OutPkts1519o1522Octets=_Stats15OutPkts1519o1522Octets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,37),_Stats15OutPkts1519o1522Octets_Type())
stats15OutPkts1519o1522Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutPkts1519o1522Octets.setStatus(_A)
_Stats15OutUndersizePkts_Type=Counter64
_Stats15OutUndersizePkts_Object=MibTableColumn
stats15OutUndersizePkts=_Stats15OutUndersizePkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,38),_Stats15OutUndersizePkts_Type())
stats15OutUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutUndersizePkts.setStatus(_A)
_Stats15OutOversizePkts_Type=Counter64
_Stats15OutOversizePkts_Object=MibTableColumn
stats15OutOversizePkts=_Stats15OutOversizePkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,39),_Stats15OutOversizePkts_Type())
stats15OutOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutOversizePkts.setStatus(_A)
_Stats15OutFragments_Type=Counter64
_Stats15OutFragments_Object=MibTableColumn
stats15OutFragments=_Stats15OutFragments_Object((1,3,6,1,4,1,17409,2,3,10,2,1,40),_Stats15OutFragments_Type())
stats15OutFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutFragments.setStatus(_A)
_Stats15OutMpcpFrames_Type=Counter64
_Stats15OutMpcpFrames_Object=MibTableColumn
stats15OutMpcpFrames=_Stats15OutMpcpFrames_Object((1,3,6,1,4,1,17409,2,3,10,2,1,41),_Stats15OutMpcpFrames_Type())
stats15OutMpcpFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutMpcpFrames.setStatus(_A)
_Stats15OutMpcpOctets_Type=Counter64
_Stats15OutMpcpOctets_Object=MibTableColumn
stats15OutMpcpOctets=_Stats15OutMpcpOctets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,42),_Stats15OutMpcpOctets_Type())
stats15OutMpcpOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutMpcpOctets.setStatus(_A)
_Stats15OutOAMFrames_Type=Counter64
_Stats15OutOAMFrames_Object=MibTableColumn
stats15OutOAMFrames=_Stats15OutOAMFrames_Object((1,3,6,1,4,1,17409,2,3,10,2,1,43),_Stats15OutOAMFrames_Type())
stats15OutOAMFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutOAMFrames.setStatus(_A)
_Stats15OutOAMOctets_Type=Counter64
_Stats15OutOAMOctets_Object=MibTableColumn
stats15OutOAMOctets=_Stats15OutOAMOctets_Object((1,3,6,1,4,1,17409,2,3,10,2,1,44),_Stats15OutOAMOctets_Type())
stats15OutOAMOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutOAMOctets.setStatus(_A)
_Stats15OutCRCErrorPkts_Type=Counter64
_Stats15OutCRCErrorPkts_Object=MibTableColumn
stats15OutCRCErrorPkts=_Stats15OutCRCErrorPkts_Object((1,3,6,1,4,1,17409,2,3,10,2,1,45),_Stats15OutCRCErrorPkts_Type())
stats15OutCRCErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutCRCErrorPkts.setStatus(_A)
_Stats15OutDropEvents_Type=Counter64
_Stats15OutDropEvents_Object=MibTableColumn
stats15OutDropEvents=_Stats15OutDropEvents_Object((1,3,6,1,4,1,17409,2,3,10,2,1,46),_Stats15OutDropEvents_Type())
stats15OutDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutDropEvents.setStatus(_A)
_Stats15OutJabbers_Type=Counter64
_Stats15OutJabbers_Object=MibTableColumn
stats15OutJabbers=_Stats15OutJabbers_Object((1,3,6,1,4,1,17409,2,3,10,2,1,47),_Stats15OutJabbers_Type())
stats15OutJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutJabbers.setStatus(_A)
_Stats15OutCollision_Type=Counter64
_Stats15OutCollision_Object=MibTableColumn
stats15OutCollision=_Stats15OutCollision_Object((1,3,6,1,4,1,17409,2,3,10,2,1,48),_Stats15OutCollision_Type())
stats15OutCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15OutCollision.setStatus(_A)
class _Stats15StatusAndAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('clean',2)))
_Stats15StatusAndAction_Type.__name__=_F
_Stats15StatusAndAction_Object=MibTableColumn
stats15StatusAndAction=_Stats15StatusAndAction_Object((1,3,6,1,4,1,17409,2,3,10,2,1,49),_Stats15StatusAndAction_Type())
stats15StatusAndAction.setMaxAccess(_E)
if mibBuilder.loadTexts:stats15StatusAndAction.setStatus(_A)
_Stats15ValidityTag_Type=TruthValue
_Stats15ValidityTag_Object=MibTableColumn
stats15ValidityTag=_Stats15ValidityTag_Object((1,3,6,1,4,1,17409,2,3,10,2,1,50),_Stats15ValidityTag_Type())
stats15ValidityTag.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15ValidityTag.setStatus(_A)
_Stats15ElapsedTime_Type=Counter32
_Stats15ElapsedTime_Object=MibTableColumn
stats15ElapsedTime=_Stats15ElapsedTime_Object((1,3,6,1,4,1,17409,2,3,10,2,1,51),_Stats15ElapsedTime_Type())
stats15ElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15ElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:stats15ElapsedTime.setUnits(_R)
_Stats15EndTime_Type=DateAndTime
_Stats15EndTime_Object=MibTableColumn
stats15EndTime=_Stats15EndTime_Object((1,3,6,1,4,1,17409,2,3,10,2,1,52),_Stats15EndTime_Type())
stats15EndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stats15EndTime.setStatus(_A)
_Stats24Table_Object=MibTable
stats24Table=_Stats24Table_Object((1,3,6,1,4,1,17409,2,3,10,3))
if mibBuilder.loadTexts:stats24Table.setStatus(_A)
_Stats24Entry_Object=MibTableRow
stats24Entry=_Stats24Entry_Object((1,3,6,1,4,1,17409,2,3,10,3,1))
stats24Entry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:stats24Entry.setStatus(_A)
_Stats24DeviceIndex_Type=EponDeviceIndex
_Stats24DeviceIndex_Object=MibTableColumn
stats24DeviceIndex=_Stats24DeviceIndex_Object((1,3,6,1,4,1,17409,2,3,10,3,1,1),_Stats24DeviceIndex_Type())
stats24DeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:stats24DeviceIndex.setStatus(_A)
_Stats24CardIndex_Type=EponCardIndex
_Stats24CardIndex_Object=MibTableColumn
stats24CardIndex=_Stats24CardIndex_Object((1,3,6,1,4,1,17409,2,3,10,3,1,2),_Stats24CardIndex_Type())
stats24CardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:stats24CardIndex.setStatus(_A)
_Stats24PortIndex_Type=EponPortIndex
_Stats24PortIndex_Object=MibTableColumn
stats24PortIndex=_Stats24PortIndex_Object((1,3,6,1,4,1,17409,2,3,10,3,1,3),_Stats24PortIndex_Type())
stats24PortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:stats24PortIndex.setStatus(_A)
_Stats24Index_Type=EponStats24HourRecordType
_Stats24Index_Object=MibTableColumn
stats24Index=_Stats24Index_Object((1,3,6,1,4,1,17409,2,3,10,3,1,4),_Stats24Index_Type())
stats24Index.setMaxAccess(_D)
if mibBuilder.loadTexts:stats24Index.setStatus(_A)
_Stats24InOctets_Type=Counter64
_Stats24InOctets_Object=MibTableColumn
stats24InOctets=_Stats24InOctets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,5),_Stats24InOctets_Type())
stats24InOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InOctets.setStatus(_A)
_Stats24InPkts_Type=Counter64
_Stats24InPkts_Object=MibTableColumn
stats24InPkts=_Stats24InPkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,6),_Stats24InPkts_Type())
stats24InPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InPkts.setStatus(_A)
_Stats24InBroadcastPkts_Type=Counter64
_Stats24InBroadcastPkts_Object=MibTableColumn
stats24InBroadcastPkts=_Stats24InBroadcastPkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,7),_Stats24InBroadcastPkts_Type())
stats24InBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InBroadcastPkts.setStatus(_A)
_Stats24InMulticastPkts_Type=Counter64
_Stats24InMulticastPkts_Object=MibTableColumn
stats24InMulticastPkts=_Stats24InMulticastPkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,8),_Stats24InMulticastPkts_Type())
stats24InMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InMulticastPkts.setStatus(_A)
_Stats24InPkts64Octets_Type=Counter64
_Stats24InPkts64Octets_Object=MibTableColumn
stats24InPkts64Octets=_Stats24InPkts64Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,9),_Stats24InPkts64Octets_Type())
stats24InPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InPkts64Octets.setStatus(_A)
_Stats24InPkts65to127Octets_Type=Counter64
_Stats24InPkts65to127Octets_Object=MibTableColumn
stats24InPkts65to127Octets=_Stats24InPkts65to127Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,10),_Stats24InPkts65to127Octets_Type())
stats24InPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InPkts65to127Octets.setStatus(_A)
_Stats24InPkts128to255Octets_Type=Counter64
_Stats24InPkts128to255Octets_Object=MibTableColumn
stats24InPkts128to255Octets=_Stats24InPkts128to255Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,11),_Stats24InPkts128to255Octets_Type())
stats24InPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InPkts128to255Octets.setStatus(_A)
_Stats24InPkts256to511Octets_Type=Counter64
_Stats24InPkts256to511Octets_Object=MibTableColumn
stats24InPkts256to511Octets=_Stats24InPkts256to511Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,12),_Stats24InPkts256to511Octets_Type())
stats24InPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InPkts256to511Octets.setStatus(_A)
_Stats24InPkts512to1023Octets_Type=Counter64
_Stats24InPkts512to1023Octets_Object=MibTableColumn
stats24InPkts512to1023Octets=_Stats24InPkts512to1023Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,13),_Stats24InPkts512to1023Octets_Type())
stats24InPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InPkts512to1023Octets.setStatus(_A)
_Stats24InPkts1024to1518Octets_Type=Counter64
_Stats24InPkts1024to1518Octets_Object=MibTableColumn
stats24InPkts1024to1518Octets=_Stats24InPkts1024to1518Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,14),_Stats24InPkts1024to1518Octets_Type())
stats24InPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InPkts1024to1518Octets.setStatus(_A)
_Stats24InPkts1519to1522Octets_Type=Counter64
_Stats24InPkts1519to1522Octets_Object=MibTableColumn
stats24InPkts1519to1522Octets=_Stats24InPkts1519to1522Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,15),_Stats24InPkts1519to1522Octets_Type())
stats24InPkts1519to1522Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InPkts1519to1522Octets.setStatus(_A)
_Stats24InUndersizePkts_Type=Counter64
_Stats24InUndersizePkts_Object=MibTableColumn
stats24InUndersizePkts=_Stats24InUndersizePkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,16),_Stats24InUndersizePkts_Type())
stats24InUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InUndersizePkts.setStatus(_A)
_Stats24InOversizePkts_Type=Counter64
_Stats24InOversizePkts_Object=MibTableColumn
stats24InOversizePkts=_Stats24InOversizePkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,17),_Stats24InOversizePkts_Type())
stats24InOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InOversizePkts.setStatus(_A)
_Stats24InFragments_Type=Counter64
_Stats24InFragments_Object=MibTableColumn
stats24InFragments=_Stats24InFragments_Object((1,3,6,1,4,1,17409,2,3,10,3,1,18),_Stats24InFragments_Type())
stats24InFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InFragments.setStatus(_A)
_Stats24InMpcpFrames_Type=Counter64
_Stats24InMpcpFrames_Object=MibTableColumn
stats24InMpcpFrames=_Stats24InMpcpFrames_Object((1,3,6,1,4,1,17409,2,3,10,3,1,19),_Stats24InMpcpFrames_Type())
stats24InMpcpFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InMpcpFrames.setStatus(_A)
_Stats24InMpcpOctets_Type=Counter64
_Stats24InMpcpOctets_Object=MibTableColumn
stats24InMpcpOctets=_Stats24InMpcpOctets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,20),_Stats24InMpcpOctets_Type())
stats24InMpcpOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InMpcpOctets.setStatus(_A)
_Stats24InOAMFrames_Type=Counter64
_Stats24InOAMFrames_Object=MibTableColumn
stats24InOAMFrames=_Stats24InOAMFrames_Object((1,3,6,1,4,1,17409,2,3,10,3,1,21),_Stats24InOAMFrames_Type())
stats24InOAMFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InOAMFrames.setStatus(_A)
_Stats24InOAMOctets_Type=Counter64
_Stats24InOAMOctets_Object=MibTableColumn
stats24InOAMOctets=_Stats24InOAMOctets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,22),_Stats24InOAMOctets_Type())
stats24InOAMOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InOAMOctets.setStatus(_A)
_Stats24InCRCErrorPkts_Type=Counter64
_Stats24InCRCErrorPkts_Object=MibTableColumn
stats24InCRCErrorPkts=_Stats24InCRCErrorPkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,23),_Stats24InCRCErrorPkts_Type())
stats24InCRCErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InCRCErrorPkts.setStatus(_A)
_Stats24InDropEvents_Type=Counter64
_Stats24InDropEvents_Object=MibTableColumn
stats24InDropEvents=_Stats24InDropEvents_Object((1,3,6,1,4,1,17409,2,3,10,3,1,24),_Stats24InDropEvents_Type())
stats24InDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InDropEvents.setStatus(_A)
_Stats24InJabbers_Type=Counter64
_Stats24InJabbers_Object=MibTableColumn
stats24InJabbers=_Stats24InJabbers_Object((1,3,6,1,4,1,17409,2,3,10,3,1,25),_Stats24InJabbers_Type())
stats24InJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InJabbers.setStatus(_A)
_Stats24InCollision_Type=Counter64
_Stats24InCollision_Object=MibTableColumn
stats24InCollision=_Stats24InCollision_Object((1,3,6,1,4,1,17409,2,3,10,3,1,26),_Stats24InCollision_Type())
stats24InCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24InCollision.setStatus(_A)
_Stats24OutOctets_Type=Counter64
_Stats24OutOctets_Object=MibTableColumn
stats24OutOctets=_Stats24OutOctets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,27),_Stats24OutOctets_Type())
stats24OutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutOctets.setStatus(_A)
_Stats24OutPkts_Type=Counter64
_Stats24OutPkts_Object=MibTableColumn
stats24OutPkts=_Stats24OutPkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,28),_Stats24OutPkts_Type())
stats24OutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutPkts.setStatus(_A)
_Stats24OutBroadcastPkts_Type=Counter64
_Stats24OutBroadcastPkts_Object=MibTableColumn
stats24OutBroadcastPkts=_Stats24OutBroadcastPkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,29),_Stats24OutBroadcastPkts_Type())
stats24OutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutBroadcastPkts.setStatus(_A)
_Stats24OutMulticastPkts_Type=Counter64
_Stats24OutMulticastPkts_Object=MibTableColumn
stats24OutMulticastPkts=_Stats24OutMulticastPkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,30),_Stats24OutMulticastPkts_Type())
stats24OutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutMulticastPkts.setStatus(_A)
_Stats24OutPkts64Octets_Type=Counter64
_Stats24OutPkts64Octets_Object=MibTableColumn
stats24OutPkts64Octets=_Stats24OutPkts64Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,31),_Stats24OutPkts64Octets_Type())
stats24OutPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutPkts64Octets.setStatus(_A)
_Stats24OutPkts65to127Octets_Type=Counter64
_Stats24OutPkts65to127Octets_Object=MibTableColumn
stats24OutPkts65to127Octets=_Stats24OutPkts65to127Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,32),_Stats24OutPkts65to127Octets_Type())
stats24OutPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutPkts65to127Octets.setStatus(_A)
_Stats24OutPkts128to255Octets_Type=Counter64
_Stats24OutPkts128to255Octets_Object=MibTableColumn
stats24OutPkts128to255Octets=_Stats24OutPkts128to255Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,33),_Stats24OutPkts128to255Octets_Type())
stats24OutPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutPkts128to255Octets.setStatus(_A)
_Stats24OutPkts256to511Octets_Type=Counter64
_Stats24OutPkts256to511Octets_Object=MibTableColumn
stats24OutPkts256to511Octets=_Stats24OutPkts256to511Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,34),_Stats24OutPkts256to511Octets_Type())
stats24OutPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutPkts256to511Octets.setStatus(_A)
_Stats24OutPkts512to1023Octets_Type=Counter64
_Stats24OutPkts512to1023Octets_Object=MibTableColumn
stats24OutPkts512to1023Octets=_Stats24OutPkts512to1023Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,35),_Stats24OutPkts512to1023Octets_Type())
stats24OutPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutPkts512to1023Octets.setStatus(_A)
_Stats24OutPkts1024to1518Octets_Type=Counter64
_Stats24OutPkts1024to1518Octets_Object=MibTableColumn
stats24OutPkts1024to1518Octets=_Stats24OutPkts1024to1518Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,36),_Stats24OutPkts1024to1518Octets_Type())
stats24OutPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutPkts1024to1518Octets.setStatus(_A)
_Stats24OutPkts1519o1522Octets_Type=Counter64
_Stats24OutPkts1519o1522Octets_Object=MibTableColumn
stats24OutPkts1519o1522Octets=_Stats24OutPkts1519o1522Octets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,37),_Stats24OutPkts1519o1522Octets_Type())
stats24OutPkts1519o1522Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutPkts1519o1522Octets.setStatus(_A)
_Stats24OutUndersizePkts_Type=Counter64
_Stats24OutUndersizePkts_Object=MibTableColumn
stats24OutUndersizePkts=_Stats24OutUndersizePkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,38),_Stats24OutUndersizePkts_Type())
stats24OutUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutUndersizePkts.setStatus(_A)
_Stats24OutOversizePkts_Type=Counter64
_Stats24OutOversizePkts_Object=MibTableColumn
stats24OutOversizePkts=_Stats24OutOversizePkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,39),_Stats24OutOversizePkts_Type())
stats24OutOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutOversizePkts.setStatus(_A)
_Stats24OutFragments_Type=Counter64
_Stats24OutFragments_Object=MibTableColumn
stats24OutFragments=_Stats24OutFragments_Object((1,3,6,1,4,1,17409,2,3,10,3,1,40),_Stats24OutFragments_Type())
stats24OutFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutFragments.setStatus(_A)
_Stats24OutMpcpFrames_Type=Counter64
_Stats24OutMpcpFrames_Object=MibTableColumn
stats24OutMpcpFrames=_Stats24OutMpcpFrames_Object((1,3,6,1,4,1,17409,2,3,10,3,1,41),_Stats24OutMpcpFrames_Type())
stats24OutMpcpFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutMpcpFrames.setStatus(_A)
_Stats24OutMpcpOctets_Type=Counter64
_Stats24OutMpcpOctets_Object=MibTableColumn
stats24OutMpcpOctets=_Stats24OutMpcpOctets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,42),_Stats24OutMpcpOctets_Type())
stats24OutMpcpOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutMpcpOctets.setStatus(_A)
_Stats24OutOAMFrames_Type=Counter64
_Stats24OutOAMFrames_Object=MibTableColumn
stats24OutOAMFrames=_Stats24OutOAMFrames_Object((1,3,6,1,4,1,17409,2,3,10,3,1,43),_Stats24OutOAMFrames_Type())
stats24OutOAMFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutOAMFrames.setStatus(_A)
_Stats24OutOAMOctets_Type=Counter64
_Stats24OutOAMOctets_Object=MibTableColumn
stats24OutOAMOctets=_Stats24OutOAMOctets_Object((1,3,6,1,4,1,17409,2,3,10,3,1,44),_Stats24OutOAMOctets_Type())
stats24OutOAMOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutOAMOctets.setStatus(_A)
_Stats24OutCRCErrorPkts_Type=Counter64
_Stats24OutCRCErrorPkts_Object=MibTableColumn
stats24OutCRCErrorPkts=_Stats24OutCRCErrorPkts_Object((1,3,6,1,4,1,17409,2,3,10,3,1,45),_Stats24OutCRCErrorPkts_Type())
stats24OutCRCErrorPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutCRCErrorPkts.setStatus(_A)
_Stats24OutDropEvents_Type=Counter64
_Stats24OutDropEvents_Object=MibTableColumn
stats24OutDropEvents=_Stats24OutDropEvents_Object((1,3,6,1,4,1,17409,2,3,10,3,1,46),_Stats24OutDropEvents_Type())
stats24OutDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutDropEvents.setStatus(_A)
_Stats24OutJabbers_Type=Counter64
_Stats24OutJabbers_Object=MibTableColumn
stats24OutJabbers=_Stats24OutJabbers_Object((1,3,6,1,4,1,17409,2,3,10,3,1,47),_Stats24OutJabbers_Type())
stats24OutJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutJabbers.setStatus(_A)
_Stats24OutCollision_Type=Counter64
_Stats24OutCollision_Object=MibTableColumn
stats24OutCollision=_Stats24OutCollision_Object((1,3,6,1,4,1,17409,2,3,10,3,1,48),_Stats24OutCollision_Type())
stats24OutCollision.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24OutCollision.setStatus(_A)
class _Stats24StatusAndAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('clear',2)))
_Stats24StatusAndAction_Type.__name__=_F
_Stats24StatusAndAction_Object=MibTableColumn
stats24StatusAndAction=_Stats24StatusAndAction_Object((1,3,6,1,4,1,17409,2,3,10,3,1,49),_Stats24StatusAndAction_Type())
stats24StatusAndAction.setMaxAccess(_E)
if mibBuilder.loadTexts:stats24StatusAndAction.setStatus(_A)
_Stats24ValidityTag_Type=TruthValue
_Stats24ValidityTag_Object=MibTableColumn
stats24ValidityTag=_Stats24ValidityTag_Object((1,3,6,1,4,1,17409,2,3,10,3,1,50),_Stats24ValidityTag_Type())
stats24ValidityTag.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24ValidityTag.setStatus(_A)
_Stats24ElapsedTime_Type=Counter32
_Stats24ElapsedTime_Object=MibTableColumn
stats24ElapsedTime=_Stats24ElapsedTime_Object((1,3,6,1,4,1,17409,2,3,10,3,1,51),_Stats24ElapsedTime_Type())
stats24ElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24ElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:stats24ElapsedTime.setUnits(_R)
_Stats24EndTime_Type=DateAndTime
_Stats24EndTime_Object=MibTableColumn
stats24EndTime=_Stats24EndTime_Object((1,3,6,1,4,1,17409,2,3,10,3,1,52),_Stats24EndTime_Type())
stats24EndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stats24EndTime.setStatus(_A)
_PerfStatsGlobalSet_ObjectIdentity=ObjectIdentity
perfStatsGlobalSet=_PerfStatsGlobalSet_ObjectIdentity((1,3,6,1,4,1,17409,2,3,10,4))
if mibBuilder.loadTexts:perfStatsGlobalSet.setStatus(_A)
class _PerfStats15MinMaxRecord_Type(EponStats15MinRecordType):defaultValue=96
_PerfStats15MinMaxRecord_Type.__name__=_I
_PerfStats15MinMaxRecord_Object=MibScalar
perfStats15MinMaxRecord=_PerfStats15MinMaxRecord_Object((1,3,6,1,4,1,17409,2,3,10,4,1),_PerfStats15MinMaxRecord_Type())
perfStats15MinMaxRecord.setMaxAccess(_E)
if mibBuilder.loadTexts:perfStats15MinMaxRecord.setStatus(_A)
class _PerfStats24HourMaxRecord_Type(EponStats24HourRecordType):defaultValue=7
_PerfStats24HourMaxRecord_Type.__name__=_J
_PerfStats24HourMaxRecord_Object=MibScalar
perfStats24HourMaxRecord=_PerfStats24HourMaxRecord_Object((1,3,6,1,4,1,17409,2,3,10,4,2),_PerfStats24HourMaxRecord_Type())
perfStats24HourMaxRecord.setMaxAccess(_E)
if mibBuilder.loadTexts:perfStats24HourMaxRecord.setStatus(_A)
_PerfStatsThresholdTable_Object=MibTable
perfStatsThresholdTable=_PerfStatsThresholdTable_Object((1,3,6,1,4,1,17409,2,3,10,5))
if mibBuilder.loadTexts:perfStatsThresholdTable.setStatus(_A)
_PerfStatsThresholdEntry_Object=MibTableRow
perfStatsThresholdEntry=_PerfStatsThresholdEntry_Object((1,3,6,1,4,1,17409,2,3,10,5,1))
perfStatsThresholdEntry.setIndexNames((0,_C,_W),(0,_C,_X),(0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:perfStatsThresholdEntry.setStatus(_A)
_PerfStatsThresholdDeviceIndex_Type=EponDeviceIndex
_PerfStatsThresholdDeviceIndex_Object=MibTableColumn
perfStatsThresholdDeviceIndex=_PerfStatsThresholdDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,10,5,1,1),_PerfStatsThresholdDeviceIndex_Type())
perfStatsThresholdDeviceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:perfStatsThresholdDeviceIndex.setStatus(_A)
_PerfStatsThresholdCardIndex_Type=EponCardIndex
_PerfStatsThresholdCardIndex_Object=MibTableColumn
perfStatsThresholdCardIndex=_PerfStatsThresholdCardIndex_Object((1,3,6,1,4,1,17409,2,3,10,5,1,2),_PerfStatsThresholdCardIndex_Type())
perfStatsThresholdCardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:perfStatsThresholdCardIndex.setStatus(_A)
_PerfStatsThresholdPortIndex_Type=EponPortIndex
_PerfStatsThresholdPortIndex_Object=MibTableColumn
perfStatsThresholdPortIndex=_PerfStatsThresholdPortIndex_Object((1,3,6,1,4,1,17409,2,3,10,5,1,3),_PerfStatsThresholdPortIndex_Type())
perfStatsThresholdPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:perfStatsThresholdPortIndex.setStatus(_A)
_PerfStatsThresholdTypeIndex_Type=EponStatsThresholdType
_PerfStatsThresholdTypeIndex_Object=MibTableColumn
perfStatsThresholdTypeIndex=_PerfStatsThresholdTypeIndex_Object((1,3,6,1,4,1,17409,2,3,10,5,1,4),_PerfStatsThresholdTypeIndex_Type())
perfStatsThresholdTypeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:perfStatsThresholdTypeIndex.setStatus(_A)
_PerfStatsThresholdUpper_Type=Counter64
_PerfStatsThresholdUpper_Object=MibTableColumn
perfStatsThresholdUpper=_PerfStatsThresholdUpper_Object((1,3,6,1,4,1,17409,2,3,10,5,1,5),_PerfStatsThresholdUpper_Type())
perfStatsThresholdUpper.setMaxAccess(_H)
if mibBuilder.loadTexts:perfStatsThresholdUpper.setStatus(_A)
_PerfStatsThresholdLower_Type=Counter64
_PerfStatsThresholdLower_Object=MibTableColumn
perfStatsThresholdLower=_PerfStatsThresholdLower_Object((1,3,6,1,4,1,17409,2,3,10,5,1,6),_PerfStatsThresholdLower_Type())
perfStatsThresholdLower.setMaxAccess(_H)
if mibBuilder.loadTexts:perfStatsThresholdLower.setStatus(_A)
_PerfStatsThresholdRowStatus_Type=RowStatus
_PerfStatsThresholdRowStatus_Object=MibTableColumn
perfStatsThresholdRowStatus=_PerfStatsThresholdRowStatus_Object((1,3,6,1,4,1,17409,2,3,10,5,1,7),_PerfStatsThresholdRowStatus_Type())
perfStatsThresholdRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:perfStatsThresholdRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'curStatsTable':curStatsTable,'curStatsEntry':curStatsEntry,_K:curStatsDeviceIndex,_L:curStatsCardIndex,_M:curStatsPortIndex,'curStatsInOctets':curStatsInOctets,'curStatsInPkts':curStatsInPkts,'curStatsInBroadcastPkts':curStatsInBroadcastPkts,'curStatsInMulticastPkts':curStatsInMulticastPkts,'curStatsInPkts64Octets':curStatsInPkts64Octets,'curStatsInPkts65to127Octets':curStatsInPkts65to127Octets,'curStatsInPkts128to255Octets':curStatsInPkts128to255Octets,'curStatsInPkts256to511Octets':curStatsInPkts256to511Octets,'curStatsInPkts512to1023Octets':curStatsInPkts512to1023Octets,'curStatsInPkts1024to1518Octets':curStatsInPkts1024to1518Octets,'curStatsInPkts1519to1522Octets':curStatsInPkts1519to1522Octets,'curStatsInUndersizePkts':curStatsInUndersizePkts,'curStatsInOversizePkts':curStatsInOversizePkts,'curStatsInFragments':curStatsInFragments,'curStatsInMpcpFrames':curStatsInMpcpFrames,'curStatsInMpcpOctets':curStatsInMpcpOctets,'curStatsInOAMFrames':curStatsInOAMFrames,'curStatsInOAMOctets':curStatsInOAMOctets,'curStatsInCRCErrorPkts':curStatsInCRCErrorPkts,'curStatsInDropEvents':curStatsInDropEvents,'curStatsInJabbers':curStatsInJabbers,'curStatsInCollision':curStatsInCollision,'curStatsOutOctets':curStatsOutOctets,'curStatsOutPkts':curStatsOutPkts,'curStatsOutBroadcastPkts':curStatsOutBroadcastPkts,'curStatsOutMulticastPkts':curStatsOutMulticastPkts,'curStatsOutPkts64Octets':curStatsOutPkts64Octets,'curStatsOutPkts65to127Octets':curStatsOutPkts65to127Octets,'curStatsOutPkts128to255Octets':curStatsOutPkts128to255Octets,'curStatsOutPkts256to511Octets':curStatsOutPkts256to511Octets,'curStatsOutPkts512to1023Octets':curStatsOutPkts512to1023Octets,'curStatsOutPkts1024to1518Octets':curStatsOutPkts1024to1518Octets,'curStatsOutPkts1519o1522Octets':curStatsOutPkts1519o1522Octets,'curStatsOutUndersizePkts':curStatsOutUndersizePkts,'curStatsOutOversizePkts':curStatsOutOversizePkts,'curStatsOutFragments':curStatsOutFragments,'curStatsOutMpcpFrames':curStatsOutMpcpFrames,'curStatsOutMpcpOctets':curStatsOutMpcpOctets,'curStatsOutOAMFrames':curStatsOutOAMFrames,'curStatsOutOAMOctets':curStatsOutOAMOctets,'curStatsOutCRCErrorPkts':curStatsOutCRCErrorPkts,'curStatsOutDropEvents':curStatsOutDropEvents,'curStatsOutJabbers':curStatsOutJabbers,'curStatsOutCollision':curStatsOutCollision,'curStatsStatusAndAction':curStatsStatusAndAction,'stats15Table':stats15Table,'stats15Entry':stats15Entry,_N:stats15DeviceIndex,_O:stats15CardIndex,_P:stats15PortIndex,_Q:stats15Index,'stats15InOctets':stats15InOctets,'stats15InPkts':stats15InPkts,'stats15InBroadcastPkts':stats15InBroadcastPkts,'stats15InMulticastPkts':stats15InMulticastPkts,'stats15InPkts64Octets':stats15InPkts64Octets,'stats15InPkts65to127Octets':stats15InPkts65to127Octets,'stats15InPkts128to255Octets':stats15InPkts128to255Octets,'stats15InPkts256to511Octets':stats15InPkts256to511Octets,'stats15InPkts512to1023Octets':stats15InPkts512to1023Octets,'stats15InPkts1024to1518Octets':stats15InPkts1024to1518Octets,'stats15InPkts1519to1522Octets':stats15InPkts1519to1522Octets,'stats15InUndersizePkts':stats15InUndersizePkts,'stats15InOversizePkts':stats15InOversizePkts,'stats15InFragments':stats15InFragments,'stats15InMpcpFrames':stats15InMpcpFrames,'stats15InMpcpOctets':stats15InMpcpOctets,'stats15InOAMFrames':stats15InOAMFrames,'stats15InOAMOctets':stats15InOAMOctets,'stats15InCRCErrorPkts':stats15InCRCErrorPkts,'stats15InDropEvents':stats15InDropEvents,'stats15InJabbers':stats15InJabbers,'stats15InCollision':stats15InCollision,'stats15OutOctets':stats15OutOctets,'stats15OutPkts':stats15OutPkts,'stats15OutBroadcastPkts':stats15OutBroadcastPkts,'stats15OutMulticastPkts':stats15OutMulticastPkts,'stats15OutPkts64Octets':stats15OutPkts64Octets,'stats15OutPkts65to127Octets':stats15OutPkts65to127Octets,'stats15OutPkts128to255Octets':stats15OutPkts128to255Octets,'stats15OutPkts256to511Octets':stats15OutPkts256to511Octets,'stats15OutPkts512to1023Octets':stats15OutPkts512to1023Octets,'stats15OutPkts1024to1518Octets':stats15OutPkts1024to1518Octets,'stats15OutPkts1519o1522Octets':stats15OutPkts1519o1522Octets,'stats15OutUndersizePkts':stats15OutUndersizePkts,'stats15OutOversizePkts':stats15OutOversizePkts,'stats15OutFragments':stats15OutFragments,'stats15OutMpcpFrames':stats15OutMpcpFrames,'stats15OutMpcpOctets':stats15OutMpcpOctets,'stats15OutOAMFrames':stats15OutOAMFrames,'stats15OutOAMOctets':stats15OutOAMOctets,'stats15OutCRCErrorPkts':stats15OutCRCErrorPkts,'stats15OutDropEvents':stats15OutDropEvents,'stats15OutJabbers':stats15OutJabbers,'stats15OutCollision':stats15OutCollision,'stats15StatusAndAction':stats15StatusAndAction,'stats15ValidityTag':stats15ValidityTag,'stats15ElapsedTime':stats15ElapsedTime,'stats15EndTime':stats15EndTime,'stats24Table':stats24Table,'stats24Entry':stats24Entry,_S:stats24DeviceIndex,_T:stats24CardIndex,_U:stats24PortIndex,_V:stats24Index,'stats24InOctets':stats24InOctets,'stats24InPkts':stats24InPkts,'stats24InBroadcastPkts':stats24InBroadcastPkts,'stats24InMulticastPkts':stats24InMulticastPkts,'stats24InPkts64Octets':stats24InPkts64Octets,'stats24InPkts65to127Octets':stats24InPkts65to127Octets,'stats24InPkts128to255Octets':stats24InPkts128to255Octets,'stats24InPkts256to511Octets':stats24InPkts256to511Octets,'stats24InPkts512to1023Octets':stats24InPkts512to1023Octets,'stats24InPkts1024to1518Octets':stats24InPkts1024to1518Octets,'stats24InPkts1519to1522Octets':stats24InPkts1519to1522Octets,'stats24InUndersizePkts':stats24InUndersizePkts,'stats24InOversizePkts':stats24InOversizePkts,'stats24InFragments':stats24InFragments,'stats24InMpcpFrames':stats24InMpcpFrames,'stats24InMpcpOctets':stats24InMpcpOctets,'stats24InOAMFrames':stats24InOAMFrames,'stats24InOAMOctets':stats24InOAMOctets,'stats24InCRCErrorPkts':stats24InCRCErrorPkts,'stats24InDropEvents':stats24InDropEvents,'stats24InJabbers':stats24InJabbers,'stats24InCollision':stats24InCollision,'stats24OutOctets':stats24OutOctets,'stats24OutPkts':stats24OutPkts,'stats24OutBroadcastPkts':stats24OutBroadcastPkts,'stats24OutMulticastPkts':stats24OutMulticastPkts,'stats24OutPkts64Octets':stats24OutPkts64Octets,'stats24OutPkts65to127Octets':stats24OutPkts65to127Octets,'stats24OutPkts128to255Octets':stats24OutPkts128to255Octets,'stats24OutPkts256to511Octets':stats24OutPkts256to511Octets,'stats24OutPkts512to1023Octets':stats24OutPkts512to1023Octets,'stats24OutPkts1024to1518Octets':stats24OutPkts1024to1518Octets,'stats24OutPkts1519o1522Octets':stats24OutPkts1519o1522Octets,'stats24OutUndersizePkts':stats24OutUndersizePkts,'stats24OutOversizePkts':stats24OutOversizePkts,'stats24OutFragments':stats24OutFragments,'stats24OutMpcpFrames':stats24OutMpcpFrames,'stats24OutMpcpOctets':stats24OutMpcpOctets,'stats24OutOAMFrames':stats24OutOAMFrames,'stats24OutOAMOctets':stats24OutOAMOctets,'stats24OutCRCErrorPkts':stats24OutCRCErrorPkts,'stats24OutDropEvents':stats24OutDropEvents,'stats24OutJabbers':stats24OutJabbers,'stats24OutCollision':stats24OutCollision,'stats24StatusAndAction':stats24StatusAndAction,'stats24ValidityTag':stats24ValidityTag,'stats24ElapsedTime':stats24ElapsedTime,'stats24EndTime':stats24EndTime,'perfStatsGlobalSet':perfStatsGlobalSet,'perfStats15MinMaxRecord':perfStats15MinMaxRecord,'perfStats24HourMaxRecord':perfStats24HourMaxRecord,'perfStatsThresholdTable':perfStatsThresholdTable,'perfStatsThresholdEntry':perfStatsThresholdEntry,_W:perfStatsThresholdDeviceIndex,_X:perfStatsThresholdCardIndex,_Y:perfStatsThresholdPortIndex,_Z:perfStatsThresholdTypeIndex,'perfStatsThresholdUpper':perfStatsThresholdUpper,'perfStatsThresholdLower':perfStatsThresholdLower,'perfStatsThresholdRowStatus':perfStatsThresholdRowStatus})