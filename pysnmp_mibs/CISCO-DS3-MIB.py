_B6='ciscoDs3Previous24HrGroup'
_B5='ciscoPlcpCounterMIBGroup'
_B4='ciscoDs3AlarmMIBGroup'
_B3='cds3StatsMIBGroup'
_B2='ciscoDs3ConfMIBGroup'
_B1='cds3LSESPrevious24Hr'
_B0='cds3CSESPrevious24Hr'
_A_='cds3CESPrevious24Hr'
_Az='cds3CCVPrevious24Hr'
_Ay='cds3UASPrevious24Hr'
_Ax='cds3SEFSPrevious24Hr'
_Aw='cds3PSESPrevious24Hr'
_Av='cds3PESPrevious24Hr'
_Au='cds3PCVPrevious24Hr'
_At='cds3LESPrevious24Hr'
_As='cds3LCVPrevious24Hr'
_Ar='cds3PlcpUAS24HrBucket'
_Aq='cds3PlcpUASCurrent'
_Ap='cds3PlcpSEFS24HrBucket'
_Ao='cds3PlcpSEFSCurrent'
_An='cds3PlcpBip8SES24HrBucket'
_Am='cds3PlcpBip8SESCurrent'
_Al='cds3PlcpBip8ES24HrBucket'
_Ak='cds3PlcpBip8ESCurrent'
_Aj='cds3PlcpBip8CV24HrBucket'
_Ai='cds3PlcpBip8CVCurrent'
_Ah='cds3PlcpLineStatisticalAlarmState'
_Ag='cds3PlcpLineAlarmState'
_Af='cds3PlcpUAS24HrThreshold'
_Ae='cds3PlcpUAS15MinThreshold'
_Ad='cds3PlcpSEFS24HrThreshold'
_Ac='cds3PlcpSEFS15MinThreshold'
_Ab='cds3PlcpBip8SES24HrThreshold'
_Aa='cds3PlcpBip8SES15MinThreshold'
_AZ='cds3PlcpBip8ES24HrThreshold'
_AY='cds3PlcpBip8ES15MinThreshold'
_AX='cds3PlcpBip8CV24HrThreshold'
_AW='cds3PlcpBip8CV15MinThreshold'
_AV='cds3PlcpStatisticalAlarmSeverity'
_AU='cds3PlcpSEFEBESecCount'
_AT='cds3PlcpFEBESecCount'
_AS='cds3PlcpFEBECount'
_AR='cds3PlcpSEFSecCount'
_AQ='cds3PlcpFESecCount'
_AP='cds3PlcpFECount'
_AO='cds3PlcpRcvRAICount'
_AN='cds3PlcpRcvOOFCount'
_AM='cds3PlcpRcvBip8Count'
_AL='cds3LSESCurrent24Hr'
_AK='cds3CSESCurrent24Hr'
_AJ='cds3CESCurrent24Hr'
_AI='cds3CCVCurrent24Hr'
_AH='cds3UASCurrent24Hr'
_AG='cds3SEFSCurrent24Hr'
_AF='cds3PSESCurrent24Hr'
_AE='cds3PESCurrent24Hr'
_AD='cds3PCVCurrent24Hr'
_AC='cds3LESCurrent24Hr'
_AB='cds3LCVCurrent24Hr'
_AA='cds3IntervalLSESs'
_A9='cds3LineStatisticalAlarmState'
_A8='cds3LSES24HrThreshold'
_A7='cds3LSES15MinThreshold'
_A6='cds3CSES24HrThreshold'
_A5='cds3CSES15MinThreshold'
_A4='cds3CES24HrThreshold'
_A3='cds3CES15MinThreshold'
_A2='cds3CCV24HrThreshold'
_A1='cds3CCV15MinThreshold'
_A0='cds3UAS24HrThreshold'
_z='cds3UAS15MinThreshold'
_y='cds3SEFS24HrThreshold'
_x='cds3SEFS15MinThreshold'
_w='cds3PSES24HrThreshold'
_v='cds3PSES15MinThreshold'
_u='cds3PES24HrThreshold'
_t='cds3PES15MinThreshold'
_s='cds3PCV24HrThreshold'
_r='cds3PCV15MinThreshold'
_q='cds3LES24HrThreshold'
_p='cds3LES15MinThreshold'
_o='cds3LCV24HrThreshold'
_n='cds3LCV15MinThreshold'
_m='cds3StatisticalAlarmSeverity'
_l='cds3FEAlarmThreshold'
_k='cds3FEAlarmDownCount'
_j='cds3FEAlarmUpCount'
_i='cds3NEAlarmThreshold'
_h='cds3NEAlarmDownCount'
_g='cds3NEAlarmUpCount'
_f='cds3RcvAISCount'
_e='cds3FEBECount'
_d='cds3CPECount'
_c='cds3PCVCount'
_b='cds3LCVCount'
_a='cds3EXZSCount'
_Z='cds3FECount'
_Y='cds3CCVCount'
_X='cds3RAICount'
_W='cds3RcvOOFCount'
_V='cds3RcvLOSCount'
_U='cds3FarEndLineLoopbackStatus'
_T='cds3NearEndLineLoopbackStatus'
_S='cds3InternalEqualizer'
_R='cds3TraceAlarm'
_Q='cds3TraceToExpect'
_P='cds3TraceToTransmit'
_O='cds3LineOOFCriteria'
_N='cds3LineRcvFEACValidation'
_M='cds3LineAIScBitsCheck'
_L='cds3LineType'
_K='notApplicable'
_J='cds3IntervalNumber'
_I='DisplayString'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='CISCO-DS3-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
ciscoDs3MIB=ModuleIdentity((1,3,6,1,4,1,9,9,132))
if mibBuilder.loadTexts:ciscoDs3MIB.setRevisions(('2002-05-21 00:00','2001-08-31 00:00','2000-10-10 00:00','2000-02-28 00:00'))
_CiscoDs3MIBObjects_ObjectIdentity=ObjectIdentity
ciscoDs3MIBObjects=_CiscoDs3MIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,132,1))
_Cds3Config_ObjectIdentity=ObjectIdentity
cds3Config=_Cds3Config_ObjectIdentity((1,3,6,1,4,1,9,9,132,1,1))
_Cds3ConfigTable_Object=MibTable
cds3ConfigTable=_Cds3ConfigTable_Object((1,3,6,1,4,1,9,9,132,1,1,1))
if mibBuilder.loadTexts:cds3ConfigTable.setStatus(_A)
_Cds3ConfigEntry_Object=MibTableRow
cds3ConfigEntry=_Cds3ConfigEntry_Object((1,3,6,1,4,1,9,9,132,1,1,1,1))
cds3ConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cds3ConfigEntry.setStatus(_A)
class _Cds3LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('ds3cbitadm',1),('ds3cbitplcp',2),('e3g832adm',3),('e3g751adm',4),('e3g751plcp',5),('ds3m23adm',6),('ds3m23plcp',7),('other',8),('dsx3M23',9),('dsx3SYNTRAN',10),('dsx3CbitParity',11),('dsx3ClearChannel',12),('e3Framed',13),('e3Plcp',14),('ds3cbitfrmronly',15),('ds3m23frmronly',16),('e3g832frmronly',17),('e3g751frmronly',18)))
_Cds3LineType_Type.__name__=_H
_Cds3LineType_Object=MibTableColumn
cds3LineType=_Cds3LineType_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,1),_Cds3LineType_Type())
cds3LineType.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LineType.setStatus(_A)
class _Cds3LineAIScBitsCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('check',1),('ignore',2),(_K,3)))
_Cds3LineAIScBitsCheck_Type.__name__=_H
_Cds3LineAIScBitsCheck_Object=MibTableColumn
cds3LineAIScBitsCheck=_Cds3LineAIScBitsCheck_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,2),_Cds3LineAIScBitsCheck_Type())
cds3LineAIScBitsCheck.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LineAIScBitsCheck.setStatus(_A)
class _Cds3LineRcvFEACValidation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fEACCodes4Of5',1),('fEACCodes8Of10',2),('disable',3)))
_Cds3LineRcvFEACValidation_Type.__name__=_H
_Cds3LineRcvFEACValidation_Object=MibTableColumn
cds3LineRcvFEACValidation=_Cds3LineRcvFEACValidation_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,3),_Cds3LineRcvFEACValidation_Type())
cds3LineRcvFEACValidation.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LineRcvFEACValidation.setStatus(_A)
class _Cds3LineOOFCriteria_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('bits3Of8',1),('bits3Of16',2),(_K,3)))
_Cds3LineOOFCriteria_Type.__name__=_H
_Cds3LineOOFCriteria_Object=MibTableColumn
cds3LineOOFCriteria=_Cds3LineOOFCriteria_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,4),_Cds3LineOOFCriteria_Type())
cds3LineOOFCriteria.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LineOOFCriteria.setStatus(_A)
class _Cds3TraceToTransmit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Cds3TraceToTransmit_Type.__name__=_I
_Cds3TraceToTransmit_Object=MibTableColumn
cds3TraceToTransmit=_Cds3TraceToTransmit_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,5),_Cds3TraceToTransmit_Type())
cds3TraceToTransmit.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3TraceToTransmit.setStatus(_A)
class _Cds3TraceToExpect_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_Cds3TraceToExpect_Type.__name__=_I
_Cds3TraceToExpect_Object=MibTableColumn
cds3TraceToExpect=_Cds3TraceToExpect_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,6),_Cds3TraceToExpect_Type())
cds3TraceToExpect.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3TraceToExpect.setStatus(_A)
class _Cds3TraceAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAlarm',1),('traceFailure',2)))
_Cds3TraceAlarm_Type.__name__=_H
_Cds3TraceAlarm_Object=MibTableColumn
cds3TraceAlarm=_Cds3TraceAlarm_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,7),_Cds3TraceAlarm_Type())
cds3TraceAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3TraceAlarm.setStatus(_A)
class _Cds3InternalEqualizer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('use',1),('byPass',2)))
_Cds3InternalEqualizer_Type.__name__=_H
_Cds3InternalEqualizer_Object=MibTableColumn
cds3InternalEqualizer=_Cds3InternalEqualizer_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,8),_Cds3InternalEqualizer_Type())
cds3InternalEqualizer.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3InternalEqualizer.setStatus(_A)
class _Cds3NearEndLineLoopbackStatus_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3NearEndLineLoopbackStatus_Type.__name__=_E
_Cds3NearEndLineLoopbackStatus_Object=MibTableColumn
cds3NearEndLineLoopbackStatus=_Cds3NearEndLineLoopbackStatus_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,9),_Cds3NearEndLineLoopbackStatus_Type())
cds3NearEndLineLoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3NearEndLineLoopbackStatus.setStatus(_A)
class _Cds3FarEndLineLoopbackStatus_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3FarEndLineLoopbackStatus_Type.__name__=_E
_Cds3FarEndLineLoopbackStatus_Object=MibTableColumn
cds3FarEndLineLoopbackStatus=_Cds3FarEndLineLoopbackStatus_Object((1,3,6,1,4,1,9,9,132,1,1,1,1,10),_Cds3FarEndLineLoopbackStatus_Type())
cds3FarEndLineLoopbackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3FarEndLineLoopbackStatus.setStatus(_A)
_Cds3Alarm_ObjectIdentity=ObjectIdentity
cds3Alarm=_Cds3Alarm_ObjectIdentity((1,3,6,1,4,1,9,9,132,1,2))
_Cds3AlarmConfig_ObjectIdentity=ObjectIdentity
cds3AlarmConfig=_Cds3AlarmConfig_ObjectIdentity((1,3,6,1,4,1,9,9,132,1,2,1))
_Cds3AlarmConfigTable_Object=MibTable
cds3AlarmConfigTable=_Cds3AlarmConfigTable_Object((1,3,6,1,4,1,9,9,132,1,2,1,1))
if mibBuilder.loadTexts:cds3AlarmConfigTable.setStatus(_A)
_Cds3AlarmConfigEntry_Object=MibTableRow
cds3AlarmConfigEntry=_Cds3AlarmConfigEntry_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1))
cds3AlarmConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cds3AlarmConfigEntry.setStatus(_A)
class _Cds3NEAlarmUpCount_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3NEAlarmUpCount_Type.__name__=_E
_Cds3NEAlarmUpCount_Object=MibTableColumn
cds3NEAlarmUpCount=_Cds3NEAlarmUpCount_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,1),_Cds3NEAlarmUpCount_Type())
cds3NEAlarmUpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3NEAlarmUpCount.setStatus(_A)
class _Cds3NEAlarmDownCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3NEAlarmDownCount_Type.__name__=_E
_Cds3NEAlarmDownCount_Object=MibTableColumn
cds3NEAlarmDownCount=_Cds3NEAlarmDownCount_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,2),_Cds3NEAlarmDownCount_Type())
cds3NEAlarmDownCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3NEAlarmDownCount.setStatus(_A)
class _Cds3NEAlarmThreshold_Type(Unsigned32):defaultValue=150;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3NEAlarmThreshold_Type.__name__=_E
_Cds3NEAlarmThreshold_Object=MibTableColumn
cds3NEAlarmThreshold=_Cds3NEAlarmThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,3),_Cds3NEAlarmThreshold_Type())
cds3NEAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3NEAlarmThreshold.setStatus(_A)
class _Cds3FEAlarmUpCount_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3FEAlarmUpCount_Type.__name__=_E
_Cds3FEAlarmUpCount_Object=MibTableColumn
cds3FEAlarmUpCount=_Cds3FEAlarmUpCount_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,4),_Cds3FEAlarmUpCount_Type())
cds3FEAlarmUpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3FEAlarmUpCount.setStatus(_A)
class _Cds3FEAlarmDownCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3FEAlarmDownCount_Type.__name__=_E
_Cds3FEAlarmDownCount_Object=MibTableColumn
cds3FEAlarmDownCount=_Cds3FEAlarmDownCount_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,5),_Cds3FEAlarmDownCount_Type())
cds3FEAlarmDownCount.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3FEAlarmDownCount.setStatus(_A)
class _Cds3FEAlarmThreshold_Type(Unsigned32):defaultValue=150;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3FEAlarmThreshold_Type.__name__=_E
_Cds3FEAlarmThreshold_Object=MibTableColumn
cds3FEAlarmThreshold=_Cds3FEAlarmThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,6),_Cds3FEAlarmThreshold_Type())
cds3FEAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3FEAlarmThreshold.setStatus(_A)
class _Cds3StatisticalAlarmSeverity_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('minor',1),('major',2),('none',3)))
_Cds3StatisticalAlarmSeverity_Type.__name__=_H
_Cds3StatisticalAlarmSeverity_Object=MibTableColumn
cds3StatisticalAlarmSeverity=_Cds3StatisticalAlarmSeverity_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,7),_Cds3StatisticalAlarmSeverity_Type())
cds3StatisticalAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3StatisticalAlarmSeverity.setStatus(_A)
class _Cds3LCV15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3LCV15MinThreshold_Type.__name__=_E
_Cds3LCV15MinThreshold_Object=MibTableColumn
cds3LCV15MinThreshold=_Cds3LCV15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,8),_Cds3LCV15MinThreshold_Type())
cds3LCV15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LCV15MinThreshold.setStatus(_A)
class _Cds3LCV24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3LCV24HrThreshold_Type.__name__=_E
_Cds3LCV24HrThreshold_Object=MibTableColumn
cds3LCV24HrThreshold=_Cds3LCV24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,9),_Cds3LCV24HrThreshold_Type())
cds3LCV24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LCV24HrThreshold.setStatus(_A)
class _Cds3LES15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3LES15MinThreshold_Type.__name__=_E
_Cds3LES15MinThreshold_Object=MibTableColumn
cds3LES15MinThreshold=_Cds3LES15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,10),_Cds3LES15MinThreshold_Type())
cds3LES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LES15MinThreshold.setStatus(_A)
class _Cds3LES24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3LES24HrThreshold_Type.__name__=_E
_Cds3LES24HrThreshold_Object=MibTableColumn
cds3LES24HrThreshold=_Cds3LES24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,11),_Cds3LES24HrThreshold_Type())
cds3LES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LES24HrThreshold.setStatus(_A)
class _Cds3PCV15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PCV15MinThreshold_Type.__name__=_E
_Cds3PCV15MinThreshold_Object=MibTableColumn
cds3PCV15MinThreshold=_Cds3PCV15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,12),_Cds3PCV15MinThreshold_Type())
cds3PCV15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PCV15MinThreshold.setStatus(_A)
class _Cds3PCV24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PCV24HrThreshold_Type.__name__=_E
_Cds3PCV24HrThreshold_Object=MibTableColumn
cds3PCV24HrThreshold=_Cds3PCV24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,13),_Cds3PCV24HrThreshold_Type())
cds3PCV24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PCV24HrThreshold.setStatus(_A)
class _Cds3PES15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PES15MinThreshold_Type.__name__=_E
_Cds3PES15MinThreshold_Object=MibTableColumn
cds3PES15MinThreshold=_Cds3PES15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,14),_Cds3PES15MinThreshold_Type())
cds3PES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PES15MinThreshold.setStatus(_A)
class _Cds3PES24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PES24HrThreshold_Type.__name__=_E
_Cds3PES24HrThreshold_Object=MibTableColumn
cds3PES24HrThreshold=_Cds3PES24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,15),_Cds3PES24HrThreshold_Type())
cds3PES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PES24HrThreshold.setStatus(_A)
class _Cds3PSES15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PSES15MinThreshold_Type.__name__=_E
_Cds3PSES15MinThreshold_Object=MibTableColumn
cds3PSES15MinThreshold=_Cds3PSES15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,16),_Cds3PSES15MinThreshold_Type())
cds3PSES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PSES15MinThreshold.setStatus(_A)
class _Cds3PSES24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PSES24HrThreshold_Type.__name__=_E
_Cds3PSES24HrThreshold_Object=MibTableColumn
cds3PSES24HrThreshold=_Cds3PSES24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,17),_Cds3PSES24HrThreshold_Type())
cds3PSES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PSES24HrThreshold.setStatus(_A)
class _Cds3SEFS15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3SEFS15MinThreshold_Type.__name__=_E
_Cds3SEFS15MinThreshold_Object=MibTableColumn
cds3SEFS15MinThreshold=_Cds3SEFS15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,18),_Cds3SEFS15MinThreshold_Type())
cds3SEFS15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3SEFS15MinThreshold.setStatus(_A)
class _Cds3SEFS24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3SEFS24HrThreshold_Type.__name__=_E
_Cds3SEFS24HrThreshold_Object=MibTableColumn
cds3SEFS24HrThreshold=_Cds3SEFS24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,19),_Cds3SEFS24HrThreshold_Type())
cds3SEFS24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3SEFS24HrThreshold.setStatus(_A)
class _Cds3UAS15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3UAS15MinThreshold_Type.__name__=_E
_Cds3UAS15MinThreshold_Object=MibTableColumn
cds3UAS15MinThreshold=_Cds3UAS15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,20),_Cds3UAS15MinThreshold_Type())
cds3UAS15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3UAS15MinThreshold.setStatus(_A)
class _Cds3UAS24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3UAS24HrThreshold_Type.__name__=_E
_Cds3UAS24HrThreshold_Object=MibTableColumn
cds3UAS24HrThreshold=_Cds3UAS24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,21),_Cds3UAS24HrThreshold_Type())
cds3UAS24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3UAS24HrThreshold.setStatus(_A)
class _Cds3CCV15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3CCV15MinThreshold_Type.__name__=_E
_Cds3CCV15MinThreshold_Object=MibTableColumn
cds3CCV15MinThreshold=_Cds3CCV15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,22),_Cds3CCV15MinThreshold_Type())
cds3CCV15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3CCV15MinThreshold.setStatus(_A)
class _Cds3CCV24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3CCV24HrThreshold_Type.__name__=_E
_Cds3CCV24HrThreshold_Object=MibTableColumn
cds3CCV24HrThreshold=_Cds3CCV24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,23),_Cds3CCV24HrThreshold_Type())
cds3CCV24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3CCV24HrThreshold.setStatus(_A)
class _Cds3CES15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3CES15MinThreshold_Type.__name__=_E
_Cds3CES15MinThreshold_Object=MibTableColumn
cds3CES15MinThreshold=_Cds3CES15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,24),_Cds3CES15MinThreshold_Type())
cds3CES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3CES15MinThreshold.setStatus(_A)
class _Cds3CES24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3CES24HrThreshold_Type.__name__=_E
_Cds3CES24HrThreshold_Object=MibTableColumn
cds3CES24HrThreshold=_Cds3CES24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,25),_Cds3CES24HrThreshold_Type())
cds3CES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3CES24HrThreshold.setStatus(_A)
class _Cds3CSES15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3CSES15MinThreshold_Type.__name__=_E
_Cds3CSES15MinThreshold_Object=MibTableColumn
cds3CSES15MinThreshold=_Cds3CSES15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,26),_Cds3CSES15MinThreshold_Type())
cds3CSES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3CSES15MinThreshold.setStatus(_A)
class _Cds3CSES24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3CSES24HrThreshold_Type.__name__=_E
_Cds3CSES24HrThreshold_Object=MibTableColumn
cds3CSES24HrThreshold=_Cds3CSES24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,27),_Cds3CSES24HrThreshold_Type())
cds3CSES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3CSES24HrThreshold.setStatus(_A)
class _Cds3LSES15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3LSES15MinThreshold_Type.__name__=_E
_Cds3LSES15MinThreshold_Object=MibTableColumn
cds3LSES15MinThreshold=_Cds3LSES15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,28),_Cds3LSES15MinThreshold_Type())
cds3LSES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LSES15MinThreshold.setStatus(_A)
class _Cds3LSES24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3LSES24HrThreshold_Type.__name__=_E
_Cds3LSES24HrThreshold_Object=MibTableColumn
cds3LSES24HrThreshold=_Cds3LSES24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,29),_Cds3LSES24HrThreshold_Type())
cds3LSES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3LSES24HrThreshold.setStatus(_A)
class _Cds3LineStatisticalAlarmState_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3LineStatisticalAlarmState_Type.__name__=_E
_Cds3LineStatisticalAlarmState_Object=MibTableColumn
cds3LineStatisticalAlarmState=_Cds3LineStatisticalAlarmState_Object((1,3,6,1,4,1,9,9,132,1,2,1,1,1,30),_Cds3LineStatisticalAlarmState_Type())
cds3LineStatisticalAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3LineStatisticalAlarmState.setStatus(_A)
_Cds3AlarmConfigPlcpTable_Object=MibTable
cds3AlarmConfigPlcpTable=_Cds3AlarmConfigPlcpTable_Object((1,3,6,1,4,1,9,9,132,1,2,1,2))
if mibBuilder.loadTexts:cds3AlarmConfigPlcpTable.setStatus(_A)
_Cds3AlarmConfigPlcpEntry_Object=MibTableRow
cds3AlarmConfigPlcpEntry=_Cds3AlarmConfigPlcpEntry_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1))
cds3AlarmConfigPlcpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cds3AlarmConfigPlcpEntry.setStatus(_A)
class _Cds3PlcpStatisticalAlarmSeverity_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('minor',1),('major',2),('none',3)))
_Cds3PlcpStatisticalAlarmSeverity_Type.__name__=_H
_Cds3PlcpStatisticalAlarmSeverity_Object=MibTableColumn
cds3PlcpStatisticalAlarmSeverity=_Cds3PlcpStatisticalAlarmSeverity_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,1),_Cds3PlcpStatisticalAlarmSeverity_Type())
cds3PlcpStatisticalAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpStatisticalAlarmSeverity.setStatus(_A)
class _Cds3PlcpBip8CV15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpBip8CV15MinThreshold_Type.__name__=_E
_Cds3PlcpBip8CV15MinThreshold_Object=MibTableColumn
cds3PlcpBip8CV15MinThreshold=_Cds3PlcpBip8CV15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,2),_Cds3PlcpBip8CV15MinThreshold_Type())
cds3PlcpBip8CV15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpBip8CV15MinThreshold.setStatus(_A)
class _Cds3PlcpBip8CV24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpBip8CV24HrThreshold_Type.__name__=_E
_Cds3PlcpBip8CV24HrThreshold_Object=MibTableColumn
cds3PlcpBip8CV24HrThreshold=_Cds3PlcpBip8CV24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,3),_Cds3PlcpBip8CV24HrThreshold_Type())
cds3PlcpBip8CV24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpBip8CV24HrThreshold.setStatus(_A)
class _Cds3PlcpBip8ES15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpBip8ES15MinThreshold_Type.__name__=_E
_Cds3PlcpBip8ES15MinThreshold_Object=MibTableColumn
cds3PlcpBip8ES15MinThreshold=_Cds3PlcpBip8ES15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,4),_Cds3PlcpBip8ES15MinThreshold_Type())
cds3PlcpBip8ES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpBip8ES15MinThreshold.setStatus(_A)
class _Cds3PlcpBip8ES24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpBip8ES24HrThreshold_Type.__name__=_E
_Cds3PlcpBip8ES24HrThreshold_Object=MibTableColumn
cds3PlcpBip8ES24HrThreshold=_Cds3PlcpBip8ES24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,5),_Cds3PlcpBip8ES24HrThreshold_Type())
cds3PlcpBip8ES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpBip8ES24HrThreshold.setStatus(_A)
class _Cds3PlcpBip8SES15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpBip8SES15MinThreshold_Type.__name__=_E
_Cds3PlcpBip8SES15MinThreshold_Object=MibTableColumn
cds3PlcpBip8SES15MinThreshold=_Cds3PlcpBip8SES15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,6),_Cds3PlcpBip8SES15MinThreshold_Type())
cds3PlcpBip8SES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpBip8SES15MinThreshold.setStatus(_A)
class _Cds3PlcpBip8SES24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpBip8SES24HrThreshold_Type.__name__=_E
_Cds3PlcpBip8SES24HrThreshold_Object=MibTableColumn
cds3PlcpBip8SES24HrThreshold=_Cds3PlcpBip8SES24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,7),_Cds3PlcpBip8SES24HrThreshold_Type())
cds3PlcpBip8SES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpBip8SES24HrThreshold.setStatus(_A)
class _Cds3PlcpSEFS15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpSEFS15MinThreshold_Type.__name__=_E
_Cds3PlcpSEFS15MinThreshold_Object=MibTableColumn
cds3PlcpSEFS15MinThreshold=_Cds3PlcpSEFS15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,8),_Cds3PlcpSEFS15MinThreshold_Type())
cds3PlcpSEFS15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpSEFS15MinThreshold.setStatus(_A)
class _Cds3PlcpSEFS24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpSEFS24HrThreshold_Type.__name__=_E
_Cds3PlcpSEFS24HrThreshold_Object=MibTableColumn
cds3PlcpSEFS24HrThreshold=_Cds3PlcpSEFS24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,9),_Cds3PlcpSEFS24HrThreshold_Type())
cds3PlcpSEFS24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpSEFS24HrThreshold.setStatus(_A)
class _Cds3PlcpUAS15MinThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpUAS15MinThreshold_Type.__name__=_E
_Cds3PlcpUAS15MinThreshold_Object=MibTableColumn
cds3PlcpUAS15MinThreshold=_Cds3PlcpUAS15MinThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,10),_Cds3PlcpUAS15MinThreshold_Type())
cds3PlcpUAS15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpUAS15MinThreshold.setStatus(_A)
class _Cds3PlcpUAS24HrThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Cds3PlcpUAS24HrThreshold_Type.__name__=_E
_Cds3PlcpUAS24HrThreshold_Object=MibTableColumn
cds3PlcpUAS24HrThreshold=_Cds3PlcpUAS24HrThreshold_Object((1,3,6,1,4,1,9,9,132,1,2,1,2,1,11),_Cds3PlcpUAS24HrThreshold_Type())
cds3PlcpUAS24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cds3PlcpUAS24HrThreshold.setStatus(_A)
_Cds3AlarmPlcpTable_Object=MibTable
cds3AlarmPlcpTable=_Cds3AlarmPlcpTable_Object((1,3,6,1,4,1,9,9,132,1,2,2))
if mibBuilder.loadTexts:cds3AlarmPlcpTable.setStatus(_A)
_Cds3AlarmPlcpEntry_Object=MibTableRow
cds3AlarmPlcpEntry=_Cds3AlarmPlcpEntry_Object((1,3,6,1,4,1,9,9,132,1,2,2,1))
cds3AlarmPlcpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cds3AlarmPlcpEntry.setStatus(_A)
_Cds3PlcpLineAlarmState_Type=Unsigned32
_Cds3PlcpLineAlarmState_Object=MibTableColumn
cds3PlcpLineAlarmState=_Cds3PlcpLineAlarmState_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,1),_Cds3PlcpLineAlarmState_Type())
cds3PlcpLineAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpLineAlarmState.setStatus(_A)
_Cds3PlcpLineStatisticalAlarmState_Type=Unsigned32
_Cds3PlcpLineStatisticalAlarmState_Object=MibTableColumn
cds3PlcpLineStatisticalAlarmState=_Cds3PlcpLineStatisticalAlarmState_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,2),_Cds3PlcpLineStatisticalAlarmState_Type())
cds3PlcpLineStatisticalAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpLineStatisticalAlarmState.setStatus(_A)
_Cds3PlcpBip8CVCurrent_Type=Counter32
_Cds3PlcpBip8CVCurrent_Object=MibTableColumn
cds3PlcpBip8CVCurrent=_Cds3PlcpBip8CVCurrent_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,3),_Cds3PlcpBip8CVCurrent_Type())
cds3PlcpBip8CVCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpBip8CVCurrent.setStatus(_A)
_Cds3PlcpBip8CV24HrBucket_Type=Counter32
_Cds3PlcpBip8CV24HrBucket_Object=MibTableColumn
cds3PlcpBip8CV24HrBucket=_Cds3PlcpBip8CV24HrBucket_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,4),_Cds3PlcpBip8CV24HrBucket_Type())
cds3PlcpBip8CV24HrBucket.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpBip8CV24HrBucket.setStatus(_A)
_Cds3PlcpBip8ESCurrent_Type=Counter32
_Cds3PlcpBip8ESCurrent_Object=MibTableColumn
cds3PlcpBip8ESCurrent=_Cds3PlcpBip8ESCurrent_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,5),_Cds3PlcpBip8ESCurrent_Type())
cds3PlcpBip8ESCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpBip8ESCurrent.setStatus(_A)
_Cds3PlcpBip8ES24HrBucket_Type=Counter32
_Cds3PlcpBip8ES24HrBucket_Object=MibTableColumn
cds3PlcpBip8ES24HrBucket=_Cds3PlcpBip8ES24HrBucket_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,6),_Cds3PlcpBip8ES24HrBucket_Type())
cds3PlcpBip8ES24HrBucket.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpBip8ES24HrBucket.setStatus(_A)
_Cds3PlcpBip8SESCurrent_Type=Counter32
_Cds3PlcpBip8SESCurrent_Object=MibTableColumn
cds3PlcpBip8SESCurrent=_Cds3PlcpBip8SESCurrent_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,7),_Cds3PlcpBip8SESCurrent_Type())
cds3PlcpBip8SESCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpBip8SESCurrent.setStatus(_A)
_Cds3PlcpBip8SES24HrBucket_Type=Counter32
_Cds3PlcpBip8SES24HrBucket_Object=MibTableColumn
cds3PlcpBip8SES24HrBucket=_Cds3PlcpBip8SES24HrBucket_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,8),_Cds3PlcpBip8SES24HrBucket_Type())
cds3PlcpBip8SES24HrBucket.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpBip8SES24HrBucket.setStatus(_A)
_Cds3PlcpSEFSCurrent_Type=Counter32
_Cds3PlcpSEFSCurrent_Object=MibTableColumn
cds3PlcpSEFSCurrent=_Cds3PlcpSEFSCurrent_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,9),_Cds3PlcpSEFSCurrent_Type())
cds3PlcpSEFSCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpSEFSCurrent.setStatus(_A)
_Cds3PlcpSEFS24HrBucket_Type=Counter32
_Cds3PlcpSEFS24HrBucket_Object=MibTableColumn
cds3PlcpSEFS24HrBucket=_Cds3PlcpSEFS24HrBucket_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,10),_Cds3PlcpSEFS24HrBucket_Type())
cds3PlcpSEFS24HrBucket.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpSEFS24HrBucket.setStatus(_A)
_Cds3PlcpUASCurrent_Type=Counter32
_Cds3PlcpUASCurrent_Object=MibTableColumn
cds3PlcpUASCurrent=_Cds3PlcpUASCurrent_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,11),_Cds3PlcpUASCurrent_Type())
cds3PlcpUASCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpUASCurrent.setStatus(_A)
_Cds3PlcpUAS24HrBucket_Type=Counter32
_Cds3PlcpUAS24HrBucket_Object=MibTableColumn
cds3PlcpUAS24HrBucket=_Cds3PlcpUAS24HrBucket_Object((1,3,6,1,4,1,9,9,132,1,2,2,1,12),_Cds3PlcpUAS24HrBucket_Type())
cds3PlcpUAS24HrBucket.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpUAS24HrBucket.setStatus(_A)
_Cds3Stats_ObjectIdentity=ObjectIdentity
cds3Stats=_Cds3Stats_ObjectIdentity((1,3,6,1,4,1,9,9,132,1,3))
_Cds3StatsTable_Object=MibTable
cds3StatsTable=_Cds3StatsTable_Object((1,3,6,1,4,1,9,9,132,1,3,1))
if mibBuilder.loadTexts:cds3StatsTable.setStatus(_A)
_Cds3StatsEntry_Object=MibTableRow
cds3StatsEntry=_Cds3StatsEntry_Object((1,3,6,1,4,1,9,9,132,1,3,1,1))
cds3StatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cds3StatsEntry.setStatus(_A)
_Cds3RcvLOSCount_Type=Counter32
_Cds3RcvLOSCount_Object=MibTableColumn
cds3RcvLOSCount=_Cds3RcvLOSCount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,1),_Cds3RcvLOSCount_Type())
cds3RcvLOSCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3RcvLOSCount.setStatus(_A)
_Cds3RcvOOFCount_Type=Counter32
_Cds3RcvOOFCount_Object=MibTableColumn
cds3RcvOOFCount=_Cds3RcvOOFCount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,2),_Cds3RcvOOFCount_Type())
cds3RcvOOFCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3RcvOOFCount.setStatus(_A)
_Cds3RAICount_Type=Counter32
_Cds3RAICount_Object=MibTableColumn
cds3RAICount=_Cds3RAICount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,3),_Cds3RAICount_Type())
cds3RAICount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3RAICount.setStatus(_A)
_Cds3CCVCount_Type=Counter32
_Cds3CCVCount_Object=MibTableColumn
cds3CCVCount=_Cds3CCVCount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,4),_Cds3CCVCount_Type())
cds3CCVCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3CCVCount.setStatus(_A)
_Cds3FECount_Type=Counter32
_Cds3FECount_Object=MibTableColumn
cds3FECount=_Cds3FECount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,5),_Cds3FECount_Type())
cds3FECount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3FECount.setStatus(_A)
_Cds3EXZSCount_Type=Counter32
_Cds3EXZSCount_Object=MibTableColumn
cds3EXZSCount=_Cds3EXZSCount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,6),_Cds3EXZSCount_Type())
cds3EXZSCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3EXZSCount.setStatus(_A)
_Cds3LCVCount_Type=Counter32
_Cds3LCVCount_Object=MibTableColumn
cds3LCVCount=_Cds3LCVCount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,7),_Cds3LCVCount_Type())
cds3LCVCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3LCVCount.setStatus(_A)
_Cds3PCVCount_Type=Counter32
_Cds3PCVCount_Object=MibTableColumn
cds3PCVCount=_Cds3PCVCount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,8),_Cds3PCVCount_Type())
cds3PCVCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PCVCount.setStatus(_A)
_Cds3CPECount_Type=Counter32
_Cds3CPECount_Object=MibTableColumn
cds3CPECount=_Cds3CPECount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,9),_Cds3CPECount_Type())
cds3CPECount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3CPECount.setStatus(_A)
_Cds3FEBECount_Type=Counter32
_Cds3FEBECount_Object=MibTableColumn
cds3FEBECount=_Cds3FEBECount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,10),_Cds3FEBECount_Type())
cds3FEBECount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3FEBECount.setStatus(_A)
_Cds3RcvAISCount_Type=Counter32
_Cds3RcvAISCount_Object=MibTableColumn
cds3RcvAISCount=_Cds3RcvAISCount_Object((1,3,6,1,4,1,9,9,132,1,3,1,1,11),_Cds3RcvAISCount_Type())
cds3RcvAISCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3RcvAISCount.setStatus(_A)
_Cds3PlcpStatsTable_Object=MibTable
cds3PlcpStatsTable=_Cds3PlcpStatsTable_Object((1,3,6,1,4,1,9,9,132,1,3,2))
if mibBuilder.loadTexts:cds3PlcpStatsTable.setStatus(_A)
_Cds3PlcpStatsEntry_Object=MibTableRow
cds3PlcpStatsEntry=_Cds3PlcpStatsEntry_Object((1,3,6,1,4,1,9,9,132,1,3,2,1))
cds3PlcpStatsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cds3PlcpStatsEntry.setStatus(_A)
_Cds3PlcpRcvBip8Count_Type=Counter32
_Cds3PlcpRcvBip8Count_Object=MibTableColumn
cds3PlcpRcvBip8Count=_Cds3PlcpRcvBip8Count_Object((1,3,6,1,4,1,9,9,132,1,3,2,1,1),_Cds3PlcpRcvBip8Count_Type())
cds3PlcpRcvBip8Count.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpRcvBip8Count.setStatus(_A)
_Cds3PlcpRcvOOFCount_Type=Counter32
_Cds3PlcpRcvOOFCount_Object=MibTableColumn
cds3PlcpRcvOOFCount=_Cds3PlcpRcvOOFCount_Object((1,3,6,1,4,1,9,9,132,1,3,2,1,2),_Cds3PlcpRcvOOFCount_Type())
cds3PlcpRcvOOFCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpRcvOOFCount.setStatus(_A)
_Cds3PlcpRcvRAICount_Type=Counter32
_Cds3PlcpRcvRAICount_Object=MibTableColumn
cds3PlcpRcvRAICount=_Cds3PlcpRcvRAICount_Object((1,3,6,1,4,1,9,9,132,1,3,2,1,3),_Cds3PlcpRcvRAICount_Type())
cds3PlcpRcvRAICount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpRcvRAICount.setStatus(_A)
_Cds3PlcpFECount_Type=Counter32
_Cds3PlcpFECount_Object=MibTableColumn
cds3PlcpFECount=_Cds3PlcpFECount_Object((1,3,6,1,4,1,9,9,132,1,3,2,1,4),_Cds3PlcpFECount_Type())
cds3PlcpFECount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpFECount.setStatus(_A)
_Cds3PlcpFESecCount_Type=Counter32
_Cds3PlcpFESecCount_Object=MibTableColumn
cds3PlcpFESecCount=_Cds3PlcpFESecCount_Object((1,3,6,1,4,1,9,9,132,1,3,2,1,5),_Cds3PlcpFESecCount_Type())
cds3PlcpFESecCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpFESecCount.setStatus(_A)
_Cds3PlcpSEFSecCount_Type=Counter32
_Cds3PlcpSEFSecCount_Object=MibTableColumn
cds3PlcpSEFSecCount=_Cds3PlcpSEFSecCount_Object((1,3,6,1,4,1,9,9,132,1,3,2,1,6),_Cds3PlcpSEFSecCount_Type())
cds3PlcpSEFSecCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpSEFSecCount.setStatus(_A)
_Cds3PlcpFEBECount_Type=Counter32
_Cds3PlcpFEBECount_Object=MibTableColumn
cds3PlcpFEBECount=_Cds3PlcpFEBECount_Object((1,3,6,1,4,1,9,9,132,1,3,2,1,7),_Cds3PlcpFEBECount_Type())
cds3PlcpFEBECount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpFEBECount.setStatus(_A)
_Cds3PlcpFEBESecCount_Type=Counter32
_Cds3PlcpFEBESecCount_Object=MibTableColumn
cds3PlcpFEBESecCount=_Cds3PlcpFEBESecCount_Object((1,3,6,1,4,1,9,9,132,1,3,2,1,8),_Cds3PlcpFEBESecCount_Type())
cds3PlcpFEBESecCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpFEBESecCount.setStatus(_A)
_Cds3PlcpSEFEBESecCount_Type=Counter32
_Cds3PlcpSEFEBESecCount_Object=MibTableColumn
cds3PlcpSEFEBESecCount=_Cds3PlcpSEFEBESecCount_Object((1,3,6,1,4,1,9,9,132,1,3,2,1,9),_Cds3PlcpSEFEBESecCount_Type())
cds3PlcpSEFEBESecCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PlcpSEFEBESecCount.setStatus(_A)
_Cds3IntervalTable_Object=MibTable
cds3IntervalTable=_Cds3IntervalTable_Object((1,3,6,1,4,1,9,9,132,1,3,4))
if mibBuilder.loadTexts:cds3IntervalTable.setStatus(_A)
_Cds3IntervalEntry_Object=MibTableRow
cds3IntervalEntry=_Cds3IntervalEntry_Object((1,3,6,1,4,1,9,9,132,1,3,4,1))
cds3IntervalEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:cds3IntervalEntry.setStatus(_A)
class _Cds3IntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_Cds3IntervalNumber_Type.__name__=_H
_Cds3IntervalNumber_Object=MibTableColumn
cds3IntervalNumber=_Cds3IntervalNumber_Object((1,3,6,1,4,1,9,9,132,1,3,4,1,1),_Cds3IntervalNumber_Type())
cds3IntervalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3IntervalNumber.setStatus(_A)
_Cds3IntervalLSESs_Type=Counter32
_Cds3IntervalLSESs_Object=MibTableColumn
cds3IntervalLSESs=_Cds3IntervalLSESs_Object((1,3,6,1,4,1,9,9,132,1,3,4,1,2),_Cds3IntervalLSESs_Type())
cds3IntervalLSESs.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3IntervalLSESs.setStatus(_A)
_Cds3Current24HrTable_Object=MibTable
cds3Current24HrTable=_Cds3Current24HrTable_Object((1,3,6,1,4,1,9,9,132,1,3,5))
if mibBuilder.loadTexts:cds3Current24HrTable.setStatus(_A)
_Cds3Current24HrEntry_Object=MibTableRow
cds3Current24HrEntry=_Cds3Current24HrEntry_Object((1,3,6,1,4,1,9,9,132,1,3,5,1))
cds3Current24HrEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cds3Current24HrEntry.setStatus(_A)
_Cds3LCVCurrent24Hr_Type=Counter32
_Cds3LCVCurrent24Hr_Object=MibTableColumn
cds3LCVCurrent24Hr=_Cds3LCVCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,1),_Cds3LCVCurrent24Hr_Type())
cds3LCVCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3LCVCurrent24Hr.setStatus(_A)
_Cds3LESCurrent24Hr_Type=Counter32
_Cds3LESCurrent24Hr_Object=MibTableColumn
cds3LESCurrent24Hr=_Cds3LESCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,2),_Cds3LESCurrent24Hr_Type())
cds3LESCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3LESCurrent24Hr.setStatus(_A)
_Cds3PCVCurrent24Hr_Type=Counter32
_Cds3PCVCurrent24Hr_Object=MibTableColumn
cds3PCVCurrent24Hr=_Cds3PCVCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,3),_Cds3PCVCurrent24Hr_Type())
cds3PCVCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PCVCurrent24Hr.setStatus(_A)
_Cds3PESCurrent24Hr_Type=Counter32
_Cds3PESCurrent24Hr_Object=MibTableColumn
cds3PESCurrent24Hr=_Cds3PESCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,4),_Cds3PESCurrent24Hr_Type())
cds3PESCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PESCurrent24Hr.setStatus(_A)
_Cds3PSESCurrent24Hr_Type=Counter32
_Cds3PSESCurrent24Hr_Object=MibTableColumn
cds3PSESCurrent24Hr=_Cds3PSESCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,5),_Cds3PSESCurrent24Hr_Type())
cds3PSESCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PSESCurrent24Hr.setStatus(_A)
_Cds3SEFSCurrent24Hr_Type=Counter32
_Cds3SEFSCurrent24Hr_Object=MibTableColumn
cds3SEFSCurrent24Hr=_Cds3SEFSCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,6),_Cds3SEFSCurrent24Hr_Type())
cds3SEFSCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3SEFSCurrent24Hr.setStatus(_A)
_Cds3UASCurrent24Hr_Type=Counter32
_Cds3UASCurrent24Hr_Object=MibTableColumn
cds3UASCurrent24Hr=_Cds3UASCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,7),_Cds3UASCurrent24Hr_Type())
cds3UASCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3UASCurrent24Hr.setStatus(_A)
_Cds3CCVCurrent24Hr_Type=Counter32
_Cds3CCVCurrent24Hr_Object=MibTableColumn
cds3CCVCurrent24Hr=_Cds3CCVCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,8),_Cds3CCVCurrent24Hr_Type())
cds3CCVCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3CCVCurrent24Hr.setStatus(_A)
_Cds3CESCurrent24Hr_Type=Counter32
_Cds3CESCurrent24Hr_Object=MibTableColumn
cds3CESCurrent24Hr=_Cds3CESCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,9),_Cds3CESCurrent24Hr_Type())
cds3CESCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3CESCurrent24Hr.setStatus(_A)
_Cds3CSESCurrent24Hr_Type=Counter32
_Cds3CSESCurrent24Hr_Object=MibTableColumn
cds3CSESCurrent24Hr=_Cds3CSESCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,10),_Cds3CSESCurrent24Hr_Type())
cds3CSESCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3CSESCurrent24Hr.setStatus(_A)
_Cds3LSESCurrent24Hr_Type=Counter32
_Cds3LSESCurrent24Hr_Object=MibTableColumn
cds3LSESCurrent24Hr=_Cds3LSESCurrent24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,5,1,11),_Cds3LSESCurrent24Hr_Type())
cds3LSESCurrent24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3LSESCurrent24Hr.setStatus(_A)
_Cds3Previous24HrTable_Object=MibTable
cds3Previous24HrTable=_Cds3Previous24HrTable_Object((1,3,6,1,4,1,9,9,132,1,3,6))
if mibBuilder.loadTexts:cds3Previous24HrTable.setStatus(_A)
_Cds3Previous24HrEntry_Object=MibTableRow
cds3Previous24HrEntry=_Cds3Previous24HrEntry_Object((1,3,6,1,4,1,9,9,132,1,3,6,1))
cds3Previous24HrEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:cds3Previous24HrEntry.setStatus(_A)
_Cds3LCVPrevious24Hr_Type=Counter32
_Cds3LCVPrevious24Hr_Object=MibTableColumn
cds3LCVPrevious24Hr=_Cds3LCVPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,1),_Cds3LCVPrevious24Hr_Type())
cds3LCVPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3LCVPrevious24Hr.setStatus(_A)
_Cds3LESPrevious24Hr_Type=Counter32
_Cds3LESPrevious24Hr_Object=MibTableColumn
cds3LESPrevious24Hr=_Cds3LESPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,2),_Cds3LESPrevious24Hr_Type())
cds3LESPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3LESPrevious24Hr.setStatus(_A)
_Cds3PCVPrevious24Hr_Type=Counter32
_Cds3PCVPrevious24Hr_Object=MibTableColumn
cds3PCVPrevious24Hr=_Cds3PCVPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,3),_Cds3PCVPrevious24Hr_Type())
cds3PCVPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PCVPrevious24Hr.setStatus(_A)
_Cds3PESPrevious24Hr_Type=Counter32
_Cds3PESPrevious24Hr_Object=MibTableColumn
cds3PESPrevious24Hr=_Cds3PESPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,4),_Cds3PESPrevious24Hr_Type())
cds3PESPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PESPrevious24Hr.setStatus(_A)
_Cds3PSESPrevious24Hr_Type=Counter32
_Cds3PSESPrevious24Hr_Object=MibTableColumn
cds3PSESPrevious24Hr=_Cds3PSESPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,5),_Cds3PSESPrevious24Hr_Type())
cds3PSESPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3PSESPrevious24Hr.setStatus(_A)
_Cds3SEFSPrevious24Hr_Type=Counter32
_Cds3SEFSPrevious24Hr_Object=MibTableColumn
cds3SEFSPrevious24Hr=_Cds3SEFSPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,6),_Cds3SEFSPrevious24Hr_Type())
cds3SEFSPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3SEFSPrevious24Hr.setStatus(_A)
_Cds3UASPrevious24Hr_Type=Counter32
_Cds3UASPrevious24Hr_Object=MibTableColumn
cds3UASPrevious24Hr=_Cds3UASPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,7),_Cds3UASPrevious24Hr_Type())
cds3UASPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3UASPrevious24Hr.setStatus(_A)
_Cds3CCVPrevious24Hr_Type=Counter32
_Cds3CCVPrevious24Hr_Object=MibTableColumn
cds3CCVPrevious24Hr=_Cds3CCVPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,8),_Cds3CCVPrevious24Hr_Type())
cds3CCVPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3CCVPrevious24Hr.setStatus(_A)
_Cds3CESPrevious24Hr_Type=Counter32
_Cds3CESPrevious24Hr_Object=MibTableColumn
cds3CESPrevious24Hr=_Cds3CESPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,9),_Cds3CESPrevious24Hr_Type())
cds3CESPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3CESPrevious24Hr.setStatus(_A)
_Cds3CSESPrevious24Hr_Type=Counter32
_Cds3CSESPrevious24Hr_Object=MibTableColumn
cds3CSESPrevious24Hr=_Cds3CSESPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,10),_Cds3CSESPrevious24Hr_Type())
cds3CSESPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3CSESPrevious24Hr.setStatus(_A)
_Cds3LSESPrevious24Hr_Type=Counter32
_Cds3LSESPrevious24Hr_Object=MibTableColumn
cds3LSESPrevious24Hr=_Cds3LSESPrevious24Hr_Object((1,3,6,1,4,1,9,9,132,1,3,6,1,11),_Cds3LSESPrevious24Hr_Type())
cds3LSESPrevious24Hr.setMaxAccess(_C)
if mibBuilder.loadTexts:cds3LSESPrevious24Hr.setStatus(_A)
_CiscoDs3MIBConformance_ObjectIdentity=ObjectIdentity
ciscoDs3MIBConformance=_CiscoDs3MIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,132,8))
_CiscoDs3MIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDs3MIBCompliances=_CiscoDs3MIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,132,8,1))
_CiscoDs3MIBGroups_ObjectIdentity=ObjectIdentity
ciscoDs3MIBGroups=_CiscoDs3MIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,132,8,2))
ciscoDs3ConfMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,132,8,2,1))
ciscoDs3ConfMIBGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ciscoDs3ConfMIBGroup.setStatus(_A)
cds3StatsMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,132,8,2,2))
cds3StatsMIBGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:cds3StatsMIBGroup.setStatus(_A)
ciscoDs3AlarmMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,132,8,2,3))
ciscoDs3AlarmMIBGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_J),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:ciscoDs3AlarmMIBGroup.setStatus(_A)
ciscoPlcpCounterMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,132,8,2,4))
ciscoPlcpCounterMIBGroup.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:ciscoPlcpCounterMIBGroup.setStatus(_A)
ciscoPlcpAlarmMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,132,8,2,5))
ciscoPlcpAlarmMIBGroup.setObjects(*((_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar)))
if mibBuilder.loadTexts:ciscoPlcpAlarmMIBGroup.setStatus(_A)
ciscoDs3Previous24HrGroup=ObjectGroup((1,3,6,1,4,1,9,9,132,8,2,6))
ciscoDs3Previous24HrGroup.setObjects(*((_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1)))
if mibBuilder.loadTexts:ciscoDs3Previous24HrGroup.setStatus(_A)
ciscoDs3MIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,132,8,1,1))
ciscoDs3MIBCompliance.setObjects(*((_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6)))
if mibBuilder.loadTexts:ciscoDs3MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDs3MIB':ciscoDs3MIB,'ciscoDs3MIBObjects':ciscoDs3MIBObjects,'cds3Config':cds3Config,'cds3ConfigTable':cds3ConfigTable,'cds3ConfigEntry':cds3ConfigEntry,_L:cds3LineType,_M:cds3LineAIScBitsCheck,_N:cds3LineRcvFEACValidation,_O:cds3LineOOFCriteria,_P:cds3TraceToTransmit,_Q:cds3TraceToExpect,_R:cds3TraceAlarm,_S:cds3InternalEqualizer,_T:cds3NearEndLineLoopbackStatus,_U:cds3FarEndLineLoopbackStatus,'cds3Alarm':cds3Alarm,'cds3AlarmConfig':cds3AlarmConfig,'cds3AlarmConfigTable':cds3AlarmConfigTable,'cds3AlarmConfigEntry':cds3AlarmConfigEntry,_g:cds3NEAlarmUpCount,_h:cds3NEAlarmDownCount,_i:cds3NEAlarmThreshold,_j:cds3FEAlarmUpCount,_k:cds3FEAlarmDownCount,_l:cds3FEAlarmThreshold,_m:cds3StatisticalAlarmSeverity,_n:cds3LCV15MinThreshold,_o:cds3LCV24HrThreshold,_p:cds3LES15MinThreshold,_q:cds3LES24HrThreshold,_r:cds3PCV15MinThreshold,_s:cds3PCV24HrThreshold,_t:cds3PES15MinThreshold,_u:cds3PES24HrThreshold,_v:cds3PSES15MinThreshold,_w:cds3PSES24HrThreshold,_x:cds3SEFS15MinThreshold,_y:cds3SEFS24HrThreshold,_z:cds3UAS15MinThreshold,_A0:cds3UAS24HrThreshold,_A1:cds3CCV15MinThreshold,_A2:cds3CCV24HrThreshold,_A3:cds3CES15MinThreshold,_A4:cds3CES24HrThreshold,_A5:cds3CSES15MinThreshold,_A6:cds3CSES24HrThreshold,_A7:cds3LSES15MinThreshold,_A8:cds3LSES24HrThreshold,_A9:cds3LineStatisticalAlarmState,'cds3AlarmConfigPlcpTable':cds3AlarmConfigPlcpTable,'cds3AlarmConfigPlcpEntry':cds3AlarmConfigPlcpEntry,_AV:cds3PlcpStatisticalAlarmSeverity,_AW:cds3PlcpBip8CV15MinThreshold,_AX:cds3PlcpBip8CV24HrThreshold,_AY:cds3PlcpBip8ES15MinThreshold,_AZ:cds3PlcpBip8ES24HrThreshold,_Aa:cds3PlcpBip8SES15MinThreshold,_Ab:cds3PlcpBip8SES24HrThreshold,_Ac:cds3PlcpSEFS15MinThreshold,_Ad:cds3PlcpSEFS24HrThreshold,_Ae:cds3PlcpUAS15MinThreshold,_Af:cds3PlcpUAS24HrThreshold,'cds3AlarmPlcpTable':cds3AlarmPlcpTable,'cds3AlarmPlcpEntry':cds3AlarmPlcpEntry,_Ag:cds3PlcpLineAlarmState,_Ah:cds3PlcpLineStatisticalAlarmState,_Ai:cds3PlcpBip8CVCurrent,_Aj:cds3PlcpBip8CV24HrBucket,_Ak:cds3PlcpBip8ESCurrent,_Al:cds3PlcpBip8ES24HrBucket,_Am:cds3PlcpBip8SESCurrent,_An:cds3PlcpBip8SES24HrBucket,_Ao:cds3PlcpSEFSCurrent,_Ap:cds3PlcpSEFS24HrBucket,_Aq:cds3PlcpUASCurrent,_Ar:cds3PlcpUAS24HrBucket,'cds3Stats':cds3Stats,'cds3StatsTable':cds3StatsTable,'cds3StatsEntry':cds3StatsEntry,_V:cds3RcvLOSCount,_W:cds3RcvOOFCount,_X:cds3RAICount,_Y:cds3CCVCount,_Z:cds3FECount,_a:cds3EXZSCount,_b:cds3LCVCount,_c:cds3PCVCount,_d:cds3CPECount,_e:cds3FEBECount,_f:cds3RcvAISCount,'cds3PlcpStatsTable':cds3PlcpStatsTable,'cds3PlcpStatsEntry':cds3PlcpStatsEntry,_AM:cds3PlcpRcvBip8Count,_AN:cds3PlcpRcvOOFCount,_AO:cds3PlcpRcvRAICount,_AP:cds3PlcpFECount,_AQ:cds3PlcpFESecCount,_AR:cds3PlcpSEFSecCount,_AS:cds3PlcpFEBECount,_AT:cds3PlcpFEBESecCount,_AU:cds3PlcpSEFEBESecCount,'cds3IntervalTable':cds3IntervalTable,'cds3IntervalEntry':cds3IntervalEntry,_J:cds3IntervalNumber,_AA:cds3IntervalLSESs,'cds3Current24HrTable':cds3Current24HrTable,'cds3Current24HrEntry':cds3Current24HrEntry,_AB:cds3LCVCurrent24Hr,_AC:cds3LESCurrent24Hr,_AD:cds3PCVCurrent24Hr,_AE:cds3PESCurrent24Hr,_AF:cds3PSESCurrent24Hr,_AG:cds3SEFSCurrent24Hr,_AH:cds3UASCurrent24Hr,_AI:cds3CCVCurrent24Hr,_AJ:cds3CESCurrent24Hr,_AK:cds3CSESCurrent24Hr,_AL:cds3LSESCurrent24Hr,'cds3Previous24HrTable':cds3Previous24HrTable,'cds3Previous24HrEntry':cds3Previous24HrEntry,_As:cds3LCVPrevious24Hr,_At:cds3LESPrevious24Hr,_Au:cds3PCVPrevious24Hr,_Av:cds3PESPrevious24Hr,_Aw:cds3PSESPrevious24Hr,_Ax:cds3SEFSPrevious24Hr,_Ay:cds3UASPrevious24Hr,_Az:cds3CCVPrevious24Hr,_A_:cds3CESPrevious24Hr,_B0:cds3CSESPrevious24Hr,_B1:cds3LSESPrevious24Hr,'ciscoDs3MIBConformance':ciscoDs3MIBConformance,'ciscoDs3MIBCompliances':ciscoDs3MIBCompliances,'ciscoDs3MIBCompliance':ciscoDs3MIBCompliance,'ciscoDs3MIBGroups':ciscoDs3MIBGroups,_B2:ciscoDs3ConfMIBGroup,_B3:cds3StatsMIBGroup,_B4:ciscoDs3AlarmMIBGroup,_B5:ciscoPlcpCounterMIBGroup,'ciscoPlcpAlarmMIBGroup':ciscoPlcpAlarmMIBGroup,_B6:ciscoDs3Previous24HrGroup})