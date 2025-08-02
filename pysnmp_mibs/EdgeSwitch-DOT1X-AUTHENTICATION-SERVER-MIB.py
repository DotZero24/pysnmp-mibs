_F='agentDot1xAuthServUserIndex'
_E='EdgeSwitch-DOT1X-AUTHENTICATION-SERVER-MIB'
_D='Integer32'
_C='read-write'
_B='DisplayString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('EdgeSwitch-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_B,'PhysAddress','RowStatus','TextualConvention')
fastPathdot1xAuthenticationServer=ModuleIdentity((1,3,6,1,4,1,4413,1,1,49))
if mibBuilder.loadTexts:fastPathdot1xAuthenticationServer.setRevisions(('2011-01-26 00:00','2009-11-12 00:00'))
_AgentDot1xAuthServUserConfigGroup_ObjectIdentity=ObjectIdentity
agentDot1xAuthServUserConfigGroup=_AgentDot1xAuthServUserConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,49,1))
class _AgentDot1xAuthServUserConfigCreate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AgentDot1xAuthServUserConfigCreate_Type.__name__=_B
_AgentDot1xAuthServUserConfigCreate_Object=MibScalar
agentDot1xAuthServUserConfigCreate=_AgentDot1xAuthServUserConfigCreate_Object((1,3,6,1,4,1,4413,1,1,49,1,1),_AgentDot1xAuthServUserConfigCreate_Type())
agentDot1xAuthServUserConfigCreate.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1xAuthServUserConfigCreate.setStatus(_A)
_AgentDot1xAuthServUserConfigTable_Object=MibTable
agentDot1xAuthServUserConfigTable=_AgentDot1xAuthServUserConfigTable_Object((1,3,6,1,4,1,4413,1,1,49,1,2))
if mibBuilder.loadTexts:agentDot1xAuthServUserConfigTable.setStatus(_A)
_AgentDot1xAuthServUserConfigEntry_Object=MibTableRow
agentDot1xAuthServUserConfigEntry=_AgentDot1xAuthServUserConfigEntry_Object((1,3,6,1,4,1,4413,1,1,49,1,2,1))
agentDot1xAuthServUserConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:agentDot1xAuthServUserConfigEntry.setStatus(_A)
class _AgentDot1xAuthServUserIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_AgentDot1xAuthServUserIndex_Type.__name__=_D
_AgentDot1xAuthServUserIndex_Object=MibTableColumn
agentDot1xAuthServUserIndex=_AgentDot1xAuthServUserIndex_Object((1,3,6,1,4,1,4413,1,1,49,1,2,1,1),_AgentDot1xAuthServUserIndex_Type())
agentDot1xAuthServUserIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentDot1xAuthServUserIndex.setStatus(_A)
class _AgentDot1xAuthServUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AgentDot1xAuthServUserName_Type.__name__=_B
_AgentDot1xAuthServUserName_Object=MibTableColumn
agentDot1xAuthServUserName=_AgentDot1xAuthServUserName_Object((1,3,6,1,4,1,4413,1,1,49,1,2,1,2),_AgentDot1xAuthServUserName_Type())
agentDot1xAuthServUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1xAuthServUserName.setStatus(_A)
class _AgentDot1xAuthServUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentDot1xAuthServUserPassword_Type.__name__=_B
_AgentDot1xAuthServUserPassword_Object=MibTableColumn
agentDot1xAuthServUserPassword=_AgentDot1xAuthServUserPassword_Object((1,3,6,1,4,1,4413,1,1,49,1,2,1,3),_AgentDot1xAuthServUserPassword_Type())
agentDot1xAuthServUserPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1xAuthServUserPassword.setStatus(_A)
_AgentDot1xAuthServUserStatus_Type=RowStatus
_AgentDot1xAuthServUserStatus_Object=MibTableColumn
agentDot1xAuthServUserStatus=_AgentDot1xAuthServUserStatus_Object((1,3,6,1,4,1,4413,1,1,49,1,2,1,4),_AgentDot1xAuthServUserStatus_Type())
agentDot1xAuthServUserStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1xAuthServUserStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fastPathdot1xAuthenticationServer':fastPathdot1xAuthenticationServer,'agentDot1xAuthServUserConfigGroup':agentDot1xAuthServUserConfigGroup,'agentDot1xAuthServUserConfigCreate':agentDot1xAuthServUserConfigCreate,'agentDot1xAuthServUserConfigTable':agentDot1xAuthServUserConfigTable,'agentDot1xAuthServUserConfigEntry':agentDot1xAuthServUserConfigEntry,_F:agentDot1xAuthServUserIndex,'agentDot1xAuthServUserName':agentDot1xAuthServUserName,'agentDot1xAuthServUserPassword':agentDot1xAuthServUserPassword,'agentDot1xAuthServUserStatus':agentDot1xAuthServUserStatus})