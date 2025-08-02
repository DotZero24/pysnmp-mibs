_W='swMacBasedAuthDatabaseMacIndex'
_V='swMacBasedAuthPortIndex'
_U='swMacBasedAuthStateMacAddr'
_T='swMacBasedAuthStateOriginalVID'
_S='swMacBasedAuthStatePort'
_R='blocked'
_Q='authenticated'
_P='authenticating'
_O='read-create'
_N='not-accessible'
_M='swMacBasedAuthVID'
_L='other'
_K='swMacBasedAuthInfoMacIndex'
_J='swMacBasedAuthInfoPortIndex'
_I='start'
_H='DisplayString'
_G='enabled'
_F='disabled'
_E='read-only'
_D='Mac-Based-Authentication-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention')
swMBAMIB=ModuleIdentity((1,3,6,1,4,1,171,12,35))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwMBACtrl_ObjectIdentity=ObjectIdentity
swMBACtrl=_SwMBACtrl_ObjectIdentity((1,3,6,1,4,1,171,12,35,1))
class _SwMacBasedAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwMacBasedAuthState_Type.__name__=_B
_SwMacBasedAuthState_Object=MibScalar
swMacBasedAuthState=_SwMacBasedAuthState_Object((1,3,6,1,4,1,171,12,35,1,1),_SwMacBasedAuthState_Type())
swMacBasedAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthState.setStatus(_A)
class _SwMacBasedAuthMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('radius',2)))
_SwMacBasedAuthMethod_Type.__name__=_B
_SwMacBasedAuthMethod_Object=MibScalar
swMacBasedAuthMethod=_SwMacBasedAuthMethod_Object((1,3,6,1,4,1,171,12,35,1,2),_SwMacBasedAuthMethod_Type())
swMacBasedAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthMethod.setStatus(_A)
class _SwMacBasedAuthPWD_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SwMacBasedAuthPWD_Type.__name__=_H
_SwMacBasedAuthPWD_Object=MibScalar
swMacBasedAuthPWD=_SwMacBasedAuthPWD_Object((1,3,6,1,4,1,171,12,35,1,3),_SwMacBasedAuthPWD_Type())
swMacBasedAuthPWD.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthPWD.setStatus(_A)
class _SwMacBasedAuthVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwMacBasedAuthVlanName_Type.__name__=_H
_SwMacBasedAuthVlanName_Object=MibScalar
swMacBasedAuthVlanName=_SwMacBasedAuthVlanName_Object((1,3,6,1,4,1,171,12,35,1,4),_SwMacBasedAuthVlanName_Type())
swMacBasedAuthVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthVlanName.setStatus(_A)
_SwMacBasedAuthMemberPorts_Type=PortList
_SwMacBasedAuthMemberPorts_Object=MibScalar
swMacBasedAuthMemberPorts=_SwMacBasedAuthMemberPorts_Object((1,3,6,1,4,1,171,12,35,1,5),_SwMacBasedAuthMemberPorts_Type())
swMacBasedAuthMemberPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthMemberPorts.setStatus(_A)
class _SwMacBasedAuthVlanNameDelState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),(_I,2)))
_SwMacBasedAuthVlanNameDelState_Type.__name__=_B
_SwMacBasedAuthVlanNameDelState_Object=MibScalar
swMacBasedAuthVlanNameDelState=_SwMacBasedAuthVlanNameDelState_Object((1,3,6,1,4,1,171,12,35,1,7),_SwMacBasedAuthVlanNameDelState_Type())
swMacBasedAuthVlanNameDelState.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthVlanNameDelState.setStatus(_A)
class _SwMacBasedAuthClearAllAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_SwMacBasedAuthClearAllAction_Type.__name__=_B
_SwMacBasedAuthClearAllAction_Object=MibScalar
swMacBasedAuthClearAllAction=_SwMacBasedAuthClearAllAction_Object((1,3,6,1,4,1,171,12,35,1,8),_SwMacBasedAuthClearAllAction_Type())
swMacBasedAuthClearAllAction.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthClearAllAction.setStatus(_A)
class _SwMacBasedAuthMaxUser_Type(Integer32):defaultValue=128
_SwMacBasedAuthMaxUser_Type.__name__=_B
_SwMacBasedAuthMaxUser_Object=MibScalar
swMacBasedAuthMaxUser=_SwMacBasedAuthMaxUser_Object((1,3,6,1,4,1,171,12,35,1,9),_SwMacBasedAuthMaxUser_Type())
swMacBasedAuthMaxUser.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthMaxUser.setStatus(_A)
class _SwMacBasedAuthFailOver_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwMacBasedAuthFailOver_Type.__name__=_B
_SwMacBasedAuthFailOver_Object=MibScalar
swMacBasedAuthFailOver=_SwMacBasedAuthFailOver_Object((1,3,6,1,4,1,171,12,35,1,10),_SwMacBasedAuthFailOver_Type())
swMacBasedAuthFailOver.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthFailOver.setStatus(_A)
class _SwMacBasedAuthRadiusAuthorization_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwMacBasedAuthRadiusAuthorization_Type.__name__=_B
_SwMacBasedAuthRadiusAuthorization_Object=MibScalar
swMacBasedAuthRadiusAuthorization=_SwMacBasedAuthRadiusAuthorization_Object((1,3,6,1,4,1,171,12,35,1,11),_SwMacBasedAuthRadiusAuthorization_Type())
swMacBasedAuthRadiusAuthorization.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthRadiusAuthorization.setStatus(_A)
class _SwMacBasedAuthLocalAuthorization_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwMacBasedAuthLocalAuthorization_Type.__name__=_B
_SwMacBasedAuthLocalAuthorization_Object=MibScalar
swMacBasedAuthLocalAuthorization=_SwMacBasedAuthLocalAuthorization_Object((1,3,6,1,4,1,171,12,35,1,12),_SwMacBasedAuthLocalAuthorization_Type())
swMacBasedAuthLocalAuthorization.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthLocalAuthorization.setStatus(_A)
class _SwMacBasedAuthTrapState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwMacBasedAuthTrapState_Type.__name__=_B
_SwMacBasedAuthTrapState_Object=MibScalar
swMacBasedAuthTrapState=_SwMacBasedAuthTrapState_Object((1,3,6,1,4,1,171,12,35,1,13),_SwMacBasedAuthTrapState_Type())
swMacBasedAuthTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthTrapState.setStatus(_A)
class _SwMacBasedAuthLogState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwMacBasedAuthLogState_Type.__name__=_B
_SwMacBasedAuthLogState_Object=MibScalar
swMacBasedAuthLogState=_SwMacBasedAuthLogState_Object((1,3,6,1,4,1,171,12,35,1,14),_SwMacBasedAuthLogState_Type())
swMacBasedAuthLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthLogState.setStatus(_A)
class _SwMacBasedAuthPwdType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual_string',1),('client_mac_address',2)))
_SwMacBasedAuthPwdType_Type.__name__=_B
_SwMacBasedAuthPwdType_Object=MibScalar
swMacBasedAuthPwdType=_SwMacBasedAuthPwdType_Object((1,3,6,1,4,1,171,12,35,1,15),_SwMacBasedAuthPwdType_Type())
swMacBasedAuthPwdType.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthPwdType.setStatus(_A)
_SwMBAInfo_ObjectIdentity=ObjectIdentity
swMBAInfo=_SwMBAInfo_ObjectIdentity((1,3,6,1,4,1,171,12,35,2))
_SwMacBasedAuthPortInfoTable_Object=MibTable
swMacBasedAuthPortInfoTable=_SwMacBasedAuthPortInfoTable_Object((1,3,6,1,4,1,171,12,35,2,1))
if mibBuilder.loadTexts:swMacBasedAuthPortInfoTable.setStatus(_A)
_SwMacBasedAuthPortInfoEntry_Object=MibTableRow
swMacBasedAuthPortInfoEntry=_SwMacBasedAuthPortInfoEntry_Object((1,3,6,1,4,1,171,12,35,2,1,1))
swMacBasedAuthPortInfoEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:swMacBasedAuthPortInfoEntry.setStatus(_A)
_SwMacBasedAuthInfoPortIndex_Type=Integer32
_SwMacBasedAuthInfoPortIndex_Object=MibTableColumn
swMacBasedAuthInfoPortIndex=_SwMacBasedAuthInfoPortIndex_Object((1,3,6,1,4,1,171,12,35,2,1,1,1),_SwMacBasedAuthInfoPortIndex_Type())
swMacBasedAuthInfoPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthInfoPortIndex.setStatus(_A)
_SwMacBasedAuthInfoMacIndex_Type=MacAddress
_SwMacBasedAuthInfoMacIndex_Object=MibTableColumn
swMacBasedAuthInfoMacIndex=_SwMacBasedAuthInfoMacIndex_Object((1,3,6,1,4,1,171,12,35,2,1,1,2),_SwMacBasedAuthInfoMacIndex_Type())
swMacBasedAuthInfoMacIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthInfoMacIndex.setStatus(_A)
class _SwMacBasedAuthInfoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unconnected',1),('connecting',2),(_P,3),(_Q,4),(_R,5)))
_SwMacBasedAuthInfoStatus_Type.__name__=_B
_SwMacBasedAuthInfoStatus_Object=MibTableColumn
swMacBasedAuthInfoStatus=_SwMacBasedAuthInfoStatus_Object((1,3,6,1,4,1,171,12,35,2,1,1,3),_SwMacBasedAuthInfoStatus_Type())
swMacBasedAuthInfoStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthInfoStatus.setStatus(_A)
class _SwMacBasedAuthInfoAssignVLANName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwMacBasedAuthInfoAssignVLANName_Type.__name__=_H
_SwMacBasedAuthInfoAssignVLANName_Object=MibTableColumn
swMacBasedAuthInfoAssignVLANName=_SwMacBasedAuthInfoAssignVLANName_Object((1,3,6,1,4,1,171,12,35,2,1,1,4),_SwMacBasedAuthInfoAssignVLANName_Type())
swMacBasedAuthInfoAssignVLANName.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthInfoAssignVLANName.setStatus(_A)
class _SwMacBasedAuthClearMacAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_SwMacBasedAuthClearMacAction_Type.__name__=_B
_SwMacBasedAuthClearMacAction_Object=MibTableColumn
swMacBasedAuthClearMacAction=_SwMacBasedAuthClearMacAction_Object((1,3,6,1,4,1,171,12,35,2,1,1,5),_SwMacBasedAuthClearMacAction_Type())
swMacBasedAuthClearMacAction.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthClearMacAction.setStatus(_A)
_SwMacBasedAuthInfoPriority_Type=Integer32
_SwMacBasedAuthInfoPriority_Object=MibTableColumn
swMacBasedAuthInfoPriority=_SwMacBasedAuthInfoPriority_Object((1,3,6,1,4,1,171,12,35,2,1,1,6),_SwMacBasedAuthInfoPriority_Type())
swMacBasedAuthInfoPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthInfoPriority.setStatus(_A)
_SwMacBasedAuthInfoAgingTime_Type=Integer32
_SwMacBasedAuthInfoAgingTime_Object=MibTableColumn
swMacBasedAuthInfoAgingTime=_SwMacBasedAuthInfoAgingTime_Object((1,3,6,1,4,1,171,12,35,2,1,1,7),_SwMacBasedAuthInfoAgingTime_Type())
swMacBasedAuthInfoAgingTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthInfoAgingTime.setStatus(_A)
if mibBuilder.loadTexts:swMacBasedAuthInfoAgingTime.setUnits('minutes')
_SwMacBasedAuthInfoBlockTime_Type=Integer32
_SwMacBasedAuthInfoBlockTime_Object=MibTableColumn
swMacBasedAuthInfoBlockTime=_SwMacBasedAuthInfoBlockTime_Object((1,3,6,1,4,1,171,12,35,2,1,1,8),_SwMacBasedAuthInfoBlockTime_Type())
swMacBasedAuthInfoBlockTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthInfoBlockTime.setStatus(_A)
if mibBuilder.loadTexts:swMacBasedAuthInfoBlockTime.setUnits('seconds')
class _SwMacBasedAuthInfoAssignVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_SwMacBasedAuthInfoAssignVID_Type.__name__=_B
_SwMacBasedAuthInfoAssignVID_Object=MibTableColumn
swMacBasedAuthInfoAssignVID=_SwMacBasedAuthInfoAssignVID_Object((1,3,6,1,4,1,171,12,35,2,1,1,9),_SwMacBasedAuthInfoAssignVID_Type())
swMacBasedAuthInfoAssignVID.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthInfoAssignVID.setStatus(_A)
_SwMacBasedAuthStateTable_Object=MibTable
swMacBasedAuthStateTable=_SwMacBasedAuthStateTable_Object((1,3,6,1,4,1,171,12,35,2,2))
if mibBuilder.loadTexts:swMacBasedAuthStateTable.setStatus(_A)
_SwMacBasedAuthStateEntry_Object=MibTableRow
swMacBasedAuthStateEntry=_SwMacBasedAuthStateEntry_Object((1,3,6,1,4,1,171,12,35,2,2,1))
swMacBasedAuthStateEntry.setIndexNames((0,_D,_S),(0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:swMacBasedAuthStateEntry.setStatus(_A)
_SwMacBasedAuthStatePort_Type=Integer32
_SwMacBasedAuthStatePort_Object=MibTableColumn
swMacBasedAuthStatePort=_SwMacBasedAuthStatePort_Object((1,3,6,1,4,1,171,12,35,2,2,1,1),_SwMacBasedAuthStatePort_Type())
swMacBasedAuthStatePort.setMaxAccess(_N)
if mibBuilder.loadTexts:swMacBasedAuthStatePort.setStatus(_A)
_SwMacBasedAuthStateOriginalVID_Type=VlanId
_SwMacBasedAuthStateOriginalVID_Object=MibTableColumn
swMacBasedAuthStateOriginalVID=_SwMacBasedAuthStateOriginalVID_Object((1,3,6,1,4,1,171,12,35,2,2,1,2),_SwMacBasedAuthStateOriginalVID_Type())
swMacBasedAuthStateOriginalVID.setMaxAccess(_N)
if mibBuilder.loadTexts:swMacBasedAuthStateOriginalVID.setStatus(_A)
_SwMacBasedAuthStateMacAddr_Type=MacAddress
_SwMacBasedAuthStateMacAddr_Object=MibTableColumn
swMacBasedAuthStateMacAddr=_SwMacBasedAuthStateMacAddr_Object((1,3,6,1,4,1,171,12,35,2,2,1,3),_SwMacBasedAuthStateMacAddr_Type())
swMacBasedAuthStateMacAddr.setMaxAccess(_N)
if mibBuilder.loadTexts:swMacBasedAuthStateMacAddr.setStatus(_A)
class _SwMacBasedAuthStateAuthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_P,2),(_R,3)))
_SwMacBasedAuthStateAuthStatus_Type.__name__=_B
_SwMacBasedAuthStateAuthStatus_Object=MibTableColumn
swMacBasedAuthStateAuthStatus=_SwMacBasedAuthStateAuthStatus_Object((1,3,6,1,4,1,171,12,35,2,2,1,4),_SwMacBasedAuthStateAuthStatus_Type())
swMacBasedAuthStateAuthStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthStateAuthStatus.setStatus(_A)
_SwMacBasedAuthStateAssignVID_Type=VlanId
_SwMacBasedAuthStateAssignVID_Object=MibTableColumn
swMacBasedAuthStateAssignVID=_SwMacBasedAuthStateAssignVID_Object((1,3,6,1,4,1,171,12,35,2,2,1,5),_SwMacBasedAuthStateAssignVID_Type())
swMacBasedAuthStateAssignVID.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthStateAssignVID.setStatus(_A)
_SwMacBasedAuthStateAssignPriority_Type=Integer32
_SwMacBasedAuthStateAssignPriority_Object=MibTableColumn
swMacBasedAuthStateAssignPriority=_SwMacBasedAuthStateAssignPriority_Object((1,3,6,1,4,1,171,12,35,2,2,1,6),_SwMacBasedAuthStateAssignPriority_Type())
swMacBasedAuthStateAssignPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthStateAssignPriority.setStatus(_A)
_SwMacBasedAuthStateRemainTime_Type=Integer32
_SwMacBasedAuthStateRemainTime_Object=MibTableColumn
swMacBasedAuthStateRemainTime=_SwMacBasedAuthStateRemainTime_Object((1,3,6,1,4,1,171,12,35,2,2,1,7),_SwMacBasedAuthStateRemainTime_Type())
swMacBasedAuthStateRemainTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthStateRemainTime.setStatus(_A)
if mibBuilder.loadTexts:swMacBasedAuthStateRemainTime.setUnits('minutes/seconds')
class _SwMacBasedAuthStateDelAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_SwMacBasedAuthStateDelAction_Type.__name__=_B
_SwMacBasedAuthStateDelAction_Object=MibTableColumn
swMacBasedAuthStateDelAction=_SwMacBasedAuthStateDelAction_Object((1,3,6,1,4,1,171,12,35,2,2,1,25),_SwMacBasedAuthStateDelAction_Type())
swMacBasedAuthStateDelAction.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthStateDelAction.setStatus(_A)
_SwMBAPortMgmt_ObjectIdentity=ObjectIdentity
swMBAPortMgmt=_SwMBAPortMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,35,3))
_SwMacBasedAuthPortTable_Object=MibTable
swMacBasedAuthPortTable=_SwMacBasedAuthPortTable_Object((1,3,6,1,4,1,171,12,35,3,1))
if mibBuilder.loadTexts:swMacBasedAuthPortTable.setStatus(_A)
_SwMacBasedAuthPortEntry_Object=MibTableRow
swMacBasedAuthPortEntry=_SwMacBasedAuthPortEntry_Object((1,3,6,1,4,1,171,12,35,3,1,1))
swMacBasedAuthPortEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:swMacBasedAuthPortEntry.setStatus(_A)
class _SwMacBasedAuthPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwMacBasedAuthPortIndex_Type.__name__=_B
_SwMacBasedAuthPortIndex_Object=MibTableColumn
swMacBasedAuthPortIndex=_SwMacBasedAuthPortIndex_Object((1,3,6,1,4,1,171,12,35,3,1,1,1),_SwMacBasedAuthPortIndex_Type())
swMacBasedAuthPortIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthPortIndex.setStatus(_A)
class _SwMacBasedAuthPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwMacBasedAuthPortState_Type.__name__=_B
_SwMacBasedAuthPortState_Object=MibTableColumn
swMacBasedAuthPortState=_SwMacBasedAuthPortState_Object((1,3,6,1,4,1,171,12,35,3,1,1,2),_SwMacBasedAuthPortState_Type())
swMacBasedAuthPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthPortState.setStatus(_A)
class _SwMacBasedAuthPortMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port_based',1),('host_based',2)))
_SwMacBasedAuthPortMode_Type.__name__=_B
_SwMacBasedAuthPortMode_Object=MibTableColumn
swMacBasedAuthPortMode=_SwMacBasedAuthPortMode_Object((1,3,6,1,4,1,171,12,35,3,1,1,3),_SwMacBasedAuthPortMode_Type())
swMacBasedAuthPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthPortMode.setStatus(_A)
class _SwMacBasedAuthPortAgingTime_Type(Integer32):defaultValue=1440;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_SwMacBasedAuthPortAgingTime_Type.__name__=_B
_SwMacBasedAuthPortAgingTime_Object=MibTableColumn
swMacBasedAuthPortAgingTime=_SwMacBasedAuthPortAgingTime_Object((1,3,6,1,4,1,171,12,35,3,1,1,4),_SwMacBasedAuthPortAgingTime_Type())
swMacBasedAuthPortAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthPortAgingTime.setStatus(_A)
class _SwMacBasedAuthPortBlockTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_SwMacBasedAuthPortBlockTime_Type.__name__=_B
_SwMacBasedAuthPortBlockTime_Object=MibTableColumn
swMacBasedAuthPortBlockTime=_SwMacBasedAuthPortBlockTime_Object((1,3,6,1,4,1,171,12,35,3,1,1,5),_SwMacBasedAuthPortBlockTime_Type())
swMacBasedAuthPortBlockTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthPortBlockTime.setStatus(_A)
class _SwMacBasedAuthClearPortAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_I,2)))
_SwMacBasedAuthClearPortAction_Type.__name__=_B
_SwMacBasedAuthClearPortAction_Object=MibTableColumn
swMacBasedAuthClearPortAction=_SwMacBasedAuthClearPortAction_Object((1,3,6,1,4,1,171,12,35,3,1,1,6),_SwMacBasedAuthClearPortAction_Type())
swMacBasedAuthClearPortAction.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthClearPortAction.setStatus(_A)
class _SwMacBasedAuthPortMaxUser_Type(Integer32):defaultValue=128
_SwMacBasedAuthPortMaxUser_Type.__name__=_B
_SwMacBasedAuthPortMaxUser_Object=MibTableColumn
swMacBasedAuthPortMaxUser=_SwMacBasedAuthPortMaxUser_Object((1,3,6,1,4,1,171,12,35,3,1,1,7),_SwMacBasedAuthPortMaxUser_Type())
swMacBasedAuthPortMaxUser.setMaxAccess(_C)
if mibBuilder.loadTexts:swMacBasedAuthPortMaxUser.setStatus(_A)
_SwMBAMgmt_ObjectIdentity=ObjectIdentity
swMBAMgmt=_SwMBAMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,35,4))
_SwMacBasedAuthDatabaseTable_Object=MibTable
swMacBasedAuthDatabaseTable=_SwMacBasedAuthDatabaseTable_Object((1,3,6,1,4,1,171,12,35,4,1))
if mibBuilder.loadTexts:swMacBasedAuthDatabaseTable.setStatus(_A)
_SwMacBasedAuthDatabaseEntry_Object=MibTableRow
swMacBasedAuthDatabaseEntry=_SwMacBasedAuthDatabaseEntry_Object((1,3,6,1,4,1,171,12,35,4,1,1))
swMacBasedAuthDatabaseEntry.setIndexNames((0,_D,_W))
if mibBuilder.loadTexts:swMacBasedAuthDatabaseEntry.setStatus(_A)
_SwMacBasedAuthDatabaseMacIndex_Type=MacAddress
_SwMacBasedAuthDatabaseMacIndex_Object=MibTableColumn
swMacBasedAuthDatabaseMacIndex=_SwMacBasedAuthDatabaseMacIndex_Object((1,3,6,1,4,1,171,12,35,4,1,1,1),_SwMacBasedAuthDatabaseMacIndex_Type())
swMacBasedAuthDatabaseMacIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swMacBasedAuthDatabaseMacIndex.setStatus(_A)
class _SwMacBasedAuthDatabaseVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwMacBasedAuthDatabaseVlanName_Type.__name__=_H
_SwMacBasedAuthDatabaseVlanName_Object=MibTableColumn
swMacBasedAuthDatabaseVlanName=_SwMacBasedAuthDatabaseVlanName_Object((1,3,6,1,4,1,171,12,35,4,1,1,2),_SwMacBasedAuthDatabaseVlanName_Type())
swMacBasedAuthDatabaseVlanName.setMaxAccess(_O)
if mibBuilder.loadTexts:swMacBasedAuthDatabaseVlanName.setStatus('obsolete')
_SwMacBasedAuthDatabaseStatus_Type=RowStatus
_SwMacBasedAuthDatabaseStatus_Object=MibTableColumn
swMacBasedAuthDatabaseStatus=_SwMacBasedAuthDatabaseStatus_Object((1,3,6,1,4,1,171,12,35,4,1,1,3),_SwMacBasedAuthDatabaseStatus_Type())
swMacBasedAuthDatabaseStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:swMacBasedAuthDatabaseStatus.setStatus(_A)
class _SwMacBasedAuthDatabaseVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_SwMacBasedAuthDatabaseVID_Type.__name__=_B
_SwMacBasedAuthDatabaseVID_Object=MibTableColumn
swMacBasedAuthDatabaseVID=_SwMacBasedAuthDatabaseVID_Object((1,3,6,1,4,1,171,12,35,4,1,1,5),_SwMacBasedAuthDatabaseVID_Type())
swMacBasedAuthDatabaseVID.setMaxAccess(_O)
if mibBuilder.loadTexts:swMacBasedAuthDatabaseVID.setStatus(_A)
_SwMBATrap_ObjectIdentity=ObjectIdentity
swMBATrap=_SwMBATrap_ObjectIdentity((1,3,6,1,4,1,171,12,35,11))
_SwMBANotify_ObjectIdentity=ObjectIdentity
swMBANotify=_SwMBANotify_ObjectIdentity((1,3,6,1,4,1,171,12,35,11,1))
_SwMBANotifyPrefix_ObjectIdentity=ObjectIdentity
swMBANotifyPrefix=_SwMBANotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,35,11,1,0))
_SwMBANotifyBidings_ObjectIdentity=ObjectIdentity
swMBANotifyBidings=_SwMBANotifyBidings_ObjectIdentity((1,3,6,1,4,1,171,12,35,11,1,1))
_SwMacBasedAuthVID_Type=Integer32
_SwMacBasedAuthVID_Object=MibScalar
swMacBasedAuthVID=_SwMacBasedAuthVID_Object((1,3,6,1,4,1,171,12,35,11,1,1,1),_SwMacBasedAuthVID_Type())
swMacBasedAuthVID.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:swMacBasedAuthVID.setStatus(_A)
swMacBasedAccessControlLoggedSuccess=NotificationType((1,3,6,1,4,1,171,12,35,11,1,0,1))
swMacBasedAccessControlLoggedSuccess.setObjects(*((_D,_K),(_D,_J),(_D,_M)))
if mibBuilder.loadTexts:swMacBasedAccessControlLoggedSuccess.setStatus(_A)
swMacBasedAccessControlLoggedFail=NotificationType((1,3,6,1,4,1,171,12,35,11,1,0,2))
swMacBasedAccessControlLoggedFail.setObjects(*((_D,_K),(_D,_J),(_D,_M)))
if mibBuilder.loadTexts:swMacBasedAccessControlLoggedFail.setStatus(_A)
swMacBasedAccessControlAgesOut=NotificationType((1,3,6,1,4,1,171,12,35,11,1,0,3))
swMacBasedAccessControlAgesOut.setObjects(*((_D,_K),(_D,_J),(_D,_M)))
if mibBuilder.loadTexts:swMacBasedAccessControlAgesOut.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'PortList':PortList,'swMBAMIB':swMBAMIB,'swMBACtrl':swMBACtrl,'swMacBasedAuthState':swMacBasedAuthState,'swMacBasedAuthMethod':swMacBasedAuthMethod,'swMacBasedAuthPWD':swMacBasedAuthPWD,'swMacBasedAuthVlanName':swMacBasedAuthVlanName,'swMacBasedAuthMemberPorts':swMacBasedAuthMemberPorts,'swMacBasedAuthVlanNameDelState':swMacBasedAuthVlanNameDelState,'swMacBasedAuthClearAllAction':swMacBasedAuthClearAllAction,'swMacBasedAuthMaxUser':swMacBasedAuthMaxUser,'swMacBasedAuthFailOver':swMacBasedAuthFailOver,'swMacBasedAuthRadiusAuthorization':swMacBasedAuthRadiusAuthorization,'swMacBasedAuthLocalAuthorization':swMacBasedAuthLocalAuthorization,'swMacBasedAuthTrapState':swMacBasedAuthTrapState,'swMacBasedAuthLogState':swMacBasedAuthLogState,'swMacBasedAuthPwdType':swMacBasedAuthPwdType,'swMBAInfo':swMBAInfo,'swMacBasedAuthPortInfoTable':swMacBasedAuthPortInfoTable,'swMacBasedAuthPortInfoEntry':swMacBasedAuthPortInfoEntry,_J:swMacBasedAuthInfoPortIndex,_K:swMacBasedAuthInfoMacIndex,'swMacBasedAuthInfoStatus':swMacBasedAuthInfoStatus,'swMacBasedAuthInfoAssignVLANName':swMacBasedAuthInfoAssignVLANName,'swMacBasedAuthClearMacAction':swMacBasedAuthClearMacAction,'swMacBasedAuthInfoPriority':swMacBasedAuthInfoPriority,'swMacBasedAuthInfoAgingTime':swMacBasedAuthInfoAgingTime,'swMacBasedAuthInfoBlockTime':swMacBasedAuthInfoBlockTime,'swMacBasedAuthInfoAssignVID':swMacBasedAuthInfoAssignVID,'swMacBasedAuthStateTable':swMacBasedAuthStateTable,'swMacBasedAuthStateEntry':swMacBasedAuthStateEntry,_S:swMacBasedAuthStatePort,_T:swMacBasedAuthStateOriginalVID,_U:swMacBasedAuthStateMacAddr,'swMacBasedAuthStateAuthStatus':swMacBasedAuthStateAuthStatus,'swMacBasedAuthStateAssignVID':swMacBasedAuthStateAssignVID,'swMacBasedAuthStateAssignPriority':swMacBasedAuthStateAssignPriority,'swMacBasedAuthStateRemainTime':swMacBasedAuthStateRemainTime,'swMacBasedAuthStateDelAction':swMacBasedAuthStateDelAction,'swMBAPortMgmt':swMBAPortMgmt,'swMacBasedAuthPortTable':swMacBasedAuthPortTable,'swMacBasedAuthPortEntry':swMacBasedAuthPortEntry,_V:swMacBasedAuthPortIndex,'swMacBasedAuthPortState':swMacBasedAuthPortState,'swMacBasedAuthPortMode':swMacBasedAuthPortMode,'swMacBasedAuthPortAgingTime':swMacBasedAuthPortAgingTime,'swMacBasedAuthPortBlockTime':swMacBasedAuthPortBlockTime,'swMacBasedAuthClearPortAction':swMacBasedAuthClearPortAction,'swMacBasedAuthPortMaxUser':swMacBasedAuthPortMaxUser,'swMBAMgmt':swMBAMgmt,'swMacBasedAuthDatabaseTable':swMacBasedAuthDatabaseTable,'swMacBasedAuthDatabaseEntry':swMacBasedAuthDatabaseEntry,_W:swMacBasedAuthDatabaseMacIndex,'swMacBasedAuthDatabaseVlanName':swMacBasedAuthDatabaseVlanName,'swMacBasedAuthDatabaseStatus':swMacBasedAuthDatabaseStatus,'swMacBasedAuthDatabaseVID':swMacBasedAuthDatabaseVID,'swMBATrap':swMBATrap,'swMBANotify':swMBANotify,'swMBANotifyPrefix':swMBANotifyPrefix,'swMacBasedAccessControlLoggedSuccess':swMacBasedAccessControlLoggedSuccess,'swMacBasedAccessControlLoggedFail':swMacBasedAccessControlLoggedFail,'swMacBasedAccessControlAgesOut':swMacBasedAccessControlAgesOut,'swMBANotifyBidings':swMBANotifyBidings,_M:swMacBasedAuthVID})