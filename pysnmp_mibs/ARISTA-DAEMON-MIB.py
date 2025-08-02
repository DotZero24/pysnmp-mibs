_O='aristaDaemonBaseGroup'
_N='aristaDaemonDataValue'
_M='aristaDaemonRunning'
_L='aristaDaemonOptionValue'
_K='aristaDaemonEnabled'
_J='aristaDaemonDataKey'
_I='aristaDaemonDataAgentName'
_H='aristaDaemonRunningAgentName'
_G='aristaDaemonOptionKey'
_F='aristaDaemonOptionAgentName'
_E='aristaDaemonEnabledAgentName'
_D='read-only'
_C='not-accessible'
_B='ARISTA-DAEMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
aristaDaemonMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,17))
if mibBuilder.loadTexts:aristaDaemonMIB.setRevisions(('2015-04-27 00:00',))
class AgentName(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class AgentAttributeKey(TextualConvention,OctetString):status=_A;displayHint='64a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
class AgentAttributeValue(TextualConvention,OctetString):status=_A;displayHint='10240a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10240))
_AristaDaemonConfig_ObjectIdentity=ObjectIdentity
aristaDaemonConfig=_AristaDaemonConfig_ObjectIdentity((1,3,6,1,4,1,30065,3,17,1))
_AristaDaemonEnabledTable_Object=MibTable
aristaDaemonEnabledTable=_AristaDaemonEnabledTable_Object((1,3,6,1,4,1,30065,3,17,1,1))
if mibBuilder.loadTexts:aristaDaemonEnabledTable.setStatus(_A)
_AristaDaemonEnabledEntry_Object=MibTableRow
aristaDaemonEnabledEntry=_AristaDaemonEnabledEntry_Object((1,3,6,1,4,1,30065,3,17,1,1,1))
aristaDaemonEnabledEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:aristaDaemonEnabledEntry.setStatus(_A)
_AristaDaemonEnabledAgentName_Type=AgentName
_AristaDaemonEnabledAgentName_Object=MibTableColumn
aristaDaemonEnabledAgentName=_AristaDaemonEnabledAgentName_Object((1,3,6,1,4,1,30065,3,17,1,1,1,1),_AristaDaemonEnabledAgentName_Type())
aristaDaemonEnabledAgentName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaDaemonEnabledAgentName.setStatus(_A)
_AristaDaemonEnabled_Type=TruthValue
_AristaDaemonEnabled_Object=MibTableColumn
aristaDaemonEnabled=_AristaDaemonEnabled_Object((1,3,6,1,4,1,30065,3,17,1,1,1,2),_AristaDaemonEnabled_Type())
aristaDaemonEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaDaemonEnabled.setStatus(_A)
_AristaDaemonOptionTable_Object=MibTable
aristaDaemonOptionTable=_AristaDaemonOptionTable_Object((1,3,6,1,4,1,30065,3,17,1,2))
if mibBuilder.loadTexts:aristaDaemonOptionTable.setStatus(_A)
_AristaDaemonOptionEntry_Object=MibTableRow
aristaDaemonOptionEntry=_AristaDaemonOptionEntry_Object((1,3,6,1,4,1,30065,3,17,1,2,1))
aristaDaemonOptionEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:aristaDaemonOptionEntry.setStatus(_A)
_AristaDaemonOptionAgentName_Type=AgentName
_AristaDaemonOptionAgentName_Object=MibTableColumn
aristaDaemonOptionAgentName=_AristaDaemonOptionAgentName_Object((1,3,6,1,4,1,30065,3,17,1,2,1,1),_AristaDaemonOptionAgentName_Type())
aristaDaemonOptionAgentName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaDaemonOptionAgentName.setStatus(_A)
_AristaDaemonOptionKey_Type=AgentAttributeKey
_AristaDaemonOptionKey_Object=MibTableColumn
aristaDaemonOptionKey=_AristaDaemonOptionKey_Object((1,3,6,1,4,1,30065,3,17,1,2,1,2),_AristaDaemonOptionKey_Type())
aristaDaemonOptionKey.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaDaemonOptionKey.setStatus(_A)
_AristaDaemonOptionValue_Type=AgentAttributeValue
_AristaDaemonOptionValue_Object=MibTableColumn
aristaDaemonOptionValue=_AristaDaemonOptionValue_Object((1,3,6,1,4,1,30065,3,17,1,2,1,3),_AristaDaemonOptionValue_Type())
aristaDaemonOptionValue.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaDaemonOptionValue.setStatus(_A)
_AristaDaemonStatus_ObjectIdentity=ObjectIdentity
aristaDaemonStatus=_AristaDaemonStatus_ObjectIdentity((1,3,6,1,4,1,30065,3,17,2))
_AristaDaemonRunningTable_Object=MibTable
aristaDaemonRunningTable=_AristaDaemonRunningTable_Object((1,3,6,1,4,1,30065,3,17,2,1))
if mibBuilder.loadTexts:aristaDaemonRunningTable.setStatus(_A)
_AristaDaemonRunningEntry_Object=MibTableRow
aristaDaemonRunningEntry=_AristaDaemonRunningEntry_Object((1,3,6,1,4,1,30065,3,17,2,1,1))
aristaDaemonRunningEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:aristaDaemonRunningEntry.setStatus(_A)
_AristaDaemonRunningAgentName_Type=AgentName
_AristaDaemonRunningAgentName_Object=MibTableColumn
aristaDaemonRunningAgentName=_AristaDaemonRunningAgentName_Object((1,3,6,1,4,1,30065,3,17,2,1,1,1),_AristaDaemonRunningAgentName_Type())
aristaDaemonRunningAgentName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaDaemonRunningAgentName.setStatus(_A)
_AristaDaemonRunning_Type=TruthValue
_AristaDaemonRunning_Object=MibTableColumn
aristaDaemonRunning=_AristaDaemonRunning_Object((1,3,6,1,4,1,30065,3,17,2,1,1,2),_AristaDaemonRunning_Type())
aristaDaemonRunning.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaDaemonRunning.setStatus(_A)
_AristaDaemonDataTable_Object=MibTable
aristaDaemonDataTable=_AristaDaemonDataTable_Object((1,3,6,1,4,1,30065,3,17,2,2))
if mibBuilder.loadTexts:aristaDaemonDataTable.setStatus(_A)
_AristaDaemonDataEntry_Object=MibTableRow
aristaDaemonDataEntry=_AristaDaemonDataEntry_Object((1,3,6,1,4,1,30065,3,17,2,2,1))
aristaDaemonDataEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:aristaDaemonDataEntry.setStatus(_A)
_AristaDaemonDataAgentName_Type=AgentName
_AristaDaemonDataAgentName_Object=MibTableColumn
aristaDaemonDataAgentName=_AristaDaemonDataAgentName_Object((1,3,6,1,4,1,30065,3,17,2,2,1,1),_AristaDaemonDataAgentName_Type())
aristaDaemonDataAgentName.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaDaemonDataAgentName.setStatus(_A)
_AristaDaemonDataKey_Type=AgentAttributeKey
_AristaDaemonDataKey_Object=MibTableColumn
aristaDaemonDataKey=_AristaDaemonDataKey_Object((1,3,6,1,4,1,30065,3,17,2,2,1,2),_AristaDaemonDataKey_Type())
aristaDaemonDataKey.setMaxAccess(_C)
if mibBuilder.loadTexts:aristaDaemonDataKey.setStatus(_A)
_AristaDaemonDataValue_Type=AgentAttributeValue
_AristaDaemonDataValue_Object=MibTableColumn
aristaDaemonDataValue=_AristaDaemonDataValue_Object((1,3,6,1,4,1,30065,3,17,2,2,1,3),_AristaDaemonDataValue_Type())
aristaDaemonDataValue.setMaxAccess(_D)
if mibBuilder.loadTexts:aristaDaemonDataValue.setStatus(_A)
_AristaDaemonConformance_ObjectIdentity=ObjectIdentity
aristaDaemonConformance=_AristaDaemonConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,17,3))
_AristaDaemonGroups_ObjectIdentity=ObjectIdentity
aristaDaemonGroups=_AristaDaemonGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,17,3,1))
_AristaDaemonCompliances_ObjectIdentity=ObjectIdentity
aristaDaemonCompliances=_AristaDaemonCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,17,3,2))
aristaDaemonBaseGroup=ObjectGroup((1,3,6,1,4,1,30065,3,17,3,1,1))
aristaDaemonBaseGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:aristaDaemonBaseGroup.setStatus(_A)
aristaDaemonCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,17,3,2,1))
aristaDaemonCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:aristaDaemonCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AgentName':AgentName,'AgentAttributeKey':AgentAttributeKey,'AgentAttributeValue':AgentAttributeValue,'aristaDaemonMIB':aristaDaemonMIB,'aristaDaemonConfig':aristaDaemonConfig,'aristaDaemonEnabledTable':aristaDaemonEnabledTable,'aristaDaemonEnabledEntry':aristaDaemonEnabledEntry,_E:aristaDaemonEnabledAgentName,_K:aristaDaemonEnabled,'aristaDaemonOptionTable':aristaDaemonOptionTable,'aristaDaemonOptionEntry':aristaDaemonOptionEntry,_F:aristaDaemonOptionAgentName,_G:aristaDaemonOptionKey,_L:aristaDaemonOptionValue,'aristaDaemonStatus':aristaDaemonStatus,'aristaDaemonRunningTable':aristaDaemonRunningTable,'aristaDaemonRunningEntry':aristaDaemonRunningEntry,_H:aristaDaemonRunningAgentName,_M:aristaDaemonRunning,'aristaDaemonDataTable':aristaDaemonDataTable,'aristaDaemonDataEntry':aristaDaemonDataEntry,_I:aristaDaemonDataAgentName,_J:aristaDaemonDataKey,_N:aristaDaemonDataValue,'aristaDaemonConformance':aristaDaemonConformance,'aristaDaemonGroups':aristaDaemonGroups,_O:aristaDaemonBaseGroup,'aristaDaemonCompliances':aristaDaemonCompliances,'aristaDaemonCompliance':aristaDaemonCompliance})