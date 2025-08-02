_P='snMacAuthClearMacSessionMac'
_O='snMacAuthClearMacSessionIfIndex'
_N='snMacAuthMac'
_M='snMacAuthVlanId'
_L='snMacAuthIfIndex'
_K='snMacAuthClearIfCmdIfIndex'
_J='enabled'
_I='disabled'
_H='clear'
_G='valid'
_F='read-only'
_E='read-write'
_D='not-accessible'
_C='FOUNDRY-SN-MAC-AUTHENTICATION-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp')
snMacAuth=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,28))
if mibBuilder.loadTexts:snMacAuth.setRevisions(('2007-06-25 00:00','2017-08-07 00:00'))
_SnMacAuthGlobal_ObjectIdentity=ObjectIdentity
snMacAuthGlobal=_SnMacAuthGlobal_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,28,1))
class _SnMacAuthClearGlobalCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnMacAuthClearGlobalCmd_Type.__name__=_B
_SnMacAuthClearGlobalCmd_Object=MibScalar
snMacAuthClearGlobalCmd=_SnMacAuthClearGlobalCmd_Object((1,3,6,1,4,1,1991,1,1,3,28,1,1),_SnMacAuthClearGlobalCmd_Type())
snMacAuthClearGlobalCmd.setMaxAccess(_E)
if mibBuilder.loadTexts:snMacAuthClearGlobalCmd.setStatus(_A)
class _SnMacAuthGlobalConfigState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SnMacAuthGlobalConfigState_Type.__name__=_B
_SnMacAuthGlobalConfigState_Object=MibScalar
snMacAuthGlobalConfigState=_SnMacAuthGlobalConfigState_Object((1,3,6,1,4,1,1991,1,1,3,28,1,2),_SnMacAuthGlobalConfigState_Type())
snMacAuthGlobalConfigState.setMaxAccess(_E)
if mibBuilder.loadTexts:snMacAuthGlobalConfigState.setStatus(_A)
_SnMacAuthClearIfCmdTable_Object=MibTable
snMacAuthClearIfCmdTable=_SnMacAuthClearIfCmdTable_Object((1,3,6,1,4,1,1991,1,1,3,28,2))
if mibBuilder.loadTexts:snMacAuthClearIfCmdTable.setStatus(_A)
_SnMacAuthClearIfCmdEntry_Object=MibTableRow
snMacAuthClearIfCmdEntry=_SnMacAuthClearIfCmdEntry_Object((1,3,6,1,4,1,1991,1,1,3,28,2,1))
snMacAuthClearIfCmdEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:snMacAuthClearIfCmdEntry.setStatus(_A)
_SnMacAuthClearIfCmdIfIndex_Type=InterfaceIndex
_SnMacAuthClearIfCmdIfIndex_Object=MibTableColumn
snMacAuthClearIfCmdIfIndex=_SnMacAuthClearIfCmdIfIndex_Object((1,3,6,1,4,1,1991,1,1,3,28,2,1,1),_SnMacAuthClearIfCmdIfIndex_Type())
snMacAuthClearIfCmdIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snMacAuthClearIfCmdIfIndex.setStatus(_A)
class _SnMacAuthClearIfCmdAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnMacAuthClearIfCmdAction_Type.__name__=_B
_SnMacAuthClearIfCmdAction_Object=MibTableColumn
snMacAuthClearIfCmdAction=_SnMacAuthClearIfCmdAction_Object((1,3,6,1,4,1,1991,1,1,3,28,2,1,2),_SnMacAuthClearIfCmdAction_Type())
snMacAuthClearIfCmdAction.setMaxAccess(_E)
if mibBuilder.loadTexts:snMacAuthClearIfCmdAction.setStatus(_A)
_SnMacAuthTable_Object=MibTable
snMacAuthTable=_SnMacAuthTable_Object((1,3,6,1,4,1,1991,1,1,3,28,3))
if mibBuilder.loadTexts:snMacAuthTable.setStatus(_A)
_SnMacAuthEntry_Object=MibTableRow
snMacAuthEntry=_SnMacAuthEntry_Object((1,3,6,1,4,1,1991,1,1,3,28,3,1))
snMacAuthEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:snMacAuthEntry.setStatus(_A)
_SnMacAuthIfIndex_Type=InterfaceIndex
_SnMacAuthIfIndex_Object=MibTableColumn
snMacAuthIfIndex=_SnMacAuthIfIndex_Object((1,3,6,1,4,1,1991,1,1,3,28,3,1,1),_SnMacAuthIfIndex_Type())
snMacAuthIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snMacAuthIfIndex.setStatus(_A)
_SnMacAuthVlanId_Type=Integer32
_SnMacAuthVlanId_Object=MibTableColumn
snMacAuthVlanId=_SnMacAuthVlanId_Object((1,3,6,1,4,1,1991,1,1,3,28,3,1,2),_SnMacAuthVlanId_Type())
snMacAuthVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:snMacAuthVlanId.setStatus(_A)
_SnMacAuthMac_Type=MacAddress
_SnMacAuthMac_Object=MibTableColumn
snMacAuthMac=_SnMacAuthMac_Object((1,3,6,1,4,1,1991,1,1,3,28,3,1,3),_SnMacAuthMac_Type())
snMacAuthMac.setMaxAccess(_D)
if mibBuilder.loadTexts:snMacAuthMac.setStatus(_A)
class _SnMacAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authenticate',1),('unauthenticate',2)))
_SnMacAuthState_Type.__name__=_B
_SnMacAuthState_Object=MibTableColumn
snMacAuthState=_SnMacAuthState_Object((1,3,6,1,4,1,1991,1,1,3,28,3,1,4),_SnMacAuthState_Type())
snMacAuthState.setMaxAccess(_F)
if mibBuilder.loadTexts:snMacAuthState.setStatus(_A)
_SnMacAuthTimeStamp_Type=TimeStamp
_SnMacAuthTimeStamp_Object=MibTableColumn
snMacAuthTimeStamp=_SnMacAuthTimeStamp_Object((1,3,6,1,4,1,1991,1,1,3,28,3,1,5),_SnMacAuthTimeStamp_Type())
snMacAuthTimeStamp.setMaxAccess(_F)
if mibBuilder.loadTexts:snMacAuthTimeStamp.setStatus(_A)
_SnMacAuthAge_Type=Integer32
_SnMacAuthAge_Object=MibTableColumn
snMacAuthAge=_SnMacAuthAge_Object((1,3,6,1,4,1,1991,1,1,3,28,3,1,6),_SnMacAuthAge_Type())
snMacAuthAge.setMaxAccess(_F)
if mibBuilder.loadTexts:snMacAuthAge.setStatus(_A)
class _SnMacAuthDot1x_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SnMacAuthDot1x_Type.__name__=_B
_SnMacAuthDot1x_Object=MibTableColumn
snMacAuthDot1x=_SnMacAuthDot1x_Object((1,3,6,1,4,1,1991,1,1,3,28,3,1,7),_SnMacAuthDot1x_Type())
snMacAuthDot1x.setMaxAccess(_F)
if mibBuilder.loadTexts:snMacAuthDot1x.setStatus(_A)
_SnMacAuthClearMacSessionTable_Object=MibTable
snMacAuthClearMacSessionTable=_SnMacAuthClearMacSessionTable_Object((1,3,6,1,4,1,1991,1,1,3,28,4))
if mibBuilder.loadTexts:snMacAuthClearMacSessionTable.setStatus(_A)
_SnMacAuthClearMacSessionEntry_Object=MibTableRow
snMacAuthClearMacSessionEntry=_SnMacAuthClearMacSessionEntry_Object((1,3,6,1,4,1,1991,1,1,3,28,4,1))
snMacAuthClearMacSessionEntry.setIndexNames((0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:snMacAuthClearMacSessionEntry.setStatus(_A)
_SnMacAuthClearMacSessionIfIndex_Type=InterfaceIndex
_SnMacAuthClearMacSessionIfIndex_Object=MibTableColumn
snMacAuthClearMacSessionIfIndex=_SnMacAuthClearMacSessionIfIndex_Object((1,3,6,1,4,1,1991,1,1,3,28,4,1,1),_SnMacAuthClearMacSessionIfIndex_Type())
snMacAuthClearMacSessionIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:snMacAuthClearMacSessionIfIndex.setStatus(_A)
_SnMacAuthClearMacSessionMac_Type=MacAddress
_SnMacAuthClearMacSessionMac_Object=MibTableColumn
snMacAuthClearMacSessionMac=_SnMacAuthClearMacSessionMac_Object((1,3,6,1,4,1,1991,1,1,3,28,4,1,2),_SnMacAuthClearMacSessionMac_Type())
snMacAuthClearMacSessionMac.setMaxAccess(_D)
if mibBuilder.loadTexts:snMacAuthClearMacSessionMac.setStatus(_A)
class _SnMacAuthClearMacSessionAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_H,1)))
_SnMacAuthClearMacSessionAction_Type.__name__=_B
_SnMacAuthClearMacSessionAction_Object=MibTableColumn
snMacAuthClearMacSessionAction=_SnMacAuthClearMacSessionAction_Object((1,3,6,1,4,1,1991,1,1,3,28,4,1,3),_SnMacAuthClearMacSessionAction_Type())
snMacAuthClearMacSessionAction.setMaxAccess(_E)
if mibBuilder.loadTexts:snMacAuthClearMacSessionAction.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'snMacAuth':snMacAuth,'snMacAuthGlobal':snMacAuthGlobal,'snMacAuthClearGlobalCmd':snMacAuthClearGlobalCmd,'snMacAuthGlobalConfigState':snMacAuthGlobalConfigState,'snMacAuthClearIfCmdTable':snMacAuthClearIfCmdTable,'snMacAuthClearIfCmdEntry':snMacAuthClearIfCmdEntry,_K:snMacAuthClearIfCmdIfIndex,'snMacAuthClearIfCmdAction':snMacAuthClearIfCmdAction,'snMacAuthTable':snMacAuthTable,'snMacAuthEntry':snMacAuthEntry,_L:snMacAuthIfIndex,_M:snMacAuthVlanId,_N:snMacAuthMac,'snMacAuthState':snMacAuthState,'snMacAuthTimeStamp':snMacAuthTimeStamp,'snMacAuthAge':snMacAuthAge,'snMacAuthDot1x':snMacAuthDot1x,'snMacAuthClearMacSessionTable':snMacAuthClearMacSessionTable,'snMacAuthClearMacSessionEntry':snMacAuthClearMacSessionEntry,_O:snMacAuthClearMacSessionIfIndex,_P:snMacAuthClearMacSessionMac,'snMacAuthClearMacSessionAction':snMacAuthClearMacSessionAction})