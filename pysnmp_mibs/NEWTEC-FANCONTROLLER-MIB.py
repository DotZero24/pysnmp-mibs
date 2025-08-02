_D='ntcFanCConfGrpV1Standard'
_C='ntcFanCAlmFanFailure'
_B='NEWTEC-FANCONTROLLER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcFanController=ModuleIdentity((1,3,6,1,4,1,5835,5,2,3500))
if mibBuilder.loadTexts:ntcFanController.setRevisions(('2013-07-05 06:00',))
_NtcFanCObjects_ObjectIdentity=ObjectIdentity
ntcFanCObjects=_NtcFanCObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3500,1))
if mibBuilder.loadTexts:ntcFanCObjects.setStatus(_A)
_NtcFanAlarm_ObjectIdentity=ObjectIdentity
ntcFanAlarm=_NtcFanAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3500,1,1))
if mibBuilder.loadTexts:ntcFanAlarm.setStatus(_A)
_NtcFanCAlmFanFailure_Type=NtcAlarmState
_NtcFanCAlmFanFailure_Object=MibScalar
ntcFanCAlmFanFailure=_NtcFanCAlmFanFailure_Object((1,3,6,1,4,1,5835,5,2,3500,1,1,1),_NtcFanCAlmFanFailure_Type())
ntcFanCAlmFanFailure.setMaxAccess('read-only')
if mibBuilder.loadTexts:ntcFanCAlmFanFailure.setStatus(_A)
_NtcFanCConformance_ObjectIdentity=ObjectIdentity
ntcFanCConformance=_NtcFanCConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3500,2))
if mibBuilder.loadTexts:ntcFanCConformance.setStatus(_A)
_NtcFanCConfCompliance_ObjectIdentity=ObjectIdentity
ntcFanCConfCompliance=_NtcFanCConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3500,2,1))
if mibBuilder.loadTexts:ntcFanCConfCompliance.setStatus(_A)
_NtcFanCConfGroup_ObjectIdentity=ObjectIdentity
ntcFanCConfGroup=_NtcFanCConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3500,2,2))
if mibBuilder.loadTexts:ntcFanCConfGroup.setStatus(_A)
ntcFanCConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,3500,2,2,1))
ntcFanCConfGrpV1Standard.setObjects((_B,_C))
if mibBuilder.loadTexts:ntcFanCConfGrpV1Standard.setStatus(_A)
ntcFanCConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,3500,2,1,1))
ntcFanCConfCompV1Standard.setObjects((_B,_D))
if mibBuilder.loadTexts:ntcFanCConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcFanController':ntcFanController,'ntcFanCObjects':ntcFanCObjects,'ntcFanAlarm':ntcFanAlarm,_C:ntcFanCAlmFanFailure,'ntcFanCConformance':ntcFanCConformance,'ntcFanCConfCompliance':ntcFanCConfCompliance,'ntcFanCConfCompV1Standard':ntcFanCConfCompV1Standard,'ntcFanCConfGroup':ntcFanCConfGroup,_D:ntcFanCConfGrpV1Standard})