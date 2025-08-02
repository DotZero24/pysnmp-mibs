_M='ntcRefClkConfGrpV1Standard'
_L='ntcRefClkActiveRef'
_K='ntcRefClkAlmRefClockNoLock'
_J='ntcRefClkAlmRefClockNoSignal'
_I='ntcRefClkExtRefFrequency'
_H='ntcRefClkRefSelection'
_G='read-write'
_F='external'
_E='internal'
_D='read-only'
_C='Integer32'
_B='NEWTEC-REFERENCECLOCK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcReferenceClock=ModuleIdentity((1,3,6,1,4,1,5835,5,2,300))
if mibBuilder.loadTexts:ntcReferenceClock.setRevisions(('2013-09-20 08:00','2012-06-28 12:00'))
_NtcRefClkObjects_ObjectIdentity=ObjectIdentity
ntcRefClkObjects=_NtcRefClkObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,300,1))
if mibBuilder.loadTexts:ntcRefClkObjects.setStatus(_A)
class _NtcRefClkRefSelection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NtcRefClkRefSelection_Type.__name__=_C
_NtcRefClkRefSelection_Object=MibScalar
ntcRefClkRefSelection=_NtcRefClkRefSelection_Object((1,3,6,1,4,1,5835,5,2,300,1,1),_NtcRefClkRefSelection_Type())
ntcRefClkRefSelection.setMaxAccess(_G)
if mibBuilder.loadTexts:ntcRefClkRefSelection.setStatus(_A)
class _NtcRefClkExtRefFrequency_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,3,4,5)));namedValues=NamedValues(*(('e1Mhz',0),('e2Mhz',1),('e5Mhz',3),('e10Mhz',4),('e20Mhz',5)))
_NtcRefClkExtRefFrequency_Type.__name__=_C
_NtcRefClkExtRefFrequency_Object=MibScalar
ntcRefClkExtRefFrequency=_NtcRefClkExtRefFrequency_Object((1,3,6,1,4,1,5835,5,2,300,1,2),_NtcRefClkExtRefFrequency_Type())
ntcRefClkExtRefFrequency.setMaxAccess(_G)
if mibBuilder.loadTexts:ntcRefClkExtRefFrequency.setStatus(_A)
_NtcRefClkAlarm_ObjectIdentity=ObjectIdentity
ntcRefClkAlarm=_NtcRefClkAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,300,1,3))
if mibBuilder.loadTexts:ntcRefClkAlarm.setStatus(_A)
_NtcRefClkAlmRefClockNoSignal_Type=NtcAlarmState
_NtcRefClkAlmRefClockNoSignal_Object=MibScalar
ntcRefClkAlmRefClockNoSignal=_NtcRefClkAlmRefClockNoSignal_Object((1,3,6,1,4,1,5835,5,2,300,1,3,1),_NtcRefClkAlmRefClockNoSignal_Type())
ntcRefClkAlmRefClockNoSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcRefClkAlmRefClockNoSignal.setStatus(_A)
_NtcRefClkAlmRefClockNoLock_Type=NtcAlarmState
_NtcRefClkAlmRefClockNoLock_Object=MibScalar
ntcRefClkAlmRefClockNoLock=_NtcRefClkAlmRefClockNoLock_Object((1,3,6,1,4,1,5835,5,2,300,1,3,2),_NtcRefClkAlmRefClockNoLock_Type())
ntcRefClkAlmRefClockNoLock.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcRefClkAlmRefClockNoLock.setStatus(_A)
class _NtcRefClkActiveRef_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_NtcRefClkActiveRef_Type.__name__=_C
_NtcRefClkActiveRef_Object=MibScalar
ntcRefClkActiveRef=_NtcRefClkActiveRef_Object((1,3,6,1,4,1,5835,5,2,300,1,4),_NtcRefClkActiveRef_Type())
ntcRefClkActiveRef.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcRefClkActiveRef.setStatus(_A)
_NtcRefClkConformance_ObjectIdentity=ObjectIdentity
ntcRefClkConformance=_NtcRefClkConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,300,2))
if mibBuilder.loadTexts:ntcRefClkConformance.setStatus(_A)
_NtcRefClkConfCompliance_ObjectIdentity=ObjectIdentity
ntcRefClkConfCompliance=_NtcRefClkConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,300,2,1))
if mibBuilder.loadTexts:ntcRefClkConfCompliance.setStatus(_A)
_NtcRefClkConfGroup_ObjectIdentity=ObjectIdentity
ntcRefClkConfGroup=_NtcRefClkConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,300,2,2))
if mibBuilder.loadTexts:ntcRefClkConfGroup.setStatus(_A)
ntcRefClkConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,300,2,2,1))
ntcRefClkConfGrpV1Standard.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:ntcRefClkConfGrpV1Standard.setStatus(_A)
ntcRefClkConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,300,2,1,1))
ntcRefClkConfCompV1Standard.setObjects((_B,_M))
if mibBuilder.loadTexts:ntcRefClkConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcReferenceClock':ntcReferenceClock,'ntcRefClkObjects':ntcRefClkObjects,_H:ntcRefClkRefSelection,_I:ntcRefClkExtRefFrequency,'ntcRefClkAlarm':ntcRefClkAlarm,_J:ntcRefClkAlmRefClockNoSignal,_K:ntcRefClkAlmRefClockNoLock,_L:ntcRefClkActiveRef,'ntcRefClkConformance':ntcRefClkConformance,'ntcRefClkConfCompliance':ntcRefClkConfCompliance,'ntcRefClkConfCompV1Standard':ntcRefClkConfCompV1Standard,'ntcRefClkConfGroup':ntcRefClkConfGroup,_M:ntcRefClkConfGrpV1Standard})