_u='etsysWpaBaseGroup'
_t='etsysWPAStatsTKIPCounterMeasuresInvoked'
_s='etsysWPAStatsTKIPRemoteMICFailures'
_r='etsysWPAStatsTKIPLocalMICFailures'
_q='etsysWPAStatsTKIPICVErrors'
_p='etsysWPAStatsSelectedUnicastCipher'
_o='etsysWPAStatsVersion'
_n='etsysWPAStatsSTAAddress'
_m='etsysWPAConfigAuthenticationSuiteEnabled'
_l='etsysWPAConfigAuthenticationSuite'
_k='etsysWPAConfigUnicastCipherEnabled'
_j='etsysWPAConfigUnicastCipher'
_i='etsysWPAConfigRekeyPairwiseWEP'
_h='etsysWPAConfigAllowLegacyClients'
_g='etsysWPAConfigLegacyOptionSupported'
_f='etsysWPAConfigPairwiseUpdateCount'
_e='etsysWPAConfigPairwiseUpdateTimeOut'
_d='etsysWPAConfigGroupUpdateCount'
_c='etsysWPAConfigGroupUpdateTimeOut'
_b='etsysWPAConfigGroupMasterRekeyTime'
_a='etsysWPAConfigPSKPassPhrase'
_Z='etsysWPAConfigMultipleAuthSuitesSupported'
_Y='etsysWPAConfigPSKValueEntered'
_X='etsysWPAConfigPSKValue'
_W='etsysWPAConfigGroupRekeyStrict'
_V='etsysWPAConfigGroupRekeyPackets'
_U='etsysWPAConfigGroupRekeyTime'
_T='etsysWPAConfigGroupRekeyMethod'
_S='etsysWPAConfigMulticastCipher'
_R='etsysWPAConfigPairwiseKeysSupported'
_Q='etsysWPAConfigVersion'
_P='etsysWPAConfigTKIPNumberOfReplayCounters'
_O='etsysWPAConfigEnabled'
_N='etsysWPAConfigOptionImplemented'
_M='etsysWPAStatsIndex'
_L='etsysWPAConfigAuthenticationSuiteIndex'
_K='etsysWPAConfigUnicastCipherIndex'
_J='Integer32'
_I='seconds'
_H='not-accessible'
_G='etsysWPAConfigIndex'
_F='OctetString'
_E='Unsigned32'
_D='read-only'
_C='read-write'
_B='ENTERASYS-WIFI-PROTECTED-ACCESS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
etsysWiFiProtectedAccessMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,32))
if mibBuilder.loadTexts:etsysWiFiProtectedAccessMIB.setRevisions(('2003-11-06 15:15','2003-08-07 17:08'))
_EtsysWiFiProtectedAccessObjects_ObjectIdentity=ObjectIdentity
etsysWiFiProtectedAccessObjects=_EtsysWiFiProtectedAccessObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,32,1))
_EtsysWPAConfigTable_Object=MibTable
etsysWPAConfigTable=_EtsysWPAConfigTable_Object((1,3,6,1,4,1,5624,1,2,32,1,1))
if mibBuilder.loadTexts:etsysWPAConfigTable.setStatus(_A)
_EtsysWPAConfigEntry_Object=MibTableRow
etsysWPAConfigEntry=_EtsysWPAConfigEntry_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1))
etsysWPAConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:etsysWPAConfigEntry.setStatus(_A)
class _EtsysWPAConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EtsysWPAConfigIndex_Type.__name__=_J
_EtsysWPAConfigIndex_Object=MibTableColumn
etsysWPAConfigIndex=_EtsysWPAConfigIndex_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,1),_EtsysWPAConfigIndex_Type())
etsysWPAConfigIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysWPAConfigIndex.setStatus(_A)
_EtsysWPAConfigOptionImplemented_Type=TruthValue
_EtsysWPAConfigOptionImplemented_Object=MibTableColumn
etsysWPAConfigOptionImplemented=_EtsysWPAConfigOptionImplemented_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,2),_EtsysWPAConfigOptionImplemented_Type())
etsysWPAConfigOptionImplemented.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAConfigOptionImplemented.setStatus(_A)
_EtsysWPAConfigEnabled_Type=TruthValue
_EtsysWPAConfigEnabled_Object=MibTableColumn
etsysWPAConfigEnabled=_EtsysWPAConfigEnabled_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,3),_EtsysWPAConfigEnabled_Type())
etsysWPAConfigEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigEnabled.setStatus(_A)
_EtsysWPAConfigTKIPNumberOfReplayCounters_Type=Integer32
_EtsysWPAConfigTKIPNumberOfReplayCounters_Object=MibTableColumn
etsysWPAConfigTKIPNumberOfReplayCounters=_EtsysWPAConfigTKIPNumberOfReplayCounters_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,4),_EtsysWPAConfigTKIPNumberOfReplayCounters_Type())
etsysWPAConfigTKIPNumberOfReplayCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAConfigTKIPNumberOfReplayCounters.setStatus(_A)
_EtsysWPAConfigVersion_Type=Integer32
_EtsysWPAConfigVersion_Object=MibTableColumn
etsysWPAConfigVersion=_EtsysWPAConfigVersion_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,5),_EtsysWPAConfigVersion_Type())
etsysWPAConfigVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAConfigVersion.setStatus(_A)
class _EtsysWPAConfigPairwiseKeysSupported_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_EtsysWPAConfigPairwiseKeysSupported_Type.__name__=_E
_EtsysWPAConfigPairwiseKeysSupported_Object=MibTableColumn
etsysWPAConfigPairwiseKeysSupported=_EtsysWPAConfigPairwiseKeysSupported_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,6),_EtsysWPAConfigPairwiseKeysSupported_Type())
etsysWPAConfigPairwiseKeysSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAConfigPairwiseKeysSupported.setStatus(_A)
class _EtsysWPAConfigMulticastCipher_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_EtsysWPAConfigMulticastCipher_Type.__name__=_F
_EtsysWPAConfigMulticastCipher_Object=MibTableColumn
etsysWPAConfigMulticastCipher=_EtsysWPAConfigMulticastCipher_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,7),_EtsysWPAConfigMulticastCipher_Type())
etsysWPAConfigMulticastCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigMulticastCipher.setStatus(_A)
class _EtsysWPAConfigGroupRekeyMethod_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),('timeBased',2),('packetBased',3)))
_EtsysWPAConfigGroupRekeyMethod_Type.__name__=_J
_EtsysWPAConfigGroupRekeyMethod_Object=MibTableColumn
etsysWPAConfigGroupRekeyMethod=_EtsysWPAConfigGroupRekeyMethod_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,8),_EtsysWPAConfigGroupRekeyMethod_Type())
etsysWPAConfigGroupRekeyMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigGroupRekeyMethod.setStatus(_A)
class _EtsysWPAConfigGroupRekeyTime_Type(Unsigned32):defaultValue=86400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAConfigGroupRekeyTime_Type.__name__=_E
_EtsysWPAConfigGroupRekeyTime_Object=MibTableColumn
etsysWPAConfigGroupRekeyTime=_EtsysWPAConfigGroupRekeyTime_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,9),_EtsysWPAConfigGroupRekeyTime_Type())
etsysWPAConfigGroupRekeyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigGroupRekeyTime.setStatus(_A)
if mibBuilder.loadTexts:etsysWPAConfigGroupRekeyTime.setUnits(_I)
class _EtsysWPAConfigGroupRekeyPackets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAConfigGroupRekeyPackets_Type.__name__=_E
_EtsysWPAConfigGroupRekeyPackets_Object=MibTableColumn
etsysWPAConfigGroupRekeyPackets=_EtsysWPAConfigGroupRekeyPackets_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,10),_EtsysWPAConfigGroupRekeyPackets_Type())
etsysWPAConfigGroupRekeyPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigGroupRekeyPackets.setStatus(_A)
if mibBuilder.loadTexts:etsysWPAConfigGroupRekeyPackets.setUnits('1000 packets')
_EtsysWPAConfigGroupRekeyStrict_Type=TruthValue
_EtsysWPAConfigGroupRekeyStrict_Object=MibTableColumn
etsysWPAConfigGroupRekeyStrict=_EtsysWPAConfigGroupRekeyStrict_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,11),_EtsysWPAConfigGroupRekeyStrict_Type())
etsysWPAConfigGroupRekeyStrict.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigGroupRekeyStrict.setStatus(_A)
class _EtsysWPAConfigPSKValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_EtsysWPAConfigPSKValue_Type.__name__=_F
_EtsysWPAConfigPSKValue_Object=MibTableColumn
etsysWPAConfigPSKValue=_EtsysWPAConfigPSKValue_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,12),_EtsysWPAConfigPSKValue_Type())
etsysWPAConfigPSKValue.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigPSKValue.setStatus(_A)
_EtsysWPAConfigPSKPassPhrase_Type=DisplayString
_EtsysWPAConfigPSKPassPhrase_Object=MibTableColumn
etsysWPAConfigPSKPassPhrase=_EtsysWPAConfigPSKPassPhrase_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,13),_EtsysWPAConfigPSKPassPhrase_Type())
etsysWPAConfigPSKPassPhrase.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigPSKPassPhrase.setStatus(_A)
_EtsysWPAConfigPSKValueEntered_Type=TruthValue
_EtsysWPAConfigPSKValueEntered_Object=MibTableColumn
etsysWPAConfigPSKValueEntered=_EtsysWPAConfigPSKValueEntered_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,14),_EtsysWPAConfigPSKValueEntered_Type())
etsysWPAConfigPSKValueEntered.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAConfigPSKValueEntered.setStatus(_A)
_EtsysWPAConfigMultipleAuthSuitesSupported_Type=TruthValue
_EtsysWPAConfigMultipleAuthSuitesSupported_Object=MibTableColumn
etsysWPAConfigMultipleAuthSuitesSupported=_EtsysWPAConfigMultipleAuthSuitesSupported_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,15),_EtsysWPAConfigMultipleAuthSuitesSupported_Type())
etsysWPAConfigMultipleAuthSuitesSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAConfigMultipleAuthSuitesSupported.setStatus(_A)
class _EtsysWPAConfigGroupMasterRekeyTime_Type(Unsigned32):defaultValue=604800;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAConfigGroupMasterRekeyTime_Type.__name__=_E
_EtsysWPAConfigGroupMasterRekeyTime_Object=MibTableColumn
etsysWPAConfigGroupMasterRekeyTime=_EtsysWPAConfigGroupMasterRekeyTime_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,16),_EtsysWPAConfigGroupMasterRekeyTime_Type())
etsysWPAConfigGroupMasterRekeyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigGroupMasterRekeyTime.setStatus(_A)
if mibBuilder.loadTexts:etsysWPAConfigGroupMasterRekeyTime.setUnits(_I)
class _EtsysWPAConfigGroupUpdateTimeOut_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAConfigGroupUpdateTimeOut_Type.__name__=_E
_EtsysWPAConfigGroupUpdateTimeOut_Object=MibTableColumn
etsysWPAConfigGroupUpdateTimeOut=_EtsysWPAConfigGroupUpdateTimeOut_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,17),_EtsysWPAConfigGroupUpdateTimeOut_Type())
etsysWPAConfigGroupUpdateTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigGroupUpdateTimeOut.setStatus(_A)
if mibBuilder.loadTexts:etsysWPAConfigGroupUpdateTimeOut.setUnits(_I)
class _EtsysWPAConfigGroupUpdateCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAConfigGroupUpdateCount_Type.__name__=_E
_EtsysWPAConfigGroupUpdateCount_Object=MibTableColumn
etsysWPAConfigGroupUpdateCount=_EtsysWPAConfigGroupUpdateCount_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,18),_EtsysWPAConfigGroupUpdateCount_Type())
etsysWPAConfigGroupUpdateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigGroupUpdateCount.setStatus(_A)
class _EtsysWPAConfigPairwiseUpdateTimeOut_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAConfigPairwiseUpdateTimeOut_Type.__name__=_E
_EtsysWPAConfigPairwiseUpdateTimeOut_Object=MibTableColumn
etsysWPAConfigPairwiseUpdateTimeOut=_EtsysWPAConfigPairwiseUpdateTimeOut_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,19),_EtsysWPAConfigPairwiseUpdateTimeOut_Type())
etsysWPAConfigPairwiseUpdateTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigPairwiseUpdateTimeOut.setStatus(_A)
if mibBuilder.loadTexts:etsysWPAConfigPairwiseUpdateTimeOut.setUnits(_I)
class _EtsysWPAConfigPairwiseUpdateCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAConfigPairwiseUpdateCount_Type.__name__=_E
_EtsysWPAConfigPairwiseUpdateCount_Object=MibTableColumn
etsysWPAConfigPairwiseUpdateCount=_EtsysWPAConfigPairwiseUpdateCount_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,20),_EtsysWPAConfigPairwiseUpdateCount_Type())
etsysWPAConfigPairwiseUpdateCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigPairwiseUpdateCount.setStatus(_A)
_EtsysWPAConfigLegacyOptionSupported_Type=TruthValue
_EtsysWPAConfigLegacyOptionSupported_Object=MibTableColumn
etsysWPAConfigLegacyOptionSupported=_EtsysWPAConfigLegacyOptionSupported_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,21),_EtsysWPAConfigLegacyOptionSupported_Type())
etsysWPAConfigLegacyOptionSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAConfigLegacyOptionSupported.setStatus(_A)
_EtsysWPAConfigAllowLegacyClients_Type=TruthValue
_EtsysWPAConfigAllowLegacyClients_Object=MibTableColumn
etsysWPAConfigAllowLegacyClients=_EtsysWPAConfigAllowLegacyClients_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,22),_EtsysWPAConfigAllowLegacyClients_Type())
etsysWPAConfigAllowLegacyClients.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigAllowLegacyClients.setStatus(_A)
_EtsysWPAConfigRekeyPairwiseWEP_Type=TruthValue
_EtsysWPAConfigRekeyPairwiseWEP_Object=MibTableColumn
etsysWPAConfigRekeyPairwiseWEP=_EtsysWPAConfigRekeyPairwiseWEP_Object((1,3,6,1,4,1,5624,1,2,32,1,1,1,23),_EtsysWPAConfigRekeyPairwiseWEP_Type())
etsysWPAConfigRekeyPairwiseWEP.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigRekeyPairwiseWEP.setStatus(_A)
_EtsysWPAConfigUnicastCiphersTable_Object=MibTable
etsysWPAConfigUnicastCiphersTable=_EtsysWPAConfigUnicastCiphersTable_Object((1,3,6,1,4,1,5624,1,2,32,1,2))
if mibBuilder.loadTexts:etsysWPAConfigUnicastCiphersTable.setStatus(_A)
_EtsysWPAConfigUnicastCiphersEntry_Object=MibTableRow
etsysWPAConfigUnicastCiphersEntry=_EtsysWPAConfigUnicastCiphersEntry_Object((1,3,6,1,4,1,5624,1,2,32,1,2,1))
etsysWPAConfigUnicastCiphersEntry.setIndexNames((0,_B,_G),(0,_B,_K))
if mibBuilder.loadTexts:etsysWPAConfigUnicastCiphersEntry.setStatus(_A)
class _EtsysWPAConfigUnicastCipherIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAConfigUnicastCipherIndex_Type.__name__=_E
_EtsysWPAConfigUnicastCipherIndex_Object=MibTableColumn
etsysWPAConfigUnicastCipherIndex=_EtsysWPAConfigUnicastCipherIndex_Object((1,3,6,1,4,1,5624,1,2,32,1,2,1,1),_EtsysWPAConfigUnicastCipherIndex_Type())
etsysWPAConfigUnicastCipherIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysWPAConfigUnicastCipherIndex.setStatus(_A)
class _EtsysWPAConfigUnicastCipher_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_EtsysWPAConfigUnicastCipher_Type.__name__=_F
_EtsysWPAConfigUnicastCipher_Object=MibTableColumn
etsysWPAConfigUnicastCipher=_EtsysWPAConfigUnicastCipher_Object((1,3,6,1,4,1,5624,1,2,32,1,2,1,2),_EtsysWPAConfigUnicastCipher_Type())
etsysWPAConfigUnicastCipher.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAConfigUnicastCipher.setStatus(_A)
_EtsysWPAConfigUnicastCipherEnabled_Type=TruthValue
_EtsysWPAConfigUnicastCipherEnabled_Object=MibTableColumn
etsysWPAConfigUnicastCipherEnabled=_EtsysWPAConfigUnicastCipherEnabled_Object((1,3,6,1,4,1,5624,1,2,32,1,2,1,3),_EtsysWPAConfigUnicastCipherEnabled_Type())
etsysWPAConfigUnicastCipherEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigUnicastCipherEnabled.setStatus(_A)
_EtsysWPAConfigAuthenticationSuitesTable_Object=MibTable
etsysWPAConfigAuthenticationSuitesTable=_EtsysWPAConfigAuthenticationSuitesTable_Object((1,3,6,1,4,1,5624,1,2,32,1,3))
if mibBuilder.loadTexts:etsysWPAConfigAuthenticationSuitesTable.setStatus(_A)
_EtsysWPAConfigAuthenticationSuitesEntry_Object=MibTableRow
etsysWPAConfigAuthenticationSuitesEntry=_EtsysWPAConfigAuthenticationSuitesEntry_Object((1,3,6,1,4,1,5624,1,2,32,1,3,1))
etsysWPAConfigAuthenticationSuitesEntry.setIndexNames((0,_B,_G),(0,_B,_L))
if mibBuilder.loadTexts:etsysWPAConfigAuthenticationSuitesEntry.setStatus(_A)
class _EtsysWPAConfigAuthenticationSuiteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAConfigAuthenticationSuiteIndex_Type.__name__=_E
_EtsysWPAConfigAuthenticationSuiteIndex_Object=MibTableColumn
etsysWPAConfigAuthenticationSuiteIndex=_EtsysWPAConfigAuthenticationSuiteIndex_Object((1,3,6,1,4,1,5624,1,2,32,1,3,1,1),_EtsysWPAConfigAuthenticationSuiteIndex_Type())
etsysWPAConfigAuthenticationSuiteIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysWPAConfigAuthenticationSuiteIndex.setStatus(_A)
class _EtsysWPAConfigAuthenticationSuite_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_EtsysWPAConfigAuthenticationSuite_Type.__name__=_F
_EtsysWPAConfigAuthenticationSuite_Object=MibTableColumn
etsysWPAConfigAuthenticationSuite=_EtsysWPAConfigAuthenticationSuite_Object((1,3,6,1,4,1,5624,1,2,32,1,3,1,2),_EtsysWPAConfigAuthenticationSuite_Type())
etsysWPAConfigAuthenticationSuite.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAConfigAuthenticationSuite.setStatus(_A)
_EtsysWPAConfigAuthenticationSuiteEnabled_Type=TruthValue
_EtsysWPAConfigAuthenticationSuiteEnabled_Object=MibTableColumn
etsysWPAConfigAuthenticationSuiteEnabled=_EtsysWPAConfigAuthenticationSuiteEnabled_Object((1,3,6,1,4,1,5624,1,2,32,1,3,1,3),_EtsysWPAConfigAuthenticationSuiteEnabled_Type())
etsysWPAConfigAuthenticationSuiteEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysWPAConfigAuthenticationSuiteEnabled.setStatus(_A)
_EtsysWPAStatsTable_Object=MibTable
etsysWPAStatsTable=_EtsysWPAStatsTable_Object((1,3,6,1,4,1,5624,1,2,32,1,4))
if mibBuilder.loadTexts:etsysWPAStatsTable.setStatus(_A)
_EtsysWPAStatsEntry_Object=MibTableRow
etsysWPAStatsEntry=_EtsysWPAStatsEntry_Object((1,3,6,1,4,1,5624,1,2,32,1,4,1))
etsysWPAStatsEntry.setIndexNames((0,_B,_G),(0,_B,_M))
if mibBuilder.loadTexts:etsysWPAStatsEntry.setStatus(_A)
class _EtsysWPAStatsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAStatsIndex_Type.__name__=_E
_EtsysWPAStatsIndex_Object=MibTableColumn
etsysWPAStatsIndex=_EtsysWPAStatsIndex_Object((1,3,6,1,4,1,5624,1,2,32,1,4,1,1),_EtsysWPAStatsIndex_Type())
etsysWPAStatsIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysWPAStatsIndex.setStatus(_A)
_EtsysWPAStatsSTAAddress_Type=MacAddress
_EtsysWPAStatsSTAAddress_Object=MibTableColumn
etsysWPAStatsSTAAddress=_EtsysWPAStatsSTAAddress_Object((1,3,6,1,4,1,5624,1,2,32,1,4,1,2),_EtsysWPAStatsSTAAddress_Type())
etsysWPAStatsSTAAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAStatsSTAAddress.setStatus(_A)
class _EtsysWPAStatsVersion_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EtsysWPAStatsVersion_Type.__name__=_E
_EtsysWPAStatsVersion_Object=MibTableColumn
etsysWPAStatsVersion=_EtsysWPAStatsVersion_Object((1,3,6,1,4,1,5624,1,2,32,1,4,1,3),_EtsysWPAStatsVersion_Type())
etsysWPAStatsVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAStatsVersion.setStatus(_A)
class _EtsysWPAStatsSelectedUnicastCipher_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_EtsysWPAStatsSelectedUnicastCipher_Type.__name__=_F
_EtsysWPAStatsSelectedUnicastCipher_Object=MibTableColumn
etsysWPAStatsSelectedUnicastCipher=_EtsysWPAStatsSelectedUnicastCipher_Object((1,3,6,1,4,1,5624,1,2,32,1,4,1,4),_EtsysWPAStatsSelectedUnicastCipher_Type())
etsysWPAStatsSelectedUnicastCipher.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAStatsSelectedUnicastCipher.setStatus(_A)
_EtsysWPAStatsTKIPICVErrors_Type=Counter32
_EtsysWPAStatsTKIPICVErrors_Object=MibTableColumn
etsysWPAStatsTKIPICVErrors=_EtsysWPAStatsTKIPICVErrors_Object((1,3,6,1,4,1,5624,1,2,32,1,4,1,5),_EtsysWPAStatsTKIPICVErrors_Type())
etsysWPAStatsTKIPICVErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAStatsTKIPICVErrors.setStatus(_A)
_EtsysWPAStatsTKIPLocalMICFailures_Type=Counter32
_EtsysWPAStatsTKIPLocalMICFailures_Object=MibTableColumn
etsysWPAStatsTKIPLocalMICFailures=_EtsysWPAStatsTKIPLocalMICFailures_Object((1,3,6,1,4,1,5624,1,2,32,1,4,1,6),_EtsysWPAStatsTKIPLocalMICFailures_Type())
etsysWPAStatsTKIPLocalMICFailures.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAStatsTKIPLocalMICFailures.setStatus(_A)
_EtsysWPAStatsTKIPRemoteMICFailures_Type=Counter32
_EtsysWPAStatsTKIPRemoteMICFailures_Object=MibTableColumn
etsysWPAStatsTKIPRemoteMICFailures=_EtsysWPAStatsTKIPRemoteMICFailures_Object((1,3,6,1,4,1,5624,1,2,32,1,4,1,7),_EtsysWPAStatsTKIPRemoteMICFailures_Type())
etsysWPAStatsTKIPRemoteMICFailures.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAStatsTKIPRemoteMICFailures.setStatus(_A)
_EtsysWPAStatsTKIPCounterMeasuresInvoked_Type=Counter32
_EtsysWPAStatsTKIPCounterMeasuresInvoked_Object=MibTableColumn
etsysWPAStatsTKIPCounterMeasuresInvoked=_EtsysWPAStatsTKIPCounterMeasuresInvoked_Object((1,3,6,1,4,1,5624,1,2,32,1,4,1,8),_EtsysWPAStatsTKIPCounterMeasuresInvoked_Type())
etsysWPAStatsTKIPCounterMeasuresInvoked.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysWPAStatsTKIPCounterMeasuresInvoked.setStatus(_A)
_EtsysWpaConformance_ObjectIdentity=ObjectIdentity
etsysWpaConformance=_EtsysWpaConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,32,2))
_EtsysWpaGroups_ObjectIdentity=ObjectIdentity
etsysWpaGroups=_EtsysWpaGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,32,2,1))
_EtsysWpaCompliances_ObjectIdentity=ObjectIdentity
etsysWpaCompliances=_EtsysWpaCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,32,2,2))
etsysWpaBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,32,2,1,1))
etsysWpaBaseGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:etsysWpaBaseGroup.setStatus(_A)
etsysWpaUnicastCipherGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,32,2,1,2))
etsysWpaUnicastCipherGroup.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:etsysWpaUnicastCipherGroup.setStatus(_A)
etsysWpaAuthSuiteGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,32,2,1,3))
etsysWpaAuthSuiteGroup.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:etsysWpaAuthSuiteGroup.setStatus(_A)
etsysWpaStatsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,32,2,1,4))
etsysWpaStatsGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:etsysWpaStatsGroup.setStatus(_A)
etsysWpaCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,32,2,2,1))
etsysWpaCompliance.setObjects((_B,_u))
if mibBuilder.loadTexts:etsysWpaCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysWiFiProtectedAccessMIB':etsysWiFiProtectedAccessMIB,'etsysWiFiProtectedAccessObjects':etsysWiFiProtectedAccessObjects,'etsysWPAConfigTable':etsysWPAConfigTable,'etsysWPAConfigEntry':etsysWPAConfigEntry,_G:etsysWPAConfigIndex,_N:etsysWPAConfigOptionImplemented,_O:etsysWPAConfigEnabled,_P:etsysWPAConfigTKIPNumberOfReplayCounters,_Q:etsysWPAConfigVersion,_R:etsysWPAConfigPairwiseKeysSupported,_S:etsysWPAConfigMulticastCipher,_T:etsysWPAConfigGroupRekeyMethod,_U:etsysWPAConfigGroupRekeyTime,_V:etsysWPAConfigGroupRekeyPackets,_W:etsysWPAConfigGroupRekeyStrict,_X:etsysWPAConfigPSKValue,_a:etsysWPAConfigPSKPassPhrase,_Y:etsysWPAConfigPSKValueEntered,_Z:etsysWPAConfigMultipleAuthSuitesSupported,_b:etsysWPAConfigGroupMasterRekeyTime,_c:etsysWPAConfigGroupUpdateTimeOut,_d:etsysWPAConfigGroupUpdateCount,_e:etsysWPAConfigPairwiseUpdateTimeOut,_f:etsysWPAConfigPairwiseUpdateCount,_g:etsysWPAConfigLegacyOptionSupported,_h:etsysWPAConfigAllowLegacyClients,_i:etsysWPAConfigRekeyPairwiseWEP,'etsysWPAConfigUnicastCiphersTable':etsysWPAConfigUnicastCiphersTable,'etsysWPAConfigUnicastCiphersEntry':etsysWPAConfigUnicastCiphersEntry,_K:etsysWPAConfigUnicastCipherIndex,_j:etsysWPAConfigUnicastCipher,_k:etsysWPAConfigUnicastCipherEnabled,'etsysWPAConfigAuthenticationSuitesTable':etsysWPAConfigAuthenticationSuitesTable,'etsysWPAConfigAuthenticationSuitesEntry':etsysWPAConfigAuthenticationSuitesEntry,_L:etsysWPAConfigAuthenticationSuiteIndex,_l:etsysWPAConfigAuthenticationSuite,_m:etsysWPAConfigAuthenticationSuiteEnabled,'etsysWPAStatsTable':etsysWPAStatsTable,'etsysWPAStatsEntry':etsysWPAStatsEntry,_M:etsysWPAStatsIndex,_n:etsysWPAStatsSTAAddress,_o:etsysWPAStatsVersion,_p:etsysWPAStatsSelectedUnicastCipher,_q:etsysWPAStatsTKIPICVErrors,_r:etsysWPAStatsTKIPLocalMICFailures,_s:etsysWPAStatsTKIPRemoteMICFailures,_t:etsysWPAStatsTKIPCounterMeasuresInvoked,'etsysWpaConformance':etsysWpaConformance,'etsysWpaGroups':etsysWpaGroups,_u:etsysWpaBaseGroup,'etsysWpaUnicastCipherGroup':etsysWpaUnicastCipherGroup,'etsysWpaAuthSuiteGroup':etsysWpaAuthSuiteGroup,'etsysWpaStatsGroup':etsysWpaStatsGroup,'etsysWpaCompliances':etsysWpaCompliances,'etsysWpaCompliance':etsysWpaCompliance})