_P='dpMgmdSnpVlanIfCfgGoup'
_O='dpMgmdSnpGblCfgGroup'
_N='dpMgmdSnpIfQuerierStateEnabled'
_M='dpMgmdSnpIfStateEnabled'
_L='dpMgmdSnpStateGblEnabled'
_K='read-create'
_J='dpMgmdSnpStaticGrpAddress'
_I='dpMgmdSnpStaticGrpVlanIfIndex'
_H='dpMgmdSnpGroupAddress'
_G='dpMgmdSnpGroupVlanIfIndex'
_F='dpMgmdSnpIfVlanIfIndex'
_E='read-write'
_D='TruthValue'
_C='not-accessible'
_B='DLINKPRIME-MGMD-SNOOPING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
PortList,VlanId,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId','VlanIdOrNone')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
dlinkPrimeMgmdSnoopingMIB=ModuleIdentity((1,3,6,1,4,1,171,15,9))
if mibBuilder.loadTexts:dlinkPrimeMgmdSnoopingMIB.setRevisions(('2014-04-26 00:00',))
class SnoopingType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('igmpSnooping',1),('mldSnooping',2)))
_DpMgmdSnpMIBNotifications_ObjectIdentity=ObjectIdentity
dpMgmdSnpMIBNotifications=_DpMgmdSnpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,9,0))
_DpMgmdSnpMIBObjects_ObjectIdentity=ObjectIdentity
dpMgmdSnpMIBObjects=_DpMgmdSnpMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,9,1))
_DpMgmdSnpGlobalCtrl_ObjectIdentity=ObjectIdentity
dpMgmdSnpGlobalCtrl=_DpMgmdSnpGlobalCtrl_ObjectIdentity((1,3,6,1,4,1,171,15,9,1,1))
class _DpMgmdSnpStateGblEnabled_Type(Bits):namedValues=NamedValues(*(('ipv4',0),('ipv6',1)))
_DpMgmdSnpStateGblEnabled_Type.__name__='Bits'
_DpMgmdSnpStateGblEnabled_Object=MibScalar
dpMgmdSnpStateGblEnabled=_DpMgmdSnpStateGblEnabled_Object((1,3,6,1,4,1,171,15,9,1,1,1),_DpMgmdSnpStateGblEnabled_Type())
dpMgmdSnpStateGblEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:dpMgmdSnpStateGblEnabled.setStatus(_A)
_DpMgmdSnpVlanIfCtrl_ObjectIdentity=ObjectIdentity
dpMgmdSnpVlanIfCtrl=_DpMgmdSnpVlanIfCtrl_ObjectIdentity((1,3,6,1,4,1,171,15,9,1,2))
_DpMgmdSnpIfTable_Object=MibTable
dpMgmdSnpIfTable=_DpMgmdSnpIfTable_Object((1,3,6,1,4,1,171,15,9,1,2,1))
if mibBuilder.loadTexts:dpMgmdSnpIfTable.setStatus(_A)
_DpMgmdSnpIfEntry_Object=MibTableRow
dpMgmdSnpIfEntry=_DpMgmdSnpIfEntry_Object((1,3,6,1,4,1,171,15,9,1,2,1,1))
dpMgmdSnpIfEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:dpMgmdSnpIfEntry.setStatus(_A)
_DpMgmdSnpIfVlanIfIndex_Type=InterfaceIndex
_DpMgmdSnpIfVlanIfIndex_Object=MibTableColumn
dpMgmdSnpIfVlanIfIndex=_DpMgmdSnpIfVlanIfIndex_Object((1,3,6,1,4,1,171,15,9,1,2,1,1,1),_DpMgmdSnpIfVlanIfIndex_Type())
dpMgmdSnpIfVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dpMgmdSnpIfVlanIfIndex.setStatus(_A)
class _DpMgmdSnpIfStateEnabled_Type(TruthValue):defaultValue=2
_DpMgmdSnpIfStateEnabled_Type.__name__=_D
_DpMgmdSnpIfStateEnabled_Object=MibTableColumn
dpMgmdSnpIfStateEnabled=_DpMgmdSnpIfStateEnabled_Object((1,3,6,1,4,1,171,15,9,1,2,1,1,2),_DpMgmdSnpIfStateEnabled_Type())
dpMgmdSnpIfStateEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:dpMgmdSnpIfStateEnabled.setStatus(_A)
class _DpMgmdSnpIfQuerierStateEnabled_Type(TruthValue):defaultValue=2
_DpMgmdSnpIfQuerierStateEnabled_Type.__name__=_D
_DpMgmdSnpIfQuerierStateEnabled_Object=MibTableColumn
dpMgmdSnpIfQuerierStateEnabled=_DpMgmdSnpIfQuerierStateEnabled_Object((1,3,6,1,4,1,171,15,9,1,2,1,1,3),_DpMgmdSnpIfQuerierStateEnabled_Type())
dpMgmdSnpIfQuerierStateEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:dpMgmdSnpIfQuerierStateEnabled.setStatus(_A)
_DpMgmdSnpGroupCtrl_ObjectIdentity=ObjectIdentity
dpMgmdSnpGroupCtrl=_DpMgmdSnpGroupCtrl_ObjectIdentity((1,3,6,1,4,1,171,15,9,1,3))
_DpMgmdSnpGroupTable_Object=MibTable
dpMgmdSnpGroupTable=_DpMgmdSnpGroupTable_Object((1,3,6,1,4,1,171,15,9,1,3,1))
if mibBuilder.loadTexts:dpMgmdSnpGroupTable.setStatus(_A)
_DpMgmdSnpGroupEntry_Object=MibTableRow
dpMgmdSnpGroupEntry=_DpMgmdSnpGroupEntry_Object((1,3,6,1,4,1,171,15,9,1,3,1,1))
dpMgmdSnpGroupEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:dpMgmdSnpGroupEntry.setStatus(_A)
_DpMgmdSnpGroupVlanIfIndex_Type=InterfaceIndex
_DpMgmdSnpGroupVlanIfIndex_Object=MibTableColumn
dpMgmdSnpGroupVlanIfIndex=_DpMgmdSnpGroupVlanIfIndex_Object((1,3,6,1,4,1,171,15,9,1,3,1,1,1),_DpMgmdSnpGroupVlanIfIndex_Type())
dpMgmdSnpGroupVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dpMgmdSnpGroupVlanIfIndex.setStatus(_A)
_DpMgmdSnpGroupAddress_Type=InetAddress
_DpMgmdSnpGroupAddress_Object=MibTableColumn
dpMgmdSnpGroupAddress=_DpMgmdSnpGroupAddress_Object((1,3,6,1,4,1,171,15,9,1,3,1,1,2),_DpMgmdSnpGroupAddress_Type())
dpMgmdSnpGroupAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dpMgmdSnpGroupAddress.setStatus(_A)
_DpMgmdSnpGroupIfIndex_Type=PortList
_DpMgmdSnpGroupIfIndex_Object=MibTableColumn
dpMgmdSnpGroupIfIndex=_DpMgmdSnpGroupIfIndex_Object((1,3,6,1,4,1,171,15,9,1,3,1,1,3),_DpMgmdSnpGroupIfIndex_Type())
dpMgmdSnpGroupIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:dpMgmdSnpGroupIfIndex.setStatus(_A)
_DpMgmdSnpStaticGrpTable_Object=MibTable
dpMgmdSnpStaticGrpTable=_DpMgmdSnpStaticGrpTable_Object((1,3,6,1,4,1,171,15,9,1,3,2))
if mibBuilder.loadTexts:dpMgmdSnpStaticGrpTable.setStatus(_A)
_DpMgmdSnpStaticGrpEntry_Object=MibTableRow
dpMgmdSnpStaticGrpEntry=_DpMgmdSnpStaticGrpEntry_Object((1,3,6,1,4,1,171,15,9,1,3,2,1))
dpMgmdSnpStaticGrpEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:dpMgmdSnpStaticGrpEntry.setStatus(_A)
_DpMgmdSnpStaticGrpVlanIfIndex_Type=InterfaceIndex
_DpMgmdSnpStaticGrpVlanIfIndex_Object=MibTableColumn
dpMgmdSnpStaticGrpVlanIfIndex=_DpMgmdSnpStaticGrpVlanIfIndex_Object((1,3,6,1,4,1,171,15,9,1,3,2,1,1),_DpMgmdSnpStaticGrpVlanIfIndex_Type())
dpMgmdSnpStaticGrpVlanIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dpMgmdSnpStaticGrpVlanIfIndex.setStatus(_A)
_DpMgmdSnpStaticGrpAddress_Type=InetAddress
_DpMgmdSnpStaticGrpAddress_Object=MibTableColumn
dpMgmdSnpStaticGrpAddress=_DpMgmdSnpStaticGrpAddress_Object((1,3,6,1,4,1,171,15,9,1,3,2,1,2),_DpMgmdSnpStaticGrpAddress_Type())
dpMgmdSnpStaticGrpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dpMgmdSnpStaticGrpAddress.setStatus(_A)
_DpMgmdSnpStaticGrpIfIndex_Type=PortList
_DpMgmdSnpStaticGrpIfIndex_Object=MibTableColumn
dpMgmdSnpStaticGrpIfIndex=_DpMgmdSnpStaticGrpIfIndex_Object((1,3,6,1,4,1,171,15,9,1,3,2,1,3),_DpMgmdSnpStaticGrpIfIndex_Type())
dpMgmdSnpStaticGrpIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:dpMgmdSnpStaticGrpIfIndex.setStatus(_A)
_DpMgmdSnpStaticGrpStatus_Type=RowStatus
_DpMgmdSnpStaticGrpStatus_Object=MibTableColumn
dpMgmdSnpStaticGrpStatus=_DpMgmdSnpStaticGrpStatus_Object((1,3,6,1,4,1,171,15,9,1,3,2,1,4),_DpMgmdSnpStaticGrpStatus_Type())
dpMgmdSnpStaticGrpStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:dpMgmdSnpStaticGrpStatus.setStatus(_A)
_DpMgmdSnpMIBConformance_ObjectIdentity=ObjectIdentity
dpMgmdSnpMIBConformance=_DpMgmdSnpMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,9,2))
_DpMgmdSnpCompliances_ObjectIdentity=ObjectIdentity
dpMgmdSnpCompliances=_DpMgmdSnpCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,9,2,1))
_DpMgmdSnpGroups_ObjectIdentity=ObjectIdentity
dpMgmdSnpGroups=_DpMgmdSnpGroups_ObjectIdentity((1,3,6,1,4,1,171,15,9,2,2))
dpMgmdSnpGblCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,9,2,2,1))
dpMgmdSnpGblCfgGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:dpMgmdSnpGblCfgGroup.setStatus(_A)
dpMgmdSnpVlanIfCfgGoup=ObjectGroup((1,3,6,1,4,1,171,15,9,2,2,2))
dpMgmdSnpVlanIfCfgGoup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:dpMgmdSnpVlanIfCfgGoup.setStatus(_A)
dpMgmdSnpCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,9,2,1,1))
dpMgmdSnpCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:dpMgmdSnpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SnoopingType':SnoopingType,'dlinkPrimeMgmdSnoopingMIB':dlinkPrimeMgmdSnoopingMIB,'dpMgmdSnpMIBNotifications':dpMgmdSnpMIBNotifications,'dpMgmdSnpMIBObjects':dpMgmdSnpMIBObjects,'dpMgmdSnpGlobalCtrl':dpMgmdSnpGlobalCtrl,_L:dpMgmdSnpStateGblEnabled,'dpMgmdSnpVlanIfCtrl':dpMgmdSnpVlanIfCtrl,'dpMgmdSnpIfTable':dpMgmdSnpIfTable,'dpMgmdSnpIfEntry':dpMgmdSnpIfEntry,_F:dpMgmdSnpIfVlanIfIndex,_M:dpMgmdSnpIfStateEnabled,_N:dpMgmdSnpIfQuerierStateEnabled,'dpMgmdSnpGroupCtrl':dpMgmdSnpGroupCtrl,'dpMgmdSnpGroupTable':dpMgmdSnpGroupTable,'dpMgmdSnpGroupEntry':dpMgmdSnpGroupEntry,_G:dpMgmdSnpGroupVlanIfIndex,_H:dpMgmdSnpGroupAddress,'dpMgmdSnpGroupIfIndex':dpMgmdSnpGroupIfIndex,'dpMgmdSnpStaticGrpTable':dpMgmdSnpStaticGrpTable,'dpMgmdSnpStaticGrpEntry':dpMgmdSnpStaticGrpEntry,_I:dpMgmdSnpStaticGrpVlanIfIndex,_J:dpMgmdSnpStaticGrpAddress,'dpMgmdSnpStaticGrpIfIndex':dpMgmdSnpStaticGrpIfIndex,'dpMgmdSnpStaticGrpStatus':dpMgmdSnpStaticGrpStatus,'dpMgmdSnpMIBConformance':dpMgmdSnpMIBConformance,'dpMgmdSnpCompliances':dpMgmdSnpCompliances,'dpMgmdSnpCompliance':dpMgmdSnpCompliance,'dpMgmdSnpGroups':dpMgmdSnpGroups,_O:dpMgmdSnpGblCfgGroup,_P:dpMgmdSnpVlanIfCfgGoup})