_b='cbeDot1dOperVlanGroup'
_a='deprecated'
_Z='cbeDot1dVlanOperVlan'
_Y='cbeDot1dStaticStatus'
_X='cbeDot1dStaticAllowedToGoTo'
_W='cbeDot1dTpVlanRowStatus'
_V='cbeDot1dTpVlanAgingTime'
_U='cbeDot1dTpVlanAgingFromGlobal'
_T='cbeDot1dTpGlobalAgingTime'
_S='cbeDot1dStaticPortRangeIndex'
_R='cbeDot1dStaticReceivePort'
_Q='cbeDot1dStaticAddress'
_P='cbeDot1dVlanIndex'
_O='cbeDot1dTpVlanIndex'
_N='seconds'
_M='TruthValue'
_L='dot1dBasePort'
_K='BRIDGE-MIB'
_J='cbeDot1dStaticGroup'
_I='read-create'
_H='read-write'
_G='Unsigned32'
_F='Integer32'
_E='cbeDot1dTpVlanGroup'
_D='cbeDot1dTpGroup'
_C='not-accessible'
_B='CISCO-BRIDGE-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_K,_L)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPortList,CiscoPortListRange=mibBuilder.importSymbols('CISCO-TC','CiscoPortList','CiscoPortListRange')
VlanId,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_M)
ciscoBridgeExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,401))
if mibBuilder.loadTexts:ciscoBridgeExtMIB.setRevisions(('2008-05-22 00:00','2005-04-07 00:00','2004-12-03 00:00','2004-08-23 00:00'))
_CbExtMIBNotifications_ObjectIdentity=ObjectIdentity
cbExtMIBNotifications=_CbExtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,401,0))
_CbExtMIBObjects_ObjectIdentity=ObjectIdentity
cbExtMIBObjects=_CbExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,401,1))
_CbeDot1dTp_ObjectIdentity=ObjectIdentity
cbeDot1dTp=_CbeDot1dTp_ObjectIdentity((1,3,6,1,4,1,9,9,401,1,1))
class _CbeDot1dTpGlobalAgingTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,1000000))
_CbeDot1dTpGlobalAgingTime_Type.__name__=_G
_CbeDot1dTpGlobalAgingTime_Object=MibScalar
cbeDot1dTpGlobalAgingTime=_CbeDot1dTpGlobalAgingTime_Object((1,3,6,1,4,1,9,9,401,1,1,1),_CbeDot1dTpGlobalAgingTime_Type())
cbeDot1dTpGlobalAgingTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cbeDot1dTpGlobalAgingTime.setStatus(_A)
if mibBuilder.loadTexts:cbeDot1dTpGlobalAgingTime.setUnits(_N)
_CbeDot1dTpVlanTable_Object=MibTable
cbeDot1dTpVlanTable=_CbeDot1dTpVlanTable_Object((1,3,6,1,4,1,9,9,401,1,1,2))
if mibBuilder.loadTexts:cbeDot1dTpVlanTable.setStatus(_A)
_CbeDot1dTpVlanEntry_Object=MibTableRow
cbeDot1dTpVlanEntry=_CbeDot1dTpVlanEntry_Object((1,3,6,1,4,1,9,9,401,1,1,2,1))
cbeDot1dTpVlanEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:cbeDot1dTpVlanEntry.setStatus(_A)
_CbeDot1dTpVlanIndex_Type=VlanIndex
_CbeDot1dTpVlanIndex_Object=MibTableColumn
cbeDot1dTpVlanIndex=_CbeDot1dTpVlanIndex_Object((1,3,6,1,4,1,9,9,401,1,1,2,1,1),_CbeDot1dTpVlanIndex_Type())
cbeDot1dTpVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cbeDot1dTpVlanIndex.setStatus(_A)
class _CbeDot1dTpVlanAgingTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(10,1000000))
_CbeDot1dTpVlanAgingTime_Type.__name__=_G
_CbeDot1dTpVlanAgingTime_Object=MibTableColumn
cbeDot1dTpVlanAgingTime=_CbeDot1dTpVlanAgingTime_Object((1,3,6,1,4,1,9,9,401,1,1,2,1,2),_CbeDot1dTpVlanAgingTime_Type())
cbeDot1dTpVlanAgingTime.setMaxAccess(_I)
if mibBuilder.loadTexts:cbeDot1dTpVlanAgingTime.setStatus(_A)
if mibBuilder.loadTexts:cbeDot1dTpVlanAgingTime.setUnits(_N)
class _CbeDot1dTpVlanAgingFromGlobal_Type(TruthValue):defaultValue=2
_CbeDot1dTpVlanAgingFromGlobal_Type.__name__=_M
_CbeDot1dTpVlanAgingFromGlobal_Object=MibTableColumn
cbeDot1dTpVlanAgingFromGlobal=_CbeDot1dTpVlanAgingFromGlobal_Object((1,3,6,1,4,1,9,9,401,1,1,2,1,3),_CbeDot1dTpVlanAgingFromGlobal_Type())
cbeDot1dTpVlanAgingFromGlobal.setMaxAccess(_I)
if mibBuilder.loadTexts:cbeDot1dTpVlanAgingFromGlobal.setStatus(_A)
_CbeDot1dTpVlanRowStatus_Type=RowStatus
_CbeDot1dTpVlanRowStatus_Object=MibTableColumn
cbeDot1dTpVlanRowStatus=_CbeDot1dTpVlanRowStatus_Object((1,3,6,1,4,1,9,9,401,1,1,2,1,4),_CbeDot1dTpVlanRowStatus_Type())
cbeDot1dTpVlanRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:cbeDot1dTpVlanRowStatus.setStatus(_A)
_CbeDot1dStatic_ObjectIdentity=ObjectIdentity
cbeDot1dStatic=_CbeDot1dStatic_ObjectIdentity((1,3,6,1,4,1,9,9,401,1,2))
_CbeDot1dStaticTable_Object=MibTable
cbeDot1dStaticTable=_CbeDot1dStaticTable_Object((1,3,6,1,4,1,9,9,401,1,2,1))
if mibBuilder.loadTexts:cbeDot1dStaticTable.setStatus(_A)
_CbeDot1dStaticEntry_Object=MibTableRow
cbeDot1dStaticEntry=_CbeDot1dStaticEntry_Object((1,3,6,1,4,1,9,9,401,1,2,1,1))
cbeDot1dStaticEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:cbeDot1dStaticEntry.setStatus(_A)
_CbeDot1dVlanIndex_Type=VlanIndex
_CbeDot1dVlanIndex_Object=MibTableColumn
cbeDot1dVlanIndex=_CbeDot1dVlanIndex_Object((1,3,6,1,4,1,9,9,401,1,2,1,1,1),_CbeDot1dVlanIndex_Type())
cbeDot1dVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cbeDot1dVlanIndex.setStatus(_A)
_CbeDot1dStaticAddress_Type=MacAddress
_CbeDot1dStaticAddress_Object=MibTableColumn
cbeDot1dStaticAddress=_CbeDot1dStaticAddress_Object((1,3,6,1,4,1,9,9,401,1,2,1,1,2),_CbeDot1dStaticAddress_Type())
cbeDot1dStaticAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cbeDot1dStaticAddress.setStatus(_A)
class _CbeDot1dStaticReceivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CbeDot1dStaticReceivePort_Type.__name__=_F
_CbeDot1dStaticReceivePort_Object=MibTableColumn
cbeDot1dStaticReceivePort=_CbeDot1dStaticReceivePort_Object((1,3,6,1,4,1,9,9,401,1,2,1,1,3),_CbeDot1dStaticReceivePort_Type())
cbeDot1dStaticReceivePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cbeDot1dStaticReceivePort.setStatus(_A)
_CbeDot1dStaticPortRangeIndex_Type=CiscoPortListRange
_CbeDot1dStaticPortRangeIndex_Object=MibTableColumn
cbeDot1dStaticPortRangeIndex=_CbeDot1dStaticPortRangeIndex_Object((1,3,6,1,4,1,9,9,401,1,2,1,1,4),_CbeDot1dStaticPortRangeIndex_Type())
cbeDot1dStaticPortRangeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cbeDot1dStaticPortRangeIndex.setStatus(_A)
_CbeDot1dStaticAllowedToGoTo_Type=CiscoPortList
_CbeDot1dStaticAllowedToGoTo_Object=MibTableColumn
cbeDot1dStaticAllowedToGoTo=_CbeDot1dStaticAllowedToGoTo_Object((1,3,6,1,4,1,9,9,401,1,2,1,1,5),_CbeDot1dStaticAllowedToGoTo_Type())
cbeDot1dStaticAllowedToGoTo.setMaxAccess(_H)
if mibBuilder.loadTexts:cbeDot1dStaticAllowedToGoTo.setStatus(_A)
class _CbeDot1dStaticStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('permanent',3),('deleteOnReset',4),('deleteOnTimeout',5)))
_CbeDot1dStaticStatus_Type.__name__=_F
_CbeDot1dStaticStatus_Object=MibTableColumn
cbeDot1dStaticStatus=_CbeDot1dStaticStatus_Object((1,3,6,1,4,1,9,9,401,1,2,1,1,6),_CbeDot1dStaticStatus_Type())
cbeDot1dStaticStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cbeDot1dStaticStatus.setStatus(_A)
_CbeDot1dVlan_ObjectIdentity=ObjectIdentity
cbeDot1dVlan=_CbeDot1dVlan_ObjectIdentity((1,3,6,1,4,1,9,9,401,1,3))
_CbeDot1dVlanTable_Object=MibTable
cbeDot1dVlanTable=_CbeDot1dVlanTable_Object((1,3,6,1,4,1,9,9,401,1,3,1))
if mibBuilder.loadTexts:cbeDot1dVlanTable.setStatus(_A)
_CbeDot1dVlanEntry_Object=MibTableRow
cbeDot1dVlanEntry=_CbeDot1dVlanEntry_Object((1,3,6,1,4,1,9,9,401,1,3,1,1))
cbeDot1dVlanEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:cbeDot1dVlanEntry.setStatus(_A)
_CbeDot1dVlanOperVlan_Type=VlanId
_CbeDot1dVlanOperVlan_Object=MibTableColumn
cbeDot1dVlanOperVlan=_CbeDot1dVlanOperVlan_Object((1,3,6,1,4,1,9,9,401,1,3,1,1,1),_CbeDot1dVlanOperVlan_Type())
cbeDot1dVlanOperVlan.setMaxAccess('read-only')
if mibBuilder.loadTexts:cbeDot1dVlanOperVlan.setStatus(_A)
_CbExtMIBConformance_ObjectIdentity=ObjectIdentity
cbExtMIBConformance=_CbExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,401,2))
_CbExtMIBCompliances_ObjectIdentity=ObjectIdentity
cbExtMIBCompliances=_CbExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,401,2,1))
_CbExtMIBGroups_ObjectIdentity=ObjectIdentity
cbExtMIBGroups=_CbExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,401,2,2))
cbeDot1dTpGroup=ObjectGroup((1,3,6,1,4,1,9,9,401,2,2,1))
cbeDot1dTpGroup.setObjects(*((_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cbeDot1dTpGroup.setStatus(_A)
cbeDot1dTpVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,401,2,2,2))
cbeDot1dTpVlanGroup.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cbeDot1dTpVlanGroup.setStatus(_A)
cbeDot1dStaticGroup=ObjectGroup((1,3,6,1,4,1,9,9,401,2,2,3))
cbeDot1dStaticGroup.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cbeDot1dStaticGroup.setStatus(_A)
cbeDot1dOperVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,401,2,2,4))
cbeDot1dOperVlanGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:cbeDot1dOperVlanGroup.setStatus(_A)
cbExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,401,2,1,1))
cbExtMIBCompliance.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:cbExtMIBCompliance.setStatus(_a)
cbExtMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,401,2,1,2))
cbExtMIBCompliance2.setObjects(*((_B,_D),(_B,_E),(_B,_J)))
if mibBuilder.loadTexts:cbExtMIBCompliance2.setStatus(_a)
cbExtMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,401,2,1,3))
cbExtMIBCompliance3.setObjects(*((_B,_D),(_B,_E),(_B,_J),(_B,_b)))
if mibBuilder.loadTexts:cbExtMIBCompliance3.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoBridgeExtMIB':ciscoBridgeExtMIB,'cbExtMIBNotifications':cbExtMIBNotifications,'cbExtMIBObjects':cbExtMIBObjects,'cbeDot1dTp':cbeDot1dTp,_T:cbeDot1dTpGlobalAgingTime,'cbeDot1dTpVlanTable':cbeDot1dTpVlanTable,'cbeDot1dTpVlanEntry':cbeDot1dTpVlanEntry,_O:cbeDot1dTpVlanIndex,_V:cbeDot1dTpVlanAgingTime,_U:cbeDot1dTpVlanAgingFromGlobal,_W:cbeDot1dTpVlanRowStatus,'cbeDot1dStatic':cbeDot1dStatic,'cbeDot1dStaticTable':cbeDot1dStaticTable,'cbeDot1dStaticEntry':cbeDot1dStaticEntry,_P:cbeDot1dVlanIndex,_Q:cbeDot1dStaticAddress,_R:cbeDot1dStaticReceivePort,_S:cbeDot1dStaticPortRangeIndex,_X:cbeDot1dStaticAllowedToGoTo,_Y:cbeDot1dStaticStatus,'cbeDot1dVlan':cbeDot1dVlan,'cbeDot1dVlanTable':cbeDot1dVlanTable,'cbeDot1dVlanEntry':cbeDot1dVlanEntry,_Z:cbeDot1dVlanOperVlan,'cbExtMIBConformance':cbExtMIBConformance,'cbExtMIBCompliances':cbExtMIBCompliances,'cbExtMIBCompliance':cbExtMIBCompliance,'cbExtMIBCompliance2':cbExtMIBCompliance2,'cbExtMIBCompliance3':cbExtMIBCompliance3,'cbExtMIBGroups':cbExtMIBGroups,_D:cbeDot1dTpGroup,_E:cbeDot1dTpVlanGroup,_J:cbeDot1dStaticGroup,_b:cbeDot1dOperVlanGroup})