_l='ciscoAtmIfPhysMIBE1Group'
_k='ciscoAtmIfPhysMIBDs1Group'
_j='ciscoAtmIfPhysMIBDs1E1Group'
_i='obsolete'
_h='ciscoAtmIfPhysE1CrcErrors'
_g='ciscoAtmIfPhysDS1BitErrors'
_f='ciscoAtmIfPhysLineCode'
_e='ciscoAtmIfPhysLineBuildOut'
_d='ciscoAtmIfPhysStsStreamScrambling'
_c='ciscoAtmIfPhysPathFebeErrors'
_b='ciscoAtmIfPhysLineFebeErrors'
_a='ciscoAtmIfPhysClockSourceStatus'
_Z='ciscoAtmIfPhysClockSourcePriority'
_Y='ciscoAtmIfPhysTransmitClockSource'
_X='ciscoAtmIfPhysLoopbackConfig'
_W='ciscoAtmIfPhysFramingMode'
_V='ciscoAtmIfPhysCellPayloadScrambling'
_U='ciscoAtmIfPhysPBitParityErrors'
_T='ciscoAtmIfPhysCBitParityErrors'
_S='ciscoAtmIfPhysPathParityErrors'
_R='ciscoAtmIfPhysLineParityErrors'
_Q='ciscoAtmIfPhysSectionParityErrors'
_P='ciscoAtmIfPhysStatus'
_O='ifIndex'
_N='IF-MIB'
_M='ciscoAtmIfPhysMIBDs3Group'
_L='ciscoAtmIfPhysMIBDs3E3Group'
_K='ciscoAtmIfPhysMIBSonetGroup2'
_J='ciscoAtmIfPhysMIBSonetGroup'
_I='ciscoAtmIfPhysMIBCommonGroup2'
_H='ciscoAtmIfPhysPlcpBipViolations'
_G='ciscoAtmIfPhysLcvErrors'
_F='ciscoAtmIfPhysMIBCommonGroup'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-ATM-IF-PHYS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_N,_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoAtmIfPhysMIB=ModuleIdentity((1,3,6,1,4,1,9,9,45))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIB.setRevisions(('1996-09-19 00:00','1996-08-08 00:00','1995-12-02 00:00'))
_CiscoAtmIfPhysMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAtmIfPhysMIBObjects=_CiscoAtmIfPhysMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,45,1))
_CiscoAtmIfPhysTable_Object=MibTable
ciscoAtmIfPhysTable=_CiscoAtmIfPhysTable_Object((1,3,6,1,4,1,9,9,45,1,1))
if mibBuilder.loadTexts:ciscoAtmIfPhysTable.setStatus(_B)
_CiscoAtmIfPhysEntry_Object=MibTableRow
ciscoAtmIfPhysEntry=_CiscoAtmIfPhysEntry_Object((1,3,6,1,4,1,9,9,45,1,1,1))
ciscoAtmIfPhysEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:ciscoAtmIfPhysEntry.setStatus(_B)
class _CiscoAtmIfPhysStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('normal',1),('los',2),('lof',3),('loc',4),('ais',5),('yellowLine',6),('yellowPath',7),('lop',8),('idle',9),('yellowAlarm',10),('plcpLOF',11),('plcpYellow',12),('maFERF',13),('pathAis',14),('ocd',15)))
_CiscoAtmIfPhysStatus_Type.__name__=_D
_CiscoAtmIfPhysStatus_Object=MibTableColumn
ciscoAtmIfPhysStatus=_CiscoAtmIfPhysStatus_Object((1,3,6,1,4,1,9,9,45,1,1,1,1),_CiscoAtmIfPhysStatus_Type())
ciscoAtmIfPhysStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysStatus.setStatus(_B)
_CiscoAtmIfPhysSectionParityErrors_Type=Counter32
_CiscoAtmIfPhysSectionParityErrors_Object=MibTableColumn
ciscoAtmIfPhysSectionParityErrors=_CiscoAtmIfPhysSectionParityErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,2),_CiscoAtmIfPhysSectionParityErrors_Type())
ciscoAtmIfPhysSectionParityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysSectionParityErrors.setStatus(_B)
_CiscoAtmIfPhysLineParityErrors_Type=Counter32
_CiscoAtmIfPhysLineParityErrors_Object=MibTableColumn
ciscoAtmIfPhysLineParityErrors=_CiscoAtmIfPhysLineParityErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,3),_CiscoAtmIfPhysLineParityErrors_Type())
ciscoAtmIfPhysLineParityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysLineParityErrors.setStatus(_B)
_CiscoAtmIfPhysPathParityErrors_Type=Counter32
_CiscoAtmIfPhysPathParityErrors_Object=MibTableColumn
ciscoAtmIfPhysPathParityErrors=_CiscoAtmIfPhysPathParityErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,4),_CiscoAtmIfPhysPathParityErrors_Type())
ciscoAtmIfPhysPathParityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysPathParityErrors.setStatus(_B)
_CiscoAtmIfPhysLcvErrors_Type=Counter32
_CiscoAtmIfPhysLcvErrors_Object=MibTableColumn
ciscoAtmIfPhysLcvErrors=_CiscoAtmIfPhysLcvErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,5),_CiscoAtmIfPhysLcvErrors_Type())
ciscoAtmIfPhysLcvErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysLcvErrors.setStatus(_B)
_CiscoAtmIfPhysCBitParityErrors_Type=Counter32
_CiscoAtmIfPhysCBitParityErrors_Object=MibTableColumn
ciscoAtmIfPhysCBitParityErrors=_CiscoAtmIfPhysCBitParityErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,6),_CiscoAtmIfPhysCBitParityErrors_Type())
ciscoAtmIfPhysCBitParityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysCBitParityErrors.setStatus(_B)
_CiscoAtmIfPhysPBitParityErrors_Type=Counter32
_CiscoAtmIfPhysPBitParityErrors_Object=MibTableColumn
ciscoAtmIfPhysPBitParityErrors=_CiscoAtmIfPhysPBitParityErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,7),_CiscoAtmIfPhysPBitParityErrors_Type())
ciscoAtmIfPhysPBitParityErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysPBitParityErrors.setStatus(_B)
_CiscoAtmIfPhysPlcpBipViolations_Type=Counter32
_CiscoAtmIfPhysPlcpBipViolations_Object=MibTableColumn
ciscoAtmIfPhysPlcpBipViolations=_CiscoAtmIfPhysPlcpBipViolations_Object((1,3,6,1,4,1,9,9,45,1,1,1,8),_CiscoAtmIfPhysPlcpBipViolations_Type())
ciscoAtmIfPhysPlcpBipViolations.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysPlcpBipViolations.setStatus(_B)
_CiscoAtmIfPhysLineFebeErrors_Type=Counter32
_CiscoAtmIfPhysLineFebeErrors_Object=MibTableColumn
ciscoAtmIfPhysLineFebeErrors=_CiscoAtmIfPhysLineFebeErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,9),_CiscoAtmIfPhysLineFebeErrors_Type())
ciscoAtmIfPhysLineFebeErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysLineFebeErrors.setStatus(_B)
_CiscoAtmIfPhysPathFebeErrors_Type=Counter32
_CiscoAtmIfPhysPathFebeErrors_Object=MibTableColumn
ciscoAtmIfPhysPathFebeErrors=_CiscoAtmIfPhysPathFebeErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,10),_CiscoAtmIfPhysPathFebeErrors_Type())
ciscoAtmIfPhysPathFebeErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysPathFebeErrors.setStatus(_B)
class _CiscoAtmIfPhysCellPayloadScrambling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_CiscoAtmIfPhysCellPayloadScrambling_Type.__name__=_D
_CiscoAtmIfPhysCellPayloadScrambling_Object=MibTableColumn
ciscoAtmIfPhysCellPayloadScrambling=_CiscoAtmIfPhysCellPayloadScrambling_Object((1,3,6,1,4,1,9,9,45,1,1,1,11),_CiscoAtmIfPhysCellPayloadScrambling_Type())
ciscoAtmIfPhysCellPayloadScrambling.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPhysCellPayloadScrambling.setStatus(_B)
class _CiscoAtmIfPhysStsStreamScrambling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_CiscoAtmIfPhysStsStreamScrambling_Type.__name__=_D
_CiscoAtmIfPhysStsStreamScrambling_Object=MibTableColumn
ciscoAtmIfPhysStsStreamScrambling=_CiscoAtmIfPhysStsStreamScrambling_Object((1,3,6,1,4,1,9,9,45,1,1,1,12),_CiscoAtmIfPhysStsStreamScrambling_Type())
ciscoAtmIfPhysStsStreamScrambling.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPhysStsStreamScrambling.setStatus(_B)
class _CiscoAtmIfPhysFramingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('sonet',1),('sdh',2),('ds3m23adm',3),('ds3m23plcp',4),('ds3cbitadm',5),('ds3cbitplcp',6),('e3g832adm',7),('e3g751adm',8),('e3g751plcp',9),('ds1sfadm',10),('ds1esfadm',11),('ds1sfplcp',12),('ds1esfplcp',13),('e1adm',14),('e1plcp',15),('e1crcadm',16),('e1crcplcp',17)))
_CiscoAtmIfPhysFramingMode_Type.__name__=_D
_CiscoAtmIfPhysFramingMode_Object=MibTableColumn
ciscoAtmIfPhysFramingMode=_CiscoAtmIfPhysFramingMode_Object((1,3,6,1,4,1,9,9,45,1,1,1,13),_CiscoAtmIfPhysFramingMode_Type())
ciscoAtmIfPhysFramingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPhysFramingMode.setStatus(_B)
class _CiscoAtmIfPhysLoopbackConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noLoop',1),('diagnosticLoop',2),('lineLoop',3),('otherLoop',4)))
_CiscoAtmIfPhysLoopbackConfig_Type.__name__=_D
_CiscoAtmIfPhysLoopbackConfig_Object=MibTableColumn
ciscoAtmIfPhysLoopbackConfig=_CiscoAtmIfPhysLoopbackConfig_Object((1,3,6,1,4,1,9,9,45,1,1,1,14),_CiscoAtmIfPhysLoopbackConfig_Type())
ciscoAtmIfPhysLoopbackConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPhysLoopbackConfig.setStatus(_B)
class _CiscoAtmIfPhysLineBuildOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('e3AllCables',1),('ds3CablesUnder225',2),('ds3CablesOver225',3),('ds1Cables0To110',4),('ds1Cables110To220',5),('ds1Cables220To330',6),('ds1Cables330To440',7),('ds1Cables440To550',8),('ds1Cables550To660',9),('ds1CablesOver600',10),('e1AllCables',11)))
_CiscoAtmIfPhysLineBuildOut_Type.__name__=_D
_CiscoAtmIfPhysLineBuildOut_Object=MibTableColumn
ciscoAtmIfPhysLineBuildOut=_CiscoAtmIfPhysLineBuildOut_Object((1,3,6,1,4,1,9,9,45,1,1,1,15),_CiscoAtmIfPhysLineBuildOut_Type())
ciscoAtmIfPhysLineBuildOut.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPhysLineBuildOut.setStatus(_B)
class _CiscoAtmIfPhysTransmitClockSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('loopTiming',1),('freeRunning',2),('networkDerived',3)))
_CiscoAtmIfPhysTransmitClockSource_Type.__name__=_D
_CiscoAtmIfPhysTransmitClockSource_Object=MibTableColumn
ciscoAtmIfPhysTransmitClockSource=_CiscoAtmIfPhysTransmitClockSource_Object((1,3,6,1,4,1,9,9,45,1,1,1,16),_CiscoAtmIfPhysTransmitClockSource_Type())
ciscoAtmIfPhysTransmitClockSource.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPhysTransmitClockSource.setStatus(_B)
class _CiscoAtmIfPhysClockSourcePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notConfigured',1),('priority1',2),('priority2',3),('priority3',4),('priority4',5)))
_CiscoAtmIfPhysClockSourcePriority_Type.__name__=_D
_CiscoAtmIfPhysClockSourcePriority_Object=MibTableColumn
ciscoAtmIfPhysClockSourcePriority=_CiscoAtmIfPhysClockSourcePriority_Object((1,3,6,1,4,1,9,9,45,1,1,1,17),_CiscoAtmIfPhysClockSourcePriority_Type())
ciscoAtmIfPhysClockSourcePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPhysClockSourcePriority.setStatus(_B)
class _CiscoAtmIfPhysClockSourceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notSelected',1),('selected',2)))
_CiscoAtmIfPhysClockSourceStatus_Type.__name__=_D
_CiscoAtmIfPhysClockSourceStatus_Object=MibTableColumn
ciscoAtmIfPhysClockSourceStatus=_CiscoAtmIfPhysClockSourceStatus_Object((1,3,6,1,4,1,9,9,45,1,1,1,18),_CiscoAtmIfPhysClockSourceStatus_Type())
ciscoAtmIfPhysClockSourceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysClockSourceStatus.setStatus(_B)
_CiscoAtmIfPhysDS1BitErrors_Type=Counter32
_CiscoAtmIfPhysDS1BitErrors_Object=MibTableColumn
ciscoAtmIfPhysDS1BitErrors=_CiscoAtmIfPhysDS1BitErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,19),_CiscoAtmIfPhysDS1BitErrors_Type())
ciscoAtmIfPhysDS1BitErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysDS1BitErrors.setStatus(_B)
_CiscoAtmIfPhysE1CrcErrors_Type=Counter32
_CiscoAtmIfPhysE1CrcErrors_Object=MibTableColumn
ciscoAtmIfPhysE1CrcErrors=_CiscoAtmIfPhysE1CrcErrors_Object((1,3,6,1,4,1,9,9,45,1,1,1,20),_CiscoAtmIfPhysE1CrcErrors_Type())
ciscoAtmIfPhysE1CrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoAtmIfPhysE1CrcErrors.setStatus(_B)
class _CiscoAtmIfPhysLineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ami',1),('b8zs',2),('hdb3',3)))
_CiscoAtmIfPhysLineCode_Type.__name__=_D
_CiscoAtmIfPhysLineCode_Object=MibTableColumn
ciscoAtmIfPhysLineCode=_CiscoAtmIfPhysLineCode_Object((1,3,6,1,4,1,9,9,45,1,1,1,21),_CiscoAtmIfPhysLineCode_Type())
ciscoAtmIfPhysLineCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ciscoAtmIfPhysLineCode.setStatus(_B)
_CiscoAtmIfPhysMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAtmIfPhysMIBConformance=_CiscoAtmIfPhysMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,45,3))
_CiscoAtmIfPhysMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAtmIfPhysMIBCompliances=_CiscoAtmIfPhysMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,45,3,1))
_CiscoAtmIfPhysMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAtmIfPhysMIBGroups=_CiscoAtmIfPhysMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,45,3,2))
ciscoAtmIfPhysMIBCommonGroup=ObjectGroup((1,3,6,1,4,1,9,9,45,3,2,1))
ciscoAtmIfPhysMIBCommonGroup.setObjects((_A,_P))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBCommonGroup.setStatus(_B)
ciscoAtmIfPhysMIBSonetGroup=ObjectGroup((1,3,6,1,4,1,9,9,45,3,2,2))
ciscoAtmIfPhysMIBSonetGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBSonetGroup.setStatus(_B)
ciscoAtmIfPhysMIBDs3E3Group=ObjectGroup((1,3,6,1,4,1,9,9,45,3,2,3))
ciscoAtmIfPhysMIBDs3E3Group.setObjects(*((_A,_G),(_A,_T),(_A,_U),(_A,_H)))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBDs3E3Group.setStatus(_B)
ciscoAtmIfPhysMIBCommonGroup2=ObjectGroup((1,3,6,1,4,1,9,9,45,3,2,4))
ciscoAtmIfPhysMIBCommonGroup2.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBCommonGroup2.setStatus(_B)
ciscoAtmIfPhysMIBSonetGroup2=ObjectGroup((1,3,6,1,4,1,9,9,45,3,2,5))
ciscoAtmIfPhysMIBSonetGroup2.setObjects(*((_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBSonetGroup2.setStatus(_B)
ciscoAtmIfPhysMIBDs3Group=ObjectGroup((1,3,6,1,4,1,9,9,45,3,2,6))
ciscoAtmIfPhysMIBDs3Group.setObjects((_A,_e))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBDs3Group.setStatus(_B)
ciscoAtmIfPhysMIBDs1E1Group=ObjectGroup((1,3,6,1,4,1,9,9,45,3,2,7))
ciscoAtmIfPhysMIBDs1E1Group.setObjects(*((_A,_G),(_A,_H),(_A,_f)))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBDs1E1Group.setStatus(_B)
ciscoAtmIfPhysMIBDs1Group=ObjectGroup((1,3,6,1,4,1,9,9,45,3,2,8))
ciscoAtmIfPhysMIBDs1Group.setObjects((_A,_g))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBDs1Group.setStatus(_B)
ciscoAtmIfPhysMIBE1Group=ObjectGroup((1,3,6,1,4,1,9,9,45,3,2,9))
ciscoAtmIfPhysMIBE1Group.setObjects((_A,_h))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBE1Group.setStatus(_B)
ciscoAtmIfPhysMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,45,3,1,1))
ciscoAtmIfPhysMIBCompliance.setObjects((_A,_F))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBCompliance.setStatus(_i)
ciscoAtmIfPhysMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,45,3,1,2))
ciscoAtmIfPhysMIBCompliance2.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBCompliance2.setStatus(_i)
ciscoAtmIfPhysMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,45,3,1,3))
ciscoAtmIfPhysMIBCompliance3.setObjects(*((_A,_F),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:ciscoAtmIfPhysMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoAtmIfPhysMIB':ciscoAtmIfPhysMIB,'ciscoAtmIfPhysMIBObjects':ciscoAtmIfPhysMIBObjects,'ciscoAtmIfPhysTable':ciscoAtmIfPhysTable,'ciscoAtmIfPhysEntry':ciscoAtmIfPhysEntry,_P:ciscoAtmIfPhysStatus,_Q:ciscoAtmIfPhysSectionParityErrors,_R:ciscoAtmIfPhysLineParityErrors,_S:ciscoAtmIfPhysPathParityErrors,_G:ciscoAtmIfPhysLcvErrors,_T:ciscoAtmIfPhysCBitParityErrors,_U:ciscoAtmIfPhysPBitParityErrors,_H:ciscoAtmIfPhysPlcpBipViolations,_b:ciscoAtmIfPhysLineFebeErrors,_c:ciscoAtmIfPhysPathFebeErrors,_V:ciscoAtmIfPhysCellPayloadScrambling,_d:ciscoAtmIfPhysStsStreamScrambling,_W:ciscoAtmIfPhysFramingMode,_X:ciscoAtmIfPhysLoopbackConfig,_e:ciscoAtmIfPhysLineBuildOut,_Y:ciscoAtmIfPhysTransmitClockSource,_Z:ciscoAtmIfPhysClockSourcePriority,_a:ciscoAtmIfPhysClockSourceStatus,_g:ciscoAtmIfPhysDS1BitErrors,_h:ciscoAtmIfPhysE1CrcErrors,_f:ciscoAtmIfPhysLineCode,'ciscoAtmIfPhysMIBConformance':ciscoAtmIfPhysMIBConformance,'ciscoAtmIfPhysMIBCompliances':ciscoAtmIfPhysMIBCompliances,'ciscoAtmIfPhysMIBCompliance':ciscoAtmIfPhysMIBCompliance,'ciscoAtmIfPhysMIBCompliance2':ciscoAtmIfPhysMIBCompliance2,'ciscoAtmIfPhysMIBCompliance3':ciscoAtmIfPhysMIBCompliance3,'ciscoAtmIfPhysMIBGroups':ciscoAtmIfPhysMIBGroups,_F:ciscoAtmIfPhysMIBCommonGroup,_J:ciscoAtmIfPhysMIBSonetGroup,_L:ciscoAtmIfPhysMIBDs3E3Group,_I:ciscoAtmIfPhysMIBCommonGroup2,_K:ciscoAtmIfPhysMIBSonetGroup2,_M:ciscoAtmIfPhysMIBDs3Group,_j:ciscoAtmIfPhysMIBDs1E1Group,_k:ciscoAtmIfPhysMIBDs1Group,_l:ciscoAtmIfPhysMIBE1Group})