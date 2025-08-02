_k='etsysDot11ExtBaseGroup'
_j='etsysDot11ExtOIDNotInEffect'
_i='etsysDot11ExtWEPEnhancedImplemented'
_h='etsysDot11ExtWEPKeyValue'
_g='etsysDot11ExtWEPKeyDefined'
_f='etsysDot11ExtBldgMPActivationKey'
_e='etsysDot11ExtBldgRemoteMAC6'
_d='etsysDot11ExtBldgRemoteMAC5'
_c='etsysDot11ExtBldgRemoteMAC4'
_b='etsysDot11ExtBldgRemoteMAC3'
_a='etsysDot11ExtBldgRemoteMAC2'
_Z='etsysDot11ExtBldgRemoteMAC1'
_Y='etsysDot11ExtStationName'
_X='etsysDot11ExtResetOptions'
_W='etsysDot11ExtBridgeMode'
_V='etsysDot11ExtPCCardVersions'
_U='etsysDot11ExtPCCardType'
_T='etsysDot11ExtIntraBSSRelay'
_S='etsysDot11ExtMulticastTxRate'
_R='etsysDot11ExtSecureAccess'
_Q='etsysDot11ExtSystemScale'
_P='etsysDot11ExtLTRemoteContents'
_O='etsysDot11ExtLTTrigger'
_N='etsysDot11ExtLTRemoteStationName'
_M='etsysDot11ExtLTRemoteStationMAC'
_L='etsysDot11ExtOIDIndex'
_K='dot11WEPDefaultKeyIndex'
_J='IEEE802dot11-MIB'
_I='SnmpAdminString'
_H='OctetString'
_G='read-only'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='ENTERASYS-IEEE802DOT11EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
dot11WEPDefaultKeyIndex,=mibBuilder.importSymbols(_J,_K)
ifIndex,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
etsysDot11ExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,9))
if mibBuilder.loadTexts:etsysDot11ExtMIB.setRevisions(('2002-03-07 19:45','2001-05-08 18:00'))
_EtsysDot11ExtObjects_ObjectIdentity=ObjectIdentity
etsysDot11ExtObjects=_EtsysDot11ExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,9,1))
_EtsysDot11ExtLinkTest_ObjectIdentity=ObjectIdentity
etsysDot11ExtLinkTest=_EtsysDot11ExtLinkTest_ObjectIdentity((1,3,6,1,4,1,5624,1,2,9,1,1))
_EtsysDot11ExtLinkTestTable_Object=MibTable
etsysDot11ExtLinkTestTable=_EtsysDot11ExtLinkTestTable_Object((1,3,6,1,4,1,5624,1,2,9,1,1,1))
if mibBuilder.loadTexts:etsysDot11ExtLinkTestTable.setStatus(_A)
_EtsysDot11ExtLinkTestEntry_Object=MibTableRow
etsysDot11ExtLinkTestEntry=_EtsysDot11ExtLinkTestEntry_Object((1,3,6,1,4,1,5624,1,2,9,1,1,1,1))
etsysDot11ExtLinkTestEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:etsysDot11ExtLinkTestEntry.setStatus(_A)
_EtsysDot11ExtLTRemoteStationMAC_Type=MacAddress
_EtsysDot11ExtLTRemoteStationMAC_Object=MibTableColumn
etsysDot11ExtLTRemoteStationMAC=_EtsysDot11ExtLTRemoteStationMAC_Object((1,3,6,1,4,1,5624,1,2,9,1,1,1,1,1),_EtsysDot11ExtLTRemoteStationMAC_Type())
etsysDot11ExtLTRemoteStationMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtLTRemoteStationMAC.setStatus(_A)
class _EtsysDot11ExtLTRemoteStationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EtsysDot11ExtLTRemoteStationName_Type.__name__=_I
_EtsysDot11ExtLTRemoteStationName_Object=MibTableColumn
etsysDot11ExtLTRemoteStationName=_EtsysDot11ExtLTRemoteStationName_Object((1,3,6,1,4,1,5624,1,2,9,1,1,1,1,2),_EtsysDot11ExtLTRemoteStationName_Type())
etsysDot11ExtLTRemoteStationName.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysDot11ExtLTRemoteStationName.setStatus(_A)
class _EtsysDot11ExtLTTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_EtsysDot11ExtLTTrigger_Type.__name__=_F
_EtsysDot11ExtLTTrigger_Object=MibTableColumn
etsysDot11ExtLTTrigger=_EtsysDot11ExtLTTrigger_Object((1,3,6,1,4,1,5624,1,2,9,1,1,1,1,3),_EtsysDot11ExtLTTrigger_Type())
etsysDot11ExtLTTrigger.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtLTTrigger.setStatus(_A)
class _EtsysDot11ExtLTRemoteContents_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(84,84));fixedLength=84
_EtsysDot11ExtLTRemoteContents_Type.__name__=_H
_EtsysDot11ExtLTRemoteContents_Object=MibTableColumn
etsysDot11ExtLTRemoteContents=_EtsysDot11ExtLTRemoteContents_Object((1,3,6,1,4,1,5624,1,2,9,1,1,1,1,4),_EtsysDot11ExtLTRemoteContents_Type())
etsysDot11ExtLTRemoteContents.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysDot11ExtLTRemoteContents.setStatus(_A)
_EtsysDot11ExtGeneral_ObjectIdentity=ObjectIdentity
etsysDot11ExtGeneral=_EtsysDot11ExtGeneral_ObjectIdentity((1,3,6,1,4,1,5624,1,2,9,1,2))
_EtsysDot11ExtGeneralTable_Object=MibTable
etsysDot11ExtGeneralTable=_EtsysDot11ExtGeneralTable_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1))
if mibBuilder.loadTexts:etsysDot11ExtGeneralTable.setStatus(_A)
_EtsysDot11ExtGeneralEntry_Object=MibTableRow
etsysDot11ExtGeneralEntry=_EtsysDot11ExtGeneralEntry_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1))
etsysDot11ExtGeneralEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:etsysDot11ExtGeneralEntry.setStatus(_A)
class _EtsysDot11ExtPCCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,15)));namedValues=NamedValues(*(('none',1),('deprecatedValue1',2),('deprecatedValue2',3),('deprecatedValue3',4),('ds80211b',5),('ds80211a',6),('unknown',15)))
_EtsysDot11ExtPCCardType_Type.__name__=_F
_EtsysDot11ExtPCCardType_Object=MibTableColumn
etsysDot11ExtPCCardType=_EtsysDot11ExtPCCardType_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1,1),_EtsysDot11ExtPCCardType_Type())
etsysDot11ExtPCCardType.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysDot11ExtPCCardType.setStatus(_A)
class _EtsysDot11ExtPCCardVersions_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_EtsysDot11ExtPCCardVersions_Type.__name__=_I
_EtsysDot11ExtPCCardVersions_Object=MibTableColumn
etsysDot11ExtPCCardVersions=_EtsysDot11ExtPCCardVersions_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1,2),_EtsysDot11ExtPCCardVersions_Type())
etsysDot11ExtPCCardVersions.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysDot11ExtPCCardVersions.setStatus(_A)
class _EtsysDot11ExtBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('workgroup',1),('lanToLanEndpoint',2),('lanToLanMultipoint',3)))
_EtsysDot11ExtBridgeMode_Type.__name__=_F
_EtsysDot11ExtBridgeMode_Object=MibTableColumn
etsysDot11ExtBridgeMode=_EtsysDot11ExtBridgeMode_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1,3),_EtsysDot11ExtBridgeMode_Type())
etsysDot11ExtBridgeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtBridgeMode.setStatus(_A)
class _EtsysDot11ExtResetOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noReset',0),('resetRadioCardIfNecessary',1),('resetRadioCardRegardless',2)))
_EtsysDot11ExtResetOptions_Type.__name__=_F
_EtsysDot11ExtResetOptions_Object=MibTableColumn
etsysDot11ExtResetOptions=_EtsysDot11ExtResetOptions_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1,4),_EtsysDot11ExtResetOptions_Type())
etsysDot11ExtResetOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtResetOptions.setStatus(_A)
class _EtsysDot11ExtSystemScale_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('low',1),('medium',2),('high',3)))
_EtsysDot11ExtSystemScale_Type.__name__=_F
_EtsysDot11ExtSystemScale_Object=MibTableColumn
etsysDot11ExtSystemScale=_EtsysDot11ExtSystemScale_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1,5),_EtsysDot11ExtSystemScale_Type())
etsysDot11ExtSystemScale.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtSystemScale.setStatus(_A)
_EtsysDot11ExtSecureAccess_Type=EnabledStatus
_EtsysDot11ExtSecureAccess_Object=MibTableColumn
etsysDot11ExtSecureAccess=_EtsysDot11ExtSecureAccess_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1,6),_EtsysDot11ExtSecureAccess_Type())
etsysDot11ExtSecureAccess.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtSecureAccess.setStatus(_A)
class _EtsysDot11ExtMulticastTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fixed1Mbit',1),('fixed2Mbit',2),('fixedMediumRate',3),('fixedHighRate',4)))
_EtsysDot11ExtMulticastTxRate_Type.__name__=_F
_EtsysDot11ExtMulticastTxRate_Object=MibTableColumn
etsysDot11ExtMulticastTxRate=_EtsysDot11ExtMulticastTxRate_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1,7),_EtsysDot11ExtMulticastTxRate_Type())
etsysDot11ExtMulticastTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtMulticastTxRate.setStatus(_A)
_EtsysDot11ExtIntraBSSRelay_Type=EnabledStatus
_EtsysDot11ExtIntraBSSRelay_Object=MibTableColumn
etsysDot11ExtIntraBSSRelay=_EtsysDot11ExtIntraBSSRelay_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1,8),_EtsysDot11ExtIntraBSSRelay_Type())
etsysDot11ExtIntraBSSRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtIntraBSSRelay.setStatus(_A)
class _EtsysDot11ExtStationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EtsysDot11ExtStationName_Type.__name__=_I
_EtsysDot11ExtStationName_Object=MibTableColumn
etsysDot11ExtStationName=_EtsysDot11ExtStationName_Object((1,3,6,1,4,1,5624,1,2,9,1,2,1,1,9),_EtsysDot11ExtStationName_Type())
etsysDot11ExtStationName.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtStationName.setStatus(_A)
_EtsysDot11ExtBldg_ObjectIdentity=ObjectIdentity
etsysDot11ExtBldg=_EtsysDot11ExtBldg_ObjectIdentity((1,3,6,1,4,1,5624,1,2,9,1,3))
_EtsysDot11ExtBldgTable_Object=MibTable
etsysDot11ExtBldgTable=_EtsysDot11ExtBldgTable_Object((1,3,6,1,4,1,5624,1,2,9,1,3,1))
if mibBuilder.loadTexts:etsysDot11ExtBldgTable.setStatus(_A)
_EtsysDot11ExtBldgEntry_Object=MibTableRow
etsysDot11ExtBldgEntry=_EtsysDot11ExtBldgEntry_Object((1,3,6,1,4,1,5624,1,2,9,1,3,1,1))
etsysDot11ExtBldgEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:etsysDot11ExtBldgEntry.setStatus(_A)
_EtsysDot11ExtBldgRemoteMAC1_Type=MacAddress
_EtsysDot11ExtBldgRemoteMAC1_Object=MibTableColumn
etsysDot11ExtBldgRemoteMAC1=_EtsysDot11ExtBldgRemoteMAC1_Object((1,3,6,1,4,1,5624,1,2,9,1,3,1,1,1),_EtsysDot11ExtBldgRemoteMAC1_Type())
etsysDot11ExtBldgRemoteMAC1.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtBldgRemoteMAC1.setStatus(_A)
_EtsysDot11ExtBldgRemoteMAC2_Type=MacAddress
_EtsysDot11ExtBldgRemoteMAC2_Object=MibTableColumn
etsysDot11ExtBldgRemoteMAC2=_EtsysDot11ExtBldgRemoteMAC2_Object((1,3,6,1,4,1,5624,1,2,9,1,3,1,1,2),_EtsysDot11ExtBldgRemoteMAC2_Type())
etsysDot11ExtBldgRemoteMAC2.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtBldgRemoteMAC2.setStatus(_A)
_EtsysDot11ExtBldgRemoteMAC3_Type=MacAddress
_EtsysDot11ExtBldgRemoteMAC3_Object=MibTableColumn
etsysDot11ExtBldgRemoteMAC3=_EtsysDot11ExtBldgRemoteMAC3_Object((1,3,6,1,4,1,5624,1,2,9,1,3,1,1,3),_EtsysDot11ExtBldgRemoteMAC3_Type())
etsysDot11ExtBldgRemoteMAC3.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtBldgRemoteMAC3.setStatus(_A)
_EtsysDot11ExtBldgRemoteMAC4_Type=MacAddress
_EtsysDot11ExtBldgRemoteMAC4_Object=MibTableColumn
etsysDot11ExtBldgRemoteMAC4=_EtsysDot11ExtBldgRemoteMAC4_Object((1,3,6,1,4,1,5624,1,2,9,1,3,1,1,4),_EtsysDot11ExtBldgRemoteMAC4_Type())
etsysDot11ExtBldgRemoteMAC4.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtBldgRemoteMAC4.setStatus(_A)
_EtsysDot11ExtBldgRemoteMAC5_Type=MacAddress
_EtsysDot11ExtBldgRemoteMAC5_Object=MibTableColumn
etsysDot11ExtBldgRemoteMAC5=_EtsysDot11ExtBldgRemoteMAC5_Object((1,3,6,1,4,1,5624,1,2,9,1,3,1,1,5),_EtsysDot11ExtBldgRemoteMAC5_Type())
etsysDot11ExtBldgRemoteMAC5.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtBldgRemoteMAC5.setStatus(_A)
_EtsysDot11ExtBldgRemoteMAC6_Type=MacAddress
_EtsysDot11ExtBldgRemoteMAC6_Object=MibTableColumn
etsysDot11ExtBldgRemoteMAC6=_EtsysDot11ExtBldgRemoteMAC6_Object((1,3,6,1,4,1,5624,1,2,9,1,3,1,1,6),_EtsysDot11ExtBldgRemoteMAC6_Type())
etsysDot11ExtBldgRemoteMAC6.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtBldgRemoteMAC6.setStatus(_A)
class _EtsysDot11ExtBldgMPActivationKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_EtsysDot11ExtBldgMPActivationKey_Type.__name__=_H
_EtsysDot11ExtBldgMPActivationKey_Object=MibTableColumn
etsysDot11ExtBldgMPActivationKey=_EtsysDot11ExtBldgMPActivationKey_Object((1,3,6,1,4,1,5624,1,2,9,1,3,1,1,7),_EtsysDot11ExtBldgMPActivationKey_Type())
etsysDot11ExtBldgMPActivationKey.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtBldgMPActivationKey.setStatus(_A)
_EtsysDot11ExtWEP_ObjectIdentity=ObjectIdentity
etsysDot11ExtWEP=_EtsysDot11ExtWEP_ObjectIdentity((1,3,6,1,4,1,5624,1,2,9,1,4))
_EtsysDot11ExtWEPDefaultKeysTable_Object=MibTable
etsysDot11ExtWEPDefaultKeysTable=_EtsysDot11ExtWEPDefaultKeysTable_Object((1,3,6,1,4,1,5624,1,2,9,1,4,1))
if mibBuilder.loadTexts:etsysDot11ExtWEPDefaultKeysTable.setStatus(_A)
_EtsysDot11ExtWEPDefaultKeysEntry_Object=MibTableRow
etsysDot11ExtWEPDefaultKeysEntry=_EtsysDot11ExtWEPDefaultKeysEntry_Object((1,3,6,1,4,1,5624,1,2,9,1,4,1,1))
etsysDot11ExtWEPDefaultKeysEntry.setIndexNames((0,_D,_E),(0,_J,_K))
if mibBuilder.loadTexts:etsysDot11ExtWEPDefaultKeysEntry.setStatus(_A)
_EtsysDot11ExtWEPKeyDefined_Type=TruthValue
_EtsysDot11ExtWEPKeyDefined_Object=MibTableColumn
etsysDot11ExtWEPKeyDefined=_EtsysDot11ExtWEPKeyDefined_Object((1,3,6,1,4,1,5624,1,2,9,1,4,1,1,1),_EtsysDot11ExtWEPKeyDefined_Type())
etsysDot11ExtWEPKeyDefined.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysDot11ExtWEPKeyDefined.setStatus(_A)
class _EtsysDot11ExtWEPKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5),ValueSizeConstraint(13,13))
_EtsysDot11ExtWEPKeyValue_Type.__name__=_H
_EtsysDot11ExtWEPKeyValue_Object=MibTableColumn
etsysDot11ExtWEPKeyValue=_EtsysDot11ExtWEPKeyValue_Object((1,3,6,1,4,1,5624,1,2,9,1,4,1,1,2),_EtsysDot11ExtWEPKeyValue_Type())
etsysDot11ExtWEPKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot11ExtWEPKeyValue.setStatus(_A)
_EtsysDot11ExtWEPEnhancedTable_Object=MibTable
etsysDot11ExtWEPEnhancedTable=_EtsysDot11ExtWEPEnhancedTable_Object((1,3,6,1,4,1,5624,1,2,9,1,4,2))
if mibBuilder.loadTexts:etsysDot11ExtWEPEnhancedTable.setStatus(_A)
_EtsysDot11ExtWEPEnhancedEntry_Object=MibTableRow
etsysDot11ExtWEPEnhancedEntry=_EtsysDot11ExtWEPEnhancedEntry_Object((1,3,6,1,4,1,5624,1,2,9,1,4,2,1))
etsysDot11ExtWEPEnhancedEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:etsysDot11ExtWEPEnhancedEntry.setStatus(_A)
_EtsysDot11ExtWEPEnhancedImplemented_Type=TruthValue
_EtsysDot11ExtWEPEnhancedImplemented_Object=MibTableColumn
etsysDot11ExtWEPEnhancedImplemented=_EtsysDot11ExtWEPEnhancedImplemented_Object((1,3,6,1,4,1,5624,1,2,9,1,4,2,1,1),_EtsysDot11ExtWEPEnhancedImplemented_Type())
etsysDot11ExtWEPEnhancedImplemented.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysDot11ExtWEPEnhancedImplemented.setStatus(_A)
_EtsysDot11ExtEffect_ObjectIdentity=ObjectIdentity
etsysDot11ExtEffect=_EtsysDot11ExtEffect_ObjectIdentity((1,3,6,1,4,1,5624,1,2,9,1,5))
_EtsysDot11ExtOIDNotInEffectTable_Object=MibTable
etsysDot11ExtOIDNotInEffectTable=_EtsysDot11ExtOIDNotInEffectTable_Object((1,3,6,1,4,1,5624,1,2,9,1,5,1))
if mibBuilder.loadTexts:etsysDot11ExtOIDNotInEffectTable.setStatus(_A)
_EtsysDot11ExtOIDNotInEffectEntry_Object=MibTableRow
etsysDot11ExtOIDNotInEffectEntry=_EtsysDot11ExtOIDNotInEffectEntry_Object((1,3,6,1,4,1,5624,1,2,9,1,5,1,1))
etsysDot11ExtOIDNotInEffectEntry.setIndexNames((0,_D,_E),(0,_B,_L))
if mibBuilder.loadTexts:etsysDot11ExtOIDNotInEffectEntry.setStatus(_A)
_EtsysDot11ExtOIDIndex_Type=AutonomousType
_EtsysDot11ExtOIDIndex_Object=MibTableColumn
etsysDot11ExtOIDIndex=_EtsysDot11ExtOIDIndex_Object((1,3,6,1,4,1,5624,1,2,9,1,5,1,1,1),_EtsysDot11ExtOIDIndex_Type())
etsysDot11ExtOIDIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysDot11ExtOIDIndex.setStatus(_A)
_EtsysDot11ExtOIDNotInEffect_Type=TruthValue
_EtsysDot11ExtOIDNotInEffect_Object=MibTableColumn
etsysDot11ExtOIDNotInEffect=_EtsysDot11ExtOIDNotInEffect_Object((1,3,6,1,4,1,5624,1,2,9,1,5,1,1,2),_EtsysDot11ExtOIDNotInEffect_Type())
etsysDot11ExtOIDNotInEffect.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysDot11ExtOIDNotInEffect.setStatus(_A)
_EtsysDot11ExtConformance_ObjectIdentity=ObjectIdentity
etsysDot11ExtConformance=_EtsysDot11ExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,9,2))
_EtsysDot11ExtGroups_ObjectIdentity=ObjectIdentity
etsysDot11ExtGroups=_EtsysDot11ExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,9,2,1))
_EtsysDot11ExtCompliances_ObjectIdentity=ObjectIdentity
etsysDot11ExtCompliances=_EtsysDot11ExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,9,2,2))
etsysDot11ExtBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,9,2,1,1))
etsysDot11ExtBaseGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:etsysDot11ExtBaseGroup.setStatus(_A)
etsysDot11ExtCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,9,2,2,1))
etsysDot11ExtCompliance.setObjects((_B,_k))
if mibBuilder.loadTexts:etsysDot11ExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysDot11ExtMIB':etsysDot11ExtMIB,'etsysDot11ExtObjects':etsysDot11ExtObjects,'etsysDot11ExtLinkTest':etsysDot11ExtLinkTest,'etsysDot11ExtLinkTestTable':etsysDot11ExtLinkTestTable,'etsysDot11ExtLinkTestEntry':etsysDot11ExtLinkTestEntry,_M:etsysDot11ExtLTRemoteStationMAC,_N:etsysDot11ExtLTRemoteStationName,_O:etsysDot11ExtLTTrigger,_P:etsysDot11ExtLTRemoteContents,'etsysDot11ExtGeneral':etsysDot11ExtGeneral,'etsysDot11ExtGeneralTable':etsysDot11ExtGeneralTable,'etsysDot11ExtGeneralEntry':etsysDot11ExtGeneralEntry,_U:etsysDot11ExtPCCardType,_V:etsysDot11ExtPCCardVersions,_W:etsysDot11ExtBridgeMode,_X:etsysDot11ExtResetOptions,_Q:etsysDot11ExtSystemScale,_R:etsysDot11ExtSecureAccess,_S:etsysDot11ExtMulticastTxRate,_T:etsysDot11ExtIntraBSSRelay,_Y:etsysDot11ExtStationName,'etsysDot11ExtBldg':etsysDot11ExtBldg,'etsysDot11ExtBldgTable':etsysDot11ExtBldgTable,'etsysDot11ExtBldgEntry':etsysDot11ExtBldgEntry,_Z:etsysDot11ExtBldgRemoteMAC1,_a:etsysDot11ExtBldgRemoteMAC2,_b:etsysDot11ExtBldgRemoteMAC3,_c:etsysDot11ExtBldgRemoteMAC4,_d:etsysDot11ExtBldgRemoteMAC5,_e:etsysDot11ExtBldgRemoteMAC6,_f:etsysDot11ExtBldgMPActivationKey,'etsysDot11ExtWEP':etsysDot11ExtWEP,'etsysDot11ExtWEPDefaultKeysTable':etsysDot11ExtWEPDefaultKeysTable,'etsysDot11ExtWEPDefaultKeysEntry':etsysDot11ExtWEPDefaultKeysEntry,_g:etsysDot11ExtWEPKeyDefined,_h:etsysDot11ExtWEPKeyValue,'etsysDot11ExtWEPEnhancedTable':etsysDot11ExtWEPEnhancedTable,'etsysDot11ExtWEPEnhancedEntry':etsysDot11ExtWEPEnhancedEntry,_i:etsysDot11ExtWEPEnhancedImplemented,'etsysDot11ExtEffect':etsysDot11ExtEffect,'etsysDot11ExtOIDNotInEffectTable':etsysDot11ExtOIDNotInEffectTable,'etsysDot11ExtOIDNotInEffectEntry':etsysDot11ExtOIDNotInEffectEntry,_L:etsysDot11ExtOIDIndex,_j:etsysDot11ExtOIDNotInEffect,'etsysDot11ExtConformance':etsysDot11ExtConformance,'etsysDot11ExtGroups':etsysDot11ExtGroups,_k:etsysDot11ExtBaseGroup,'etsysDot11ExtCompliances':etsysDot11ExtCompliances,'etsysDot11ExtCompliance':etsysDot11ExtCompliance})