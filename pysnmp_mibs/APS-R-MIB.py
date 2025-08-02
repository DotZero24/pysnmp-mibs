_v='apsChanGeneralR'
_u='apsStatusGeneralR'
_t='apsConfigGeneralR'
_s='apsTrapFEPLFr'
_r='apsTrapPSBFr'
_q='apsTrapChannelMismatchR'
_p='apsTrapModeMismatchR'
_o='apsTrapSwitchoverR'
_n='apsMapChanNumberR'
_m='apsMapGroupNameR'
_l='apsChanLTEsR'
_k='apsConfigGroupsR'
_j='apsChanPriorityR'
_i='apsChanLastSwitchoverR'
_h='apsChanSignalFailuresR'
_g='apsChanSignalDegradesR'
_f='apsChanRowStatusR'
_e='apsChanIfIndexR'
_d='apsStatusK1K2TransR'
_c='apsStatusK1K2RcvR'
_b='apsCommandControlR'
_a='apsConfigWaitToRestoreR'
_Z='apsConfigCreationTimeR'
_Y='apsConfigOperDelayR'
_X='apsConfigSfBerThresholdR'
_W='apsConfigSdBerThresholdR'
_V='apsConfigModeR'
_U='apsConfigRowStatusR'
_T='apsMapIfIndexR'
_S='apsChanSwitchoversR'
_R='apsChanStatusR'
_Q='apsStatusFEPLFsR'
_P='apsStatusPSBFsR'
_O='apsStatusChannelMismatchesR'
_N='apsStatusModeMismatchesR'
_M='apsCommandSwitchR'
_L='apsConfigNameR'
_K='apsChanNumberR'
_J='apsChanGroupNameR'
_I='not-accessible'
_H='Bits'
_G='SnmpAdminString'
_F='apsStatusCurrentR'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='APS-R-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
radExperimental,=mibBuilder.importSymbols('RAD-SMI-MIB','radExperimental')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_H,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
apsMIBr=ModuleIdentity((1,3,6,1,4,1,164,20,2))
class ApsK1K2(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class ApsSwitchCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('clear',1),('lockoutOfProtection',2),('forcedSwitchWorkToProtect',3),('forcedSwitchProtectToWork',4),('manualSwitchWorkToProtect',5),('manualSwitchProtectToWork',6),('exercise',7)))
class ApsControlCommand(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lockoutWorkingChannel',1),('clearLockoutWorkingChannel',2)))
_ApsMIBObjectsR_ObjectIdentity=ObjectIdentity
apsMIBObjectsR=_ApsMIBObjectsR_ObjectIdentity((1,3,6,1,4,1,164,20,2,1))
_ApsConfigR_ObjectIdentity=ObjectIdentity
apsConfigR=_ApsConfigR_ObjectIdentity((1,3,6,1,4,1,164,20,2,1,1))
_ApsConfigGroupsR_Type=Counter32
_ApsConfigGroupsR_Object=MibScalar
apsConfigGroupsR=_ApsConfigGroupsR_Object((1,3,6,1,4,1,164,20,2,1,1,1),_ApsConfigGroupsR_Type())
apsConfigGroupsR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigGroupsR.setStatus(_A)
_ApsConfigTableR_Object=MibTable
apsConfigTableR=_ApsConfigTableR_Object((1,3,6,1,4,1,164,20,2,1,1,2))
if mibBuilder.loadTexts:apsConfigTableR.setStatus(_A)
_ApsConfigEntryR_Object=MibTableRow
apsConfigEntryR=_ApsConfigEntryR_Object((1,3,6,1,4,1,164,20,2,1,1,2,1))
apsConfigEntryR.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:apsConfigEntryR.setStatus(_A)
class _ApsConfigNameR_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApsConfigNameR_Type.__name__=_G
_ApsConfigNameR_Object=MibTableColumn
apsConfigNameR=_ApsConfigNameR_Object((1,3,6,1,4,1,164,20,2,1,1,2,1,1),_ApsConfigNameR_Type())
apsConfigNameR.setMaxAccess(_I)
if mibBuilder.loadTexts:apsConfigNameR.setStatus(_A)
_ApsConfigRowStatusR_Type=RowStatus
_ApsConfigRowStatusR_Object=MibTableColumn
apsConfigRowStatusR=_ApsConfigRowStatusR_Object((1,3,6,1,4,1,164,20,2,1,1,2,1,2),_ApsConfigRowStatusR_Type())
apsConfigRowStatusR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsConfigRowStatusR.setStatus(_A)
class _ApsConfigModeR_Type(Bits):namedValues=NamedValues(*(('onePlusOne',0),('oneToN',1),('revertive',2),('bidirectional',3),('extraTrafficAllowed',4),('onePlusOneOptimized',5),('pathProtection',6),('yCable',7)))
_ApsConfigModeR_Type.__name__=_H
_ApsConfigModeR_Object=MibTableColumn
apsConfigModeR=_ApsConfigModeR_Object((1,3,6,1,4,1,164,20,2,1,1,2,1,3),_ApsConfigModeR_Type())
apsConfigModeR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsConfigModeR.setStatus(_A)
class _ApsConfigSdBerThresholdR_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,9))
_ApsConfigSdBerThresholdR_Type.__name__=_E
_ApsConfigSdBerThresholdR_Object=MibTableColumn
apsConfigSdBerThresholdR=_ApsConfigSdBerThresholdR_Object((1,3,6,1,4,1,164,20,2,1,1,2,1,4),_ApsConfigSdBerThresholdR_Type())
apsConfigSdBerThresholdR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsConfigSdBerThresholdR.setStatus(_A)
class _ApsConfigSfBerThresholdR_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,5))
_ApsConfigSfBerThresholdR_Type.__name__=_E
_ApsConfigSfBerThresholdR_Object=MibTableColumn
apsConfigSfBerThresholdR=_ApsConfigSfBerThresholdR_Object((1,3,6,1,4,1,164,20,2,1,1,2,1,5),_ApsConfigSfBerThresholdR_Type())
apsConfigSfBerThresholdR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsConfigSfBerThresholdR.setStatus(_A)
class _ApsConfigWaitToRestoreR_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,720))
_ApsConfigWaitToRestoreR_Type.__name__=_E
_ApsConfigWaitToRestoreR_Object=MibTableColumn
apsConfigWaitToRestoreR=_ApsConfigWaitToRestoreR_Object((1,3,6,1,4,1,164,20,2,1,1,2,1,6),_ApsConfigWaitToRestoreR_Type())
apsConfigWaitToRestoreR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsConfigWaitToRestoreR.setStatus(_A)
_ApsConfigCreationTimeR_Type=TimeTicks
_ApsConfigCreationTimeR_Object=MibTableColumn
apsConfigCreationTimeR=_ApsConfigCreationTimeR_Object((1,3,6,1,4,1,164,20,2,1,1,2,1,7),_ApsConfigCreationTimeR_Type())
apsConfigCreationTimeR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsConfigCreationTimeR.setStatus(_A)
class _ApsConfigOperDelayR_Type(Integer32):defaultValue=10
_ApsConfigOperDelayR_Type.__name__=_E
_ApsConfigOperDelayR_Object=MibTableColumn
apsConfigOperDelayR=_ApsConfigOperDelayR_Object((1,3,6,1,4,1,164,20,2,1,1,2,1,8),_ApsConfigOperDelayR_Type())
apsConfigOperDelayR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsConfigOperDelayR.setStatus(_A)
_ApsStatusTableR_Object=MibTable
apsStatusTableR=_ApsStatusTableR_Object((1,3,6,1,4,1,164,20,2,1,2))
if mibBuilder.loadTexts:apsStatusTableR.setStatus(_A)
_ApsStatusEntryR_Object=MibTableRow
apsStatusEntryR=_ApsStatusEntryR_Object((1,3,6,1,4,1,164,20,2,1,2,1))
apsStatusEntryR.setIndexNames((1,_B,_L))
if mibBuilder.loadTexts:apsStatusEntryR.setStatus(_A)
_ApsStatusK1K2RcvR_Type=ApsK1K2
_ApsStatusK1K2RcvR_Object=MibTableColumn
apsStatusK1K2RcvR=_ApsStatusK1K2RcvR_Object((1,3,6,1,4,1,164,20,2,1,2,1,1),_ApsStatusK1K2RcvR_Type())
apsStatusK1K2RcvR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusK1K2RcvR.setStatus(_A)
_ApsStatusK1K2TransR_Type=ApsK1K2
_ApsStatusK1K2TransR_Object=MibTableColumn
apsStatusK1K2TransR=_ApsStatusK1K2TransR_Object((1,3,6,1,4,1,164,20,2,1,2,1,2),_ApsStatusK1K2TransR_Type())
apsStatusK1K2TransR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusK1K2TransR.setStatus(_A)
class _ApsStatusCurrentR_Type(Bits):namedValues=NamedValues(*(('modeMismatch',0),('channelMismatch',1),('psbf',2),('feplf',3),('extraTraffic',4)))
_ApsStatusCurrentR_Type.__name__=_H
_ApsStatusCurrentR_Object=MibTableColumn
apsStatusCurrentR=_ApsStatusCurrentR_Object((1,3,6,1,4,1,164,20,2,1,2,1,3),_ApsStatusCurrentR_Type())
apsStatusCurrentR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusCurrentR.setStatus(_A)
_ApsStatusModeMismatchesR_Type=Counter32
_ApsStatusModeMismatchesR_Object=MibTableColumn
apsStatusModeMismatchesR=_ApsStatusModeMismatchesR_Object((1,3,6,1,4,1,164,20,2,1,2,1,4),_ApsStatusModeMismatchesR_Type())
apsStatusModeMismatchesR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusModeMismatchesR.setStatus(_A)
_ApsStatusChannelMismatchesR_Type=Counter32
_ApsStatusChannelMismatchesR_Object=MibTableColumn
apsStatusChannelMismatchesR=_ApsStatusChannelMismatchesR_Object((1,3,6,1,4,1,164,20,2,1,2,1,5),_ApsStatusChannelMismatchesR_Type())
apsStatusChannelMismatchesR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusChannelMismatchesR.setStatus(_A)
_ApsStatusPSBFsR_Type=Counter32
_ApsStatusPSBFsR_Object=MibTableColumn
apsStatusPSBFsR=_ApsStatusPSBFsR_Object((1,3,6,1,4,1,164,20,2,1,2,1,6),_ApsStatusPSBFsR_Type())
apsStatusPSBFsR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusPSBFsR.setStatus(_A)
_ApsStatusFEPLFsR_Type=Counter32
_ApsStatusFEPLFsR_Object=MibTableColumn
apsStatusFEPLFsR=_ApsStatusFEPLFsR_Object((1,3,6,1,4,1,164,20,2,1,2,1,7),_ApsStatusFEPLFsR_Type())
apsStatusFEPLFsR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsStatusFEPLFsR.setStatus(_A)
_ApsMapR_ObjectIdentity=ObjectIdentity
apsMapR=_ApsMapR_ObjectIdentity((1,3,6,1,4,1,164,20,2,1,3))
_ApsChanLTEsR_Type=Counter32
_ApsChanLTEsR_Object=MibScalar
apsChanLTEsR=_ApsChanLTEsR_Object((1,3,6,1,4,1,164,20,2,1,3,1),_ApsChanLTEsR_Type())
apsChanLTEsR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanLTEsR.setStatus(_A)
_ApsMapTableR_Object=MibTable
apsMapTableR=_ApsMapTableR_Object((1,3,6,1,4,1,164,20,2,1,3,2))
if mibBuilder.loadTexts:apsMapTableR.setStatus(_A)
_ApsMapEntryR_Object=MibTableRow
apsMapEntryR=_ApsMapEntryR_Object((1,3,6,1,4,1,164,20,2,1,3,2,1))
apsMapEntryR.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:apsMapEntryR.setStatus(_A)
_ApsMapIfIndexR_Type=InterfaceIndex
_ApsMapIfIndexR_Object=MibTableColumn
apsMapIfIndexR=_ApsMapIfIndexR_Object((1,3,6,1,4,1,164,20,2,1,3,2,1,1),_ApsMapIfIndexR_Type())
apsMapIfIndexR.setMaxAccess(_I)
if mibBuilder.loadTexts:apsMapIfIndexR.setStatus(_A)
class _ApsMapGroupNameR_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApsMapGroupNameR_Type.__name__=_G
_ApsMapGroupNameR_Object=MibTableColumn
apsMapGroupNameR=_ApsMapGroupNameR_Object((1,3,6,1,4,1,164,20,2,1,3,2,1,2),_ApsMapGroupNameR_Type())
apsMapGroupNameR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsMapGroupNameR.setStatus(_A)
class _ApsMapChanNumberR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,14))
_ApsMapChanNumberR_Type.__name__=_E
_ApsMapChanNumberR_Object=MibTableColumn
apsMapChanNumberR=_ApsMapChanNumberR_Object((1,3,6,1,4,1,164,20,2,1,3,2,1,3),_ApsMapChanNumberR_Type())
apsMapChanNumberR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsMapChanNumberR.setStatus(_A)
_ApsChanConfigTableR_Object=MibTable
apsChanConfigTableR=_ApsChanConfigTableR_Object((1,3,6,1,4,1,164,20,2,1,4))
if mibBuilder.loadTexts:apsChanConfigTableR.setStatus(_A)
_ApsChanConfigEntryR_Object=MibTableRow
apsChanConfigEntryR=_ApsChanConfigEntryR_Object((1,3,6,1,4,1,164,20,2,1,4,1))
apsChanConfigEntryR.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:apsChanConfigEntryR.setStatus(_A)
class _ApsChanGroupNameR_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ApsChanGroupNameR_Type.__name__=_G
_ApsChanGroupNameR_Object=MibTableColumn
apsChanGroupNameR=_ApsChanGroupNameR_Object((1,3,6,1,4,1,164,20,2,1,4,1,1),_ApsChanGroupNameR_Type())
apsChanGroupNameR.setMaxAccess(_I)
if mibBuilder.loadTexts:apsChanGroupNameR.setStatus(_A)
class _ApsChanNumberR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_ApsChanNumberR_Type.__name__=_E
_ApsChanNumberR_Object=MibTableColumn
apsChanNumberR=_ApsChanNumberR_Object((1,3,6,1,4,1,164,20,2,1,4,1,2),_ApsChanNumberR_Type())
apsChanNumberR.setMaxAccess(_I)
if mibBuilder.loadTexts:apsChanNumberR.setStatus(_A)
_ApsChanRowStatusR_Type=RowStatus
_ApsChanRowStatusR_Object=MibTableColumn
apsChanRowStatusR=_ApsChanRowStatusR_Object((1,3,6,1,4,1,164,20,2,1,4,1,3),_ApsChanRowStatusR_Type())
apsChanRowStatusR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsChanRowStatusR.setStatus(_A)
_ApsChanIfIndexR_Type=InterfaceIndex
_ApsChanIfIndexR_Object=MibTableColumn
apsChanIfIndexR=_ApsChanIfIndexR_Object((1,3,6,1,4,1,164,20,2,1,4,1,4),_ApsChanIfIndexR_Type())
apsChanIfIndexR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsChanIfIndexR.setStatus(_A)
class _ApsChanPriorityR_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_ApsChanPriorityR_Type.__name__=_E
_ApsChanPriorityR_Object=MibTableColumn
apsChanPriorityR=_ApsChanPriorityR_Object((1,3,6,1,4,1,164,20,2,1,4,1,5),_ApsChanPriorityR_Type())
apsChanPriorityR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsChanPriorityR.setStatus(_A)
_ApsCommandTableR_Object=MibTable
apsCommandTableR=_ApsCommandTableR_Object((1,3,6,1,4,1,164,20,2,1,5))
if mibBuilder.loadTexts:apsCommandTableR.setStatus(_A)
_ApsCommandEntryR_Object=MibTableRow
apsCommandEntryR=_ApsCommandEntryR_Object((1,3,6,1,4,1,164,20,2,1,5,1))
apsCommandEntryR.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:apsCommandEntryR.setStatus(_A)
_ApsCommandSwitchR_Type=ApsSwitchCommand
_ApsCommandSwitchR_Object=MibTableColumn
apsCommandSwitchR=_ApsCommandSwitchR_Object((1,3,6,1,4,1,164,20,2,1,5,1,1),_ApsCommandSwitchR_Type())
apsCommandSwitchR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsCommandSwitchR.setStatus(_A)
_ApsCommandControlR_Type=ApsControlCommand
_ApsCommandControlR_Object=MibTableColumn
apsCommandControlR=_ApsCommandControlR_Object((1,3,6,1,4,1,164,20,2,1,5,1,2),_ApsCommandControlR_Type())
apsCommandControlR.setMaxAccess(_D)
if mibBuilder.loadTexts:apsCommandControlR.setStatus(_A)
_ApsChanStatusTableR_Object=MibTable
apsChanStatusTableR=_ApsChanStatusTableR_Object((1,3,6,1,4,1,164,20,2,1,6))
if mibBuilder.loadTexts:apsChanStatusTableR.setStatus(_A)
_ApsChanStatusEntryR_Object=MibTableRow
apsChanStatusEntryR=_ApsChanStatusEntryR_Object((1,3,6,1,4,1,164,20,2,1,6,1))
apsChanStatusEntryR.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:apsChanStatusEntryR.setStatus(_A)
class _ApsChanStatusR_Type(Bits):namedValues=NamedValues(*(('lockedOut',0),('sd',1),('sf',2),('switched',3)))
_ApsChanStatusR_Type.__name__=_H
_ApsChanStatusR_Object=MibTableColumn
apsChanStatusR=_ApsChanStatusR_Object((1,3,6,1,4,1,164,20,2,1,6,1,1),_ApsChanStatusR_Type())
apsChanStatusR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanStatusR.setStatus(_A)
_ApsChanSignalDegradesR_Type=Counter32
_ApsChanSignalDegradesR_Object=MibTableColumn
apsChanSignalDegradesR=_ApsChanSignalDegradesR_Object((1,3,6,1,4,1,164,20,2,1,6,1,2),_ApsChanSignalDegradesR_Type())
apsChanSignalDegradesR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanSignalDegradesR.setStatus(_A)
_ApsChanSignalFailuresR_Type=Counter32
_ApsChanSignalFailuresR_Object=MibTableColumn
apsChanSignalFailuresR=_ApsChanSignalFailuresR_Object((1,3,6,1,4,1,164,20,2,1,6,1,3),_ApsChanSignalFailuresR_Type())
apsChanSignalFailuresR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanSignalFailuresR.setStatus(_A)
_ApsChanSwitchoversR_Type=Counter32
_ApsChanSwitchoversR_Object=MibTableColumn
apsChanSwitchoversR=_ApsChanSwitchoversR_Object((1,3,6,1,4,1,164,20,2,1,6,1,4),_ApsChanSwitchoversR_Type())
apsChanSwitchoversR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanSwitchoversR.setStatus(_A)
_ApsChanLastSwitchoverR_Type=TimeTicks
_ApsChanLastSwitchoverR_Object=MibTableColumn
apsChanLastSwitchoverR=_ApsChanLastSwitchoverR_Object((1,3,6,1,4,1,164,20,2,1,6,1,5),_ApsChanLastSwitchoverR_Type())
apsChanLastSwitchoverR.setMaxAccess(_C)
if mibBuilder.loadTexts:apsChanLastSwitchoverR.setStatus(_A)
_ApsMIBNotificationsR_ObjectIdentity=ObjectIdentity
apsMIBNotificationsR=_ApsMIBNotificationsR_ObjectIdentity((1,3,6,1,4,1,164,20,2,2))
_ApsNotificationsPrefixR_ObjectIdentity=ObjectIdentity
apsNotificationsPrefixR=_ApsNotificationsPrefixR_ObjectIdentity((1,3,6,1,4,1,164,20,2,2,0))
_ApsMIBConformanceR_ObjectIdentity=ObjectIdentity
apsMIBConformanceR=_ApsMIBConformanceR_ObjectIdentity((1,3,6,1,4,1,164,20,2,3))
_ApsGroupsR_ObjectIdentity=ObjectIdentity
apsGroupsR=_ApsGroupsR_ObjectIdentity((1,3,6,1,4,1,164,20,2,3,1))
_ApsCompliancesR_ObjectIdentity=ObjectIdentity
apsCompliancesR=_ApsCompliancesR_ObjectIdentity((1,3,6,1,4,1,164,20,2,3,2))
apsConfigGeneralR=ObjectGroup((1,3,6,1,4,1,164,20,2,3,1,1))
apsConfigGeneralR.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:apsConfigGeneralR.setStatus(_A)
apsConfigOneToNr=ObjectGroup((1,3,6,1,4,1,164,20,2,3,1,2))
apsConfigOneToNr.setObjects((_B,_a))
if mibBuilder.loadTexts:apsConfigOneToNr.setStatus(_A)
apsCommandOnePlusOneR=ObjectGroup((1,3,6,1,4,1,164,20,2,3,1,3))
apsCommandOnePlusOneR.setObjects((_B,_M))
if mibBuilder.loadTexts:apsCommandOnePlusOneR.setStatus(_A)
apsCommandOneToNr=ObjectGroup((1,3,6,1,4,1,164,20,2,3,1,4))
apsCommandOneToNr.setObjects(*((_B,_M),(_B,_b)))
if mibBuilder.loadTexts:apsCommandOneToNr.setStatus(_A)
apsStatusGeneralR=ObjectGroup((1,3,6,1,4,1,164,20,2,3,1,5))
apsStatusGeneralR.setObjects(*((_B,_c),(_B,_d),(_B,_F),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:apsStatusGeneralR.setStatus(_A)
apsChanGeneralR=ObjectGroup((1,3,6,1,4,1,164,20,2,3,1,6))
apsChanGeneralR.setObjects(*((_B,_e),(_B,_f),(_B,_R),(_B,_g),(_B,_h),(_B,_S),(_B,_i)))
if mibBuilder.loadTexts:apsChanGeneralR.setStatus(_A)
apsChanOneToNr=ObjectGroup((1,3,6,1,4,1,164,20,2,3,1,7))
apsChanOneToNr.setObjects((_B,_j))
if mibBuilder.loadTexts:apsChanOneToNr.setStatus(_A)
apsTotalsGroupR=ObjectGroup((1,3,6,1,4,1,164,20,2,3,1,8))
apsTotalsGroupR.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:apsTotalsGroupR.setStatus(_A)
apsMapGroupR=ObjectGroup((1,3,6,1,4,1,164,20,2,3,1,9))
apsMapGroupR.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:apsMapGroupR.setStatus(_A)
apsTrapSwitchoverR=NotificationType((1,3,6,1,4,1,164,20,2,2,0,1))
apsTrapSwitchoverR.setObjects(*((_B,_S),(_B,_R)))
if mibBuilder.loadTexts:apsTrapSwitchoverR.setStatus(_A)
apsTrapModeMismatchR=NotificationType((1,3,6,1,4,1,164,20,2,2,0,2))
apsTrapModeMismatchR.setObjects(*((_B,_N),(_B,_F)))
if mibBuilder.loadTexts:apsTrapModeMismatchR.setStatus(_A)
apsTrapChannelMismatchR=NotificationType((1,3,6,1,4,1,164,20,2,2,0,3))
apsTrapChannelMismatchR.setObjects(*((_B,_O),(_B,_F)))
if mibBuilder.loadTexts:apsTrapChannelMismatchR.setStatus(_A)
apsTrapPSBFr=NotificationType((1,3,6,1,4,1,164,20,2,2,0,4))
apsTrapPSBFr.setObjects(*((_B,_P),(_B,_F)))
if mibBuilder.loadTexts:apsTrapPSBFr.setStatus(_A)
apsTrapFEPLFr=NotificationType((1,3,6,1,4,1,164,20,2,2,0,5))
apsTrapFEPLFr.setObjects(*((_B,_Q),(_B,_F)))
if mibBuilder.loadTexts:apsTrapFEPLFr.setStatus(_A)
apsTrapOptionalR=NotificationGroup((1,3,6,1,4,1,164,20,2,3,1,10))
apsTrapOptionalR.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:apsTrapOptionalR.setStatus(_A)
apsComplianceR=ModuleCompliance((1,3,6,1,4,1,164,20,2,3,2,1))
apsComplianceR.setObjects(*((_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:apsComplianceR.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ApsK1K2':ApsK1K2,'ApsSwitchCommand':ApsSwitchCommand,'ApsControlCommand':ApsControlCommand,'apsMIBr':apsMIBr,'apsMIBObjectsR':apsMIBObjectsR,'apsConfigR':apsConfigR,_k:apsConfigGroupsR,'apsConfigTableR':apsConfigTableR,'apsConfigEntryR':apsConfigEntryR,_L:apsConfigNameR,_U:apsConfigRowStatusR,_V:apsConfigModeR,_W:apsConfigSdBerThresholdR,_X:apsConfigSfBerThresholdR,_a:apsConfigWaitToRestoreR,_Z:apsConfigCreationTimeR,_Y:apsConfigOperDelayR,'apsStatusTableR':apsStatusTableR,'apsStatusEntryR':apsStatusEntryR,_c:apsStatusK1K2RcvR,_d:apsStatusK1K2TransR,_F:apsStatusCurrentR,_N:apsStatusModeMismatchesR,_O:apsStatusChannelMismatchesR,_P:apsStatusPSBFsR,_Q:apsStatusFEPLFsR,'apsMapR':apsMapR,_l:apsChanLTEsR,'apsMapTableR':apsMapTableR,'apsMapEntryR':apsMapEntryR,_T:apsMapIfIndexR,_m:apsMapGroupNameR,_n:apsMapChanNumberR,'apsChanConfigTableR':apsChanConfigTableR,'apsChanConfigEntryR':apsChanConfigEntryR,_J:apsChanGroupNameR,_K:apsChanNumberR,_f:apsChanRowStatusR,_e:apsChanIfIndexR,_j:apsChanPriorityR,'apsCommandTableR':apsCommandTableR,'apsCommandEntryR':apsCommandEntryR,_M:apsCommandSwitchR,_b:apsCommandControlR,'apsChanStatusTableR':apsChanStatusTableR,'apsChanStatusEntryR':apsChanStatusEntryR,_R:apsChanStatusR,_g:apsChanSignalDegradesR,_h:apsChanSignalFailuresR,_S:apsChanSwitchoversR,_i:apsChanLastSwitchoverR,'apsMIBNotificationsR':apsMIBNotificationsR,'apsNotificationsPrefixR':apsNotificationsPrefixR,_o:apsTrapSwitchoverR,_p:apsTrapModeMismatchR,_q:apsTrapChannelMismatchR,_r:apsTrapPSBFr,_s:apsTrapFEPLFr,'apsMIBConformanceR':apsMIBConformanceR,'apsGroupsR':apsGroupsR,_t:apsConfigGeneralR,'apsConfigOneToNr':apsConfigOneToNr,'apsCommandOnePlusOneR':apsCommandOnePlusOneR,'apsCommandOneToNr':apsCommandOneToNr,_u:apsStatusGeneralR,_v:apsChanGeneralR,'apsChanOneToNr':apsChanOneToNr,'apsTotalsGroupR':apsTotalsGroupR,'apsMapGroupR':apsMapGroupR,'apsTrapOptionalR':apsTrapOptionalR,'apsCompliancesR':apsCompliancesR,'apsComplianceR':apsComplianceR})