_S='dpVlanAsymmetricVlanCfgGroup'
_R='dpVlanIfCfgGroup'
_Q='dpVlanAsymVlanStateEnabled'
_P='dpVlanPortIfUntagAllowVlanLstSecond2K'
_O='dpVlanPortIfUntagAllowVlanLstFirst2K'
_N='dpVlanPortIfTagAllowVlanLstSecond2K'
_M='dpVlanPortIfTagAllowVlanLstFirst2K'
_L='dpVlanPortIfAcceptableFrameTypes'
_K='dpVlanPortIfTrunkNativeVlanTagged'
_J='dpVlanPortIfMode'
_I='dpPortBasedVlanIndex'
_H='VlanIdOrNone'
_G='dot1dBasePort'
_F='BRIDGE-MIB'
_E='read-create'
_D='Integer32'
_C='read-write'
_B='DLINKPRIME-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_F,_G)
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
PortList,VlanId,VlanIdOrNone,dot1vProtocolPortGroupId=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId',_H,'dot1vProtocolPortGroupId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlinkPrimeVlanMIB=ModuleIdentity((1,3,6,1,4,1,171,15,26))
if mibBuilder.loadTexts:dlinkPrimeVlanMIB.setRevisions(('2014-04-26 00:00',))
class Dlink2kVlanList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_DpVlanMIBNotifications_ObjectIdentity=ObjectIdentity
dpVlanMIBNotifications=_DpVlanMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,26,0))
_DpVlanMIBObjects_ObjectIdentity=ObjectIdentity
dpVlanMIBObjects=_DpVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,26,1))
_DpVlanPortIfCtrlTable_Object=MibTable
dpVlanPortIfCtrlTable=_DpVlanPortIfCtrlTable_Object((1,3,6,1,4,1,171,15,26,1,1))
if mibBuilder.loadTexts:dpVlanPortIfCtrlTable.setStatus(_A)
_DpVlanPortIfCtrlEntry_Object=MibTableRow
dpVlanPortIfCtrlEntry=_DpVlanPortIfCtrlEntry_Object((1,3,6,1,4,1,171,15,26,1,1,1))
dpVlanPortIfCtrlEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dpVlanPortIfCtrlEntry.setStatus(_A)
class _DpVlanPortIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('access',1),('hybrid',2),('trunk',3),('dot1qTunnel',4),('privateVlanHost',5),('privateVlanPromiscuous',6),('privateVlanTrunkPromiscuous',7),('privateVlanTrunkSecondary',8)))
_DpVlanPortIfMode_Type.__name__=_D
_DpVlanPortIfMode_Object=MibTableColumn
dpVlanPortIfMode=_DpVlanPortIfMode_Object((1,3,6,1,4,1,171,15,26,1,1,1,1),_DpVlanPortIfMode_Type())
dpVlanPortIfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanPortIfMode.setStatus(_A)
_DpVlanPortIfTrunkNativeVlanTagged_Type=TruthValue
_DpVlanPortIfTrunkNativeVlanTagged_Object=MibTableColumn
dpVlanPortIfTrunkNativeVlanTagged=_DpVlanPortIfTrunkNativeVlanTagged_Object((1,3,6,1,4,1,171,15,26,1,1,1,2),_DpVlanPortIfTrunkNativeVlanTagged_Type())
dpVlanPortIfTrunkNativeVlanTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanPortIfTrunkNativeVlanTagged.setStatus(_A)
class _DpVlanPortIfAcceptableFrameTypes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('admitAll',1),('admitUntaggedAndPriority',2),('admitTagged',3)))
_DpVlanPortIfAcceptableFrameTypes_Type.__name__=_D
_DpVlanPortIfAcceptableFrameTypes_Object=MibTableColumn
dpVlanPortIfAcceptableFrameTypes=_DpVlanPortIfAcceptableFrameTypes_Object((1,3,6,1,4,1,171,15,26,1,1,1,3),_DpVlanPortIfAcceptableFrameTypes_Type())
dpVlanPortIfAcceptableFrameTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanPortIfAcceptableFrameTypes.setStatus(_A)
_DpVlanPortIfTagAllowVlanLstFirst2K_Type=Dlink2kVlanList
_DpVlanPortIfTagAllowVlanLstFirst2K_Object=MibTableColumn
dpVlanPortIfTagAllowVlanLstFirst2K=_DpVlanPortIfTagAllowVlanLstFirst2K_Object((1,3,6,1,4,1,171,15,26,1,1,1,4),_DpVlanPortIfTagAllowVlanLstFirst2K_Type())
dpVlanPortIfTagAllowVlanLstFirst2K.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanPortIfTagAllowVlanLstFirst2K.setStatus(_A)
_DpVlanPortIfTagAllowVlanLstSecond2K_Type=Dlink2kVlanList
_DpVlanPortIfTagAllowVlanLstSecond2K_Object=MibTableColumn
dpVlanPortIfTagAllowVlanLstSecond2K=_DpVlanPortIfTagAllowVlanLstSecond2K_Object((1,3,6,1,4,1,171,15,26,1,1,1,5),_DpVlanPortIfTagAllowVlanLstSecond2K_Type())
dpVlanPortIfTagAllowVlanLstSecond2K.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanPortIfTagAllowVlanLstSecond2K.setStatus(_A)
_DpVlanPortIfUntagAllowVlanLstFirst2K_Type=Dlink2kVlanList
_DpVlanPortIfUntagAllowVlanLstFirst2K_Object=MibTableColumn
dpVlanPortIfUntagAllowVlanLstFirst2K=_DpVlanPortIfUntagAllowVlanLstFirst2K_Object((1,3,6,1,4,1,171,15,26,1,1,1,6),_DpVlanPortIfUntagAllowVlanLstFirst2K_Type())
dpVlanPortIfUntagAllowVlanLstFirst2K.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanPortIfUntagAllowVlanLstFirst2K.setStatus(_A)
_DpVlanPortIfUntagAllowVlanLstSecond2K_Type=Dlink2kVlanList
_DpVlanPortIfUntagAllowVlanLstSecond2K_Object=MibTableColumn
dpVlanPortIfUntagAllowVlanLstSecond2K=_DpVlanPortIfUntagAllowVlanLstSecond2K_Object((1,3,6,1,4,1,171,15,26,1,1,1,7),_DpVlanPortIfUntagAllowVlanLstSecond2K_Type())
dpVlanPortIfUntagAllowVlanLstSecond2K.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanPortIfUntagAllowVlanLstSecond2K.setStatus(_A)
_DpVlanAsymVlanStateEnabled_Type=TruthValue
_DpVlanAsymVlanStateEnabled_Object=MibScalar
dpVlanAsymVlanStateEnabled=_DpVlanAsymVlanStateEnabled_Object((1,3,6,1,4,1,171,15,26,1,2),_DpVlanAsymVlanStateEnabled_Type())
dpVlanAsymVlanStateEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanAsymVlanStateEnabled.setStatus(_A)
_DpVlanManagementVlanGlobal_ObjectIdentity=ObjectIdentity
dpVlanManagementVlanGlobal=_DpVlanManagementVlanGlobal_ObjectIdentity((1,3,6,1,4,1,171,15,26,1,3))
_DpVlanManagementVlanEnabled_Type=TruthValue
_DpVlanManagementVlanEnabled_Object=MibScalar
dpVlanManagementVlanEnabled=_DpVlanManagementVlanEnabled_Object((1,3,6,1,4,1,171,15,26,1,3,1),_DpVlanManagementVlanEnabled_Type())
dpVlanManagementVlanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanManagementVlanEnabled.setStatus(_A)
class _DpVlanManagementVlanId_Type(VlanIdOrNone):defaultValue=0
_DpVlanManagementVlanId_Type.__name__=_H
_DpVlanManagementVlanId_Object=MibScalar
dpVlanManagementVlanId=_DpVlanManagementVlanId_Object((1,3,6,1,4,1,171,15,26,1,3,2),_DpVlanManagementVlanId_Type())
dpVlanManagementVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanManagementVlanId.setStatus(_A)
_DpVlanPortBasedVlan_ObjectIdentity=ObjectIdentity
dpVlanPortBasedVlan=_DpVlanPortBasedVlan_ObjectIdentity((1,3,6,1,4,1,171,15,26,1,4))
_DpVlanPortBasedVlanEnabled_Type=TruthValue
_DpVlanPortBasedVlanEnabled_Object=MibScalar
dpVlanPortBasedVlanEnabled=_DpVlanPortBasedVlanEnabled_Object((1,3,6,1,4,1,171,15,26,1,4,1),_DpVlanPortBasedVlanEnabled_Type())
dpVlanPortBasedVlanEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dpVlanPortBasedVlanEnabled.setStatus(_A)
_DpPortBasedVlanTable_Object=MibTable
dpPortBasedVlanTable=_DpPortBasedVlanTable_Object((1,3,6,1,4,1,171,15,26,1,4,2))
if mibBuilder.loadTexts:dpPortBasedVlanTable.setStatus(_A)
_DpPortBasedVlanEntry_Object=MibTableRow
dpPortBasedVlanEntry=_DpPortBasedVlanEntry_Object((1,3,6,1,4,1,171,15,26,1,4,2,1))
dpPortBasedVlanEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:dpPortBasedVlanEntry.setStatus(_A)
_DpPortBasedVlanIndex_Type=Integer32
_DpPortBasedVlanIndex_Object=MibTableColumn
dpPortBasedVlanIndex=_DpPortBasedVlanIndex_Object((1,3,6,1,4,1,171,15,26,1,4,2,1,1),_DpPortBasedVlanIndex_Type())
dpPortBasedVlanIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:dpPortBasedVlanIndex.setStatus(_A)
_DpPortBasedVlanEgressPorts_Type=PortList
_DpPortBasedVlanEgressPorts_Object=MibTableColumn
dpPortBasedVlanEgressPorts=_DpPortBasedVlanEgressPorts_Object((1,3,6,1,4,1,171,15,26,1,4,2,1,2),_DpPortBasedVlanEgressPorts_Type())
dpPortBasedVlanEgressPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:dpPortBasedVlanEgressPorts.setStatus(_A)
_DpPortBasedVlanRowStatus_Type=RowStatus
_DpPortBasedVlanRowStatus_Object=MibTableColumn
dpPortBasedVlanRowStatus=_DpPortBasedVlanRowStatus_Object((1,3,6,1,4,1,171,15,26,1,4,2,1,3),_DpPortBasedVlanRowStatus_Type())
dpPortBasedVlanRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dpPortBasedVlanRowStatus.setStatus(_A)
_DpVlanMIBConformance_ObjectIdentity=ObjectIdentity
dpVlanMIBConformance=_DpVlanMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,26,2))
_DpVlanCompliances_ObjectIdentity=ObjectIdentity
dpVlanCompliances=_DpVlanCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,26,2,1))
_DpVlanGroups_ObjectIdentity=ObjectIdentity
dpVlanGroups=_DpVlanGroups_ObjectIdentity((1,3,6,1,4,1,171,15,26,2,2))
dpVlanIfCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,26,2,2,1))
dpVlanIfCfgGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:dpVlanIfCfgGroup.setStatus(_A)
dpVlanAsymmetricVlanCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,26,2,2,2))
dpVlanAsymmetricVlanCfgGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:dpVlanAsymmetricVlanCfgGroup.setStatus(_A)
dpVlanCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,26,2,1,1))
dpVlanCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:dpVlanCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Dlink2kVlanList':Dlink2kVlanList,'dlinkPrimeVlanMIB':dlinkPrimeVlanMIB,'dpVlanMIBNotifications':dpVlanMIBNotifications,'dpVlanMIBObjects':dpVlanMIBObjects,'dpVlanPortIfCtrlTable':dpVlanPortIfCtrlTable,'dpVlanPortIfCtrlEntry':dpVlanPortIfCtrlEntry,_J:dpVlanPortIfMode,_K:dpVlanPortIfTrunkNativeVlanTagged,_L:dpVlanPortIfAcceptableFrameTypes,_M:dpVlanPortIfTagAllowVlanLstFirst2K,_N:dpVlanPortIfTagAllowVlanLstSecond2K,_O:dpVlanPortIfUntagAllowVlanLstFirst2K,_P:dpVlanPortIfUntagAllowVlanLstSecond2K,_Q:dpVlanAsymVlanStateEnabled,'dpVlanManagementVlanGlobal':dpVlanManagementVlanGlobal,'dpVlanManagementVlanEnabled':dpVlanManagementVlanEnabled,'dpVlanManagementVlanId':dpVlanManagementVlanId,'dpVlanPortBasedVlan':dpVlanPortBasedVlan,'dpVlanPortBasedVlanEnabled':dpVlanPortBasedVlanEnabled,'dpPortBasedVlanTable':dpPortBasedVlanTable,'dpPortBasedVlanEntry':dpPortBasedVlanEntry,_I:dpPortBasedVlanIndex,'dpPortBasedVlanEgressPorts':dpPortBasedVlanEgressPorts,'dpPortBasedVlanRowStatus':dpPortBasedVlanRowStatus,'dpVlanMIBConformance':dpVlanMIBConformance,'dpVlanCompliances':dpVlanCompliances,'dpVlanCompliance':dpVlanCompliance,'dpVlanGroups':dpVlanGroups,_R:dpVlanIfCfgGroup,_S:dpVlanAsymmetricVlanCfgGroup})