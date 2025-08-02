_F='ntcMoRfBucConfGrpV1Standard'
_E='ntcMoRfBucCommunication'
_D='ntcMoRfBucHardware'
_C='read-only'
_B='NEWTEC-MORFBUC-MIB'
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
ntcMoRfBlockUpConv=ModuleIdentity((1,3,6,1,4,1,5835,5,2,10000))
if mibBuilder.loadTexts:ntcMoRfBlockUpConv.setRevisions(('2016-05-17 09:00',))
_NtcMoRfBucObjects_ObjectIdentity=ObjectIdentity
ntcMoRfBucObjects=_NtcMoRfBucObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10000,1))
if mibBuilder.loadTexts:ntcMoRfBucObjects.setStatus(_A)
_NtcMoRfBucAlarm_ObjectIdentity=ObjectIdentity
ntcMoRfBucAlarm=_NtcMoRfBucAlarm_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10000,1,1))
if mibBuilder.loadTexts:ntcMoRfBucAlarm.setStatus(_A)
_NtcMoRfBucHardware_Type=NtcAlarmState
_NtcMoRfBucHardware_Object=MibScalar
ntcMoRfBucHardware=_NtcMoRfBucHardware_Object((1,3,6,1,4,1,5835,5,2,10000,1,1,1),_NtcMoRfBucHardware_Type())
ntcMoRfBucHardware.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMoRfBucHardware.setStatus(_A)
_NtcMoRfBucCommunication_Type=NtcAlarmState
_NtcMoRfBucCommunication_Object=MibScalar
ntcMoRfBucCommunication=_NtcMoRfBucCommunication_Object((1,3,6,1,4,1,5835,5,2,10000,1,1,2),_NtcMoRfBucCommunication_Type())
ntcMoRfBucCommunication.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcMoRfBucCommunication.setStatus(_A)
_NtcMoRfBucConformance_ObjectIdentity=ObjectIdentity
ntcMoRfBucConformance=_NtcMoRfBucConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10000,2))
if mibBuilder.loadTexts:ntcMoRfBucConformance.setStatus(_A)
_NtcMoRfBucConfCompliance_ObjectIdentity=ObjectIdentity
ntcMoRfBucConfCompliance=_NtcMoRfBucConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10000,2,1))
if mibBuilder.loadTexts:ntcMoRfBucConfCompliance.setStatus(_A)
_NtcMoRfBucConfGroup_ObjectIdentity=ObjectIdentity
ntcMoRfBucConfGroup=_NtcMoRfBucConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10000,2,2))
if mibBuilder.loadTexts:ntcMoRfBucConfGroup.setStatus(_A)
ntcMoRfBucConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,10000,2,2,1))
ntcMoRfBucConfGrpV1Standard.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:ntcMoRfBucConfGrpV1Standard.setStatus(_A)
ntcMoRfBucConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,10000,2,1,1))
ntcMoRfBucConfCompV1Standard.setObjects((_B,_F))
if mibBuilder.loadTexts:ntcMoRfBucConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcMoRfBlockUpConv':ntcMoRfBlockUpConv,'ntcMoRfBucObjects':ntcMoRfBucObjects,'ntcMoRfBucAlarm':ntcMoRfBucAlarm,_D:ntcMoRfBucHardware,_E:ntcMoRfBucCommunication,'ntcMoRfBucConformance':ntcMoRfBucConformance,'ntcMoRfBucConfCompliance':ntcMoRfBucConfCompliance,'ntcMoRfBucConfCompV1Standard':ntcMoRfBucConfCompV1Standard,'ntcMoRfBucConfGroup':ntcMoRfBucConfGroup,_F:ntcMoRfBucConfGrpV1Standard})