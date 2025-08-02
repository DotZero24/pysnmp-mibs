_H='not-accessible'
_G='zySubnetBasedVlanSourceMaskBits'
_F='zySubnetBasedVlanSourceIpAddress'
_E='DisplayString'
_D='ZYXEL-SUBNET-BASED-VLAN-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelSubnetBasedVlan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,80))
_ZyxelSubnetBasedVlanSetup_ObjectIdentity=ObjectIdentity
zyxelSubnetBasedVlanSetup=_ZyxelSubnetBasedVlanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,80,1))
_ZySubnetBasedVlanState_Type=EnabledStatus
_ZySubnetBasedVlanState_Object=MibScalar
zySubnetBasedVlanState=_ZySubnetBasedVlanState_Object((1,3,6,1,4,1,890,1,15,3,80,1,1),_ZySubnetBasedVlanState_Type())
zySubnetBasedVlanState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySubnetBasedVlanState.setStatus(_A)
_ZySubnetBasedVlanDhcpVlanOverrideState_Type=EnabledStatus
_ZySubnetBasedVlanDhcpVlanOverrideState_Object=MibScalar
zySubnetBasedVlanDhcpVlanOverrideState=_ZySubnetBasedVlanDhcpVlanOverrideState_Object((1,3,6,1,4,1,890,1,15,3,80,1,2),_ZySubnetBasedVlanDhcpVlanOverrideState_Type())
zySubnetBasedVlanDhcpVlanOverrideState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySubnetBasedVlanDhcpVlanOverrideState.setStatus(_A)
_ZySubnetBasedVlanMaxNumberOfVlans_Type=Integer32
_ZySubnetBasedVlanMaxNumberOfVlans_Object=MibScalar
zySubnetBasedVlanMaxNumberOfVlans=_ZySubnetBasedVlanMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,80,1,3),_ZySubnetBasedVlanMaxNumberOfVlans_Type())
zySubnetBasedVlanMaxNumberOfVlans.setMaxAccess('read-only')
if mibBuilder.loadTexts:zySubnetBasedVlanMaxNumberOfVlans.setStatus(_A)
_ZyxelSubnetBasedVlanTable_Object=MibTable
zyxelSubnetBasedVlanTable=_ZyxelSubnetBasedVlanTable_Object((1,3,6,1,4,1,890,1,15,3,80,1,4))
if mibBuilder.loadTexts:zyxelSubnetBasedVlanTable.setStatus(_A)
_ZyxelSubnetBasedVlanEntry_Object=MibTableRow
zyxelSubnetBasedVlanEntry=_ZyxelSubnetBasedVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,80,1,4,1))
zyxelSubnetBasedVlanEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:zyxelSubnetBasedVlanEntry.setStatus(_A)
_ZySubnetBasedVlanSourceIpAddress_Type=IpAddress
_ZySubnetBasedVlanSourceIpAddress_Object=MibTableColumn
zySubnetBasedVlanSourceIpAddress=_ZySubnetBasedVlanSourceIpAddress_Object((1,3,6,1,4,1,890,1,15,3,80,1,4,1,1),_ZySubnetBasedVlanSourceIpAddress_Type())
zySubnetBasedVlanSourceIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:zySubnetBasedVlanSourceIpAddress.setStatus(_A)
class _ZySubnetBasedVlanSourceMaskBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ZySubnetBasedVlanSourceMaskBits_Type.__name__=_C
_ZySubnetBasedVlanSourceMaskBits_Object=MibTableColumn
zySubnetBasedVlanSourceMaskBits=_ZySubnetBasedVlanSourceMaskBits_Object((1,3,6,1,4,1,890,1,15,3,80,1,4,1,2),_ZySubnetBasedVlanSourceMaskBits_Type())
zySubnetBasedVlanSourceMaskBits.setMaxAccess(_H)
if mibBuilder.loadTexts:zySubnetBasedVlanSourceMaskBits.setStatus(_A)
class _ZySubnetBasedVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZySubnetBasedVlanName_Type.__name__=_E
_ZySubnetBasedVlanName_Object=MibTableColumn
zySubnetBasedVlanName=_ZySubnetBasedVlanName_Object((1,3,6,1,4,1,890,1,15,3,80,1,4,1,3),_ZySubnetBasedVlanName_Type())
zySubnetBasedVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:zySubnetBasedVlanName.setStatus(_A)
class _ZySubnetBasedVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZySubnetBasedVlanVid_Type.__name__=_C
_ZySubnetBasedVlanVid_Object=MibTableColumn
zySubnetBasedVlanVid=_ZySubnetBasedVlanVid_Object((1,3,6,1,4,1,890,1,15,3,80,1,4,1,4),_ZySubnetBasedVlanVid_Type())
zySubnetBasedVlanVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zySubnetBasedVlanVid.setStatus(_A)
class _ZySubnetBasedVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZySubnetBasedVlanPriority_Type.__name__=_C
_ZySubnetBasedVlanPriority_Object=MibTableColumn
zySubnetBasedVlanPriority=_ZySubnetBasedVlanPriority_Object((1,3,6,1,4,1,890,1,15,3,80,1,4,1,5),_ZySubnetBasedVlanPriority_Type())
zySubnetBasedVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zySubnetBasedVlanPriority.setStatus(_A)
_ZySubnetBasedVlanRowStatus_Type=RowStatus
_ZySubnetBasedVlanRowStatus_Object=MibTableColumn
zySubnetBasedVlanRowStatus=_ZySubnetBasedVlanRowStatus_Object((1,3,6,1,4,1,890,1,15,3,80,1,4,1,6),_ZySubnetBasedVlanRowStatus_Type())
zySubnetBasedVlanRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zySubnetBasedVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelSubnetBasedVlan':zyxelSubnetBasedVlan,'zyxelSubnetBasedVlanSetup':zyxelSubnetBasedVlanSetup,'zySubnetBasedVlanState':zySubnetBasedVlanState,'zySubnetBasedVlanDhcpVlanOverrideState':zySubnetBasedVlanDhcpVlanOverrideState,'zySubnetBasedVlanMaxNumberOfVlans':zySubnetBasedVlanMaxNumberOfVlans,'zyxelSubnetBasedVlanTable':zyxelSubnetBasedVlanTable,'zyxelSubnetBasedVlanEntry':zyxelSubnetBasedVlanEntry,_F:zySubnetBasedVlanSourceIpAddress,_G:zySubnetBasedVlanSourceMaskBits,'zySubnetBasedVlanName':zySubnetBasedVlanName,'zySubnetBasedVlanVid':zySubnetBasedVlanVid,'zySubnetBasedVlanPriority':zySubnetBasedVlanPriority,'zySubnetBasedVlanRowStatus':zySubnetBasedVlanRowStatus})