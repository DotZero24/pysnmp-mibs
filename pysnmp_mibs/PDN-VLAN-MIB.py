_H='pdnVlanInbandMgmtVlanGroup'
_G='pdnVlanReservedBlockGroup'
_F='pdnVlanInbandMgmtVlanId2'
_E='pdnVlanReservedBlockStart'
_D='pdnVlanInbandMgmtVlanId'
_C='read-write'
_B='PDN-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_common,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-common')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnVlanMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,46))
if mibBuilder.loadTexts:pdnVlanMIB.setRevisions(('2003-11-12 00:00','2003-04-24 00:00','2003-04-11 00:00'))
_PdnVlanNotifications_ObjectIdentity=ObjectIdentity
pdnVlanNotifications=_PdnVlanNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,46,0))
_PdnVlanObjects_ObjectIdentity=ObjectIdentity
pdnVlanObjects=_PdnVlanObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,46,1))
_PdnVlanReservedBlockStart_Type=VlanIndex
_PdnVlanReservedBlockStart_Object=MibScalar
pdnVlanReservedBlockStart=_PdnVlanReservedBlockStart_Object((1,3,6,1,4,1,1795,2,24,2,46,1,1),_PdnVlanReservedBlockStart_Type())
pdnVlanReservedBlockStart.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnVlanReservedBlockStart.setStatus(_A)
_PdnVlanInbandMgmtVlanId_Type=VlanIndex
_PdnVlanInbandMgmtVlanId_Object=MibScalar
pdnVlanInbandMgmtVlanId=_PdnVlanInbandMgmtVlanId_Object((1,3,6,1,4,1,1795,2,24,2,46,1,2),_PdnVlanInbandMgmtVlanId_Type())
pdnVlanInbandMgmtVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnVlanInbandMgmtVlanId.setStatus(_A)
_PdnVlanInbandMgmtVlanId2_Type=VlanIndex
_PdnVlanInbandMgmtVlanId2_Object=MibScalar
pdnVlanInbandMgmtVlanId2=_PdnVlanInbandMgmtVlanId2_Object((1,3,6,1,4,1,1795,2,24,2,46,1,3),_PdnVlanInbandMgmtVlanId2_Type())
pdnVlanInbandMgmtVlanId2.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnVlanInbandMgmtVlanId2.setStatus(_A)
_PdnVlanAFNs_ObjectIdentity=ObjectIdentity
pdnVlanAFNs=_PdnVlanAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,46,2))
_PdnVlanConformance_ObjectIdentity=ObjectIdentity
pdnVlanConformance=_PdnVlanConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,46,3))
_PdnVlanCompliances_ObjectIdentity=ObjectIdentity
pdnVlanCompliances=_PdnVlanCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,46,3,1))
_PdnVlanGroups_ObjectIdentity=ObjectIdentity
pdnVlanGroups=_PdnVlanGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,46,3,2))
_PdnVlanObjGroups_ObjectIdentity=ObjectIdentity
pdnVlanObjGroups=_PdnVlanObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,46,3,2,1))
_PdnVlanAfnGroups_ObjectIdentity=ObjectIdentity
pdnVlanAfnGroups=_PdnVlanAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,46,3,2,2))
_PdnVlanNtfyGroups_ObjectIdentity=ObjectIdentity
pdnVlanNtfyGroups=_PdnVlanNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,46,3,2,3))
pdnVlanReservedBlockGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,46,3,2,1,1))
pdnVlanReservedBlockGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:pdnVlanReservedBlockGroup.setStatus(_A)
pdnVlanInbandMgmtVlanGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,46,3,2,1,2))
pdnVlanInbandMgmtVlanGroup.setObjects((_B,_D))
if mibBuilder.loadTexts:pdnVlanInbandMgmtVlanGroup.setStatus(_A)
pdnVlanInbandMgmtVlan2Group=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,46,3,2,1,3))
pdnVlanInbandMgmtVlan2Group.setObjects(*((_B,_D),(_B,_F)))
if mibBuilder.loadTexts:pdnVlanInbandMgmtVlan2Group.setStatus(_A)
pdnVlanMIBCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,46,3,1,1))
pdnVlanMIBCompliance.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:pdnVlanMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnVlanMIB':pdnVlanMIB,'pdnVlanNotifications':pdnVlanNotifications,'pdnVlanObjects':pdnVlanObjects,_E:pdnVlanReservedBlockStart,_D:pdnVlanInbandMgmtVlanId,_F:pdnVlanInbandMgmtVlanId2,'pdnVlanAFNs':pdnVlanAFNs,'pdnVlanConformance':pdnVlanConformance,'pdnVlanCompliances':pdnVlanCompliances,'pdnVlanMIBCompliance':pdnVlanMIBCompliance,'pdnVlanGroups':pdnVlanGroups,'pdnVlanObjGroups':pdnVlanObjGroups,_G:pdnVlanReservedBlockGroup,_H:pdnVlanInbandMgmtVlanGroup,'pdnVlanInbandMgmtVlan2Group':pdnVlanInbandMgmtVlan2Group,'pdnVlanAfnGroups':pdnVlanAfnGroups,'pdnVlanNtfyGroups':pdnVlanNtfyGroups})