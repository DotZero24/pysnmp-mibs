_v='charGroup'
_u='charSessStartTime'
_t='charSessConnectionId'
_s='charSessOutCharacters'
_r='charSessInCharacters'
_q='charSessOperOrigin'
_p='charSessProtocol'
_o='charSessState'
_n='charSessKill'
_m='charPortLowerIfIndex'
_l='charPortSessionIndex'
_k='charPortSessionNumber'
_j='charPortOutCharacters'
_i='charPortInCharacters'
_h='charPortOutFlowTypes'
_g='charPortInFlowTypes'
_f='charPortSessionMaximum'
_e='charPortAdminOrigin'
_d='charPortOutFlowState'
_c='charPortInFlowState'
_b='charPortLastChange'
_a='charPortOperStatus'
_Z='charPortAdminStatus'
_Y='charPortReset'
_X='charPortHardware'
_W='charPortType'
_V='charPortName'
_U='charNumber'
_T='network'
_S='deprecated'
_R='dsrDtr'
_Q='ctsRts'
_P='hardware'
_O='xonXoff'
_N='maintenance'
_M='execute'
_L='DisplayString'
_K='charSessIndex'
_J='charSessPortIndex'
_I='unknown'
_H='charPortIndex'
_G='OctetString'
_F='none'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CHARACTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2','transmission')
AutonomousType,DisplayString,InstancePointer,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_L,'InstancePointer','PhysAddress','TextualConvention')
char=ModuleIdentity((1,3,6,1,2,1,19))
class PortIndex(TextualConvention,Integer32):status=_A;displayHint='d'
_CharNumber_Type=Integer32
_CharNumber_Object=MibScalar
charNumber=_CharNumber_Object((1,3,6,1,2,1,19,1),_CharNumber_Type())
charNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:charNumber.setStatus(_A)
_CharPortTable_Object=MibTable
charPortTable=_CharPortTable_Object((1,3,6,1,2,1,19,2))
if mibBuilder.loadTexts:charPortTable.setStatus(_A)
_CharPortEntry_Object=MibTableRow
charPortEntry=_CharPortEntry_Object((1,3,6,1,2,1,19,2,1))
charPortEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:charPortEntry.setStatus(_A)
_CharPortIndex_Type=PortIndex
_CharPortIndex_Object=MibTableColumn
charPortIndex=_CharPortIndex_Object((1,3,6,1,2,1,19,2,1,1),_CharPortIndex_Type())
charPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortIndex.setStatus(_A)
class _CharPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CharPortName_Type.__name__=_L
_CharPortName_Object=MibTableColumn
charPortName=_CharPortName_Object((1,3,6,1,2,1,19,2,1,2),_CharPortName_Type())
charPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:charPortName.setStatus(_A)
class _CharPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('physical',1),('virtual',2)))
_CharPortType_Type.__name__=_D
_CharPortType_Object=MibTableColumn
charPortType=_CharPortType_Object((1,3,6,1,2,1,19,2,1,3),_CharPortType_Type())
charPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortType.setStatus(_A)
_CharPortHardware_Type=AutonomousType
_CharPortHardware_Object=MibTableColumn
charPortHardware=_CharPortHardware_Object((1,3,6,1,2,1,19,2,1,4),_CharPortHardware_Type())
charPortHardware.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortHardware.setStatus(_A)
class _CharPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ready',1),(_M,2)))
_CharPortReset_Type.__name__=_D
_CharPortReset_Object=MibTableColumn
charPortReset=_CharPortReset_Object((1,3,6,1,2,1,19,2,1,5),_CharPortReset_Type())
charPortReset.setMaxAccess(_E)
if mibBuilder.loadTexts:charPortReset.setStatus(_A)
class _CharPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('off',3),(_N,4)))
_CharPortAdminStatus_Type.__name__=_D
_CharPortAdminStatus_Object=MibTableColumn
charPortAdminStatus=_CharPortAdminStatus_Object((1,3,6,1,2,1,19,2,1,6),_CharPortAdminStatus_Type())
charPortAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:charPortAdminStatus.setStatus(_A)
class _CharPortOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('up',1),('down',2),(_N,3),('absent',4),('active',5)))
_CharPortOperStatus_Type.__name__=_D
_CharPortOperStatus_Object=MibTableColumn
charPortOperStatus=_CharPortOperStatus_Object((1,3,6,1,2,1,19,2,1,7),_CharPortOperStatus_Type())
charPortOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortOperStatus.setStatus(_A)
_CharPortLastChange_Type=TimeTicks
_CharPortLastChange_Object=MibTableColumn
charPortLastChange=_CharPortLastChange_Object((1,3,6,1,2,1,19,2,1,8),_CharPortLastChange_Type())
charPortLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortLastChange.setStatus(_A)
class _CharPortInFlowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_CharPortInFlowType_Type.__name__=_D
_CharPortInFlowType_Object=MibTableColumn
charPortInFlowType=_CharPortInFlowType_Object((1,3,6,1,2,1,19,2,1,9),_CharPortInFlowType_Type())
charPortInFlowType.setMaxAccess(_E)
if mibBuilder.loadTexts:charPortInFlowType.setStatus(_S)
class _CharPortOutFlowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_O,2),(_P,3),(_Q,4),(_R,5)))
_CharPortOutFlowType_Type.__name__=_D
_CharPortOutFlowType_Object=MibTableColumn
charPortOutFlowType=_CharPortOutFlowType_Object((1,3,6,1,2,1,19,2,1,10),_CharPortOutFlowType_Type())
charPortOutFlowType.setMaxAccess(_E)
if mibBuilder.loadTexts:charPortOutFlowType.setStatus(_S)
class _CharPortInFlowState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),('stop',3),('go',4)))
_CharPortInFlowState_Type.__name__=_D
_CharPortInFlowState_Object=MibTableColumn
charPortInFlowState=_CharPortInFlowState_Object((1,3,6,1,2,1,19,2,1,11),_CharPortInFlowState_Type())
charPortInFlowState.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortInFlowState.setStatus(_A)
class _CharPortOutFlowState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_I,2),('stop',3),('go',4)))
_CharPortOutFlowState_Type.__name__=_D
_CharPortOutFlowState_Object=MibTableColumn
charPortOutFlowState=_CharPortOutFlowState_Object((1,3,6,1,2,1,19,2,1,12),_CharPortOutFlowState_Type())
charPortOutFlowState.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortOutFlowState.setStatus(_A)
_CharPortInCharacters_Type=Counter32
_CharPortInCharacters_Object=MibTableColumn
charPortInCharacters=_CharPortInCharacters_Object((1,3,6,1,2,1,19,2,1,13),_CharPortInCharacters_Type())
charPortInCharacters.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortInCharacters.setStatus(_A)
_CharPortOutCharacters_Type=Counter32
_CharPortOutCharacters_Object=MibTableColumn
charPortOutCharacters=_CharPortOutCharacters_Object((1,3,6,1,2,1,19,2,1,14),_CharPortOutCharacters_Type())
charPortOutCharacters.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortOutCharacters.setStatus(_A)
class _CharPortAdminOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dynamic',1),(_T,2),('local',3),(_F,4)))
_CharPortAdminOrigin_Type.__name__=_D
_CharPortAdminOrigin_Object=MibTableColumn
charPortAdminOrigin=_CharPortAdminOrigin_Object((1,3,6,1,2,1,19,2,1,15),_CharPortAdminOrigin_Type())
charPortAdminOrigin.setMaxAccess(_E)
if mibBuilder.loadTexts:charPortAdminOrigin.setStatus(_A)
class _CharPortSessionMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CharPortSessionMaximum_Type.__name__=_D
_CharPortSessionMaximum_Object=MibTableColumn
charPortSessionMaximum=_CharPortSessionMaximum_Object((1,3,6,1,2,1,19,2,1,16),_CharPortSessionMaximum_Type())
charPortSessionMaximum.setMaxAccess(_E)
if mibBuilder.loadTexts:charPortSessionMaximum.setStatus(_A)
_CharPortSessionNumber_Type=Gauge32
_CharPortSessionNumber_Object=MibTableColumn
charPortSessionNumber=_CharPortSessionNumber_Object((1,3,6,1,2,1,19,2,1,17),_CharPortSessionNumber_Type())
charPortSessionNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortSessionNumber.setStatus(_A)
class _CharPortSessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CharPortSessionIndex_Type.__name__=_D
_CharPortSessionIndex_Object=MibTableColumn
charPortSessionIndex=_CharPortSessionIndex_Object((1,3,6,1,2,1,19,2,1,18),_CharPortSessionIndex_Type())
charPortSessionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortSessionIndex.setStatus(_A)
class _CharPortInFlowTypes_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CharPortInFlowTypes_Type.__name__=_G
_CharPortInFlowTypes_Object=MibTableColumn
charPortInFlowTypes=_CharPortInFlowTypes_Object((1,3,6,1,2,1,19,2,1,19),_CharPortInFlowTypes_Type())
charPortInFlowTypes.setMaxAccess(_E)
if mibBuilder.loadTexts:charPortInFlowTypes.setStatus(_A)
class _CharPortOutFlowTypes_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_CharPortOutFlowTypes_Type.__name__=_G
_CharPortOutFlowTypes_Object=MibTableColumn
charPortOutFlowTypes=_CharPortOutFlowTypes_Object((1,3,6,1,2,1,19,2,1,20),_CharPortOutFlowTypes_Type())
charPortOutFlowTypes.setMaxAccess(_E)
if mibBuilder.loadTexts:charPortOutFlowTypes.setStatus(_A)
_CharPortLowerIfIndex_Type=InterfaceIndex
_CharPortLowerIfIndex_Object=MibTableColumn
charPortLowerIfIndex=_CharPortLowerIfIndex_Object((1,3,6,1,2,1,19,2,1,21),_CharPortLowerIfIndex_Type())
charPortLowerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:charPortLowerIfIndex.setStatus(_A)
_CharSessTable_Object=MibTable
charSessTable=_CharSessTable_Object((1,3,6,1,2,1,19,3))
if mibBuilder.loadTexts:charSessTable.setStatus(_A)
_CharSessEntry_Object=MibTableRow
charSessEntry=_CharSessEntry_Object((1,3,6,1,2,1,19,3,1))
charSessEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:charSessEntry.setStatus(_A)
_CharSessPortIndex_Type=PortIndex
_CharSessPortIndex_Object=MibTableColumn
charSessPortIndex=_CharSessPortIndex_Object((1,3,6,1,2,1,19,3,1,1),_CharSessPortIndex_Type())
charSessPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:charSessPortIndex.setStatus(_A)
class _CharSessIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CharSessIndex_Type.__name__=_D
_CharSessIndex_Object=MibTableColumn
charSessIndex=_CharSessIndex_Object((1,3,6,1,2,1,19,3,1,2),_CharSessIndex_Type())
charSessIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:charSessIndex.setStatus(_A)
class _CharSessKill_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ready',1),(_M,2)))
_CharSessKill_Type.__name__=_D
_CharSessKill_Object=MibTableColumn
charSessKill=_CharSessKill_Object((1,3,6,1,2,1,19,3,1,3),_CharSessKill_Type())
charSessKill.setMaxAccess(_E)
if mibBuilder.loadTexts:charSessKill.setStatus(_A)
class _CharSessState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('connecting',1),('connected',2),('disconnecting',3)))
_CharSessState_Type.__name__=_D
_CharSessState_Object=MibTableColumn
charSessState=_CharSessState_Object((1,3,6,1,2,1,19,3,1,4),_CharSessState_Type())
charSessState.setMaxAccess(_C)
if mibBuilder.loadTexts:charSessState.setStatus(_A)
_CharSessProtocol_Type=AutonomousType
_CharSessProtocol_Object=MibTableColumn
charSessProtocol=_CharSessProtocol_Object((1,3,6,1,2,1,19,3,1,5),_CharSessProtocol_Type())
charSessProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:charSessProtocol.setStatus(_A)
class _CharSessOperOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_T,2),('local',3)))
_CharSessOperOrigin_Type.__name__=_D
_CharSessOperOrigin_Object=MibTableColumn
charSessOperOrigin=_CharSessOperOrigin_Object((1,3,6,1,2,1,19,3,1,6),_CharSessOperOrigin_Type())
charSessOperOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:charSessOperOrigin.setStatus(_A)
_CharSessInCharacters_Type=Counter32
_CharSessInCharacters_Object=MibTableColumn
charSessInCharacters=_CharSessInCharacters_Object((1,3,6,1,2,1,19,3,1,7),_CharSessInCharacters_Type())
charSessInCharacters.setMaxAccess(_C)
if mibBuilder.loadTexts:charSessInCharacters.setStatus(_A)
_CharSessOutCharacters_Type=Counter32
_CharSessOutCharacters_Object=MibTableColumn
charSessOutCharacters=_CharSessOutCharacters_Object((1,3,6,1,2,1,19,3,1,8),_CharSessOutCharacters_Type())
charSessOutCharacters.setMaxAccess(_C)
if mibBuilder.loadTexts:charSessOutCharacters.setStatus(_A)
_CharSessConnectionId_Type=InstancePointer
_CharSessConnectionId_Object=MibTableColumn
charSessConnectionId=_CharSessConnectionId_Object((1,3,6,1,2,1,19,3,1,9),_CharSessConnectionId_Type())
charSessConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:charSessConnectionId.setStatus(_A)
_CharSessStartTime_Type=TimeTicks
_CharSessStartTime_Object=MibTableColumn
charSessStartTime=_CharSessStartTime_Object((1,3,6,1,2,1,19,3,1,10),_CharSessStartTime_Type())
charSessStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:charSessStartTime.setStatus(_A)
_WellKnownProtocols_ObjectIdentity=ObjectIdentity
wellKnownProtocols=_WellKnownProtocols_ObjectIdentity((1,3,6,1,2,1,19,4))
_ProtocolOther_ObjectIdentity=ObjectIdentity
protocolOther=_ProtocolOther_ObjectIdentity((1,3,6,1,2,1,19,4,1))
_ProtocolTelnet_ObjectIdentity=ObjectIdentity
protocolTelnet=_ProtocolTelnet_ObjectIdentity((1,3,6,1,2,1,19,4,2))
_ProtocolRlogin_ObjectIdentity=ObjectIdentity
protocolRlogin=_ProtocolRlogin_ObjectIdentity((1,3,6,1,2,1,19,4,3))
_ProtocolLat_ObjectIdentity=ObjectIdentity
protocolLat=_ProtocolLat_ObjectIdentity((1,3,6,1,2,1,19,4,4))
_ProtocolX29_ObjectIdentity=ObjectIdentity
protocolX29=_ProtocolX29_ObjectIdentity((1,3,6,1,2,1,19,4,5))
_ProtocolVtp_ObjectIdentity=ObjectIdentity
protocolVtp=_ProtocolVtp_ObjectIdentity((1,3,6,1,2,1,19,4,6))
_CharConformance_ObjectIdentity=ObjectIdentity
charConformance=_CharConformance_ObjectIdentity((1,3,6,1,2,1,19,5))
_CharGroups_ObjectIdentity=ObjectIdentity
charGroups=_CharGroups_ObjectIdentity((1,3,6,1,2,1,19,5,1))
_CharCompliances_ObjectIdentity=ObjectIdentity
charCompliances=_CharCompliances_ObjectIdentity((1,3,6,1,2,1,19,5,2))
charGroup=ObjectGroup((1,3,6,1,2,1,19,5,1,1))
charGroup.setObjects(*((_B,_U),(_B,_H),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_J),(_B,_K),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:charGroup.setStatus(_A)
charCompliance=ModuleCompliance((1,3,6,1,2,1,19,5,2,1))
charCompliance.setObjects((_B,_v))
if mibBuilder.loadTexts:charCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PortIndex':PortIndex,'char':char,_U:charNumber,'charPortTable':charPortTable,'charPortEntry':charPortEntry,_H:charPortIndex,_V:charPortName,_W:charPortType,_X:charPortHardware,_Y:charPortReset,_Z:charPortAdminStatus,_a:charPortOperStatus,_b:charPortLastChange,'charPortInFlowType':charPortInFlowType,'charPortOutFlowType':charPortOutFlowType,_c:charPortInFlowState,_d:charPortOutFlowState,_i:charPortInCharacters,_j:charPortOutCharacters,_e:charPortAdminOrigin,_f:charPortSessionMaximum,_k:charPortSessionNumber,_l:charPortSessionIndex,_g:charPortInFlowTypes,_h:charPortOutFlowTypes,_m:charPortLowerIfIndex,'charSessTable':charSessTable,'charSessEntry':charSessEntry,_J:charSessPortIndex,_K:charSessIndex,_n:charSessKill,_o:charSessState,_p:charSessProtocol,_q:charSessOperOrigin,_r:charSessInCharacters,_s:charSessOutCharacters,_t:charSessConnectionId,_u:charSessStartTime,'wellKnownProtocols':wellKnownProtocols,'protocolOther':protocolOther,'protocolTelnet':protocolTelnet,'protocolRlogin':protocolRlogin,'protocolLat':protocolLat,'protocolX29':protocolX29,'protocolVtp':protocolVtp,'charConformance':charConformance,'charGroups':charGroups,_v:charGroup,'charCompliances':charCompliances,'charCompliance':charCompliance})