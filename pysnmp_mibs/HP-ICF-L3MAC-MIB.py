_F='hpicfL3MacConfigIfAdvTimer'
_E='hpicfL3MacConfigIfEntry'
_D='Integer32'
_C='hpicfL3MacConfigGroup'
_B='HP-ICF-L3MAC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifRcvAddressEntry,=mibBuilder.importSymbols('IF-MIB','ifRcvAddressEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpicfL3MacConfigMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,36))
if mibBuilder.loadTexts:hpicfL3MacConfigMIB.setRevisions(('2008-10-01 00:00','2006-08-08 16:00'))
_HpicfL3MacConfigObjects_ObjectIdentity=ObjectIdentity
hpicfL3MacConfigObjects=_HpicfL3MacConfigObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,36,1))
_HpicfL3MacConfigIfTable_Object=MibTable
hpicfL3MacConfigIfTable=_HpicfL3MacConfigIfTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,36,1,1))
if mibBuilder.loadTexts:hpicfL3MacConfigIfTable.setStatus(_A)
_HpicfL3MacConfigIfEntry_Object=MibTableRow
hpicfL3MacConfigIfEntry=_HpicfL3MacConfigIfEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,36,1,1,1))
if mibBuilder.loadTexts:hpicfL3MacConfigIfEntry.setStatus(_A)
class _HpicfL3MacConfigIfAdvTimer_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpicfL3MacConfigIfAdvTimer_Type.__name__=_D
_HpicfL3MacConfigIfAdvTimer_Object=MibTableColumn
hpicfL3MacConfigIfAdvTimer=_HpicfL3MacConfigIfAdvTimer_Object((1,3,6,1,4,1,11,2,14,11,5,1,36,1,1,1,1),_HpicfL3MacConfigIfAdvTimer_Type())
hpicfL3MacConfigIfAdvTimer.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpicfL3MacConfigIfAdvTimer.setStatus(_A)
_HpicfL3MacConfigConformance_ObjectIdentity=ObjectIdentity
hpicfL3MacConfigConformance=_HpicfL3MacConfigConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,36,2))
_HpicfL3MacConfigMIBCompliances_ObjectIdentity=ObjectIdentity
hpicfL3MacConfigMIBCompliances=_HpicfL3MacConfigMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,36,2,1))
_HpicfL3MacConfigMIBGroups_ObjectIdentity=ObjectIdentity
hpicfL3MacConfigMIBGroups=_HpicfL3MacConfigMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,36,2,2))
ifRcvAddressEntry.registerAugmentions((_B,_E))
hpicfL3MacConfigIfEntry.setIndexNames(*ifRcvAddressEntry.getIndexNames())
hpicfL3MacConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,36,2,2,1))
hpicfL3MacConfigGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:hpicfL3MacConfigGroup.setStatus(_A)
hpicfL3MacConfigMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,36,2,1,1))
hpicfL3MacConfigMIBCompliance.setObjects(*((_B,_C),(_B,_C)))
if mibBuilder.loadTexts:hpicfL3MacConfigMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfL3MacConfigMIB':hpicfL3MacConfigMIB,'hpicfL3MacConfigObjects':hpicfL3MacConfigObjects,'hpicfL3MacConfigIfTable':hpicfL3MacConfigIfTable,_E:hpicfL3MacConfigIfEntry,_F:hpicfL3MacConfigIfAdvTimer,'hpicfL3MacConfigConformance':hpicfL3MacConfigConformance,'hpicfL3MacConfigMIBCompliances':hpicfL3MacConfigMIBCompliances,'hpicfL3MacConfigMIBCompliance':hpicfL3MacConfigMIBCompliance,'hpicfL3MacConfigMIBGroups':hpicfL3MacConfigMIBGroups,_C:hpicfL3MacConfigGroup})