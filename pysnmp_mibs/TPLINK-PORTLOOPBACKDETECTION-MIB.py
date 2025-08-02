_I='enable'
_H='disable'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='OctetString'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkLoopbackDetectionMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,80))
if mibBuilder.loadTexts:tplinkLoopbackDetectionMIB.setRevisions(('2009-08-27 00:00',))
_TplinkLoopbackDetectionMIBObjects_ObjectIdentity=ObjectIdentity
tplinkLoopbackDetectionMIBObjects=_TplinkLoopbackDetectionMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,80,1))
class _LoopbackDetectionEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_LoopbackDetectionEnable_Type.__name__=_B
_LoopbackDetectionEnable_Object=MibScalar
loopbackDetectionEnable=_LoopbackDetectionEnable_Object((1,3,6,1,4,1,11863,6,80,1,1),_LoopbackDetectionEnable_Type())
loopbackDetectionEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:loopbackDetectionEnable.setStatus(_A)
class _LoopbackDetectionInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_LoopbackDetectionInterval_Type.__name__=_B
_LoopbackDetectionInterval_Object=MibScalar
loopbackDetectionInterval=_LoopbackDetectionInterval_Object((1,3,6,1,4,1,11863,6,80,1,2),_LoopbackDetectionInterval_Type())
loopbackDetectionInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:loopbackDetectionInterval.setStatus(_A)
class _LoopbackDetectionRecoveryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,100000))
_LoopbackDetectionRecoveryTime_Type.__name__=_B
_LoopbackDetectionRecoveryTime_Object=MibScalar
loopbackDetectionRecoveryTime=_LoopbackDetectionRecoveryTime_Object((1,3,6,1,4,1,11863,6,80,1,3),_LoopbackDetectionRecoveryTime_Type())
loopbackDetectionRecoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:loopbackDetectionRecoveryTime.setStatus(_A)
_LoopbackDetectionCtrlTable_Object=MibTable
loopbackDetectionCtrlTable=_LoopbackDetectionCtrlTable_Object((1,3,6,1,4,1,11863,6,80,1,4))
if mibBuilder.loadTexts:loopbackDetectionCtrlTable.setStatus(_A)
_LoopbackDetectionCtrlEntry_Object=MibTableRow
loopbackDetectionCtrlEntry=_LoopbackDetectionCtrlEntry_Object((1,3,6,1,4,1,11863,6,80,1,4,1))
loopbackDetectionCtrlEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:loopbackDetectionCtrlEntry.setStatus(_A)
class _LoopbackDetectionPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LoopbackDetectionPort_Type.__name__=_D
_LoopbackDetectionPort_Object=MibTableColumn
loopbackDetectionPort=_LoopbackDetectionPort_Object((1,3,6,1,4,1,11863,6,80,1,4,1,1),_LoopbackDetectionPort_Type())
loopbackDetectionPort.setMaxAccess(_E)
if mibBuilder.loadTexts:loopbackDetectionPort.setStatus(_A)
class _LoopbackDetectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),(_I,1)))
_LoopbackDetectionState_Type.__name__=_B
_LoopbackDetectionState_Object=MibTableColumn
loopbackDetectionState=_LoopbackDetectionState_Object((1,3,6,1,4,1,11863,6,80,1,4,1,2),_LoopbackDetectionState_Type())
loopbackDetectionState.setMaxAccess(_C)
if mibBuilder.loadTexts:loopbackDetectionState.setStatus(_A)
class _LoopbackDetectionProcessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('alert',0),('portbased',1),('vlanbased',2)))
_LoopbackDetectionProcessMode_Type.__name__=_B
_LoopbackDetectionProcessMode_Object=MibTableColumn
loopbackDetectionProcessMode=_LoopbackDetectionProcessMode_Object((1,3,6,1,4,1,11863,6,80,1,4,1,3),_LoopbackDetectionProcessMode_Type())
loopbackDetectionProcessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:loopbackDetectionProcessMode.setStatus(_A)
class _LoopbackDetectionRecoverMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('auto',0),('manual',1)))
_LoopbackDetectionRecoverMode_Type.__name__=_B
_LoopbackDetectionRecoverMode_Object=MibTableColumn
loopbackDetectionRecoverMode=_LoopbackDetectionRecoverMode_Object((1,3,6,1,4,1,11863,6,80,1,4,1,4),_LoopbackDetectionRecoverMode_Type())
loopbackDetectionRecoverMode.setMaxAccess(_C)
if mibBuilder.loadTexts:loopbackDetectionRecoverMode.setStatus(_A)
class _LoopbackDetectionLoopState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LoopbackDetectionLoopState_Type.__name__=_D
_LoopbackDetectionLoopState_Object=MibTableColumn
loopbackDetectionLoopState=_LoopbackDetectionLoopState_Object((1,3,6,1,4,1,11863,6,80,1,4,1,5),_LoopbackDetectionLoopState_Type())
loopbackDetectionLoopState.setMaxAccess(_E)
if mibBuilder.loadTexts:loopbackDetectionLoopState.setStatus(_A)
class _LoopbackDetectionBlockState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LoopbackDetectionBlockState_Type.__name__=_D
_LoopbackDetectionBlockState_Object=MibTableColumn
loopbackDetectionBlockState=_LoopbackDetectionBlockState_Object((1,3,6,1,4,1,11863,6,80,1,4,1,6),_LoopbackDetectionBlockState_Type())
loopbackDetectionBlockState.setMaxAccess(_E)
if mibBuilder.loadTexts:loopbackDetectionBlockState.setStatus(_A)
class _LoopbackDetectionLagState_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LoopbackDetectionLagState_Type.__name__=_D
_LoopbackDetectionLagState_Object=MibTableColumn
loopbackDetectionLagState=_LoopbackDetectionLagState_Object((1,3,6,1,4,1,11863,6,80,1,4,1,7),_LoopbackDetectionLagState_Type())
loopbackDetectionLagState.setMaxAccess(_E)
if mibBuilder.loadTexts:loopbackDetectionLagState.setStatus(_A)
_LoopbackDetectionRecoverPort_Type=Integer32
_LoopbackDetectionRecoverPort_Object=MibTableColumn
loopbackDetectionRecoverPort=_LoopbackDetectionRecoverPort_Object((1,3,6,1,4,1,11863,6,80,1,4,1,8),_LoopbackDetectionRecoverPort_Type())
loopbackDetectionRecoverPort.setMaxAccess(_C)
if mibBuilder.loadTexts:loopbackDetectionRecoverPort.setStatus(_A)
_TplinkLoopbackDetectionNotifications_ObjectIdentity=ObjectIdentity
tplinkLoopbackDetectionNotifications=_TplinkLoopbackDetectionNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,80,2))
loopbackStatusChange=NotificationType((1,3,6,1,4,1,11863,6,80,2,1))
if mibBuilder.loadTexts:loopbackStatusChange.setStatus(_A)
mibBuilder.exportSymbols('TPLINK-PORTLOOPBACKDETECTION-MIB',**{'tplinkLoopbackDetectionMIB':tplinkLoopbackDetectionMIB,'tplinkLoopbackDetectionMIBObjects':tplinkLoopbackDetectionMIBObjects,'loopbackDetectionEnable':loopbackDetectionEnable,'loopbackDetectionInterval':loopbackDetectionInterval,'loopbackDetectionRecoveryTime':loopbackDetectionRecoveryTime,'loopbackDetectionCtrlTable':loopbackDetectionCtrlTable,'loopbackDetectionCtrlEntry':loopbackDetectionCtrlEntry,'loopbackDetectionPort':loopbackDetectionPort,'loopbackDetectionState':loopbackDetectionState,'loopbackDetectionProcessMode':loopbackDetectionProcessMode,'loopbackDetectionRecoverMode':loopbackDetectionRecoverMode,'loopbackDetectionLoopState':loopbackDetectionLoopState,'loopbackDetectionBlockState':loopbackDetectionBlockState,'loopbackDetectionLagState':loopbackDetectionLagState,'loopbackDetectionRecoverPort':loopbackDetectionRecoverPort,'tplinkLoopbackDetectionNotifications':tplinkLoopbackDetectionNotifications,'loopbackStatusChange':loopbackStatusChange})