_W='dpL2FdbMcastFilterModeCfgGroup'
_V='dpL2FdbInterfaceGroup'
_U='dpL2FdbMacAddrTableGroup'
_T='dpL2FdbGlobalGroup'
_S='dpL2FdbMcastFilterMode'
_R='dpL2FdbIfMacLearningEnabled'
_Q='dpL2FdbStaticUnicastRowStatus'
_P='dpL2FdbStaticUnicastPortNum'
_O='dpL2FdbAgingTime'
_N='dpL2FdbClearAllMacAddr'
_M='dpL2FdbStaticMulticastMacAddr'
_L='dpL2FdbStaticMulticastVlanID'
_K='dpL2FdbStaticUnicastMacAddr'
_J='dpL2FdbStaticUnicastVlanID'
_I='Unsigned32'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='read-create'
_D='not-accessible'
_C='read-write'
_B='DLINKPRIME-L2FDB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndex','InterfaceIndexOrZero',_H)
PortList,VlanId,dot1qFdbId,dot1qStaticUnicastAddress=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId','dot1qFdbId','dot1qStaticUnicastAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkPrimeL2FdbMIB=ModuleIdentity((1,3,6,1,4,1,171,15,5))
if mibBuilder.loadTexts:dlinkPrimeL2FdbMIB.setRevisions(('2014-04-26 00:00',))
_DpL2FdbMIBNotifications_ObjectIdentity=ObjectIdentity
dpL2FdbMIBNotifications=_DpL2FdbMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,5,0))
_DpL2FdbMIBObjects_ObjectIdentity=ObjectIdentity
dpL2FdbMIBObjects=_DpL2FdbMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,5,1))
_DpL2FdbGblCtrl_ObjectIdentity=ObjectIdentity
dpL2FdbGblCtrl=_DpL2FdbGblCtrl_ObjectIdentity((1,3,6,1,4,1,171,15,5,1,1))
_DpL2FdbClearCtrl_ObjectIdentity=ObjectIdentity
dpL2FdbClearCtrl=_DpL2FdbClearCtrl_ObjectIdentity((1,3,6,1,4,1,171,15,5,1,1,1))
class _DpL2FdbClearAllMacAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('noOp',2)))
_DpL2FdbClearAllMacAddr_Type.__name__=_F
_DpL2FdbClearAllMacAddr_Object=MibScalar
dpL2FdbClearAllMacAddr=_DpL2FdbClearAllMacAddr_Object((1,3,6,1,4,1,171,15,5,1,1,1,1),_DpL2FdbClearAllMacAddr_Type())
dpL2FdbClearAllMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:dpL2FdbClearAllMacAddr.setStatus(_A)
class _DpL2FdbAgingTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,1000000))
_DpL2FdbAgingTime_Type.__name__=_I
_DpL2FdbAgingTime_Object=MibScalar
dpL2FdbAgingTime=_DpL2FdbAgingTime_Object((1,3,6,1,4,1,171,15,5,1,1,2),_DpL2FdbAgingTime_Type())
dpL2FdbAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dpL2FdbAgingTime.setStatus(_A)
if mibBuilder.loadTexts:dpL2FdbAgingTime.setUnits('second')
_DpL2FdbStaticUnicastTable_Object=MibTable
dpL2FdbStaticUnicastTable=_DpL2FdbStaticUnicastTable_Object((1,3,6,1,4,1,171,15,5,1,2))
if mibBuilder.loadTexts:dpL2FdbStaticUnicastTable.setStatus(_A)
_DpL2FdbStaticUnicastEntry_Object=MibTableRow
dpL2FdbStaticUnicastEntry=_DpL2FdbStaticUnicastEntry_Object((1,3,6,1,4,1,171,15,5,1,2,1))
dpL2FdbStaticUnicastEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:dpL2FdbStaticUnicastEntry.setStatus(_A)
_DpL2FdbStaticUnicastVlanID_Type=VlanId
_DpL2FdbStaticUnicastVlanID_Object=MibTableColumn
dpL2FdbStaticUnicastVlanID=_DpL2FdbStaticUnicastVlanID_Object((1,3,6,1,4,1,171,15,5,1,2,1,1),_DpL2FdbStaticUnicastVlanID_Type())
dpL2FdbStaticUnicastVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpL2FdbStaticUnicastVlanID.setStatus(_A)
_DpL2FdbStaticUnicastMacAddr_Type=MacAddress
_DpL2FdbStaticUnicastMacAddr_Object=MibTableColumn
dpL2FdbStaticUnicastMacAddr=_DpL2FdbStaticUnicastMacAddr_Object((1,3,6,1,4,1,171,15,5,1,2,1,2),_DpL2FdbStaticUnicastMacAddr_Type())
dpL2FdbStaticUnicastMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dpL2FdbStaticUnicastMacAddr.setStatus(_A)
_DpL2FdbStaticUnicastPortNum_Type=Integer32
_DpL2FdbStaticUnicastPortNum_Object=MibTableColumn
dpL2FdbStaticUnicastPortNum=_DpL2FdbStaticUnicastPortNum_Object((1,3,6,1,4,1,171,15,5,1,2,1,3),_DpL2FdbStaticUnicastPortNum_Type())
dpL2FdbStaticUnicastPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:dpL2FdbStaticUnicastPortNum.setStatus(_A)
_DpL2FdbStaticUnicastRowStatus_Type=RowStatus
_DpL2FdbStaticUnicastRowStatus_Object=MibTableColumn
dpL2FdbStaticUnicastRowStatus=_DpL2FdbStaticUnicastRowStatus_Object((1,3,6,1,4,1,171,15,5,1,2,1,4),_DpL2FdbStaticUnicastRowStatus_Type())
dpL2FdbStaticUnicastRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dpL2FdbStaticUnicastRowStatus.setStatus(_A)
_DpL2FdbStaticMulticastTable_Object=MibTable
dpL2FdbStaticMulticastTable=_DpL2FdbStaticMulticastTable_Object((1,3,6,1,4,1,171,15,5,1,3))
if mibBuilder.loadTexts:dpL2FdbStaticMulticastTable.setStatus(_A)
_DpL2FdbStaticMulticastEntry_Object=MibTableRow
dpL2FdbStaticMulticastEntry=_DpL2FdbStaticMulticastEntry_Object((1,3,6,1,4,1,171,15,5,1,3,1))
dpL2FdbStaticMulticastEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:dpL2FdbStaticMulticastEntry.setStatus(_A)
_DpL2FdbStaticMulticastVlanID_Type=VlanId
_DpL2FdbStaticMulticastVlanID_Object=MibTableColumn
dpL2FdbStaticMulticastVlanID=_DpL2FdbStaticMulticastVlanID_Object((1,3,6,1,4,1,171,15,5,1,3,1,1),_DpL2FdbStaticMulticastVlanID_Type())
dpL2FdbStaticMulticastVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:dpL2FdbStaticMulticastVlanID.setStatus(_A)
_DpL2FdbStaticMulticastMacAddr_Type=MacAddress
_DpL2FdbStaticMulticastMacAddr_Object=MibTableColumn
dpL2FdbStaticMulticastMacAddr=_DpL2FdbStaticMulticastMacAddr_Object((1,3,6,1,4,1,171,15,5,1,3,1,2),_DpL2FdbStaticMulticastMacAddr_Type())
dpL2FdbStaticMulticastMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dpL2FdbStaticMulticastMacAddr.setStatus(_A)
_DpL2FdbStaticMulticastEgressPorts_Type=PortList
_DpL2FdbStaticMulticastEgressPorts_Object=MibTableColumn
dpL2FdbStaticMulticastEgressPorts=_DpL2FdbStaticMulticastEgressPorts_Object((1,3,6,1,4,1,171,15,5,1,3,1,3),_DpL2FdbStaticMulticastEgressPorts_Type())
dpL2FdbStaticMulticastEgressPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dpL2FdbStaticMulticastEgressPorts.setStatus(_A)
_DpL2FdbStaticMulticastRowStatus_Type=RowStatus
_DpL2FdbStaticMulticastRowStatus_Object=MibTableColumn
dpL2FdbStaticMulticastRowStatus=_DpL2FdbStaticMulticastRowStatus_Object((1,3,6,1,4,1,171,15,5,1,3,1,4),_DpL2FdbStaticMulticastRowStatus_Type())
dpL2FdbStaticMulticastRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dpL2FdbStaticMulticastRowStatus.setStatus(_A)
_DpL2FdbIfCtrlTable_Object=MibTable
dpL2FdbIfCtrlTable=_DpL2FdbIfCtrlTable_Object((1,3,6,1,4,1,171,15,5,1,4))
if mibBuilder.loadTexts:dpL2FdbIfCtrlTable.setStatus(_A)
_DpL2FdbIfCtrlEntry_Object=MibTableRow
dpL2FdbIfCtrlEntry=_DpL2FdbIfCtrlEntry_Object((1,3,6,1,4,1,171,15,5,1,4,1))
dpL2FdbIfCtrlEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dpL2FdbIfCtrlEntry.setStatus(_A)
_DpL2FdbIfMacLearningEnabled_Type=TruthValue
_DpL2FdbIfMacLearningEnabled_Object=MibTableColumn
dpL2FdbIfMacLearningEnabled=_DpL2FdbIfMacLearningEnabled_Object((1,3,6,1,4,1,171,15,5,1,4,1,1),_DpL2FdbIfMacLearningEnabled_Type())
dpL2FdbIfMacLearningEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpL2FdbIfMacLearningEnabled.setStatus(_A)
class _DpL2FdbMcastFilterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forwardAll',1),('forwardUnregistered',2),('filterUnregistered',3)))
_DpL2FdbMcastFilterMode_Type.__name__=_F
_DpL2FdbMcastFilterMode_Object=MibScalar
dpL2FdbMcastFilterMode=_DpL2FdbMcastFilterMode_Object((1,3,6,1,4,1,171,15,5,1,5),_DpL2FdbMcastFilterMode_Type())
dpL2FdbMcastFilterMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dpL2FdbMcastFilterMode.setStatus(_A)
_DpL2FdbMIBConformance_ObjectIdentity=ObjectIdentity
dpL2FdbMIBConformance=_DpL2FdbMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,5,2))
_DpL2FdbCompliances_ObjectIdentity=ObjectIdentity
dpL2FdbCompliances=_DpL2FdbCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,5,2,1))
_DpL2FdbGroups_ObjectIdentity=ObjectIdentity
dpL2FdbGroups=_DpL2FdbGroups_ObjectIdentity((1,3,6,1,4,1,171,15,5,2,2))
dpL2FdbGlobalGroup=ObjectGroup((1,3,6,1,4,1,171,15,5,2,2,1))
dpL2FdbGlobalGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:dpL2FdbGlobalGroup.setStatus(_A)
dpL2FdbMacAddrTableGroup=ObjectGroup((1,3,6,1,4,1,171,15,5,2,2,2))
dpL2FdbMacAddrTableGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:dpL2FdbMacAddrTableGroup.setStatus(_A)
dpL2FdbInterfaceGroup=ObjectGroup((1,3,6,1,4,1,171,15,5,2,2,3))
dpL2FdbInterfaceGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:dpL2FdbInterfaceGroup.setStatus(_A)
dpL2FdbMcastFilterModeCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,5,2,2,4))
dpL2FdbMcastFilterModeCfgGroup.setObjects((_B,_S))
if mibBuilder.loadTexts:dpL2FdbMcastFilterModeCfgGroup.setStatus(_A)
dpL2FdbCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,5,2,1,1))
dpL2FdbCompliance.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:dpL2FdbCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeL2FdbMIB':dlinkPrimeL2FdbMIB,'dpL2FdbMIBNotifications':dpL2FdbMIBNotifications,'dpL2FdbMIBObjects':dpL2FdbMIBObjects,'dpL2FdbGblCtrl':dpL2FdbGblCtrl,'dpL2FdbClearCtrl':dpL2FdbClearCtrl,_N:dpL2FdbClearAllMacAddr,_O:dpL2FdbAgingTime,'dpL2FdbStaticUnicastTable':dpL2FdbStaticUnicastTable,'dpL2FdbStaticUnicastEntry':dpL2FdbStaticUnicastEntry,_J:dpL2FdbStaticUnicastVlanID,_K:dpL2FdbStaticUnicastMacAddr,_P:dpL2FdbStaticUnicastPortNum,_Q:dpL2FdbStaticUnicastRowStatus,'dpL2FdbStaticMulticastTable':dpL2FdbStaticMulticastTable,'dpL2FdbStaticMulticastEntry':dpL2FdbStaticMulticastEntry,_L:dpL2FdbStaticMulticastVlanID,_M:dpL2FdbStaticMulticastMacAddr,'dpL2FdbStaticMulticastEgressPorts':dpL2FdbStaticMulticastEgressPorts,'dpL2FdbStaticMulticastRowStatus':dpL2FdbStaticMulticastRowStatus,'dpL2FdbIfCtrlTable':dpL2FdbIfCtrlTable,'dpL2FdbIfCtrlEntry':dpL2FdbIfCtrlEntry,_R:dpL2FdbIfMacLearningEnabled,_S:dpL2FdbMcastFilterMode,'dpL2FdbMIBConformance':dpL2FdbMIBConformance,'dpL2FdbCompliances':dpL2FdbCompliances,'dpL2FdbCompliance':dpL2FdbCompliance,'dpL2FdbGroups':dpL2FdbGroups,_T:dpL2FdbGlobalGroup,_U:dpL2FdbMacAddrTableGroup,_V:dpL2FdbInterfaceGroup,_W:dpL2FdbMcastFilterModeCfgGroup})