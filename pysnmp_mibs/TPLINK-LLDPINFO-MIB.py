_M='lldpNeighborManAddr'
_L='lldpNeighborManAddrSubtype'
_K='lldpNeighborManAddrPortIndexId'
_J='lldpNeighborPortIndexId'
_I='IF-MIB'
_H='TPLINK-LLDPINFO-MIB'
_G='ifIndex'
_F='enable'
_E='disable'
_D='Integer32'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkLldpMIBObjects,=mibBuilder.importSymbols('TPLINK-LLDP-MIB','tplinkLldpMIBObjects')
_LldpInfo_ObjectIdentity=ObjectIdentity
lldpInfo=_LldpInfo_ObjectIdentity((1,3,6,1,4,1,11863,6,35,1,2))
_LldpLocalInfoTable_Object=MibTable
lldpLocalInfoTable=_LldpLocalInfoTable_Object((1,3,6,1,4,1,11863,6,35,1,2,1))
if mibBuilder.loadTexts:lldpLocalInfoTable.setStatus(_A)
_LldpLocalInfoEntry_Object=MibTableRow
lldpLocalInfoEntry=_LldpLocalInfoEntry_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1))
lldpLocalInfoEntry.setIndexNames((0,_I,_G))
if mibBuilder.loadTexts:lldpLocalInfoEntry.setStatus(_A)
class _LldpLocalPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalPortId_Type.__name__=_C
_LldpLocalPortId_Object=MibTableColumn
lldpLocalPortId=_LldpLocalPortId_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,1),_LldpLocalPortId_Type())
lldpLocalPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalPortId.setStatus(_A)
class _LldpLocalChassisIdType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalChassisIdType_Type.__name__=_C
_LldpLocalChassisIdType_Object=MibTableColumn
lldpLocalChassisIdType=_LldpLocalChassisIdType_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,2),_LldpLocalChassisIdType_Type())
lldpLocalChassisIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalChassisIdType.setStatus(_A)
class _LldpLocalChassisId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalChassisId_Type.__name__=_C
_LldpLocalChassisId_Object=MibTableColumn
lldpLocalChassisId=_LldpLocalChassisId_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,3),_LldpLocalChassisId_Type())
lldpLocalChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalChassisId.setStatus(_A)
class _LldpLocalPortIdType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalPortIdType_Type.__name__=_C
_LldpLocalPortIdType_Object=MibTableColumn
lldpLocalPortIdType=_LldpLocalPortIdType_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,4),_LldpLocalPortIdType_Type())
lldpLocalPortIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalPortIdType.setStatus(_A)
class _LldpLocalPortIdDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalPortIdDescr_Type.__name__=_C
_LldpLocalPortIdDescr_Object=MibTableColumn
lldpLocalPortIdDescr=_LldpLocalPortIdDescr_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,5),_LldpLocalPortIdDescr_Type())
lldpLocalPortIdDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalPortIdDescr.setStatus(_A)
_LldpLocalTtl_Type=Integer32
_LldpLocalTtl_Object=MibTableColumn
lldpLocalTtl=_LldpLocalTtl_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,6),_LldpLocalTtl_Type())
lldpLocalTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalTtl.setStatus(_A)
class _LldpLocalPortDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalPortDescr_Type.__name__=_C
_LldpLocalPortDescr_Object=MibTableColumn
lldpLocalPortDescr=_LldpLocalPortDescr_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,7),_LldpLocalPortDescr_Type())
lldpLocalPortDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalPortDescr.setStatus(_A)
class _LldpLocalDeviceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalDeviceName_Type.__name__=_C
_LldpLocalDeviceName_Object=MibTableColumn
lldpLocalDeviceName=_LldpLocalDeviceName_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,8),_LldpLocalDeviceName_Type())
lldpLocalDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalDeviceName.setStatus(_A)
class _LldpLocalDeviceDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalDeviceDescr_Type.__name__=_C
_LldpLocalDeviceDescr_Object=MibTableColumn
lldpLocalDeviceDescr=_LldpLocalDeviceDescr_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,9),_LldpLocalDeviceDescr_Type())
lldpLocalDeviceDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalDeviceDescr.setStatus(_A)
class _LldpLocalCapAvailable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalCapAvailable_Type.__name__=_C
_LldpLocalCapAvailable_Object=MibTableColumn
lldpLocalCapAvailable=_LldpLocalCapAvailable_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,10),_LldpLocalCapAvailable_Type())
lldpLocalCapAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalCapAvailable.setStatus(_A)
class _LldpLocalCapEnabled_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalCapEnabled_Type.__name__=_C
_LldpLocalCapEnabled_Object=MibTableColumn
lldpLocalCapEnabled=_LldpLocalCapEnabled_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,11),_LldpLocalCapEnabled_Type())
lldpLocalCapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalCapEnabled.setStatus(_A)
_LldpLocalManageIpAddr_Type=IpAddress
_LldpLocalManageIpAddr_Object=MibTableColumn
lldpLocalManageIpAddr=_LldpLocalManageIpAddr_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,12),_LldpLocalManageIpAddr_Type())
lldpLocalManageIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalManageIpAddr.setStatus(_A)
class _LldpLocalManageAddrType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalManageAddrType_Type.__name__=_C
_LldpLocalManageAddrType_Object=MibTableColumn
lldpLocalManageAddrType=_LldpLocalManageAddrType_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,13),_LldpLocalManageAddrType_Type())
lldpLocalManageAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalManageAddrType.setStatus(_A)
class _LldpLocalManageAddrInterfaceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalManageAddrInterfaceType_Type.__name__=_C
_LldpLocalManageAddrInterfaceType_Object=MibTableColumn
lldpLocalManageAddrInterfaceType=_LldpLocalManageAddrInterfaceType_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,14),_LldpLocalManageAddrInterfaceType_Type())
lldpLocalManageAddrInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalManageAddrInterfaceType.setStatus(_A)
_LldpLocalManageAddrInterfaceId_Type=Integer32
_LldpLocalManageAddrInterfaceId_Object=MibTableColumn
lldpLocalManageAddrInterfaceId=_LldpLocalManageAddrInterfaceId_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,15),_LldpLocalManageAddrInterfaceId_Type())
lldpLocalManageAddrInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalManageAddrInterfaceId.setStatus(_A)
class _LldpLocalManageAddrOID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalManageAddrOID_Type.__name__=_C
_LldpLocalManageAddrOID_Object=MibTableColumn
lldpLocalManageAddrOID=_LldpLocalManageAddrOID_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,16),_LldpLocalManageAddrOID_Type())
lldpLocalManageAddrOID.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalManageAddrOID.setStatus(_A)
class _LldpLocalPortAndProtocolVlanID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalPortAndProtocolVlanID_Type.__name__=_C
_LldpLocalPortAndProtocolVlanID_Object=MibTableColumn
lldpLocalPortAndProtocolVlanID=_LldpLocalPortAndProtocolVlanID_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,17),_LldpLocalPortAndProtocolVlanID_Type())
lldpLocalPortAndProtocolVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalPortAndProtocolVlanID.setStatus(_A)
class _LldpLocalVlanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalVlanName_Type.__name__=_C
_LldpLocalVlanName_Object=MibTableColumn
lldpLocalVlanName=_LldpLocalVlanName_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,18),_LldpLocalVlanName_Type())
lldpLocalVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalVlanName.setStatus(_A)
class _LldpLocalAutoNegotiationSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpLocalAutoNegotiationSupported_Type.__name__=_D
_LldpLocalAutoNegotiationSupported_Object=MibTableColumn
lldpLocalAutoNegotiationSupported=_LldpLocalAutoNegotiationSupported_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,19),_LldpLocalAutoNegotiationSupported_Type())
lldpLocalAutoNegotiationSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalAutoNegotiationSupported.setStatus(_A)
class _LldpLocalAutoNegotiationEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpLocalAutoNegotiationEnabled_Type.__name__=_D
_LldpLocalAutoNegotiationEnabled_Object=MibTableColumn
lldpLocalAutoNegotiationEnabled=_LldpLocalAutoNegotiationEnabled_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,20),_LldpLocalAutoNegotiationEnabled_Type())
lldpLocalAutoNegotiationEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalAutoNegotiationEnabled.setStatus(_A)
class _LldpLocalOperMau_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalOperMau_Type.__name__=_C
_LldpLocalOperMau_Object=MibTableColumn
lldpLocalOperMau=_LldpLocalOperMau_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,21),_LldpLocalOperMau_Type())
lldpLocalOperMau.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalOperMau.setStatus(_A)
class _LldpLocalLinkAggregationSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpLocalLinkAggregationSupported_Type.__name__=_D
_LldpLocalLinkAggregationSupported_Object=MibTableColumn
lldpLocalLinkAggregationSupported=_LldpLocalLinkAggregationSupported_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,22),_LldpLocalLinkAggregationSupported_Type())
lldpLocalLinkAggregationSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalLinkAggregationSupported.setStatus(_A)
class _LldpLocalLinkAggregationEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpLocalLinkAggregationEnabled_Type.__name__=_D
_LldpLocalLinkAggregationEnabled_Object=MibTableColumn
lldpLocalLinkAggregationEnabled=_LldpLocalLinkAggregationEnabled_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,23),_LldpLocalLinkAggregationEnabled_Type())
lldpLocalLinkAggregationEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalLinkAggregationEnabled.setStatus(_A)
_LldpLocalAggregationPortId_Type=Integer32
_LldpLocalAggregationPortId_Object=MibTableColumn
lldpLocalAggregationPortId=_LldpLocalAggregationPortId_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,24),_LldpLocalAggregationPortId_Type())
lldpLocalAggregationPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalAggregationPortId.setStatus(_A)
class _LldpLocalPowerPortClass_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpLocalPowerPortClass_Type.__name__=_C
_LldpLocalPowerPortClass_Object=MibTableColumn
lldpLocalPowerPortClass=_LldpLocalPowerPortClass_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,25),_LldpLocalPowerPortClass_Type())
lldpLocalPowerPortClass.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalPowerPortClass.setStatus(_A)
class _LldpLocalPsePowerSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpLocalPsePowerSupported_Type.__name__=_D
_LldpLocalPsePowerSupported_Object=MibTableColumn
lldpLocalPsePowerSupported=_LldpLocalPsePowerSupported_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,26),_LldpLocalPsePowerSupported_Type())
lldpLocalPsePowerSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalPsePowerSupported.setStatus(_A)
class _LldpLocalPsePowerEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpLocalPsePowerEnabled_Type.__name__=_D
_LldpLocalPsePowerEnabled_Object=MibTableColumn
lldpLocalPsePowerEnabled=_LldpLocalPsePowerEnabled_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,27),_LldpLocalPsePowerEnabled_Type())
lldpLocalPsePowerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalPsePowerEnabled.setStatus(_A)
class _LldpLocalPsePairsControlAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpLocalPsePairsControlAbility_Type.__name__=_D
_LldpLocalPsePairsControlAbility_Object=MibTableColumn
lldpLocalPsePairsControlAbility=_LldpLocalPsePairsControlAbility_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,28),_LldpLocalPsePairsControlAbility_Type())
lldpLocalPsePairsControlAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalPsePairsControlAbility.setStatus(_A)
_LldpLocalMaximumFrameSize_Type=Integer32
_LldpLocalMaximumFrameSize_Object=MibTableColumn
lldpLocalMaximumFrameSize=_LldpLocalMaximumFrameSize_Object((1,3,6,1,4,1,11863,6,35,1,2,1,1,29),_LldpLocalMaximumFrameSize_Type())
lldpLocalMaximumFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpLocalMaximumFrameSize.setStatus(_A)
_LldpNeighborInfoTable_Object=MibTable
lldpNeighborInfoTable=_LldpNeighborInfoTable_Object((1,3,6,1,4,1,11863,6,35,1,2,2))
if mibBuilder.loadTexts:lldpNeighborInfoTable.setStatus(_A)
_LldpNeighborInfoEntry_Object=MibTableRow
lldpNeighborInfoEntry=_LldpNeighborInfoEntry_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1))
lldpNeighborInfoEntry.setIndexNames((0,_I,_G),(0,_H,_J))
if mibBuilder.loadTexts:lldpNeighborInfoEntry.setStatus(_A)
class _LldpNeighborPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborPortId_Type.__name__=_C
_LldpNeighborPortId_Object=MibTableColumn
lldpNeighborPortId=_LldpNeighborPortId_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,1),_LldpNeighborPortId_Type())
lldpNeighborPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPortId.setStatus(_A)
_LldpNeighborPortIndexId_Type=Integer32
_LldpNeighborPortIndexId_Object=MibTableColumn
lldpNeighborPortIndexId=_LldpNeighborPortIndexId_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,2),_LldpNeighborPortIndexId_Type())
lldpNeighborPortIndexId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPortIndexId.setStatus(_A)
class _LldpNeighborChassisIdType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborChassisIdType_Type.__name__=_C
_LldpNeighborChassisIdType_Object=MibTableColumn
lldpNeighborChassisIdType=_LldpNeighborChassisIdType_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,3),_LldpNeighborChassisIdType_Type())
lldpNeighborChassisIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborChassisIdType.setStatus(_A)
class _LldpNeighborChassisId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborChassisId_Type.__name__=_C
_LldpNeighborChassisId_Object=MibTableColumn
lldpNeighborChassisId=_LldpNeighborChassisId_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,4),_LldpNeighborChassisId_Type())
lldpNeighborChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborChassisId.setStatus(_A)
class _LldpNeighborPortIdType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborPortIdType_Type.__name__=_C
_LldpNeighborPortIdType_Object=MibTableColumn
lldpNeighborPortIdType=_LldpNeighborPortIdType_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,5),_LldpNeighborPortIdType_Type())
lldpNeighborPortIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPortIdType.setStatus(_A)
class _LldpNeighborPortIdDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborPortIdDescr_Type.__name__=_C
_LldpNeighborPortIdDescr_Object=MibTableColumn
lldpNeighborPortIdDescr=_LldpNeighborPortIdDescr_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,6),_LldpNeighborPortIdDescr_Type())
lldpNeighborPortIdDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPortIdDescr.setStatus(_A)
_LldpNeighborTtl_Type=Integer32
_LldpNeighborTtl_Object=MibTableColumn
lldpNeighborTtl=_LldpNeighborTtl_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,7),_LldpNeighborTtl_Type())
lldpNeighborTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborTtl.setStatus(_A)
class _LldpNeighborPortDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborPortDescr_Type.__name__=_C
_LldpNeighborPortDescr_Object=MibTableColumn
lldpNeighborPortDescr=_LldpNeighborPortDescr_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,8),_LldpNeighborPortDescr_Type())
lldpNeighborPortDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPortDescr.setStatus(_A)
class _LldpNeighborDeviceName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborDeviceName_Type.__name__=_C
_LldpNeighborDeviceName_Object=MibTableColumn
lldpNeighborDeviceName=_LldpNeighborDeviceName_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,9),_LldpNeighborDeviceName_Type())
lldpNeighborDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborDeviceName.setStatus(_A)
class _LldpNeighborDeviceDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborDeviceDescr_Type.__name__=_C
_LldpNeighborDeviceDescr_Object=MibTableColumn
lldpNeighborDeviceDescr=_LldpNeighborDeviceDescr_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,10),_LldpNeighborDeviceDescr_Type())
lldpNeighborDeviceDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborDeviceDescr.setStatus(_A)
class _LldpNeighborCapAvailable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborCapAvailable_Type.__name__=_C
_LldpNeighborCapAvailable_Object=MibTableColumn
lldpNeighborCapAvailable=_LldpNeighborCapAvailable_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,11),_LldpNeighborCapAvailable_Type())
lldpNeighborCapAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborCapAvailable.setStatus(_A)
class _LldpNeighborCapEnabled_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborCapEnabled_Type.__name__=_C
_LldpNeighborCapEnabled_Object=MibTableColumn
lldpNeighborCapEnabled=_LldpNeighborCapEnabled_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,12),_LldpNeighborCapEnabled_Type())
lldpNeighborCapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborCapEnabled.setStatus(_A)
_LldpNeighborManageIpAddr_Type=IpAddress
_LldpNeighborManageIpAddr_Object=MibTableColumn
lldpNeighborManageIpAddr=_LldpNeighborManageIpAddr_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,13),_LldpNeighborManageIpAddr_Type())
lldpNeighborManageIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManageIpAddr.setStatus(_A)
class _LldpNeighborManageAddrType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborManageAddrType_Type.__name__=_C
_LldpNeighborManageAddrType_Object=MibTableColumn
lldpNeighborManageAddrType=_LldpNeighborManageAddrType_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,14),_LldpNeighborManageAddrType_Type())
lldpNeighborManageAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManageAddrType.setStatus(_A)
class _LldpNeighborManageAddrInterfaceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborManageAddrInterfaceType_Type.__name__=_C
_LldpNeighborManageAddrInterfaceType_Object=MibTableColumn
lldpNeighborManageAddrInterfaceType=_LldpNeighborManageAddrInterfaceType_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,15),_LldpNeighborManageAddrInterfaceType_Type())
lldpNeighborManageAddrInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManageAddrInterfaceType.setStatus(_A)
_LldpNeighborManageAddrInterfaceId_Type=Integer32
_LldpNeighborManageAddrInterfaceId_Object=MibTableColumn
lldpNeighborManageAddrInterfaceId=_LldpNeighborManageAddrInterfaceId_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,16),_LldpNeighborManageAddrInterfaceId_Type())
lldpNeighborManageAddrInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManageAddrInterfaceId.setStatus(_A)
class _LldpNeighborManageAddrOID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborManageAddrOID_Type.__name__=_C
_LldpNeighborManageAddrOID_Object=MibTableColumn
lldpNeighborManageAddrOID=_LldpNeighborManageAddrOID_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,17),_LldpNeighborManageAddrOID_Type())
lldpNeighborManageAddrOID.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManageAddrOID.setStatus(_A)
class _LldpNeighborPortAndProtocolVlanID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_LldpNeighborPortAndProtocolVlanID_Type.__name__=_C
_LldpNeighborPortAndProtocolVlanID_Object=MibTableColumn
lldpNeighborPortAndProtocolVlanID=_LldpNeighborPortAndProtocolVlanID_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,18),_LldpNeighborPortAndProtocolVlanID_Type())
lldpNeighborPortAndProtocolVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPortAndProtocolVlanID.setStatus(_A)
class _LldpNeighborVlanName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_LldpNeighborVlanName_Type.__name__=_C
_LldpNeighborVlanName_Object=MibTableColumn
lldpNeighborVlanName=_LldpNeighborVlanName_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,19),_LldpNeighborVlanName_Type())
lldpNeighborVlanName.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborVlanName.setStatus(_A)
class _LldpNeighborProtocolIdentity_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_LldpNeighborProtocolIdentity_Type.__name__=_C
_LldpNeighborProtocolIdentity_Object=MibTableColumn
lldpNeighborProtocolIdentity=_LldpNeighborProtocolIdentity_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,20),_LldpNeighborProtocolIdentity_Type())
lldpNeighborProtocolIdentity.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborProtocolIdentity.setStatus(_A)
class _LldpNeighborAutoNegotiationSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpNeighborAutoNegotiationSupported_Type.__name__=_D
_LldpNeighborAutoNegotiationSupported_Object=MibTableColumn
lldpNeighborAutoNegotiationSupported=_LldpNeighborAutoNegotiationSupported_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,21),_LldpNeighborAutoNegotiationSupported_Type())
lldpNeighborAutoNegotiationSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborAutoNegotiationSupported.setStatus(_A)
class _LldpNeighborAutoNegotiationEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpNeighborAutoNegotiationEnabled_Type.__name__=_D
_LldpNeighborAutoNegotiationEnabled_Object=MibTableColumn
lldpNeighborAutoNegotiationEnabled=_LldpNeighborAutoNegotiationEnabled_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,22),_LldpNeighborAutoNegotiationEnabled_Type())
lldpNeighborAutoNegotiationEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborAutoNegotiationEnabled.setStatus(_A)
class _LldpNeighborOperMau_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborOperMau_Type.__name__=_C
_LldpNeighborOperMau_Object=MibTableColumn
lldpNeighborOperMau=_LldpNeighborOperMau_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,23),_LldpNeighborOperMau_Type())
lldpNeighborOperMau.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborOperMau.setStatus(_A)
class _LldpNeighborLinkAggregationSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpNeighborLinkAggregationSupported_Type.__name__=_D
_LldpNeighborLinkAggregationSupported_Object=MibTableColumn
lldpNeighborLinkAggregationSupported=_LldpNeighborLinkAggregationSupported_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,24),_LldpNeighborLinkAggregationSupported_Type())
lldpNeighborLinkAggregationSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborLinkAggregationSupported.setStatus(_A)
class _LldpNeighborLinkAggregationEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpNeighborLinkAggregationEnabled_Type.__name__=_D
_LldpNeighborLinkAggregationEnabled_Object=MibTableColumn
lldpNeighborLinkAggregationEnabled=_LldpNeighborLinkAggregationEnabled_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,25),_LldpNeighborLinkAggregationEnabled_Type())
lldpNeighborLinkAggregationEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborLinkAggregationEnabled.setStatus(_A)
_LldpNeighborAggregationPortId_Type=Integer32
_LldpNeighborAggregationPortId_Object=MibTableColumn
lldpNeighborAggregationPortId=_LldpNeighborAggregationPortId_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,26),_LldpNeighborAggregationPortId_Type())
lldpNeighborAggregationPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborAggregationPortId.setStatus(_A)
class _LldpNeighborPowerPortClass_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborPowerPortClass_Type.__name__=_C
_LldpNeighborPowerPortClass_Object=MibTableColumn
lldpNeighborPowerPortClass=_LldpNeighborPowerPortClass_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,27),_LldpNeighborPowerPortClass_Type())
lldpNeighborPowerPortClass.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPowerPortClass.setStatus(_A)
class _LldpNeighborPsePowerSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpNeighborPsePowerSupported_Type.__name__=_D
_LldpNeighborPsePowerSupported_Object=MibTableColumn
lldpNeighborPsePowerSupported=_LldpNeighborPsePowerSupported_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,28),_LldpNeighborPsePowerSupported_Type())
lldpNeighborPsePowerSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPsePowerSupported.setStatus(_A)
class _LldpNeighborPsePowerEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpNeighborPsePowerEnabled_Type.__name__=_D
_LldpNeighborPsePowerEnabled_Object=MibTableColumn
lldpNeighborPsePowerEnabled=_LldpNeighborPsePowerEnabled_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,29),_LldpNeighborPsePowerEnabled_Type())
lldpNeighborPsePowerEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPsePowerEnabled.setStatus(_A)
class _LldpNeighborPsePairsControlAbility_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_LldpNeighborPsePairsControlAbility_Type.__name__=_D
_LldpNeighborPsePairsControlAbility_Object=MibTableColumn
lldpNeighborPsePairsControlAbility=_LldpNeighborPsePairsControlAbility_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,30),_LldpNeighborPsePairsControlAbility_Type())
lldpNeighborPsePairsControlAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborPsePairsControlAbility.setStatus(_A)
_LldpNeighborMaximumFrameSize_Type=Integer32
_LldpNeighborMaximumFrameSize_Object=MibTableColumn
lldpNeighborMaximumFrameSize=_LldpNeighborMaximumFrameSize_Object((1,3,6,1,4,1,11863,6,35,1,2,2,1,31),_LldpNeighborMaximumFrameSize_Type())
lldpNeighborMaximumFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborMaximumFrameSize.setStatus(_A)
_LldpNeighborManAddrTable_Object=MibTable
lldpNeighborManAddrTable=_LldpNeighborManAddrTable_Object((1,3,6,1,4,1,11863,6,35,1,2,3))
if mibBuilder.loadTexts:lldpNeighborManAddrTable.setStatus(_A)
_LldpNeighborManAddrEntry_Object=MibTableRow
lldpNeighborManAddrEntry=_LldpNeighborManAddrEntry_Object((1,3,6,1,4,1,11863,6,35,1,2,3,1))
lldpNeighborManAddrEntry.setIndexNames((0,_I,_G),(0,_H,_K),(0,_H,_L),(0,_H,_M))
if mibBuilder.loadTexts:lldpNeighborManAddrEntry.setStatus(_A)
class _LldpNeighborManAddrPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborManAddrPortId_Type.__name__=_C
_LldpNeighborManAddrPortId_Object=MibTableColumn
lldpNeighborManAddrPortId=_LldpNeighborManAddrPortId_Object((1,3,6,1,4,1,11863,6,35,1,2,3,1,1),_LldpNeighborManAddrPortId_Type())
lldpNeighborManAddrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManAddrPortId.setStatus(_A)
_LldpNeighborManAddrPortIndexId_Type=Integer32
_LldpNeighborManAddrPortIndexId_Object=MibTableColumn
lldpNeighborManAddrPortIndexId=_LldpNeighborManAddrPortIndexId_Object((1,3,6,1,4,1,11863,6,35,1,2,3,1,2),_LldpNeighborManAddrPortIndexId_Type())
lldpNeighborManAddrPortIndexId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManAddrPortIndexId.setStatus(_A)
class _LldpNeighborManAddrSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_LldpNeighborManAddrSubtype_Type.__name__=_D
_LldpNeighborManAddrSubtype_Object=MibTableColumn
lldpNeighborManAddrSubtype=_LldpNeighborManAddrSubtype_Object((1,3,6,1,4,1,11863,6,35,1,2,3,1,3),_LldpNeighborManAddrSubtype_Type())
lldpNeighborManAddrSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManAddrSubtype.setStatus(_A)
class _LldpNeighborManAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborManAddr_Type.__name__=_C
_LldpNeighborManAddr_Object=MibTableColumn
lldpNeighborManAddr=_LldpNeighborManAddr_Object((1,3,6,1,4,1,11863,6,35,1,2,3,1,4),_LldpNeighborManAddr_Type())
lldpNeighborManAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManAddr.setStatus(_A)
class _LldpNeighborManAddrIfSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),(_G,2),('sysPortNumber',3)))
_LldpNeighborManAddrIfSubtype_Type.__name__=_D
_LldpNeighborManAddrIfSubtype_Object=MibTableColumn
lldpNeighborManAddrIfSubtype=_LldpNeighborManAddrIfSubtype_Object((1,3,6,1,4,1,11863,6,35,1,2,3,1,5),_LldpNeighborManAddrIfSubtype_Type())
lldpNeighborManAddrIfSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManAddrIfSubtype.setStatus(_A)
_LldpNeighborManAddrIfId_Type=Integer32
_LldpNeighborManAddrIfId_Object=MibTableColumn
lldpNeighborManAddrIfId=_LldpNeighborManAddrIfId_Object((1,3,6,1,4,1,11863,6,35,1,2,3,1,6),_LldpNeighborManAddrIfId_Type())
lldpNeighborManAddrIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManAddrIfId.setStatus(_A)
class _LldpNeighborManAddrIfOID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_LldpNeighborManAddrIfOID_Type.__name__=_C
_LldpNeighborManAddrIfOID_Object=MibTableColumn
lldpNeighborManAddrIfOID=_LldpNeighborManAddrIfOID_Object((1,3,6,1,4,1,11863,6,35,1,2,3,1,7),_LldpNeighborManAddrIfOID_Type())
lldpNeighborManAddrIfOID.setMaxAccess(_B)
if mibBuilder.loadTexts:lldpNeighborManAddrIfOID.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'lldpInfo':lldpInfo,'lldpLocalInfoTable':lldpLocalInfoTable,'lldpLocalInfoEntry':lldpLocalInfoEntry,'lldpLocalPortId':lldpLocalPortId,'lldpLocalChassisIdType':lldpLocalChassisIdType,'lldpLocalChassisId':lldpLocalChassisId,'lldpLocalPortIdType':lldpLocalPortIdType,'lldpLocalPortIdDescr':lldpLocalPortIdDescr,'lldpLocalTtl':lldpLocalTtl,'lldpLocalPortDescr':lldpLocalPortDescr,'lldpLocalDeviceName':lldpLocalDeviceName,'lldpLocalDeviceDescr':lldpLocalDeviceDescr,'lldpLocalCapAvailable':lldpLocalCapAvailable,'lldpLocalCapEnabled':lldpLocalCapEnabled,'lldpLocalManageIpAddr':lldpLocalManageIpAddr,'lldpLocalManageAddrType':lldpLocalManageAddrType,'lldpLocalManageAddrInterfaceType':lldpLocalManageAddrInterfaceType,'lldpLocalManageAddrInterfaceId':lldpLocalManageAddrInterfaceId,'lldpLocalManageAddrOID':lldpLocalManageAddrOID,'lldpLocalPortAndProtocolVlanID':lldpLocalPortAndProtocolVlanID,'lldpLocalVlanName':lldpLocalVlanName,'lldpLocalAutoNegotiationSupported':lldpLocalAutoNegotiationSupported,'lldpLocalAutoNegotiationEnabled':lldpLocalAutoNegotiationEnabled,'lldpLocalOperMau':lldpLocalOperMau,'lldpLocalLinkAggregationSupported':lldpLocalLinkAggregationSupported,'lldpLocalLinkAggregationEnabled':lldpLocalLinkAggregationEnabled,'lldpLocalAggregationPortId':lldpLocalAggregationPortId,'lldpLocalPowerPortClass':lldpLocalPowerPortClass,'lldpLocalPsePowerSupported':lldpLocalPsePowerSupported,'lldpLocalPsePowerEnabled':lldpLocalPsePowerEnabled,'lldpLocalPsePairsControlAbility':lldpLocalPsePairsControlAbility,'lldpLocalMaximumFrameSize':lldpLocalMaximumFrameSize,'lldpNeighborInfoTable':lldpNeighborInfoTable,'lldpNeighborInfoEntry':lldpNeighborInfoEntry,'lldpNeighborPortId':lldpNeighborPortId,_J:lldpNeighborPortIndexId,'lldpNeighborChassisIdType':lldpNeighborChassisIdType,'lldpNeighborChassisId':lldpNeighborChassisId,'lldpNeighborPortIdType':lldpNeighborPortIdType,'lldpNeighborPortIdDescr':lldpNeighborPortIdDescr,'lldpNeighborTtl':lldpNeighborTtl,'lldpNeighborPortDescr':lldpNeighborPortDescr,'lldpNeighborDeviceName':lldpNeighborDeviceName,'lldpNeighborDeviceDescr':lldpNeighborDeviceDescr,'lldpNeighborCapAvailable':lldpNeighborCapAvailable,'lldpNeighborCapEnabled':lldpNeighborCapEnabled,'lldpNeighborManageIpAddr':lldpNeighborManageIpAddr,'lldpNeighborManageAddrType':lldpNeighborManageAddrType,'lldpNeighborManageAddrInterfaceType':lldpNeighborManageAddrInterfaceType,'lldpNeighborManageAddrInterfaceId':lldpNeighborManageAddrInterfaceId,'lldpNeighborManageAddrOID':lldpNeighborManageAddrOID,'lldpNeighborPortAndProtocolVlanID':lldpNeighborPortAndProtocolVlanID,'lldpNeighborVlanName':lldpNeighborVlanName,'lldpNeighborProtocolIdentity':lldpNeighborProtocolIdentity,'lldpNeighborAutoNegotiationSupported':lldpNeighborAutoNegotiationSupported,'lldpNeighborAutoNegotiationEnabled':lldpNeighborAutoNegotiationEnabled,'lldpNeighborOperMau':lldpNeighborOperMau,'lldpNeighborLinkAggregationSupported':lldpNeighborLinkAggregationSupported,'lldpNeighborLinkAggregationEnabled':lldpNeighborLinkAggregationEnabled,'lldpNeighborAggregationPortId':lldpNeighborAggregationPortId,'lldpNeighborPowerPortClass':lldpNeighborPowerPortClass,'lldpNeighborPsePowerSupported':lldpNeighborPsePowerSupported,'lldpNeighborPsePowerEnabled':lldpNeighborPsePowerEnabled,'lldpNeighborPsePairsControlAbility':lldpNeighborPsePairsControlAbility,'lldpNeighborMaximumFrameSize':lldpNeighborMaximumFrameSize,'lldpNeighborManAddrTable':lldpNeighborManAddrTable,'lldpNeighborManAddrEntry':lldpNeighborManAddrEntry,'lldpNeighborManAddrPortId':lldpNeighborManAddrPortId,_K:lldpNeighborManAddrPortIndexId,_L:lldpNeighborManAddrSubtype,_M:lldpNeighborManAddr,'lldpNeighborManAddrIfSubtype':lldpNeighborManAddrIfSubtype,'lldpNeighborManAddrIfId':lldpNeighborManAddrIfId,'lldpNeighborManAddrIfOID':lldpNeighborManAddrIfOID})