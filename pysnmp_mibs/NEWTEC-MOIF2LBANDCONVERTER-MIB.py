_F='ntcMoIF2LConvConfGrpV1Standard'
_E='ntcMoIF2LConvCommunication'
_D='ntcMoIF2LConvHardware'
_C='read-only'
_B='NEWTEC-MOIF2LBANDCONVERTER-MIB'
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
ntcMoIF2LbandConverter=ModuleIdentity((1,3,6,1,4,1,5835,5,2,8600))
if mibBuilder.loadTexts:ntcMoIF2LbandConverter.setRevisions(('2015-02-19 09:00',))
_NtcMoIF2LConvObjects_ObjectIdentity=ObjectIdentity
ntcMoIF2LConvObjects=_NtcMoIF2LConvObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8600,1))
if mibBuilder.loadTexts:ntcMoIF2LConvObjects.setStatus(_A)
_NtcMoIF2LConvAlarm_ObjectIdentity=ObjectIdentity
ntcMoIF2LConvAlarm=_NtcMoIF2LConvAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8600,1,1))
if mibBuilder.loadTexts:ntcMoIF2LConvAlarm.setStatus(_A)
_NtcMoIF2LConvHardware_Type=NtcAlarmState
_NtcMoIF2LConvHardware_Object=MibScalar
ntcMoIF2LConvHardware=_NtcMoIF2LConvHardware_Object((1,3,6,1,4,1,5835,5,2,8600,1,1,1),_NtcMoIF2LConvHardware_Type())
ntcMoIF2LConvHardware.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMoIF2LConvHardware.setStatus(_A)
_NtcMoIF2LConvCommunication_Type=NtcAlarmState
_NtcMoIF2LConvCommunication_Object=MibScalar
ntcMoIF2LConvCommunication=_NtcMoIF2LConvCommunication_Object((1,3,6,1,4,1,5835,5,2,8600,1,1,2),_NtcMoIF2LConvCommunication_Type())
ntcMoIF2LConvCommunication.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMoIF2LConvCommunication.setStatus(_A)
_NtcMoIF2LConvConformance_ObjectIdentity=ObjectIdentity
ntcMoIF2LConvConformance=_NtcMoIF2LConvConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8600,2))
if mibBuilder.loadTexts:ntcMoIF2LConvConformance.setStatus(_A)
_NtcMoIF2LConvConfCompliance_ObjectIdentity=ObjectIdentity
ntcMoIF2LConvConfCompliance=_NtcMoIF2LConvConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8600,2,1))
if mibBuilder.loadTexts:ntcMoIF2LConvConfCompliance.setStatus(_A)
_NtcMoIF2LConvConfGroup_ObjectIdentity=ObjectIdentity
ntcMoIF2LConvConfGroup=_NtcMoIF2LConvConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,8600,2,2))
if mibBuilder.loadTexts:ntcMoIF2LConvConfGroup.setStatus(_A)
ntcMoIF2LConvConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,8600,2,2,1))
ntcMoIF2LConvConfGrpV1Standard.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:ntcMoIF2LConvConfGrpV1Standard.setStatus(_A)
ntcMoIF2LConvConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,8600,2,1,1))
ntcMoIF2LConvConfCompV1Standard.setObjects((_B,_F))
if mibBuilder.loadTexts:ntcMoIF2LConvConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcMoIF2LbandConverter':ntcMoIF2LbandConverter,'ntcMoIF2LConvObjects':ntcMoIF2LConvObjects,'ntcMoIF2LConvAlarm':ntcMoIF2LConvAlarm,_D:ntcMoIF2LConvHardware,_E:ntcMoIF2LConvCommunication,'ntcMoIF2LConvConformance':ntcMoIF2LConvConformance,'ntcMoIF2LConvConfCompliance':ntcMoIF2LConvConfCompliance,'ntcMoIF2LConvConfCompV1Standard':ntcMoIF2LConvConfCompV1Standard,'ntcMoIF2LConvConfGroup':ntcMoIF2LConvConfGroup,_F:ntcMoIF2LConvConfGrpV1Standard})