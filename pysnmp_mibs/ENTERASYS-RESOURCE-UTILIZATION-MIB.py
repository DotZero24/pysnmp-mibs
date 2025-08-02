_b='etsysResourceUtilizationScalarsGroup'
_a='etsysResourceUtilizationNotificationGroup'
_Z='etsysResourceUtilizationStorageGroup'
_Y='etsysResourceUtilizationProcessGroup'
_X='etsysResourceUtilizationCpuGroup'
_W='etsysResourceCpuLoad1minThresholdExceeded'
_V='etsysResource1minThreshold'
_U='etsysResourceStorageAvailable'
_T='etsysResourceStorageSize'
_S='etsysResourceStorageDescr'
_R='etsysResourceProcessLoad5min'
_Q='etsysResourceProcessLoad1min'
_P='etsysResourceProcessLoad5sec'
_O='etsysResourceProcessName'
_N='etsysResourceCpuLoad5min'
_M='etsysResourceCpuLoad5sec'
_L='ResourceUtilization'
_K='etsysResourceStorageTypeID'
_J='etsysResourceStorageType'
_I='etsysResourceProcessID'
_H='etsysResourceCpuLoad1min'
_G='etsysResourceCpuId'
_F='not-accessible'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='ENTERASYS-RESOURCE-UTILIZATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysResourceUtilizationMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,49))
if mibBuilder.loadTexts:etsysResourceUtilizationMIB.setRevisions(('2009-11-02 15:41','2004-11-30 16:33'))
class ResourceStorageType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ram',2),('flash',3),('usbFlash',4)))
class ResourceUtilization(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_EtsysResourceUtilizationObjects_ObjectIdentity=ObjectIdentity
etsysResourceUtilizationObjects=_EtsysResourceUtilizationObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,49,1))
_EtsysResourceUtilizationNotifications_ObjectIdentity=ObjectIdentity
etsysResourceUtilizationNotifications=_EtsysResourceUtilizationNotifications_ObjectIdentity((1,3,6,1,4,1,5624,1,2,49,1,0))
_EtsysResourceCpu_ObjectIdentity=ObjectIdentity
etsysResourceCpu=_EtsysResourceCpu_ObjectIdentity((1,3,6,1,4,1,5624,1,2,49,1,1))
_EtsysResourceCpuTable_Object=MibTable
etsysResourceCpuTable=_EtsysResourceCpuTable_Object((1,3,6,1,4,1,5624,1,2,49,1,1,1))
if mibBuilder.loadTexts:etsysResourceCpuTable.setStatus(_A)
_EtsysResourceCpuEntry_Object=MibTableRow
etsysResourceCpuEntry=_EtsysResourceCpuEntry_Object((1,3,6,1,4,1,5624,1,2,49,1,1,1,1))
etsysResourceCpuEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:etsysResourceCpuEntry.setStatus(_A)
_EtsysResourceCpuId_Type=Unsigned32
_EtsysResourceCpuId_Object=MibTableColumn
etsysResourceCpuId=_EtsysResourceCpuId_Object((1,3,6,1,4,1,5624,1,2,49,1,1,1,1,1),_EtsysResourceCpuId_Type())
etsysResourceCpuId.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysResourceCpuId.setStatus(_A)
_EtsysResourceCpuLoad5sec_Type=ResourceUtilization
_EtsysResourceCpuLoad5sec_Object=MibTableColumn
etsysResourceCpuLoad5sec=_EtsysResourceCpuLoad5sec_Object((1,3,6,1,4,1,5624,1,2,49,1,1,1,1,2),_EtsysResourceCpuLoad5sec_Type())
etsysResourceCpuLoad5sec.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceCpuLoad5sec.setStatus(_A)
_EtsysResourceCpuLoad1min_Type=ResourceUtilization
_EtsysResourceCpuLoad1min_Object=MibTableColumn
etsysResourceCpuLoad1min=_EtsysResourceCpuLoad1min_Object((1,3,6,1,4,1,5624,1,2,49,1,1,1,1,3),_EtsysResourceCpuLoad1min_Type())
etsysResourceCpuLoad1min.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceCpuLoad1min.setStatus(_A)
_EtsysResourceCpuLoad5min_Type=ResourceUtilization
_EtsysResourceCpuLoad5min_Object=MibTableColumn
etsysResourceCpuLoad5min=_EtsysResourceCpuLoad5min_Object((1,3,6,1,4,1,5624,1,2,49,1,1,1,1,4),_EtsysResourceCpuLoad5min_Type())
etsysResourceCpuLoad5min.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceCpuLoad5min.setStatus(_A)
_EtsysResourceProcess_ObjectIdentity=ObjectIdentity
etsysResourceProcess=_EtsysResourceProcess_ObjectIdentity((1,3,6,1,4,1,5624,1,2,49,1,2))
_EtsysResourceProcessTable_Object=MibTable
etsysResourceProcessTable=_EtsysResourceProcessTable_Object((1,3,6,1,4,1,5624,1,2,49,1,2,1))
if mibBuilder.loadTexts:etsysResourceProcessTable.setStatus(_A)
_EtsysResourceProcessEntry_Object=MibTableRow
etsysResourceProcessEntry=_EtsysResourceProcessEntry_Object((1,3,6,1,4,1,5624,1,2,49,1,2,1,1))
etsysResourceProcessEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:etsysResourceProcessEntry.setStatus(_A)
_EtsysResourceProcessID_Type=Unsigned32
_EtsysResourceProcessID_Object=MibTableColumn
etsysResourceProcessID=_EtsysResourceProcessID_Object((1,3,6,1,4,1,5624,1,2,49,1,2,1,1,1),_EtsysResourceProcessID_Type())
etsysResourceProcessID.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysResourceProcessID.setStatus(_A)
_EtsysResourceProcessName_Type=SnmpAdminString
_EtsysResourceProcessName_Object=MibTableColumn
etsysResourceProcessName=_EtsysResourceProcessName_Object((1,3,6,1,4,1,5624,1,2,49,1,2,1,1,2),_EtsysResourceProcessName_Type())
etsysResourceProcessName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceProcessName.setStatus(_A)
_EtsysResourceProcessLoad5sec_Type=ResourceUtilization
_EtsysResourceProcessLoad5sec_Object=MibTableColumn
etsysResourceProcessLoad5sec=_EtsysResourceProcessLoad5sec_Object((1,3,6,1,4,1,5624,1,2,49,1,2,1,1,3),_EtsysResourceProcessLoad5sec_Type())
etsysResourceProcessLoad5sec.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceProcessLoad5sec.setStatus(_A)
_EtsysResourceProcessLoad1min_Type=ResourceUtilization
_EtsysResourceProcessLoad1min_Object=MibTableColumn
etsysResourceProcessLoad1min=_EtsysResourceProcessLoad1min_Object((1,3,6,1,4,1,5624,1,2,49,1,2,1,1,4),_EtsysResourceProcessLoad1min_Type())
etsysResourceProcessLoad1min.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceProcessLoad1min.setStatus(_A)
_EtsysResourceProcessLoad5min_Type=ResourceUtilization
_EtsysResourceProcessLoad5min_Object=MibTableColumn
etsysResourceProcessLoad5min=_EtsysResourceProcessLoad5min_Object((1,3,6,1,4,1,5624,1,2,49,1,2,1,1,5),_EtsysResourceProcessLoad5min_Type())
etsysResourceProcessLoad5min.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceProcessLoad5min.setStatus(_A)
_EtsysResourceStorage_ObjectIdentity=ObjectIdentity
etsysResourceStorage=_EtsysResourceStorage_ObjectIdentity((1,3,6,1,4,1,5624,1,2,49,1,3))
_EtsysResourceStorageTable_Object=MibTable
etsysResourceStorageTable=_EtsysResourceStorageTable_Object((1,3,6,1,4,1,5624,1,2,49,1,3,1))
if mibBuilder.loadTexts:etsysResourceStorageTable.setStatus(_A)
_EtsysResourceStorageEntry_Object=MibTableRow
etsysResourceStorageEntry=_EtsysResourceStorageEntry_Object((1,3,6,1,4,1,5624,1,2,49,1,3,1,1))
etsysResourceStorageEntry.setIndexNames((0,_D,_E),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:etsysResourceStorageEntry.setStatus(_A)
_EtsysResourceStorageType_Type=ResourceStorageType
_EtsysResourceStorageType_Object=MibTableColumn
etsysResourceStorageType=_EtsysResourceStorageType_Object((1,3,6,1,4,1,5624,1,2,49,1,3,1,1,1),_EtsysResourceStorageType_Type())
etsysResourceStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysResourceStorageType.setStatus(_A)
_EtsysResourceStorageTypeID_Type=Unsigned32
_EtsysResourceStorageTypeID_Object=MibTableColumn
etsysResourceStorageTypeID=_EtsysResourceStorageTypeID_Object((1,3,6,1,4,1,5624,1,2,49,1,3,1,1,2),_EtsysResourceStorageTypeID_Type())
etsysResourceStorageTypeID.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysResourceStorageTypeID.setStatus(_A)
_EtsysResourceStorageDescr_Type=SnmpAdminString
_EtsysResourceStorageDescr_Object=MibTableColumn
etsysResourceStorageDescr=_EtsysResourceStorageDescr_Object((1,3,6,1,4,1,5624,1,2,49,1,3,1,1,3),_EtsysResourceStorageDescr_Type())
etsysResourceStorageDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceStorageDescr.setStatus(_A)
_EtsysResourceStorageSize_Type=Unsigned32
_EtsysResourceStorageSize_Object=MibTableColumn
etsysResourceStorageSize=_EtsysResourceStorageSize_Object((1,3,6,1,4,1,5624,1,2,49,1,3,1,1,4),_EtsysResourceStorageSize_Type())
etsysResourceStorageSize.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceStorageSize.setStatus(_A)
_EtsysResourceStorageAvailable_Type=Unsigned32
_EtsysResourceStorageAvailable_Object=MibTableColumn
etsysResourceStorageAvailable=_EtsysResourceStorageAvailable_Object((1,3,6,1,4,1,5624,1,2,49,1,3,1,1,5),_EtsysResourceStorageAvailable_Type())
etsysResourceStorageAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysResourceStorageAvailable.setStatus(_A)
_EtsysResourceScalars_ObjectIdentity=ObjectIdentity
etsysResourceScalars=_EtsysResourceScalars_ObjectIdentity((1,3,6,1,4,1,5624,1,2,49,1,4))
class _EtsysResource1minThreshold_Type(ResourceUtilization):defaultValue=800
_EtsysResource1minThreshold_Type.__name__=_L
_EtsysResource1minThreshold_Object=MibScalar
etsysResource1minThreshold=_EtsysResource1minThreshold_Object((1,3,6,1,4,1,5624,1,2,49,1,4,1),_EtsysResource1minThreshold_Type())
etsysResource1minThreshold.setMaxAccess('read-write')
if mibBuilder.loadTexts:etsysResource1minThreshold.setStatus(_A)
_EtsysResourceUtilizationConformance_ObjectIdentity=ObjectIdentity
etsysResourceUtilizationConformance=_EtsysResourceUtilizationConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,49,2))
_EtsysResourceUtilizationGroups_ObjectIdentity=ObjectIdentity
etsysResourceUtilizationGroups=_EtsysResourceUtilizationGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,49,2,1))
_EtsysResourceUtilizationCompliances_ObjectIdentity=ObjectIdentity
etsysResourceUtilizationCompliances=_EtsysResourceUtilizationCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,49,2,2))
etsysResourceUtilizationCpuGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,49,2,1,1))
etsysResourceUtilizationCpuGroup.setObjects(*((_B,_M),(_B,_H),(_B,_N)))
if mibBuilder.loadTexts:etsysResourceUtilizationCpuGroup.setStatus(_A)
etsysResourceUtilizationProcessGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,49,2,1,2))
etsysResourceUtilizationProcessGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:etsysResourceUtilizationProcessGroup.setStatus(_A)
etsysResourceUtilizationStorageGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,49,2,1,3))
etsysResourceUtilizationStorageGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:etsysResourceUtilizationStorageGroup.setStatus(_A)
etsysResourceUtilizationScalarsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,49,2,1,5))
etsysResourceUtilizationScalarsGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:etsysResourceUtilizationScalarsGroup.setStatus(_A)
etsysResourceCpuLoad1minThresholdExceeded=NotificationType((1,3,6,1,4,1,5624,1,2,49,1,0,1))
etsysResourceCpuLoad1minThresholdExceeded.setObjects((_B,_H))
if mibBuilder.loadTexts:etsysResourceCpuLoad1minThresholdExceeded.setStatus(_A)
etsysResourceUtilizationNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,49,2,1,4))
etsysResourceUtilizationNotificationGroup.setObjects((_B,_W))
if mibBuilder.loadTexts:etsysResourceUtilizationNotificationGroup.setStatus(_A)
etsysResourceUtilizationCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,49,2,2,1))
etsysResourceUtilizationCompliance.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:etsysResourceUtilizationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ResourceStorageType':ResourceStorageType,_L:ResourceUtilization,'etsysResourceUtilizationMIB':etsysResourceUtilizationMIB,'etsysResourceUtilizationObjects':etsysResourceUtilizationObjects,'etsysResourceUtilizationNotifications':etsysResourceUtilizationNotifications,_W:etsysResourceCpuLoad1minThresholdExceeded,'etsysResourceCpu':etsysResourceCpu,'etsysResourceCpuTable':etsysResourceCpuTable,'etsysResourceCpuEntry':etsysResourceCpuEntry,_G:etsysResourceCpuId,_M:etsysResourceCpuLoad5sec,_H:etsysResourceCpuLoad1min,_N:etsysResourceCpuLoad5min,'etsysResourceProcess':etsysResourceProcess,'etsysResourceProcessTable':etsysResourceProcessTable,'etsysResourceProcessEntry':etsysResourceProcessEntry,_I:etsysResourceProcessID,_O:etsysResourceProcessName,_P:etsysResourceProcessLoad5sec,_Q:etsysResourceProcessLoad1min,_R:etsysResourceProcessLoad5min,'etsysResourceStorage':etsysResourceStorage,'etsysResourceStorageTable':etsysResourceStorageTable,'etsysResourceStorageEntry':etsysResourceStorageEntry,_J:etsysResourceStorageType,_K:etsysResourceStorageTypeID,_S:etsysResourceStorageDescr,_T:etsysResourceStorageSize,_U:etsysResourceStorageAvailable,'etsysResourceScalars':etsysResourceScalars,_V:etsysResource1minThreshold,'etsysResourceUtilizationConformance':etsysResourceUtilizationConformance,'etsysResourceUtilizationGroups':etsysResourceUtilizationGroups,_X:etsysResourceUtilizationCpuGroup,_Y:etsysResourceUtilizationProcessGroup,_Z:etsysResourceUtilizationStorageGroup,_a:etsysResourceUtilizationNotificationGroup,_b:etsysResourceUtilizationScalarsGroup,'etsysResourceUtilizationCompliances':etsysResourceUtilizationCompliances,'etsysResourceUtilizationCompliance':etsysResourceUtilizationCompliance})