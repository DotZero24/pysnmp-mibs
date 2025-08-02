_R='vmwResourceGroup'
_Q='vmwHbaPci'
_P='vmwHbaDriverName'
_O='vmwHbaModelName'
_N='vmwHbaStatus'
_M='vmwHbaBusNumber'
_L='vmwHbaDeviceName'
_K='vmwHostBusAdapterNumber'
_J='vmwMemAvail'
_I='vmwMemCOS'
_H='vmwMemSize'
_G='vmwNumCPUs'
_F='vmwHostBusAdapterIndex'
_E='kilobytes'
_D='Integer32'
_C='read-only'
_B='VMWARE-RESOURCES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwResources,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwResources')
VmwSubsystemStatus,=mibBuilder.importSymbols('VMWARE-TC-MIB','VmwSubsystemStatus')
vmwResourcesMIB=ModuleIdentity((1,3,6,1,4,1,6876,3,10))
if mibBuilder.loadTexts:vmwResourcesMIB.setRevisions(('2008-10-15 00:00','2007-12-27 00:00'))
_VmwCPU_ObjectIdentity=ObjectIdentity
vmwCPU=_VmwCPU_ObjectIdentity((1,3,6,1,4,1,6876,3,1))
if mibBuilder.loadTexts:vmwCPU.setStatus(_A)
_VmwNumCPUs_Type=Gauge32
_VmwNumCPUs_Object=MibScalar
vmwNumCPUs=_VmwNumCPUs_Object((1,3,6,1,4,1,6876,3,1,1),_VmwNumCPUs_Type())
vmwNumCPUs.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNumCPUs.setStatus(_A)
_VmwMemory_ObjectIdentity=ObjectIdentity
vmwMemory=_VmwMemory_ObjectIdentity((1,3,6,1,4,1,6876,3,2))
_VmwMemSize_Type=Gauge32
_VmwMemSize_Object=MibScalar
vmwMemSize=_VmwMemSize_Object((1,3,6,1,4,1,6876,3,2,1),_VmwMemSize_Type())
vmwMemSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwMemSize.setStatus(_A)
if mibBuilder.loadTexts:vmwMemSize.setUnits(_E)
_VmwMemCOS_Type=Gauge32
_VmwMemCOS_Object=MibScalar
vmwMemCOS=_VmwMemCOS_Object((1,3,6,1,4,1,6876,3,2,2),_VmwMemCOS_Type())
vmwMemCOS.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwMemCOS.setStatus(_A)
if mibBuilder.loadTexts:vmwMemCOS.setUnits(_E)
_VmwMemAvail_Type=Gauge32
_VmwMemAvail_Object=MibScalar
vmwMemAvail=_VmwMemAvail_Object((1,3,6,1,4,1,6876,3,2,3),_VmwMemAvail_Type())
vmwMemAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwMemAvail.setStatus(_A)
if mibBuilder.loadTexts:vmwMemAvail.setUnits(_E)
_VmwStorage_ObjectIdentity=ObjectIdentity
vmwStorage=_VmwStorage_ObjectIdentity((1,3,6,1,4,1,6876,3,5))
_VmwHostBusAdapterNumber_Type=Integer32
_VmwHostBusAdapterNumber_Object=MibScalar
vmwHostBusAdapterNumber=_VmwHostBusAdapterNumber_Object((1,3,6,1,4,1,6876,3,5,1),_VmwHostBusAdapterNumber_Type())
vmwHostBusAdapterNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHostBusAdapterNumber.setStatus(_A)
_VmwHostBusAdapterTable_Object=MibTable
vmwHostBusAdapterTable=_VmwHostBusAdapterTable_Object((1,3,6,1,4,1,6876,3,5,2))
if mibBuilder.loadTexts:vmwHostBusAdapterTable.setStatus(_A)
_VmwHostBusAdapterEntry_Object=MibTableRow
vmwHostBusAdapterEntry=_VmwHostBusAdapterEntry_Object((1,3,6,1,4,1,6876,3,5,2,1))
vmwHostBusAdapterEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:vmwHostBusAdapterEntry.setStatus(_A)
class _VmwHostBusAdapterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_VmwHostBusAdapterIndex_Type.__name__=_D
_VmwHostBusAdapterIndex_Object=MibTableColumn
vmwHostBusAdapterIndex=_VmwHostBusAdapterIndex_Object((1,3,6,1,4,1,6876,3,5,2,1,1),_VmwHostBusAdapterIndex_Type())
vmwHostBusAdapterIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vmwHostBusAdapterIndex.setStatus(_A)
_VmwHbaDeviceName_Type=DisplayString
_VmwHbaDeviceName_Object=MibTableColumn
vmwHbaDeviceName=_VmwHbaDeviceName_Object((1,3,6,1,4,1,6876,3,5,2,1,2),_VmwHbaDeviceName_Type())
vmwHbaDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaDeviceName.setStatus(_A)
class _VmwHbaBusNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,1023))
_VmwHbaBusNumber_Type.__name__=_D
_VmwHbaBusNumber_Object=MibTableColumn
vmwHbaBusNumber=_VmwHbaBusNumber_Object((1,3,6,1,4,1,6876,3,5,2,1,3),_VmwHbaBusNumber_Type())
vmwHbaBusNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaBusNumber.setStatus(_A)
_VmwHbaStatus_Type=VmwSubsystemStatus
_VmwHbaStatus_Object=MibTableColumn
vmwHbaStatus=_VmwHbaStatus_Object((1,3,6,1,4,1,6876,3,5,2,1,4),_VmwHbaStatus_Type())
vmwHbaStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaStatus.setStatus(_A)
_VmwHbaModelName_Type=DisplayString
_VmwHbaModelName_Object=MibTableColumn
vmwHbaModelName=_VmwHbaModelName_Object((1,3,6,1,4,1,6876,3,5,2,1,5),_VmwHbaModelName_Type())
vmwHbaModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaModelName.setStatus(_A)
_VmwHbaDriverName_Type=DisplayString
_VmwHbaDriverName_Object=MibTableColumn
vmwHbaDriverName=_VmwHbaDriverName_Object((1,3,6,1,4,1,6876,3,5,2,1,6),_VmwHbaDriverName_Type())
vmwHbaDriverName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaDriverName.setStatus(_A)
_VmwHbaPci_Type=DisplayString
_VmwHbaPci_Object=MibTableColumn
vmwHbaPci=_VmwHbaPci_Object((1,3,6,1,4,1,6876,3,5,2,1,7),_VmwHbaPci_Type())
vmwHbaPci.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaPci.setStatus(_A)
_VmwResourceMIBConformance_ObjectIdentity=ObjectIdentity
vmwResourceMIBConformance=_VmwResourceMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,3,10,2))
_VmwResourceMIBCompliances_ObjectIdentity=ObjectIdentity
vmwResourceMIBCompliances=_VmwResourceMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,3,10,2,1))
_VmwResMIBGroups_ObjectIdentity=ObjectIdentity
vmwResMIBGroups=_VmwResMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,3,10,2,2))
vmwResourceGroup=ObjectGroup((1,3,6,1,4,1,6876,3,10,2,2,1))
vmwResourceGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:vmwResourceGroup.setStatus(_A)
vmwResourceMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6876,3,10,2,1,2))
vmwResourceMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:vmwResourceMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vmwCPU':vmwCPU,_G:vmwNumCPUs,'vmwMemory':vmwMemory,_H:vmwMemSize,_I:vmwMemCOS,_J:vmwMemAvail,'vmwStorage':vmwStorage,_K:vmwHostBusAdapterNumber,'vmwHostBusAdapterTable':vmwHostBusAdapterTable,'vmwHostBusAdapterEntry':vmwHostBusAdapterEntry,_F:vmwHostBusAdapterIndex,_L:vmwHbaDeviceName,_M:vmwHbaBusNumber,_N:vmwHbaStatus,_O:vmwHbaModelName,_P:vmwHbaDriverName,_Q:vmwHbaPci,'vmwResourcesMIB':vmwResourcesMIB,'vmwResourceMIBConformance':vmwResourceMIBConformance,'vmwResourceMIBCompliances':vmwResourceMIBCompliances,'vmwResourceMIBCompliance':vmwResourceMIBCompliance,'vmwResMIBGroups':vmwResMIBGroups,_R:vmwResourceGroup})