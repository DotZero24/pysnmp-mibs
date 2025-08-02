_Z='alaLldpTrustTrapGroup'
_Y='alaINDLLDPTrustBaseGroup'
_X='alaINDLLDPTrustRemoteAgentGroup'
_W='alaINDLLDPTrustAgentGroup'
_V='alaLldpTrustViolation'
_U='alaLLDPTrustedRemPortId'
_T='alaLLDPTrustedRemPortIdSubtype'
_S='alaLLDPTrustedRemChassisId'
_R='alaLLDPTrustedRemChassisIdSubtype'
_Q='alaLldpTrustedChassisSubtype'
_P='alaLldpTrustedStatus'
_O='alaLldpTrustAction'
_N='alaLldpTrustAdminStatus'
_M='alaLLDPTrustChassisId'
_L='alaLLDPTrustPortId'
_K='alaLLDPTrustedRemLocalPortNumber'
_J='not-accessible'
_I='alaLLDPTrustLocalPortNumber'
_H='alaLLDPTrustViolationReason'
_G='alaLLDPTrustPortIfIndex'
_F='read-write'
_E='accessible-for-notify'
_D='read-only'
_C='Integer32'
_B='ALCATEL-ENT1-LLDP-TRUST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1LldpTrust,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1LldpTrust')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
LldpChassisId,LldpChassisIdSubtype,LldpPortId,LldpPortIdSubtype,LldpPortNumber=mibBuilder.importSymbols('LLDP-MIB','LldpChassisId','LldpChassisIdSubtype','LldpPortId','LldpPortIdSubtype','LldpPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
alcatelIND1LLDPTRUSTMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,87,1))
if mibBuilder.loadTexts:alcatelIND1LLDPTRUSTMIB.setRevisions(('2009-08-11 00:00',))
_AlaLLDPTraps_ObjectIdentity=ObjectIdentity
alaLLDPTraps=_AlaLLDPTraps_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,87,1,0))
if mibBuilder.loadTexts:alaLLDPTraps.setStatus(_A)
_AlcatelIND1LLDPTRUSTMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1LLDPTRUSTMIBObjects=_AlcatelIND1LLDPTRUSTMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,87,1,1))
if mibBuilder.loadTexts:alcatelIND1LLDPTRUSTMIBObjects.setStatus(_A)
_AlaIND1LLDPTRUSTMIBObjects_ObjectIdentity=ObjectIdentity
alaIND1LLDPTRUSTMIBObjects=_AlaIND1LLDPTRUSTMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1))
_AlaLLDPTrustPortTable_Object=MibTable
alaLLDPTrustPortTable=_AlaLLDPTrustPortTable_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,1))
if mibBuilder.loadTexts:alaLLDPTrustPortTable.setStatus(_A)
_AlaLLDPTrustPortEntry_Object=MibTableRow
alaLLDPTrustPortEntry=_AlaLLDPTrustPortEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,1,1))
alaLLDPTrustPortEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:alaLLDPTrustPortEntry.setStatus(_A)
_AlaLLDPTrustLocalPortNumber_Type=LldpPortNumber
_AlaLLDPTrustLocalPortNumber_Object=MibTableColumn
alaLLDPTrustLocalPortNumber=_AlaLLDPTrustLocalPortNumber_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,1,1,1),_AlaLLDPTrustLocalPortNumber_Type())
alaLLDPTrustLocalPortNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:alaLLDPTrustLocalPortNumber.setStatus(_A)
class _AlaLldpTrustAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AlaLldpTrustAdminStatus_Type.__name__=_C
_AlaLldpTrustAdminStatus_Object=MibTableColumn
alaLldpTrustAdminStatus=_AlaLldpTrustAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,1,1,2),_AlaLldpTrustAdminStatus_Type())
alaLldpTrustAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLldpTrustAdminStatus.setStatus(_A)
class _AlaLldpTrustAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('trap',1),('shutdown',2),('both',3)))
_AlaLldpTrustAction_Type.__name__=_C
_AlaLldpTrustAction_Object=MibTableColumn
alaLldpTrustAction=_AlaLldpTrustAction_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,1,1,3),_AlaLldpTrustAction_Type())
alaLldpTrustAction.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLldpTrustAction.setStatus(_A)
class _AlaLldpTrustedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trusted',1),('violated',2)))
_AlaLldpTrustedStatus_Type.__name__=_C
_AlaLldpTrustedStatus_Object=MibTableColumn
alaLldpTrustedStatus=_AlaLldpTrustedStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,1,1,4),_AlaLldpTrustedStatus_Type())
alaLldpTrustedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLldpTrustedStatus.setStatus(_A)
class _AlaLldpTrustedChassisSubtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('chassisComponent',1),('interfaceAlias',2),('portComponent',3),('macAddress',4),('networkAddress',5),('interfaceName',6),('local',7),('any',8)))
_AlaLldpTrustedChassisSubtype_Type.__name__=_C
_AlaLldpTrustedChassisSubtype_Object=MibTableColumn
alaLldpTrustedChassisSubtype=_AlaLldpTrustedChassisSubtype_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,1,1,5),_AlaLldpTrustedChassisSubtype_Type())
alaLldpTrustedChassisSubtype.setMaxAccess(_F)
if mibBuilder.loadTexts:alaLldpTrustedChassisSubtype.setStatus(_A)
_AlaLLDPTrustedRemTable_Object=MibTable
alaLLDPTrustedRemTable=_AlaLLDPTrustedRemTable_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,2))
if mibBuilder.loadTexts:alaLLDPTrustedRemTable.setStatus(_A)
_AlaLLDPTrustedRemEntry_Object=MibTableRow
alaLLDPTrustedRemEntry=_AlaLLDPTrustedRemEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,2,1))
alaLLDPTrustedRemEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:alaLLDPTrustedRemEntry.setStatus(_A)
_AlaLLDPTrustedRemLocalPortNumber_Type=LldpPortNumber
_AlaLLDPTrustedRemLocalPortNumber_Object=MibTableColumn
alaLLDPTrustedRemLocalPortNumber=_AlaLLDPTrustedRemLocalPortNumber_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,2,1,1),_AlaLLDPTrustedRemLocalPortNumber_Type())
alaLLDPTrustedRemLocalPortNumber.setMaxAccess(_J)
if mibBuilder.loadTexts:alaLLDPTrustedRemLocalPortNumber.setStatus(_A)
_AlaLLDPTrustedRemChassisIdSubtype_Type=LldpChassisIdSubtype
_AlaLLDPTrustedRemChassisIdSubtype_Object=MibTableColumn
alaLLDPTrustedRemChassisIdSubtype=_AlaLLDPTrustedRemChassisIdSubtype_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,2,1,2),_AlaLLDPTrustedRemChassisIdSubtype_Type())
alaLLDPTrustedRemChassisIdSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLLDPTrustedRemChassisIdSubtype.setStatus(_A)
_AlaLLDPTrustedRemChassisId_Type=LldpChassisId
_AlaLLDPTrustedRemChassisId_Object=MibTableColumn
alaLLDPTrustedRemChassisId=_AlaLLDPTrustedRemChassisId_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,2,1,3),_AlaLLDPTrustedRemChassisId_Type())
alaLLDPTrustedRemChassisId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLLDPTrustedRemChassisId.setStatus(_A)
_AlaLLDPTrustedRemPortIdSubtype_Type=LldpPortIdSubtype
_AlaLLDPTrustedRemPortIdSubtype_Object=MibTableColumn
alaLLDPTrustedRemPortIdSubtype=_AlaLLDPTrustedRemPortIdSubtype_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,2,1,4),_AlaLLDPTrustedRemPortIdSubtype_Type())
alaLLDPTrustedRemPortIdSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLLDPTrustedRemPortIdSubtype.setStatus(_A)
_AlaLLDPTrustedRemPortId_Type=LldpPortId
_AlaLLDPTrustedRemPortId_Object=MibTableColumn
alaLLDPTrustedRemPortId=_AlaLLDPTrustedRemPortId_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,2,1,5),_AlaLLDPTrustedRemPortId_Type())
alaLLDPTrustedRemPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:alaLLDPTrustedRemPortId.setStatus(_A)
_AlaLLDPTrustPortIfIndex_Type=InterfaceIndex
_AlaLLDPTrustPortIfIndex_Object=MibScalar
alaLLDPTrustPortIfIndex=_AlaLLDPTrustPortIfIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,3),_AlaLLDPTrustPortIfIndex_Type())
alaLLDPTrustPortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLLDPTrustPortIfIndex.setStatus(_A)
class _AlaLLDPTrustViolationReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('agentalreadyexistonport',1),('agentalreadyexistonotherport',2),('chassisidsubtypemissmatch',3)))
_AlaLLDPTrustViolationReason_Type.__name__=_C
_AlaLLDPTrustViolationReason_Object=MibScalar
alaLLDPTrustViolationReason=_AlaLLDPTrustViolationReason_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,4),_AlaLLDPTrustViolationReason_Type())
alaLLDPTrustViolationReason.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLLDPTrustViolationReason.setStatus(_A)
_AlaLLDPTrustPortId_Type=Integer32
_AlaLLDPTrustPortId_Object=MibScalar
alaLLDPTrustPortId=_AlaLLDPTrustPortId_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,5),_AlaLLDPTrustPortId_Type())
alaLLDPTrustPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLLDPTrustPortId.setStatus(_A)
_AlaLLDPTrustChassisId_Type=LldpChassisId
_AlaLLDPTrustChassisId_Object=MibScalar
alaLLDPTrustChassisId=_AlaLLDPTrustChassisId_Object((1,3,6,1,4,1,6486,801,1,2,1,87,1,1,1,6),_AlaLLDPTrustChassisId_Type())
alaLLDPTrustChassisId.setMaxAccess(_E)
if mibBuilder.loadTexts:alaLLDPTrustChassisId.setStatus(_A)
_AlaIND1LLDPTRUSTMIBConformance_ObjectIdentity=ObjectIdentity
alaIND1LLDPTRUSTMIBConformance=_AlaIND1LLDPTRUSTMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,87,1,2))
if mibBuilder.loadTexts:alaIND1LLDPTRUSTMIBConformance.setStatus(_A)
_AlaIND1LLDPTRUSTMIBGroups_ObjectIdentity=ObjectIdentity
alaIND1LLDPTRUSTMIBGroups=_AlaIND1LLDPTRUSTMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,87,1,2,1))
if mibBuilder.loadTexts:alaIND1LLDPTRUSTMIBGroups.setStatus(_A)
_AlaIND1LLDPTRUSTMIBCompliances_ObjectIdentity=ObjectIdentity
alaIND1LLDPTRUSTMIBCompliances=_AlaIND1LLDPTRUSTMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,87,1,2,2))
if mibBuilder.loadTexts:alaIND1LLDPTRUSTMIBCompliances.setStatus(_A)
alaINDLLDPTrustBaseGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,87,1,2,1,1))
alaINDLLDPTrustBaseGroup.setObjects(*((_B,_G),(_B,_H),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:alaINDLLDPTrustBaseGroup.setStatus(_A)
alaINDLLDPTrustAgentGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,87,1,2,1,2))
alaINDLLDPTrustAgentGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:alaINDLLDPTrustAgentGroup.setStatus(_A)
alaINDLLDPTrustRemoteAgentGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,87,1,2,1,3))
alaINDLLDPTrustRemoteAgentGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:alaINDLLDPTrustRemoteAgentGroup.setStatus(_A)
alaLldpTrustViolation=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,87,1,0,1))
alaLldpTrustViolation.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:alaLldpTrustViolation.setStatus(_A)
alaLldpTrustTrapGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,87,1,2,1,4))
alaLldpTrustTrapGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:alaLldpTrustTrapGroup.setStatus(_A)
alaIND1LLDPTRUSTMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,87,1,2,2,1))
alaIND1LLDPTRUSTMIBCompliance.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:alaIND1LLDPTRUSTMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1LLDPTRUSTMIB':alcatelIND1LLDPTRUSTMIB,'alaLLDPTraps':alaLLDPTraps,_V:alaLldpTrustViolation,'alcatelIND1LLDPTRUSTMIBObjects':alcatelIND1LLDPTRUSTMIBObjects,'alaIND1LLDPTRUSTMIBObjects':alaIND1LLDPTRUSTMIBObjects,'alaLLDPTrustPortTable':alaLLDPTrustPortTable,'alaLLDPTrustPortEntry':alaLLDPTrustPortEntry,_I:alaLLDPTrustLocalPortNumber,_N:alaLldpTrustAdminStatus,_O:alaLldpTrustAction,_P:alaLldpTrustedStatus,_Q:alaLldpTrustedChassisSubtype,'alaLLDPTrustedRemTable':alaLLDPTrustedRemTable,'alaLLDPTrustedRemEntry':alaLLDPTrustedRemEntry,_K:alaLLDPTrustedRemLocalPortNumber,_R:alaLLDPTrustedRemChassisIdSubtype,_S:alaLLDPTrustedRemChassisId,_T:alaLLDPTrustedRemPortIdSubtype,_U:alaLLDPTrustedRemPortId,_G:alaLLDPTrustPortIfIndex,_H:alaLLDPTrustViolationReason,_L:alaLLDPTrustPortId,_M:alaLLDPTrustChassisId,'alaIND1LLDPTRUSTMIBConformance':alaIND1LLDPTRUSTMIBConformance,'alaIND1LLDPTRUSTMIBGroups':alaIND1LLDPTRUSTMIBGroups,_Y:alaINDLLDPTrustBaseGroup,_W:alaINDLLDPTrustAgentGroup,_X:alaINDLLDPTrustRemoteAgentGroup,_Z:alaLldpTrustTrapGroup,'alaIND1LLDPTRUSTMIBCompliances':alaIND1LLDPTRUSTMIBCompliances,'alaIND1LLDPTRUSTMIBCompliance':alaIND1LLDPTRUSTMIBCompliance})