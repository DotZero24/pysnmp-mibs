_X='cbdMemberInfoGroup'
_W='cbdSystemInfoGroup'
_V='cbdMembercMac'
_U='cbdMemberStatus'
_T='cbdMemberStorageType'
_S='cbdMemberSplitHorizonNum'
_R='cbdMemberSplitHorizon'
_Q='cbdMemberAdminState'
_P='cbdMemberOperState'
_O='cbdMemberType'
_N='cbdMembersConfigured'
_M='unknown'
_L='CbdType'
_K='cbdSIIndex'
_J='read-only'
_I='StorageType'
_H='RowStatus'
_G='ifIndex'
_F='IF-MIB'
_E='Unsigned32'
_D='Integer32'
_C='read-create'
_B='CISCO-BRIDGE-DOMAIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_H,_I,'TextualConvention','TruthValue')
ciscoBridgeDomainMIB=ModuleIdentity((1,3,6,1,4,1,9,9,642))
if mibBuilder.loadTexts:ciscoBridgeDomainMIB.setRevisions(('2007-12-29 00:00','2007-12-04 00:00'))
class CbdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ether',2),('atmVc',3),('frVc',4)))
_CiscoBdMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoBdMIBNotifications=_CiscoBdMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,642,0))
_CiscoBdNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoBdNotificationPrefix=_CiscoBdNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,642,0,0))
_CiscoBdMIBObjects_ObjectIdentity=ObjectIdentity
ciscoBdMIBObjects=_CiscoBdMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,642,1))
_CbdSystemInfo_ObjectIdentity=ObjectIdentity
cbdSystemInfo=_CbdSystemInfo_ObjectIdentity((1,3,6,1,4,1,9,9,642,1,1))
_CbdMembersConfigured_Type=Unsigned32
_CbdMembersConfigured_Object=MibScalar
cbdMembersConfigured=_CbdMembersConfigured_Object((1,3,6,1,4,1,9,9,642,1,1,1),_CbdMembersConfigured_Type())
cbdMembersConfigured.setMaxAccess(_J)
if mibBuilder.loadTexts:cbdMembersConfigured.setStatus(_A)
_CbdMemberInfo_ObjectIdentity=ObjectIdentity
cbdMemberInfo=_CbdMemberInfo_ObjectIdentity((1,3,6,1,4,1,9,9,642,1,2))
_CbdMemberInfoTable_Object=MibTable
cbdMemberInfoTable=_CbdMemberInfoTable_Object((1,3,6,1,4,1,9,9,642,1,2,1))
if mibBuilder.loadTexts:cbdMemberInfoTable.setStatus(_A)
_CbdMemberInfoEntry_Object=MibTableRow
cbdMemberInfoEntry=_CbdMemberInfoEntry_Object((1,3,6,1,4,1,9,9,642,1,2,1,1))
cbdMemberInfoEntry.setIndexNames((0,_F,_G),(0,_B,_K))
if mibBuilder.loadTexts:cbdMemberInfoEntry.setStatus(_A)
class _CbdSIIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CbdSIIndex_Type.__name__=_E
_CbdSIIndex_Object=MibTableColumn
cbdSIIndex=_CbdSIIndex_Object((1,3,6,1,4,1,9,9,642,1,2,1,1,1),_CbdSIIndex_Type())
cbdSIIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cbdSIIndex.setStatus(_A)
class _CbdMemberType_Type(CbdType):defaultValue=1
_CbdMemberType_Type.__name__=_L
_CbdMemberType_Object=MibTableColumn
cbdMemberType=_CbdMemberType_Object((1,3,6,1,4,1,9,9,642,1,2,1,1,2),_CbdMemberType_Type())
cbdMemberType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbdMemberType.setStatus(_A)
class _CbdMemberOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('up',2),('down',3)))
_CbdMemberOperState_Type.__name__=_D
_CbdMemberOperState_Object=MibTableColumn
cbdMemberOperState=_CbdMemberOperState_Object((1,3,6,1,4,1,9,9,642,1,2,1,1,3),_CbdMemberOperState_Type())
cbdMemberOperState.setMaxAccess(_J)
if mibBuilder.loadTexts:cbdMemberOperState.setStatus(_A)
class _CbdMemberAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('up',2),('down',3)))
_CbdMemberAdminState_Type.__name__=_D
_CbdMemberAdminState_Object=MibTableColumn
cbdMemberAdminState=_CbdMemberAdminState_Object((1,3,6,1,4,1,9,9,642,1,2,1,1,4),_CbdMemberAdminState_Type())
cbdMemberAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:cbdMemberAdminState.setStatus(_A)
_CbdMemberSplitHorizon_Type=TruthValue
_CbdMemberSplitHorizon_Object=MibTableColumn
cbdMemberSplitHorizon=_CbdMemberSplitHorizon_Object((1,3,6,1,4,1,9,9,642,1,2,1,1,5),_CbdMemberSplitHorizon_Type())
cbdMemberSplitHorizon.setMaxAccess(_C)
if mibBuilder.loadTexts:cbdMemberSplitHorizon.setStatus(_A)
class _CbdMemberSplitHorizonNum_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CbdMemberSplitHorizonNum_Type.__name__=_E
_CbdMemberSplitHorizonNum_Object=MibTableColumn
cbdMemberSplitHorizonNum=_CbdMemberSplitHorizonNum_Object((1,3,6,1,4,1,9,9,642,1,2,1,1,6),_CbdMemberSplitHorizonNum_Type())
cbdMemberSplitHorizonNum.setMaxAccess(_C)
if mibBuilder.loadTexts:cbdMemberSplitHorizonNum.setStatus(_A)
class _CbdMemberStorageType_Type(StorageType):defaultValue=3
_CbdMemberStorageType_Type.__name__=_I
_CbdMemberStorageType_Object=MibTableColumn
cbdMemberStorageType=_CbdMemberStorageType_Object((1,3,6,1,4,1,9,9,642,1,2,1,1,7),_CbdMemberStorageType_Type())
cbdMemberStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbdMemberStorageType.setStatus(_A)
class _CbdMemberStatus_Type(RowStatus):defaultValue=1
_CbdMemberStatus_Type.__name__=_H
_CbdMemberStatus_Object=MibTableColumn
cbdMemberStatus=_CbdMemberStatus_Object((1,3,6,1,4,1,9,9,642,1,2,1,1,8),_CbdMemberStatus_Type())
cbdMemberStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cbdMemberStatus.setStatus(_A)
_CbdMembercMac_Type=TruthValue
_CbdMembercMac_Object=MibTableColumn
cbdMembercMac=_CbdMembercMac_Object((1,3,6,1,4,1,9,9,642,1,2,1,1,9),_CbdMembercMac_Type())
cbdMembercMac.setMaxAccess(_C)
if mibBuilder.loadTexts:cbdMembercMac.setStatus(_A)
_CiscoBdMIBConformance_ObjectIdentity=ObjectIdentity
ciscoBdMIBConformance=_CiscoBdMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,642,2))
_CiscoBdMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoBdMIBCompliances=_CiscoBdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,642,2,1))
_CiscoBdMIBGroups_ObjectIdentity=ObjectIdentity
ciscoBdMIBGroups=_CiscoBdMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,642,2,2))
cbdSystemInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,642,2,2,1))
cbdSystemInfoGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:cbdSystemInfoGroup.setStatus(_A)
cbdMemberInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,642,2,2,2))
cbdMemberInfoGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cbdMemberInfoGroup.setStatus(_A)
ciscoBdMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,642,2,1,1))
ciscoBdMIBComplianceRev1.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoBdMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_L:CbdType,'ciscoBridgeDomainMIB':ciscoBridgeDomainMIB,'ciscoBdMIBNotifications':ciscoBdMIBNotifications,'ciscoBdNotificationPrefix':ciscoBdNotificationPrefix,'ciscoBdMIBObjects':ciscoBdMIBObjects,'cbdSystemInfo':cbdSystemInfo,_N:cbdMembersConfigured,'cbdMemberInfo':cbdMemberInfo,'cbdMemberInfoTable':cbdMemberInfoTable,'cbdMemberInfoEntry':cbdMemberInfoEntry,_K:cbdSIIndex,_O:cbdMemberType,_P:cbdMemberOperState,_Q:cbdMemberAdminState,_R:cbdMemberSplitHorizon,_S:cbdMemberSplitHorizonNum,_T:cbdMemberStorageType,_U:cbdMemberStatus,_V:cbdMembercMac,'ciscoBdMIBConformance':ciscoBdMIBConformance,'ciscoBdMIBCompliances':ciscoBdMIBCompliances,'ciscoBdMIBComplianceRev1':ciscoBdMIBComplianceRev1,'ciscoBdMIBGroups':ciscoBdMIBGroups,_W:cbdSystemInfoGroup,_X:cbdMemberInfoGroup})