_P='acdTidNotificationsGroup'
_O='acdTidGlobalCfgGroup'
_N='acdTidTableGroup'
_M='acdTidGeneralGroup'
_L='acdTidGlobalCfgChange'
_K='acdTidInfoLastChangeTid'
_J='acdTidInfoDescr'
_I='acdTidInfoType'
_H='acdTidInfoOID'
_G='acdTidStatusLastChangeTid'
_F='acdTidCfgLastChangeTid'
_E='acdTidInfoIndex'
_D='acdTidglobalCfgChangeCount'
_C='read-only'
_B='ACD-TID-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acdMibs,=mibBuilder.importSymbols('ACCEDIAN-SMI','acdMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
acdTid=ModuleIdentity((1,3,6,1,4,1,22420,2,14))
if mibBuilder.loadTexts:acdTid.setRevisions(('2012-11-05 22:00','2011-11-11 01:00'))
class AcdTidType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('configuration',1),('status',2)))
_AcdTidNotifications_ObjectIdentity=ObjectIdentity
acdTidNotifications=_AcdTidNotifications_ObjectIdentity((1,3,6,1,4,1,22420,2,14,0))
_AcdTidNotificationPrefix_ObjectIdentity=ObjectIdentity
acdTidNotificationPrefix=_AcdTidNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,22420,2,14,0,0))
_AcdTidMIBObjects_ObjectIdentity=ObjectIdentity
acdTidMIBObjects=_AcdTidMIBObjects_ObjectIdentity((1,3,6,1,4,1,22420,2,14,1))
_AcdTidGeneral_ObjectIdentity=ObjectIdentity
acdTidGeneral=_AcdTidGeneral_ObjectIdentity((1,3,6,1,4,1,22420,2,14,1,1))
_AcdTidCfgLastChangeTid_Type=Unsigned32
_AcdTidCfgLastChangeTid_Object=MibScalar
acdTidCfgLastChangeTid=_AcdTidCfgLastChangeTid_Object((1,3,6,1,4,1,22420,2,14,1,1,1),_AcdTidCfgLastChangeTid_Type())
acdTidCfgLastChangeTid.setMaxAccess(_C)
if mibBuilder.loadTexts:acdTidCfgLastChangeTid.setStatus(_A)
_AcdTidStatusLastChangeTid_Type=Unsigned32
_AcdTidStatusLastChangeTid_Object=MibScalar
acdTidStatusLastChangeTid=_AcdTidStatusLastChangeTid_Object((1,3,6,1,4,1,22420,2,14,1,1,2),_AcdTidStatusLastChangeTid_Type())
acdTidStatusLastChangeTid.setMaxAccess(_C)
if mibBuilder.loadTexts:acdTidStatusLastChangeTid.setStatus(_A)
_AcdTidInfo_ObjectIdentity=ObjectIdentity
acdTidInfo=_AcdTidInfo_ObjectIdentity((1,3,6,1,4,1,22420,2,14,1,2))
_AcdTidInfoTable_Object=MibTable
acdTidInfoTable=_AcdTidInfoTable_Object((1,3,6,1,4,1,22420,2,14,1,2,1))
if mibBuilder.loadTexts:acdTidInfoTable.setStatus(_A)
_AcdTidInfoEntry_Object=MibTableRow
acdTidInfoEntry=_AcdTidInfoEntry_Object((1,3,6,1,4,1,22420,2,14,1,2,1,1))
acdTidInfoEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:acdTidInfoEntry.setStatus(_A)
_AcdTidInfoIndex_Type=Unsigned32
_AcdTidInfoIndex_Object=MibTableColumn
acdTidInfoIndex=_AcdTidInfoIndex_Object((1,3,6,1,4,1,22420,2,14,1,2,1,1,1),_AcdTidInfoIndex_Type())
acdTidInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:acdTidInfoIndex.setStatus(_A)
_AcdTidInfoOID_Type=ObjectIdentifier
_AcdTidInfoOID_Object=MibTableColumn
acdTidInfoOID=_AcdTidInfoOID_Object((1,3,6,1,4,1,22420,2,14,1,2,1,1,2),_AcdTidInfoOID_Type())
acdTidInfoOID.setMaxAccess(_C)
if mibBuilder.loadTexts:acdTidInfoOID.setStatus(_A)
_AcdTidInfoType_Type=AcdTidType
_AcdTidInfoType_Object=MibTableColumn
acdTidInfoType=_AcdTidInfoType_Object((1,3,6,1,4,1,22420,2,14,1,2,1,1,3),_AcdTidInfoType_Type())
acdTidInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:acdTidInfoType.setStatus(_A)
_AcdTidInfoDescr_Type=DisplayString
_AcdTidInfoDescr_Object=MibTableColumn
acdTidInfoDescr=_AcdTidInfoDescr_Object((1,3,6,1,4,1,22420,2,14,1,2,1,1,4),_AcdTidInfoDescr_Type())
acdTidInfoDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:acdTidInfoDescr.setStatus(_A)
_AcdTidInfoLastChangeTid_Type=Unsigned32
_AcdTidInfoLastChangeTid_Object=MibTableColumn
acdTidInfoLastChangeTid=_AcdTidInfoLastChangeTid_Object((1,3,6,1,4,1,22420,2,14,1,2,1,1,5),_AcdTidInfoLastChangeTid_Type())
acdTidInfoLastChangeTid.setMaxAccess(_C)
if mibBuilder.loadTexts:acdTidInfoLastChangeTid.setStatus(_A)
_AcdTidGlobalCfg_ObjectIdentity=ObjectIdentity
acdTidGlobalCfg=_AcdTidGlobalCfg_ObjectIdentity((1,3,6,1,4,1,22420,2,14,1,3))
_AcdTidglobalCfgChangeCount_Type=Unsigned32
_AcdTidglobalCfgChangeCount_Object=MibScalar
acdTidglobalCfgChangeCount=_AcdTidglobalCfgChangeCount_Object((1,3,6,1,4,1,22420,2,14,1,3,2),_AcdTidglobalCfgChangeCount_Type())
acdTidglobalCfgChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:acdTidglobalCfgChangeCount.setStatus(_A)
_AcdTidConformance_ObjectIdentity=ObjectIdentity
acdTidConformance=_AcdTidConformance_ObjectIdentity((1,3,6,1,4,1,22420,2,14,2))
_AcdTidCompliances_ObjectIdentity=ObjectIdentity
acdTidCompliances=_AcdTidCompliances_ObjectIdentity((1,3,6,1,4,1,22420,2,14,2,1))
_AcdTidGroups_ObjectIdentity=ObjectIdentity
acdTidGroups=_AcdTidGroups_ObjectIdentity((1,3,6,1,4,1,22420,2,14,2,2))
acdTidGeneralGroup=ObjectGroup((1,3,6,1,4,1,22420,2,14,2,2,1))
acdTidGeneralGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:acdTidGeneralGroup.setStatus(_A)
acdTidTableGroup=ObjectGroup((1,3,6,1,4,1,22420,2,14,2,2,2))
acdTidTableGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:acdTidTableGroup.setStatus(_A)
acdTidGlobalCfgGroup=ObjectGroup((1,3,6,1,4,1,22420,2,14,2,2,3))
acdTidGlobalCfgGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:acdTidGlobalCfgGroup.setStatus(_A)
acdTidGlobalCfgChange=NotificationType((1,3,6,1,4,1,22420,2,14,0,0,1))
acdTidGlobalCfgChange.setObjects((_B,_D))
if mibBuilder.loadTexts:acdTidGlobalCfgChange.setStatus(_A)
acdTidNotificationsGroup=NotificationGroup((1,3,6,1,4,1,22420,2,14,2,2,4))
acdTidNotificationsGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:acdTidNotificationsGroup.setStatus(_A)
acdTidCompliance=ModuleCompliance((1,3,6,1,4,1,22420,2,14,2,1,1))
acdTidCompliance.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:acdTidCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AcdTidType':AcdTidType,'acdTid':acdTid,'acdTidNotifications':acdTidNotifications,'acdTidNotificationPrefix':acdTidNotificationPrefix,_L:acdTidGlobalCfgChange,'acdTidMIBObjects':acdTidMIBObjects,'acdTidGeneral':acdTidGeneral,_F:acdTidCfgLastChangeTid,_G:acdTidStatusLastChangeTid,'acdTidInfo':acdTidInfo,'acdTidInfoTable':acdTidInfoTable,'acdTidInfoEntry':acdTidInfoEntry,_E:acdTidInfoIndex,_H:acdTidInfoOID,_I:acdTidInfoType,_J:acdTidInfoDescr,_K:acdTidInfoLastChangeTid,'acdTidGlobalCfg':acdTidGlobalCfg,_D:acdTidglobalCfgChangeCount,'acdTidConformance':acdTidConformance,'acdTidCompliances':acdTidCompliances,'acdTidCompliance':acdTidCompliance,'acdTidGroups':acdTidGroups,_M:acdTidGeneralGroup,_N:acdTidTableGroup,_O:acdTidGlobalCfgGroup,_P:acdTidNotificationsGroup})