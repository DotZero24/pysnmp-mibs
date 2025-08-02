_J='not-accessible'
_I='zyProtocolBasedVlanEthernetType'
_H='zyProtocolBasedVlanPacketType'
_G='DisplayString'
_F='dot1dBasePort'
_E='BRIDGE-MIB'
_D='read-write'
_C='ZYXEL-PROTOCOL-BASED-VLAN-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelProtocolBasedVlan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,69))
_ZyxelProtocolBasedVlanSetup_ObjectIdentity=ObjectIdentity
zyxelProtocolBasedVlanSetup=_ZyxelProtocolBasedVlanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,69,1))
_ZyProtocolBasedVlanMaxNumberOfVlans_Type=Integer32
_ZyProtocolBasedVlanMaxNumberOfVlans_Object=MibScalar
zyProtocolBasedVlanMaxNumberOfVlans=_ZyProtocolBasedVlanMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,69,1,1),_ZyProtocolBasedVlanMaxNumberOfVlans_Type())
zyProtocolBasedVlanMaxNumberOfVlans.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyProtocolBasedVlanMaxNumberOfVlans.setStatus(_A)
_ZyxelProtocolBasedVlanTable_Object=MibTable
zyxelProtocolBasedVlanTable=_ZyxelProtocolBasedVlanTable_Object((1,3,6,1,4,1,890,1,15,3,69,1,2))
if mibBuilder.loadTexts:zyxelProtocolBasedVlanTable.setStatus(_A)
_ZyxelProtocolBasedVlanEntry_Object=MibTableRow
zyxelProtocolBasedVlanEntry=_ZyxelProtocolBasedVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,69,1,2,1))
zyxelProtocolBasedVlanEntry.setIndexNames((0,_E,_F),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:zyxelProtocolBasedVlanEntry.setStatus(_A)
class _ZyProtocolBasedVlanPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('etherII',1),('snap',2),('llc',3)))
_ZyProtocolBasedVlanPacketType_Type.__name__=_B
_ZyProtocolBasedVlanPacketType_Object=MibTableColumn
zyProtocolBasedVlanPacketType=_ZyProtocolBasedVlanPacketType_Object((1,3,6,1,4,1,890,1,15,3,69,1,2,1,1),_ZyProtocolBasedVlanPacketType_Type())
zyProtocolBasedVlanPacketType.setMaxAccess(_J)
if mibBuilder.loadTexts:zyProtocolBasedVlanPacketType.setStatus(_A)
_ZyProtocolBasedVlanEthernetType_Type=Integer32
_ZyProtocolBasedVlanEthernetType_Object=MibTableColumn
zyProtocolBasedVlanEthernetType=_ZyProtocolBasedVlanEthernetType_Object((1,3,6,1,4,1,890,1,15,3,69,1,2,1,2),_ZyProtocolBasedVlanEthernetType_Type())
zyProtocolBasedVlanEthernetType.setMaxAccess(_J)
if mibBuilder.loadTexts:zyProtocolBasedVlanEthernetType.setStatus(_A)
class _ZyProtocolBasedVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZyProtocolBasedVlanName_Type.__name__=_G
_ZyProtocolBasedVlanName_Object=MibTableColumn
zyProtocolBasedVlanName=_ZyProtocolBasedVlanName_Object((1,3,6,1,4,1,890,1,15,3,69,1,2,1,3),_ZyProtocolBasedVlanName_Type())
zyProtocolBasedVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:zyProtocolBasedVlanName.setStatus(_A)
class _ZyProtocolBasedVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyProtocolBasedVlanVid_Type.__name__=_B
_ZyProtocolBasedVlanVid_Object=MibTableColumn
zyProtocolBasedVlanVid=_ZyProtocolBasedVlanVid_Object((1,3,6,1,4,1,890,1,15,3,69,1,2,1,4),_ZyProtocolBasedVlanVid_Type())
zyProtocolBasedVlanVid.setMaxAccess(_D)
if mibBuilder.loadTexts:zyProtocolBasedVlanVid.setStatus(_A)
class _ZyProtocolBasedVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZyProtocolBasedVlanPriority_Type.__name__=_B
_ZyProtocolBasedVlanPriority_Object=MibTableColumn
zyProtocolBasedVlanPriority=_ZyProtocolBasedVlanPriority_Object((1,3,6,1,4,1,890,1,15,3,69,1,2,1,5),_ZyProtocolBasedVlanPriority_Type())
zyProtocolBasedVlanPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:zyProtocolBasedVlanPriority.setStatus(_A)
_ZyProtocolBasedVlanRowStatus_Type=RowStatus
_ZyProtocolBasedVlanRowStatus_Object=MibTableColumn
zyProtocolBasedVlanRowStatus=_ZyProtocolBasedVlanRowStatus_Object((1,3,6,1,4,1,890,1,15,3,69,1,2,1,6),_ZyProtocolBasedVlanRowStatus_Type())
zyProtocolBasedVlanRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyProtocolBasedVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelProtocolBasedVlan':zyxelProtocolBasedVlan,'zyxelProtocolBasedVlanSetup':zyxelProtocolBasedVlanSetup,'zyProtocolBasedVlanMaxNumberOfVlans':zyProtocolBasedVlanMaxNumberOfVlans,'zyxelProtocolBasedVlanTable':zyxelProtocolBasedVlanTable,'zyxelProtocolBasedVlanEntry':zyxelProtocolBasedVlanEntry,_H:zyProtocolBasedVlanPacketType,_I:zyProtocolBasedVlanEthernetType,'zyProtocolBasedVlanName':zyProtocolBasedVlanName,'zyProtocolBasedVlanVid':zyProtocolBasedVlanVid,'zyProtocolBasedVlanPriority':zyProtocolBasedVlanPriority,'zyProtocolBasedVlanRowStatus':zyProtocolBasedVlanRowStatus})