_Q='bsveVrrpTrapStateTransitionCause'
_P='bsveVrrpTrapStateTransitionType'
_O='accessible-for-notify'
_N='vrrpOperVrId'
_M='vrrpOperPrimaryIpAddr'
_L='ipAdEntAddr'
_K='IP-MIB'
_J='ifIndex'
_I='IF-MIB'
_H='BAY-STACK-VRRP-EXT-MIB'
_G='none'
_F='read-only'
_E='VRRP-MIB'
_D='TruthValue'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ipAdEntAddr,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_D)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
vrrpOperPrimaryIpAddr,vrrpOperVrId=mibBuilder.importSymbols(_E,_M,_N)
bayStackVrrpExtMib=ModuleIdentity((1,3,6,1,4,1,45,5,11))
if mibBuilder.loadTexts:bayStackVrrpExtMib.setRevisions(('2005-07-01 00:00','2012-10-18 00:00'))
_BsveNotifications_ObjectIdentity=ObjectIdentity
bsveNotifications=_BsveNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,11,0))
_BsveObjects_ObjectIdentity=ObjectIdentity
bsveObjects=_BsveObjects_ObjectIdentity((1,3,6,1,4,1,45,5,11,1))
_BsveScalars_ObjectIdentity=ObjectIdentity
bsveScalars=_BsveScalars_ObjectIdentity((1,3,6,1,4,1,45,5,11,1,1))
_BsveVrrpEnabled_Type=TruthValue
_BsveVrrpEnabled_Object=MibScalar
bsveVrrpEnabled=_BsveVrrpEnabled_Object((1,3,6,1,4,1,45,5,11,1,1,1),_BsveVrrpEnabled_Type())
bsveVrrpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsveVrrpEnabled.setStatus(_A)
class _BsveVrrpPingVirtualAddrEnabled_Type(TruthValue):defaultValue=1
_BsveVrrpPingVirtualAddrEnabled_Type.__name__=_D
_BsveVrrpPingVirtualAddrEnabled_Object=MibScalar
bsveVrrpPingVirtualAddrEnabled=_BsveVrrpPingVirtualAddrEnabled_Object((1,3,6,1,4,1,45,5,11,1,1,2),_BsveVrrpPingVirtualAddrEnabled_Type())
bsveVrrpPingVirtualAddrEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsveVrrpPingVirtualAddrEnabled.setStatus(_A)
_BsveVrrpOperExtTable_Object=MibTable
bsveVrrpOperExtTable=_BsveVrrpOperExtTable_Object((1,3,6,1,4,1,45,5,11,1,2))
if mibBuilder.loadTexts:bsveVrrpOperExtTable.setStatus(_A)
_BsveVrrpOperExtEntry_Object=MibTableRow
bsveVrrpOperExtEntry=_BsveVrrpOperExtEntry_Object((1,3,6,1,4,1,45,5,11,1,2,1))
bsveVrrpOperExtEntry.setIndexNames((0,_I,_J),(0,_E,_N))
if mibBuilder.loadTexts:bsveVrrpOperExtEntry.setStatus(_A)
_BsveVrrpOperExtCriticalIpAddr_Type=IpAddress
_BsveVrrpOperExtCriticalIpAddr_Object=MibTableColumn
bsveVrrpOperExtCriticalIpAddr=_BsveVrrpOperExtCriticalIpAddr_Object((1,3,6,1,4,1,45,5,11,1,2,1,1),_BsveVrrpOperExtCriticalIpAddr_Type())
bsveVrrpOperExtCriticalIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bsveVrrpOperExtCriticalIpAddr.setStatus(_A)
class _BsveVrrpOperExtCriticalIpAddrEnabled_Type(TruthValue):defaultValue=2
_BsveVrrpOperExtCriticalIpAddrEnabled_Type.__name__=_D
_BsveVrrpOperExtCriticalIpAddrEnabled_Object=MibTableColumn
bsveVrrpOperExtCriticalIpAddrEnabled=_BsveVrrpOperExtCriticalIpAddrEnabled_Object((1,3,6,1,4,1,45,5,11,1,2,1,2),_BsveVrrpOperExtCriticalIpAddrEnabled_Type())
bsveVrrpOperExtCriticalIpAddrEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsveVrrpOperExtCriticalIpAddrEnabled.setStatus(_A)
class _BsveVrrpOperExtHoldDownTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,21600))
_BsveVrrpOperExtHoldDownTimer_Type.__name__=_B
_BsveVrrpOperExtHoldDownTimer_Object=MibTableColumn
bsveVrrpOperExtHoldDownTimer=_BsveVrrpOperExtHoldDownTimer_Object((1,3,6,1,4,1,45,5,11,1,2,1,3),_BsveVrrpOperExtHoldDownTimer_Type())
bsveVrrpOperExtHoldDownTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:bsveVrrpOperExtHoldDownTimer.setStatus(_A)
class _BsveVrrpOperExtHoldDownState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dormant',1),('active',2)))
_BsveVrrpOperExtHoldDownState_Type.__name__=_B
_BsveVrrpOperExtHoldDownState_Object=MibTableColumn
bsveVrrpOperExtHoldDownState=_BsveVrrpOperExtHoldDownState_Object((1,3,6,1,4,1,45,5,11,1,2,1,4),_BsveVrrpOperExtHoldDownState_Type())
bsveVrrpOperExtHoldDownState.setMaxAccess(_F)
if mibBuilder.loadTexts:bsveVrrpOperExtHoldDownState.setStatus(_A)
class _BsveVrrpOperExtHoldDownTimeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,21600))
_BsveVrrpOperExtHoldDownTimeRemaining_Type.__name__=_B
_BsveVrrpOperExtHoldDownTimeRemaining_Object=MibTableColumn
bsveVrrpOperExtHoldDownTimeRemaining=_BsveVrrpOperExtHoldDownTimeRemaining_Object((1,3,6,1,4,1,45,5,11,1,2,1,5),_BsveVrrpOperExtHoldDownTimeRemaining_Type())
bsveVrrpOperExtHoldDownTimeRemaining.setMaxAccess(_F)
if mibBuilder.loadTexts:bsveVrrpOperExtHoldDownTimeRemaining.setStatus(_A)
class _BsveVrrpOperExtAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('preemptHoldDownTimer',2)))
_BsveVrrpOperExtAction_Type.__name__=_B
_BsveVrrpOperExtAction_Object=MibTableColumn
bsveVrrpOperExtAction=_BsveVrrpOperExtAction_Object((1,3,6,1,4,1,45,5,11,1,2,1,6),_BsveVrrpOperExtAction_Type())
bsveVrrpOperExtAction.setMaxAccess(_C)
if mibBuilder.loadTexts:bsveVrrpOperExtAction.setStatus(_A)
class _BsveVrrpOperExtBackUpMasterEnabled_Type(TruthValue):defaultValue=2
_BsveVrrpOperExtBackUpMasterEnabled_Type.__name__=_D
_BsveVrrpOperExtBackUpMasterEnabled_Object=MibTableColumn
bsveVrrpOperExtBackUpMasterEnabled=_BsveVrrpOperExtBackUpMasterEnabled_Object((1,3,6,1,4,1,45,5,11,1,2,1,7),_BsveVrrpOperExtBackUpMasterEnabled_Type())
bsveVrrpOperExtBackUpMasterEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsveVrrpOperExtBackUpMasterEnabled.setStatus(_A)
class _BsveVrrpOperExtBackUpMasterState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_BsveVrrpOperExtBackUpMasterState_Type.__name__=_B
_BsveVrrpOperExtBackUpMasterState_Object=MibTableColumn
bsveVrrpOperExtBackUpMasterState=_BsveVrrpOperExtBackUpMasterState_Object((1,3,6,1,4,1,45,5,11,1,2,1,8),_BsveVrrpOperExtBackUpMasterState_Type())
bsveVrrpOperExtBackUpMasterState.setMaxAccess(_F)
if mibBuilder.loadTexts:bsveVrrpOperExtBackUpMasterState.setStatus(_A)
class _BsveVrrpOperExtFasterAdvInterval_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,1000))
_BsveVrrpOperExtFasterAdvInterval_Type.__name__=_B
_BsveVrrpOperExtFasterAdvInterval_Object=MibTableColumn
bsveVrrpOperExtFasterAdvInterval=_BsveVrrpOperExtFasterAdvInterval_Object((1,3,6,1,4,1,45,5,11,1,2,1,9),_BsveVrrpOperExtFasterAdvInterval_Type())
bsveVrrpOperExtFasterAdvInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bsveVrrpOperExtFasterAdvInterval.setStatus(_A)
class _BsveVrrpOperExtFasterAdvIntervalEnabled_Type(TruthValue):defaultValue=2
_BsveVrrpOperExtFasterAdvIntervalEnabled_Type.__name__=_D
_BsveVrrpOperExtFasterAdvIntervalEnabled_Object=MibTableColumn
bsveVrrpOperExtFasterAdvIntervalEnabled=_BsveVrrpOperExtFasterAdvIntervalEnabled_Object((1,3,6,1,4,1,45,5,11,1,2,1,10),_BsveVrrpOperExtFasterAdvIntervalEnabled_Type())
bsveVrrpOperExtFasterAdvIntervalEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bsveVrrpOperExtFasterAdvIntervalEnabled.setStatus(_A)
_BsveNotificationObjects_ObjectIdentity=ObjectIdentity
bsveNotificationObjects=_BsveNotificationObjects_ObjectIdentity((1,3,6,1,4,1,45,5,11,1,4))
class _BsveVrrpTrapStateTransitionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,1),('masterToBackup',2),('backupToMaster',3),('initializeToMaster',4),('masterToInitialize',5),('initializeToBackup',6),('backupToInitialize',7),('backupToBackUpMaster',8),('backUpMasterToBackup',9)))
_BsveVrrpTrapStateTransitionType_Type.__name__=_B
_BsveVrrpTrapStateTransitionType_Object=MibScalar
bsveVrrpTrapStateTransitionType=_BsveVrrpTrapStateTransitionType_Object((1,3,6,1,4,1,45,5,11,1,4,1),_BsveVrrpTrapStateTransitionType_Type())
bsveVrrpTrapStateTransitionType.setMaxAccess(_O)
if mibBuilder.loadTexts:bsveVrrpTrapStateTransitionType.setStatus(_A)
class _BsveVrrpTrapStateTransitionCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_G,1),('higherPriorityAdvertizeReceived',2),('shutdownReceived',3),('vrrpAddrAndPhysicalAddrMatch',4),('masterDownInterval',5),('preempted',6),('criticalIPFail',7),('usrConfig',8),('syncFromPrimary',9),('iPInterfaceDown',10),('lowerPrioAdvReceived',11),('higherSrcIPEqualPrioAdvReceived',12),('lowerSrcIPEqualPrioAdvReceived',13),('startVR',14),('other',15),('reboot',16)))
_BsveVrrpTrapStateTransitionCause_Type.__name__=_B
_BsveVrrpTrapStateTransitionCause_Object=MibScalar
bsveVrrpTrapStateTransitionCause=_BsveVrrpTrapStateTransitionCause_Object((1,3,6,1,4,1,45,5,11,1,4,2),_BsveVrrpTrapStateTransitionCause_Type())
bsveVrrpTrapStateTransitionCause.setMaxAccess(_O)
if mibBuilder.loadTexts:bsveVrrpTrapStateTransitionCause.setStatus(_A)
bsveVrrpTrapStateTransition=NotificationType((1,3,6,1,4,1,45,5,11,0,1))
bsveVrrpTrapStateTransition.setObjects(*((_H,_P),(_H,_Q),(_E,_M),(_K,_L)))
if mibBuilder.loadTexts:bsveVrrpTrapStateTransition.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'bayStackVrrpExtMib':bayStackVrrpExtMib,'bsveNotifications':bsveNotifications,'bsveVrrpTrapStateTransition':bsveVrrpTrapStateTransition,'bsveObjects':bsveObjects,'bsveScalars':bsveScalars,'bsveVrrpEnabled':bsveVrrpEnabled,'bsveVrrpPingVirtualAddrEnabled':bsveVrrpPingVirtualAddrEnabled,'bsveVrrpOperExtTable':bsveVrrpOperExtTable,'bsveVrrpOperExtEntry':bsveVrrpOperExtEntry,'bsveVrrpOperExtCriticalIpAddr':bsveVrrpOperExtCriticalIpAddr,'bsveVrrpOperExtCriticalIpAddrEnabled':bsveVrrpOperExtCriticalIpAddrEnabled,'bsveVrrpOperExtHoldDownTimer':bsveVrrpOperExtHoldDownTimer,'bsveVrrpOperExtHoldDownState':bsveVrrpOperExtHoldDownState,'bsveVrrpOperExtHoldDownTimeRemaining':bsveVrrpOperExtHoldDownTimeRemaining,'bsveVrrpOperExtAction':bsveVrrpOperExtAction,'bsveVrrpOperExtBackUpMasterEnabled':bsveVrrpOperExtBackUpMasterEnabled,'bsveVrrpOperExtBackUpMasterState':bsveVrrpOperExtBackUpMasterState,'bsveVrrpOperExtFasterAdvInterval':bsveVrrpOperExtFasterAdvInterval,'bsveVrrpOperExtFasterAdvIntervalEnabled':bsveVrrpOperExtFasterAdvIntervalEnabled,'bsveNotificationObjects':bsveNotificationObjects,_P:bsveVrrpTrapStateTransitionType,_Q:bsveVrrpTrapStateTransitionCause})