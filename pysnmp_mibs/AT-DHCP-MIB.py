_M='dhcpRangeExhaustedGateway'
_L='dhcpClientIpAddress'
_K='dhcpRangeExceededPercentage'
_J='dhcpRangeExceededRemaining'
_I='dhcpRangeExceededClients'
_H='dhcpRangeExceededRange'
_G='dhcpRangeIndex'
_F='DisplayStringUnsized'
_E='dhcpRangeExhaustedInterface'
_D='Integer32'
_C='read-only'
_B='AT-DHCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB',_F,'modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
dhcp=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,70))
if mibBuilder.loadTexts:dhcp.setRevisions(('2009-04-01 02:00','2006-06-28 12:22'))
_DhcpTraps_ObjectIdentity=ObjectIdentity
dhcpTraps=_DhcpTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,70,0))
_DhcpRangeTable_Object=MibTable
dhcpRangeTable=_DhcpRangeTable_Object((1,3,6,1,4,1,207,8,4,4,4,70,1))
if mibBuilder.loadTexts:dhcpRangeTable.setStatus(_A)
_DhcpRangeEntry_Object=MibTableRow
dhcpRangeEntry=_DhcpRangeEntry_Object((1,3,6,1,4,1,207,8,4,4,4,70,1,1))
dhcpRangeEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:dhcpRangeEntry.setStatus(_A)
_DhcpRangeIndex_Type=Integer32
_DhcpRangeIndex_Object=MibTableColumn
dhcpRangeIndex=_DhcpRangeIndex_Object((1,3,6,1,4,1,207,8,4,4,4,70,1,1,1),_DhcpRangeIndex_Type())
dhcpRangeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeIndex.setStatus(_A)
class _DhcpRangeName_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_DhcpRangeName_Type.__name__=_F
_DhcpRangeName_Object=MibTableColumn
dhcpRangeName=_DhcpRangeName_Object((1,3,6,1,4,1,207,8,4,4,4,70,1,1,2),_DhcpRangeName_Type())
dhcpRangeName.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeName.setStatus(_A)
_DhcpRangeBaseAddress_Type=IpAddress
_DhcpRangeBaseAddress_Object=MibTableColumn
dhcpRangeBaseAddress=_DhcpRangeBaseAddress_Object((1,3,6,1,4,1,207,8,4,4,4,70,1,1,3),_DhcpRangeBaseAddress_Type())
dhcpRangeBaseAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeBaseAddress.setStatus(_A)
class _DhcpRangeNumberOfAddresses_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_DhcpRangeNumberOfAddresses_Type.__name__=_D
_DhcpRangeNumberOfAddresses_Object=MibTableColumn
dhcpRangeNumberOfAddresses=_DhcpRangeNumberOfAddresses_Object((1,3,6,1,4,1,207,8,4,4,4,70,1,1,4),_DhcpRangeNumberOfAddresses_Type())
dhcpRangeNumberOfAddresses.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeNumberOfAddresses.setStatus(_A)
_DhcpRangeGateway_Type=IpAddress
_DhcpRangeGateway_Object=MibTableColumn
dhcpRangeGateway=_DhcpRangeGateway_Object((1,3,6,1,4,1,207,8,4,4,4,70,1,1,5),_DhcpRangeGateway_Type())
dhcpRangeGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeGateway.setStatus(_A)
_DhcpTrapVariable_ObjectIdentity=ObjectIdentity
dhcpTrapVariable=_DhcpTrapVariable_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,70,2))
_DhcpRangeExhaustedGateway_Type=IpAddress
_DhcpRangeExhaustedGateway_Object=MibScalar
dhcpRangeExhaustedGateway=_DhcpRangeExhaustedGateway_Object((1,3,6,1,4,1,207,8,4,4,4,70,2,1),_DhcpRangeExhaustedGateway_Type())
dhcpRangeExhaustedGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeExhaustedGateway.setStatus(_A)
_DhcpRangeExhaustedInterface_Type=IpAddress
_DhcpRangeExhaustedInterface_Object=MibScalar
dhcpRangeExhaustedInterface=_DhcpRangeExhaustedInterface_Object((1,3,6,1,4,1,207,8,4,4,4,70,2,2),_DhcpRangeExhaustedInterface_Type())
dhcpRangeExhaustedInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeExhaustedInterface.setStatus(_A)
class _DhcpRangeExceededRange_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_DhcpRangeExceededRange_Type.__name__=_F
_DhcpRangeExceededRange_Object=MibScalar
dhcpRangeExceededRange=_DhcpRangeExceededRange_Object((1,3,6,1,4,1,207,8,4,4,4,70,2,3),_DhcpRangeExceededRange_Type())
dhcpRangeExceededRange.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeExceededRange.setStatus(_A)
class _DhcpRangeExceededClients_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_DhcpRangeExceededClients_Type.__name__=_D
_DhcpRangeExceededClients_Object=MibScalar
dhcpRangeExceededClients=_DhcpRangeExceededClients_Object((1,3,6,1,4,1,207,8,4,4,4,70,2,4),_DhcpRangeExceededClients_Type())
dhcpRangeExceededClients.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeExceededClients.setStatus(_A)
class _DhcpRangeExceededRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_DhcpRangeExceededRemaining_Type.__name__=_D
_DhcpRangeExceededRemaining_Object=MibScalar
dhcpRangeExceededRemaining=_DhcpRangeExceededRemaining_Object((1,3,6,1,4,1,207,8,4,4,4,70,2,5),_DhcpRangeExceededRemaining_Type())
dhcpRangeExceededRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeExceededRemaining.setStatus(_A)
class _DhcpRangeExceededPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DhcpRangeExceededPercentage_Type.__name__=_D
_DhcpRangeExceededPercentage_Object=MibScalar
dhcpRangeExceededPercentage=_DhcpRangeExceededPercentage_Object((1,3,6,1,4,1,207,8,4,4,4,70,2,6),_DhcpRangeExceededPercentage_Type())
dhcpRangeExceededPercentage.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpRangeExceededPercentage.setStatus(_A)
_DhcpClientTable_Object=MibTable
dhcpClientTable=_DhcpClientTable_Object((1,3,6,1,4,1,207,8,4,4,4,70,3))
if mibBuilder.loadTexts:dhcpClientTable.setStatus(_A)
_DhcpClientEntry_Object=MibTableRow
dhcpClientEntry=_DhcpClientEntry_Object((1,3,6,1,4,1,207,8,4,4,4,70,3,1))
dhcpClientEntry.setIndexNames((0,_B,_G),(0,_B,_L))
if mibBuilder.loadTexts:dhcpClientEntry.setStatus(_A)
_DhcpClientIpAddress_Type=IpAddress
_DhcpClientIpAddress_Object=MibTableColumn
dhcpClientIpAddress=_DhcpClientIpAddress_Object((1,3,6,1,4,1,207,8,4,4,4,70,3,1,1),_DhcpClientIpAddress_Type())
dhcpClientIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpClientIpAddress.setStatus(_A)
_DhcpClientID_Type=OctetString
_DhcpClientID_Object=MibTableColumn
dhcpClientID=_DhcpClientID_Object((1,3,6,1,4,1,207,8,4,4,4,70,3,1,2),_DhcpClientID_Type())
dhcpClientID.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpClientID.setStatus(_A)
class _DhcpClientState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unused',0),('reclaiming',1),('inuse',2),('offered',3)))
_DhcpClientState_Type.__name__=_D
_DhcpClientState_Object=MibTableColumn
dhcpClientState=_DhcpClientState_Object((1,3,6,1,4,1,207,8,4,4,4,70,3,1,3),_DhcpClientState_Type())
dhcpClientState.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpClientState.setStatus(_A)
class _DhcpClientType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('dyn',2),('static',3)))
_DhcpClientType_Type.__name__=_D
_DhcpClientType_Object=MibTableColumn
dhcpClientType=_DhcpClientType_Object((1,3,6,1,4,1,207,8,4,4,4,70,3,1,4),_DhcpClientType_Type())
dhcpClientType.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpClientType.setStatus(_A)
_DhcpClientExpiry_Type=OctetString
_DhcpClientExpiry_Object=MibTableColumn
dhcpClientExpiry=_DhcpClientExpiry_Object((1,3,6,1,4,1,207,8,4,4,4,70,3,1,5),_DhcpClientExpiry_Type())
dhcpClientExpiry.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpClientExpiry.setStatus(_A)
dhcpRangeExhaustedTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,70,0,1))
dhcpRangeExhaustedTrap.setObjects(*((_B,_M),(_B,_E)))
if mibBuilder.loadTexts:dhcpRangeExhaustedTrap.setStatus(_A)
dhcpRangeExceededThresholdTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,70,0,2))
dhcpRangeExceededThresholdTrap.setObjects(*((_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:dhcpRangeExceededThresholdTrap.setStatus(_A)
dhcpRangeExceededThresholdClearTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,70,0,3))
dhcpRangeExceededThresholdClearTrap.setObjects(*((_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:dhcpRangeExceededThresholdClearTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dhcp':dhcp,'dhcpTraps':dhcpTraps,'dhcpRangeExhaustedTrap':dhcpRangeExhaustedTrap,'dhcpRangeExceededThresholdTrap':dhcpRangeExceededThresholdTrap,'dhcpRangeExceededThresholdClearTrap':dhcpRangeExceededThresholdClearTrap,'dhcpRangeTable':dhcpRangeTable,'dhcpRangeEntry':dhcpRangeEntry,_G:dhcpRangeIndex,'dhcpRangeName':dhcpRangeName,'dhcpRangeBaseAddress':dhcpRangeBaseAddress,'dhcpRangeNumberOfAddresses':dhcpRangeNumberOfAddresses,'dhcpRangeGateway':dhcpRangeGateway,'dhcpTrapVariable':dhcpTrapVariable,_M:dhcpRangeExhaustedGateway,_E:dhcpRangeExhaustedInterface,_H:dhcpRangeExceededRange,_I:dhcpRangeExceededClients,_J:dhcpRangeExceededRemaining,_K:dhcpRangeExceededPercentage,'dhcpClientTable':dhcpClientTable,'dhcpClientEntry':dhcpClientEntry,_L:dhcpClientIpAddress,'dhcpClientID':dhcpClientID,'dhcpClientState':dhcpClientState,'dhcpClientType':dhcpClientType,'dhcpClientExpiry':dhcpClientExpiry})