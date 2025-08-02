_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelVlan=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,86))
_ZyxelVlanSetup_ObjectIdentity=ObjectIdentity
zyxelVlanSetup=_ZyxelVlanSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,86,1))
class _ZyVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dot1Q',1),('portBased',2)))
_ZyVlanType_Type.__name__=_A
_ZyVlanType_Object=MibScalar
zyVlanType=_ZyVlanType_Object((1,3,6,1,4,1,890,1,15,3,86,1,1),_ZyVlanType_Type())
zyVlanType.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanType.setStatus(_C)
_ZyVlanIngressCheckState_Type=EnabledStatus
_ZyVlanIngressCheckState_Object=MibScalar
zyVlanIngressCheckState=_ZyVlanIngressCheckState_Object((1,3,6,1,4,1,890,1,15,3,86,1,2),_ZyVlanIngressCheckState_Type())
zyVlanIngressCheckState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanIngressCheckState.setStatus(_C)
mibBuilder.exportSymbols('ZYXEL-VLAN-MIB',**{'zyxelVlan':zyxelVlan,'zyxelVlanSetup':zyxelVlanSetup,'zyVlanType':zyVlanType,'zyVlanIngressCheckState':zyVlanIngressCheckState})