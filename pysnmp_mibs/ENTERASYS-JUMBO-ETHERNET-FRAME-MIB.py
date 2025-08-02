_N='etsysJumboEnetFrameControlGroup2'
_M='etsysJumboEnetFrameControlGroup'
_L='etsysJumboEnetFrameOperStatus'
_K='etsysJumboEnetFrameAdminStatus'
_J='etsysJumboEnetFrameEnable'
_I='read-only'
_H='read-write'
_G='ifIndex'
_F='IF-MIB'
_E='etsysJumboEnetFrameMtu'
_D='obsolete'
_C='EnabledStatus'
_B='current'
_A='ENTERASYS-JUMBO-ETHERNET-FRAME-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,=mibBuilder.importSymbols(_F,_G)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_C)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysJumboEthernetFrameMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,34))
if mibBuilder.loadTexts:etsysJumboEthernetFrameMIB.setRevisions(('2003-01-24 21:26','2002-12-20 21:56'))
_EtsysJumboEthernetFrame_ObjectIdentity=ObjectIdentity
etsysJumboEthernetFrame=_EtsysJumboEthernetFrame_ObjectIdentity((1,3,6,1,4,1,5624,1,2,34,1))
_EtsysJumboEnetFrameControl_ObjectIdentity=ObjectIdentity
etsysJumboEnetFrameControl=_EtsysJumboEnetFrameControl_ObjectIdentity((1,3,6,1,4,1,5624,1,2,34,1,1))
_EtsysJumboEnetFrameTable_Object=MibTable
etsysJumboEnetFrameTable=_EtsysJumboEnetFrameTable_Object((1,3,6,1,4,1,5624,1,2,34,1,1,1))
if mibBuilder.loadTexts:etsysJumboEnetFrameTable.setStatus(_B)
_EtsysJumboEnetFrameEntry_Object=MibTableRow
etsysJumboEnetFrameEntry=_EtsysJumboEnetFrameEntry_Object((1,3,6,1,4,1,5624,1,2,34,1,1,1,1))
etsysJumboEnetFrameEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:etsysJumboEnetFrameEntry.setStatus(_B)
class _EtsysJumboEnetFrameEnable_Type(EnabledStatus):defaultValue=2
_EtsysJumboEnetFrameEnable_Type.__name__=_C
_EtsysJumboEnetFrameEnable_Object=MibTableColumn
etsysJumboEnetFrameEnable=_EtsysJumboEnetFrameEnable_Object((1,3,6,1,4,1,5624,1,2,34,1,1,1,1,1),_EtsysJumboEnetFrameEnable_Type())
etsysJumboEnetFrameEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysJumboEnetFrameEnable.setStatus(_D)
_EtsysJumboEnetFrameMtu_Type=Integer32
_EtsysJumboEnetFrameMtu_Object=MibTableColumn
etsysJumboEnetFrameMtu=_EtsysJumboEnetFrameMtu_Object((1,3,6,1,4,1,5624,1,2,34,1,1,1,1,2),_EtsysJumboEnetFrameMtu_Type())
etsysJumboEnetFrameMtu.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysJumboEnetFrameMtu.setStatus(_B)
class _EtsysJumboEnetFrameAdminStatus_Type(EnabledStatus):defaultValue=2
_EtsysJumboEnetFrameAdminStatus_Type.__name__=_C
_EtsysJumboEnetFrameAdminStatus_Object=MibTableColumn
etsysJumboEnetFrameAdminStatus=_EtsysJumboEnetFrameAdminStatus_Object((1,3,6,1,4,1,5624,1,2,34,1,1,1,1,3),_EtsysJumboEnetFrameAdminStatus_Type())
etsysJumboEnetFrameAdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysJumboEnetFrameAdminStatus.setStatus(_B)
_EtsysJumboEnetFrameOperStatus_Type=EnabledStatus
_EtsysJumboEnetFrameOperStatus_Object=MibTableColumn
etsysJumboEnetFrameOperStatus=_EtsysJumboEnetFrameOperStatus_Object((1,3,6,1,4,1,5624,1,2,34,1,1,1,1,4),_EtsysJumboEnetFrameOperStatus_Type())
etsysJumboEnetFrameOperStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysJumboEnetFrameOperStatus.setStatus(_B)
_EtsysJumboEnetFrameConformance_ObjectIdentity=ObjectIdentity
etsysJumboEnetFrameConformance=_EtsysJumboEnetFrameConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,34,2))
_EtsysJumboEnetFrameGroups_ObjectIdentity=ObjectIdentity
etsysJumboEnetFrameGroups=_EtsysJumboEnetFrameGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,34,2,1))
_EtsysJumboEnetFrameCompliances_ObjectIdentity=ObjectIdentity
etsysJumboEnetFrameCompliances=_EtsysJumboEnetFrameCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,34,2,2))
etsysJumboEnetFrameControlGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,34,2,1,1))
etsysJumboEnetFrameControlGroup.setObjects(*((_A,_J),(_A,_E)))
if mibBuilder.loadTexts:etsysJumboEnetFrameControlGroup.setStatus(_D)
etsysJumboEnetFrameControlGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,34,2,1,2))
etsysJumboEnetFrameControlGroup2.setObjects(*((_A,_E),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:etsysJumboEnetFrameControlGroup2.setStatus(_B)
etsysJumboEnetFrameCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,34,2,2,1))
etsysJumboEnetFrameCompliance.setObjects((_A,_M))
if mibBuilder.loadTexts:etsysJumboEnetFrameCompliance.setStatus(_D)
etsysJumboEnetFrameCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,34,2,2,2))
etsysJumboEnetFrameCompliance2.setObjects((_A,_N))
if mibBuilder.loadTexts:etsysJumboEnetFrameCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysJumboEthernetFrameMIB':etsysJumboEthernetFrameMIB,'etsysJumboEthernetFrame':etsysJumboEthernetFrame,'etsysJumboEnetFrameControl':etsysJumboEnetFrameControl,'etsysJumboEnetFrameTable':etsysJumboEnetFrameTable,'etsysJumboEnetFrameEntry':etsysJumboEnetFrameEntry,_J:etsysJumboEnetFrameEnable,_E:etsysJumboEnetFrameMtu,_K:etsysJumboEnetFrameAdminStatus,_L:etsysJumboEnetFrameOperStatus,'etsysJumboEnetFrameConformance':etsysJumboEnetFrameConformance,'etsysJumboEnetFrameGroups':etsysJumboEnetFrameGroups,_M:etsysJumboEnetFrameControlGroup,_N:etsysJumboEnetFrameControlGroup2,'etsysJumboEnetFrameCompliances':etsysJumboEnetFrameCompliances,'etsysJumboEnetFrameCompliance':etsysJumboEnetFrameCompliance,'etsysJumboEnetFrameCompliance2':etsysJumboEnetFrameCompliance2})