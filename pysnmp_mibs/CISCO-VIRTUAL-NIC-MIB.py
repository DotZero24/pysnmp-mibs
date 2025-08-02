_a='cvnConnecteeGroup'
_Z='cvnPinningGroup'
_Y='cvnVethGroup'
_X='cvnConnecteeDeviceType'
_W='cvnConnecteeDeviceName'
_V='cvnConnecteeMac'
_U='cvnConnecteeType'
_T='cvnConnecteeUuid'
_S='cvnConnecteeName'
_R='cvnDVSPort'
_Q='cvnConnecteeAttachType'
_P='cvnPinnedSubGrpId'
_O='cvnVethStateReason'
_N='cvnVethIfAdditionalState'
_M='cvnVethIfProfileAlias'
_L='cvnVethPortProfileUsed'
_K='cvnVethHostAddr'
_J='cvnVethHostAddrType'
_I='cvnVethHostID'
_H='cvnVethOwner'
_G='cvnVethAdapter'
_F='unknown'
_E='cvnVethInterface'
_D='Integer32'
_C='read-only'
_B='CISCO-VIRTUAL-NIC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
ciscoVirtualNicMIB=ModuleIdentity((1,3,6,1,4,1,9,9,710))
if mibBuilder.loadTexts:ciscoVirtualNicMIB.setRevisions(('2009-10-26 00:00',))
_CiscoVirtualNicMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVirtualNicMIBNotifs=_CiscoVirtualNicMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,710,0))
_CiscoVirtualNicMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVirtualNicMIBObjects=_CiscoVirtualNicMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,710,1))
_CvnInterfaceObjects_ObjectIdentity=ObjectIdentity
cvnInterfaceObjects=_CvnInterfaceObjects_ObjectIdentity((1,3,6,1,4,1,9,9,710,1,1))
_CvnVethIfTable_Object=MibTable
cvnVethIfTable=_CvnVethIfTable_Object((1,3,6,1,4,1,9,9,710,1,1,1))
if mibBuilder.loadTexts:cvnVethIfTable.setStatus(_A)
_CvnVethIfEntry_Object=MibTableRow
cvnVethIfEntry=_CvnVethIfEntry_Object((1,3,6,1,4,1,9,9,710,1,1,1,1))
cvnVethIfEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cvnVethIfEntry.setStatus(_A)
_CvnVethInterface_Type=InterfaceIndex
_CvnVethInterface_Object=MibTableColumn
cvnVethInterface=_CvnVethInterface_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,1),_CvnVethInterface_Type())
cvnVethInterface.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cvnVethInterface.setStatus(_A)
_CvnVethAdapter_Type=SnmpAdminString
_CvnVethAdapter_Object=MibTableColumn
cvnVethAdapter=_CvnVethAdapter_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,2),_CvnVethAdapter_Type())
cvnVethAdapter.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnVethAdapter.setStatus(_A)
_CvnVethOwner_Type=SnmpAdminString
_CvnVethOwner_Object=MibTableColumn
cvnVethOwner=_CvnVethOwner_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,3),_CvnVethOwner_Type())
cvnVethOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnVethOwner.setStatus(_A)
_CvnVethHostID_Type=Unsigned32
_CvnVethHostID_Object=MibTableColumn
cvnVethHostID=_CvnVethHostID_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,4),_CvnVethHostID_Type())
cvnVethHostID.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnVethHostID.setStatus(_A)
_CvnVethHostAddrType_Type=InetAddressType
_CvnVethHostAddrType_Object=MibTableColumn
cvnVethHostAddrType=_CvnVethHostAddrType_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,5),_CvnVethHostAddrType_Type())
cvnVethHostAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnVethHostAddrType.setStatus(_A)
_CvnVethHostAddr_Type=InetAddress
_CvnVethHostAddr_Object=MibTableColumn
cvnVethHostAddr=_CvnVethHostAddr_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,6),_CvnVethHostAddr_Type())
cvnVethHostAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnVethHostAddr.setStatus(_A)
_CvnVethPortProfileUsed_Type=SnmpAdminString
_CvnVethPortProfileUsed_Object=MibTableColumn
cvnVethPortProfileUsed=_CvnVethPortProfileUsed_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,7),_CvnVethPortProfileUsed_Type())
cvnVethPortProfileUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnVethPortProfileUsed.setStatus(_A)
_CvnVethIfProfileAlias_Type=SnmpAdminString
_CvnVethIfProfileAlias_Object=MibTableColumn
cvnVethIfProfileAlias=_CvnVethIfProfileAlias_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,8),_CvnVethIfProfileAlias_Type())
cvnVethIfProfileAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnVethIfProfileAlias.setStatus(_A)
class _CvnVethIfAdditionalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('participating',2),('suspended',3),('errDisabled',4),('nonParticipating',5)))
_CvnVethIfAdditionalState_Type.__name__=_D
_CvnVethIfAdditionalState_Object=MibTableColumn
cvnVethIfAdditionalState=_CvnVethIfAdditionalState_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,9),_CvnVethIfAdditionalState_Type())
cvnVethIfAdditionalState.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnVethIfAdditionalState.setStatus(_A)
_CvnVethStateReason_Type=SnmpAdminString
_CvnVethStateReason_Object=MibTableColumn
cvnVethStateReason=_CvnVethStateReason_Object((1,3,6,1,4,1,9,9,710,1,1,1,1,10),_CvnVethStateReason_Type())
cvnVethStateReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnVethStateReason.setStatus(_A)
_CvnPinningTable_Object=MibTable
cvnPinningTable=_CvnPinningTable_Object((1,3,6,1,4,1,9,9,710,1,1,2))
if mibBuilder.loadTexts:cvnPinningTable.setStatus(_A)
_CvnPinningEntry_Object=MibTableRow
cvnPinningEntry=_CvnPinningEntry_Object((1,3,6,1,4,1,9,9,710,1,1,2,1))
cvnPinningEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cvnPinningEntry.setStatus(_A)
class _CvnPinnedSubGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CvnPinnedSubGrpId_Type.__name__=_D
_CvnPinnedSubGrpId_Object=MibTableColumn
cvnPinnedSubGrpId=_CvnPinnedSubGrpId_Object((1,3,6,1,4,1,9,9,710,1,1,2,1,1),_CvnPinnedSubGrpId_Type())
cvnPinnedSubGrpId.setMaxAccess('read-write')
if mibBuilder.loadTexts:cvnPinnedSubGrpId.setStatus(_A)
_CvnConnecteeObjects_ObjectIdentity=ObjectIdentity
cvnConnecteeObjects=_CvnConnecteeObjects_ObjectIdentity((1,3,6,1,4,1,9,9,710,1,2))
_CvnConnecteeTable_Object=MibTable
cvnConnecteeTable=_CvnConnecteeTable_Object((1,3,6,1,4,1,9,9,710,1,2,1))
if mibBuilder.loadTexts:cvnConnecteeTable.setStatus(_A)
_CvnConnecteeEntry_Object=MibTableRow
cvnConnecteeEntry=_CvnConnecteeEntry_Object((1,3,6,1,4,1,9,9,710,1,2,1,1))
cvnConnecteeEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cvnConnecteeEntry.setStatus(_A)
class _CvnConnecteeAttachType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('vem',2),('niv',3)))
_CvnConnecteeAttachType_Type.__name__=_D
_CvnConnecteeAttachType_Object=MibTableColumn
cvnConnecteeAttachType=_CvnConnecteeAttachType_Object((1,3,6,1,4,1,9,9,710,1,2,1,1,1),_CvnConnecteeAttachType_Type())
cvnConnecteeAttachType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnConnecteeAttachType.setStatus(_A)
_CvnDVSPort_Type=Unsigned32
_CvnDVSPort_Object=MibTableColumn
cvnDVSPort=_CvnDVSPort_Object((1,3,6,1,4,1,9,9,710,1,2,1,1,2),_CvnDVSPort_Type())
cvnDVSPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnDVSPort.setStatus(_A)
_CvnConnecteeName_Type=SnmpAdminString
_CvnConnecteeName_Object=MibTableColumn
cvnConnecteeName=_CvnConnecteeName_Object((1,3,6,1,4,1,9,9,710,1,2,1,1,3),_CvnConnecteeName_Type())
cvnConnecteeName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnConnecteeName.setStatus(_A)
_CvnConnecteeUuid_Type=SnmpAdminString
_CvnConnecteeUuid_Object=MibTableColumn
cvnConnecteeUuid=_CvnConnecteeUuid_Object((1,3,6,1,4,1,9,9,710,1,2,1,1,4),_CvnConnecteeUuid_Type())
cvnConnecteeUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnConnecteeUuid.setStatus(_A)
class _CvnConnecteeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('vmwareVm',2),('vmwareHost',3)))
_CvnConnecteeType_Type.__name__=_D
_CvnConnecteeType_Object=MibTableColumn
cvnConnecteeType=_CvnConnecteeType_Object((1,3,6,1,4,1,9,9,710,1,2,1,1,5),_CvnConnecteeType_Type())
cvnConnecteeType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnConnecteeType.setStatus(_A)
_CvnConnecteeMac_Type=MacAddress
_CvnConnecteeMac_Object=MibTableColumn
cvnConnecteeMac=_CvnConnecteeMac_Object((1,3,6,1,4,1,9,9,710,1,2,1,1,6),_CvnConnecteeMac_Type())
cvnConnecteeMac.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnConnecteeMac.setStatus(_A)
_CvnConnecteeDeviceName_Type=SnmpAdminString
_CvnConnecteeDeviceName_Object=MibTableColumn
cvnConnecteeDeviceName=_CvnConnecteeDeviceName_Object((1,3,6,1,4,1,9,9,710,1,2,1,1,7),_CvnConnecteeDeviceName_Type())
cvnConnecteeDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnConnecteeDeviceName.setStatus(_A)
class _CvnConnecteeDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),('pnic',2),('vnic',3),('vswif',4),('vmknic',5)))
_CvnConnecteeDeviceType_Type.__name__=_D
_CvnConnecteeDeviceType_Object=MibTableColumn
cvnConnecteeDeviceType=_CvnConnecteeDeviceType_Object((1,3,6,1,4,1,9,9,710,1,2,1,1,8),_CvnConnecteeDeviceType_Type())
cvnConnecteeDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvnConnecteeDeviceType.setStatus(_A)
_CiscoVirtualNicMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVirtualNicMIBConformance=_CiscoVirtualNicMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,710,2))
_CiscoVirtualNicMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVirtualNicMIBCompliances=_CiscoVirtualNicMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,710,2,1))
_CiscoVirtualNicMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVirtualNicMIBGroups=_CiscoVirtualNicMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,710,2,2))
cvnVethGroup=ObjectGroup((1,3,6,1,4,1,9,9,710,2,2,1))
cvnVethGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cvnVethGroup.setStatus(_A)
cvnPinningGroup=ObjectGroup((1,3,6,1,4,1,9,9,710,2,2,2))
cvnPinningGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:cvnPinningGroup.setStatus(_A)
cvnConnecteeGroup=ObjectGroup((1,3,6,1,4,1,9,9,710,2,2,3))
cvnConnecteeGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cvnConnecteeGroup.setStatus(_A)
virtualNicMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,710,2,1,1))
virtualNicMIBCompliance.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:virtualNicMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVirtualNicMIB':ciscoVirtualNicMIB,'ciscoVirtualNicMIBNotifs':ciscoVirtualNicMIBNotifs,'ciscoVirtualNicMIBObjects':ciscoVirtualNicMIBObjects,'cvnInterfaceObjects':cvnInterfaceObjects,'cvnVethIfTable':cvnVethIfTable,'cvnVethIfEntry':cvnVethIfEntry,_E:cvnVethInterface,_G:cvnVethAdapter,_H:cvnVethOwner,_I:cvnVethHostID,_J:cvnVethHostAddrType,_K:cvnVethHostAddr,_L:cvnVethPortProfileUsed,_M:cvnVethIfProfileAlias,_N:cvnVethIfAdditionalState,_O:cvnVethStateReason,'cvnPinningTable':cvnPinningTable,'cvnPinningEntry':cvnPinningEntry,_P:cvnPinnedSubGrpId,'cvnConnecteeObjects':cvnConnecteeObjects,'cvnConnecteeTable':cvnConnecteeTable,'cvnConnecteeEntry':cvnConnecteeEntry,_Q:cvnConnecteeAttachType,_R:cvnDVSPort,_S:cvnConnecteeName,_T:cvnConnecteeUuid,_U:cvnConnecteeType,_V:cvnConnecteeMac,_W:cvnConnecteeDeviceName,_X:cvnConnecteeDeviceType,'ciscoVirtualNicMIBConformance':ciscoVirtualNicMIBConformance,'ciscoVirtualNicMIBCompliances':ciscoVirtualNicMIBCompliances,'virtualNicMIBCompliance':virtualNicMIBCompliance,'ciscoVirtualNicMIBGroups':ciscoVirtualNicMIBGroups,_Y:cvnVethGroup,_Z:cvnPinningGroup,_a:cvnConnecteeGroup})