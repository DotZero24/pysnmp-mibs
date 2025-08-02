_R='hh3cSysLoghostTrapVpnName'
_Q='hh3cSysLoghostIpaddress'
_P='hh3cSysLoghostIpaddressType'
_O='hh3cSysLoghostIndex'
_N='hh3cSystemWorkingModeIndex'
_M='read-create'
_L='not-accessible'
_K='hh3cSystemDiagInfoIndex'
_J='hh3cSysFirstTrapTime'
_I='OctetString'
_H='seconds'
_G='accessible-for-notify'
_F='DisplayString'
_E='HH3C-COMMON-SYSTEM-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hh3c,=mibBuilder.importSymbols('HH3C-OID-MIB','hh3c')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention','TimeStamp')
hh3cSystem=ModuleIdentity((1,3,6,1,4,1,25506,6))
if mibBuilder.loadTexts:hh3cSystem.setRevisions(('2015-05-05 00:00','2015-03-25 00:00','2014-08-07 17:10','2013-09-13 00:00','2013-05-28 00:00','2012-06-06 00:00','2012-01-07 00:00','2009-05-05 00:00','2008-11-11 00:00','2004-10-12 00:00','2004-08-16 00:00','2004-06-30 00:00'))
class _Hh3cWriteConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('save',1))
_Hh3cWriteConfig_Type.__name__=_B
_Hh3cWriteConfig_Object=MibScalar
hh3cWriteConfig=_Hh3cWriteConfig_Object((1,3,6,1,4,1,25506,6,5),_Hh3cWriteConfig_Type())
hh3cWriteConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cWriteConfig.setStatus(_A)
class _Hh3cStartFtpServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_Hh3cStartFtpServer_Type.__name__=_B
_Hh3cStartFtpServer_Object=MibScalar
hh3cStartFtpServer=_Hh3cStartFtpServer_Object((1,3,6,1,4,1,25506,6,6),_Hh3cStartFtpServer_Type())
hh3cStartFtpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cStartFtpServer.setStatus(_A)
class _Hh3cReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('reboot',1)))
_Hh3cReboot_Type.__name__=_B
_Hh3cReboot_Object=MibScalar
hh3cReboot=_Hh3cReboot_Object((1,3,6,1,4,1,25506,6,7),_Hh3cReboot_Type())
hh3cReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cReboot.setStatus(_A)
_Hh3cSystemNotification_ObjectIdentity=ObjectIdentity
hh3cSystemNotification=_Hh3cSystemNotification_ObjectIdentity((1,3,6,1,4,1,25506,6,8))
_Hh3cSoftwareVersion_Type=DisplayString
_Hh3cSoftwareVersion_Object=MibScalar
hh3cSoftwareVersion=_Hh3cSoftwareVersion_Object((1,3,6,1,4,1,25506,6,9),_Hh3cSoftwareVersion_Type())
hh3cSoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSoftwareVersion.setStatus(_A)
class _Hh3cSysBootType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('coldStart',1),('warmStart',2)))
_Hh3cSysBootType_Type.__name__=_B
_Hh3cSysBootType_Object=MibScalar
hh3cSysBootType=_Hh3cSysBootType_Object((1,3,6,1,4,1,25506,6,10),_Hh3cSysBootType_Type())
hh3cSysBootType.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSysBootType.setStatus(_A)
_Hh3cSystemInfo_ObjectIdentity=ObjectIdentity
hh3cSystemInfo=_Hh3cSystemInfo_ObjectIdentity((1,3,6,1,4,1,25506,6,11))
class _Hh3cSysStatisticPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_Hh3cSysStatisticPeriod_Type.__name__=_B
_Hh3cSysStatisticPeriod_Object=MibScalar
hh3cSysStatisticPeriod=_Hh3cSysStatisticPeriod_Object((1,3,6,1,4,1,25506,6,11,1),_Hh3cSysStatisticPeriod_Type())
hh3cSysStatisticPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cSysStatisticPeriod.setStatus(_A)
if mibBuilder.loadTexts:hh3cSysStatisticPeriod.setUnits(_H)
class _Hh3cSysSamplePeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_Hh3cSysSamplePeriod_Type.__name__=_B
_Hh3cSysSamplePeriod_Object=MibScalar
hh3cSysSamplePeriod=_Hh3cSysSamplePeriod_Object((1,3,6,1,4,1,25506,6,11,2),_Hh3cSysSamplePeriod_Type())
hh3cSysSamplePeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cSysSamplePeriod.setStatus(_A)
if mibBuilder.loadTexts:hh3cSysSamplePeriod.setUnits(_H)
class _Hh3cSysTrapResendPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_Hh3cSysTrapResendPeriod_Type.__name__=_B
_Hh3cSysTrapResendPeriod_Object=MibScalar
hh3cSysTrapResendPeriod=_Hh3cSysTrapResendPeriod_Object((1,3,6,1,4,1,25506,6,11,3),_Hh3cSysTrapResendPeriod_Type())
hh3cSysTrapResendPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cSysTrapResendPeriod.setStatus(_A)
if mibBuilder.loadTexts:hh3cSysTrapResendPeriod.setUnits(_H)
class _Hh3cSysTrapCollectionPeriod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_Hh3cSysTrapCollectionPeriod_Type.__name__=_B
_Hh3cSysTrapCollectionPeriod_Object=MibScalar
hh3cSysTrapCollectionPeriod=_Hh3cSysTrapCollectionPeriod_Object((1,3,6,1,4,1,25506,6,11,4),_Hh3cSysTrapCollectionPeriod_Type())
hh3cSysTrapCollectionPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cSysTrapCollectionPeriod.setStatus(_A)
if mibBuilder.loadTexts:hh3cSysTrapCollectionPeriod.setUnits(_H)
_Hh3cSysSnmpPort_Type=Integer32
_Hh3cSysSnmpPort_Object=MibScalar
hh3cSysSnmpPort=_Hh3cSysSnmpPort_Object((1,3,6,1,4,1,25506,6,11,5),_Hh3cSysSnmpPort_Type())
hh3cSysSnmpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSysSnmpPort.setStatus(_A)
_Hh3cSysSnmpTrapPort_Type=Integer32
_Hh3cSysSnmpTrapPort_Object=MibScalar
hh3cSysSnmpTrapPort=_Hh3cSysSnmpTrapPort_Object((1,3,6,1,4,1,25506,6,11,6),_Hh3cSysSnmpTrapPort_Type())
hh3cSysSnmpTrapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSysSnmpTrapPort.setStatus(_A)
class _Hh3cSysNetID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Hh3cSysNetID_Type.__name__=_I
_Hh3cSysNetID_Object=MibScalar
hh3cSysNetID=_Hh3cSysNetID_Object((1,3,6,1,4,1,25506,6,11,7),_Hh3cSysNetID_Type())
hh3cSysNetID.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cSysNetID.setStatus(_A)
_Hh3cSysLastSampleTime_Type=DateAndTime
_Hh3cSysLastSampleTime_Object=MibScalar
hh3cSysLastSampleTime=_Hh3cSysLastSampleTime_Object((1,3,6,1,4,1,25506,6,11,8),_Hh3cSysLastSampleTime_Type())
hh3cSysLastSampleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSysLastSampleTime.setStatus(_A)
class _Hh3cSysTrapSendNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_Hh3cSysTrapSendNum_Type.__name__=_B
_Hh3cSysTrapSendNum_Object=MibScalar
hh3cSysTrapSendNum=_Hh3cSysTrapSendNum_Object((1,3,6,1,4,1,25506,6,11,9),_Hh3cSysTrapSendNum_Type())
hh3cSysTrapSendNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cSysTrapSendNum.setStatus(_A)
_Hh3cSysFirstTrapTime_Type=TimeTicks
_Hh3cSysFirstTrapTime_Object=MibScalar
hh3cSysFirstTrapTime=_Hh3cSysFirstTrapTime_Object((1,3,6,1,4,1,25506,6,11,10),_Hh3cSysFirstTrapTime_Type())
hh3cSysFirstTrapTime.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSysFirstTrapTime.setStatus(_A)
class _Hh3cSysBannerMOTD_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2000))
_Hh3cSysBannerMOTD_Type.__name__=_I
_Hh3cSysBannerMOTD_Object=MibScalar
hh3cSysBannerMOTD=_Hh3cSysBannerMOTD_Object((1,3,6,1,4,1,25506,6,11,11),_Hh3cSysBannerMOTD_Type())
hh3cSysBannerMOTD.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cSysBannerMOTD.setStatus(_A)
_Hh3cSystemNotificationInfo_ObjectIdentity=ObjectIdentity
hh3cSystemNotificationInfo=_Hh3cSystemNotificationInfo_ObjectIdentity((1,3,6,1,4,1,25506,6,12))
_Hh3cSysLoghostIndex_Type=Integer32
_Hh3cSysLoghostIndex_Object=MibScalar
hh3cSysLoghostIndex=_Hh3cSysLoghostIndex_Object((1,3,6,1,4,1,25506,6,12,1),_Hh3cSysLoghostIndex_Type())
hh3cSysLoghostIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSysLoghostIndex.setStatus(_A)
_Hh3cSysLoghostIpaddressType_Type=InetAddressType
_Hh3cSysLoghostIpaddressType_Object=MibScalar
hh3cSysLoghostIpaddressType=_Hh3cSysLoghostIpaddressType_Object((1,3,6,1,4,1,25506,6,12,2),_Hh3cSysLoghostIpaddressType_Type())
hh3cSysLoghostIpaddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSysLoghostIpaddressType.setStatus(_A)
_Hh3cSysLoghostIpaddress_Type=InetAddress
_Hh3cSysLoghostIpaddress_Object=MibScalar
hh3cSysLoghostIpaddress=_Hh3cSysLoghostIpaddress_Object((1,3,6,1,4,1,25506,6,12,3),_Hh3cSysLoghostIpaddress_Type())
hh3cSysLoghostIpaddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSysLoghostIpaddress.setStatus(_A)
class _Hh3cSysLoghostTrapVpnName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_Hh3cSysLoghostTrapVpnName_Type.__name__=_F
_Hh3cSysLoghostTrapVpnName_Object=MibScalar
hh3cSysLoghostTrapVpnName=_Hh3cSysLoghostTrapVpnName_Object((1,3,6,1,4,1,25506,6,12,4),_Hh3cSysLoghostTrapVpnName_Type())
hh3cSysLoghostTrapVpnName.setMaxAccess(_G)
if mibBuilder.loadTexts:hh3cSysLoghostTrapVpnName.setStatus(_A)
_Hh3cSystemDiagInfoTable_Object=MibTable
hh3cSystemDiagInfoTable=_Hh3cSystemDiagInfoTable_Object((1,3,6,1,4,1,25506,6,13))
if mibBuilder.loadTexts:hh3cSystemDiagInfoTable.setStatus(_A)
_Hh3cSystemDiagInfoEntry_Object=MibTableRow
hh3cSystemDiagInfoEntry=_Hh3cSystemDiagInfoEntry_Object((1,3,6,1,4,1,25506,6,13,1))
hh3cSystemDiagInfoEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:hh3cSystemDiagInfoEntry.setStatus(_A)
class _Hh3cSystemDiagInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hh3cSystemDiagInfoIndex_Type.__name__=_B
_Hh3cSystemDiagInfoIndex_Object=MibTableColumn
hh3cSystemDiagInfoIndex=_Hh3cSystemDiagInfoIndex_Object((1,3,6,1,4,1,25506,6,13,1,1),_Hh3cSystemDiagInfoIndex_Type())
hh3cSystemDiagInfoIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hh3cSystemDiagInfoIndex.setStatus(_A)
class _Hh3cSystemDiagInfoFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hh3cSystemDiagInfoFilename_Type.__name__=_F
_Hh3cSystemDiagInfoFilename_Object=MibTableColumn
hh3cSystemDiagInfoFilename=_Hh3cSystemDiagInfoFilename_Object((1,3,6,1,4,1,25506,6,13,1,2),_Hh3cSystemDiagInfoFilename_Type())
hh3cSystemDiagInfoFilename.setMaxAccess(_M)
if mibBuilder.loadTexts:hh3cSystemDiagInfoFilename.setStatus(_A)
_Hh3cSystemDiagInfoRowStatus_Type=RowStatus
_Hh3cSystemDiagInfoRowStatus_Object=MibTableColumn
hh3cSystemDiagInfoRowStatus=_Hh3cSystemDiagInfoRowStatus_Object((1,3,6,1,4,1,25506,6,13,1,3),_Hh3cSystemDiagInfoRowStatus_Type())
hh3cSystemDiagInfoRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:hh3cSystemDiagInfoRowStatus.setStatus(_A)
_Hh3cSystemDiagInfoOperEndTime_Type=TimeStamp
_Hh3cSystemDiagInfoOperEndTime_Object=MibTableColumn
hh3cSystemDiagInfoOperEndTime=_Hh3cSystemDiagInfoOperEndTime_Object((1,3,6,1,4,1,25506,6,13,1,4),_Hh3cSystemDiagInfoOperEndTime_Type())
hh3cSystemDiagInfoOperEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSystemDiagInfoOperEndTime.setStatus(_A)
class _Hh3cSystemDiagInfoOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('opInProgress',1),('opSuccess',2),('opFailure',3)))
_Hh3cSystemDiagInfoOperState_Type.__name__=_B
_Hh3cSystemDiagInfoOperState_Object=MibTableColumn
hh3cSystemDiagInfoOperState=_Hh3cSystemDiagInfoOperState_Object((1,3,6,1,4,1,25506,6,13,1,5),_Hh3cSystemDiagInfoOperState_Type())
hh3cSystemDiagInfoOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSystemDiagInfoOperState.setStatus(_A)
class _Hh3cSystemDiagInfoOperFailReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Hh3cSystemDiagInfoOperFailReason_Type.__name__=_F
_Hh3cSystemDiagInfoOperFailReason_Object=MibTableColumn
hh3cSystemDiagInfoOperFailReason=_Hh3cSystemDiagInfoOperFailReason_Object((1,3,6,1,4,1,25506,6,13,1,6),_Hh3cSystemDiagInfoOperFailReason_Type())
hh3cSystemDiagInfoOperFailReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSystemDiagInfoOperFailReason.setStatus(_A)
_Hh3cSystemWorkingMode_ObjectIdentity=ObjectIdentity
hh3cSystemWorkingMode=_Hh3cSystemWorkingMode_ObjectIdentity((1,3,6,1,4,1,25506,6,14))
_Hh3cSystemWorkingModeTable_Object=MibTable
hh3cSystemWorkingModeTable=_Hh3cSystemWorkingModeTable_Object((1,3,6,1,4,1,25506,6,14,1))
if mibBuilder.loadTexts:hh3cSystemWorkingModeTable.setStatus(_A)
_Hh3cSystemWorkingModeEntry_Object=MibTableRow
hh3cSystemWorkingModeEntry=_Hh3cSystemWorkingModeEntry_Object((1,3,6,1,4,1,25506,6,14,1,1))
hh3cSystemWorkingModeEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:hh3cSystemWorkingModeEntry.setStatus(_A)
class _Hh3cSystemWorkingModeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hh3cSystemWorkingModeIndex_Type.__name__=_B
_Hh3cSystemWorkingModeIndex_Object=MibTableColumn
hh3cSystemWorkingModeIndex=_Hh3cSystemWorkingModeIndex_Object((1,3,6,1,4,1,25506,6,14,1,1,1),_Hh3cSystemWorkingModeIndex_Type())
hh3cSystemWorkingModeIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hh3cSystemWorkingModeIndex.setStatus(_A)
class _Hh3cSystemWorkingModeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Hh3cSystemWorkingModeName_Type.__name__=_F
_Hh3cSystemWorkingModeName_Object=MibTableColumn
hh3cSystemWorkingModeName=_Hh3cSystemWorkingModeName_Object((1,3,6,1,4,1,25506,6,14,1,1,2),_Hh3cSystemWorkingModeName_Type())
hh3cSystemWorkingModeName.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSystemWorkingModeName.setStatus(_A)
class _Hh3cSystemWorkingModeDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_Hh3cSystemWorkingModeDescr_Type.__name__=_F
_Hh3cSystemWorkingModeDescr_Object=MibTableColumn
hh3cSystemWorkingModeDescr=_Hh3cSystemWorkingModeDescr_Object((1,3,6,1,4,1,25506,6,14,1,1,3),_Hh3cSystemWorkingModeDescr_Type())
hh3cSystemWorkingModeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSystemWorkingModeDescr.setStatus(_A)
class _Hh3cSystemWorkingModeDefault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hh3cSystemWorkingModeDefault_Type.__name__=_B
_Hh3cSystemWorkingModeDefault_Object=MibScalar
hh3cSystemWorkingModeDefault=_Hh3cSystemWorkingModeDefault_Object((1,3,6,1,4,1,25506,6,14,2),_Hh3cSystemWorkingModeDefault_Type())
hh3cSystemWorkingModeDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSystemWorkingModeDefault.setStatus(_A)
class _Hh3cSystemWorkingModeCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hh3cSystemWorkingModeCurrent_Type.__name__=_B
_Hh3cSystemWorkingModeCurrent_Object=MibScalar
hh3cSystemWorkingModeCurrent=_Hh3cSystemWorkingModeCurrent_Object((1,3,6,1,4,1,25506,6,14,3),_Hh3cSystemWorkingModeCurrent_Type())
hh3cSystemWorkingModeCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:hh3cSystemWorkingModeCurrent.setStatus(_A)
class _Hh3cSystemWorkingModeNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Hh3cSystemWorkingModeNext_Type.__name__=_B
_Hh3cSystemWorkingModeNext_Object=MibScalar
hh3cSystemWorkingModeNext=_Hh3cSystemWorkingModeNext_Object((1,3,6,1,4,1,25506,6,14,4),_Hh3cSystemWorkingModeNext_Type())
hh3cSystemWorkingModeNext.setMaxAccess(_D)
if mibBuilder.loadTexts:hh3cSystemWorkingModeNext.setStatus(_A)
hh3cWriteSuccessTrap=NotificationType((1,3,6,1,4,1,25506,6,8,1))
if mibBuilder.loadTexts:hh3cWriteSuccessTrap.setStatus(_A)
hh3cWriteFailureTrap=NotificationType((1,3,6,1,4,1,25506,6,8,2))
if mibBuilder.loadTexts:hh3cWriteFailureTrap.setStatus(_A)
hh3cRebootSendTrap=NotificationType((1,3,6,1,4,1,25506,6,8,3))
if mibBuilder.loadTexts:hh3cRebootSendTrap.setStatus(_A)
hh3cSysColdStartTrap=NotificationType((1,3,6,1,4,1,25506,6,8,4))
hh3cSysColdStartTrap.setObjects((_E,_J))
if mibBuilder.loadTexts:hh3cSysColdStartTrap.setStatus(_A)
hh3cSysWarmStartTrap=NotificationType((1,3,6,1,4,1,25506,6,8,5))
hh3cSysWarmStartTrap.setObjects((_E,_J))
if mibBuilder.loadTexts:hh3cSysWarmStartTrap.setStatus(_A)
hh3cSysLoghostUnreachableTrap=NotificationType((1,3,6,1,4,1,25506,6,8,6))
hh3cSysLoghostUnreachableTrap.setObjects(*((_E,_O),(_E,_P),(_E,_Q),(_E,_R)))
if mibBuilder.loadTexts:hh3cSysLoghostUnreachableTrap.setStatus(_A)
hh3cSysDyingGaspTrap=NotificationType((1,3,6,1,4,1,25506,6,8,7))
if mibBuilder.loadTexts:hh3cSysDyingGaspTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hh3cSystem':hh3cSystem,'hh3cWriteConfig':hh3cWriteConfig,'hh3cStartFtpServer':hh3cStartFtpServer,'hh3cReboot':hh3cReboot,'hh3cSystemNotification':hh3cSystemNotification,'hh3cWriteSuccessTrap':hh3cWriteSuccessTrap,'hh3cWriteFailureTrap':hh3cWriteFailureTrap,'hh3cRebootSendTrap':hh3cRebootSendTrap,'hh3cSysColdStartTrap':hh3cSysColdStartTrap,'hh3cSysWarmStartTrap':hh3cSysWarmStartTrap,'hh3cSysLoghostUnreachableTrap':hh3cSysLoghostUnreachableTrap,'hh3cSysDyingGaspTrap':hh3cSysDyingGaspTrap,'hh3cSoftwareVersion':hh3cSoftwareVersion,'hh3cSysBootType':hh3cSysBootType,'hh3cSystemInfo':hh3cSystemInfo,'hh3cSysStatisticPeriod':hh3cSysStatisticPeriod,'hh3cSysSamplePeriod':hh3cSysSamplePeriod,'hh3cSysTrapResendPeriod':hh3cSysTrapResendPeriod,'hh3cSysTrapCollectionPeriod':hh3cSysTrapCollectionPeriod,'hh3cSysSnmpPort':hh3cSysSnmpPort,'hh3cSysSnmpTrapPort':hh3cSysSnmpTrapPort,'hh3cSysNetID':hh3cSysNetID,'hh3cSysLastSampleTime':hh3cSysLastSampleTime,'hh3cSysTrapSendNum':hh3cSysTrapSendNum,_J:hh3cSysFirstTrapTime,'hh3cSysBannerMOTD':hh3cSysBannerMOTD,'hh3cSystemNotificationInfo':hh3cSystemNotificationInfo,_O:hh3cSysLoghostIndex,_P:hh3cSysLoghostIpaddressType,_Q:hh3cSysLoghostIpaddress,_R:hh3cSysLoghostTrapVpnName,'hh3cSystemDiagInfoTable':hh3cSystemDiagInfoTable,'hh3cSystemDiagInfoEntry':hh3cSystemDiagInfoEntry,_K:hh3cSystemDiagInfoIndex,'hh3cSystemDiagInfoFilename':hh3cSystemDiagInfoFilename,'hh3cSystemDiagInfoRowStatus':hh3cSystemDiagInfoRowStatus,'hh3cSystemDiagInfoOperEndTime':hh3cSystemDiagInfoOperEndTime,'hh3cSystemDiagInfoOperState':hh3cSystemDiagInfoOperState,'hh3cSystemDiagInfoOperFailReason':hh3cSystemDiagInfoOperFailReason,'hh3cSystemWorkingMode':hh3cSystemWorkingMode,'hh3cSystemWorkingModeTable':hh3cSystemWorkingModeTable,'hh3cSystemWorkingModeEntry':hh3cSystemWorkingModeEntry,_N:hh3cSystemWorkingModeIndex,'hh3cSystemWorkingModeName':hh3cSystemWorkingModeName,'hh3cSystemWorkingModeDescr':hh3cSystemWorkingModeDescr,'hh3cSystemWorkingModeDefault':hh3cSystemWorkingModeDefault,'hh3cSystemWorkingModeCurrent':hh3cSystemWorkingModeCurrent,'hh3cSystemWorkingModeNext':hh3cSystemWorkingModeNext})