_a='cvifPhysicalConformanceObjects'
_Z='cvifGroupConformanceObjects'
_Y='cvifFailureCause'
_X='cvifBindingIfIndex'
_W='cvifRowStatus'
_V='cvifCreationTime'
_U='cvifIfIndex'
_T='cvifGroupsSupported'
_S='cvifGroupRowStatus'
_R='cvifGroupOperState'
_Q='cvifGroupFailureCause'
_P='cvifGroupCreationTime'
_O='cvifGroupMemberList'
_N='cvifGroupBindingIfIndex'
_M='cvifGroupIfIndex'
_L='cvifType'
_K='cvifIndex'
_J='cvifGroupIndex'
_I='Integer32'
_H='PortMemberList'
_G='cvifCommonConformanceObjects'
_F='not-accessible'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='CISCO-VIRTUAL-INTERFACE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
PortMemberList,=mibBuilder.importSymbols('CISCO-ST-TC',_H)
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoVirtualInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,9,9,648))
if mibBuilder.loadTexts:ciscoVirtualInterfaceMIB.setRevisions(('2008-02-27 00:00',))
_CiscoVirtualInterfaceMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVirtualInterfaceMIBObjects=_CiscoVirtualInterfaceMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,648,1))
_CvifGlobals_ObjectIdentity=ObjectIdentity
cvifGlobals=_CvifGlobals_ObjectIdentity((1,3,6,1,4,1,9,9,648,1,1))
_CvifGroupsSupported_Type=TruthValue
_CvifGroupsSupported_Object=MibScalar
cvifGroupsSupported=_CvifGroupsSupported_Object((1,3,6,1,4,1,9,9,648,1,1,1),_CvifGroupsSupported_Type())
cvifGroupsSupported.setMaxAccess('read-write')
if mibBuilder.loadTexts:cvifGroupsSupported.setStatus(_A)
_CvifConfig_ObjectIdentity=ObjectIdentity
cvifConfig=_CvifConfig_ObjectIdentity((1,3,6,1,4,1,9,9,648,1,2))
_CvifGroupTable_Object=MibTable
cvifGroupTable=_CvifGroupTable_Object((1,3,6,1,4,1,9,9,648,1,2,1))
if mibBuilder.loadTexts:cvifGroupTable.setStatus(_A)
_CvifGroupEntry_Object=MibTableRow
cvifGroupEntry=_CvifGroupEntry_Object((1,3,6,1,4,1,9,9,648,1,2,1,1))
cvifGroupEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:cvifGroupEntry.setStatus(_A)
class _CvifGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CvifGroupIndex_Type.__name__=_E
_CvifGroupIndex_Object=MibTableColumn
cvifGroupIndex=_CvifGroupIndex_Object((1,3,6,1,4,1,9,9,648,1,2,1,1,1),_CvifGroupIndex_Type())
cvifGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cvifGroupIndex.setStatus(_A)
_CvifGroupIfIndex_Type=InterfaceIndex
_CvifGroupIfIndex_Object=MibTableColumn
cvifGroupIfIndex=_CvifGroupIfIndex_Object((1,3,6,1,4,1,9,9,648,1,2,1,1,2),_CvifGroupIfIndex_Type())
cvifGroupIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cvifGroupIfIndex.setStatus(_A)
_CvifGroupBindingIfIndex_Type=InterfaceIndexOrZero
_CvifGroupBindingIfIndex_Object=MibTableColumn
cvifGroupBindingIfIndex=_CvifGroupBindingIfIndex_Object((1,3,6,1,4,1,9,9,648,1,2,1,1,3),_CvifGroupBindingIfIndex_Type())
cvifGroupBindingIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cvifGroupBindingIfIndex.setStatus(_A)
class _CvifGroupMemberList_Type(PortMemberList):defaultHexValue=''
_CvifGroupMemberList_Type.__name__=_H
_CvifGroupMemberList_Object=MibTableColumn
cvifGroupMemberList=_CvifGroupMemberList_Object((1,3,6,1,4,1,9,9,648,1,2,1,1,4),_CvifGroupMemberList_Type())
cvifGroupMemberList.setMaxAccess(_C)
if mibBuilder.loadTexts:cvifGroupMemberList.setStatus(_A)
_CvifGroupCreationTime_Type=TimeStamp
_CvifGroupCreationTime_Object=MibTableColumn
cvifGroupCreationTime=_CvifGroupCreationTime_Object((1,3,6,1,4,1,9,9,648,1,2,1,1,5),_CvifGroupCreationTime_Type())
cvifGroupCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cvifGroupCreationTime.setStatus(_A)
_CvifGroupFailureCause_Type=SnmpAdminString
_CvifGroupFailureCause_Object=MibTableColumn
cvifGroupFailureCause=_CvifGroupFailureCause_Object((1,3,6,1,4,1,9,9,648,1,2,1,1,6),_CvifGroupFailureCause_Type())
cvifGroupFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:cvifGroupFailureCause.setStatus(_A)
class _CvifGroupOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CvifGroupOperState_Type.__name__=_I
_CvifGroupOperState_Object=MibTableColumn
cvifGroupOperState=_CvifGroupOperState_Object((1,3,6,1,4,1,9,9,648,1,2,1,1,7),_CvifGroupOperState_Type())
cvifGroupOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:cvifGroupOperState.setStatus(_A)
_CvifGroupRowStatus_Type=RowStatus
_CvifGroupRowStatus_Object=MibTableColumn
cvifGroupRowStatus=_CvifGroupRowStatus_Object((1,3,6,1,4,1,9,9,648,1,2,1,1,8),_CvifGroupRowStatus_Type())
cvifGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cvifGroupRowStatus.setStatus(_A)
_CvifTable_Object=MibTable
cvifTable=_CvifTable_Object((1,3,6,1,4,1,9,9,648,1,2,2))
if mibBuilder.loadTexts:cvifTable.setStatus(_A)
_CvifEntry_Object=MibTableRow
cvifEntry=_CvifEntry_Object((1,3,6,1,4,1,9,9,648,1,2,2,1))
cvifEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:cvifEntry.setStatus(_A)
class _CvifIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CvifIndex_Type.__name__=_E
_CvifIndex_Object=MibTableColumn
cvifIndex=_CvifIndex_Object((1,3,6,1,4,1,9,9,648,1,2,2,1,1),_CvifIndex_Type())
cvifIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cvifIndex.setStatus(_A)
_CvifType_Type=IANAifType
_CvifType_Object=MibTableColumn
cvifType=_CvifType_Object((1,3,6,1,4,1,9,9,648,1,2,2,1,2),_CvifType_Type())
cvifType.setMaxAccess(_F)
if mibBuilder.loadTexts:cvifType.setStatus(_A)
_CvifIfIndex_Type=InterfaceIndex
_CvifIfIndex_Object=MibTableColumn
cvifIfIndex=_CvifIfIndex_Object((1,3,6,1,4,1,9,9,648,1,2,2,1,3),_CvifIfIndex_Type())
cvifIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cvifIfIndex.setStatus(_A)
_CvifCreationTime_Type=TimeStamp
_CvifCreationTime_Object=MibTableColumn
cvifCreationTime=_CvifCreationTime_Object((1,3,6,1,4,1,9,9,648,1,2,2,1,4),_CvifCreationTime_Type())
cvifCreationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cvifCreationTime.setStatus(_A)
_CvifBindingIfIndex_Type=InterfaceIndexOrZero
_CvifBindingIfIndex_Object=MibTableColumn
cvifBindingIfIndex=_CvifBindingIfIndex_Object((1,3,6,1,4,1,9,9,648,1,2,2,1,5),_CvifBindingIfIndex_Type())
cvifBindingIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cvifBindingIfIndex.setStatus(_A)
_CvifFailureCause_Type=SnmpAdminString
_CvifFailureCause_Object=MibTableColumn
cvifFailureCause=_CvifFailureCause_Object((1,3,6,1,4,1,9,9,648,1,2,2,1,6),_CvifFailureCause_Type())
cvifFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:cvifFailureCause.setStatus(_A)
_CvifRowStatus_Type=RowStatus
_CvifRowStatus_Object=MibTableColumn
cvifRowStatus=_CvifRowStatus_Object((1,3,6,1,4,1,9,9,648,1,2,2,1,7),_CvifRowStatus_Type())
cvifRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cvifRowStatus.setStatus(_A)
_CiscoVirtualInterfaceMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVirtualInterfaceMIBConformance=_CiscoVirtualInterfaceMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,648,2))
_CvifMIBCompliances_ObjectIdentity=ObjectIdentity
cvifMIBCompliances=_CvifMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,648,2,1))
_CvifMIBGroups_ObjectIdentity=ObjectIdentity
cvifMIBGroups=_CvifMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,648,2,2))
cvifGroupConformanceObjects=ObjectGroup((1,3,6,1,4,1,9,9,648,2,2,1))
cvifGroupConformanceObjects.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:cvifGroupConformanceObjects.setStatus(_A)
cvifCommonConformanceObjects=ObjectGroup((1,3,6,1,4,1,9,9,648,2,2,2))
cvifCommonConformanceObjects.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cvifCommonConformanceObjects.setStatus(_A)
cvifPhysicalConformanceObjects=ObjectGroup((1,3,6,1,4,1,9,9,648,2,2,3))
cvifPhysicalConformanceObjects.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cvifPhysicalConformanceObjects.setStatus(_A)
cvifGroupMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,648,2,1,1))
cvifGroupMIBCompliance.setObjects(*((_B,_Z),(_B,_G)))
if mibBuilder.loadTexts:cvifGroupMIBCompliance.setStatus(_A)
cvifMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,648,2,1,2))
cvifMIBCompliance.setObjects(*((_B,_a),(_B,_G)))
if mibBuilder.loadTexts:cvifMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVirtualInterfaceMIB':ciscoVirtualInterfaceMIB,'ciscoVirtualInterfaceMIBObjects':ciscoVirtualInterfaceMIBObjects,'cvifGlobals':cvifGlobals,_T:cvifGroupsSupported,'cvifConfig':cvifConfig,'cvifGroupTable':cvifGroupTable,'cvifGroupEntry':cvifGroupEntry,_J:cvifGroupIndex,_M:cvifGroupIfIndex,_N:cvifGroupBindingIfIndex,_O:cvifGroupMemberList,_P:cvifGroupCreationTime,_Q:cvifGroupFailureCause,_R:cvifGroupOperState,_S:cvifGroupRowStatus,'cvifTable':cvifTable,'cvifEntry':cvifEntry,_K:cvifIndex,_L:cvifType,_U:cvifIfIndex,_V:cvifCreationTime,_X:cvifBindingIfIndex,_Y:cvifFailureCause,_W:cvifRowStatus,'ciscoVirtualInterfaceMIBConformance':ciscoVirtualInterfaceMIBConformance,'cvifMIBCompliances':cvifMIBCompliances,'cvifGroupMIBCompliance':cvifGroupMIBCompliance,'cvifMIBCompliance':cvifMIBCompliance,'cvifMIBGroups':cvifMIBGroups,_Z:cvifGroupConformanceObjects,_G:cvifCommonConformanceObjects,_a:cvifPhysicalConformanceObjects})