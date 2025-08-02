_E='ntcTermConfGrpV1Standard'
_D='ntcTermId'
_C='Unsigned32'
_B='NEWTEC-TERMINAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcTerminal=ModuleIdentity((1,3,6,1,4,1,5835,5,2,2900))
if mibBuilder.loadTexts:ntcTerminal.setRevisions(('2013-01-08 12:00',))
_NtcTermObjects_ObjectIdentity=ObjectIdentity
ntcTermObjects=_NtcTermObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2900,1))
if mibBuilder.loadTexts:ntcTermObjects.setStatus(_A)
class _NtcTermId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65277))
_NtcTermId_Type.__name__=_C
_NtcTermId_Object=MibScalar
ntcTermId=_NtcTermId_Object((1,3,6,1,4,1,5835,5,2,2900,1,1),_NtcTermId_Type())
ntcTermId.setMaxAccess('read-write')
if mibBuilder.loadTexts:ntcTermId.setStatus(_A)
_NtcTermConformance_ObjectIdentity=ObjectIdentity
ntcTermConformance=_NtcTermConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2900,2))
if mibBuilder.loadTexts:ntcTermConformance.setStatus(_A)
_NtcTermConfCompliance_ObjectIdentity=ObjectIdentity
ntcTermConfCompliance=_NtcTermConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2900,2,1))
if mibBuilder.loadTexts:ntcTermConfCompliance.setStatus(_A)
_NtcTermConfGroup_ObjectIdentity=ObjectIdentity
ntcTermConfGroup=_NtcTermConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2900,2,2))
if mibBuilder.loadTexts:ntcTermConfGroup.setStatus(_A)
ntcTermConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,2900,2,2,1))
ntcTermConfGrpV1Standard.setObjects((_B,_D))
if mibBuilder.loadTexts:ntcTermConfGrpV1Standard.setStatus(_A)
ntcTermConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,2900,2,1,1))
ntcTermConfCompV1Standard.setObjects((_B,_E))
if mibBuilder.loadTexts:ntcTermConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcTerminal':ntcTerminal,'ntcTermObjects':ntcTermObjects,_D:ntcTermId,'ntcTermConformance':ntcTermConformance,'ntcTermConfCompliance':ntcTermConfCompliance,'ntcTermConfCompV1Standard':ntcTermConfCompV1Standard,'ntcTermConfGroup':ntcTermConfGroup,_E:ntcTermConfGrpV1Standard})