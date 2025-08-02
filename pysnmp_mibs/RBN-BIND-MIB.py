_Y='rbnBindConfigGroup2'
_X='rbnBindConfigGroup'
_W='rbnBindAuthDhcp'
_V='deprecated'
_U='rbnBindCircuit'
_T='rbnBindVpn'
_S='rbnBindPvcPort'
_R='rbnBindPvcSlot'
_Q='rbnBindMaxSessions'
_P='rbnBindAuthPapFirst'
_O='rbnBindAuthWait'
_N='rbnBindAuthPap'
_M='rbnBindAuthChap'
_L='rbnBindAcl'
_K='rbnBindServiceGrp'
_J='rbnBindAuthContext'
_I='rbnBindPassword'
_H='rbnBindContext'
_G='rbnBindName'
_F='rbnBindType'
_E='Unsigned32'
_D='SnmpAdminString'
_C='read-create'
_B='current'
_A='RBN-BIND-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
RbnCircuitHandle,RbnPort,RbnSlot=mibBuilder.importSymbols('RBN-TC','RbnCircuitHandle','RbnPort','RbnSlot')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rbnBindMib=ModuleIdentity((1,3,6,1,4,1,2352,2,17))
if mibBuilder.loadTexts:rbnBindMib.setRevisions(('2003-10-13 17:00','2003-03-07 17:00','2002-11-13 00:00','2002-07-25 17:00','2002-01-07 17:00'))
class RbnBindType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('unbound',1),('authBind',2),('bypassBind',3),('interfaceBind',4),('subscriberBind',5),('l2tptunnelBind',6),('sessionBind',7),('dot1qBind',8),('multiIntfBind',9),('multiSubBind',10),('multiClipsBind',11)))
_RbnBindMIBObjects_ObjectIdentity=ObjectIdentity
rbnBindMIBObjects=_RbnBindMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,17,1))
_RbnBindTable_Object=MibTable
rbnBindTable=_RbnBindTable_Object((1,3,6,1,4,1,2352,2,17,1,1))
if mibBuilder.loadTexts:rbnBindTable.setStatus(_B)
_RbnBindEntry_Object=MibTableRow
rbnBindEntry=_RbnBindEntry_Object((1,3,6,1,4,1,2352,2,17,1,1,1))
rbnBindEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:rbnBindEntry.setStatus(_B)
_RbnBindCircuit_Type=RbnCircuitHandle
_RbnBindCircuit_Object=MibTableColumn
rbnBindCircuit=_RbnBindCircuit_Object((1,3,6,1,4,1,2352,2,17,1,1,1,1),_RbnBindCircuit_Type())
rbnBindCircuit.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbnBindCircuit.setStatus(_B)
_RbnBindType_Type=RbnBindType
_RbnBindType_Object=MibTableColumn
rbnBindType=_RbnBindType_Object((1,3,6,1,4,1,2352,2,17,1,1,1,2),_RbnBindType_Type())
rbnBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindType.setStatus(_B)
class _RbnBindName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,192))
_RbnBindName_Type.__name__=_D
_RbnBindName_Object=MibTableColumn
rbnBindName=_RbnBindName_Object((1,3,6,1,4,1,2352,2,17,1,1,1,3),_RbnBindName_Type())
rbnBindName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindName.setStatus(_B)
class _RbnBindPassword_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RbnBindPassword_Type.__name__=_D
_RbnBindPassword_Object=MibTableColumn
rbnBindPassword=_RbnBindPassword_Object((1,3,6,1,4,1,2352,2,17,1,1,1,4),_RbnBindPassword_Type())
rbnBindPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindPassword.setStatus(_B)
class _RbnBindContext_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RbnBindContext_Type.__name__=_D
_RbnBindContext_Object=MibTableColumn
rbnBindContext=_RbnBindContext_Object((1,3,6,1,4,1,2352,2,17,1,1,1,5),_RbnBindContext_Type())
rbnBindContext.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindContext.setStatus(_B)
class _RbnBindAuthContext_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RbnBindAuthContext_Type.__name__=_D
_RbnBindAuthContext_Object=MibTableColumn
rbnBindAuthContext=_RbnBindAuthContext_Object((1,3,6,1,4,1,2352,2,17,1,1,1,6),_RbnBindAuthContext_Type())
rbnBindAuthContext.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindAuthContext.setStatus(_B)
class _RbnBindServiceGrp_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RbnBindServiceGrp_Type.__name__=_D
_RbnBindServiceGrp_Object=MibTableColumn
rbnBindServiceGrp=_RbnBindServiceGrp_Object((1,3,6,1,4,1,2352,2,17,1,1,1,7),_RbnBindServiceGrp_Type())
rbnBindServiceGrp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindServiceGrp.setStatus(_B)
class _RbnBindAcl_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RbnBindAcl_Type.__name__=_D
_RbnBindAcl_Object=MibTableColumn
rbnBindAcl=_RbnBindAcl_Object((1,3,6,1,4,1,2352,2,17,1,1,1,8),_RbnBindAcl_Type())
rbnBindAcl.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindAcl.setStatus(_B)
_RbnBindAuthChap_Type=TruthValue
_RbnBindAuthChap_Object=MibTableColumn
rbnBindAuthChap=_RbnBindAuthChap_Object((1,3,6,1,4,1,2352,2,17,1,1,1,9),_RbnBindAuthChap_Type())
rbnBindAuthChap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindAuthChap.setStatus(_B)
_RbnBindAuthPap_Type=TruthValue
_RbnBindAuthPap_Object=MibTableColumn
rbnBindAuthPap=_RbnBindAuthPap_Object((1,3,6,1,4,1,2352,2,17,1,1,1,10),_RbnBindAuthPap_Type())
rbnBindAuthPap.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindAuthPap.setStatus(_B)
_RbnBindAuthWait_Type=TruthValue
_RbnBindAuthWait_Object=MibTableColumn
rbnBindAuthWait=_RbnBindAuthWait_Object((1,3,6,1,4,1,2352,2,17,1,1,1,11),_RbnBindAuthWait_Type())
rbnBindAuthWait.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindAuthWait.setStatus(_B)
_RbnBindAuthPapFirst_Type=TruthValue
_RbnBindAuthPapFirst_Object=MibTableColumn
rbnBindAuthPapFirst=_RbnBindAuthPapFirst_Object((1,3,6,1,4,1,2352,2,17,1,1,1,12),_RbnBindAuthPapFirst_Type())
rbnBindAuthPapFirst.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindAuthPapFirst.setStatus(_B)
class _RbnBindMaxSessions_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RbnBindMaxSessions_Type.__name__=_E
_RbnBindMaxSessions_Object=MibTableColumn
rbnBindMaxSessions=_RbnBindMaxSessions_Object((1,3,6,1,4,1,2352,2,17,1,1,1,13),_RbnBindMaxSessions_Type())
rbnBindMaxSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindMaxSessions.setStatus(_B)
_RbnBindPvcSlot_Type=RbnSlot
_RbnBindPvcSlot_Object=MibTableColumn
rbnBindPvcSlot=_RbnBindPvcSlot_Object((1,3,6,1,4,1,2352,2,17,1,1,1,14),_RbnBindPvcSlot_Type())
rbnBindPvcSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindPvcSlot.setStatus(_B)
_RbnBindPvcPort_Type=RbnPort
_RbnBindPvcPort_Object=MibTableColumn
rbnBindPvcPort=_RbnBindPvcPort_Object((1,3,6,1,4,1,2352,2,17,1,1,1,15),_RbnBindPvcPort_Type())
rbnBindPvcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindPvcPort.setStatus(_B)
class _RbnBindVpn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_RbnBindVpn_Type.__name__=_E
_RbnBindVpn_Object=MibTableColumn
rbnBindVpn=_RbnBindVpn_Object((1,3,6,1,4,1,2352,2,17,1,1,1,16),_RbnBindVpn_Type())
rbnBindVpn.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindVpn.setStatus(_B)
_RbnBindAuthDhcp_Type=TruthValue
_RbnBindAuthDhcp_Object=MibTableColumn
rbnBindAuthDhcp=_RbnBindAuthDhcp_Object((1,3,6,1,4,1,2352,2,17,1,1,1,17),_RbnBindAuthDhcp_Type())
rbnBindAuthDhcp.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnBindAuthDhcp.setStatus(_B)
_RbnBindMIBConformance_ObjectIdentity=ObjectIdentity
rbnBindMIBConformance=_RbnBindMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,17,2))
_RbnBindCompliances_ObjectIdentity=ObjectIdentity
rbnBindCompliances=_RbnBindCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,17,2,1))
_RbnBindGroups_ObjectIdentity=ObjectIdentity
rbnBindGroups=_RbnBindGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,17,2,2))
_RbnBindMIBNotifications_ObjectIdentity=ObjectIdentity
rbnBindMIBNotifications=_RbnBindMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2352,2,17,3))
rbnBindConfigGroup=ObjectGroup((1,3,6,1,4,1,2352,2,17,2,2,1))
rbnBindConfigGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:rbnBindConfigGroup.setStatus(_V)
rbnBindConfigGroup2=ObjectGroup((1,3,6,1,4,1,2352,2,17,2,2,2))
rbnBindConfigGroup2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_W)))
if mibBuilder.loadTexts:rbnBindConfigGroup2.setStatus(_B)
rbnBindCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,17,2,1,1))
rbnBindCompliance.setObjects((_A,_X))
if mibBuilder.loadTexts:rbnBindCompliance.setStatus(_V)
rbnBindCompliance2=ModuleCompliance((1,3,6,1,4,1,2352,2,17,2,1,2))
rbnBindCompliance2.setObjects((_A,_Y))
if mibBuilder.loadTexts:rbnBindCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'RbnBindType':RbnBindType,'rbnBindMib':rbnBindMib,'rbnBindMIBObjects':rbnBindMIBObjects,'rbnBindTable':rbnBindTable,'rbnBindEntry':rbnBindEntry,_U:rbnBindCircuit,_F:rbnBindType,_G:rbnBindName,_I:rbnBindPassword,_H:rbnBindContext,_J:rbnBindAuthContext,_K:rbnBindServiceGrp,_L:rbnBindAcl,_M:rbnBindAuthChap,_N:rbnBindAuthPap,_O:rbnBindAuthWait,_P:rbnBindAuthPapFirst,_Q:rbnBindMaxSessions,_R:rbnBindPvcSlot,_S:rbnBindPvcPort,_T:rbnBindVpn,_W:rbnBindAuthDhcp,'rbnBindMIBConformance':rbnBindMIBConformance,'rbnBindCompliances':rbnBindCompliances,'rbnBindCompliance':rbnBindCompliance,'rbnBindCompliance2':rbnBindCompliance2,'rbnBindGroups':rbnBindGroups,_X:rbnBindConfigGroup,_Y:rbnBindConfigGroup2,'rbnBindMIBNotifications':rbnBindMIBNotifications})