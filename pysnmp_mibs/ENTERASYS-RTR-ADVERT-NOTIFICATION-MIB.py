_N='etsysRtrAdvertNotificationGroup'
_M='etsysRtrAdvertInformationGroup'
_L='etsysRtrAdvertConfigGroup'
_K='etsysRtrAdvertInconsistent'
_J='etsysRtrAdvertInconsistentEnabled'
_I='TruthValue'
_H='ifName'
_G='IF-MIB'
_F='etsysRtrAdvertUserData'
_E='etsysRtrAdvertInetAddress'
_D='etsysRtrAdvertInetAddrType'
_C='accessible-for-notify'
_B='current'
_A='ENTERASYS-RTR-ADVERT-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifName,=mibBuilder.importSymbols(_G,_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
etsysRtrAdvertNotificationMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,82))
if mibBuilder.loadTexts:etsysRtrAdvertNotificationMIB.setRevisions(('2011-05-13 13:47',))
_EtsysRtrAdvertNotificationObjects_ObjectIdentity=ObjectIdentity
etsysRtrAdvertNotificationObjects=_EtsysRtrAdvertNotificationObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,82,1))
_EtsysRtrAdvertConfigBranch_ObjectIdentity=ObjectIdentity
etsysRtrAdvertConfigBranch=_EtsysRtrAdvertConfigBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,82,1,0))
class _EtsysRtrAdvertInconsistentEnabled_Type(TruthValue):defaultValue=2
_EtsysRtrAdvertInconsistentEnabled_Type.__name__=_I
_EtsysRtrAdvertInconsistentEnabled_Object=MibScalar
etsysRtrAdvertInconsistentEnabled=_EtsysRtrAdvertInconsistentEnabled_Object((1,3,6,1,4,1,5624,1,2,82,1,0,1),_EtsysRtrAdvertInconsistentEnabled_Type())
etsysRtrAdvertInconsistentEnabled.setMaxAccess('read-write')
if mibBuilder.loadTexts:etsysRtrAdvertInconsistentEnabled.setStatus(_B)
_EtsysRtrAdvertInformationBranch_ObjectIdentity=ObjectIdentity
etsysRtrAdvertInformationBranch=_EtsysRtrAdvertInformationBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,82,1,1))
_EtsysRtrAdvertInetAddrType_Type=InetAddressType
_EtsysRtrAdvertInetAddrType_Object=MibScalar
etsysRtrAdvertInetAddrType=_EtsysRtrAdvertInetAddrType_Object((1,3,6,1,4,1,5624,1,2,82,1,1,1),_EtsysRtrAdvertInetAddrType_Type())
etsysRtrAdvertInetAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysRtrAdvertInetAddrType.setStatus(_B)
_EtsysRtrAdvertInetAddress_Type=InetAddress
_EtsysRtrAdvertInetAddress_Object=MibScalar
etsysRtrAdvertInetAddress=_EtsysRtrAdvertInetAddress_Object((1,3,6,1,4,1,5624,1,2,82,1,1,2),_EtsysRtrAdvertInetAddress_Type())
etsysRtrAdvertInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysRtrAdvertInetAddress.setStatus(_B)
_EtsysRtrAdvertUserData_Type=SnmpAdminString
_EtsysRtrAdvertUserData_Object=MibScalar
etsysRtrAdvertUserData=_EtsysRtrAdvertUserData_Object((1,3,6,1,4,1,5624,1,2,82,1,1,3),_EtsysRtrAdvertUserData_Type())
etsysRtrAdvertUserData.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysRtrAdvertUserData.setStatus(_B)
_EtsysRtrAdvertNotificationBranch_ObjectIdentity=ObjectIdentity
etsysRtrAdvertNotificationBranch=_EtsysRtrAdvertNotificationBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,82,1,2))
_EtsysRtrAdvertConformance_ObjectIdentity=ObjectIdentity
etsysRtrAdvertConformance=_EtsysRtrAdvertConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,82,2))
_EtsysRtrAdvertGroups_ObjectIdentity=ObjectIdentity
etsysRtrAdvertGroups=_EtsysRtrAdvertGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,82,2,1))
_EtsysRtrAdvertCompliances_ObjectIdentity=ObjectIdentity
etsysRtrAdvertCompliances=_EtsysRtrAdvertCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,82,2,2))
etsysRtrAdvertConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,82,2,1,1))
etsysRtrAdvertConfigGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:etsysRtrAdvertConfigGroup.setStatus(_B)
etsysRtrAdvertInformationGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,82,2,1,2))
etsysRtrAdvertInformationGroup.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:etsysRtrAdvertInformationGroup.setStatus(_B)
etsysRtrAdvertInconsistent=NotificationType((1,3,6,1,4,1,5624,1,2,82,1,2,1))
etsysRtrAdvertInconsistent.setObjects(*((_A,_D),(_A,_E),(_G,_H),(_A,_F)))
if mibBuilder.loadTexts:etsysRtrAdvertInconsistent.setStatus(_B)
etsysRtrAdvertNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,82,2,1,3))
etsysRtrAdvertNotificationGroup.setObjects((_A,_K))
if mibBuilder.loadTexts:etsysRtrAdvertNotificationGroup.setStatus(_B)
etsysRtrAdvertCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,82,2,2,1))
etsysRtrAdvertCompliance.setObjects(*((_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:etsysRtrAdvertCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysRtrAdvertNotificationMIB':etsysRtrAdvertNotificationMIB,'etsysRtrAdvertNotificationObjects':etsysRtrAdvertNotificationObjects,'etsysRtrAdvertConfigBranch':etsysRtrAdvertConfigBranch,_J:etsysRtrAdvertInconsistentEnabled,'etsysRtrAdvertInformationBranch':etsysRtrAdvertInformationBranch,_D:etsysRtrAdvertInetAddrType,_E:etsysRtrAdvertInetAddress,_F:etsysRtrAdvertUserData,'etsysRtrAdvertNotificationBranch':etsysRtrAdvertNotificationBranch,_K:etsysRtrAdvertInconsistent,'etsysRtrAdvertConformance':etsysRtrAdvertConformance,'etsysRtrAdvertGroups':etsysRtrAdvertGroups,_L:etsysRtrAdvertConfigGroup,_M:etsysRtrAdvertInformationGroup,_N:etsysRtrAdvertNotificationGroup,'etsysRtrAdvertCompliances':etsysRtrAdvertCompliances,'etsysRtrAdvertCompliance':etsysRtrAdvertCompliance})