_F='ntcDualPSConfGrpV1Standard'
_E='ntcDualPSAlmPowerSupplyBFailure'
_D='ntcDualPSAlmPowerSupplyAFailure'
_C='read-only'
_B='NEWTEC-DUALPOWERSUPPLY-MIB'
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
ntcDualPowerSupply=ModuleIdentity((1,3,6,1,4,1,5835,5,2,3000))
if mibBuilder.loadTexts:ntcDualPowerSupply.setRevisions(('2012-11-13 12:00',))
_NtcDualPSObjects_ObjectIdentity=ObjectIdentity
ntcDualPSObjects=_NtcDualPSObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3000,1))
if mibBuilder.loadTexts:ntcDualPSObjects.setStatus(_A)
_NtcDualPSAlarm_ObjectIdentity=ObjectIdentity
ntcDualPSAlarm=_NtcDualPSAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3000,1,1))
if mibBuilder.loadTexts:ntcDualPSAlarm.setStatus(_A)
_NtcDualPSAlmPowerSupplyAFailure_Type=NtcAlarmState
_NtcDualPSAlmPowerSupplyAFailure_Object=MibScalar
ntcDualPSAlmPowerSupplyAFailure=_NtcDualPSAlmPowerSupplyAFailure_Object((1,3,6,1,4,1,5835,5,2,3000,1,1,1),_NtcDualPSAlmPowerSupplyAFailure_Type())
ntcDualPSAlmPowerSupplyAFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDualPSAlmPowerSupplyAFailure.setStatus(_A)
_NtcDualPSAlmPowerSupplyBFailure_Type=NtcAlarmState
_NtcDualPSAlmPowerSupplyBFailure_Object=MibScalar
ntcDualPSAlmPowerSupplyBFailure=_NtcDualPSAlmPowerSupplyBFailure_Object((1,3,6,1,4,1,5835,5,2,3000,1,1,2),_NtcDualPSAlmPowerSupplyBFailure_Type())
ntcDualPSAlmPowerSupplyBFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcDualPSAlmPowerSupplyBFailure.setStatus(_A)
_NtcDualPSConformance_ObjectIdentity=ObjectIdentity
ntcDualPSConformance=_NtcDualPSConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3000,2))
if mibBuilder.loadTexts:ntcDualPSConformance.setStatus(_A)
_NtcDualPSConfCompliance_ObjectIdentity=ObjectIdentity
ntcDualPSConfCompliance=_NtcDualPSConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3000,2,1))
if mibBuilder.loadTexts:ntcDualPSConfCompliance.setStatus(_A)
_NtcDualPSConfGroup_ObjectIdentity=ObjectIdentity
ntcDualPSConfGroup=_NtcDualPSConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,3000,2,2))
if mibBuilder.loadTexts:ntcDualPSConfGroup.setStatus(_A)
ntcDualPSConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,3000,2,2,1))
ntcDualPSConfGrpV1Standard.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:ntcDualPSConfGrpV1Standard.setStatus(_A)
ntcDualPSConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,3000,2,1,1))
ntcDualPSConfCompV1Standard.setObjects((_B,_F))
if mibBuilder.loadTexts:ntcDualPSConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcDualPowerSupply':ntcDualPowerSupply,'ntcDualPSObjects':ntcDualPSObjects,'ntcDualPSAlarm':ntcDualPSAlarm,_D:ntcDualPSAlmPowerSupplyAFailure,_E:ntcDualPSAlmPowerSupplyBFailure,'ntcDualPSConformance':ntcDualPSConformance,'ntcDualPSConfCompliance':ntcDualPSConfCompliance,'ntcDualPSConfCompV1Standard':ntcDualPSConfCompV1Standard,'ntcDualPSConfGroup':ntcDualPSConfGroup,_F:ntcDualPSConfGrpV1Standard})