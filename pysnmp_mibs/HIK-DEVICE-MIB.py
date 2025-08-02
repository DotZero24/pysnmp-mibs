_D='read-write'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Test_ObjectIdentity=ObjectIdentity
test=_Test_ObjectIdentity((1,3,6,1,4,1,39165))
_Devicemib_ObjectIdentity=ObjectIdentity
devicemib=_Devicemib_ObjectIdentity((1,3,6,1,4,1,39165,1))
class _DeviceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DeviceType_Type.__name__=_C
_DeviceType_Object=MibScalar
deviceType=_DeviceType_Object((1,3,6,1,4,1,39165,1,1),_DeviceType_Type())
deviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceType.setStatus(_A)
class _HardwVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HardwVersion_Type.__name__=_C
_HardwVersion_Object=MibScalar
hardwVersion=_HardwVersion_Object((1,3,6,1,4,1,39165,1,2),_HardwVersion_Type())
hardwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hardwVersion.setStatus(_A)
class _SoftwVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SoftwVersion_Type.__name__=_C
_SoftwVersion_Object=MibScalar
softwVersion=_SoftwVersion_Object((1,3,6,1,4,1,39165,1,3),_SoftwVersion_Type())
softwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:softwVersion.setStatus(_A)
class _MacAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MacAddr_Type.__name__=_C
_MacAddr_Object=MibScalar
macAddr=_MacAddr_Object((1,3,6,1,4,1,39165,1,4),_MacAddr_Type())
macAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:macAddr.setStatus(_A)
class _DeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DeviceID_Type.__name__=_C
_DeviceID_Object=MibScalar
deviceID=_DeviceID_Object((1,3,6,1,4,1,39165,1,5),_DeviceID_Type())
deviceID.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceID.setStatus(_A)
class _Manufacturer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Manufacturer_Type.__name__=_C
_Manufacturer_Object=MibScalar
manufacturer=_Manufacturer_Object((1,3,6,1,4,1,39165,1,6),_Manufacturer_Type())
manufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:manufacturer.setStatus(_A)
class _CpuPercent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpuPercent_Type.__name__=_C
_CpuPercent_Object=MibScalar
cpuPercent=_CpuPercent_Object((1,3,6,1,4,1,39165,1,7),_CpuPercent_Type())
cpuPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuPercent.setStatus(_A)
class _DiskSize_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DiskSize_Type.__name__=_C
_DiskSize_Object=MibScalar
diskSize=_DiskSize_Object((1,3,6,1,4,1,39165,1,8),_DiskSize_Type())
diskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:diskSize.setStatus(_A)
class _DiskPercent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DiskPercent_Type.__name__=_C
_DiskPercent_Object=MibScalar
diskPercent=_DiskPercent_Object((1,3,6,1,4,1,39165,1,9),_DiskPercent_Type())
diskPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:diskPercent.setStatus(_A)
class _MemSize_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MemSize_Type.__name__=_C
_MemSize_Object=MibScalar
memSize=_MemSize_Object((1,3,6,1,4,1,39165,1,10),_MemSize_Type())
memSize.setMaxAccess(_B)
if mibBuilder.loadTexts:memSize.setStatus(_A)
class _MemUsed_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MemUsed_Type.__name__=_C
_MemUsed_Object=MibScalar
memUsed=_MemUsed_Object((1,3,6,1,4,1,39165,1,11),_MemUsed_Type())
memUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:memUsed.setStatus(_A)
_RestartDev_Type=Integer32
_RestartDev_Object=MibScalar
restartDev=_RestartDev_Object((1,3,6,1,4,1,39165,1,12),_RestartDev_Type())
restartDev.setMaxAccess(_D)
if mibBuilder.loadTexts:restartDev.setStatus(_A)
_DynIpAddr_Type=IpAddress
_DynIpAddr_Object=MibScalar
dynIpAddr=_DynIpAddr_Object((1,3,6,1,4,1,39165,1,13),_DynIpAddr_Type())
dynIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:dynIpAddr.setStatus(_A)
_DynNetMask_Type=IpAddress
_DynNetMask_Object=MibScalar
dynNetMask=_DynNetMask_Object((1,3,6,1,4,1,39165,1,14),_DynNetMask_Type())
dynNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:dynNetMask.setStatus(_A)
_DynGateway_Type=IpAddress
_DynGateway_Object=MibScalar
dynGateway=_DynGateway_Object((1,3,6,1,4,1,39165,1,15),_DynGateway_Type())
dynGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:dynGateway.setStatus(_A)
_StaticIpAddr_Type=IpAddress
_StaticIpAddr_Object=MibScalar
staticIpAddr=_StaticIpAddr_Object((1,3,6,1,4,1,39165,1,16),_StaticIpAddr_Type())
staticIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:staticIpAddr.setStatus(_A)
_StaticNetMask_Type=IpAddress
_StaticNetMask_Object=MibScalar
staticNetMask=_StaticNetMask_Object((1,3,6,1,4,1,39165,1,17),_StaticNetMask_Type())
staticNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:staticNetMask.setStatus(_A)
_StaticGateway_Type=IpAddress
_StaticGateway_Object=MibScalar
staticGateway=_StaticGateway_Object((1,3,6,1,4,1,39165,1,18),_StaticGateway_Type())
staticGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:staticGateway.setStatus(_A)
class _SysTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysTime_Type.__name__=_C
_SysTime_Object=MibScalar
sysTime=_SysTime_Object((1,3,6,1,4,1,39165,1,19),_SysTime_Type())
sysTime.setMaxAccess(_D)
if mibBuilder.loadTexts:sysTime.setStatus(_A)
_VideoInChanNum_Type=Integer32
_VideoInChanNum_Object=MibScalar
videoInChanNum=_VideoInChanNum_Object((1,3,6,1,4,1,39165,1,20),_VideoInChanNum_Type())
videoInChanNum.setMaxAccess(_B)
if mibBuilder.loadTexts:videoInChanNum.setStatus(_A)
class _VideoEncode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VideoEncode_Type.__name__=_C
_VideoEncode_Object=MibScalar
videoEncode=_VideoEncode_Object((1,3,6,1,4,1,39165,1,21),_VideoEncode_Type())
videoEncode.setMaxAccess(_B)
if mibBuilder.loadTexts:videoEncode.setStatus(_A)
class _VideoNetTrans_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VideoNetTrans_Type.__name__=_C
_VideoNetTrans_Object=MibScalar
videoNetTrans=_VideoNetTrans_Object((1,3,6,1,4,1,39165,1,22),_VideoNetTrans_Type())
videoNetTrans.setMaxAccess(_B)
if mibBuilder.loadTexts:videoNetTrans.setStatus(_A)
_AudioAbility_Type=Integer32
_AudioAbility_Object=MibScalar
audioAbility=_AudioAbility_Object((1,3,6,1,4,1,39165,1,23),_AudioAbility_Type())
audioAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:audioAbility.setStatus(_A)
_AudioInNum_Type=Integer32
_AudioInNum_Object=MibScalar
audioInNum=_AudioInNum_Object((1,3,6,1,4,1,39165,1,24),_AudioInNum_Type())
audioInNum.setMaxAccess(_B)
if mibBuilder.loadTexts:audioInNum.setStatus(_A)
_VideoOutNum_Type=Integer32
_VideoOutNum_Object=MibScalar
videoOutNum=_VideoOutNum_Object((1,3,6,1,4,1,39165,1,25),_VideoOutNum_Type())
videoOutNum.setMaxAccess(_B)
if mibBuilder.loadTexts:videoOutNum.setStatus(_A)
_ClarityChanNum_Type=Integer32
_ClarityChanNum_Object=MibScalar
clarityChanNum=_ClarityChanNum_Object((1,3,6,1,4,1,39165,1,26),_ClarityChanNum_Type())
clarityChanNum.setMaxAccess(_B)
if mibBuilder.loadTexts:clarityChanNum.setStatus(_A)
_LocalStorage_Type=Integer32
_LocalStorage_Object=MibScalar
localStorage=_LocalStorage_Object((1,3,6,1,4,1,39165,1,27),_LocalStorage_Type())
localStorage.setMaxAccess(_B)
if mibBuilder.loadTexts:localStorage.setStatus(_A)
_RtspPlayBack_Type=Integer32
_RtspPlayBack_Object=MibScalar
rtspPlayBack=_RtspPlayBack_Object((1,3,6,1,4,1,39165,1,28),_RtspPlayBack_Type())
rtspPlayBack.setMaxAccess(_B)
if mibBuilder.loadTexts:rtspPlayBack.setStatus(_A)
class _NetAccessType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NetAccessType_Type.__name__=_C
_NetAccessType_Object=MibScalar
netAccessType=_NetAccessType_Object((1,3,6,1,4,1,39165,1,29),_NetAccessType_Type())
netAccessType.setMaxAccess(_B)
if mibBuilder.loadTexts:netAccessType.setStatus(_A)
_AlarmInChanNum_Type=Integer32
_AlarmInChanNum_Object=MibScalar
alarmInChanNum=_AlarmInChanNum_Object((1,3,6,1,4,1,39165,1,30),_AlarmInChanNum_Type())
alarmInChanNum.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmInChanNum.setStatus(_A)
_AlarmOutChanNum_Type=Integer32
_AlarmOutChanNum_Object=MibScalar
alarmOutChanNum=_AlarmOutChanNum_Object((1,3,6,1,4,1,39165,1,31),_AlarmOutChanNum_Type())
alarmOutChanNum.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmOutChanNum.setStatus(_A)
_ManageServAddr_Type=IpAddress
_ManageServAddr_Object=MibScalar
manageServAddr=_ManageServAddr_Object((1,3,6,1,4,1,39165,1,32),_ManageServAddr_Type())
manageServAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:manageServAddr.setStatus(_A)
class _NtpServIpAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NtpServIpAddr_Type.__name__=_C
_NtpServIpAddr_Object=MibScalar
ntpServIpAddr=_NtpServIpAddr_Object((1,3,6,1,4,1,39165,1,33),_NtpServIpAddr_Type())
ntpServIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ntpServIpAddr.setStatus(_A)
_ManagePort_Type=Integer32
_ManagePort_Object=MibScalar
managePort=_ManagePort_Object((1,3,6,1,4,1,39165,1,34),_ManagePort_Type())
managePort.setMaxAccess(_D)
if mibBuilder.loadTexts:managePort.setStatus(_A)
mibBuilder.exportSymbols('HIK-DEVICE-MIB',**{'test':test,'devicemib':devicemib,'deviceType':deviceType,'hardwVersion':hardwVersion,'softwVersion':softwVersion,'macAddr':macAddr,'deviceID':deviceID,'manufacturer':manufacturer,'cpuPercent':cpuPercent,'diskSize':diskSize,'diskPercent':diskPercent,'memSize':memSize,'memUsed':memUsed,'restartDev':restartDev,'dynIpAddr':dynIpAddr,'dynNetMask':dynNetMask,'dynGateway':dynGateway,'staticIpAddr':staticIpAddr,'staticNetMask':staticNetMask,'staticGateway':staticGateway,'sysTime':sysTime,'videoInChanNum':videoInChanNum,'videoEncode':videoEncode,'videoNetTrans':videoNetTrans,'audioAbility':audioAbility,'audioInNum':audioInNum,'videoOutNum':videoOutNum,'clarityChanNum':clarityChanNum,'localStorage':localStorage,'rtspPlayBack':rtspPlayBack,'netAccessType':netAccessType,'alarmInChanNum':alarmInChanNum,'alarmOutChanNum':alarmOutChanNum,'manageServAddr':manageServAddr,'ntpServIpAddr':ntpServIpAddr,'managePort':managePort})