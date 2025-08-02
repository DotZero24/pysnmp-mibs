_N='eventLogIndex'
_M='snmpIpTrapRcvrIpAddress'
_L='segBusIndex'
_K='read-create'
_J='not-accessible'
_I='SWITCH-CHASSIS-MIB'
_H='deprecated'
_G='obsolete'
_F='OctetString'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp')
switchChassis,=mibBuilder.importSymbols('TELESYN-ATI-TC','switchChassis')
switchChassisMib=ModuleIdentity((1,3,6,1,4,1,207,8,9,1,1))
if mibBuilder.loadTexts:switchChassisMib.setRevisions(('1997-04-29 20:00','1997-01-14 20:00','1996-12-19 22:00'))
class HostNameOrIpAddr(DisplayString):status=_A
class HwIdentifier(TextualConvention,OctetString):status=_A;displayHint='2d.2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class SwVersionId(TextualConvention,OctetString):status=_A;displayHint='2d.2d.2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_ChassisParams_ObjectIdentity=ObjectIdentity
chassisParams=_ChassisParams_ObjectIdentity((1,3,6,1,4,1,207,8,9,1,1,1))
class _ChassisSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ChassisSerialNumber_Type.__name__=_E
_ChassisSerialNumber_Object=MibScalar
chassisSerialNumber=_ChassisSerialNumber_Object((1,3,6,1,4,1,207,8,9,1,1,1,1),_ChassisSerialNumber_Type())
chassisSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSerialNumber.setStatus(_A)
_ChassisHwId_Type=HwIdentifier
_ChassisHwId_Object=MibScalar
chassisHwId=_ChassisHwId_Object((1,3,6,1,4,1,207,8,9,1,1,1,2),_ChassisHwId_Type())
chassisHwId.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisHwId.setStatus(_A)
class _ChassisOSVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ChassisOSVersion_Type.__name__=_E
_ChassisOSVersion_Object=MibScalar
chassisOSVersion=_ChassisOSVersion_Object((1,3,6,1,4,1,207,8,9,1,1,1,3),_ChassisOSVersion_Type())
chassisOSVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisOSVersion.setStatus(_A)
class _ChassisFwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ChassisFwVersion_Type.__name__=_E
_ChassisFwVersion_Object=MibScalar
chassisFwVersion=_ChassisFwVersion_Object((1,3,6,1,4,1,207,8,9,1,1,1,4),_ChassisFwVersion_Type())
chassisFwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisFwVersion.setStatus(_A)
_ChassisLastChanges_Type=Counter32
_ChassisLastChanges_Object=MibScalar
chassisLastChanges=_ChassisLastChanges_Object((1,3,6,1,4,1,207,8,9,1,1,1,5),_ChassisLastChanges_Type())
chassisLastChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisLastChanges.setStatus(_A)
_ChassisBaseMacAddress_Type=MacAddress
_ChassisBaseMacAddress_Object=MibScalar
chassisBaseMacAddress=_ChassisBaseMacAddress_Object((1,3,6,1,4,1,207,8,9,1,1,1,6),_ChassisBaseMacAddress_Type())
chassisBaseMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisBaseMacAddress.setStatus(_A)
class _ChassisFanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('slowOrStopped',2)))
_ChassisFanStatus_Type.__name__=_D
_ChassisFanStatus_Object=MibScalar
chassisFanStatus=_ChassisFanStatus_Object((1,3,6,1,4,1,207,8,9,1,1,1,7),_ChassisFanStatus_Type())
chassisFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisFanStatus.setStatus(_A)
class _ChassisBoardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ChassisBoardSerialNumber_Type.__name__=_E
_ChassisBoardSerialNumber_Object=MibScalar
chassisBoardSerialNumber=_ChassisBoardSerialNumber_Object((1,3,6,1,4,1,207,8,9,1,1,1,8),_ChassisBoardSerialNumber_Type())
chassisBoardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisBoardSerialNumber.setStatus(_A)
_IpParams_ObjectIdentity=ObjectIdentity
ipParams=_IpParams_ObjectIdentity((1,3,6,1,4,1,207,8,9,1,1,3))
_IpAddr_Type=IpAddress
_IpAddr_Object=MibScalar
ipAddr=_IpAddr_Object((1,3,6,1,4,1,207,8,9,1,1,3,1),_IpAddr_Type())
ipAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ipAddr.setStatus(_G)
_IpNetMask_Type=IpAddress
_IpNetMask_Object=MibScalar
ipNetMask=_IpNetMask_Object((1,3,6,1,4,1,207,8,9,1,1,3,2),_IpNetMask_Type())
ipNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipNetMask.setStatus(_G)
class _IpBcastForm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allOnes',1),('allZeros',2)))
_IpBcastForm_Type.__name__=_D
_IpBcastForm_Object=MibScalar
ipBcastForm=_IpBcastForm_Object((1,3,6,1,4,1,207,8,9,1,1,3,3),_IpBcastForm_Type())
ipBcastForm.setMaxAccess(_C)
if mibBuilder.loadTexts:ipBcastForm.setStatus(_G)
class _IpEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ethernet',1),('ieee8022',2)))
_IpEncap_Type.__name__=_D
_IpEncap_Object=MibScalar
ipEncap=_IpEncap_Object((1,3,6,1,4,1,207,8,9,1,1,3,4),_IpEncap_Type())
ipEncap.setMaxAccess(_C)
if mibBuilder.loadTexts:ipEncap.setStatus(_G)
_IpDefaultGateway_Type=IpAddress
_IpDefaultGateway_Object=MibScalar
ipDefaultGateway=_IpDefaultGateway_Object((1,3,6,1,4,1,207,8,9,1,1,3,5),_IpDefaultGateway_Type())
ipDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:ipDefaultGateway.setStatus(_G)
class _IpDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_IpDomainName_Type.__name__=_E
_IpDomainName_Object=MibScalar
ipDomainName=_IpDomainName_Object((1,3,6,1,4,1,207,8,9,1,1,3,6),_IpDomainName_Type())
ipDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:ipDomainName.setStatus(_G)
_SysConfigParams_ObjectIdentity=ObjectIdentity
sysConfigParams=_SysConfigParams_ObjectIdentity((1,3,6,1,4,1,207,8,9,1,1,4))
class _BootFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8,16,32,48,64,128,192)));namedValues=NamedValues(*(('bootSystem',0),('skipPost',1),('runMonitor',2),('useBackupBoot',4),('loopPost',8),('bootLoader',16),('bootNetwork',32),('bootDiag',48),('networkEth0',64),('networkEth1',128),('networkCom0',192)))
_BootFlag_Type.__name__=_D
_BootFlag_Object=MibScalar
bootFlag=_BootFlag_Object((1,3,6,1,4,1,207,8,9,1,1,4,1),_BootFlag_Type())
bootFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:bootFlag.setStatus(_H)
_DramSize_Type=Unsigned32
_DramSize_Object=MibScalar
dramSize=_DramSize_Object((1,3,6,1,4,1,207,8,9,1,1,4,2),_DramSize_Type())
dramSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dramSize.setStatus(_A)
_CpuVer_Type=HwIdentifier
_CpuVer_Object=MibScalar
cpuVer=_CpuVer_Object((1,3,6,1,4,1,207,8,9,1,1,4,3),_CpuVer_Type())
cpuVer.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuVer.setStatus(_A)
_IscVer_Type=HwIdentifier
_IscVer_Object=MibScalar
iscVer=_IscVer_Object((1,3,6,1,4,1,207,8,9,1,1,4,4),_IscVer_Type())
iscVer.setMaxAccess(_B)
if mibBuilder.loadTexts:iscVer.setStatus(_A)
_PigVer_Type=HwIdentifier
_PigVer_Object=MibScalar
pigVer=_PigVer_Object((1,3,6,1,4,1,207,8,9,1,1,4,5),_PigVer_Type())
pigVer.setMaxAccess(_B)
if mibBuilder.loadTexts:pigVer.setStatus(_A)
_PostVer_Type=SwVersionId
_PostVer_Object=MibScalar
postVer=_PostVer_Object((1,3,6,1,4,1,207,8,9,1,1,4,6),_PostVer_Type())
postVer.setMaxAccess(_B)
if mibBuilder.loadTexts:postVer.setStatus(_A)
_IsdVer_Type=SwVersionId
_IsdVer_Object=MibScalar
isdVer=_IsdVer_Object((1,3,6,1,4,1,207,8,9,1,1,4,7),_IsdVer_Type())
isdVer.setMaxAccess(_B)
if mibBuilder.loadTexts:isdVer.setStatus(_A)
_BootVer_Type=SwVersionId
_BootVer_Object=MibScalar
bootVer=_BootVer_Object((1,3,6,1,4,1,207,8,9,1,1,4,8),_BootVer_Type())
bootVer.setMaxAccess(_B)
if mibBuilder.loadTexts:bootVer.setStatus(_A)
_QmuMemSize_Type=Unsigned32
_QmuMemSize_Object=MibScalar
qmuMemSize=_QmuMemSize_Object((1,3,6,1,4,1,207,8,9,1,1,4,9),_QmuMemSize_Type())
qmuMemSize.setMaxAccess(_B)
if mibBuilder.loadTexts:qmuMemSize.setStatus(_A)
_SegBusTable_Object=MibTable
segBusTable=_SegBusTable_Object((1,3,6,1,4,1,207,8,9,1,1,4,10))
if mibBuilder.loadTexts:segBusTable.setStatus(_A)
_SegBusEntry_Object=MibTableRow
segBusEntry=_SegBusEntry_Object((1,3,6,1,4,1,207,8,9,1,1,4,10,1))
segBusEntry.setIndexNames((0,_I,_L))
if mibBuilder.loadTexts:segBusEntry.setStatus(_A)
class _SegBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_SegBusIndex_Type.__name__=_D
_SegBusIndex_Object=MibTableColumn
segBusIndex=_SegBusIndex_Object((1,3,6,1,4,1,207,8,9,1,1,4,10,1,1),_SegBusIndex_Type())
segBusIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:segBusIndex.setStatus(_A)
_SegBusPmiuId_Type=HwIdentifier
_SegBusPmiuId_Object=MibTableColumn
segBusPmiuId=_SegBusPmiuId_Object((1,3,6,1,4,1,207,8,9,1,1,4,10,1,2),_SegBusPmiuId_Type())
segBusPmiuId.setMaxAccess(_B)
if mibBuilder.loadTexts:segBusPmiuId.setStatus(_A)
_SegBusQmuId_Type=HwIdentifier
_SegBusQmuId_Object=MibTableColumn
segBusQmuId=_SegBusQmuId_Object((1,3,6,1,4,1,207,8,9,1,1,4,10,1,3),_SegBusQmuId_Type())
segBusQmuId.setMaxAccess(_B)
if mibBuilder.loadTexts:segBusQmuId.setStatus(_A)
_SnmpParams_ObjectIdentity=ObjectIdentity
snmpParams=_SnmpParams_ObjectIdentity((1,3,6,1,4,1,207,8,9,1,1,6))
_SnmpIpTrapRcvrTable_Object=MibTable
snmpIpTrapRcvrTable=_SnmpIpTrapRcvrTable_Object((1,3,6,1,4,1,207,8,9,1,1,6,1))
if mibBuilder.loadTexts:snmpIpTrapRcvrTable.setStatus(_A)
_SnmpIpTrapRcvrEntry_Object=MibTableRow
snmpIpTrapRcvrEntry=_SnmpIpTrapRcvrEntry_Object((1,3,6,1,4,1,207,8,9,1,1,6,1,1))
snmpIpTrapRcvrEntry.setIndexNames((0,_I,_M))
if mibBuilder.loadTexts:snmpIpTrapRcvrEntry.setStatus(_A)
_SnmpIpTrapRcvrIpAddress_Type=IpAddress
_SnmpIpTrapRcvrIpAddress_Object=MibTableColumn
snmpIpTrapRcvrIpAddress=_SnmpIpTrapRcvrIpAddress_Object((1,3,6,1,4,1,207,8,9,1,1,6,1,1,1),_SnmpIpTrapRcvrIpAddress_Type())
snmpIpTrapRcvrIpAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:snmpIpTrapRcvrIpAddress.setStatus(_A)
class _SnmpIpTrapRcvrPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnmpIpTrapRcvrPort_Type.__name__=_D
_SnmpIpTrapRcvrPort_Object=MibTableColumn
snmpIpTrapRcvrPort=_SnmpIpTrapRcvrPort_Object((1,3,6,1,4,1,207,8,9,1,1,6,1,1,2),_SnmpIpTrapRcvrPort_Type())
snmpIpTrapRcvrPort.setMaxAccess(_K)
if mibBuilder.loadTexts:snmpIpTrapRcvrPort.setStatus(_A)
class _SnmpIpTrapRcvrCommunity_Type(DisplayString):defaultValue=OctetString('public');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SnmpIpTrapRcvrCommunity_Type.__name__=_E
_SnmpIpTrapRcvrCommunity_Object=MibTableColumn
snmpIpTrapRcvrCommunity=_SnmpIpTrapRcvrCommunity_Object((1,3,6,1,4,1,207,8,9,1,1,6,1,1,3),_SnmpIpTrapRcvrCommunity_Type())
snmpIpTrapRcvrCommunity.setMaxAccess(_K)
if mibBuilder.loadTexts:snmpIpTrapRcvrCommunity.setStatus(_A)
_SnmpIpTrapRcvrStatus_Type=RowStatus
_SnmpIpTrapRcvrStatus_Object=MibTableColumn
snmpIpTrapRcvrStatus=_SnmpIpTrapRcvrStatus_Object((1,3,6,1,4,1,207,8,9,1,1,6,1,1,4),_SnmpIpTrapRcvrStatus_Type())
snmpIpTrapRcvrStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:snmpIpTrapRcvrStatus.setStatus(_A)
_SnmpUnAuthIpAddr_Type=IpAddress
_SnmpUnAuthIpAddr_Object=MibScalar
snmpUnAuthIpAddr=_SnmpUnAuthIpAddr_Object((1,3,6,1,4,1,207,8,9,1,1,6,2),_SnmpUnAuthIpAddr_Type())
snmpUnAuthIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpUnAuthIpAddr.setStatus(_A)
class _SnmpUnAuthCommunity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SnmpUnAuthCommunity_Type.__name__=_F
_SnmpUnAuthCommunity_Object=MibScalar
snmpUnAuthCommunity=_SnmpUnAuthCommunity_Object((1,3,6,1,4,1,207,8,9,1,1,6,3),_SnmpUnAuthCommunity_Type())
snmpUnAuthCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpUnAuthCommunity.setStatus(_A)
_ConsoleParams_ObjectIdentity=ObjectIdentity
consoleParams=_ConsoleParams_ObjectIdentity((1,3,6,1,4,1,207,8,9,1,1,7))
_ConsolePortSpeed_Type=Unsigned32
_ConsolePortSpeed_Object=MibScalar
consolePortSpeed=_ConsolePortSpeed_Object((1,3,6,1,4,1,207,8,9,1,1,7,1),_ConsolePortSpeed_Type())
consolePortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:consolePortSpeed.setStatus(_H)
class _ConsolePortDataBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(7,8))
_ConsolePortDataBits_Type.__name__=_D
_ConsolePortDataBits_Object=MibScalar
consolePortDataBits=_ConsolePortDataBits_Object((1,3,6,1,4,1,207,8,9,1,1,7,2),_ConsolePortDataBits_Type())
consolePortDataBits.setMaxAccess(_C)
if mibBuilder.loadTexts:consolePortDataBits.setStatus(_H)
class _ConsolePortStopBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('one',1),('two',2),('onePointFive',3)))
_ConsolePortStopBits_Type.__name__=_D
_ConsolePortStopBits_Object=MibScalar
consolePortStopBits=_ConsolePortStopBits_Object((1,3,6,1,4,1,207,8,9,1,1,7,3),_ConsolePortStopBits_Type())
consolePortStopBits.setMaxAccess(_C)
if mibBuilder.loadTexts:consolePortStopBits.setStatus(_H)
class _ConsolePortParity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('odd',2),('even',3),('mark',4),('space',5)))
_ConsolePortParity_Type.__name__=_D
_ConsolePortParity_Object=MibScalar
consolePortParity=_ConsolePortParity_Object((1,3,6,1,4,1,207,8,9,1,1,7,4),_ConsolePortParity_Type())
consolePortParity.setMaxAccess(_C)
if mibBuilder.loadTexts:consolePortParity.setStatus(_H)
_LogParams_ObjectIdentity=ObjectIdentity
logParams=_LogParams_ObjectIdentity((1,3,6,1,4,1,207,8,9,1,1,8))
class _EventLogEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_EventLogEnable_Type.__name__=_D
_EventLogEnable_Object=MibScalar
eventLogEnable=_EventLogEnable_Object((1,3,6,1,4,1,207,8,9,1,1,8,1),_EventLogEnable_Type())
eventLogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eventLogEnable.setStatus(_A)
_EventLogSize_Type=Unsigned32
_EventLogSize_Object=MibScalar
eventLogSize=_EventLogSize_Object((1,3,6,1,4,1,207,8,9,1,1,8,2),_EventLogSize_Type())
eventLogSize.setMaxAccess(_B)
if mibBuilder.loadTexts:eventLogSize.setStatus(_A)
_EventLogCount_Type=Unsigned32
_EventLogCount_Object=MibScalar
eventLogCount=_EventLogCount_Object((1,3,6,1,4,1,207,8,9,1,1,8,3),_EventLogCount_Type())
eventLogCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eventLogCount.setStatus(_A)
_EventLogTable_Object=MibTable
eventLogTable=_EventLogTable_Object((1,3,6,1,4,1,207,8,9,1,1,8,4))
if mibBuilder.loadTexts:eventLogTable.setStatus(_A)
_EventLogEntry_Object=MibTableRow
eventLogEntry=_EventLogEntry_Object((1,3,6,1,4,1,207,8,9,1,1,8,4,1))
eventLogEntry.setIndexNames((0,_I,_N))
if mibBuilder.loadTexts:eventLogEntry.setStatus(_A)
class _EventLogIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EventLogIndex_Type.__name__=_D
_EventLogIndex_Object=MibTableColumn
eventLogIndex=_EventLogIndex_Object((1,3,6,1,4,1,207,8,9,1,1,8,4,1,1),_EventLogIndex_Type())
eventLogIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:eventLogIndex.setStatus(_A)
_EventLogTime_Type=DisplayString
_EventLogTime_Object=MibTableColumn
eventLogTime=_EventLogTime_Object((1,3,6,1,4,1,207,8,9,1,1,8,4,1,2),_EventLogTime_Type())
eventLogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eventLogTime.setStatus(_A)
_EventLogDescr_Type=DisplayString
_EventLogDescr_Object=MibTableColumn
eventLogDescr=_EventLogDescr_Object((1,3,6,1,4,1,207,8,9,1,1,8,4,1,3),_EventLogDescr_Type())
eventLogDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:eventLogDescr.setStatus(_A)
_EventLogDetail_Type=DisplayString
_EventLogDetail_Object=MibTableColumn
eventLogDetail=_EventLogDetail_Object((1,3,6,1,4,1,207,8,9,1,1,8,4,1,4),_EventLogDetail_Type())
eventLogDetail.setMaxAccess(_B)
if mibBuilder.loadTexts:eventLogDetail.setStatus(_A)
class _EventLogRawEntry_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EventLogRawEntry_Type.__name__=_F
_EventLogRawEntry_Object=MibTableColumn
eventLogRawEntry=_EventLogRawEntry_Object((1,3,6,1,4,1,207,8,9,1,1,8,4,1,5),_EventLogRawEntry_Type())
eventLogRawEntry.setMaxAccess(_B)
if mibBuilder.loadTexts:eventLogRawEntry.setStatus(_A)
_BootParams_ObjectIdentity=ObjectIdentity
bootParams=_BootParams_ObjectIdentity((1,3,6,1,4,1,207,8,9,1,1,9))
class _DeviceReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('reset',2)))
_DeviceReset_Type.__name__=_D
_DeviceReset_Object=MibScalar
deviceReset=_DeviceReset_Object((1,3,6,1,4,1,207,8,9,1,1,9,1),_DeviceReset_Type())
deviceReset.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceReset.setStatus(_A)
_TftpGroup_ObjectIdentity=ObjectIdentity
tftpGroup=_TftpGroup_ObjectIdentity((1,3,6,1,4,1,207,8,9,1,1,9,4))
_TftpServerName_Type=HostNameOrIpAddr
_TftpServerName_Object=MibScalar
tftpServerName=_TftpServerName_Object((1,3,6,1,4,1,207,8,9,1,1,9,4,1),_TftpServerName_Type())
tftpServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpServerName.setStatus(_A)
class _TftpUserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_TftpUserName_Type.__name__=_F
_TftpUserName_Object=MibScalar
tftpUserName=_TftpUserName_Object((1,3,6,1,4,1,207,8,9,1,1,9,4,2),_TftpUserName_Type())
tftpUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpUserName.setStatus(_A)
class _TftpRemoteFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_TftpRemoteFileName_Type.__name__=_F
_TftpRemoteFileName_Object=MibScalar
tftpRemoteFileName=_TftpRemoteFileName_Object((1,3,6,1,4,1,207,8,9,1,1,9,4,3),_TftpRemoteFileName_Type())
tftpRemoteFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpRemoteFileName.setStatus(_A)
class _TftpLocalFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_TftpLocalFileName_Type.__name__=_F
_TftpLocalFileName_Object=MibScalar
tftpLocalFileName=_TftpLocalFileName_Object((1,3,6,1,4,1,207,8,9,1,1,9,4,4),_TftpLocalFileName_Type())
tftpLocalFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpLocalFileName.setStatus(_A)
class _TftpOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('putFile',1),('getFile',2),('getFirmware',3)))
_TftpOperation_Type.__name__=_D
_TftpOperation_Object=MibScalar
tftpOperation=_TftpOperation_Object((1,3,6,1,4,1,207,8,9,1,1,9,4,5),_TftpOperation_Type())
tftpOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpOperation.setStatus(_A)
class _TftpAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configure',1),('execute',2)))
_TftpAdminState_Type.__name__=_D
_TftpAdminState_Object=MibScalar
tftpAdminState=_TftpAdminState_Object((1,3,6,1,4,1,207,8,9,1,1,9,4,6),_TftpAdminState_Type())
tftpAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tftpAdminState.setStatus(_A)
class _TftpOperationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('inactive',1),('executing',2),('succeeded',3),('localFileProblem',4),('unknownHost',5),('timedOut',6),('remoteFileProblem',7),('otherFailure',8)))
_TftpOperationState_Type.__name__=_D
_TftpOperationState_Object=MibScalar
tftpOperationState=_TftpOperationState_Object((1,3,6,1,4,1,207,8,9,1,1,9,4,7),_TftpOperationState_Type())
tftpOperationState.setMaxAccess(_B)
if mibBuilder.loadTexts:tftpOperationState.setStatus(_A)
_TftpOperationStateChange_Type=TimeStamp
_TftpOperationStateChange_Object=MibScalar
tftpOperationStateChange=_TftpOperationStateChange_Object((1,3,6,1,4,1,207,8,9,1,1,9,4,8),_TftpOperationStateChange_Type())
tftpOperationStateChange.setMaxAccess(_B)
if mibBuilder.loadTexts:tftpOperationStateChange.setStatus(_A)
class _TftpErrorMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TftpErrorMessage_Type.__name__=_E
_TftpErrorMessage_Object=MibScalar
tftpErrorMessage=_TftpErrorMessage_Object((1,3,6,1,4,1,207,8,9,1,1,9,4,9),_TftpErrorMessage_Type())
tftpErrorMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:tftpErrorMessage.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'HostNameOrIpAddr':HostNameOrIpAddr,'HwIdentifier':HwIdentifier,'SwVersionId':SwVersionId,'switchChassisMib':switchChassisMib,'chassisParams':chassisParams,'chassisSerialNumber':chassisSerialNumber,'chassisHwId':chassisHwId,'chassisOSVersion':chassisOSVersion,'chassisFwVersion':chassisFwVersion,'chassisLastChanges':chassisLastChanges,'chassisBaseMacAddress':chassisBaseMacAddress,'chassisFanStatus':chassisFanStatus,'chassisBoardSerialNumber':chassisBoardSerialNumber,'ipParams':ipParams,'ipAddr':ipAddr,'ipNetMask':ipNetMask,'ipBcastForm':ipBcastForm,'ipEncap':ipEncap,'ipDefaultGateway':ipDefaultGateway,'ipDomainName':ipDomainName,'sysConfigParams':sysConfigParams,'bootFlag':bootFlag,'dramSize':dramSize,'cpuVer':cpuVer,'iscVer':iscVer,'pigVer':pigVer,'postVer':postVer,'isdVer':isdVer,'bootVer':bootVer,'qmuMemSize':qmuMemSize,'segBusTable':segBusTable,'segBusEntry':segBusEntry,_L:segBusIndex,'segBusPmiuId':segBusPmiuId,'segBusQmuId':segBusQmuId,'snmpParams':snmpParams,'snmpIpTrapRcvrTable':snmpIpTrapRcvrTable,'snmpIpTrapRcvrEntry':snmpIpTrapRcvrEntry,_M:snmpIpTrapRcvrIpAddress,'snmpIpTrapRcvrPort':snmpIpTrapRcvrPort,'snmpIpTrapRcvrCommunity':snmpIpTrapRcvrCommunity,'snmpIpTrapRcvrStatus':snmpIpTrapRcvrStatus,'snmpUnAuthIpAddr':snmpUnAuthIpAddr,'snmpUnAuthCommunity':snmpUnAuthCommunity,'consoleParams':consoleParams,'consolePortSpeed':consolePortSpeed,'consolePortDataBits':consolePortDataBits,'consolePortStopBits':consolePortStopBits,'consolePortParity':consolePortParity,'logParams':logParams,'eventLogEnable':eventLogEnable,'eventLogSize':eventLogSize,'eventLogCount':eventLogCount,'eventLogTable':eventLogTable,'eventLogEntry':eventLogEntry,_N:eventLogIndex,'eventLogTime':eventLogTime,'eventLogDescr':eventLogDescr,'eventLogDetail':eventLogDetail,'eventLogRawEntry':eventLogRawEntry,'bootParams':bootParams,'deviceReset':deviceReset,'tftpGroup':tftpGroup,'tftpServerName':tftpServerName,'tftpUserName':tftpUserName,'tftpRemoteFileName':tftpRemoteFileName,'tftpLocalFileName':tftpLocalFileName,'tftpOperation':tftpOperation,'tftpAdminState':tftpAdminState,'tftpOperationState':tftpOperationState,'tftpOperationStateChange':tftpOperationStateChange,'tftpErrorMessage':tftpErrorMessage})