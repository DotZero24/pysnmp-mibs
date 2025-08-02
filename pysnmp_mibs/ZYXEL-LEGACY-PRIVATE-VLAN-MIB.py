_E='read-write'
_D='zyLegacyPrivateVlanVid'
_C='ZYXEL-LEGACY-PRIVATE-VLAN-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelLegacyPrivateVlan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,41))
_ZyxelLegacyPrivateVlanSetup_ObjectIdentity=ObjectIdentity
zyxelLegacyPrivateVlanSetup=_ZyxelLegacyPrivateVlanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,41,1))
_ZyLegacyPrivateVlanMaxNumberOfVlans_Type=Integer32
_ZyLegacyPrivateVlanMaxNumberOfVlans_Object=MibScalar
zyLegacyPrivateVlanMaxNumberOfVlans=_ZyLegacyPrivateVlanMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,41,1,1),_ZyLegacyPrivateVlanMaxNumberOfVlans_Type())
zyLegacyPrivateVlanMaxNumberOfVlans.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyLegacyPrivateVlanMaxNumberOfVlans.setStatus(_A)
_ZyxelLegacyPrivateVlanTable_Object=MibTable
zyxelLegacyPrivateVlanTable=_ZyxelLegacyPrivateVlanTable_Object((1,3,6,1,4,1,890,1,15,3,41,1,2))
if mibBuilder.loadTexts:zyxelLegacyPrivateVlanTable.setStatus(_A)
_ZyxelLegacyPrivateVlanEntry_Object=MibTableRow
zyxelLegacyPrivateVlanEntry=_ZyxelLegacyPrivateVlanEntry_Object((1,3,6,1,4,1,890,1,15,3,41,1,2,1))
zyxelLegacyPrivateVlanEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelLegacyPrivateVlanEntry.setStatus(_A)
class _ZyLegacyPrivateVlanVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyLegacyPrivateVlanVid_Type.__name__=_B
_ZyLegacyPrivateVlanVid_Object=MibTableColumn
zyLegacyPrivateVlanVid=_ZyLegacyPrivateVlanVid_Object((1,3,6,1,4,1,890,1,15,3,41,1,2,1,1),_ZyLegacyPrivateVlanVid_Type())
zyLegacyPrivateVlanVid.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyLegacyPrivateVlanVid.setStatus(_A)
_ZyLegacyPrivateVlanName_Type=DisplayString
_ZyLegacyPrivateVlanName_Object=MibTableColumn
zyLegacyPrivateVlanName=_ZyLegacyPrivateVlanName_Object((1,3,6,1,4,1,890,1,15,3,41,1,2,1,2),_ZyLegacyPrivateVlanName_Type())
zyLegacyPrivateVlanName.setMaxAccess(_E)
if mibBuilder.loadTexts:zyLegacyPrivateVlanName.setStatus(_A)
_ZyLegacyPrivateVlanPromiscuousPorts_Type=PortList
_ZyLegacyPrivateVlanPromiscuousPorts_Object=MibTableColumn
zyLegacyPrivateVlanPromiscuousPorts=_ZyLegacyPrivateVlanPromiscuousPorts_Object((1,3,6,1,4,1,890,1,15,3,41,1,2,1,3),_ZyLegacyPrivateVlanPromiscuousPorts_Type())
zyLegacyPrivateVlanPromiscuousPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:zyLegacyPrivateVlanPromiscuousPorts.setStatus(_A)
_ZyLegacyPrivateVlanRowStatus_Type=RowStatus
_ZyLegacyPrivateVlanRowStatus_Object=MibTableColumn
zyLegacyPrivateVlanRowStatus=_ZyLegacyPrivateVlanRowStatus_Object((1,3,6,1,4,1,890,1,15,3,41,1,2,1,4),_ZyLegacyPrivateVlanRowStatus_Type())
zyLegacyPrivateVlanRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyLegacyPrivateVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelLegacyPrivateVlan':zyxelLegacyPrivateVlan,'zyxelLegacyPrivateVlanSetup':zyxelLegacyPrivateVlanSetup,'zyLegacyPrivateVlanMaxNumberOfVlans':zyLegacyPrivateVlanMaxNumberOfVlans,'zyxelLegacyPrivateVlanTable':zyxelLegacyPrivateVlanTable,'zyxelLegacyPrivateVlanEntry':zyxelLegacyPrivateVlanEntry,_D:zyLegacyPrivateVlanVid,'zyLegacyPrivateVlanName':zyLegacyPrivateVlanName,'zyLegacyPrivateVlanPromiscuousPorts':zyLegacyPrivateVlanPromiscuousPorts,'zyLegacyPrivateVlanRowStatus':zyLegacyPrivateVlanRowStatus})