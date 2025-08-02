_P='jnxAtmVpEntry'
_O='jnxAtmVCEntry'
_N='jnxAtmIfEntry'
_M='active'
_L='multicast'
_K='passiveOam'
_J='shapingEnabled'
_I='oamEnabled'
_H='ifIndex'
_G='IF-MIB'
_F='atmCccCellRelay'
_E='JUNIPER-ATM-MIB'
_D='other'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmInterfaceConfEntry,atmVclEntry,atmVplEntry=mibBuilder.importSymbols('ATM-MIB','atmInterfaceConfEntry','atmVclEntry','atmVplEntry')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxAtm=ModuleIdentity((1,3,6,1,4,1,2636,3,10))
if mibBuilder.loadTexts:jnxAtm.setRevisions(('2004-01-06 00:00','2003-12-04 00:00','2003-09-17 00:00','2002-07-04 00:00','2002-01-23 00:00','2001-07-08 00:00'))
class JnxAtmFlags(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('inverseArpEnabled',0),('ilmiEnabled',1),(_I,2),(_J,3),(_K,4),(_L,5),('closed',6),('down',7),(_M,8),('cosEnabled',9)))
_JnxAtmIfTable_Object=MibTable
jnxAtmIfTable=_JnxAtmIfTable_Object((1,3,6,1,4,1,2636,3,10,1))
if mibBuilder.loadTexts:jnxAtmIfTable.setStatus(_A)
_JnxAtmIfEntry_Object=MibTableRow
jnxAtmIfEntry=_JnxAtmIfEntry_Object((1,3,6,1,4,1,2636,3,10,1,1))
if mibBuilder.loadTexts:jnxAtmIfEntry.setStatus(_A)
class _JnxAtmIfPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_D,1),('oc3',2),('oc12',3),('t3',4),('e3',5),('oc48',6)))
_JnxAtmIfPortType_Type.__name__=_C
_JnxAtmIfPortType_Object=MibTableColumn
jnxAtmIfPortType=_JnxAtmIfPortType_Object((1,3,6,1,4,1,2636,3,10,1,1,1),_JnxAtmIfPortType_Type())
jnxAtmIfPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfPortType.setStatus(_A)
class _JnxAtmIfEncaps_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('atmPvc',2),(_F,3)))
_JnxAtmIfEncaps_Type.__name__=_C
_JnxAtmIfEncaps_Object=MibTableColumn
jnxAtmIfEncaps=_JnxAtmIfEncaps_Object((1,3,6,1,4,1,2636,3,10,1,1,2),_JnxAtmIfEncaps_Type())
jnxAtmIfEncaps.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfEncaps.setStatus(_A)
class _JnxAtmIfLpBackInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noLoopBack',1),('localLoopBack',2),('remoteLoopBack',3)))
_JnxAtmIfLpBackInfo_Type.__name__=_C
_JnxAtmIfLpBackInfo_Object=MibTableColumn
jnxAtmIfLpBackInfo=_JnxAtmIfLpBackInfo_Object((1,3,6,1,4,1,2636,3,10,1,1,3),_JnxAtmIfLpBackInfo_Type())
jnxAtmIfLpBackInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfLpBackInfo.setStatus(_A)
class _JnxAtmIfScrambleEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_JnxAtmIfScrambleEnable_Type.__name__=_C
_JnxAtmIfScrambleEnable_Object=MibTableColumn
jnxAtmIfScrambleEnable=_JnxAtmIfScrambleEnable_Object((1,3,6,1,4,1,2636,3,10,1,1,4),_JnxAtmIfScrambleEnable_Type())
jnxAtmIfScrambleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfScrambleEnable.setStatus(_A)
_JnxAtmIfTxCellCount_Type=Counter64
_JnxAtmIfTxCellCount_Object=MibTableColumn
jnxAtmIfTxCellCount=_JnxAtmIfTxCellCount_Object((1,3,6,1,4,1,2636,3,10,1,1,5),_JnxAtmIfTxCellCount_Type())
jnxAtmIfTxCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfTxCellCount.setStatus(_A)
_JnxAtmIfRxCellCount_Type=Counter64
_JnxAtmIfRxCellCount_Object=MibTableColumn
jnxAtmIfRxCellCount=_JnxAtmIfRxCellCount_Object((1,3,6,1,4,1,2636,3,10,1,1,6),_JnxAtmIfRxCellCount_Type())
jnxAtmIfRxCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfRxCellCount.setStatus(_A)
_JnxAtmIfTxIdleCellCount_Type=Counter64
_JnxAtmIfTxIdleCellCount_Object=MibTableColumn
jnxAtmIfTxIdleCellCount=_JnxAtmIfTxIdleCellCount_Object((1,3,6,1,4,1,2636,3,10,1,1,7),_JnxAtmIfTxIdleCellCount_Type())
jnxAtmIfTxIdleCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfTxIdleCellCount.setStatus(_A)
_JnxAtmIfUncorrHCSErrs_Type=Counter64
_JnxAtmIfUncorrHCSErrs_Object=MibTableColumn
jnxAtmIfUncorrHCSErrs=_JnxAtmIfUncorrHCSErrs_Object((1,3,6,1,4,1,2636,3,10,1,1,8),_JnxAtmIfUncorrHCSErrs_Type())
jnxAtmIfUncorrHCSErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfUncorrHCSErrs.setStatus(_A)
_JnxAtmIfCorrHCSErrs_Type=Counter64
_JnxAtmIfCorrHCSErrs_Object=MibTableColumn
jnxAtmIfCorrHCSErrs=_JnxAtmIfCorrHCSErrs_Object((1,3,6,1,4,1,2636,3,10,1,1,9),_JnxAtmIfCorrHCSErrs_Type())
jnxAtmIfCorrHCSErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfCorrHCSErrs.setStatus(_A)
_JnxAtmIfTxCellFIFOOverRuns_Type=Counter64
_JnxAtmIfTxCellFIFOOverRuns_Object=MibTableColumn
jnxAtmIfTxCellFIFOOverRuns=_JnxAtmIfTxCellFIFOOverRuns_Object((1,3,6,1,4,1,2636,3,10,1,1,10),_JnxAtmIfTxCellFIFOOverRuns_Type())
jnxAtmIfTxCellFIFOOverRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfTxCellFIFOOverRuns.setStatus(_A)
_JnxAtmIfRxCellFIFOOverRuns_Type=Counter64
_JnxAtmIfRxCellFIFOOverRuns_Object=MibTableColumn
jnxAtmIfRxCellFIFOOverRuns=_JnxAtmIfRxCellFIFOOverRuns_Object((1,3,6,1,4,1,2636,3,10,1,1,11),_JnxAtmIfRxCellFIFOOverRuns_Type())
jnxAtmIfRxCellFIFOOverRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfRxCellFIFOOverRuns.setStatus(_A)
_JnxAtmIfRxCellFIFOUnderRuns_Type=Counter64
_JnxAtmIfRxCellFIFOUnderRuns_Object=MibTableColumn
jnxAtmIfRxCellFIFOUnderRuns=_JnxAtmIfRxCellFIFOUnderRuns_Object((1,3,6,1,4,1,2636,3,10,1,1,12),_JnxAtmIfRxCellFIFOUnderRuns_Type())
jnxAtmIfRxCellFIFOUnderRuns.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfRxCellFIFOUnderRuns.setStatus(_A)
_JnxAtmIfInInvalidVCCells_Type=Counter64
_JnxAtmIfInInvalidVCCells_Object=MibTableColumn
jnxAtmIfInInvalidVCCells=_JnxAtmIfInInvalidVCCells_Object((1,3,6,1,4,1,2636,3,10,1,1,13),_JnxAtmIfInInvalidVCCells_Type())
jnxAtmIfInInvalidVCCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfInInvalidVCCells.setStatus(_A)
_JnxAtmIfInNoBufferOAMCells_Type=Counter64
_JnxAtmIfInNoBufferOAMCells_Object=MibTableColumn
jnxAtmIfInNoBufferOAMCells=_JnxAtmIfInNoBufferOAMCells_Object((1,3,6,1,4,1,2636,3,10,1,1,14),_JnxAtmIfInNoBufferOAMCells_Type())
jnxAtmIfInNoBufferOAMCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfInNoBufferOAMCells.setStatus(_A)
_JnxAtmIfInNoBufDropPkts_Type=Counter64
_JnxAtmIfInNoBufDropPkts_Object=MibTableColumn
jnxAtmIfInNoBufDropPkts=_JnxAtmIfInNoBufDropPkts_Object((1,3,6,1,4,1,2636,3,10,1,1,15),_JnxAtmIfInNoBufDropPkts_Type())
jnxAtmIfInNoBufDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfInNoBufDropPkts.setStatus(_A)
_JnxAtmIfOutVCQueueDrops_Type=Counter64
_JnxAtmIfOutVCQueueDrops_Object=MibTableColumn
jnxAtmIfOutVCQueueDrops=_JnxAtmIfOutVCQueueDrops_Object((1,3,6,1,4,1,2636,3,10,1,1,16),_JnxAtmIfOutVCQueueDrops_Type())
jnxAtmIfOutVCQueueDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfOutVCQueueDrops.setStatus(_A)
_JnxAtmIfInBadCrcs_Type=Counter64
_JnxAtmIfInBadCrcs_Object=MibTableColumn
jnxAtmIfInBadCrcs=_JnxAtmIfInBadCrcs_Object((1,3,6,1,4,1,2636,3,10,1,1,17),_JnxAtmIfInBadCrcs_Type())
jnxAtmIfInBadCrcs.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfInBadCrcs.setStatus(_A)
_JnxAtmIfInLenErrPkts_Type=Counter64
_JnxAtmIfInLenErrPkts_Object=MibTableColumn
jnxAtmIfInLenErrPkts=_JnxAtmIfInLenErrPkts_Object((1,3,6,1,4,1,2636,3,10,1,1,18),_JnxAtmIfInLenErrPkts_Type())
jnxAtmIfInLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfInLenErrPkts.setStatus(_A)
_JnxAtmIfInTimeoutPkts_Type=Counter64
_JnxAtmIfInTimeoutPkts_Object=MibTableColumn
jnxAtmIfInTimeoutPkts=_JnxAtmIfInTimeoutPkts_Object((1,3,6,1,4,1,2636,3,10,1,1,19),_JnxAtmIfInTimeoutPkts_Type())
jnxAtmIfInTimeoutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfInTimeoutPkts.setStatus(_A)
class _JnxAtmIfL2CircuitMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('notApplicable',1),('none',2),('aal5',3),('cell',4),('uniTrunk',5),('nniTrunk',6)))
_JnxAtmIfL2CircuitMode_Type.__name__=_C
_JnxAtmIfL2CircuitMode_Object=MibTableColumn
jnxAtmIfL2CircuitMode=_JnxAtmIfL2CircuitMode_Object((1,3,6,1,4,1,2636,3,10,1,1,20),_JnxAtmIfL2CircuitMode_Type())
jnxAtmIfL2CircuitMode.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmIfL2CircuitMode.setStatus(_A)
_JnxAtmVCTable_Object=MibTable
jnxAtmVCTable=_JnxAtmVCTable_Object((1,3,6,1,4,1,2636,3,10,2))
if mibBuilder.loadTexts:jnxAtmVCTable.setStatus(_A)
_JnxAtmVCEntry_Object=MibTableRow
jnxAtmVCEntry=_JnxAtmVCEntry_Object((1,3,6,1,4,1,2636,3,10,2,1))
if mibBuilder.loadTexts:jnxAtmVCEntry.setStatus(_A)
class _JnxAtmVCConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_D,1),('p2p',2),('p2mp',3),(_L,4)))
_JnxAtmVCConnType_Type.__name__=_C
_JnxAtmVCConnType_Object=MibTableColumn
jnxAtmVCConnType=_JnxAtmVCConnType_Object((1,3,6,1,4,1,2636,3,10,2,1,1),_JnxAtmVCConnType_Type())
jnxAtmVCConnType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCConnType.setStatus(_A)
class _JnxAtmVCEncapsulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_D,1),(_F,2),('atmCccVcMux',3),('atmCiscoNlpid',4),('atmNlpid',5),('atmSnap',6),('atmVcMux',7),('atmTccVcMux',8),('atmTccSnap',9)))
_JnxAtmVCEncapsulation_Type.__name__=_C
_JnxAtmVCEncapsulation_Object=MibTableColumn
jnxAtmVCEncapsulation=_JnxAtmVCEncapsulation_Object((1,3,6,1,4,1,2636,3,10,2,1,2),_JnxAtmVCEncapsulation_Type())
jnxAtmVCEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCEncapsulation.setStatus(_A)
_JnxAtmVCMpDestIPv4Addr_Type=InetAddressIPv4
_JnxAtmVCMpDestIPv4Addr_Object=MibTableColumn
jnxAtmVCMpDestIPv4Addr=_JnxAtmVCMpDestIPv4Addr_Object((1,3,6,1,4,1,2636,3,10,2,1,3),_JnxAtmVCMpDestIPv4Addr_Type())
jnxAtmVCMpDestIPv4Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCMpDestIPv4Addr.setStatus(_A)
_JnxAtmVCMpDestIPv6Addr_Type=InetAddressIPv6
_JnxAtmVCMpDestIPv6Addr_Object=MibTableColumn
jnxAtmVCMpDestIPv6Addr=_JnxAtmVCMpDestIPv6Addr_Object((1,3,6,1,4,1,2636,3,10,2,1,4),_JnxAtmVCMpDestIPv6Addr_Type())
jnxAtmVCMpDestIPv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCMpDestIPv6Addr.setStatus(_A)
_JnxAtmVCFlags_Type=JnxAtmFlags
_JnxAtmVCFlags_Object=MibTableColumn
jnxAtmVCFlags=_JnxAtmVCFlags_Object((1,3,6,1,4,1,2636,3,10,2,1,5),_JnxAtmVCFlags_Type())
jnxAtmVCFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCFlags.setStatus(_A)
_JnxAtmVCTotalDownTime_Type=Integer32
_JnxAtmVCTotalDownTime_Object=MibTableColumn
jnxAtmVCTotalDownTime=_JnxAtmVCTotalDownTime_Object((1,3,6,1,4,1,2636,3,10,2,1,6),_JnxAtmVCTotalDownTime_Type())
jnxAtmVCTotalDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCTotalDownTime.setStatus(_A)
_JnxAtmVCInBytes_Type=Counter64
_JnxAtmVCInBytes_Object=MibTableColumn
jnxAtmVCInBytes=_JnxAtmVCInBytes_Object((1,3,6,1,4,1,2636,3,10,2,1,7),_JnxAtmVCInBytes_Type())
jnxAtmVCInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCInBytes.setStatus(_A)
_JnxAtmVCOutBytes_Type=Counter64
_JnxAtmVCOutBytes_Object=MibTableColumn
jnxAtmVCOutBytes=_JnxAtmVCOutBytes_Object((1,3,6,1,4,1,2636,3,10,2,1,8),_JnxAtmVCOutBytes_Type())
jnxAtmVCOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCOutBytes.setStatus(_A)
_JnxAtmVCInPkts_Type=Counter64
_JnxAtmVCInPkts_Object=MibTableColumn
jnxAtmVCInPkts=_JnxAtmVCInPkts_Object((1,3,6,1,4,1,2636,3,10,2,1,9),_JnxAtmVCInPkts_Type())
jnxAtmVCInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCInPkts.setStatus(_A)
_JnxAtmVCOutPkts_Type=Counter64
_JnxAtmVCOutPkts_Object=MibTableColumn
jnxAtmVCOutPkts=_JnxAtmVCOutPkts_Object((1,3,6,1,4,1,2636,3,10,2,1,10),_JnxAtmVCOutPkts_Type())
jnxAtmVCOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCOutPkts.setStatus(_A)
_JnxAtmVCTailQueuePktDrops_Type=Counter64
_JnxAtmVCTailQueuePktDrops_Object=MibTableColumn
jnxAtmVCTailQueuePktDrops=_JnxAtmVCTailQueuePktDrops_Object((1,3,6,1,4,1,2636,3,10,2,1,11),_JnxAtmVCTailQueuePktDrops_Type())
jnxAtmVCTailQueuePktDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCTailQueuePktDrops.setStatus(_A)
_JnxAtmVCOAMPeriod_Type=Integer32
_JnxAtmVCOAMPeriod_Object=MibTableColumn
jnxAtmVCOAMPeriod=_JnxAtmVCOAMPeriod_Object((1,3,6,1,4,1,2636,3,10,2,1,12),_JnxAtmVCOAMPeriod_Type())
jnxAtmVCOAMPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCOAMPeriod.setStatus(_A)
_JnxAtmVCOAMUpCellCount_Type=Integer32
_JnxAtmVCOAMUpCellCount_Object=MibTableColumn
jnxAtmVCOAMUpCellCount=_JnxAtmVCOAMUpCellCount_Object((1,3,6,1,4,1,2636,3,10,2,1,13),_JnxAtmVCOAMUpCellCount_Type())
jnxAtmVCOAMUpCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCOAMUpCellCount.setStatus(_A)
_JnxAtmVCOAMDownCellCount_Type=Integer32
_JnxAtmVCOAMDownCellCount_Object=MibTableColumn
jnxAtmVCOAMDownCellCount=_JnxAtmVCOAMDownCellCount_Object((1,3,6,1,4,1,2636,3,10,2,1,14),_JnxAtmVCOAMDownCellCount_Type())
jnxAtmVCOAMDownCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCOAMDownCellCount.setStatus(_A)
_JnxAtmVCInOAMF5LoopCells_Type=Counter32
_JnxAtmVCInOAMF5LoopCells_Object=MibTableColumn
jnxAtmVCInOAMF5LoopCells=_JnxAtmVCInOAMF5LoopCells_Object((1,3,6,1,4,1,2636,3,10,2,1,15),_JnxAtmVCInOAMF5LoopCells_Type())
jnxAtmVCInOAMF5LoopCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCInOAMF5LoopCells.setStatus(_A)
_JnxAtmVCOutOAMF5LoopCells_Type=Counter32
_JnxAtmVCOutOAMF5LoopCells_Object=MibTableColumn
jnxAtmVCOutOAMF5LoopCells=_JnxAtmVCOutOAMF5LoopCells_Object((1,3,6,1,4,1,2636,3,10,2,1,16),_JnxAtmVCOutOAMF5LoopCells_Type())
jnxAtmVCOutOAMF5LoopCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCOutOAMF5LoopCells.setStatus(_A)
_JnxAtmVCInOAMF5RDICells_Type=Counter32
_JnxAtmVCInOAMF5RDICells_Object=MibTableColumn
jnxAtmVCInOAMF5RDICells=_JnxAtmVCInOAMF5RDICells_Object((1,3,6,1,4,1,2636,3,10,2,1,17),_JnxAtmVCInOAMF5RDICells_Type())
jnxAtmVCInOAMF5RDICells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCInOAMF5RDICells.setStatus(_A)
_JnxAtmVCOutOAMF5RDICells_Type=Counter32
_JnxAtmVCOutOAMF5RDICells_Object=MibTableColumn
jnxAtmVCOutOAMF5RDICells=_JnxAtmVCOutOAMF5RDICells_Object((1,3,6,1,4,1,2636,3,10,2,1,18),_JnxAtmVCOutOAMF5RDICells_Type())
jnxAtmVCOutOAMF5RDICells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCOutOAMF5RDICells.setStatus(_A)
_JnxAtmVCInOAMF5AISCells_Type=Counter32
_JnxAtmVCInOAMF5AISCells_Object=MibTableColumn
jnxAtmVCInOAMF5AISCells=_JnxAtmVCInOAMF5AISCells_Object((1,3,6,1,4,1,2636,3,10,2,1,19),_JnxAtmVCInOAMF5AISCells_Type())
jnxAtmVCInOAMF5AISCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCInOAMF5AISCells.setStatus(_A)
_JnxAtmVCOutOAMF5AISCells_Type=Counter32
_JnxAtmVCOutOAMF5AISCells_Object=MibTableColumn
jnxAtmVCOutOAMF5AISCells=_JnxAtmVCOutOAMF5AISCells_Object((1,3,6,1,4,1,2636,3,10,2,1,20),_JnxAtmVCOutOAMF5AISCells_Type())
jnxAtmVCOutOAMF5AISCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVCOutOAMF5AISCells.setStatus(_A)
_JnxAtmVpTable_Object=MibTable
jnxAtmVpTable=_JnxAtmVpTable_Object((1,3,6,1,4,1,2636,3,10,3))
if mibBuilder.loadTexts:jnxAtmVpTable.setStatus(_A)
_JnxAtmVpEntry_Object=MibTableRow
jnxAtmVpEntry=_JnxAtmVpEntry_Object((1,3,6,1,4,1,2636,3,10,3,1))
if mibBuilder.loadTexts:jnxAtmVpEntry.setStatus(_A)
class _JnxAtmVpFlags_Type(Bits):namedValues=NamedValues(*((_M,0),('down',1),(_I,2),(_J,3),(_K,4)))
_JnxAtmVpFlags_Type.__name__='Bits'
_JnxAtmVpFlags_Object=MibTableColumn
jnxAtmVpFlags=_JnxAtmVpFlags_Object((1,3,6,1,4,1,2636,3,10,3,1,1),_JnxAtmVpFlags_Type())
jnxAtmVpFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpFlags.setStatus(_A)
_JnxAtmVpTotalDownTime_Type=Integer32
_JnxAtmVpTotalDownTime_Object=MibTableColumn
jnxAtmVpTotalDownTime=_JnxAtmVpTotalDownTime_Object((1,3,6,1,4,1,2636,3,10,3,1,2),_JnxAtmVpTotalDownTime_Type())
jnxAtmVpTotalDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpTotalDownTime.setStatus(_A)
_JnxAtmVpOamPeriod_Type=Integer32
_JnxAtmVpOamPeriod_Object=MibTableColumn
jnxAtmVpOamPeriod=_JnxAtmVpOamPeriod_Object((1,3,6,1,4,1,2636,3,10,3,1,3),_JnxAtmVpOamPeriod_Type())
jnxAtmVpOamPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpOamPeriod.setStatus(_A)
_JnxAtmVpOamUpCellCount_Type=Integer32
_JnxAtmVpOamUpCellCount_Object=MibTableColumn
jnxAtmVpOamUpCellCount=_JnxAtmVpOamUpCellCount_Object((1,3,6,1,4,1,2636,3,10,3,1,4),_JnxAtmVpOamUpCellCount_Type())
jnxAtmVpOamUpCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpOamUpCellCount.setStatus(_A)
_JnxAtmVpOamDownCellCount_Type=Integer32
_JnxAtmVpOamDownCellCount_Object=MibTableColumn
jnxAtmVpOamDownCellCount=_JnxAtmVpOamDownCellCount_Object((1,3,6,1,4,1,2636,3,10,3,1,5),_JnxAtmVpOamDownCellCount_Type())
jnxAtmVpOamDownCellCount.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpOamDownCellCount.setStatus(_A)
_JnxAtmVpInBytes_Type=Counter64
_JnxAtmVpInBytes_Object=MibTableColumn
jnxAtmVpInBytes=_JnxAtmVpInBytes_Object((1,3,6,1,4,1,2636,3,10,3,1,6),_JnxAtmVpInBytes_Type())
jnxAtmVpInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpInBytes.setStatus(_A)
_JnxAtmVpOutBytes_Type=Counter64
_JnxAtmVpOutBytes_Object=MibTableColumn
jnxAtmVpOutBytes=_JnxAtmVpOutBytes_Object((1,3,6,1,4,1,2636,3,10,3,1,7),_JnxAtmVpOutBytes_Type())
jnxAtmVpOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpOutBytes.setStatus(_A)
_JnxAtmVpInPkts_Type=Counter64
_JnxAtmVpInPkts_Object=MibTableColumn
jnxAtmVpInPkts=_JnxAtmVpInPkts_Object((1,3,6,1,4,1,2636,3,10,3,1,8),_JnxAtmVpInPkts_Type())
jnxAtmVpInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpInPkts.setStatus(_A)
_JnxAtmVpOutPkts_Type=Counter64
_JnxAtmVpOutPkts_Object=MibTableColumn
jnxAtmVpOutPkts=_JnxAtmVpOutPkts_Object((1,3,6,1,4,1,2636,3,10,3,1,9),_JnxAtmVpOutPkts_Type())
jnxAtmVpOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpOutPkts.setStatus(_A)
_JnxAtmVpInOamF4Cells_Type=Counter32
_JnxAtmVpInOamF4Cells_Object=MibTableColumn
jnxAtmVpInOamF4Cells=_JnxAtmVpInOamF4Cells_Object((1,3,6,1,4,1,2636,3,10,3,1,10),_JnxAtmVpInOamF4Cells_Type())
jnxAtmVpInOamF4Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpInOamF4Cells.setStatus(_A)
_JnxAtmVpOutOamF4Cells_Type=Counter32
_JnxAtmVpOutOamF4Cells_Object=MibTableColumn
jnxAtmVpOutOamF4Cells=_JnxAtmVpOutOamF4Cells_Object((1,3,6,1,4,1,2636,3,10,3,1,11),_JnxAtmVpOutOamF4Cells_Type())
jnxAtmVpOutOamF4Cells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpOutOamF4Cells.setStatus(_A)
_JnxAtmVpInOamF4LoopCells_Type=Counter32
_JnxAtmVpInOamF4LoopCells_Object=MibTableColumn
jnxAtmVpInOamF4LoopCells=_JnxAtmVpInOamF4LoopCells_Object((1,3,6,1,4,1,2636,3,10,3,1,12),_JnxAtmVpInOamF4LoopCells_Type())
jnxAtmVpInOamF4LoopCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpInOamF4LoopCells.setStatus(_A)
_JnxAtmVpOutOamF4LoopCells_Type=Counter32
_JnxAtmVpOutOamF4LoopCells_Object=MibTableColumn
jnxAtmVpOutOamF4LoopCells=_JnxAtmVpOutOamF4LoopCells_Object((1,3,6,1,4,1,2636,3,10,3,1,13),_JnxAtmVpOutOamF4LoopCells_Type())
jnxAtmVpOutOamF4LoopCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpOutOamF4LoopCells.setStatus(_A)
_JnxAtmVpInOamF4RdiCells_Type=Counter32
_JnxAtmVpInOamF4RdiCells_Object=MibTableColumn
jnxAtmVpInOamF4RdiCells=_JnxAtmVpInOamF4RdiCells_Object((1,3,6,1,4,1,2636,3,10,3,1,14),_JnxAtmVpInOamF4RdiCells_Type())
jnxAtmVpInOamF4RdiCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpInOamF4RdiCells.setStatus(_A)
_JnxAtmVpOutOamF4RdiCells_Type=Counter32
_JnxAtmVpOutOamF4RdiCells_Object=MibTableColumn
jnxAtmVpOutOamF4RdiCells=_JnxAtmVpOutOamF4RdiCells_Object((1,3,6,1,4,1,2636,3,10,3,1,15),_JnxAtmVpOutOamF4RdiCells_Type())
jnxAtmVpOutOamF4RdiCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpOutOamF4RdiCells.setStatus(_A)
_JnxAtmVpInOamF4AisCells_Type=Counter32
_JnxAtmVpInOamF4AisCells_Object=MibTableColumn
jnxAtmVpInOamF4AisCells=_JnxAtmVpInOamF4AisCells_Object((1,3,6,1,4,1,2636,3,10,3,1,16),_JnxAtmVpInOamF4AisCells_Type())
jnxAtmVpInOamF4AisCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmVpInOamF4AisCells.setStatus(_A)
_JnxAtmTrunkTable_Object=MibTable
jnxAtmTrunkTable=_JnxAtmTrunkTable_Object((1,3,6,1,4,1,2636,3,10,4))
if mibBuilder.loadTexts:jnxAtmTrunkTable.setStatus(_A)
_JnxAtmTrunkEntry_Object=MibTableRow
jnxAtmTrunkEntry=_JnxAtmTrunkEntry_Object((1,3,6,1,4,1,2636,3,10,4,1))
jnxAtmTrunkEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:jnxAtmTrunkEntry.setStatus(_A)
_JnxAtmTrunkId_Type=Integer32
_JnxAtmTrunkId_Object=MibTableColumn
jnxAtmTrunkId=_JnxAtmTrunkId_Object((1,3,6,1,4,1,2636,3,10,4,1,1),_JnxAtmTrunkId_Type())
jnxAtmTrunkId.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkId.setStatus(_A)
class _JnxAtmTrunkConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),('p2p',2)))
_JnxAtmTrunkConnType_Type.__name__=_C
_JnxAtmTrunkConnType_Object=MibTableColumn
jnxAtmTrunkConnType=_JnxAtmTrunkConnType_Object((1,3,6,1,4,1,2636,3,10,4,1,2),_JnxAtmTrunkConnType_Type())
jnxAtmTrunkConnType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkConnType.setStatus(_A)
class _JnxAtmTrunkEncapsulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_F,2)))
_JnxAtmTrunkEncapsulation_Type.__name__=_C
_JnxAtmTrunkEncapsulation_Object=MibTableColumn
jnxAtmTrunkEncapsulation=_JnxAtmTrunkEncapsulation_Object((1,3,6,1,4,1,2636,3,10,4,1,3),_JnxAtmTrunkEncapsulation_Type())
jnxAtmTrunkEncapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkEncapsulation.setStatus(_A)
_JnxAtmTrunkFlags_Type=JnxAtmFlags
_JnxAtmTrunkFlags_Object=MibTableColumn
jnxAtmTrunkFlags=_JnxAtmTrunkFlags_Object((1,3,6,1,4,1,2636,3,10,4,1,4),_JnxAtmTrunkFlags_Type())
jnxAtmTrunkFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkFlags.setStatus(_A)
_JnxAtmTrunkTotalDownTime_Type=Integer32
_JnxAtmTrunkTotalDownTime_Object=MibTableColumn
jnxAtmTrunkTotalDownTime=_JnxAtmTrunkTotalDownTime_Object((1,3,6,1,4,1,2636,3,10,4,1,5),_JnxAtmTrunkTotalDownTime_Type())
jnxAtmTrunkTotalDownTime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkTotalDownTime.setStatus(_A)
_JnxAtmTrunkInBytes_Type=Counter64
_JnxAtmTrunkInBytes_Object=MibTableColumn
jnxAtmTrunkInBytes=_JnxAtmTrunkInBytes_Object((1,3,6,1,4,1,2636,3,10,4,1,6),_JnxAtmTrunkInBytes_Type())
jnxAtmTrunkInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkInBytes.setStatus(_A)
_JnxAtmTrunkOutBytes_Type=Counter64
_JnxAtmTrunkOutBytes_Object=MibTableColumn
jnxAtmTrunkOutBytes=_JnxAtmTrunkOutBytes_Object((1,3,6,1,4,1,2636,3,10,4,1,7),_JnxAtmTrunkOutBytes_Type())
jnxAtmTrunkOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkOutBytes.setStatus(_A)
_JnxAtmTrunkInPkts_Type=Counter64
_JnxAtmTrunkInPkts_Object=MibTableColumn
jnxAtmTrunkInPkts=_JnxAtmTrunkInPkts_Object((1,3,6,1,4,1,2636,3,10,4,1,8),_JnxAtmTrunkInPkts_Type())
jnxAtmTrunkInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkInPkts.setStatus(_A)
_JnxAtmTrunkOutPkts_Type=Counter64
_JnxAtmTrunkOutPkts_Object=MibTableColumn
jnxAtmTrunkOutPkts=_JnxAtmTrunkOutPkts_Object((1,3,6,1,4,1,2636,3,10,4,1,9),_JnxAtmTrunkOutPkts_Type())
jnxAtmTrunkOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkOutPkts.setStatus(_A)
_JnxAtmTrunkTailQueuePktDrops_Type=Counter64
_JnxAtmTrunkTailQueuePktDrops_Object=MibTableColumn
jnxAtmTrunkTailQueuePktDrops=_JnxAtmTrunkTailQueuePktDrops_Object((1,3,6,1,4,1,2636,3,10,4,1,10),_JnxAtmTrunkTailQueuePktDrops_Type())
jnxAtmTrunkTailQueuePktDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkTailQueuePktDrops.setStatus(_A)
_JnxAtmTrunkInOAMF4AISCells_Type=Counter32
_JnxAtmTrunkInOAMF4AISCells_Object=MibTableColumn
jnxAtmTrunkInOAMF4AISCells=_JnxAtmTrunkInOAMF4AISCells_Object((1,3,6,1,4,1,2636,3,10,4,1,15),_JnxAtmTrunkInOAMF4AISCells_Type())
jnxAtmTrunkInOAMF4AISCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkInOAMF4AISCells.setStatus(_A)
_JnxAtmTrunkOutOAMF4AISCells_Type=Counter32
_JnxAtmTrunkOutOAMF4AISCells_Object=MibTableColumn
jnxAtmTrunkOutOAMF4AISCells=_JnxAtmTrunkOutOAMF4AISCells_Object((1,3,6,1,4,1,2636,3,10,4,1,16),_JnxAtmTrunkOutOAMF4AISCells_Type())
jnxAtmTrunkOutOAMF4AISCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxAtmTrunkOutOAMF4AISCells.setStatus(_A)
atmInterfaceConfEntry.registerAugmentions((_E,_N))
jnxAtmIfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
atmVclEntry.registerAugmentions((_E,_O))
jnxAtmVCEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVplEntry.registerAugmentions((_E,_P))
jnxAtmVpEntry.setIndexNames(*atmVplEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'JnxAtmFlags':JnxAtmFlags,'jnxAtm':jnxAtm,'jnxAtmIfTable':jnxAtmIfTable,_N:jnxAtmIfEntry,'jnxAtmIfPortType':jnxAtmIfPortType,'jnxAtmIfEncaps':jnxAtmIfEncaps,'jnxAtmIfLpBackInfo':jnxAtmIfLpBackInfo,'jnxAtmIfScrambleEnable':jnxAtmIfScrambleEnable,'jnxAtmIfTxCellCount':jnxAtmIfTxCellCount,'jnxAtmIfRxCellCount':jnxAtmIfRxCellCount,'jnxAtmIfTxIdleCellCount':jnxAtmIfTxIdleCellCount,'jnxAtmIfUncorrHCSErrs':jnxAtmIfUncorrHCSErrs,'jnxAtmIfCorrHCSErrs':jnxAtmIfCorrHCSErrs,'jnxAtmIfTxCellFIFOOverRuns':jnxAtmIfTxCellFIFOOverRuns,'jnxAtmIfRxCellFIFOOverRuns':jnxAtmIfRxCellFIFOOverRuns,'jnxAtmIfRxCellFIFOUnderRuns':jnxAtmIfRxCellFIFOUnderRuns,'jnxAtmIfInInvalidVCCells':jnxAtmIfInInvalidVCCells,'jnxAtmIfInNoBufferOAMCells':jnxAtmIfInNoBufferOAMCells,'jnxAtmIfInNoBufDropPkts':jnxAtmIfInNoBufDropPkts,'jnxAtmIfOutVCQueueDrops':jnxAtmIfOutVCQueueDrops,'jnxAtmIfInBadCrcs':jnxAtmIfInBadCrcs,'jnxAtmIfInLenErrPkts':jnxAtmIfInLenErrPkts,'jnxAtmIfInTimeoutPkts':jnxAtmIfInTimeoutPkts,'jnxAtmIfL2CircuitMode':jnxAtmIfL2CircuitMode,'jnxAtmVCTable':jnxAtmVCTable,_O:jnxAtmVCEntry,'jnxAtmVCConnType':jnxAtmVCConnType,'jnxAtmVCEncapsulation':jnxAtmVCEncapsulation,'jnxAtmVCMpDestIPv4Addr':jnxAtmVCMpDestIPv4Addr,'jnxAtmVCMpDestIPv6Addr':jnxAtmVCMpDestIPv6Addr,'jnxAtmVCFlags':jnxAtmVCFlags,'jnxAtmVCTotalDownTime':jnxAtmVCTotalDownTime,'jnxAtmVCInBytes':jnxAtmVCInBytes,'jnxAtmVCOutBytes':jnxAtmVCOutBytes,'jnxAtmVCInPkts':jnxAtmVCInPkts,'jnxAtmVCOutPkts':jnxAtmVCOutPkts,'jnxAtmVCTailQueuePktDrops':jnxAtmVCTailQueuePktDrops,'jnxAtmVCOAMPeriod':jnxAtmVCOAMPeriod,'jnxAtmVCOAMUpCellCount':jnxAtmVCOAMUpCellCount,'jnxAtmVCOAMDownCellCount':jnxAtmVCOAMDownCellCount,'jnxAtmVCInOAMF5LoopCells':jnxAtmVCInOAMF5LoopCells,'jnxAtmVCOutOAMF5LoopCells':jnxAtmVCOutOAMF5LoopCells,'jnxAtmVCInOAMF5RDICells':jnxAtmVCInOAMF5RDICells,'jnxAtmVCOutOAMF5RDICells':jnxAtmVCOutOAMF5RDICells,'jnxAtmVCInOAMF5AISCells':jnxAtmVCInOAMF5AISCells,'jnxAtmVCOutOAMF5AISCells':jnxAtmVCOutOAMF5AISCells,'jnxAtmVpTable':jnxAtmVpTable,_P:jnxAtmVpEntry,'jnxAtmVpFlags':jnxAtmVpFlags,'jnxAtmVpTotalDownTime':jnxAtmVpTotalDownTime,'jnxAtmVpOamPeriod':jnxAtmVpOamPeriod,'jnxAtmVpOamUpCellCount':jnxAtmVpOamUpCellCount,'jnxAtmVpOamDownCellCount':jnxAtmVpOamDownCellCount,'jnxAtmVpInBytes':jnxAtmVpInBytes,'jnxAtmVpOutBytes':jnxAtmVpOutBytes,'jnxAtmVpInPkts':jnxAtmVpInPkts,'jnxAtmVpOutPkts':jnxAtmVpOutPkts,'jnxAtmVpInOamF4Cells':jnxAtmVpInOamF4Cells,'jnxAtmVpOutOamF4Cells':jnxAtmVpOutOamF4Cells,'jnxAtmVpInOamF4LoopCells':jnxAtmVpInOamF4LoopCells,'jnxAtmVpOutOamF4LoopCells':jnxAtmVpOutOamF4LoopCells,'jnxAtmVpInOamF4RdiCells':jnxAtmVpInOamF4RdiCells,'jnxAtmVpOutOamF4RdiCells':jnxAtmVpOutOamF4RdiCells,'jnxAtmVpInOamF4AisCells':jnxAtmVpInOamF4AisCells,'jnxAtmTrunkTable':jnxAtmTrunkTable,'jnxAtmTrunkEntry':jnxAtmTrunkEntry,'jnxAtmTrunkId':jnxAtmTrunkId,'jnxAtmTrunkConnType':jnxAtmTrunkConnType,'jnxAtmTrunkEncapsulation':jnxAtmTrunkEncapsulation,'jnxAtmTrunkFlags':jnxAtmTrunkFlags,'jnxAtmTrunkTotalDownTime':jnxAtmTrunkTotalDownTime,'jnxAtmTrunkInBytes':jnxAtmTrunkInBytes,'jnxAtmTrunkOutBytes':jnxAtmTrunkOutBytes,'jnxAtmTrunkInPkts':jnxAtmTrunkInPkts,'jnxAtmTrunkOutPkts':jnxAtmTrunkOutPkts,'jnxAtmTrunkTailQueuePktDrops':jnxAtmTrunkTailQueuePktDrops,'jnxAtmTrunkInOAMF4AISCells':jnxAtmTrunkInOAMF4AISCells,'jnxAtmTrunkOutOAMF4AISCells':jnxAtmTrunkOutOAMF4AISCells})