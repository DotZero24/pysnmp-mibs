_S='ciscoPimNotificationObjectGroup'
_R='ciscoPimSparseMIBGroup'
_Q='cpimLastErrorType'
_P='pimRPSetHoldTime'
_O='cpimRPMappingChangeType'
_N='cpimInvalidJoinPruneMsgsRcvd'
_M='cpimInvalidRegisterMsgsRcvd'
_L='Integer32'
_K='pimInterfaceStatus'
_J='cpimLastErrorRP'
_I='cpimLastErrorRPType'
_H='cpimLastErrorGroup'
_G='cpimLastErrorGroupType'
_F='cpimLastErrorOrigin'
_E='cpimLastErrorOriginType'
_D='PIM-MIB'
_C='read-only'
_B='current'
_A='CISCO-PIM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
pimInterfaceStatus,pimRPSetHoldTime=mibBuilder.importSymbols(_D,_K,_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoPimMIB=ModuleIdentity((1,3,6,1,4,1,9,9,184))
if mibBuilder.loadTexts:ciscoPimMIB.setRevisions(('2000-11-02 00:00',))
_CiscoPimMIBObjects_ObjectIdentity=ObjectIdentity
ciscoPimMIBObjects=_CiscoPimMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,184,1))
_Cpim_ObjectIdentity=ObjectIdentity
cpim=_Cpim_ObjectIdentity((1,3,6,1,4,1,9,9,184,1,1))
_CpimInvalidRegisterMsgsRcvd_Type=Counter32
_CpimInvalidRegisterMsgsRcvd_Object=MibScalar
cpimInvalidRegisterMsgsRcvd=_CpimInvalidRegisterMsgsRcvd_Object((1,3,6,1,4,1,9,9,184,1,1,1),_CpimInvalidRegisterMsgsRcvd_Type())
cpimInvalidRegisterMsgsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimInvalidRegisterMsgsRcvd.setStatus(_B)
_CpimInvalidJoinPruneMsgsRcvd_Type=Counter32
_CpimInvalidJoinPruneMsgsRcvd_Object=MibScalar
cpimInvalidJoinPruneMsgsRcvd=_CpimInvalidJoinPruneMsgsRcvd_Object((1,3,6,1,4,1,9,9,184,1,1,2),_CpimInvalidJoinPruneMsgsRcvd_Type())
cpimInvalidJoinPruneMsgsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimInvalidJoinPruneMsgsRcvd.setStatus(_B)
class _CpimLastErrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('invalidRegister',2),('invalidJoinPrune',3)))
_CpimLastErrorType_Type.__name__=_L
_CpimLastErrorType_Object=MibScalar
cpimLastErrorType=_CpimLastErrorType_Object((1,3,6,1,4,1,9,9,184,1,1,3),_CpimLastErrorType_Type())
cpimLastErrorType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimLastErrorType.setStatus(_B)
_CpimLastErrorOriginType_Type=InetAddressType
_CpimLastErrorOriginType_Object=MibScalar
cpimLastErrorOriginType=_CpimLastErrorOriginType_Object((1,3,6,1,4,1,9,9,184,1,1,4),_CpimLastErrorOriginType_Type())
cpimLastErrorOriginType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimLastErrorOriginType.setStatus(_B)
_CpimLastErrorOrigin_Type=InetAddress
_CpimLastErrorOrigin_Object=MibScalar
cpimLastErrorOrigin=_CpimLastErrorOrigin_Object((1,3,6,1,4,1,9,9,184,1,1,5),_CpimLastErrorOrigin_Type())
cpimLastErrorOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimLastErrorOrigin.setStatus(_B)
_CpimLastErrorGroupType_Type=InetAddressType
_CpimLastErrorGroupType_Object=MibScalar
cpimLastErrorGroupType=_CpimLastErrorGroupType_Object((1,3,6,1,4,1,9,9,184,1,1,6),_CpimLastErrorGroupType_Type())
cpimLastErrorGroupType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimLastErrorGroupType.setStatus(_B)
_CpimLastErrorGroup_Type=InetAddress
_CpimLastErrorGroup_Object=MibScalar
cpimLastErrorGroup=_CpimLastErrorGroup_Object((1,3,6,1,4,1,9,9,184,1,1,7),_CpimLastErrorGroup_Type())
cpimLastErrorGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimLastErrorGroup.setStatus(_B)
_CpimLastErrorRPType_Type=InetAddressType
_CpimLastErrorRPType_Object=MibScalar
cpimLastErrorRPType=_CpimLastErrorRPType_Object((1,3,6,1,4,1,9,9,184,1,1,8),_CpimLastErrorRPType_Type())
cpimLastErrorRPType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimLastErrorRPType.setStatus(_B)
_CpimLastErrorRP_Type=InetAddress
_CpimLastErrorRP_Object=MibScalar
cpimLastErrorRP=_CpimLastErrorRP_Object((1,3,6,1,4,1,9,9,184,1,1,9),_CpimLastErrorRP_Type())
cpimLastErrorRP.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimLastErrorRP.setStatus(_B)
_CiscoPimMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoPimMIBNotificationPrefix=_CiscoPimMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,184,2))
_CiscoPimMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoPimMIBNotifications=_CiscoPimMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,184,2,0))
_CiscoPimMIBNotificationObjects_ObjectIdentity=ObjectIdentity
ciscoPimMIBNotificationObjects=_CiscoPimMIBNotificationObjects_ObjectIdentity((1,3,6,1,4,1,9,9,184,2,1))
class _CpimRPMappingChangeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('newMapping',1),('deletedMapping',2),('modifiedOldMapping',3),('modifiedNewMapping',4)))
_CpimRPMappingChangeType_Type.__name__=_L
_CpimRPMappingChangeType_Object=MibScalar
cpimRPMappingChangeType=_CpimRPMappingChangeType_Object((1,3,6,1,4,1,9,9,184,2,1,1),_CpimRPMappingChangeType_Type())
cpimRPMappingChangeType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpimRPMappingChangeType.setStatus(_B)
_CiscoPimMIBConformance_ObjectIdentity=ObjectIdentity
ciscoPimMIBConformance=_CiscoPimMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,184,3))
_CiscoPimMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoPimMIBCompliances=_CiscoPimMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,184,3,1))
_CiscoPimMIBGroups_ObjectIdentity=ObjectIdentity
ciscoPimMIBGroups=_CiscoPimMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,184,3,2))
ciscoPimSparseMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,184,3,2,1))
ciscoPimSparseMIBGroup.setObjects(*((_A,_M),(_A,_N),(_A,_Q),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:ciscoPimSparseMIBGroup.setStatus(_B)
ciscoPimNotificationObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,184,3,2,2))
ciscoPimNotificationObjectGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:ciscoPimNotificationObjectGroup.setStatus(_B)
ciscoPimInterfaceUp=NotificationType((1,3,6,1,4,1,9,9,184,2,0,1))
ciscoPimInterfaceUp.setObjects((_D,_K))
if mibBuilder.loadTexts:ciscoPimInterfaceUp.setStatus(_B)
ciscoPimInterfaceDown=NotificationType((1,3,6,1,4,1,9,9,184,2,0,2))
ciscoPimInterfaceDown.setObjects((_D,_K))
if mibBuilder.loadTexts:ciscoPimInterfaceDown.setStatus(_B)
ciscoPimRPMappingChange=NotificationType((1,3,6,1,4,1,9,9,184,2,0,3))
ciscoPimRPMappingChange.setObjects(*((_D,_P),(_A,_O)))
if mibBuilder.loadTexts:ciscoPimRPMappingChange.setStatus(_B)
ciscoPimInvalidRegister=NotificationType((1,3,6,1,4,1,9,9,184,2,0,4))
ciscoPimInvalidRegister.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_M)))
if mibBuilder.loadTexts:ciscoPimInvalidRegister.setStatus(_B)
ciscoPimInvalidJoinPrune=NotificationType((1,3,6,1,4,1,9,9,184,2,0,5))
ciscoPimInvalidJoinPrune.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_N)))
if mibBuilder.loadTexts:ciscoPimInvalidJoinPrune.setStatus(_B)
ciscoPimSparseMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,184,3,1,1))
ciscoPimSparseMIBCompliance.setObjects(*((_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoPimSparseMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoPimMIB':ciscoPimMIB,'ciscoPimMIBObjects':ciscoPimMIBObjects,'cpim':cpim,_M:cpimInvalidRegisterMsgsRcvd,_N:cpimInvalidJoinPruneMsgsRcvd,_Q:cpimLastErrorType,_E:cpimLastErrorOriginType,_F:cpimLastErrorOrigin,_G:cpimLastErrorGroupType,_H:cpimLastErrorGroup,_I:cpimLastErrorRPType,_J:cpimLastErrorRP,'ciscoPimMIBNotificationPrefix':ciscoPimMIBNotificationPrefix,'ciscoPimMIBNotifications':ciscoPimMIBNotifications,'ciscoPimInterfaceUp':ciscoPimInterfaceUp,'ciscoPimInterfaceDown':ciscoPimInterfaceDown,'ciscoPimRPMappingChange':ciscoPimRPMappingChange,'ciscoPimInvalidRegister':ciscoPimInvalidRegister,'ciscoPimInvalidJoinPrune':ciscoPimInvalidJoinPrune,'ciscoPimMIBNotificationObjects':ciscoPimMIBNotificationObjects,_O:cpimRPMappingChangeType,'ciscoPimMIBConformance':ciscoPimMIBConformance,'ciscoPimMIBCompliances':ciscoPimMIBCompliances,'ciscoPimSparseMIBCompliance':ciscoPimSparseMIBCompliance,'ciscoPimMIBGroups':ciscoPimMIBGroups,_R:ciscoPimSparseMIBGroup,_S:ciscoPimNotificationObjectGroup})