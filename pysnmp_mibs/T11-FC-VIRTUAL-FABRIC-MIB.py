_g='t11vfGeneralGroup'
_f='t11vfLocallyEnabledStorageType'
_e='t11vfPortStorageType'
_d='t11vfVirtualSwitchStorageType'
_c='t11vfCoreSwitchStorageType'
_b='t11vfLocallyEnabledRowStatus'
_a='t11vfPortTaggingOperStatus'
_Z='t11vfLocallyEnabledOperStatus'
_Y='t11vfPortTaggingAdminStatus'
_X='t11vfPortVfId'
_W='t11vfVirtualSwitchRowStatus'
_V='t11vfVirtualSwitchCoreSwitchName'
_U='t11vfVirtualSwitchVfId'
_T='t11vfCoreSwitchMaxSupported'
_S='t11vfPortEntry'
_R='t11vfVirtualSwitchEntry'
_Q='t11vfLocallyEnabledVfId'
_P='t11vfLocallyEnabledPortIfIndex'
_O='t11vfCoreSwitchSwitchName'
_N='T11FabricIndex'
_M='Unsigned32'
_L='fcmInstanceIndex'
_K='FC-MGMT-MIB'
_J='off'
_I='read-only'
_H='not-accessible'
_G='FcNameIdOrZero'
_F='Integer32'
_E='read-create'
_D='read-write'
_C='StorageType'
_B='T11-FC-VIRTUAL-FABRIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
FcNameIdOrZero,fcmInstanceIndex,fcmPortEntry,fcmSwitchEntry=mibBuilder.importSymbols(_K,_G,_L,'fcmPortEntry','fcmSwitchEntry')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_C,'TextualConvention')
T11FabricIndex,=mibBuilder.importSymbols('T11-TC-MIB',_N)
t11FcVirtualFabricMIB=ModuleIdentity((1,3,6,1,2,1,147))
if mibBuilder.loadTexts:t11FcVirtualFabricMIB.setRevisions(('2006-11-10 00:00',))
_T11vfObjects_ObjectIdentity=ObjectIdentity
t11vfObjects=_T11vfObjects_ObjectIdentity((1,3,6,1,2,1,147,1))
_T11vfCoreSwitchTable_Object=MibTable
t11vfCoreSwitchTable=_T11vfCoreSwitchTable_Object((1,3,6,1,2,1,147,1,1))
if mibBuilder.loadTexts:t11vfCoreSwitchTable.setStatus(_A)
_T11vfCoreSwitchEntry_Object=MibTableRow
t11vfCoreSwitchEntry=_T11vfCoreSwitchEntry_Object((1,3,6,1,2,1,147,1,1,1))
t11vfCoreSwitchEntry.setIndexNames((0,_K,_L),(0,_B,_O))
if mibBuilder.loadTexts:t11vfCoreSwitchEntry.setStatus(_A)
class _T11vfCoreSwitchSwitchName_Type(FcNameIdOrZero):subtypeSpec=FcNameIdOrZero.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(16,16))
_T11vfCoreSwitchSwitchName_Type.__name__=_G
_T11vfCoreSwitchSwitchName_Object=MibTableColumn
t11vfCoreSwitchSwitchName=_T11vfCoreSwitchSwitchName_Object((1,3,6,1,2,1,147,1,1,1,1),_T11vfCoreSwitchSwitchName_Type())
t11vfCoreSwitchSwitchName.setMaxAccess(_H)
if mibBuilder.loadTexts:t11vfCoreSwitchSwitchName.setStatus(_A)
class _T11vfCoreSwitchMaxSupported_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_T11vfCoreSwitchMaxSupported_Type.__name__=_M
_T11vfCoreSwitchMaxSupported_Object=MibTableColumn
t11vfCoreSwitchMaxSupported=_T11vfCoreSwitchMaxSupported_Object((1,3,6,1,2,1,147,1,1,1,2),_T11vfCoreSwitchMaxSupported_Type())
t11vfCoreSwitchMaxSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:t11vfCoreSwitchMaxSupported.setStatus(_A)
class _T11vfCoreSwitchStorageType_Type(StorageType):defaultValue=3
_T11vfCoreSwitchStorageType_Type.__name__=_C
_T11vfCoreSwitchStorageType_Object=MibTableColumn
t11vfCoreSwitchStorageType=_T11vfCoreSwitchStorageType_Object((1,3,6,1,2,1,147,1,1,1,3),_T11vfCoreSwitchStorageType_Type())
t11vfCoreSwitchStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:t11vfCoreSwitchStorageType.setStatus(_A)
_T11vfVirtualSwitchTable_Object=MibTable
t11vfVirtualSwitchTable=_T11vfVirtualSwitchTable_Object((1,3,6,1,2,1,147,1,2))
if mibBuilder.loadTexts:t11vfVirtualSwitchTable.setStatus(_A)
_T11vfVirtualSwitchEntry_Object=MibTableRow
t11vfVirtualSwitchEntry=_T11vfVirtualSwitchEntry_Object((1,3,6,1,2,1,147,1,2,1))
if mibBuilder.loadTexts:t11vfVirtualSwitchEntry.setStatus(_A)
_T11vfVirtualSwitchVfId_Type=T11FabricIndex
_T11vfVirtualSwitchVfId_Object=MibTableColumn
t11vfVirtualSwitchVfId=_T11vfVirtualSwitchVfId_Object((1,3,6,1,2,1,147,1,2,1,1),_T11vfVirtualSwitchVfId_Type())
t11vfVirtualSwitchVfId.setMaxAccess(_E)
if mibBuilder.loadTexts:t11vfVirtualSwitchVfId.setStatus(_A)
class _T11vfVirtualSwitchCoreSwitchName_Type(FcNameIdOrZero):subtypeSpec=FcNameIdOrZero.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(16,16))
_T11vfVirtualSwitchCoreSwitchName_Type.__name__=_G
_T11vfVirtualSwitchCoreSwitchName_Object=MibTableColumn
t11vfVirtualSwitchCoreSwitchName=_T11vfVirtualSwitchCoreSwitchName_Object((1,3,6,1,2,1,147,1,2,1,2),_T11vfVirtualSwitchCoreSwitchName_Type())
t11vfVirtualSwitchCoreSwitchName.setMaxAccess(_I)
if mibBuilder.loadTexts:t11vfVirtualSwitchCoreSwitchName.setStatus(_A)
_T11vfVirtualSwitchRowStatus_Type=RowStatus
_T11vfVirtualSwitchRowStatus_Object=MibTableColumn
t11vfVirtualSwitchRowStatus=_T11vfVirtualSwitchRowStatus_Object((1,3,6,1,2,1,147,1,2,1,3),_T11vfVirtualSwitchRowStatus_Type())
t11vfVirtualSwitchRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:t11vfVirtualSwitchRowStatus.setStatus(_A)
class _T11vfVirtualSwitchStorageType_Type(StorageType):defaultValue=3
_T11vfVirtualSwitchStorageType_Type.__name__=_C
_T11vfVirtualSwitchStorageType_Object=MibTableColumn
t11vfVirtualSwitchStorageType=_T11vfVirtualSwitchStorageType_Object((1,3,6,1,2,1,147,1,2,1,4),_T11vfVirtualSwitchStorageType_Type())
t11vfVirtualSwitchStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:t11vfVirtualSwitchStorageType.setStatus(_A)
_T11vfPortTable_Object=MibTable
t11vfPortTable=_T11vfPortTable_Object((1,3,6,1,2,1,147,1,3))
if mibBuilder.loadTexts:t11vfPortTable.setStatus(_A)
_T11vfPortEntry_Object=MibTableRow
t11vfPortEntry=_T11vfPortEntry_Object((1,3,6,1,2,1,147,1,3,1))
if mibBuilder.loadTexts:t11vfPortEntry.setStatus(_A)
class _T11vfPortVfId_Type(T11FabricIndex):defaultValue=1
_T11vfPortVfId_Type.__name__=_N
_T11vfPortVfId_Object=MibTableColumn
t11vfPortVfId=_T11vfPortVfId_Object((1,3,6,1,2,1,147,1,3,1,1),_T11vfPortVfId_Type())
t11vfPortVfId.setMaxAccess(_D)
if mibBuilder.loadTexts:t11vfPortVfId.setStatus(_A)
class _T11vfPortTaggingAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('on',2),('auto',3)))
_T11vfPortTaggingAdminStatus_Type.__name__=_F
_T11vfPortTaggingAdminStatus_Object=MibTableColumn
t11vfPortTaggingAdminStatus=_T11vfPortTaggingAdminStatus_Object((1,3,6,1,2,1,147,1,3,1,2),_T11vfPortTaggingAdminStatus_Type())
t11vfPortTaggingAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:t11vfPortTaggingAdminStatus.setStatus(_A)
class _T11vfPortTaggingOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('on',2)))
_T11vfPortTaggingOperStatus_Type.__name__=_F
_T11vfPortTaggingOperStatus_Object=MibTableColumn
t11vfPortTaggingOperStatus=_T11vfPortTaggingOperStatus_Object((1,3,6,1,2,1,147,1,3,1,3),_T11vfPortTaggingOperStatus_Type())
t11vfPortTaggingOperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:t11vfPortTaggingOperStatus.setStatus(_A)
class _T11vfPortStorageType_Type(StorageType):defaultValue=3
_T11vfPortStorageType_Type.__name__=_C
_T11vfPortStorageType_Object=MibTableColumn
t11vfPortStorageType=_T11vfPortStorageType_Object((1,3,6,1,2,1,147,1,3,1,4),_T11vfPortStorageType_Type())
t11vfPortStorageType.setMaxAccess(_D)
if mibBuilder.loadTexts:t11vfPortStorageType.setStatus(_A)
_T11vfLocallyEnabledTable_Object=MibTable
t11vfLocallyEnabledTable=_T11vfLocallyEnabledTable_Object((1,3,6,1,2,1,147,1,4))
if mibBuilder.loadTexts:t11vfLocallyEnabledTable.setStatus(_A)
_T11vfLocallyEnabledEntry_Object=MibTableRow
t11vfLocallyEnabledEntry=_T11vfLocallyEnabledEntry_Object((1,3,6,1,2,1,147,1,4,1))
t11vfLocallyEnabledEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:t11vfLocallyEnabledEntry.setStatus(_A)
_T11vfLocallyEnabledPortIfIndex_Type=InterfaceIndex
_T11vfLocallyEnabledPortIfIndex_Object=MibTableColumn
t11vfLocallyEnabledPortIfIndex=_T11vfLocallyEnabledPortIfIndex_Object((1,3,6,1,2,1,147,1,4,1,1),_T11vfLocallyEnabledPortIfIndex_Type())
t11vfLocallyEnabledPortIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:t11vfLocallyEnabledPortIfIndex.setStatus(_A)
_T11vfLocallyEnabledVfId_Type=T11FabricIndex
_T11vfLocallyEnabledVfId_Object=MibTableColumn
t11vfLocallyEnabledVfId=_T11vfLocallyEnabledVfId_Object((1,3,6,1,2,1,147,1,4,1,2),_T11vfLocallyEnabledVfId_Type())
t11vfLocallyEnabledVfId.setMaxAccess(_H)
if mibBuilder.loadTexts:t11vfLocallyEnabledVfId.setStatus(_A)
class _T11vfLocallyEnabledOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('on',2)))
_T11vfLocallyEnabledOperStatus_Type.__name__=_F
_T11vfLocallyEnabledOperStatus_Object=MibTableColumn
t11vfLocallyEnabledOperStatus=_T11vfLocallyEnabledOperStatus_Object((1,3,6,1,2,1,147,1,4,1,3),_T11vfLocallyEnabledOperStatus_Type())
t11vfLocallyEnabledOperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:t11vfLocallyEnabledOperStatus.setStatus(_A)
_T11vfLocallyEnabledRowStatus_Type=RowStatus
_T11vfLocallyEnabledRowStatus_Object=MibTableColumn
t11vfLocallyEnabledRowStatus=_T11vfLocallyEnabledRowStatus_Object((1,3,6,1,2,1,147,1,4,1,4),_T11vfLocallyEnabledRowStatus_Type())
t11vfLocallyEnabledRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:t11vfLocallyEnabledRowStatus.setStatus(_A)
class _T11vfLocallyEnabledStorageType_Type(StorageType):defaultValue=3
_T11vfLocallyEnabledStorageType_Type.__name__=_C
_T11vfLocallyEnabledStorageType_Object=MibTableColumn
t11vfLocallyEnabledStorageType=_T11vfLocallyEnabledStorageType_Object((1,3,6,1,2,1,147,1,4,1,5),_T11vfLocallyEnabledStorageType_Type())
t11vfLocallyEnabledStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:t11vfLocallyEnabledStorageType.setStatus(_A)
_T11vfConformance_ObjectIdentity=ObjectIdentity
t11vfConformance=_T11vfConformance_ObjectIdentity((1,3,6,1,2,1,147,2))
_T11vfMIBCompliances_ObjectIdentity=ObjectIdentity
t11vfMIBCompliances=_T11vfMIBCompliances_ObjectIdentity((1,3,6,1,2,1,147,2,1))
_T11vfMIBGroups_ObjectIdentity=ObjectIdentity
t11vfMIBGroups=_T11vfMIBGroups_ObjectIdentity((1,3,6,1,2,1,147,2,2))
fcmSwitchEntry.registerAugmentions((_B,_R))
t11vfVirtualSwitchEntry.setIndexNames(*fcmSwitchEntry.getIndexNames())
fcmPortEntry.registerAugmentions((_B,_S))
t11vfPortEntry.setIndexNames(*fcmPortEntry.getIndexNames())
t11vfGeneralGroup=ObjectGroup((1,3,6,1,2,1,147,2,2,1))
t11vfGeneralGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:t11vfGeneralGroup.setStatus(_A)
t11vfMIBCompliance=ModuleCompliance((1,3,6,1,2,1,147,2,1,1))
t11vfMIBCompliance.setObjects((_B,_g))
if mibBuilder.loadTexts:t11vfMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'t11FcVirtualFabricMIB':t11FcVirtualFabricMIB,'t11vfObjects':t11vfObjects,'t11vfCoreSwitchTable':t11vfCoreSwitchTable,'t11vfCoreSwitchEntry':t11vfCoreSwitchEntry,_O:t11vfCoreSwitchSwitchName,_T:t11vfCoreSwitchMaxSupported,_c:t11vfCoreSwitchStorageType,'t11vfVirtualSwitchTable':t11vfVirtualSwitchTable,_R:t11vfVirtualSwitchEntry,_U:t11vfVirtualSwitchVfId,_V:t11vfVirtualSwitchCoreSwitchName,_W:t11vfVirtualSwitchRowStatus,_d:t11vfVirtualSwitchStorageType,'t11vfPortTable':t11vfPortTable,_S:t11vfPortEntry,_X:t11vfPortVfId,_Y:t11vfPortTaggingAdminStatus,_a:t11vfPortTaggingOperStatus,_e:t11vfPortStorageType,'t11vfLocallyEnabledTable':t11vfLocallyEnabledTable,'t11vfLocallyEnabledEntry':t11vfLocallyEnabledEntry,_P:t11vfLocallyEnabledPortIfIndex,_Q:t11vfLocallyEnabledVfId,_Z:t11vfLocallyEnabledOperStatus,_b:t11vfLocallyEnabledRowStatus,_f:t11vfLocallyEnabledStorageType,'t11vfConformance':t11vfConformance,'t11vfMIBCompliances':t11vfMIBCompliances,'t11vfMIBCompliance':t11vfMIBCompliance,'t11vfMIBGroups':t11vfMIBGroups,_g:t11vfGeneralGroup})