_S='bdSampleTime'
_R='bdType'
_Q='bdAvgFrameSize'
_P='bdAbsoluteValue'
_O='bdAggrStats'
_N='bdThreshold'
_M='nBdType'
_L='bdWinAvgTime'
_K='slotPort'
_J='seconds'
_I='swVfId'
_H='SW-MIB'
_G='userPortNumber'
_F='Integer32'
_E='accessible-for-notify'
_D='DisplayString'
_C='read-only'
_B='BD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,fcSwitch=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules','fcSwitch')
SwPortIndex,=mibBuilder.importSymbols('Brocade-TC','SwPortIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
swVfId,=mibBuilder.importSymbols(_H,_I)
bd=ModuleIdentity((1,3,6,1,4,1,1588,2,1,1,51))
if mibBuilder.loadTexts:bd.setRevisions(('2014-04-10 11:46',))
class BdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('congestion',1),('latency',2)))
_BdTraps_ObjectIdentity=ObjectIdentity
bdTraps=_BdTraps_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,51,0))
if mibBuilder.loadTexts:bdTraps.setStatus(_A)
_BdConfig_ObjectIdentity=ObjectIdentity
bdConfig=_BdConfig_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,51,1))
if mibBuilder.loadTexts:bdConfig.setStatus(_A)
_BdStatus_Type=TruthValue
_BdStatus_Object=MibScalar
bdStatus=_BdStatus_Object((1,3,6,1,4,1,1588,2,1,1,51,1,1),_BdStatus_Type())
bdStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bdStatus.setStatus(_A)
class _BdLThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_BdLThreshold_Type.__name__=_D
_BdLThreshold_Object=MibScalar
bdLThreshold=_BdLThreshold_Object((1,3,6,1,4,1,1588,2,1,1,51,1,2),_BdLThreshold_Type())
bdLThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bdLThreshold.setStatus(_A)
class _BdCThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_BdCThreshold_Type.__name__=_D
_BdCThreshold_Object=MibScalar
bdCThreshold=_BdCThreshold_Object((1,3,6,1,4,1,1588,2,1,1,51,1,3),_BdCThreshold_Type())
bdCThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:bdCThreshold.setStatus(_A)
class _BdQTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_BdQTime_Type.__name__=_F
_BdQTime_Object=MibScalar
bdQTime=_BdQTime_Object((1,3,6,1,4,1,1588,2,1,1,51,1,4),_BdQTime_Type())
bdQTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bdQTime.setStatus(_A)
if mibBuilder.loadTexts:bdQTime.setUnits(_J)
class _BdWinAvgTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_BdWinAvgTime_Type.__name__=_F
_BdWinAvgTime_Object=MibScalar
bdWinAvgTime=_BdWinAvgTime_Object((1,3,6,1,4,1,1588,2,1,1,51,1,5),_BdWinAvgTime_Type())
bdWinAvgTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bdWinAvgTime.setStatus(_A)
if mibBuilder.loadTexts:bdWinAvgTime.setUnits(_J)
class _BdThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_BdThreshold_Type.__name__=_D
_BdThreshold_Object=MibScalar
bdThreshold=_BdThreshold_Object((1,3,6,1,4,1,1588,2,1,1,51,1,6),_BdThreshold_Type())
bdThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:bdThreshold.setStatus(_A)
_NBdType_Type=BdType
_NBdType_Object=MibScalar
nBdType=_NBdType_Object((1,3,6,1,4,1,1588,2,1,1,51,1,7),_NBdType_Type())
nBdType.setMaxAccess(_E)
if mibBuilder.loadTexts:nBdType.setStatus(_A)
_BdStats_ObjectIdentity=ObjectIdentity
bdStats=_BdStats_ObjectIdentity((1,3,6,1,4,1,1588,2,1,1,51,2))
if mibBuilder.loadTexts:bdStats.setStatus(_A)
_BdNumOfEntries_Type=Integer32
_BdNumOfEntries_Object=MibScalar
bdNumOfEntries=_BdNumOfEntries_Object((1,3,6,1,4,1,1588,2,1,1,51,2,1),_BdNumOfEntries_Type())
bdNumOfEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:bdNumOfEntries.setStatus(_A)
_BdStatsTable_Object=MibTable
bdStatsTable=_BdStatsTable_Object((1,3,6,1,4,1,1588,2,1,1,51,2,2))
if mibBuilder.loadTexts:bdStatsTable.setStatus(_A)
_BdStatsEntry_Object=MibTableRow
bdStatsEntry=_BdStatsEntry_Object((1,3,6,1,4,1,1588,2,1,1,51,2,2,1))
bdStatsEntry.setIndexNames((0,_B,_G),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:bdStatsEntry.setStatus(_A)
_UserPortNumber_Type=SwPortIndex
_UserPortNumber_Object=MibTableColumn
userPortNumber=_UserPortNumber_Object((1,3,6,1,4,1,1588,2,1,1,51,2,2,1,1),_UserPortNumber_Type())
userPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:userPortNumber.setStatus(_A)
_BdSampleTime_Type=Unsigned32
_BdSampleTime_Object=MibTableColumn
bdSampleTime=_BdSampleTime_Object((1,3,6,1,4,1,1588,2,1,1,51,2,2,1,2),_BdSampleTime_Type())
bdSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bdSampleTime.setStatus(_A)
if mibBuilder.loadTexts:bdSampleTime.setUnits(_J)
_BdType_Type=BdType
_BdType_Object=MibTableColumn
bdType=_BdType_Object((1,3,6,1,4,1,1588,2,1,1,51,2,2,1,3),_BdType_Type())
bdType.setMaxAccess(_C)
if mibBuilder.loadTexts:bdType.setStatus(_A)
class _BdStatsValue10SecsSample_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_BdStatsValue10SecsSample_Type.__name__=_D
_BdStatsValue10SecsSample_Object=MibTableColumn
bdStatsValue10SecsSample=_BdStatsValue10SecsSample_Object((1,3,6,1,4,1,1588,2,1,1,51,2,2,1,4),_BdStatsValue10SecsSample_Type())
bdStatsValue10SecsSample.setMaxAccess(_C)
if mibBuilder.loadTexts:bdStatsValue10SecsSample.setStatus(_A)
class _BdStatsValue60SecsSample_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_BdStatsValue60SecsSample_Type.__name__=_D
_BdStatsValue60SecsSample_Object=MibTableColumn
bdStatsValue60SecsSample=_BdStatsValue60SecsSample_Object((1,3,6,1,4,1,1588,2,1,1,51,2,2,1,5),_BdStatsValue60SecsSample_Type())
bdStatsValue60SecsSample.setMaxAccess(_C)
if mibBuilder.loadTexts:bdStatsValue60SecsSample.setStatus(_A)
class _BdStatsValue300SecsSample_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,5))
_BdStatsValue300SecsSample_Type.__name__=_D
_BdStatsValue300SecsSample_Object=MibTableColumn
bdStatsValue300SecsSample=_BdStatsValue300SecsSample_Object((1,3,6,1,4,1,1588,2,1,1,51,2,2,1,6),_BdStatsValue300SecsSample_Type())
bdStatsValue300SecsSample.setMaxAccess(_C)
if mibBuilder.loadTexts:bdStatsValue300SecsSample.setStatus(_A)
_SlotPort_Type=DisplayString
_SlotPort_Object=MibTableColumn
slotPort=_SlotPort_Object((1,3,6,1,4,1,1588,2,1,1,51,2,2,1,7),_SlotPort_Type())
slotPort.setMaxAccess(_E)
if mibBuilder.loadTexts:slotPort.setStatus(_A)
class _BdAggrStats_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_BdAggrStats_Type.__name__=_D
_BdAggrStats_Object=MibScalar
bdAggrStats=_BdAggrStats_Object((1,3,6,1,4,1,1588,2,1,1,51,2,3),_BdAggrStats_Type())
bdAggrStats.setMaxAccess(_E)
if mibBuilder.loadTexts:bdAggrStats.setStatus(_A)
class _BdAbsoluteValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_BdAbsoluteValue_Type.__name__=_F
_BdAbsoluteValue_Object=MibScalar
bdAbsoluteValue=_BdAbsoluteValue_Object((1,3,6,1,4,1,1588,2,1,1,51,2,4),_BdAbsoluteValue_Type())
bdAbsoluteValue.setMaxAccess(_E)
if mibBuilder.loadTexts:bdAbsoluteValue.setStatus(_A)
_BdAvgFrameSize_Type=Unsigned32
_BdAvgFrameSize_Object=MibScalar
bdAvgFrameSize=_BdAvgFrameSize_Object((1,3,6,1,4,1,1588,2,1,1,51,2,5),_BdAvgFrameSize_Type())
bdAvgFrameSize.setMaxAccess(_E)
if mibBuilder.loadTexts:bdAvgFrameSize.setStatus(_A)
bdTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,51,0,1))
bdTrap.setObjects(*((_B,_G),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_H,_I),(_B,_Q)))
if mibBuilder.loadTexts:bdTrap.setStatus(_A)
bdClearTrap=NotificationType((1,3,6,1,4,1,1588,2,1,1,51,0,2))
bdClearTrap.setObjects(*((_B,_G),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_H,_I),(_B,_Q)))
if mibBuilder.loadTexts:bdClearTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'BdType':BdType,'bd':bd,'bdTraps':bdTraps,'bdTrap':bdTrap,'bdClearTrap':bdClearTrap,'bdConfig':bdConfig,'bdStatus':bdStatus,'bdLThreshold':bdLThreshold,'bdCThreshold':bdCThreshold,'bdQTime':bdQTime,_L:bdWinAvgTime,_N:bdThreshold,_M:nBdType,'bdStats':bdStats,'bdNumOfEntries':bdNumOfEntries,'bdStatsTable':bdStatsTable,'bdStatsEntry':bdStatsEntry,_G:userPortNumber,_S:bdSampleTime,_R:bdType,'bdStatsValue10SecsSample':bdStatsValue10SecsSample,'bdStatsValue60SecsSample':bdStatsValue60SecsSample,'bdStatsValue300SecsSample':bdStatsValue300SecsSample,_K:slotPort,_O:bdAggrStats,_P:bdAbsoluteValue,_Q:bdAvgFrameSize})