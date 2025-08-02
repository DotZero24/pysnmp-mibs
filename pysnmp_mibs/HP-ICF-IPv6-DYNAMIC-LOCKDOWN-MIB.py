_h='hpicfSourceBindingTrapsGroup'
_g='hpicfSourceBindingTrapObjectsGroup'
_f='hpicfIpv6LockBaseGroup'
_e='hpicfDIPLDv6SourceBindingVoilations'
_d='hpicfDIPDv6SourceBindingOutOfResources'
_c='hpicfDIPLDv6SourceBindingViolationsTrapCtrl'
_b='hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl'
_a='hpicfDIPLDv6ResourceAvailable'
_Z='hpicfDIPLDv6AddrVlan'
_Y='hpicfDIPLDv6PortOperStatus'
_X='hpicfDIPLDv6PortEnable'
_W='hpicfDIPLDv6LockEnable'
_V='hpicfDIPLDv6AddrEntry'
_U='ifIndex'
_T='IF-MIB'
_S='hpicfDIPLDv6SourceBindingVoilationsPktCount'
_R='hpicfDIPLDv6SourceBindingVoilationsMacAddress'
_Q='hpicfDIPLDv6SourceBindingVoilationsDstIpAddress'
_P='hpicfDIPLDv6SourceBindingVoilationsDstIpType'
_O='hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress'
_N='hpicfDIPLDv6SourceBindingVoilationsSrcIpType'
_M='hpicfDIPLDv6SourceBindingVoilationsPort'
_L='hpicfDIPLDv6SourceBindingVoilationsCount'
_K='hpicfDIPLDv6SourceBindingAddrVlan'
_J='hpicfDIPLDv6SourceBindingAddrIpAddress'
_I='hpicfDIPLDv6SourceBindingAddrIpAddressType'
_H='hpicfDIPLDv6SourceBindingAddrMacAddress'
_G='hpicfDIPLDv6SourceBindingAddrPort'
_F='TruthValue'
_E='read-write'
_D='read-only'
_C='accessible-for-notify'
_B='current'
_A='HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
hpicfSaviObjectsFilteringEntry,=mibBuilder.importSymbols('HPICF-SAVI-MIB','hpicfSaviObjectsFilteringEntry')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_T,'InterfaceIndex',_U)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_F)
hpicfIpv6Lockdown=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103))
if mibBuilder.loadTexts:hpicfIpv6Lockdown.setRevisions(('2017-11-08 00:00','2013-10-06 00:00'))
_HpicfDIPLDv6SourceBindingNotifications_ObjectIdentity=ObjectIdentity
hpicfDIPLDv6SourceBindingNotifications=_HpicfDIPLDv6SourceBindingNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103,0))
_HpicfDIPLDv6SourceBindingOutOfResourcesObjects_ObjectIdentity=ObjectIdentity
hpicfDIPLDv6SourceBindingOutOfResourcesObjects=_HpicfDIPLDv6SourceBindingOutOfResourcesObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103,0,2))
_HpicfDIPLDv6SourceBindingAddrPort_Type=InterfaceIndex
_HpicfDIPLDv6SourceBindingAddrPort_Object=MibScalar
hpicfDIPLDv6SourceBindingAddrPort=_HpicfDIPLDv6SourceBindingAddrPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,2,1),_HpicfDIPLDv6SourceBindingAddrPort_Type())
hpicfDIPLDv6SourceBindingAddrPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingAddrPort.setStatus(_B)
_HpicfDIPLDv6SourceBindingAddrMacAddress_Type=MacAddress
_HpicfDIPLDv6SourceBindingAddrMacAddress_Object=MibScalar
hpicfDIPLDv6SourceBindingAddrMacAddress=_HpicfDIPLDv6SourceBindingAddrMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,2,2),_HpicfDIPLDv6SourceBindingAddrMacAddress_Type())
hpicfDIPLDv6SourceBindingAddrMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingAddrMacAddress.setStatus(_B)
_HpicfDIPLDv6SourceBindingAddrIpAddressType_Type=InetAddressType
_HpicfDIPLDv6SourceBindingAddrIpAddressType_Object=MibScalar
hpicfDIPLDv6SourceBindingAddrIpAddressType=_HpicfDIPLDv6SourceBindingAddrIpAddressType_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,2,3),_HpicfDIPLDv6SourceBindingAddrIpAddressType_Type())
hpicfDIPLDv6SourceBindingAddrIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingAddrIpAddressType.setStatus(_B)
_HpicfDIPLDv6SourceBindingAddrIpAddress_Type=InetAddress
_HpicfDIPLDv6SourceBindingAddrIpAddress_Object=MibScalar
hpicfDIPLDv6SourceBindingAddrIpAddress=_HpicfDIPLDv6SourceBindingAddrIpAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,2,4),_HpicfDIPLDv6SourceBindingAddrIpAddress_Type())
hpicfDIPLDv6SourceBindingAddrIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingAddrIpAddress.setStatus(_B)
_HpicfDIPLDv6SourceBindingAddrVlan_Type=VlanIndex
_HpicfDIPLDv6SourceBindingAddrVlan_Object=MibScalar
hpicfDIPLDv6SourceBindingAddrVlan=_HpicfDIPLDv6SourceBindingAddrVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,2,5),_HpicfDIPLDv6SourceBindingAddrVlan_Type())
hpicfDIPLDv6SourceBindingAddrVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingAddrVlan.setStatus(_B)
_HpicfDIPLDv6SourceBindingVoilationsObjects_ObjectIdentity=ObjectIdentity
hpicfDIPLDv6SourceBindingVoilationsObjects=_HpicfDIPLDv6SourceBindingVoilationsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103,0,4))
_HpicfDIPLDv6SourceBindingVoilationsCount_Type=Counter32
_HpicfDIPLDv6SourceBindingVoilationsCount_Object=MibScalar
hpicfDIPLDv6SourceBindingVoilationsCount=_HpicfDIPLDv6SourceBindingVoilationsCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,4,1),_HpicfDIPLDv6SourceBindingVoilationsCount_Type())
hpicfDIPLDv6SourceBindingVoilationsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingVoilationsCount.setStatus(_B)
_HpicfDIPLDv6SourceBindingVoilationsPort_Type=InterfaceIndex
_HpicfDIPLDv6SourceBindingVoilationsPort_Object=MibScalar
hpicfDIPLDv6SourceBindingVoilationsPort=_HpicfDIPLDv6SourceBindingVoilationsPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,4,2),_HpicfDIPLDv6SourceBindingVoilationsPort_Type())
hpicfDIPLDv6SourceBindingVoilationsPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingVoilationsPort.setStatus(_B)
_HpicfDIPLDv6SourceBindingVoilationsSrcIpType_Type=InetAddressType
_HpicfDIPLDv6SourceBindingVoilationsSrcIpType_Object=MibScalar
hpicfDIPLDv6SourceBindingVoilationsSrcIpType=_HpicfDIPLDv6SourceBindingVoilationsSrcIpType_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,4,3),_HpicfDIPLDv6SourceBindingVoilationsSrcIpType_Type())
hpicfDIPLDv6SourceBindingVoilationsSrcIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingVoilationsSrcIpType.setStatus(_B)
_HpicfDIPLDv6SourceBindingVoilationsSrcIpAddress_Type=InetAddress
_HpicfDIPLDv6SourceBindingVoilationsSrcIpAddress_Object=MibScalar
hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress=_HpicfDIPLDv6SourceBindingVoilationsSrcIpAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,4,4),_HpicfDIPLDv6SourceBindingVoilationsSrcIpAddress_Type())
hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress.setStatus(_B)
_HpicfDIPLDv6SourceBindingVoilationsDstIpType_Type=InetAddressType
_HpicfDIPLDv6SourceBindingVoilationsDstIpType_Object=MibScalar
hpicfDIPLDv6SourceBindingVoilationsDstIpType=_HpicfDIPLDv6SourceBindingVoilationsDstIpType_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,4,5),_HpicfDIPLDv6SourceBindingVoilationsDstIpType_Type())
hpicfDIPLDv6SourceBindingVoilationsDstIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingVoilationsDstIpType.setStatus(_B)
_HpicfDIPLDv6SourceBindingVoilationsDstIpAddress_Type=InetAddress
_HpicfDIPLDv6SourceBindingVoilationsDstIpAddress_Object=MibScalar
hpicfDIPLDv6SourceBindingVoilationsDstIpAddress=_HpicfDIPLDv6SourceBindingVoilationsDstIpAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,4,6),_HpicfDIPLDv6SourceBindingVoilationsDstIpAddress_Type())
hpicfDIPLDv6SourceBindingVoilationsDstIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingVoilationsDstIpAddress.setStatus(_B)
_HpicfDIPLDv6SourceBindingVoilationsMacAddress_Type=MacAddress
_HpicfDIPLDv6SourceBindingVoilationsMacAddress_Object=MibScalar
hpicfDIPLDv6SourceBindingVoilationsMacAddress=_HpicfDIPLDv6SourceBindingVoilationsMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,4,7),_HpicfDIPLDv6SourceBindingVoilationsMacAddress_Type())
hpicfDIPLDv6SourceBindingVoilationsMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingVoilationsMacAddress.setStatus(_B)
_HpicfDIPLDv6SourceBindingVoilationsPktCount_Type=Counter32
_HpicfDIPLDv6SourceBindingVoilationsPktCount_Object=MibScalar
hpicfDIPLDv6SourceBindingVoilationsPktCount=_HpicfDIPLDv6SourceBindingVoilationsPktCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,0,4,8),_HpicfDIPLDv6SourceBindingVoilationsPktCount_Type())
hpicfDIPLDv6SourceBindingVoilationsPktCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingVoilationsPktCount.setStatus(_B)
_HpicfDIPLDv6Objects_ObjectIdentity=ObjectIdentity
hpicfDIPLDv6Objects=_HpicfDIPLDv6Objects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103,1))
_HpicfDIPLDv6Config_ObjectIdentity=ObjectIdentity
hpicfDIPLDv6Config=_HpicfDIPLDv6Config_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103,1,1))
_HpicfDIPLDv6LockEnable_Type=TruthValue
_HpicfDIPLDv6LockEnable_Object=MibScalar
hpicfDIPLDv6LockEnable=_HpicfDIPLDv6LockEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,1,1),_HpicfDIPLDv6LockEnable_Type())
hpicfDIPLDv6LockEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDIPLDv6LockEnable.setStatus(_B)
_HpicfDIPLDv6PortTable_Object=MibTable
hpicfDIPLDv6PortTable=_HpicfDIPLDv6PortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,1,2))
if mibBuilder.loadTexts:hpicfDIPLDv6PortTable.setStatus(_B)
_HpicfDIPLDv6PortEntry_Object=MibTableRow
hpicfDIPLDv6PortEntry=_HpicfDIPLDv6PortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,1,2,1))
hpicfDIPLDv6PortEntry.setIndexNames((0,_T,_U))
if mibBuilder.loadTexts:hpicfDIPLDv6PortEntry.setStatus(_B)
_HpicfDIPLDv6PortEnable_Type=TruthValue
_HpicfDIPLDv6PortEnable_Object=MibTableColumn
hpicfDIPLDv6PortEnable=_HpicfDIPLDv6PortEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,1,2,1,1),_HpicfDIPLDv6PortEnable_Type())
hpicfDIPLDv6PortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDIPLDv6PortEnable.setStatus(_B)
class _HpicfDIPLDv6PortOperStatus_Type(Bits):namedValues=NamedValues(*(('active',0),('noDsnoopv6',1),('trustedPort',2),('noSnoopingVlan',3)))
_HpicfDIPLDv6PortOperStatus_Type.__name__='Bits'
_HpicfDIPLDv6PortOperStatus_Object=MibTableColumn
hpicfDIPLDv6PortOperStatus=_HpicfDIPLDv6PortOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,1,2,1,2),_HpicfDIPLDv6PortOperStatus_Type())
hpicfDIPLDv6PortOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDIPLDv6PortOperStatus.setStatus(_B)
class _HpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl_Type(TruthValue):defaultValue=1
_HpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl_Type.__name__=_F
_HpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl_Object=MibScalar
hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl=_HpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,1,3),_HpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl_Type())
hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl.setStatus(_B)
class _HpicfDIPLDv6SourceBindingViolationsTrapCtrl_Type(TruthValue):defaultValue=1
_HpicfDIPLDv6SourceBindingViolationsTrapCtrl_Type.__name__=_F
_HpicfDIPLDv6SourceBindingViolationsTrapCtrl_Object=MibScalar
hpicfDIPLDv6SourceBindingViolationsTrapCtrl=_HpicfDIPLDv6SourceBindingViolationsTrapCtrl_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,1,4),_HpicfDIPLDv6SourceBindingViolationsTrapCtrl_Type())
hpicfDIPLDv6SourceBindingViolationsTrapCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingViolationsTrapCtrl.setStatus(_B)
_HpicfDIPLDv6Status_ObjectIdentity=ObjectIdentity
hpicfDIPLDv6Status=_HpicfDIPLDv6Status_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103,1,2))
_HpicfDIPLDv6AddrTable_Object=MibTable
hpicfDIPLDv6AddrTable=_HpicfDIPLDv6AddrTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,2,1))
if mibBuilder.loadTexts:hpicfDIPLDv6AddrTable.setStatus(_B)
_HpicfDIPLDv6AddrEntry_Object=MibTableRow
hpicfDIPLDv6AddrEntry=_HpicfDIPLDv6AddrEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,2,1,1))
if mibBuilder.loadTexts:hpicfDIPLDv6AddrEntry.setStatus(_B)
_HpicfDIPLDv6AddrVlan_Type=VlanIndex
_HpicfDIPLDv6AddrVlan_Object=MibTableColumn
hpicfDIPLDv6AddrVlan=_HpicfDIPLDv6AddrVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,2,1,1,1),_HpicfDIPLDv6AddrVlan_Type())
hpicfDIPLDv6AddrVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDIPLDv6AddrVlan.setStatus(_B)
_HpicfDIPLDv6ResourceAvailable_Type=TruthValue
_HpicfDIPLDv6ResourceAvailable_Object=MibTableColumn
hpicfDIPLDv6ResourceAvailable=_HpicfDIPLDv6ResourceAvailable_Object((1,3,6,1,4,1,11,2,14,11,5,1,103,1,2,1,1,2),_HpicfDIPLDv6ResourceAvailable_Type())
hpicfDIPLDv6ResourceAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDIPLDv6ResourceAvailable.setStatus(_B)
_HpicfIpv6LockConformance_ObjectIdentity=ObjectIdentity
hpicfIpv6LockConformance=_HpicfIpv6LockConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103,2))
_HpicfIpv6LockGroups_ObjectIdentity=ObjectIdentity
hpicfIpv6LockGroups=_HpicfIpv6LockGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103,2,1))
_HpicfIpv6LockCompliances_ObjectIdentity=ObjectIdentity
hpicfIpv6LockCompliances=_HpicfIpv6LockCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,103,2,2))
hpicfSaviObjectsFilteringEntry.registerAugmentions((_A,_V))
hpicfDIPLDv6AddrEntry.setIndexNames(*hpicfSaviObjectsFilteringEntry.getIndexNames())
hpicfIpv6LockBaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,103,2,1,1))
hpicfIpv6LockBaseGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:hpicfIpv6LockBaseGroup.setStatus(_B)
hpicfSourceBindingTrapObjectsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,103,2,1,2))
hpicfSourceBindingTrapObjectsGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:hpicfSourceBindingTrapObjectsGroup.setStatus(_B)
hpicfDIPDv6SourceBindingOutOfResources=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,103,0,1))
hpicfDIPDv6SourceBindingOutOfResources.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:hpicfDIPDv6SourceBindingOutOfResources.setStatus(_B)
hpicfDIPLDv6SourceBindingVoilations=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,103,0,3))
hpicfDIPLDv6SourceBindingVoilations.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:hpicfDIPLDv6SourceBindingVoilations.setStatus(_B)
hpicfSourceBindingTrapsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,103,2,1,3))
hpicfSourceBindingTrapsGroup.setObjects(*((_A,_d),(_A,_e)))
if mibBuilder.loadTexts:hpicfSourceBindingTrapsGroup.setStatus(_B)
hpicfDIPLDv6Compliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,103,2,2,1))
hpicfDIPLDv6Compliance.setObjects((_A,_f))
if mibBuilder.loadTexts:hpicfDIPLDv6Compliance.setStatus(_B)
hpicfIpv6SourceBindingTrapCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,103,2,2,2))
hpicfIpv6SourceBindingTrapCompliance.setObjects(*((_A,_g),(_A,_h)))
if mibBuilder.loadTexts:hpicfIpv6SourceBindingTrapCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfIpv6Lockdown':hpicfIpv6Lockdown,'hpicfDIPLDv6SourceBindingNotifications':hpicfDIPLDv6SourceBindingNotifications,_d:hpicfDIPDv6SourceBindingOutOfResources,'hpicfDIPLDv6SourceBindingOutOfResourcesObjects':hpicfDIPLDv6SourceBindingOutOfResourcesObjects,_G:hpicfDIPLDv6SourceBindingAddrPort,_H:hpicfDIPLDv6SourceBindingAddrMacAddress,_I:hpicfDIPLDv6SourceBindingAddrIpAddressType,_J:hpicfDIPLDv6SourceBindingAddrIpAddress,_K:hpicfDIPLDv6SourceBindingAddrVlan,_e:hpicfDIPLDv6SourceBindingVoilations,'hpicfDIPLDv6SourceBindingVoilationsObjects':hpicfDIPLDv6SourceBindingVoilationsObjects,_L:hpicfDIPLDv6SourceBindingVoilationsCount,_M:hpicfDIPLDv6SourceBindingVoilationsPort,_N:hpicfDIPLDv6SourceBindingVoilationsSrcIpType,_O:hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress,_P:hpicfDIPLDv6SourceBindingVoilationsDstIpType,_Q:hpicfDIPLDv6SourceBindingVoilationsDstIpAddress,_R:hpicfDIPLDv6SourceBindingVoilationsMacAddress,_S:hpicfDIPLDv6SourceBindingVoilationsPktCount,'hpicfDIPLDv6Objects':hpicfDIPLDv6Objects,'hpicfDIPLDv6Config':hpicfDIPLDv6Config,_W:hpicfDIPLDv6LockEnable,'hpicfDIPLDv6PortTable':hpicfDIPLDv6PortTable,'hpicfDIPLDv6PortEntry':hpicfDIPLDv6PortEntry,_X:hpicfDIPLDv6PortEnable,_Y:hpicfDIPLDv6PortOperStatus,_b:hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl,_c:hpicfDIPLDv6SourceBindingViolationsTrapCtrl,'hpicfDIPLDv6Status':hpicfDIPLDv6Status,'hpicfDIPLDv6AddrTable':hpicfDIPLDv6AddrTable,_V:hpicfDIPLDv6AddrEntry,_Z:hpicfDIPLDv6AddrVlan,_a:hpicfDIPLDv6ResourceAvailable,'hpicfIpv6LockConformance':hpicfIpv6LockConformance,'hpicfIpv6LockGroups':hpicfIpv6LockGroups,_f:hpicfIpv6LockBaseGroup,_g:hpicfSourceBindingTrapObjectsGroup,_h:hpicfSourceBindingTrapsGroup,'hpicfIpv6LockCompliances':hpicfIpv6LockCompliances,'hpicfDIPLDv6Compliance':hpicfDIPLDv6Compliance,'hpicfIpv6SourceBindingTrapCompliance':hpicfIpv6SourceBindingTrapCompliance})