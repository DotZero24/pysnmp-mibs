_K='not-accessible'
_J='cadMplsLdpNeighborIpAddress'
_I='cadMplsLdpNeighborAddressType'
_H='TruthValue'
_G='DisplayString'
_F='OctetString'
_E='read-create'
_D='CADANT-MPLS-MIB'
_C='read-write'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadMpls,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadMpls')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
cadMplsMIB=ModuleIdentity((1,3,6,1,4,1,4998,1,1,130,1))
if mibBuilder.loadTexts:cadMplsMIB.setRevisions(('2014-01-24 00:00','2013-12-04 00:00','2013-11-04 00:00'))
_CadMplsMIBObjects_ObjectIdentity=ObjectIdentity
cadMplsMIBObjects=_CadMplsMIBObjects_ObjectIdentity((1,3,6,1,4,1,4998,1,1,130,1,1))
_CadMplsParams_ObjectIdentity=ObjectIdentity
cadMplsParams=_CadMplsParams_ObjectIdentity((1,3,6,1,4,1,4998,1,1,130,1,1,1))
class _CadMplsLdpHelloHoldTimer_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CadMplsLdpHelloHoldTimer_Type.__name__=_B
_CadMplsLdpHelloHoldTimer_Object=MibScalar
cadMplsLdpHelloHoldTimer=_CadMplsLdpHelloHoldTimer_Object((1,3,6,1,4,1,4998,1,1,130,1,1,1,1),_CadMplsLdpHelloHoldTimer_Type())
cadMplsLdpHelloHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cadMplsLdpHelloHoldTimer.setStatus(_A)
if mibBuilder.loadTexts:cadMplsLdpHelloHoldTimer.setUnits('second')
class _CadMplsLdpTargetedHelloHoldTimer_Type(Unsigned32):defaultValue=45;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CadMplsLdpTargetedHelloHoldTimer_Type.__name__=_B
_CadMplsLdpTargetedHelloHoldTimer_Object=MibScalar
cadMplsLdpTargetedHelloHoldTimer=_CadMplsLdpTargetedHelloHoldTimer_Object((1,3,6,1,4,1,4998,1,1,130,1,1,1,2),_CadMplsLdpTargetedHelloHoldTimer_Type())
cadMplsLdpTargetedHelloHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cadMplsLdpTargetedHelloHoldTimer.setStatus(_A)
class _CadMplsLdpKeepAliveHoldTimer_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CadMplsLdpKeepAliveHoldTimer_Type.__name__=_B
_CadMplsLdpKeepAliveHoldTimer_Object=MibScalar
cadMplsLdpKeepAliveHoldTimer=_CadMplsLdpKeepAliveHoldTimer_Object((1,3,6,1,4,1,4998,1,1,130,1,1,1,3),_CadMplsLdpKeepAliveHoldTimer_Type())
cadMplsLdpKeepAliveHoldTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cadMplsLdpKeepAliveHoldTimer.setStatus(_A)
class _CadMplsLdpVcDescription_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CadMplsLdpVcDescription_Type.__name__=_G
_CadMplsLdpVcDescription_Object=MibScalar
cadMplsLdpVcDescription=_CadMplsLdpVcDescription_Object((1,3,6,1,4,1,4998,1,1,130,1,1,1,4),_CadMplsLdpVcDescription_Type())
cadMplsLdpVcDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cadMplsLdpVcDescription.setStatus(_A)
_CadMplsLdpNeighborTable_Object=MibTable
cadMplsLdpNeighborTable=_CadMplsLdpNeighborTable_Object((1,3,6,1,4,1,4998,1,1,130,1,1,2))
if mibBuilder.loadTexts:cadMplsLdpNeighborTable.setStatus(_A)
_CadMplsLdpNeighborEntry_Object=MibTableRow
cadMplsLdpNeighborEntry=_CadMplsLdpNeighborEntry_Object((1,3,6,1,4,1,4998,1,1,130,1,1,2,1))
cadMplsLdpNeighborEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:cadMplsLdpNeighborEntry.setStatus(_A)
_CadMplsLdpNeighborAddressType_Type=InetAddressType
_CadMplsLdpNeighborAddressType_Object=MibTableColumn
cadMplsLdpNeighborAddressType=_CadMplsLdpNeighborAddressType_Object((1,3,6,1,4,1,4998,1,1,130,1,1,2,1,1),_CadMplsLdpNeighborAddressType_Type())
cadMplsLdpNeighborAddressType.setMaxAccess(_K)
if mibBuilder.loadTexts:cadMplsLdpNeighborAddressType.setStatus(_A)
_CadMplsLdpNeighborIpAddress_Type=InetAddress
_CadMplsLdpNeighborIpAddress_Object=MibTableColumn
cadMplsLdpNeighborIpAddress=_CadMplsLdpNeighborIpAddress_Object((1,3,6,1,4,1,4998,1,1,130,1,1,2,1,2),_CadMplsLdpNeighborIpAddress_Type())
cadMplsLdpNeighborIpAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:cadMplsLdpNeighborIpAddress.setStatus(_A)
class _CadMplsLdpNeighborPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CadMplsLdpNeighborPassword_Type.__name__=_F
_CadMplsLdpNeighborPassword_Object=MibTableColumn
cadMplsLdpNeighborPassword=_CadMplsLdpNeighborPassword_Object((1,3,6,1,4,1,4998,1,1,130,1,1,2,1,3),_CadMplsLdpNeighborPassword_Type())
cadMplsLdpNeighborPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:cadMplsLdpNeighborPassword.setStatus(_A)
class _CadMplsLdpNeighborTargetedPeer_Type(TruthValue):defaultValue=2
_CadMplsLdpNeighborTargetedPeer_Type.__name__=_H
_CadMplsLdpNeighborTargetedPeer_Object=MibTableColumn
cadMplsLdpNeighborTargetedPeer=_CadMplsLdpNeighborTargetedPeer_Object((1,3,6,1,4,1,4998,1,1,130,1,1,2,1,4),_CadMplsLdpNeighborTargetedPeer_Type())
cadMplsLdpNeighborTargetedPeer.setMaxAccess(_E)
if mibBuilder.loadTexts:cadMplsLdpNeighborTargetedPeer.setStatus(_A)
_CadMplsLdpNeighborRowStatus_Type=RowStatus
_CadMplsLdpNeighborRowStatus_Object=MibTableColumn
cadMplsLdpNeighborRowStatus=_CadMplsLdpNeighborRowStatus_Object((1,3,6,1,4,1,4998,1,1,130,1,1,2,1,5),_CadMplsLdpNeighborRowStatus_Type())
cadMplsLdpNeighborRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cadMplsLdpNeighborRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cadMplsMIB':cadMplsMIB,'cadMplsMIBObjects':cadMplsMIBObjects,'cadMplsParams':cadMplsParams,'cadMplsLdpHelloHoldTimer':cadMplsLdpHelloHoldTimer,'cadMplsLdpTargetedHelloHoldTimer':cadMplsLdpTargetedHelloHoldTimer,'cadMplsLdpKeepAliveHoldTimer':cadMplsLdpKeepAliveHoldTimer,'cadMplsLdpVcDescription':cadMplsLdpVcDescription,'cadMplsLdpNeighborTable':cadMplsLdpNeighborTable,'cadMplsLdpNeighborEntry':cadMplsLdpNeighborEntry,_I:cadMplsLdpNeighborAddressType,_J:cadMplsLdpNeighborIpAddress,'cadMplsLdpNeighborPassword':cadMplsLdpNeighborPassword,'cadMplsLdpNeighborTargetedPeer':cadMplsLdpNeighborTargetedPeer,'cadMplsLdpNeighborRowStatus':cadMplsLdpNeighborRowStatus})