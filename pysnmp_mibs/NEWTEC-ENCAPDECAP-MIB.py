_E='ntcEncapDecapConfGrpV1Standard'
_D='ntcEncapDecapForwardingMode'
_C='Integer32'
_B='NEWTEC-ENCAPDECAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcEncapDecap=ModuleIdentity((1,3,6,1,4,1,5835,5,2,2220))
if mibBuilder.loadTexts:ntcEncapDecap.setRevisions(('2014-02-03 12:00',))
_NtcEncapDecapObjects_ObjectIdentity=ObjectIdentity
ntcEncapDecapObjects=_NtcEncapDecapObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2220,1))
if mibBuilder.loadTexts:ntcEncapDecapObjects.setStatus(_A)
class _NtcEncapDecapForwardingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('l2',0),('l3',1)))
_NtcEncapDecapForwardingMode_Type.__name__=_C
_NtcEncapDecapForwardingMode_Object=MibScalar
ntcEncapDecapForwardingMode=_NtcEncapDecapForwardingMode_Object((1,3,6,1,4,1,5835,5,2,2220,1,1),_NtcEncapDecapForwardingMode_Type())
ntcEncapDecapForwardingMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:ntcEncapDecapForwardingMode.setStatus(_A)
_NtcEncapDecapConformance_ObjectIdentity=ObjectIdentity
ntcEncapDecapConformance=_NtcEncapDecapConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2220,2))
if mibBuilder.loadTexts:ntcEncapDecapConformance.setStatus(_A)
_NtcEncapDecapConfCompliance_ObjectIdentity=ObjectIdentity
ntcEncapDecapConfCompliance=_NtcEncapDecapConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2220,2,1))
if mibBuilder.loadTexts:ntcEncapDecapConfCompliance.setStatus(_A)
_NtcEncapDecapConfGroup_ObjectIdentity=ObjectIdentity
ntcEncapDecapConfGroup=_NtcEncapDecapConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,2220,2,2))
if mibBuilder.loadTexts:ntcEncapDecapConfGroup.setStatus(_A)
ntcEncapDecapConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,2220,2,2,1))
ntcEncapDecapConfGrpV1Standard.setObjects((_B,_D))
if mibBuilder.loadTexts:ntcEncapDecapConfGrpV1Standard.setStatus(_A)
ntcEncapDecapConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,2220,2,1,1))
ntcEncapDecapConfCompV1Standard.setObjects((_B,_E))
if mibBuilder.loadTexts:ntcEncapDecapConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcEncapDecap':ntcEncapDecap,'ntcEncapDecapObjects':ntcEncapDecapObjects,_D:ntcEncapDecapForwardingMode,'ntcEncapDecapConformance':ntcEncapDecapConformance,'ntcEncapDecapConfCompliance':ntcEncapDecapConfCompliance,'ntcEncapDecapConfCompV1Standard':ntcEncapDecapConfCompV1Standard,'ntcEncapDecapConfGroup':ntcEncapDecapConfGroup,_E:ntcEncapDecapConfGrpV1Standard})