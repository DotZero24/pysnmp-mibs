_I='arubaWiredLedLocatorTableGroup'
_H='arubaWiredLedLocatorTable'
_G='arubaWiredLedLocatorState'
_F='arubaWiredLedLocatorName'
_E='arubaWiredLedLocatorGroupIndex'
_D='Integer32'
_C='DisplayString'
_B='ARUBAWIRED-LED-LOCATOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arubaWiredChassisMIB,=mibBuilder.importSymbols('ARUBAWIRED-CHASSIS-MIB','arubaWiredChassisMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
arubaWiredLedLocator=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,7))
if mibBuilder.loadTexts:arubaWiredLedLocator.setRevisions(('2023-06-06 00:00',))
_ArubaWiredLedLocatorObjects_ObjectIdentity=ObjectIdentity
arubaWiredLedLocatorObjects=_ArubaWiredLedLocatorObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,7,1))
_ArubaWiredLedLocatorDetails_ObjectIdentity=ObjectIdentity
arubaWiredLedLocatorDetails=_ArubaWiredLedLocatorDetails_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,7,1,1))
_ArubaWiredLedLocatorTable_Object=MibTable
arubaWiredLedLocatorTable=_ArubaWiredLedLocatorTable_Object((1,3,6,1,4,1,47196,4,1,1,3,11,7,1,1,1))
if mibBuilder.loadTexts:arubaWiredLedLocatorTable.setStatus(_A)
_ArubaWiredLedLocatorEntry_Object=MibTableRow
arubaWiredLedLocatorEntry=_ArubaWiredLedLocatorEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,11,7,1,1,1,1))
arubaWiredLedLocatorEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:arubaWiredLedLocatorEntry.setStatus(_A)
class _ArubaWiredLedLocatorGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredLedLocatorGroupIndex_Type.__name__=_D
_ArubaWiredLedLocatorGroupIndex_Object=MibTableColumn
arubaWiredLedLocatorGroupIndex=_ArubaWiredLedLocatorGroupIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,7,1,1,1,1,1),_ArubaWiredLedLocatorGroupIndex_Type())
arubaWiredLedLocatorGroupIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:arubaWiredLedLocatorGroupIndex.setStatus(_A)
class _ArubaWiredLedLocatorName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ArubaWiredLedLocatorName_Type.__name__=_C
_ArubaWiredLedLocatorName_Object=MibTableColumn
arubaWiredLedLocatorName=_ArubaWiredLedLocatorName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,7,1,1,1,1,2),_ArubaWiredLedLocatorName_Type())
arubaWiredLedLocatorName.setMaxAccess('read-only')
if mibBuilder.loadTexts:arubaWiredLedLocatorName.setStatus(_A)
class _ArubaWiredLedLocatorState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredLedLocatorState_Type.__name__=_C
_ArubaWiredLedLocatorState_Object=MibTableColumn
arubaWiredLedLocatorState=_ArubaWiredLedLocatorState_Object((1,3,6,1,4,1,47196,4,1,1,3,11,7,1,1,1,1,3),_ArubaWiredLedLocatorState_Type())
arubaWiredLedLocatorState.setMaxAccess('read-write')
if mibBuilder.loadTexts:arubaWiredLedLocatorState.setStatus(_A)
_ArubaWiredLedLocatorConformance_ObjectIdentity=ObjectIdentity
arubaWiredLedLocatorConformance=_ArubaWiredLedLocatorConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,7,2))
_ArubaWiredLedLocatorCompliances_ObjectIdentity=ObjectIdentity
arubaWiredLedLocatorCompliances=_ArubaWiredLedLocatorCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,7,2,1))
_ArubaWiredLedLocatorGroups_ObjectIdentity=ObjectIdentity
arubaWiredLedLocatorGroups=_ArubaWiredLedLocatorGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,7,2,2))
arubaWiredLedLocatorTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,11,7,2,2,1))
arubaWiredLedLocatorTableGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:arubaWiredLedLocatorTableGroup.setStatus(_A)
arubaWiredLedLocatorCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,11,7,2,1,1))
arubaWiredLedLocatorCompliance.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:arubaWiredLedLocatorCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'arubaWiredLedLocator':arubaWiredLedLocator,'arubaWiredLedLocatorObjects':arubaWiredLedLocatorObjects,'arubaWiredLedLocatorDetails':arubaWiredLedLocatorDetails,_H:arubaWiredLedLocatorTable,'arubaWiredLedLocatorEntry':arubaWiredLedLocatorEntry,_E:arubaWiredLedLocatorGroupIndex,_F:arubaWiredLedLocatorName,_G:arubaWiredLedLocatorState,'arubaWiredLedLocatorConformance':arubaWiredLedLocatorConformance,'arubaWiredLedLocatorCompliances':arubaWiredLedLocatorCompliances,'arubaWiredLedLocatorCompliance':arubaWiredLedLocatorCompliance,'arubaWiredLedLocatorGroups':arubaWiredLedLocatorGroups,_I:arubaWiredLedLocatorTableGroup})