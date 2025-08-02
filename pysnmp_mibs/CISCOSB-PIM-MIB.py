_a='rlPimInterfaceEntry'
_Z='rlPimTmEntIndex'
_Y='StdAccessListListIndexOrZero'
_X='not-accessible'
_W='NumericIndexOrZero'
_V='operStatusActFailed'
_U='operStatusGoingDown'
_T='operStatusGoingUp'
_S='operStatusDown'
_R='operStatusUp'
_Q='pimNeighborIfIndex'
_P='pimNeighborAddressType'
_O='pimNeighborAddress'
_N='pimInterfaceIfIndex'
_M='pimInterfaceIPVersion'
_L='InetAddressType'
_K='rlPimNmEntIndex'
_J='AdminStatus'
_I='CISCOSB-PIM-MIB'
_H='seconds'
_G='DisplayString'
_F='PIM-STD-MIB'
_E='TruthValue'
_D='Unsigned32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
IANAipRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType,InetVersion=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength',_L,'InetVersion')
pimInterfaceEntry,pimInterfaceIPVersion,pimInterfaceIfIndex,pimNeighborAddress,pimNeighborAddressType,pimNeighborIfIndex=mibBuilder.importSymbols(_F,'pimInterfaceEntry',_M,_N,_O,_P,_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention',_E)
rlPim=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,211))
if mibBuilder.loadTexts:rlPim.setRevisions(('2008-09-25 00:00',))
class AdminStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('adminStatusUp',1),('adminStatusDown',2)))
class OperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5)))
class Unsigned32NonZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class NumericIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NumericIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class EntityIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class EntityIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class StdAccessListListIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class StdAccessListRuleIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class ExtAccessListListIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class ExtAccessListListIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class PimStatsCounter(TextualConvention,Unsigned32):status=_A
class NpgOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,8,10,11)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5),('operStatusFailed',8),('operStatusFailedPerm',10),('operStatusFailing',11)))
_RlPimInterfaceTable_Object=MibTable
rlPimInterfaceTable=_RlPimInterfaceTable_Object((1,3,6,1,4,1,9,6,1,101,211,1))
if mibBuilder.loadTexts:rlPimInterfaceTable.setStatus(_A)
_RlPimInterfaceEntry_Object=MibTableRow
rlPimInterfaceEntry=_RlPimInterfaceEntry_Object((1,3,6,1,4,1,9,6,1,101,211,1,1))
if mibBuilder.loadTexts:rlPimInterfaceEntry.setStatus(_A)
class _RlPimInterfaceAdminStatus_Type(AdminStatus):defaultValue=1
_RlPimInterfaceAdminStatus_Type.__name__=_J
_RlPimInterfaceAdminStatus_Object=MibTableColumn
rlPimInterfaceAdminStatus=_RlPimInterfaceAdminStatus_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,3),_RlPimInterfaceAdminStatus_Type())
rlPimInterfaceAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceAdminStatus.setStatus(_A)
_RlPimInterfaceOperStatus_Type=NpgOperStatus
_RlPimInterfaceOperStatus_Object=MibTableColumn
rlPimInterfaceOperStatus=_RlPimInterfaceOperStatus_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,4),_RlPimInterfaceOperStatus_Type())
rlPimInterfaceOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimInterfaceOperStatus.setStatus(_A)
class _RlPimInterfaceStubInterface_Type(TruthValue):defaultValue=2
_RlPimInterfaceStubInterface_Type.__name__=_E
_RlPimInterfaceStubInterface_Object=MibTableColumn
rlPimInterfaceStubInterface=_RlPimInterfaceStubInterface_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,5),_RlPimInterfaceStubInterface_Type())
rlPimInterfaceStubInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceStubInterface.setStatus(_A)
class _RlPimInterfaceP2PNoHellos_Type(TruthValue):defaultValue=2
_RlPimInterfaceP2PNoHellos_Type.__name__=_E
_RlPimInterfaceP2PNoHellos_Object=MibTableColumn
rlPimInterfaceP2PNoHellos=_RlPimInterfaceP2PNoHellos_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,6),_RlPimInterfaceP2PNoHellos_Type())
rlPimInterfaceP2PNoHellos.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceP2PNoHellos.setStatus(_A)
class _RlPimInterfaceMgmdEntIndex_Type(NumericIndexOrZero):defaultValue=0
_RlPimInterfaceMgmdEntIndex_Type.__name__=_W
_RlPimInterfaceMgmdEntIndex_Object=MibTableColumn
rlPimInterfaceMgmdEntIndex=_RlPimInterfaceMgmdEntIndex_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,7),_RlPimInterfaceMgmdEntIndex_Type())
rlPimInterfaceMgmdEntIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceMgmdEntIndex.setStatus(_A)
_RlPimInterfaceNeighborCount_Type=Gauge32
_RlPimInterfaceNeighborCount_Object=MibTableColumn
rlPimInterfaceNeighborCount=_RlPimInterfaceNeighborCount_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,8),_RlPimInterfaceNeighborCount_Type())
rlPimInterfaceNeighborCount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimInterfaceNeighborCount.setStatus(_A)
class _RlPimInterfaceStarGStateLimit_Type(Unsigned32):defaultValue=0
_RlPimInterfaceStarGStateLimit_Type.__name__=_D
_RlPimInterfaceStarGStateLimit_Object=MibTableColumn
rlPimInterfaceStarGStateLimit=_RlPimInterfaceStarGStateLimit_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,9),_RlPimInterfaceStarGStateLimit_Type())
rlPimInterfaceStarGStateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceStarGStateLimit.setStatus(_A)
class _RlPimInterfaceStarGStateWarnThold_Type(Unsigned32):defaultValue=0
_RlPimInterfaceStarGStateWarnThold_Type.__name__=_D
_RlPimInterfaceStarGStateWarnThold_Object=MibTableColumn
rlPimInterfaceStarGStateWarnThold=_RlPimInterfaceStarGStateWarnThold_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,10),_RlPimInterfaceStarGStateWarnThold_Type())
rlPimInterfaceStarGStateWarnThold.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceStarGStateWarnThold.setStatus(_A)
_RlPimInterfaceStarGStateStored_Type=Gauge32
_RlPimInterfaceStarGStateStored_Object=MibTableColumn
rlPimInterfaceStarGStateStored=_RlPimInterfaceStarGStateStored_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,11),_RlPimInterfaceStarGStateStored_Type())
rlPimInterfaceStarGStateStored.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimInterfaceStarGStateStored.setStatus(_A)
class _RlPimInterfaceSGStateLimit_Type(Unsigned32):defaultValue=0
_RlPimInterfaceSGStateLimit_Type.__name__=_D
_RlPimInterfaceSGStateLimit_Object=MibTableColumn
rlPimInterfaceSGStateLimit=_RlPimInterfaceSGStateLimit_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,12),_RlPimInterfaceSGStateLimit_Type())
rlPimInterfaceSGStateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceSGStateLimit.setStatus(_A)
class _RlPimInterfaceSGStateWarnThold_Type(Unsigned32):defaultValue=0
_RlPimInterfaceSGStateWarnThold_Type.__name__=_D
_RlPimInterfaceSGStateWarnThold_Object=MibTableColumn
rlPimInterfaceSGStateWarnThold=_RlPimInterfaceSGStateWarnThold_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,13),_RlPimInterfaceSGStateWarnThold_Type())
rlPimInterfaceSGStateWarnThold.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceSGStateWarnThold.setStatus(_A)
_RlPimInterfaceSGStateStored_Type=Gauge32
_RlPimInterfaceSGStateStored_Object=MibTableColumn
rlPimInterfaceSGStateStored=_RlPimInterfaceSGStateStored_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,14),_RlPimInterfaceSGStateStored_Type())
rlPimInterfaceSGStateStored.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimInterfaceSGStateStored.setStatus(_A)
class _RlPimInterfaceNeighborFilter_Type(DisplayString):defaultValue=OctetString('')
_RlPimInterfaceNeighborFilter_Type.__name__=_G
_RlPimInterfaceNeighborFilter_Object=MibTableColumn
rlPimInterfaceNeighborFilter=_RlPimInterfaceNeighborFilter_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,15),_RlPimInterfaceNeighborFilter_Type())
rlPimInterfaceNeighborFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceNeighborFilter.setStatus(_A)
class _RlPimInterfaceAssertInterval_Type(Unsigned32):defaultValue=177;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlPimInterfaceAssertInterval_Type.__name__=_D
_RlPimInterfaceAssertInterval_Object=MibTableColumn
rlPimInterfaceAssertInterval=_RlPimInterfaceAssertInterval_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,16),_RlPimInterfaceAssertInterval_Type())
rlPimInterfaceAssertInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceAssertInterval.setStatus(_A)
if mibBuilder.loadTexts:rlPimInterfaceAssertInterval.setUnits(_H)
class _RlPimInterfaceAssertHoldtime_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlPimInterfaceAssertHoldtime_Type.__name__=_D
_RlPimInterfaceAssertHoldtime_Object=MibTableColumn
rlPimInterfaceAssertHoldtime=_RlPimInterfaceAssertHoldtime_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,17),_RlPimInterfaceAssertHoldtime_Type())
rlPimInterfaceAssertHoldtime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceAssertHoldtime.setStatus(_A)
if mibBuilder.loadTexts:rlPimInterfaceAssertHoldtime.setUnits(_H)
class _RlPimInterfaceAsmGrpFilter_Type(DisplayString):defaultValue=OctetString('')
_RlPimInterfaceAsmGrpFilter_Type.__name__=_G
_RlPimInterfaceAsmGrpFilter_Object=MibTableColumn
rlPimInterfaceAsmGrpFilter=_RlPimInterfaceAsmGrpFilter_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,18),_RlPimInterfaceAsmGrpFilter_Type())
rlPimInterfaceAsmGrpFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceAsmGrpFilter.setStatus(_A)
class _RlPimInterfaceSsmSrcAndGrpFilter_Type(DisplayString):defaultValue=OctetString('')
_RlPimInterfaceSsmSrcAndGrpFilter_Type.__name__=_G
_RlPimInterfaceSsmSrcAndGrpFilter_Object=MibTableColumn
rlPimInterfaceSsmSrcAndGrpFilter=_RlPimInterfaceSsmSrcAndGrpFilter_Object((1,3,6,1,4,1,9,6,1,101,211,1,1,19),_RlPimInterfaceSsmSrcAndGrpFilter_Type())
rlPimInterfaceSsmSrcAndGrpFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimInterfaceSsmSrcAndGrpFilter.setStatus(_A)
_RlPimIfStatsTable_Object=MibTable
rlPimIfStatsTable=_RlPimIfStatsTable_Object((1,3,6,1,4,1,9,6,1,101,211,2))
if mibBuilder.loadTexts:rlPimIfStatsTable.setStatus(_A)
_RlPimIfStatsEntry_Object=MibTableRow
rlPimIfStatsEntry=_RlPimIfStatsEntry_Object((1,3,6,1,4,1,9,6,1,101,211,2,1))
rlPimIfStatsEntry.setIndexNames((0,_F,_N),(0,_F,_M))
if mibBuilder.loadTexts:rlPimIfStatsEntry.setStatus(_A)
_RlPimIfStatsNumSentHello_Type=PimStatsCounter
_RlPimIfStatsNumSentHello_Object=MibTableColumn
rlPimIfStatsNumSentHello=_RlPimIfStatsNumSentHello_Object((1,3,6,1,4,1,9,6,1,101,211,2,1,1),_RlPimIfStatsNumSentHello_Type())
rlPimIfStatsNumSentHello.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimIfStatsNumSentHello.setStatus(_A)
_RlPimIfStatsNumSentJoinPrune_Type=PimStatsCounter
_RlPimIfStatsNumSentJoinPrune_Object=MibTableColumn
rlPimIfStatsNumSentJoinPrune=_RlPimIfStatsNumSentJoinPrune_Object((1,3,6,1,4,1,9,6,1,101,211,2,1,2),_RlPimIfStatsNumSentJoinPrune_Type())
rlPimIfStatsNumSentJoinPrune.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimIfStatsNumSentJoinPrune.setStatus(_A)
_RlPimIfStatsNumSentAssert_Type=PimStatsCounter
_RlPimIfStatsNumSentAssert_Object=MibTableColumn
rlPimIfStatsNumSentAssert=_RlPimIfStatsNumSentAssert_Object((1,3,6,1,4,1,9,6,1,101,211,2,1,3),_RlPimIfStatsNumSentAssert_Type())
rlPimIfStatsNumSentAssert.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimIfStatsNumSentAssert.setStatus(_A)
_RlPimIfStatsNumSentBsm_Type=PimStatsCounter
_RlPimIfStatsNumSentBsm_Object=MibTableColumn
rlPimIfStatsNumSentBsm=_RlPimIfStatsNumSentBsm_Object((1,3,6,1,4,1,9,6,1,101,211,2,1,4),_RlPimIfStatsNumSentBsm_Type())
rlPimIfStatsNumSentBsm.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimIfStatsNumSentBsm.setStatus(_A)
_RlPimIfStatsNumErrHello_Type=PimStatsCounter
_RlPimIfStatsNumErrHello_Object=MibTableColumn
rlPimIfStatsNumErrHello=_RlPimIfStatsNumErrHello_Object((1,3,6,1,4,1,9,6,1,101,211,2,1,5),_RlPimIfStatsNumErrHello_Type())
rlPimIfStatsNumErrHello.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimIfStatsNumErrHello.setStatus(_A)
_RlPimIfStatsNumRecvUnknownNbr_Type=PimStatsCounter
_RlPimIfStatsNumRecvUnknownNbr_Object=MibTableColumn
rlPimIfStatsNumRecvUnknownNbr=_RlPimIfStatsNumRecvUnknownNbr_Object((1,3,6,1,4,1,9,6,1,101,211,2,1,6),_RlPimIfStatsNumRecvUnknownNbr_Type())
rlPimIfStatsNumRecvUnknownNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimIfStatsNumRecvUnknownNbr.setStatus(_A)
_RlPimIfStatsNumUnknownHelloOpt_Type=PimStatsCounter
_RlPimIfStatsNumUnknownHelloOpt_Object=MibTableColumn
rlPimIfStatsNumUnknownHelloOpt=_RlPimIfStatsNumUnknownHelloOpt_Object((1,3,6,1,4,1,9,6,1,101,211,2,1,7),_RlPimIfStatsNumUnknownHelloOpt_Type())
rlPimIfStatsNumUnknownHelloOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimIfStatsNumUnknownHelloOpt.setStatus(_A)
_RlPimIfStatsNumFilteredOut_Type=PimStatsCounter
_RlPimIfStatsNumFilteredOut_Object=MibTableColumn
rlPimIfStatsNumFilteredOut=_RlPimIfStatsNumFilteredOut_Object((1,3,6,1,4,1,9,6,1,101,211,2,1,8),_RlPimIfStatsNumFilteredOut_Type())
rlPimIfStatsNumFilteredOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimIfStatsNumFilteredOut.setStatus(_A)
_RlPimNmEntTable_Object=MibTable
rlPimNmEntTable=_RlPimNmEntTable_Object((1,3,6,1,4,1,9,6,1,101,211,3))
if mibBuilder.loadTexts:rlPimNmEntTable.setStatus(_A)
_RlPimNmEntEntry_Object=MibTableRow
rlPimNmEntEntry=_RlPimNmEntEntry_Object((1,3,6,1,4,1,9,6,1,101,211,3,1))
rlPimNmEntEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:rlPimNmEntEntry.setStatus(_A)
_RlPimNmEntIndex_Type=NumericIndex
_RlPimNmEntIndex_Object=MibTableColumn
rlPimNmEntIndex=_RlPimNmEntIndex_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,1),_RlPimNmEntIndex_Type())
rlPimNmEntIndex.setMaxAccess(_X)
if mibBuilder.loadTexts:rlPimNmEntIndex.setStatus(_A)
_RlPimNmEntRowStatus_Type=RowStatus
_RlPimNmEntRowStatus_Object=MibTableColumn
rlPimNmEntRowStatus=_RlPimNmEntRowStatus_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,2),_RlPimNmEntRowStatus_Type())
rlPimNmEntRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimNmEntRowStatus.setStatus(_A)
class _RlPimNmEntAdminStatus_Type(AdminStatus):defaultValue=1
_RlPimNmEntAdminStatus_Type.__name__=_J
_RlPimNmEntAdminStatus_Object=MibTableColumn
rlPimNmEntAdminStatus=_RlPimNmEntAdminStatus_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,3),_RlPimNmEntAdminStatus_Type())
rlPimNmEntAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimNmEntAdminStatus.setStatus(_A)
_RlPimNmEntOperStatus_Type=NpgOperStatus
_RlPimNmEntOperStatus_Object=MibTableColumn
rlPimNmEntOperStatus=_RlPimNmEntOperStatus_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,4),_RlPimNmEntOperStatus_Type())
rlPimNmEntOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntOperStatus.setStatus(_A)
_RlPimNmEntTmEntIndex_Type=NumericIndex
_RlPimNmEntTmEntIndex_Object=MibTableColumn
rlPimNmEntTmEntIndex=_RlPimNmEntTmEntIndex_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,5),_RlPimNmEntTmEntIndex_Type())
rlPimNmEntTmEntIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimNmEntTmEntIndex.setStatus(_A)
_RlPimNmEntI3JoinOperStatus_Type=NpgOperStatus
_RlPimNmEntI3JoinOperStatus_Object=MibTableColumn
rlPimNmEntI3JoinOperStatus=_RlPimNmEntI3JoinOperStatus_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,6),_RlPimNmEntI3JoinOperStatus_Type())
rlPimNmEntI3JoinOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntI3JoinOperStatus.setStatus(_A)
_RlPimNmEntNmiJoinOperStatus_Type=NpgOperStatus
_RlPimNmEntNmiJoinOperStatus_Object=MibTableColumn
rlPimNmEntNmiJoinOperStatus=_RlPimNmEntNmiJoinOperStatus_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,7),_RlPimNmEntNmiJoinOperStatus_Type())
rlPimNmEntNmiJoinOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntNmiJoinOperStatus.setStatus(_A)
_RlPimNmEntSckJoinOperStatus_Type=NpgOperStatus
_RlPimNmEntSckJoinOperStatus_Object=MibTableColumn
rlPimNmEntSckJoinOperStatus=_RlPimNmEntSckJoinOperStatus_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,8),_RlPimNmEntSckJoinOperStatus_Type())
rlPimNmEntSckJoinOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntSckJoinOperStatus.setStatus(_A)
class _RlPimNmEntClearStatsCounters_Type(TruthValue):defaultValue=2
_RlPimNmEntClearStatsCounters_Type.__name__=_E
_RlPimNmEntClearStatsCounters_Object=MibTableColumn
rlPimNmEntClearStatsCounters=_RlPimNmEntClearStatsCounters_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,9),_RlPimNmEntClearStatsCounters_Type())
rlPimNmEntClearStatsCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimNmEntClearStatsCounters.setStatus(_A)
_RlPimNmEntStatsUpTime_Type=TimeTicks
_RlPimNmEntStatsUpTime_Object=MibTableColumn
rlPimNmEntStatsUpTime=_RlPimNmEntStatsUpTime_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,10),_RlPimNmEntStatsUpTime_Type())
rlPimNmEntStatsUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsUpTime.setStatus(_A)
class _RlPimNmEntEnableUnicastMessages_Type(TruthValue):defaultValue=1
_RlPimNmEntEnableUnicastMessages_Type.__name__=_E
_RlPimNmEntEnableUnicastMessages_Object=MibTableColumn
rlPimNmEntEnableUnicastMessages=_RlPimNmEntEnableUnicastMessages_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,11),_RlPimNmEntEnableUnicastMessages_Type())
rlPimNmEntEnableUnicastMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimNmEntEnableUnicastMessages.setStatus(_A)
class _RlPimNmEntAcceptUnicastBsms_Type(TruthValue):defaultValue=2
_RlPimNmEntAcceptUnicastBsms_Type.__name__=_E
_RlPimNmEntAcceptUnicastBsms_Object=MibTableColumn
rlPimNmEntAcceptUnicastBsms=_RlPimNmEntAcceptUnicastBsms_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,12),_RlPimNmEntAcceptUnicastBsms_Type())
rlPimNmEntAcceptUnicastBsms.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimNmEntAcceptUnicastBsms.setStatus(_A)
class _RlPimNmEntCrpAdvFilterIndex_Type(StdAccessListListIndexOrZero):defaultValue=0
_RlPimNmEntCrpAdvFilterIndex_Type.__name__=_Y
_RlPimNmEntCrpAdvFilterIndex_Object=MibTableColumn
rlPimNmEntCrpAdvFilterIndex=_RlPimNmEntCrpAdvFilterIndex_Object((1,3,6,1,4,1,9,6,1,101,211,3,1,13),_RlPimNmEntCrpAdvFilterIndex_Type())
rlPimNmEntCrpAdvFilterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimNmEntCrpAdvFilterIndex.setStatus(_A)
_RlPimNmEntStatsTable_Object=MibTable
rlPimNmEntStatsTable=_RlPimNmEntStatsTable_Object((1,3,6,1,4,1,9,6,1,101,211,4))
if mibBuilder.loadTexts:rlPimNmEntStatsTable.setStatus(_A)
_RlPimNmEntStatsEntry_Object=MibTableRow
rlPimNmEntStatsEntry=_RlPimNmEntStatsEntry_Object((1,3,6,1,4,1,9,6,1,101,211,4,1))
rlPimNmEntStatsEntry.setIndexNames((0,_I,_K))
if mibBuilder.loadTexts:rlPimNmEntStatsEntry.setStatus(_A)
_RlPimNmEntStatsNumSentCRPAdvert_Type=PimStatsCounter
_RlPimNmEntStatsNumSentCRPAdvert_Object=MibTableColumn
rlPimNmEntStatsNumSentCRPAdvert=_RlPimNmEntStatsNumSentCRPAdvert_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,1),_RlPimNmEntStatsNumSentCRPAdvert_Type())
rlPimNmEntStatsNumSentCRPAdvert.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumSentCRPAdvert.setStatus(_A)
_RlPimNmEntStatsNumSentRegister_Type=PimStatsCounter
_RlPimNmEntStatsNumSentRegister_Object=MibTableColumn
rlPimNmEntStatsNumSentRegister=_RlPimNmEntStatsNumSentRegister_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,2),_RlPimNmEntStatsNumSentRegister_Type())
rlPimNmEntStatsNumSentRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumSentRegister.setStatus(_A)
_RlPimNmEntStatsNumSentRegisterStop_Type=PimStatsCounter
_RlPimNmEntStatsNumSentRegisterStop_Object=MibTableColumn
rlPimNmEntStatsNumSentRegisterStop=_RlPimNmEntStatsNumSentRegisterStop_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,3),_RlPimNmEntStatsNumSentRegisterStop_Type())
rlPimNmEntStatsNumSentRegisterStop.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumSentRegisterStop.setStatus(_A)
_RlPimNmEntStatsNumRecvCRPAdvert_Type=PimStatsCounter
_RlPimNmEntStatsNumRecvCRPAdvert_Object=MibTableColumn
rlPimNmEntStatsNumRecvCRPAdvert=_RlPimNmEntStatsNumRecvCRPAdvert_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,4),_RlPimNmEntStatsNumRecvCRPAdvert_Type())
rlPimNmEntStatsNumRecvCRPAdvert.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumRecvCRPAdvert.setStatus(_A)
_RlPimNmEntStatsNumRecvRegister_Type=PimStatsCounter
_RlPimNmEntStatsNumRecvRegister_Object=MibTableColumn
rlPimNmEntStatsNumRecvRegister=_RlPimNmEntStatsNumRecvRegister_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,5),_RlPimNmEntStatsNumRecvRegister_Type())
rlPimNmEntStatsNumRecvRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumRecvRegister.setStatus(_A)
_RlPimNmEntStatsNumRecvRegisterStop_Type=PimStatsCounter
_RlPimNmEntStatsNumRecvRegisterStop_Object=MibTableColumn
rlPimNmEntStatsNumRecvRegisterStop=_RlPimNmEntStatsNumRecvRegisterStop_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,6),_RlPimNmEntStatsNumRecvRegisterStop_Type())
rlPimNmEntStatsNumRecvRegisterStop.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumRecvRegisterStop.setStatus(_A)
_RlPimNmEntStatsNumErrCRPAdvert_Type=PimStatsCounter
_RlPimNmEntStatsNumErrCRPAdvert_Object=MibTableColumn
rlPimNmEntStatsNumErrCRPAdvert=_RlPimNmEntStatsNumErrCRPAdvert_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,7),_RlPimNmEntStatsNumErrCRPAdvert_Type())
rlPimNmEntStatsNumErrCRPAdvert.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumErrCRPAdvert.setStatus(_A)
_RlPimNmEntStatsNumErrRegister_Type=PimStatsCounter
_RlPimNmEntStatsNumErrRegister_Object=MibTableColumn
rlPimNmEntStatsNumErrRegister=_RlPimNmEntStatsNumErrRegister_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,8),_RlPimNmEntStatsNumErrRegister_Type())
rlPimNmEntStatsNumErrRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumErrRegister.setStatus(_A)
_RlPimNmEntStatsNumErrRegisterStop_Type=PimStatsCounter
_RlPimNmEntStatsNumErrRegisterStop_Object=MibTableColumn
rlPimNmEntStatsNumErrRegisterStop=_RlPimNmEntStatsNumErrRegisterStop_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,9),_RlPimNmEntStatsNumErrRegisterStop_Type())
rlPimNmEntStatsNumErrRegisterStop.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumErrRegisterStop.setStatus(_A)
_RlPimNmEntStatsNumRecvIgnoredType_Type=PimStatsCounter
_RlPimNmEntStatsNumRecvIgnoredType_Object=MibTableColumn
rlPimNmEntStatsNumRecvIgnoredType=_RlPimNmEntStatsNumRecvIgnoredType_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,10),_RlPimNmEntStatsNumRecvIgnoredType_Type())
rlPimNmEntStatsNumRecvIgnoredType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumRecvIgnoredType.setStatus(_A)
_RlPimNmEntStatsNumRecvUnknownType_Type=PimStatsCounter
_RlPimNmEntStatsNumRecvUnknownType_Object=MibTableColumn
rlPimNmEntStatsNumRecvUnknownType=_RlPimNmEntStatsNumRecvUnknownType_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,11),_RlPimNmEntStatsNumRecvUnknownType_Type())
rlPimNmEntStatsNumRecvUnknownType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumRecvUnknownType.setStatus(_A)
_RlPimNmEntStatsNumRecvUnknownVer_Type=PimStatsCounter
_RlPimNmEntStatsNumRecvUnknownVer_Object=MibTableColumn
rlPimNmEntStatsNumRecvUnknownVer=_RlPimNmEntStatsNumRecvUnknownVer_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,12),_RlPimNmEntStatsNumRecvUnknownVer_Type())
rlPimNmEntStatsNumRecvUnknownVer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumRecvUnknownVer.setStatus(_A)
_RlPimNmEntStatsNumRecvBadChecksum_Type=PimStatsCounter
_RlPimNmEntStatsNumRecvBadChecksum_Object=MibTableColumn
rlPimNmEntStatsNumRecvBadChecksum=_RlPimNmEntStatsNumRecvBadChecksum_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,13),_RlPimNmEntStatsNumRecvBadChecksum_Type())
rlPimNmEntStatsNumRecvBadChecksum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumRecvBadChecksum.setStatus(_A)
_RlPimNmEntStatsNumRecvBadLength_Type=PimStatsCounter
_RlPimNmEntStatsNumRecvBadLength_Object=MibTableColumn
rlPimNmEntStatsNumRecvBadLength=_RlPimNmEntStatsNumRecvBadLength_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,14),_RlPimNmEntStatsNumRecvBadLength_Type())
rlPimNmEntStatsNumRecvBadLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumRecvBadLength.setStatus(_A)
_RlPimNmEntStatsNumCRPAdvfiltered_Type=PimStatsCounter
_RlPimNmEntStatsNumCRPAdvfiltered_Object=MibTableColumn
rlPimNmEntStatsNumCRPAdvfiltered=_RlPimNmEntStatsNumCRPAdvfiltered_Object((1,3,6,1,4,1,9,6,1,101,211,4,1,15),_RlPimNmEntStatsNumCRPAdvfiltered_Type())
rlPimNmEntStatsNumCRPAdvfiltered.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNmEntStatsNumCRPAdvfiltered.setStatus(_A)
_RlPimNbrStatsTable_Object=MibTable
rlPimNbrStatsTable=_RlPimNbrStatsTable_Object((1,3,6,1,4,1,9,6,1,101,211,5))
if mibBuilder.loadTexts:rlPimNbrStatsTable.setStatus(_A)
_RlPimNbrStatsEntry_Object=MibTableRow
rlPimNbrStatsEntry=_RlPimNbrStatsEntry_Object((1,3,6,1,4,1,9,6,1,101,211,5,1))
rlPimNbrStatsEntry.setIndexNames((0,_F,_Q),(0,_F,_P),(0,_F,_O))
if mibBuilder.loadTexts:rlPimNbrStatsEntry.setStatus(_A)
_RlPimNbrStatsNumRecvHello_Type=PimStatsCounter
_RlPimNbrStatsNumRecvHello_Object=MibTableColumn
rlPimNbrStatsNumRecvHello=_RlPimNbrStatsNumRecvHello_Object((1,3,6,1,4,1,9,6,1,101,211,5,1,1),_RlPimNbrStatsNumRecvHello_Type())
rlPimNbrStatsNumRecvHello.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNbrStatsNumRecvHello.setStatus(_A)
_RlPimNbrStatsNumRecvJoinPrune_Type=PimStatsCounter
_RlPimNbrStatsNumRecvJoinPrune_Object=MibTableColumn
rlPimNbrStatsNumRecvJoinPrune=_RlPimNbrStatsNumRecvJoinPrune_Object((1,3,6,1,4,1,9,6,1,101,211,5,1,2),_RlPimNbrStatsNumRecvJoinPrune_Type())
rlPimNbrStatsNumRecvJoinPrune.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNbrStatsNumRecvJoinPrune.setStatus(_A)
_RlPimNbrStatsNumRecvAssert_Type=PimStatsCounter
_RlPimNbrStatsNumRecvAssert_Object=MibTableColumn
rlPimNbrStatsNumRecvAssert=_RlPimNbrStatsNumRecvAssert_Object((1,3,6,1,4,1,9,6,1,101,211,5,1,3),_RlPimNbrStatsNumRecvAssert_Type())
rlPimNbrStatsNumRecvAssert.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNbrStatsNumRecvAssert.setStatus(_A)
_RlPimNbrStatsNumRecvBSM_Type=PimStatsCounter
_RlPimNbrStatsNumRecvBSM_Object=MibTableColumn
rlPimNbrStatsNumRecvBSM=_RlPimNbrStatsNumRecvBSM_Object((1,3,6,1,4,1,9,6,1,101,211,5,1,4),_RlPimNbrStatsNumRecvBSM_Type())
rlPimNbrStatsNumRecvBSM.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNbrStatsNumRecvBSM.setStatus(_A)
_RlPimNbrStatsNumErrJoinPrune_Type=PimStatsCounter
_RlPimNbrStatsNumErrJoinPrune_Object=MibTableColumn
rlPimNbrStatsNumErrJoinPrune=_RlPimNbrStatsNumErrJoinPrune_Object((1,3,6,1,4,1,9,6,1,101,211,5,1,5),_RlPimNbrStatsNumErrJoinPrune_Type())
rlPimNbrStatsNumErrJoinPrune.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNbrStatsNumErrJoinPrune.setStatus(_A)
_RlPimNbrStatsNumErrAssert_Type=PimStatsCounter
_RlPimNbrStatsNumErrAssert_Object=MibTableColumn
rlPimNbrStatsNumErrAssert=_RlPimNbrStatsNumErrAssert_Object((1,3,6,1,4,1,9,6,1,101,211,5,1,6),_RlPimNbrStatsNumErrAssert_Type())
rlPimNbrStatsNumErrAssert.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNbrStatsNumErrAssert.setStatus(_A)
_RlPimNbrStatsNumErrBSM_Type=PimStatsCounter
_RlPimNbrStatsNumErrBSM_Object=MibTableColumn
rlPimNbrStatsNumErrBSM=_RlPimNbrStatsNumErrBSM_Object((1,3,6,1,4,1,9,6,1,101,211,5,1,7),_RlPimNbrStatsNumErrBSM_Type())
rlPimNbrStatsNumErrBSM.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimNbrStatsNumErrBSM.setStatus(_A)
_RlPimTmEntTable_Object=MibTable
rlPimTmEntTable=_RlPimTmEntTable_Object((1,3,6,1,4,1,9,6,1,101,211,6))
if mibBuilder.loadTexts:rlPimTmEntTable.setStatus(_A)
_RlPimTmEntEntry_Object=MibTableRow
rlPimTmEntEntry=_RlPimTmEntEntry_Object((1,3,6,1,4,1,9,6,1,101,211,6,1))
rlPimTmEntEntry.setIndexNames((0,_I,_Z))
if mibBuilder.loadTexts:rlPimTmEntEntry.setStatus(_A)
_RlPimTmEntIndex_Type=NumericIndex
_RlPimTmEntIndex_Object=MibTableColumn
rlPimTmEntIndex=_RlPimTmEntIndex_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,1),_RlPimTmEntIndex_Type())
rlPimTmEntIndex.setMaxAccess(_X)
if mibBuilder.loadTexts:rlPimTmEntIndex.setStatus(_A)
_RlPimTmEntRowStatus_Type=RowStatus
_RlPimTmEntRowStatus_Object=MibTableColumn
rlPimTmEntRowStatus=_RlPimTmEntRowStatus_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,2),_RlPimTmEntRowStatus_Type())
rlPimTmEntRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntRowStatus.setStatus(_A)
class _RlPimTmEntAdminStatus_Type(AdminStatus):defaultValue=1
_RlPimTmEntAdminStatus_Type.__name__=_J
_RlPimTmEntAdminStatus_Object=MibTableColumn
rlPimTmEntAdminStatus=_RlPimTmEntAdminStatus_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,3),_RlPimTmEntAdminStatus_Type())
rlPimTmEntAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntAdminStatus.setStatus(_A)
_RlPimTmEntOperStatus_Type=NpgOperStatus
_RlPimTmEntOperStatus_Object=MibTableColumn
rlPimTmEntOperStatus=_RlPimTmEntOperStatus_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,4),_RlPimTmEntOperStatus_Type())
rlPimTmEntOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimTmEntOperStatus.setStatus(_A)
class _RlPimTmEntGStateLimit_Type(Unsigned32):defaultValue=0
_RlPimTmEntGStateLimit_Type.__name__=_D
_RlPimTmEntGStateLimit_Object=MibTableColumn
rlPimTmEntGStateLimit=_RlPimTmEntGStateLimit_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,5),_RlPimTmEntGStateLimit_Type())
rlPimTmEntGStateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntGStateLimit.setStatus(_A)
class _RlPimTmEntGStateWarnThold_Type(Unsigned32):defaultValue=0
_RlPimTmEntGStateWarnThold_Type.__name__=_D
_RlPimTmEntGStateWarnThold_Object=MibTableColumn
rlPimTmEntGStateWarnThold=_RlPimTmEntGStateWarnThold_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,6),_RlPimTmEntGStateWarnThold_Type())
rlPimTmEntGStateWarnThold.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntGStateWarnThold.setStatus(_A)
_RlPimTmEntGStateStored_Type=Gauge32
_RlPimTmEntGStateStored_Object=MibTableColumn
rlPimTmEntGStateStored=_RlPimTmEntGStateStored_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,7),_RlPimTmEntGStateStored_Type())
rlPimTmEntGStateStored.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimTmEntGStateStored.setStatus(_A)
class _RlPimTmEntSGStateLimit_Type(Unsigned32):defaultValue=0
_RlPimTmEntSGStateLimit_Type.__name__=_D
_RlPimTmEntSGStateLimit_Object=MibTableColumn
rlPimTmEntSGStateLimit=_RlPimTmEntSGStateLimit_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,8),_RlPimTmEntSGStateLimit_Type())
rlPimTmEntSGStateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntSGStateLimit.setStatus(_A)
class _RlPimTmEntSGStateWarnThold_Type(Unsigned32):defaultValue=0
_RlPimTmEntSGStateWarnThold_Type.__name__=_D
_RlPimTmEntSGStateWarnThold_Object=MibTableColumn
rlPimTmEntSGStateWarnThold=_RlPimTmEntSGStateWarnThold_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,9),_RlPimTmEntSGStateWarnThold_Type())
rlPimTmEntSGStateWarnThold.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntSGStateWarnThold.setStatus(_A)
_RlPimTmEntSGStateStored_Type=Gauge32
_RlPimTmEntSGStateStored_Object=MibTableColumn
rlPimTmEntSGStateStored=_RlPimTmEntSGStateStored_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,10),_RlPimTmEntSGStateStored_Type())
rlPimTmEntSGStateStored.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimTmEntSGStateStored.setStatus(_A)
class _RlPimTmEntStarGIStateLimit_Type(Unsigned32):defaultValue=0
_RlPimTmEntStarGIStateLimit_Type.__name__=_D
_RlPimTmEntStarGIStateLimit_Object=MibTableColumn
rlPimTmEntStarGIStateLimit=_RlPimTmEntStarGIStateLimit_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,11),_RlPimTmEntStarGIStateLimit_Type())
rlPimTmEntStarGIStateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntStarGIStateLimit.setStatus(_A)
class _RlPimTmEntStarGIStateWarnThold_Type(Unsigned32):defaultValue=0
_RlPimTmEntStarGIStateWarnThold_Type.__name__=_D
_RlPimTmEntStarGIStateWarnThold_Object=MibTableColumn
rlPimTmEntStarGIStateWarnThold=_RlPimTmEntStarGIStateWarnThold_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,12),_RlPimTmEntStarGIStateWarnThold_Type())
rlPimTmEntStarGIStateWarnThold.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntStarGIStateWarnThold.setStatus(_A)
_RlPimTmEntStarGIStateStored_Type=Gauge32
_RlPimTmEntStarGIStateStored_Object=MibTableColumn
rlPimTmEntStarGIStateStored=_RlPimTmEntStarGIStateStored_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,13),_RlPimTmEntStarGIStateStored_Type())
rlPimTmEntStarGIStateStored.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimTmEntStarGIStateStored.setStatus(_A)
class _RlPimTmEntSGIStateLimit_Type(Unsigned32):defaultValue=0
_RlPimTmEntSGIStateLimit_Type.__name__=_D
_RlPimTmEntSGIStateLimit_Object=MibTableColumn
rlPimTmEntSGIStateLimit=_RlPimTmEntSGIStateLimit_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,14),_RlPimTmEntSGIStateLimit_Type())
rlPimTmEntSGIStateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntSGIStateLimit.setStatus(_A)
class _RlPimTmEntSGIStateWarnThold_Type(Unsigned32):defaultValue=0
_RlPimTmEntSGIStateWarnThold_Type.__name__=_D
_RlPimTmEntSGIStateWarnThold_Object=MibTableColumn
rlPimTmEntSGIStateWarnThold=_RlPimTmEntSGIStateWarnThold_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,15),_RlPimTmEntSGIStateWarnThold_Type())
rlPimTmEntSGIStateWarnThold.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntSGIStateWarnThold.setStatus(_A)
_RlPimTmEntSGIStateStored_Type=Gauge32
_RlPimTmEntSGIStateStored_Object=MibTableColumn
rlPimTmEntSGIStateStored=_RlPimTmEntSGIStateStored_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,16),_RlPimTmEntSGIStateStored_Type())
rlPimTmEntSGIStateStored.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPimTmEntSGIStateStored.setStatus(_A)
_RlPimTmEntAsmGrpFilter_Type=DisplayString
_RlPimTmEntAsmGrpFilter_Object=MibTableColumn
rlPimTmEntAsmGrpFilter=_RlPimTmEntAsmGrpFilter_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,17),_RlPimTmEntAsmGrpFilter_Type())
rlPimTmEntAsmGrpFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntAsmGrpFilter.setStatus(_A)
_RlPimTmEntSsmSrcAndGrpFilter_Type=DisplayString
_RlPimTmEntSsmSrcAndGrpFilter_Object=MibTableColumn
rlPimTmEntSsmSrcAndGrpFilter=_RlPimTmEntSsmSrcAndGrpFilter_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,18),_RlPimTmEntSsmSrcAndGrpFilter_Type())
rlPimTmEntSsmSrcAndGrpFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntSsmSrcAndGrpFilter.setStatus(_A)
class _RlPimTmEntRegSrcAndGrpFilter_Type(DisplayString):defaultValue=OctetString('')
_RlPimTmEntRegSrcAndGrpFilter_Type.__name__=_G
_RlPimTmEntRegSrcAndGrpFilter_Object=MibTableColumn
rlPimTmEntRegSrcAndGrpFilter=_RlPimTmEntRegSrcAndGrpFilter_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,19),_RlPimTmEntRegSrcAndGrpFilter_Type())
rlPimTmEntRegSrcAndGrpFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntRegSrcAndGrpFilter.setStatus(_A)
class _RlPimTmEntRegSuppressionTime_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlPimTmEntRegSuppressionTime_Type.__name__=_D
_RlPimTmEntRegSuppressionTime_Object=MibTableColumn
rlPimTmEntRegSuppressionTime=_RlPimTmEntRegSuppressionTime_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,20),_RlPimTmEntRegSuppressionTime_Type())
rlPimTmEntRegSuppressionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntRegSuppressionTime.setStatus(_A)
if mibBuilder.loadTexts:rlPimTmEntRegSuppressionTime.setUnits(_H)
class _RlPimTmEntRegProbeTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlPimTmEntRegProbeTime_Type.__name__=_D
_RlPimTmEntRegProbeTime_Object=MibTableColumn
rlPimTmEntRegProbeTime=_RlPimTmEntRegProbeTime_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,21),_RlPimTmEntRegProbeTime_Type())
rlPimTmEntRegProbeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntRegProbeTime.setStatus(_A)
if mibBuilder.loadTexts:rlPimTmEntRegProbeTime.setUnits(_H)
class _RlPimTmEntKeepalivePeriod_Type(Unsigned32):defaultValue=210;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlPimTmEntKeepalivePeriod_Type.__name__=_D
_RlPimTmEntKeepalivePeriod_Object=MibTableColumn
rlPimTmEntKeepalivePeriod=_RlPimTmEntKeepalivePeriod_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,22),_RlPimTmEntKeepalivePeriod_Type())
rlPimTmEntKeepalivePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntKeepalivePeriod.setStatus(_A)
if mibBuilder.loadTexts:rlPimTmEntKeepalivePeriod.setUnits(_H)
class _RlPimTmEntSendIfStateChangeTraps_Type(TruthValue):defaultValue=2
_RlPimTmEntSendIfStateChangeTraps_Type.__name__=_E
_RlPimTmEntSendIfStateChangeTraps_Object=MibTableColumn
rlPimTmEntSendIfStateChangeTraps=_RlPimTmEntSendIfStateChangeTraps_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,23),_RlPimTmEntSendIfStateChangeTraps_Type())
rlPimTmEntSendIfStateChangeTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntSendIfStateChangeTraps.setStatus(_A)
class _RlPimTmEntSupportedAddrType_Type(InetAddressType):defaultValue=1
_RlPimTmEntSupportedAddrType_Type.__name__=_L
_RlPimTmEntSupportedAddrType_Object=MibTableColumn
rlPimTmEntSupportedAddrType=_RlPimTmEntSupportedAddrType_Object((1,3,6,1,4,1,9,6,1,101,211,6,1,24),_RlPimTmEntSupportedAddrType_Type())
rlPimTmEntSupportedAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPimTmEntSupportedAddrType.setStatus(_A)
class _RlPimEmbeddedRpEnabled_Type(TruthValue):defaultValue=1
_RlPimEmbeddedRpEnabled_Type.__name__=_E
_RlPimEmbeddedRpEnabled_Object=MibScalar
rlPimEmbeddedRpEnabled=_RlPimEmbeddedRpEnabled_Object((1,3,6,1,4,1,9,6,1,101,211,7),_RlPimEmbeddedRpEnabled_Type())
rlPimEmbeddedRpEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:rlPimEmbeddedRpEnabled.setStatus(_A)
pimInterfaceEntry.registerAugmentions((_I,_a))
rlPimInterfaceEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())
mibBuilder.exportSymbols(_I,**{_J:AdminStatus,'OperStatus':OperStatus,'Unsigned32NonZero':Unsigned32NonZero,'NumericIndex':NumericIndex,_W:NumericIndexOrZero,'EntityIndex':EntityIndex,'EntityIndexOrZero':EntityIndexOrZero,_Y:StdAccessListListIndexOrZero,'StdAccessListRuleIndex':StdAccessListRuleIndex,'ExtAccessListListIndex':ExtAccessListListIndex,'ExtAccessListListIndexOrZero':ExtAccessListListIndexOrZero,'PimStatsCounter':PimStatsCounter,'NpgOperStatus':NpgOperStatus,'rlPim':rlPim,'rlPimInterfaceTable':rlPimInterfaceTable,_a:rlPimInterfaceEntry,'rlPimInterfaceAdminStatus':rlPimInterfaceAdminStatus,'rlPimInterfaceOperStatus':rlPimInterfaceOperStatus,'rlPimInterfaceStubInterface':rlPimInterfaceStubInterface,'rlPimInterfaceP2PNoHellos':rlPimInterfaceP2PNoHellos,'rlPimInterfaceMgmdEntIndex':rlPimInterfaceMgmdEntIndex,'rlPimInterfaceNeighborCount':rlPimInterfaceNeighborCount,'rlPimInterfaceStarGStateLimit':rlPimInterfaceStarGStateLimit,'rlPimInterfaceStarGStateWarnThold':rlPimInterfaceStarGStateWarnThold,'rlPimInterfaceStarGStateStored':rlPimInterfaceStarGStateStored,'rlPimInterfaceSGStateLimit':rlPimInterfaceSGStateLimit,'rlPimInterfaceSGStateWarnThold':rlPimInterfaceSGStateWarnThold,'rlPimInterfaceSGStateStored':rlPimInterfaceSGStateStored,'rlPimInterfaceNeighborFilter':rlPimInterfaceNeighborFilter,'rlPimInterfaceAssertInterval':rlPimInterfaceAssertInterval,'rlPimInterfaceAssertHoldtime':rlPimInterfaceAssertHoldtime,'rlPimInterfaceAsmGrpFilter':rlPimInterfaceAsmGrpFilter,'rlPimInterfaceSsmSrcAndGrpFilter':rlPimInterfaceSsmSrcAndGrpFilter,'rlPimIfStatsTable':rlPimIfStatsTable,'rlPimIfStatsEntry':rlPimIfStatsEntry,'rlPimIfStatsNumSentHello':rlPimIfStatsNumSentHello,'rlPimIfStatsNumSentJoinPrune':rlPimIfStatsNumSentJoinPrune,'rlPimIfStatsNumSentAssert':rlPimIfStatsNumSentAssert,'rlPimIfStatsNumSentBsm':rlPimIfStatsNumSentBsm,'rlPimIfStatsNumErrHello':rlPimIfStatsNumErrHello,'rlPimIfStatsNumRecvUnknownNbr':rlPimIfStatsNumRecvUnknownNbr,'rlPimIfStatsNumUnknownHelloOpt':rlPimIfStatsNumUnknownHelloOpt,'rlPimIfStatsNumFilteredOut':rlPimIfStatsNumFilteredOut,'rlPimNmEntTable':rlPimNmEntTable,'rlPimNmEntEntry':rlPimNmEntEntry,_K:rlPimNmEntIndex,'rlPimNmEntRowStatus':rlPimNmEntRowStatus,'rlPimNmEntAdminStatus':rlPimNmEntAdminStatus,'rlPimNmEntOperStatus':rlPimNmEntOperStatus,'rlPimNmEntTmEntIndex':rlPimNmEntTmEntIndex,'rlPimNmEntI3JoinOperStatus':rlPimNmEntI3JoinOperStatus,'rlPimNmEntNmiJoinOperStatus':rlPimNmEntNmiJoinOperStatus,'rlPimNmEntSckJoinOperStatus':rlPimNmEntSckJoinOperStatus,'rlPimNmEntClearStatsCounters':rlPimNmEntClearStatsCounters,'rlPimNmEntStatsUpTime':rlPimNmEntStatsUpTime,'rlPimNmEntEnableUnicastMessages':rlPimNmEntEnableUnicastMessages,'rlPimNmEntAcceptUnicastBsms':rlPimNmEntAcceptUnicastBsms,'rlPimNmEntCrpAdvFilterIndex':rlPimNmEntCrpAdvFilterIndex,'rlPimNmEntStatsTable':rlPimNmEntStatsTable,'rlPimNmEntStatsEntry':rlPimNmEntStatsEntry,'rlPimNmEntStatsNumSentCRPAdvert':rlPimNmEntStatsNumSentCRPAdvert,'rlPimNmEntStatsNumSentRegister':rlPimNmEntStatsNumSentRegister,'rlPimNmEntStatsNumSentRegisterStop':rlPimNmEntStatsNumSentRegisterStop,'rlPimNmEntStatsNumRecvCRPAdvert':rlPimNmEntStatsNumRecvCRPAdvert,'rlPimNmEntStatsNumRecvRegister':rlPimNmEntStatsNumRecvRegister,'rlPimNmEntStatsNumRecvRegisterStop':rlPimNmEntStatsNumRecvRegisterStop,'rlPimNmEntStatsNumErrCRPAdvert':rlPimNmEntStatsNumErrCRPAdvert,'rlPimNmEntStatsNumErrRegister':rlPimNmEntStatsNumErrRegister,'rlPimNmEntStatsNumErrRegisterStop':rlPimNmEntStatsNumErrRegisterStop,'rlPimNmEntStatsNumRecvIgnoredType':rlPimNmEntStatsNumRecvIgnoredType,'rlPimNmEntStatsNumRecvUnknownType':rlPimNmEntStatsNumRecvUnknownType,'rlPimNmEntStatsNumRecvUnknownVer':rlPimNmEntStatsNumRecvUnknownVer,'rlPimNmEntStatsNumRecvBadChecksum':rlPimNmEntStatsNumRecvBadChecksum,'rlPimNmEntStatsNumRecvBadLength':rlPimNmEntStatsNumRecvBadLength,'rlPimNmEntStatsNumCRPAdvfiltered':rlPimNmEntStatsNumCRPAdvfiltered,'rlPimNbrStatsTable':rlPimNbrStatsTable,'rlPimNbrStatsEntry':rlPimNbrStatsEntry,'rlPimNbrStatsNumRecvHello':rlPimNbrStatsNumRecvHello,'rlPimNbrStatsNumRecvJoinPrune':rlPimNbrStatsNumRecvJoinPrune,'rlPimNbrStatsNumRecvAssert':rlPimNbrStatsNumRecvAssert,'rlPimNbrStatsNumRecvBSM':rlPimNbrStatsNumRecvBSM,'rlPimNbrStatsNumErrJoinPrune':rlPimNbrStatsNumErrJoinPrune,'rlPimNbrStatsNumErrAssert':rlPimNbrStatsNumErrAssert,'rlPimNbrStatsNumErrBSM':rlPimNbrStatsNumErrBSM,'rlPimTmEntTable':rlPimTmEntTable,'rlPimTmEntEntry':rlPimTmEntEntry,_Z:rlPimTmEntIndex,'rlPimTmEntRowStatus':rlPimTmEntRowStatus,'rlPimTmEntAdminStatus':rlPimTmEntAdminStatus,'rlPimTmEntOperStatus':rlPimTmEntOperStatus,'rlPimTmEntGStateLimit':rlPimTmEntGStateLimit,'rlPimTmEntGStateWarnThold':rlPimTmEntGStateWarnThold,'rlPimTmEntGStateStored':rlPimTmEntGStateStored,'rlPimTmEntSGStateLimit':rlPimTmEntSGStateLimit,'rlPimTmEntSGStateWarnThold':rlPimTmEntSGStateWarnThold,'rlPimTmEntSGStateStored':rlPimTmEntSGStateStored,'rlPimTmEntStarGIStateLimit':rlPimTmEntStarGIStateLimit,'rlPimTmEntStarGIStateWarnThold':rlPimTmEntStarGIStateWarnThold,'rlPimTmEntStarGIStateStored':rlPimTmEntStarGIStateStored,'rlPimTmEntSGIStateLimit':rlPimTmEntSGIStateLimit,'rlPimTmEntSGIStateWarnThold':rlPimTmEntSGIStateWarnThold,'rlPimTmEntSGIStateStored':rlPimTmEntSGIStateStored,'rlPimTmEntAsmGrpFilter':rlPimTmEntAsmGrpFilter,'rlPimTmEntSsmSrcAndGrpFilter':rlPimTmEntSsmSrcAndGrpFilter,'rlPimTmEntRegSrcAndGrpFilter':rlPimTmEntRegSrcAndGrpFilter,'rlPimTmEntRegSuppressionTime':rlPimTmEntRegSuppressionTime,'rlPimTmEntRegProbeTime':rlPimTmEntRegProbeTime,'rlPimTmEntKeepalivePeriod':rlPimTmEntKeepalivePeriod,'rlPimTmEntSendIfStateChangeTraps':rlPimTmEntSendIfStateChangeTraps,'rlPimTmEntSupportedAddrType':rlPimTmEntSupportedAddrType,'rlPimEmbeddedRpEnabled':rlPimEmbeddedRpEnabled})