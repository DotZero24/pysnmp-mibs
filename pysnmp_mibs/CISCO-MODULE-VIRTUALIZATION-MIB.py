_a='cmVirtContextNotificationGroup'
_Z='cmVirtContextNotifControlGroup'
_Y='cmVirtContextIfMapGroup'
_X='cmVirtContextconfigGroup'
_W='cmVirtContextRemoved'
_V='cmVirtContextAdded'
_U='cmVirtContextNotifEnable'
_T='cmVirtContextIfMapRowStatus'
_S='cmVirtContextIfMapStorageType'
_R='cmVirtContextIfMapIdHigh'
_Q='cmVirtContextRowStatus'
_P='cmVirtContextStorageType'
_O='cmVirtContextResourceClass'
_N='cmVirtContextURL'
_M='cmVirtContextDescr'
_L='cmVirtContextIfMapIdLow'
_K='cmVirtContextIfMapType'
_J='SnmpAdminString'
_I='entPhysicalIndex'
_H='ENTITY-MIB'
_G='not-accessible'
_F='cmVirtContextName'
_E='StorageType'
_D='cmNotifVirtContextName'
_C='read-create'
_B='CISCO-MODULE-VIRTUALIZATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CiscoResourceClass,=mibBuilder.importSymbols('CISCO-L4L7MODULE-RESOURCE-LIMIT-MIB','CiscoResourceClass')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoURLString,=mibBuilder.importSymbols('CISCO-TC','CiscoURLString')
entPhysicalIndex,=mibBuilder.importSymbols(_H,_I)
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_E,'TextualConvention','TruthValue')
ciscoModuleVirtualizationMIB=ModuleIdentity((1,3,6,1,4,1,9,9,472))
if mibBuilder.loadTexts:ciscoModuleVirtualizationMIB.setRevisions(('2006-05-29 00:00','2005-12-12 00:00'))
_CmVirtualizationNotifs_ObjectIdentity=ObjectIdentity
cmVirtualizationNotifs=_CmVirtualizationNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,472,0))
_CmVirtualizationMIBObjects_ObjectIdentity=ObjectIdentity
cmVirtualizationMIBObjects=_CmVirtualizationMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,472,1))
_CmVirtualContext_ObjectIdentity=ObjectIdentity
cmVirtualContext=_CmVirtualContext_ObjectIdentity((1,3,6,1,4,1,9,9,472,1,1))
_CmVirtualContextTable_Object=MibTable
cmVirtualContextTable=_CmVirtualContextTable_Object((1,3,6,1,4,1,9,9,472,1,1,1))
if mibBuilder.loadTexts:cmVirtualContextTable.setStatus(_A)
_CmVirtualContextEntry_Object=MibTableRow
cmVirtualContextEntry=_CmVirtualContextEntry_Object((1,3,6,1,4,1,9,9,472,1,1,1,1))
cmVirtualContextEntry.setIndexNames((0,_H,_I),(0,_B,_F))
if mibBuilder.loadTexts:cmVirtualContextEntry.setStatus(_A)
_CmVirtContextName_Type=SnmpAdminString
_CmVirtContextName_Object=MibTableColumn
cmVirtContextName=_CmVirtContextName_Object((1,3,6,1,4,1,9,9,472,1,1,1,1,1),_CmVirtContextName_Type())
cmVirtContextName.setMaxAccess(_G)
if mibBuilder.loadTexts:cmVirtContextName.setStatus(_A)
class _CmVirtContextDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_CmVirtContextDescr_Type.__name__=_J
_CmVirtContextDescr_Object=MibTableColumn
cmVirtContextDescr=_CmVirtContextDescr_Object((1,3,6,1,4,1,9,9,472,1,1,1,1,2),_CmVirtContextDescr_Type())
cmVirtContextDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cmVirtContextDescr.setStatus(_A)
_CmVirtContextURL_Type=CiscoURLString
_CmVirtContextURL_Object=MibTableColumn
cmVirtContextURL=_CmVirtContextURL_Object((1,3,6,1,4,1,9,9,472,1,1,1,1,3),_CmVirtContextURL_Type())
cmVirtContextURL.setMaxAccess(_C)
if mibBuilder.loadTexts:cmVirtContextURL.setStatus(_A)
_CmVirtContextResourceClass_Type=CiscoResourceClass
_CmVirtContextResourceClass_Object=MibTableColumn
cmVirtContextResourceClass=_CmVirtContextResourceClass_Object((1,3,6,1,4,1,9,9,472,1,1,1,1,4),_CmVirtContextResourceClass_Type())
cmVirtContextResourceClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cmVirtContextResourceClass.setStatus(_A)
class _CmVirtContextStorageType_Type(StorageType):defaultValue=3
_CmVirtContextStorageType_Type.__name__=_E
_CmVirtContextStorageType_Object=MibTableColumn
cmVirtContextStorageType=_CmVirtContextStorageType_Object((1,3,6,1,4,1,9,9,472,1,1,1,1,5),_CmVirtContextStorageType_Type())
cmVirtContextStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmVirtContextStorageType.setStatus(_A)
_CmVirtContextRowStatus_Type=RowStatus
_CmVirtContextRowStatus_Object=MibTableColumn
cmVirtContextRowStatus=_CmVirtContextRowStatus_Object((1,3,6,1,4,1,9,9,472,1,1,1,1,6),_CmVirtContextRowStatus_Type())
cmVirtContextRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmVirtContextRowStatus.setStatus(_A)
_CmVirtContextIfMapTable_Object=MibTable
cmVirtContextIfMapTable=_CmVirtContextIfMapTable_Object((1,3,6,1,4,1,9,9,472,1,1,2))
if mibBuilder.loadTexts:cmVirtContextIfMapTable.setStatus(_A)
_CmVirtContextIfMapEntry_Object=MibTableRow
cmVirtContextIfMapEntry=_CmVirtContextIfMapEntry_Object((1,3,6,1,4,1,9,9,472,1,1,2,1))
cmVirtContextIfMapEntry.setIndexNames((0,_B,_F),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:cmVirtContextIfMapEntry.setStatus(_A)
_CmVirtContextIfMapType_Type=IANAifType
_CmVirtContextIfMapType_Object=MibTableColumn
cmVirtContextIfMapType=_CmVirtContextIfMapType_Object((1,3,6,1,4,1,9,9,472,1,1,2,1,1),_CmVirtContextIfMapType_Type())
cmVirtContextIfMapType.setMaxAccess(_G)
if mibBuilder.loadTexts:cmVirtContextIfMapType.setStatus(_A)
_CmVirtContextIfMapIdLow_Type=Unsigned32
_CmVirtContextIfMapIdLow_Object=MibTableColumn
cmVirtContextIfMapIdLow=_CmVirtContextIfMapIdLow_Object((1,3,6,1,4,1,9,9,472,1,1,2,1,2),_CmVirtContextIfMapIdLow_Type())
cmVirtContextIfMapIdLow.setMaxAccess(_G)
if mibBuilder.loadTexts:cmVirtContextIfMapIdLow.setStatus(_A)
_CmVirtContextIfMapIdHigh_Type=Unsigned32
_CmVirtContextIfMapIdHigh_Object=MibTableColumn
cmVirtContextIfMapIdHigh=_CmVirtContextIfMapIdHigh_Object((1,3,6,1,4,1,9,9,472,1,1,2,1,3),_CmVirtContextIfMapIdHigh_Type())
cmVirtContextIfMapIdHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:cmVirtContextIfMapIdHigh.setStatus(_A)
class _CmVirtContextIfMapStorageType_Type(StorageType):defaultValue=3
_CmVirtContextIfMapStorageType_Type.__name__=_E
_CmVirtContextIfMapStorageType_Object=MibTableColumn
cmVirtContextIfMapStorageType=_CmVirtContextIfMapStorageType_Object((1,3,6,1,4,1,9,9,472,1,1,2,1,4),_CmVirtContextIfMapStorageType_Type())
cmVirtContextIfMapStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmVirtContextIfMapStorageType.setStatus(_A)
_CmVirtContextIfMapRowStatus_Type=RowStatus
_CmVirtContextIfMapRowStatus_Object=MibTableColumn
cmVirtContextIfMapRowStatus=_CmVirtContextIfMapRowStatus_Object((1,3,6,1,4,1,9,9,472,1,1,2,1,5),_CmVirtContextIfMapRowStatus_Type())
cmVirtContextIfMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cmVirtContextIfMapRowStatus.setStatus(_A)
_CmVirtualContextNotifControl_ObjectIdentity=ObjectIdentity
cmVirtualContextNotifControl=_CmVirtualContextNotifControl_ObjectIdentity((1,3,6,1,4,1,9,9,472,1,2))
_CmVirtContextNotifEnable_Type=TruthValue
_CmVirtContextNotifEnable_Object=MibScalar
cmVirtContextNotifEnable=_CmVirtContextNotifEnable_Object((1,3,6,1,4,1,9,9,472,1,2,1),_CmVirtContextNotifEnable_Type())
cmVirtContextNotifEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cmVirtContextNotifEnable.setStatus(_A)
_CmVirtualContextNotifObjects_ObjectIdentity=ObjectIdentity
cmVirtualContextNotifObjects=_CmVirtualContextNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,472,1,3))
_CmNotifVirtContextName_Type=SnmpAdminString
_CmNotifVirtContextName_Object=MibScalar
cmNotifVirtContextName=_CmNotifVirtContextName_Object((1,3,6,1,4,1,9,9,472,1,3,1),_CmNotifVirtContextName_Type())
cmNotifVirtContextName.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cmNotifVirtContextName.setStatus(_A)
_CmVirtualizationMIBConformance_ObjectIdentity=ObjectIdentity
cmVirtualizationMIBConformance=_CmVirtualizationMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,472,2))
_CmVirtualizationCompliances_ObjectIdentity=ObjectIdentity
cmVirtualizationCompliances=_CmVirtualizationCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,472,2,1))
_CmVirtualizationGroups_ObjectIdentity=ObjectIdentity
cmVirtualizationGroups=_CmVirtualizationGroups_ObjectIdentity((1,3,6,1,4,1,9,9,472,2,2))
cmVirtContextconfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,472,2,2,1))
cmVirtContextconfigGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cmVirtContextconfigGroup.setStatus(_A)
cmVirtContextIfMapGroup=ObjectGroup((1,3,6,1,4,1,9,9,472,2,2,2))
cmVirtContextIfMapGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cmVirtContextIfMapGroup.setStatus(_A)
cmVirtContextNotifControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,472,2,2,3))
cmVirtContextNotifControlGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:cmVirtContextNotifControlGroup.setStatus(_A)
cmVirtContextNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,472,2,2,4))
cmVirtContextNotifObjectsGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:cmVirtContextNotifObjectsGroup.setStatus(_A)
cmVirtContextAdded=NotificationType((1,3,6,1,4,1,9,9,472,0,1))
cmVirtContextAdded.setObjects((_B,_D))
if mibBuilder.loadTexts:cmVirtContextAdded.setStatus(_A)
cmVirtContextRemoved=NotificationType((1,3,6,1,4,1,9,9,472,0,2))
cmVirtContextRemoved.setObjects((_B,_D))
if mibBuilder.loadTexts:cmVirtContextRemoved.setStatus(_A)
cmVirtContextNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,472,2,2,5))
cmVirtContextNotificationGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cmVirtContextNotificationGroup.setStatus(_A)
cmVirtualizationCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,472,2,1,1))
cmVirtualizationCompliance.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cmVirtualizationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoModuleVirtualizationMIB':ciscoModuleVirtualizationMIB,'cmVirtualizationNotifs':cmVirtualizationNotifs,_V:cmVirtContextAdded,_W:cmVirtContextRemoved,'cmVirtualizationMIBObjects':cmVirtualizationMIBObjects,'cmVirtualContext':cmVirtualContext,'cmVirtualContextTable':cmVirtualContextTable,'cmVirtualContextEntry':cmVirtualContextEntry,_F:cmVirtContextName,_M:cmVirtContextDescr,_N:cmVirtContextURL,_O:cmVirtContextResourceClass,_P:cmVirtContextStorageType,_Q:cmVirtContextRowStatus,'cmVirtContextIfMapTable':cmVirtContextIfMapTable,'cmVirtContextIfMapEntry':cmVirtContextIfMapEntry,_K:cmVirtContextIfMapType,_L:cmVirtContextIfMapIdLow,_R:cmVirtContextIfMapIdHigh,_S:cmVirtContextIfMapStorageType,_T:cmVirtContextIfMapRowStatus,'cmVirtualContextNotifControl':cmVirtualContextNotifControl,_U:cmVirtContextNotifEnable,'cmVirtualContextNotifObjects':cmVirtualContextNotifObjects,_D:cmNotifVirtContextName,'cmVirtualizationMIBConformance':cmVirtualizationMIBConformance,'cmVirtualizationCompliances':cmVirtualizationCompliances,'cmVirtualizationCompliance':cmVirtualizationCompliance,'cmVirtualizationGroups':cmVirtualizationGroups,_X:cmVirtContextconfigGroup,_Y:cmVirtContextIfMapGroup,_Z:cmVirtContextNotifControlGroup,'cmVirtContextNotifObjectsGroup':cmVirtContextNotifObjectsGroup,_a:cmVirtContextNotificationGroup})