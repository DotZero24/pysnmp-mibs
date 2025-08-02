_l='ptopoNotificationsGroup'
_k='ptopoConfigGroup'
_j='ptopoGeneralGroup'
_i='ptopoDataGroup'
_h='ptopoConfigChange'
_g='ptopoConfigMaxHoldTime'
_f='ptopoConfigTrapInterval'
_e='ptopoLastChangeTime'
_d='ptopoConnRowStatus'
_c='ptopoConnLastVerifyTime'
_b='ptopoConnIsStatic'
_a='ptopoConnMultiNetSASeen'
_Z='ptopoConnMultiMacSASeen'
_Y='ptopoConnAgentNetAddr'
_X='ptopoConnAgentNetAddrType'
_W='ptopoConnDiscAlgorithm'
_V='ptopoConnRemotePort'
_U='ptopoConnRemotePortType'
_T='ptopoConnRemoteChassis'
_S='ptopoConnRemoteChassisType'
_R='seconds'
_Q='read-write'
_P='ptopoConnIndex'
_O='ptopoConnLocalPort'
_N='ptopoConnLocalChassis'
_M='ptopoConnTimeMark'
_L='TruthValue'
_K='ptopoConnTabAgeouts'
_J='ptopoConnTabDrops'
_I='ptopoConnTabDeletes'
_H='ptopoConnTabInserts'
_G='table entries'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='PTOPO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
TimeFilter,=mibBuilder.importSymbols('RMON2-MIB','TimeFilter')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_L)
ptopoMIB=ModuleIdentity((1,3,6,1,2,1,79))
if mibBuilder.loadTexts:ptopoMIB.setRevisions(('2000-09-21 00:00',))
class PtopoGenAddr(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
class PtopoChassisIdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('chasIdEntPhysicalAlias',1),('chasIdIfAlias',2),('chasIdPortEntPhysicalAlias',3),('chasIdMacAddress',4),('chasIdPtopoGenAddr',5)))
class PtopoChassisId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class PtopoPortIdType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('portIdIfAlias',1),('portIdEntPhysicalAlias',2),('portIdMacAddr',3),('portIdPtopoGenAddr',4)))
class PtopoPortId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class PtopoAddrSeenState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notUsed',1),('unknown',2),('oneAddr',3),('multiAddr',4)))
_PtopoMIBObjects_ObjectIdentity=ObjectIdentity
ptopoMIBObjects=_PtopoMIBObjects_ObjectIdentity((1,3,6,1,2,1,79,1))
_PtopoData_ObjectIdentity=ObjectIdentity
ptopoData=_PtopoData_ObjectIdentity((1,3,6,1,2,1,79,1,1))
_PtopoConnTable_Object=MibTable
ptopoConnTable=_PtopoConnTable_Object((1,3,6,1,2,1,79,1,1,1))
if mibBuilder.loadTexts:ptopoConnTable.setStatus(_A)
_PtopoConnEntry_Object=MibTableRow
ptopoConnEntry=_PtopoConnEntry_Object((1,3,6,1,2,1,79,1,1,1,1))
ptopoConnEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:ptopoConnEntry.setStatus(_A)
_PtopoConnTimeMark_Type=TimeFilter
_PtopoConnTimeMark_Object=MibTableColumn
ptopoConnTimeMark=_PtopoConnTimeMark_Object((1,3,6,1,2,1,79,1,1,1,1,1),_PtopoConnTimeMark_Type())
ptopoConnTimeMark.setMaxAccess(_F)
if mibBuilder.loadTexts:ptopoConnTimeMark.setStatus(_A)
_PtopoConnLocalChassis_Type=PhysicalIndex
_PtopoConnLocalChassis_Object=MibTableColumn
ptopoConnLocalChassis=_PtopoConnLocalChassis_Object((1,3,6,1,2,1,79,1,1,1,1,2),_PtopoConnLocalChassis_Type())
ptopoConnLocalChassis.setMaxAccess(_F)
if mibBuilder.loadTexts:ptopoConnLocalChassis.setStatus(_A)
_PtopoConnLocalPort_Type=PhysicalIndex
_PtopoConnLocalPort_Object=MibTableColumn
ptopoConnLocalPort=_PtopoConnLocalPort_Object((1,3,6,1,2,1,79,1,1,1,1,3),_PtopoConnLocalPort_Type())
ptopoConnLocalPort.setMaxAccess(_F)
if mibBuilder.loadTexts:ptopoConnLocalPort.setStatus(_A)
class _PtopoConnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PtopoConnIndex_Type.__name__=_E
_PtopoConnIndex_Object=MibTableColumn
ptopoConnIndex=_PtopoConnIndex_Object((1,3,6,1,2,1,79,1,1,1,1,4),_PtopoConnIndex_Type())
ptopoConnIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ptopoConnIndex.setStatus(_A)
_PtopoConnRemoteChassisType_Type=PtopoChassisIdType
_PtopoConnRemoteChassisType_Object=MibTableColumn
ptopoConnRemoteChassisType=_PtopoConnRemoteChassisType_Object((1,3,6,1,2,1,79,1,1,1,1,5),_PtopoConnRemoteChassisType_Type())
ptopoConnRemoteChassisType.setMaxAccess(_D)
if mibBuilder.loadTexts:ptopoConnRemoteChassisType.setStatus(_A)
_PtopoConnRemoteChassis_Type=PtopoChassisId
_PtopoConnRemoteChassis_Object=MibTableColumn
ptopoConnRemoteChassis=_PtopoConnRemoteChassis_Object((1,3,6,1,2,1,79,1,1,1,1,6),_PtopoConnRemoteChassis_Type())
ptopoConnRemoteChassis.setMaxAccess(_D)
if mibBuilder.loadTexts:ptopoConnRemoteChassis.setStatus(_A)
_PtopoConnRemotePortType_Type=PtopoPortIdType
_PtopoConnRemotePortType_Object=MibTableColumn
ptopoConnRemotePortType=_PtopoConnRemotePortType_Object((1,3,6,1,2,1,79,1,1,1,1,7),_PtopoConnRemotePortType_Type())
ptopoConnRemotePortType.setMaxAccess(_D)
if mibBuilder.loadTexts:ptopoConnRemotePortType.setStatus(_A)
_PtopoConnRemotePort_Type=PtopoPortId
_PtopoConnRemotePort_Object=MibTableColumn
ptopoConnRemotePort=_PtopoConnRemotePort_Object((1,3,6,1,2,1,79,1,1,1,1,8),_PtopoConnRemotePort_Type())
ptopoConnRemotePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ptopoConnRemotePort.setStatus(_A)
_PtopoConnDiscAlgorithm_Type=AutonomousType
_PtopoConnDiscAlgorithm_Object=MibTableColumn
ptopoConnDiscAlgorithm=_PtopoConnDiscAlgorithm_Object((1,3,6,1,2,1,79,1,1,1,1,9),_PtopoConnDiscAlgorithm_Type())
ptopoConnDiscAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnDiscAlgorithm.setStatus(_A)
_PtopoConnAgentNetAddrType_Type=AddressFamilyNumbers
_PtopoConnAgentNetAddrType_Object=MibTableColumn
ptopoConnAgentNetAddrType=_PtopoConnAgentNetAddrType_Object((1,3,6,1,2,1,79,1,1,1,1,10),_PtopoConnAgentNetAddrType_Type())
ptopoConnAgentNetAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:ptopoConnAgentNetAddrType.setStatus(_A)
_PtopoConnAgentNetAddr_Type=PtopoGenAddr
_PtopoConnAgentNetAddr_Object=MibTableColumn
ptopoConnAgentNetAddr=_PtopoConnAgentNetAddr_Object((1,3,6,1,2,1,79,1,1,1,1,11),_PtopoConnAgentNetAddr_Type())
ptopoConnAgentNetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ptopoConnAgentNetAddr.setStatus(_A)
_PtopoConnMultiMacSASeen_Type=PtopoAddrSeenState
_PtopoConnMultiMacSASeen_Object=MibTableColumn
ptopoConnMultiMacSASeen=_PtopoConnMultiMacSASeen_Object((1,3,6,1,2,1,79,1,1,1,1,12),_PtopoConnMultiMacSASeen_Type())
ptopoConnMultiMacSASeen.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnMultiMacSASeen.setStatus(_A)
_PtopoConnMultiNetSASeen_Type=PtopoAddrSeenState
_PtopoConnMultiNetSASeen_Object=MibTableColumn
ptopoConnMultiNetSASeen=_PtopoConnMultiNetSASeen_Object((1,3,6,1,2,1,79,1,1,1,1,13),_PtopoConnMultiNetSASeen_Type())
ptopoConnMultiNetSASeen.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnMultiNetSASeen.setStatus(_A)
class _PtopoConnIsStatic_Type(TruthValue):defaultValue=2
_PtopoConnIsStatic_Type.__name__=_L
_PtopoConnIsStatic_Object=MibTableColumn
ptopoConnIsStatic=_PtopoConnIsStatic_Object((1,3,6,1,2,1,79,1,1,1,1,14),_PtopoConnIsStatic_Type())
ptopoConnIsStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:ptopoConnIsStatic.setStatus(_A)
_PtopoConnLastVerifyTime_Type=TimeStamp
_PtopoConnLastVerifyTime_Object=MibTableColumn
ptopoConnLastVerifyTime=_PtopoConnLastVerifyTime_Object((1,3,6,1,2,1,79,1,1,1,1,15),_PtopoConnLastVerifyTime_Type())
ptopoConnLastVerifyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnLastVerifyTime.setStatus(_A)
_PtopoConnRowStatus_Type=RowStatus
_PtopoConnRowStatus_Object=MibTableColumn
ptopoConnRowStatus=_PtopoConnRowStatus_Object((1,3,6,1,2,1,79,1,1,1,1,16),_PtopoConnRowStatus_Type())
ptopoConnRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ptopoConnRowStatus.setStatus(_A)
_PtopoGeneral_ObjectIdentity=ObjectIdentity
ptopoGeneral=_PtopoGeneral_ObjectIdentity((1,3,6,1,2,1,79,1,2))
_PtopoLastChangeTime_Type=TimeStamp
_PtopoLastChangeTime_Object=MibScalar
ptopoLastChangeTime=_PtopoLastChangeTime_Object((1,3,6,1,2,1,79,1,2,1),_PtopoLastChangeTime_Type())
ptopoLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoLastChangeTime.setStatus(_A)
_PtopoConnTabInserts_Type=Counter32
_PtopoConnTabInserts_Object=MibScalar
ptopoConnTabInserts=_PtopoConnTabInserts_Object((1,3,6,1,2,1,79,1,2,2),_PtopoConnTabInserts_Type())
ptopoConnTabInserts.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnTabInserts.setStatus(_A)
if mibBuilder.loadTexts:ptopoConnTabInserts.setUnits(_G)
_PtopoConnTabDeletes_Type=Counter32
_PtopoConnTabDeletes_Object=MibScalar
ptopoConnTabDeletes=_PtopoConnTabDeletes_Object((1,3,6,1,2,1,79,1,2,3),_PtopoConnTabDeletes_Type())
ptopoConnTabDeletes.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnTabDeletes.setStatus(_A)
if mibBuilder.loadTexts:ptopoConnTabDeletes.setUnits(_G)
_PtopoConnTabDrops_Type=Counter32
_PtopoConnTabDrops_Object=MibScalar
ptopoConnTabDrops=_PtopoConnTabDrops_Object((1,3,6,1,2,1,79,1,2,4),_PtopoConnTabDrops_Type())
ptopoConnTabDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnTabDrops.setStatus(_A)
if mibBuilder.loadTexts:ptopoConnTabDrops.setUnits(_G)
_PtopoConnTabAgeouts_Type=Counter32
_PtopoConnTabAgeouts_Object=MibScalar
ptopoConnTabAgeouts=_PtopoConnTabAgeouts_Object((1,3,6,1,2,1,79,1,2,5),_PtopoConnTabAgeouts_Type())
ptopoConnTabAgeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:ptopoConnTabAgeouts.setStatus(_A)
_PtopoConfig_ObjectIdentity=ObjectIdentity
ptopoConfig=_PtopoConfig_ObjectIdentity((1,3,6,1,2,1,79,1,3))
class _PtopoConfigTrapInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,3600))
_PtopoConfigTrapInterval_Type.__name__=_E
_PtopoConfigTrapInterval_Object=MibScalar
ptopoConfigTrapInterval=_PtopoConfigTrapInterval_Object((1,3,6,1,2,1,79,1,3,1),_PtopoConfigTrapInterval_Type())
ptopoConfigTrapInterval.setMaxAccess(_Q)
if mibBuilder.loadTexts:ptopoConfigTrapInterval.setStatus(_A)
if mibBuilder.loadTexts:ptopoConfigTrapInterval.setUnits(_R)
class _PtopoConfigMaxHoldTime_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PtopoConfigMaxHoldTime_Type.__name__=_E
_PtopoConfigMaxHoldTime_Object=MibScalar
ptopoConfigMaxHoldTime=_PtopoConfigMaxHoldTime_Object((1,3,6,1,2,1,79,1,3,2),_PtopoConfigMaxHoldTime_Type())
ptopoConfigMaxHoldTime.setMaxAccess(_Q)
if mibBuilder.loadTexts:ptopoConfigMaxHoldTime.setStatus(_A)
if mibBuilder.loadTexts:ptopoConfigMaxHoldTime.setUnits(_R)
_PtopoMIBNotifications_ObjectIdentity=ObjectIdentity
ptopoMIBNotifications=_PtopoMIBNotifications_ObjectIdentity((1,3,6,1,2,1,79,2))
_PtopoMIBTrapPrefix_ObjectIdentity=ObjectIdentity
ptopoMIBTrapPrefix=_PtopoMIBTrapPrefix_ObjectIdentity((1,3,6,1,2,1,79,2,0))
_PtopoRegistrationPoints_ObjectIdentity=ObjectIdentity
ptopoRegistrationPoints=_PtopoRegistrationPoints_ObjectIdentity((1,3,6,1,2,1,79,3))
_PtopoDiscoveryMechanisms_ObjectIdentity=ObjectIdentity
ptopoDiscoveryMechanisms=_PtopoDiscoveryMechanisms_ObjectIdentity((1,3,6,1,2,1,79,3,1))
_PtopoDiscoveryLocal_ObjectIdentity=ObjectIdentity
ptopoDiscoveryLocal=_PtopoDiscoveryLocal_ObjectIdentity((1,3,6,1,2,1,79,3,1,1))
_PtopoConformance_ObjectIdentity=ObjectIdentity
ptopoConformance=_PtopoConformance_ObjectIdentity((1,3,6,1,2,1,79,4))
_PtopoCompliances_ObjectIdentity=ObjectIdentity
ptopoCompliances=_PtopoCompliances_ObjectIdentity((1,3,6,1,2,1,79,4,1))
_PtopoGroups_ObjectIdentity=ObjectIdentity
ptopoGroups=_PtopoGroups_ObjectIdentity((1,3,6,1,2,1,79,4,2))
ptopoDataGroup=ObjectGroup((1,3,6,1,2,1,79,4,2,1))
ptopoDataGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ptopoDataGroup.setStatus(_A)
ptopoGeneralGroup=ObjectGroup((1,3,6,1,2,1,79,4,2,2))
ptopoGeneralGroup.setObjects(*((_B,_e),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ptopoGeneralGroup.setStatus(_A)
ptopoConfigGroup=ObjectGroup((1,3,6,1,2,1,79,4,2,3))
ptopoConfigGroup.setObjects(*((_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ptopoConfigGroup.setStatus(_A)
ptopoConfigChange=NotificationType((1,3,6,1,2,1,79,2,0,1))
ptopoConfigChange.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:ptopoConfigChange.setStatus(_A)
ptopoNotificationsGroup=NotificationGroup((1,3,6,1,2,1,79,4,2,4))
ptopoNotificationsGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:ptopoNotificationsGroup.setStatus(_A)
ptopoCompliance=ModuleCompliance((1,3,6,1,2,1,79,4,1,1))
ptopoCompliance.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:ptopoCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PtopoGenAddr':PtopoGenAddr,'PtopoChassisIdType':PtopoChassisIdType,'PtopoChassisId':PtopoChassisId,'PtopoPortIdType':PtopoPortIdType,'PtopoPortId':PtopoPortId,'PtopoAddrSeenState':PtopoAddrSeenState,'ptopoMIB':ptopoMIB,'ptopoMIBObjects':ptopoMIBObjects,'ptopoData':ptopoData,'ptopoConnTable':ptopoConnTable,'ptopoConnEntry':ptopoConnEntry,_M:ptopoConnTimeMark,_N:ptopoConnLocalChassis,_O:ptopoConnLocalPort,_P:ptopoConnIndex,_S:ptopoConnRemoteChassisType,_T:ptopoConnRemoteChassis,_U:ptopoConnRemotePortType,_V:ptopoConnRemotePort,_W:ptopoConnDiscAlgorithm,_X:ptopoConnAgentNetAddrType,_Y:ptopoConnAgentNetAddr,_Z:ptopoConnMultiMacSASeen,_a:ptopoConnMultiNetSASeen,_b:ptopoConnIsStatic,_c:ptopoConnLastVerifyTime,_d:ptopoConnRowStatus,'ptopoGeneral':ptopoGeneral,_e:ptopoLastChangeTime,_H:ptopoConnTabInserts,_I:ptopoConnTabDeletes,_J:ptopoConnTabDrops,_K:ptopoConnTabAgeouts,'ptopoConfig':ptopoConfig,_f:ptopoConfigTrapInterval,_g:ptopoConfigMaxHoldTime,'ptopoMIBNotifications':ptopoMIBNotifications,'ptopoMIBTrapPrefix':ptopoMIBTrapPrefix,_h:ptopoConfigChange,'ptopoRegistrationPoints':ptopoRegistrationPoints,'ptopoDiscoveryMechanisms':ptopoDiscoveryMechanisms,'ptopoDiscoveryLocal':ptopoDiscoveryLocal,'ptopoConformance':ptopoConformance,'ptopoCompliances':ptopoCompliances,'ptopoCompliance':ptopoCompliance,'ptopoGroups':ptopoGroups,_i:ptopoDataGroup,_j:ptopoGeneralGroup,_k:ptopoConfigGroup,_l:ptopoNotificationsGroup})