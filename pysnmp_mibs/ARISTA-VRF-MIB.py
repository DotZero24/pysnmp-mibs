_K='aristaVrfInformationGroup'
_J='aristaVrfIfMembership'
_I='aristaVrfState'
_H='aristaVrfRouteDistinguisher'
_G='aristaVrfRoutingStatus'
_F='aristaVrfName'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='ARISTA-VRF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aristaVrfMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,18))
if mibBuilder.loadTexts:aristaVrfMIB.setRevisions(('2015-01-11 00:00',))
class VrfName(TextualConvention,OctetString):status=_A;displayHint='100t';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
class VrfRouteDistinguisher(TextualConvention,OctetString):status=_A;displayHint='256a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
class VrfState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_AristaVrfMibObjects_ObjectIdentity=ObjectIdentity
aristaVrfMibObjects=_AristaVrfMibObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,18,1))
_AristaVrfTable_Object=MibTable
aristaVrfTable=_AristaVrfTable_Object((1,3,6,1,4,1,30065,3,18,1,1))
if mibBuilder.loadTexts:aristaVrfTable.setStatus(_A)
_AristaVrfEntry_Object=MibTableRow
aristaVrfEntry=_AristaVrfEntry_Object((1,3,6,1,4,1,30065,3,18,1,1,1))
aristaVrfEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:aristaVrfEntry.setStatus(_A)
_AristaVrfName_Type=VrfName
_AristaVrfName_Object=MibTableColumn
aristaVrfName=_AristaVrfName_Object((1,3,6,1,4,1,30065,3,18,1,1,1,1),_AristaVrfName_Type())
aristaVrfName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:aristaVrfName.setStatus(_A)
class _AristaVrfRoutingStatus_Type(Bits):namedValues=NamedValues(*(('ipv4',0),('ipv6',1)))
_AristaVrfRoutingStatus_Type.__name__='Bits'
_AristaVrfRoutingStatus_Object=MibTableColumn
aristaVrfRoutingStatus=_AristaVrfRoutingStatus_Object((1,3,6,1,4,1,30065,3,18,1,1,1,2),_AristaVrfRoutingStatus_Type())
aristaVrfRoutingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVrfRoutingStatus.setStatus(_A)
_AristaVrfRouteDistinguisher_Type=VrfRouteDistinguisher
_AristaVrfRouteDistinguisher_Object=MibTableColumn
aristaVrfRouteDistinguisher=_AristaVrfRouteDistinguisher_Object((1,3,6,1,4,1,30065,3,18,1,1,1,3),_AristaVrfRouteDistinguisher_Type())
aristaVrfRouteDistinguisher.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVrfRouteDistinguisher.setStatus(_A)
_AristaVrfState_Type=VrfState
_AristaVrfState_Object=MibTableColumn
aristaVrfState=_AristaVrfState_Object((1,3,6,1,4,1,30065,3,18,1,1,1,4),_AristaVrfState_Type())
aristaVrfState.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVrfState.setStatus(_A)
_AristaVrfIfTable_Object=MibTable
aristaVrfIfTable=_AristaVrfIfTable_Object((1,3,6,1,4,1,30065,3,18,1,2))
if mibBuilder.loadTexts:aristaVrfIfTable.setStatus(_A)
_AristaVrfIfEntry_Object=MibTableRow
aristaVrfIfEntry=_AristaVrfIfEntry_Object((1,3,6,1,4,1,30065,3,18,1,2,1))
aristaVrfIfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:aristaVrfIfEntry.setStatus(_A)
_AristaVrfIfMembership_Type=VrfName
_AristaVrfIfMembership_Object=MibTableColumn
aristaVrfIfMembership=_AristaVrfIfMembership_Object((1,3,6,1,4,1,30065,3,18,1,2,1,1),_AristaVrfIfMembership_Type())
aristaVrfIfMembership.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaVrfIfMembership.setStatus(_A)
_AristaVrfMibConformance_ObjectIdentity=ObjectIdentity
aristaVrfMibConformance=_AristaVrfMibConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,18,2))
_AristaVrfMibCompliances_ObjectIdentity=ObjectIdentity
aristaVrfMibCompliances=_AristaVrfMibCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,18,2,1))
_AristaVrfMibGroups_ObjectIdentity=ObjectIdentity
aristaVrfMibGroups=_AristaVrfMibGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,18,2,2))
aristaVrfInformationGroup=ObjectGroup((1,3,6,1,4,1,30065,3,18,2,2,1))
aristaVrfInformationGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:aristaVrfInformationGroup.setStatus(_A)
aristaVrfMibCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,18,2,1,1))
aristaVrfMibCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:aristaVrfMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VrfName':VrfName,'VrfRouteDistinguisher':VrfRouteDistinguisher,'VrfState':VrfState,'aristaVrfMIB':aristaVrfMIB,'aristaVrfMibObjects':aristaVrfMibObjects,'aristaVrfTable':aristaVrfTable,'aristaVrfEntry':aristaVrfEntry,_F:aristaVrfName,_G:aristaVrfRoutingStatus,_H:aristaVrfRouteDistinguisher,_I:aristaVrfState,'aristaVrfIfTable':aristaVrfIfTable,'aristaVrfIfEntry':aristaVrfIfEntry,_J:aristaVrfIfMembership,'aristaVrfMibConformance':aristaVrfMibConformance,'aristaVrfMibCompliances':aristaVrfMibCompliances,'aristaVrfMibCompliance':aristaVrfMibCompliance,'aristaVrfMibGroups':aristaVrfMibGroups,_K:aristaVrfInformationGroup})