_A0='tmnxApsNotificationsV9v0Group'
_z='tmnxApsGroupCommandV9v0Group'
_y='tmnxApsNotifications'
_x='tApsPrimaryChannelChange'
_w='tApsChanTxLaisStateChange'
_v='tApsMcApsCtlLinkStateChange'
_u='tApsAnnexBCommandSwitch'
_t='tApsRdiAlarmGeneration'
_s='tApsLineSDHoldTime'
_r='tApsLineSFHoldTime'
_q='tApsProtectionType'
_p='tApsMcHoldTime'
_o='tApsMcAdvertiseInterval'
_n='tApsMcNeighborAddr'
_m='tApsMcNeighborAddrType'
_l='tApsExerciseCommandResult'
_k='tApsGroupCommandEntry'
_j='tApsConfigEntry'
_i='tApsMcStatusEntry'
_h='tApsMcConfigEntry'
_g='tApsChanStatusEntry'
_f='tApsCommandEntry'
_e='InetAddress'
_d='apsStatusSwitchedChannel'
_c='apsStatusK1K2Trans'
_b='apsStatusK1K2Rcv'
_a='tmnxApsConfigV8v0Group'
_Z='tApsRemoteSwitchCommandClear'
_Y='tApsRemoteSwitchCommandSet'
_X='tApsLocalSwitchCommandClear'
_W='tApsLocalSwitchCommandSet'
_V='tApsFEPLFClear'
_U='tApsPSBFClear'
_T='tApsChannelMismatchClear'
_S='tApsModeMismatchClear'
_R='tApsMcApsCtlLinkState'
_Q='tApsChanTxLaisState'
_P='read-only'
_O='tmnxApsConfigGroup'
_N='deciseconds'
_M='tmnxApsNotificationsV4v0'
_L='tmnxApsMcGroup'
_K='obsolete'
_J='Unsigned32'
_I='apsStatusCurrent'
_H='apsCommandSwitch'
_G='tmnxApsChanStatus'
_F='tmnxApsSwitchCommand'
_E='Integer32'
_D='read-write'
_C='APS-MIB'
_B='current'
_A='TIMETRA-APS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
apsChanConfigEntry,apsCommandEntry,apsCommandSwitch,apsConfigEntry,apsStatusCurrent,apsStatusK1K2Rcv,apsStatusK1K2Trans,apsStatusSwitchedChannel=mibBuilder.importSymbols(_C,'apsChanConfigEntry','apsCommandEntry',_H,'apsConfigEntry',_I,_b,_c,_d)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_e,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
timetraAPSMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,29))
if mibBuilder.loadTexts:timetraAPSMIBModule.setRevisions(('2011-02-01 00:00','2006-03-23 00:00','2005-08-31 00:00','2005-01-24 00:00','2004-10-28 00:00'))
_TApsMIBConformance_ObjectIdentity=ObjectIdentity
tApsMIBConformance=_TApsMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,29))
_TmnxApsMIBCompliances_ObjectIdentity=ObjectIdentity
tmnxApsMIBCompliances=_TmnxApsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,29,1))
_TmnxApsMIBGroups_ObjectIdentity=ObjectIdentity
tmnxApsMIBGroups=_TmnxApsMIBGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,29,2))
_TApsMIBObjs_ObjectIdentity=ObjectIdentity
tApsMIBObjs=_TApsMIBObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,29))
_TApsCommandTable_Object=MibTable
tApsCommandTable=_TApsCommandTable_Object((1,3,6,1,4,1,6527,3,1,2,29,1))
if mibBuilder.loadTexts:tApsCommandTable.setStatus(_B)
_TApsCommandEntry_Object=MibTableRow
tApsCommandEntry=_TApsCommandEntry_Object((1,3,6,1,4,1,6527,3,1,2,29,1,1))
if mibBuilder.loadTexts:tApsCommandEntry.setStatus(_B)
class _TApsExerciseCommandResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('passed',1),('failed',2),('preempted',3),('unknown',4)))
_TApsExerciseCommandResult_Type.__name__=_E
_TApsExerciseCommandResult_Object=MibTableColumn
tApsExerciseCommandResult=_TApsExerciseCommandResult_Object((1,3,6,1,4,1,6527,3,1,2,29,1,1,1),_TApsExerciseCommandResult_Type())
tApsExerciseCommandResult.setMaxAccess(_P)
if mibBuilder.loadTexts:tApsExerciseCommandResult.setStatus(_B)
_TApsChanStatusTable_Object=MibTable
tApsChanStatusTable=_TApsChanStatusTable_Object((1,3,6,1,4,1,6527,3,1,2,29,2))
if mibBuilder.loadTexts:tApsChanStatusTable.setStatus(_B)
_TApsChanStatusEntry_Object=MibTableRow
tApsChanStatusEntry=_TApsChanStatusEntry_Object((1,3,6,1,4,1,6527,3,1,2,29,2,1))
if mibBuilder.loadTexts:tApsChanStatusEntry.setStatus(_B)
class _TApsChanTxLaisState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('clear',0),('momentary',1),('persistent',2)))
_TApsChanTxLaisState_Type.__name__=_E
_TApsChanTxLaisState_Object=MibTableColumn
tApsChanTxLaisState=_TApsChanTxLaisState_Object((1,3,6,1,4,1,6527,3,1,2,29,2,1,1),_TApsChanTxLaisState_Type())
tApsChanTxLaisState.setMaxAccess(_P)
if mibBuilder.loadTexts:tApsChanTxLaisState.setStatus(_B)
_TApsMcConfigTable_Object=MibTable
tApsMcConfigTable=_TApsMcConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,29,3))
if mibBuilder.loadTexts:tApsMcConfigTable.setStatus(_B)
_TApsMcConfigEntry_Object=MibTableRow
tApsMcConfigEntry=_TApsMcConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,29,3,1))
if mibBuilder.loadTexts:tApsMcConfigEntry.setStatus(_B)
_TApsMcNeighborAddrType_Type=InetAddressType
_TApsMcNeighborAddrType_Object=MibTableColumn
tApsMcNeighborAddrType=_TApsMcNeighborAddrType_Object((1,3,6,1,4,1,6527,3,1,2,29,3,1,1),_TApsMcNeighborAddrType_Type())
tApsMcNeighborAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tApsMcNeighborAddrType.setStatus(_B)
class _TApsMcNeighborAddr_Type(InetAddress):defaultHexValue='00000000000000000000000000000000';subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_TApsMcNeighborAddr_Type.__name__=_e
_TApsMcNeighborAddr_Object=MibTableColumn
tApsMcNeighborAddr=_TApsMcNeighborAddr_Object((1,3,6,1,4,1,6527,3,1,2,29,3,1,2),_TApsMcNeighborAddr_Type())
tApsMcNeighborAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tApsMcNeighborAddr.setStatus(_B)
class _TApsMcAdvertiseInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,650))
_TApsMcAdvertiseInterval_Type.__name__=_J
_TApsMcAdvertiseInterval_Object=MibTableColumn
tApsMcAdvertiseInterval=_TApsMcAdvertiseInterval_Object((1,3,6,1,4,1,6527,3,1,2,29,3,1,3),_TApsMcAdvertiseInterval_Type())
tApsMcAdvertiseInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tApsMcAdvertiseInterval.setStatus(_B)
if mibBuilder.loadTexts:tApsMcAdvertiseInterval.setUnits(_N)
class _TApsMcHoldTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,650))
_TApsMcHoldTime_Type.__name__=_J
_TApsMcHoldTime_Object=MibTableColumn
tApsMcHoldTime=_TApsMcHoldTime_Object((1,3,6,1,4,1,6527,3,1,2,29,3,1,4),_TApsMcHoldTime_Type())
tApsMcHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tApsMcHoldTime.setStatus(_B)
if mibBuilder.loadTexts:tApsMcHoldTime.setUnits(_N)
_TApsMcStatusTable_Object=MibTable
tApsMcStatusTable=_TApsMcStatusTable_Object((1,3,6,1,4,1,6527,3,1,2,29,4))
if mibBuilder.loadTexts:tApsMcStatusTable.setStatus(_B)
_TApsMcStatusEntry_Object=MibTableRow
tApsMcStatusEntry=_TApsMcStatusEntry_Object((1,3,6,1,4,1,6527,3,1,2,29,4,1))
if mibBuilder.loadTexts:tApsMcStatusEntry.setStatus(_B)
class _TApsMcApsCtlLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('up',0),('dnSignalingFailure',1),('dnIncompatibleNbr',2)))
_TApsMcApsCtlLinkState_Type.__name__=_E
_TApsMcApsCtlLinkState_Object=MibTableColumn
tApsMcApsCtlLinkState=_TApsMcApsCtlLinkState_Object((1,3,6,1,4,1,6527,3,1,2,29,4,1,1),_TApsMcApsCtlLinkState_Type())
tApsMcApsCtlLinkState.setMaxAccess(_P)
if mibBuilder.loadTexts:tApsMcApsCtlLinkState.setStatus(_B)
_TApsConfigTable_Object=MibTable
tApsConfigTable=_TApsConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,29,5))
if mibBuilder.loadTexts:tApsConfigTable.setStatus(_B)
_TApsConfigEntry_Object=MibTableRow
tApsConfigEntry=_TApsConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,29,5,1))
if mibBuilder.loadTexts:tApsConfigEntry.setStatus(_B)
class _TApsProtectionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('onePlusOneSignalling',1),('onePlusOne',2)))
_TApsProtectionType_Type.__name__=_E
_TApsProtectionType_Object=MibTableColumn
tApsProtectionType=_TApsProtectionType_Object((1,3,6,1,4,1,6527,3,1,2,29,5,1,1),_TApsProtectionType_Type())
tApsProtectionType.setMaxAccess(_D)
if mibBuilder.loadTexts:tApsProtectionType.setStatus(_B)
class _TApsLineSFHoldTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TApsLineSFHoldTime_Type.__name__=_J
_TApsLineSFHoldTime_Object=MibTableColumn
tApsLineSFHoldTime=_TApsLineSFHoldTime_Object((1,3,6,1,4,1,6527,3,1,2,29,5,1,2),_TApsLineSFHoldTime_Type())
tApsLineSFHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tApsLineSFHoldTime.setStatus(_B)
if mibBuilder.loadTexts:tApsLineSFHoldTime.setUnits(_N)
class _TApsLineSDHoldTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TApsLineSDHoldTime_Type.__name__=_J
_TApsLineSDHoldTime_Object=MibTableColumn
tApsLineSDHoldTime=_TApsLineSDHoldTime_Object((1,3,6,1,4,1,6527,3,1,2,29,5,1,3),_TApsLineSDHoldTime_Type())
tApsLineSDHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tApsLineSDHoldTime.setStatus(_B)
if mibBuilder.loadTexts:tApsLineSDHoldTime.setUnits(_N)
class _TApsRdiAlarmGeneration_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('suppress',0),('circuit',1)))
_TApsRdiAlarmGeneration_Type.__name__=_E
_TApsRdiAlarmGeneration_Object=MibTableColumn
tApsRdiAlarmGeneration=_TApsRdiAlarmGeneration_Object((1,3,6,1,4,1,6527,3,1,2,29,5,1,4),_TApsRdiAlarmGeneration_Type())
tApsRdiAlarmGeneration.setMaxAccess(_D)
if mibBuilder.loadTexts:tApsRdiAlarmGeneration.setStatus(_B)
_TApsGroupCommandTable_Object=MibTable
tApsGroupCommandTable=_TApsGroupCommandTable_Object((1,3,6,1,4,1,6527,3,1,2,29,6))
if mibBuilder.loadTexts:tApsGroupCommandTable.setStatus(_B)
_TApsGroupCommandEntry_Object=MibTableRow
tApsGroupCommandEntry=_TApsGroupCommandEntry_Object((1,3,6,1,4,1,6527,3,1,2,29,6,1))
if mibBuilder.loadTexts:tApsGroupCommandEntry.setStatus(_B)
class _TApsAnnexBCommandSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noCmd',1),('lockout',2),('clearLockout',3)))
_TApsAnnexBCommandSwitch_Type.__name__=_E
_TApsAnnexBCommandSwitch_Object=MibTableColumn
tApsAnnexBCommandSwitch=_TApsAnnexBCommandSwitch_Object((1,3,6,1,4,1,6527,3,1,2,29,6,1,1),_TApsAnnexBCommandSwitch_Type())
tApsAnnexBCommandSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:tApsAnnexBCommandSwitch.setStatus(_B)
_TApsNotificationsPrefix_ObjectIdentity=ObjectIdentity
tApsNotificationsPrefix=_TApsNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,29))
_TApsNotifications_ObjectIdentity=ObjectIdentity
tApsNotifications=_TApsNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,29,0))
apsCommandEntry.registerAugmentions((_A,_f))
tApsCommandEntry.setIndexNames(*apsCommandEntry.getIndexNames())
apsChanConfigEntry.registerAugmentions((_A,_g))
tApsChanStatusEntry.setIndexNames(*apsChanConfigEntry.getIndexNames())
apsConfigEntry.registerAugmentions((_A,_h))
tApsMcConfigEntry.setIndexNames(*apsConfigEntry.getIndexNames())
apsConfigEntry.registerAugmentions((_A,_i))
tApsMcStatusEntry.setIndexNames(*apsConfigEntry.getIndexNames())
apsConfigEntry.registerAugmentions((_A,_j))
tApsConfigEntry.setIndexNames(*apsConfigEntry.getIndexNames())
apsConfigEntry.registerAugmentions((_A,_k))
tApsGroupCommandEntry.setIndexNames(*apsConfigEntry.getIndexNames())
tmnxApsSwitchCommand=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,29,2,1))
tmnxApsSwitchCommand.setObjects((_A,_l))
if mibBuilder.loadTexts:tmnxApsSwitchCommand.setStatus(_B)
tmnxApsChanStatus=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,29,2,2))
tmnxApsChanStatus.setObjects((_A,_Q))
if mibBuilder.loadTexts:tmnxApsChanStatus.setStatus(_B)
tmnxApsMcGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,29,2,5))
tmnxApsMcGroup.setObjects(*((_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_R)))
if mibBuilder.loadTexts:tmnxApsMcGroup.setStatus(_B)
tmnxApsConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,29,2,6))
tmnxApsConfigGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:tmnxApsConfigGroup.setStatus(_B)
tmnxApsConfigV8v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,29,2,7))
tmnxApsConfigV8v0Group.setObjects((_A,_t))
if mibBuilder.loadTexts:tmnxApsConfigV8v0Group.setStatus(_B)
tmnxApsGroupCommandV9v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,29,2,8))
tmnxApsGroupCommandV9v0Group.setObjects((_A,_u))
if mibBuilder.loadTexts:tmnxApsGroupCommandV9v0Group.setStatus(_B)
tApsModeMismatchClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,1))
tApsModeMismatchClear.setObjects((_C,_I))
if mibBuilder.loadTexts:tApsModeMismatchClear.setStatus(_B)
tApsChannelMismatchClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,2))
tApsChannelMismatchClear.setObjects((_C,_I))
if mibBuilder.loadTexts:tApsChannelMismatchClear.setStatus(_B)
tApsPSBFClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,3))
tApsPSBFClear.setObjects((_C,_I))
if mibBuilder.loadTexts:tApsPSBFClear.setStatus(_B)
tApsFEPLFClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,4))
tApsFEPLFClear.setObjects((_C,_I))
if mibBuilder.loadTexts:tApsFEPLFClear.setStatus(_B)
tApsLocalSwitchCommandSet=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,5))
tApsLocalSwitchCommandSet.setObjects((_C,_H))
if mibBuilder.loadTexts:tApsLocalSwitchCommandSet.setStatus(_B)
tApsLocalSwitchCommandClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,6))
tApsLocalSwitchCommandClear.setObjects((_C,_H))
if mibBuilder.loadTexts:tApsLocalSwitchCommandClear.setStatus(_B)
tApsRemoteSwitchCommandSet=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,7))
tApsRemoteSwitchCommandSet.setObjects((_C,_H))
if mibBuilder.loadTexts:tApsRemoteSwitchCommandSet.setStatus(_B)
tApsRemoteSwitchCommandClear=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,8))
tApsRemoteSwitchCommandClear.setObjects((_C,_H))
if mibBuilder.loadTexts:tApsRemoteSwitchCommandClear.setStatus(_B)
tApsMcApsCtlLinkStateChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,9))
tApsMcApsCtlLinkStateChange.setObjects((_A,_R))
if mibBuilder.loadTexts:tApsMcApsCtlLinkStateChange.setStatus(_B)
tApsChanTxLaisStateChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,10))
tApsChanTxLaisStateChange.setObjects((_A,_Q))
if mibBuilder.loadTexts:tApsChanTxLaisStateChange.setStatus(_B)
tApsPrimaryChannelChange=NotificationType((1,3,6,1,4,1,6527,3,1,3,29,0,11))
tApsPrimaryChannelChange.setObjects(*((_C,_d),(_C,_c),(_C,_b)))
if mibBuilder.loadTexts:tApsPrimaryChannelChange.setStatus(_B)
tmnxApsNotifications=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,29,2,3))
tmnxApsNotifications.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:tmnxApsNotifications.setStatus(_K)
tmnxApsNotificationsV4v0=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,29,2,4))
tmnxApsNotificationsV4v0.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:tmnxApsNotificationsV4v0.setStatus(_B)
tmnxApsNotificationsV9v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,29,2,9))
tmnxApsNotificationsV9v0Group.setObjects((_A,_x))
if mibBuilder.loadTexts:tmnxApsNotificationsV9v0Group.setStatus(_B)
tApsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,29,1,1))
tApsMIBCompliance.setObjects(*((_A,_F),(_A,_G),(_A,_y)))
if mibBuilder.loadTexts:tApsMIBCompliance.setStatus(_K)
tApsMIBComplianceV4v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,29,1,2))
tApsMIBComplianceV4v0.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:tApsMIBComplianceV4v0.setStatus(_K)
tApsMIBComplianceV7v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,29,1,3))
tApsMIBComplianceV7v0.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_M),(_A,_O)))
if mibBuilder.loadTexts:tApsMIBComplianceV7v0.setStatus(_K)
tApsMIBComplianceV8v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,29,1,4))
tApsMIBComplianceV8v0.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_M),(_A,_O),(_A,_a)))
if mibBuilder.loadTexts:tApsMIBComplianceV8v0.setStatus(_K)
tApsMIBComplianceV9v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,29,1,5))
tApsMIBComplianceV9v0.setObjects(*((_A,_F),(_A,_G),(_A,_L),(_A,_M),(_A,_O),(_A,_a),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:tApsMIBComplianceV9v0.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'timetraAPSMIBModule':timetraAPSMIBModule,'tApsMIBConformance':tApsMIBConformance,'tmnxApsMIBCompliances':tmnxApsMIBCompliances,'tApsMIBCompliance':tApsMIBCompliance,'tApsMIBComplianceV4v0':tApsMIBComplianceV4v0,'tApsMIBComplianceV7v0':tApsMIBComplianceV7v0,'tApsMIBComplianceV8v0':tApsMIBComplianceV8v0,'tApsMIBComplianceV9v0':tApsMIBComplianceV9v0,'tmnxApsMIBGroups':tmnxApsMIBGroups,_F:tmnxApsSwitchCommand,_G:tmnxApsChanStatus,_y:tmnxApsNotifications,_M:tmnxApsNotificationsV4v0,_L:tmnxApsMcGroup,_O:tmnxApsConfigGroup,_a:tmnxApsConfigV8v0Group,_z:tmnxApsGroupCommandV9v0Group,_A0:tmnxApsNotificationsV9v0Group,'tApsMIBObjs':tApsMIBObjs,'tApsCommandTable':tApsCommandTable,_f:tApsCommandEntry,_l:tApsExerciseCommandResult,'tApsChanStatusTable':tApsChanStatusTable,_g:tApsChanStatusEntry,_Q:tApsChanTxLaisState,'tApsMcConfigTable':tApsMcConfigTable,_h:tApsMcConfigEntry,_m:tApsMcNeighborAddrType,_n:tApsMcNeighborAddr,_o:tApsMcAdvertiseInterval,_p:tApsMcHoldTime,'tApsMcStatusTable':tApsMcStatusTable,_i:tApsMcStatusEntry,_R:tApsMcApsCtlLinkState,'tApsConfigTable':tApsConfigTable,_j:tApsConfigEntry,_q:tApsProtectionType,_r:tApsLineSFHoldTime,_s:tApsLineSDHoldTime,_t:tApsRdiAlarmGeneration,'tApsGroupCommandTable':tApsGroupCommandTable,_k:tApsGroupCommandEntry,_u:tApsAnnexBCommandSwitch,'tApsNotificationsPrefix':tApsNotificationsPrefix,'tApsNotifications':tApsNotifications,_S:tApsModeMismatchClear,_T:tApsChannelMismatchClear,_U:tApsPSBFClear,_V:tApsFEPLFClear,_W:tApsLocalSwitchCommandSet,_X:tApsLocalSwitchCommandClear,_Y:tApsRemoteSwitchCommandSet,_Z:tApsRemoteSwitchCommandClear,_v:tApsMcApsCtlLinkStateChange,_w:tApsChanTxLaisStateChange,_x:tApsPrimaryChannelChange})