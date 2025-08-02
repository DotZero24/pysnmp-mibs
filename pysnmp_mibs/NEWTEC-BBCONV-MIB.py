_G='ntcBbcConfGrpV1Standard'
_F='ntcBbcConfSelection'
_E='ntcBbcConfEnable'
_D='read-write'
_C='Integer32'
_B='NEWTEC-BBCONV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcBBandConverter=ModuleIdentity((1,3,6,1,4,1,5835,5,2,10500))
if mibBuilder.loadTexts:ntcBBandConverter.setRevisions(('2017-07-10 12:00',))
_NtcBbcObjects_ObjectIdentity=ObjectIdentity
ntcBbcObjects=_NtcBbcObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10500,1))
if mibBuilder.loadTexts:ntcBbcObjects.setStatus(_A)
_NtcBbcConf_ObjectIdentity=ObjectIdentity
ntcBbcConf=_NtcBbcConf_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10500,1,1))
if mibBuilder.loadTexts:ntcBbcConf.setStatus(_A)
class _NtcBbcConfEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('off',0),('on',1)))
_NtcBbcConfEnable_Type.__name__=_C
_NtcBbcConfEnable_Object=MibScalar
ntcBbcConfEnable=_NtcBbcConfEnable_Object((1,3,6,1,4,1,5835,5,2,10500,1,1,1),_NtcBbcConfEnable_Type())
ntcBbcConfEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbcConfEnable.setStatus(_A)
class _NtcBbcConfSelection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('abandRHCP99W',0),('abandLHCP99W',1),('bbandRHCP99W',2),('bbandLHCP99W',3),('abandRHCP103W',4),('abandLHCP103W',5),('bbandRHCP103W',6),('bbandLHCP103W',7)))
_NtcBbcConfSelection_Type.__name__=_C
_NtcBbcConfSelection_Object=MibScalar
ntcBbcConfSelection=_NtcBbcConfSelection_Object((1,3,6,1,4,1,5835,5,2,10500,1,1,2),_NtcBbcConfSelection_Type())
ntcBbcConfSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbcConfSelection.setStatus(_A)
_NtcBbcConformance_ObjectIdentity=ObjectIdentity
ntcBbcConformance=_NtcBbcConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10500,2))
if mibBuilder.loadTexts:ntcBbcConformance.setStatus(_A)
_NtcBbcConfCompliance_ObjectIdentity=ObjectIdentity
ntcBbcConfCompliance=_NtcBbcConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10500,2,1))
if mibBuilder.loadTexts:ntcBbcConfCompliance.setStatus(_A)
_NtcBbcConfGroup_ObjectIdentity=ObjectIdentity
ntcBbcConfGroup=_NtcBbcConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,10500,2,2))
if mibBuilder.loadTexts:ntcBbcConfGroup.setStatus(_A)
ntcBbcConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,10500,2,2,1))
ntcBbcConfGrpV1Standard.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:ntcBbcConfGrpV1Standard.setStatus(_A)
ntcBbcConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,10500,2,1,1))
ntcBbcConfCompV1Standard.setObjects((_B,_G))
if mibBuilder.loadTexts:ntcBbcConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcBBandConverter':ntcBBandConverter,'ntcBbcObjects':ntcBbcObjects,'ntcBbcConf':ntcBbcConf,_E:ntcBbcConfEnable,_F:ntcBbcConfSelection,'ntcBbcConformance':ntcBbcConformance,'ntcBbcConfCompliance':ntcBbcConfCompliance,'ntcBbcConfCompV1Standard':ntcBbcConfCompV1Standard,'ntcBbcConfGroup':ntcBbcConfGroup,_G:ntcBbcConfGrpV1Standard})