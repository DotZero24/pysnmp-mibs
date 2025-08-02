_L='pdnDs1ExtE1ConfigGroup'
_K='pdnDs1ExtT1ConfigGroup'
_J='pdnDs1ExtConfConnector'
_I='pdnDs1ExtConfLineBuildOut'
_H='pdnDs1ExtConfLineLength'
_G='ifIndex'
_F='IF-MIB'
_E='pdnDs1ExtConfLineLengthType'
_D='read-write'
_C='Integer32'
_B='PDN-DS1EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ent_ds1,=mibBuilder.importSymbols('PDN-HEADER-MIB','ent-ds1')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnDs1Ext=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,5,5))
_PdnDs1ExtObjects_ObjectIdentity=ObjectIdentity
pdnDs1ExtObjects=_PdnDs1ExtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,5,5,1))
_PdnDs1ExtConfTable_Object=MibTable
pdnDs1ExtConfTable=_PdnDs1ExtConfTable_Object((1,3,6,1,4,1,1795,2,24,2,6,5,5,1,1))
if mibBuilder.loadTexts:pdnDs1ExtConfTable.setStatus(_A)
_PdnDs1ExtConfEntry_Object=MibTableRow
pdnDs1ExtConfEntry=_PdnDs1ExtConfEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,5,5,1,1,1))
pdnDs1ExtConfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pdnDs1ExtConfEntry.setStatus(_A)
class _PdnDs1ExtConfLineLengthType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('shortHaul',1),('longHaul',2)))
_PdnDs1ExtConfLineLengthType_Type.__name__=_C
_PdnDs1ExtConfLineLengthType_Object=MibTableColumn
pdnDs1ExtConfLineLengthType=_PdnDs1ExtConfLineLengthType_Object((1,3,6,1,4,1,1795,2,24,2,6,5,5,1,1,1,1),_PdnDs1ExtConfLineLengthType_Type())
pdnDs1ExtConfLineLengthType.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDs1ExtConfLineLengthType.setStatus(_A)
class _PdnDs1ExtConfLineLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('feet000To133',1),('feet134To266',2),('feet267To399',3),('feet400To533',4),('feet534To655',5)))
_PdnDs1ExtConfLineLength_Type.__name__=_C
_PdnDs1ExtConfLineLength_Object=MibTableColumn
pdnDs1ExtConfLineLength=_PdnDs1ExtConfLineLength_Object((1,3,6,1,4,1,1795,2,24,2,6,5,5,1,1,1,2),_PdnDs1ExtConfLineLength_Type())
pdnDs1ExtConfLineLength.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDs1ExtConfLineLength.setStatus(_A)
class _PdnDs1ExtConfLineBuildOut_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dB0Pnt0',1),('dB7Pnt5',2),('dB15Pnt0',3),('dB22Pnt5',4)))
_PdnDs1ExtConfLineBuildOut_Type.__name__=_C
_PdnDs1ExtConfLineBuildOut_Object=MibTableColumn
pdnDs1ExtConfLineBuildOut=_PdnDs1ExtConfLineBuildOut_Object((1,3,6,1,4,1,1795,2,24,2,6,5,5,1,1,1,3),_PdnDs1ExtConfLineBuildOut_Type())
pdnDs1ExtConfLineBuildOut.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDs1ExtConfLineBuildOut.setStatus(_A)
class _PdnDs1ExtConfConnector_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bnc',1),('rj48',2)))
_PdnDs1ExtConfConnector_Type.__name__=_C
_PdnDs1ExtConfConnector_Object=MibTableColumn
pdnDs1ExtConfConnector=_PdnDs1ExtConfConnector_Object((1,3,6,1,4,1,1795,2,24,2,6,5,5,1,1,1,4),_PdnDs1ExtConfConnector_Type())
pdnDs1ExtConfConnector.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnDs1ExtConfConnector.setStatus(_A)
_PdnDs1ExtConformance_ObjectIdentity=ObjectIdentity
pdnDs1ExtConformance=_PdnDs1ExtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,5,5,2))
_PdnDs1ExtGroups_ObjectIdentity=ObjectIdentity
pdnDs1ExtGroups=_PdnDs1ExtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,5,5,2,1))
_PdnDs1ExtCompliances_ObjectIdentity=ObjectIdentity
pdnDs1ExtCompliances=_PdnDs1ExtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,5,5,2,2))
pdnDs1ExtT1ConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,5,5,2,1,1))
pdnDs1ExtT1ConfigGroup.setObjects(*((_B,_E),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:pdnDs1ExtT1ConfigGroup.setStatus(_A)
pdnDs1ExtE1ConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,5,5,2,1,2))
pdnDs1ExtE1ConfigGroup.setObjects(*((_B,_E),(_B,_J)))
if mibBuilder.loadTexts:pdnDs1ExtE1ConfigGroup.setStatus(_A)
pdnDs1ExtCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,5,5,2,2,1))
pdnDs1ExtCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:pdnDs1ExtCompliance.setStatus(_A)
pdnDs1ExtG703Compliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,5,5,2,2,2))
pdnDs1ExtG703Compliance.setObjects((_B,_L))
if mibBuilder.loadTexts:pdnDs1ExtG703Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnDs1Ext':pdnDs1Ext,'pdnDs1ExtObjects':pdnDs1ExtObjects,'pdnDs1ExtConfTable':pdnDs1ExtConfTable,'pdnDs1ExtConfEntry':pdnDs1ExtConfEntry,_E:pdnDs1ExtConfLineLengthType,_H:pdnDs1ExtConfLineLength,_I:pdnDs1ExtConfLineBuildOut,_J:pdnDs1ExtConfConnector,'pdnDs1ExtConformance':pdnDs1ExtConformance,'pdnDs1ExtGroups':pdnDs1ExtGroups,_K:pdnDs1ExtT1ConfigGroup,_L:pdnDs1ExtE1ConfigGroup,'pdnDs1ExtCompliances':pdnDs1ExtCompliances,'pdnDs1ExtCompliance':pdnDs1ExtCompliance,'pdnDs1ExtG703Compliance':pdnDs1ExtG703Compliance})