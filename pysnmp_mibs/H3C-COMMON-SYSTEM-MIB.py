_R='hwSysLoghostTrapVpnName'
_Q='hwSysLoghostIpaddress'
_P='hwSysLoghostIpaddressType'
_O='hwSysLoghostIndex'
_N='hwSystemWorkingModeIndex'
_M='read-create'
_L='not-accessible'
_K='hwSystemDiagInfoIndex'
_J='hwSysFirstTrapTime'
_I='OctetString'
_H='seconds'
_G='accessible-for-notify'
_F='DisplayString'
_E='H3C-COMMON-SYSTEM-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3c,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3c')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention','TimeStamp')
hwSystem=ModuleIdentity((1,3,6,1,4,1,2011,10,6))
if mibBuilder.loadTexts:hwSystem.setRevisions(('2015-05-05 00:00','2015-03-25 00:00','2014-08-07 17:10','2013-09-13 00:00','2013-05-28 00:00','2012-06-06 00:00','2012-01-07 00:00','2009-05-05 00:00','2008-11-11 00:00','2004-10-12 00:00','2004-08-16 00:00','2004-06-30 00:00'))
class _HwWriteConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('save',1))
_HwWriteConfig_Type.__name__=_B
_HwWriteConfig_Object=MibScalar
hwWriteConfig=_HwWriteConfig_Object((1,3,6,1,4,1,2011,10,6,5),_HwWriteConfig_Type())
hwWriteConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:hwWriteConfig.setStatus(_A)
class _HwStartFtpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HwStartFtpServer_Type.__name__=_B
_HwStartFtpServer_Object=MibScalar
hwStartFtpServer=_HwStartFtpServer_Object((1,3,6,1,4,1,2011,10,6,6),_HwStartFtpServer_Type())
hwStartFtpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:hwStartFtpServer.setStatus(_A)
class _HwReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('reboot',1)))
_HwReboot_Type.__name__=_B
_HwReboot_Object=MibScalar
hwReboot=_HwReboot_Object((1,3,6,1,4,1,2011,10,6,7),_HwReboot_Type())
hwReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:hwReboot.setStatus(_A)
_HwSystemNotification_ObjectIdentity=ObjectIdentity
hwSystemNotification=_HwSystemNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,6,8))
_HwSoftwareVersion_Type=DisplayString
_HwSoftwareVersion_Object=MibScalar
hwSoftwareVersion=_HwSoftwareVersion_Object((1,3,6,1,4,1,2011,10,6,9),_HwSoftwareVersion_Type())
hwSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSoftwareVersion.setStatus(_A)
class _HwSysBootType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('coldStart',1),('warmStart',2)))
_HwSysBootType_Type.__name__=_B
_HwSysBootType_Object=MibScalar
hwSysBootType=_HwSysBootType_Object((1,3,6,1,4,1,2011,10,6,10),_HwSysBootType_Type())
hwSysBootType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysBootType.setStatus(_A)
_HwSystemInfo_ObjectIdentity=ObjectIdentity
hwSystemInfo=_HwSystemInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,6,11))
class _HwSysStatisticPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_HwSysStatisticPeriod_Type.__name__=_B
_HwSysStatisticPeriod_Object=MibScalar
hwSysStatisticPeriod=_HwSysStatisticPeriod_Object((1,3,6,1,4,1,2011,10,6,11,1),_HwSysStatisticPeriod_Type())
hwSysStatisticPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysStatisticPeriod.setStatus(_A)
if mibBuilder.loadTexts:hwSysStatisticPeriod.setUnits(_H)
class _HwSysSamplePeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_HwSysSamplePeriod_Type.__name__=_B
_HwSysSamplePeriod_Object=MibScalar
hwSysSamplePeriod=_HwSysSamplePeriod_Object((1,3,6,1,4,1,2011,10,6,11,2),_HwSysSamplePeriod_Type())
hwSysSamplePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysSamplePeriod.setStatus(_A)
if mibBuilder.loadTexts:hwSysSamplePeriod.setUnits(_H)
class _HwSysTrapResendPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_HwSysTrapResendPeriod_Type.__name__=_B
_HwSysTrapResendPeriod_Object=MibScalar
hwSysTrapResendPeriod=_HwSysTrapResendPeriod_Object((1,3,6,1,4,1,2011,10,6,11,3),_HwSysTrapResendPeriod_Type())
hwSysTrapResendPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysTrapResendPeriod.setStatus(_A)
if mibBuilder.loadTexts:hwSysTrapResendPeriod.setUnits(_H)
class _HwSysTrapCollectionPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_HwSysTrapCollectionPeriod_Type.__name__=_B
_HwSysTrapCollectionPeriod_Object=MibScalar
hwSysTrapCollectionPeriod=_HwSysTrapCollectionPeriod_Object((1,3,6,1,4,1,2011,10,6,11,4),_HwSysTrapCollectionPeriod_Type())
hwSysTrapCollectionPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysTrapCollectionPeriod.setStatus(_A)
if mibBuilder.loadTexts:hwSysTrapCollectionPeriod.setUnits(_H)
_HwSysSnmpPort_Type=Integer32
_HwSysSnmpPort_Object=MibScalar
hwSysSnmpPort=_HwSysSnmpPort_Object((1,3,6,1,4,1,2011,10,6,11,5),_HwSysSnmpPort_Type())
hwSysSnmpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysSnmpPort.setStatus(_A)
_HwSysSnmpTrapPort_Type=Integer32
_HwSysSnmpTrapPort_Object=MibScalar
hwSysSnmpTrapPort=_HwSysSnmpTrapPort_Object((1,3,6,1,4,1,2011,10,6,11,6),_HwSysSnmpTrapPort_Type())
hwSysSnmpTrapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysSnmpTrapPort.setStatus(_A)
class _HwSysNetID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HwSysNetID_Type.__name__=_I
_HwSysNetID_Object=MibScalar
hwSysNetID=_HwSysNetID_Object((1,3,6,1,4,1,2011,10,6,11,7),_HwSysNetID_Type())
hwSysNetID.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysNetID.setStatus(_A)
_HwSysLastSampleTime_Type=DateAndTime
_HwSysLastSampleTime_Object=MibScalar
hwSysLastSampleTime=_HwSysLastSampleTime_Object((1,3,6,1,4,1,2011,10,6,11,8),_HwSysLastSampleTime_Type())
hwSysLastSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSysLastSampleTime.setStatus(_A)
class _HwSysTrapSendNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_HwSysTrapSendNum_Type.__name__=_B
_HwSysTrapSendNum_Object=MibScalar
hwSysTrapSendNum=_HwSysTrapSendNum_Object((1,3,6,1,4,1,2011,10,6,11,9),_HwSysTrapSendNum_Type())
hwSysTrapSendNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysTrapSendNum.setStatus(_A)
_HwSysFirstTrapTime_Type=TimeTicks
_HwSysFirstTrapTime_Object=MibScalar
hwSysFirstTrapTime=_HwSysFirstTrapTime_Object((1,3,6,1,4,1,2011,10,6,11,10),_HwSysFirstTrapTime_Type())
hwSysFirstTrapTime.setMaxAccess(_G)
if mibBuilder.loadTexts:hwSysFirstTrapTime.setStatus(_A)
class _HwSysBannerMOTD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2000))
_HwSysBannerMOTD_Type.__name__=_I
_HwSysBannerMOTD_Object=MibScalar
hwSysBannerMOTD=_HwSysBannerMOTD_Object((1,3,6,1,4,1,2011,10,6,11,11),_HwSysBannerMOTD_Type())
hwSysBannerMOTD.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSysBannerMOTD.setStatus(_A)
_HwSystemNotificationInfo_ObjectIdentity=ObjectIdentity
hwSystemNotificationInfo=_HwSystemNotificationInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,6,12))
_HwSysLoghostIndex_Type=Integer32
_HwSysLoghostIndex_Object=MibScalar
hwSysLoghostIndex=_HwSysLoghostIndex_Object((1,3,6,1,4,1,2011,10,6,12,1),_HwSysLoghostIndex_Type())
hwSysLoghostIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwSysLoghostIndex.setStatus(_A)
_HwSysLoghostIpaddressType_Type=InetAddressType
_HwSysLoghostIpaddressType_Object=MibScalar
hwSysLoghostIpaddressType=_HwSysLoghostIpaddressType_Object((1,3,6,1,4,1,2011,10,6,12,2),_HwSysLoghostIpaddressType_Type())
hwSysLoghostIpaddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:hwSysLoghostIpaddressType.setStatus(_A)
_HwSysLoghostIpaddress_Type=InetAddress
_HwSysLoghostIpaddress_Object=MibScalar
hwSysLoghostIpaddress=_HwSysLoghostIpaddress_Object((1,3,6,1,4,1,2011,10,6,12,3),_HwSysLoghostIpaddress_Type())
hwSysLoghostIpaddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hwSysLoghostIpaddress.setStatus(_A)
class _HwSysLoghostTrapVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HwSysLoghostTrapVpnName_Type.__name__=_F
_HwSysLoghostTrapVpnName_Object=MibScalar
hwSysLoghostTrapVpnName=_HwSysLoghostTrapVpnName_Object((1,3,6,1,4,1,2011,10,6,12,4),_HwSysLoghostTrapVpnName_Type())
hwSysLoghostTrapVpnName.setMaxAccess(_G)
if mibBuilder.loadTexts:hwSysLoghostTrapVpnName.setStatus(_A)
_HwSystemDiagInfoTable_Object=MibTable
hwSystemDiagInfoTable=_HwSystemDiagInfoTable_Object((1,3,6,1,4,1,2011,10,6,13))
if mibBuilder.loadTexts:hwSystemDiagInfoTable.setStatus(_A)
_HwSystemDiagInfoEntry_Object=MibTableRow
hwSystemDiagInfoEntry=_HwSystemDiagInfoEntry_Object((1,3,6,1,4,1,2011,10,6,13,1))
hwSystemDiagInfoEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:hwSystemDiagInfoEntry.setStatus(_A)
class _HwSystemDiagInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwSystemDiagInfoIndex_Type.__name__=_B
_HwSystemDiagInfoIndex_Object=MibTableColumn
hwSystemDiagInfoIndex=_HwSystemDiagInfoIndex_Object((1,3,6,1,4,1,2011,10,6,13,1,1),_HwSystemDiagInfoIndex_Type())
hwSystemDiagInfoIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hwSystemDiagInfoIndex.setStatus(_A)
class _HwSystemDiagInfoFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwSystemDiagInfoFilename_Type.__name__=_F
_HwSystemDiagInfoFilename_Object=MibTableColumn
hwSystemDiagInfoFilename=_HwSystemDiagInfoFilename_Object((1,3,6,1,4,1,2011,10,6,13,1,2),_HwSystemDiagInfoFilename_Type())
hwSystemDiagInfoFilename.setMaxAccess(_M)
if mibBuilder.loadTexts:hwSystemDiagInfoFilename.setStatus(_A)
_HwSystemDiagInfoRowStatus_Type=RowStatus
_HwSystemDiagInfoRowStatus_Object=MibTableColumn
hwSystemDiagInfoRowStatus=_HwSystemDiagInfoRowStatus_Object((1,3,6,1,4,1,2011,10,6,13,1,3),_HwSystemDiagInfoRowStatus_Type())
hwSystemDiagInfoRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:hwSystemDiagInfoRowStatus.setStatus(_A)
_HwSystemDiagInfoOperEndTime_Type=TimeStamp
_HwSystemDiagInfoOperEndTime_Object=MibTableColumn
hwSystemDiagInfoOperEndTime=_HwSystemDiagInfoOperEndTime_Object((1,3,6,1,4,1,2011,10,6,13,1,4),_HwSystemDiagInfoOperEndTime_Type())
hwSystemDiagInfoOperEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSystemDiagInfoOperEndTime.setStatus(_A)
class _HwSystemDiagInfoOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('opInProgress',1),('opSuccess',2),('opFailure',3)))
_HwSystemDiagInfoOperState_Type.__name__=_B
_HwSystemDiagInfoOperState_Object=MibTableColumn
hwSystemDiagInfoOperState=_HwSystemDiagInfoOperState_Object((1,3,6,1,4,1,2011,10,6,13,1,5),_HwSystemDiagInfoOperState_Type())
hwSystemDiagInfoOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSystemDiagInfoOperState.setStatus(_A)
class _HwSystemDiagInfoOperFailReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwSystemDiagInfoOperFailReason_Type.__name__=_F
_HwSystemDiagInfoOperFailReason_Object=MibTableColumn
hwSystemDiagInfoOperFailReason=_HwSystemDiagInfoOperFailReason_Object((1,3,6,1,4,1,2011,10,6,13,1,6),_HwSystemDiagInfoOperFailReason_Type())
hwSystemDiagInfoOperFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSystemDiagInfoOperFailReason.setStatus(_A)
_HwSystemWorkingMode_ObjectIdentity=ObjectIdentity
hwSystemWorkingMode=_HwSystemWorkingMode_ObjectIdentity((1,3,6,1,4,1,2011,10,6,14))
_HwSystemWorkingModeTable_Object=MibTable
hwSystemWorkingModeTable=_HwSystemWorkingModeTable_Object((1,3,6,1,4,1,2011,10,6,14,1))
if mibBuilder.loadTexts:hwSystemWorkingModeTable.setStatus(_A)
_HwSystemWorkingModeEntry_Object=MibTableRow
hwSystemWorkingModeEntry=_HwSystemWorkingModeEntry_Object((1,3,6,1,4,1,2011,10,6,14,1,1))
hwSystemWorkingModeEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:hwSystemWorkingModeEntry.setStatus(_A)
class _HwSystemWorkingModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwSystemWorkingModeIndex_Type.__name__=_B
_HwSystemWorkingModeIndex_Object=MibTableColumn
hwSystemWorkingModeIndex=_HwSystemWorkingModeIndex_Object((1,3,6,1,4,1,2011,10,6,14,1,1,1),_HwSystemWorkingModeIndex_Type())
hwSystemWorkingModeIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hwSystemWorkingModeIndex.setStatus(_A)
class _HwSystemWorkingModeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HwSystemWorkingModeName_Type.__name__=_F
_HwSystemWorkingModeName_Object=MibTableColumn
hwSystemWorkingModeName=_HwSystemWorkingModeName_Object((1,3,6,1,4,1,2011,10,6,14,1,1,2),_HwSystemWorkingModeName_Type())
hwSystemWorkingModeName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSystemWorkingModeName.setStatus(_A)
class _HwSystemWorkingModeDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_HwSystemWorkingModeDescr_Type.__name__=_F
_HwSystemWorkingModeDescr_Object=MibTableColumn
hwSystemWorkingModeDescr=_HwSystemWorkingModeDescr_Object((1,3,6,1,4,1,2011,10,6,14,1,1,3),_HwSystemWorkingModeDescr_Type())
hwSystemWorkingModeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSystemWorkingModeDescr.setStatus(_A)
class _HwSystemWorkingModeDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwSystemWorkingModeDefault_Type.__name__=_B
_HwSystemWorkingModeDefault_Object=MibScalar
hwSystemWorkingModeDefault=_HwSystemWorkingModeDefault_Object((1,3,6,1,4,1,2011,10,6,14,2),_HwSystemWorkingModeDefault_Type())
hwSystemWorkingModeDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSystemWorkingModeDefault.setStatus(_A)
class _HwSystemWorkingModeCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwSystemWorkingModeCurrent_Type.__name__=_B
_HwSystemWorkingModeCurrent_Object=MibScalar
hwSystemWorkingModeCurrent=_HwSystemWorkingModeCurrent_Object((1,3,6,1,4,1,2011,10,6,14,3),_HwSystemWorkingModeCurrent_Type())
hwSystemWorkingModeCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSystemWorkingModeCurrent.setStatus(_A)
class _HwSystemWorkingModeNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwSystemWorkingModeNext_Type.__name__=_B
_HwSystemWorkingModeNext_Object=MibScalar
hwSystemWorkingModeNext=_HwSystemWorkingModeNext_Object((1,3,6,1,4,1,2011,10,6,14,4),_HwSystemWorkingModeNext_Type())
hwSystemWorkingModeNext.setMaxAccess(_D)
if mibBuilder.loadTexts:hwSystemWorkingModeNext.setStatus(_A)
hwWriteSuccessTrap=NotificationType((1,3,6,1,4,1,2011,10,6,8,1))
if mibBuilder.loadTexts:hwWriteSuccessTrap.setStatus(_A)
hwWriteFailureTrap=NotificationType((1,3,6,1,4,1,2011,10,6,8,2))
if mibBuilder.loadTexts:hwWriteFailureTrap.setStatus(_A)
hwRebootSendTrap=NotificationType((1,3,6,1,4,1,2011,10,6,8,3))
if mibBuilder.loadTexts:hwRebootSendTrap.setStatus(_A)
hwSysColdStartTrap=NotificationType((1,3,6,1,4,1,2011,10,6,8,4))
hwSysColdStartTrap.setObjects((_E,_J))
if mibBuilder.loadTexts:hwSysColdStartTrap.setStatus(_A)
hwSysWarmStartTrap=NotificationType((1,3,6,1,4,1,2011,10,6,8,5))
hwSysWarmStartTrap.setObjects((_E,_J))
if mibBuilder.loadTexts:hwSysWarmStartTrap.setStatus(_A)
hwSysLoghostUnreachableTrap=NotificationType((1,3,6,1,4,1,2011,10,6,8,6))
hwSysLoghostUnreachableTrap.setObjects(*((_E,_O),(_E,_P),(_E,_Q),(_E,_R)))
if mibBuilder.loadTexts:hwSysLoghostUnreachableTrap.setStatus(_A)
hwSysDyingGaspTrap=NotificationType((1,3,6,1,4,1,2011,10,6,8,7))
if mibBuilder.loadTexts:hwSysDyingGaspTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hwSystem':hwSystem,'hwWriteConfig':hwWriteConfig,'hwStartFtpServer':hwStartFtpServer,'hwReboot':hwReboot,'hwSystemNotification':hwSystemNotification,'hwWriteSuccessTrap':hwWriteSuccessTrap,'hwWriteFailureTrap':hwWriteFailureTrap,'hwRebootSendTrap':hwRebootSendTrap,'hwSysColdStartTrap':hwSysColdStartTrap,'hwSysWarmStartTrap':hwSysWarmStartTrap,'hwSysLoghostUnreachableTrap':hwSysLoghostUnreachableTrap,'hwSysDyingGaspTrap':hwSysDyingGaspTrap,'hwSoftwareVersion':hwSoftwareVersion,'hwSysBootType':hwSysBootType,'hwSystemInfo':hwSystemInfo,'hwSysStatisticPeriod':hwSysStatisticPeriod,'hwSysSamplePeriod':hwSysSamplePeriod,'hwSysTrapResendPeriod':hwSysTrapResendPeriod,'hwSysTrapCollectionPeriod':hwSysTrapCollectionPeriod,'hwSysSnmpPort':hwSysSnmpPort,'hwSysSnmpTrapPort':hwSysSnmpTrapPort,'hwSysNetID':hwSysNetID,'hwSysLastSampleTime':hwSysLastSampleTime,'hwSysTrapSendNum':hwSysTrapSendNum,_J:hwSysFirstTrapTime,'hwSysBannerMOTD':hwSysBannerMOTD,'hwSystemNotificationInfo':hwSystemNotificationInfo,_O:hwSysLoghostIndex,_P:hwSysLoghostIpaddressType,_Q:hwSysLoghostIpaddress,_R:hwSysLoghostTrapVpnName,'hwSystemDiagInfoTable':hwSystemDiagInfoTable,'hwSystemDiagInfoEntry':hwSystemDiagInfoEntry,_K:hwSystemDiagInfoIndex,'hwSystemDiagInfoFilename':hwSystemDiagInfoFilename,'hwSystemDiagInfoRowStatus':hwSystemDiagInfoRowStatus,'hwSystemDiagInfoOperEndTime':hwSystemDiagInfoOperEndTime,'hwSystemDiagInfoOperState':hwSystemDiagInfoOperState,'hwSystemDiagInfoOperFailReason':hwSystemDiagInfoOperFailReason,'hwSystemWorkingMode':hwSystemWorkingMode,'hwSystemWorkingModeTable':hwSystemWorkingModeTable,'hwSystemWorkingModeEntry':hwSystemWorkingModeEntry,_N:hwSystemWorkingModeIndex,'hwSystemWorkingModeName':hwSystemWorkingModeName,'hwSystemWorkingModeDescr':hwSystemWorkingModeDescr,'hwSystemWorkingModeDefault':hwSystemWorkingModeDefault,'hwSystemWorkingModeCurrent':hwSystemWorkingModeCurrent,'hwSystemWorkingModeNext':hwSystemWorkingModeNext})