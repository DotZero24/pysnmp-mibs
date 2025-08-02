_s='pdnAtmfM4LoopbackLocationGroup'
_r='pdnAtmfM4VpLoopbackTestErrorCode'
_q='pdnAtmfM4VpLoopbackTestAvgRTDelay'
_p='pdnAtmfM4VpLoopbackTestMaxRTDelay'
_o='pdnAtmfM4VpLoopbackTestMinRTDelay'
_n='pdnAtmfM4VpLoopbackTestCellsRcvd'
_m='pdnAtmfM4VpLoopbackTestCellsSent'
_l='pdnAtmfM4VpLoopbackTestElpsTime'
_k='pdnAtmfM4LoopbackLocationCode'
_j='pdnAtmfM4Vc1CellLoopErrorCode'
_i='pdnAtmfM4Vc1CellLoopReportedLocation'
_h='pdnAtmfM4Vc1CellLoopRTDelay'
_g='pdnAtmfM4VcLoopbackTestErrorCode'
_f='pdnAtmfM4VcLoopbackTestAvgRTDelay'
_e='pdnAtmfM4VcLoopbackTestMaxRTDelay'
_d='pdnAtmfM4VcLoopbackTestMinRTDelay'
_c='pdnAtmfM4VcLoopbackTestCellsRcvd'
_b='pdnAtmfM4VcLoopbackTestCellsSent'
_a='pdnAtmfM4VcLoopbackTestElpsTime'
_Z='pdnAtmfM4TcProtoHistCorrectedHEC'
_Y='pdnAtmfM4TcProtoHistUnknownCells'
_X='pdnAtmfM4TcProtoHistLCDEvents'
_W='pdnAtmfM4TcProtoHistOutDiscards'
_V='pdnAtmfM4TcProtoHistInDiscards'
_U='pdnAtmfM4TcProtoHistCellOuts'
_T='pdnAtmfM4TcProtoHistCellIns'
_S='pdnAtmfM4TcProtoCurrCorrectedHEC'
_R='pdnAtmfM4TcProtoCurrUnknownCells'
_Q='pdnAtmfM4TcProtoCurrLCDEvents'
_P='pdnAtmfM4TcProtoCurrOutDiscards'
_O='pdnAtmfM4TcProtoCurrInDiscards'
_N='pdnAtmfM4TcProtoCurrCellOuts'
_M='pdnAtmfM4TcProtoCurrCellIns'
_L='pdnAtmfM4VpLoopbackTestEntry'
_K='pdnAtmfM4Vc1CellLoopEntry'
_J='pdnAtmfM4VcLoopbackTestEntry'
_I='pdnAtmfM4TcProtoHistExtEntry'
_H='pdnAtmfM4TcProtoCurrExtEntry'
_G='ifIndex'
_F='IF-MIB'
_E='OctetString'
_D='milliseconds'
_C='read-only'
_B='PDN-ATMM4EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmfM4TcProtoCurrEntry,atmfM4TcProtoHistEntry,atmfM4VcTestEntry,atmfM4VpTestEntry=mibBuilder.importSymbols('ATM-FORUM-SNMP-M4-MIB','atmfM4TcProtoCurrEntry','atmfM4TcProtoHistEntry','atmfM4VcTestEntry','atmfM4VpTestEntry')
ifIndex,=mibBuilder.importSymbols(_F,_G)
pdnAtm,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnAtm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnAtmfM4ExtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6))
if mibBuilder.loadTexts:pdnAtmfM4ExtMIB.setRevisions(('2002-08-15 00:00','2001-03-08 00:00','2000-09-26 00:00','2000-09-22 00:00','2000-09-21 00:00','2000-09-08 00:00','2000-06-29 00:00'))
class PdnAtmfM4TestErrorCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noError',0),('badIfIndex',1),('noVccFound',2),('notOwner',3),('noResourceAvailable',4),('noLoopbackAllocated',5),('testCompleted',6),('testTimeOut',7),('adminStatusDisabled',8)))
_PdnAtmfM4ExtObjects_ObjectIdentity=ObjectIdentity
pdnAtmfM4ExtObjects=_PdnAtmfM4ExtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6,1))
_PdnAtmfM4TcProtoCurrExtTable_Object=MibTable
pdnAtmfM4TcProtoCurrExtTable=_PdnAtmfM4TcProtoCurrExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,1))
if mibBuilder.loadTexts:pdnAtmfM4TcProtoCurrExtTable.setStatus(_A)
_PdnAtmfM4TcProtoCurrExtEntry_Object=MibTableRow
pdnAtmfM4TcProtoCurrExtEntry=_PdnAtmfM4TcProtoCurrExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,1,1))
if mibBuilder.loadTexts:pdnAtmfM4TcProtoCurrExtEntry.setStatus(_A)
_PdnAtmfM4TcProtoCurrCellIns_Type=Gauge32
_PdnAtmfM4TcProtoCurrCellIns_Object=MibTableColumn
pdnAtmfM4TcProtoCurrCellIns=_PdnAtmfM4TcProtoCurrCellIns_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,1,1,1),_PdnAtmfM4TcProtoCurrCellIns_Type())
pdnAtmfM4TcProtoCurrCellIns.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoCurrCellIns.setStatus(_A)
_PdnAtmfM4TcProtoCurrCellOuts_Type=Gauge32
_PdnAtmfM4TcProtoCurrCellOuts_Object=MibTableColumn
pdnAtmfM4TcProtoCurrCellOuts=_PdnAtmfM4TcProtoCurrCellOuts_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,1,1,2),_PdnAtmfM4TcProtoCurrCellOuts_Type())
pdnAtmfM4TcProtoCurrCellOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoCurrCellOuts.setStatus(_A)
_PdnAtmfM4TcProtoCurrInDiscards_Type=Gauge32
_PdnAtmfM4TcProtoCurrInDiscards_Object=MibTableColumn
pdnAtmfM4TcProtoCurrInDiscards=_PdnAtmfM4TcProtoCurrInDiscards_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,1,1,3),_PdnAtmfM4TcProtoCurrInDiscards_Type())
pdnAtmfM4TcProtoCurrInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoCurrInDiscards.setStatus(_A)
_PdnAtmfM4TcProtoCurrOutDiscards_Type=Gauge32
_PdnAtmfM4TcProtoCurrOutDiscards_Object=MibTableColumn
pdnAtmfM4TcProtoCurrOutDiscards=_PdnAtmfM4TcProtoCurrOutDiscards_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,1,1,4),_PdnAtmfM4TcProtoCurrOutDiscards_Type())
pdnAtmfM4TcProtoCurrOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoCurrOutDiscards.setStatus(_A)
_PdnAtmfM4TcProtoCurrLCDEvents_Type=Gauge32
_PdnAtmfM4TcProtoCurrLCDEvents_Object=MibTableColumn
pdnAtmfM4TcProtoCurrLCDEvents=_PdnAtmfM4TcProtoCurrLCDEvents_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,1,1,5),_PdnAtmfM4TcProtoCurrLCDEvents_Type())
pdnAtmfM4TcProtoCurrLCDEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoCurrLCDEvents.setStatus(_A)
_PdnAtmfM4TcProtoCurrUnknownCells_Type=Gauge32
_PdnAtmfM4TcProtoCurrUnknownCells_Object=MibTableColumn
pdnAtmfM4TcProtoCurrUnknownCells=_PdnAtmfM4TcProtoCurrUnknownCells_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,1,1,6),_PdnAtmfM4TcProtoCurrUnknownCells_Type())
pdnAtmfM4TcProtoCurrUnknownCells.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoCurrUnknownCells.setStatus(_A)
_PdnAtmfM4TcProtoCurrCorrectedHEC_Type=Gauge32
_PdnAtmfM4TcProtoCurrCorrectedHEC_Object=MibTableColumn
pdnAtmfM4TcProtoCurrCorrectedHEC=_PdnAtmfM4TcProtoCurrCorrectedHEC_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,1,1,7),_PdnAtmfM4TcProtoCurrCorrectedHEC_Type())
pdnAtmfM4TcProtoCurrCorrectedHEC.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoCurrCorrectedHEC.setStatus(_A)
_PdnAtmfM4TcProtoHistExtTable_Object=MibTable
pdnAtmfM4TcProtoHistExtTable=_PdnAtmfM4TcProtoHistExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,2))
if mibBuilder.loadTexts:pdnAtmfM4TcProtoHistExtTable.setStatus(_A)
_PdnAtmfM4TcProtoHistExtEntry_Object=MibTableRow
pdnAtmfM4TcProtoHistExtEntry=_PdnAtmfM4TcProtoHistExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,2,1))
if mibBuilder.loadTexts:pdnAtmfM4TcProtoHistExtEntry.setStatus(_A)
_PdnAtmfM4TcProtoHistCellIns_Type=Gauge32
_PdnAtmfM4TcProtoHistCellIns_Object=MibTableColumn
pdnAtmfM4TcProtoHistCellIns=_PdnAtmfM4TcProtoHistCellIns_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,2,1,1),_PdnAtmfM4TcProtoHistCellIns_Type())
pdnAtmfM4TcProtoHistCellIns.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoHistCellIns.setStatus(_A)
_PdnAtmfM4TcProtoHistCellOuts_Type=Gauge32
_PdnAtmfM4TcProtoHistCellOuts_Object=MibTableColumn
pdnAtmfM4TcProtoHistCellOuts=_PdnAtmfM4TcProtoHistCellOuts_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,2,1,2),_PdnAtmfM4TcProtoHistCellOuts_Type())
pdnAtmfM4TcProtoHistCellOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoHistCellOuts.setStatus(_A)
_PdnAtmfM4TcProtoHistInDiscards_Type=Gauge32
_PdnAtmfM4TcProtoHistInDiscards_Object=MibTableColumn
pdnAtmfM4TcProtoHistInDiscards=_PdnAtmfM4TcProtoHistInDiscards_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,2,1,3),_PdnAtmfM4TcProtoHistInDiscards_Type())
pdnAtmfM4TcProtoHistInDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoHistInDiscards.setStatus(_A)
_PdnAtmfM4TcProtoHistOutDiscards_Type=Gauge32
_PdnAtmfM4TcProtoHistOutDiscards_Object=MibTableColumn
pdnAtmfM4TcProtoHistOutDiscards=_PdnAtmfM4TcProtoHistOutDiscards_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,2,1,4),_PdnAtmfM4TcProtoHistOutDiscards_Type())
pdnAtmfM4TcProtoHistOutDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoHistOutDiscards.setStatus(_A)
_PdnAtmfM4TcProtoHistLCDEvents_Type=Gauge32
_PdnAtmfM4TcProtoHistLCDEvents_Object=MibTableColumn
pdnAtmfM4TcProtoHistLCDEvents=_PdnAtmfM4TcProtoHistLCDEvents_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,2,1,5),_PdnAtmfM4TcProtoHistLCDEvents_Type())
pdnAtmfM4TcProtoHistLCDEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoHistLCDEvents.setStatus(_A)
_PdnAtmfM4TcProtoHistUnknownCells_Type=Gauge32
_PdnAtmfM4TcProtoHistUnknownCells_Object=MibTableColumn
pdnAtmfM4TcProtoHistUnknownCells=_PdnAtmfM4TcProtoHistUnknownCells_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,2,1,6),_PdnAtmfM4TcProtoHistUnknownCells_Type())
pdnAtmfM4TcProtoHistUnknownCells.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoHistUnknownCells.setStatus(_A)
_PdnAtmfM4TcProtoHistCorrectedHEC_Type=Gauge32
_PdnAtmfM4TcProtoHistCorrectedHEC_Object=MibTableColumn
pdnAtmfM4TcProtoHistCorrectedHEC=_PdnAtmfM4TcProtoHistCorrectedHEC_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,2,1,7),_PdnAtmfM4TcProtoHistCorrectedHEC_Type())
pdnAtmfM4TcProtoHistCorrectedHEC.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4TcProtoHistCorrectedHEC.setStatus(_A)
_PdnAtmfM4TestTypes_ObjectIdentity=ObjectIdentity
pdnAtmfM4TestTypes=_PdnAtmfM4TestTypes_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,3))
_PdnAtmfM4TestOAMLoopbackSegMultiCell_ObjectIdentity=ObjectIdentity
pdnAtmfM4TestOAMLoopbackSegMultiCell=_PdnAtmfM4TestOAMLoopbackSegMultiCell_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,3,1))
if mibBuilder.loadTexts:pdnAtmfM4TestOAMLoopbackSegMultiCell.setStatus(_A)
_PdnAtmfM4TestOAMLoopbackE2EMultiCell_ObjectIdentity=ObjectIdentity
pdnAtmfM4TestOAMLoopbackE2EMultiCell=_PdnAtmfM4TestOAMLoopbackE2EMultiCell_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,3,2))
if mibBuilder.loadTexts:pdnAtmfM4TestOAMLoopbackE2EMultiCell.setStatus(_A)
_PdnAtmfM4VcLoopbackTestTable_Object=MibTable
pdnAtmfM4VcLoopbackTestTable=_PdnAtmfM4VcLoopbackTestTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,4))
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestTable.setStatus(_A)
_PdnAtmfM4VcLoopbackTestEntry_Object=MibTableRow
pdnAtmfM4VcLoopbackTestEntry=_PdnAtmfM4VcLoopbackTestEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,4,1))
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestEntry.setStatus(_A)
_PdnAtmfM4VcLoopbackTestElpsTime_Type=TimeTicks
_PdnAtmfM4VcLoopbackTestElpsTime_Object=MibTableColumn
pdnAtmfM4VcLoopbackTestElpsTime=_PdnAtmfM4VcLoopbackTestElpsTime_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,4,1,1),_PdnAtmfM4VcLoopbackTestElpsTime_Type())
pdnAtmfM4VcLoopbackTestElpsTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestElpsTime.setStatus(_A)
_PdnAtmfM4VcLoopbackTestCellsSent_Type=Gauge32
_PdnAtmfM4VcLoopbackTestCellsSent_Object=MibTableColumn
pdnAtmfM4VcLoopbackTestCellsSent=_PdnAtmfM4VcLoopbackTestCellsSent_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,4,1,2),_PdnAtmfM4VcLoopbackTestCellsSent_Type())
pdnAtmfM4VcLoopbackTestCellsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestCellsSent.setStatus(_A)
_PdnAtmfM4VcLoopbackTestCellsRcvd_Type=Gauge32
_PdnAtmfM4VcLoopbackTestCellsRcvd_Object=MibTableColumn
pdnAtmfM4VcLoopbackTestCellsRcvd=_PdnAtmfM4VcLoopbackTestCellsRcvd_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,4,1,3),_PdnAtmfM4VcLoopbackTestCellsRcvd_Type())
pdnAtmfM4VcLoopbackTestCellsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestCellsRcvd.setStatus(_A)
_PdnAtmfM4VcLoopbackTestMinRTDelay_Type=Gauge32
_PdnAtmfM4VcLoopbackTestMinRTDelay_Object=MibTableColumn
pdnAtmfM4VcLoopbackTestMinRTDelay=_PdnAtmfM4VcLoopbackTestMinRTDelay_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,4,1,4),_PdnAtmfM4VcLoopbackTestMinRTDelay_Type())
pdnAtmfM4VcLoopbackTestMinRTDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestMinRTDelay.setStatus(_A)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestMinRTDelay.setUnits(_D)
_PdnAtmfM4VcLoopbackTestMaxRTDelay_Type=Gauge32
_PdnAtmfM4VcLoopbackTestMaxRTDelay_Object=MibTableColumn
pdnAtmfM4VcLoopbackTestMaxRTDelay=_PdnAtmfM4VcLoopbackTestMaxRTDelay_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,4,1,5),_PdnAtmfM4VcLoopbackTestMaxRTDelay_Type())
pdnAtmfM4VcLoopbackTestMaxRTDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestMaxRTDelay.setStatus(_A)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestMaxRTDelay.setUnits(_D)
_PdnAtmfM4VcLoopbackTestAvgRTDelay_Type=Gauge32
_PdnAtmfM4VcLoopbackTestAvgRTDelay_Object=MibTableColumn
pdnAtmfM4VcLoopbackTestAvgRTDelay=_PdnAtmfM4VcLoopbackTestAvgRTDelay_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,4,1,6),_PdnAtmfM4VcLoopbackTestAvgRTDelay_Type())
pdnAtmfM4VcLoopbackTestAvgRTDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestAvgRTDelay.setStatus(_A)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestAvgRTDelay.setUnits(_D)
_PdnAtmfM4VcLoopbackTestErrorCode_Type=PdnAtmfM4TestErrorCode
_PdnAtmfM4VcLoopbackTestErrorCode_Object=MibTableColumn
pdnAtmfM4VcLoopbackTestErrorCode=_PdnAtmfM4VcLoopbackTestErrorCode_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,4,1,7),_PdnAtmfM4VcLoopbackTestErrorCode_Type())
pdnAtmfM4VcLoopbackTestErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestErrorCode.setStatus(_A)
_PdnAtmfM4Vc1CellLoopTable_Object=MibTable
pdnAtmfM4Vc1CellLoopTable=_PdnAtmfM4Vc1CellLoopTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,5))
if mibBuilder.loadTexts:pdnAtmfM4Vc1CellLoopTable.setStatus(_A)
_PdnAtmfM4Vc1CellLoopEntry_Object=MibTableRow
pdnAtmfM4Vc1CellLoopEntry=_PdnAtmfM4Vc1CellLoopEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,5,1))
if mibBuilder.loadTexts:pdnAtmfM4Vc1CellLoopEntry.setStatus(_A)
_PdnAtmfM4Vc1CellLoopRTDelay_Type=Gauge32
_PdnAtmfM4Vc1CellLoopRTDelay_Object=MibTableColumn
pdnAtmfM4Vc1CellLoopRTDelay=_PdnAtmfM4Vc1CellLoopRTDelay_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,5,1,1),_PdnAtmfM4Vc1CellLoopRTDelay_Type())
pdnAtmfM4Vc1CellLoopRTDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4Vc1CellLoopRTDelay.setStatus(_A)
if mibBuilder.loadTexts:pdnAtmfM4Vc1CellLoopRTDelay.setUnits(_D)
class _PdnAtmfM4Vc1CellLoopReportedLocation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_PdnAtmfM4Vc1CellLoopReportedLocation_Type.__name__=_E
_PdnAtmfM4Vc1CellLoopReportedLocation_Object=MibTableColumn
pdnAtmfM4Vc1CellLoopReportedLocation=_PdnAtmfM4Vc1CellLoopReportedLocation_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,5,1,2),_PdnAtmfM4Vc1CellLoopReportedLocation_Type())
pdnAtmfM4Vc1CellLoopReportedLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4Vc1CellLoopReportedLocation.setStatus(_A)
_PdnAtmfM4Vc1CellLoopErrorCode_Type=PdnAtmfM4TestErrorCode
_PdnAtmfM4Vc1CellLoopErrorCode_Object=MibTableColumn
pdnAtmfM4Vc1CellLoopErrorCode=_PdnAtmfM4Vc1CellLoopErrorCode_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,5,1,3),_PdnAtmfM4Vc1CellLoopErrorCode_Type())
pdnAtmfM4Vc1CellLoopErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4Vc1CellLoopErrorCode.setStatus(_A)
_PdnAtmfM4LoopbackLocationTable_Object=MibTable
pdnAtmfM4LoopbackLocationTable=_PdnAtmfM4LoopbackLocationTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,6))
if mibBuilder.loadTexts:pdnAtmfM4LoopbackLocationTable.setStatus(_A)
_PdnAtmfM4LoopbackLocationEntry_Object=MibTableRow
pdnAtmfM4LoopbackLocationEntry=_PdnAtmfM4LoopbackLocationEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,6,1))
pdnAtmfM4LoopbackLocationEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pdnAtmfM4LoopbackLocationEntry.setStatus(_A)
class _PdnAtmfM4LoopbackLocationCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_PdnAtmfM4LoopbackLocationCode_Type.__name__=_E
_PdnAtmfM4LoopbackLocationCode_Object=MibTableColumn
pdnAtmfM4LoopbackLocationCode=_PdnAtmfM4LoopbackLocationCode_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,6,1,1),_PdnAtmfM4LoopbackLocationCode_Type())
pdnAtmfM4LoopbackLocationCode.setMaxAccess('read-write')
if mibBuilder.loadTexts:pdnAtmfM4LoopbackLocationCode.setStatus(_A)
_PdnAtmfM4VpLoopbackTestTable_Object=MibTable
pdnAtmfM4VpLoopbackTestTable=_PdnAtmfM4VpLoopbackTestTable_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,7))
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestTable.setStatus(_A)
_PdnAtmfM4VpLoopbackTestEntry_Object=MibTableRow
pdnAtmfM4VpLoopbackTestEntry=_PdnAtmfM4VpLoopbackTestEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,7,1))
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestEntry.setStatus(_A)
_PdnAtmfM4VpLoopbackTestElpsTime_Type=TimeTicks
_PdnAtmfM4VpLoopbackTestElpsTime_Object=MibTableColumn
pdnAtmfM4VpLoopbackTestElpsTime=_PdnAtmfM4VpLoopbackTestElpsTime_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,7,1,1),_PdnAtmfM4VpLoopbackTestElpsTime_Type())
pdnAtmfM4VpLoopbackTestElpsTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestElpsTime.setStatus(_A)
_PdnAtmfM4VpLoopbackTestCellsSent_Type=Gauge32
_PdnAtmfM4VpLoopbackTestCellsSent_Object=MibTableColumn
pdnAtmfM4VpLoopbackTestCellsSent=_PdnAtmfM4VpLoopbackTestCellsSent_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,7,1,2),_PdnAtmfM4VpLoopbackTestCellsSent_Type())
pdnAtmfM4VpLoopbackTestCellsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestCellsSent.setStatus(_A)
_PdnAtmfM4VpLoopbackTestCellsRcvd_Type=Gauge32
_PdnAtmfM4VpLoopbackTestCellsRcvd_Object=MibTableColumn
pdnAtmfM4VpLoopbackTestCellsRcvd=_PdnAtmfM4VpLoopbackTestCellsRcvd_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,7,1,3),_PdnAtmfM4VpLoopbackTestCellsRcvd_Type())
pdnAtmfM4VpLoopbackTestCellsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestCellsRcvd.setStatus(_A)
_PdnAtmfM4VpLoopbackTestMinRTDelay_Type=Gauge32
_PdnAtmfM4VpLoopbackTestMinRTDelay_Object=MibTableColumn
pdnAtmfM4VpLoopbackTestMinRTDelay=_PdnAtmfM4VpLoopbackTestMinRTDelay_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,7,1,4),_PdnAtmfM4VpLoopbackTestMinRTDelay_Type())
pdnAtmfM4VpLoopbackTestMinRTDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestMinRTDelay.setStatus(_A)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestMinRTDelay.setUnits(_D)
_PdnAtmfM4VpLoopbackTestMaxRTDelay_Type=Gauge32
_PdnAtmfM4VpLoopbackTestMaxRTDelay_Object=MibTableColumn
pdnAtmfM4VpLoopbackTestMaxRTDelay=_PdnAtmfM4VpLoopbackTestMaxRTDelay_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,7,1,5),_PdnAtmfM4VpLoopbackTestMaxRTDelay_Type())
pdnAtmfM4VpLoopbackTestMaxRTDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestMaxRTDelay.setStatus(_A)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestMaxRTDelay.setUnits(_D)
_PdnAtmfM4VpLoopbackTestAvgRTDelay_Type=Gauge32
_PdnAtmfM4VpLoopbackTestAvgRTDelay_Object=MibTableColumn
pdnAtmfM4VpLoopbackTestAvgRTDelay=_PdnAtmfM4VpLoopbackTestAvgRTDelay_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,7,1,6),_PdnAtmfM4VpLoopbackTestAvgRTDelay_Type())
pdnAtmfM4VpLoopbackTestAvgRTDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestAvgRTDelay.setStatus(_A)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestAvgRTDelay.setUnits(_D)
_PdnAtmfM4VpLoopbackTestErrorCode_Type=PdnAtmfM4TestErrorCode
_PdnAtmfM4VpLoopbackTestErrorCode_Object=MibTableColumn
pdnAtmfM4VpLoopbackTestErrorCode=_PdnAtmfM4VpLoopbackTestErrorCode_Object((1,3,6,1,4,1,1795,2,24,2,6,11,6,1,7,1,7),_PdnAtmfM4VpLoopbackTestErrorCode_Type())
pdnAtmfM4VpLoopbackTestErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestErrorCode.setStatus(_A)
_PdnAtmfM4ExtTraps_ObjectIdentity=ObjectIdentity
pdnAtmfM4ExtTraps=_PdnAtmfM4ExtTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6,2))
_PdnAtmfM4ExtTrapPrefix_ObjectIdentity=ObjectIdentity
pdnAtmfM4ExtTrapPrefix=_PdnAtmfM4ExtTrapPrefix_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6,2,0))
_PdnAtmfM4ExtConformance_ObjectIdentity=ObjectIdentity
pdnAtmfM4ExtConformance=_PdnAtmfM4ExtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6,3))
_PdnAtmfM4Groups_ObjectIdentity=ObjectIdentity
pdnAtmfM4Groups=_PdnAtmfM4Groups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6,3,1))
_PdnAtmfM4Compliances_ObjectIdentity=ObjectIdentity
pdnAtmfM4Compliances=_PdnAtmfM4Compliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,11,6,3,2))
atmfM4TcProtoCurrEntry.registerAugmentions((_B,_H))
pdnAtmfM4TcProtoCurrExtEntry.setIndexNames(*atmfM4TcProtoCurrEntry.getIndexNames())
atmfM4TcProtoHistEntry.registerAugmentions((_B,_I))
pdnAtmfM4TcProtoHistExtEntry.setIndexNames(*atmfM4TcProtoHistEntry.getIndexNames())
atmfM4VcTestEntry.registerAugmentions((_B,_J))
pdnAtmfM4VcLoopbackTestEntry.setIndexNames(*atmfM4VcTestEntry.getIndexNames())
atmfM4VcTestEntry.registerAugmentions((_B,_K))
pdnAtmfM4Vc1CellLoopEntry.setIndexNames(*atmfM4VcTestEntry.getIndexNames())
atmfM4VpTestEntry.registerAugmentions((_B,_L))
pdnAtmfM4VpLoopbackTestEntry.setIndexNames(*atmfM4VpTestEntry.getIndexNames())
pdnAtmfM4TcCurrGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,11,6,3,1,1))
pdnAtmfM4TcCurrGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:pdnAtmfM4TcCurrGroup.setStatus(_A)
pdnAtmfM4TcHistGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,11,6,3,1,2))
pdnAtmfM4TcHistGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:pdnAtmfM4TcHistGroup.setStatus(_A)
pdnAtmfM4VcLoopbackTestGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,11,6,3,1,3))
pdnAtmfM4VcLoopbackTestGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:pdnAtmfM4VcLoopbackTestGroup.setStatus(_A)
pdnAtmfM4Vc1CellLoopGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,11,6,3,1,4))
pdnAtmfM4Vc1CellLoopGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:pdnAtmfM4Vc1CellLoopGroup.setStatus(_A)
pdnAtmfM4LoopbackLocationGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,11,6,3,1,5))
pdnAtmfM4LoopbackLocationGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:pdnAtmfM4LoopbackLocationGroup.setStatus(_A)
pdnAtmfM4VpLoopbackTestGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,11,6,3,1,6))
pdnAtmfM4VpLoopbackTestGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:pdnAtmfM4VpLoopbackTestGroup.setStatus(_A)
pdnAtmfM4Compliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,11,6,3,2,1))
pdnAtmfM4Compliance.setObjects((_B,_s))
if mibBuilder.loadTexts:pdnAtmfM4Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PdnAtmfM4TestErrorCode':PdnAtmfM4TestErrorCode,'pdnAtmfM4ExtMIB':pdnAtmfM4ExtMIB,'pdnAtmfM4ExtObjects':pdnAtmfM4ExtObjects,'pdnAtmfM4TcProtoCurrExtTable':pdnAtmfM4TcProtoCurrExtTable,_H:pdnAtmfM4TcProtoCurrExtEntry,_M:pdnAtmfM4TcProtoCurrCellIns,_N:pdnAtmfM4TcProtoCurrCellOuts,_O:pdnAtmfM4TcProtoCurrInDiscards,_P:pdnAtmfM4TcProtoCurrOutDiscards,_Q:pdnAtmfM4TcProtoCurrLCDEvents,_R:pdnAtmfM4TcProtoCurrUnknownCells,_S:pdnAtmfM4TcProtoCurrCorrectedHEC,'pdnAtmfM4TcProtoHistExtTable':pdnAtmfM4TcProtoHistExtTable,_I:pdnAtmfM4TcProtoHistExtEntry,_T:pdnAtmfM4TcProtoHistCellIns,_U:pdnAtmfM4TcProtoHistCellOuts,_V:pdnAtmfM4TcProtoHistInDiscards,_W:pdnAtmfM4TcProtoHistOutDiscards,_X:pdnAtmfM4TcProtoHistLCDEvents,_Y:pdnAtmfM4TcProtoHistUnknownCells,_Z:pdnAtmfM4TcProtoHistCorrectedHEC,'pdnAtmfM4TestTypes':pdnAtmfM4TestTypes,'pdnAtmfM4TestOAMLoopbackSegMultiCell':pdnAtmfM4TestOAMLoopbackSegMultiCell,'pdnAtmfM4TestOAMLoopbackE2EMultiCell':pdnAtmfM4TestOAMLoopbackE2EMultiCell,'pdnAtmfM4VcLoopbackTestTable':pdnAtmfM4VcLoopbackTestTable,_J:pdnAtmfM4VcLoopbackTestEntry,_a:pdnAtmfM4VcLoopbackTestElpsTime,_b:pdnAtmfM4VcLoopbackTestCellsSent,_c:pdnAtmfM4VcLoopbackTestCellsRcvd,_d:pdnAtmfM4VcLoopbackTestMinRTDelay,_e:pdnAtmfM4VcLoopbackTestMaxRTDelay,_f:pdnAtmfM4VcLoopbackTestAvgRTDelay,_g:pdnAtmfM4VcLoopbackTestErrorCode,'pdnAtmfM4Vc1CellLoopTable':pdnAtmfM4Vc1CellLoopTable,_K:pdnAtmfM4Vc1CellLoopEntry,_h:pdnAtmfM4Vc1CellLoopRTDelay,_i:pdnAtmfM4Vc1CellLoopReportedLocation,_j:pdnAtmfM4Vc1CellLoopErrorCode,'pdnAtmfM4LoopbackLocationTable':pdnAtmfM4LoopbackLocationTable,'pdnAtmfM4LoopbackLocationEntry':pdnAtmfM4LoopbackLocationEntry,_k:pdnAtmfM4LoopbackLocationCode,'pdnAtmfM4VpLoopbackTestTable':pdnAtmfM4VpLoopbackTestTable,_L:pdnAtmfM4VpLoopbackTestEntry,_l:pdnAtmfM4VpLoopbackTestElpsTime,_m:pdnAtmfM4VpLoopbackTestCellsSent,_n:pdnAtmfM4VpLoopbackTestCellsRcvd,_o:pdnAtmfM4VpLoopbackTestMinRTDelay,_p:pdnAtmfM4VpLoopbackTestMaxRTDelay,_q:pdnAtmfM4VpLoopbackTestAvgRTDelay,_r:pdnAtmfM4VpLoopbackTestErrorCode,'pdnAtmfM4ExtTraps':pdnAtmfM4ExtTraps,'pdnAtmfM4ExtTrapPrefix':pdnAtmfM4ExtTrapPrefix,'pdnAtmfM4ExtConformance':pdnAtmfM4ExtConformance,'pdnAtmfM4Groups':pdnAtmfM4Groups,'pdnAtmfM4TcCurrGroup':pdnAtmfM4TcCurrGroup,'pdnAtmfM4TcHistGroup':pdnAtmfM4TcHistGroup,'pdnAtmfM4VcLoopbackTestGroup':pdnAtmfM4VcLoopbackTestGroup,'pdnAtmfM4Vc1CellLoopGroup':pdnAtmfM4Vc1CellLoopGroup,_s:pdnAtmfM4LoopbackLocationGroup,'pdnAtmfM4VpLoopbackTestGroup':pdnAtmfM4VpLoopbackTestGroup,'pdnAtmfM4Compliances':pdnAtmfM4Compliances,'pdnAtmfM4Compliance':pdnAtmfM4Compliance})