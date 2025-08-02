_H='active'
_G='inActive'
_F='imagingStatisticsIndex'
_E='pcoipStatisticsIndex'
_D='TERADICI-PCOIP-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
teraMibModule=ModuleIdentity((1,3,6,1,4,1,25071))
if mibBuilder.loadTexts:teraMibModule.setRevisions(('2008-01-28 10:00',))
_TeraProducts_ObjectIdentity=ObjectIdentity
teraProducts=_TeraProducts_ObjectIdentity((1,3,6,1,4,1,25071,1))
_TeraPcoip_ObjectIdentity=ObjectIdentity
teraPcoip=_TeraPcoip_ObjectIdentity((1,3,6,1,4,1,25071,1,1))
_TeraPcoipStatistics_ObjectIdentity=ObjectIdentity
teraPcoipStatistics=_TeraPcoipStatistics_ObjectIdentity((1,3,6,1,4,1,25071,1,1,1))
_PcoipStatisticsTable_Object=MibTable
pcoipStatisticsTable=_PcoipStatisticsTable_Object((1,3,6,1,4,1,25071,1,1,1,1))
if mibBuilder.loadTexts:pcoipStatisticsTable.setStatus(_A)
_PcoipStatisticsEntry_Object=MibTableRow
pcoipStatisticsEntry=_PcoipStatisticsEntry_Object((1,3,6,1,4,1,25071,1,1,1,1,1))
pcoipStatisticsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pcoipStatisticsEntry.setStatus(_A)
class _PcoipStatisticsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipStatisticsIndex_Type.__name__=_C
_PcoipStatisticsIndex_Object=MibTableColumn
pcoipStatisticsIndex=_PcoipStatisticsIndex_Object((1,3,6,1,4,1,25071,1,1,1,1,1,1),_PcoipStatisticsIndex_Type())
pcoipStatisticsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipStatisticsIndex.setStatus(_A)
class _PcoipStatisticsSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_PcoipStatisticsSessionNumber_Type.__name__=_C
_PcoipStatisticsSessionNumber_Object=MibTableColumn
pcoipStatisticsSessionNumber=_PcoipStatisticsSessionNumber_Object((1,3,6,1,4,1,25071,1,1,1,1,1,2),_PcoipStatisticsSessionNumber_Type())
pcoipStatisticsSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipStatisticsSessionNumber.setStatus(_A)
_PcoipStatisticsPcoipPacketsTransmitted_Type=Counter64
_PcoipStatisticsPcoipPacketsTransmitted_Object=MibTableColumn
pcoipStatisticsPcoipPacketsTransmitted=_PcoipStatisticsPcoipPacketsTransmitted_Object((1,3,6,1,4,1,25071,1,1,1,1,1,3),_PcoipStatisticsPcoipPacketsTransmitted_Type())
pcoipStatisticsPcoipPacketsTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipStatisticsPcoipPacketsTransmitted.setStatus(_A)
_PcoipStatisticsPcoipBytesTransmitted_Type=Counter64
_PcoipStatisticsPcoipBytesTransmitted_Object=MibTableColumn
pcoipStatisticsPcoipBytesTransmitted=_PcoipStatisticsPcoipBytesTransmitted_Object((1,3,6,1,4,1,25071,1,1,1,1,1,4),_PcoipStatisticsPcoipBytesTransmitted_Type())
pcoipStatisticsPcoipBytesTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipStatisticsPcoipBytesTransmitted.setStatus(_A)
_PcoipStatisticsPcoipPacketsReceived_Type=Counter64
_PcoipStatisticsPcoipPacketsReceived_Object=MibTableColumn
pcoipStatisticsPcoipPacketsReceived=_PcoipStatisticsPcoipPacketsReceived_Object((1,3,6,1,4,1,25071,1,1,1,1,1,5),_PcoipStatisticsPcoipPacketsReceived_Type())
pcoipStatisticsPcoipPacketsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipStatisticsPcoipPacketsReceived.setStatus(_A)
_PcoipStatisticsPcoipBytesReceived_Type=Counter64
_PcoipStatisticsPcoipBytesReceived_Object=MibTableColumn
pcoipStatisticsPcoipBytesReceived=_PcoipStatisticsPcoipBytesReceived_Object((1,3,6,1,4,1,25071,1,1,1,1,1,6),_PcoipStatisticsPcoipBytesReceived_Type())
pcoipStatisticsPcoipBytesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipStatisticsPcoipBytesReceived.setStatus(_A)
_PcoipStatisticsPcoipLostPackets_Type=Counter64
_PcoipStatisticsPcoipLostPackets_Object=MibTableColumn
pcoipStatisticsPcoipLostPackets=_PcoipStatisticsPcoipLostPackets_Object((1,3,6,1,4,1,25071,1,1,1,1,1,7),_PcoipStatisticsPcoipLostPackets_Type())
pcoipStatisticsPcoipLostPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipStatisticsPcoipLostPackets.setStatus(_A)
class _PcoipStatisticsPcoipLatency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PcoipStatisticsPcoipLatency_Type.__name__=_C
_PcoipStatisticsPcoipLatency_Object=MibTableColumn
pcoipStatisticsPcoipLatency=_PcoipStatisticsPcoipLatency_Object((1,3,6,1,4,1,25071,1,1,1,1,1,8),_PcoipStatisticsPcoipLatency_Type())
pcoipStatisticsPcoipLatency.setMaxAccess(_B)
if mibBuilder.loadTexts:pcoipStatisticsPcoipLatency.setStatus(_A)
_TeraImagingStatistics_ObjectIdentity=ObjectIdentity
teraImagingStatistics=_TeraImagingStatistics_ObjectIdentity((1,3,6,1,4,1,25071,1,1,2))
_ImagingStatisticsTable_Object=MibTable
imagingStatisticsTable=_ImagingStatisticsTable_Object((1,3,6,1,4,1,25071,1,1,2,1))
if mibBuilder.loadTexts:imagingStatisticsTable.setStatus(_A)
_ImagingStatisticsEntry_Object=MibTableRow
imagingStatisticsEntry=_ImagingStatisticsEntry_Object((1,3,6,1,4,1,25071,1,1,2,1,1))
imagingStatisticsEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:imagingStatisticsEntry.setStatus(_A)
class _ImagingStatisticsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ImagingStatisticsIndex_Type.__name__=_C
_ImagingStatisticsIndex_Object=MibTableColumn
imagingStatisticsIndex=_ImagingStatisticsIndex_Object((1,3,6,1,4,1,25071,1,1,2,1,1,1),_ImagingStatisticsIndex_Type())
imagingStatisticsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:imagingStatisticsIndex.setStatus(_A)
class _ImagingStatisticsSessionNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_ImagingStatisticsSessionNumber_Type.__name__=_C
_ImagingStatisticsSessionNumber_Object=MibTableColumn
imagingStatisticsSessionNumber=_ImagingStatisticsSessionNumber_Object((1,3,6,1,4,1,25071,1,1,2,1,1,2),_ImagingStatisticsSessionNumber_Type())
imagingStatisticsSessionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:imagingStatisticsSessionNumber.setStatus(_A)
class _ImagingStatisticsSessionActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ImagingStatisticsSessionActive_Type.__name__=_C
_ImagingStatisticsSessionActive_Object=MibTableColumn
imagingStatisticsSessionActive=_ImagingStatisticsSessionActive_Object((1,3,6,1,4,1,25071,1,1,2,1,1,3),_ImagingStatisticsSessionActive_Type())
imagingStatisticsSessionActive.setMaxAccess(_B)
if mibBuilder.loadTexts:imagingStatisticsSessionActive.setStatus(_A)
class _ImagingStatisticsDisplayActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_ImagingStatisticsDisplayActive_Type.__name__=_C
_ImagingStatisticsDisplayActive_Object=MibTableColumn
imagingStatisticsDisplayActive=_ImagingStatisticsDisplayActive_Object((1,3,6,1,4,1,25071,1,1,2,1,1,4),_ImagingStatisticsDisplayActive_Type())
imagingStatisticsDisplayActive.setMaxAccess(_B)
if mibBuilder.loadTexts:imagingStatisticsDisplayActive.setStatus(_A)
class _ImagingStatisticsDisplayWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1600))
_ImagingStatisticsDisplayWidth_Type.__name__=_C
_ImagingStatisticsDisplayWidth_Object=MibTableColumn
imagingStatisticsDisplayWidth=_ImagingStatisticsDisplayWidth_Object((1,3,6,1,4,1,25071,1,1,2,1,1,5),_ImagingStatisticsDisplayWidth_Type())
imagingStatisticsDisplayWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:imagingStatisticsDisplayWidth.setStatus(_A)
class _ImagingStatisticsDisplayHeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1600))
_ImagingStatisticsDisplayHeight_Type.__name__=_C
_ImagingStatisticsDisplayHeight_Object=MibTableColumn
imagingStatisticsDisplayHeight=_ImagingStatisticsDisplayHeight_Object((1,3,6,1,4,1,25071,1,1,2,1,1,6),_ImagingStatisticsDisplayHeight_Type())
imagingStatisticsDisplayHeight.setMaxAccess(_B)
if mibBuilder.loadTexts:imagingStatisticsDisplayHeight.setStatus(_A)
class _ImagingStatisticsDisplayRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_ImagingStatisticsDisplayRefreshRate_Type.__name__=_C
_ImagingStatisticsDisplayRefreshRate_Object=MibTableColumn
imagingStatisticsDisplayRefreshRate=_ImagingStatisticsDisplayRefreshRate_Object((1,3,6,1,4,1,25071,1,1,2,1,1,7),_ImagingStatisticsDisplayRefreshRate_Type())
imagingStatisticsDisplayRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:imagingStatisticsDisplayRefreshRate.setStatus(_A)
_ImagingStatisticsFrameCount_Type=Counter64
_ImagingStatisticsFrameCount_Object=MibTableColumn
imagingStatisticsFrameCount=_ImagingStatisticsFrameCount_Object((1,3,6,1,4,1,25071,1,1,2,1,1,8),_ImagingStatisticsFrameCount_Type())
imagingStatisticsFrameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:imagingStatisticsFrameCount.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'teraMibModule':teraMibModule,'teraProducts':teraProducts,'teraPcoip':teraPcoip,'teraPcoipStatistics':teraPcoipStatistics,'pcoipStatisticsTable':pcoipStatisticsTable,'pcoipStatisticsEntry':pcoipStatisticsEntry,_E:pcoipStatisticsIndex,'pcoipStatisticsSessionNumber':pcoipStatisticsSessionNumber,'pcoipStatisticsPcoipPacketsTransmitted':pcoipStatisticsPcoipPacketsTransmitted,'pcoipStatisticsPcoipBytesTransmitted':pcoipStatisticsPcoipBytesTransmitted,'pcoipStatisticsPcoipPacketsReceived':pcoipStatisticsPcoipPacketsReceived,'pcoipStatisticsPcoipBytesReceived':pcoipStatisticsPcoipBytesReceived,'pcoipStatisticsPcoipLostPackets':pcoipStatisticsPcoipLostPackets,'pcoipStatisticsPcoipLatency':pcoipStatisticsPcoipLatency,'teraImagingStatistics':teraImagingStatistics,'imagingStatisticsTable':imagingStatisticsTable,'imagingStatisticsEntry':imagingStatisticsEntry,_F:imagingStatisticsIndex,'imagingStatisticsSessionNumber':imagingStatisticsSessionNumber,'imagingStatisticsSessionActive':imagingStatisticsSessionActive,'imagingStatisticsDisplayActive':imagingStatisticsDisplayActive,'imagingStatisticsDisplayWidth':imagingStatisticsDisplayWidth,'imagingStatisticsDisplayHeight':imagingStatisticsDisplayHeight,'imagingStatisticsDisplayRefreshRate':imagingStatisticsDisplayRefreshRate,'imagingStatisticsFrameCount':imagingStatisticsFrameCount})