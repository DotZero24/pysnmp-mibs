_G='read-write'
_F='sysResCpuIndex'
_E='sysResSlotID'
_D='Integer32'
_C='SYSTEM-RESOURCE-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctResource,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctResource')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_SysResourceInstalled_ObjectIdentity=ObjectIdentity
sysResourceInstalled=_SysResourceInstalled_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,12,1))
_SysResourceCpuTable_Object=MibTable
sysResourceCpuTable=_SysResourceCpuTable_Object((1,3,6,1,4,1,52,4,1,1,12,1,1))
if mibBuilder.loadTexts:sysResourceCpuTable.setStatus(_A)
_SysResourceCpuEntry_Object=MibTableRow
sysResourceCpuEntry=_SysResourceCpuEntry_Object((1,3,6,1,4,1,52,4,1,1,12,1,1,1))
sysResourceCpuEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:sysResourceCpuEntry.setStatus(_A)
_SysResSlotID_Type=Integer32
_SysResSlotID_Object=MibTableColumn
sysResSlotID=_SysResSlotID_Object((1,3,6,1,4,1,52,4,1,1,12,1,1,1,1),_SysResSlotID_Type())
sysResSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResSlotID.setStatus(_A)
_SysResCpuIndex_Type=Integer32
_SysResCpuIndex_Object=MibTableColumn
sysResCpuIndex=_SysResCpuIndex_Object((1,3,6,1,4,1,52,4,1,1,12,1,1,1,2),_SysResCpuIndex_Type())
sysResCpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResCpuIndex.setStatus(_A)
_SysResCpuType_Type=ObjectIdentifier
_SysResCpuType_Object=MibTableColumn
sysResCpuType=_SysResCpuType_Object((1,3,6,1,4,1,52,4,1,1,12,1,1,1,3),_SysResCpuType_Type())
sysResCpuType.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResCpuType.setStatus(_A)
_SysResCpuSpeed_Type=Integer32
_SysResCpuSpeed_Object=MibTableColumn
sysResCpuSpeed=_SysResCpuSpeed_Object((1,3,6,1,4,1,52,4,1,1,12,1,1,1,4),_SysResCpuSpeed_Type())
sysResCpuSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResCpuSpeed.setStatus(_A)
_SysResCpuID_Type=Integer32
_SysResCpuID_Object=MibTableColumn
sysResCpuID=_SysResCpuID_Object((1,3,6,1,4,1,52,4,1,1,12,1,1,1,5),_SysResCpuID_Type())
sysResCpuID.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResCpuID.setStatus(_A)
_SysResInstalledLocalMemory_Type=Integer32
_SysResInstalledLocalMemory_Object=MibTableColumn
sysResInstalledLocalMemory=_SysResInstalledLocalMemory_Object((1,3,6,1,4,1,52,4,1,1,12,1,1,1,6),_SysResInstalledLocalMemory_Type())
sysResInstalledLocalMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResInstalledLocalMemory.setStatus(_A)
_SysResUsedLocalMemory_Type=Integer32
_SysResUsedLocalMemory_Object=MibTableColumn
sysResUsedLocalMemory=_SysResUsedLocalMemory_Object((1,3,6,1,4,1,52,4,1,1,12,1,1,1,7),_SysResUsedLocalMemory_Type())
sysResUsedLocalMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResUsedLocalMemory.setStatus(_A)
_SysResourceTable_Object=MibTable
sysResourceTable=_SysResourceTable_Object((1,3,6,1,4,1,52,4,1,1,12,1,2))
if mibBuilder.loadTexts:sysResourceTable.setStatus(_A)
_SysResourceEntry_Object=MibTableRow
sysResourceEntry=_SysResourceEntry_Object((1,3,6,1,4,1,52,4,1,1,12,1,2,1))
sysResourceEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:sysResourceEntry.setStatus(_A)
_SysResInstalledNvram_Type=Integer32
_SysResInstalledNvram_Object=MibTableColumn
sysResInstalledNvram=_SysResInstalledNvram_Object((1,3,6,1,4,1,52,4,1,1,12,1,2,1,1),_SysResInstalledNvram_Type())
sysResInstalledNvram.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResInstalledNvram.setStatus(_A)
_SysResInstalledFlash_Type=Integer32
_SysResInstalledFlash_Object=MibTableColumn
sysResInstalledFlash=_SysResInstalledFlash_Object((1,3,6,1,4,1,52,4,1,1,12,1,2,1,2),_SysResInstalledFlash_Type())
sysResInstalledFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResInstalledFlash.setStatus(_A)
_SysResInstalledSharedMemory_Type=Integer32
_SysResInstalledSharedMemory_Object=MibTableColumn
sysResInstalledSharedMemory=_SysResInstalledSharedMemory_Object((1,3,6,1,4,1,52,4,1,1,12,1,2,1,3),_SysResInstalledSharedMemory_Type())
sysResInstalledSharedMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResInstalledSharedMemory.setStatus(_A)
_SysResUsedNvram_Type=Integer32
_SysResUsedNvram_Object=MibTableColumn
sysResUsedNvram=_SysResUsedNvram_Object((1,3,6,1,4,1,52,4,1,1,12,1,2,1,4),_SysResUsedNvram_Type())
sysResUsedNvram.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResUsedNvram.setStatus(_A)
_SysResUsedFlash_Type=Integer32
_SysResUsedFlash_Object=MibTableColumn
sysResUsedFlash=_SysResUsedFlash_Object((1,3,6,1,4,1,52,4,1,1,12,1,2,1,5),_SysResUsedFlash_Type())
sysResUsedFlash.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResUsedFlash.setStatus(_A)
_SysResUsedSharedMemory_Type=Integer32
_SysResUsedSharedMemory_Object=MibTableColumn
sysResUsedSharedMemory=_SysResUsedSharedMemory_Object((1,3,6,1,4,1,52,4,1,1,12,1,2,1,6),_SysResUsedSharedMemory_Type())
sysResUsedSharedMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:sysResUsedSharedMemory.setStatus(_A)
_SysResourceSwitch_ObjectIdentity=ObjectIdentity
sysResourceSwitch=_SysResourceSwitch_ObjectIdentity((1,3,6,1,4,1,52,4,1,1,12,2))
class _SysResManagementCpuResource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('limited',2),('full',3)))
_SysResManagementCpuResource_Type.__name__=_D
_SysResManagementCpuResource_Object=MibScalar
sysResManagementCpuResource=_SysResManagementCpuResource_Object((1,3,6,1,4,1,52,4,1,1,12,2,1),_SysResManagementCpuResource_Type())
sysResManagementCpuResource.setMaxAccess(_G)
if mibBuilder.loadTexts:sysResManagementCpuResource.setStatus(_A)
_SwitchLoad_Type=Integer32
_SwitchLoad_Object=MibScalar
switchLoad=_SwitchLoad_Object((1,3,6,1,4,1,52,4,1,1,12,2,2),_SwitchLoad_Type())
switchLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:switchLoad.setStatus(_A)
_PeakSwitchload_Type=Integer32
_PeakSwitchload_Object=MibScalar
peakSwitchload=_PeakSwitchload_Object((1,3,6,1,4,1,52,4,1,1,12,2,3),_PeakSwitchload_Type())
peakSwitchload.setMaxAccess(_B)
if mibBuilder.loadTexts:peakSwitchload.setStatus(_A)
_PeakSwitchLoadTime_Type=TimeTicks
_PeakSwitchLoadTime_Object=MibScalar
peakSwitchLoadTime=_PeakSwitchLoadTime_Object((1,3,6,1,4,1,52,4,1,1,12,2,4),_PeakSwitchLoadTime_Type())
peakSwitchLoadTime.setMaxAccess(_B)
if mibBuilder.loadTexts:peakSwitchLoadTime.setStatus(_A)
class _PeakSwitchClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('noClear',2)))
_PeakSwitchClear_Type.__name__=_D
_PeakSwitchClear_Object=MibScalar
peakSwitchClear=_PeakSwitchClear_Object((1,3,6,1,4,1,52,4,1,1,12,2,5),_PeakSwitchClear_Type())
peakSwitchClear.setMaxAccess(_G)
if mibBuilder.loadTexts:peakSwitchClear.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'sysResourceInstalled':sysResourceInstalled,'sysResourceCpuTable':sysResourceCpuTable,'sysResourceCpuEntry':sysResourceCpuEntry,_E:sysResSlotID,_F:sysResCpuIndex,'sysResCpuType':sysResCpuType,'sysResCpuSpeed':sysResCpuSpeed,'sysResCpuID':sysResCpuID,'sysResInstalledLocalMemory':sysResInstalledLocalMemory,'sysResUsedLocalMemory':sysResUsedLocalMemory,'sysResourceTable':sysResourceTable,'sysResourceEntry':sysResourceEntry,'sysResInstalledNvram':sysResInstalledNvram,'sysResInstalledFlash':sysResInstalledFlash,'sysResInstalledSharedMemory':sysResInstalledSharedMemory,'sysResUsedNvram':sysResUsedNvram,'sysResUsedFlash':sysResUsedFlash,'sysResUsedSharedMemory':sysResUsedSharedMemory,'sysResourceSwitch':sysResourceSwitch,'sysResManagementCpuResource':sysResManagementCpuResource,'switchLoad':switchLoad,'peakSwitchload':peakSwitchload,'peakSwitchLoadTime':peakSwitchLoadTime,'peakSwitchClear':peakSwitchClear})