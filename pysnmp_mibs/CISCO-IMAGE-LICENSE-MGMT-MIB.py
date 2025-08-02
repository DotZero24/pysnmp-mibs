_a='cilmOperGroup'
_Z='cilmNotifGroup'
_Y='cilmAdminGroup'
_X='cilmBootImageLevelChanged'
_W='cilmImageLicensePriority'
_V='cilmImageLicenseName'
_U='cilmImageLicenseImageLevel'
_T='cilmImageLevelChangedNotif'
_S='cilmEULAAccepted'
_R='cilmNextBootLicenseIndex'
_Q='cilmNextBootLicenseStoreIndex'
_P='cilmCurrentLicenseIndex'
_O='cilmCurrentLicenseStoreIndex'
_N='cilmNextBootImageLevel'
_M='cilmImageLicenseMapIndex'
_L='not-accessible'
_K='Unsigned32'
_J='cilmConfiguredBootImageLevel'
_I='cilmCurrentImageLevel'
_H='read-write'
_G='cilmModuleName'
_F='TruthValue'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='CISCO-IMAGE-LICENSE-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
ciscoImageLicenseMgmtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,640))
if mibBuilder.loadTexts:ciscoImageLicenseMgmtMIB.setRevisions(('2007-10-16 00:00',))
class BootImageLevel(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class LicenseNameList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CiscoImageLicenseMgmtMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoImageLicenseMgmtMIBNotifs=_CiscoImageLicenseMgmtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,640,0))
_CiscoImageLicenseMgmtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoImageLicenseMgmtMIBObjects=_CiscoImageLicenseMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,640,1))
_CilmBootImageLevelTable_Object=MibTable
cilmBootImageLevelTable=_CilmBootImageLevelTable_Object((1,3,6,1,4,1,9,9,640,1,1))
if mibBuilder.loadTexts:cilmBootImageLevelTable.setStatus(_A)
_CilmBootImageLevelEntry_Object=MibTableRow
cilmBootImageLevelEntry=_CilmBootImageLevelEntry_Object((1,3,6,1,4,1,9,9,640,1,1,1))
cilmBootImageLevelEntry.setIndexNames((0,_D,_E),(0,_B,_G))
if mibBuilder.loadTexts:cilmBootImageLevelEntry.setStatus(_A)
_CilmModuleName_Type=SnmpAdminString
_CilmModuleName_Object=MibTableColumn
cilmModuleName=_CilmModuleName_Object((1,3,6,1,4,1,9,9,640,1,1,1,1),_CilmModuleName_Type())
cilmModuleName.setMaxAccess(_L)
if mibBuilder.loadTexts:cilmModuleName.setStatus(_A)
_CilmCurrentImageLevel_Type=BootImageLevel
_CilmCurrentImageLevel_Object=MibTableColumn
cilmCurrentImageLevel=_CilmCurrentImageLevel_Object((1,3,6,1,4,1,9,9,640,1,1,1,2),_CilmCurrentImageLevel_Type())
cilmCurrentImageLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cilmCurrentImageLevel.setStatus(_A)
_CilmConfiguredBootImageLevel_Type=BootImageLevel
_CilmConfiguredBootImageLevel_Object=MibTableColumn
cilmConfiguredBootImageLevel=_CilmConfiguredBootImageLevel_Object((1,3,6,1,4,1,9,9,640,1,1,1,3),_CilmConfiguredBootImageLevel_Type())
cilmConfiguredBootImageLevel.setMaxAccess(_H)
if mibBuilder.loadTexts:cilmConfiguredBootImageLevel.setStatus(_A)
_CilmNextBootImageLevel_Type=BootImageLevel
_CilmNextBootImageLevel_Object=MibTableColumn
cilmNextBootImageLevel=_CilmNextBootImageLevel_Object((1,3,6,1,4,1,9,9,640,1,1,1,4),_CilmNextBootImageLevel_Type())
cilmNextBootImageLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cilmNextBootImageLevel.setStatus(_A)
_CilmCurrentLicenseStoreIndex_Type=Unsigned32
_CilmCurrentLicenseStoreIndex_Object=MibTableColumn
cilmCurrentLicenseStoreIndex=_CilmCurrentLicenseStoreIndex_Object((1,3,6,1,4,1,9,9,640,1,1,1,5),_CilmCurrentLicenseStoreIndex_Type())
cilmCurrentLicenseStoreIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cilmCurrentLicenseStoreIndex.setStatus(_A)
_CilmCurrentLicenseIndex_Type=Unsigned32
_CilmCurrentLicenseIndex_Object=MibTableColumn
cilmCurrentLicenseIndex=_CilmCurrentLicenseIndex_Object((1,3,6,1,4,1,9,9,640,1,1,1,6),_CilmCurrentLicenseIndex_Type())
cilmCurrentLicenseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cilmCurrentLicenseIndex.setStatus(_A)
_CilmNextBootLicenseStoreIndex_Type=Unsigned32
_CilmNextBootLicenseStoreIndex_Object=MibTableColumn
cilmNextBootLicenseStoreIndex=_CilmNextBootLicenseStoreIndex_Object((1,3,6,1,4,1,9,9,640,1,1,1,7),_CilmNextBootLicenseStoreIndex_Type())
cilmNextBootLicenseStoreIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cilmNextBootLicenseStoreIndex.setStatus(_A)
_CilmNextBootLicenseIndex_Type=Unsigned32
_CilmNextBootLicenseIndex_Object=MibTableColumn
cilmNextBootLicenseIndex=_CilmNextBootLicenseIndex_Object((1,3,6,1,4,1,9,9,640,1,1,1,8),_CilmNextBootLicenseIndex_Type())
cilmNextBootLicenseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cilmNextBootLicenseIndex.setStatus(_A)
_CilmImageLevelToLicenseMapTable_Object=MibTable
cilmImageLevelToLicenseMapTable=_CilmImageLevelToLicenseMapTable_Object((1,3,6,1,4,1,9,9,640,1,2))
if mibBuilder.loadTexts:cilmImageLevelToLicenseMapTable.setStatus(_A)
_CilmImageLevelToLicenseMapEntry_Object=MibTableRow
cilmImageLevelToLicenseMapEntry=_CilmImageLevelToLicenseMapEntry_Object((1,3,6,1,4,1,9,9,640,1,2,1))
cilmImageLevelToLicenseMapEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_M))
if mibBuilder.loadTexts:cilmImageLevelToLicenseMapEntry.setStatus(_A)
_CilmImageLicenseMapIndex_Type=Unsigned32
_CilmImageLicenseMapIndex_Object=MibTableColumn
cilmImageLicenseMapIndex=_CilmImageLicenseMapIndex_Object((1,3,6,1,4,1,9,9,640,1,2,1,1),_CilmImageLicenseMapIndex_Type())
cilmImageLicenseMapIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:cilmImageLicenseMapIndex.setStatus(_A)
_CilmImageLicenseImageLevel_Type=BootImageLevel
_CilmImageLicenseImageLevel_Object=MibTableColumn
cilmImageLicenseImageLevel=_CilmImageLicenseImageLevel_Object((1,3,6,1,4,1,9,9,640,1,2,1,2),_CilmImageLicenseImageLevel_Type())
cilmImageLicenseImageLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:cilmImageLicenseImageLevel.setStatus(_A)
_CilmImageLicenseName_Type=LicenseNameList
_CilmImageLicenseName_Object=MibTableColumn
cilmImageLicenseName=_CilmImageLicenseName_Object((1,3,6,1,4,1,9,9,640,1,2,1,3),_CilmImageLicenseName_Type())
cilmImageLicenseName.setMaxAccess(_C)
if mibBuilder.loadTexts:cilmImageLicenseName.setStatus(_A)
class _CilmImageLicensePriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CilmImageLicensePriority_Type.__name__=_K
_CilmImageLicensePriority_Object=MibTableColumn
cilmImageLicensePriority=_CilmImageLicensePriority_Object((1,3,6,1,4,1,9,9,640,1,2,1,4),_CilmImageLicensePriority_Type())
cilmImageLicensePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cilmImageLicensePriority.setStatus(_A)
class _CilmEULAAccepted_Type(TruthValue):defaultValue=2
_CilmEULAAccepted_Type.__name__=_F
_CilmEULAAccepted_Object=MibScalar
cilmEULAAccepted=_CilmEULAAccepted_Object((1,3,6,1,4,1,9,9,640,1,3),_CilmEULAAccepted_Type())
cilmEULAAccepted.setMaxAccess(_H)
if mibBuilder.loadTexts:cilmEULAAccepted.setStatus(_A)
_CilmNotifCntl_ObjectIdentity=ObjectIdentity
cilmNotifCntl=_CilmNotifCntl_ObjectIdentity((1,3,6,1,4,1,9,9,640,1,4))
class _CilmImageLevelChangedNotif_Type(TruthValue):defaultValue=2
_CilmImageLevelChangedNotif_Type.__name__=_F
_CilmImageLevelChangedNotif_Object=MibScalar
cilmImageLevelChangedNotif=_CilmImageLevelChangedNotif_Object((1,3,6,1,4,1,9,9,640,1,4,1),_CilmImageLevelChangedNotif_Type())
cilmImageLevelChangedNotif.setMaxAccess(_H)
if mibBuilder.loadTexts:cilmImageLevelChangedNotif.setStatus(_A)
_CiscoImageLicenseMgmtMIBConform_ObjectIdentity=ObjectIdentity
ciscoImageLicenseMgmtMIBConform=_CiscoImageLicenseMgmtMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,640,2))
_CilmModuleCompliances_ObjectIdentity=ObjectIdentity
cilmModuleCompliances=_CilmModuleCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,640,2,1))
_CilmModuleGroups_ObjectIdentity=ObjectIdentity
cilmModuleGroups=_CilmModuleGroups_ObjectIdentity((1,3,6,1,4,1,9,9,640,2,2))
cilmAdminGroup=ObjectGroup((1,3,6,1,4,1,9,9,640,2,2,1))
cilmAdminGroup.setObjects(*((_B,_I),(_B,_J),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cilmAdminGroup.setStatus(_A)
cilmOperGroup=ObjectGroup((1,3,6,1,4,1,9,9,640,2,2,2))
cilmOperGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cilmOperGroup.setStatus(_A)
cilmBootImageLevelChanged=NotificationType((1,3,6,1,4,1,9,9,640,0,1))
cilmBootImageLevelChanged.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cilmBootImageLevelChanged.setStatus(_A)
cilmNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,640,2,2,3))
cilmNotifGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:cilmNotifGroup.setStatus(_A)
cilmModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,640,2,1,1))
cilmModuleCompliance.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cilmModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'BootImageLevel':BootImageLevel,'LicenseNameList':LicenseNameList,'ciscoImageLicenseMgmtMIB':ciscoImageLicenseMgmtMIB,'ciscoImageLicenseMgmtMIBNotifs':ciscoImageLicenseMgmtMIBNotifs,_X:cilmBootImageLevelChanged,'ciscoImageLicenseMgmtMIBObjects':ciscoImageLicenseMgmtMIBObjects,'cilmBootImageLevelTable':cilmBootImageLevelTable,'cilmBootImageLevelEntry':cilmBootImageLevelEntry,_G:cilmModuleName,_I:cilmCurrentImageLevel,_J:cilmConfiguredBootImageLevel,_N:cilmNextBootImageLevel,_O:cilmCurrentLicenseStoreIndex,_P:cilmCurrentLicenseIndex,_Q:cilmNextBootLicenseStoreIndex,_R:cilmNextBootLicenseIndex,'cilmImageLevelToLicenseMapTable':cilmImageLevelToLicenseMapTable,'cilmImageLevelToLicenseMapEntry':cilmImageLevelToLicenseMapEntry,_M:cilmImageLicenseMapIndex,_U:cilmImageLicenseImageLevel,_V:cilmImageLicenseName,_W:cilmImageLicensePriority,_S:cilmEULAAccepted,'cilmNotifCntl':cilmNotifCntl,_T:cilmImageLevelChangedNotif,'ciscoImageLicenseMgmtMIBConform':ciscoImageLicenseMgmtMIBConform,'cilmModuleCompliances':cilmModuleCompliances,'cilmModuleCompliance':cilmModuleCompliance,'cilmModuleGroups':cilmModuleGroups,_Y:cilmAdminGroup,_a:cilmOperGroup,_Z:cilmNotifGroup})