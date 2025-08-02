_z='oacAtmOamStatGeneralGroup'
_y='oacAtmOamVclOamCellsDropped'
_x='oacAtmOamVclEndCCOut'
_w='oacAtmOamVclSegCCOut'
_v='oacAtmOamVclRdiOut'
_u='oacAtmOamVclAisOut'
_t='oacAtmOamVclSegLoopOut'
_s='oacAtmOamVclEndLoopOut'
_r='oacAtmOamVclSegLoopbackOut'
_q='oacAtmOamVclEndLoopbackOut'
_p='oacAtmOamVclOamCellsSent'
_o='oacAtmOamVclEndCCIn'
_n='oacAtmOamVclSegCCIn'
_m='oacAtmOamVclRdiIn'
_l='oacAtmOamVclAisIn'
_k='oacAtmOamVclSegLoopIn'
_j='oacAtmOamVclEndLoopIn'
_i='oacAtmOamVclSegLoopbackIn'
_h='oacAtmOamVclEndLoopbackIn'
_g='oacAtmOamVclOamCellsReceived'
_f='oacAtmOamVclPvcIntrusive'
_e='oacAtmOamVclAisRdiRetryUpTimer'
_d='oacAtmOamVclAisRdiRetryDownCount'
_c='oacAtmOamVclAlarmStateLastChange'
_b='oacAtmOamVclAlarmState'
_a='oacAtmOamVclLoopbackTxRetryDownCount'
_Z='oacAtmOamVclLoopbackTxRetryUpCount'
_Y='oacAtmOamVclLoopbackTxRetryFrequency'
_X='oacAtmOamVclLoopbackTxInterval'
_W='oacAtmOamVclEndContinuityCheckEnable'
_V='oacAtmOamVclSegmentContinuityCheckEnable'
_U='oacAtmOamVclAisRdiEnable'
_T='oacAtmOamVclEndLoopback'
_S='oacAtmOamVclSegmentLoopback'
_R='oacAtmOamVclPvcManage'
_Q='oacAtmOamSwitchCurrentConnections'
_P='oacAtmOamSwitchOamCellsTransmitted'
_O='oacAtmOamSwitchOamCellsReceived'
_N='oacAtmOamSwitchEndContinuityCheckEnable'
_M='oacAtmOamSwitchSegmentContinuityCheckEnable'
_L='oacAtmOamSwitchAisRdiEnable'
_K='oacAtmOamSwitchEndLoopback'
_J='oacAtmOamSwitchSegLoopback'
_I='oacAtmOamSwitchMaxConnections'
_H='oacAtmOamVclCountersEntry'
_G='oacAtmOamVclEntry'
_F='disable'
_E='enable'
_D='Integer32'
_C='read-only'
_B='ONEACCESS-OAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVclEntry,=mibBuilder.importSymbols('ATM-MIB','atmVclEntry')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
oacExpIMAtmOamStatistics,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMAtmOamStatistics','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval','TimeStamp')
oacOamMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,673))
if mibBuilder.loadTexts:oacOamMIBModule.setRevisions(('2011-10-27 00:00','2010-07-08 00:01'))
_OacAtmOamStatObjects_ObjectIdentity=ObjectIdentity
oacAtmOamStatObjects=_OacAtmOamStatObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,2,1))
_OacAtmOamStatSwitch_ObjectIdentity=ObjectIdentity
oacAtmOamStatSwitch=_OacAtmOamStatSwitch_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,2,1,1))
_OacAtmOamSwitchMaxConnections_Type=Unsigned32
_OacAtmOamSwitchMaxConnections_Object=MibScalar
oacAtmOamSwitchMaxConnections=_OacAtmOamSwitchMaxConnections_Object((1,3,6,1,4,1,13191,10,3,2,2,1,1,1),_OacAtmOamSwitchMaxConnections_Type())
oacAtmOamSwitchMaxConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamSwitchMaxConnections.setStatus(_A)
class _OacAtmOamSwitchSegLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamSwitchSegLoopback_Type.__name__=_D
_OacAtmOamSwitchSegLoopback_Object=MibScalar
oacAtmOamSwitchSegLoopback=_OacAtmOamSwitchSegLoopback_Object((1,3,6,1,4,1,13191,10,3,2,2,1,1,2),_OacAtmOamSwitchSegLoopback_Type())
oacAtmOamSwitchSegLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamSwitchSegLoopback.setStatus(_A)
class _OacAtmOamSwitchEndLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamSwitchEndLoopback_Type.__name__=_D
_OacAtmOamSwitchEndLoopback_Object=MibScalar
oacAtmOamSwitchEndLoopback=_OacAtmOamSwitchEndLoopback_Object((1,3,6,1,4,1,13191,10,3,2,2,1,1,3),_OacAtmOamSwitchEndLoopback_Type())
oacAtmOamSwitchEndLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamSwitchEndLoopback.setStatus(_A)
class _OacAtmOamSwitchAisRdiEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamSwitchAisRdiEnable_Type.__name__=_D
_OacAtmOamSwitchAisRdiEnable_Object=MibScalar
oacAtmOamSwitchAisRdiEnable=_OacAtmOamSwitchAisRdiEnable_Object((1,3,6,1,4,1,13191,10,3,2,2,1,1,4),_OacAtmOamSwitchAisRdiEnable_Type())
oacAtmOamSwitchAisRdiEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamSwitchAisRdiEnable.setStatus(_A)
class _OacAtmOamSwitchSegmentContinuityCheckEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamSwitchSegmentContinuityCheckEnable_Type.__name__=_D
_OacAtmOamSwitchSegmentContinuityCheckEnable_Object=MibScalar
oacAtmOamSwitchSegmentContinuityCheckEnable=_OacAtmOamSwitchSegmentContinuityCheckEnable_Object((1,3,6,1,4,1,13191,10,3,2,2,1,1,5),_OacAtmOamSwitchSegmentContinuityCheckEnable_Type())
oacAtmOamSwitchSegmentContinuityCheckEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamSwitchSegmentContinuityCheckEnable.setStatus(_A)
class _OacAtmOamSwitchEndContinuityCheckEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamSwitchEndContinuityCheckEnable_Type.__name__=_D
_OacAtmOamSwitchEndContinuityCheckEnable_Object=MibScalar
oacAtmOamSwitchEndContinuityCheckEnable=_OacAtmOamSwitchEndContinuityCheckEnable_Object((1,3,6,1,4,1,13191,10,3,2,2,1,1,6),_OacAtmOamSwitchEndContinuityCheckEnable_Type())
oacAtmOamSwitchEndContinuityCheckEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamSwitchEndContinuityCheckEnable.setStatus(_A)
_OacAtmOamSwitchOamCellsReceived_Type=Counter32
_OacAtmOamSwitchOamCellsReceived_Object=MibScalar
oacAtmOamSwitchOamCellsReceived=_OacAtmOamSwitchOamCellsReceived_Object((1,3,6,1,4,1,13191,10,3,2,2,1,1,7),_OacAtmOamSwitchOamCellsReceived_Type())
oacAtmOamSwitchOamCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamSwitchOamCellsReceived.setStatus(_A)
_OacAtmOamSwitchOamCellsTransmitted_Type=Counter32
_OacAtmOamSwitchOamCellsTransmitted_Object=MibScalar
oacAtmOamSwitchOamCellsTransmitted=_OacAtmOamSwitchOamCellsTransmitted_Object((1,3,6,1,4,1,13191,10,3,2,2,1,1,8),_OacAtmOamSwitchOamCellsTransmitted_Type())
oacAtmOamSwitchOamCellsTransmitted.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamSwitchOamCellsTransmitted.setStatus(_A)
_OacAtmOamSwitchCurrentConnections_Type=Unsigned32
_OacAtmOamSwitchCurrentConnections_Object=MibScalar
oacAtmOamSwitchCurrentConnections=_OacAtmOamSwitchCurrentConnections_Object((1,3,6,1,4,1,13191,10,3,2,2,1,1,9),_OacAtmOamSwitchCurrentConnections_Type())
oacAtmOamSwitchCurrentConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamSwitchCurrentConnections.setStatus(_A)
_OacAtmOamVclTable_Object=MibTable
oacAtmOamVclTable=_OacAtmOamVclTable_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2))
if mibBuilder.loadTexts:oacAtmOamVclTable.setStatus(_A)
_OacAtmOamVclEntry_Object=MibTableRow
oacAtmOamVclEntry=_OacAtmOamVclEntry_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1))
if mibBuilder.loadTexts:oacAtmOamVclEntry.setStatus(_A)
class _OacAtmOamVclPvcManage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamVclPvcManage_Type.__name__=_D
_OacAtmOamVclPvcManage_Object=MibTableColumn
oacAtmOamVclPvcManage=_OacAtmOamVclPvcManage_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,1),_OacAtmOamVclPvcManage_Type())
oacAtmOamVclPvcManage.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclPvcManage.setStatus(_A)
class _OacAtmOamVclSegmentLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamVclSegmentLoopback_Type.__name__=_D
_OacAtmOamVclSegmentLoopback_Object=MibTableColumn
oacAtmOamVclSegmentLoopback=_OacAtmOamVclSegmentLoopback_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,2),_OacAtmOamVclSegmentLoopback_Type())
oacAtmOamVclSegmentLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclSegmentLoopback.setStatus(_A)
class _OacAtmOamVclEndLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamVclEndLoopback_Type.__name__=_D
_OacAtmOamVclEndLoopback_Object=MibTableColumn
oacAtmOamVclEndLoopback=_OacAtmOamVclEndLoopback_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,3),_OacAtmOamVclEndLoopback_Type())
oacAtmOamVclEndLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclEndLoopback.setStatus(_A)
class _OacAtmOamVclAisRdiEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamVclAisRdiEnable_Type.__name__=_D
_OacAtmOamVclAisRdiEnable_Object=MibTableColumn
oacAtmOamVclAisRdiEnable=_OacAtmOamVclAisRdiEnable_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,4),_OacAtmOamVclAisRdiEnable_Type())
oacAtmOamVclAisRdiEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclAisRdiEnable.setStatus(_A)
class _OacAtmOamVclSegmentContinuityCheckEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamVclSegmentContinuityCheckEnable_Type.__name__=_D
_OacAtmOamVclSegmentContinuityCheckEnable_Object=MibTableColumn
oacAtmOamVclSegmentContinuityCheckEnable=_OacAtmOamVclSegmentContinuityCheckEnable_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,5),_OacAtmOamVclSegmentContinuityCheckEnable_Type())
oacAtmOamVclSegmentContinuityCheckEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclSegmentContinuityCheckEnable.setStatus(_A)
class _OacAtmOamVclEndContinuityCheckEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamVclEndContinuityCheckEnable_Type.__name__=_D
_OacAtmOamVclEndContinuityCheckEnable_Object=MibTableColumn
oacAtmOamVclEndContinuityCheckEnable=_OacAtmOamVclEndContinuityCheckEnable_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,6),_OacAtmOamVclEndContinuityCheckEnable_Type())
oacAtmOamVclEndContinuityCheckEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclEndContinuityCheckEnable.setStatus(_A)
_OacAtmOamVclLoopbackTxInterval_Type=Integer32
_OacAtmOamVclLoopbackTxInterval_Object=MibTableColumn
oacAtmOamVclLoopbackTxInterval=_OacAtmOamVclLoopbackTxInterval_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,7),_OacAtmOamVclLoopbackTxInterval_Type())
oacAtmOamVclLoopbackTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclLoopbackTxInterval.setStatus(_A)
_OacAtmOamVclLoopbackTxRetryFrequency_Type=Integer32
_OacAtmOamVclLoopbackTxRetryFrequency_Object=MibTableColumn
oacAtmOamVclLoopbackTxRetryFrequency=_OacAtmOamVclLoopbackTxRetryFrequency_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,8),_OacAtmOamVclLoopbackTxRetryFrequency_Type())
oacAtmOamVclLoopbackTxRetryFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclLoopbackTxRetryFrequency.setStatus(_A)
_OacAtmOamVclLoopbackTxRetryUpCount_Type=Integer32
_OacAtmOamVclLoopbackTxRetryUpCount_Object=MibTableColumn
oacAtmOamVclLoopbackTxRetryUpCount=_OacAtmOamVclLoopbackTxRetryUpCount_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,9),_OacAtmOamVclLoopbackTxRetryUpCount_Type())
oacAtmOamVclLoopbackTxRetryUpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclLoopbackTxRetryUpCount.setStatus(_A)
_OacAtmOamVclLoopbackTxRetryDownCount_Type=Integer32
_OacAtmOamVclLoopbackTxRetryDownCount_Object=MibTableColumn
oacAtmOamVclLoopbackTxRetryDownCount=_OacAtmOamVclLoopbackTxRetryDownCount_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,10),_OacAtmOamVclLoopbackTxRetryDownCount_Type())
oacAtmOamVclLoopbackTxRetryDownCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclLoopbackTxRetryDownCount.setStatus(_A)
_OacAtmOamVclAlarmState_Type=Integer32
_OacAtmOamVclAlarmState_Object=MibTableColumn
oacAtmOamVclAlarmState=_OacAtmOamVclAlarmState_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,11),_OacAtmOamVclAlarmState_Type())
oacAtmOamVclAlarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclAlarmState.setStatus(_A)
_OacAtmOamVclAlarmStateLastChange_Type=TimeStamp
_OacAtmOamVclAlarmStateLastChange_Object=MibTableColumn
oacAtmOamVclAlarmStateLastChange=_OacAtmOamVclAlarmStateLastChange_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,12),_OacAtmOamVclAlarmStateLastChange_Type())
oacAtmOamVclAlarmStateLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclAlarmStateLastChange.setStatus(_A)
_OacAtmOamVclAisRdiRetryDownCount_Type=Integer32
_OacAtmOamVclAisRdiRetryDownCount_Object=MibTableColumn
oacAtmOamVclAisRdiRetryDownCount=_OacAtmOamVclAisRdiRetryDownCount_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,13),_OacAtmOamVclAisRdiRetryDownCount_Type())
oacAtmOamVclAisRdiRetryDownCount.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclAisRdiRetryDownCount.setStatus(_A)
_OacAtmOamVclAisRdiRetryUpTimer_Type=Integer32
_OacAtmOamVclAisRdiRetryUpTimer_Object=MibTableColumn
oacAtmOamVclAisRdiRetryUpTimer=_OacAtmOamVclAisRdiRetryUpTimer_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,14),_OacAtmOamVclAisRdiRetryUpTimer_Type())
oacAtmOamVclAisRdiRetryUpTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclAisRdiRetryUpTimer.setStatus(_A)
class _OacAtmOamVclPvcIntrusive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_OacAtmOamVclPvcIntrusive_Type.__name__=_D
_OacAtmOamVclPvcIntrusive_Object=MibTableColumn
oacAtmOamVclPvcIntrusive=_OacAtmOamVclPvcIntrusive_Object((1,3,6,1,4,1,13191,10,3,2,2,1,2,1,15),_OacAtmOamVclPvcIntrusive_Type())
oacAtmOamVclPvcIntrusive.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclPvcIntrusive.setStatus(_A)
_OacAtmOamVclCountersTable_Object=MibTable
oacAtmOamVclCountersTable=_OacAtmOamVclCountersTable_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3))
if mibBuilder.loadTexts:oacAtmOamVclCountersTable.setStatus(_A)
_OacAtmOamVclCountersEntry_Object=MibTableRow
oacAtmOamVclCountersEntry=_OacAtmOamVclCountersEntry_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1))
if mibBuilder.loadTexts:oacAtmOamVclCountersEntry.setStatus(_A)
_OacAtmOamVclOamCellsReceived_Type=Counter32
_OacAtmOamVclOamCellsReceived_Object=MibTableColumn
oacAtmOamVclOamCellsReceived=_OacAtmOamVclOamCellsReceived_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,1),_OacAtmOamVclOamCellsReceived_Type())
oacAtmOamVclOamCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclOamCellsReceived.setStatus(_A)
_OacAtmOamVclEndLoopbackIn_Type=Counter32
_OacAtmOamVclEndLoopbackIn_Object=MibTableColumn
oacAtmOamVclEndLoopbackIn=_OacAtmOamVclEndLoopbackIn_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,2),_OacAtmOamVclEndLoopbackIn_Type())
oacAtmOamVclEndLoopbackIn.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclEndLoopbackIn.setStatus(_A)
_OacAtmOamVclSegLoopbackIn_Type=Counter32
_OacAtmOamVclSegLoopbackIn_Object=MibTableColumn
oacAtmOamVclSegLoopbackIn=_OacAtmOamVclSegLoopbackIn_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,3),_OacAtmOamVclSegLoopbackIn_Type())
oacAtmOamVclSegLoopbackIn.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclSegLoopbackIn.setStatus(_A)
_OacAtmOamVclEndLoopIn_Type=Counter32
_OacAtmOamVclEndLoopIn_Object=MibTableColumn
oacAtmOamVclEndLoopIn=_OacAtmOamVclEndLoopIn_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,4),_OacAtmOamVclEndLoopIn_Type())
oacAtmOamVclEndLoopIn.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclEndLoopIn.setStatus(_A)
_OacAtmOamVclSegLoopIn_Type=Counter32
_OacAtmOamVclSegLoopIn_Object=MibTableColumn
oacAtmOamVclSegLoopIn=_OacAtmOamVclSegLoopIn_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,5),_OacAtmOamVclSegLoopIn_Type())
oacAtmOamVclSegLoopIn.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclSegLoopIn.setStatus(_A)
_OacAtmOamVclAisIn_Type=Counter32
_OacAtmOamVclAisIn_Object=MibTableColumn
oacAtmOamVclAisIn=_OacAtmOamVclAisIn_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,6),_OacAtmOamVclAisIn_Type())
oacAtmOamVclAisIn.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclAisIn.setStatus(_A)
_OacAtmOamVclRdiIn_Type=Counter32
_OacAtmOamVclRdiIn_Object=MibTableColumn
oacAtmOamVclRdiIn=_OacAtmOamVclRdiIn_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,7),_OacAtmOamVclRdiIn_Type())
oacAtmOamVclRdiIn.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclRdiIn.setStatus(_A)
_OacAtmOamVclSegCCIn_Type=Counter32
_OacAtmOamVclSegCCIn_Object=MibTableColumn
oacAtmOamVclSegCCIn=_OacAtmOamVclSegCCIn_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,8),_OacAtmOamVclSegCCIn_Type())
oacAtmOamVclSegCCIn.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclSegCCIn.setStatus(_A)
_OacAtmOamVclEndCCIn_Type=Counter32
_OacAtmOamVclEndCCIn_Object=MibTableColumn
oacAtmOamVclEndCCIn=_OacAtmOamVclEndCCIn_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,9),_OacAtmOamVclEndCCIn_Type())
oacAtmOamVclEndCCIn.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclEndCCIn.setStatus(_A)
_OacAtmOamVclOamCellsSent_Type=Counter32
_OacAtmOamVclOamCellsSent_Object=MibTableColumn
oacAtmOamVclOamCellsSent=_OacAtmOamVclOamCellsSent_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,10),_OacAtmOamVclOamCellsSent_Type())
oacAtmOamVclOamCellsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclOamCellsSent.setStatus(_A)
_OacAtmOamVclEndLoopbackOut_Type=Counter32
_OacAtmOamVclEndLoopbackOut_Object=MibTableColumn
oacAtmOamVclEndLoopbackOut=_OacAtmOamVclEndLoopbackOut_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,11),_OacAtmOamVclEndLoopbackOut_Type())
oacAtmOamVclEndLoopbackOut.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclEndLoopbackOut.setStatus(_A)
_OacAtmOamVclSegLoopbackOut_Type=Counter32
_OacAtmOamVclSegLoopbackOut_Object=MibTableColumn
oacAtmOamVclSegLoopbackOut=_OacAtmOamVclSegLoopbackOut_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,12),_OacAtmOamVclSegLoopbackOut_Type())
oacAtmOamVclSegLoopbackOut.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclSegLoopbackOut.setStatus(_A)
_OacAtmOamVclEndLoopOut_Type=Counter32
_OacAtmOamVclEndLoopOut_Object=MibTableColumn
oacAtmOamVclEndLoopOut=_OacAtmOamVclEndLoopOut_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,13),_OacAtmOamVclEndLoopOut_Type())
oacAtmOamVclEndLoopOut.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclEndLoopOut.setStatus(_A)
_OacAtmOamVclSegLoopOut_Type=Counter32
_OacAtmOamVclSegLoopOut_Object=MibTableColumn
oacAtmOamVclSegLoopOut=_OacAtmOamVclSegLoopOut_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,14),_OacAtmOamVclSegLoopOut_Type())
oacAtmOamVclSegLoopOut.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclSegLoopOut.setStatus(_A)
_OacAtmOamVclAisOut_Type=Counter32
_OacAtmOamVclAisOut_Object=MibTableColumn
oacAtmOamVclAisOut=_OacAtmOamVclAisOut_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,15),_OacAtmOamVclAisOut_Type())
oacAtmOamVclAisOut.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclAisOut.setStatus(_A)
_OacAtmOamVclRdiOut_Type=Counter32
_OacAtmOamVclRdiOut_Object=MibTableColumn
oacAtmOamVclRdiOut=_OacAtmOamVclRdiOut_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,16),_OacAtmOamVclRdiOut_Type())
oacAtmOamVclRdiOut.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclRdiOut.setStatus(_A)
_OacAtmOamVclSegCCOut_Type=Counter32
_OacAtmOamVclSegCCOut_Object=MibTableColumn
oacAtmOamVclSegCCOut=_OacAtmOamVclSegCCOut_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,17),_OacAtmOamVclSegCCOut_Type())
oacAtmOamVclSegCCOut.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclSegCCOut.setStatus(_A)
_OacAtmOamVclEndCCOut_Type=Counter32
_OacAtmOamVclEndCCOut_Object=MibTableColumn
oacAtmOamVclEndCCOut=_OacAtmOamVclEndCCOut_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,18),_OacAtmOamVclEndCCOut_Type())
oacAtmOamVclEndCCOut.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclEndCCOut.setStatus(_A)
_OacAtmOamVclOamCellsDropped_Type=Counter32
_OacAtmOamVclOamCellsDropped_Object=MibTableColumn
oacAtmOamVclOamCellsDropped=_OacAtmOamVclOamCellsDropped_Object((1,3,6,1,4,1,13191,10,3,2,2,1,3,1,19),_OacAtmOamVclOamCellsDropped_Type())
oacAtmOamVclOamCellsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:oacAtmOamVclOamCellsDropped.setStatus(_A)
_OacAtmOamStatNotifications_ObjectIdentity=ObjectIdentity
oacAtmOamStatNotifications=_OacAtmOamStatNotifications_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,2,2))
_OacAtmOamStatConformance_ObjectIdentity=ObjectIdentity
oacAtmOamStatConformance=_OacAtmOamStatConformance_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,2,3))
_OacAtmOamStatGroups_ObjectIdentity=ObjectIdentity
oacAtmOamStatGroups=_OacAtmOamStatGroups_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,2,3,1))
_OacAtmOamStatCompliances_ObjectIdentity=ObjectIdentity
oacAtmOamStatCompliances=_OacAtmOamStatCompliances_ObjectIdentity((1,3,6,1,4,1,13191,10,3,2,2,3,2))
atmVclEntry.registerAugmentions((_B,_G))
oacAtmOamVclEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVclEntry.registerAugmentions((_B,_H))
oacAtmOamVclCountersEntry.setIndexNames(*atmVclEntry.getIndexNames())
oacAtmOamStatGeneralGroup=ObjectGroup((1,3,6,1,4,1,13191,10,3,2,2,3,1,1))
oacAtmOamStatGeneralGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:oacAtmOamStatGeneralGroup.setStatus(_A)
oacAtmOamStatCompliance=ModuleCompliance((1,3,6,1,4,1,13191,10,3,2,2,3,2,1))
oacAtmOamStatCompliance.setObjects((_B,_z))
if mibBuilder.loadTexts:oacAtmOamStatCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oacOamMIBModule':oacOamMIBModule,'oacAtmOamStatObjects':oacAtmOamStatObjects,'oacAtmOamStatSwitch':oacAtmOamStatSwitch,_I:oacAtmOamSwitchMaxConnections,_J:oacAtmOamSwitchSegLoopback,_K:oacAtmOamSwitchEndLoopback,_L:oacAtmOamSwitchAisRdiEnable,_M:oacAtmOamSwitchSegmentContinuityCheckEnable,_N:oacAtmOamSwitchEndContinuityCheckEnable,_O:oacAtmOamSwitchOamCellsReceived,_P:oacAtmOamSwitchOamCellsTransmitted,_Q:oacAtmOamSwitchCurrentConnections,'oacAtmOamVclTable':oacAtmOamVclTable,_G:oacAtmOamVclEntry,_R:oacAtmOamVclPvcManage,_S:oacAtmOamVclSegmentLoopback,_T:oacAtmOamVclEndLoopback,_U:oacAtmOamVclAisRdiEnable,_V:oacAtmOamVclSegmentContinuityCheckEnable,_W:oacAtmOamVclEndContinuityCheckEnable,_X:oacAtmOamVclLoopbackTxInterval,_Y:oacAtmOamVclLoopbackTxRetryFrequency,_Z:oacAtmOamVclLoopbackTxRetryUpCount,_a:oacAtmOamVclLoopbackTxRetryDownCount,_b:oacAtmOamVclAlarmState,_c:oacAtmOamVclAlarmStateLastChange,_d:oacAtmOamVclAisRdiRetryDownCount,_e:oacAtmOamVclAisRdiRetryUpTimer,_f:oacAtmOamVclPvcIntrusive,'oacAtmOamVclCountersTable':oacAtmOamVclCountersTable,_H:oacAtmOamVclCountersEntry,_g:oacAtmOamVclOamCellsReceived,_h:oacAtmOamVclEndLoopbackIn,_i:oacAtmOamVclSegLoopbackIn,_j:oacAtmOamVclEndLoopIn,_k:oacAtmOamVclSegLoopIn,_l:oacAtmOamVclAisIn,_m:oacAtmOamVclRdiIn,_n:oacAtmOamVclSegCCIn,_o:oacAtmOamVclEndCCIn,_p:oacAtmOamVclOamCellsSent,_q:oacAtmOamVclEndLoopbackOut,_r:oacAtmOamVclSegLoopbackOut,_s:oacAtmOamVclEndLoopOut,_t:oacAtmOamVclSegLoopOut,_u:oacAtmOamVclAisOut,_v:oacAtmOamVclRdiOut,_w:oacAtmOamVclSegCCOut,_x:oacAtmOamVclEndCCOut,_y:oacAtmOamVclOamCellsDropped,'oacAtmOamStatNotifications':oacAtmOamStatNotifications,'oacAtmOamStatConformance':oacAtmOamStatConformance,'oacAtmOamStatGroups':oacAtmOamStatGroups,_z:oacAtmOamStatGeneralGroup,'oacAtmOamStatCompliances':oacAtmOamStatCompliances,'oacAtmOamStatCompliance':oacAtmOamStatCompliance})