_d='dslStatsVer1'
_c='dslModemVer1'
_b='fastPathRxCrcError'
_a='fastPathTxCrcError'
_Z='interleavedPathTxCrcError'
_Y='interleavedPathRxCrcError'
_X='dslModemTxPeakCellRate'
_W='dslModemSeverlyErroredFrameCount'
_V='dslModemLossOfSignalCount'
_U='dslModemRxSuperframeCnt'
_T='dslModemTxSuperframeCnt'
_S='dslModemRxPayload'
_R='dslModemTxPayload'
_Q='dslModemRxMargin'
_P='dslModemTxMargin'
_O='dslModemRxLineAttenuation'
_N='dslModemTxLineAttenuation'
_M='dslModemRxConnectionRate'
_L='dslModemTxConnectionRate'
_K='dslTrainedModulation'
_J='dslTrainedPath'
_I='dslModemState'
_H='dslModulation'
_G='adsl2PlusDelt'
_F='adsl2Plus'
_E='adsl2Delt'
_D='Integer32'
_C='read-only'
_B='MX-DSL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixConfig,mediatrixMgmt=mibBuilder.importSymbols('MX-SMI','mediatrixConfig','mediatrixMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dslMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,250))
if mibBuilder.loadTexts:dslMIB.setRevisions(('2005-01-26 00:00','2005-01-31 00:00','2005-02-08 00:00'))
_DslStatus_ObjectIdentity=ObjectIdentity
dslStatus=_DslStatus_ObjectIdentity((1,3,6,1,4,1,4935,10,100))
class _DslModemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unconnected',0),('connecting',1),('connected',2)))
_DslModemState_Type.__name__=_D
_DslModemState_Object=MibScalar
dslModemState=_DslModemState_Object((1,3,6,1,4,1,4935,10,100,100),_DslModemState_Type())
dslModemState.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemState.setStatus(_A)
class _DslTrainedPath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fast',0),('interleaved',1)))
_DslTrainedPath_Type.__name__=_D
_DslTrainedPath_Object=MibScalar
dslTrainedPath=_DslTrainedPath_Object((1,3,6,1,4,1,4935,10,100,150),_DslTrainedPath_Type())
dslTrainedPath.setMaxAccess(_C)
if mibBuilder.loadTexts:dslTrainedPath.setStatus(_A)
class _DslTrainedModulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4,8,9,16,17)));namedValues=NamedValues(*(('notTrained',0),('t1413',2),('gDmt',3),('gLite',4),('adsl2',8),(_E,9),(_F,16),(_G,17)))
_DslTrainedModulation_Type.__name__=_D
_DslTrainedModulation_Object=MibScalar
dslTrainedModulation=_DslTrainedModulation_Object((1,3,6,1,4,1,4935,10,100,200),_DslTrainedModulation_Type())
dslTrainedModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:dslTrainedModulation.setStatus(_A)
_DslModemStats_ObjectIdentity=ObjectIdentity
dslModemStats=_DslModemStats_ObjectIdentity((1,3,6,1,4,1,4935,10,100,5000))
_DslModemTxConnectionRate_Type=Unsigned32
_DslModemTxConnectionRate_Object=MibScalar
dslModemTxConnectionRate=_DslModemTxConnectionRate_Object((1,3,6,1,4,1,4935,10,100,5000,50),_DslModemTxConnectionRate_Type())
dslModemTxConnectionRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemTxConnectionRate.setStatus(_A)
_DslModemRxConnectionRate_Type=Unsigned32
_DslModemRxConnectionRate_Object=MibScalar
dslModemRxConnectionRate=_DslModemRxConnectionRate_Object((1,3,6,1,4,1,4935,10,100,5000,100),_DslModemRxConnectionRate_Type())
dslModemRxConnectionRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemRxConnectionRate.setStatus(_A)
_DslModemTxLineAttenuation_Type=Unsigned32
_DslModemTxLineAttenuation_Object=MibScalar
dslModemTxLineAttenuation=_DslModemTxLineAttenuation_Object((1,3,6,1,4,1,4935,10,100,5000,150),_DslModemTxLineAttenuation_Type())
dslModemTxLineAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemTxLineAttenuation.setStatus(_A)
_DslModemRxLineAttenuation_Type=Unsigned32
_DslModemRxLineAttenuation_Object=MibScalar
dslModemRxLineAttenuation=_DslModemRxLineAttenuation_Object((1,3,6,1,4,1,4935,10,100,5000,200),_DslModemRxLineAttenuation_Type())
dslModemRxLineAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemRxLineAttenuation.setStatus(_A)
_DslModemTxMargin_Type=Unsigned32
_DslModemTxMargin_Object=MibScalar
dslModemTxMargin=_DslModemTxMargin_Object((1,3,6,1,4,1,4935,10,100,5000,250),_DslModemTxMargin_Type())
dslModemTxMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemTxMargin.setStatus(_A)
_DslModemRxMargin_Type=Unsigned32
_DslModemRxMargin_Object=MibScalar
dslModemRxMargin=_DslModemRxMargin_Object((1,3,6,1,4,1,4935,10,100,5000,300),_DslModemRxMargin_Type())
dslModemRxMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemRxMargin.setStatus(_A)
_DslModemTxPayload_Type=Unsigned32
_DslModemTxPayload_Object=MibScalar
dslModemTxPayload=_DslModemTxPayload_Object((1,3,6,1,4,1,4935,10,100,5000,350),_DslModemTxPayload_Type())
dslModemTxPayload.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemTxPayload.setStatus(_A)
_DslModemRxPayload_Type=Unsigned32
_DslModemRxPayload_Object=MibScalar
dslModemRxPayload=_DslModemRxPayload_Object((1,3,6,1,4,1,4935,10,100,5000,400),_DslModemRxPayload_Type())
dslModemRxPayload.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemRxPayload.setStatus(_A)
_DslModemTxSuperframeCnt_Type=Unsigned32
_DslModemTxSuperframeCnt_Object=MibScalar
dslModemTxSuperframeCnt=_DslModemTxSuperframeCnt_Object((1,3,6,1,4,1,4935,10,100,5000,450),_DslModemTxSuperframeCnt_Type())
dslModemTxSuperframeCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemTxSuperframeCnt.setStatus(_A)
_DslModemRxSuperframeCnt_Type=Unsigned32
_DslModemRxSuperframeCnt_Object=MibScalar
dslModemRxSuperframeCnt=_DslModemRxSuperframeCnt_Object((1,3,6,1,4,1,4935,10,100,5000,500),_DslModemRxSuperframeCnt_Type())
dslModemRxSuperframeCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemRxSuperframeCnt.setStatus(_A)
_DslModemLossOfSignalCount_Type=Unsigned32
_DslModemLossOfSignalCount_Object=MibScalar
dslModemLossOfSignalCount=_DslModemLossOfSignalCount_Object((1,3,6,1,4,1,4935,10,100,5000,650),_DslModemLossOfSignalCount_Type())
dslModemLossOfSignalCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemLossOfSignalCount.setStatus(_A)
_DslModemSeverlyErroredFrameCount_Type=Unsigned32
_DslModemSeverlyErroredFrameCount_Object=MibScalar
dslModemSeverlyErroredFrameCount=_DslModemSeverlyErroredFrameCount_Object((1,3,6,1,4,1,4935,10,100,5000,700),_DslModemSeverlyErroredFrameCount_Type())
dslModemSeverlyErroredFrameCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemSeverlyErroredFrameCount.setStatus(_A)
_DslModemTxPeakCellRate_Type=Unsigned32
_DslModemTxPeakCellRate_Object=MibScalar
dslModemTxPeakCellRate=_DslModemTxPeakCellRate_Object((1,3,6,1,4,1,4935,10,100,5000,750),_DslModemTxPeakCellRate_Type())
dslModemTxPeakCellRate.setMaxAccess(_C)
if mibBuilder.loadTexts:dslModemTxPeakCellRate.setStatus(_A)
_InterleavedPath_ObjectIdentity=ObjectIdentity
interleavedPath=_InterleavedPath_ObjectIdentity((1,3,6,1,4,1,4935,10,100,5000,5000))
_InterleavedPathTxCrcError_Type=Unsigned32
_InterleavedPathTxCrcError_Object=MibScalar
interleavedPathTxCrcError=_InterleavedPathTxCrcError_Object((1,3,6,1,4,1,4935,10,100,5000,5000,50),_InterleavedPathTxCrcError_Type())
interleavedPathTxCrcError.setMaxAccess(_C)
if mibBuilder.loadTexts:interleavedPathTxCrcError.setStatus(_A)
_InterleavedPathRxCrcError_Type=Unsigned32
_InterleavedPathRxCrcError_Object=MibScalar
interleavedPathRxCrcError=_InterleavedPathRxCrcError_Object((1,3,6,1,4,1,4935,10,100,5000,5000,100),_InterleavedPathRxCrcError_Type())
interleavedPathRxCrcError.setMaxAccess(_C)
if mibBuilder.loadTexts:interleavedPathRxCrcError.setStatus(_A)
_FastPath_ObjectIdentity=ObjectIdentity
fastPath=_FastPath_ObjectIdentity((1,3,6,1,4,1,4935,10,100,5000,8000))
_FastPathTxCrcError_Type=Unsigned32
_FastPathTxCrcError_Object=MibScalar
fastPathTxCrcError=_FastPathTxCrcError_Object((1,3,6,1,4,1,4935,10,100,5000,8000,50),_FastPathTxCrcError_Type())
fastPathTxCrcError.setMaxAccess(_C)
if mibBuilder.loadTexts:fastPathTxCrcError.setStatus(_A)
_FastPathRxCrcError_Type=Unsigned32
_FastPathRxCrcError_Object=MibScalar
fastPathRxCrcError=_FastPathRxCrcError_Object((1,3,6,1,4,1,4935,10,100,5000,8000,100),_FastPathRxCrcError_Type())
fastPathRxCrcError.setMaxAccess(_C)
if mibBuilder.loadTexts:fastPathRxCrcError.setStatus(_A)
_DslMIBObjects_ObjectIdentity=ObjectIdentity
dslMIBObjects=_DslMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,250,1))
class _DslModulation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,8,9,16,17)));namedValues=NamedValues(*(('mMode',1),('t1413',2),('gDmt',3),('gLite',4),('adsl2',8),(_E,9),(_F,16),(_G,17)))
_DslModulation_Type.__name__=_D
_DslModulation_Object=MibScalar
dslModulation=_DslModulation_Object((1,3,6,1,4,1,4935,15,250,1,50),_DslModulation_Type())
dslModulation.setMaxAccess('read-write')
if mibBuilder.loadTexts:dslModulation.setStatus(_A)
_DslConformance_ObjectIdentity=ObjectIdentity
dslConformance=_DslConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,250,2))
_DslCompliances_ObjectIdentity=ObjectIdentity
dslCompliances=_DslCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,250,2,1))
_DslGroups_ObjectIdentity=ObjectIdentity
dslGroups=_DslGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,250,2,5))
dslModemVer1=ObjectGroup((1,3,6,1,4,1,4935,15,250,2,5,50))
dslModemVer1.setObjects((_B,_H))
if mibBuilder.loadTexts:dslModemVer1.setStatus(_A)
dslStatsVer1=ObjectGroup((1,3,6,1,4,1,4935,15,250,2,5,100))
dslStatsVer1.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:dslStatsVer1.setStatus(_A)
dslComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,250,2,1,1))
dslComplVer1.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:dslComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dslStatus':dslStatus,_I:dslModemState,_J:dslTrainedPath,_K:dslTrainedModulation,'dslModemStats':dslModemStats,_L:dslModemTxConnectionRate,_M:dslModemRxConnectionRate,_N:dslModemTxLineAttenuation,_O:dslModemRxLineAttenuation,_P:dslModemTxMargin,_Q:dslModemRxMargin,_R:dslModemTxPayload,_S:dslModemRxPayload,_T:dslModemTxSuperframeCnt,_U:dslModemRxSuperframeCnt,_V:dslModemLossOfSignalCount,_W:dslModemSeverlyErroredFrameCount,_X:dslModemTxPeakCellRate,'interleavedPath':interleavedPath,_Z:interleavedPathTxCrcError,_Y:interleavedPathRxCrcError,'fastPath':fastPath,_a:fastPathTxCrcError,_b:fastPathRxCrcError,'dslMIB':dslMIB,'dslMIBObjects':dslMIBObjects,_H:dslModulation,'dslConformance':dslConformance,'dslCompliances':dslCompliances,'dslComplVer1':dslComplVer1,'dslGroups':dslGroups,_c:dslModemVer1,_d:dslStatsVer1})