_AD='otuClientCtpGroup'
_AC='otuClientCtpTxBei15MinutesTceReporting'
_AB='otuClientCtpTxBeiDayTceReporting'
_AA='otuClientCtpRxBei15MinutesTceReporting'
_A9='otuClientCtpRxBeiDayTceReporting'
_A8='otuClientCtpTxBeiDayTce'
_A7='otuClientCtpRxBeiDayTce'
_A6='otuClientCtpTxBei15MinutesTce'
_A5='otuClientCtpRxBei15MinutesTce'
_A4='otuClientCtpTermMonitoringMode'
_A3='otuClientCtpFacMonitoringMode'
_A2='otuClientCtpFacDSThreshold'
_A1='otuClientCtpSupportingCircuitIdList'
_A0='otuClientCtpAlarmReportControl'
_z='otuClientCtpTermPmHistStatsEnable'
_y='otuClientCtpFacPmHistStatsEnable'
_x='otuClientCtpLoopback'
_w='otuClientCtpTamType'
_v='otuClientCtpConfiguredServiceType'
_u='otuClientCtpTxDs15MinutesTceReporting'
_t='otuClientCtpTxDsDayTceReporting'
_s='otuClientCtpRxDs15MinutesTceReporting'
_r='otuClientCtpRxDsDayTceReporting'
_q='otuClientCtpTxEb15MinutesTceReporting'
_p='otuClientCtpTxEbDayTceReporting'
_o='otuClientCtpRxEb15MinutesTceReporting'
_n='otuClientCtpRxEbDayTceReporting'
_m='otuClientCtpTxDsDayTce'
_l='otuClientCtpRxDsDayTce'
_k='otuClientCtpTxDs15MinutesTce'
_j='otuClientCtpRxDs15MinutesTce'
_i='otuClientCtpTxEbDayTce'
_h='otuClientCtpRxEbDayTce'
_g='otuClientCtpTxEb15MinutesTce'
_f='otuClientCtpRxEb15MinutesTce'
_e='otuClientCtpFacTimDetMode'
_d='otuClientCtpTermTimDetMode'
_c='otuClientCtpFacReceivedTTI'
_b='otuClientCtpTermReceivedTTI'
_a='otuClientCtpFacExpectedDAPI'
_Z='otuClientCtpFacExpectedSAPI'
_Y='otuClientCtpFacTxTTI'
_X='otuClientCtpTermExpectedDAPI'
_W='otuClientCtpTermExpectedSAPI'
_V='otuClientCtpTermTxTTI'
_U='otuClientCtpFecEnabled'
_T='otuClientCtpFecCorrection'
_S='otuClientCtpServiceModeQualifier'
_R='otuClientCtpServiceMode'
_Q='otuClientCtpFacPrbsMonMode'
_P='otuClientCtpFacPrbsGenMode'
_O='sapidapi'
_N='InfnServiceMode'
_M='InfnSMQ'
_L='InfnLoopbackType'
_K='InfnArc'
_J='ifIndex'
_I='IF-MIB'
_H='read-only'
_G='DisplayString'
_F='InfnEnableDisable'
_E='TruthValue'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-OTUCLIENTCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnArc,InfnEnableDisable,InfnEqptType,InfnLoopbackType,InfnMonitoringMode,InfnSMQ,InfnServiceMode,InfnServiceType=mibBuilder.importSymbols('INFINERA-TC-MIB',_K,_F,'InfnEqptType',_L,'InfnMonitoringMode',_M,_N,'InfnServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention',_E)
otuClientCtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,25))
if mibBuilder.loadTexts:otuClientCtpMIB.setRevisions(('2009-04-20 00:00',))
_OtuClientCtpTable_Object=MibTable
otuClientCtpTable=_OtuClientCtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1))
if mibBuilder.loadTexts:otuClientCtpTable.setStatus(_A)
_OtuClientCtpEntry_Object=MibTableRow
otuClientCtpEntry=_OtuClientCtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1))
otuClientCtpEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:otuClientCtpEntry.setStatus(_A)
class _OtuClientCtpFacPrbsGenMode_Type(InfnEnableDisable):defaultValue=1
_OtuClientCtpFacPrbsGenMode_Type.__name__=_F
_OtuClientCtpFacPrbsGenMode_Object=MibTableColumn
otuClientCtpFacPrbsGenMode=_OtuClientCtpFacPrbsGenMode_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,1),_OtuClientCtpFacPrbsGenMode_Type())
otuClientCtpFacPrbsGenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFacPrbsGenMode.setStatus(_A)
class _OtuClientCtpFacPrbsMonMode_Type(InfnEnableDisable):defaultValue=1
_OtuClientCtpFacPrbsMonMode_Type.__name__=_F
_OtuClientCtpFacPrbsMonMode_Object=MibTableColumn
otuClientCtpFacPrbsMonMode=_OtuClientCtpFacPrbsMonMode_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,2),_OtuClientCtpFacPrbsMonMode_Type())
otuClientCtpFacPrbsMonMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFacPrbsMonMode.setStatus(_A)
class _OtuClientCtpServiceMode_Type(InfnServiceMode):defaultValue=1
_OtuClientCtpServiceMode_Type.__name__=_N
_OtuClientCtpServiceMode_Object=MibTableColumn
otuClientCtpServiceMode=_OtuClientCtpServiceMode_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,3),_OtuClientCtpServiceMode_Type())
otuClientCtpServiceMode.setMaxAccess(_H)
if mibBuilder.loadTexts:otuClientCtpServiceMode.setStatus(_A)
class _OtuClientCtpServiceModeQualifier_Type(InfnSMQ):defaultValue=1
_OtuClientCtpServiceModeQualifier_Type.__name__=_M
_OtuClientCtpServiceModeQualifier_Object=MibTableColumn
otuClientCtpServiceModeQualifier=_OtuClientCtpServiceModeQualifier_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,4),_OtuClientCtpServiceModeQualifier_Type())
otuClientCtpServiceModeQualifier.setMaxAccess(_H)
if mibBuilder.loadTexts:otuClientCtpServiceModeQualifier.setStatus(_A)
class _OtuClientCtpFecCorrection_Type(InfnEnableDisable):defaultValue=2
_OtuClientCtpFecCorrection_Type.__name__=_F
_OtuClientCtpFecCorrection_Object=MibTableColumn
otuClientCtpFecCorrection=_OtuClientCtpFecCorrection_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,5),_OtuClientCtpFecCorrection_Type())
otuClientCtpFecCorrection.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFecCorrection.setStatus(_A)
class _OtuClientCtpFecEnabled_Type(InfnEnableDisable):defaultValue=2
_OtuClientCtpFecEnabled_Type.__name__=_F
_OtuClientCtpFecEnabled_Object=MibTableColumn
otuClientCtpFecEnabled=_OtuClientCtpFecEnabled_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,6),_OtuClientCtpFecEnabled_Type())
otuClientCtpFecEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFecEnabled.setStatus(_A)
class _OtuClientCtpTermTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OtuClientCtpTermTxTTI_Type.__name__=_G
_OtuClientCtpTermTxTTI_Object=MibTableColumn
otuClientCtpTermTxTTI=_OtuClientCtpTermTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,7),_OtuClientCtpTermTxTTI_Type())
otuClientCtpTermTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTermTxTTI.setStatus(_A)
class _OtuClientCtpTermExpectedSAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OtuClientCtpTermExpectedSAPI_Type.__name__=_G
_OtuClientCtpTermExpectedSAPI_Object=MibTableColumn
otuClientCtpTermExpectedSAPI=_OtuClientCtpTermExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,8),_OtuClientCtpTermExpectedSAPI_Type())
otuClientCtpTermExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTermExpectedSAPI.setStatus(_A)
class _OtuClientCtpTermExpectedDAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OtuClientCtpTermExpectedDAPI_Type.__name__=_G
_OtuClientCtpTermExpectedDAPI_Object=MibTableColumn
otuClientCtpTermExpectedDAPI=_OtuClientCtpTermExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,9),_OtuClientCtpTermExpectedDAPI_Type())
otuClientCtpTermExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTermExpectedDAPI.setStatus(_A)
class _OtuClientCtpFacTxTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OtuClientCtpFacTxTTI_Type.__name__=_G
_OtuClientCtpFacTxTTI_Object=MibTableColumn
otuClientCtpFacTxTTI=_OtuClientCtpFacTxTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,10),_OtuClientCtpFacTxTTI_Type())
otuClientCtpFacTxTTI.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFacTxTTI.setStatus(_A)
class _OtuClientCtpFacExpectedSAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OtuClientCtpFacExpectedSAPI_Type.__name__=_G
_OtuClientCtpFacExpectedSAPI_Object=MibTableColumn
otuClientCtpFacExpectedSAPI=_OtuClientCtpFacExpectedSAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,11),_OtuClientCtpFacExpectedSAPI_Type())
otuClientCtpFacExpectedSAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFacExpectedSAPI.setStatus(_A)
class _OtuClientCtpFacExpectedDAPI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_OtuClientCtpFacExpectedDAPI_Type.__name__=_G
_OtuClientCtpFacExpectedDAPI_Object=MibTableColumn
otuClientCtpFacExpectedDAPI=_OtuClientCtpFacExpectedDAPI_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,12),_OtuClientCtpFacExpectedDAPI_Type())
otuClientCtpFacExpectedDAPI.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFacExpectedDAPI.setStatus(_A)
class _OtuClientCtpTermReceivedTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OtuClientCtpTermReceivedTTI_Type.__name__=_G
_OtuClientCtpTermReceivedTTI_Object=MibTableColumn
otuClientCtpTermReceivedTTI=_OtuClientCtpTermReceivedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,13),_OtuClientCtpTermReceivedTTI_Type())
otuClientCtpTermReceivedTTI.setMaxAccess(_H)
if mibBuilder.loadTexts:otuClientCtpTermReceivedTTI.setStatus(_A)
class _OtuClientCtpFacReceivedTTI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_OtuClientCtpFacReceivedTTI_Type.__name__=_G
_OtuClientCtpFacReceivedTTI_Object=MibTableColumn
otuClientCtpFacReceivedTTI=_OtuClientCtpFacReceivedTTI_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,14),_OtuClientCtpFacReceivedTTI_Type())
otuClientCtpFacReceivedTTI.setMaxAccess(_H)
if mibBuilder.loadTexts:otuClientCtpFacReceivedTTI.setStatus(_A)
class _OtuClientCtpRxEb15MinutesTce_Type(Integer32):defaultValue=1500
_OtuClientCtpRxEb15MinutesTce_Type.__name__=_D
_OtuClientCtpRxEb15MinutesTce_Object=MibTableColumn
otuClientCtpRxEb15MinutesTce=_OtuClientCtpRxEb15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,15),_OtuClientCtpRxEb15MinutesTce_Type())
otuClientCtpRxEb15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxEb15MinutesTce.setStatus(_A)
class _OtuClientCtpTxEb15MinutesTce_Type(Integer32):defaultValue=1500
_OtuClientCtpTxEb15MinutesTce_Type.__name__=_D
_OtuClientCtpTxEb15MinutesTce_Object=MibTableColumn
otuClientCtpTxEb15MinutesTce=_OtuClientCtpTxEb15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,16),_OtuClientCtpTxEb15MinutesTce_Type())
otuClientCtpTxEb15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxEb15MinutesTce.setStatus(_A)
class _OtuClientCtpRxEbDayTce_Type(Integer32):defaultValue=15000
_OtuClientCtpRxEbDayTce_Type.__name__=_D
_OtuClientCtpRxEbDayTce_Object=MibTableColumn
otuClientCtpRxEbDayTce=_OtuClientCtpRxEbDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,17),_OtuClientCtpRxEbDayTce_Type())
otuClientCtpRxEbDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxEbDayTce.setStatus(_A)
class _OtuClientCtpTxEbDayTce_Type(Integer32):defaultValue=15000
_OtuClientCtpTxEbDayTce_Type.__name__=_D
_OtuClientCtpTxEbDayTce_Object=MibTableColumn
otuClientCtpTxEbDayTce=_OtuClientCtpTxEbDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,18),_OtuClientCtpTxEbDayTce_Type())
otuClientCtpTxEbDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxEbDayTce.setStatus(_A)
class _OtuClientCtpRxDs15MinutesTce_Type(Integer32):defaultValue=120
_OtuClientCtpRxDs15MinutesTce_Type.__name__=_D
_OtuClientCtpRxDs15MinutesTce_Object=MibTableColumn
otuClientCtpRxDs15MinutesTce=_OtuClientCtpRxDs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,19),_OtuClientCtpRxDs15MinutesTce_Type())
otuClientCtpRxDs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxDs15MinutesTce.setStatus(_A)
class _OtuClientCtpTxDs15MinutesTce_Type(Integer32):defaultValue=120
_OtuClientCtpTxDs15MinutesTce_Type.__name__=_D
_OtuClientCtpTxDs15MinutesTce_Object=MibTableColumn
otuClientCtpTxDs15MinutesTce=_OtuClientCtpTxDs15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,20),_OtuClientCtpTxDs15MinutesTce_Type())
otuClientCtpTxDs15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxDs15MinutesTce.setStatus(_A)
class _OtuClientCtpRxDsDayTce_Type(Integer32):defaultValue=1200
_OtuClientCtpRxDsDayTce_Type.__name__=_D
_OtuClientCtpRxDsDayTce_Object=MibTableColumn
otuClientCtpRxDsDayTce=_OtuClientCtpRxDsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,21),_OtuClientCtpRxDsDayTce_Type())
otuClientCtpRxDsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxDsDayTce.setStatus(_A)
class _OtuClientCtpTxDsDayTce_Type(Integer32):defaultValue=1200
_OtuClientCtpTxDsDayTce_Type.__name__=_D
_OtuClientCtpTxDsDayTce_Object=MibTableColumn
otuClientCtpTxDsDayTce=_OtuClientCtpTxDsDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,22),_OtuClientCtpTxDsDayTce_Type())
otuClientCtpTxDsDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxDsDayTce.setStatus(_A)
class _OtuClientCtpRxEbDayTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpRxEbDayTceReporting_Type.__name__=_E
_OtuClientCtpRxEbDayTceReporting_Object=MibTableColumn
otuClientCtpRxEbDayTceReporting=_OtuClientCtpRxEbDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,23),_OtuClientCtpRxEbDayTceReporting_Type())
otuClientCtpRxEbDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxEbDayTceReporting.setStatus(_A)
class _OtuClientCtpRxEb15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpRxEb15MinutesTceReporting_Type.__name__=_E
_OtuClientCtpRxEb15MinutesTceReporting_Object=MibTableColumn
otuClientCtpRxEb15MinutesTceReporting=_OtuClientCtpRxEb15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,24),_OtuClientCtpRxEb15MinutesTceReporting_Type())
otuClientCtpRxEb15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxEb15MinutesTceReporting.setStatus(_A)
class _OtuClientCtpTxEbDayTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpTxEbDayTceReporting_Type.__name__=_E
_OtuClientCtpTxEbDayTceReporting_Object=MibTableColumn
otuClientCtpTxEbDayTceReporting=_OtuClientCtpTxEbDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,25),_OtuClientCtpTxEbDayTceReporting_Type())
otuClientCtpTxEbDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxEbDayTceReporting.setStatus(_A)
class _OtuClientCtpTxEb15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpTxEb15MinutesTceReporting_Type.__name__=_E
_OtuClientCtpTxEb15MinutesTceReporting_Object=MibTableColumn
otuClientCtpTxEb15MinutesTceReporting=_OtuClientCtpTxEb15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,26),_OtuClientCtpTxEb15MinutesTceReporting_Type())
otuClientCtpTxEb15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxEb15MinutesTceReporting.setStatus(_A)
class _OtuClientCtpRxDsDayTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpRxDsDayTceReporting_Type.__name__=_E
_OtuClientCtpRxDsDayTceReporting_Object=MibTableColumn
otuClientCtpRxDsDayTceReporting=_OtuClientCtpRxDsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,27),_OtuClientCtpRxDsDayTceReporting_Type())
otuClientCtpRxDsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxDsDayTceReporting.setStatus(_A)
class _OtuClientCtpRxDs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpRxDs15MinutesTceReporting_Type.__name__=_E
_OtuClientCtpRxDs15MinutesTceReporting_Object=MibTableColumn
otuClientCtpRxDs15MinutesTceReporting=_OtuClientCtpRxDs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,28),_OtuClientCtpRxDs15MinutesTceReporting_Type())
otuClientCtpRxDs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxDs15MinutesTceReporting.setStatus(_A)
class _OtuClientCtpTxDsDayTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpTxDsDayTceReporting_Type.__name__=_E
_OtuClientCtpTxDsDayTceReporting_Object=MibTableColumn
otuClientCtpTxDsDayTceReporting=_OtuClientCtpTxDsDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,29),_OtuClientCtpTxDsDayTceReporting_Type())
otuClientCtpTxDsDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxDsDayTceReporting.setStatus(_A)
class _OtuClientCtpTxDs15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpTxDs15MinutesTceReporting_Type.__name__=_E
_OtuClientCtpTxDs15MinutesTceReporting_Object=MibTableColumn
otuClientCtpTxDs15MinutesTceReporting=_OtuClientCtpTxDs15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,30),_OtuClientCtpTxDs15MinutesTceReporting_Type())
otuClientCtpTxDs15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxDs15MinutesTceReporting.setStatus(_A)
class _OtuClientCtpTermTimDetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),(_O,4)))
_OtuClientCtpTermTimDetMode_Type.__name__=_D
_OtuClientCtpTermTimDetMode_Object=MibTableColumn
otuClientCtpTermTimDetMode=_OtuClientCtpTermTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,31),_OtuClientCtpTermTimDetMode_Type())
otuClientCtpTermTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTermTimDetMode.setStatus(_A)
class _OtuClientCtpFacTimDetMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('sapi',2),('dapi',3),(_O,4)))
_OtuClientCtpFacTimDetMode_Type.__name__=_D
_OtuClientCtpFacTimDetMode_Object=MibTableColumn
otuClientCtpFacTimDetMode=_OtuClientCtpFacTimDetMode_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,32),_OtuClientCtpFacTimDetMode_Type())
otuClientCtpFacTimDetMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFacTimDetMode.setStatus(_A)
_OtuClientCtpConfiguredServiceType_Type=InfnServiceType
_OtuClientCtpConfiguredServiceType_Object=MibTableColumn
otuClientCtpConfiguredServiceType=_OtuClientCtpConfiguredServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,33),_OtuClientCtpConfiguredServiceType_Type())
otuClientCtpConfiguredServiceType.setMaxAccess(_H)
if mibBuilder.loadTexts:otuClientCtpConfiguredServiceType.setStatus(_A)
_OtuClientCtpTamType_Type=InfnEqptType
_OtuClientCtpTamType_Object=MibTableColumn
otuClientCtpTamType=_OtuClientCtpTamType_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,34),_OtuClientCtpTamType_Type())
otuClientCtpTamType.setMaxAccess(_H)
if mibBuilder.loadTexts:otuClientCtpTamType.setStatus('obsolete')
class _OtuClientCtpLoopback_Type(InfnLoopbackType):defaultValue=1
_OtuClientCtpLoopback_Type.__name__=_L
_OtuClientCtpLoopback_Object=MibTableColumn
otuClientCtpLoopback=_OtuClientCtpLoopback_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,35),_OtuClientCtpLoopback_Type())
otuClientCtpLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpLoopback.setStatus(_A)
class _OtuClientCtpFacPmHistStatsEnable_Type(InfnEnableDisable):defaultValue=2
_OtuClientCtpFacPmHistStatsEnable_Type.__name__=_F
_OtuClientCtpFacPmHistStatsEnable_Object=MibTableColumn
otuClientCtpFacPmHistStatsEnable=_OtuClientCtpFacPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,36),_OtuClientCtpFacPmHistStatsEnable_Type())
otuClientCtpFacPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFacPmHistStatsEnable.setStatus(_A)
class _OtuClientCtpTermPmHistStatsEnable_Type(InfnEnableDisable):defaultValue=2
_OtuClientCtpTermPmHistStatsEnable_Type.__name__=_F
_OtuClientCtpTermPmHistStatsEnable_Object=MibTableColumn
otuClientCtpTermPmHistStatsEnable=_OtuClientCtpTermPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,37),_OtuClientCtpTermPmHistStatsEnable_Type())
otuClientCtpTermPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTermPmHistStatsEnable.setStatus(_A)
class _OtuClientCtpAlarmReportControl_Type(InfnArc):defaultValue=1
_OtuClientCtpAlarmReportControl_Type.__name__=_K
_OtuClientCtpAlarmReportControl_Object=MibTableColumn
otuClientCtpAlarmReportControl=_OtuClientCtpAlarmReportControl_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,38),_OtuClientCtpAlarmReportControl_Type())
otuClientCtpAlarmReportControl.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpAlarmReportControl.setStatus(_A)
_OtuClientCtpSupportingCircuitIdList_Type=DisplayString
_OtuClientCtpSupportingCircuitIdList_Object=MibTableColumn
otuClientCtpSupportingCircuitIdList=_OtuClientCtpSupportingCircuitIdList_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,39),_OtuClientCtpSupportingCircuitIdList_Type())
otuClientCtpSupportingCircuitIdList.setMaxAccess(_H)
if mibBuilder.loadTexts:otuClientCtpSupportingCircuitIdList.setStatus(_A)
class _OtuClientCtpFacDSThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OtuClientCtpFacDSThreshold_Type.__name__=_D
_OtuClientCtpFacDSThreshold_Object=MibTableColumn
otuClientCtpFacDSThreshold=_OtuClientCtpFacDSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,40),_OtuClientCtpFacDSThreshold_Type())
otuClientCtpFacDSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFacDSThreshold.setStatus(_A)
class _OtuClientCtpTermDSThreshold_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OtuClientCtpTermDSThreshold_Type.__name__=_D
_OtuClientCtpTermDSThreshold_Object=MibTableColumn
otuClientCtpTermDSThreshold=_OtuClientCtpTermDSThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,41),_OtuClientCtpTermDSThreshold_Type())
otuClientCtpTermDSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTermDSThreshold.setStatus(_A)
class _OtuClientCtpTermPrbsGenMode_Type(InfnEnableDisable):defaultValue=1
_OtuClientCtpTermPrbsGenMode_Type.__name__=_F
_OtuClientCtpTermPrbsGenMode_Object=MibTableColumn
otuClientCtpTermPrbsGenMode=_OtuClientCtpTermPrbsGenMode_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,42),_OtuClientCtpTermPrbsGenMode_Type())
otuClientCtpTermPrbsGenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTermPrbsGenMode.setStatus(_A)
class _OtuClientCtpTermPrbsMonMode_Type(InfnEnableDisable):defaultValue=1
_OtuClientCtpTermPrbsMonMode_Type.__name__=_F
_OtuClientCtpTermPrbsMonMode_Object=MibTableColumn
otuClientCtpTermPrbsMonMode=_OtuClientCtpTermPrbsMonMode_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,43),_OtuClientCtpTermPrbsMonMode_Type())
otuClientCtpTermPrbsMonMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTermPrbsMonMode.setStatus(_A)
_OtuClientCtpFacMonitoringMode_Type=InfnMonitoringMode
_OtuClientCtpFacMonitoringMode_Object=MibTableColumn
otuClientCtpFacMonitoringMode=_OtuClientCtpFacMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,44),_OtuClientCtpFacMonitoringMode_Type())
otuClientCtpFacMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpFacMonitoringMode.setStatus(_A)
_OtuClientCtpTermMonitoringMode_Type=InfnMonitoringMode
_OtuClientCtpTermMonitoringMode_Object=MibTableColumn
otuClientCtpTermMonitoringMode=_OtuClientCtpTermMonitoringMode_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,45),_OtuClientCtpTermMonitoringMode_Type())
otuClientCtpTermMonitoringMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTermMonitoringMode.setStatus(_A)
class _OtuClientCtpRxBei15MinutesTce_Type(Integer32):defaultValue=1500
_OtuClientCtpRxBei15MinutesTce_Type.__name__=_D
_OtuClientCtpRxBei15MinutesTce_Object=MibTableColumn
otuClientCtpRxBei15MinutesTce=_OtuClientCtpRxBei15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,46),_OtuClientCtpRxBei15MinutesTce_Type())
otuClientCtpRxBei15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxBei15MinutesTce.setStatus(_A)
class _OtuClientCtpTxBei15MinutesTce_Type(Integer32):defaultValue=1500
_OtuClientCtpTxBei15MinutesTce_Type.__name__=_D
_OtuClientCtpTxBei15MinutesTce_Object=MibTableColumn
otuClientCtpTxBei15MinutesTce=_OtuClientCtpTxBei15MinutesTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,47),_OtuClientCtpTxBei15MinutesTce_Type())
otuClientCtpTxBei15MinutesTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxBei15MinutesTce.setStatus(_A)
class _OtuClientCtpRxBeiDayTce_Type(Integer32):defaultValue=15000
_OtuClientCtpRxBeiDayTce_Type.__name__=_D
_OtuClientCtpRxBeiDayTce_Object=MibTableColumn
otuClientCtpRxBeiDayTce=_OtuClientCtpRxBeiDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,48),_OtuClientCtpRxBeiDayTce_Type())
otuClientCtpRxBeiDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxBeiDayTce.setStatus(_A)
class _OtuClientCtpTxBeiDayTce_Type(Integer32):defaultValue=15000
_OtuClientCtpTxBeiDayTce_Type.__name__=_D
_OtuClientCtpTxBeiDayTce_Object=MibTableColumn
otuClientCtpTxBeiDayTce=_OtuClientCtpTxBeiDayTce_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,49),_OtuClientCtpTxBeiDayTce_Type())
otuClientCtpTxBeiDayTce.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxBeiDayTce.setStatus(_A)
class _OtuClientCtpRxBeiDayTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpRxBeiDayTceReporting_Type.__name__=_E
_OtuClientCtpRxBeiDayTceReporting_Object=MibTableColumn
otuClientCtpRxBeiDayTceReporting=_OtuClientCtpRxBeiDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,50),_OtuClientCtpRxBeiDayTceReporting_Type())
otuClientCtpRxBeiDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxBeiDayTceReporting.setStatus(_A)
class _OtuClientCtpRxBei15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpRxBei15MinutesTceReporting_Type.__name__=_E
_OtuClientCtpRxBei15MinutesTceReporting_Object=MibTableColumn
otuClientCtpRxBei15MinutesTceReporting=_OtuClientCtpRxBei15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,51),_OtuClientCtpRxBei15MinutesTceReporting_Type())
otuClientCtpRxBei15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpRxBei15MinutesTceReporting.setStatus(_A)
class _OtuClientCtpTxBeiDayTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpTxBeiDayTceReporting_Type.__name__=_E
_OtuClientCtpTxBeiDayTceReporting_Object=MibTableColumn
otuClientCtpTxBeiDayTceReporting=_OtuClientCtpTxBeiDayTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,52),_OtuClientCtpTxBeiDayTceReporting_Type())
otuClientCtpTxBeiDayTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxBeiDayTceReporting.setStatus(_A)
class _OtuClientCtpTxBei15MinutesTceReporting_Type(TruthValue):defaultValue=2
_OtuClientCtpTxBei15MinutesTceReporting_Type.__name__=_E
_OtuClientCtpTxBei15MinutesTceReporting_Object=MibTableColumn
otuClientCtpTxBei15MinutesTceReporting=_OtuClientCtpTxBei15MinutesTceReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,25,1,1,53),_OtuClientCtpTxBei15MinutesTceReporting_Type())
otuClientCtpTxBei15MinutesTceReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:otuClientCtpTxBei15MinutesTceReporting.setStatus(_A)
_OtuClientCtpConformance_ObjectIdentity=ObjectIdentity
otuClientCtpConformance=_OtuClientCtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,25,3))
_OtuClientCtpCompliances_ObjectIdentity=ObjectIdentity
otuClientCtpCompliances=_OtuClientCtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,25,3,1))
_OtuClientCtpGroups_ObjectIdentity=ObjectIdentity
otuClientCtpGroups=_OtuClientCtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,25,3,2))
otuClientCtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,25,3,2,1))
otuClientCtpGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:otuClientCtpGroup.setStatus(_A)
otuClientCtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,25,3,1,1))
otuClientCtpCompliance.setObjects((_B,_AD))
if mibBuilder.loadTexts:otuClientCtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otuClientCtpMIB':otuClientCtpMIB,'otuClientCtpTable':otuClientCtpTable,'otuClientCtpEntry':otuClientCtpEntry,_P:otuClientCtpFacPrbsGenMode,_Q:otuClientCtpFacPrbsMonMode,_R:otuClientCtpServiceMode,_S:otuClientCtpServiceModeQualifier,_T:otuClientCtpFecCorrection,_U:otuClientCtpFecEnabled,_V:otuClientCtpTermTxTTI,_W:otuClientCtpTermExpectedSAPI,_X:otuClientCtpTermExpectedDAPI,_Y:otuClientCtpFacTxTTI,_Z:otuClientCtpFacExpectedSAPI,_a:otuClientCtpFacExpectedDAPI,_b:otuClientCtpTermReceivedTTI,_c:otuClientCtpFacReceivedTTI,_f:otuClientCtpRxEb15MinutesTce,_g:otuClientCtpTxEb15MinutesTce,_h:otuClientCtpRxEbDayTce,_i:otuClientCtpTxEbDayTce,_j:otuClientCtpRxDs15MinutesTce,_k:otuClientCtpTxDs15MinutesTce,_l:otuClientCtpRxDsDayTce,_m:otuClientCtpTxDsDayTce,_n:otuClientCtpRxEbDayTceReporting,_o:otuClientCtpRxEb15MinutesTceReporting,_p:otuClientCtpTxEbDayTceReporting,_q:otuClientCtpTxEb15MinutesTceReporting,_r:otuClientCtpRxDsDayTceReporting,_s:otuClientCtpRxDs15MinutesTceReporting,_t:otuClientCtpTxDsDayTceReporting,_u:otuClientCtpTxDs15MinutesTceReporting,_d:otuClientCtpTermTimDetMode,_e:otuClientCtpFacTimDetMode,_v:otuClientCtpConfiguredServiceType,_w:otuClientCtpTamType,_x:otuClientCtpLoopback,_y:otuClientCtpFacPmHistStatsEnable,_z:otuClientCtpTermPmHistStatsEnable,_A0:otuClientCtpAlarmReportControl,_A1:otuClientCtpSupportingCircuitIdList,_A2:otuClientCtpFacDSThreshold,'otuClientCtpTermDSThreshold':otuClientCtpTermDSThreshold,'otuClientCtpTermPrbsGenMode':otuClientCtpTermPrbsGenMode,'otuClientCtpTermPrbsMonMode':otuClientCtpTermPrbsMonMode,_A3:otuClientCtpFacMonitoringMode,_A4:otuClientCtpTermMonitoringMode,_A5:otuClientCtpRxBei15MinutesTce,_A6:otuClientCtpTxBei15MinutesTce,_A7:otuClientCtpRxBeiDayTce,_A8:otuClientCtpTxBeiDayTce,_A9:otuClientCtpRxBeiDayTceReporting,_AA:otuClientCtpRxBei15MinutesTceReporting,_AB:otuClientCtpTxBeiDayTceReporting,_AC:otuClientCtpTxBei15MinutesTceReporting,'otuClientCtpConformance':otuClientCtpConformance,'otuClientCtpCompliances':otuClientCtpCompliances,'otuClientCtpCompliance':otuClientCtpCompliance,'otuClientCtpGroups':otuClientCtpGroups,_AD:otuClientCtpGroup})