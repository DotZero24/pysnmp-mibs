_M='seconds'
_L='agentNtpServerIndex'
_K='not-accessible'
_J='agentNtpAuthKeyIndex'
_I='InetAddress'
_H='DNOS-NTP-MIB'
_G='DisplayString'
_F='Integer32'
_E='TruthValue'
_D='read-create'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','RowStatus','TextualConvention',_E)
agentNtpMIB=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168))
if mibBuilder.loadTexts:agentNtpMIB.setRevisions(('2021-12-06 00:00',))
_AgentNtpObjects_ObjectIdentity=ObjectIdentity
agentNtpObjects=_AgentNtpObjects_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1))
_AgentNtpConfigGroup_ObjectIdentity=ObjectIdentity
agentNtpConfigGroup=_AgentNtpConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1))
class _AgentNtpAuthenticationMode_Type(TruthValue):defaultValue=2
_AgentNtpAuthenticationMode_Type.__name__=_E
_AgentNtpAuthenticationMode_Object=MibScalar
agentNtpAuthenticationMode=_AgentNtpAuthenticationMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,1),_AgentNtpAuthenticationMode_Type())
agentNtpAuthenticationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpAuthenticationMode.setStatus(_A)
class _AgentNtpBroadcastDelay_Type(Unsigned32):defaultValue=3000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999999))
_AgentNtpBroadcastDelay_Type.__name__=_C
_AgentNtpBroadcastDelay_Object=MibScalar
agentNtpBroadcastDelay=_AgentNtpBroadcastDelay_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,2),_AgentNtpBroadcastDelay_Type())
agentNtpBroadcastDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpBroadcastDelay.setStatus(_A)
class _AgentNtpBroadcastClientMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentNtpBroadcastClientMode_Type.__name__=_F
_AgentNtpBroadcastClientMode_Object=MibScalar
agentNtpBroadcastClientMode=_AgentNtpBroadcastClientMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,3),_AgentNtpBroadcastClientMode_Type())
agentNtpBroadcastClientMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpBroadcastClientMode.setStatus(_A)
_AgentNtpSourceInterface_Type=InterfaceIndexOrZero
_AgentNtpSourceInterface_Object=MibScalar
agentNtpSourceInterface=_AgentNtpSourceInterface_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,4),_AgentNtpSourceInterface_Type())
agentNtpSourceInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpSourceInterface.setStatus(_A)
class _AgentNtpServicePortSrcInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('servicePortEnable',1),('servicePortDisable',2)))
_AgentNtpServicePortSrcInterface_Type.__name__=_F
_AgentNtpServicePortSrcInterface_Object=MibScalar
agentNtpServicePortSrcInterface=_AgentNtpServicePortSrcInterface_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,5),_AgentNtpServicePortSrcInterface_Type())
agentNtpServicePortSrcInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpServicePortSrcInterface.setStatus(_A)
class _AgentNtpVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AgentNtpVrfName_Type.__name__=_G
_AgentNtpVrfName_Object=MibScalar
agentNtpVrfName=_AgentNtpVrfName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,6),_AgentNtpVrfName_Type())
agentNtpVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpVrfName.setStatus(_A)
_AgentNtpAuthKeyTable_Object=MibTable
agentNtpAuthKeyTable=_AgentNtpAuthKeyTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,7))
if mibBuilder.loadTexts:agentNtpAuthKeyTable.setStatus(_A)
_AgentNtpAuthKeyEntry_Object=MibTableRow
agentNtpAuthKeyEntry=_AgentNtpAuthKeyEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,7,1))
agentNtpAuthKeyEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:agentNtpAuthKeyEntry.setStatus(_A)
class _AgentNtpAuthKeyIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_AgentNtpAuthKeyIndex_Type.__name__=_C
_AgentNtpAuthKeyIndex_Object=MibTableColumn
agentNtpAuthKeyIndex=_AgentNtpAuthKeyIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,7,1,1),_AgentNtpAuthKeyIndex_Type())
agentNtpAuthKeyIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentNtpAuthKeyIndex.setStatus(_A)
class _AgentNtpAuthKeyNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentNtpAuthKeyNumber_Type.__name__=_C
_AgentNtpAuthKeyNumber_Object=MibTableColumn
agentNtpAuthKeyNumber=_AgentNtpAuthKeyNumber_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,7,1,2),_AgentNtpAuthKeyNumber_Type())
agentNtpAuthKeyNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNtpAuthKeyNumber.setStatus(_A)
class _AgentNtpAuthKeyMessageAuthAlg_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('md5',1),('sha1',2),('sha2',3)))
_AgentNtpAuthKeyMessageAuthAlg_Type.__name__=_F
_AgentNtpAuthKeyMessageAuthAlg_Object=MibTableColumn
agentNtpAuthKeyMessageAuthAlg=_AgentNtpAuthKeyMessageAuthAlg_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,7,1,3),_AgentNtpAuthKeyMessageAuthAlg_Type())
agentNtpAuthKeyMessageAuthAlg.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNtpAuthKeyMessageAuthAlg.setStatus(_A)
class _AgentNtpAuthKeyEncryptionStatus_Type(TruthValue):defaultValue=2
_AgentNtpAuthKeyEncryptionStatus_Type.__name__=_E
_AgentNtpAuthKeyEncryptionStatus_Object=MibTableColumn
agentNtpAuthKeyEncryptionStatus=_AgentNtpAuthKeyEncryptionStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,7,1,4),_AgentNtpAuthKeyEncryptionStatus_Type())
agentNtpAuthKeyEncryptionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNtpAuthKeyEncryptionStatus.setStatus(_A)
class _AgentNtpAuthKeyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_AgentNtpAuthKeyName_Type.__name__=_G
_AgentNtpAuthKeyName_Object=MibTableColumn
agentNtpAuthKeyName=_AgentNtpAuthKeyName_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,7,1,5),_AgentNtpAuthKeyName_Type())
agentNtpAuthKeyName.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNtpAuthKeyName.setStatus(_A)
class _AgentNtpAuthKeyTrustedStatus_Type(TruthValue):defaultValue=2
_AgentNtpAuthKeyTrustedStatus_Type.__name__=_E
_AgentNtpAuthKeyTrustedStatus_Object=MibTableColumn
agentNtpAuthKeyTrustedStatus=_AgentNtpAuthKeyTrustedStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,7,1,6),_AgentNtpAuthKeyTrustedStatus_Type())
agentNtpAuthKeyTrustedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpAuthKeyTrustedStatus.setStatus(_A)
_AgentNtpAuthKeyRowStatus_Type=RowStatus
_AgentNtpAuthKeyRowStatus_Object=MibTableColumn
agentNtpAuthKeyRowStatus=_AgentNtpAuthKeyRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,7,1,7),_AgentNtpAuthKeyRowStatus_Type())
agentNtpAuthKeyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNtpAuthKeyRowStatus.setStatus(_A)
_AgentNtpServerTable_Object=MibTable
agentNtpServerTable=_AgentNtpServerTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8))
if mibBuilder.loadTexts:agentNtpServerTable.setStatus(_A)
_AgentNtpServerEntry_Object=MibTableRow
agentNtpServerEntry=_AgentNtpServerEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1))
agentNtpServerEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:agentNtpServerEntry.setStatus(_A)
class _AgentNtpServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AgentNtpServerIndex_Type.__name__=_C
_AgentNtpServerIndex_Object=MibTableColumn
agentNtpServerIndex=_AgentNtpServerIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,1),_AgentNtpServerIndex_Type())
agentNtpServerIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:agentNtpServerIndex.setStatus(_A)
_AgentNtpServerAddressType_Type=InetAddressType
_AgentNtpServerAddressType_Object=MibTableColumn
agentNtpServerAddressType=_AgentNtpServerAddressType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,2),_AgentNtpServerAddressType_Type())
agentNtpServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNtpServerAddressType.setStatus(_A)
class _AgentNtpServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_AgentNtpServerAddress_Type.__name__=_I
_AgentNtpServerAddress_Object=MibTableColumn
agentNtpServerAddress=_AgentNtpServerAddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,3),_AgentNtpServerAddress_Type())
agentNtpServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNtpServerAddress.setStatus(_A)
class _AgentNtpServerVersion_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('version1',1),('version2',2),('version3',3),('version4',4)))
_AgentNtpServerVersion_Type.__name__=_F
_AgentNtpServerVersion_Object=MibTableColumn
agentNtpServerVersion=_AgentNtpServerVersion_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,4),_AgentNtpServerVersion_Type())
agentNtpServerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpServerVersion.setStatus(_A)
class _AgentNtpServerAuthKeyNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentNtpServerAuthKeyNumber_Type.__name__=_C
_AgentNtpServerAuthKeyNumber_Object=MibTableColumn
agentNtpServerAuthKeyNumber=_AgentNtpServerAuthKeyNumber_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,5),_AgentNtpServerAuthKeyNumber_Type())
agentNtpServerAuthKeyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpServerAuthKeyNumber.setStatus(_A)
class _AgentNtpServerMinPollInterval_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,10))
_AgentNtpServerMinPollInterval_Type.__name__=_C
_AgentNtpServerMinPollInterval_Object=MibTableColumn
agentNtpServerMinPollInterval=_AgentNtpServerMinPollInterval_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,6),_AgentNtpServerMinPollInterval_Type())
agentNtpServerMinPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpServerMinPollInterval.setStatus(_A)
if mibBuilder.loadTexts:agentNtpServerMinPollInterval.setUnits(_M)
class _AgentNtpServerMaxPollInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,10))
_AgentNtpServerMaxPollInterval_Type.__name__=_C
_AgentNtpServerMaxPollInterval_Object=MibTableColumn
agentNtpServerMaxPollInterval=_AgentNtpServerMaxPollInterval_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,7),_AgentNtpServerMaxPollInterval_Type())
agentNtpServerMaxPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpServerMaxPollInterval.setStatus(_A)
if mibBuilder.loadTexts:agentNtpServerMaxPollInterval.setUnits(_M)
class _AgentNtpServerPreferStatus_Type(TruthValue):defaultValue=2
_AgentNtpServerPreferStatus_Type.__name__=_E
_AgentNtpServerPreferStatus_Object=MibTableColumn
agentNtpServerPreferStatus=_AgentNtpServerPreferStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,8),_AgentNtpServerPreferStatus_Type())
agentNtpServerPreferStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpServerPreferStatus.setStatus(_A)
class _AgentNtpServerBurstStatus_Type(TruthValue):defaultValue=2
_AgentNtpServerBurstStatus_Type.__name__=_E
_AgentNtpServerBurstStatus_Object=MibTableColumn
agentNtpServerBurstStatus=_AgentNtpServerBurstStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,9),_AgentNtpServerBurstStatus_Type())
agentNtpServerBurstStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpServerBurstStatus.setStatus(_A)
class _AgentNtpServerIburstStatus_Type(TruthValue):defaultValue=2
_AgentNtpServerIburstStatus_Type.__name__=_E
_AgentNtpServerIburstStatus_Object=MibTableColumn
agentNtpServerIburstStatus=_AgentNtpServerIburstStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,10),_AgentNtpServerIburstStatus_Type())
agentNtpServerIburstStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentNtpServerIburstStatus.setStatus(_A)
_AgentNtpServerRowStatus_Type=RowStatus
_AgentNtpServerRowStatus_Object=MibTableColumn
agentNtpServerRowStatus=_AgentNtpServerRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,168,1,1,8,1,11),_AgentNtpServerRowStatus_Type())
agentNtpServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentNtpServerRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'agentNtpMIB':agentNtpMIB,'agentNtpObjects':agentNtpObjects,'agentNtpConfigGroup':agentNtpConfigGroup,'agentNtpAuthenticationMode':agentNtpAuthenticationMode,'agentNtpBroadcastDelay':agentNtpBroadcastDelay,'agentNtpBroadcastClientMode':agentNtpBroadcastClientMode,'agentNtpSourceInterface':agentNtpSourceInterface,'agentNtpServicePortSrcInterface':agentNtpServicePortSrcInterface,'agentNtpVrfName':agentNtpVrfName,'agentNtpAuthKeyTable':agentNtpAuthKeyTable,'agentNtpAuthKeyEntry':agentNtpAuthKeyEntry,_J:agentNtpAuthKeyIndex,'agentNtpAuthKeyNumber':agentNtpAuthKeyNumber,'agentNtpAuthKeyMessageAuthAlg':agentNtpAuthKeyMessageAuthAlg,'agentNtpAuthKeyEncryptionStatus':agentNtpAuthKeyEncryptionStatus,'agentNtpAuthKeyName':agentNtpAuthKeyName,'agentNtpAuthKeyTrustedStatus':agentNtpAuthKeyTrustedStatus,'agentNtpAuthKeyRowStatus':agentNtpAuthKeyRowStatus,'agentNtpServerTable':agentNtpServerTable,'agentNtpServerEntry':agentNtpServerEntry,_L:agentNtpServerIndex,'agentNtpServerAddressType':agentNtpServerAddressType,'agentNtpServerAddress':agentNtpServerAddress,'agentNtpServerVersion':agentNtpServerVersion,'agentNtpServerAuthKeyNumber':agentNtpServerAuthKeyNumber,'agentNtpServerMinPollInterval':agentNtpServerMinPollInterval,'agentNtpServerMaxPollInterval':agentNtpServerMaxPollInterval,'agentNtpServerPreferStatus':agentNtpServerPreferStatus,'agentNtpServerBurstStatus':agentNtpServerBurstStatus,'agentNtpServerIburstStatus':agentNtpServerIburstStatus,'agentNtpServerRowStatus':agentNtpServerRowStatus})