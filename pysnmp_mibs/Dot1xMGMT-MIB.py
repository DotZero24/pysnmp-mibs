_D='DisplayString'
_C='Integer32'
_B='current'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
swdot1xMGMTMIB=ModuleIdentity((1,3,6,1,4,1,171,12,30))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_Dot1xGuestVlan_ObjectIdentity=ObjectIdentity
dot1xGuestVlan=_Dot1xGuestVlan_ObjectIdentity((1,3,6,1,4,1,171,12,30,1))
class _Dot1xGuestVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot1xGuestVlanName_Type.__name__=_D
_Dot1xGuestVlanName_Object=MibScalar
dot1xGuestVlanName=_Dot1xGuestVlanName_Object((1,3,6,1,4,1,171,12,30,1,1),_Dot1xGuestVlanName_Type())
dot1xGuestVlanName.setMaxAccess(_A)
if mibBuilder.loadTexts:dot1xGuestVlanName.setStatus(_B)
_Dot1xGuestVlanPort_Type=PortList
_Dot1xGuestVlanPort_Object=MibScalar
dot1xGuestVlanPort=_Dot1xGuestVlanPort_Object((1,3,6,1,4,1,171,12,30,1,2),_Dot1xGuestVlanPort_Type())
dot1xGuestVlanPort.setMaxAccess(_A)
if mibBuilder.loadTexts:dot1xGuestVlanPort.setStatus(_B)
class _Dot1xGuestVlanDelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('start',2)))
_Dot1xGuestVlanDelState_Type.__name__=_C
_Dot1xGuestVlanDelState_Object=MibScalar
dot1xGuestVlanDelState=_Dot1xGuestVlanDelState_Object((1,3,6,1,4,1,171,12,30,1,3),_Dot1xGuestVlanDelState_Type())
dot1xGuestVlanDelState.setMaxAccess(_A)
if mibBuilder.loadTexts:dot1xGuestVlanDelState.setStatus(_B)
mibBuilder.exportSymbols('Dot1xMGMT-MIB',**{'PortList':PortList,'swdot1xMGMTMIB':swdot1xMGMTMIB,'dot1xGuestVlan':dot1xGuestVlan,'dot1xGuestVlanName':dot1xGuestVlanName,'dot1xGuestVlanPort':dot1xGuestVlanPort,'dot1xGuestVlanDelState':dot1xGuestVlanDelState})