_O='etsysVlanAuthorizationGroup'
_N='etsysVlanAuthorizationVlanID'
_M='etsysVlanAuthorizationOperEgress'
_L='etsysVlanAuthorizationAdminEgress'
_K='etsysVlanAuthorizationStatus'
_J='etsysVlanAuthorizationEnable'
_I='read-only'
_H='Integer32'
_G='dot1dBasePort'
_F='BRIDGE-MIB'
_E='VlanAuthEgressStatus'
_D='read-write'
_C='EnabledStatus'
_B='ENTERASYS-VLAN-AUTHORIZATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_F,_G)
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysVlanAuthorizationMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,48))
if mibBuilder.loadTexts:etsysVlanAuthorizationMIB.setRevisions(('2004-06-02 19:22',))
class VlanAuthEgressStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('tagged',2),('untagged',3),('dynamic',4)))
_EtsysVlanAuthorizationObjects_ObjectIdentity=ObjectIdentity
etsysVlanAuthorizationObjects=_EtsysVlanAuthorizationObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,48,1))
_EtsysVlanAuthorizationSystem_ObjectIdentity=ObjectIdentity
etsysVlanAuthorizationSystem=_EtsysVlanAuthorizationSystem_ObjectIdentity((1,3,6,1,4,1,5624,1,2,48,1,1))
class _EtsysVlanAuthorizationEnable_Type(EnabledStatus):defaultValue=2
_EtsysVlanAuthorizationEnable_Type.__name__=_C
_EtsysVlanAuthorizationEnable_Object=MibScalar
etsysVlanAuthorizationEnable=_EtsysVlanAuthorizationEnable_Object((1,3,6,1,4,1,5624,1,2,48,1,1,1),_EtsysVlanAuthorizationEnable_Type())
etsysVlanAuthorizationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVlanAuthorizationEnable.setStatus(_A)
_EtsysVlanAuthorizationPorts_ObjectIdentity=ObjectIdentity
etsysVlanAuthorizationPorts=_EtsysVlanAuthorizationPorts_ObjectIdentity((1,3,6,1,4,1,5624,1,2,48,1,2))
_EtsysVlanAuthorizationTable_Object=MibTable
etsysVlanAuthorizationTable=_EtsysVlanAuthorizationTable_Object((1,3,6,1,4,1,5624,1,2,48,1,2,1))
if mibBuilder.loadTexts:etsysVlanAuthorizationTable.setStatus(_A)
_EtsysVlanAuthorizationEntry_Object=MibTableRow
etsysVlanAuthorizationEntry=_EtsysVlanAuthorizationEntry_Object((1,3,6,1,4,1,5624,1,2,48,1,2,1,1))
etsysVlanAuthorizationEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:etsysVlanAuthorizationEntry.setStatus(_A)
class _EtsysVlanAuthorizationStatus_Type(EnabledStatus):defaultValue=1
_EtsysVlanAuthorizationStatus_Type.__name__=_C
_EtsysVlanAuthorizationStatus_Object=MibTableColumn
etsysVlanAuthorizationStatus=_EtsysVlanAuthorizationStatus_Object((1,3,6,1,4,1,5624,1,2,48,1,2,1,1,1),_EtsysVlanAuthorizationStatus_Type())
etsysVlanAuthorizationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVlanAuthorizationStatus.setStatus(_A)
class _EtsysVlanAuthorizationAdminEgress_Type(VlanAuthEgressStatus):defaultValue=3
_EtsysVlanAuthorizationAdminEgress_Type.__name__=_E
_EtsysVlanAuthorizationAdminEgress_Object=MibTableColumn
etsysVlanAuthorizationAdminEgress=_EtsysVlanAuthorizationAdminEgress_Object((1,3,6,1,4,1,5624,1,2,48,1,2,1,1,2),_EtsysVlanAuthorizationAdminEgress_Type())
etsysVlanAuthorizationAdminEgress.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysVlanAuthorizationAdminEgress.setStatus(_A)
class _EtsysVlanAuthorizationOperEgress_Type(VlanAuthEgressStatus):defaultValue=1
_EtsysVlanAuthorizationOperEgress_Type.__name__=_E
_EtsysVlanAuthorizationOperEgress_Object=MibTableColumn
etsysVlanAuthorizationOperEgress=_EtsysVlanAuthorizationOperEgress_Object((1,3,6,1,4,1,5624,1,2,48,1,2,1,1,3),_EtsysVlanAuthorizationOperEgress_Type())
etsysVlanAuthorizationOperEgress.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysVlanAuthorizationOperEgress.setStatus(_A)
class _EtsysVlanAuthorizationVlanID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_EtsysVlanAuthorizationVlanID_Type.__name__=_H
_EtsysVlanAuthorizationVlanID_Object=MibTableColumn
etsysVlanAuthorizationVlanID=_EtsysVlanAuthorizationVlanID_Object((1,3,6,1,4,1,5624,1,2,48,1,2,1,1,4),_EtsysVlanAuthorizationVlanID_Type())
etsysVlanAuthorizationVlanID.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysVlanAuthorizationVlanID.setStatus(_A)
_EtsysVlanAuthorizationConformance_ObjectIdentity=ObjectIdentity
etsysVlanAuthorizationConformance=_EtsysVlanAuthorizationConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,48,2))
_EtsysVlanAuthorizationGroups_ObjectIdentity=ObjectIdentity
etsysVlanAuthorizationGroups=_EtsysVlanAuthorizationGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,48,2,1))
_EtsysVlanAuthorizationCompliances_ObjectIdentity=ObjectIdentity
etsysVlanAuthorizationCompliances=_EtsysVlanAuthorizationCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,48,2,2))
etsysVlanAuthorizationGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,48,2,1,1))
etsysVlanAuthorizationGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:etsysVlanAuthorizationGroup.setStatus(_A)
etsysVlanAuthorizationCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,48,2,2,1))
etsysVlanAuthorizationCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:etsysVlanAuthorizationCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_E:VlanAuthEgressStatus,'etsysVlanAuthorizationMIB':etsysVlanAuthorizationMIB,'etsysVlanAuthorizationObjects':etsysVlanAuthorizationObjects,'etsysVlanAuthorizationSystem':etsysVlanAuthorizationSystem,_J:etsysVlanAuthorizationEnable,'etsysVlanAuthorizationPorts':etsysVlanAuthorizationPorts,'etsysVlanAuthorizationTable':etsysVlanAuthorizationTable,'etsysVlanAuthorizationEntry':etsysVlanAuthorizationEntry,_K:etsysVlanAuthorizationStatus,_L:etsysVlanAuthorizationAdminEgress,_M:etsysVlanAuthorizationOperEgress,_N:etsysVlanAuthorizationVlanID,'etsysVlanAuthorizationConformance':etsysVlanAuthorizationConformance,'etsysVlanAuthorizationGroups':etsysVlanAuthorizationGroups,_O:etsysVlanAuthorizationGroup,'etsysVlanAuthorizationCompliances':etsysVlanAuthorizationCompliances,'etsysVlanAuthorizationCompliance':etsysVlanAuthorizationCompliance})