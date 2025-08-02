_F='biboPingIndex'
_E='BIANCA-BRICK-PING-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Biboip_ObjectIdentity=ObjectIdentity
biboip=_Biboip_ObjectIdentity((1,3,6,1,4,1,272,4,5))
_Biboping_ObjectIdentity=ObjectIdentity
biboping=_Biboping_ObjectIdentity((1,3,6,1,4,1,272,4,5,27))
_BiboPingTable_Object=MibTable
biboPingTable=_BiboPingTable_Object((1,3,6,1,4,1,272,4,5,27,1))
if mibBuilder.loadTexts:biboPingTable.setStatus(_A)
_BiboPingEntry_Object=MibTableRow
biboPingEntry=_BiboPingEntry_Object((1,3,6,1,4,1,272,4,5,27,1,1))
biboPingEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:biboPingEntry.setStatus(_A)
class _BiboPingIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BiboPingIndex_Type.__name__=_B
_BiboPingIndex_Object=MibTableColumn
biboPingIndex=_BiboPingIndex_Object((1,3,6,1,4,1,272,4,5,27,1,1,1),_BiboPingIndex_Type())
biboPingIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:biboPingIndex.setStatus(_A)
class _BiboPingStatus_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notinservice',2),('notready',3),('createandgo',4),('createandwait',5),('delete',6)))
_BiboPingStatus_Type.__name__=_B
_BiboPingStatus_Object=MibTableColumn
biboPingStatus=_BiboPingStatus_Object((1,3,6,1,4,1,272,4,5,27,1,1,2),_BiboPingStatus_Type())
biboPingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:biboPingStatus.setStatus(_A)
class _BiboPingCompleted_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_BiboPingCompleted_Type.__name__=_B
_BiboPingCompleted_Object=MibTableColumn
biboPingCompleted=_BiboPingCompleted_Object((1,3,6,1,4,1,272,4,5,27,1,1,3),_BiboPingCompleted_Type())
biboPingCompleted.setMaxAccess(_D)
if mibBuilder.loadTexts:biboPingCompleted.setStatus(_A)
_BiboPingSourceAddress_Type=IpAddress
_BiboPingSourceAddress_Object=MibTableColumn
biboPingSourceAddress=_BiboPingSourceAddress_Object((1,3,6,1,4,1,272,4,5,27,1,1,4),_BiboPingSourceAddress_Type())
biboPingSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:biboPingSourceAddress.setStatus(_A)
_BiboPingAddress_Type=IpAddress
_BiboPingAddress_Object=MibTableColumn
biboPingAddress=_BiboPingAddress_Object((1,3,6,1,4,1,272,4,5,27,1,1,5),_BiboPingAddress_Type())
biboPingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:biboPingAddress.setStatus(_A)
class _BiboPingPacketCount_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BiboPingPacketCount_Type.__name__=_B
_BiboPingPacketCount_Object=MibTableColumn
biboPingPacketCount=_BiboPingPacketCount_Object((1,3,6,1,4,1,272,4,5,27,1,1,6),_BiboPingPacketCount_Type())
biboPingPacketCount.setMaxAccess(_C)
if mibBuilder.loadTexts:biboPingPacketCount.setStatus(_A)
class _BiboPingPacketSize_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,4096))
_BiboPingPacketSize_Type.__name__=_B
_BiboPingPacketSize_Object=MibTableColumn
biboPingPacketSize=_BiboPingPacketSize_Object((1,3,6,1,4,1,272,4,5,27,1,1,7),_BiboPingPacketSize_Type())
biboPingPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:biboPingPacketSize.setStatus(_A)
class _BiboPingPacketTimeout_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BiboPingPacketTimeout_Type.__name__=_B
_BiboPingPacketTimeout_Object=MibTableColumn
biboPingPacketTimeout=_BiboPingPacketTimeout_Object((1,3,6,1,4,1,272,4,5,27,1,1,8),_BiboPingPacketTimeout_Type())
biboPingPacketTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:biboPingPacketTimeout.setStatus(_A)
class _BiboPingReceivedPackets_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BiboPingReceivedPackets_Type.__name__=_B
_BiboPingReceivedPackets_Object=MibTableColumn
biboPingReceivedPackets=_BiboPingReceivedPackets_Object((1,3,6,1,4,1,272,4,5,27,1,1,9),_BiboPingReceivedPackets_Type())
biboPingReceivedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:biboPingReceivedPackets.setStatus(_A)
class _BiboPingMinRoundTrip_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BiboPingMinRoundTrip_Type.__name__=_B
_BiboPingMinRoundTrip_Object=MibTableColumn
biboPingMinRoundTrip=_BiboPingMinRoundTrip_Object((1,3,6,1,4,1,272,4,5,27,1,1,10),_BiboPingMinRoundTrip_Type())
biboPingMinRoundTrip.setMaxAccess(_D)
if mibBuilder.loadTexts:biboPingMinRoundTrip.setStatus(_A)
class _BiboPingMaxRoundTrip_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BiboPingMaxRoundTrip_Type.__name__=_B
_BiboPingMaxRoundTrip_Object=MibTableColumn
biboPingMaxRoundTrip=_BiboPingMaxRoundTrip_Object((1,3,6,1,4,1,272,4,5,27,1,1,11),_BiboPingMaxRoundTrip_Type())
biboPingMaxRoundTrip.setMaxAccess(_D)
if mibBuilder.loadTexts:biboPingMaxRoundTrip.setStatus(_A)
class _BiboPingAvgRoundTrip_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BiboPingAvgRoundTrip_Type.__name__=_B
_BiboPingAvgRoundTrip_Object=MibTableColumn
biboPingAvgRoundTrip=_BiboPingAvgRoundTrip_Object((1,3,6,1,4,1,272,4,5,27,1,1,12),_BiboPingAvgRoundTrip_Type())
biboPingAvgRoundTrip.setMaxAccess(_D)
if mibBuilder.loadTexts:biboPingAvgRoundTrip.setStatus(_A)
class _BiboPingTTL_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BiboPingTTL_Type.__name__=_B
_BiboPingTTL_Object=MibTableColumn
biboPingTTL=_BiboPingTTL_Object((1,3,6,1,4,1,272,4,5,27,1,1,13),_BiboPingTTL_Type())
biboPingTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:biboPingTTL.setStatus(_A)
class _BiboPingTOS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BiboPingTOS_Type.__name__=_B
_BiboPingTOS_Object=MibTableColumn
biboPingTOS=_BiboPingTOS_Object((1,3,6,1,4,1,272,4,5,27,1,1,14),_BiboPingTOS_Type())
biboPingTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:biboPingTOS.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bintec':bintec,'bibo':bibo,'biboip':biboip,'biboping':biboping,'biboPingTable':biboPingTable,'biboPingEntry':biboPingEntry,_F:biboPingIndex,'biboPingStatus':biboPingStatus,'biboPingCompleted':biboPingCompleted,'biboPingSourceAddress':biboPingSourceAddress,'biboPingAddress':biboPingAddress,'biboPingPacketCount':biboPingPacketCount,'biboPingPacketSize':biboPingPacketSize,'biboPingPacketTimeout':biboPingPacketTimeout,'biboPingReceivedPackets':biboPingReceivedPackets,'biboPingMinRoundTrip':biboPingMinRoundTrip,'biboPingMaxRoundTrip':biboPingMaxRoundTrip,'biboPingAvgRoundTrip':biboPingAvgRoundTrip,'biboPingTTL':biboPingTTL,'biboPingTOS':biboPingTOS})