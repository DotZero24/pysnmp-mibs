_e='hm2PortLockingArpLastAlarmNewMacAddress'
_d='hm2PortLockingArpLastAlarmOldMacAddress'
_c='hm2PortLockingArpLastAlarmIpAddress'
_b='hm2PortLockingArpLastAlarmError'
_a='hm2PortLockingArpLastVerificationTPA'
_Z='hm2PortLockingArpLastVerificationTHA'
_Y='hm2PortLockingArpLastVerificationSHA'
_X='hm2PortLockingArpLastVerificationDA'
_W='hm2PortLockingArpLastVerificationSA'
_V='hm2PortLockingArpLastVerificationError'
_U='hm2PortLockingArpLastVerificationType'
_T='hm2PortLockingLastDiscardedMAC'
_S='hm2PortLockingArpDatabaseIpAddr'
_R='hm2PortLockingStaticMACAddress'
_Q='hm2PortLockingStaticVLANId'
_P='hm2PortLockingDynamicMACAddress'
_O='hm2PortLockingDynamicVLANId'
_N='StorageType'
_M='Unsigned32'
_L='none'
_K='read-create'
_J='disable'
_I='enable'
_H='ifIndex'
_G='IF-MIB'
_F='TruthValue'
_E='Integer32'
_D='HM2-PORTLOCKING-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2ConfigurationMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2ConfigurationMibs')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus',_N,'TextualConvention',_F)
hm2PortLocking=ModuleIdentity((1,3,6,1,4,1,248,11,250))
if mibBuilder.loadTexts:hm2PortLocking.setRevisions(('2021-04-28 00:00',))
_Hm2PortLockingMibNotifications_ObjectIdentity=ObjectIdentity
hm2PortLockingMibNotifications=_Hm2PortLockingMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,250,0))
_Hm2PortLockingMibObjects_ObjectIdentity=ObjectIdentity
hm2PortLockingMibObjects=_Hm2PortLockingMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,250,1))
_Hm2PortLockingGroup_ObjectIdentity=ObjectIdentity
hm2PortLockingGroup=_Hm2PortLockingGroup_ObjectIdentity((1,3,6,1,4,1,248,11,250,1,1))
class _Hm2GlobalPortLockingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Hm2GlobalPortLockingMode_Type.__name__=_E
_Hm2GlobalPortLockingMode_Object=MibScalar
hm2GlobalPortLockingMode=_Hm2GlobalPortLockingMode_Object((1,3,6,1,4,1,248,11,250,1,1,1),_Hm2GlobalPortLockingMode_Type())
hm2GlobalPortLockingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingMode.setStatus(_A)
class _Hm2GlobalPortLockingOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('locked',1),('unlocked',2),('lockpending',3)))
_Hm2GlobalPortLockingOperMode_Type.__name__=_E
_Hm2GlobalPortLockingOperMode_Object=MibScalar
hm2GlobalPortLockingOperMode=_Hm2GlobalPortLockingOperMode_Object((1,3,6,1,4,1,248,11,250,1,1,2),_Hm2GlobalPortLockingOperMode_Type())
hm2GlobalPortLockingOperMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingOperMode.setStatus(_A)
class _Hm2GlobalPortLockingLockOnlyPorts_Type(TruthValue):defaultValue=2
_Hm2GlobalPortLockingLockOnlyPorts_Type.__name__=_F
_Hm2GlobalPortLockingLockOnlyPorts_Object=MibScalar
hm2GlobalPortLockingLockOnlyPorts=_Hm2GlobalPortLockingLockOnlyPorts_Object((1,3,6,1,4,1,248,11,250,1,1,3),_Hm2GlobalPortLockingLockOnlyPorts_Type())
hm2GlobalPortLockingLockOnlyPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingLockOnlyPorts.setStatus('deprecated')
class _Hm2GlobalPortLockingFallbackTimer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_Hm2GlobalPortLockingFallbackTimer_Type.__name__=_E
_Hm2GlobalPortLockingFallbackTimer_Object=MibScalar
hm2GlobalPortLockingFallbackTimer=_Hm2GlobalPortLockingFallbackTimer_Object((1,3,6,1,4,1,248,11,250,1,1,4),_Hm2GlobalPortLockingFallbackTimer_Type())
hm2GlobalPortLockingFallbackTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingFallbackTimer.setStatus(_A)
_Hm2GlobalPortLockingFallbackTimeRemaining_Type=Integer32
_Hm2GlobalPortLockingFallbackTimeRemaining_Object=MibScalar
hm2GlobalPortLockingFallbackTimeRemaining=_Hm2GlobalPortLockingFallbackTimeRemaining_Object((1,3,6,1,4,1,248,11,250,1,1,5),_Hm2GlobalPortLockingFallbackTimeRemaining_Type())
hm2GlobalPortLockingFallbackTimeRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingFallbackTimeRemaining.setStatus(_A)
_Hm2GlobalPortLockingStatusMessage_Type=DisplayString
_Hm2GlobalPortLockingStatusMessage_Object=MibScalar
hm2GlobalPortLockingStatusMessage=_Hm2GlobalPortLockingStatusMessage_Object((1,3,6,1,4,1,248,11,250,1,1,6),_Hm2GlobalPortLockingStatusMessage_Type())
hm2GlobalPortLockingStatusMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingStatusMessage.setStatus(_A)
_Hm2GlobalPortLockingNumDynamicEntries_Type=Unsigned32
_Hm2GlobalPortLockingNumDynamicEntries_Object=MibScalar
hm2GlobalPortLockingNumDynamicEntries=_Hm2GlobalPortLockingNumDynamicEntries_Object((1,3,6,1,4,1,248,11,250,1,1,7),_Hm2GlobalPortLockingNumDynamicEntries_Type())
hm2GlobalPortLockingNumDynamicEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingNumDynamicEntries.setStatus(_A)
_Hm2GlobalPortLockingNumStaticEntries_Type=Unsigned32
_Hm2GlobalPortLockingNumStaticEntries_Object=MibScalar
hm2GlobalPortLockingNumStaticEntries=_Hm2GlobalPortLockingNumStaticEntries_Object((1,3,6,1,4,1,248,11,250,1,1,8),_Hm2GlobalPortLockingNumStaticEntries_Type())
hm2GlobalPortLockingNumStaticEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingNumStaticEntries.setStatus(_A)
class _Hm2GlobalPortLockingIgnoreUplinkPorts_Type(TruthValue):defaultValue=1
_Hm2GlobalPortLockingIgnoreUplinkPorts_Type.__name__=_F
_Hm2GlobalPortLockingIgnoreUplinkPorts_Object=MibScalar
hm2GlobalPortLockingIgnoreUplinkPorts=_Hm2GlobalPortLockingIgnoreUplinkPorts_Object((1,3,6,1,4,1,248,11,250,1,1,9),_Hm2GlobalPortLockingIgnoreUplinkPorts_Type())
hm2GlobalPortLockingIgnoreUplinkPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingIgnoreUplinkPorts.setStatus(_A)
_Hm2PortLockingTable_Object=MibTable
hm2PortLockingTable=_Hm2PortLockingTable_Object((1,3,6,1,4,1,248,11,250,1,1,10))
if mibBuilder.loadTexts:hm2PortLockingTable.setStatus(_A)
_Hm2PortLockingEntry_Object=MibTableRow
hm2PortLockingEntry=_Hm2PortLockingEntry_Object((1,3,6,1,4,1,248,11,250,1,1,10,1))
hm2PortLockingEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PortLockingEntry.setStatus(_A)
class _Hm2PortLockingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Hm2PortLockingMode_Type.__name__=_E
_Hm2PortLockingMode_Object=MibTableColumn
hm2PortLockingMode=_Hm2PortLockingMode_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,1),_Hm2PortLockingMode_Type())
hm2PortLockingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortLockingMode.setStatus(_A)
class _Hm2PortLockingDisabledByLocking_Type(TruthValue):defaultValue=2
_Hm2PortLockingDisabledByLocking_Type.__name__=_F
_Hm2PortLockingDisabledByLocking_Object=MibTableColumn
hm2PortLockingDisabledByLocking=_Hm2PortLockingDisabledByLocking_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,2),_Hm2PortLockingDisabledByLocking_Type())
hm2PortLockingDisabledByLocking.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortLockingDisabledByLocking.setStatus(_A)
class _Hm2PortLockingStaticLimit_Type(Unsigned32):defaultValue=1024;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_Hm2PortLockingStaticLimit_Type.__name__=_M
_Hm2PortLockingStaticLimit_Object=MibTableColumn
hm2PortLockingStaticLimit=_Hm2PortLockingStaticLimit_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,3),_Hm2PortLockingStaticLimit_Type())
hm2PortLockingStaticLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortLockingStaticLimit.setStatus(_A)
class _Hm2PortLockingViolationTrapMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Hm2PortLockingViolationTrapMode_Type.__name__=_E
_Hm2PortLockingViolationTrapMode_Object=MibTableColumn
hm2PortLockingViolationTrapMode=_Hm2PortLockingViolationTrapMode_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,4),_Hm2PortLockingViolationTrapMode_Type())
hm2PortLockingViolationTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortLockingViolationTrapMode.setStatus(_A)
_Hm2PortLockingLastDiscardedMAC_Type=DisplayString
_Hm2PortLockingLastDiscardedMAC_Object=MibTableColumn
hm2PortLockingLastDiscardedMAC=_Hm2PortLockingLastDiscardedMAC_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,5),_Hm2PortLockingLastDiscardedMAC_Type())
hm2PortLockingLastDiscardedMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingLastDiscardedMAC.setStatus(_A)
_Hm2PortLockingNumDynamicEntries_Type=Unsigned32
_Hm2PortLockingNumDynamicEntries_Object=MibTableColumn
hm2PortLockingNumDynamicEntries=_Hm2PortLockingNumDynamicEntries_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,6),_Hm2PortLockingNumDynamicEntries_Type())
hm2PortLockingNumDynamicEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingNumDynamicEntries.setStatus(_A)
_Hm2PortLockingNumStaticEntries_Type=Unsigned32
_Hm2PortLockingNumStaticEntries_Object=MibTableColumn
hm2PortLockingNumStaticEntries=_Hm2PortLockingNumStaticEntries_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,7),_Hm2PortLockingNumStaticEntries_Type())
hm2PortLockingNumStaticEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingNumStaticEntries.setStatus(_A)
_Hm2PortLockingMACAddressAdd_Type=DisplayString
_Hm2PortLockingMACAddressAdd_Object=MibTableColumn
hm2PortLockingMACAddressAdd=_Hm2PortLockingMACAddressAdd_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,8),_Hm2PortLockingMACAddressAdd_Type())
hm2PortLockingMACAddressAdd.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortLockingMACAddressAdd.setStatus(_A)
_Hm2PortLockingMACAddressRemove_Type=DisplayString
_Hm2PortLockingMACAddressRemove_Object=MibTableColumn
hm2PortLockingMACAddressRemove=_Hm2PortLockingMACAddressRemove_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,9),_Hm2PortLockingMACAddressRemove_Type())
hm2PortLockingMACAddressRemove.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortLockingMACAddressRemove.setStatus(_A)
_Hm2PortLockingStatusMessage_Type=DisplayString
_Hm2PortLockingStatusMessage_Object=MibTableColumn
hm2PortLockingStatusMessage=_Hm2PortLockingStatusMessage_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,10),_Hm2PortLockingStatusMessage_Type())
hm2PortLockingStatusMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingStatusMessage.setStatus(_A)
_Hm2PortLockingNumViolationEntries_Type=Unsigned32
_Hm2PortLockingNumViolationEntries_Object=MibTableColumn
hm2PortLockingNumViolationEntries=_Hm2PortLockingNumViolationEntries_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,11),_Hm2PortLockingNumViolationEntries_Type())
hm2PortLockingNumViolationEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingNumViolationEntries.setStatus(_A)
_Hm2PortLockingIsUplinkPort_Type=TruthValue
_Hm2PortLockingIsUplinkPort_Object=MibTableColumn
hm2PortLockingIsUplinkPort=_Hm2PortLockingIsUplinkPort_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,12),_Hm2PortLockingIsUplinkPort_Type())
hm2PortLockingIsUplinkPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingIsUplinkPort.setStatus(_A)
class _Hm2PortLockingIsMacLockedPort_Type(TruthValue):defaultValue=2
_Hm2PortLockingIsMacLockedPort_Type.__name__=_F
_Hm2PortLockingIsMacLockedPort_Object=MibTableColumn
hm2PortLockingIsMacLockedPort=_Hm2PortLockingIsMacLockedPort_Object((1,3,6,1,4,1,248,11,250,1,1,10,1,13),_Hm2PortLockingIsMacLockedPort_Type())
hm2PortLockingIsMacLockedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PortLockingIsMacLockedPort.setStatus(_A)
_Hm2PortLockingDynamicTable_Object=MibTable
hm2PortLockingDynamicTable=_Hm2PortLockingDynamicTable_Object((1,3,6,1,4,1,248,11,250,1,1,11))
if mibBuilder.loadTexts:hm2PortLockingDynamicTable.setStatus(_A)
_Hm2PortLockingDynamicEntry_Object=MibTableRow
hm2PortLockingDynamicEntry=_Hm2PortLockingDynamicEntry_Object((1,3,6,1,4,1,248,11,250,1,1,11,1))
hm2PortLockingDynamicEntry.setIndexNames((0,_G,_H),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:hm2PortLockingDynamicEntry.setStatus(_A)
_Hm2PortLockingDynamicVLANId_Type=Unsigned32
_Hm2PortLockingDynamicVLANId_Object=MibTableColumn
hm2PortLockingDynamicVLANId=_Hm2PortLockingDynamicVLANId_Object((1,3,6,1,4,1,248,11,250,1,1,11,1,1),_Hm2PortLockingDynamicVLANId_Type())
hm2PortLockingDynamicVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingDynamicVLANId.setStatus(_A)
_Hm2PortLockingDynamicMACAddress_Type=MacAddress
_Hm2PortLockingDynamicMACAddress_Object=MibTableColumn
hm2PortLockingDynamicMACAddress=_Hm2PortLockingDynamicMACAddress_Object((1,3,6,1,4,1,248,11,250,1,1,11,1,2),_Hm2PortLockingDynamicMACAddress_Type())
hm2PortLockingDynamicMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingDynamicMACAddress.setStatus(_A)
_Hm2PortLockingStaticTable_Object=MibTable
hm2PortLockingStaticTable=_Hm2PortLockingStaticTable_Object((1,3,6,1,4,1,248,11,250,1,1,12))
if mibBuilder.loadTexts:hm2PortLockingStaticTable.setStatus(_A)
_Hm2PortLockingStaticEntry_Object=MibTableRow
hm2PortLockingStaticEntry=_Hm2PortLockingStaticEntry_Object((1,3,6,1,4,1,248,11,250,1,1,12,1))
hm2PortLockingStaticEntry.setIndexNames((0,_G,_H),(0,_D,_Q),(0,_D,_R))
if mibBuilder.loadTexts:hm2PortLockingStaticEntry.setStatus(_A)
_Hm2PortLockingStaticVLANId_Type=Unsigned32
_Hm2PortLockingStaticVLANId_Object=MibTableColumn
hm2PortLockingStaticVLANId=_Hm2PortLockingStaticVLANId_Object((1,3,6,1,4,1,248,11,250,1,1,12,1,1),_Hm2PortLockingStaticVLANId_Type())
hm2PortLockingStaticVLANId.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingStaticVLANId.setStatus(_A)
_Hm2PortLockingStaticMACAddress_Type=MacAddress
_Hm2PortLockingStaticMACAddress_Object=MibTableColumn
hm2PortLockingStaticMACAddress=_Hm2PortLockingStaticMACAddress_Object((1,3,6,1,4,1,248,11,250,1,1,12,1,2),_Hm2PortLockingStaticMACAddress_Type())
hm2PortLockingStaticMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingStaticMACAddress.setStatus(_A)
class _Hm2GlobalPortLockingMethod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('lockMacAndDisableUnusedPorts',0),('disableUnusedPortsOnly',1),('lockMacOnly',2)))
_Hm2GlobalPortLockingMethod_Type.__name__=_E
_Hm2GlobalPortLockingMethod_Object=MibScalar
hm2GlobalPortLockingMethod=_Hm2GlobalPortLockingMethod_Object((1,3,6,1,4,1,248,11,250,1,1,15),_Hm2GlobalPortLockingMethod_Type())
hm2GlobalPortLockingMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingMethod.setStatus(_A)
class _Hm2GlobalPortLockingResetMacViolation_Type(Integer32):defaultValue=0
_Hm2GlobalPortLockingResetMacViolation_Type.__name__=_E
_Hm2GlobalPortLockingResetMacViolation_Object=MibScalar
hm2GlobalPortLockingResetMacViolation=_Hm2GlobalPortLockingResetMacViolation_Object((1,3,6,1,4,1,248,11,250,1,1,16),_Hm2GlobalPortLockingResetMacViolation_Type())
hm2GlobalPortLockingResetMacViolation.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingResetMacViolation.setStatus(_A)
class _Hm2GlobalPortLockingUplinkDetectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('numMac',0),('pdu',1)))
_Hm2GlobalPortLockingUplinkDetectionMode_Type.__name__=_E
_Hm2GlobalPortLockingUplinkDetectionMode_Object=MibScalar
hm2GlobalPortLockingUplinkDetectionMode=_Hm2GlobalPortLockingUplinkDetectionMode_Object((1,3,6,1,4,1,248,11,250,1,1,17),_Hm2GlobalPortLockingUplinkDetectionMode_Type())
hm2GlobalPortLockingUplinkDetectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingUplinkDetectionMode.setStatus(_A)
class _Hm2GlobalPortLockingUplinkFreezeMacAddresses_Type(TruthValue):defaultValue=1
_Hm2GlobalPortLockingUplinkFreezeMacAddresses_Type.__name__=_F
_Hm2GlobalPortLockingUplinkFreezeMacAddresses_Object=MibScalar
hm2GlobalPortLockingUplinkFreezeMacAddresses=_Hm2GlobalPortLockingUplinkFreezeMacAddresses_Object((1,3,6,1,4,1,248,11,250,1,1,18),_Hm2GlobalPortLockingUplinkFreezeMacAddresses_Type())
hm2GlobalPortLockingUplinkFreezeMacAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingUplinkFreezeMacAddresses.setStatus(_A)
class _Hm2GlobalPortLockingUplinkReportMacAddresses_Type(TruthValue):defaultValue=1
_Hm2GlobalPortLockingUplinkReportMacAddresses_Type.__name__=_F
_Hm2GlobalPortLockingUplinkReportMacAddresses_Object=MibScalar
hm2GlobalPortLockingUplinkReportMacAddresses=_Hm2GlobalPortLockingUplinkReportMacAddresses_Object((1,3,6,1,4,1,248,11,250,1,1,19),_Hm2GlobalPortLockingUplinkReportMacAddresses_Type())
hm2GlobalPortLockingUplinkReportMacAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingUplinkReportMacAddresses.setStatus(_A)
_Hm2PortLockingArpGroup_ObjectIdentity=ObjectIdentity
hm2PortLockingArpGroup=_Hm2PortLockingArpGroup_ObjectIdentity((1,3,6,1,4,1,248,11,250,1,5))
class _Hm2GlobalPortLockingArpInspectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Hm2GlobalPortLockingArpInspectionMode_Type.__name__=_E
_Hm2GlobalPortLockingArpInspectionMode_Object=MibScalar
hm2GlobalPortLockingArpInspectionMode=_Hm2GlobalPortLockingArpInspectionMode_Object((1,3,6,1,4,1,248,11,250,1,5,1),_Hm2GlobalPortLockingArpInspectionMode_Type())
hm2GlobalPortLockingArpInspectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpInspectionMode.setStatus(_A)
class _Hm2GlobalPortLockingArpInspectionDropMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_Hm2GlobalPortLockingArpInspectionDropMode_Type.__name__=_E
_Hm2GlobalPortLockingArpInspectionDropMode_Object=MibScalar
hm2GlobalPortLockingArpInspectionDropMode=_Hm2GlobalPortLockingArpInspectionDropMode_Object((1,3,6,1,4,1,248,11,250,1,5,2),_Hm2GlobalPortLockingArpInspectionDropMode_Type())
hm2GlobalPortLockingArpInspectionDropMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpInspectionDropMode.setStatus(_A)
class _Hm2GlobalPortLockingArpVerifySrcMac_Type(TruthValue):defaultValue=1
_Hm2GlobalPortLockingArpVerifySrcMac_Type.__name__=_F
_Hm2GlobalPortLockingArpVerifySrcMac_Object=MibScalar
hm2GlobalPortLockingArpVerifySrcMac=_Hm2GlobalPortLockingArpVerifySrcMac_Object((1,3,6,1,4,1,248,11,250,1,5,3),_Hm2GlobalPortLockingArpVerifySrcMac_Type())
hm2GlobalPortLockingArpVerifySrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpVerifySrcMac.setStatus(_A)
class _Hm2GlobalPortLockingArpVerifyDstMac_Type(TruthValue):defaultValue=1
_Hm2GlobalPortLockingArpVerifyDstMac_Type.__name__=_F
_Hm2GlobalPortLockingArpVerifyDstMac_Object=MibScalar
hm2GlobalPortLockingArpVerifyDstMac=_Hm2GlobalPortLockingArpVerifyDstMac_Object((1,3,6,1,4,1,248,11,250,1,5,4),_Hm2GlobalPortLockingArpVerifyDstMac_Type())
hm2GlobalPortLockingArpVerifyDstMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpVerifyDstMac.setStatus(_A)
class _Hm2GlobalPortLockingArpVerifyIp_Type(TruthValue):defaultValue=1
_Hm2GlobalPortLockingArpVerifyIp_Type.__name__=_F
_Hm2GlobalPortLockingArpVerifyIp_Object=MibScalar
hm2GlobalPortLockingArpVerifyIp=_Hm2GlobalPortLockingArpVerifyIp_Object((1,3,6,1,4,1,248,11,250,1,5,5),_Hm2GlobalPortLockingArpVerifyIp_Type())
hm2GlobalPortLockingArpVerifyIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpVerifyIp.setStatus(_A)
class _Hm2GlobalPortLockingArpVerifySubnet_Type(TruthValue):defaultValue=2
_Hm2GlobalPortLockingArpVerifySubnet_Type.__name__=_F
_Hm2GlobalPortLockingArpVerifySubnet_Object=MibScalar
hm2GlobalPortLockingArpVerifySubnet=_Hm2GlobalPortLockingArpVerifySubnet_Object((1,3,6,1,4,1,248,11,250,1,5,6),_Hm2GlobalPortLockingArpVerifySubnet_Type())
hm2GlobalPortLockingArpVerifySubnet.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpVerifySubnet.setStatus(_A)
class _Hm2GlobalPortLockingSendVerificationTrap_Type(TruthValue):defaultValue=1
_Hm2GlobalPortLockingSendVerificationTrap_Type.__name__=_F
_Hm2GlobalPortLockingSendVerificationTrap_Object=MibScalar
hm2GlobalPortLockingSendVerificationTrap=_Hm2GlobalPortLockingSendVerificationTrap_Object((1,3,6,1,4,1,248,11,250,1,5,7),_Hm2GlobalPortLockingSendVerificationTrap_Type())
hm2GlobalPortLockingSendVerificationTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingSendVerificationTrap.setStatus(_A)
class _Hm2GlobalPortLockingSendDatabaseModificationTrap_Type(TruthValue):defaultValue=1
_Hm2GlobalPortLockingSendDatabaseModificationTrap_Type.__name__=_F
_Hm2GlobalPortLockingSendDatabaseModificationTrap_Object=MibScalar
hm2GlobalPortLockingSendDatabaseModificationTrap=_Hm2GlobalPortLockingSendDatabaseModificationTrap_Object((1,3,6,1,4,1,248,11,250,1,5,8),_Hm2GlobalPortLockingSendDatabaseModificationTrap_Type())
hm2GlobalPortLockingSendDatabaseModificationTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingSendDatabaseModificationTrap.setStatus(_A)
class _Hm2GlobalPortLockingSendDatabaseAlarmTrap_Type(TruthValue):defaultValue=1
_Hm2GlobalPortLockingSendDatabaseAlarmTrap_Type.__name__=_F
_Hm2GlobalPortLockingSendDatabaseAlarmTrap_Object=MibScalar
hm2GlobalPortLockingSendDatabaseAlarmTrap=_Hm2GlobalPortLockingSendDatabaseAlarmTrap_Object((1,3,6,1,4,1,248,11,250,1,5,9),_Hm2GlobalPortLockingSendDatabaseAlarmTrap_Type())
hm2GlobalPortLockingSendDatabaseAlarmTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingSendDatabaseAlarmTrap.setStatus(_A)
class _Hm2GlobalPortLockingArpResetCache_Type(TruthValue):defaultValue=2
_Hm2GlobalPortLockingArpResetCache_Type.__name__=_F
_Hm2GlobalPortLockingArpResetCache_Object=MibScalar
hm2GlobalPortLockingArpResetCache=_Hm2GlobalPortLockingArpResetCache_Object((1,3,6,1,4,1,248,11,250,1,5,10),_Hm2GlobalPortLockingArpResetCache_Type())
hm2GlobalPortLockingArpResetCache.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpResetCache.setStatus(_A)
_Hm2GlobalPortLockingArpInspectionTableEntries_Type=Counter32
_Hm2GlobalPortLockingArpInspectionTableEntries_Object=MibScalar
hm2GlobalPortLockingArpInspectionTableEntries=_Hm2GlobalPortLockingArpInspectionTableEntries_Object((1,3,6,1,4,1,248,11,250,1,5,11),_Hm2GlobalPortLockingArpInspectionTableEntries_Type())
hm2GlobalPortLockingArpInspectionTableEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpInspectionTableEntries.setStatus(_A)
_Hm2PortLockingArpDatabaseTable_Object=MibTable
hm2PortLockingArpDatabaseTable=_Hm2PortLockingArpDatabaseTable_Object((1,3,6,1,4,1,248,11,250,1,5,20))
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseTable.setStatus(_A)
_Hm2PortLockingArpDatabaseEntry_Object=MibTableRow
hm2PortLockingArpDatabaseEntry=_Hm2PortLockingArpDatabaseEntry_Object((1,3,6,1,4,1,248,11,250,1,5,20,1))
hm2PortLockingArpDatabaseEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseEntry.setStatus(_A)
_Hm2PortLockingArpDatabaseIpAddr_Type=IpAddress
_Hm2PortLockingArpDatabaseIpAddr_Object=MibTableColumn
hm2PortLockingArpDatabaseIpAddr=_Hm2PortLockingArpDatabaseIpAddr_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,1),_Hm2PortLockingArpDatabaseIpAddr_Type())
hm2PortLockingArpDatabaseIpAddr.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseIpAddr.setStatus(_A)
_Hm2PortLockingArpDatabaseIfIndex_Type=Integer32
_Hm2PortLockingArpDatabaseIfIndex_Object=MibTableColumn
hm2PortLockingArpDatabaseIfIndex=_Hm2PortLockingArpDatabaseIfIndex_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,2),_Hm2PortLockingArpDatabaseIfIndex_Type())
hm2PortLockingArpDatabaseIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseIfIndex.setStatus(_A)
_Hm2PortLockingArpDatabaseVlanId_Type=Integer32
_Hm2PortLockingArpDatabaseVlanId_Object=MibTableColumn
hm2PortLockingArpDatabaseVlanId=_Hm2PortLockingArpDatabaseVlanId_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,3),_Hm2PortLockingArpDatabaseVlanId_Type())
hm2PortLockingArpDatabaseVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseVlanId.setStatus(_A)
_Hm2PortLockingArpDatabaseMacAddr_Type=PhysAddress
_Hm2PortLockingArpDatabaseMacAddr_Object=MibTableColumn
hm2PortLockingArpDatabaseMacAddr=_Hm2PortLockingArpDatabaseMacAddr_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,4),_Hm2PortLockingArpDatabaseMacAddr_Type())
hm2PortLockingArpDatabaseMacAddr.setMaxAccess(_K)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseMacAddr.setStatus(_A)
_Hm2PortLockingArpDatabaseHitCounter_Type=Counter32
_Hm2PortLockingArpDatabaseHitCounter_Object=MibTableColumn
hm2PortLockingArpDatabaseHitCounter=_Hm2PortLockingArpDatabaseHitCounter_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,5),_Hm2PortLockingArpDatabaseHitCounter_Type())
hm2PortLockingArpDatabaseHitCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseHitCounter.setStatus(_A)
_Hm2PortLockingArpDatabaseIfAlarmCounter_Type=Counter32
_Hm2PortLockingArpDatabaseIfAlarmCounter_Object=MibTableColumn
hm2PortLockingArpDatabaseIfAlarmCounter=_Hm2PortLockingArpDatabaseIfAlarmCounter_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,6),_Hm2PortLockingArpDatabaseIfAlarmCounter_Type())
hm2PortLockingArpDatabaseIfAlarmCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseIfAlarmCounter.setStatus(_A)
_Hm2PortLockingArpDatabaseMacAlarmCounter_Type=Counter32
_Hm2PortLockingArpDatabaseMacAlarmCounter_Object=MibTableColumn
hm2PortLockingArpDatabaseMacAlarmCounter=_Hm2PortLockingArpDatabaseMacAlarmCounter_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,7),_Hm2PortLockingArpDatabaseMacAlarmCounter_Type())
hm2PortLockingArpDatabaseMacAlarmCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseMacAlarmCounter.setStatus(_A)
_Hm2PortLockingArpDatabaseDropCounter_Type=Counter32
_Hm2PortLockingArpDatabaseDropCounter_Object=MibTableColumn
hm2PortLockingArpDatabaseDropCounter=_Hm2PortLockingArpDatabaseDropCounter_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,8),_Hm2PortLockingArpDatabaseDropCounter_Type())
hm2PortLockingArpDatabaseDropCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseDropCounter.setStatus(_A)
class _Hm2PortLockingArpDatabaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dynamic',0),('static',1)))
_Hm2PortLockingArpDatabaseType_Type.__name__=_E
_Hm2PortLockingArpDatabaseType_Object=MibTableColumn
hm2PortLockingArpDatabaseType=_Hm2PortLockingArpDatabaseType_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,9),_Hm2PortLockingArpDatabaseType_Type())
hm2PortLockingArpDatabaseType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseType.setStatus(_A)
class _Hm2PortLockingArpDatabaseStorageType_Type(StorageType):defaultValue=3
_Hm2PortLockingArpDatabaseStorageType_Type.__name__=_N
_Hm2PortLockingArpDatabaseStorageType_Object=MibTableColumn
hm2PortLockingArpDatabaseStorageType=_Hm2PortLockingArpDatabaseStorageType_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,10),_Hm2PortLockingArpDatabaseStorageType_Type())
hm2PortLockingArpDatabaseStorageType.setMaxAccess(_K)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseStorageType.setStatus(_A)
_Hm2PortLockingArpDatabaseRowStatus_Type=RowStatus
_Hm2PortLockingArpDatabaseRowStatus_Object=MibTableColumn
hm2PortLockingArpDatabaseRowStatus=_Hm2PortLockingArpDatabaseRowStatus_Object((1,3,6,1,4,1,248,11,250,1,5,20,1,11),_Hm2PortLockingArpDatabaseRowStatus_Type())
hm2PortLockingArpDatabaseRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hm2PortLockingArpDatabaseRowStatus.setStatus(_A)
_Hm2GlobalPortLockingArpStatistics_ObjectIdentity=ObjectIdentity
hm2GlobalPortLockingArpStatistics=_Hm2GlobalPortLockingArpStatistics_ObjectIdentity((1,3,6,1,4,1,248,11,250,1,5,21))
_Hm2GlobalPortLockingArpStatisticsPacketsReceived_Type=Counter32
_Hm2GlobalPortLockingArpStatisticsPacketsReceived_Object=MibScalar
hm2GlobalPortLockingArpStatisticsPacketsReceived=_Hm2GlobalPortLockingArpStatisticsPacketsReceived_Object((1,3,6,1,4,1,248,11,250,1,5,21,1),_Hm2GlobalPortLockingArpStatisticsPacketsReceived_Type())
hm2GlobalPortLockingArpStatisticsPacketsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpStatisticsPacketsReceived.setStatus(_A)
_Hm2GlobalPortLockingArpStatisticsUcPacketsReceived_Type=Counter32
_Hm2GlobalPortLockingArpStatisticsUcPacketsReceived_Object=MibScalar
hm2GlobalPortLockingArpStatisticsUcPacketsReceived=_Hm2GlobalPortLockingArpStatisticsUcPacketsReceived_Object((1,3,6,1,4,1,248,11,250,1,5,21,2),_Hm2GlobalPortLockingArpStatisticsUcPacketsReceived_Type())
hm2GlobalPortLockingArpStatisticsUcPacketsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpStatisticsUcPacketsReceived.setStatus(_A)
_Hm2GlobalPortLockingArpStatisticsSrcMacFailure_Type=Counter32
_Hm2GlobalPortLockingArpStatisticsSrcMacFailure_Object=MibScalar
hm2GlobalPortLockingArpStatisticsSrcMacFailure=_Hm2GlobalPortLockingArpStatisticsSrcMacFailure_Object((1,3,6,1,4,1,248,11,250,1,5,21,3),_Hm2GlobalPortLockingArpStatisticsSrcMacFailure_Type())
hm2GlobalPortLockingArpStatisticsSrcMacFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpStatisticsSrcMacFailure.setStatus(_A)
_Hm2GlobalPortLockingArpStatisticsDstMacFailure_Type=Counter32
_Hm2GlobalPortLockingArpStatisticsDstMacFailure_Object=MibScalar
hm2GlobalPortLockingArpStatisticsDstMacFailure=_Hm2GlobalPortLockingArpStatisticsDstMacFailure_Object((1,3,6,1,4,1,248,11,250,1,5,21,4),_Hm2GlobalPortLockingArpStatisticsDstMacFailure_Type())
hm2GlobalPortLockingArpStatisticsDstMacFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpStatisticsDstMacFailure.setStatus(_A)
_Hm2GlobalPortLockingArpStatisticsIpFailure_Type=Counter32
_Hm2GlobalPortLockingArpStatisticsIpFailure_Object=MibScalar
hm2GlobalPortLockingArpStatisticsIpFailure=_Hm2GlobalPortLockingArpStatisticsIpFailure_Object((1,3,6,1,4,1,248,11,250,1,5,21,5),_Hm2GlobalPortLockingArpStatisticsIpFailure_Type())
hm2GlobalPortLockingArpStatisticsIpFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpStatisticsIpFailure.setStatus(_A)
_Hm2GlobalPortLockingArpStatisticsSubnetFailure_Type=Counter32
_Hm2GlobalPortLockingArpStatisticsSubnetFailure_Object=MibScalar
hm2GlobalPortLockingArpStatisticsSubnetFailure=_Hm2GlobalPortLockingArpStatisticsSubnetFailure_Object((1,3,6,1,4,1,248,11,250,1,5,21,6),_Hm2GlobalPortLockingArpStatisticsSubnetFailure_Type())
hm2GlobalPortLockingArpStatisticsSubnetFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpStatisticsSubnetFailure.setStatus(_A)
_Hm2GlobalPortLockingArpStatisticsDropCounter_Type=Counter32
_Hm2GlobalPortLockingArpStatisticsDropCounter_Object=MibScalar
hm2GlobalPortLockingArpStatisticsDropCounter=_Hm2GlobalPortLockingArpStatisticsDropCounter_Object((1,3,6,1,4,1,248,11,250,1,5,21,7),_Hm2GlobalPortLockingArpStatisticsDropCounter_Type())
hm2GlobalPortLockingArpStatisticsDropCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2GlobalPortLockingArpStatisticsDropCounter.setStatus(_A)
_Hm2PortLockingArpLastVerificationTable_Object=MibTable
hm2PortLockingArpLastVerificationTable=_Hm2PortLockingArpLastVerificationTable_Object((1,3,6,1,4,1,248,11,250,1,5,22))
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationTable.setStatus(_A)
_Hm2PortLockingArpLastVerificationEntry_Object=MibTableRow
hm2PortLockingArpLastVerificationEntry=_Hm2PortLockingArpLastVerificationEntry_Object((1,3,6,1,4,1,248,11,250,1,5,22,1))
hm2PortLockingArpLastVerificationEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationEntry.setStatus(_A)
class _Hm2PortLockingArpLastVerificationError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),('da',1),('sa',2),('ip',3),('subnet',4)))
_Hm2PortLockingArpLastVerificationError_Type.__name__=_E
_Hm2PortLockingArpLastVerificationError_Object=MibTableColumn
hm2PortLockingArpLastVerificationError=_Hm2PortLockingArpLastVerificationError_Object((1,3,6,1,4,1,248,11,250,1,5,22,1,1),_Hm2PortLockingArpLastVerificationError_Type())
hm2PortLockingArpLastVerificationError.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationError.setStatus(_A)
class _Hm2PortLockingArpLastVerificationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),('arpRequest',1),('arpReply',2)))
_Hm2PortLockingArpLastVerificationType_Type.__name__=_E
_Hm2PortLockingArpLastVerificationType_Object=MibTableColumn
hm2PortLockingArpLastVerificationType=_Hm2PortLockingArpLastVerificationType_Object((1,3,6,1,4,1,248,11,250,1,5,22,1,2),_Hm2PortLockingArpLastVerificationType_Type())
hm2PortLockingArpLastVerificationType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationType.setStatus(_A)
_Hm2PortLockingArpLastVerificationSA_Type=MacAddress
_Hm2PortLockingArpLastVerificationSA_Object=MibTableColumn
hm2PortLockingArpLastVerificationSA=_Hm2PortLockingArpLastVerificationSA_Object((1,3,6,1,4,1,248,11,250,1,5,22,1,3),_Hm2PortLockingArpLastVerificationSA_Type())
hm2PortLockingArpLastVerificationSA.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationSA.setStatus(_A)
_Hm2PortLockingArpLastVerificationDA_Type=MacAddress
_Hm2PortLockingArpLastVerificationDA_Object=MibTableColumn
hm2PortLockingArpLastVerificationDA=_Hm2PortLockingArpLastVerificationDA_Object((1,3,6,1,4,1,248,11,250,1,5,22,1,4),_Hm2PortLockingArpLastVerificationDA_Type())
hm2PortLockingArpLastVerificationDA.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationDA.setStatus(_A)
_Hm2PortLockingArpLastVerificationSHA_Type=MacAddress
_Hm2PortLockingArpLastVerificationSHA_Object=MibTableColumn
hm2PortLockingArpLastVerificationSHA=_Hm2PortLockingArpLastVerificationSHA_Object((1,3,6,1,4,1,248,11,250,1,5,22,1,5),_Hm2PortLockingArpLastVerificationSHA_Type())
hm2PortLockingArpLastVerificationSHA.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationSHA.setStatus(_A)
_Hm2PortLockingArpLastVerificationTHA_Type=MacAddress
_Hm2PortLockingArpLastVerificationTHA_Object=MibTableColumn
hm2PortLockingArpLastVerificationTHA=_Hm2PortLockingArpLastVerificationTHA_Object((1,3,6,1,4,1,248,11,250,1,5,22,1,6),_Hm2PortLockingArpLastVerificationTHA_Type())
hm2PortLockingArpLastVerificationTHA.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationTHA.setStatus(_A)
_Hm2PortLockingArpLastVerificationSPA_Type=IpAddress
_Hm2PortLockingArpLastVerificationSPA_Object=MibTableColumn
hm2PortLockingArpLastVerificationSPA=_Hm2PortLockingArpLastVerificationSPA_Object((1,3,6,1,4,1,248,11,250,1,5,22,1,7),_Hm2PortLockingArpLastVerificationSPA_Type())
hm2PortLockingArpLastVerificationSPA.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationSPA.setStatus(_A)
_Hm2PortLockingArpLastVerificationTPA_Type=IpAddress
_Hm2PortLockingArpLastVerificationTPA_Object=MibTableColumn
hm2PortLockingArpLastVerificationTPA=_Hm2PortLockingArpLastVerificationTPA_Object((1,3,6,1,4,1,248,11,250,1,5,22,1,8),_Hm2PortLockingArpLastVerificationTPA_Type())
hm2PortLockingArpLastVerificationTPA.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastVerificationTPA.setStatus(_A)
_Hm2PortLockingArpLastAlarmTable_Object=MibTable
hm2PortLockingArpLastAlarmTable=_Hm2PortLockingArpLastAlarmTable_Object((1,3,6,1,4,1,248,11,250,1,5,23))
if mibBuilder.loadTexts:hm2PortLockingArpLastAlarmTable.setStatus(_A)
_Hm2PortLockingArpLastAlarmEntry_Object=MibTableRow
hm2PortLockingArpLastAlarmEntry=_Hm2PortLockingArpLastAlarmEntry_Object((1,3,6,1,4,1,248,11,250,1,5,23,1))
hm2PortLockingArpLastAlarmEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PortLockingArpLastAlarmEntry.setStatus(_A)
class _Hm2PortLockingArpLastAlarmError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,5,6,7)));namedValues=NamedValues(*((_L,0),('newEntry',5),('changedEntry',6),('violation',7)))
_Hm2PortLockingArpLastAlarmError_Type.__name__=_E
_Hm2PortLockingArpLastAlarmError_Object=MibTableColumn
hm2PortLockingArpLastAlarmError=_Hm2PortLockingArpLastAlarmError_Object((1,3,6,1,4,1,248,11,250,1,5,23,1,1),_Hm2PortLockingArpLastAlarmError_Type())
hm2PortLockingArpLastAlarmError.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastAlarmError.setStatus(_A)
_Hm2PortLockingArpLastAlarmIpAddress_Type=IpAddress
_Hm2PortLockingArpLastAlarmIpAddress_Object=MibTableColumn
hm2PortLockingArpLastAlarmIpAddress=_Hm2PortLockingArpLastAlarmIpAddress_Object((1,3,6,1,4,1,248,11,250,1,5,23,1,2),_Hm2PortLockingArpLastAlarmIpAddress_Type())
hm2PortLockingArpLastAlarmIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastAlarmIpAddress.setStatus(_A)
_Hm2PortLockingArpLastAlarmOldMacAddress_Type=MacAddress
_Hm2PortLockingArpLastAlarmOldMacAddress_Object=MibTableColumn
hm2PortLockingArpLastAlarmOldMacAddress=_Hm2PortLockingArpLastAlarmOldMacAddress_Object((1,3,6,1,4,1,248,11,250,1,5,23,1,3),_Hm2PortLockingArpLastAlarmOldMacAddress_Type())
hm2PortLockingArpLastAlarmOldMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastAlarmOldMacAddress.setStatus(_A)
_Hm2PortLockingArpLastAlarmNewMacAddress_Type=MacAddress
_Hm2PortLockingArpLastAlarmNewMacAddress_Object=MibTableColumn
hm2PortLockingArpLastAlarmNewMacAddress=_Hm2PortLockingArpLastAlarmNewMacAddress_Object((1,3,6,1,4,1,248,11,250,1,5,23,1,4),_Hm2PortLockingArpLastAlarmNewMacAddress_Type())
hm2PortLockingArpLastAlarmNewMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PortLockingArpLastAlarmNewMacAddress.setStatus(_A)
hm2PortLockingViolation=NotificationType((1,3,6,1,4,1,248,11,250,0,1))
hm2PortLockingViolation.setObjects(*((_G,_H),(_D,_T)))
if mibBuilder.loadTexts:hm2PortLockingViolation.setStatus(_A)
hm2PortLockingArpVerificationError=NotificationType((1,3,6,1,4,1,248,11,250,0,2))
hm2PortLockingArpVerificationError.setObjects(*((_G,_H),(_D,_U),(_D,_V),(_D,_W),(_D,_X),(_D,_Y),(_D,_Z),(_D,_a)))
if mibBuilder.loadTexts:hm2PortLockingArpVerificationError.setStatus(_A)
hm2PortLockingArpAlarm=NotificationType((1,3,6,1,4,1,248,11,250,0,3))
hm2PortLockingArpAlarm.setObjects(*((_G,_H),(_D,_b),(_D,_c),(_D,_d),(_D,_e)))
if mibBuilder.loadTexts:hm2PortLockingArpAlarm.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hm2PortLocking':hm2PortLocking,'hm2PortLockingMibNotifications':hm2PortLockingMibNotifications,'hm2PortLockingViolation':hm2PortLockingViolation,'hm2PortLockingArpVerificationError':hm2PortLockingArpVerificationError,'hm2PortLockingArpAlarm':hm2PortLockingArpAlarm,'hm2PortLockingMibObjects':hm2PortLockingMibObjects,'hm2PortLockingGroup':hm2PortLockingGroup,'hm2GlobalPortLockingMode':hm2GlobalPortLockingMode,'hm2GlobalPortLockingOperMode':hm2GlobalPortLockingOperMode,'hm2GlobalPortLockingLockOnlyPorts':hm2GlobalPortLockingLockOnlyPorts,'hm2GlobalPortLockingFallbackTimer':hm2GlobalPortLockingFallbackTimer,'hm2GlobalPortLockingFallbackTimeRemaining':hm2GlobalPortLockingFallbackTimeRemaining,'hm2GlobalPortLockingStatusMessage':hm2GlobalPortLockingStatusMessage,'hm2GlobalPortLockingNumDynamicEntries':hm2GlobalPortLockingNumDynamicEntries,'hm2GlobalPortLockingNumStaticEntries':hm2GlobalPortLockingNumStaticEntries,'hm2GlobalPortLockingIgnoreUplinkPorts':hm2GlobalPortLockingIgnoreUplinkPorts,'hm2PortLockingTable':hm2PortLockingTable,'hm2PortLockingEntry':hm2PortLockingEntry,'hm2PortLockingMode':hm2PortLockingMode,'hm2PortLockingDisabledByLocking':hm2PortLockingDisabledByLocking,'hm2PortLockingStaticLimit':hm2PortLockingStaticLimit,'hm2PortLockingViolationTrapMode':hm2PortLockingViolationTrapMode,_T:hm2PortLockingLastDiscardedMAC,'hm2PortLockingNumDynamicEntries':hm2PortLockingNumDynamicEntries,'hm2PortLockingNumStaticEntries':hm2PortLockingNumStaticEntries,'hm2PortLockingMACAddressAdd':hm2PortLockingMACAddressAdd,'hm2PortLockingMACAddressRemove':hm2PortLockingMACAddressRemove,'hm2PortLockingStatusMessage':hm2PortLockingStatusMessage,'hm2PortLockingNumViolationEntries':hm2PortLockingNumViolationEntries,'hm2PortLockingIsUplinkPort':hm2PortLockingIsUplinkPort,'hm2PortLockingIsMacLockedPort':hm2PortLockingIsMacLockedPort,'hm2PortLockingDynamicTable':hm2PortLockingDynamicTable,'hm2PortLockingDynamicEntry':hm2PortLockingDynamicEntry,_O:hm2PortLockingDynamicVLANId,_P:hm2PortLockingDynamicMACAddress,'hm2PortLockingStaticTable':hm2PortLockingStaticTable,'hm2PortLockingStaticEntry':hm2PortLockingStaticEntry,_Q:hm2PortLockingStaticVLANId,_R:hm2PortLockingStaticMACAddress,'hm2GlobalPortLockingMethod':hm2GlobalPortLockingMethod,'hm2GlobalPortLockingResetMacViolation':hm2GlobalPortLockingResetMacViolation,'hm2GlobalPortLockingUplinkDetectionMode':hm2GlobalPortLockingUplinkDetectionMode,'hm2GlobalPortLockingUplinkFreezeMacAddresses':hm2GlobalPortLockingUplinkFreezeMacAddresses,'hm2GlobalPortLockingUplinkReportMacAddresses':hm2GlobalPortLockingUplinkReportMacAddresses,'hm2PortLockingArpGroup':hm2PortLockingArpGroup,'hm2GlobalPortLockingArpInspectionMode':hm2GlobalPortLockingArpInspectionMode,'hm2GlobalPortLockingArpInspectionDropMode':hm2GlobalPortLockingArpInspectionDropMode,'hm2GlobalPortLockingArpVerifySrcMac':hm2GlobalPortLockingArpVerifySrcMac,'hm2GlobalPortLockingArpVerifyDstMac':hm2GlobalPortLockingArpVerifyDstMac,'hm2GlobalPortLockingArpVerifyIp':hm2GlobalPortLockingArpVerifyIp,'hm2GlobalPortLockingArpVerifySubnet':hm2GlobalPortLockingArpVerifySubnet,'hm2GlobalPortLockingSendVerificationTrap':hm2GlobalPortLockingSendVerificationTrap,'hm2GlobalPortLockingSendDatabaseModificationTrap':hm2GlobalPortLockingSendDatabaseModificationTrap,'hm2GlobalPortLockingSendDatabaseAlarmTrap':hm2GlobalPortLockingSendDatabaseAlarmTrap,'hm2GlobalPortLockingArpResetCache':hm2GlobalPortLockingArpResetCache,'hm2GlobalPortLockingArpInspectionTableEntries':hm2GlobalPortLockingArpInspectionTableEntries,'hm2PortLockingArpDatabaseTable':hm2PortLockingArpDatabaseTable,'hm2PortLockingArpDatabaseEntry':hm2PortLockingArpDatabaseEntry,_S:hm2PortLockingArpDatabaseIpAddr,'hm2PortLockingArpDatabaseIfIndex':hm2PortLockingArpDatabaseIfIndex,'hm2PortLockingArpDatabaseVlanId':hm2PortLockingArpDatabaseVlanId,'hm2PortLockingArpDatabaseMacAddr':hm2PortLockingArpDatabaseMacAddr,'hm2PortLockingArpDatabaseHitCounter':hm2PortLockingArpDatabaseHitCounter,'hm2PortLockingArpDatabaseIfAlarmCounter':hm2PortLockingArpDatabaseIfAlarmCounter,'hm2PortLockingArpDatabaseMacAlarmCounter':hm2PortLockingArpDatabaseMacAlarmCounter,'hm2PortLockingArpDatabaseDropCounter':hm2PortLockingArpDatabaseDropCounter,'hm2PortLockingArpDatabaseType':hm2PortLockingArpDatabaseType,'hm2PortLockingArpDatabaseStorageType':hm2PortLockingArpDatabaseStorageType,'hm2PortLockingArpDatabaseRowStatus':hm2PortLockingArpDatabaseRowStatus,'hm2GlobalPortLockingArpStatistics':hm2GlobalPortLockingArpStatistics,'hm2GlobalPortLockingArpStatisticsPacketsReceived':hm2GlobalPortLockingArpStatisticsPacketsReceived,'hm2GlobalPortLockingArpStatisticsUcPacketsReceived':hm2GlobalPortLockingArpStatisticsUcPacketsReceived,'hm2GlobalPortLockingArpStatisticsSrcMacFailure':hm2GlobalPortLockingArpStatisticsSrcMacFailure,'hm2GlobalPortLockingArpStatisticsDstMacFailure':hm2GlobalPortLockingArpStatisticsDstMacFailure,'hm2GlobalPortLockingArpStatisticsIpFailure':hm2GlobalPortLockingArpStatisticsIpFailure,'hm2GlobalPortLockingArpStatisticsSubnetFailure':hm2GlobalPortLockingArpStatisticsSubnetFailure,'hm2GlobalPortLockingArpStatisticsDropCounter':hm2GlobalPortLockingArpStatisticsDropCounter,'hm2PortLockingArpLastVerificationTable':hm2PortLockingArpLastVerificationTable,'hm2PortLockingArpLastVerificationEntry':hm2PortLockingArpLastVerificationEntry,_V:hm2PortLockingArpLastVerificationError,_U:hm2PortLockingArpLastVerificationType,_W:hm2PortLockingArpLastVerificationSA,_X:hm2PortLockingArpLastVerificationDA,_Y:hm2PortLockingArpLastVerificationSHA,_Z:hm2PortLockingArpLastVerificationTHA,'hm2PortLockingArpLastVerificationSPA':hm2PortLockingArpLastVerificationSPA,_a:hm2PortLockingArpLastVerificationTPA,'hm2PortLockingArpLastAlarmTable':hm2PortLockingArpLastAlarmTable,'hm2PortLockingArpLastAlarmEntry':hm2PortLockingArpLastAlarmEntry,_b:hm2PortLockingArpLastAlarmError,_c:hm2PortLockingArpLastAlarmIpAddress,_d:hm2PortLockingArpLastAlarmOldMacAddress,_e:hm2PortLockingArpLastAlarmNewMacAddress})