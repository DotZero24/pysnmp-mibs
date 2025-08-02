_H='arubaWiredPortVlanMemberTableGroup'
_G='arubaWiredPortVlanMemberVid'
_F='arubaWiredPortVlanMemberMode'
_E='read-only'
_D='arubaWiredPortVlanMemberIndex'
_C='Integer32'
_B='ARUBAWIRED-PORTVLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arubaWiredPortVlanMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,18))
if mibBuilder.loadTexts:arubaWiredPortVlanMIB.setRevisions(('2021-10-14 00:00','2020-11-20 00:00'))
class VidList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_ArubaWiredPortVlanNotifications_ObjectIdentity=ObjectIdentity
arubaWiredPortVlanNotifications=_ArubaWiredPortVlanNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,18,0))
_ArubaWiredPortVlanObjects_ObjectIdentity=ObjectIdentity
arubaWiredPortVlanObjects=_ArubaWiredPortVlanObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,18,1))
_ArubaWiredPortVlanConfig_ObjectIdentity=ObjectIdentity
arubaWiredPortVlanConfig=_ArubaWiredPortVlanConfig_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,18,1,0))
_ArubaWiredPortVlanStatus_ObjectIdentity=ObjectIdentity
arubaWiredPortVlanStatus=_ArubaWiredPortVlanStatus_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,18,1,1))
_ArubaWiredPortVlanMemberTable_Object=MibTable
arubaWiredPortVlanMemberTable=_ArubaWiredPortVlanMemberTable_Object((1,3,6,1,4,1,47196,4,1,1,3,18,1,1,1))
if mibBuilder.loadTexts:arubaWiredPortVlanMemberTable.setStatus(_A)
_ArubaWiredPortVlanMemberEntry_Object=MibTableRow
arubaWiredPortVlanMemberEntry=_ArubaWiredPortVlanMemberEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,18,1,1,1,1))
arubaWiredPortVlanMemberEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:arubaWiredPortVlanMemberEntry.setStatus(_A)
_ArubaWiredPortVlanMemberIndex_Type=InterfaceIndex
_ArubaWiredPortVlanMemberIndex_Object=MibTableColumn
arubaWiredPortVlanMemberIndex=_ArubaWiredPortVlanMemberIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,18,1,1,1,1,1),_ArubaWiredPortVlanMemberIndex_Type())
arubaWiredPortVlanMemberIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:arubaWiredPortVlanMemberIndex.setStatus(_A)
class _ArubaWiredPortVlanMemberMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trunk',1),('access',2)))
_ArubaWiredPortVlanMemberMode_Type.__name__=_C
_ArubaWiredPortVlanMemberMode_Object=MibTableColumn
arubaWiredPortVlanMemberMode=_ArubaWiredPortVlanMemberMode_Object((1,3,6,1,4,1,47196,4,1,1,3,18,1,1,1,1,2),_ArubaWiredPortVlanMemberMode_Type())
arubaWiredPortVlanMemberMode.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredPortVlanMemberMode.setStatus(_A)
_ArubaWiredPortVlanMemberVid_Type=VidList
_ArubaWiredPortVlanMemberVid_Object=MibTableColumn
arubaWiredPortVlanMemberVid=_ArubaWiredPortVlanMemberVid_Object((1,3,6,1,4,1,47196,4,1,1,3,18,1,1,1,1,3),_ArubaWiredPortVlanMemberVid_Type())
arubaWiredPortVlanMemberVid.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredPortVlanMemberVid.setStatus(_A)
_ArubaWiredPortVlanConformance_ObjectIdentity=ObjectIdentity
arubaWiredPortVlanConformance=_ArubaWiredPortVlanConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,18,2))
_ArubaWiredPortVlanCompliances_ObjectIdentity=ObjectIdentity
arubaWiredPortVlanCompliances=_ArubaWiredPortVlanCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,18,2,1))
_ArubaWiredPortVlanGroups_ObjectIdentity=ObjectIdentity
arubaWiredPortVlanGroups=_ArubaWiredPortVlanGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,18,2,2))
arubaWiredPortVlanMemberTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,18,2,2,1))
arubaWiredPortVlanMemberTableGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:arubaWiredPortVlanMemberTableGroup.setStatus(_A)
arubaWiredPortVlanMibCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,18,2,1,1))
arubaWiredPortVlanMibCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:arubaWiredPortVlanMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VidList':VidList,'arubaWiredPortVlanMIB':arubaWiredPortVlanMIB,'arubaWiredPortVlanNotifications':arubaWiredPortVlanNotifications,'arubaWiredPortVlanObjects':arubaWiredPortVlanObjects,'arubaWiredPortVlanConfig':arubaWiredPortVlanConfig,'arubaWiredPortVlanStatus':arubaWiredPortVlanStatus,'arubaWiredPortVlanMemberTable':arubaWiredPortVlanMemberTable,'arubaWiredPortVlanMemberEntry':arubaWiredPortVlanMemberEntry,_D:arubaWiredPortVlanMemberIndex,_F:arubaWiredPortVlanMemberMode,_G:arubaWiredPortVlanMemberVid,'arubaWiredPortVlanConformance':arubaWiredPortVlanConformance,'arubaWiredPortVlanCompliances':arubaWiredPortVlanCompliances,'arubaWiredPortVlanMibCompliance':arubaWiredPortVlanMibCompliance,'arubaWiredPortVlanGroups':arubaWiredPortVlanGroups,_H:arubaWiredPortVlanMemberTableGroup})