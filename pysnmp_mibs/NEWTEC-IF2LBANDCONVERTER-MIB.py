_F='ntcIF2LConvConfGrpV1Standard'
_E='ntcIF2LConvCommunication'
_D='ntcIF2LConvHardware'
_C='read-only'
_B='NEWTEC-IF2LBANDCONVERTER-MIB'
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
ntcIF2LbandConverter=ModuleIdentity((1,3,6,1,4,1,5835,5,2,4600))
if mibBuilder.loadTexts:ntcIF2LbandConverter.setRevisions(('2012-06-28 12:00',))
_NtcIF2LConvObjects_ObjectIdentity=ObjectIdentity
ntcIF2LConvObjects=_NtcIF2LConvObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4600,1))
if mibBuilder.loadTexts:ntcIF2LConvObjects.setStatus(_A)
_NtcIF2LConvAlarm_ObjectIdentity=ObjectIdentity
ntcIF2LConvAlarm=_NtcIF2LConvAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4600,1,1))
if mibBuilder.loadTexts:ntcIF2LConvAlarm.setStatus(_A)
_NtcIF2LConvHardware_Type=NtcAlarmState
_NtcIF2LConvHardware_Object=MibScalar
ntcIF2LConvHardware=_NtcIF2LConvHardware_Object((1,3,6,1,4,1,5835,5,2,4600,1,1,1),_NtcIF2LConvHardware_Type())
ntcIF2LConvHardware.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIF2LConvHardware.setStatus(_A)
_NtcIF2LConvCommunication_Type=NtcAlarmState
_NtcIF2LConvCommunication_Object=MibScalar
ntcIF2LConvCommunication=_NtcIF2LConvCommunication_Object((1,3,6,1,4,1,5835,5,2,4600,1,1,2),_NtcIF2LConvCommunication_Type())
ntcIF2LConvCommunication.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcIF2LConvCommunication.setStatus(_A)
_NtcIF2LConvConformance_ObjectIdentity=ObjectIdentity
ntcIF2LConvConformance=_NtcIF2LConvConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4600,2))
if mibBuilder.loadTexts:ntcIF2LConvConformance.setStatus(_A)
_NtcIF2LConvConfCompliance_ObjectIdentity=ObjectIdentity
ntcIF2LConvConfCompliance=_NtcIF2LConvConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4600,2,1))
if mibBuilder.loadTexts:ntcIF2LConvConfCompliance.setStatus(_A)
_NtcIF2LConvConfGroup_ObjectIdentity=ObjectIdentity
ntcIF2LConvConfGroup=_NtcIF2LConvConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4600,2,2))
if mibBuilder.loadTexts:ntcIF2LConvConfGroup.setStatus(_A)
ntcIF2LConvConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,4600,2,2,1))
ntcIF2LConvConfGrpV1Standard.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:ntcIF2LConvConfGrpV1Standard.setStatus(_A)
ntcIF2LConvConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,4600,2,1,1))
ntcIF2LConvConfCompV1Standard.setObjects((_B,_F))
if mibBuilder.loadTexts:ntcIF2LConvConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcIF2LbandConverter':ntcIF2LbandConverter,'ntcIF2LConvObjects':ntcIF2LConvObjects,'ntcIF2LConvAlarm':ntcIF2LConvAlarm,_D:ntcIF2LConvHardware,_E:ntcIF2LConvCommunication,'ntcIF2LConvConformance':ntcIF2LConvConformance,'ntcIF2LConvConfCompliance':ntcIF2LConvConfCompliance,'ntcIF2LConvConfCompV1Standard':ntcIF2LConvConfCompV1Standard,'ntcIF2LConvConfGroup':ntcIF2LConvConfGroup,_F:ntcIF2LConvConfGrpV1Standard})