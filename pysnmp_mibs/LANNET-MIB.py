_R='vnsPacketBoxAgentIP'
_Q='vnsPacketDetectedVLAN'
_P='vnsPacketExpectedVLAN'
_O='vnsPacketBackbonePort'
_N='vnsPacketPortId'
_M='vnsPacketPortGroupId'
_L='vnsPacketIPXnetwork'
_K='vnsPacketIPNetMask'
_J='vnsPacketIPAddress'
_I='vnsPacketProtocolTypeMask'
_H='notSupported'
_G='unknown'
_F='vnsPacketMACAddress'
_E='OctetString'
_D='Integer32'
_C='read-only'
_B='LANNET-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Lannet_ObjectIdentity=ObjectIdentity
lannet=_Lannet_ObjectIdentity((1,3,6,1,4,1,81))
_LntBoxIdent_ObjectIdentity=ObjectIdentity
lntBoxIdent=_LntBoxIdent_ObjectIdentity((1,3,6,1,4,1,81,17,1,5))
_LntLanSwitch_ObjectIdentity=ObjectIdentity
lntLanSwitch=_LntLanSwitch_ObjectIdentity((1,3,6,1,4,1,81,19))
_VnsPacket_ObjectIdentity=ObjectIdentity
vnsPacket=_VnsPacket_ObjectIdentity((1,3,6,1,4,1,81,19,7))
_VnsPacketTable_Object=MibTable
vnsPacketTable=_VnsPacketTable_Object((1,3,6,1,4,1,81,19,7,1))
if mibBuilder.loadTexts:vnsPacketTable.setStatus(_A)
_VnsPacketEntry_Object=MibTableRow
vnsPacketEntry=_VnsPacketEntry_Object((1,3,6,1,4,1,81,19,7,1,1))
vnsPacketEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:vnsPacketEntry.setStatus(_A)
class _VnsPacketMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_VnsPacketMACAddress_Type.__name__=_E
_VnsPacketMACAddress_Object=MibTableColumn
vnsPacketMACAddress=_VnsPacketMACAddress_Object((1,3,6,1,4,1,81,19,7,1,1,1),_VnsPacketMACAddress_Type())
vnsPacketMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketMACAddress.setStatus(_A)
class _VnsPacketProtocolTypeMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_VnsPacketProtocolTypeMask_Type.__name__=_E
_VnsPacketProtocolTypeMask_Object=MibTableColumn
vnsPacketProtocolTypeMask=_VnsPacketProtocolTypeMask_Object((1,3,6,1,4,1,81,19,7,1,1,2),_VnsPacketProtocolTypeMask_Type())
vnsPacketProtocolTypeMask.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketProtocolTypeMask.setStatus(_A)
_VnsPacketIPAddress_Type=IpAddress
_VnsPacketIPAddress_Object=MibTableColumn
vnsPacketIPAddress=_VnsPacketIPAddress_Object((1,3,6,1,4,1,81,19,7,1,1,3),_VnsPacketIPAddress_Type())
vnsPacketIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketIPAddress.setStatus(_A)
_VnsPacketIPNetMask_Type=IpAddress
_VnsPacketIPNetMask_Object=MibTableColumn
vnsPacketIPNetMask=_VnsPacketIPNetMask_Object((1,3,6,1,4,1,81,19,7,1,1,4),_VnsPacketIPNetMask_Type())
vnsPacketIPNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketIPNetMask.setStatus(_A)
class _VnsPacketIPXnetwork_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_VnsPacketIPXnetwork_Type.__name__=_E
_VnsPacketIPXnetwork_Object=MibTableColumn
vnsPacketIPXnetwork=_VnsPacketIPXnetwork_Object((1,3,6,1,4,1,81,19,7,1,1,5),_VnsPacketIPXnetwork_Type())
vnsPacketIPXnetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketIPXnetwork.setStatus(_A)
class _VnsPacketStationType_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_G,1),('client',2),('server',3),(_H,255)))
_VnsPacketStationType_Type.__name__=_D
_VnsPacketStationType_Object=MibTableColumn
vnsPacketStationType=_VnsPacketStationType_Object((1,3,6,1,4,1,81,19,7,1,1,6),_VnsPacketStationType_Type())
vnsPacketStationType.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketStationType.setStatus(_A)
class _VnsPacketPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VnsPacketPortGroupId_Type.__name__=_D
_VnsPacketPortGroupId_Object=MibTableColumn
vnsPacketPortGroupId=_VnsPacketPortGroupId_Object((1,3,6,1,4,1,81,19,7,1,1,7),_VnsPacketPortGroupId_Type())
vnsPacketPortGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketPortGroupId.setStatus(_A)
class _VnsPacketPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VnsPacketPortId_Type.__name__=_D
_VnsPacketPortId_Object=MibTableColumn
vnsPacketPortId=_VnsPacketPortId_Object((1,3,6,1,4,1,81,19,7,1,1,8),_VnsPacketPortId_Type())
vnsPacketPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketPortId.setStatus(_A)
class _VnsPacketBackbonePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,255)));namedValues=NamedValues(*((_G,1),('backbone',2),('noBackbone',3),(_H,255)))
_VnsPacketBackbonePort_Type.__name__=_D
_VnsPacketBackbonePort_Object=MibTableColumn
vnsPacketBackbonePort=_VnsPacketBackbonePort_Object((1,3,6,1,4,1,81,19,7,1,1,9),_VnsPacketBackbonePort_Type())
vnsPacketBackbonePort.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketBackbonePort.setStatus(_A)
_VnsPacketExpectedVLAN_Type=Integer32
_VnsPacketExpectedVLAN_Object=MibTableColumn
vnsPacketExpectedVLAN=_VnsPacketExpectedVLAN_Object((1,3,6,1,4,1,81,19,7,1,1,10),_VnsPacketExpectedVLAN_Type())
vnsPacketExpectedVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketExpectedVLAN.setStatus(_A)
_VnsPacketDetectedVLAN_Type=Integer32
_VnsPacketDetectedVLAN_Object=MibTableColumn
vnsPacketDetectedVLAN=_VnsPacketDetectedVLAN_Object((1,3,6,1,4,1,81,19,7,1,1,11),_VnsPacketDetectedVLAN_Type())
vnsPacketDetectedVLAN.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketDetectedVLAN.setStatus(_A)
_VnsPacketBoxAgentIP_Type=IpAddress
_VnsPacketBoxAgentIP_Object=MibTableColumn
vnsPacketBoxAgentIP=_VnsPacketBoxAgentIP_Object((1,3,6,1,4,1,81,19,7,1,1,12),_VnsPacketBoxAgentIP_Type())
vnsPacketBoxAgentIP.setMaxAccess(_C)
if mibBuilder.loadTexts:vnsPacketBoxAgentIP.setStatus(_A)
lreVLANViolationTrap=NotificationType((1,3,6,1,4,1,81,17,1,5,0,26))
lreVLANViolationTrap.setObjects(*((_B,_F),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:lreVLANViolationTrap.setStatus('')
mibBuilder.exportSymbols(_B,**{'lannet':lannet,'lntBoxIdent':lntBoxIdent,'lreVLANViolationTrap':lreVLANViolationTrap,'lntLanSwitch':lntLanSwitch,'vnsPacket':vnsPacket,'vnsPacketTable':vnsPacketTable,'vnsPacketEntry':vnsPacketEntry,_F:vnsPacketMACAddress,_I:vnsPacketProtocolTypeMask,_J:vnsPacketIPAddress,_K:vnsPacketIPNetMask,_L:vnsPacketIPXnetwork,'vnsPacketStationType':vnsPacketStationType,_M:vnsPacketPortGroupId,_N:vnsPacketPortId,_O:vnsPacketBackbonePort,_P:vnsPacketExpectedVLAN,_Q:vnsPacketDetectedVLAN,_R:vnsPacketBoxAgentIP})