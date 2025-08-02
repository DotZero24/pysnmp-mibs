_g='tnGmplsNeSubnodeGroup'
_f='tnGmplsNeGroup'
_e='tnGmplsNeObjsGroup'
_d='tnGmplsNeSubnodeRowStatus'
_c='tnGmplsNeSubnodeAdminStatus'
_b='tnGmplsNeSubnodeId'
_a='tnGmplsNeRowStatus'
_Z='tnGmplsNeColocatedNode'
_Y='tnGmplsNeColocatedNodeAddrType'
_X='tnGmplsNeOperationalState'
_W='tnGmplsNeAdminStatus'
_V='tnGmplsNeInstalledNWVersion'
_U='tnGmplsNeActiveNWVersion'
_T='tnGmplsNeAutomode'
_S='tnGmplsNeRestorationMode'
_R='tnGmplsNeDcnOspfArea'
_Q='tnGmplsNeNodeName'
_P='tnGmplsNeNotifyAddr'
_O='tnGmplsNeNotifyAddrType'
_N='tnGmplsNeNodeAddr'
_M='tnGmplsNeNodeAddrType'
_L='tnGmplsNeCPNodeId'
_K='tnGmplsNeAttributeTotal'
_J='tnGmplsNeSubnodeIndex'
_I='manual'
_H='not-accessible'
_G='tnGmplsNeIndex'
_F='down'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='TROPIC-GMPLS-NE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressIPv4,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv4','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
tnGmplsMIBModules,tnGmplsObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnGmplsMIBModules','tnGmplsObjs')
tnGmplsNeMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,6,4))
if mibBuilder.loadTexts:tnGmplsNeMibModule.setRevisions(('2018-02-23 12:00','2017-07-07 12:00','2016-11-16 12:00','2013-06-27 12:00'))
_TnGmplsNeMIB_ObjectIdentity=ObjectIdentity
tnGmplsNeMIB=_TnGmplsNeMIB_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,4))
_TnGmplsNeObjs_ObjectIdentity=ObjectIdentity
tnGmplsNeObjs=_TnGmplsNeObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,4,1))
_TnGmplsNeAttributeTotal_Type=Integer32
_TnGmplsNeAttributeTotal_Object=MibScalar
tnGmplsNeAttributeTotal=_TnGmplsNeAttributeTotal_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,1),_TnGmplsNeAttributeTotal_Type())
tnGmplsNeAttributeTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:tnGmplsNeAttributeTotal.setStatus(_A)
_TnGmplsNeTable_Object=MibTable
tnGmplsNeTable=_TnGmplsNeTable_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2))
if mibBuilder.loadTexts:tnGmplsNeTable.setStatus(_A)
_TnGmplsNeEntry_Object=MibTableRow
tnGmplsNeEntry=_TnGmplsNeEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1))
tnGmplsNeEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:tnGmplsNeEntry.setStatus(_A)
_TnGmplsNeIndex_Type=Unsigned32
_TnGmplsNeIndex_Object=MibTableColumn
tnGmplsNeIndex=_TnGmplsNeIndex_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,1),_TnGmplsNeIndex_Type())
tnGmplsNeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:tnGmplsNeIndex.setStatus(_A)
_TnGmplsNeCPNodeId_Type=InetAddressIPv4
_TnGmplsNeCPNodeId_Object=MibTableColumn
tnGmplsNeCPNodeId=_TnGmplsNeCPNodeId_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,2),_TnGmplsNeCPNodeId_Type())
tnGmplsNeCPNodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeCPNodeId.setStatus(_A)
_TnGmplsNeNodeAddrType_Type=InetAddressType
_TnGmplsNeNodeAddrType_Object=MibTableColumn
tnGmplsNeNodeAddrType=_TnGmplsNeNodeAddrType_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,3),_TnGmplsNeNodeAddrType_Type())
tnGmplsNeNodeAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnGmplsNeNodeAddrType.setStatus(_A)
_TnGmplsNeNodeAddr_Type=InetAddress
_TnGmplsNeNodeAddr_Object=MibTableColumn
tnGmplsNeNodeAddr=_TnGmplsNeNodeAddr_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,4),_TnGmplsNeNodeAddr_Type())
tnGmplsNeNodeAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tnGmplsNeNodeAddr.setStatus(_A)
_TnGmplsNeNotifyAddrType_Type=InetAddressType
_TnGmplsNeNotifyAddrType_Object=MibTableColumn
tnGmplsNeNotifyAddrType=_TnGmplsNeNotifyAddrType_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,5),_TnGmplsNeNotifyAddrType_Type())
tnGmplsNeNotifyAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnGmplsNeNotifyAddrType.setStatus(_A)
_TnGmplsNeNotifyAddr_Type=InetAddress
_TnGmplsNeNotifyAddr_Object=MibTableColumn
tnGmplsNeNotifyAddr=_TnGmplsNeNotifyAddr_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,6),_TnGmplsNeNotifyAddr_Type())
tnGmplsNeNotifyAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tnGmplsNeNotifyAddr.setStatus(_A)
_TnGmplsNeNodeName_Type=DisplayString
_TnGmplsNeNodeName_Object=MibTableColumn
tnGmplsNeNodeName=_TnGmplsNeNodeName_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,7),_TnGmplsNeNodeName_Type())
tnGmplsNeNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeNodeName.setStatus(_A)
_TnGmplsNeDcnOspfArea_Type=InetAddressIPv4
_TnGmplsNeDcnOspfArea_Object=MibTableColumn
tnGmplsNeDcnOspfArea=_TnGmplsNeDcnOspfArea_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,8),_TnGmplsNeDcnOspfArea_Type())
tnGmplsNeDcnOspfArea.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeDcnOspfArea.setStatus(_A)
class _TnGmplsNeRestorationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('automatic',1),(_I,2),('prio2',3),('prio3',4),('prio4',5),('prio5',6)))
_TnGmplsNeRestorationMode_Type.__name__=_E
_TnGmplsNeRestorationMode_Object=MibTableColumn
tnGmplsNeRestorationMode=_TnGmplsNeRestorationMode_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,9),_TnGmplsNeRestorationMode_Type())
tnGmplsNeRestorationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeRestorationMode.setStatus(_A)
class _TnGmplsNeAutomode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('managed',2),('full',3)))
_TnGmplsNeAutomode_Type.__name__=_E
_TnGmplsNeAutomode_Object=MibTableColumn
tnGmplsNeAutomode=_TnGmplsNeAutomode_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,10),_TnGmplsNeAutomode_Type())
tnGmplsNeAutomode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeAutomode.setStatus(_A)
_TnGmplsNeActiveNWVersion_Type=DisplayString
_TnGmplsNeActiveNWVersion_Object=MibTableColumn
tnGmplsNeActiveNWVersion=_TnGmplsNeActiveNWVersion_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,11),_TnGmplsNeActiveNWVersion_Type())
tnGmplsNeActiveNWVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeActiveNWVersion.setStatus(_A)
_TnGmplsNeInstalledNWVersion_Type=DisplayString
_TnGmplsNeInstalledNWVersion_Object=MibTableColumn
tnGmplsNeInstalledNWVersion=_TnGmplsNeInstalledNWVersion_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,12),_TnGmplsNeInstalledNWVersion_Type())
tnGmplsNeInstalledNWVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:tnGmplsNeInstalledNWVersion.setStatus(_A)
class _TnGmplsNeAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('up',2)))
_TnGmplsNeAdminStatus_Type.__name__=_E
_TnGmplsNeAdminStatus_Object=MibTableColumn
tnGmplsNeAdminStatus=_TnGmplsNeAdminStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,13),_TnGmplsNeAdminStatus_Type())
tnGmplsNeAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeAdminStatus.setStatus(_A)
class _TnGmplsNeOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('degraded',2),('up',3)))
_TnGmplsNeOperationalState_Type.__name__=_E
_TnGmplsNeOperationalState_Object=MibTableColumn
tnGmplsNeOperationalState=_TnGmplsNeOperationalState_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,14),_TnGmplsNeOperationalState_Type())
tnGmplsNeOperationalState.setMaxAccess(_D)
if mibBuilder.loadTexts:tnGmplsNeOperationalState.setStatus(_A)
_TnGmplsNeColocatedNodeAddrType_Type=InetAddressType
_TnGmplsNeColocatedNodeAddrType_Object=MibTableColumn
tnGmplsNeColocatedNodeAddrType=_TnGmplsNeColocatedNodeAddrType_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,15),_TnGmplsNeColocatedNodeAddrType_Type())
tnGmplsNeColocatedNodeAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeColocatedNodeAddrType.setStatus(_A)
_TnGmplsNeColocatedNode_Type=InetAddress
_TnGmplsNeColocatedNode_Object=MibTableColumn
tnGmplsNeColocatedNode=_TnGmplsNeColocatedNode_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,16),_TnGmplsNeColocatedNode_Type())
tnGmplsNeColocatedNode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeColocatedNode.setStatus(_A)
_TnGmplsNeRowStatus_Type=RowStatus
_TnGmplsNeRowStatus_Object=MibTableColumn
tnGmplsNeRowStatus=_TnGmplsNeRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,2,1,17),_TnGmplsNeRowStatus_Type())
tnGmplsNeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeRowStatus.setStatus(_A)
_TnGmplsNeSubnodeTable_Object=MibTable
tnGmplsNeSubnodeTable=_TnGmplsNeSubnodeTable_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,3))
if mibBuilder.loadTexts:tnGmplsNeSubnodeTable.setStatus(_A)
_TnGmplsNeSubnodeEntry_Object=MibTableRow
tnGmplsNeSubnodeEntry=_TnGmplsNeSubnodeEntry_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,3,1))
tnGmplsNeSubnodeEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:tnGmplsNeSubnodeEntry.setStatus(_A)
_TnGmplsNeSubnodeIndex_Type=Unsigned32
_TnGmplsNeSubnodeIndex_Object=MibTableColumn
tnGmplsNeSubnodeIndex=_TnGmplsNeSubnodeIndex_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,3,1,1),_TnGmplsNeSubnodeIndex_Type())
tnGmplsNeSubnodeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:tnGmplsNeSubnodeIndex.setStatus(_A)
_TnGmplsNeSubnodeId_Type=Unsigned32
_TnGmplsNeSubnodeId_Object=MibTableColumn
tnGmplsNeSubnodeId=_TnGmplsNeSubnodeId_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,3,1,2),_TnGmplsNeSubnodeId_Type())
tnGmplsNeSubnodeId.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeSubnodeId.setStatus(_A)
class _TnGmplsNeSubnodeAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('up',2)))
_TnGmplsNeSubnodeAdminStatus_Type.__name__=_E
_TnGmplsNeSubnodeAdminStatus_Object=MibTableColumn
tnGmplsNeSubnodeAdminStatus=_TnGmplsNeSubnodeAdminStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,3,1,3),_TnGmplsNeSubnodeAdminStatus_Type())
tnGmplsNeSubnodeAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeSubnodeAdminStatus.setStatus(_A)
_TnGmplsNeSubnodeRowStatus_Type=RowStatus
_TnGmplsNeSubnodeRowStatus_Object=MibTableColumn
tnGmplsNeSubnodeRowStatus=_TnGmplsNeSubnodeRowStatus_Object((1,3,6,1,4,1,7483,2,1,10,1,4,1,3,1,4),_TnGmplsNeSubnodeRowStatus_Type())
tnGmplsNeSubnodeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tnGmplsNeSubnodeRowStatus.setStatus(_A)
_TnGmplsNeConf_ObjectIdentity=ObjectIdentity
tnGmplsNeConf=_TnGmplsNeConf_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,4,3))
_TnGmplsNeGroups_ObjectIdentity=ObjectIdentity
tnGmplsNeGroups=_TnGmplsNeGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,4,3,1))
_TnGmplsNeCompliances_ObjectIdentity=ObjectIdentity
tnGmplsNeCompliances=_TnGmplsNeCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,1,10,1,4,3,2))
tnGmplsNeObjsGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,4,3,1,1))
tnGmplsNeObjsGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:tnGmplsNeObjsGroup.setStatus(_A)
tnGmplsNeGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,4,3,1,2))
tnGmplsNeGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:tnGmplsNeGroup.setStatus(_A)
tnGmplsNeSubnodeGroup=ObjectGroup((1,3,6,1,4,1,7483,2,1,10,1,4,3,1,3))
tnGmplsNeSubnodeGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:tnGmplsNeSubnodeGroup.setStatus(_A)
tnGmplsNeCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,1,10,1,4,3,2,1))
tnGmplsNeCompliance.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:tnGmplsNeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnGmplsNeMibModule':tnGmplsNeMibModule,'tnGmplsNeMIB':tnGmplsNeMIB,'tnGmplsNeObjs':tnGmplsNeObjs,_K:tnGmplsNeAttributeTotal,'tnGmplsNeTable':tnGmplsNeTable,'tnGmplsNeEntry':tnGmplsNeEntry,_G:tnGmplsNeIndex,_L:tnGmplsNeCPNodeId,_M:tnGmplsNeNodeAddrType,_N:tnGmplsNeNodeAddr,_O:tnGmplsNeNotifyAddrType,_P:tnGmplsNeNotifyAddr,_Q:tnGmplsNeNodeName,_R:tnGmplsNeDcnOspfArea,_S:tnGmplsNeRestorationMode,_T:tnGmplsNeAutomode,_U:tnGmplsNeActiveNWVersion,_V:tnGmplsNeInstalledNWVersion,_W:tnGmplsNeAdminStatus,_X:tnGmplsNeOperationalState,_Y:tnGmplsNeColocatedNodeAddrType,_Z:tnGmplsNeColocatedNode,_a:tnGmplsNeRowStatus,'tnGmplsNeSubnodeTable':tnGmplsNeSubnodeTable,'tnGmplsNeSubnodeEntry':tnGmplsNeSubnodeEntry,_J:tnGmplsNeSubnodeIndex,_b:tnGmplsNeSubnodeId,_c:tnGmplsNeSubnodeAdminStatus,_d:tnGmplsNeSubnodeRowStatus,'tnGmplsNeConf':tnGmplsNeConf,'tnGmplsNeGroups':tnGmplsNeGroups,_e:tnGmplsNeObjsGroup,_f:tnGmplsNeGroup,_g:tnGmplsNeSubnodeGroup,'tnGmplsNeCompliances':tnGmplsNeCompliances,'tnGmplsNeCompliance':tnGmplsNeCompliance})