_g='tptThresholdNotifyZonePair'
_f='tptThresholdNotifySignatureID'
_e='tptThresholdNotifyPolicyID'
_d='tptThresholdNotifyDeviceID'
_c='interfaceHistDaysIndex'
_b='interfaceHistDaysIfIndex'
_a='interfaceHistHoursIndex'
_Z='interfaceHistHoursIfIndex'
_Y='interfaceHistMinutesIndex'
_X='interfaceHistMinutesIfIndex'
_W='interfaceHistSecondsIndex'
_V='interfaceHistSecondsIfIndex'
_U='thresholdGlobalID'
_T='thresholdHistDaysIndex'
_S='thresholdHistDaysGlobalID'
_R='thresholdHistHoursIndex'
_Q='thresholdHistHoursGlobalID'
_P='thresholdHistMinutesIndex'
_O='thresholdHistMinutesGlobalID'
_N='thresholdHistSecondsIndex'
_M='thresholdHistSecondsGlobalID'
_L='rateLimitHistHoursIndex'
_K='rateLimitHistHoursGlobalID'
_J='rateLimitHistMinutesIndex'
_I='rateLimitHistMinutesGlobalID'
_H='rateLimitHistSecondsIndex'
_G='rateLimitHistSecondsGlobalID'
_F='rateLimitGlobalID'
_E='OctetString'
_D='not-accessible'
_C='TPT-TRAFFIC-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_eventsV2,tpt_tpa_objs,tpt_tpa_unkparams=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-eventsV2','tpt-tpa-objs','tpt-tpa-unkparams')
tpt_traffic=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,8))
if mibBuilder.loadTexts:tpt_traffic.setRevisions(('2016-05-25 18:54',))
class ThresholdFilterState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('green',1),('yellow',2),('red',3)))
_RateLimitTable_Object=MibTable
rateLimitTable=_RateLimitTable_Object((1,3,6,1,4,1,10734,3,3,2,8,1))
if mibBuilder.loadTexts:rateLimitTable.setStatus(_A)
_RateLimitEntry_Object=MibTableRow
rateLimitEntry=_RateLimitEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1))
rateLimitEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:rateLimitEntry.setStatus(_A)
class _RateLimitGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RateLimitGlobalID_Type.__name__=_E
_RateLimitGlobalID_Object=MibTableColumn
rateLimitGlobalID=_RateLimitGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1,1),_RateLimitGlobalID_Type())
rateLimitGlobalID.setMaxAccess(_D)
if mibBuilder.loadTexts:rateLimitGlobalID.setStatus(_A)
_RateLimitRequestedRate_Type=Unsigned32
_RateLimitRequestedRate_Object=MibTableColumn
rateLimitRequestedRate=_RateLimitRequestedRate_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1,2),_RateLimitRequestedRate_Type())
rateLimitRequestedRate.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitRequestedRate.setStatus(_A)
_RateLimitActualRate_Type=Unsigned32
_RateLimitActualRate_Object=MibTableColumn
rateLimitActualRate=_RateLimitActualRate_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1,3),_RateLimitActualRate_Type())
rateLimitActualRate.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitActualRate.setStatus(_A)
_RateLimitPacketsSent_Type=Counter64
_RateLimitPacketsSent_Object=MibTableColumn
rateLimitPacketsSent=_RateLimitPacketsSent_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1,4),_RateLimitPacketsSent_Type())
rateLimitPacketsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitPacketsSent.setStatus(_A)
_RateLimitPacketsDropped_Type=Counter64
_RateLimitPacketsDropped_Object=MibTableColumn
rateLimitPacketsDropped=_RateLimitPacketsDropped_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1,5),_RateLimitPacketsDropped_Type())
rateLimitPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitPacketsDropped.setStatus(_A)
_RateLimitPacketsQueued_Type=Counter64
_RateLimitPacketsQueued_Object=MibTableColumn
rateLimitPacketsQueued=_RateLimitPacketsQueued_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1,6),_RateLimitPacketsQueued_Type())
rateLimitPacketsQueued.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitPacketsQueued.setStatus(_A)
_RateLimitHistNumSeconds_Type=Unsigned32
_RateLimitHistNumSeconds_Object=MibTableColumn
rateLimitHistNumSeconds=_RateLimitHistNumSeconds_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1,7),_RateLimitHistNumSeconds_Type())
rateLimitHistNumSeconds.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitHistNumSeconds.setStatus(_A)
_RateLimitHistNumMinutes_Type=Unsigned32
_RateLimitHistNumMinutes_Object=MibTableColumn
rateLimitHistNumMinutes=_RateLimitHistNumMinutes_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1,8),_RateLimitHistNumMinutes_Type())
rateLimitHistNumMinutes.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitHistNumMinutes.setStatus(_A)
_RateLimitHistNumHours_Type=Unsigned32
_RateLimitHistNumHours_Object=MibTableColumn
rateLimitHistNumHours=_RateLimitHistNumHours_Object((1,3,6,1,4,1,10734,3,3,2,8,1,1,9),_RateLimitHistNumHours_Type())
rateLimitHistNumHours.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitHistNumHours.setStatus(_A)
_RateLimitHistSecondsTable_Object=MibTable
rateLimitHistSecondsTable=_RateLimitHistSecondsTable_Object((1,3,6,1,4,1,10734,3,3,2,8,2))
if mibBuilder.loadTexts:rateLimitHistSecondsTable.setStatus(_A)
_RateLimitHistSecondsEntry_Object=MibTableRow
rateLimitHistSecondsEntry=_RateLimitHistSecondsEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,2,1))
rateLimitHistSecondsEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:rateLimitHistSecondsEntry.setStatus(_A)
class _RateLimitHistSecondsGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RateLimitHistSecondsGlobalID_Type.__name__=_E
_RateLimitHistSecondsGlobalID_Object=MibTableColumn
rateLimitHistSecondsGlobalID=_RateLimitHistSecondsGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,8,2,1,1),_RateLimitHistSecondsGlobalID_Type())
rateLimitHistSecondsGlobalID.setMaxAccess(_D)
if mibBuilder.loadTexts:rateLimitHistSecondsGlobalID.setStatus(_A)
_RateLimitHistSecondsIndex_Type=Unsigned32
_RateLimitHistSecondsIndex_Object=MibTableColumn
rateLimitHistSecondsIndex=_RateLimitHistSecondsIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,2,1,2),_RateLimitHistSecondsIndex_Type())
rateLimitHistSecondsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rateLimitHistSecondsIndex.setStatus(_A)
_RateLimitHistSecondsBytesSent_Type=Counter64
_RateLimitHistSecondsBytesSent_Object=MibTableColumn
rateLimitHistSecondsBytesSent=_RateLimitHistSecondsBytesSent_Object((1,3,6,1,4,1,10734,3,3,2,8,2,1,3),_RateLimitHistSecondsBytesSent_Type())
rateLimitHistSecondsBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitHistSecondsBytesSent.setStatus(_A)
_RateLimitHistSecondsTimestamp_Type=Unsigned32
_RateLimitHistSecondsTimestamp_Object=MibTableColumn
rateLimitHistSecondsTimestamp=_RateLimitHistSecondsTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,2,1,4),_RateLimitHistSecondsTimestamp_Type())
rateLimitHistSecondsTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitHistSecondsTimestamp.setStatus(_A)
_RateLimitHistMinutesTable_Object=MibTable
rateLimitHistMinutesTable=_RateLimitHistMinutesTable_Object((1,3,6,1,4,1,10734,3,3,2,8,3))
if mibBuilder.loadTexts:rateLimitHistMinutesTable.setStatus(_A)
_RateLimitHistMinutesEntry_Object=MibTableRow
rateLimitHistMinutesEntry=_RateLimitHistMinutesEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,3,1))
rateLimitHistMinutesEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:rateLimitHistMinutesEntry.setStatus(_A)
class _RateLimitHistMinutesGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RateLimitHistMinutesGlobalID_Type.__name__=_E
_RateLimitHistMinutesGlobalID_Object=MibTableColumn
rateLimitHistMinutesGlobalID=_RateLimitHistMinutesGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,8,3,1,1),_RateLimitHistMinutesGlobalID_Type())
rateLimitHistMinutesGlobalID.setMaxAccess(_D)
if mibBuilder.loadTexts:rateLimitHistMinutesGlobalID.setStatus(_A)
_RateLimitHistMinutesIndex_Type=Unsigned32
_RateLimitHistMinutesIndex_Object=MibTableColumn
rateLimitHistMinutesIndex=_RateLimitHistMinutesIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,3,1,2),_RateLimitHistMinutesIndex_Type())
rateLimitHistMinutesIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rateLimitHistMinutesIndex.setStatus(_A)
_RateLimitHistMinutesBytesSent_Type=Counter64
_RateLimitHistMinutesBytesSent_Object=MibTableColumn
rateLimitHistMinutesBytesSent=_RateLimitHistMinutesBytesSent_Object((1,3,6,1,4,1,10734,3,3,2,8,3,1,3),_RateLimitHistMinutesBytesSent_Type())
rateLimitHistMinutesBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitHistMinutesBytesSent.setStatus(_A)
_RateLimitHistMinutesTimestamp_Type=Unsigned32
_RateLimitHistMinutesTimestamp_Object=MibTableColumn
rateLimitHistMinutesTimestamp=_RateLimitHistMinutesTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,3,1,4),_RateLimitHistMinutesTimestamp_Type())
rateLimitHistMinutesTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitHistMinutesTimestamp.setStatus(_A)
_RateLimitHistHoursTable_Object=MibTable
rateLimitHistHoursTable=_RateLimitHistHoursTable_Object((1,3,6,1,4,1,10734,3,3,2,8,4))
if mibBuilder.loadTexts:rateLimitHistHoursTable.setStatus(_A)
_RateLimitHistHoursEntry_Object=MibTableRow
rateLimitHistHoursEntry=_RateLimitHistHoursEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,4,1))
rateLimitHistHoursEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:rateLimitHistHoursEntry.setStatus(_A)
class _RateLimitHistHoursGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_RateLimitHistHoursGlobalID_Type.__name__=_E
_RateLimitHistHoursGlobalID_Object=MibTableColumn
rateLimitHistHoursGlobalID=_RateLimitHistHoursGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,8,4,1,1),_RateLimitHistHoursGlobalID_Type())
rateLimitHistHoursGlobalID.setMaxAccess(_D)
if mibBuilder.loadTexts:rateLimitHistHoursGlobalID.setStatus(_A)
_RateLimitHistHoursIndex_Type=Unsigned32
_RateLimitHistHoursIndex_Object=MibTableColumn
rateLimitHistHoursIndex=_RateLimitHistHoursIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,4,1,2),_RateLimitHistHoursIndex_Type())
rateLimitHistHoursIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rateLimitHistHoursIndex.setStatus(_A)
_RateLimitHistHoursBytesSent_Type=Counter64
_RateLimitHistHoursBytesSent_Object=MibTableColumn
rateLimitHistHoursBytesSent=_RateLimitHistHoursBytesSent_Object((1,3,6,1,4,1,10734,3,3,2,8,4,1,3),_RateLimitHistHoursBytesSent_Type())
rateLimitHistHoursBytesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitHistHoursBytesSent.setStatus(_A)
_RateLimitHistHoursTimestamp_Type=Unsigned32
_RateLimitHistHoursTimestamp_Object=MibTableColumn
rateLimitHistHoursTimestamp=_RateLimitHistHoursTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,4,1,4),_RateLimitHistHoursTimestamp_Type())
rateLimitHistHoursTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:rateLimitHistHoursTimestamp.setStatus(_A)
_ThresholdHistSecondsTable_Object=MibTable
thresholdHistSecondsTable=_ThresholdHistSecondsTable_Object((1,3,6,1,4,1,10734,3,3,2,8,5))
if mibBuilder.loadTexts:thresholdHistSecondsTable.setStatus(_A)
_ThresholdHistSecondsEntry_Object=MibTableRow
thresholdHistSecondsEntry=_ThresholdHistSecondsEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,5,1))
thresholdHistSecondsEntry.setIndexNames((0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:thresholdHistSecondsEntry.setStatus(_A)
class _ThresholdHistSecondsGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ThresholdHistSecondsGlobalID_Type.__name__=_E
_ThresholdHistSecondsGlobalID_Object=MibTableColumn
thresholdHistSecondsGlobalID=_ThresholdHistSecondsGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,8,5,1,1),_ThresholdHistSecondsGlobalID_Type())
thresholdHistSecondsGlobalID.setMaxAccess(_D)
if mibBuilder.loadTexts:thresholdHistSecondsGlobalID.setStatus(_A)
_ThresholdHistSecondsIndex_Type=Unsigned32
_ThresholdHistSecondsIndex_Object=MibTableColumn
thresholdHistSecondsIndex=_ThresholdHistSecondsIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,5,1,2),_ThresholdHistSecondsIndex_Type())
thresholdHistSecondsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:thresholdHistSecondsIndex.setStatus(_A)
_ThresholdHistSecondsUnitCount_Type=Counter64
_ThresholdHistSecondsUnitCount_Object=MibTableColumn
thresholdHistSecondsUnitCount=_ThresholdHistSecondsUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,8,5,1,3),_ThresholdHistSecondsUnitCount_Type())
thresholdHistSecondsUnitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdHistSecondsUnitCount.setStatus(_A)
_ThresholdHistSecondsTimestamp_Type=Unsigned32
_ThresholdHistSecondsTimestamp_Object=MibTableColumn
thresholdHistSecondsTimestamp=_ThresholdHistSecondsTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,5,1,4),_ThresholdHistSecondsTimestamp_Type())
thresholdHistSecondsTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdHistSecondsTimestamp.setStatus(_A)
_ThresholdHistMinutesTable_Object=MibTable
thresholdHistMinutesTable=_ThresholdHistMinutesTable_Object((1,3,6,1,4,1,10734,3,3,2,8,6))
if mibBuilder.loadTexts:thresholdHistMinutesTable.setStatus(_A)
_ThresholdHistMinutesEntry_Object=MibTableRow
thresholdHistMinutesEntry=_ThresholdHistMinutesEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,6,1))
thresholdHistMinutesEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:thresholdHistMinutesEntry.setStatus(_A)
class _ThresholdHistMinutesGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ThresholdHistMinutesGlobalID_Type.__name__=_E
_ThresholdHistMinutesGlobalID_Object=MibTableColumn
thresholdHistMinutesGlobalID=_ThresholdHistMinutesGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,8,6,1,1),_ThresholdHistMinutesGlobalID_Type())
thresholdHistMinutesGlobalID.setMaxAccess(_D)
if mibBuilder.loadTexts:thresholdHistMinutesGlobalID.setStatus(_A)
_ThresholdHistMinutesIndex_Type=Unsigned32
_ThresholdHistMinutesIndex_Object=MibTableColumn
thresholdHistMinutesIndex=_ThresholdHistMinutesIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,6,1,2),_ThresholdHistMinutesIndex_Type())
thresholdHistMinutesIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:thresholdHistMinutesIndex.setStatus(_A)
_ThresholdHistMinutesUnitCount_Type=Counter64
_ThresholdHistMinutesUnitCount_Object=MibTableColumn
thresholdHistMinutesUnitCount=_ThresholdHistMinutesUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,8,6,1,3),_ThresholdHistMinutesUnitCount_Type())
thresholdHistMinutesUnitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdHistMinutesUnitCount.setStatus(_A)
_ThresholdHistMinutesTimestamp_Type=Unsigned32
_ThresholdHistMinutesTimestamp_Object=MibTableColumn
thresholdHistMinutesTimestamp=_ThresholdHistMinutesTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,6,1,4),_ThresholdHistMinutesTimestamp_Type())
thresholdHistMinutesTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdHistMinutesTimestamp.setStatus(_A)
_ThresholdHistHoursTable_Object=MibTable
thresholdHistHoursTable=_ThresholdHistHoursTable_Object((1,3,6,1,4,1,10734,3,3,2,8,7))
if mibBuilder.loadTexts:thresholdHistHoursTable.setStatus(_A)
_ThresholdHistHoursEntry_Object=MibTableRow
thresholdHistHoursEntry=_ThresholdHistHoursEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,7,1))
thresholdHistHoursEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:thresholdHistHoursEntry.setStatus(_A)
class _ThresholdHistHoursGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ThresholdHistHoursGlobalID_Type.__name__=_E
_ThresholdHistHoursGlobalID_Object=MibTableColumn
thresholdHistHoursGlobalID=_ThresholdHistHoursGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,8,7,1,1),_ThresholdHistHoursGlobalID_Type())
thresholdHistHoursGlobalID.setMaxAccess(_D)
if mibBuilder.loadTexts:thresholdHistHoursGlobalID.setStatus(_A)
_ThresholdHistHoursIndex_Type=Unsigned32
_ThresholdHistHoursIndex_Object=MibTableColumn
thresholdHistHoursIndex=_ThresholdHistHoursIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,7,1,2),_ThresholdHistHoursIndex_Type())
thresholdHistHoursIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:thresholdHistHoursIndex.setStatus(_A)
_ThresholdHistHoursUnitCount_Type=Counter64
_ThresholdHistHoursUnitCount_Object=MibTableColumn
thresholdHistHoursUnitCount=_ThresholdHistHoursUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,8,7,1,3),_ThresholdHistHoursUnitCount_Type())
thresholdHistHoursUnitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdHistHoursUnitCount.setStatus(_A)
_ThresholdHistHoursTimestamp_Type=Unsigned32
_ThresholdHistHoursTimestamp_Object=MibTableColumn
thresholdHistHoursTimestamp=_ThresholdHistHoursTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,7,1,4),_ThresholdHistHoursTimestamp_Type())
thresholdHistHoursTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdHistHoursTimestamp.setStatus(_A)
_ThresholdHistDaysTable_Object=MibTable
thresholdHistDaysTable=_ThresholdHistDaysTable_Object((1,3,6,1,4,1,10734,3,3,2,8,8))
if mibBuilder.loadTexts:thresholdHistDaysTable.setStatus(_A)
_ThresholdHistDaysEntry_Object=MibTableRow
thresholdHistDaysEntry=_ThresholdHistDaysEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,8,1))
thresholdHistDaysEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:thresholdHistDaysEntry.setStatus(_A)
class _ThresholdHistDaysGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ThresholdHistDaysGlobalID_Type.__name__=_E
_ThresholdHistDaysGlobalID_Object=MibTableColumn
thresholdHistDaysGlobalID=_ThresholdHistDaysGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,8,8,1,1),_ThresholdHistDaysGlobalID_Type())
thresholdHistDaysGlobalID.setMaxAccess(_D)
if mibBuilder.loadTexts:thresholdHistDaysGlobalID.setStatus(_A)
_ThresholdHistDaysIndex_Type=Unsigned32
_ThresholdHistDaysIndex_Object=MibTableColumn
thresholdHistDaysIndex=_ThresholdHistDaysIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,8,1,2),_ThresholdHistDaysIndex_Type())
thresholdHistDaysIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:thresholdHistDaysIndex.setStatus(_A)
_ThresholdHistDaysUnitCount_Type=Counter64
_ThresholdHistDaysUnitCount_Object=MibTableColumn
thresholdHistDaysUnitCount=_ThresholdHistDaysUnitCount_Object((1,3,6,1,4,1,10734,3,3,2,8,8,1,3),_ThresholdHistDaysUnitCount_Type())
thresholdHistDaysUnitCount.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdHistDaysUnitCount.setStatus(_A)
_ThresholdHistDaysTimestamp_Type=Unsigned32
_ThresholdHistDaysTimestamp_Object=MibTableColumn
thresholdHistDaysTimestamp=_ThresholdHistDaysTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,8,1,4),_ThresholdHistDaysTimestamp_Type())
thresholdHistDaysTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdHistDaysTimestamp.setStatus(_A)
_ThresholdTable_Object=MibTable
thresholdTable=_ThresholdTable_Object((1,3,6,1,4,1,10734,3,3,2,8,9))
if mibBuilder.loadTexts:thresholdTable.setStatus(_A)
_ThresholdEntry_Object=MibTableRow
thresholdEntry=_ThresholdEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,9,1))
thresholdEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:thresholdEntry.setStatus(_A)
class _ThresholdGlobalID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ThresholdGlobalID_Type.__name__=_E
_ThresholdGlobalID_Object=MibTableColumn
thresholdGlobalID=_ThresholdGlobalID_Object((1,3,6,1,4,1,10734,3,3,2,8,9,1,1),_ThresholdGlobalID_Type())
thresholdGlobalID.setMaxAccess(_D)
if mibBuilder.loadTexts:thresholdGlobalID.setStatus(_A)
_ThresholdState_Type=ThresholdFilterState
_ThresholdState_Object=MibTableColumn
thresholdState=_ThresholdState_Object((1,3,6,1,4,1,10734,3,3,2,8,9,1,2),_ThresholdState_Type())
thresholdState.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdState.setStatus(_A)
class _ThresholdUnits_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ThresholdUnits_Type.__name__=_E
_ThresholdUnits_Object=MibTableColumn
thresholdUnits=_ThresholdUnits_Object((1,3,6,1,4,1,10734,3,3,2,8,9,1,3),_ThresholdUnits_Type())
thresholdUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:thresholdUnits.setStatus(_A)
_InterfaceHistSecondsTable_Object=MibTable
interfaceHistSecondsTable=_InterfaceHistSecondsTable_Object((1,3,6,1,4,1,10734,3,3,2,8,10))
if mibBuilder.loadTexts:interfaceHistSecondsTable.setStatus(_A)
_InterfaceHistSecondsEntry_Object=MibTableRow
interfaceHistSecondsEntry=_InterfaceHistSecondsEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,10,1))
interfaceHistSecondsEntry.setIndexNames((0,_C,_V),(0,_C,_W))
if mibBuilder.loadTexts:interfaceHistSecondsEntry.setStatus(_A)
_InterfaceHistSecondsIfIndex_Type=InterfaceIndex
_InterfaceHistSecondsIfIndex_Object=MibTableColumn
interfaceHistSecondsIfIndex=_InterfaceHistSecondsIfIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,10,1,1),_InterfaceHistSecondsIfIndex_Type())
interfaceHistSecondsIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceHistSecondsIfIndex.setStatus(_A)
_InterfaceHistSecondsIndex_Type=Unsigned32
_InterfaceHistSecondsIndex_Object=MibTableColumn
interfaceHistSecondsIndex=_InterfaceHistSecondsIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,10,1,2),_InterfaceHistSecondsIndex_Type())
interfaceHistSecondsIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceHistSecondsIndex.setStatus(_A)
_InterfaceHistSecondsUnitCountIn_Type=Counter64
_InterfaceHistSecondsUnitCountIn_Object=MibTableColumn
interfaceHistSecondsUnitCountIn=_InterfaceHistSecondsUnitCountIn_Object((1,3,6,1,4,1,10734,3,3,2,8,10,1,3),_InterfaceHistSecondsUnitCountIn_Type())
interfaceHistSecondsUnitCountIn.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistSecondsUnitCountIn.setStatus(_A)
_InterfaceHistSecondsUnitCountOut_Type=Counter64
_InterfaceHistSecondsUnitCountOut_Object=MibTableColumn
interfaceHistSecondsUnitCountOut=_InterfaceHistSecondsUnitCountOut_Object((1,3,6,1,4,1,10734,3,3,2,8,10,1,4),_InterfaceHistSecondsUnitCountOut_Type())
interfaceHistSecondsUnitCountOut.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistSecondsUnitCountOut.setStatus(_A)
_InterfaceHistSecondsTimestamp_Type=Unsigned32
_InterfaceHistSecondsTimestamp_Object=MibTableColumn
interfaceHistSecondsTimestamp=_InterfaceHistSecondsTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,10,1,5),_InterfaceHistSecondsTimestamp_Type())
interfaceHistSecondsTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistSecondsTimestamp.setStatus(_A)
_InterfaceHistMinutesTable_Object=MibTable
interfaceHistMinutesTable=_InterfaceHistMinutesTable_Object((1,3,6,1,4,1,10734,3,3,2,8,11))
if mibBuilder.loadTexts:interfaceHistMinutesTable.setStatus(_A)
_InterfaceHistMinutesEntry_Object=MibTableRow
interfaceHistMinutesEntry=_InterfaceHistMinutesEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,11,1))
interfaceHistMinutesEntry.setIndexNames((0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:interfaceHistMinutesEntry.setStatus(_A)
_InterfaceHistMinutesIfIndex_Type=InterfaceIndex
_InterfaceHistMinutesIfIndex_Object=MibTableColumn
interfaceHistMinutesIfIndex=_InterfaceHistMinutesIfIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,11,1,1),_InterfaceHistMinutesIfIndex_Type())
interfaceHistMinutesIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceHistMinutesIfIndex.setStatus(_A)
_InterfaceHistMinutesIndex_Type=Unsigned32
_InterfaceHistMinutesIndex_Object=MibTableColumn
interfaceHistMinutesIndex=_InterfaceHistMinutesIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,11,1,2),_InterfaceHistMinutesIndex_Type())
interfaceHistMinutesIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceHistMinutesIndex.setStatus(_A)
_InterfaceHistMinutesUnitCountIn_Type=Counter64
_InterfaceHistMinutesUnitCountIn_Object=MibTableColumn
interfaceHistMinutesUnitCountIn=_InterfaceHistMinutesUnitCountIn_Object((1,3,6,1,4,1,10734,3,3,2,8,11,1,3),_InterfaceHistMinutesUnitCountIn_Type())
interfaceHistMinutesUnitCountIn.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistMinutesUnitCountIn.setStatus(_A)
_InterfaceHistMinutesUnitCountOut_Type=Counter64
_InterfaceHistMinutesUnitCountOut_Object=MibTableColumn
interfaceHistMinutesUnitCountOut=_InterfaceHistMinutesUnitCountOut_Object((1,3,6,1,4,1,10734,3,3,2,8,11,1,4),_InterfaceHistMinutesUnitCountOut_Type())
interfaceHistMinutesUnitCountOut.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistMinutesUnitCountOut.setStatus(_A)
_InterfaceHistMinutesTimestamp_Type=Unsigned32
_InterfaceHistMinutesTimestamp_Object=MibTableColumn
interfaceHistMinutesTimestamp=_InterfaceHistMinutesTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,11,1,5),_InterfaceHistMinutesTimestamp_Type())
interfaceHistMinutesTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistMinutesTimestamp.setStatus(_A)
_InterfaceHistHoursTable_Object=MibTable
interfaceHistHoursTable=_InterfaceHistHoursTable_Object((1,3,6,1,4,1,10734,3,3,2,8,12))
if mibBuilder.loadTexts:interfaceHistHoursTable.setStatus(_A)
_InterfaceHistHoursEntry_Object=MibTableRow
interfaceHistHoursEntry=_InterfaceHistHoursEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,12,1))
interfaceHistHoursEntry.setIndexNames((0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:interfaceHistHoursEntry.setStatus(_A)
_InterfaceHistHoursIfIndex_Type=InterfaceIndex
_InterfaceHistHoursIfIndex_Object=MibTableColumn
interfaceHistHoursIfIndex=_InterfaceHistHoursIfIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,12,1,1),_InterfaceHistHoursIfIndex_Type())
interfaceHistHoursIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceHistHoursIfIndex.setStatus(_A)
_InterfaceHistHoursIndex_Type=Unsigned32
_InterfaceHistHoursIndex_Object=MibTableColumn
interfaceHistHoursIndex=_InterfaceHistHoursIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,12,1,2),_InterfaceHistHoursIndex_Type())
interfaceHistHoursIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceHistHoursIndex.setStatus(_A)
_InterfaceHistHoursUnitCountIn_Type=Counter64
_InterfaceHistHoursUnitCountIn_Object=MibTableColumn
interfaceHistHoursUnitCountIn=_InterfaceHistHoursUnitCountIn_Object((1,3,6,1,4,1,10734,3,3,2,8,12,1,3),_InterfaceHistHoursUnitCountIn_Type())
interfaceHistHoursUnitCountIn.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistHoursUnitCountIn.setStatus(_A)
_InterfaceHistHoursUnitCountOut_Type=Counter64
_InterfaceHistHoursUnitCountOut_Object=MibTableColumn
interfaceHistHoursUnitCountOut=_InterfaceHistHoursUnitCountOut_Object((1,3,6,1,4,1,10734,3,3,2,8,12,1,4),_InterfaceHistHoursUnitCountOut_Type())
interfaceHistHoursUnitCountOut.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistHoursUnitCountOut.setStatus(_A)
_InterfaceHistHoursTimestamp_Type=Unsigned32
_InterfaceHistHoursTimestamp_Object=MibTableColumn
interfaceHistHoursTimestamp=_InterfaceHistHoursTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,12,1,5),_InterfaceHistHoursTimestamp_Type())
interfaceHistHoursTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistHoursTimestamp.setStatus(_A)
_InterfaceHistDaysTable_Object=MibTable
interfaceHistDaysTable=_InterfaceHistDaysTable_Object((1,3,6,1,4,1,10734,3,3,2,8,13))
if mibBuilder.loadTexts:interfaceHistDaysTable.setStatus(_A)
_InterfaceHistDaysEntry_Object=MibTableRow
interfaceHistDaysEntry=_InterfaceHistDaysEntry_Object((1,3,6,1,4,1,10734,3,3,2,8,13,1))
interfaceHistDaysEntry.setIndexNames((0,_C,_b),(0,_C,_c))
if mibBuilder.loadTexts:interfaceHistDaysEntry.setStatus(_A)
_InterfaceHistDaysIfIndex_Type=InterfaceIndex
_InterfaceHistDaysIfIndex_Object=MibTableColumn
interfaceHistDaysIfIndex=_InterfaceHistDaysIfIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,13,1,1),_InterfaceHistDaysIfIndex_Type())
interfaceHistDaysIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceHistDaysIfIndex.setStatus(_A)
_InterfaceHistDaysIndex_Type=Unsigned32
_InterfaceHistDaysIndex_Object=MibTableColumn
interfaceHistDaysIndex=_InterfaceHistDaysIndex_Object((1,3,6,1,4,1,10734,3,3,2,8,13,1,2),_InterfaceHistDaysIndex_Type())
interfaceHistDaysIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:interfaceHistDaysIndex.setStatus(_A)
_InterfaceHistDaysUnitCountIn_Type=Counter64
_InterfaceHistDaysUnitCountIn_Object=MibTableColumn
interfaceHistDaysUnitCountIn=_InterfaceHistDaysUnitCountIn_Object((1,3,6,1,4,1,10734,3,3,2,8,13,1,3),_InterfaceHistDaysUnitCountIn_Type())
interfaceHistDaysUnitCountIn.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistDaysUnitCountIn.setStatus(_A)
_InterfaceHistDaysUnitCountOut_Type=Counter64
_InterfaceHistDaysUnitCountOut_Object=MibTableColumn
interfaceHistDaysUnitCountOut=_InterfaceHistDaysUnitCountOut_Object((1,3,6,1,4,1,10734,3,3,2,8,13,1,4),_InterfaceHistDaysUnitCountOut_Type())
interfaceHistDaysUnitCountOut.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistDaysUnitCountOut.setStatus(_A)
_InterfaceHistDaysTimestamp_Type=Unsigned32
_InterfaceHistDaysTimestamp_Object=MibTableColumn
interfaceHistDaysTimestamp=_InterfaceHistDaysTimestamp_Object((1,3,6,1,4,1,10734,3,3,2,8,13,1,5),_InterfaceHistDaysTimestamp_Type())
interfaceHistDaysTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceHistDaysTimestamp.setStatus(_A)
class _TptThresholdNotifyDeviceID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptThresholdNotifyDeviceID_Type.__name__=_E
_TptThresholdNotifyDeviceID_Object=MibScalar
tptThresholdNotifyDeviceID=_TptThresholdNotifyDeviceID_Object((1,3,6,1,4,1,10734,3,3,3,1,111),_TptThresholdNotifyDeviceID_Type())
tptThresholdNotifyDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptThresholdNotifyDeviceID.setStatus(_A)
class _TptThresholdNotifyPolicyID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptThresholdNotifyPolicyID_Type.__name__=_E
_TptThresholdNotifyPolicyID_Object=MibScalar
tptThresholdNotifyPolicyID=_TptThresholdNotifyPolicyID_Object((1,3,6,1,4,1,10734,3,3,3,1,112),_TptThresholdNotifyPolicyID_Type())
tptThresholdNotifyPolicyID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptThresholdNotifyPolicyID.setStatus(_A)
class _TptThresholdNotifySignatureID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_TptThresholdNotifySignatureID_Type.__name__=_E
_TptThresholdNotifySignatureID_Object=MibScalar
tptThresholdNotifySignatureID=_TptThresholdNotifySignatureID_Object((1,3,6,1,4,1,10734,3,3,3,1,113),_TptThresholdNotifySignatureID_Type())
tptThresholdNotifySignatureID.setMaxAccess(_B)
if mibBuilder.loadTexts:tptThresholdNotifySignatureID.setStatus(_A)
class _TptThresholdNotifySegmentName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TptThresholdNotifySegmentName_Type.__name__=_E
_TptThresholdNotifySegmentName_Object=MibScalar
tptThresholdNotifySegmentName=_TptThresholdNotifySegmentName_Object((1,3,6,1,4,1,10734,3,3,3,1,114),_TptThresholdNotifySegmentName_Type())
tptThresholdNotifySegmentName.setMaxAccess(_B)
if mibBuilder.loadTexts:tptThresholdNotifySegmentName.setStatus('obsolete')
class _TptThresholdNotifyZonePair_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TptThresholdNotifyZonePair_Type.__name__=_E
_TptThresholdNotifyZonePair_Object=MibScalar
tptThresholdNotifyZonePair=_TptThresholdNotifyZonePair_Object((1,3,6,1,4,1,10734,3,3,3,1,115),_TptThresholdNotifyZonePair_Type())
tptThresholdNotifyZonePair.setMaxAccess(_B)
if mibBuilder.loadTexts:tptThresholdNotifyZonePair.setStatus(_A)
tptThresholdFilterNotify=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,17))
tptThresholdFilterNotify.setObjects(*((_C,_d),(_C,_e),(_C,_f),(_C,_g)))
if mibBuilder.loadTexts:tptThresholdFilterNotify.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ThresholdFilterState':ThresholdFilterState,'tpt-traffic':tpt_traffic,'rateLimitTable':rateLimitTable,'rateLimitEntry':rateLimitEntry,_F:rateLimitGlobalID,'rateLimitRequestedRate':rateLimitRequestedRate,'rateLimitActualRate':rateLimitActualRate,'rateLimitPacketsSent':rateLimitPacketsSent,'rateLimitPacketsDropped':rateLimitPacketsDropped,'rateLimitPacketsQueued':rateLimitPacketsQueued,'rateLimitHistNumSeconds':rateLimitHistNumSeconds,'rateLimitHistNumMinutes':rateLimitHistNumMinutes,'rateLimitHistNumHours':rateLimitHistNumHours,'rateLimitHistSecondsTable':rateLimitHistSecondsTable,'rateLimitHistSecondsEntry':rateLimitHistSecondsEntry,_G:rateLimitHistSecondsGlobalID,_H:rateLimitHistSecondsIndex,'rateLimitHistSecondsBytesSent':rateLimitHistSecondsBytesSent,'rateLimitHistSecondsTimestamp':rateLimitHistSecondsTimestamp,'rateLimitHistMinutesTable':rateLimitHistMinutesTable,'rateLimitHistMinutesEntry':rateLimitHistMinutesEntry,_I:rateLimitHistMinutesGlobalID,_J:rateLimitHistMinutesIndex,'rateLimitHistMinutesBytesSent':rateLimitHistMinutesBytesSent,'rateLimitHistMinutesTimestamp':rateLimitHistMinutesTimestamp,'rateLimitHistHoursTable':rateLimitHistHoursTable,'rateLimitHistHoursEntry':rateLimitHistHoursEntry,_K:rateLimitHistHoursGlobalID,_L:rateLimitHistHoursIndex,'rateLimitHistHoursBytesSent':rateLimitHistHoursBytesSent,'rateLimitHistHoursTimestamp':rateLimitHistHoursTimestamp,'thresholdHistSecondsTable':thresholdHistSecondsTable,'thresholdHistSecondsEntry':thresholdHistSecondsEntry,_M:thresholdHistSecondsGlobalID,_N:thresholdHistSecondsIndex,'thresholdHistSecondsUnitCount':thresholdHistSecondsUnitCount,'thresholdHistSecondsTimestamp':thresholdHistSecondsTimestamp,'thresholdHistMinutesTable':thresholdHistMinutesTable,'thresholdHistMinutesEntry':thresholdHistMinutesEntry,_O:thresholdHistMinutesGlobalID,_P:thresholdHistMinutesIndex,'thresholdHistMinutesUnitCount':thresholdHistMinutesUnitCount,'thresholdHistMinutesTimestamp':thresholdHistMinutesTimestamp,'thresholdHistHoursTable':thresholdHistHoursTable,'thresholdHistHoursEntry':thresholdHistHoursEntry,_Q:thresholdHistHoursGlobalID,_R:thresholdHistHoursIndex,'thresholdHistHoursUnitCount':thresholdHistHoursUnitCount,'thresholdHistHoursTimestamp':thresholdHistHoursTimestamp,'thresholdHistDaysTable':thresholdHistDaysTable,'thresholdHistDaysEntry':thresholdHistDaysEntry,_S:thresholdHistDaysGlobalID,_T:thresholdHistDaysIndex,'thresholdHistDaysUnitCount':thresholdHistDaysUnitCount,'thresholdHistDaysTimestamp':thresholdHistDaysTimestamp,'thresholdTable':thresholdTable,'thresholdEntry':thresholdEntry,_U:thresholdGlobalID,'thresholdState':thresholdState,'thresholdUnits':thresholdUnits,'interfaceHistSecondsTable':interfaceHistSecondsTable,'interfaceHistSecondsEntry':interfaceHistSecondsEntry,_V:interfaceHistSecondsIfIndex,_W:interfaceHistSecondsIndex,'interfaceHistSecondsUnitCountIn':interfaceHistSecondsUnitCountIn,'interfaceHistSecondsUnitCountOut':interfaceHistSecondsUnitCountOut,'interfaceHistSecondsTimestamp':interfaceHistSecondsTimestamp,'interfaceHistMinutesTable':interfaceHistMinutesTable,'interfaceHistMinutesEntry':interfaceHistMinutesEntry,_X:interfaceHistMinutesIfIndex,_Y:interfaceHistMinutesIndex,'interfaceHistMinutesUnitCountIn':interfaceHistMinutesUnitCountIn,'interfaceHistMinutesUnitCountOut':interfaceHistMinutesUnitCountOut,'interfaceHistMinutesTimestamp':interfaceHistMinutesTimestamp,'interfaceHistHoursTable':interfaceHistHoursTable,'interfaceHistHoursEntry':interfaceHistHoursEntry,_Z:interfaceHistHoursIfIndex,_a:interfaceHistHoursIndex,'interfaceHistHoursUnitCountIn':interfaceHistHoursUnitCountIn,'interfaceHistHoursUnitCountOut':interfaceHistHoursUnitCountOut,'interfaceHistHoursTimestamp':interfaceHistHoursTimestamp,'interfaceHistDaysTable':interfaceHistDaysTable,'interfaceHistDaysEntry':interfaceHistDaysEntry,_b:interfaceHistDaysIfIndex,_c:interfaceHistDaysIndex,'interfaceHistDaysUnitCountIn':interfaceHistDaysUnitCountIn,'interfaceHistDaysUnitCountOut':interfaceHistDaysUnitCountOut,'interfaceHistDaysTimestamp':interfaceHistDaysTimestamp,'tptThresholdFilterNotify':tptThresholdFilterNotify,_d:tptThresholdNotifyDeviceID,_e:tptThresholdNotifyPolicyID,_f:tptThresholdNotifySignatureID,'tptThresholdNotifySegmentName':tptThresholdNotifySegmentName,_g:tptThresholdNotifyZonePair})