_I='read-only'
_H='secondaryVlan'
_G='TPLINK-PRIVATE-VLAN-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkPrivateVlanMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,18))
if mibBuilder.loadTexts:tplinkPrivateVlanMIB.setRevisions(('2010-12-20 00:00',))
_TplinkPrivateVlanMIBObjects_ObjectIdentity=ObjectIdentity
tplinkPrivateVlanMIBObjects=_TplinkPrivateVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,18,1))
_PrivateVlanTable_Object=MibTable
privateVlanTable=_PrivateVlanTable_Object((1,3,6,1,4,1,11863,6,18,1,1))
if mibBuilder.loadTexts:privateVlanTable.setStatus(_A)
_PrivateVlanEntry_Object=MibTableRow
privateVlanEntry=_PrivateVlanEntry_Object((1,3,6,1,4,1,11863,6,18,1,1,1))
privateVlanEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:privateVlanEntry.setStatus(_A)
class _SecondaryVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_SecondaryVlan_Type.__name__=_C
_SecondaryVlan_Object=MibTableColumn
secondaryVlan=_SecondaryVlan_Object((1,3,6,1,4,1,11863,6,18,1,1,1,1),_SecondaryVlan_Type())
secondaryVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:secondaryVlan.setStatus(_A)
class _PrimaryVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_PrimaryVlan_Type.__name__=_C
_PrimaryVlan_Object=MibTableColumn
primaryVlan=_PrimaryVlan_Object((1,3,6,1,4,1,11863,6,18,1,1,1,2),_PrimaryVlan_Type())
primaryVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:primaryVlan.setStatus(_A)
class _PrivateVlanPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PrivateVlanPort_Type.__name__=_D
_PrivateVlanPort_Object=MibTableColumn
privateVlanPort=_PrivateVlanPort_Object((1,3,6,1,4,1,11863,6,18,1,1,1,3),_PrivateVlanPort_Type())
privateVlanPort.setMaxAccess(_I)
if mibBuilder.loadTexts:privateVlanPort.setStatus(_A)
class _PrivateVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('community',1),('isolated',2)))
_PrivateVlanType_Type.__name__=_C
_PrivateVlanType_Object=MibTableColumn
privateVlanType=_PrivateVlanType_Object((1,3,6,1,4,1,11863,6,18,1,1,1,4),_PrivateVlanType_Type())
privateVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:privateVlanType.setStatus(_A)
_PrivateVlanStatus_Type=TPRowStatus
_PrivateVlanStatus_Object=MibTableColumn
privateVlanStatus=_PrivateVlanStatus_Object((1,3,6,1,4,1,11863,6,18,1,1,1,5),_PrivateVlanStatus_Type())
privateVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:privateVlanStatus.setStatus(_A)
_PrivateVlanPortTable_Object=MibTable
privateVlanPortTable=_PrivateVlanPortTable_Object((1,3,6,1,4,1,11863,6,18,1,2))
if mibBuilder.loadTexts:privateVlanPortTable.setStatus(_A)
_PrivateVlanPortEntry_Object=MibTableRow
privateVlanPortEntry=_PrivateVlanPortEntry_Object((1,3,6,1,4,1,11863,6,18,1,2,1))
privateVlanPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:privateVlanPortEntry.setStatus(_A)
class _PortNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortNum_Type.__name__=_D
_PortNum_Object=MibTableColumn
portNum=_PortNum_Object((1,3,6,1,4,1,11863,6,18,1,2,1,1),_PortNum_Type())
portNum.setMaxAccess(_I)
if mibBuilder.loadTexts:portNum.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('promiscuous',1),('host',2)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,11863,6,18,1,2,1,2),_PortType_Type())
portType.setMaxAccess(_B)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortConfigPrimaryVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_PortConfigPrimaryVlan_Type.__name__=_C
_PortConfigPrimaryVlan_Object=MibTableColumn
portConfigPrimaryVlan=_PortConfigPrimaryVlan_Object((1,3,6,1,4,1,11863,6,18,1,2,1,3),_PortConfigPrimaryVlan_Type())
portConfigPrimaryVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigPrimaryVlan.setStatus(_A)
class _PortConfigsecondaryVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_PortConfigsecondaryVlan_Type.__name__=_C
_PortConfigsecondaryVlan_Object=MibTableColumn
portConfigsecondaryVlan=_PortConfigsecondaryVlan_Object((1,3,6,1,4,1,11863,6,18,1,2,1,4),_PortConfigsecondaryVlan_Type())
portConfigsecondaryVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:portConfigsecondaryVlan.setStatus(_A)
_VlanPortStatus_Type=TPRowStatus
_VlanPortStatus_Object=MibTableColumn
vlanPortStatus=_VlanPortStatus_Object((1,3,6,1,4,1,11863,6,18,1,2,1,5),_VlanPortStatus_Type())
vlanPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortStatus.setStatus(_A)
_TplinkPrivateVlanMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkPrivateVlanMIBNotifications=_TplinkPrivateVlanMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,18,2))
mibBuilder.exportSymbols(_G,**{'tplinkPrivateVlanMIB':tplinkPrivateVlanMIB,'tplinkPrivateVlanMIBObjects':tplinkPrivateVlanMIBObjects,'privateVlanTable':privateVlanTable,'privateVlanEntry':privateVlanEntry,_H:secondaryVlan,'primaryVlan':primaryVlan,'privateVlanPort':privateVlanPort,'privateVlanType':privateVlanType,'privateVlanStatus':privateVlanStatus,'privateVlanPortTable':privateVlanPortTable,'privateVlanPortEntry':privateVlanPortEntry,'portNum':portNum,'portType':portType,'portConfigPrimaryVlan':portConfigPrimaryVlan,'portConfigsecondaryVlan':portConfigsecondaryVlan,'vlanPortStatus':vlanPortStatus,'tplinkPrivateVlanMIBNotifications':tplinkPrivateVlanMIBNotifications})