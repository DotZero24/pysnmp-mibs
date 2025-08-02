_F='oacExpIMSysHwcIndex'
_E='oacSysCpuUsedIndex'
_D='ONEACCESS-SYS-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oacExpIMSystem,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMSystem','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
oacSysMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,671))
if mibBuilder.loadTexts:oacSysMIBModule.setRevisions(('2014-05-05 00:01','2011-06-15 00:00','2010-12-14 00:01','2010-08-11 10:00','2010-07-08 10:00'))
class OASysHwcClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('board',0),('cpu',1),('slot',2)))
class OASysHwcType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('mainboard',0),('microprocessor',1),('ram',2),('flash',3),('dsp',4),('uplink',5),('module',6)))
class OASysCoreType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('controlplane',0),('dataforwarding',1),('application',2),('mixed',3)))
_OacExpIMSysStatistics_ObjectIdentity=ObjectIdentity
oacExpIMSysStatistics=_OacExpIMSysStatistics_ObjectIdentity((1,3,6,1,4,1,13191,10,3,3,1))
_OacSysMemStatistics_ObjectIdentity=ObjectIdentity
oacSysMemStatistics=_OacSysMemStatistics_ObjectIdentity((1,3,6,1,4,1,13191,10,3,3,1,1))
_OacSysMemoryFree_Type=Unsigned32
_OacSysMemoryFree_Object=MibScalar
oacSysMemoryFree=_OacSysMemoryFree_Object((1,3,6,1,4,1,13191,10,3,3,1,1,1),_OacSysMemoryFree_Type())
oacSysMemoryFree.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysMemoryFree.setStatus(_A)
_OacSysMemoryAllocated_Type=Unsigned32
_OacSysMemoryAllocated_Object=MibScalar
oacSysMemoryAllocated=_OacSysMemoryAllocated_Object((1,3,6,1,4,1,13191,10,3,3,1,1,2),_OacSysMemoryAllocated_Type())
oacSysMemoryAllocated.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysMemoryAllocated.setStatus(_A)
_OacSysMemoryTotal_Type=Unsigned32
_OacSysMemoryTotal_Object=MibScalar
oacSysMemoryTotal=_OacSysMemoryTotal_Object((1,3,6,1,4,1,13191,10,3,3,1,1,3),_OacSysMemoryTotal_Type())
oacSysMemoryTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysMemoryTotal.setStatus(_A)
_OacSysMemoryUsed_Type=Unsigned32
_OacSysMemoryUsed_Object=MibScalar
oacSysMemoryUsed=_OacSysMemoryUsed_Object((1,3,6,1,4,1,13191,10,3,3,1,1,4),_OacSysMemoryUsed_Type())
oacSysMemoryUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysMemoryUsed.setStatus(_A)
_OacSysCpuStatistics_ObjectIdentity=ObjectIdentity
oacSysCpuStatistics=_OacSysCpuStatistics_ObjectIdentity((1,3,6,1,4,1,13191,10,3,3,1,2))
_OacSysCpuUsed_Type=Unsigned32
_OacSysCpuUsed_Object=MibScalar
oacSysCpuUsed=_OacSysCpuUsed_Object((1,3,6,1,4,1,13191,10,3,3,1,2,1),_OacSysCpuUsed_Type())
oacSysCpuUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysCpuUsed.setStatus(_A)
_OacSysCpuUsedCoresCount_Type=Unsigned32
_OacSysCpuUsedCoresCount_Object=MibScalar
oacSysCpuUsedCoresCount=_OacSysCpuUsedCoresCount_Object((1,3,6,1,4,1,13191,10,3,3,1,2,2),_OacSysCpuUsedCoresCount_Type())
oacSysCpuUsedCoresCount.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysCpuUsedCoresCount.setStatus(_A)
_OacSysCpuUsedCoresTable_Object=MibTable
oacSysCpuUsedCoresTable=_OacSysCpuUsedCoresTable_Object((1,3,6,1,4,1,13191,10,3,3,1,2,3))
if mibBuilder.loadTexts:oacSysCpuUsedCoresTable.setStatus(_A)
_OacSysCpuUsedCoresEntry_Object=MibTableRow
oacSysCpuUsedCoresEntry=_OacSysCpuUsedCoresEntry_Object((1,3,6,1,4,1,13191,10,3,3,1,2,3,1))
oacSysCpuUsedCoresEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:oacSysCpuUsedCoresEntry.setStatus(_A)
_OacSysCpuUsedIndex_Type=Unsigned32
_OacSysCpuUsedIndex_Object=MibTableColumn
oacSysCpuUsedIndex=_OacSysCpuUsedIndex_Object((1,3,6,1,4,1,13191,10,3,3,1,2,3,1,1),_OacSysCpuUsedIndex_Type())
oacSysCpuUsedIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysCpuUsedIndex.setStatus(_A)
_OacSysCpuUsedCoreType_Type=OASysCoreType
_OacSysCpuUsedCoreType_Object=MibTableColumn
oacSysCpuUsedCoreType=_OacSysCpuUsedCoreType_Object((1,3,6,1,4,1,13191,10,3,3,1,2,3,1,2),_OacSysCpuUsedCoreType_Type())
oacSysCpuUsedCoreType.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysCpuUsedCoreType.setStatus(_A)
_OacSysCpuUsedValue_Type=Unsigned32
_OacSysCpuUsedValue_Object=MibTableColumn
oacSysCpuUsedValue=_OacSysCpuUsedValue_Object((1,3,6,1,4,1,13191,10,3,3,1,2,3,1,3),_OacSysCpuUsedValue_Type())
oacSysCpuUsedValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysCpuUsedValue.setStatus(_A)
_OacSysCpuUsedOneMinuteValue_Type=Unsigned32
_OacSysCpuUsedOneMinuteValue_Object=MibTableColumn
oacSysCpuUsedOneMinuteValue=_OacSysCpuUsedOneMinuteValue_Object((1,3,6,1,4,1,13191,10,3,3,1,2,3,1,4),_OacSysCpuUsedOneMinuteValue_Type())
oacSysCpuUsedOneMinuteValue.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysCpuUsedOneMinuteValue.setStatus(_A)
_OacSysLastRebootCause_Type=DisplayString
_OacSysLastRebootCause_Object=MibScalar
oacSysLastRebootCause=_OacSysLastRebootCause_Object((1,3,6,1,4,1,13191,10,3,3,1,3),_OacSysLastRebootCause_Type())
oacSysLastRebootCause.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysLastRebootCause.setStatus(_A)
_OacSysSecureCrashlogCount_Type=Integer32
_OacSysSecureCrashlogCount_Object=MibScalar
oacSysSecureCrashlogCount=_OacSysSecureCrashlogCount_Object((1,3,6,1,4,1,13191,10,3,3,1,100),_OacSysSecureCrashlogCount_Type())
oacSysSecureCrashlogCount.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysSecureCrashlogCount.setStatus(_A)
class _OacSysStartCaused_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSysStartCaused_Type.__name__=_C
_OacSysStartCaused_Object=MibScalar
oacSysStartCaused=_OacSysStartCaused_Object((1,3,6,1,4,1,13191,10,3,3,1,200),_OacSysStartCaused_Type())
oacSysStartCaused.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysStartCaused.setStatus(_A)
_OacExpIMSysHardwareDescription_ObjectIdentity=ObjectIdentity
oacExpIMSysHardwareDescription=_OacExpIMSysHardwareDescription_ObjectIdentity((1,3,6,1,4,1,13191,10,3,3,2))
_OacSysIMSysMainBoard_ObjectIdentity=ObjectIdentity
oacSysIMSysMainBoard=_OacSysIMSysMainBoard_ObjectIdentity((1,3,6,1,4,1,13191,10,3,3,2,1))
_OacSysIMSysMainIdentifier_Type=ObjectIdentifier
_OacSysIMSysMainIdentifier_Object=MibScalar
oacSysIMSysMainIdentifier=_OacSysIMSysMainIdentifier_Object((1,3,6,1,4,1,13191,10,3,3,2,1,1),_OacSysIMSysMainIdentifier_Type())
oacSysIMSysMainIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysIMSysMainIdentifier.setStatus(_A)
class _OacSysIMSysMainManufacturedIdentity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSysIMSysMainManufacturedIdentity_Type.__name__=_C
_OacSysIMSysMainManufacturedIdentity_Object=MibScalar
oacSysIMSysMainManufacturedIdentity=_OacSysIMSysMainManufacturedIdentity_Object((1,3,6,1,4,1,13191,10,3,3,2,1,2),_OacSysIMSysMainManufacturedIdentity_Type())
oacSysIMSysMainManufacturedIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysIMSysMainManufacturedIdentity.setStatus(_A)
class _OacSysIMSysMainManufacturedDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSysIMSysMainManufacturedDate_Type.__name__=_C
_OacSysIMSysMainManufacturedDate_Object=MibScalar
oacSysIMSysMainManufacturedDate=_OacSysIMSysMainManufacturedDate_Object((1,3,6,1,4,1,13191,10,3,3,2,1,3),_OacSysIMSysMainManufacturedDate_Type())
oacSysIMSysMainManufacturedDate.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysIMSysMainManufacturedDate.setStatus(_A)
class _OacSysIMSysMainCPU_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSysIMSysMainCPU_Type.__name__=_C
_OacSysIMSysMainCPU_Object=MibScalar
oacSysIMSysMainCPU=_OacSysIMSysMainCPU_Object((1,3,6,1,4,1,13191,10,3,3,2,1,4),_OacSysIMSysMainCPU_Type())
oacSysIMSysMainCPU.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysIMSysMainCPU.setStatus(_A)
class _OacSysIMSysMainBSPVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSysIMSysMainBSPVersion_Type.__name__=_C
_OacSysIMSysMainBSPVersion_Object=MibScalar
oacSysIMSysMainBSPVersion=_OacSysIMSysMainBSPVersion_Object((1,3,6,1,4,1,13191,10,3,3,2,1,5),_OacSysIMSysMainBSPVersion_Type())
oacSysIMSysMainBSPVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysIMSysMainBSPVersion.setStatus(_A)
class _OacSysIMSysMainBootVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSysIMSysMainBootVersion_Type.__name__=_C
_OacSysIMSysMainBootVersion_Object=MibScalar
oacSysIMSysMainBootVersion=_OacSysIMSysMainBootVersion_Object((1,3,6,1,4,1,13191,10,3,3,2,1,6),_OacSysIMSysMainBootVersion_Type())
oacSysIMSysMainBootVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysIMSysMainBootVersion.setStatus(_A)
class _OacSysIMSysMainBootDateCreation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacSysIMSysMainBootDateCreation_Type.__name__=_C
_OacSysIMSysMainBootDateCreation_Object=MibScalar
oacSysIMSysMainBootDateCreation=_OacSysIMSysMainBootDateCreation_Object((1,3,6,1,4,1,13191,10,3,3,2,1,7),_OacSysIMSysMainBootDateCreation_Type())
oacSysIMSysMainBootDateCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:oacSysIMSysMainBootDateCreation.setStatus(_A)
_OacExpIMSysHwComponents_ObjectIdentity=ObjectIdentity
oacExpIMSysHwComponents=_OacExpIMSysHwComponents_ObjectIdentity((1,3,6,1,4,1,13191,10,3,3,2,2))
_OacExpIMSysHwComponentsCount_Type=Unsigned32
_OacExpIMSysHwComponentsCount_Object=MibScalar
oacExpIMSysHwComponentsCount=_OacExpIMSysHwComponentsCount_Object((1,3,6,1,4,1,13191,10,3,3,2,2,1),_OacExpIMSysHwComponentsCount_Type())
oacExpIMSysHwComponentsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysHwComponentsCount.setStatus(_A)
_OacExpIMSysHwComponentsTable_Object=MibTable
oacExpIMSysHwComponentsTable=_OacExpIMSysHwComponentsTable_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2))
if mibBuilder.loadTexts:oacExpIMSysHwComponentsTable.setStatus(_A)
_OacExpIMSysHwComponentsEntry_Object=MibTableRow
oacExpIMSysHwComponentsEntry=_OacExpIMSysHwComponentsEntry_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2,1))
oacExpIMSysHwComponentsEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:oacExpIMSysHwComponentsEntry.setStatus(_A)
_OacExpIMSysHwcIndex_Type=Unsigned32
_OacExpIMSysHwcIndex_Object=MibTableColumn
oacExpIMSysHwcIndex=_OacExpIMSysHwcIndex_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2,1,1),_OacExpIMSysHwcIndex_Type())
oacExpIMSysHwcIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysHwcIndex.setStatus(_A)
_OacExpIMSysHwcClass_Type=OASysHwcClass
_OacExpIMSysHwcClass_Object=MibTableColumn
oacExpIMSysHwcClass=_OacExpIMSysHwcClass_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2,1,2),_OacExpIMSysHwcClass_Type())
oacExpIMSysHwcClass.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysHwcClass.setStatus(_A)
_OacExpIMSysHwcType_Type=OASysHwcType
_OacExpIMSysHwcType_Object=MibTableColumn
oacExpIMSysHwcType=_OacExpIMSysHwcType_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2,1,3),_OacExpIMSysHwcType_Type())
oacExpIMSysHwcType.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysHwcType.setStatus(_A)
_OacExpIMSysHwcDescription_Type=DisplayString
_OacExpIMSysHwcDescription_Object=MibTableColumn
oacExpIMSysHwcDescription=_OacExpIMSysHwcDescription_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2,1,4),_OacExpIMSysHwcDescription_Type())
oacExpIMSysHwcDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysHwcDescription.setStatus(_A)
_OacExpIMSysHwcSerialNumber_Type=DisplayString
_OacExpIMSysHwcSerialNumber_Object=MibTableColumn
oacExpIMSysHwcSerialNumber=_OacExpIMSysHwcSerialNumber_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2,1,5),_OacExpIMSysHwcSerialNumber_Type())
oacExpIMSysHwcSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysHwcSerialNumber.setStatus(_A)
_OacExpIMSysHwcManufacturer_Type=DisplayString
_OacExpIMSysHwcManufacturer_Object=MibTableColumn
oacExpIMSysHwcManufacturer=_OacExpIMSysHwcManufacturer_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2,1,6),_OacExpIMSysHwcManufacturer_Type())
oacExpIMSysHwcManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysHwcManufacturer.setStatus(_A)
class _OacExpIMSysHwcManufacturedDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_OacExpIMSysHwcManufacturedDate_Type.__name__=_C
_OacExpIMSysHwcManufacturedDate_Object=MibTableColumn
oacExpIMSysHwcManufacturedDate=_OacExpIMSysHwcManufacturedDate_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2,1,7),_OacExpIMSysHwcManufacturedDate_Type())
oacExpIMSysHwcManufacturedDate.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysHwcManufacturedDate.setStatus(_A)
class _OacExpIMSysHwcProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OacExpIMSysHwcProductName_Type.__name__=_C
_OacExpIMSysHwcProductName_Object=MibTableColumn
oacExpIMSysHwcProductName=_OacExpIMSysHwcProductName_Object((1,3,6,1,4,1,13191,10,3,3,2,2,2,1,8),_OacExpIMSysHwcProductName_Type())
oacExpIMSysHwcProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysHwcProductName.setStatus(_A)
_OacExpIMSysFactory_ObjectIdentity=ObjectIdentity
oacExpIMSysFactory=_OacExpIMSysFactory_ObjectIdentity((1,3,6,1,4,1,13191,10,3,3,2,3))
class _OacExpIMSysFactorySupplierID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_OacExpIMSysFactorySupplierID_Type.__name__=_C
_OacExpIMSysFactorySupplierID_Object=MibScalar
oacExpIMSysFactorySupplierID=_OacExpIMSysFactorySupplierID_Object((1,3,6,1,4,1,13191,10,3,3,2,3,1),_OacExpIMSysFactorySupplierID_Type())
oacExpIMSysFactorySupplierID.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysFactorySupplierID.setStatus(_A)
class _OacExpIMSysFactoryProductSalesCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_OacExpIMSysFactoryProductSalesCode_Type.__name__=_C
_OacExpIMSysFactoryProductSalesCode_Object=MibScalar
oacExpIMSysFactoryProductSalesCode=_OacExpIMSysFactoryProductSalesCode_Object((1,3,6,1,4,1,13191,10,3,3,2,3,2),_OacExpIMSysFactoryProductSalesCode_Type())
oacExpIMSysFactoryProductSalesCode.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysFactoryProductSalesCode.setStatus(_A)
class _OacExpIMSysFactoryHwRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,7))
_OacExpIMSysFactoryHwRevision_Type.__name__=_C
_OacExpIMSysFactoryHwRevision_Object=MibScalar
oacExpIMSysFactoryHwRevision=_OacExpIMSysFactoryHwRevision_Object((1,3,6,1,4,1,13191,10,3,3,2,3,3),_OacExpIMSysFactoryHwRevision_Type())
oacExpIMSysFactoryHwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:oacExpIMSysFactoryHwRevision.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'OASysHwcClass':OASysHwcClass,'OASysHwcType':OASysHwcType,'OASysCoreType':OASysCoreType,'oacSysMIBModule':oacSysMIBModule,'oacExpIMSysStatistics':oacExpIMSysStatistics,'oacSysMemStatistics':oacSysMemStatistics,'oacSysMemoryFree':oacSysMemoryFree,'oacSysMemoryAllocated':oacSysMemoryAllocated,'oacSysMemoryTotal':oacSysMemoryTotal,'oacSysMemoryUsed':oacSysMemoryUsed,'oacSysCpuStatistics':oacSysCpuStatistics,'oacSysCpuUsed':oacSysCpuUsed,'oacSysCpuUsedCoresCount':oacSysCpuUsedCoresCount,'oacSysCpuUsedCoresTable':oacSysCpuUsedCoresTable,'oacSysCpuUsedCoresEntry':oacSysCpuUsedCoresEntry,_E:oacSysCpuUsedIndex,'oacSysCpuUsedCoreType':oacSysCpuUsedCoreType,'oacSysCpuUsedValue':oacSysCpuUsedValue,'oacSysCpuUsedOneMinuteValue':oacSysCpuUsedOneMinuteValue,'oacSysLastRebootCause':oacSysLastRebootCause,'oacSysSecureCrashlogCount':oacSysSecureCrashlogCount,'oacSysStartCaused':oacSysStartCaused,'oacExpIMSysHardwareDescription':oacExpIMSysHardwareDescription,'oacSysIMSysMainBoard':oacSysIMSysMainBoard,'oacSysIMSysMainIdentifier':oacSysIMSysMainIdentifier,'oacSysIMSysMainManufacturedIdentity':oacSysIMSysMainManufacturedIdentity,'oacSysIMSysMainManufacturedDate':oacSysIMSysMainManufacturedDate,'oacSysIMSysMainCPU':oacSysIMSysMainCPU,'oacSysIMSysMainBSPVersion':oacSysIMSysMainBSPVersion,'oacSysIMSysMainBootVersion':oacSysIMSysMainBootVersion,'oacSysIMSysMainBootDateCreation':oacSysIMSysMainBootDateCreation,'oacExpIMSysHwComponents':oacExpIMSysHwComponents,'oacExpIMSysHwComponentsCount':oacExpIMSysHwComponentsCount,'oacExpIMSysHwComponentsTable':oacExpIMSysHwComponentsTable,'oacExpIMSysHwComponentsEntry':oacExpIMSysHwComponentsEntry,_F:oacExpIMSysHwcIndex,'oacExpIMSysHwcClass':oacExpIMSysHwcClass,'oacExpIMSysHwcType':oacExpIMSysHwcType,'oacExpIMSysHwcDescription':oacExpIMSysHwcDescription,'oacExpIMSysHwcSerialNumber':oacExpIMSysHwcSerialNumber,'oacExpIMSysHwcManufacturer':oacExpIMSysHwcManufacturer,'oacExpIMSysHwcManufacturedDate':oacExpIMSysHwcManufacturedDate,'oacExpIMSysHwcProductName':oacExpIMSysHwcProductName,'oacExpIMSysFactory':oacExpIMSysFactory,'oacExpIMSysFactorySupplierID':oacExpIMSysFactorySupplierID,'oacExpIMSysFactoryProductSalesCode':oacExpIMSysFactoryProductSalesCode,'oacExpIMSysFactoryHwRevision':oacExpIMSysFactoryHwRevision})