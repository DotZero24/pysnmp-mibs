_v='ciscoOamPingMIBGroupRev3'
_u='ciscoOamPing2MIBGroup'
_t='ciscoOamPingMIBGroup'
_s='oamLoopbackPingCompletionTrap'
_r='oamLoopbackPingMaxRttuSec'
_q='oamLoopbackPingMinRttuSec'
_p='oamLoopbackPingAvgRttuSec'
_o='oamLoopSegRowStatus'
_n='oamLoopSegVci'
_m='oamLoopSegVpi'
_l='oamLoopbackPingSerialNumber'
_k='TruthValue'
_j='ifIndex'
_i='IF-MIB'
_h='OctetString'
_g='ciscoOamPingSegEndPointGroup'
_f='oamLoopbackNotificationsGroup'
_e='oamLoopbackPingExecTime'
_d='oamLoopbackPingOperStatus'
_c='oamLoopbackPingDir'
_b='microseconds'
_a='not-accessible'
_Z='Unsigned32'
_Y='deprecated'
_X='oamLoopbackPingEntryStatus'
_W='oamLoopbackPingEntryOwner'
_V='oamLoopbackPingMaxRtt'
_U='oamLoopbackPingAvgRtt'
_T='oamLoopbackPingMinRtt'
_S='oamLoopbackPingReceivedCells'
_R='oamLoopbackPingSentCells'
_Q='oamLoopbackPingTrapOnCompletion'
_P='oamLoopbackPingDelay'
_O='oamLoopbackPingTimeout'
_N='oamLoopbackPingLocationFlag'
_M='oamLoopbackPingLocation'
_L='oamLoopbackPingType'
_K='oamLoopbackPingCount'
_J='oamLoopbackPingVci'
_I='oamLoopbackPingVpi'
_H='oamLoopbackPingInterface'
_G='oamLoopbackPingCompleted'
_F='milliseconds'
_E='read-only'
_D='read-create'
_C='Integer32'
_B='current'
_A='CISCO-OAM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_h,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_i,_j)
OwnerString,=mibBuilder.importSymbols('RMON-MIB','OwnerString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Z,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_k)
ciscoOamPingMIB=ModuleIdentity((1,3,6,1,4,1,9,10,15))
if mibBuilder.loadTexts:ciscoOamPingMIB.setRevisions(('2006-02-17 00:00','2003-06-27 00:00','2003-04-04 00:00','1996-05-01 00:00'))
class CiscoOAMPingDir(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('backward',2)))
class CiscoOAMPingStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('success',1),('timeOut',2),('resourceNotAvailable',3),('aborted',4),('inProgress',5),('noResponseData',6),('failToStart',7)))
_CiscoOamPingMIBObjects_ObjectIdentity=ObjectIdentity
ciscoOamPingMIBObjects=_CiscoOamPingMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,15,1))
_OamLoopbackPingTable_Object=MibTable
oamLoopbackPingTable=_OamLoopbackPingTable_Object((1,3,6,1,4,1,9,10,15,1,1))
if mibBuilder.loadTexts:oamLoopbackPingTable.setStatus(_B)
_OamLoopbackPingEntry_Object=MibTableRow
oamLoopbackPingEntry=_OamLoopbackPingEntry_Object((1,3,6,1,4,1,9,10,15,1,1,1))
oamLoopbackPingEntry.setIndexNames((0,_A,_l))
if mibBuilder.loadTexts:oamLoopbackPingEntry.setStatus(_B)
class _OamLoopbackPingSerialNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OamLoopbackPingSerialNumber_Type.__name__=_C
_OamLoopbackPingSerialNumber_Object=MibTableColumn
oamLoopbackPingSerialNumber=_OamLoopbackPingSerialNumber_Object((1,3,6,1,4,1,9,10,15,1,1,1,1),_OamLoopbackPingSerialNumber_Type())
oamLoopbackPingSerialNumber.setMaxAccess(_a)
if mibBuilder.loadTexts:oamLoopbackPingSerialNumber.setStatus(_B)
class _OamLoopbackPingInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OamLoopbackPingInterface_Type.__name__=_C
_OamLoopbackPingInterface_Object=MibTableColumn
oamLoopbackPingInterface=_OamLoopbackPingInterface_Object((1,3,6,1,4,1,9,10,15,1,1,1,2),_OamLoopbackPingInterface_Type())
oamLoopbackPingInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingInterface.setStatus(_B)
class _OamLoopbackPingVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_OamLoopbackPingVpi_Type.__name__=_C
_OamLoopbackPingVpi_Object=MibTableColumn
oamLoopbackPingVpi=_OamLoopbackPingVpi_Object((1,3,6,1,4,1,9,10,15,1,1,1,3),_OamLoopbackPingVpi_Type())
oamLoopbackPingVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingVpi.setStatus(_B)
class _OamLoopbackPingVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65535))
_OamLoopbackPingVci_Type.__name__=_C
_OamLoopbackPingVci_Object=MibTableColumn
oamLoopbackPingVci=_OamLoopbackPingVci_Object((1,3,6,1,4,1,9,10,15,1,1,1,4),_OamLoopbackPingVci_Type())
oamLoopbackPingVci.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingVci.setStatus(_B)
class _OamLoopbackPingType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('segment',1),('end2end',2)))
_OamLoopbackPingType_Type.__name__=_C
_OamLoopbackPingType_Object=MibTableColumn
oamLoopbackPingType=_OamLoopbackPingType_Object((1,3,6,1,4,1,9,10,15,1,1,1,5),_OamLoopbackPingType_Type())
oamLoopbackPingType.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingType.setStatus(_B)
class _OamLoopbackPingLocation_Type(OctetString):defaultHexValue='FF';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_OamLoopbackPingLocation_Type.__name__=_h
_OamLoopbackPingLocation_Object=MibTableColumn
oamLoopbackPingLocation=_OamLoopbackPingLocation_Object((1,3,6,1,4,1,9,10,15,1,1,1,6),_OamLoopbackPingLocation_Type())
oamLoopbackPingLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingLocation.setStatus(_B)
class _OamLoopbackPingLocationFlag_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipAddress',1),('nsapPrefix',2),('fixed16byteValue',3)))
_OamLoopbackPingLocationFlag_Type.__name__=_C
_OamLoopbackPingLocationFlag_Object=MibTableColumn
oamLoopbackPingLocationFlag=_OamLoopbackPingLocationFlag_Object((1,3,6,1,4,1,9,10,15,1,1,1,7),_OamLoopbackPingLocationFlag_Type())
oamLoopbackPingLocationFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingLocationFlag.setStatus(_B)
class _OamLoopbackPingCount_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OamLoopbackPingCount_Type.__name__=_C
_OamLoopbackPingCount_Object=MibTableColumn
oamLoopbackPingCount=_OamLoopbackPingCount_Object((1,3,6,1,4,1,9,10,15,1,1,1,8),_OamLoopbackPingCount_Type())
oamLoopbackPingCount.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingCount.setStatus(_B)
class _OamLoopbackPingTimeout_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_OamLoopbackPingTimeout_Type.__name__=_C
_OamLoopbackPingTimeout_Object=MibTableColumn
oamLoopbackPingTimeout=_OamLoopbackPingTimeout_Object((1,3,6,1,4,1,9,10,15,1,1,1,9),_OamLoopbackPingTimeout_Type())
oamLoopbackPingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingTimeout.setStatus(_B)
if mibBuilder.loadTexts:oamLoopbackPingTimeout.setUnits(_F)
class _OamLoopbackPingDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600000))
_OamLoopbackPingDelay_Type.__name__=_C
_OamLoopbackPingDelay_Object=MibTableColumn
oamLoopbackPingDelay=_OamLoopbackPingDelay_Object((1,3,6,1,4,1,9,10,15,1,1,1,10),_OamLoopbackPingDelay_Type())
oamLoopbackPingDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingDelay.setStatus(_B)
if mibBuilder.loadTexts:oamLoopbackPingDelay.setUnits(_F)
class _OamLoopbackPingTrapOnCompletion_Type(TruthValue):defaultValue=2
_OamLoopbackPingTrapOnCompletion_Type.__name__=_k
_OamLoopbackPingTrapOnCompletion_Object=MibTableColumn
oamLoopbackPingTrapOnCompletion=_OamLoopbackPingTrapOnCompletion_Object((1,3,6,1,4,1,9,10,15,1,1,1,11),_OamLoopbackPingTrapOnCompletion_Type())
oamLoopbackPingTrapOnCompletion.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingTrapOnCompletion.setStatus(_B)
_OamLoopbackPingSentCells_Type=Counter32
_OamLoopbackPingSentCells_Object=MibTableColumn
oamLoopbackPingSentCells=_OamLoopbackPingSentCells_Object((1,3,6,1,4,1,9,10,15,1,1,1,12),_OamLoopbackPingSentCells_Type())
oamLoopbackPingSentCells.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingSentCells.setStatus(_B)
_OamLoopbackPingReceivedCells_Type=Counter32
_OamLoopbackPingReceivedCells_Object=MibTableColumn
oamLoopbackPingReceivedCells=_OamLoopbackPingReceivedCells_Object((1,3,6,1,4,1,9,10,15,1,1,1,13),_OamLoopbackPingReceivedCells_Type())
oamLoopbackPingReceivedCells.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingReceivedCells.setStatus(_B)
class _OamLoopbackPingMinRtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OamLoopbackPingMinRtt_Type.__name__=_C
_OamLoopbackPingMinRtt_Object=MibTableColumn
oamLoopbackPingMinRtt=_OamLoopbackPingMinRtt_Object((1,3,6,1,4,1,9,10,15,1,1,1,14),_OamLoopbackPingMinRtt_Type())
oamLoopbackPingMinRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingMinRtt.setStatus(_B)
if mibBuilder.loadTexts:oamLoopbackPingMinRtt.setUnits(_F)
class _OamLoopbackPingAvgRtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OamLoopbackPingAvgRtt_Type.__name__=_C
_OamLoopbackPingAvgRtt_Object=MibTableColumn
oamLoopbackPingAvgRtt=_OamLoopbackPingAvgRtt_Object((1,3,6,1,4,1,9,10,15,1,1,1,15),_OamLoopbackPingAvgRtt_Type())
oamLoopbackPingAvgRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingAvgRtt.setStatus(_B)
if mibBuilder.loadTexts:oamLoopbackPingAvgRtt.setUnits(_F)
class _OamLoopbackPingMaxRtt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OamLoopbackPingMaxRtt_Type.__name__=_C
_OamLoopbackPingMaxRtt_Object=MibTableColumn
oamLoopbackPingMaxRtt=_OamLoopbackPingMaxRtt_Object((1,3,6,1,4,1,9,10,15,1,1,1,16),_OamLoopbackPingMaxRtt_Type())
oamLoopbackPingMaxRtt.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingMaxRtt.setStatus(_B)
if mibBuilder.loadTexts:oamLoopbackPingMaxRtt.setUnits(_F)
_OamLoopbackPingCompleted_Type=TruthValue
_OamLoopbackPingCompleted_Object=MibTableColumn
oamLoopbackPingCompleted=_OamLoopbackPingCompleted_Object((1,3,6,1,4,1,9,10,15,1,1,1,17),_OamLoopbackPingCompleted_Type())
oamLoopbackPingCompleted.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingCompleted.setStatus(_B)
_OamLoopbackPingEntryOwner_Type=OwnerString
_OamLoopbackPingEntryOwner_Object=MibTableColumn
oamLoopbackPingEntryOwner=_OamLoopbackPingEntryOwner_Object((1,3,6,1,4,1,9,10,15,1,1,1,18),_OamLoopbackPingEntryOwner_Type())
oamLoopbackPingEntryOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingEntryOwner.setStatus(_B)
_OamLoopbackPingEntryStatus_Type=RowStatus
_OamLoopbackPingEntryStatus_Object=MibTableColumn
oamLoopbackPingEntryStatus=_OamLoopbackPingEntryStatus_Object((1,3,6,1,4,1,9,10,15,1,1,1,19),_OamLoopbackPingEntryStatus_Type())
oamLoopbackPingEntryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingEntryStatus.setStatus(_B)
_OamLoopbackPingDir_Type=CiscoOAMPingDir
_OamLoopbackPingDir_Object=MibTableColumn
oamLoopbackPingDir=_OamLoopbackPingDir_Object((1,3,6,1,4,1,9,10,15,1,1,1,20),_OamLoopbackPingDir_Type())
oamLoopbackPingDir.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopbackPingDir.setStatus(_B)
_OamLoopbackPingOperStatus_Type=CiscoOAMPingStatus
_OamLoopbackPingOperStatus_Object=MibTableColumn
oamLoopbackPingOperStatus=_OamLoopbackPingOperStatus_Object((1,3,6,1,4,1,9,10,15,1,1,1,21),_OamLoopbackPingOperStatus_Type())
oamLoopbackPingOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingOperStatus.setStatus(_B)
_OamLoopbackPingExecTime_Type=TimeStamp
_OamLoopbackPingExecTime_Object=MibTableColumn
oamLoopbackPingExecTime=_OamLoopbackPingExecTime_Object((1,3,6,1,4,1,9,10,15,1,1,1,22),_OamLoopbackPingExecTime_Type())
oamLoopbackPingExecTime.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingExecTime.setStatus(_B)
class _OamLoopbackPingMinRttuSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OamLoopbackPingMinRttuSec_Type.__name__=_C
_OamLoopbackPingMinRttuSec_Object=MibTableColumn
oamLoopbackPingMinRttuSec=_OamLoopbackPingMinRttuSec_Object((1,3,6,1,4,1,9,10,15,1,1,1,23),_OamLoopbackPingMinRttuSec_Type())
oamLoopbackPingMinRttuSec.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingMinRttuSec.setStatus(_B)
if mibBuilder.loadTexts:oamLoopbackPingMinRttuSec.setUnits(_b)
class _OamLoopbackPingAvgRttuSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OamLoopbackPingAvgRttuSec_Type.__name__=_C
_OamLoopbackPingAvgRttuSec_Object=MibTableColumn
oamLoopbackPingAvgRttuSec=_OamLoopbackPingAvgRttuSec_Object((1,3,6,1,4,1,9,10,15,1,1,1,24),_OamLoopbackPingAvgRttuSec_Type())
oamLoopbackPingAvgRttuSec.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingAvgRttuSec.setStatus(_B)
if mibBuilder.loadTexts:oamLoopbackPingAvgRttuSec.setUnits(_b)
class _OamLoopbackPingMaxRttuSec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_OamLoopbackPingMaxRttuSec_Type.__name__=_C
_OamLoopbackPingMaxRttuSec_Object=MibTableColumn
oamLoopbackPingMaxRttuSec=_OamLoopbackPingMaxRttuSec_Object((1,3,6,1,4,1,9,10,15,1,1,1,25),_OamLoopbackPingMaxRttuSec_Type())
oamLoopbackPingMaxRttuSec.setMaxAccess(_E)
if mibBuilder.loadTexts:oamLoopbackPingMaxRttuSec.setStatus(_B)
if mibBuilder.loadTexts:oamLoopbackPingMaxRttuSec.setUnits(_b)
_OamLoopbackSegEndPointTable_Object=MibTable
oamLoopbackSegEndPointTable=_OamLoopbackSegEndPointTable_Object((1,3,6,1,4,1,9,10,15,1,2))
if mibBuilder.loadTexts:oamLoopbackSegEndPointTable.setStatus(_B)
_OamLoopbackSegEndPointEntry_Object=MibTableRow
oamLoopbackSegEndPointEntry=_OamLoopbackSegEndPointEntry_Object((1,3,6,1,4,1,9,10,15,1,2,1))
oamLoopbackSegEndPointEntry.setIndexNames((0,_i,_j),(0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:oamLoopbackSegEndPointEntry.setStatus(_B)
class _OamLoopSegVpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_OamLoopSegVpi_Type.__name__=_Z
_OamLoopSegVpi_Object=MibTableColumn
oamLoopSegVpi=_OamLoopSegVpi_Object((1,3,6,1,4,1,9,10,15,1,2,1,1),_OamLoopSegVpi_Type())
oamLoopSegVpi.setMaxAccess(_a)
if mibBuilder.loadTexts:oamLoopSegVpi.setStatus(_B)
class _OamLoopSegVci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OamLoopSegVci_Type.__name__=_Z
_OamLoopSegVci_Object=MibTableColumn
oamLoopSegVci=_OamLoopSegVci_Object((1,3,6,1,4,1,9,10,15,1,2,1,2),_OamLoopSegVci_Type())
oamLoopSegVci.setMaxAccess(_a)
if mibBuilder.loadTexts:oamLoopSegVci.setStatus(_B)
_OamLoopSegRowStatus_Type=RowStatus
_OamLoopSegRowStatus_Object=MibTableColumn
oamLoopSegRowStatus=_OamLoopSegRowStatus_Object((1,3,6,1,4,1,9,10,15,1,2,1,3),_OamLoopSegRowStatus_Type())
oamLoopSegRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oamLoopSegRowStatus.setStatus(_B)
_OamLoopbackPingMIBTrapPrefix_ObjectIdentity=ObjectIdentity
oamLoopbackPingMIBTrapPrefix=_OamLoopbackPingMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,15,2))
_OamLoopbackPingMIBTraps_ObjectIdentity=ObjectIdentity
oamLoopbackPingMIBTraps=_OamLoopbackPingMIBTraps_ObjectIdentity((1,3,6,1,4,1,9,10,15,2,0))
_CiscoOamPingMIBConformance_ObjectIdentity=ObjectIdentity
ciscoOamPingMIBConformance=_CiscoOamPingMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,15,3))
_CiscoOamPingMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoOamPingMIBCompliances=_CiscoOamPingMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,15,3,1))
_CiscoOamPingMIBGroups_ObjectIdentity=ObjectIdentity
ciscoOamPingMIBGroups=_CiscoOamPingMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,15,3,2))
ciscoOamPingMIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,15,3,2,1))
ciscoOamPingMIBGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_G),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:ciscoOamPingMIBGroup.setStatus(_Y)
ciscoOamPing2MIBGroup=ObjectGroup((1,3,6,1,4,1,9,10,15,3,2,2))
ciscoOamPing2MIBGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_G),(_A,_W),(_A,_X),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoOamPing2MIBGroup.setStatus(_Y)
ciscoOamPingSegEndPointGroup=ObjectGroup((1,3,6,1,4,1,9,10,15,3,2,3))
ciscoOamPingSegEndPointGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:ciscoOamPingSegEndPointGroup.setStatus(_B)
ciscoOamPingMIBGroupRev3=ObjectGroup((1,3,6,1,4,1,9,10,15,3,2,5))
ciscoOamPingMIBGroupRev3.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_G),(_A,_W),(_A,_X),(_A,_c),(_A,_d),(_A,_e),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:ciscoOamPingMIBGroupRev3.setStatus(_B)
oamLoopbackPingCompletionTrap=NotificationType((1,3,6,1,4,1,9,10,15,2,0,1))
oamLoopbackPingCompletionTrap.setObjects((_A,_G))
if mibBuilder.loadTexts:oamLoopbackPingCompletionTrap.setStatus(_B)
oamLoopbackNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,10,15,3,2,4))
oamLoopbackNotificationsGroup.setObjects((_A,_s))
if mibBuilder.loadTexts:oamLoopbackNotificationsGroup.setStatus(_B)
ciscoOamPingMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,15,3,1,1))
ciscoOamPingMIBCompliance.setObjects((_A,_t))
if mibBuilder.loadTexts:ciscoOamPingMIBCompliance.setStatus(_Y)
ciscoOamPingMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,15,3,1,2))
ciscoOamPingMIBCompliance2.setObjects(*((_A,_u),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoOamPingMIBCompliance2.setStatus(_Y)
ciscoOamPingMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,10,15,3,1,3))
ciscoOamPingMIBCompliance3.setObjects(*((_A,_v),(_A,_f),(_A,_g)))
if mibBuilder.loadTexts:ciscoOamPingMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoOAMPingDir':CiscoOAMPingDir,'CiscoOAMPingStatus':CiscoOAMPingStatus,'ciscoOamPingMIB':ciscoOamPingMIB,'ciscoOamPingMIBObjects':ciscoOamPingMIBObjects,'oamLoopbackPingTable':oamLoopbackPingTable,'oamLoopbackPingEntry':oamLoopbackPingEntry,_l:oamLoopbackPingSerialNumber,_H:oamLoopbackPingInterface,_I:oamLoopbackPingVpi,_J:oamLoopbackPingVci,_L:oamLoopbackPingType,_M:oamLoopbackPingLocation,_N:oamLoopbackPingLocationFlag,_K:oamLoopbackPingCount,_O:oamLoopbackPingTimeout,_P:oamLoopbackPingDelay,_Q:oamLoopbackPingTrapOnCompletion,_R:oamLoopbackPingSentCells,_S:oamLoopbackPingReceivedCells,_T:oamLoopbackPingMinRtt,_U:oamLoopbackPingAvgRtt,_V:oamLoopbackPingMaxRtt,_G:oamLoopbackPingCompleted,_W:oamLoopbackPingEntryOwner,_X:oamLoopbackPingEntryStatus,_c:oamLoopbackPingDir,_d:oamLoopbackPingOperStatus,_e:oamLoopbackPingExecTime,_q:oamLoopbackPingMinRttuSec,_p:oamLoopbackPingAvgRttuSec,_r:oamLoopbackPingMaxRttuSec,'oamLoopbackSegEndPointTable':oamLoopbackSegEndPointTable,'oamLoopbackSegEndPointEntry':oamLoopbackSegEndPointEntry,_m:oamLoopSegVpi,_n:oamLoopSegVci,_o:oamLoopSegRowStatus,'oamLoopbackPingMIBTrapPrefix':oamLoopbackPingMIBTrapPrefix,'oamLoopbackPingMIBTraps':oamLoopbackPingMIBTraps,_s:oamLoopbackPingCompletionTrap,'ciscoOamPingMIBConformance':ciscoOamPingMIBConformance,'ciscoOamPingMIBCompliances':ciscoOamPingMIBCompliances,'ciscoOamPingMIBCompliance':ciscoOamPingMIBCompliance,'ciscoOamPingMIBCompliance2':ciscoOamPingMIBCompliance2,'ciscoOamPingMIBCompliance3':ciscoOamPingMIBCompliance3,'ciscoOamPingMIBGroups':ciscoOamPingMIBGroups,_t:ciscoOamPingMIBGroup,_u:ciscoOamPing2MIBGroup,_g:ciscoOamPingSegEndPointGroup,_f:oamLoopbackNotificationsGroup,_v:ciscoOamPingMIBGroupRev3})