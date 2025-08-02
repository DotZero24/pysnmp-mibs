_M='cvgConfigTableSizeGroup'
_L='cvgConfigTableSize'
_K='cvgConfigStorageType'
_J='cvgConfigRowStatus'
_I='cvgConfigVlansSecond2K'
_H='cvgConfigVlansFirst2K'
_G='cvgConfigGroupName'
_F='StorageType'
_E='SnmpAdminString'
_D='ciscoVlanGroupConfigGroup'
_C='read-create'
_B='CISCO-VLAN-GROUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Cisco2KVlanList,=mibBuilder.importSymbols('CISCO-TC','Cisco2KVlanList')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_F,'TextualConvention')
ciscoVlanGroupMIB=ModuleIdentity((1,3,6,1,4,1,9,9,709))
if mibBuilder.loadTexts:ciscoVlanGroupMIB.setRevisions(('2011-03-22 00:00','2009-11-20 00:00'))
_CiscoVlanGroupMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVlanGroupMIBNotifs=_CiscoVlanGroupMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,709,0))
_CiscoVlanGroupMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVlanGroupMIBObjects=_CiscoVlanGroupMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,709,1))
_CvgConfigTable_Object=MibTable
cvgConfigTable=_CvgConfigTable_Object((1,3,6,1,4,1,9,9,709,1,1))
if mibBuilder.loadTexts:cvgConfigTable.setStatus(_A)
_CvgConfigEntry_Object=MibTableRow
cvgConfigEntry=_CvgConfigEntry_Object((1,3,6,1,4,1,9,9,709,1,1,1))
cvgConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cvgConfigEntry.setStatus(_A)
class _CvgConfigGroupName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CvgConfigGroupName_Type.__name__=_E
_CvgConfigGroupName_Object=MibTableColumn
cvgConfigGroupName=_CvgConfigGroupName_Object((1,3,6,1,4,1,9,9,709,1,1,1,1),_CvgConfigGroupName_Type())
cvgConfigGroupName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cvgConfigGroupName.setStatus(_A)
_CvgConfigVlansFirst2K_Type=Cisco2KVlanList
_CvgConfigVlansFirst2K_Object=MibTableColumn
cvgConfigVlansFirst2K=_CvgConfigVlansFirst2K_Object((1,3,6,1,4,1,9,9,709,1,1,1,2),_CvgConfigVlansFirst2K_Type())
cvgConfigVlansFirst2K.setMaxAccess(_C)
if mibBuilder.loadTexts:cvgConfigVlansFirst2K.setStatus(_A)
_CvgConfigVlansSecond2K_Type=Cisco2KVlanList
_CvgConfigVlansSecond2K_Object=MibTableColumn
cvgConfigVlansSecond2K=_CvgConfigVlansSecond2K_Object((1,3,6,1,4,1,9,9,709,1,1,1,3),_CvgConfigVlansSecond2K_Type())
cvgConfigVlansSecond2K.setMaxAccess(_C)
if mibBuilder.loadTexts:cvgConfigVlansSecond2K.setStatus(_A)
class _CvgConfigStorageType_Type(StorageType):defaultValue=2
_CvgConfigStorageType_Type.__name__=_F
_CvgConfigStorageType_Object=MibTableColumn
cvgConfigStorageType=_CvgConfigStorageType_Object((1,3,6,1,4,1,9,9,709,1,1,1,4),_CvgConfigStorageType_Type())
cvgConfigStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvgConfigStorageType.setStatus(_A)
_CvgConfigRowStatus_Type=RowStatus
_CvgConfigRowStatus_Object=MibTableColumn
cvgConfigRowStatus=_CvgConfigRowStatus_Object((1,3,6,1,4,1,9,9,709,1,1,1,5),_CvgConfigRowStatus_Type())
cvgConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvgConfigRowStatus.setStatus(_A)
_CvgConfigTableSize_Type=Unsigned32
_CvgConfigTableSize_Object=MibScalar
cvgConfigTableSize=_CvgConfigTableSize_Object((1,3,6,1,4,1,9,9,709,1,2),_CvgConfigTableSize_Type())
cvgConfigTableSize.setMaxAccess('read-only')
if mibBuilder.loadTexts:cvgConfigTableSize.setStatus(_A)
_CiscoVlanGroupMIBConform_ObjectIdentity=ObjectIdentity
ciscoVlanGroupMIBConform=_CiscoVlanGroupMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,709,2))
_CiscoVlanGroupMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVlanGroupMIBCompliances=_CiscoVlanGroupMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,709,2,1))
_CiscoVlanGroupMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVlanGroupMIBGroups=_CiscoVlanGroupMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,709,2,2))
ciscoVlanGroupConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,709,2,2,1))
ciscoVlanGroupConfigGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ciscoVlanGroupConfigGroup.setStatus(_A)
cvgConfigTableSizeGroup=ObjectGroup((1,3,6,1,4,1,9,9,709,2,2,2))
cvgConfigTableSizeGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:cvgConfigTableSizeGroup.setStatus(_A)
ciscoVlanGroupMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,709,2,1,1))
ciscoVlanGroupMIBCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:ciscoVlanGroupMIBCompliance.setStatus('deprecated')
ciscoVlanGroupMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,709,2,1,2))
ciscoVlanGroupMIBCompliance2.setObjects(*((_B,_D),(_B,_M)))
if mibBuilder.loadTexts:ciscoVlanGroupMIBCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVlanGroupMIB':ciscoVlanGroupMIB,'ciscoVlanGroupMIBNotifs':ciscoVlanGroupMIBNotifs,'ciscoVlanGroupMIBObjects':ciscoVlanGroupMIBObjects,'cvgConfigTable':cvgConfigTable,'cvgConfigEntry':cvgConfigEntry,_G:cvgConfigGroupName,_H:cvgConfigVlansFirst2K,_I:cvgConfigVlansSecond2K,_K:cvgConfigStorageType,_J:cvgConfigRowStatus,_L:cvgConfigTableSize,'ciscoVlanGroupMIBConform':ciscoVlanGroupMIBConform,'ciscoVlanGroupMIBCompliances':ciscoVlanGroupMIBCompliances,'ciscoVlanGroupMIBCompliance':ciscoVlanGroupMIBCompliance,'ciscoVlanGroupMIBCompliance2':ciscoVlanGroupMIBCompliance2,'ciscoVlanGroupMIBGroups':ciscoVlanGroupMIBGroups,_D:ciscoVlanGroupConfigGroup,_M:cvgConfigTableSizeGroup})