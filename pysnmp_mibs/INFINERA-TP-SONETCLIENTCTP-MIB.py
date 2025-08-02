_AB='sonetClientCtpGroup'
_AA='sonetClientCtpEncapClientDisableAction'
_A9='sonetClientCtpServiceModeQualifier'
_A8='sonetClientCtpServiceMode'
_A7='sonetClientCtpLinePrbsMonMode'
_A6='sonetClientCtpLinePrbsGenMode'
_A5='sonetClientCtpTxSesDayTceReporting'
_A4='sonetClientCtpTxEsDayTceReporting'
_A3='sonetClientCtpTxSefsDayTceReporting'
_A2='sonetClientCtpTxCvDayTceReporting'
_A1='sonetClientCtpTxSes15MinutesTceReporting'
_A0='sonetClientCtpTxEs15MinutesTceReporting'
_z='sonetClientCtpTxSefs15MinutesTceReporting'
_y='sonetClientCtpTxCv15MinutesTceReporting'
_x='sonetClientCtpRxSesDayTceReporting'
_w='sonetClientCtpRxEsDayTceReporting'
_v='sonetClientCtpRxSefsDayTceReporting'
_u='sonetClientCtpRxCvDayTceReporting'
_t='sonetClientCtpRxSes15MinutesTceReporting'
_s='sonetClientCtpRxEs15MinutesTceReporting'
_r='sonetClientCtpRxSefs15MinutesTceReporting'
_q='sonetClientCtpRxCv15MinutesTceReporting'
_p='sonetClientCtpTxSesDayTce'
_o='sonetClientCtpTxEsDayTce'
_n='sonetClientCtpTxSefsDayTce'
_m='sonetClientCtpTxCvDayTce'
_l='sonetClientCtpTxSes15MinutesTce'
_k='sonetClientCtpTxEs15MinutesTce'
_j='sonetClientCtpTxSefs15MinutesTce'
_i='sonetClientCtpTxCv15MinutesTce'
_h='sonetClientCtpRxSesDayTce'
_g='sonetClientCtpRxEsDayTce'
_f='sonetClientCtpRxSefsDayTce'
_e='sonetClientCtpRxCvDayTce'
_d='sonetClientCtpRxSes15MinutesTce'
_c='sonetClientCtpRxEs15MinutesTce'
_b='sonetClientCtpRxSefs15MinutesTce'
_a='sonetClientCtpRxCv15MinutesTce'
_Z='sonetClientCtpRxJ0MessageCompliance'
_Y='sonetClientCtpRxJ0TraceMode'
_X='sonetClientCtpRxJ0MismatchReporting'
_W='sonetClientCtpRxJ0MessageLength'
_V='sonetClientCtpTransmittedJ0'
_U='sonetClientCtpExpectedRxJ0'
_T='sonetClientCtpRxJ0'
_S='sonetClientCtpConfiguredServiceType'
_R='sonetClientCtpPmHistStatsEnable'
_Q='sonetClientCtpLoopback'
_P='sonetClientCtpSupportingCircuitIdList'
_O='sonetClientCtpTribPrbsMonMode'
_N='sonetClientCtpTribPrbsGenMode'
_M='InfnPmHistStatsControl'
_L='InfnLoopbackType'
_K='InfnJ0TraceMode'
_J='InfnJ0MessageCompliance'
_I='ifIndex'
_H='IF-MIB'
_G='read-only'
_F='InfnEnableDisable'
_E='Integer32'
_D='TruthValue'
_C='read-write'
_B='INFINERA-TP-SONETCLIENTCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnClientAction,InfnEnableDisable,InfnJ0MessageCompliance,InfnJ0TraceMode,InfnLoopbackType,InfnPmHistStatsControl,InfnSMQ,InfnServiceMode,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnClientAction',_F,_J,_K,_L,_M,'InfnSMQ','InfnServiceMode','InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
sonetClientCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,16))
if mibBuilder.loadTexts:sonetClientCtpMIB.setRevisions(('2008-10-20 00:00',))
_SonetClientCtpTable_Object=MibTable
sonetClientCtpTable=_SonetClientCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1))
if mibBuilder.loadTexts:sonetClientCtpTable.setStatus(_A)
_SonetClientCtpEntry_Object=MibTableRow
sonetClientCtpEntry=_SonetClientCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1))
sonetClientCtpEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:sonetClientCtpEntry.setStatus(_A)
class _SonetClientCtpTribPrbsGenMode_Type(InfnEnableDisable):defaultValue=1
_SonetClientCtpTribPrbsGenMode_Type.__name__=_F
_SonetClientCtpTribPrbsGenMode_Object=MibTableColumn
sonetClientCtpTribPrbsGenMode=_SonetClientCtpTribPrbsGenMode_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,1),_SonetClientCtpTribPrbsGenMode_Type())
sonetClientCtpTribPrbsGenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTribPrbsGenMode.setStatus(_A)
class _SonetClientCtpTribPrbsMonMode_Type(InfnEnableDisable):defaultValue=1
_SonetClientCtpTribPrbsMonMode_Type.__name__=_F
_SonetClientCtpTribPrbsMonMode_Object=MibTableColumn
sonetClientCtpTribPrbsMonMode=_SonetClientCtpTribPrbsMonMode_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,2),_SonetClientCtpTribPrbsMonMode_Type())
sonetClientCtpTribPrbsMonMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTribPrbsMonMode.setStatus(_A)
_SonetClientCtpSupportingCircuitIdList_Type=DisplayString
_SonetClientCtpSupportingCircuitIdList_Object=MibTableColumn
sonetClientCtpSupportingCircuitIdList=_SonetClientCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,3),_SonetClientCtpSupportingCircuitIdList_Type())
sonetClientCtpSupportingCircuitIdList.setMaxAccess(_G)
if mibBuilder.loadTexts:sonetClientCtpSupportingCircuitIdList.setStatus(_A)
class _SonetClientCtpLoopback_Type(InfnLoopbackType):defaultValue=1
_SonetClientCtpLoopback_Type.__name__=_L
_SonetClientCtpLoopback_Object=MibTableColumn
sonetClientCtpLoopback=_SonetClientCtpLoopback_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,4),_SonetClientCtpLoopback_Type())
sonetClientCtpLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpLoopback.setStatus(_A)
class _SonetClientCtpPmHistStatsEnable_Type(InfnPmHistStatsControl):defaultValue=1
_SonetClientCtpPmHistStatsEnable_Type.__name__=_M
_SonetClientCtpPmHistStatsEnable_Object=MibTableColumn
sonetClientCtpPmHistStatsEnable=_SonetClientCtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,5),_SonetClientCtpPmHistStatsEnable_Type())
sonetClientCtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpPmHistStatsEnable.setStatus(_A)
_SonetClientCtpConfiguredServiceType_Type=InfnServiceType
_SonetClientCtpConfiguredServiceType_Object=MibTableColumn
sonetClientCtpConfiguredServiceType=_SonetClientCtpConfiguredServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,6),_SonetClientCtpConfiguredServiceType_Type())
sonetClientCtpConfiguredServiceType.setMaxAccess(_G)
if mibBuilder.loadTexts:sonetClientCtpConfiguredServiceType.setStatus(_A)
_SonetClientCtpRxJ0_Type=DisplayString
_SonetClientCtpRxJ0_Object=MibTableColumn
sonetClientCtpRxJ0=_SonetClientCtpRxJ0_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,7),_SonetClientCtpRxJ0_Type())
sonetClientCtpRxJ0.setMaxAccess(_G)
if mibBuilder.loadTexts:sonetClientCtpRxJ0.setStatus(_A)
_SonetClientCtpExpectedRxJ0_Type=DisplayString
_SonetClientCtpExpectedRxJ0_Object=MibTableColumn
sonetClientCtpExpectedRxJ0=_SonetClientCtpExpectedRxJ0_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,8),_SonetClientCtpExpectedRxJ0_Type())
sonetClientCtpExpectedRxJ0.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpExpectedRxJ0.setStatus(_A)
_SonetClientCtpTransmittedJ0_Type=DisplayString
_SonetClientCtpTransmittedJ0_Object=MibTableColumn
sonetClientCtpTransmittedJ0=_SonetClientCtpTransmittedJ0_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,9),_SonetClientCtpTransmittedJ0_Type())
sonetClientCtpTransmittedJ0.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTransmittedJ0.setStatus(_A)
class _SonetClientCtpRxJ0MessageLength_Type(Integer32):defaultValue=16
_SonetClientCtpRxJ0MessageLength_Type.__name__=_E
_SonetClientCtpRxJ0MessageLength_Object=MibTableColumn
sonetClientCtpRxJ0MessageLength=_SonetClientCtpRxJ0MessageLength_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,10),_SonetClientCtpRxJ0MessageLength_Type())
sonetClientCtpRxJ0MessageLength.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxJ0MessageLength.setStatus(_A)
class _SonetClientCtpRxJ0MismatchReporting_Type(InfnEnableDisable):defaultValue=1
_SonetClientCtpRxJ0MismatchReporting_Type.__name__=_F
_SonetClientCtpRxJ0MismatchReporting_Object=MibTableColumn
sonetClientCtpRxJ0MismatchReporting=_SonetClientCtpRxJ0MismatchReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,11),_SonetClientCtpRxJ0MismatchReporting_Type())
sonetClientCtpRxJ0MismatchReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxJ0MismatchReporting.setStatus(_A)
class _SonetClientCtpRxJ0TraceMode_Type(InfnJ0TraceMode):defaultValue=1
_SonetClientCtpRxJ0TraceMode_Type.__name__=_K
_SonetClientCtpRxJ0TraceMode_Object=MibTableColumn
sonetClientCtpRxJ0TraceMode=_SonetClientCtpRxJ0TraceMode_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,12),_SonetClientCtpRxJ0TraceMode_Type())
sonetClientCtpRxJ0TraceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxJ0TraceMode.setStatus(_A)
class _SonetClientCtpRxJ0MessageCompliance_Type(InfnJ0MessageCompliance):defaultValue=2
_SonetClientCtpRxJ0MessageCompliance_Type.__name__=_J
_SonetClientCtpRxJ0MessageCompliance_Object=MibTableColumn
sonetClientCtpRxJ0MessageCompliance=_SonetClientCtpRxJ0MessageCompliance_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,13),_SonetClientCtpRxJ0MessageCompliance_Type())
sonetClientCtpRxJ0MessageCompliance.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxJ0MessageCompliance.setStatus(_A)
_SonetClientCtpRxCv15MinutesTce_Type=Counter64
_SonetClientCtpRxCv15MinutesTce_Object=MibTableColumn
sonetClientCtpRxCv15MinutesTce=_SonetClientCtpRxCv15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,14),_SonetClientCtpRxCv15MinutesTce_Type())
sonetClientCtpRxCv15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxCv15MinutesTce.setStatus(_A)
class _SonetClientCtpRxSefs15MinutesTce_Type(Integer32):defaultValue=3
_SonetClientCtpRxSefs15MinutesTce_Type.__name__=_E
_SonetClientCtpRxSefs15MinutesTce_Object=MibTableColumn
sonetClientCtpRxSefs15MinutesTce=_SonetClientCtpRxSefs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,15),_SonetClientCtpRxSefs15MinutesTce_Type())
sonetClientCtpRxSefs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxSefs15MinutesTce.setStatus(_A)
class _SonetClientCtpRxEs15MinutesTce_Type(Integer32):defaultValue=120
_SonetClientCtpRxEs15MinutesTce_Type.__name__=_E
_SonetClientCtpRxEs15MinutesTce_Object=MibTableColumn
sonetClientCtpRxEs15MinutesTce=_SonetClientCtpRxEs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,16),_SonetClientCtpRxEs15MinutesTce_Type())
sonetClientCtpRxEs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxEs15MinutesTce.setStatus(_A)
class _SonetClientCtpRxSes15MinutesTce_Type(Integer32):defaultValue=3
_SonetClientCtpRxSes15MinutesTce_Type.__name__=_E
_SonetClientCtpRxSes15MinutesTce_Object=MibTableColumn
sonetClientCtpRxSes15MinutesTce=_SonetClientCtpRxSes15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,17),_SonetClientCtpRxSes15MinutesTce_Type())
sonetClientCtpRxSes15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxSes15MinutesTce.setStatus(_A)
_SonetClientCtpRxCvDayTce_Type=Counter64
_SonetClientCtpRxCvDayTce_Object=MibTableColumn
sonetClientCtpRxCvDayTce=_SonetClientCtpRxCvDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,18),_SonetClientCtpRxCvDayTce_Type())
sonetClientCtpRxCvDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxCvDayTce.setStatus(_A)
class _SonetClientCtpRxSefsDayTce_Type(Integer32):defaultValue=7
_SonetClientCtpRxSefsDayTce_Type.__name__=_E
_SonetClientCtpRxSefsDayTce_Object=MibTableColumn
sonetClientCtpRxSefsDayTce=_SonetClientCtpRxSefsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,19),_SonetClientCtpRxSefsDayTce_Type())
sonetClientCtpRxSefsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxSefsDayTce.setStatus(_A)
class _SonetClientCtpRxEsDayTce_Type(Integer32):defaultValue=1200
_SonetClientCtpRxEsDayTce_Type.__name__=_E
_SonetClientCtpRxEsDayTce_Object=MibTableColumn
sonetClientCtpRxEsDayTce=_SonetClientCtpRxEsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,20),_SonetClientCtpRxEsDayTce_Type())
sonetClientCtpRxEsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxEsDayTce.setStatus(_A)
class _SonetClientCtpRxSesDayTce_Type(Integer32):defaultValue=7
_SonetClientCtpRxSesDayTce_Type.__name__=_E
_SonetClientCtpRxSesDayTce_Object=MibTableColumn
sonetClientCtpRxSesDayTce=_SonetClientCtpRxSesDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,21),_SonetClientCtpRxSesDayTce_Type())
sonetClientCtpRxSesDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxSesDayTce.setStatus(_A)
_SonetClientCtpTxCv15MinutesTce_Type=Counter64
_SonetClientCtpTxCv15MinutesTce_Object=MibTableColumn
sonetClientCtpTxCv15MinutesTce=_SonetClientCtpTxCv15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,22),_SonetClientCtpTxCv15MinutesTce_Type())
sonetClientCtpTxCv15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxCv15MinutesTce.setStatus(_A)
class _SonetClientCtpTxSefs15MinutesTce_Type(Integer32):defaultValue=3
_SonetClientCtpTxSefs15MinutesTce_Type.__name__=_E
_SonetClientCtpTxSefs15MinutesTce_Object=MibTableColumn
sonetClientCtpTxSefs15MinutesTce=_SonetClientCtpTxSefs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,23),_SonetClientCtpTxSefs15MinutesTce_Type())
sonetClientCtpTxSefs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxSefs15MinutesTce.setStatus(_A)
class _SonetClientCtpTxEs15MinutesTce_Type(Integer32):defaultValue=120
_SonetClientCtpTxEs15MinutesTce_Type.__name__=_E
_SonetClientCtpTxEs15MinutesTce_Object=MibTableColumn
sonetClientCtpTxEs15MinutesTce=_SonetClientCtpTxEs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,24),_SonetClientCtpTxEs15MinutesTce_Type())
sonetClientCtpTxEs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxEs15MinutesTce.setStatus(_A)
class _SonetClientCtpTxSes15MinutesTce_Type(Integer32):defaultValue=3
_SonetClientCtpTxSes15MinutesTce_Type.__name__=_E
_SonetClientCtpTxSes15MinutesTce_Object=MibTableColumn
sonetClientCtpTxSes15MinutesTce=_SonetClientCtpTxSes15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,25),_SonetClientCtpTxSes15MinutesTce_Type())
sonetClientCtpTxSes15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxSes15MinutesTce.setStatus(_A)
_SonetClientCtpTxCvDayTce_Type=Counter64
_SonetClientCtpTxCvDayTce_Object=MibTableColumn
sonetClientCtpTxCvDayTce=_SonetClientCtpTxCvDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,26),_SonetClientCtpTxCvDayTce_Type())
sonetClientCtpTxCvDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxCvDayTce.setStatus(_A)
class _SonetClientCtpTxSefsDayTce_Type(Integer32):defaultValue=7
_SonetClientCtpTxSefsDayTce_Type.__name__=_E
_SonetClientCtpTxSefsDayTce_Object=MibTableColumn
sonetClientCtpTxSefsDayTce=_SonetClientCtpTxSefsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,27),_SonetClientCtpTxSefsDayTce_Type())
sonetClientCtpTxSefsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxSefsDayTce.setStatus(_A)
class _SonetClientCtpTxEsDayTce_Type(Integer32):defaultValue=1200
_SonetClientCtpTxEsDayTce_Type.__name__=_E
_SonetClientCtpTxEsDayTce_Object=MibTableColumn
sonetClientCtpTxEsDayTce=_SonetClientCtpTxEsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,28),_SonetClientCtpTxEsDayTce_Type())
sonetClientCtpTxEsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxEsDayTce.setStatus(_A)
class _SonetClientCtpTxSesDayTce_Type(Integer32):defaultValue=7
_SonetClientCtpTxSesDayTce_Type.__name__=_E
_SonetClientCtpTxSesDayTce_Object=MibTableColumn
sonetClientCtpTxSesDayTce=_SonetClientCtpTxSesDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,29),_SonetClientCtpTxSesDayTce_Type())
sonetClientCtpTxSesDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxSesDayTce.setStatus(_A)
class _SonetClientCtpRxCv15MinutesTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpRxCv15MinutesTceReporting_Type.__name__=_D
_SonetClientCtpRxCv15MinutesTceReporting_Object=MibTableColumn
sonetClientCtpRxCv15MinutesTceReporting=_SonetClientCtpRxCv15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,30),_SonetClientCtpRxCv15MinutesTceReporting_Type())
sonetClientCtpRxCv15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxCv15MinutesTceReporting.setStatus(_A)
class _SonetClientCtpRxSefs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpRxSefs15MinutesTceReporting_Type.__name__=_D
_SonetClientCtpRxSefs15MinutesTceReporting_Object=MibTableColumn
sonetClientCtpRxSefs15MinutesTceReporting=_SonetClientCtpRxSefs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,31),_SonetClientCtpRxSefs15MinutesTceReporting_Type())
sonetClientCtpRxSefs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxSefs15MinutesTceReporting.setStatus(_A)
class _SonetClientCtpRxEs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpRxEs15MinutesTceReporting_Type.__name__=_D
_SonetClientCtpRxEs15MinutesTceReporting_Object=MibTableColumn
sonetClientCtpRxEs15MinutesTceReporting=_SonetClientCtpRxEs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,32),_SonetClientCtpRxEs15MinutesTceReporting_Type())
sonetClientCtpRxEs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxEs15MinutesTceReporting.setStatus(_A)
class _SonetClientCtpRxSes15MinutesTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpRxSes15MinutesTceReporting_Type.__name__=_D
_SonetClientCtpRxSes15MinutesTceReporting_Object=MibTableColumn
sonetClientCtpRxSes15MinutesTceReporting=_SonetClientCtpRxSes15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,33),_SonetClientCtpRxSes15MinutesTceReporting_Type())
sonetClientCtpRxSes15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxSes15MinutesTceReporting.setStatus(_A)
class _SonetClientCtpRxCvDayTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpRxCvDayTceReporting_Type.__name__=_D
_SonetClientCtpRxCvDayTceReporting_Object=MibTableColumn
sonetClientCtpRxCvDayTceReporting=_SonetClientCtpRxCvDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,34),_SonetClientCtpRxCvDayTceReporting_Type())
sonetClientCtpRxCvDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxCvDayTceReporting.setStatus(_A)
class _SonetClientCtpRxSefsDayTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpRxSefsDayTceReporting_Type.__name__=_D
_SonetClientCtpRxSefsDayTceReporting_Object=MibTableColumn
sonetClientCtpRxSefsDayTceReporting=_SonetClientCtpRxSefsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,35),_SonetClientCtpRxSefsDayTceReporting_Type())
sonetClientCtpRxSefsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxSefsDayTceReporting.setStatus(_A)
class _SonetClientCtpRxEsDayTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpRxEsDayTceReporting_Type.__name__=_D
_SonetClientCtpRxEsDayTceReporting_Object=MibTableColumn
sonetClientCtpRxEsDayTceReporting=_SonetClientCtpRxEsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,36),_SonetClientCtpRxEsDayTceReporting_Type())
sonetClientCtpRxEsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxEsDayTceReporting.setStatus(_A)
class _SonetClientCtpRxSesDayTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpRxSesDayTceReporting_Type.__name__=_D
_SonetClientCtpRxSesDayTceReporting_Object=MibTableColumn
sonetClientCtpRxSesDayTceReporting=_SonetClientCtpRxSesDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,37),_SonetClientCtpRxSesDayTceReporting_Type())
sonetClientCtpRxSesDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpRxSesDayTceReporting.setStatus(_A)
class _SonetClientCtpTxCv15MinutesTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpTxCv15MinutesTceReporting_Type.__name__=_D
_SonetClientCtpTxCv15MinutesTceReporting_Object=MibTableColumn
sonetClientCtpTxCv15MinutesTceReporting=_SonetClientCtpTxCv15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,38),_SonetClientCtpTxCv15MinutesTceReporting_Type())
sonetClientCtpTxCv15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxCv15MinutesTceReporting.setStatus(_A)
class _SonetClientCtpTxSefs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpTxSefs15MinutesTceReporting_Type.__name__=_D
_SonetClientCtpTxSefs15MinutesTceReporting_Object=MibTableColumn
sonetClientCtpTxSefs15MinutesTceReporting=_SonetClientCtpTxSefs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,39),_SonetClientCtpTxSefs15MinutesTceReporting_Type())
sonetClientCtpTxSefs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxSefs15MinutesTceReporting.setStatus(_A)
class _SonetClientCtpTxEs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpTxEs15MinutesTceReporting_Type.__name__=_D
_SonetClientCtpTxEs15MinutesTceReporting_Object=MibTableColumn
sonetClientCtpTxEs15MinutesTceReporting=_SonetClientCtpTxEs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,40),_SonetClientCtpTxEs15MinutesTceReporting_Type())
sonetClientCtpTxEs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxEs15MinutesTceReporting.setStatus(_A)
class _SonetClientCtpTxSes15MinutesTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpTxSes15MinutesTceReporting_Type.__name__=_D
_SonetClientCtpTxSes15MinutesTceReporting_Object=MibTableColumn
sonetClientCtpTxSes15MinutesTceReporting=_SonetClientCtpTxSes15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,41),_SonetClientCtpTxSes15MinutesTceReporting_Type())
sonetClientCtpTxSes15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxSes15MinutesTceReporting.setStatus(_A)
class _SonetClientCtpTxCvDayTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpTxCvDayTceReporting_Type.__name__=_D
_SonetClientCtpTxCvDayTceReporting_Object=MibTableColumn
sonetClientCtpTxCvDayTceReporting=_SonetClientCtpTxCvDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,42),_SonetClientCtpTxCvDayTceReporting_Type())
sonetClientCtpTxCvDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxCvDayTceReporting.setStatus(_A)
class _SonetClientCtpTxSefsDayTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpTxSefsDayTceReporting_Type.__name__=_D
_SonetClientCtpTxSefsDayTceReporting_Object=MibTableColumn
sonetClientCtpTxSefsDayTceReporting=_SonetClientCtpTxSefsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,43),_SonetClientCtpTxSefsDayTceReporting_Type())
sonetClientCtpTxSefsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxSefsDayTceReporting.setStatus(_A)
class _SonetClientCtpTxEsDayTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpTxEsDayTceReporting_Type.__name__=_D
_SonetClientCtpTxEsDayTceReporting_Object=MibTableColumn
sonetClientCtpTxEsDayTceReporting=_SonetClientCtpTxEsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,44),_SonetClientCtpTxEsDayTceReporting_Type())
sonetClientCtpTxEsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxEsDayTceReporting.setStatus(_A)
class _SonetClientCtpTxSesDayTceReporting_Type(TruthValue):defaultValue=2
_SonetClientCtpTxSesDayTceReporting_Type.__name__=_D
_SonetClientCtpTxSesDayTceReporting_Object=MibTableColumn
sonetClientCtpTxSesDayTceReporting=_SonetClientCtpTxSesDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,45),_SonetClientCtpTxSesDayTceReporting_Type())
sonetClientCtpTxSesDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpTxSesDayTceReporting.setStatus(_A)
class _SonetClientCtpLinePrbsGenMode_Type(InfnEnableDisable):defaultValue=1
_SonetClientCtpLinePrbsGenMode_Type.__name__=_F
_SonetClientCtpLinePrbsGenMode_Object=MibTableColumn
sonetClientCtpLinePrbsGenMode=_SonetClientCtpLinePrbsGenMode_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,46),_SonetClientCtpLinePrbsGenMode_Type())
sonetClientCtpLinePrbsGenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpLinePrbsGenMode.setStatus(_A)
class _SonetClientCtpLinePrbsMonMode_Type(InfnEnableDisable):defaultValue=1
_SonetClientCtpLinePrbsMonMode_Type.__name__=_F
_SonetClientCtpLinePrbsMonMode_Object=MibTableColumn
sonetClientCtpLinePrbsMonMode=_SonetClientCtpLinePrbsMonMode_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,47),_SonetClientCtpLinePrbsMonMode_Type())
sonetClientCtpLinePrbsMonMode.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpLinePrbsMonMode.setStatus(_A)
_SonetClientCtpServiceMode_Type=InfnServiceMode
_SonetClientCtpServiceMode_Object=MibTableColumn
sonetClientCtpServiceMode=_SonetClientCtpServiceMode_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,48),_SonetClientCtpServiceMode_Type())
sonetClientCtpServiceMode.setMaxAccess(_G)
if mibBuilder.loadTexts:sonetClientCtpServiceMode.setStatus(_A)
_SonetClientCtpServiceModeQualifier_Type=InfnSMQ
_SonetClientCtpServiceModeQualifier_Object=MibTableColumn
sonetClientCtpServiceModeQualifier=_SonetClientCtpServiceModeQualifier_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,49),_SonetClientCtpServiceModeQualifier_Type())
sonetClientCtpServiceModeQualifier.setMaxAccess(_G)
if mibBuilder.loadTexts:sonetClientCtpServiceModeQualifier.setStatus(_A)
_SonetClientCtpEncapClientDisableAction_Type=InfnClientAction
_SonetClientCtpEncapClientDisableAction_Object=MibTableColumn
sonetClientCtpEncapClientDisableAction=_SonetClientCtpEncapClientDisableAction_Object((1,3,6,1,4,1,21296,2,2,2,2,16,1,1,50),_SonetClientCtpEncapClientDisableAction_Type())
sonetClientCtpEncapClientDisableAction.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetClientCtpEncapClientDisableAction.setStatus(_A)
_SonetClientCtpConformance_ObjectIdentity=ObjectIdentity
sonetClientCtpConformance=_SonetClientCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,16,3))
_SonetClientCtpCompliances_ObjectIdentity=ObjectIdentity
sonetClientCtpCompliances=_SonetClientCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,16,3,1))
_SonetClientCtpGroups_ObjectIdentity=ObjectIdentity
sonetClientCtpGroups=_SonetClientCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,16,3,2))
sonetClientCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,16,3,2,1))
sonetClientCtpGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:sonetClientCtpGroup.setStatus(_A)
sonetClientCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,16,3,1,1))
sonetClientCtpCompliance.setObjects((_B,_AB))
if mibBuilder.loadTexts:sonetClientCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sonetClientCtpMIB':sonetClientCtpMIB,'sonetClientCtpTable':sonetClientCtpTable,'sonetClientCtpEntry':sonetClientCtpEntry,_N:sonetClientCtpTribPrbsGenMode,_O:sonetClientCtpTribPrbsMonMode,_P:sonetClientCtpSupportingCircuitIdList,_Q:sonetClientCtpLoopback,_R:sonetClientCtpPmHistStatsEnable,_S:sonetClientCtpConfiguredServiceType,_T:sonetClientCtpRxJ0,_U:sonetClientCtpExpectedRxJ0,_V:sonetClientCtpTransmittedJ0,_W:sonetClientCtpRxJ0MessageLength,_X:sonetClientCtpRxJ0MismatchReporting,_Y:sonetClientCtpRxJ0TraceMode,_Z:sonetClientCtpRxJ0MessageCompliance,_a:sonetClientCtpRxCv15MinutesTce,_b:sonetClientCtpRxSefs15MinutesTce,_c:sonetClientCtpRxEs15MinutesTce,_d:sonetClientCtpRxSes15MinutesTce,_e:sonetClientCtpRxCvDayTce,_f:sonetClientCtpRxSefsDayTce,_g:sonetClientCtpRxEsDayTce,_h:sonetClientCtpRxSesDayTce,_i:sonetClientCtpTxCv15MinutesTce,_j:sonetClientCtpTxSefs15MinutesTce,_k:sonetClientCtpTxEs15MinutesTce,_l:sonetClientCtpTxSes15MinutesTce,_m:sonetClientCtpTxCvDayTce,_n:sonetClientCtpTxSefsDayTce,_o:sonetClientCtpTxEsDayTce,_p:sonetClientCtpTxSesDayTce,_q:sonetClientCtpRxCv15MinutesTceReporting,_r:sonetClientCtpRxSefs15MinutesTceReporting,_s:sonetClientCtpRxEs15MinutesTceReporting,_t:sonetClientCtpRxSes15MinutesTceReporting,_u:sonetClientCtpRxCvDayTceReporting,_v:sonetClientCtpRxSefsDayTceReporting,_w:sonetClientCtpRxEsDayTceReporting,_x:sonetClientCtpRxSesDayTceReporting,_y:sonetClientCtpTxCv15MinutesTceReporting,_z:sonetClientCtpTxSefs15MinutesTceReporting,_A0:sonetClientCtpTxEs15MinutesTceReporting,_A1:sonetClientCtpTxSes15MinutesTceReporting,_A2:sonetClientCtpTxCvDayTceReporting,_A3:sonetClientCtpTxSefsDayTceReporting,_A4:sonetClientCtpTxEsDayTceReporting,_A5:sonetClientCtpTxSesDayTceReporting,_A6:sonetClientCtpLinePrbsGenMode,_A7:sonetClientCtpLinePrbsMonMode,_A8:sonetClientCtpServiceMode,_A9:sonetClientCtpServiceModeQualifier,_AA:sonetClientCtpEncapClientDisableAction,'sonetClientCtpConformance':sonetClientCtpConformance,'sonetClientCtpCompliances':sonetClientCtpCompliances,'sonetClientCtpCompliance':sonetClientCtpCompliance,'sonetClientCtpGroups':sonetClientCtpGroups,_AB:sonetClientCtpGroup})