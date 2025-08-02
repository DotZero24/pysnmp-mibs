_H='OctetString'
_G='hwSysFirstTrapTime'
_F='A3COM-HUAWEI-COMMON-MIB'
_E='seconds'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hwSystem,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','hwSystem')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
class _HwWriteConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('save',1))
_HwWriteConfig_Type.__name__=_B
_HwWriteConfig_Object=MibScalar
hwWriteConfig=_HwWriteConfig_Object((1,3,6,1,4,1,43,45,1,10,6,5),_HwWriteConfig_Type())
hwWriteConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hwWriteConfig.setStatus(_A)
class _HwStartFtpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HwStartFtpServer_Type.__name__=_B
_HwStartFtpServer_Object=MibScalar
hwStartFtpServer=_HwStartFtpServer_Object((1,3,6,1,4,1,43,45,1,10,6,6),_HwStartFtpServer_Type())
hwStartFtpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStartFtpServer.setStatus(_A)
class _HwReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reboot',1))
_HwReboot_Type.__name__=_B
_HwReboot_Object=MibScalar
hwReboot=_HwReboot_Object((1,3,6,1,4,1,43,45,1,10,6,7),_HwReboot_Type())
hwReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:hwReboot.setStatus(_A)
_HwSystemNotification_ObjectIdentity=ObjectIdentity
hwSystemNotification=_HwSystemNotification_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,6,8))
_HwSoftwareVersion_Type=DisplayString
_HwSoftwareVersion_Object=MibScalar
hwSoftwareVersion=_HwSoftwareVersion_Object((1,3,6,1,4,1,43,45,1,10,6,9),_HwSoftwareVersion_Type())
hwSoftwareVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSoftwareVersion.setStatus(_A)
class _HwSysBootType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('coldStart',1),('warmStart',2)))
_HwSysBootType_Type.__name__=_B
_HwSysBootType_Object=MibScalar
hwSysBootType=_HwSysBootType_Object((1,3,6,1,4,1,43,45,1,10,6,10),_HwSysBootType_Type())
hwSysBootType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysBootType.setStatus(_A)
_HwSystemInfo_ObjectIdentity=ObjectIdentity
hwSystemInfo=_HwSystemInfo_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,6,11))
class _HwSysStatisticPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_HwSysStatisticPeriod_Type.__name__=_B
_HwSysStatisticPeriod_Object=MibScalar
hwSysStatisticPeriod=_HwSysStatisticPeriod_Object((1,3,6,1,4,1,43,45,1,10,6,11,1),_HwSysStatisticPeriod_Type())
hwSysStatisticPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysStatisticPeriod.setStatus(_A)
if mibBuilder.loadTexts:hwSysStatisticPeriod.setUnits(_E)
class _HwSysSamplePeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_HwSysSamplePeriod_Type.__name__=_B
_HwSysSamplePeriod_Object=MibScalar
hwSysSamplePeriod=_HwSysSamplePeriod_Object((1,3,6,1,4,1,43,45,1,10,6,11,2),_HwSysSamplePeriod_Type())
hwSysSamplePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysSamplePeriod.setStatus(_A)
if mibBuilder.loadTexts:hwSysSamplePeriod.setUnits(_E)
class _HwSysTrapResendPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_HwSysTrapResendPeriod_Type.__name__=_B
_HwSysTrapResendPeriod_Object=MibScalar
hwSysTrapResendPeriod=_HwSysTrapResendPeriod_Object((1,3,6,1,4,1,43,45,1,10,6,11,3),_HwSysTrapResendPeriod_Type())
hwSysTrapResendPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysTrapResendPeriod.setStatus(_A)
if mibBuilder.loadTexts:hwSysTrapResendPeriod.setUnits(_E)
class _HwSysTrapCollectionPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_HwSysTrapCollectionPeriod_Type.__name__=_B
_HwSysTrapCollectionPeriod_Object=MibScalar
hwSysTrapCollectionPeriod=_HwSysTrapCollectionPeriod_Object((1,3,6,1,4,1,43,45,1,10,6,11,4),_HwSysTrapCollectionPeriod_Type())
hwSysTrapCollectionPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysTrapCollectionPeriod.setStatus(_A)
if mibBuilder.loadTexts:hwSysTrapCollectionPeriod.setUnits(_E)
_HwSysSnmpPort_Type=Integer32
_HwSysSnmpPort_Object=MibScalar
hwSysSnmpPort=_HwSysSnmpPort_Object((1,3,6,1,4,1,43,45,1,10,6,11,5),_HwSysSnmpPort_Type())
hwSysSnmpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysSnmpPort.setStatus(_A)
_HwSysSnmpTrapPort_Type=Integer32
_HwSysSnmpTrapPort_Object=MibScalar
hwSysSnmpTrapPort=_HwSysSnmpTrapPort_Object((1,3,6,1,4,1,43,45,1,10,6,11,6),_HwSysSnmpTrapPort_Type())
hwSysSnmpTrapPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysSnmpTrapPort.setStatus(_A)
class _HwSysNetID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HwSysNetID_Type.__name__=_H
_HwSysNetID_Object=MibScalar
hwSysNetID=_HwSysNetID_Object((1,3,6,1,4,1,43,45,1,10,6,11,7),_HwSysNetID_Type())
hwSysNetID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysNetID.setStatus(_A)
_HwSysLastSampleTime_Type=DateAndTime
_HwSysLastSampleTime_Object=MibScalar
hwSysLastSampleTime=_HwSysLastSampleTime_Object((1,3,6,1,4,1,43,45,1,10,6,11,8),_HwSysLastSampleTime_Type())
hwSysLastSampleTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysLastSampleTime.setStatus(_A)
class _HwSysTrapSendNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_HwSysTrapSendNum_Type.__name__=_B
_HwSysTrapSendNum_Object=MibScalar
hwSysTrapSendNum=_HwSysTrapSendNum_Object((1,3,6,1,4,1,43,45,1,10,6,11,9),_HwSysTrapSendNum_Type())
hwSysTrapSendNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysTrapSendNum.setStatus(_A)
_HwSysFirstTrapTime_Type=TimeTicks
_HwSysFirstTrapTime_Object=MibScalar
hwSysFirstTrapTime=_HwSysFirstTrapTime_Object((1,3,6,1,4,1,43,45,1,10,6,11,10),_HwSysFirstTrapTime_Type())
hwSysFirstTrapTime.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hwSysFirstTrapTime.setStatus(_A)
hwWriteSuccessTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,6,8,1))
if mibBuilder.loadTexts:hwWriteSuccessTrap.setStatus(_A)
hwWriteFailureTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,6,8,2))
if mibBuilder.loadTexts:hwWriteFailureTrap.setStatus(_A)
hwRebootSendTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,6,8,3))
if mibBuilder.loadTexts:hwRebootSendTrap.setStatus(_A)
hwSysColdStartTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,6,8,4))
hwSysColdStartTrap.setObjects((_F,_G))
if mibBuilder.loadTexts:hwSysColdStartTrap.setStatus(_A)
hwSysWarmStartTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,6,8,5))
hwSysWarmStartTrap.setObjects((_F,_G))
if mibBuilder.loadTexts:hwSysWarmStartTrap.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hwWriteConfig':hwWriteConfig,'hwStartFtpServer':hwStartFtpServer,'hwReboot':hwReboot,'hwSystemNotification':hwSystemNotification,'hwWriteSuccessTrap':hwWriteSuccessTrap,'hwWriteFailureTrap':hwWriteFailureTrap,'hwRebootSendTrap':hwRebootSendTrap,'hwSysColdStartTrap':hwSysColdStartTrap,'hwSysWarmStartTrap':hwSysWarmStartTrap,'hwSoftwareVersion':hwSoftwareVersion,'hwSysBootType':hwSysBootType,'hwSystemInfo':hwSystemInfo,'hwSysStatisticPeriod':hwSysStatisticPeriod,'hwSysSamplePeriod':hwSysSamplePeriod,'hwSysTrapResendPeriod':hwSysTrapResendPeriod,'hwSysTrapCollectionPeriod':hwSysTrapCollectionPeriod,'hwSysSnmpPort':hwSysSnmpPort,'hwSysSnmpTrapPort':hwSysSnmpTrapPort,'hwSysNetID':hwSysNetID,'hwSysLastSampleTime':hwSysLastSampleTime,'hwSysTrapSendNum':hwSysTrapSendNum,_G:hwSysFirstTrapTime})