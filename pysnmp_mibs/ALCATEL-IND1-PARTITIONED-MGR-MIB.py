_X='endUserProfileVlanIdGroup'
_W='endUserProfileSlotPortGroup'
_V='endUserProfileGroup'
_U='endUserProfileVlanIdRowStatus'
_T='endUserProfileVlanIdEnd'
_S='endUserProfileSlotPortRowStatus'
_R='endUserProfilePortList'
_Q='endUserProfileRowStatus'
_P='endUserProfileAreaSpantree'
_O='endUserProfileAreaMacFilteringTable'
_N='endUserProfileAreaIpRoutesTable'
_M='endUserProfileAreaBasicIpRouting'
_L='endUserProfileAreaVlanTable'
_K='endUserProfileAreaPhysical'
_J='Integer32'
_I='SnmpAdminString'
_H='endUserProfileVlanIdStart'
_G='endUserProfileSlotNumber'
_F='read-only'
_E='endUserProfileName'
_D='EndUserProfileArea'
_C='read-create'
_B='ALCATEL-IND1-PARTITIONED-MGR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Partmgr,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Partmgr')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alcatelIND1PartitionedMgrMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,25,1))
class EndUserPortList(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('port1',0),('port2',1),('port3',2),('port4',3),('port5',4),('port6',5),('port7',6),('port8',7),('port9',8),('port10',9),('port11',10),('port12',11),('port13',12),('port14',13),('port15',14),('port16',15),('port17',16),('port18',17),('port19',18),('port20',19),('port21',20),('port22',21),('port23',22),('port24',23),('port25',24),('port26',25),('port27',26),('port28',27),('port29',28),('port30',29),('port31',30),('port32',31),('port33',32),('port34',33),('port35',34),('port36',35),('port37',36),('port38',37),('port39',38),('port40',39),('port41',40),('port42',41),('port43',42),('port44',43),('port45',44),('port46',45),('port47',46),('port48',47),('port49',48),('port50',49),('port51',50),('port52',51),('port53',52),('port54',53),('port55',54),('port56',55),('port57',56),('port58',57),('port59',58),('port60',59),('port61',60),('port62',61),('port63',62),('port64',63)))
class EndUserProfileArea(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('readOnly',2),('readWrite',3)))
_AlcatelIND1PartitionedMgrMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1PartitionedMgrMIBObjects=_AlcatelIND1PartitionedMgrMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,25,1,1))
if mibBuilder.loadTexts:alcatelIND1PartitionedMgrMIBObjects.setStatus(_A)
_EndUserProfileMgrMIB_ObjectIdentity=ObjectIdentity
endUserProfileMgrMIB=_EndUserProfileMgrMIB_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1))
_EndUserProfileTable_Object=MibTable
endUserProfileTable=_EndUserProfileTable_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1))
if mibBuilder.loadTexts:endUserProfileTable.setStatus(_A)
_EndUserProfileEntry_Object=MibTableRow
endUserProfileEntry=_EndUserProfileEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1,1))
endUserProfileEntry.setIndexNames((1,_B,_E))
if mibBuilder.loadTexts:endUserProfileEntry.setStatus(_A)
class _EndUserProfileName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_EndUserProfileName_Type.__name__=_I
_EndUserProfileName_Object=MibTableColumn
endUserProfileName=_EndUserProfileName_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1,1,1),_EndUserProfileName_Type())
endUserProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:endUserProfileName.setStatus(_A)
class _EndUserProfileAreaPhysical_Type(EndUserProfileArea):defaultValue=1
_EndUserProfileAreaPhysical_Type.__name__=_D
_EndUserProfileAreaPhysical_Object=MibTableColumn
endUserProfileAreaPhysical=_EndUserProfileAreaPhysical_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1,1,2),_EndUserProfileAreaPhysical_Type())
endUserProfileAreaPhysical.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileAreaPhysical.setStatus(_A)
class _EndUserProfileAreaVlanTable_Type(EndUserProfileArea):defaultValue=1
_EndUserProfileAreaVlanTable_Type.__name__=_D
_EndUserProfileAreaVlanTable_Object=MibTableColumn
endUserProfileAreaVlanTable=_EndUserProfileAreaVlanTable_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1,1,3),_EndUserProfileAreaVlanTable_Type())
endUserProfileAreaVlanTable.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileAreaVlanTable.setStatus(_A)
class _EndUserProfileAreaBasicIpRouting_Type(EndUserProfileArea):defaultValue=1
_EndUserProfileAreaBasicIpRouting_Type.__name__=_D
_EndUserProfileAreaBasicIpRouting_Object=MibTableColumn
endUserProfileAreaBasicIpRouting=_EndUserProfileAreaBasicIpRouting_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1,1,4),_EndUserProfileAreaBasicIpRouting_Type())
endUserProfileAreaBasicIpRouting.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileAreaBasicIpRouting.setStatus(_A)
class _EndUserProfileAreaIpRoutesTable_Type(EndUserProfileArea):defaultValue=1
_EndUserProfileAreaIpRoutesTable_Type.__name__=_D
_EndUserProfileAreaIpRoutesTable_Object=MibTableColumn
endUserProfileAreaIpRoutesTable=_EndUserProfileAreaIpRoutesTable_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1,1,5),_EndUserProfileAreaIpRoutesTable_Type())
endUserProfileAreaIpRoutesTable.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileAreaIpRoutesTable.setStatus(_A)
class _EndUserProfileAreaMacFilteringTable_Type(EndUserProfileArea):defaultValue=1
_EndUserProfileAreaMacFilteringTable_Type.__name__=_D
_EndUserProfileAreaMacFilteringTable_Object=MibTableColumn
endUserProfileAreaMacFilteringTable=_EndUserProfileAreaMacFilteringTable_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1,1,6),_EndUserProfileAreaMacFilteringTable_Type())
endUserProfileAreaMacFilteringTable.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileAreaMacFilteringTable.setStatus(_A)
class _EndUserProfileAreaSpantree_Type(EndUserProfileArea):defaultValue=1
_EndUserProfileAreaSpantree_Type.__name__=_D
_EndUserProfileAreaSpantree_Object=MibTableColumn
endUserProfileAreaSpantree=_EndUserProfileAreaSpantree_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1,1,7),_EndUserProfileAreaSpantree_Type())
endUserProfileAreaSpantree.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileAreaSpantree.setStatus(_A)
_EndUserProfileRowStatus_Type=RowStatus
_EndUserProfileRowStatus_Object=MibTableColumn
endUserProfileRowStatus=_EndUserProfileRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,1,1,8),_EndUserProfileRowStatus_Type())
endUserProfileRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileRowStatus.setStatus(_A)
_EndUserProfileSlotPortTable_Object=MibTable
endUserProfileSlotPortTable=_EndUserProfileSlotPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,2))
if mibBuilder.loadTexts:endUserProfileSlotPortTable.setStatus(_A)
_EndUserProfileSlotPortEntry_Object=MibTableRow
endUserProfileSlotPortEntry=_EndUserProfileSlotPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,2,1))
endUserProfileSlotPortEntry.setIndexNames((0,_B,_G),(1,_B,_E))
if mibBuilder.loadTexts:endUserProfileSlotPortEntry.setStatus(_A)
class _EndUserProfileSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_EndUserProfileSlotNumber_Type.__name__=_J
_EndUserProfileSlotNumber_Object=MibTableColumn
endUserProfileSlotNumber=_EndUserProfileSlotNumber_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,2,1,1),_EndUserProfileSlotNumber_Type())
endUserProfileSlotNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:endUserProfileSlotNumber.setStatus(_A)
_EndUserProfilePortList_Type=EndUserPortList
_EndUserProfilePortList_Object=MibTableColumn
endUserProfilePortList=_EndUserProfilePortList_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,2,1,2),_EndUserProfilePortList_Type())
endUserProfilePortList.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfilePortList.setStatus(_A)
_EndUserProfileSlotPortRowStatus_Type=RowStatus
_EndUserProfileSlotPortRowStatus_Object=MibTableColumn
endUserProfileSlotPortRowStatus=_EndUserProfileSlotPortRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,2,1,3),_EndUserProfileSlotPortRowStatus_Type())
endUserProfileSlotPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileSlotPortRowStatus.setStatus(_A)
_EndUserProfileVlanIdTable_Object=MibTable
endUserProfileVlanIdTable=_EndUserProfileVlanIdTable_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,3))
if mibBuilder.loadTexts:endUserProfileVlanIdTable.setStatus(_A)
_EndUserProfileVlanIdEntry_Object=MibTableRow
endUserProfileVlanIdEntry=_EndUserProfileVlanIdEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,3,1))
endUserProfileVlanIdEntry.setIndexNames((0,_B,_H),(1,_B,_E))
if mibBuilder.loadTexts:endUserProfileVlanIdEntry.setStatus(_A)
_EndUserProfileVlanIdStart_Type=VlanId
_EndUserProfileVlanIdStart_Object=MibTableColumn
endUserProfileVlanIdStart=_EndUserProfileVlanIdStart_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,3,1,1),_EndUserProfileVlanIdStart_Type())
endUserProfileVlanIdStart.setMaxAccess(_F)
if mibBuilder.loadTexts:endUserProfileVlanIdStart.setStatus(_A)
_EndUserProfileVlanIdEnd_Type=VlanId
_EndUserProfileVlanIdEnd_Object=MibTableColumn
endUserProfileVlanIdEnd=_EndUserProfileVlanIdEnd_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,3,1,2),_EndUserProfileVlanIdEnd_Type())
endUserProfileVlanIdEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileVlanIdEnd.setStatus(_A)
_EndUserProfileVlanIdRowStatus_Type=RowStatus
_EndUserProfileVlanIdRowStatus_Object=MibTableColumn
endUserProfileVlanIdRowStatus=_EndUserProfileVlanIdRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,25,1,1,1,3,1,3),_EndUserProfileVlanIdRowStatus_Type())
endUserProfileVlanIdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:endUserProfileVlanIdRowStatus.setStatus(_A)
_AlcatelIND1PartitionedMgrMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1PartitionedMgrMIBConformance=_AlcatelIND1PartitionedMgrMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,25,1,2))
if mibBuilder.loadTexts:alcatelIND1PartitionedMgrMIBConformance.setStatus(_A)
_AlcatelIND1PartitionedMgrMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1PartitionedMgrMIBGroups=_AlcatelIND1PartitionedMgrMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,25,1,2,1))
if mibBuilder.loadTexts:alcatelIND1PartitionedMgrMIBGroups.setStatus(_A)
_AlcatelIND1PartitionedMgrMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1PartitionedMgrMIBCompliances=_AlcatelIND1PartitionedMgrMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,25,1,2,2))
if mibBuilder.loadTexts:alcatelIND1PartitionedMgrMIBCompliances.setStatus(_A)
endUserProfileGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,25,1,2,1,1))
endUserProfileGroup.setObjects(*((_B,_E),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:endUserProfileGroup.setStatus(_A)
endUserProfileSlotPortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,25,1,2,1,2))
endUserProfileSlotPortGroup.setObjects(*((_B,_G),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:endUserProfileSlotPortGroup.setStatus(_A)
endUserProfileVlanIdGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,25,1,2,1,3))
endUserProfileVlanIdGroup.setObjects(*((_B,_H),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:endUserProfileVlanIdGroup.setStatus(_A)
alcatelIND1PartitionedMgrMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,25,1,2,2,1))
alcatelIND1PartitionedMgrMIBCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:alcatelIND1PartitionedMgrMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EndUserPortList':EndUserPortList,_D:EndUserProfileArea,'alcatelIND1PartitionedMgrMIB':alcatelIND1PartitionedMgrMIB,'alcatelIND1PartitionedMgrMIBObjects':alcatelIND1PartitionedMgrMIBObjects,'endUserProfileMgrMIB':endUserProfileMgrMIB,'endUserProfileTable':endUserProfileTable,'endUserProfileEntry':endUserProfileEntry,_E:endUserProfileName,_K:endUserProfileAreaPhysical,_L:endUserProfileAreaVlanTable,_M:endUserProfileAreaBasicIpRouting,_N:endUserProfileAreaIpRoutesTable,_O:endUserProfileAreaMacFilteringTable,_P:endUserProfileAreaSpantree,_Q:endUserProfileRowStatus,'endUserProfileSlotPortTable':endUserProfileSlotPortTable,'endUserProfileSlotPortEntry':endUserProfileSlotPortEntry,_G:endUserProfileSlotNumber,_R:endUserProfilePortList,_S:endUserProfileSlotPortRowStatus,'endUserProfileVlanIdTable':endUserProfileVlanIdTable,'endUserProfileVlanIdEntry':endUserProfileVlanIdEntry,_H:endUserProfileVlanIdStart,_T:endUserProfileVlanIdEnd,_U:endUserProfileVlanIdRowStatus,'alcatelIND1PartitionedMgrMIBConformance':alcatelIND1PartitionedMgrMIBConformance,'alcatelIND1PartitionedMgrMIBGroups':alcatelIND1PartitionedMgrMIBGroups,_V:endUserProfileGroup,_W:endUserProfileSlotPortGroup,_X:endUserProfileVlanIdGroup,'alcatelIND1PartitionedMgrMIBCompliances':alcatelIND1PartitionedMgrMIBCompliances,'alcatelIND1PartitionedMgrMIBCompliance':alcatelIND1PartitionedMgrMIBCompliance})