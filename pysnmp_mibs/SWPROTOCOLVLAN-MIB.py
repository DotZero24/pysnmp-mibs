_H='swdot1vProtocolPortEntry'
_G='swProtocolVLANIndex'
_F='DisplayString'
_E='current'
_D='SWPROTOCOLVLAN-MIB'
_C='Integer32'
_B='read-create'
_A='obsolete'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
dot1vProtocolPortEntry,=mibBuilder.importSymbols('Q-BRIDGE-MIB','dot1vProtocolPortEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
swProtocolVLANMIB=ModuleIdentity((1,3,6,1,4,1,171,12,16))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwProtocolVLANCtrl_ObjectIdentity=ObjectIdentity
swProtocolVLANCtrl=_SwProtocolVLANCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,16,1))
_SwProtocolVLANTable_Object=MibTable
swProtocolVLANTable=_SwProtocolVLANTable_Object((1,3,6,1,4,1,171,12,16,1,1))
if mibBuilder.loadTexts:swProtocolVLANTable.setStatus(_A)
_SwProtocolVLANEntry_Object=MibTableRow
swProtocolVLANEntry=_SwProtocolVLANEntry_Object((1,3,6,1,4,1,171,12,16,1,1,1))
swProtocolVLANEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:swProtocolVLANEntry.setStatus(_A)
class _SwProtocolVLANIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwProtocolVLANIndex_Type.__name__=_C
_SwProtocolVLANIndex_Object=MibTableColumn
swProtocolVLANIndex=_SwProtocolVLANIndex_Object((1,3,6,1,4,1,171,12,16,1,1,1,1),_SwProtocolVLANIndex_Type())
swProtocolVLANIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:swProtocolVLANIndex.setStatus(_A)
class _SwProtocolVLANName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_SwProtocolVLANName_Type.__name__=_F
_SwProtocolVLANName_Object=MibTableColumn
swProtocolVLANName=_SwProtocolVLANName_Object((1,3,6,1,4,1,171,12,16,1,1,1,2),_SwProtocolVLANName_Type())
swProtocolVLANName.setMaxAccess(_B)
if mibBuilder.loadTexts:swProtocolVLANName.setStatus(_A)
class _SwProtocolVLANProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('dot1q-vlan',1),('protocol-ip',2),('protocol-ipx803dot3',3),('protocol-ipx802dot2',4),('protocol-ipxSnap',5),('protocol-ipxEthernet2',6),('protocol-appleTalk',7),('protocol-decLat',8),('protocol-dexOther',9),('protocol-sna802dot2',10),('protocol-snaEthernet2',11),('protocol-netBios',12),('protocol-xns',13),('protocol-vines',14),('protocol-ipV6',15),('protocol-userDefined',16),('protocol-rarp',17)))
_SwProtocolVLANProtocolType_Type.__name__=_C
_SwProtocolVLANProtocolType_Object=MibTableColumn
swProtocolVLANProtocolType=_SwProtocolVLANProtocolType_Object((1,3,6,1,4,1,171,12,16,1,1,1,3),_SwProtocolVLANProtocolType_Type())
swProtocolVLANProtocolType.setMaxAccess(_B)
if mibBuilder.loadTexts:swProtocolVLANProtocolType.setStatus(_A)
class _SwProtocolVLANAdvertisement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_SwProtocolVLANAdvertisement_Type.__name__=_C
_SwProtocolVLANAdvertisement_Object=MibTableColumn
swProtocolVLANAdvertisement=_SwProtocolVLANAdvertisement_Object((1,3,6,1,4,1,171,12,16,1,1,1,4),_SwProtocolVLANAdvertisement_Type())
swProtocolVLANAdvertisement.setMaxAccess(_B)
if mibBuilder.loadTexts:swProtocolVLANAdvertisement.setStatus(_A)
class _SwProtocolVLANUserDefinedProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwProtocolVLANUserDefinedProtocol_Type.__name__=_C
_SwProtocolVLANUserDefinedProtocol_Object=MibTableColumn
swProtocolVLANUserDefinedProtocol=_SwProtocolVLANUserDefinedProtocol_Object((1,3,6,1,4,1,171,12,16,1,1,1,5),_SwProtocolVLANUserDefinedProtocol_Type())
swProtocolVLANUserDefinedProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:swProtocolVLANUserDefinedProtocol.setStatus(_A)
class _SwProtocolVLANencap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ethernet',1),('llc',2),('snap',3),('all',4)))
_SwProtocolVLANencap_Type.__name__=_C
_SwProtocolVLANencap_Object=MibTableColumn
swProtocolVLANencap=_SwProtocolVLANencap_Object((1,3,6,1,4,1,171,12,16,1,1,1,6),_SwProtocolVLANencap_Type())
swProtocolVLANencap.setMaxAccess(_B)
if mibBuilder.loadTexts:swProtocolVLANencap.setStatus(_A)
_SwProtocolVLANRowStatus_Type=RowStatus
_SwProtocolVLANRowStatus_Object=MibTableColumn
swProtocolVLANRowStatus=_SwProtocolVLANRowStatus_Object((1,3,6,1,4,1,171,12,16,1,1,1,7),_SwProtocolVLANRowStatus_Type())
swProtocolVLANRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swProtocolVLANRowStatus.setStatus(_A)
_Swdot1vProtocolPortTable_Object=MibTable
swdot1vProtocolPortTable=_Swdot1vProtocolPortTable_Object((1,3,6,1,4,1,171,12,16,1,2))
if mibBuilder.loadTexts:swdot1vProtocolPortTable.setStatus(_E)
_Swdot1vProtocolPortEntry_Object=MibTableRow
swdot1vProtocolPortEntry=_Swdot1vProtocolPortEntry_Object((1,3,6,1,4,1,171,12,16,1,2,1))
if mibBuilder.loadTexts:swdot1vProtocolPortEntry.setStatus(_E)
class _Swdot1vProtocolPortGroupPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Swdot1vProtocolPortGroupPriority_Type.__name__=_C
_Swdot1vProtocolPortGroupPriority_Object=MibTableColumn
swdot1vProtocolPortGroupPriority=_Swdot1vProtocolPortGroupPriority_Object((1,3,6,1,4,1,171,12,16,1,2,1,1),_Swdot1vProtocolPortGroupPriority_Type())
swdot1vProtocolPortGroupPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:swdot1vProtocolPortGroupPriority.setStatus(_E)
dot1vProtocolPortEntry.registerAugmentions((_D,_H))
swdot1vProtocolPortEntry.setIndexNames(*dot1vProtocolPortEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'PortList':PortList,'swProtocolVLANMIB':swProtocolVLANMIB,'swProtocolVLANCtrl':swProtocolVLANCtrl,'swProtocolVLANTable':swProtocolVLANTable,'swProtocolVLANEntry':swProtocolVLANEntry,_G:swProtocolVLANIndex,'swProtocolVLANName':swProtocolVLANName,'swProtocolVLANProtocolType':swProtocolVLANProtocolType,'swProtocolVLANAdvertisement':swProtocolVLANAdvertisement,'swProtocolVLANUserDefinedProtocol':swProtocolVLANUserDefinedProtocol,'swProtocolVLANencap':swProtocolVLANencap,'swProtocolVLANRowStatus':swProtocolVLANRowStatus,'swdot1vProtocolPortTable':swdot1vProtocolPortTable,_H:swdot1vProtocolPortEntry,'swdot1vProtocolPortGroupPriority':swdot1vProtocolPortGroupPriority})