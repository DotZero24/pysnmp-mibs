_x='alaPPPoEIAStatsGroup'
_w='alaPPPoEIAPortConfigGroup'
_v='alaPPPoEIAGlobalConfigGroup'
_u='alaPPPoEIAStatsPADSRxDiscardCounter'
_t='alaPPPoEIAStatsPADORxDiscardCounter'
_s='alaPPPoEIAStatsPADTRxDiscardCounter'
_r='alaPPPoEIAStatsPADRRxDiscardCounter'
_q='alaPPPoEIAStatsPADIRxDiscardCounter'
_p='alaPPPoEIAStatsPADTRxCounter'
_o='alaPPPoEIAStatsPADRRxCounter'
_n='alaPPPoEIAStatsPADIRxCounter'
_m='alaPPPoEIAStatsClearStats'
_l='alaPPPoEIAPortConfigTrustMode'
_k='alaPPPoEIAPortConfigStatus'
_j='alaPPPoEIAGlobalClearStats'
_i='alaPPPoEIAGlobalRemoteIDStringValue'
_h='alaPPPoEIAGlobalRemoteIDFormatType'
_g='alaPPPoEIAGlobalCircuitIDDelimiter'
_f='alaPPPoEIAGlobalCircuitIDField5StrVal'
_e='alaPPPoEIAGlobalCircuitIDField5'
_d='alaPPPoEIAGlobalCircuitIDField4StrVal'
_c='alaPPPoEIAGlobalCircuitIDField4'
_b='alaPPPoEIAGlobalCircuitIDField3StrVal'
_a='alaPPPoEIAGlobalCircuitIDField3'
_Z='alaPPPoEIAGlobalCircuitIDField2StrVal'
_Y='alaPPPoEIAGlobalCircuitIDField2'
_X='alaPPPoEIAGlobalCircuitIDField1StrVal'
_W='alaPPPoEIAGlobalCircuitIDField1'
_V='alaPPPoEIAGlobalCircuitIDFormatType'
_U='alaPPPoEIAGlobalAccessNodeIDStringValue'
_T='alaPPPoEIAGlobalAccessNodeIDFormatType'
_S='alaPPPoEIAGlobalStatus'
_R='alaPPPoEIAStatsIfIndex'
_Q='not-accessible'
_P='alaPPPoEIAPortConfigIfIndex'
_O='mgnt-address'
_N='disable'
_M='enable'
_L='OctetString'
_K='default'
_J='user-string'
_I='system-name'
_H='base-mac'
_G='PPPoEIACircuitIDFieldType'
_F='read-only'
_E='SnmpAdminString'
_D='Integer32'
_C='read-write'
_B='ALCATEL-IND1-PPPOEIA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1PPPoEIA,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1PPPoEIA')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1PPPoEIAMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,64,1))
if mibBuilder.loadTexts:alcatelIND1PPPoEIAMIB.setRevisions(('2011-01-24 00:00',))
class PPPoEIACircuitIDFieldType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',0),(_H,1),(_I,2),(_J,3),('interface-alias',4),('vlan',5),('interface',6),('cvlan',7)))
_AlcatelIND1PPPoEIAMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1PPPoEIAMIBObjects=_AlcatelIND1PPPoEIAMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,64,1,1))
if mibBuilder.loadTexts:alcatelIND1PPPoEIAMIBObjects.setStatus(_A)
class _AlaPPPoEIAGlobalStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_AlaPPPoEIAGlobalStatus_Type.__name__=_D
_AlaPPPoEIAGlobalStatus_Object=MibScalar
alaPPPoEIAGlobalStatus=_AlaPPPoEIAGlobalStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,1),_AlaPPPoEIAGlobalStatus_Type())
alaPPPoEIAGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalStatus.setStatus(_A)
class _AlaPPPoEIAGlobalAccessNodeIDFormatType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_O,3),(_J,4)))
_AlaPPPoEIAGlobalAccessNodeIDFormatType_Type.__name__=_D
_AlaPPPoEIAGlobalAccessNodeIDFormatType_Object=MibScalar
alaPPPoEIAGlobalAccessNodeIDFormatType=_AlaPPPoEIAGlobalAccessNodeIDFormatType_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,2),_AlaPPPoEIAGlobalAccessNodeIDFormatType_Type())
alaPPPoEIAGlobalAccessNodeIDFormatType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalAccessNodeIDFormatType.setStatus(_A)
class _AlaPPPoEIAGlobalAccessNodeIDStringValue_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaPPPoEIAGlobalAccessNodeIDStringValue_Type.__name__=_E
_AlaPPPoEIAGlobalAccessNodeIDStringValue_Object=MibScalar
alaPPPoEIAGlobalAccessNodeIDStringValue=_AlaPPPoEIAGlobalAccessNodeIDStringValue_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,3),_AlaPPPoEIAGlobalAccessNodeIDStringValue_Type())
alaPPPoEIAGlobalAccessNodeIDStringValue.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalAccessNodeIDStringValue.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDFormatType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('ascii',2),('atm',3)))
_AlaPPPoEIAGlobalCircuitIDFormatType_Type.__name__=_D
_AlaPPPoEIAGlobalCircuitIDFormatType_Object=MibScalar
alaPPPoEIAGlobalCircuitIDFormatType=_AlaPPPoEIAGlobalCircuitIDFormatType_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,4),_AlaPPPoEIAGlobalCircuitIDFormatType_Type())
alaPPPoEIAGlobalCircuitIDFormatType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDFormatType.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField1_Type(PPPoEIACircuitIDFieldType):defaultValue=0
_AlaPPPoEIAGlobalCircuitIDField1_Type.__name__=_G
_AlaPPPoEIAGlobalCircuitIDField1_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField1=_AlaPPPoEIAGlobalCircuitIDField1_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,5),_AlaPPPoEIAGlobalCircuitIDField1_Type())
alaPPPoEIAGlobalCircuitIDField1.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField1.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField1StrVal_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaPPPoEIAGlobalCircuitIDField1StrVal_Type.__name__=_E
_AlaPPPoEIAGlobalCircuitIDField1StrVal_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField1StrVal=_AlaPPPoEIAGlobalCircuitIDField1StrVal_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,6),_AlaPPPoEIAGlobalCircuitIDField1StrVal_Type())
alaPPPoEIAGlobalCircuitIDField1StrVal.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField1StrVal.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField2_Type(PPPoEIACircuitIDFieldType):defaultValue=0
_AlaPPPoEIAGlobalCircuitIDField2_Type.__name__=_G
_AlaPPPoEIAGlobalCircuitIDField2_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField2=_AlaPPPoEIAGlobalCircuitIDField2_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,7),_AlaPPPoEIAGlobalCircuitIDField2_Type())
alaPPPoEIAGlobalCircuitIDField2.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField2.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField2StrVal_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaPPPoEIAGlobalCircuitIDField2StrVal_Type.__name__=_E
_AlaPPPoEIAGlobalCircuitIDField2StrVal_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField2StrVal=_AlaPPPoEIAGlobalCircuitIDField2StrVal_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,8),_AlaPPPoEIAGlobalCircuitIDField2StrVal_Type())
alaPPPoEIAGlobalCircuitIDField2StrVal.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField2StrVal.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField3_Type(PPPoEIACircuitIDFieldType):defaultValue=0
_AlaPPPoEIAGlobalCircuitIDField3_Type.__name__=_G
_AlaPPPoEIAGlobalCircuitIDField3_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField3=_AlaPPPoEIAGlobalCircuitIDField3_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,9),_AlaPPPoEIAGlobalCircuitIDField3_Type())
alaPPPoEIAGlobalCircuitIDField3.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField3.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField3StrVal_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaPPPoEIAGlobalCircuitIDField3StrVal_Type.__name__=_E
_AlaPPPoEIAGlobalCircuitIDField3StrVal_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField3StrVal=_AlaPPPoEIAGlobalCircuitIDField3StrVal_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,10),_AlaPPPoEIAGlobalCircuitIDField3StrVal_Type())
alaPPPoEIAGlobalCircuitIDField3StrVal.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField3StrVal.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField4_Type(PPPoEIACircuitIDFieldType):defaultValue=0
_AlaPPPoEIAGlobalCircuitIDField4_Type.__name__=_G
_AlaPPPoEIAGlobalCircuitIDField4_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField4=_AlaPPPoEIAGlobalCircuitIDField4_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,11),_AlaPPPoEIAGlobalCircuitIDField4_Type())
alaPPPoEIAGlobalCircuitIDField4.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField4.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField4StrVal_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaPPPoEIAGlobalCircuitIDField4StrVal_Type.__name__=_E
_AlaPPPoEIAGlobalCircuitIDField4StrVal_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField4StrVal=_AlaPPPoEIAGlobalCircuitIDField4StrVal_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,12),_AlaPPPoEIAGlobalCircuitIDField4StrVal_Type())
alaPPPoEIAGlobalCircuitIDField4StrVal.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField4StrVal.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField5_Type(PPPoEIACircuitIDFieldType):defaultValue=0
_AlaPPPoEIAGlobalCircuitIDField5_Type.__name__=_G
_AlaPPPoEIAGlobalCircuitIDField5_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField5=_AlaPPPoEIAGlobalCircuitIDField5_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,13),_AlaPPPoEIAGlobalCircuitIDField5_Type())
alaPPPoEIAGlobalCircuitIDField5.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField5.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDField5StrVal_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaPPPoEIAGlobalCircuitIDField5StrVal_Type.__name__=_E
_AlaPPPoEIAGlobalCircuitIDField5StrVal_Object=MibScalar
alaPPPoEIAGlobalCircuitIDField5StrVal=_AlaPPPoEIAGlobalCircuitIDField5StrVal_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,14),_AlaPPPoEIAGlobalCircuitIDField5StrVal_Type())
alaPPPoEIAGlobalCircuitIDField5StrVal.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDField5StrVal.setStatus(_A)
class _AlaPPPoEIAGlobalCircuitIDDelimiter_Type(OctetString):defaultValue=OctetString(':');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_AlaPPPoEIAGlobalCircuitIDDelimiter_Type.__name__=_L
_AlaPPPoEIAGlobalCircuitIDDelimiter_Object=MibScalar
alaPPPoEIAGlobalCircuitIDDelimiter=_AlaPPPoEIAGlobalCircuitIDDelimiter_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,15),_AlaPPPoEIAGlobalCircuitIDDelimiter_Type())
alaPPPoEIAGlobalCircuitIDDelimiter.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalCircuitIDDelimiter.setStatus(_A)
class _AlaPPPoEIAGlobalRemoteIDFormatType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_I,2),(_O,3),(_J,4)))
_AlaPPPoEIAGlobalRemoteIDFormatType_Type.__name__=_D
_AlaPPPoEIAGlobalRemoteIDFormatType_Object=MibScalar
alaPPPoEIAGlobalRemoteIDFormatType=_AlaPPPoEIAGlobalRemoteIDFormatType_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,16),_AlaPPPoEIAGlobalRemoteIDFormatType_Type())
alaPPPoEIAGlobalRemoteIDFormatType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalRemoteIDFormatType.setStatus(_A)
class _AlaPPPoEIAGlobalRemoteIDStringValue_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlaPPPoEIAGlobalRemoteIDStringValue_Type.__name__=_E
_AlaPPPoEIAGlobalRemoteIDStringValue_Object=MibScalar
alaPPPoEIAGlobalRemoteIDStringValue=_AlaPPPoEIAGlobalRemoteIDStringValue_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,17),_AlaPPPoEIAGlobalRemoteIDStringValue_Type())
alaPPPoEIAGlobalRemoteIDStringValue.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalRemoteIDStringValue.setStatus(_A)
class _AlaPPPoEIAGlobalClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('reset',1)))
_AlaPPPoEIAGlobalClearStats_Type.__name__=_D
_AlaPPPoEIAGlobalClearStats_Object=MibScalar
alaPPPoEIAGlobalClearStats=_AlaPPPoEIAGlobalClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,18),_AlaPPPoEIAGlobalClearStats_Type())
alaPPPoEIAGlobalClearStats.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAGlobalClearStats.setStatus(_A)
_AlaPPPoEIAPortConfig_ObjectIdentity=ObjectIdentity
alaPPPoEIAPortConfig=_AlaPPPoEIAPortConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,19))
_AlaPPPoEIAPortConfigTable_Object=MibTable
alaPPPoEIAPortConfigTable=_AlaPPPoEIAPortConfigTable_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,19,1))
if mibBuilder.loadTexts:alaPPPoEIAPortConfigTable.setStatus(_A)
_AlaPPPoEIAPortConfigEntry_Object=MibTableRow
alaPPPoEIAPortConfigEntry=_AlaPPPoEIAPortConfigEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,19,1,1))
alaPPPoEIAPortConfigEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:alaPPPoEIAPortConfigEntry.setStatus(_A)
_AlaPPPoEIAPortConfigIfIndex_Type=InterfaceIndex
_AlaPPPoEIAPortConfigIfIndex_Object=MibTableColumn
alaPPPoEIAPortConfigIfIndex=_AlaPPPoEIAPortConfigIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,19,1,1,1),_AlaPPPoEIAPortConfigIfIndex_Type())
alaPPPoEIAPortConfigIfIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:alaPPPoEIAPortConfigIfIndex.setStatus(_A)
class _AlaPPPoEIAPortConfigStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_AlaPPPoEIAPortConfigStatus_Type.__name__=_D
_AlaPPPoEIAPortConfigStatus_Object=MibTableColumn
alaPPPoEIAPortConfigStatus=_AlaPPPoEIAPortConfigStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,19,1,1,2),_AlaPPPoEIAPortConfigStatus_Type())
alaPPPoEIAPortConfigStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAPortConfigStatus.setStatus(_A)
class _AlaPPPoEIAPortConfigTrustMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('client',1),('trusted',2)))
_AlaPPPoEIAPortConfigTrustMode_Type.__name__=_D
_AlaPPPoEIAPortConfigTrustMode_Object=MibTableColumn
alaPPPoEIAPortConfigTrustMode=_AlaPPPoEIAPortConfigTrustMode_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,19,1,1,3),_AlaPPPoEIAPortConfigTrustMode_Type())
alaPPPoEIAPortConfigTrustMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAPortConfigTrustMode.setStatus(_A)
_AlaPPPoEIAStats_ObjectIdentity=ObjectIdentity
alaPPPoEIAStats=_AlaPPPoEIAStats_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20))
_AlaPPPoEIAStatsTable_Object=MibTable
alaPPPoEIAStatsTable=_AlaPPPoEIAStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1))
if mibBuilder.loadTexts:alaPPPoEIAStatsTable.setStatus(_A)
_AlaPPPoEIAStatsEntry_Object=MibTableRow
alaPPPoEIAStatsEntry=_AlaPPPoEIAStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1))
alaPPPoEIAStatsEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:alaPPPoEIAStatsEntry.setStatus(_A)
_AlaPPPoEIAStatsIfIndex_Type=InterfaceIndex
_AlaPPPoEIAStatsIfIndex_Object=MibTableColumn
alaPPPoEIAStatsIfIndex=_AlaPPPoEIAStatsIfIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,1),_AlaPPPoEIAStatsIfIndex_Type())
alaPPPoEIAStatsIfIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:alaPPPoEIAStatsIfIndex.setStatus(_A)
class _AlaPPPoEIAStatsClearStats_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_K,0),('reset',1)))
_AlaPPPoEIAStatsClearStats_Type.__name__=_D
_AlaPPPoEIAStatsClearStats_Object=MibTableColumn
alaPPPoEIAStatsClearStats=_AlaPPPoEIAStatsClearStats_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,2),_AlaPPPoEIAStatsClearStats_Type())
alaPPPoEIAStatsClearStats.setMaxAccess(_C)
if mibBuilder.loadTexts:alaPPPoEIAStatsClearStats.setStatus(_A)
_AlaPPPoEIAStatsPADIRxCounter_Type=Counter32
_AlaPPPoEIAStatsPADIRxCounter_Object=MibTableColumn
alaPPPoEIAStatsPADIRxCounter=_AlaPPPoEIAStatsPADIRxCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,3),_AlaPPPoEIAStatsPADIRxCounter_Type())
alaPPPoEIAStatsPADIRxCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPPPoEIAStatsPADIRxCounter.setStatus(_A)
_AlaPPPoEIAStatsPADRRxCounter_Type=Counter32
_AlaPPPoEIAStatsPADRRxCounter_Object=MibTableColumn
alaPPPoEIAStatsPADRRxCounter=_AlaPPPoEIAStatsPADRRxCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,4),_AlaPPPoEIAStatsPADRRxCounter_Type())
alaPPPoEIAStatsPADRRxCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPPPoEIAStatsPADRRxCounter.setStatus(_A)
_AlaPPPoEIAStatsPADTRxCounter_Type=Counter32
_AlaPPPoEIAStatsPADTRxCounter_Object=MibTableColumn
alaPPPoEIAStatsPADTRxCounter=_AlaPPPoEIAStatsPADTRxCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,5),_AlaPPPoEIAStatsPADTRxCounter_Type())
alaPPPoEIAStatsPADTRxCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPPPoEIAStatsPADTRxCounter.setStatus(_A)
_AlaPPPoEIAStatsPADIRxDiscardCounter_Type=Counter32
_AlaPPPoEIAStatsPADIRxDiscardCounter_Object=MibTableColumn
alaPPPoEIAStatsPADIRxDiscardCounter=_AlaPPPoEIAStatsPADIRxDiscardCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,6),_AlaPPPoEIAStatsPADIRxDiscardCounter_Type())
alaPPPoEIAStatsPADIRxDiscardCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPPPoEIAStatsPADIRxDiscardCounter.setStatus(_A)
_AlaPPPoEIAStatsPADRRxDiscardCounter_Type=Counter32
_AlaPPPoEIAStatsPADRRxDiscardCounter_Object=MibTableColumn
alaPPPoEIAStatsPADRRxDiscardCounter=_AlaPPPoEIAStatsPADRRxDiscardCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,7),_AlaPPPoEIAStatsPADRRxDiscardCounter_Type())
alaPPPoEIAStatsPADRRxDiscardCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPPPoEIAStatsPADRRxDiscardCounter.setStatus(_A)
_AlaPPPoEIAStatsPADTRxDiscardCounter_Type=Counter32
_AlaPPPoEIAStatsPADTRxDiscardCounter_Object=MibTableColumn
alaPPPoEIAStatsPADTRxDiscardCounter=_AlaPPPoEIAStatsPADTRxDiscardCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,8),_AlaPPPoEIAStatsPADTRxDiscardCounter_Type())
alaPPPoEIAStatsPADTRxDiscardCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPPPoEIAStatsPADTRxDiscardCounter.setStatus(_A)
_AlaPPPoEIAStatsPADORxDiscardCounter_Type=Counter32
_AlaPPPoEIAStatsPADORxDiscardCounter_Object=MibTableColumn
alaPPPoEIAStatsPADORxDiscardCounter=_AlaPPPoEIAStatsPADORxDiscardCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,9),_AlaPPPoEIAStatsPADORxDiscardCounter_Type())
alaPPPoEIAStatsPADORxDiscardCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPPPoEIAStatsPADORxDiscardCounter.setStatus(_A)
_AlaPPPoEIAStatsPADSRxDiscardCounter_Type=Counter32
_AlaPPPoEIAStatsPADSRxDiscardCounter_Object=MibTableColumn
alaPPPoEIAStatsPADSRxDiscardCounter=_AlaPPPoEIAStatsPADSRxDiscardCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,64,1,1,20,1,1,10),_AlaPPPoEIAStatsPADSRxDiscardCounter_Type())
alaPPPoEIAStatsPADSRxDiscardCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:alaPPPoEIAStatsPADSRxDiscardCounter.setStatus(_A)
_AlcatelIND1PPPoEIAMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1PPPoEIAMIBConformance=_AlcatelIND1PPPoEIAMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,64,1,2))
if mibBuilder.loadTexts:alcatelIND1PPPoEIAMIBConformance.setStatus(_A)
_AlcatelIND1PPPoEIAMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1PPPoEIAMIBGroups=_AlcatelIND1PPPoEIAMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,64,1,2,1))
if mibBuilder.loadTexts:alcatelIND1PPPoEIAMIBGroups.setStatus(_A)
_AlcatelIND1PPPoEIAMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1PPPoEIAMIBCompliances=_AlcatelIND1PPPoEIAMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,64,1,2,2))
if mibBuilder.loadTexts:alcatelIND1PPPoEIAMIBCompliances.setStatus(_A)
alaPPPoEIAGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,64,1,2,1,1))
alaPPPoEIAGlobalConfigGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:alaPPPoEIAGlobalConfigGroup.setStatus(_A)
alaPPPoEIAPortConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,64,1,2,1,2))
alaPPPoEIAPortConfigGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:alaPPPoEIAPortConfigGroup.setStatus(_A)
alaPPPoEIAStatsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,64,1,2,1,3))
alaPPPoEIAStatsGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:alaPPPoEIAStatsGroup.setStatus(_A)
alcatelIND1PPPoEIAMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,64,1,2,2,1))
alcatelIND1PPPoEIAMIBCompliance.setObjects(*((_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:alcatelIND1PPPoEIAMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:PPPoEIACircuitIDFieldType,'alcatelIND1PPPoEIAMIB':alcatelIND1PPPoEIAMIB,'alcatelIND1PPPoEIAMIBObjects':alcatelIND1PPPoEIAMIBObjects,_S:alaPPPoEIAGlobalStatus,_T:alaPPPoEIAGlobalAccessNodeIDFormatType,_U:alaPPPoEIAGlobalAccessNodeIDStringValue,_V:alaPPPoEIAGlobalCircuitIDFormatType,_W:alaPPPoEIAGlobalCircuitIDField1,_X:alaPPPoEIAGlobalCircuitIDField1StrVal,_Y:alaPPPoEIAGlobalCircuitIDField2,_Z:alaPPPoEIAGlobalCircuitIDField2StrVal,_a:alaPPPoEIAGlobalCircuitIDField3,_b:alaPPPoEIAGlobalCircuitIDField3StrVal,_c:alaPPPoEIAGlobalCircuitIDField4,_d:alaPPPoEIAGlobalCircuitIDField4StrVal,_e:alaPPPoEIAGlobalCircuitIDField5,_f:alaPPPoEIAGlobalCircuitIDField5StrVal,_g:alaPPPoEIAGlobalCircuitIDDelimiter,_h:alaPPPoEIAGlobalRemoteIDFormatType,_i:alaPPPoEIAGlobalRemoteIDStringValue,_j:alaPPPoEIAGlobalClearStats,'alaPPPoEIAPortConfig':alaPPPoEIAPortConfig,'alaPPPoEIAPortConfigTable':alaPPPoEIAPortConfigTable,'alaPPPoEIAPortConfigEntry':alaPPPoEIAPortConfigEntry,_P:alaPPPoEIAPortConfigIfIndex,_k:alaPPPoEIAPortConfigStatus,_l:alaPPPoEIAPortConfigTrustMode,'alaPPPoEIAStats':alaPPPoEIAStats,'alaPPPoEIAStatsTable':alaPPPoEIAStatsTable,'alaPPPoEIAStatsEntry':alaPPPoEIAStatsEntry,_R:alaPPPoEIAStatsIfIndex,_m:alaPPPoEIAStatsClearStats,_n:alaPPPoEIAStatsPADIRxCounter,_o:alaPPPoEIAStatsPADRRxCounter,_p:alaPPPoEIAStatsPADTRxCounter,_q:alaPPPoEIAStatsPADIRxDiscardCounter,_r:alaPPPoEIAStatsPADRRxDiscardCounter,_s:alaPPPoEIAStatsPADTRxDiscardCounter,_t:alaPPPoEIAStatsPADORxDiscardCounter,_u:alaPPPoEIAStatsPADSRxDiscardCounter,'alcatelIND1PPPoEIAMIBConformance':alcatelIND1PPPoEIAMIBConformance,'alcatelIND1PPPoEIAMIBGroups':alcatelIND1PPPoEIAMIBGroups,_v:alaPPPoEIAGlobalConfigGroup,_w:alaPPPoEIAPortConfigGroup,_x:alaPPPoEIAStatsGroup,'alcatelIND1PPPoEIAMIBCompliances':alcatelIND1PPPoEIAMIBCompliances,'alcatelIND1PPPoEIAMIBCompliance':alcatelIND1PPPoEIAMIBCompliance})