_N='hpnicfSysLoghostTrapVpnName'
_M='hpnicfSysLoghostIpaddress'
_L='hpnicfSysLoghostIpaddressType'
_K='hpnicfSysLoghostIndex'
_J='DisplayString'
_I='hpnicfSysFirstTrapTime'
_H='OctetString'
_G='seconds'
_F='accessible-for-notify'
_E='read-only'
_D='HPN-ICF-COMMON-SYSTEM-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicf,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicf')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_J,'PhysAddress','TextualConvention')
hpnicfSystem=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,6))
if mibBuilder.loadTexts:hpnicfSystem.setRevisions(('2004-06-30 00:00',))
class _HpnicfWriteConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('save',1))
_HpnicfWriteConfig_Type.__name__=_B
_HpnicfWriteConfig_Object=MibScalar
hpnicfWriteConfig=_HpnicfWriteConfig_Object((1,3,6,1,4,1,11,2,14,11,15,6,5),_HpnicfWriteConfig_Type())
hpnicfWriteConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfWriteConfig.setStatus(_A)
class _HpnicfStartFtpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpnicfStartFtpServer_Type.__name__=_B
_HpnicfStartFtpServer_Object=MibScalar
hpnicfStartFtpServer=_HpnicfStartFtpServer_Object((1,3,6,1,4,1,11,2,14,11,15,6,6),_HpnicfStartFtpServer_Type())
hpnicfStartFtpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStartFtpServer.setStatus(_A)
class _HpnicfReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('reboot',1)))
_HpnicfReboot_Type.__name__=_B
_HpnicfReboot_Object=MibScalar
hpnicfReboot=_HpnicfReboot_Object((1,3,6,1,4,1,11,2,14,11,15,6,7),_HpnicfReboot_Type())
hpnicfReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfReboot.setStatus(_A)
_HpnicfSystemNotification_ObjectIdentity=ObjectIdentity
hpnicfSystemNotification=_HpnicfSystemNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,6,8))
_HpnicfSoftwareVersion_Type=DisplayString
_HpnicfSoftwareVersion_Object=MibScalar
hpnicfSoftwareVersion=_HpnicfSoftwareVersion_Object((1,3,6,1,4,1,11,2,14,11,15,6,9),_HpnicfSoftwareVersion_Type())
hpnicfSoftwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSoftwareVersion.setStatus(_A)
class _HpnicfSysBootType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('coldStart',1),('warmStart',2)))
_HpnicfSysBootType_Type.__name__=_B
_HpnicfSysBootType_Object=MibScalar
hpnicfSysBootType=_HpnicfSysBootType_Object((1,3,6,1,4,1,11,2,14,11,15,6,10),_HpnicfSysBootType_Type())
hpnicfSysBootType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSysBootType.setStatus(_A)
_HpnicfSystemInfo_ObjectIdentity=ObjectIdentity
hpnicfSystemInfo=_HpnicfSystemInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,6,11))
class _HpnicfSysStatisticPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_HpnicfSysStatisticPeriod_Type.__name__=_B
_HpnicfSysStatisticPeriod_Object=MibScalar
hpnicfSysStatisticPeriod=_HpnicfSysStatisticPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,1),_HpnicfSysStatisticPeriod_Type())
hpnicfSysStatisticPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSysStatisticPeriod.setStatus(_A)
if mibBuilder.loadTexts:hpnicfSysStatisticPeriod.setUnits(_G)
class _HpnicfSysSamplePeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_HpnicfSysSamplePeriod_Type.__name__=_B
_HpnicfSysSamplePeriod_Object=MibScalar
hpnicfSysSamplePeriod=_HpnicfSysSamplePeriod_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,2),_HpnicfSysSamplePeriod_Type())
hpnicfSysSamplePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSysSamplePeriod.setStatus(_A)
if mibBuilder.loadTexts:hpnicfSysSamplePeriod.setUnits(_G)
class _HpnicfSysTrapResendPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_HpnicfSysTrapResendPeriod_Type.__name__=_B
_HpnicfSysTrapResendPeriod_Object=MibScalar
hpnicfSysTrapResendPeriod=_HpnicfSysTrapResendPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,3),_HpnicfSysTrapResendPeriod_Type())
hpnicfSysTrapResendPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSysTrapResendPeriod.setStatus(_A)
if mibBuilder.loadTexts:hpnicfSysTrapResendPeriod.setUnits(_G)
class _HpnicfSysTrapCollectionPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_HpnicfSysTrapCollectionPeriod_Type.__name__=_B
_HpnicfSysTrapCollectionPeriod_Object=MibScalar
hpnicfSysTrapCollectionPeriod=_HpnicfSysTrapCollectionPeriod_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,4),_HpnicfSysTrapCollectionPeriod_Type())
hpnicfSysTrapCollectionPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSysTrapCollectionPeriod.setStatus(_A)
if mibBuilder.loadTexts:hpnicfSysTrapCollectionPeriod.setUnits(_G)
_HpnicfSysSnmpPort_Type=Integer32
_HpnicfSysSnmpPort_Object=MibScalar
hpnicfSysSnmpPort=_HpnicfSysSnmpPort_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,5),_HpnicfSysSnmpPort_Type())
hpnicfSysSnmpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSysSnmpPort.setStatus(_A)
_HpnicfSysSnmpTrapPort_Type=Integer32
_HpnicfSysSnmpTrapPort_Object=MibScalar
hpnicfSysSnmpTrapPort=_HpnicfSysSnmpTrapPort_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,6),_HpnicfSysSnmpTrapPort_Type())
hpnicfSysSnmpTrapPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSysSnmpTrapPort.setStatus(_A)
class _HpnicfSysNetID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfSysNetID_Type.__name__=_H
_HpnicfSysNetID_Object=MibScalar
hpnicfSysNetID=_HpnicfSysNetID_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,7),_HpnicfSysNetID_Type())
hpnicfSysNetID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSysNetID.setStatus(_A)
_HpnicfSysLastSampleTime_Type=DateAndTime
_HpnicfSysLastSampleTime_Object=MibScalar
hpnicfSysLastSampleTime=_HpnicfSysLastSampleTime_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,8),_HpnicfSysLastSampleTime_Type())
hpnicfSysLastSampleTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfSysLastSampleTime.setStatus(_A)
class _HpnicfSysTrapSendNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_HpnicfSysTrapSendNum_Type.__name__=_B
_HpnicfSysTrapSendNum_Object=MibScalar
hpnicfSysTrapSendNum=_HpnicfSysTrapSendNum_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,9),_HpnicfSysTrapSendNum_Type())
hpnicfSysTrapSendNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSysTrapSendNum.setStatus(_A)
_HpnicfSysFirstTrapTime_Type=TimeTicks
_HpnicfSysFirstTrapTime_Object=MibScalar
hpnicfSysFirstTrapTime=_HpnicfSysFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,10),_HpnicfSysFirstTrapTime_Type())
hpnicfSysFirstTrapTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysFirstTrapTime.setStatus(_A)
class _HpnicfSysBannerMOTD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2000))
_HpnicfSysBannerMOTD_Type.__name__=_H
_HpnicfSysBannerMOTD_Object=MibScalar
hpnicfSysBannerMOTD=_HpnicfSysBannerMOTD_Object((1,3,6,1,4,1,11,2,14,11,15,6,11,11),_HpnicfSysBannerMOTD_Type())
hpnicfSysBannerMOTD.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfSysBannerMOTD.setStatus(_A)
_HpnicfSystemNotificationInfo_ObjectIdentity=ObjectIdentity
hpnicfSystemNotificationInfo=_HpnicfSystemNotificationInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,6,12))
_HpnicfSysLoghostIndex_Type=Integer32
_HpnicfSysLoghostIndex_Object=MibScalar
hpnicfSysLoghostIndex=_HpnicfSysLoghostIndex_Object((1,3,6,1,4,1,11,2,14,11,15,6,12,1),_HpnicfSysLoghostIndex_Type())
hpnicfSysLoghostIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysLoghostIndex.setStatus(_A)
_HpnicfSysLoghostIpaddressType_Type=InetAddressType
_HpnicfSysLoghostIpaddressType_Object=MibScalar
hpnicfSysLoghostIpaddressType=_HpnicfSysLoghostIpaddressType_Object((1,3,6,1,4,1,11,2,14,11,15,6,12,2),_HpnicfSysLoghostIpaddressType_Type())
hpnicfSysLoghostIpaddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysLoghostIpaddressType.setStatus(_A)
_HpnicfSysLoghostIpaddress_Type=InetAddress
_HpnicfSysLoghostIpaddress_Object=MibScalar
hpnicfSysLoghostIpaddress=_HpnicfSysLoghostIpaddress_Object((1,3,6,1,4,1,11,2,14,11,15,6,12,3),_HpnicfSysLoghostIpaddress_Type())
hpnicfSysLoghostIpaddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysLoghostIpaddress.setStatus(_A)
class _HpnicfSysLoghostTrapVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfSysLoghostTrapVpnName_Type.__name__=_J
_HpnicfSysLoghostTrapVpnName_Object=MibScalar
hpnicfSysLoghostTrapVpnName=_HpnicfSysLoghostTrapVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,6,12,4),_HpnicfSysLoghostTrapVpnName_Type())
hpnicfSysLoghostTrapVpnName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfSysLoghostTrapVpnName.setStatus(_A)
hpnicfWriteSuccessTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,6,8,1))
if mibBuilder.loadTexts:hpnicfWriteSuccessTrap.setStatus(_A)
hpnicfWriteFailureTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,6,8,2))
if mibBuilder.loadTexts:hpnicfWriteFailureTrap.setStatus(_A)
hpnicfRebootSendTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,6,8,3))
if mibBuilder.loadTexts:hpnicfRebootSendTrap.setStatus(_A)
hpnicfSysColdStartTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,6,8,4))
hpnicfSysColdStartTrap.setObjects((_D,_I))
if mibBuilder.loadTexts:hpnicfSysColdStartTrap.setStatus(_A)
hpnicfSysWarmStartTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,6,8,5))
hpnicfSysWarmStartTrap.setObjects((_D,_I))
if mibBuilder.loadTexts:hpnicfSysWarmStartTrap.setStatus(_A)
hpnicfSysLoghostUnreachableTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,6,8,6))
hpnicfSysLoghostUnreachableTrap.setObjects(*((_D,_K),(_D,_L),(_D,_M),(_D,_N)))
if mibBuilder.loadTexts:hpnicfSysLoghostUnreachableTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfSystem':hpnicfSystem,'hpnicfWriteConfig':hpnicfWriteConfig,'hpnicfStartFtpServer':hpnicfStartFtpServer,'hpnicfReboot':hpnicfReboot,'hpnicfSystemNotification':hpnicfSystemNotification,'hpnicfWriteSuccessTrap':hpnicfWriteSuccessTrap,'hpnicfWriteFailureTrap':hpnicfWriteFailureTrap,'hpnicfRebootSendTrap':hpnicfRebootSendTrap,'hpnicfSysColdStartTrap':hpnicfSysColdStartTrap,'hpnicfSysWarmStartTrap':hpnicfSysWarmStartTrap,'hpnicfSysLoghostUnreachableTrap':hpnicfSysLoghostUnreachableTrap,'hpnicfSoftwareVersion':hpnicfSoftwareVersion,'hpnicfSysBootType':hpnicfSysBootType,'hpnicfSystemInfo':hpnicfSystemInfo,'hpnicfSysStatisticPeriod':hpnicfSysStatisticPeriod,'hpnicfSysSamplePeriod':hpnicfSysSamplePeriod,'hpnicfSysTrapResendPeriod':hpnicfSysTrapResendPeriod,'hpnicfSysTrapCollectionPeriod':hpnicfSysTrapCollectionPeriod,'hpnicfSysSnmpPort':hpnicfSysSnmpPort,'hpnicfSysSnmpTrapPort':hpnicfSysSnmpTrapPort,'hpnicfSysNetID':hpnicfSysNetID,'hpnicfSysLastSampleTime':hpnicfSysLastSampleTime,'hpnicfSysTrapSendNum':hpnicfSysTrapSendNum,_I:hpnicfSysFirstTrapTime,'hpnicfSysBannerMOTD':hpnicfSysBannerMOTD,'hpnicfSystemNotificationInfo':hpnicfSystemNotificationInfo,_K:hpnicfSysLoghostIndex,_L:hpnicfSysLoghostIpaddressType,_M:hpnicfSysLoghostIpaddress,_N:hpnicfSysLoghostTrapVpnName})