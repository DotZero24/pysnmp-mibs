_F='pingIndex'
_E='AT-PING-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ping=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,58))
if mibBuilder.loadTexts:ping.setRevisions(('2006-06-28 12:22',))
_PingTraps_ObjectIdentity=ObjectIdentity
pingTraps=_PingTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,58,0))
_PingTable_Object=MibTable
pingTable=_PingTable_Object((1,3,6,1,4,1,207,8,4,4,4,58,1))
if mibBuilder.loadTexts:pingTable.setStatus(_A)
_PingEntry_Object=MibTableRow
pingEntry=_PingEntry_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1))
pingEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pingEntry.setStatus(_A)
class _PingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_PingIndex_Type.__name__=_C
_PingIndex_Object=MibTableColumn
pingIndex=_PingIndex_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,1),_PingIndex_Type())
pingIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pingIndex.setStatus(_A)
class _PingProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('undefined',0),('apple',1),('ip',2),('ipx',3),('osi',4)))
_PingProtocol_Type.__name__=_C
_PingProtocol_Object=MibTableColumn
pingProtocol=_PingProtocol_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,2),_PingProtocol_Type())
pingProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:pingProtocol.setStatus(_A)
_PingAddress_Type=OctetString
_PingAddress_Object=MibTableColumn
pingAddress=_PingAddress_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,3),_PingAddress_Type())
pingAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:pingAddress.setStatus(_A)
class _PingNumberOfPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PingNumberOfPackets_Type.__name__=_C
_PingNumberOfPackets_Object=MibTableColumn
pingNumberOfPackets=_PingNumberOfPackets_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,4),_PingNumberOfPackets_Type())
pingNumberOfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pingNumberOfPackets.setStatus(_A)
class _PingPacketSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1500))
_PingPacketSize_Type.__name__=_C
_PingPacketSize_Object=MibTableColumn
pingPacketSize=_PingPacketSize_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,5),_PingPacketSize_Type())
pingPacketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:pingPacketSize.setStatus(_A)
class _PingTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PingTimeout_Type.__name__=_C
_PingTimeout_Object=MibTableColumn
pingTimeout=_PingTimeout_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,6),_PingTimeout_Type())
pingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:pingTimeout.setStatus(_A)
class _PingDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PingDelay_Type.__name__=_C
_PingDelay_Object=MibTableColumn
pingDelay=_PingDelay_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,7),_PingDelay_Type())
pingDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:pingDelay.setStatus(_A)
_PingTrapOnCompletion_Type=TruthValue
_PingTrapOnCompletion_Object=MibTableColumn
pingTrapOnCompletion=_PingTrapOnCompletion_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,8),_PingTrapOnCompletion_Type())
pingTrapOnCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:pingTrapOnCompletion.setStatus(_A)
class _PingTypeOfService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PingTypeOfService_Type.__name__=_C
_PingTypeOfService_Object=MibTableColumn
pingTypeOfService=_PingTypeOfService_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,9),_PingTypeOfService_Type())
pingTypeOfService.setMaxAccess(_B)
if mibBuilder.loadTexts:pingTypeOfService.setStatus(_A)
_PingPattern_Type=Unsigned32
_PingPattern_Object=MibTableColumn
pingPattern=_PingPattern_Object((1,3,6,1,4,1,207,8,4,4,4,58,1,1,10),_PingPattern_Type())
pingPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:pingPattern.setStatus(_A)
class _PingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('startRunning',1),('stopStopped',2)))
_PingStatus_Type.__name__=_C
_PingStatus_Object=MibScalar
pingStatus=_PingStatus_Object((1,3,6,1,4,1,207,8,4,4,4,58,2),_PingStatus_Type())
pingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pingStatus.setStatus(_A)
_PingStatistics_ObjectIdentity=ObjectIdentity
pingStatistics=_PingStatistics_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,58,3))
_PingSentPackets_Type=Integer32
_PingSentPackets_Object=MibScalar
pingSentPackets=_PingSentPackets_Object((1,3,6,1,4,1,207,8,4,4,4,58,3,1),_PingSentPackets_Type())
pingSentPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:pingSentPackets.setStatus(_A)
_PingReceivedPackets_Type=Integer32
_PingReceivedPackets_Object=MibScalar
pingReceivedPackets=_PingReceivedPackets_Object((1,3,6,1,4,1,207,8,4,4,4,58,3,2),_PingReceivedPackets_Type())
pingReceivedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:pingReceivedPackets.setStatus(_A)
_PingMinimumRoundTripTime_Type=Integer32
_PingMinimumRoundTripTime_Object=MibScalar
pingMinimumRoundTripTime=_PingMinimumRoundTripTime_Object((1,3,6,1,4,1,207,8,4,4,4,58,3,3),_PingMinimumRoundTripTime_Type())
pingMinimumRoundTripTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pingMinimumRoundTripTime.setStatus(_A)
_PingAverageRoundTripTime_Type=Integer32
_PingAverageRoundTripTime_Object=MibScalar
pingAverageRoundTripTime=_PingAverageRoundTripTime_Object((1,3,6,1,4,1,207,8,4,4,4,58,3,4),_PingAverageRoundTripTime_Type())
pingAverageRoundTripTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pingAverageRoundTripTime.setStatus(_A)
_PingMaximumRoundTripTime_Type=Integer32
_PingMaximumRoundTripTime_Object=MibScalar
pingMaximumRoundTripTime=_PingMaximumRoundTripTime_Object((1,3,6,1,4,1,207,8,4,4,4,58,3,5),_PingMaximumRoundTripTime_Type())
pingMaximumRoundTripTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pingMaximumRoundTripTime.setStatus(_A)
pingTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,58,0,1))
if mibBuilder.loadTexts:pingTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ping':ping,'pingTraps':pingTraps,'pingTrap':pingTrap,'pingTable':pingTable,'pingEntry':pingEntry,_F:pingIndex,'pingProtocol':pingProtocol,'pingAddress':pingAddress,'pingNumberOfPackets':pingNumberOfPackets,'pingPacketSize':pingPacketSize,'pingTimeout':pingTimeout,'pingDelay':pingDelay,'pingTrapOnCompletion':pingTrapOnCompletion,'pingTypeOfService':pingTypeOfService,'pingPattern':pingPattern,'pingStatus':pingStatus,'pingStatistics':pingStatistics,'pingSentPackets':pingSentPackets,'pingReceivedPackets':pingReceivedPackets,'pingMinimumRoundTripTime':pingMinimumRoundTripTime,'pingAverageRoundTripTime':pingAverageRoundTripTime,'pingMaximumRoundTripTime':pingMaximumRoundTripTime})