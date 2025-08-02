_a='interopStartCallInVbdInterfaceId'
_Z='interopDtmfDetectionInterfaceId'
_Y='distinctiveCallWaitingToneIndex'
_X='specificMachineDetectionInterfaceId'
_W='faxmode'
_V='passthrough'
_U='countryCustomizationToneTone'
_T='stutter'
_S='ringback'
_R='reorder'
_Q='preemption'
_P='messageWaiting'
_O='intercept'
_N='congestion'
_M='confirmation'
_L='callWaiting'
_K='countryToneStatusTone'
_J='specificCountryCustomizationDialingInterfaceId'
_I='specificCountryCustomizationUserGainInterfaceId'
_H='OctetString'
_G='MX-TELIF-MIB'
_F='read-only'
_E='Unsigned32'
_D='MxEnableState'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_D,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
telIfMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775))
_TelIfMIBObjects_ObjectIdentity=ObjectIdentity
telIfMIBObjects=_TelIfMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1))
class _CountrySelection_Type(Integer32):defaultValue=17000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(900,1000,1100,2000,3000,4000,4500,5000,6000,7000,7100,10100,11000,12100,14000,15000,16000,17000,18000,19000,20000,21000,23100,23200,23300,24000)));namedValues=NamedValues(*(('argentina1',900),('australia1',1000),('australia2',1100),('austria1',2000),('brazil1',3000),('china1',4000),('czechRepublic1',4500),('denmark1',5000),('france1',6000),('germany1',7000),('germany2',7100),('israel2',10100),('italy1',11000),('japan2',12100),('mexico1',14000),('netherlands1',15000),('newZealand1',16000),('northAmerica1',17000),('russia1',18000),('spain1',19000),('sweden1',20000),('switzerland1',21000),('uae2',23100),('uae3',23200),('uae4',23300),('uk1',24000)))
_CountrySelection_Type.__name__=_C
_CountrySelection_Object=MibScalar
countrySelection=_CountrySelection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,100),_CountrySelection_Type())
countrySelection.setMaxAccess(_B)
if mibBuilder.loadTexts:countrySelection.setStatus(_A)
_CountryCustomizationGroup_ObjectIdentity=ObjectIdentity
countryCustomizationGroup=_CountryCustomizationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200))
_CountryCustomizationUserGainGroup_ObjectIdentity=ObjectIdentity
countryCustomizationUserGainGroup=_CountryCustomizationUserGainGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,100))
class _DefaultCountryCustomizationUserGainInputOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,12))
_DefaultCountryCustomizationUserGainInputOffset_Type.__name__=_C
_DefaultCountryCustomizationUserGainInputOffset_Object=MibScalar
defaultCountryCustomizationUserGainInputOffset=_DefaultCountryCustomizationUserGainInputOffset_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,100,100),_DefaultCountryCustomizationUserGainInputOffset_Type())
defaultCountryCustomizationUserGainInputOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCountryCustomizationUserGainInputOffset.setStatus(_A)
class _DefaultCountryCustomizationUserGainOutputOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,12))
_DefaultCountryCustomizationUserGainOutputOffset_Type.__name__=_C
_DefaultCountryCustomizationUserGainOutputOffset_Object=MibScalar
defaultCountryCustomizationUserGainOutputOffset=_DefaultCountryCustomizationUserGainOutputOffset_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,100,200),_DefaultCountryCustomizationUserGainOutputOffset_Type())
defaultCountryCustomizationUserGainOutputOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCountryCustomizationUserGainOutputOffset.setStatus(_A)
_SpecificCountryCustomizationUserGainTable_Object=MibTable
specificCountryCustomizationUserGainTable=_SpecificCountryCustomizationUserGainTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,100,300))
if mibBuilder.loadTexts:specificCountryCustomizationUserGainTable.setStatus(_A)
_SpecificCountryCustomizationUserGainEntry_Object=MibTableRow
specificCountryCustomizationUserGainEntry=_SpecificCountryCustomizationUserGainEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,100,300,1))
specificCountryCustomizationUserGainEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:specificCountryCustomizationUserGainEntry.setStatus(_A)
_SpecificCountryCustomizationUserGainInterfaceId_Type=OctetString
_SpecificCountryCustomizationUserGainInterfaceId_Object=MibTableColumn
specificCountryCustomizationUserGainInterfaceId=_SpecificCountryCustomizationUserGainInterfaceId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,100,300,1,100),_SpecificCountryCustomizationUserGainInterfaceId_Type())
specificCountryCustomizationUserGainInterfaceId.setMaxAccess(_F)
if mibBuilder.loadTexts:specificCountryCustomizationUserGainInterfaceId.setStatus(_A)
class _SpecificCountryCustomizationUserGainEnableConfig_Type(MxEnableState):defaultValue=0
_SpecificCountryCustomizationUserGainEnableConfig_Type.__name__=_D
_SpecificCountryCustomizationUserGainEnableConfig_Object=MibTableColumn
specificCountryCustomizationUserGainEnableConfig=_SpecificCountryCustomizationUserGainEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,100,300,1,200),_SpecificCountryCustomizationUserGainEnableConfig_Type())
specificCountryCustomizationUserGainEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificCountryCustomizationUserGainEnableConfig.setStatus(_A)
class _SpecificCountryCustomizationUserGainInputOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,12))
_SpecificCountryCustomizationUserGainInputOffset_Type.__name__=_C
_SpecificCountryCustomizationUserGainInputOffset_Object=MibTableColumn
specificCountryCustomizationUserGainInputOffset=_SpecificCountryCustomizationUserGainInputOffset_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,100,300,1,300),_SpecificCountryCustomizationUserGainInputOffset_Type())
specificCountryCustomizationUserGainInputOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:specificCountryCustomizationUserGainInputOffset.setStatus(_A)
class _SpecificCountryCustomizationUserGainOutputOffset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-12,12))
_SpecificCountryCustomizationUserGainOutputOffset_Type.__name__=_C
_SpecificCountryCustomizationUserGainOutputOffset_Object=MibTableColumn
specificCountryCustomizationUserGainOutputOffset=_SpecificCountryCustomizationUserGainOutputOffset_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,100,300,1,400),_SpecificCountryCustomizationUserGainOutputOffset_Type())
specificCountryCustomizationUserGainOutputOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:specificCountryCustomizationUserGainOutputOffset.setStatus(_A)
_CountryCustomizationDialingGroup_ObjectIdentity=ObjectIdentity
countryCustomizationDialingGroup=_CountryCustomizationDialingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400))
class _DefaultCountryCustomizationDialingOverride_Type(MxEnableState):defaultValue=0
_DefaultCountryCustomizationDialingOverride_Type.__name__=_D
_DefaultCountryCustomizationDialingOverride_Object=MibScalar
defaultCountryCustomizationDialingOverride=_DefaultCountryCustomizationDialingOverride_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,100),_DefaultCountryCustomizationDialingOverride_Type())
defaultCountryCustomizationDialingOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCountryCustomizationDialingOverride.setStatus(_A)
class _DefaultCountryCustomizationDialingInterDtmfDialDelay_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_DefaultCountryCustomizationDialingInterDtmfDialDelay_Type.__name__=_E
_DefaultCountryCustomizationDialingInterDtmfDialDelay_Object=MibScalar
defaultCountryCustomizationDialingInterDtmfDialDelay=_DefaultCountryCustomizationDialingInterDtmfDialDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,200),_DefaultCountryCustomizationDialingInterDtmfDialDelay_Type())
defaultCountryCustomizationDialingInterDtmfDialDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCountryCustomizationDialingInterDtmfDialDelay.setStatus(_A)
class _DefaultCountryCustomizationDialingDtmfDuration_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_DefaultCountryCustomizationDialingDtmfDuration_Type.__name__=_E
_DefaultCountryCustomizationDialingDtmfDuration_Object=MibScalar
defaultCountryCustomizationDialingDtmfDuration=_DefaultCountryCustomizationDialingDtmfDuration_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,300),_DefaultCountryCustomizationDialingDtmfDuration_Type())
defaultCountryCustomizationDialingDtmfDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCountryCustomizationDialingDtmfDuration.setStatus(_A)
class _DefaultCountryCustomizationDialingInterMfR1DialDelay_Type(Unsigned32):defaultValue=68;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_DefaultCountryCustomizationDialingInterMfR1DialDelay_Type.__name__=_E
_DefaultCountryCustomizationDialingInterMfR1DialDelay_Object=MibScalar
defaultCountryCustomizationDialingInterMfR1DialDelay=_DefaultCountryCustomizationDialingInterMfR1DialDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,340),_DefaultCountryCustomizationDialingInterMfR1DialDelay_Type())
defaultCountryCustomizationDialingInterMfR1DialDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCountryCustomizationDialingInterMfR1DialDelay.setStatus(_A)
class _DefaultCountryCustomizationDialingMfR1Duration_Type(Unsigned32):defaultValue=68;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_DefaultCountryCustomizationDialingMfR1Duration_Type.__name__=_E
_DefaultCountryCustomizationDialingMfR1Duration_Object=MibScalar
defaultCountryCustomizationDialingMfR1Duration=_DefaultCountryCustomizationDialingMfR1Duration_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,370),_DefaultCountryCustomizationDialingMfR1Duration_Type())
defaultCountryCustomizationDialingMfR1Duration.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultCountryCustomizationDialingMfR1Duration.setStatus(_A)
_SpecificCountryCustomizationDialingTable_Object=MibTable
specificCountryCustomizationDialingTable=_SpecificCountryCustomizationDialingTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,400))
if mibBuilder.loadTexts:specificCountryCustomizationDialingTable.setStatus(_A)
_SpecificCountryCustomizationDialingEntry_Object=MibTableRow
specificCountryCustomizationDialingEntry=_SpecificCountryCustomizationDialingEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,400,1))
specificCountryCustomizationDialingEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:specificCountryCustomizationDialingEntry.setStatus(_A)
_SpecificCountryCustomizationDialingInterfaceId_Type=OctetString
_SpecificCountryCustomizationDialingInterfaceId_Object=MibTableColumn
specificCountryCustomizationDialingInterfaceId=_SpecificCountryCustomizationDialingInterfaceId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,400,1,100),_SpecificCountryCustomizationDialingInterfaceId_Type())
specificCountryCustomizationDialingInterfaceId.setMaxAccess(_F)
if mibBuilder.loadTexts:specificCountryCustomizationDialingInterfaceId.setStatus(_A)
class _SpecificCountryCustomizationDialingEnableConfig_Type(MxEnableState):defaultValue=0
_SpecificCountryCustomizationDialingEnableConfig_Type.__name__=_D
_SpecificCountryCustomizationDialingEnableConfig_Object=MibTableColumn
specificCountryCustomizationDialingEnableConfig=_SpecificCountryCustomizationDialingEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,400,1,200),_SpecificCountryCustomizationDialingEnableConfig_Type())
specificCountryCustomizationDialingEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificCountryCustomizationDialingEnableConfig.setStatus(_A)
class _SpecificCountryCustomizationDialingOverride_Type(MxEnableState):defaultValue=0
_SpecificCountryCustomizationDialingOverride_Type.__name__=_D
_SpecificCountryCustomizationDialingOverride_Object=MibTableColumn
specificCountryCustomizationDialingOverride=_SpecificCountryCustomizationDialingOverride_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,400,1,300),_SpecificCountryCustomizationDialingOverride_Type())
specificCountryCustomizationDialingOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:specificCountryCustomizationDialingOverride.setStatus(_A)
class _SpecificCountryCustomizationDialingInterDtmfDialDelay_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_SpecificCountryCustomizationDialingInterDtmfDialDelay_Type.__name__=_E
_SpecificCountryCustomizationDialingInterDtmfDialDelay_Object=MibTableColumn
specificCountryCustomizationDialingInterDtmfDialDelay=_SpecificCountryCustomizationDialingInterDtmfDialDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,400,1,400),_SpecificCountryCustomizationDialingInterDtmfDialDelay_Type())
specificCountryCustomizationDialingInterDtmfDialDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:specificCountryCustomizationDialingInterDtmfDialDelay.setStatus(_A)
class _SpecificCountryCustomizationDialingDtmfDuration_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_SpecificCountryCustomizationDialingDtmfDuration_Type.__name__=_E
_SpecificCountryCustomizationDialingDtmfDuration_Object=MibTableColumn
specificCountryCustomizationDialingDtmfDuration=_SpecificCountryCustomizationDialingDtmfDuration_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,400,1,500),_SpecificCountryCustomizationDialingDtmfDuration_Type())
specificCountryCustomizationDialingDtmfDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:specificCountryCustomizationDialingDtmfDuration.setStatus(_A)
class _SpecificCountryCustomizationDialingInterMfR1DialDelay_Type(Unsigned32):defaultValue=68;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_SpecificCountryCustomizationDialingInterMfR1DialDelay_Type.__name__=_E
_SpecificCountryCustomizationDialingInterMfR1DialDelay_Object=MibTableColumn
specificCountryCustomizationDialingInterMfR1DialDelay=_SpecificCountryCustomizationDialingInterMfR1DialDelay_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,400,1,600),_SpecificCountryCustomizationDialingInterMfR1DialDelay_Type())
specificCountryCustomizationDialingInterMfR1DialDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:specificCountryCustomizationDialingInterMfR1DialDelay.setStatus(_A)
class _SpecificCountryCustomizationDialingMfR1Duration_Type(Unsigned32):defaultValue=68;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,600))
_SpecificCountryCustomizationDialingMfR1Duration_Type.__name__=_E
_SpecificCountryCustomizationDialingMfR1Duration_Object=MibTableColumn
specificCountryCustomizationDialingMfR1Duration=_SpecificCountryCustomizationDialingMfR1Duration_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,400,400,1,700),_SpecificCountryCustomizationDialingMfR1Duration_Type())
specificCountryCustomizationDialingMfR1Duration.setMaxAccess(_B)
if mibBuilder.loadTexts:specificCountryCustomizationDialingMfR1Duration.setStatus(_A)
_CountryCustomizationToneGroup_ObjectIdentity=ObjectIdentity
countryCustomizationToneGroup=_CountryCustomizationToneGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500))
_CountryToneStatusTable_Object=MibTable
countryToneStatusTable=_CountryToneStatusTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500,100))
if mibBuilder.loadTexts:countryToneStatusTable.setStatus(_A)
_CountryToneStatusEntry_Object=MibTableRow
countryToneStatusEntry=_CountryToneStatusEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500,100,1))
countryToneStatusEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:countryToneStatusEntry.setStatus(_A)
class _CountryToneStatusTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,150,200,300,400,500,600,700,800,900,1000,1100,1200,1300)));namedValues=NamedValues(*(('busy',100),(_L,150),(_M,200),(_N,300),('dial',400),('hold',500),(_O,600),(_P,700),(_Q,800),(_R,900),(_S,1000),('roh',1100),('sit',1200),(_T,1300)))
_CountryToneStatusTone_Type.__name__=_C
_CountryToneStatusTone_Object=MibTableColumn
countryToneStatusTone=_CountryToneStatusTone_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500,100,1,100),_CountryToneStatusTone_Type())
countryToneStatusTone.setMaxAccess(_F)
if mibBuilder.loadTexts:countryToneStatusTone.setStatus(_A)
class _CountryToneStatusPattern_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CountryToneStatusPattern_Type.__name__=_H
_CountryToneStatusPattern_Object=MibTableColumn
countryToneStatusPattern=_CountryToneStatusPattern_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500,100,1,300),_CountryToneStatusPattern_Type())
countryToneStatusPattern.setMaxAccess(_F)
if mibBuilder.loadTexts:countryToneStatusPattern.setStatus(_A)
_CountryCustomizationToneTable_Object=MibTable
countryCustomizationToneTable=_CountryCustomizationToneTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500,200))
if mibBuilder.loadTexts:countryCustomizationToneTable.setStatus(_A)
_CountryCustomizationToneEntry_Object=MibTableRow
countryCustomizationToneEntry=_CountryCustomizationToneEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500,200,1))
countryCustomizationToneEntry.setIndexNames((0,_G,_U))
if mibBuilder.loadTexts:countryCustomizationToneEntry.setStatus(_A)
class _CountryCustomizationToneTone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,150,200,300,400,500,600,700,800,900,1000,1100,1200,1300)));namedValues=NamedValues(*(('busy',100),(_L,150),(_M,200),(_N,300),('dial',400),('hold',500),(_O,600),(_P,700),(_Q,800),(_R,900),(_S,1000),('roh',1100),('sit',1200),(_T,1300)))
_CountryCustomizationToneTone_Type.__name__=_C
_CountryCustomizationToneTone_Object=MibTableColumn
countryCustomizationToneTone=_CountryCustomizationToneTone_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500,200,1,100),_CountryCustomizationToneTone_Type())
countryCustomizationToneTone.setMaxAccess(_F)
if mibBuilder.loadTexts:countryCustomizationToneTone.setStatus(_A)
class _CountryCustomizationToneOverride_Type(MxEnableState):defaultValue=0
_CountryCustomizationToneOverride_Type.__name__=_D
_CountryCustomizationToneOverride_Object=MibTableColumn
countryCustomizationToneOverride=_CountryCustomizationToneOverride_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500,200,1,200),_CountryCustomizationToneOverride_Type())
countryCustomizationToneOverride.setMaxAccess(_B)
if mibBuilder.loadTexts:countryCustomizationToneOverride.setStatus(_A)
class _CountryCustomizationTonePattern_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_CountryCustomizationTonePattern_Type.__name__=_H
_CountryCustomizationTonePattern_Object=MibTableColumn
countryCustomizationTonePattern=_CountryCustomizationTonePattern_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,200,500,200,1,300),_CountryCustomizationTonePattern_Type())
countryCustomizationTonePattern.setMaxAccess(_B)
if mibBuilder.loadTexts:countryCustomizationTonePattern.setStatus(_A)
_MachineDetectionGroup_ObjectIdentity=ObjectIdentity
machineDetectionGroup=_MachineDetectionGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300))
class _DefaultMachineDetectionCngToneDetection_Type(MxEnableState):defaultValue=1
_DefaultMachineDetectionCngToneDetection_Type.__name__=_D
_DefaultMachineDetectionCngToneDetection_Object=MibScalar
defaultMachineDetectionCngToneDetection=_DefaultMachineDetectionCngToneDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,100),_DefaultMachineDetectionCngToneDetection_Type())
defaultMachineDetectionCngToneDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultMachineDetectionCngToneDetection.setStatus(_A)
class _DefaultMachineDetectionCedToneDetection_Type(MxEnableState):defaultValue=1
_DefaultMachineDetectionCedToneDetection_Type.__name__=_D
_DefaultMachineDetectionCedToneDetection_Object=MibScalar
defaultMachineDetectionCedToneDetection=_DefaultMachineDetectionCedToneDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,101),_DefaultMachineDetectionCedToneDetection_Type())
defaultMachineDetectionCedToneDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultMachineDetectionCedToneDetection.setStatus(_A)
class _DefaultMachineDetectionV21ModulationDetection_Type(MxEnableState):defaultValue=1
_DefaultMachineDetectionV21ModulationDetection_Type.__name__=_D
_DefaultMachineDetectionV21ModulationDetection_Object=MibScalar
defaultMachineDetectionV21ModulationDetection=_DefaultMachineDetectionV21ModulationDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,102),_DefaultMachineDetectionV21ModulationDetection_Type())
defaultMachineDetectionV21ModulationDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultMachineDetectionV21ModulationDetection.setStatus(_A)
class _DefaultMachineDetectionBehaviorOnCedToneDetection_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_V,100),(_W,200)))
_DefaultMachineDetectionBehaviorOnCedToneDetection_Type.__name__=_C
_DefaultMachineDetectionBehaviorOnCedToneDetection_Object=MibScalar
defaultMachineDetectionBehaviorOnCedToneDetection=_DefaultMachineDetectionBehaviorOnCedToneDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,110),_DefaultMachineDetectionBehaviorOnCedToneDetection_Type())
defaultMachineDetectionBehaviorOnCedToneDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:defaultMachineDetectionBehaviorOnCedToneDetection.setStatus(_A)
_SpecificMachineDetectionTable_Object=MibTable
specificMachineDetectionTable=_SpecificMachineDetectionTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,200))
if mibBuilder.loadTexts:specificMachineDetectionTable.setStatus(_A)
_SpecificMachineDetectionEntry_Object=MibTableRow
specificMachineDetectionEntry=_SpecificMachineDetectionEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,200,1))
specificMachineDetectionEntry.setIndexNames((0,_G,_X))
if mibBuilder.loadTexts:specificMachineDetectionEntry.setStatus(_A)
_SpecificMachineDetectionInterfaceId_Type=OctetString
_SpecificMachineDetectionInterfaceId_Object=MibTableColumn
specificMachineDetectionInterfaceId=_SpecificMachineDetectionInterfaceId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,200,1,100),_SpecificMachineDetectionInterfaceId_Type())
specificMachineDetectionInterfaceId.setMaxAccess(_F)
if mibBuilder.loadTexts:specificMachineDetectionInterfaceId.setStatus(_A)
class _SpecificMachineDetectionEnableConfig_Type(MxEnableState):defaultValue=0
_SpecificMachineDetectionEnableConfig_Type.__name__=_D
_SpecificMachineDetectionEnableConfig_Object=MibTableColumn
specificMachineDetectionEnableConfig=_SpecificMachineDetectionEnableConfig_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,200,1,200),_SpecificMachineDetectionEnableConfig_Type())
specificMachineDetectionEnableConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:specificMachineDetectionEnableConfig.setStatus(_A)
class _SpecificMachineDetectionCngToneDetection_Type(MxEnableState):defaultValue=1
_SpecificMachineDetectionCngToneDetection_Type.__name__=_D
_SpecificMachineDetectionCngToneDetection_Object=MibTableColumn
specificMachineDetectionCngToneDetection=_SpecificMachineDetectionCngToneDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,200,1,300),_SpecificMachineDetectionCngToneDetection_Type())
specificMachineDetectionCngToneDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:specificMachineDetectionCngToneDetection.setStatus(_A)
class _SpecificMachineDetectionCedToneDetection_Type(MxEnableState):defaultValue=1
_SpecificMachineDetectionCedToneDetection_Type.__name__=_D
_SpecificMachineDetectionCedToneDetection_Object=MibTableColumn
specificMachineDetectionCedToneDetection=_SpecificMachineDetectionCedToneDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,200,1,310),_SpecificMachineDetectionCedToneDetection_Type())
specificMachineDetectionCedToneDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:specificMachineDetectionCedToneDetection.setStatus(_A)
class _SpecificMachineDetectionV21ModulationDetection_Type(MxEnableState):defaultValue=1
_SpecificMachineDetectionV21ModulationDetection_Type.__name__=_D
_SpecificMachineDetectionV21ModulationDetection_Object=MibTableColumn
specificMachineDetectionV21ModulationDetection=_SpecificMachineDetectionV21ModulationDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,200,1,320),_SpecificMachineDetectionV21ModulationDetection_Type())
specificMachineDetectionV21ModulationDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:specificMachineDetectionV21ModulationDetection.setStatus(_A)
class _SpecificMachineDetectionBehaviorOnCedToneDetection_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_V,100),(_W,200)))
_SpecificMachineDetectionBehaviorOnCedToneDetection_Type.__name__=_C
_SpecificMachineDetectionBehaviorOnCedToneDetection_Object=MibTableColumn
specificMachineDetectionBehaviorOnCedToneDetection=_SpecificMachineDetectionBehaviorOnCedToneDetection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,300,200,1,400),_SpecificMachineDetectionBehaviorOnCedToneDetection_Type())
specificMachineDetectionBehaviorOnCedToneDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:specificMachineDetectionBehaviorOnCedToneDetection.setStatus(_A)
_MusicOnHoldStreamingGroup_ObjectIdentity=ObjectIdentity
musicOnHoldStreamingGroup=_MusicOnHoldStreamingGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,400))
class _MusicOnHoldStreamingEnable_Type(MxEnableState):defaultValue=0
_MusicOnHoldStreamingEnable_Type.__name__=_D
_MusicOnHoldStreamingEnable_Object=MibScalar
musicOnHoldStreamingEnable=_MusicOnHoldStreamingEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,400,100),_MusicOnHoldStreamingEnable_Type())
musicOnHoldStreamingEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:musicOnHoldStreamingEnable.setStatus(_A)
_CallWaitingToneGroup_ObjectIdentity=ObjectIdentity
callWaitingToneGroup=_CallWaitingToneGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,500))
_DistinctiveCallWaitingToneTable_Object=MibTable
distinctiveCallWaitingToneTable=_DistinctiveCallWaitingToneTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,500,100))
if mibBuilder.loadTexts:distinctiveCallWaitingToneTable.setStatus(_A)
_DistinctiveCallWaitingToneEntry_Object=MibTableRow
distinctiveCallWaitingToneEntry=_DistinctiveCallWaitingToneEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,500,100,1))
distinctiveCallWaitingToneEntry.setIndexNames((0,_G,_Y))
if mibBuilder.loadTexts:distinctiveCallWaitingToneEntry.setStatus(_A)
class _DistinctiveCallWaitingToneIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_DistinctiveCallWaitingToneIndex_Type.__name__=_E
_DistinctiveCallWaitingToneIndex_Object=MibTableColumn
distinctiveCallWaitingToneIndex=_DistinctiveCallWaitingToneIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,500,100,1,100),_DistinctiveCallWaitingToneIndex_Type())
distinctiveCallWaitingToneIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:distinctiveCallWaitingToneIndex.setStatus(_A)
class _DistinctiveCallWaitingToneToneId_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_DistinctiveCallWaitingToneToneId_Type.__name__=_H
_DistinctiveCallWaitingToneToneId_Object=MibTableColumn
distinctiveCallWaitingToneToneId=_DistinctiveCallWaitingToneToneId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,500,100,1,200),_DistinctiveCallWaitingToneToneId_Type())
distinctiveCallWaitingToneToneId.setMaxAccess(_B)
if mibBuilder.loadTexts:distinctiveCallWaitingToneToneId.setStatus(_A)
class _DistinctiveCallWaitingTonePattern_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_DistinctiveCallWaitingTonePattern_Type.__name__=_H
_DistinctiveCallWaitingTonePattern_Object=MibTableColumn
distinctiveCallWaitingTonePattern=_DistinctiveCallWaitingTonePattern_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,500,100,1,300),_DistinctiveCallWaitingTonePattern_Type())
distinctiveCallWaitingTonePattern.setMaxAccess(_B)
if mibBuilder.loadTexts:distinctiveCallWaitingTonePattern.setStatus(_A)
_InteropGroup_ObjectIdentity=ObjectIdentity
interopGroup=_InteropGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000))
_InteropDtmfDetectionTable_Object=MibTable
interopDtmfDetectionTable=_InteropDtmfDetectionTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,100))
if mibBuilder.loadTexts:interopDtmfDetectionTable.setStatus(_A)
_InteropDtmfDetectionEntry_Object=MibTableRow
interopDtmfDetectionEntry=_InteropDtmfDetectionEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,100,1))
interopDtmfDetectionEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:interopDtmfDetectionEntry.setStatus(_A)
_InteropDtmfDetectionInterfaceId_Type=OctetString
_InteropDtmfDetectionInterfaceId_Object=MibTableColumn
interopDtmfDetectionInterfaceId=_InteropDtmfDetectionInterfaceId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,100,1,100),_InteropDtmfDetectionInterfaceId_Type())
interopDtmfDetectionInterfaceId.setMaxAccess(_F)
if mibBuilder.loadTexts:interopDtmfDetectionInterfaceId.setStatus(_A)
class _InteropDtmfDetectionRiseTimeCriteria_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('checkSr',100),('confirmSnr',200)))
_InteropDtmfDetectionRiseTimeCriteria_Type.__name__=_C
_InteropDtmfDetectionRiseTimeCriteria_Object=MibTableColumn
interopDtmfDetectionRiseTimeCriteria=_InteropDtmfDetectionRiseTimeCriteria_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,100,1,200),_InteropDtmfDetectionRiseTimeCriteria_Type())
interopDtmfDetectionRiseTimeCriteria.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDtmfDetectionRiseTimeCriteria.setStatus(_A)
class _InteropDtmfDetectionPositiveTwist_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_InteropDtmfDetectionPositiveTwist_Type.__name__=_E
_InteropDtmfDetectionPositiveTwist_Object=MibTableColumn
interopDtmfDetectionPositiveTwist=_InteropDtmfDetectionPositiveTwist_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,100,1,300),_InteropDtmfDetectionPositiveTwist_Type())
interopDtmfDetectionPositiveTwist.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDtmfDetectionPositiveTwist.setStatus(_A)
class _InteropDtmfDetectionNegativeTwist_Type(Unsigned32):defaultValue=9;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_InteropDtmfDetectionNegativeTwist_Type.__name__=_E
_InteropDtmfDetectionNegativeTwist_Object=MibTableColumn
interopDtmfDetectionNegativeTwist=_InteropDtmfDetectionNegativeTwist_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,100,1,350),_InteropDtmfDetectionNegativeTwist_Type())
interopDtmfDetectionNegativeTwist.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDtmfDetectionNegativeTwist.setStatus(_A)
class _InteropDtmfDetectionMaxPowerThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,1))
_InteropDtmfDetectionMaxPowerThreshold_Type.__name__=_C
_InteropDtmfDetectionMaxPowerThreshold_Object=MibTableColumn
interopDtmfDetectionMaxPowerThreshold=_InteropDtmfDetectionMaxPowerThreshold_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,100,1,400),_InteropDtmfDetectionMaxPowerThreshold_Type())
interopDtmfDetectionMaxPowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDtmfDetectionMaxPowerThreshold.setStatus(_A)
class _InteropDtmfDetectionMinPowerThreshold_Type(Integer32):defaultValue=-30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-45,-10))
_InteropDtmfDetectionMinPowerThreshold_Type.__name__=_C
_InteropDtmfDetectionMinPowerThreshold_Object=MibTableColumn
interopDtmfDetectionMinPowerThreshold=_InteropDtmfDetectionMinPowerThreshold_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,100,1,450),_InteropDtmfDetectionMinPowerThreshold_Type())
interopDtmfDetectionMinPowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDtmfDetectionMinPowerThreshold.setStatus(_A)
class _InteropDtmfDetectionBreakPowerThreshold_Type(Integer32):defaultValue=-32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-45,-12))
_InteropDtmfDetectionBreakPowerThreshold_Type.__name__=_C
_InteropDtmfDetectionBreakPowerThreshold_Object=MibTableColumn
interopDtmfDetectionBreakPowerThreshold=_InteropDtmfDetectionBreakPowerThreshold_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,100,1,500),_InteropDtmfDetectionBreakPowerThreshold_Type())
interopDtmfDetectionBreakPowerThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:interopDtmfDetectionBreakPowerThreshold.setStatus(_A)
_InteropStartCallInVbdTable_Object=MibTable
interopStartCallInVbdTable=_InteropStartCallInVbdTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,200))
if mibBuilder.loadTexts:interopStartCallInVbdTable.setStatus(_A)
_InteropStartCallInVbdEntry_Object=MibTableRow
interopStartCallInVbdEntry=_InteropStartCallInVbdEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,200,1))
interopStartCallInVbdEntry.setIndexNames((0,_G,_a))
if mibBuilder.loadTexts:interopStartCallInVbdEntry.setStatus(_A)
_InteropStartCallInVbdInterfaceId_Type=OctetString
_InteropStartCallInVbdInterfaceId_Object=MibTableColumn
interopStartCallInVbdInterfaceId=_InteropStartCallInVbdInterfaceId_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,200,1,100),_InteropStartCallInVbdInterfaceId_Type())
interopStartCallInVbdInterfaceId.setMaxAccess(_F)
if mibBuilder.loadTexts:interopStartCallInVbdInterfaceId.setStatus(_A)
class _InteropStartCallInVbdEnable_Type(MxEnableState):defaultValue=0
_InteropStartCallInVbdEnable_Type.__name__=_D
_InteropStartCallInVbdEnable_Object=MibTableColumn
interopStartCallInVbdEnable=_InteropStartCallInVbdEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,50000,200,1,200),_InteropStartCallInVbdEnable_Type())
interopStartCallInVbdEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:interopStartCallInVbdEnable.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1775,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'telIfMIB':telIfMIB,'telIfMIBObjects':telIfMIBObjects,'countrySelection':countrySelection,'countryCustomizationGroup':countryCustomizationGroup,'countryCustomizationUserGainGroup':countryCustomizationUserGainGroup,'defaultCountryCustomizationUserGainInputOffset':defaultCountryCustomizationUserGainInputOffset,'defaultCountryCustomizationUserGainOutputOffset':defaultCountryCustomizationUserGainOutputOffset,'specificCountryCustomizationUserGainTable':specificCountryCustomizationUserGainTable,'specificCountryCustomizationUserGainEntry':specificCountryCustomizationUserGainEntry,_I:specificCountryCustomizationUserGainInterfaceId,'specificCountryCustomizationUserGainEnableConfig':specificCountryCustomizationUserGainEnableConfig,'specificCountryCustomizationUserGainInputOffset':specificCountryCustomizationUserGainInputOffset,'specificCountryCustomizationUserGainOutputOffset':specificCountryCustomizationUserGainOutputOffset,'countryCustomizationDialingGroup':countryCustomizationDialingGroup,'defaultCountryCustomizationDialingOverride':defaultCountryCustomizationDialingOverride,'defaultCountryCustomizationDialingInterDtmfDialDelay':defaultCountryCustomizationDialingInterDtmfDialDelay,'defaultCountryCustomizationDialingDtmfDuration':defaultCountryCustomizationDialingDtmfDuration,'defaultCountryCustomizationDialingInterMfR1DialDelay':defaultCountryCustomizationDialingInterMfR1DialDelay,'defaultCountryCustomizationDialingMfR1Duration':defaultCountryCustomizationDialingMfR1Duration,'specificCountryCustomizationDialingTable':specificCountryCustomizationDialingTable,'specificCountryCustomizationDialingEntry':specificCountryCustomizationDialingEntry,_J:specificCountryCustomizationDialingInterfaceId,'specificCountryCustomizationDialingEnableConfig':specificCountryCustomizationDialingEnableConfig,'specificCountryCustomizationDialingOverride':specificCountryCustomizationDialingOverride,'specificCountryCustomizationDialingInterDtmfDialDelay':specificCountryCustomizationDialingInterDtmfDialDelay,'specificCountryCustomizationDialingDtmfDuration':specificCountryCustomizationDialingDtmfDuration,'specificCountryCustomizationDialingInterMfR1DialDelay':specificCountryCustomizationDialingInterMfR1DialDelay,'specificCountryCustomizationDialingMfR1Duration':specificCountryCustomizationDialingMfR1Duration,'countryCustomizationToneGroup':countryCustomizationToneGroup,'countryToneStatusTable':countryToneStatusTable,'countryToneStatusEntry':countryToneStatusEntry,_K:countryToneStatusTone,'countryToneStatusPattern':countryToneStatusPattern,'countryCustomizationToneTable':countryCustomizationToneTable,'countryCustomizationToneEntry':countryCustomizationToneEntry,_U:countryCustomizationToneTone,'countryCustomizationToneOverride':countryCustomizationToneOverride,'countryCustomizationTonePattern':countryCustomizationTonePattern,'machineDetectionGroup':machineDetectionGroup,'defaultMachineDetectionCngToneDetection':defaultMachineDetectionCngToneDetection,'defaultMachineDetectionCedToneDetection':defaultMachineDetectionCedToneDetection,'defaultMachineDetectionV21ModulationDetection':defaultMachineDetectionV21ModulationDetection,'defaultMachineDetectionBehaviorOnCedToneDetection':defaultMachineDetectionBehaviorOnCedToneDetection,'specificMachineDetectionTable':specificMachineDetectionTable,'specificMachineDetectionEntry':specificMachineDetectionEntry,_X:specificMachineDetectionInterfaceId,'specificMachineDetectionEnableConfig':specificMachineDetectionEnableConfig,'specificMachineDetectionCngToneDetection':specificMachineDetectionCngToneDetection,'specificMachineDetectionCedToneDetection':specificMachineDetectionCedToneDetection,'specificMachineDetectionV21ModulationDetection':specificMachineDetectionV21ModulationDetection,'specificMachineDetectionBehaviorOnCedToneDetection':specificMachineDetectionBehaviorOnCedToneDetection,'musicOnHoldStreamingGroup':musicOnHoldStreamingGroup,'musicOnHoldStreamingEnable':musicOnHoldStreamingEnable,'callWaitingToneGroup':callWaitingToneGroup,'distinctiveCallWaitingToneTable':distinctiveCallWaitingToneTable,'distinctiveCallWaitingToneEntry':distinctiveCallWaitingToneEntry,_Y:distinctiveCallWaitingToneIndex,'distinctiveCallWaitingToneToneId':distinctiveCallWaitingToneToneId,'distinctiveCallWaitingTonePattern':distinctiveCallWaitingTonePattern,'interopGroup':interopGroup,'interopDtmfDetectionTable':interopDtmfDetectionTable,'interopDtmfDetectionEntry':interopDtmfDetectionEntry,_Z:interopDtmfDetectionInterfaceId,'interopDtmfDetectionRiseTimeCriteria':interopDtmfDetectionRiseTimeCriteria,'interopDtmfDetectionPositiveTwist':interopDtmfDetectionPositiveTwist,'interopDtmfDetectionNegativeTwist':interopDtmfDetectionNegativeTwist,'interopDtmfDetectionMaxPowerThreshold':interopDtmfDetectionMaxPowerThreshold,'interopDtmfDetectionMinPowerThreshold':interopDtmfDetectionMinPowerThreshold,'interopDtmfDetectionBreakPowerThreshold':interopDtmfDetectionBreakPowerThreshold,'interopStartCallInVbdTable':interopStartCallInVbdTable,'interopStartCallInVbdEntry':interopStartCallInVbdEntry,_a:interopStartCallInVbdInterfaceId,'interopStartCallInVbdEnable':interopStartCallInVbdEnable,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})