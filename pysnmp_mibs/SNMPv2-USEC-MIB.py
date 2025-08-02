_R='usecStatsGroup'
_Q='usecBasicGroup'
_P='usecStatsUnauthorizedOperations'
_O='usecStatsBadParameters'
_N='usecStatsUnknownContexts'
_M='usecStatsWrongDigestValues'
_L='usecStatsUnknownUserNames'
_K='usecStatsNotInWindows'
_J='usecStatsUnsupportedQoS'
_I='agentSize'
_H='agentTime'
_G='agentBoots'
_F='agentID'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='SNMPv2-USEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','snmpModules')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
usecMIB=ModuleIdentity((1,3,6,1,6,3,6))
class AgentID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_UsecMIBObjects_ObjectIdentity=ObjectIdentity
usecMIBObjects=_UsecMIBObjects_ObjectIdentity((1,3,6,1,6,3,6,1))
_UsecAgent_ObjectIdentity=ObjectIdentity
usecAgent=_UsecAgent_ObjectIdentity((1,3,6,1,6,3,6,1,1))
_AgentID_Type=AgentID
_AgentID_Object=MibScalar
agentID=_AgentID_Object((1,3,6,1,6,3,6,1,1,1),_AgentID_Type())
agentID.setMaxAccess(_C)
if mibBuilder.loadTexts:agentID.setStatus(_A)
_AgentBoots_Type=Unsigned32
_AgentBoots_Object=MibScalar
agentBoots=_AgentBoots_Object((1,3,6,1,6,3,6,1,1,2),_AgentBoots_Type())
agentBoots.setMaxAccess(_C)
if mibBuilder.loadTexts:agentBoots.setStatus(_A)
class _AgentTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentTime_Type.__name__=_E
_AgentTime_Object=MibScalar
agentTime=_AgentTime_Object((1,3,6,1,6,3,6,1,1,3),_AgentTime_Type())
agentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentTime.setStatus(_A)
if mibBuilder.loadTexts:agentTime.setUnits('seconds')
class _AgentSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(484,65507))
_AgentSize_Type.__name__=_D
_AgentSize_Object=MibScalar
agentSize=_AgentSize_Object((1,3,6,1,6,3,6,1,1,4),_AgentSize_Type())
agentSize.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSize.setStatus(_A)
_UsecStats_ObjectIdentity=ObjectIdentity
usecStats=_UsecStats_ObjectIdentity((1,3,6,1,6,3,6,1,2))
_UsecStatsUnsupportedQoS_Type=Counter32
_UsecStatsUnsupportedQoS_Object=MibScalar
usecStatsUnsupportedQoS=_UsecStatsUnsupportedQoS_Object((1,3,6,1,6,3,6,1,2,1),_UsecStatsUnsupportedQoS_Type())
usecStatsUnsupportedQoS.setMaxAccess(_C)
if mibBuilder.loadTexts:usecStatsUnsupportedQoS.setStatus(_A)
_UsecStatsNotInWindows_Type=Counter32
_UsecStatsNotInWindows_Object=MibScalar
usecStatsNotInWindows=_UsecStatsNotInWindows_Object((1,3,6,1,6,3,6,1,2,2),_UsecStatsNotInWindows_Type())
usecStatsNotInWindows.setMaxAccess(_C)
if mibBuilder.loadTexts:usecStatsNotInWindows.setStatus(_A)
_UsecStatsUnknownUserNames_Type=Counter32
_UsecStatsUnknownUserNames_Object=MibScalar
usecStatsUnknownUserNames=_UsecStatsUnknownUserNames_Object((1,3,6,1,6,3,6,1,2,3),_UsecStatsUnknownUserNames_Type())
usecStatsUnknownUserNames.setMaxAccess(_C)
if mibBuilder.loadTexts:usecStatsUnknownUserNames.setStatus(_A)
_UsecStatsWrongDigestValues_Type=Counter32
_UsecStatsWrongDigestValues_Object=MibScalar
usecStatsWrongDigestValues=_UsecStatsWrongDigestValues_Object((1,3,6,1,6,3,6,1,2,4),_UsecStatsWrongDigestValues_Type())
usecStatsWrongDigestValues.setMaxAccess(_C)
if mibBuilder.loadTexts:usecStatsWrongDigestValues.setStatus(_A)
_UsecStatsUnknownContexts_Type=Counter32
_UsecStatsUnknownContexts_Object=MibScalar
usecStatsUnknownContexts=_UsecStatsUnknownContexts_Object((1,3,6,1,6,3,6,1,2,5),_UsecStatsUnknownContexts_Type())
usecStatsUnknownContexts.setMaxAccess(_C)
if mibBuilder.loadTexts:usecStatsUnknownContexts.setStatus(_A)
_UsecStatsBadParameters_Type=Counter32
_UsecStatsBadParameters_Object=MibScalar
usecStatsBadParameters=_UsecStatsBadParameters_Object((1,3,6,1,6,3,6,1,2,6),_UsecStatsBadParameters_Type())
usecStatsBadParameters.setMaxAccess(_C)
if mibBuilder.loadTexts:usecStatsBadParameters.setStatus(_A)
_UsecStatsUnauthorizedOperations_Type=Counter32
_UsecStatsUnauthorizedOperations_Object=MibScalar
usecStatsUnauthorizedOperations=_UsecStatsUnauthorizedOperations_Object((1,3,6,1,6,3,6,1,2,7),_UsecStatsUnauthorizedOperations_Type())
usecStatsUnauthorizedOperations.setMaxAccess(_C)
if mibBuilder.loadTexts:usecStatsUnauthorizedOperations.setStatus(_A)
_UsecMIBConformance_ObjectIdentity=ObjectIdentity
usecMIBConformance=_UsecMIBConformance_ObjectIdentity((1,3,6,1,6,3,6,2))
_UsecMIBCompliances_ObjectIdentity=ObjectIdentity
usecMIBCompliances=_UsecMIBCompliances_ObjectIdentity((1,3,6,1,6,3,6,2,1))
_UsecMIBGroups_ObjectIdentity=ObjectIdentity
usecMIBGroups=_UsecMIBGroups_ObjectIdentity((1,3,6,1,6,3,6,2,2))
usecBasicGroup=ObjectGroup((1,3,6,1,6,3,6,2,2,1))
usecBasicGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:usecBasicGroup.setStatus(_A)
usecStatsGroup=ObjectGroup((1,3,6,1,6,3,6,2,2,2))
usecStatsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:usecStatsGroup.setStatus(_A)
usecMIBCompliance=ModuleCompliance((1,3,6,1,6,3,6,2,1,1))
usecMIBCompliance.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:usecMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AgentID':AgentID,'usecMIB':usecMIB,'usecMIBObjects':usecMIBObjects,'usecAgent':usecAgent,_F:agentID,_G:agentBoots,_H:agentTime,_I:agentSize,'usecStats':usecStats,_J:usecStatsUnsupportedQoS,_K:usecStatsNotInWindows,_L:usecStatsUnknownUserNames,_M:usecStatsWrongDigestValues,_N:usecStatsUnknownContexts,_O:usecStatsBadParameters,_P:usecStatsUnauthorizedOperations,'usecMIBConformance':usecMIBConformance,'usecMIBCompliances':usecMIBCompliances,'usecMIBCompliance':usecMIBCompliance,'usecMIBGroups':usecMIBGroups,_Q:usecBasicGroup,_R:usecStatsGroup})