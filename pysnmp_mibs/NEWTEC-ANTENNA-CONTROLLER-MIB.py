_r='ntcAntCtrlConfGrpV1Standard'
_q='ntcAntCtrlAntFailure'
_p='ntcAntCtrlCommError'
_o='ntcAntCtrlAntFailureStat'
_n='ntcAntCtrlCommErrorStat'
_m='ntcAntCtrlRxMsg'
_l='ntcAntCtrlTxMsg'
_k='ntcAntCtrlLongitude'
_j='ntcAntCtrlLatitude'
_i='ntcAntCtrlTxAllowed'
_h='ntcAntCtrlAntStatus'
_g='ntcAntCtrlInterval'
_f='ntcAntCtrlCfgTxMaxSkew'
_e='ntcAntCtrlCfgTxLoFreq'
_d='ntcAntCtrlCfgRxLoFreq'
_c='ntcAntCtrlCfgTxPol'
_b='ntcAntCtrlCfgRxPol'
_a='ntcAntCtrlCfgSatSkew'
_Z='ntcAntCtrlCfgSatLatVar'
_Y='ntcAntCtrlCfgSatLong'
_X='ntcAntCtrlCfgPort'
_W='ntcAntCtrlCfgIpAddress'
_V='ntcAntCtrlCfgEnable'
_U='ntcAntCtrlAlarmStatsControlId'
_T='unknown'
_S='ntcAntCtrlMonControlId'
_R='vertical'
_Q='horizontal'
_P='righthanded'
_O='lefthanded'
_N='ntcAntCtrlCfgControlId'
_M='NtcEnable'
_L='not-accessible'
_K='control4'
_J='control3'
_I='control2'
_H='control1'
_G='Unsigned32'
_F='deg.'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='NEWTEC-ANTENNA-CONTROLLER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Float32TC,=mibBuilder.importSymbols('FLOAT-TC-MIB','Float32TC')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcAntennaController=ModuleIdentity((1,3,6,1,4,1,5835,5,2,5700))
if mibBuilder.loadTexts:ntcAntennaController.setRevisions(('2018-02-02 09:00','2014-02-03 12:00'))
_NtcAntCtrlObjects_ObjectIdentity=ObjectIdentity
ntcAntCtrlObjects=_NtcAntCtrlObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5700,1))
if mibBuilder.loadTexts:ntcAntCtrlObjects.setStatus(_A)
_NtcAntCtrlCfg_ObjectIdentity=ObjectIdentity
ntcAntCtrlCfg=_NtcAntCtrlCfg_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5700,1,1))
if mibBuilder.loadTexts:ntcAntCtrlCfg.setStatus(_A)
_NtcAntCtrlCfgTable_Object=MibTable
ntcAntCtrlCfgTable=_NtcAntCtrlCfgTable_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1))
if mibBuilder.loadTexts:ntcAntCtrlCfgTable.setStatus(_A)
_NtcAntCtrlCfgEntry_Object=MibTableRow
ntcAntCtrlCfgEntry=_NtcAntCtrlCfgEntry_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1))
ntcAntCtrlCfgEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ntcAntCtrlCfgEntry.setStatus(_A)
class _NtcAntCtrlCfgControlId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4)))
_NtcAntCtrlCfgControlId_Type.__name__=_E
_NtcAntCtrlCfgControlId_Object=MibTableColumn
ntcAntCtrlCfgControlId=_NtcAntCtrlCfgControlId_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,1),_NtcAntCtrlCfgControlId_Type())
ntcAntCtrlCfgControlId.setMaxAccess(_L)
if mibBuilder.loadTexts:ntcAntCtrlCfgControlId.setStatus(_A)
class _NtcAntCtrlCfgEnable_Type(NtcEnable):defaultValue=0
_NtcAntCtrlCfgEnable_Type.__name__=_M
_NtcAntCtrlCfgEnable_Object=MibTableColumn
ntcAntCtrlCfgEnable=_NtcAntCtrlCfgEnable_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,2),_NtcAntCtrlCfgEnable_Type())
ntcAntCtrlCfgEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgEnable.setStatus(_A)
_NtcAntCtrlCfgIpAddress_Type=IpAddress
_NtcAntCtrlCfgIpAddress_Object=MibTableColumn
ntcAntCtrlCfgIpAddress=_NtcAntCtrlCfgIpAddress_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,3),_NtcAntCtrlCfgIpAddress_Type())
ntcAntCtrlCfgIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgIpAddress.setStatus(_A)
class _NtcAntCtrlCfgPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtcAntCtrlCfgPort_Type.__name__=_G
_NtcAntCtrlCfgPort_Object=MibTableColumn
ntcAntCtrlCfgPort=_NtcAntCtrlCfgPort_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,4),_NtcAntCtrlCfgPort_Type())
ntcAntCtrlCfgPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgPort.setStatus(_A)
_NtcAntCtrlCfgSatLong_Type=Float32TC
_NtcAntCtrlCfgSatLong_Object=MibTableColumn
ntcAntCtrlCfgSatLong=_NtcAntCtrlCfgSatLong_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,5),_NtcAntCtrlCfgSatLong_Type())
ntcAntCtrlCfgSatLong.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgSatLong.setStatus(_A)
if mibBuilder.loadTexts:ntcAntCtrlCfgSatLong.setUnits(_F)
_NtcAntCtrlCfgSatLatVar_Type=Float32TC
_NtcAntCtrlCfgSatLatVar_Object=MibTableColumn
ntcAntCtrlCfgSatLatVar=_NtcAntCtrlCfgSatLatVar_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,6),_NtcAntCtrlCfgSatLatVar_Type())
ntcAntCtrlCfgSatLatVar.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgSatLatVar.setStatus(_A)
if mibBuilder.loadTexts:ntcAntCtrlCfgSatLatVar.setUnits(_F)
_NtcAntCtrlCfgSatSkew_Type=Float32TC
_NtcAntCtrlCfgSatSkew_Object=MibTableColumn
ntcAntCtrlCfgSatSkew=_NtcAntCtrlCfgSatSkew_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,7),_NtcAntCtrlCfgSatSkew_Type())
ntcAntCtrlCfgSatSkew.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlCfgSatSkew.setStatus(_A)
if mibBuilder.loadTexts:ntcAntCtrlCfgSatSkew.setUnits(_F)
class _NtcAntCtrlCfgRxPol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,3),(_R,4)))
_NtcAntCtrlCfgRxPol_Type.__name__=_E
_NtcAntCtrlCfgRxPol_Object=MibTableColumn
ntcAntCtrlCfgRxPol=_NtcAntCtrlCfgRxPol_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,8),_NtcAntCtrlCfgRxPol_Type())
ntcAntCtrlCfgRxPol.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgRxPol.setStatus(_A)
class _NtcAntCtrlCfgTxPol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4)));namedValues=NamedValues(*((_O,0),(_P,1),(_Q,3),(_R,4)))
_NtcAntCtrlCfgTxPol_Type.__name__=_E
_NtcAntCtrlCfgTxPol_Object=MibTableColumn
ntcAntCtrlCfgTxPol=_NtcAntCtrlCfgTxPol_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,9),_NtcAntCtrlCfgTxPol_Type())
ntcAntCtrlCfgTxPol.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgTxPol.setStatus(_A)
class _NtcAntCtrlCfgRxLoFreq_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,42000000))
_NtcAntCtrlCfgRxLoFreq_Type.__name__=_G
_NtcAntCtrlCfgRxLoFreq_Object=MibTableColumn
ntcAntCtrlCfgRxLoFreq=_NtcAntCtrlCfgRxLoFreq_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,10),_NtcAntCtrlCfgRxLoFreq_Type())
ntcAntCtrlCfgRxLoFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgRxLoFreq.setStatus(_A)
if mibBuilder.loadTexts:ntcAntCtrlCfgRxLoFreq.setUnits('kHz')
class _NtcAntCtrlCfgTxLoFreq_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,42000000))
_NtcAntCtrlCfgTxLoFreq_Type.__name__=_G
_NtcAntCtrlCfgTxLoFreq_Object=MibTableColumn
ntcAntCtrlCfgTxLoFreq=_NtcAntCtrlCfgTxLoFreq_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,11),_NtcAntCtrlCfgTxLoFreq_Type())
ntcAntCtrlCfgTxLoFreq.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgTxLoFreq.setStatus(_A)
if mibBuilder.loadTexts:ntcAntCtrlCfgTxLoFreq.setUnits('kHz')
_NtcAntCtrlCfgTxMaxSkew_Type=Float32TC
_NtcAntCtrlCfgTxMaxSkew_Object=MibTableColumn
ntcAntCtrlCfgTxMaxSkew=_NtcAntCtrlCfgTxMaxSkew_Object((1,3,6,1,4,1,5835,5,2,5700,1,1,1,1,12),_NtcAntCtrlCfgTxMaxSkew_Type())
ntcAntCtrlCfgTxMaxSkew.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAntCtrlCfgTxMaxSkew.setStatus(_A)
if mibBuilder.loadTexts:ntcAntCtrlCfgTxMaxSkew.setUnits(_F)
_NtcAntCtrlMon_ObjectIdentity=ObjectIdentity
ntcAntCtrlMon=_NtcAntCtrlMon_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5700,1,2))
if mibBuilder.loadTexts:ntcAntCtrlMon.setStatus(_A)
_NtcAntCtrlMonTable_Object=MibTable
ntcAntCtrlMonTable=_NtcAntCtrlMonTable_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1))
if mibBuilder.loadTexts:ntcAntCtrlMonTable.setStatus(_A)
_NtcAntCtrlMonEntry_Object=MibTableRow
ntcAntCtrlMonEntry=_NtcAntCtrlMonEntry_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1,1))
ntcAntCtrlMonEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:ntcAntCtrlMonEntry.setStatus(_A)
class _NtcAntCtrlMonControlId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4)))
_NtcAntCtrlMonControlId_Type.__name__=_E
_NtcAntCtrlMonControlId_Object=MibTableColumn
ntcAntCtrlMonControlId=_NtcAntCtrlMonControlId_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1,1,1),_NtcAntCtrlMonControlId_Type())
ntcAntCtrlMonControlId.setMaxAccess(_L)
if mibBuilder.loadTexts:ntcAntCtrlMonControlId.setStatus(_A)
class _NtcAntCtrlInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999999))
_NtcAntCtrlInterval_Type.__name__=_G
_NtcAntCtrlInterval_Object=MibTableColumn
ntcAntCtrlInterval=_NtcAntCtrlInterval_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1,1,2),_NtcAntCtrlInterval_Type())
ntcAntCtrlInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlInterval.setStatus(_A)
if mibBuilder.loadTexts:ntcAntCtrlInterval.setUnits('s')
class _NtcAntCtrlAntStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),('ok',1),('failed',2)))
_NtcAntCtrlAntStatus_Type.__name__=_E
_NtcAntCtrlAntStatus_Object=MibTableColumn
ntcAntCtrlAntStatus=_NtcAntCtrlAntStatus_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1,1,3),_NtcAntCtrlAntStatus_Type())
ntcAntCtrlAntStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlAntStatus.setStatus(_A)
class _NtcAntCtrlTxAllowed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_T,0),('on',1),('off',2)))
_NtcAntCtrlTxAllowed_Type.__name__=_E
_NtcAntCtrlTxAllowed_Object=MibTableColumn
ntcAntCtrlTxAllowed=_NtcAntCtrlTxAllowed_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1,1,4),_NtcAntCtrlTxAllowed_Type())
ntcAntCtrlTxAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlTxAllowed.setStatus(_A)
_NtcAntCtrlLatitude_Type=Float32TC
_NtcAntCtrlLatitude_Object=MibTableColumn
ntcAntCtrlLatitude=_NtcAntCtrlLatitude_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1,1,5),_NtcAntCtrlLatitude_Type())
ntcAntCtrlLatitude.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlLatitude.setStatus(_A)
if mibBuilder.loadTexts:ntcAntCtrlLatitude.setUnits(_F)
_NtcAntCtrlLongitude_Type=Float32TC
_NtcAntCtrlLongitude_Object=MibTableColumn
ntcAntCtrlLongitude=_NtcAntCtrlLongitude_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1,1,6),_NtcAntCtrlLongitude_Type())
ntcAntCtrlLongitude.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlLongitude.setStatus(_A)
if mibBuilder.loadTexts:ntcAntCtrlLongitude.setUnits(_F)
_NtcAntCtrlTxMsg_Type=Unsigned32
_NtcAntCtrlTxMsg_Object=MibTableColumn
ntcAntCtrlTxMsg=_NtcAntCtrlTxMsg_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1,1,7),_NtcAntCtrlTxMsg_Type())
ntcAntCtrlTxMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlTxMsg.setStatus(_A)
_NtcAntCtrlRxMsg_Type=Unsigned32
_NtcAntCtrlRxMsg_Object=MibTableColumn
ntcAntCtrlRxMsg=_NtcAntCtrlRxMsg_Object((1,3,6,1,4,1,5835,5,2,5700,1,2,1,1,8),_NtcAntCtrlRxMsg_Type())
ntcAntCtrlRxMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlRxMsg.setStatus(_A)
_NtcAntCtrlAlarm_ObjectIdentity=ObjectIdentity
ntcAntCtrlAlarm=_NtcAntCtrlAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5700,1,3))
if mibBuilder.loadTexts:ntcAntCtrlAlarm.setStatus(_A)
_NtcAntCtrlAlarmStatsTable_Object=MibTable
ntcAntCtrlAlarmStatsTable=_NtcAntCtrlAlarmStatsTable_Object((1,3,6,1,4,1,5835,5,2,5700,1,3,1))
if mibBuilder.loadTexts:ntcAntCtrlAlarmStatsTable.setStatus(_A)
_NtcAntCtrlAlarmStatsEntry_Object=MibTableRow
ntcAntCtrlAlarmStatsEntry=_NtcAntCtrlAlarmStatsEntry_Object((1,3,6,1,4,1,5835,5,2,5700,1,3,1,1))
ntcAntCtrlAlarmStatsEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:ntcAntCtrlAlarmStatsEntry.setStatus(_A)
class _NtcAntCtrlAlarmStatsControlId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3),(_K,4)))
_NtcAntCtrlAlarmStatsControlId_Type.__name__=_E
_NtcAntCtrlAlarmStatsControlId_Object=MibTableColumn
ntcAntCtrlAlarmStatsControlId=_NtcAntCtrlAlarmStatsControlId_Object((1,3,6,1,4,1,5835,5,2,5700,1,3,1,1,1),_NtcAntCtrlAlarmStatsControlId_Type())
ntcAntCtrlAlarmStatsControlId.setMaxAccess(_L)
if mibBuilder.loadTexts:ntcAntCtrlAlarmStatsControlId.setStatus(_A)
_NtcAntCtrlCommErrorStat_Type=NtcAlarmState
_NtcAntCtrlCommErrorStat_Object=MibTableColumn
ntcAntCtrlCommErrorStat=_NtcAntCtrlCommErrorStat_Object((1,3,6,1,4,1,5835,5,2,5700,1,3,1,1,2),_NtcAntCtrlCommErrorStat_Type())
ntcAntCtrlCommErrorStat.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlCommErrorStat.setStatus(_A)
_NtcAntCtrlAntFailureStat_Type=NtcAlarmState
_NtcAntCtrlAntFailureStat_Object=MibTableColumn
ntcAntCtrlAntFailureStat=_NtcAntCtrlAntFailureStat_Object((1,3,6,1,4,1,5835,5,2,5700,1,3,1,1,3),_NtcAntCtrlAntFailureStat_Type())
ntcAntCtrlAntFailureStat.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlAntFailureStat.setStatus(_A)
_NtcAntCtrlCommError_Type=NtcAlarmState
_NtcAntCtrlCommError_Object=MibScalar
ntcAntCtrlCommError=_NtcAntCtrlCommError_Object((1,3,6,1,4,1,5835,5,2,5700,1,3,2),_NtcAntCtrlCommError_Type())
ntcAntCtrlCommError.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlCommError.setStatus(_A)
_NtcAntCtrlAntFailure_Type=NtcAlarmState
_NtcAntCtrlAntFailure_Object=MibScalar
ntcAntCtrlAntFailure=_NtcAntCtrlAntFailure_Object((1,3,6,1,4,1,5835,5,2,5700,1,3,3),_NtcAntCtrlAntFailure_Type())
ntcAntCtrlAntFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAntCtrlAntFailure.setStatus(_A)
_NtcAntCtrlConformance_ObjectIdentity=ObjectIdentity
ntcAntCtrlConformance=_NtcAntCtrlConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5700,2))
if mibBuilder.loadTexts:ntcAntCtrlConformance.setStatus(_A)
_NtcAntCtrlConfCompliance_ObjectIdentity=ObjectIdentity
ntcAntCtrlConfCompliance=_NtcAntCtrlConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5700,2,1))
if mibBuilder.loadTexts:ntcAntCtrlConfCompliance.setStatus(_A)
_NtcAntCtrlConfGroup_ObjectIdentity=ObjectIdentity
ntcAntCtrlConfGroup=_NtcAntCtrlConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,5700,2,2))
if mibBuilder.loadTexts:ntcAntCtrlConfGroup.setStatus(_A)
ntcAntCtrlConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,5700,2,2,1))
ntcAntCtrlConfGrpV1Standard.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ntcAntCtrlConfGrpV1Standard.setStatus(_A)
ntcAntCtrlConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,5700,2,1,1))
ntcAntCtrlConfCompV1Standard.setObjects((_B,_r))
if mibBuilder.loadTexts:ntcAntCtrlConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcAntennaController':ntcAntennaController,'ntcAntCtrlObjects':ntcAntCtrlObjects,'ntcAntCtrlCfg':ntcAntCtrlCfg,'ntcAntCtrlCfgTable':ntcAntCtrlCfgTable,'ntcAntCtrlCfgEntry':ntcAntCtrlCfgEntry,_N:ntcAntCtrlCfgControlId,_V:ntcAntCtrlCfgEnable,_W:ntcAntCtrlCfgIpAddress,_X:ntcAntCtrlCfgPort,_Y:ntcAntCtrlCfgSatLong,_Z:ntcAntCtrlCfgSatLatVar,_a:ntcAntCtrlCfgSatSkew,_b:ntcAntCtrlCfgRxPol,_c:ntcAntCtrlCfgTxPol,_d:ntcAntCtrlCfgRxLoFreq,_e:ntcAntCtrlCfgTxLoFreq,_f:ntcAntCtrlCfgTxMaxSkew,'ntcAntCtrlMon':ntcAntCtrlMon,'ntcAntCtrlMonTable':ntcAntCtrlMonTable,'ntcAntCtrlMonEntry':ntcAntCtrlMonEntry,_S:ntcAntCtrlMonControlId,_g:ntcAntCtrlInterval,_h:ntcAntCtrlAntStatus,_i:ntcAntCtrlTxAllowed,_j:ntcAntCtrlLatitude,_k:ntcAntCtrlLongitude,_l:ntcAntCtrlTxMsg,_m:ntcAntCtrlRxMsg,'ntcAntCtrlAlarm':ntcAntCtrlAlarm,'ntcAntCtrlAlarmStatsTable':ntcAntCtrlAlarmStatsTable,'ntcAntCtrlAlarmStatsEntry':ntcAntCtrlAlarmStatsEntry,_U:ntcAntCtrlAlarmStatsControlId,_n:ntcAntCtrlCommErrorStat,_o:ntcAntCtrlAntFailureStat,_p:ntcAntCtrlCommError,_q:ntcAntCtrlAntFailure,'ntcAntCtrlConformance':ntcAntCtrlConformance,'ntcAntCtrlConfCompliance':ntcAntCtrlConfCompliance,'ntcAntCtrlConfCompV1Standard':ntcAntCtrlConfCompV1Standard,'ntcAntCtrlConfGroup':ntcAntCtrlConfGroup,_r:ntcAntCtrlConfGrpV1Standard})