_M='vpnConfigVlanMappingPort'
_L='vpnConfigVlanMappingCVlan'
_K='read-only'
_J='ifIndex'
_I='IF-MIB'
_H='TPLINK-VLAN-QINQ-MIB'
_G='enable'
_F='disable'
_E='OctetString'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkQinqVlanMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,17))
if mibBuilder.loadTexts:tplinkQinqVlanMIB.setRevisions(('2008-12-16 00:00',))
_TplinkQinqVlanMIBObjects_ObjectIdentity=ObjectIdentity
tplinkQinqVlanMIBObjects=_TplinkQinqVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,17,1))
class _VpnConfigVpnMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VpnConfigVpnMode_Type.__name__=_B
_VpnConfigVpnMode_Object=MibScalar
vpnConfigVpnMode=_VpnConfigVpnMode_Object((1,3,6,1,4,1,11863,6,17,1,1),_VpnConfigVpnMode_Type())
vpnConfigVpnMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnConfigVpnMode.setStatus(_A)
_VpnConfigPort_ObjectIdentity=ObjectIdentity
vpnConfigPort=_VpnConfigPort_ObjectIdentity((1,3,6,1,4,1,11863,6,17,1,2))
_VpnConfigPortTable_Object=MibTable
vpnConfigPortTable=_VpnConfigPortTable_Object((1,3,6,1,4,1,11863,6,17,1,2,1))
if mibBuilder.loadTexts:vpnConfigPortTable.setStatus(_A)
_VpnConfigPortEntry_Object=MibTableRow
vpnConfigPortEntry=_VpnConfigPortEntry_Object((1,3,6,1,4,1,11863,6,17,1,2,1,1))
vpnConfigPortEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:vpnConfigPortEntry.setStatus(_A)
class _VpnConfigPortNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VpnConfigPortNumber_Type.__name__=_E
_VpnConfigPortNumber_Object=MibTableColumn
vpnConfigPortNumber=_VpnConfigPortNumber_Object((1,3,6,1,4,1,11863,6,17,1,2,1,1,1),_VpnConfigPortNumber_Type())
vpnConfigPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:vpnConfigPortNumber.setStatus(_A)
class _VpnConfigPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('nni',1),('uni',2)))
_VpnConfigPortType_Type.__name__=_B
_VpnConfigPortType_Object=MibTableColumn
vpnConfigPortType=_VpnConfigPortType_Object((1,3,6,1,4,1,11863,6,17,1,2,1,1,2),_VpnConfigPortType_Type())
vpnConfigPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnConfigPortType.setStatus(_A)
class _VpnConfigPortTpid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_VpnConfigPortTpid_Type.__name__=_E
_VpnConfigPortTpid_Object=MibTableColumn
vpnConfigPortTpid=_VpnConfigPortTpid_Object((1,3,6,1,4,1,11863,6,17,1,2,1,1,3),_VpnConfigPortTpid_Type())
vpnConfigPortTpid.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnConfigPortTpid.setStatus(_A)
class _VpnConfigUseInnerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VpnConfigUseInnerPriority_Type.__name__=_B
_VpnConfigUseInnerPriority_Object=MibTableColumn
vpnConfigUseInnerPriority=_VpnConfigUseInnerPriority_Object((1,3,6,1,4,1,11863,6,17,1,2,1,1,4),_VpnConfigUseInnerPriority_Type())
vpnConfigUseInnerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnConfigUseInnerPriority.setStatus(_A)
class _VpnConfigMissdrop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VpnConfigMissdrop_Type.__name__=_B
_VpnConfigMissdrop_Object=MibTableColumn
vpnConfigMissdrop=_VpnConfigMissdrop_Object((1,3,6,1,4,1,11863,6,17,1,2,1,1,5),_VpnConfigMissdrop_Type())
vpnConfigMissdrop.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnConfigMissdrop.setStatus(_A)
class _VpnConfigPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VpnConfigPortLag_Type.__name__=_E
_VpnConfigPortLag_Object=MibTableColumn
vpnConfigPortLag=_VpnConfigPortLag_Object((1,3,6,1,4,1,11863,6,17,1,2,1,1,6),_VpnConfigPortLag_Type())
vpnConfigPortLag.setMaxAccess(_K)
if mibBuilder.loadTexts:vpnConfigPortLag.setStatus(_A)
_VpnConfigVlanMapping_ObjectIdentity=ObjectIdentity
vpnConfigVlanMapping=_VpnConfigVlanMapping_ObjectIdentity((1,3,6,1,4,1,11863,6,17,1,3))
class _VpnConfigVlanMappingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_VpnConfigVlanMappingMode_Type.__name__=_B
_VpnConfigVlanMappingMode_Object=MibScalar
vpnConfigVlanMappingMode=_VpnConfigVlanMappingMode_Object((1,3,6,1,4,1,11863,6,17,1,3,1),_VpnConfigVlanMappingMode_Type())
vpnConfigVlanMappingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vpnConfigVlanMappingMode.setStatus(_A)
_VpnConfigVlanMappingTable_Object=MibTable
vpnConfigVlanMappingTable=_VpnConfigVlanMappingTable_Object((1,3,6,1,4,1,11863,6,17,1,3,2))
if mibBuilder.loadTexts:vpnConfigVlanMappingTable.setStatus(_A)
_VpnConfigVlanMappingEntry_Object=MibTableRow
vpnConfigVlanMappingEntry=_VpnConfigVlanMappingEntry_Object((1,3,6,1,4,1,11863,6,17,1,3,2,1))
vpnConfigVlanMappingEntry.setIndexNames((0,_H,_L),(0,_H,_M))
if mibBuilder.loadTexts:vpnConfigVlanMappingEntry.setStatus(_A)
_VpnConfigVlanMappingPort_Type=OctetString
_VpnConfigVlanMappingPort_Object=MibTableColumn
vpnConfigVlanMappingPort=_VpnConfigVlanMappingPort_Object((1,3,6,1,4,1,11863,6,17,1,3,2,1,1),_VpnConfigVlanMappingPort_Type())
vpnConfigVlanMappingPort.setMaxAccess(_D)
if mibBuilder.loadTexts:vpnConfigVlanMappingPort.setStatus(_A)
class _VpnConfigVlanMappingCVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VpnConfigVlanMappingCVlan_Type.__name__=_B
_VpnConfigVlanMappingCVlan_Object=MibTableColumn
vpnConfigVlanMappingCVlan=_VpnConfigVlanMappingCVlan_Object((1,3,6,1,4,1,11863,6,17,1,3,2,1,2),_VpnConfigVlanMappingCVlan_Type())
vpnConfigVlanMappingCVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:vpnConfigVlanMappingCVlan.setStatus(_A)
class _VpnConfigVlanMappingSPVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VpnConfigVlanMappingSPVlan_Type.__name__=_B
_VpnConfigVlanMappingSPVlan_Object=MibTableColumn
vpnConfigVlanMappingSPVlan=_VpnConfigVlanMappingSPVlan_Object((1,3,6,1,4,1,11863,6,17,1,3,2,1,3),_VpnConfigVlanMappingSPVlan_Type())
vpnConfigVlanMappingSPVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:vpnConfigVlanMappingSPVlan.setStatus(_A)
_VpnConfigVlanMappingDesc_Type=OctetString
_VpnConfigVlanMappingDesc_Object=MibTableColumn
vpnConfigVlanMappingDesc=_VpnConfigVlanMappingDesc_Object((1,3,6,1,4,1,11863,6,17,1,3,2,1,4),_VpnConfigVlanMappingDesc_Type())
vpnConfigVlanMappingDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:vpnConfigVlanMappingDesc.setStatus(_A)
_VpnConfigVlanMappingStatus_Type=TPRowStatus
_VpnConfigVlanMappingStatus_Object=MibTableColumn
vpnConfigVlanMappingStatus=_VpnConfigVlanMappingStatus_Object((1,3,6,1,4,1,11863,6,17,1,3,2,1,5),_VpnConfigVlanMappingStatus_Type())
vpnConfigVlanMappingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vpnConfigVlanMappingStatus.setStatus(_A)
_TplinkQinqVlanMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkQinqVlanMIBNotifications=_TplinkQinqVlanMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,17,2))
mibBuilder.exportSymbols(_H,**{'tplinkQinqVlanMIB':tplinkQinqVlanMIB,'tplinkQinqVlanMIBObjects':tplinkQinqVlanMIBObjects,'vpnConfigVpnMode':vpnConfigVpnMode,'vpnConfigPort':vpnConfigPort,'vpnConfigPortTable':vpnConfigPortTable,'vpnConfigPortEntry':vpnConfigPortEntry,'vpnConfigPortNumber':vpnConfigPortNumber,'vpnConfigPortType':vpnConfigPortType,'vpnConfigPortTpid':vpnConfigPortTpid,'vpnConfigUseInnerPriority':vpnConfigUseInnerPriority,'vpnConfigMissdrop':vpnConfigMissdrop,'vpnConfigPortLag':vpnConfigPortLag,'vpnConfigVlanMapping':vpnConfigVlanMapping,'vpnConfigVlanMappingMode':vpnConfigVlanMappingMode,'vpnConfigVlanMappingTable':vpnConfigVlanMappingTable,'vpnConfigVlanMappingEntry':vpnConfigVlanMappingEntry,_M:vpnConfigVlanMappingPort,_L:vpnConfigVlanMappingCVlan,'vpnConfigVlanMappingSPVlan':vpnConfigVlanMappingSPVlan,'vpnConfigVlanMappingDesc':vpnConfigVlanMappingDesc,'vpnConfigVlanMappingStatus':vpnConfigVlanMappingStatus,'tplinkQinqVlanMIBNotifications':tplinkQinqVlanMIBNotifications})