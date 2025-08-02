_X='slmSysLocation'
_W='slmSysName'
_V='slmSwRevStatus'
_U='slmLicenseIndex'
_T='slmChPassOldPass'
_S='slmChPassLogin'
_R='slmSyslogDestAddress'
_Q='slmTrapLogId'
_P='slmTrapDestAddress'
_O='slmAuthPassword'
_N='slmAuthLogin'
_M='noaccess'
_L='slmAdminLogin'
_K='testing'
_J='slmSwRevDirectory'
_I='DisplayString'
_H='not-accessible'
_G='OctetString'
_F='SL-MAIN-MIB'
_E='read-create'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
sitelight,=mibBuilder.importSymbols('SL-NE-MIB','sitelight')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
slMain=ModuleIdentity((1,3,6,1,4,1,4515,1,3))
class UserLogin(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
class UserPassword(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
class UserCommunity(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
class SoftwareRevision(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
class AdminAccess(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('none',0),('read',1),('readwrite',2),('provisioning',3),('admin',4),('trap',5)))
_SlmSys_ObjectIdentity=ObjectIdentity
slmSys=_SlmSys_ObjectIdentity((1,3,6,1,4,1,4515,1,3,1))
_SlmSysGatewayAddr_Type=IpAddress
_SlmSysGatewayAddr_Object=MibScalar
slmSysGatewayAddr=_SlmSysGatewayAddr_Object((1,3,6,1,4,1,4515,1,3,1,1),_SlmSysGatewayAddr_Type())
slmSysGatewayAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysGatewayAddr.setStatus(_A)
_SlmSysSubnetMask_Type=IpAddress
_SlmSysSubnetMask_Object=MibScalar
slmSysSubnetMask=_SlmSysSubnetMask_Object((1,3,6,1,4,1,4515,1,3,1,2),_SlmSysSubnetMask_Type())
slmSysSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysSubnetMask.setStatus(_A)
_SlmSysIpAddr_Type=IpAddress
_SlmSysIpAddr_Object=MibScalar
slmSysIpAddr=_SlmSysIpAddr_Object((1,3,6,1,4,1,4515,1,3,1,3),_SlmSysIpAddr_Type())
slmSysIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysIpAddr.setStatus(_A)
class _SlmSysAlmAct_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlmSysAlmAct_Type.__name__=_D
_SlmSysAlmAct_Object=MibScalar
slmSysAlmAct=_SlmSysAlmAct_Object((1,3,6,1,4,1,4515,1,3,1,4),_SlmSysAlmAct_Type())
slmSysAlmAct.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysAlmAct.setStatus(_A)
class _SlmSysAlmDeact_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_SlmSysAlmDeact_Type.__name__=_D
_SlmSysAlmDeact_Object=MibScalar
slmSysAlmDeact=_SlmSysAlmDeact_Object((1,3,6,1,4,1,4515,1,3,1,5),_SlmSysAlmDeact_Type())
slmSysAlmDeact.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysAlmDeact.setStatus(_A)
class _SlmSysAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('warmBoot',3),('coldBoot',4),('factoryBoot',5),(_K,6),('hotBoot',7)))
_SlmSysAdminStatus_Type.__name__=_D
_SlmSysAdminStatus_Object=MibScalar
slmSysAdminStatus=_SlmSysAdminStatus_Object((1,3,6,1,4,1,4515,1,3,1,6),_SlmSysAdminStatus_Type())
slmSysAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysAdminStatus.setStatus(_A)
class _SlmSysOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_K,3)))
_SlmSysOperStatus_Type.__name__=_D
_SlmSysOperStatus_Object=MibScalar
slmSysOperStatus=_SlmSysOperStatus_Object((1,3,6,1,4,1,4515,1,3,1,7),_SlmSysOperStatus_Type())
slmSysOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysOperStatus.setStatus(_A)
class _SlmBoxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('half',1),('full',2)))
_SlmBoxSize_Type.__name__=_D
_SlmBoxSize_Object=MibScalar
slmBoxSize=_SlmBoxSize_Object((1,3,6,1,4,1,4515,1,3,1,8),_SlmBoxSize_Type())
slmBoxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:slmBoxSize.setStatus(_A)
_SlmSysCalendarTime_Type=DateAndTime
_SlmSysCalendarTime_Object=MibScalar
slmSysCalendarTime=_SlmSysCalendarTime_Object((1,3,6,1,4,1,4515,1,3,1,9),_SlmSysCalendarTime_Type())
slmSysCalendarTime.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysCalendarTime.setStatus(_A)
class _SlmSysPmStartOfDay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_SlmSysPmStartOfDay_Type.__name__=_D
_SlmSysPmStartOfDay_Object=MibScalar
slmSysPmStartOfDay=_SlmSysPmStartOfDay_Object((1,3,6,1,4,1,4515,1,3,1,10),_SlmSysPmStartOfDay_Type())
slmSysPmStartOfDay.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysPmStartOfDay.setStatus(_A)
class _SlmSysActiveSwVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('swRevA',1),('swRevB',2),('swRevFtpStart',3),('swRevFtpEnd',4),('swRevAHot',5),('swRevBHot',6)))
_SlmSysActiveSwVersion_Type.__name__=_D
_SlmSysActiveSwVersion_Object=MibScalar
slmSysActiveSwVersion=_SlmSysActiveSwVersion_Object((1,3,6,1,4,1,4515,1,3,1,11),_SlmSysActiveSwVersion_Type())
slmSysActiveSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysActiveSwVersion.setStatus(_A)
_SlmSwRevTable_Object=MibTable
slmSwRevTable=_SlmSwRevTable_Object((1,3,6,1,4,1,4515,1,3,1,12))
if mibBuilder.loadTexts:slmSwRevTable.setStatus(_A)
_SlmSwRevEntry_Object=MibTableRow
slmSwRevEntry=_SlmSwRevEntry_Object((1,3,6,1,4,1,4515,1,3,1,12,1))
slmSwRevEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:slmSwRevEntry.setStatus(_A)
class _SlmSwRevDirectory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('swRevDirA',1),('swRevDirB',2)))
_SlmSwRevDirectory_Type.__name__=_D
_SlmSwRevDirectory_Object=MibTableColumn
slmSwRevDirectory=_SlmSwRevDirectory_Object((1,3,6,1,4,1,4515,1,3,1,12,1,1),_SlmSwRevDirectory_Type())
slmSwRevDirectory.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSwRevDirectory.setStatus(_A)
class _SlmSwRevStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valid',1),('invalid',2),('copyingToStandby',3)))
_SlmSwRevStatus_Type.__name__=_D
_SlmSwRevStatus_Object=MibTableColumn
slmSwRevStatus=_SlmSwRevStatus_Object((1,3,6,1,4,1,4515,1,3,1,12,1,2),_SlmSwRevStatus_Type())
slmSwRevStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSwRevStatus.setStatus(_A)
_SlmSwRevName_Type=SoftwareRevision
_SlmSwRevName_Object=MibTableColumn
slmSwRevName=_SlmSwRevName_Object((1,3,6,1,4,1,4515,1,3,1,12,1,3),_SlmSwRevName_Type())
slmSwRevName.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSwRevName.setStatus(_A)
_SlmSwRevDate_Type=DateAndTime
_SlmSwRevDate_Object=MibTableColumn
slmSwRevDate=_SlmSwRevDate_Object((1,3,6,1,4,1,4515,1,3,1,12,1,4),_SlmSwRevDate_Type())
slmSwRevDate.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSwRevDate.setStatus(_A)
_SlmConfigSysUptime_Type=TimeTicks
_SlmConfigSysUptime_Object=MibScalar
slmConfigSysUptime=_SlmConfigSysUptime_Object((1,3,6,1,4,1,4515,1,3,1,13),_SlmConfigSysUptime_Type())
slmConfigSysUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:slmConfigSysUptime.setStatus(_A)
class _SlmConfigSysSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sonet',1),('sdh',2)))
_SlmConfigSysSignalType_Type.__name__=_D
_SlmConfigSysSignalType_Object=MibScalar
slmConfigSysSignalType=_SlmConfigSysSignalType_Object((1,3,6,1,4,1,4515,1,3,1,14),_SlmConfigSysSignalType_Type())
slmConfigSysSignalType.setMaxAccess(_C)
if mibBuilder.loadTexts:slmConfigSysSignalType.setStatus(_A)
class _SlmRebootDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_SlmRebootDelay_Type.__name__=_D
_SlmRebootDelay_Object=MibScalar
slmRebootDelay=_SlmRebootDelay_Object((1,3,6,1,4,1,4515,1,3,1,16),_SlmRebootDelay_Type())
slmRebootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:slmRebootDelay.setStatus(_A)
_SlmVcatDelay_Type=Integer32
_SlmVcatDelay_Object=MibScalar
slmVcatDelay=_SlmVcatDelay_Object((1,3,6,1,4,1,4515,1,3,1,17),_SlmVcatDelay_Type())
slmVcatDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:slmVcatDelay.setStatus(_A)
class _SlmTid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlmTid_Type.__name__=_I
_SlmTid_Object=MibScalar
slmTid=_SlmTid_Object((1,3,6,1,4,1,4515,1,3,1,18),_SlmTid_Type())
slmTid.setMaxAccess(_C)
if mibBuilder.loadTexts:slmTid.setStatus(_A)
_SlmPsuNumber_Type=Integer32
_SlmPsuNumber_Object=MibScalar
slmPsuNumber=_SlmPsuNumber_Object((1,3,6,1,4,1,4515,1,3,1,19),_SlmPsuNumber_Type())
slmPsuNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:slmPsuNumber.setStatus(_A)
_SlmOemType_Type=Integer32
_SlmOemType_Object=MibScalar
slmOemType=_SlmOemType_Object((1,3,6,1,4,1,4515,1,3,1,20),_SlmOemType_Type())
slmOemType.setMaxAccess(_B)
if mibBuilder.loadTexts:slmOemType.setStatus(_A)
_SlmSysName_Type=DisplayString
_SlmSysName_Object=MibScalar
slmSysName=_SlmSysName_Object((1,3,6,1,4,1,4515,1,3,1,21),_SlmSysName_Type())
slmSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysName.setStatus(_A)
_SlmSysLocation_Type=DisplayString
_SlmSysLocation_Object=MibScalar
slmSysLocation=_SlmSysLocation_Object((1,3,6,1,4,1,4515,1,3,1,22),_SlmSysLocation_Type())
slmSysLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysLocation.setStatus(_A)
_SlmSysResetPm_Type=Integer32
_SlmSysResetPm_Object=MibScalar
slmSysResetPm=_SlmSysResetPm_Object((1,3,6,1,4,1,4515,1,3,1,23),_SlmSysResetPm_Type())
slmSysResetPm.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysResetPm.setStatus(_A)
class _SlmSysUplinkRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up100',1),('up1000',2)))
_SlmSysUplinkRate_Type.__name__=_D
_SlmSysUplinkRate_Object=MibScalar
slmSysUplinkRate=_SlmSysUplinkRate_Object((1,3,6,1,4,1,4515,1,3,1,24),_SlmSysUplinkRate_Type())
slmSysUplinkRate.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysUplinkRate.setStatus(_A)
_SlmSysChassisId_Type=Integer32
_SlmSysChassisId_Object=MibScalar
slmSysChassisId=_SlmSysChassisId_Object((1,3,6,1,4,1,4515,1,3,1,25),_SlmSysChassisId_Type())
slmSysChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysChassisId.setStatus(_A)
_SlmSysNetworkPrefix_Type=Integer32
_SlmSysNetworkPrefix_Object=MibScalar
slmSysNetworkPrefix=_SlmSysNetworkPrefix_Object((1,3,6,1,4,1,4515,1,3,1,26),_SlmSysNetworkPrefix_Type())
slmSysNetworkPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysNetworkPrefix.setStatus(_A)
_SlmSysLanIpAddr_Type=IpAddress
_SlmSysLanIpAddr_Object=MibScalar
slmSysLanIpAddr=_SlmSysLanIpAddr_Object((1,3,6,1,4,1,4515,1,3,1,27),_SlmSysLanIpAddr_Type())
slmSysLanIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysLanIpAddr.setStatus(_A)
_SlmSysLanSubnetAddr_Type=IpAddress
_SlmSysLanSubnetAddr_Object=MibScalar
slmSysLanSubnetAddr=_SlmSysLanSubnetAddr_Object((1,3,6,1,4,1,4515,1,3,1,28),_SlmSysLanSubnetAddr_Type())
slmSysLanSubnetAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysLanSubnetAddr.setStatus(_A)
_SlmPmAvailable_Type=TruthValue
_SlmPmAvailable_Object=MibScalar
slmPmAvailable=_SlmPmAvailable_Object((1,3,6,1,4,1,4515,1,3,1,29),_SlmPmAvailable_Type())
slmPmAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:slmPmAvailable.setStatus(_A)
_SlmPortsNumber_Type=Integer32
_SlmPortsNumber_Object=MibScalar
slmPortsNumber=_SlmPortsNumber_Object((1,3,6,1,4,1,4515,1,3,1,30),_SlmPortsNumber_Type())
slmPortsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slmPortsNumber.setStatus(_A)
_SlmEdfaNumber_Type=Integer32
_SlmEdfaNumber_Object=MibScalar
slmEdfaNumber=_SlmEdfaNumber_Object((1,3,6,1,4,1,4515,1,3,1,31),_SlmEdfaNumber_Type())
slmEdfaNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slmEdfaNumber.setStatus(_A)
_SlmMuxNumber_Type=Integer32
_SlmMuxNumber_Object=MibScalar
slmMuxNumber=_SlmMuxNumber_Object((1,3,6,1,4,1,4515,1,3,1,32),_SlmMuxNumber_Type())
slmMuxNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:slmMuxNumber.setStatus(_A)
_SlmOpticalSwitchExist_Type=TruthValue
_SlmOpticalSwitchExist_Object=MibScalar
slmOpticalSwitchExist=_SlmOpticalSwitchExist_Object((1,3,6,1,4,1,4515,1,3,1,33),_SlmOpticalSwitchExist_Type())
slmOpticalSwitchExist.setMaxAccess(_B)
if mibBuilder.loadTexts:slmOpticalSwitchExist.setStatus(_A)
_SlmReadCommunity_Type=DisplayString
_SlmReadCommunity_Object=MibScalar
slmReadCommunity=_SlmReadCommunity_Object((1,3,6,1,4,1,4515,1,3,1,34),_SlmReadCommunity_Type())
slmReadCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:slmReadCommunity.setStatus(_A)
_SlmWriteCommunity_Type=DisplayString
_SlmWriteCommunity_Object=MibScalar
slmWriteCommunity=_SlmWriteCommunity_Object((1,3,6,1,4,1,4515,1,3,1,35),_SlmWriteCommunity_Type())
slmWriteCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:slmWriteCommunity.setStatus(_A)
_SlmSysEffectiveSubnetMask_Type=IpAddress
_SlmSysEffectiveSubnetMask_Object=MibScalar
slmSysEffectiveSubnetMask=_SlmSysEffectiveSubnetMask_Object((1,3,6,1,4,1,4515,1,3,1,36),_SlmSysEffectiveSubnetMask_Type())
slmSysEffectiveSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysEffectiveSubnetMask.setStatus(_A)
_SlmSysEffectiveIpAddr_Type=IpAddress
_SlmSysEffectiveIpAddr_Object=MibScalar
slmSysEffectiveIpAddr=_SlmSysEffectiveIpAddr_Object((1,3,6,1,4,1,4515,1,3,1,37),_SlmSysEffectiveIpAddr_Type())
slmSysEffectiveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysEffectiveIpAddr.setStatus(_A)
_SlmSysLanEffectiveIpAddr_Type=IpAddress
_SlmSysLanEffectiveIpAddr_Object=MibScalar
slmSysLanEffectiveIpAddr=_SlmSysLanEffectiveIpAddr_Object((1,3,6,1,4,1,4515,1,3,1,38),_SlmSysLanEffectiveIpAddr_Type())
slmSysLanEffectiveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysLanEffectiveIpAddr.setStatus(_A)
_SlmSysLanEffectiveSubnetAddr_Type=IpAddress
_SlmSysLanEffectiveSubnetAddr_Object=MibScalar
slmSysLanEffectiveSubnetAddr=_SlmSysLanEffectiveSubnetAddr_Object((1,3,6,1,4,1,4515,1,3,1,39),_SlmSysLanEffectiveSubnetAddr_Type())
slmSysLanEffectiveSubnetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysLanEffectiveSubnetAddr.setStatus(_A)
_SlmSysGatewayEffectiveIpAddr_Type=IpAddress
_SlmSysGatewayEffectiveIpAddr_Object=MibScalar
slmSysGatewayEffectiveIpAddr=_SlmSysGatewayEffectiveIpAddr_Object((1,3,6,1,4,1,4515,1,3,1,40),_SlmSysGatewayEffectiveIpAddr_Type())
slmSysGatewayEffectiveIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysGatewayEffectiveIpAddr.setStatus(_A)
_SlmSysMode_Type=Integer32
_SlmSysMode_Object=MibScalar
slmSysMode=_SlmSysMode_Object((1,3,6,1,4,1,4515,1,3,1,41),_SlmSysMode_Type())
slmSysMode.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysMode.setStatus(_A)
class _SlmSysTrapFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fullIfIndex',1),('portIfIndex',2)))
_SlmSysTrapFormat_Type.__name__=_D
_SlmSysTrapFormat_Object=MibScalar
slmSysTrapFormat=_SlmSysTrapFormat_Object((1,3,6,1,4,1,4515,1,3,1,42),_SlmSysTrapFormat_Type())
slmSysTrapFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysTrapFormat.setStatus(_A)
_SlmSysTemperature_Type=Integer32
_SlmSysTemperature_Object=MibScalar
slmSysTemperature=_SlmSysTemperature_Object((1,3,6,1,4,1,4515,1,3,1,43),_SlmSysTemperature_Type())
slmSysTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysTemperature.setStatus(_A)
class _SlmNetworkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('routing',1),('switching',2)))
_SlmNetworkMode_Type.__name__=_D
_SlmNetworkMode_Object=MibScalar
slmNetworkMode=_SlmNetworkMode_Object((1,3,6,1,4,1,4515,1,3,1,44),_SlmNetworkMode_Type())
slmNetworkMode.setMaxAccess(_C)
if mibBuilder.loadTexts:slmNetworkMode.setStatus(_A)
class _Slm40GConf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,100)));namedValues=NamedValues(*(('g40',0),('g41',1),('g42',2),('g43',3),('g100',100)))
_Slm40GConf_Type.__name__=_D
_Slm40GConf_Object=MibScalar
slm40GConf=_Slm40GConf_Object((1,3,6,1,4,1,4515,1,3,1,45),_Slm40GConf_Type())
slm40GConf.setMaxAccess(_C)
if mibBuilder.loadTexts:slm40GConf.setStatus(_A)
_SlmRstpEnabled_Type=TruthValue
_SlmRstpEnabled_Object=MibScalar
slmRstpEnabled=_SlmRstpEnabled_Object((1,3,6,1,4,1,4515,1,3,1,46),_SlmRstpEnabled_Type())
slmRstpEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:slmRstpEnabled.setStatus(_A)
_SlmTopologyEnabled_Type=TruthValue
_SlmTopologyEnabled_Object=MibScalar
slmTopologyEnabled=_SlmTopologyEnabled_Object((1,3,6,1,4,1,4515,1,3,1,47),_SlmTopologyEnabled_Type())
slmTopologyEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:slmTopologyEnabled.setStatus(_A)
_SlmAdminCommunity_Type=DisplayString
_SlmAdminCommunity_Object=MibScalar
slmAdminCommunity=_SlmAdminCommunity_Object((1,3,6,1,4,1,4515,1,3,1,48),_SlmAdminCommunity_Type())
slmAdminCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:slmAdminCommunity.setStatus(_A)
_SlmTrapCommunity_Type=DisplayString
_SlmTrapCommunity_Object=MibScalar
slmTrapCommunity=_SlmTrapCommunity_Object((1,3,6,1,4,1,4515,1,3,1,49),_SlmTrapCommunity_Type())
slmTrapCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:slmTrapCommunity.setStatus(_A)
class _SlmSysSnmpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('v3Only',3),('v1v2v3',4)))
_SlmSysSnmpVersion_Type.__name__=_D
_SlmSysSnmpVersion_Object=MibScalar
slmSysSnmpVersion=_SlmSysSnmpVersion_Object((1,3,6,1,4,1,4515,1,3,1,50),_SlmSysSnmpVersion_Type())
slmSysSnmpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysSnmpVersion.setStatus(_A)
class _SlmSysEncryptionCapability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_SlmSysEncryptionCapability_Type.__name__=_D
_SlmSysEncryptionCapability_Object=MibScalar
slmSysEncryptionCapability=_SlmSysEncryptionCapability_Object((1,3,6,1,4,1,4515,1,3,1,51),_SlmSysEncryptionCapability_Type())
slmSysEncryptionCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:slmSysEncryptionCapability.setStatus(_A)
_SlmSysMaxExpirationTime_Type=Integer32
_SlmSysMaxExpirationTime_Object=MibScalar
slmSysMaxExpirationTime=_SlmSysMaxExpirationTime_Object((1,3,6,1,4,1,4515,1,3,1,52),_SlmSysMaxExpirationTime_Type())
slmSysMaxExpirationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:slmSysMaxExpirationTime.setStatus(_A)
_SlmAdmin_ObjectIdentity=ObjectIdentity
slmAdmin=_SlmAdmin_ObjectIdentity((1,3,6,1,4,1,4515,1,3,2))
_SlmAdminTable_Object=MibTable
slmAdminTable=_SlmAdminTable_Object((1,3,6,1,4,1,4515,1,3,2,1))
if mibBuilder.loadTexts:slmAdminTable.setStatus(_A)
_SlmAdminEntry_Object=MibTableRow
slmAdminEntry=_SlmAdminEntry_Object((1,3,6,1,4,1,4515,1,3,2,1,1))
slmAdminEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:slmAdminEntry.setStatus(_A)
_SlmAdminLogin_Type=UserLogin
_SlmAdminLogin_Object=MibTableColumn
slmAdminLogin=_SlmAdminLogin_Object((1,3,6,1,4,1,4515,1,3,2,1,1,3),_SlmAdminLogin_Type())
slmAdminLogin.setMaxAccess(_E)
if mibBuilder.loadTexts:slmAdminLogin.setStatus(_A)
_SlmAdminPassword_Type=UserPassword
_SlmAdminPassword_Object=MibTableColumn
slmAdminPassword=_SlmAdminPassword_Object((1,3,6,1,4,1,4515,1,3,2,1,1,4),_SlmAdminPassword_Type())
slmAdminPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:slmAdminPassword.setStatus(_A)
_SlmAdminRowStatus_Type=RowStatus
_SlmAdminRowStatus_Object=MibTableColumn
slmAdminRowStatus=_SlmAdminRowStatus_Object((1,3,6,1,4,1,4515,1,3,2,1,1,5),_SlmAdminRowStatus_Type())
slmAdminRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:slmAdminRowStatus.setStatus(_A)
_SlmAdminAccess_Type=AdminAccess
_SlmAdminAccess_Object=MibTableColumn
slmAdminAccess=_SlmAdminAccess_Object((1,3,6,1,4,1,4515,1,3,2,1,1,6),_SlmAdminAccess_Type())
slmAdminAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:slmAdminAccess.setStatus(_A)
class _SlmSnmpv3Auth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_M,1),('noauth',2),('md5',3),('sha',4),('sha224',5),('sha256',6),('sha384',7),('sha512',8)))
_SlmSnmpv3Auth_Type.__name__=_D
_SlmSnmpv3Auth_Object=MibTableColumn
slmSnmpv3Auth=_SlmSnmpv3Auth_Object((1,3,6,1,4,1,4515,1,3,2,1,1,7),_SlmSnmpv3Auth_Type())
slmSnmpv3Auth.setMaxAccess(_E)
if mibBuilder.loadTexts:slmSnmpv3Auth.setStatus(_A)
class _SlmSnmpv3Priv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_M,1),('nopriv',2),('des',3),('aes',4),('des3',5),('aes192',6),('aes256',7)))
_SlmSnmpv3Priv_Type.__name__=_D
_SlmSnmpv3Priv_Object=MibTableColumn
slmSnmpv3Priv=_SlmSnmpv3Priv_Object((1,3,6,1,4,1,4515,1,3,2,1,1,8),_SlmSnmpv3Priv_Type())
slmSnmpv3Priv.setMaxAccess(_E)
if mibBuilder.loadTexts:slmSnmpv3Priv.setStatus(_A)
_SlmSnmpv3Password_Type=UserPassword
_SlmSnmpv3Password_Object=MibTableColumn
slmSnmpv3Password=_SlmSnmpv3Password_Object((1,3,6,1,4,1,4515,1,3,2,1,1,9),_SlmSnmpv3Password_Type())
slmSnmpv3Password.setMaxAccess(_E)
if mibBuilder.loadTexts:slmSnmpv3Password.setStatus(_A)
_SlmAuth_ObjectIdentity=ObjectIdentity
slmAuth=_SlmAuth_ObjectIdentity((1,3,6,1,4,1,4515,1,3,3))
_SlmAuthTable_Object=MibTable
slmAuthTable=_SlmAuthTable_Object((1,3,6,1,4,1,4515,1,3,3,1))
if mibBuilder.loadTexts:slmAuthTable.setStatus(_A)
_SlmAuthEntry_Object=MibTableRow
slmAuthEntry=_SlmAuthEntry_Object((1,3,6,1,4,1,4515,1,3,3,1,1))
slmAuthEntry.setIndexNames((0,_F,_N),(0,_F,_O))
if mibBuilder.loadTexts:slmAuthEntry.setStatus(_A)
_SlmAuthLogin_Type=UserLogin
_SlmAuthLogin_Object=MibTableColumn
slmAuthLogin=_SlmAuthLogin_Object((1,3,6,1,4,1,4515,1,3,3,1,1,1),_SlmAuthLogin_Type())
slmAuthLogin.setMaxAccess(_H)
if mibBuilder.loadTexts:slmAuthLogin.setStatus(_A)
_SlmAuthPassword_Type=UserPassword
_SlmAuthPassword_Object=MibTableColumn
slmAuthPassword=_SlmAuthPassword_Object((1,3,6,1,4,1,4515,1,3,3,1,1,2),_SlmAuthPassword_Type())
slmAuthPassword.setMaxAccess(_H)
if mibBuilder.loadTexts:slmAuthPassword.setStatus(_A)
_SlmAuthCommunity_Type=UserCommunity
_SlmAuthCommunity_Object=MibTableColumn
slmAuthCommunity=_SlmAuthCommunity_Object((1,3,6,1,4,1,4515,1,3,3,1,1,3),_SlmAuthCommunity_Type())
slmAuthCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:slmAuthCommunity.setStatus(_A)
_SlmLogin_ObjectIdentity=ObjectIdentity
slmLogin=_SlmLogin_ObjectIdentity((1,3,6,1,4,1,4515,1,3,4))
_SlmTrap_ObjectIdentity=ObjectIdentity
slmTrap=_SlmTrap_ObjectIdentity((1,3,6,1,4,1,4515,1,3,5))
_SlmTrapDestTable_Object=MibTable
slmTrapDestTable=_SlmTrapDestTable_Object((1,3,6,1,4,1,4515,1,3,5,1))
if mibBuilder.loadTexts:slmTrapDestTable.setStatus(_A)
_SlmTrapDestEntry_Object=MibTableRow
slmTrapDestEntry=_SlmTrapDestEntry_Object((1,3,6,1,4,1,4515,1,3,5,1,1))
slmTrapDestEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:slmTrapDestEntry.setStatus(_A)
_SlmTrapDestAddress_Type=Integer32
_SlmTrapDestAddress_Object=MibTableColumn
slmTrapDestAddress=_SlmTrapDestAddress_Object((1,3,6,1,4,1,4515,1,3,5,1,1,1),_SlmTrapDestAddress_Type())
slmTrapDestAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:slmTrapDestAddress.setStatus(_A)
_SlmTrapDestRowStatus_Type=RowStatus
_SlmTrapDestRowStatus_Object=MibTableColumn
slmTrapDestRowStatus=_SlmTrapDestRowStatus_Object((1,3,6,1,4,1,4515,1,3,5,1,1,2),_SlmTrapDestRowStatus_Type())
slmTrapDestRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:slmTrapDestRowStatus.setStatus(_A)
_SlmTrapDestCommunity_Type=UserCommunity
_SlmTrapDestCommunity_Object=MibTableColumn
slmTrapDestCommunity=_SlmTrapDestCommunity_Object((1,3,6,1,4,1,4515,1,3,5,1,1,3),_SlmTrapDestCommunity_Type())
slmTrapDestCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:slmTrapDestCommunity.setStatus(_A)
class _SlmTrapDestProtVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmpVer1',1),('snmpVer2',2),('snmpVer3',3)))
_SlmTrapDestProtVersion_Type.__name__=_D
_SlmTrapDestProtVersion_Object=MibTableColumn
slmTrapDestProtVersion=_SlmTrapDestProtVersion_Object((1,3,6,1,4,1,4515,1,3,5,1,1,4),_SlmTrapDestProtVersion_Type())
slmTrapDestProtVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:slmTrapDestProtVersion.setStatus(_A)
_SlmTrapUserLogin_Type=UserLogin
_SlmTrapUserLogin_Object=MibTableColumn
slmTrapUserLogin=_SlmTrapUserLogin_Object((1,3,6,1,4,1,4515,1,3,5,1,1,5),_SlmTrapUserLogin_Type())
slmTrapUserLogin.setMaxAccess(_E)
if mibBuilder.loadTexts:slmTrapUserLogin.setStatus(_A)
_SlmTrapUserAccess_Type=AdminAccess
_SlmTrapUserAccess_Object=MibTableColumn
slmTrapUserAccess=_SlmTrapUserAccess_Object((1,3,6,1,4,1,4515,1,3,5,1,1,6),_SlmTrapUserAccess_Type())
slmTrapUserAccess.setMaxAccess(_E)
if mibBuilder.loadTexts:slmTrapUserAccess.setStatus(_A)
_SlmTrapEnable_Type=TruthValue
_SlmTrapEnable_Object=MibTableColumn
slmTrapEnable=_SlmTrapEnable_Object((1,3,6,1,4,1,4515,1,3,5,1,1,7),_SlmTrapEnable_Type())
slmTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:slmTrapEnable.setStatus(_A)
_SlmTrapPort_Type=Integer32
_SlmTrapPort_Object=MibTableColumn
slmTrapPort=_SlmTrapPort_Object((1,3,6,1,4,1,4515,1,3,5,1,1,8),_SlmTrapPort_Type())
slmTrapPort.setMaxAccess(_E)
if mibBuilder.loadTexts:slmTrapPort.setStatus(_A)
_SlmTrapDestIpAddress_Type=IpAddress
_SlmTrapDestIpAddress_Object=MibTableColumn
slmTrapDestIpAddress=_SlmTrapDestIpAddress_Object((1,3,6,1,4,1,4515,1,3,5,1,1,9),_SlmTrapDestIpAddress_Type())
slmTrapDestIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:slmTrapDestIpAddress.setStatus(_A)
_SlmTrapLogTable_Object=MibTable
slmTrapLogTable=_SlmTrapLogTable_Object((1,3,6,1,4,1,4515,1,3,5,2))
if mibBuilder.loadTexts:slmTrapLogTable.setStatus(_A)
_SlmTrapLogEntry_Object=MibTableRow
slmTrapLogEntry=_SlmTrapLogEntry_Object((1,3,6,1,4,1,4515,1,3,5,2,1))
slmTrapLogEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:slmTrapLogEntry.setStatus(_A)
_SlmTrapLogId_Type=Gauge32
_SlmTrapLogId_Object=MibTableColumn
slmTrapLogId=_SlmTrapLogId_Object((1,3,6,1,4,1,4515,1,3,5,2,1,1),_SlmTrapLogId_Type())
slmTrapLogId.setMaxAccess(_B)
if mibBuilder.loadTexts:slmTrapLogId.setStatus(_A)
class _SlmTrapLogName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlmTrapLogName_Type.__name__=_G
_SlmTrapLogName_Object=MibTableColumn
slmTrapLogName=_SlmTrapLogName_Object((1,3,6,1,4,1,4515,1,3,5,2,1,2),_SlmTrapLogName_Type())
slmTrapLogName.setMaxAccess(_B)
if mibBuilder.loadTexts:slmTrapLogName.setStatus(_A)
_SlmTrapLogTimeStamp_Type=TimeTicks
_SlmTrapLogTimeStamp_Object=MibTableColumn
slmTrapLogTimeStamp=_SlmTrapLogTimeStamp_Object((1,3,6,1,4,1,4515,1,3,5,2,1,3),_SlmTrapLogTimeStamp_Type())
slmTrapLogTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:slmTrapLogTimeStamp.setStatus(_A)
class _SlmTrapLogParam1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlmTrapLogParam1_Type.__name__=_G
_SlmTrapLogParam1_Object=MibTableColumn
slmTrapLogParam1=_SlmTrapLogParam1_Object((1,3,6,1,4,1,4515,1,3,5,2,1,4),_SlmTrapLogParam1_Type())
slmTrapLogParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:slmTrapLogParam1.setStatus(_A)
class _SlmTrapLogParam2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlmTrapLogParam2_Type.__name__=_G
_SlmTrapLogParam2_Object=MibTableColumn
slmTrapLogParam2=_SlmTrapLogParam2_Object((1,3,6,1,4,1,4515,1,3,5,2,1,5),_SlmTrapLogParam2_Type())
slmTrapLogParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:slmTrapLogParam2.setStatus(_A)
class _SlmTrapLogParam3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlmTrapLogParam3_Type.__name__=_G
_SlmTrapLogParam3_Object=MibTableColumn
slmTrapLogParam3=_SlmTrapLogParam3_Object((1,3,6,1,4,1,4515,1,3,5,2,1,6),_SlmTrapLogParam3_Type())
slmTrapLogParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:slmTrapLogParam3.setStatus(_A)
class _SlmTrapLogParam4_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlmTrapLogParam4_Type.__name__=_G
_SlmTrapLogParam4_Object=MibTableColumn
slmTrapLogParam4=_SlmTrapLogParam4_Object((1,3,6,1,4,1,4515,1,3,5,2,1,7),_SlmTrapLogParam4_Type())
slmTrapLogParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:slmTrapLogParam4.setStatus(_A)
class _SlmTrapLogParam5_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlmTrapLogParam5_Type.__name__=_G
_SlmTrapLogParam5_Object=MibTableColumn
slmTrapLogParam5=_SlmTrapLogParam5_Object((1,3,6,1,4,1,4515,1,3,5,2,1,8),_SlmTrapLogParam5_Type())
slmTrapLogParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:slmTrapLogParam5.setStatus(_A)
class _SlmTrapLogParam6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlmTrapLogParam6_Type.__name__=_G
_SlmTrapLogParam6_Object=MibTableColumn
slmTrapLogParam6=_SlmTrapLogParam6_Object((1,3,6,1,4,1,4515,1,3,5,2,1,9),_SlmTrapLogParam6_Type())
slmTrapLogParam6.setMaxAccess(_B)
if mibBuilder.loadTexts:slmTrapLogParam6.setStatus(_A)
_SlmSyslogDestTable_Object=MibTable
slmSyslogDestTable=_SlmSyslogDestTable_Object((1,3,6,1,4,1,4515,1,3,5,7))
if mibBuilder.loadTexts:slmSyslogDestTable.setStatus(_A)
_SlmSyslogDestEntry_Object=MibTableRow
slmSyslogDestEntry=_SlmSyslogDestEntry_Object((1,3,6,1,4,1,4515,1,3,5,7,1))
slmSyslogDestEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:slmSyslogDestEntry.setStatus(_A)
_SlmSyslogDestAddress_Type=Integer32
_SlmSyslogDestAddress_Object=MibTableColumn
slmSyslogDestAddress=_SlmSyslogDestAddress_Object((1,3,6,1,4,1,4515,1,3,5,7,1,1),_SlmSyslogDestAddress_Type())
slmSyslogDestAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:slmSyslogDestAddress.setStatus(_A)
_SlmSyslogDestRowStatus_Type=RowStatus
_SlmSyslogDestRowStatus_Object=MibTableColumn
slmSyslogDestRowStatus=_SlmSyslogDestRowStatus_Object((1,3,6,1,4,1,4515,1,3,5,7,1,2),_SlmSyslogDestRowStatus_Type())
slmSyslogDestRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:slmSyslogDestRowStatus.setStatus(_A)
class _SlmSyslogLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('traps',1),('log',2),('debug',3)))
_SlmSyslogLevel_Type.__name__=_D
_SlmSyslogLevel_Object=MibTableColumn
slmSyslogLevel=_SlmSyslogLevel_Object((1,3,6,1,4,1,4515,1,3,5,7,1,3),_SlmSyslogLevel_Type())
slmSyslogLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:slmSyslogLevel.setStatus(_A)
_SlmSyslogPort_Type=Integer32
_SlmSyslogPort_Object=MibTableColumn
slmSyslogPort=_SlmSyslogPort_Object((1,3,6,1,4,1,4515,1,3,5,7,1,4),_SlmSyslogPort_Type())
slmSyslogPort.setMaxAccess(_E)
if mibBuilder.loadTexts:slmSyslogPort.setStatus(_A)
_SlmSyslogDestIpAddress_Type=IpAddress
_SlmSyslogDestIpAddress_Object=MibTableColumn
slmSyslogDestIpAddress=_SlmSyslogDestIpAddress_Object((1,3,6,1,4,1,4515,1,3,5,7,1,5),_SlmSyslogDestIpAddress_Type())
slmSyslogDestIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:slmSyslogDestIpAddress.setStatus(_A)
_SlmLogFile_ObjectIdentity=ObjectIdentity
slmLogFile=_SlmLogFile_ObjectIdentity((1,3,6,1,4,1,4515,1,3,8))
_SlmConfigFile_ObjectIdentity=ObjectIdentity
slmConfigFile=_SlmConfigFile_ObjectIdentity((1,3,6,1,4,1,4515,1,3,9))
_SlmChPass_ObjectIdentity=ObjectIdentity
slmChPass=_SlmChPass_ObjectIdentity((1,3,6,1,4,1,4515,1,3,12))
_SlmChPassTable_Object=MibTable
slmChPassTable=_SlmChPassTable_Object((1,3,6,1,4,1,4515,1,3,12,1))
if mibBuilder.loadTexts:slmChPassTable.setStatus(_A)
_SlmChPassEntry_Object=MibTableRow
slmChPassEntry=_SlmChPassEntry_Object((1,3,6,1,4,1,4515,1,3,12,1,1))
slmChPassEntry.setIndexNames((0,_F,_S),(0,_F,_T))
if mibBuilder.loadTexts:slmChPassEntry.setStatus(_A)
_SlmChPassLogin_Type=UserLogin
_SlmChPassLogin_Object=MibTableColumn
slmChPassLogin=_SlmChPassLogin_Object((1,3,6,1,4,1,4515,1,3,12,1,1,1),_SlmChPassLogin_Type())
slmChPassLogin.setMaxAccess(_H)
if mibBuilder.loadTexts:slmChPassLogin.setStatus(_A)
_SlmChPassOldPass_Type=UserPassword
_SlmChPassOldPass_Object=MibTableColumn
slmChPassOldPass=_SlmChPassOldPass_Object((1,3,6,1,4,1,4515,1,3,12,1,1,2),_SlmChPassOldPass_Type())
slmChPassOldPass.setMaxAccess(_H)
if mibBuilder.loadTexts:slmChPassOldPass.setStatus(_A)
_SlmChPassNewPass_Type=UserPassword
_SlmChPassNewPass_Object=MibTableColumn
slmChPassNewPass=_SlmChPassNewPass_Object((1,3,6,1,4,1,4515,1,3,12,1,1,3),_SlmChPassNewPass_Type())
slmChPassNewPass.setMaxAccess(_C)
if mibBuilder.loadTexts:slmChPassNewPass.setStatus(_A)
_SlmLicense_ObjectIdentity=ObjectIdentity
slmLicense=_SlmLicense_ObjectIdentity((1,3,6,1,4,1,4515,1,3,17))
_SlmLicenseTable_Object=MibTable
slmLicenseTable=_SlmLicenseTable_Object((1,3,6,1,4,1,4515,1,3,17,1))
if mibBuilder.loadTexts:slmLicenseTable.setStatus(_A)
_SlmLicenseEntry_Object=MibTableRow
slmLicenseEntry=_SlmLicenseEntry_Object((1,3,6,1,4,1,4515,1,3,17,1,1))
slmLicenseEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:slmLicenseEntry.setStatus(_A)
_SlmLicenseIndex_Type=Integer32
_SlmLicenseIndex_Object=MibTableColumn
slmLicenseIndex=_SlmLicenseIndex_Object((1,3,6,1,4,1,4515,1,3,17,1,1,1),_SlmLicenseIndex_Type())
slmLicenseIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slmLicenseIndex.setStatus(_A)
_SlmLicenseExpiration_Type=Integer32
_SlmLicenseExpiration_Object=MibTableColumn
slmLicenseExpiration=_SlmLicenseExpiration_Object((1,3,6,1,4,1,4515,1,3,17,1,1,2),_SlmLicenseExpiration_Type())
slmLicenseExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:slmLicenseExpiration.setStatus(_A)
class _SlmLicenseId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_SlmLicenseId_Type.__name__=_I
_SlmLicenseId_Object=MibTableColumn
slmLicenseId=_SlmLicenseId_Object((1,3,6,1,4,1,4515,1,3,17,1,1,3),_SlmLicenseId_Type())
slmLicenseId.setMaxAccess(_B)
if mibBuilder.loadTexts:slmLicenseId.setStatus(_A)
slmTrapSoftwareStatusChange=NotificationType((1,3,6,1,4,1,4515,1,3,5,4))
slmTrapSoftwareStatusChange.setObjects(*((_F,_J),(_F,_V)))
if mibBuilder.loadTexts:slmTrapSoftwareStatusChange.setStatus(_A)
slmTrapSysNameChange=NotificationType((1,3,6,1,4,1,4515,1,3,5,5))
slmTrapSysNameChange.setObjects((_F,_W))
if mibBuilder.loadTexts:slmTrapSysNameChange.setStatus(_A)
slmTrapSysLocationChange=NotificationType((1,3,6,1,4,1,4515,1,3,5,6))
slmTrapSysLocationChange.setObjects((_F,_X))
if mibBuilder.loadTexts:slmTrapSysLocationChange.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'UserLogin':UserLogin,'UserPassword':UserPassword,'UserCommunity':UserCommunity,'SoftwareRevision':SoftwareRevision,'AdminAccess':AdminAccess,'slMain':slMain,'slmSys':slmSys,'slmSysGatewayAddr':slmSysGatewayAddr,'slmSysSubnetMask':slmSysSubnetMask,'slmSysIpAddr':slmSysIpAddr,'slmSysAlmAct':slmSysAlmAct,'slmSysAlmDeact':slmSysAlmDeact,'slmSysAdminStatus':slmSysAdminStatus,'slmSysOperStatus':slmSysOperStatus,'slmBoxSize':slmBoxSize,'slmSysCalendarTime':slmSysCalendarTime,'slmSysPmStartOfDay':slmSysPmStartOfDay,'slmSysActiveSwVersion':slmSysActiveSwVersion,'slmSwRevTable':slmSwRevTable,'slmSwRevEntry':slmSwRevEntry,_J:slmSwRevDirectory,_V:slmSwRevStatus,'slmSwRevName':slmSwRevName,'slmSwRevDate':slmSwRevDate,'slmConfigSysUptime':slmConfigSysUptime,'slmConfigSysSignalType':slmConfigSysSignalType,'slmRebootDelay':slmRebootDelay,'slmVcatDelay':slmVcatDelay,'slmTid':slmTid,'slmPsuNumber':slmPsuNumber,'slmOemType':slmOemType,_W:slmSysName,_X:slmSysLocation,'slmSysResetPm':slmSysResetPm,'slmSysUplinkRate':slmSysUplinkRate,'slmSysChassisId':slmSysChassisId,'slmSysNetworkPrefix':slmSysNetworkPrefix,'slmSysLanIpAddr':slmSysLanIpAddr,'slmSysLanSubnetAddr':slmSysLanSubnetAddr,'slmPmAvailable':slmPmAvailable,'slmPortsNumber':slmPortsNumber,'slmEdfaNumber':slmEdfaNumber,'slmMuxNumber':slmMuxNumber,'slmOpticalSwitchExist':slmOpticalSwitchExist,'slmReadCommunity':slmReadCommunity,'slmWriteCommunity':slmWriteCommunity,'slmSysEffectiveSubnetMask':slmSysEffectiveSubnetMask,'slmSysEffectiveIpAddr':slmSysEffectiveIpAddr,'slmSysLanEffectiveIpAddr':slmSysLanEffectiveIpAddr,'slmSysLanEffectiveSubnetAddr':slmSysLanEffectiveSubnetAddr,'slmSysGatewayEffectiveIpAddr':slmSysGatewayEffectiveIpAddr,'slmSysMode':slmSysMode,'slmSysTrapFormat':slmSysTrapFormat,'slmSysTemperature':slmSysTemperature,'slmNetworkMode':slmNetworkMode,'slm40GConf':slm40GConf,'slmRstpEnabled':slmRstpEnabled,'slmTopologyEnabled':slmTopologyEnabled,'slmAdminCommunity':slmAdminCommunity,'slmTrapCommunity':slmTrapCommunity,'slmSysSnmpVersion':slmSysSnmpVersion,'slmSysEncryptionCapability':slmSysEncryptionCapability,'slmSysMaxExpirationTime':slmSysMaxExpirationTime,'slmAdmin':slmAdmin,'slmAdminTable':slmAdminTable,'slmAdminEntry':slmAdminEntry,_L:slmAdminLogin,'slmAdminPassword':slmAdminPassword,'slmAdminRowStatus':slmAdminRowStatus,'slmAdminAccess':slmAdminAccess,'slmSnmpv3Auth':slmSnmpv3Auth,'slmSnmpv3Priv':slmSnmpv3Priv,'slmSnmpv3Password':slmSnmpv3Password,'slmAuth':slmAuth,'slmAuthTable':slmAuthTable,'slmAuthEntry':slmAuthEntry,_N:slmAuthLogin,_O:slmAuthPassword,'slmAuthCommunity':slmAuthCommunity,'slmLogin':slmLogin,'slmTrap':slmTrap,'slmTrapDestTable':slmTrapDestTable,'slmTrapDestEntry':slmTrapDestEntry,_P:slmTrapDestAddress,'slmTrapDestRowStatus':slmTrapDestRowStatus,'slmTrapDestCommunity':slmTrapDestCommunity,'slmTrapDestProtVersion':slmTrapDestProtVersion,'slmTrapUserLogin':slmTrapUserLogin,'slmTrapUserAccess':slmTrapUserAccess,'slmTrapEnable':slmTrapEnable,'slmTrapPort':slmTrapPort,'slmTrapDestIpAddress':slmTrapDestIpAddress,'slmTrapLogTable':slmTrapLogTable,'slmTrapLogEntry':slmTrapLogEntry,_Q:slmTrapLogId,'slmTrapLogName':slmTrapLogName,'slmTrapLogTimeStamp':slmTrapLogTimeStamp,'slmTrapLogParam1':slmTrapLogParam1,'slmTrapLogParam2':slmTrapLogParam2,'slmTrapLogParam3':slmTrapLogParam3,'slmTrapLogParam4':slmTrapLogParam4,'slmTrapLogParam5':slmTrapLogParam5,'slmTrapLogParam6':slmTrapLogParam6,'slmTrapSoftwareStatusChange':slmTrapSoftwareStatusChange,'slmTrapSysNameChange':slmTrapSysNameChange,'slmTrapSysLocationChange':slmTrapSysLocationChange,'slmSyslogDestTable':slmSyslogDestTable,'slmSyslogDestEntry':slmSyslogDestEntry,_R:slmSyslogDestAddress,'slmSyslogDestRowStatus':slmSyslogDestRowStatus,'slmSyslogLevel':slmSyslogLevel,'slmSyslogPort':slmSyslogPort,'slmSyslogDestIpAddress':slmSyslogDestIpAddress,'slmLogFile':slmLogFile,'slmConfigFile':slmConfigFile,'slmChPass':slmChPass,'slmChPassTable':slmChPassTable,'slmChPassEntry':slmChPassEntry,_S:slmChPassLogin,_T:slmChPassOldPass,'slmChPassNewPass':slmChPassNewPass,'slmLicense':slmLicense,'slmLicenseTable':slmLicenseTable,'slmLicenseEntry':slmLicenseEntry,_U:slmLicenseIndex,'slmLicenseExpiration':slmLicenseExpiration,'slmLicenseId':slmLicenseId})