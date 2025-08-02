_E='hpicfDosFilterGroup'
_D='hpicfDosFilterConfig'
_C='Integer32'
_B='HP-ICF-DOS-FILTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfDosFilterMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,60))
if mibBuilder.loadTexts:hpicfDosFilterMib.setRevisions(('2009-04-03 10:00',))
_HpicfDosFilterObjects_ObjectIdentity=ObjectIdentity
hpicfDosFilterObjects=_HpicfDosFilterObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,60,1))
class _HpicfDosFilterConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpicfDosFilterConfig_Type.__name__=_C
_HpicfDosFilterConfig_Object=MibScalar
hpicfDosFilterConfig=_HpicfDosFilterConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,60,1,1),_HpicfDosFilterConfig_Type())
hpicfDosFilterConfig.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfDosFilterConfig.setStatus(_A)
_HpicfDosFilterConformance_ObjectIdentity=ObjectIdentity
hpicfDosFilterConformance=_HpicfDosFilterConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,60,2))
_HpicfDosFilterCompliances_ObjectIdentity=ObjectIdentity
hpicfDosFilterCompliances=_HpicfDosFilterCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,60,2,1))
_HpicfDosFilterGroups_ObjectIdentity=ObjectIdentity
hpicfDosFilterGroups=_HpicfDosFilterGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,60,2,2))
hpicfDosFilterGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,60,2,2,1))
hpicfDosFilterGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:hpicfDosFilterGroup.setStatus(_A)
hpicfDosFilterCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,60,2,1,1))
hpicfDosFilterCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:hpicfDosFilterCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfDosFilterMib':hpicfDosFilterMib,'hpicfDosFilterObjects':hpicfDosFilterObjects,_D:hpicfDosFilterConfig,'hpicfDosFilterConformance':hpicfDosFilterConformance,'hpicfDosFilterCompliances':hpicfDosFilterCompliances,'hpicfDosFilterCompliance':hpicfDosFilterCompliance,'hpicfDosFilterGroups':hpicfDosFilterGroups,_E:hpicfDosFilterGroup})