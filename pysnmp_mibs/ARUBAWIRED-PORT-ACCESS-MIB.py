_W='arubaWiredPortAccessRoleGroup'
_V='arubaWiredPortAccessClientGroup'
_U='arubaWiredParVlanMode'
_T='arubaWiredParVlanId'
_S='arubaWiredParGatewayZone'
_R='arubaWiredParUbtGatewayClearpassRole'
_Q='arubaWiredParUbtGatewayRole'
_P='arubaWiredParOrigin'
_O='arubaWiredPacVlanId'
_N='arubaWiredPacAutzFailureReason'
_M='arubaWiredPacAuthState'
_L='arubaWiredPacOnboardedMethods'
_K='arubaWiredPacAppliedRoleType'
_J='arubaWiredPacAppliedRole'
_I='arubaWiredPacUserName'
_H='arubaWiredParName'
_G='arubaWiredPacMac'
_F='arubaWiredPacPortName'
_E='not-accessible'
_D='read-only'
_C='DisplayString'
_B='ARUBAWIRED-PORT-ACCESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','TextualConvention')
arubaWiredPortAccessMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,17))
if mibBuilder.loadTexts:arubaWiredPortAccessMIB.setRevisions(('2020-10-14 00:00','2021-02-17 00:00'))
_ArubaWiredPortAccessNotifications_ObjectIdentity=ObjectIdentity
arubaWiredPortAccessNotifications=_ArubaWiredPortAccessNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,17,0))
_ArubaWiredPortAccessObjects_ObjectIdentity=ObjectIdentity
arubaWiredPortAccessObjects=_ArubaWiredPortAccessObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,17,1))
_ArubaWiredPortAccessClientTable_Object=MibTable
arubaWiredPortAccessClientTable=_ArubaWiredPortAccessClientTable_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1))
if mibBuilder.loadTexts:arubaWiredPortAccessClientTable.setStatus(_A)
_ArubaWiredPortAccessClientEntry_Object=MibTableRow
arubaWiredPortAccessClientEntry=_ArubaWiredPortAccessClientEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1))
arubaWiredPortAccessClientEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:arubaWiredPortAccessClientEntry.setStatus(_A)
class _ArubaWiredPacPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_ArubaWiredPacPortName_Type.__name__=_C
_ArubaWiredPacPortName_Object=MibTableColumn
arubaWiredPacPortName=_ArubaWiredPacPortName_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1,1),_ArubaWiredPacPortName_Type())
arubaWiredPacPortName.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredPacPortName.setStatus(_A)
_ArubaWiredPacMac_Type=MacAddress
_ArubaWiredPacMac_Object=MibTableColumn
arubaWiredPacMac=_ArubaWiredPacMac_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1,2),_ArubaWiredPacMac_Type())
arubaWiredPacMac.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredPacMac.setStatus(_A)
class _ArubaWiredPacUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArubaWiredPacUserName_Type.__name__=_C
_ArubaWiredPacUserName_Object=MibTableColumn
arubaWiredPacUserName=_ArubaWiredPacUserName_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1,3),_ArubaWiredPacUserName_Type())
arubaWiredPacUserName.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPacUserName.setStatus(_A)
class _ArubaWiredPacAppliedRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArubaWiredPacAppliedRole_Type.__name__=_C
_ArubaWiredPacAppliedRole_Object=MibTableColumn
arubaWiredPacAppliedRole=_ArubaWiredPacAppliedRole_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1,4),_ArubaWiredPacAppliedRole_Type())
arubaWiredPacAppliedRole.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPacAppliedRole.setStatus(_A)
class _ArubaWiredPacAppliedRoleType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArubaWiredPacAppliedRoleType_Type.__name__=_C
_ArubaWiredPacAppliedRoleType_Object=MibTableColumn
arubaWiredPacAppliedRoleType=_ArubaWiredPacAppliedRoleType_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1,5),_ArubaWiredPacAppliedRoleType_Type())
arubaWiredPacAppliedRoleType.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPacAppliedRoleType.setStatus(_A)
class _ArubaWiredPacOnboardedMethods_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_ArubaWiredPacOnboardedMethods_Type.__name__=_C
_ArubaWiredPacOnboardedMethods_Object=MibTableColumn
arubaWiredPacOnboardedMethods=_ArubaWiredPacOnboardedMethods_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1,6),_ArubaWiredPacOnboardedMethods_Type())
arubaWiredPacOnboardedMethods.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPacOnboardedMethods.setStatus(_A)
class _ArubaWiredPacAuthState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ArubaWiredPacAuthState_Type.__name__=_C
_ArubaWiredPacAuthState_Object=MibTableColumn
arubaWiredPacAuthState=_ArubaWiredPacAuthState_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1,7),_ArubaWiredPacAuthState_Type())
arubaWiredPacAuthState.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPacAuthState.setStatus(_A)
class _ArubaWiredPacAutzFailureReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_ArubaWiredPacAutzFailureReason_Type.__name__=_C
_ArubaWiredPacAutzFailureReason_Object=MibTableColumn
arubaWiredPacAutzFailureReason=_ArubaWiredPacAutzFailureReason_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1,8),_ArubaWiredPacAutzFailureReason_Type())
arubaWiredPacAutzFailureReason.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPacAutzFailureReason.setStatus(_A)
_ArubaWiredPacVlanId_Type=Integer32
_ArubaWiredPacVlanId_Object=MibTableColumn
arubaWiredPacVlanId=_ArubaWiredPacVlanId_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,1,1,9),_ArubaWiredPacVlanId_Type())
arubaWiredPacVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredPacVlanId.setStatus(_A)
_ArubaWiredPortAccessRoleTable_Object=MibTable
arubaWiredPortAccessRoleTable=_ArubaWiredPortAccessRoleTable_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,2))
if mibBuilder.loadTexts:arubaWiredPortAccessRoleTable.setStatus(_A)
_ArubaWiredPortAccessRoleEntry_Object=MibTableRow
arubaWiredPortAccessRoleEntry=_ArubaWiredPortAccessRoleEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,2,1))
arubaWiredPortAccessRoleEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:arubaWiredPortAccessRoleEntry.setStatus(_A)
class _ArubaWiredParName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,110))
_ArubaWiredParName_Type.__name__=_C
_ArubaWiredParName_Object=MibTableColumn
arubaWiredParName=_ArubaWiredParName_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,2,1,1),_ArubaWiredParName_Type())
arubaWiredParName.setMaxAccess(_E)
if mibBuilder.loadTexts:arubaWiredParName.setStatus(_A)
class _ArubaWiredParOrigin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArubaWiredParOrigin_Type.__name__=_C
_ArubaWiredParOrigin_Object=MibTableColumn
arubaWiredParOrigin=_ArubaWiredParOrigin_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,2,1,2),_ArubaWiredParOrigin_Type())
arubaWiredParOrigin.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredParOrigin.setStatus(_A)
class _ArubaWiredParUbtGatewayRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ArubaWiredParUbtGatewayRole_Type.__name__=_C
_ArubaWiredParUbtGatewayRole_Object=MibTableColumn
arubaWiredParUbtGatewayRole=_ArubaWiredParUbtGatewayRole_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,2,1,3),_ArubaWiredParUbtGatewayRole_Type())
arubaWiredParUbtGatewayRole.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredParUbtGatewayRole.setStatus(_A)
class _ArubaWiredParUbtGatewayClearpassRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArubaWiredParUbtGatewayClearpassRole_Type.__name__=_C
_ArubaWiredParUbtGatewayClearpassRole_Object=MibTableColumn
arubaWiredParUbtGatewayClearpassRole=_ArubaWiredParUbtGatewayClearpassRole_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,2,1,4),_ArubaWiredParUbtGatewayClearpassRole_Type())
arubaWiredParUbtGatewayClearpassRole.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredParUbtGatewayClearpassRole.setStatus(_A)
class _ArubaWiredParGatewayZone_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ArubaWiredParGatewayZone_Type.__name__=_C
_ArubaWiredParGatewayZone_Object=MibTableColumn
arubaWiredParGatewayZone=_ArubaWiredParGatewayZone_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,2,1,5),_ArubaWiredParGatewayZone_Type())
arubaWiredParGatewayZone.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredParGatewayZone.setStatus(_A)
_ArubaWiredParVlanId_Type=Integer32
_ArubaWiredParVlanId_Object=MibTableColumn
arubaWiredParVlanId=_ArubaWiredParVlanId_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,2,1,6),_ArubaWiredParVlanId_Type())
arubaWiredParVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredParVlanId.setStatus(_A)
class _ArubaWiredParVlanMode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ArubaWiredParVlanMode_Type.__name__=_C
_ArubaWiredParVlanMode_Object=MibTableColumn
arubaWiredParVlanMode=_ArubaWiredParVlanMode_Object((1,3,6,1,4,1,47196,4,1,1,3,17,1,2,1,7),_ArubaWiredParVlanMode_Type())
arubaWiredParVlanMode.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredParVlanMode.setStatus(_A)
_ArubaWiredPortAccessConformance_ObjectIdentity=ObjectIdentity
arubaWiredPortAccessConformance=_ArubaWiredPortAccessConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,17,2))
_ArubaWiredPortAccessGroups_ObjectIdentity=ObjectIdentity
arubaWiredPortAccessGroups=_ArubaWiredPortAccessGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,17,2,1))
_ArubaWiredPortAccessCompliances_ObjectIdentity=ObjectIdentity
arubaWiredPortAccessCompliances=_ArubaWiredPortAccessCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,17,2,2))
arubaWiredPortAccessClientGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,17,2,1,1))
arubaWiredPortAccessClientGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:arubaWiredPortAccessClientGroup.setStatus(_A)
arubaWiredPortAccessRoleGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,17,2,1,2))
arubaWiredPortAccessRoleGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:arubaWiredPortAccessRoleGroup.setStatus(_A)
arubaWiredPortAccessCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,17,2,2,1))
arubaWiredPortAccessCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:arubaWiredPortAccessCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'arubaWiredPortAccessMIB':arubaWiredPortAccessMIB,'arubaWiredPortAccessNotifications':arubaWiredPortAccessNotifications,'arubaWiredPortAccessObjects':arubaWiredPortAccessObjects,'arubaWiredPortAccessClientTable':arubaWiredPortAccessClientTable,'arubaWiredPortAccessClientEntry':arubaWiredPortAccessClientEntry,_F:arubaWiredPacPortName,_G:arubaWiredPacMac,_I:arubaWiredPacUserName,_J:arubaWiredPacAppliedRole,_K:arubaWiredPacAppliedRoleType,_L:arubaWiredPacOnboardedMethods,_M:arubaWiredPacAuthState,_N:arubaWiredPacAutzFailureReason,_O:arubaWiredPacVlanId,'arubaWiredPortAccessRoleTable':arubaWiredPortAccessRoleTable,'arubaWiredPortAccessRoleEntry':arubaWiredPortAccessRoleEntry,_H:arubaWiredParName,_P:arubaWiredParOrigin,_Q:arubaWiredParUbtGatewayRole,_R:arubaWiredParUbtGatewayClearpassRole,_S:arubaWiredParGatewayZone,_T:arubaWiredParVlanId,_U:arubaWiredParVlanMode,'arubaWiredPortAccessConformance':arubaWiredPortAccessConformance,'arubaWiredPortAccessGroups':arubaWiredPortAccessGroups,_V:arubaWiredPortAccessClientGroup,_W:arubaWiredPortAccessRoleGroup,'arubaWiredPortAccessCompliances':arubaWiredPortAccessCompliances,'arubaWiredPortAccessCompliance':arubaWiredPortAccessCompliance})