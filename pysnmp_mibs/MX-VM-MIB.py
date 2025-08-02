_M='vmStatusIdx'
_L='virtio'
_K='MxIpAddrMask'
_J='MxEnableState'
_I='none'
_H='MX-VM-MIB'
_G='Unsigned32'
_F='noOp'
_E='OctetString'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_J,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr',_K,'MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4500))
_VmMIBObjects_ObjectIdentity=ObjectIdentity
vmMIBObjects=_VmMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4500,1))
_ConfigGroup_ObjectIdentity=ObjectIdentity
configGroup=_ConfigGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100))
_VmTable_Object=MibTable
vmTable=_VmTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100))
if mibBuilder.loadTexts:vmTable.setStatus(_A)
_VmEntry_Object=MibTableRow
vmEntry=_VmEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1))
vmEntry.setIndexNames((0,_H,'vmIdx'))
if mibBuilder.loadTexts:vmEntry.setStatus(_A)
class _VmIdx_Type(Unsigned32):defaultValue=0
_VmIdx_Type.__name__=_G
_VmIdx_Object=MibTableColumn
vmIdx=_VmIdx_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,100),_VmIdx_Type())
vmIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmIdx.setStatus(_A)
class _VmName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_VmName_Type.__name__=_E
_VmName_Object=MibTableColumn
vmName=_VmName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,200),_VmName_Type())
vmName.setMaxAccess(_D)
if mibBuilder.loadTexts:vmName.setStatus(_A)
class _VmVncDisplayId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,99))
_VmVncDisplayId_Type.__name__=_B
_VmVncDisplayId_Object=MibTableColumn
vmVncDisplayId=_VmVncDisplayId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,300),_VmVncDisplayId_Type())
vmVncDisplayId.setMaxAccess(_D)
if mibBuilder.loadTexts:vmVncDisplayId.setStatus(_A)
class _VmUsbPort_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_I,100),('all',200)))
_VmUsbPort_Type.__name__=_B
_VmUsbPort_Object=MibTableColumn
vmUsbPort=_VmUsbPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,400),_VmUsbPort_Type())
vmUsbPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vmUsbPort.setStatus(_A)
class _VmIsoName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,510))
_VmIsoName_Type.__name__=_E
_VmIsoName_Object=MibTableColumn
vmIsoName=_VmIsoName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,500),_VmIsoName_Type())
vmIsoName.setMaxAccess(_D)
if mibBuilder.loadTexts:vmIsoName.setStatus(_A)
class _VmMacAddress_Type(OctetString):defaultValue=OctetString('')
_VmMacAddress_Type.__name__=_E
_VmMacAddress_Object=MibTableColumn
vmMacAddress=_VmMacAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,550),_VmMacAddress_Type())
vmMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:vmMacAddress.setStatus(_A)
class _VmNetworkAdapter_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('e1000',100),(_L,200)))
_VmNetworkAdapter_Type.__name__=_B
_VmNetworkAdapter_Object=MibTableColumn
vmNetworkAdapter=_VmNetworkAdapter_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,560),_VmNetworkAdapter_Type())
vmNetworkAdapter.setMaxAccess(_D)
if mibBuilder.loadTexts:vmNetworkAdapter.setStatus(_A)
class _VmStartupType_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('manual',100),('auto',200)))
_VmStartupType_Type.__name__=_B
_VmStartupType_Object=MibTableColumn
vmStartupType=_VmStartupType_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,600),_VmStartupType_Type())
vmStartupType.setMaxAccess(_D)
if mibBuilder.loadTexts:vmStartupType.setStatus(_A)
class _VmShutdownTimeout_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_VmShutdownTimeout_Type.__name__=_G
_VmShutdownTimeout_Object=MibTableColumn
vmShutdownTimeout=_VmShutdownTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,650),_VmShutdownTimeout_Type())
vmShutdownTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:vmShutdownTimeout.setStatus(_A)
class _VmConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('valid',100),('uSBNotAvailable',200),('missingVMConfig',300),('needRestartToApplyConfig',400)))
_VmConfigStatus_Type.__name__=_B
_VmConfigStatus_Object=MibTableColumn
vmConfigStatus=_VmConfigStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,700),_VmConfigStatus_Type())
vmConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmConfigStatus.setStatus(_A)
class _VmStart_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('start',10)))
_VmStart_Type.__name__=_B
_VmStart_Object=MibTableColumn
vmStart=_VmStart_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,10000),_VmStart_Type())
vmStart.setMaxAccess(_D)
if mibBuilder.loadTexts:vmStart.setStatus(_A)
class _VmStop_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('stop',10)))
_VmStop_Type.__name__=_B
_VmStop_Object=MibTableColumn
vmStop=_VmStop_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,10010),_VmStop_Type())
vmStop.setMaxAccess(_D)
if mibBuilder.loadTexts:vmStop.setStatus(_A)
class _VmReboot_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('reboot',10)))
_VmReboot_Type.__name__=_B
_VmReboot_Object=MibTableColumn
vmReboot=_VmReboot_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,10020),_VmReboot_Type())
vmReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:vmReboot.setStatus(_A)
class _VmStartFromIsoImage_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('startFromIsoImage',10)))
_VmStartFromIsoImage_Type.__name__=_B
_VmStartFromIsoImage_Object=MibTableColumn
vmStartFromIsoImage=_VmStartFromIsoImage_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,10030),_VmStartFromIsoImage_Type())
vmStartFromIsoImage.setMaxAccess(_D)
if mibBuilder.loadTexts:vmStartFromIsoImage.setStatus(_A)
class _VmDelete_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_F,0),('delete',10)))
_VmDelete_Type.__name__=_B
_VmDelete_Object=MibTableColumn
vmDelete=_VmDelete_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,100,1,10040),_VmDelete_Type())
vmDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:vmDelete.setStatus(_A)
class _InternalVirtualSwitchEnable_Type(MxEnableState):defaultValue=0
_InternalVirtualSwitchEnable_Type.__name__=_J
_InternalVirtualSwitchEnable_Object=MibScalar
internalVirtualSwitchEnable=_InternalVirtualSwitchEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,200),_InternalVirtualSwitchEnable_Type())
internalVirtualSwitchEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:internalVirtualSwitchEnable.setStatus(_A)
class _InternalVirtualSwitchIpAddr_Type(MxIpAddrMask):defaultValue=OctetString('169.254.10.1/24')
_InternalVirtualSwitchIpAddr_Type.__name__=_K
_InternalVirtualSwitchIpAddr_Object=MibScalar
internalVirtualSwitchIpAddr=_InternalVirtualSwitchIpAddr_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,100,300),_InternalVirtualSwitchIpAddr_Type())
internalVirtualSwitchIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:internalVirtualSwitchIpAddr.setStatus(_A)
_StatusGroup_ObjectIdentity=ObjectIdentity
statusGroup=_StatusGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200))
_VmStatusTable_Object=MibTable
vmStatusTable=_VmStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200))
if mibBuilder.loadTexts:vmStatusTable.setStatus(_A)
_VmStatusEntry_Object=MibTableRow
vmStatusEntry=_VmStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1))
vmStatusEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:vmStatusEntry.setStatus(_A)
_VmStatusIdx_Type=Unsigned32
_VmStatusIdx_Object=MibTableColumn
vmStatusIdx=_VmStatusIdx_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,100),_VmStatusIdx_Type())
vmStatusIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusIdx.setStatus(_A)
_VmStatusName_Type=OctetString
_VmStatusName_Object=MibTableColumn
vmStatusName=_VmStatusName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,200),_VmStatusName_Type())
vmStatusName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusName.setStatus(_A)
_VmStatusVncDisplayId_Type=Integer32
_VmStatusVncDisplayId_Object=MibTableColumn
vmStatusVncDisplayId=_VmStatusVncDisplayId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,300),_VmStatusVncDisplayId_Type())
vmStatusVncDisplayId.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusVncDisplayId.setStatus(_A)
class _VmStatusUsbPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_I,100),('all',200)))
_VmStatusUsbPort_Type.__name__=_B
_VmStatusUsbPort_Object=MibTableColumn
vmStatusUsbPort=_VmStatusUsbPort_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,400),_VmStatusUsbPort_Type())
vmStatusUsbPort.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusUsbPort.setStatus(_A)
_VmStatusIsoName_Type=OctetString
_VmStatusIsoName_Object=MibTableColumn
vmStatusIsoName=_VmStatusIsoName_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,500),_VmStatusIsoName_Type())
vmStatusIsoName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusIsoName.setStatus(_A)
class _VmStatusMacAddress_Type(OctetString):defaultValue=OctetString('')
_VmStatusMacAddress_Type.__name__=_E
_VmStatusMacAddress_Object=MibTableColumn
vmStatusMacAddress=_VmStatusMacAddress_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,550),_VmStatusMacAddress_Type())
vmStatusMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusMacAddress.setStatus(_A)
class _VmStatusNetworkAdapter_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('e1000',100),(_L,200)))
_VmStatusNetworkAdapter_Type.__name__=_B
_VmStatusNetworkAdapter_Object=MibTableColumn
vmStatusNetworkAdapter=_VmStatusNetworkAdapter_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,560),_VmStatusNetworkAdapter_Type())
vmStatusNetworkAdapter.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusNetworkAdapter.setStatus(_A)
_VmStatusAllocatedRamMb_Type=Unsigned32
_VmStatusAllocatedRamMb_Object=MibTableColumn
vmStatusAllocatedRamMb=_VmStatusAllocatedRamMb_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,600),_VmStatusAllocatedRamMb_Type())
vmStatusAllocatedRamMb.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusAllocatedRamMb.setStatus(_A)
_VmStatusAllocatedStorageGb_Type=Unsigned32
_VmStatusAllocatedStorageGb_Object=MibTableColumn
vmStatusAllocatedStorageGb=_VmStatusAllocatedStorageGb_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,700),_VmStatusAllocatedStorageGb_Type())
vmStatusAllocatedStorageGb.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusAllocatedStorageGb.setStatus(_A)
class _VmStatusImageFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('qcow2',100),('raw',200),('unknown',300)))
_VmStatusImageFormat_Type.__name__=_B
_VmStatusImageFormat_Object=MibTableColumn
vmStatusImageFormat=_VmStatusImageFormat_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,710),_VmStatusImageFormat_Type())
vmStatusImageFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusImageFormat.setStatus(_A)
_VmStatusAllocatedNbCores_Type=Unsigned32
_VmStatusAllocatedNbCores_Object=MibTableColumn
vmStatusAllocatedNbCores=_VmStatusAllocatedNbCores_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,800),_VmStatusAllocatedNbCores_Type())
vmStatusAllocatedNbCores.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusAllocatedNbCores.setStatus(_A)
class _VmStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('stopped',100),('started',200),('starting',300),('stopping',400),('invalidConfig',500)))
_VmStatusState_Type.__name__=_B
_VmStatusState_Object=MibTableColumn
vmStatusState=_VmStatusState_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,200,1,900),_VmStatusState_Type())
vmStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:vmStatusState.setStatus(_A)
class _ConvertVmImageResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_I,100),('running',200),('success',300),('errorNotEnoughSpace',400)))
_ConvertVmImageResult_Type.__name__=_B
_ConvertVmImageResult_Object=MibScalar
convertVmImageResult=_ConvertVmImageResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,200,300),_ConvertVmImageResult_Type())
convertVmImageResult.setMaxAccess(_C)
if mibBuilder.loadTexts:convertVmImageResult.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_B
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_B
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,4500,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'vmMIB':vmMIB,'vmMIBObjects':vmMIBObjects,'configGroup':configGroup,'vmTable':vmTable,'vmEntry':vmEntry,'vmIdx':vmIdx,'vmName':vmName,'vmVncDisplayId':vmVncDisplayId,'vmUsbPort':vmUsbPort,'vmIsoName':vmIsoName,'vmMacAddress':vmMacAddress,'vmNetworkAdapter':vmNetworkAdapter,'vmStartupType':vmStartupType,'vmShutdownTimeout':vmShutdownTimeout,'vmConfigStatus':vmConfigStatus,'vmStart':vmStart,'vmStop':vmStop,'vmReboot':vmReboot,'vmStartFromIsoImage':vmStartFromIsoImage,'vmDelete':vmDelete,'internalVirtualSwitchEnable':internalVirtualSwitchEnable,'internalVirtualSwitchIpAddr':internalVirtualSwitchIpAddr,'statusGroup':statusGroup,'vmStatusTable':vmStatusTable,'vmStatusEntry':vmStatusEntry,_M:vmStatusIdx,'vmStatusName':vmStatusName,'vmStatusVncDisplayId':vmStatusVncDisplayId,'vmStatusUsbPort':vmStatusUsbPort,'vmStatusIsoName':vmStatusIsoName,'vmStatusMacAddress':vmStatusMacAddress,'vmStatusNetworkAdapter':vmStatusNetworkAdapter,'vmStatusAllocatedRamMb':vmStatusAllocatedRamMb,'vmStatusAllocatedStorageGb':vmStatusAllocatedStorageGb,'vmStatusImageFormat':vmStatusImageFormat,'vmStatusAllocatedNbCores':vmStatusAllocatedNbCores,'vmStatusState':vmStatusState,'convertVmImageResult':convertVmImageResult,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})