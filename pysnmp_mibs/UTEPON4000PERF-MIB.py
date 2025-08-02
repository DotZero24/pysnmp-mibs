_E='utsSystemPerfBoardPhyId'
_D='UTEPON4000PERF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,MacAddress,Timeout=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId','MacAddress','Timeout')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
utsGeponBBS4000,=mibBuilder.importSymbols('UTS-BBS-COMMON-MIB','utsGeponBBS4000')
utsGeponBBS4000Performance=ModuleIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,4))
_UtsEthIfPerfExt_ObjectIdentity=ObjectIdentity
utsEthIfPerfExt=_UtsEthIfPerfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,4,1))
_UtsEthIfStatsExtObjects_ObjectIdentity=ObjectIdentity
utsEthIfStatsExtObjects=_UtsEthIfStatsExtObjects_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,4,1,1))
_UtsEfmPonPerfExt_ObjectIdentity=ObjectIdentity
utsEfmPonPerfExt=_UtsEfmPonPerfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,4,2))
_UtsLayer3PerfExt_ObjectIdentity=ObjectIdentity
utsLayer3PerfExt=_UtsLayer3PerfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,4,3))
_UtsSystemPerfExt_ObjectIdentity=ObjectIdentity
utsSystemPerfExt=_UtsSystemPerfExt_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,4,4))
_UtsSystemStatsExtObjects_ObjectIdentity=ObjectIdentity
utsSystemStatsExtObjects=_UtsSystemStatsExtObjects_ObjectIdentity((1,3,6,1,4,1,1949,1,3,10,200,6,4,4,1))
_UtsSystemPerfTable_Object=MibTable
utsSystemPerfTable=_UtsSystemPerfTable_Object((1,3,6,1,4,1,1949,1,3,10,200,6,4,4,1,1))
if mibBuilder.loadTexts:utsSystemPerfTable.setStatus(_A)
_UtsSystemPerfEntry_Object=MibTableRow
utsSystemPerfEntry=_UtsSystemPerfEntry_Object((1,3,6,1,4,1,1949,1,3,10,200,6,4,4,1,1,1))
utsSystemPerfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:utsSystemPerfEntry.setStatus(_A)
class _UtsSystemPerfBoardPhyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_UtsSystemPerfBoardPhyId_Type.__name__=_C
_UtsSystemPerfBoardPhyId_Object=MibTableColumn
utsSystemPerfBoardPhyId=_UtsSystemPerfBoardPhyId_Object((1,3,6,1,4,1,1949,1,3,10,200,6,4,4,1,1,1,1),_UtsSystemPerfBoardPhyId_Type())
utsSystemPerfBoardPhyId.setMaxAccess(_B)
if mibBuilder.loadTexts:utsSystemPerfBoardPhyId.setStatus(_A)
class _UtsSystemPerfBoardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('other',1),('csm',2),('epm04a',3),('epm04b',4),('epm04c',5),('gem04a',6),('gem04b',7)))
_UtsSystemPerfBoardType_Type.__name__=_C
_UtsSystemPerfBoardType_Object=MibTableColumn
utsSystemPerfBoardType=_UtsSystemPerfBoardType_Object((1,3,6,1,4,1,1949,1,3,10,200,6,4,4,1,1,1,2),_UtsSystemPerfBoardType_Type())
utsSystemPerfBoardType.setMaxAccess(_B)
if mibBuilder.loadTexts:utsSystemPerfBoardType.setStatus(_A)
_UtsSystemPerfCpuUtil_Type=Integer32
_UtsSystemPerfCpuUtil_Object=MibTableColumn
utsSystemPerfCpuUtil=_UtsSystemPerfCpuUtil_Object((1,3,6,1,4,1,1949,1,3,10,200,6,4,4,1,1,1,3),_UtsSystemPerfCpuUtil_Type())
utsSystemPerfCpuUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:utsSystemPerfCpuUtil.setStatus(_A)
_UtsSystemPerfMemUtil_Type=Integer32
_UtsSystemPerfMemUtil_Object=MibTableColumn
utsSystemPerfMemUtil=_UtsSystemPerfMemUtil_Object((1,3,6,1,4,1,1949,1,3,10,200,6,4,4,1,1,1,4),_UtsSystemPerfMemUtil_Type())
utsSystemPerfMemUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:utsSystemPerfMemUtil.setStatus(_A)
_UtsSystemPerfTemperature_Type=Integer32
_UtsSystemPerfTemperature_Object=MibTableColumn
utsSystemPerfTemperature=_UtsSystemPerfTemperature_Object((1,3,6,1,4,1,1949,1,3,10,200,6,4,4,1,1,1,5),_UtsSystemPerfTemperature_Type())
utsSystemPerfTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:utsSystemPerfTemperature.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'utsGeponBBS4000Performance':utsGeponBBS4000Performance,'utsEthIfPerfExt':utsEthIfPerfExt,'utsEthIfStatsExtObjects':utsEthIfStatsExtObjects,'utsEfmPonPerfExt':utsEfmPonPerfExt,'utsLayer3PerfExt':utsLayer3PerfExt,'utsSystemPerfExt':utsSystemPerfExt,'utsSystemStatsExtObjects':utsSystemStatsExtObjects,'utsSystemPerfTable':utsSystemPerfTable,'utsSystemPerfEntry':utsSystemPerfEntry,_E:utsSystemPerfBoardPhyId,'utsSystemPerfBoardType':utsSystemPerfBoardType,'utsSystemPerfCpuUtil':utsSystemPerfCpuUtil,'utsSystemPerfMemUtil':utsSystemPerfMemUtil,'utsSystemPerfTemperature':utsSystemPerfTemperature})